#!/usr/bin/env python3
"""Build deterministic Lantern release archives."""

from pathlib import Path
import argparse
import hashlib
import zipfile


VERSION = "1.0.0"
FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
SKIPPED_PARTS = {".DS_Store", "__pycache__"}


def _iter_files(source: Path) -> list[Path]:
    return sorted(
        path
        for path in source.rglob("*")
        if path.is_file()
        and not any(part in SKIPPED_PARTS for part in path.parts)
        and path.suffix.lower() not in {".pyc", ".pyo"}
    )


def _write_zip(source: Path, prefix: str, output: Path) -> None:
    with zipfile.ZipFile(
        output,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        for path in _iter_files(source):
            relative = path.relative_to(source).as_posix()
            info = zipfile.ZipInfo(f"{prefix}/{relative}", FIXED_TIMESTAMP)
            info.create_system = 3
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compresslevel=9)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_release(
    root: Path,
    output_dir: Path,
    version: str = VERSION,
) -> tuple[Path, Path, Path]:
    """Build Skill ZIP, Project Kit ZIP, and checksum manifest."""
    root = root.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    skill_zip = output_dir / f"lantern-life-manager-v{version}.zip"
    project_zip = output_dir / f"lantern-project-kit-v{version}.zip"
    checksums = output_dir / "SHA256SUMS"

    _write_zip(root / "lantern-life-manager", "lantern-life-manager", skill_zip)
    _write_zip(root / "project-kit", "lantern-project-kit", project_zip)

    lines = [
        f"{_sha256(path)}  {path.name}"
        for path in sorted((skill_zip, project_zip), key=lambda item: item.name)
    ]
    checksums.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return skill_zip, project_zip, checksums


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Lantern release archives.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=Path("dist"))
    parser.add_argument("--version", default=VERSION)
    args = parser.parse_args()

    for path in build_release(args.root, args.output, args.version):
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
