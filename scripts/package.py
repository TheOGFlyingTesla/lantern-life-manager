#!/usr/bin/env python3
"""Build deterministic Lantern release archives."""

from pathlib import Path
import argparse
import hashlib
import zipfile


VERSION = "1.0.0"
FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
SKILL_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "assets/templates/dashboard.md",
    "assets/templates/domain-snapshot.md",
    "assets/templates/onboarding-checkpoint.md",
    "assets/templates/work-request.md",
    "references/architecture.md",
    "references/capability-setup.md",
    "references/model-routing.md",
    "references/onboarding.md",
    "references/safety-and-permissions.md",
)
PROJECT_KIT_FILES = (
    "DOMAIN_COORDINATOR_INSTRUCTIONS.md",
    "LIFE_MANAGER_INSTRUCTIONS.md",
    "START_HERE.md",
    "templates/dashboard.md",
    "templates/domain-snapshot.md",
    "templates/onboarding-checkpoint.md",
    "templates/work-request.md",
)


def _listed_files(source: Path, allowed_files: tuple[str, ...]) -> list[Path]:
    files = [source / relative for relative in allowed_files]
    missing = [path for path in files if not path.is_file()]
    if missing:
        relative = ", ".join(str(path.relative_to(source)) for path in missing)
        raise FileNotFoundError(f"Missing reviewed release file(s): {relative}")
    linked = [path for path in files if path.is_symlink()]
    if linked:
        relative = ", ".join(str(path.relative_to(source)) for path in linked)
        raise ValueError(f"Release files must not be symlinks: {relative}")
    return files


def _write_zip(
    source: Path,
    prefix: str,
    output: Path,
    allowed_files: tuple[str, ...],
) -> None:
    with zipfile.ZipFile(
        output,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        for path in _listed_files(source, allowed_files):
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

    _write_zip(
        root / "lantern-life-manager",
        "lantern-life-manager",
        skill_zip,
        SKILL_FILES,
    )
    _write_zip(
        root / "project-kit",
        "lantern-project-kit",
        project_zip,
        PROJECT_KIT_FILES,
    )

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
