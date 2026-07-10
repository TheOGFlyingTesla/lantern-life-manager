#!/usr/bin/env python3
"""Scan Lantern source and release archives without echoing sensitive values."""

from pathlib import Path
import argparse
import re
import zipfile


PATTERNS = (
    (
        "email address",
        re.compile(
            r"(?<![\w.-])[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}(?![\w.-])",
            re.IGNORECASE,
        ),
    ),
    (
        "absolute local path",
        re.compile(
            r"(?:/" + r"Users/|/" + r"Volumes/|[A-Z]:\\" + r"Users\\)"
        ),
    ),
    (
        "credential-shaped value",
        re.compile(r"(?:sk-[A-Za-z0-9_-]{20,}|gh[oprsu]_[A-Za-z0-9]{20,})"),
    ),
    (
        "phone number",
        re.compile(
            r"(?<!\d)(?:\+?1[-. ]?)?\(?\d{3}\)?[-. ]\d{3}[-. ]\d{4}(?!\d)"
        ),
    ),
)

TEXT_SUFFIXES = {".md", ".txt", ".yaml", ".yml", ".json", ".py", ".toml"}
SKIPPED_PARTS = {".git", ".worktrees", "__pycache__", "dist"}


def scan_text(
    text: str,
    label: str,
    forbidden_terms: tuple[str, ...] = (),
) -> list[str]:
    """Return redacted finding descriptions for text."""
    findings: list[str] = []
    for description, pattern in PATTERNS:
        if pattern.search(text):
            findings.append(f"{label}: {description}")

    lowered = text.casefold()
    for term in forbidden_terms:
        if term and term.casefold() in lowered:
            findings.append(f"{label}: forbidden private term")
    return findings


def load_forbidden_terms(path: Path) -> tuple[str, ...]:
    """Load private names and organizations from an untracked local file."""
    terms = tuple(
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    )
    if not terms:
        raise ValueError("Private terms file must contain at least one term.")
    return terms


def _scan_zip(path: Path, forbidden_terms: tuple[str, ...]) -> list[str]:
    findings: list[str] = []
    with zipfile.ZipFile(path) as archive:
        for info in archive.infolist():
            member = Path(info.filename)
            if member.suffix.lower() not in TEXT_SUFFIXES:
                continue
            text = archive.read(info).decode("utf-8")
            findings.extend(
                scan_text(text, f"{path.name}:{info.filename}", forbidden_terms)
            )
    return findings


def scan_path(
    path: Path,
    forbidden_terms: tuple[str, ...] = (),
) -> list[str]:
    """Scan one text file, ZIP archive, or directory tree."""
    if path.suffix.lower() == ".zip":
        return _scan_zip(path, forbidden_terms)

    files = [path] if path.is_file() else sorted(
        item
        for item in path.rglob("*")
        if item.is_file() and not any(part in SKIPPED_PARTS for part in item.parts)
    )
    findings: list[str] = []
    for item in files:
        if item.suffix.lower() not in TEXT_SUFFIXES:
            continue
        findings.extend(
            scan_text(item.read_text(encoding="utf-8"), str(item), forbidden_terms)
        )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan Lantern files without printing matched values."
    )
    parser.add_argument("path", type=Path)
    parser.add_argument("--forbid", action="append", default=[])
    parser.add_argument(
        "--forbid-file",
        type=Path,
        help="Untracked newline-delimited private names and organizations.",
    )
    parser.add_argument(
        "--release",
        action="store_true",
        help="Require a private-terms file for a public release scan.",
    )
    args = parser.parse_args()

    if args.release and args.forbid_file is None:
        parser.error("--release requires --forbid-file")
    try:
        file_terms = (
            load_forbidden_terms(args.forbid_file)
            if args.forbid_file is not None
            else ()
        )
    except (OSError, ValueError) as error:
        parser.error(str(error))

    findings = scan_path(args.path, tuple(args.forbid) + file_terms)
    if findings:
        print("\n".join(findings))
        return 1
    print("Lantern privacy scan passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
