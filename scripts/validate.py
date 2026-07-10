#!/usr/bin/env python3
"""Validate the Lantern repository and runtime Skill."""

from pathlib import Path
import re
import sys


ALLOWED_RUNTIME_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".txt"}
REQUIRED_REPO_FILES = {
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
}


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    """Return simple string frontmatter and Markdown body from a Skill file."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", text, re.DOTALL)
    if not match:
        raise ValueError(f"{path}: missing YAML frontmatter")

    metadata: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key, separator, value = line.partition(":")
        if not separator:
            raise ValueError(f"{path}: invalid frontmatter line: {line}")
        metadata[key.strip()] = value.strip().strip('"')
    return metadata, match.group(2)


def validate_skill(skill_dir: Path) -> list[str]:
    """Return validation findings for one Agent Skills directory."""
    findings: list[str] = []
    skill_path = skill_dir / "SKILL.md"
    if not skill_path.is_file():
        return [f"{skill_path}: missing"]

    try:
        metadata, body = parse_frontmatter(skill_path)
    except ValueError as error:
        return [str(error)]

    if metadata.get("name") != skill_dir.name:
        findings.append(f"{skill_path}: name must equal {skill_dir.name}")
    if not metadata.get("description"):
        findings.append(f"{skill_path}: description is required")
    if set(metadata) != {"name", "description"}:
        findings.append(
            f"{skill_path}: frontmatter may contain only name and description"
        )
    if not body.strip():
        findings.append(f"{skill_path}: body is empty")

    for path in skill_dir.rglob("*"):
        if path.is_file() and path.suffix.lower() not in ALLOWED_RUNTIME_SUFFIXES:
            findings.append(f"{path}: executable runtime file is not allowed")
    return findings


def validate_repository(root: Path) -> list[str]:
    """Return structural findings for the release repository."""
    findings = [
        f"{root / name}: missing"
        for name in sorted(REQUIRED_REPO_FILES)
        if not (root / name).is_file()
    ]
    findings.extend(validate_skill(root / "lantern-life-manager"))
    return findings


def main(argv: list[str]) -> int:
    root = Path(argv[1] if len(argv) > 1 else ".").resolve()
    findings = validate_repository(root)
    if findings:
        print("\n".join(findings))
        return 1
    print("Lantern validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
