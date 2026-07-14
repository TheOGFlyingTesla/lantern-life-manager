#!/usr/bin/env python3
"""Build deterministic Lantern release archives."""

from pathlib import Path
import argparse
import hashlib
import zipfile


VERSION = "2.0.0"
FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
SKILL_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "assets/templates/DASHBOARD.md",
    "assets/templates/START_HERE.md",
    "assets/templates/STATUS.md",
    "assets/templates/INBOX.md",
    "references/architecture.md",
    "references/capability-setup.md",
    "references/model-routing.md",
    "references/onboarding.md",
    "references/safety-and-permissions.md",
)
STARTER_WORKSPACE_FILES = (
    "AGENTS.md",
    "DASHBOARD.md",
    "LANTERN_VERSION.md",
    "START_HERE.md",
    "Domains/AGENTS.md",
    "_Lantern/Templates/START_HERE.md",
    "_Lantern/Templates/STATUS.md",
    "_Lantern/Templates/INBOX.md",
    "Domains/Personal/START_HERE.md",
    "Domains/Personal/STATUS.md",
    "Domains/Personal/INBOX.md",
    "Domains/Home/START_HERE.md",
    "Domains/Home/STATUS.md",
    "Domains/Home/INBOX.md",
    "Domains/Career & Job Search/START_HERE.md",
    "Domains/Career & Job Search/STATUS.md",
    "Domains/Career & Job Search/INBOX.md",
    "Domains/Work, Internships & Volunteering/START_HERE.md",
    "Domains/Work, Internships & Volunteering/STATUS.md",
    "Domains/Work, Internships & Volunteering/INBOX.md",
    "Domains/School & Learning/START_HERE.md",
    "Domains/School & Learning/STATUS.md",
    "Domains/School & Learning/INBOX.md",
    "Domains/Finances/START_HERE.md",
    "Domains/Finances/STATUS.md",
    "Domains/Finances/INBOX.md",
    "Domains/Appointments & Admin/START_HERE.md",
    "Domains/Appointments & Admin/STATUS.md",
    "Domains/Appointments & Admin/INBOX.md",
    "Domains/Health & Wellbeing/START_HERE.md",
    "Domains/Health & Wellbeing/STATUS.md",
    "Domains/Health & Wellbeing/INBOX.md",
    "Domains/Relationships & Community/START_HERE.md",
    "Domains/Relationships & Community/STATUS.md",
    "Domains/Relationships & Community/INBOX.md",
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
    """Build the desktop workspace, optional Skill, and checksums."""
    root = root.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    desktop_zip = output_dir / f"lantern-desktop-v{version}.zip"
    skill_zip = output_dir / f"lantern-skill-v{version}.zip"
    checksums = output_dir / "SHA256SUMS"

    _write_zip(
        root / "starter-workspace" / "Lantern",
        "Lantern",
        desktop_zip,
        STARTER_WORKSPACE_FILES,
    )
    _write_zip(
        root / "lantern-life-manager",
        "lantern-life-manager",
        skill_zip,
        SKILL_FILES,
    )

    lines = [
        f"{_sha256(path)}  {path.name}"
        for path in sorted((desktop_zip, skill_zip), key=lambda item: item.name)
    ]
    checksums.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return desktop_zip, skill_zip, checksums


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
