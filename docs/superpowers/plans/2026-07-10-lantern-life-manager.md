# Lantern Life Manager Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build, validate, package, document, privacy-scan, and publicly release Lantern as both an installable ChatGPT Skill and a nontechnical multi-Project setup kit.

**Architecture:** Lantern uses one Life Manager Project plus one Project per substantial domain. Domain coordinators publish versioned append-only snapshots to a ChatGPT-native Library Hub; the Life Manager reads those snapshots, queues work packets, handles small work directly, and optionally uses supported background Work. The repository keeps runtime instructions concise, human documentation outside the Skill package, and deterministic Python tooling for validation, privacy scanning, and release archives.

**Tech Stack:** Markdown, YAML metadata, Python 3 standard library, `unittest`, Git, GitHub CLI, deterministic ZIP archives.

## Global Constraints

- The public package contains no personal names, organization names, credentials, emails, usernames, phone numbers, addresses, or absolute local paths from development.
- The installable Skill archive contains Markdown, YAML metadata, and templates only; no executable runtime code.
- Every substantial life domain uses a separate ChatGPT Project from the beginning.
- ChatGPT Library is the primary version 1 exchange Hub; it is ChatGPT-account storage, not a device-local filesystem or transactional database.
- External storage providers are optional backup or automation bridges, not required sources of truth.
- Luna high is the default GPT-5.6 route; Luna extra high, selective Terra, and Sol medium/high are escalations described in dated guidance.
- Consequential external actions require exact-action approval immediately before execution.
- The repository is public under MIT and identifies Lantern as an unofficial community project not affiliated with OpenAI.
- End users must not need GitHub or software-development knowledge.
- All behavior and installation claims that depend on a live ChatGPT account must be smoke-tested where access permits or explicitly labeled unverified.

---

## File Structure

```text
README.md                              Human-first entry point
LICENSE                                MIT license with generic contributor holder
CHANGELOG.md                           Release history
SECURITY.md                            Private reporting and security scope
CONTRIBUTING.md                        Contribution and privacy rules
.gitignore                             Generated, OS, editor, and cache exclusions
docs/INSTALL.md                        Skill and Project Kit installation
docs/USING_LANTERN.md                  Everyday multi-Project workflow
docs/PRIVACY_AND_SAFETY.md             Data controls, approvals, and limits
docs/TROUBLESHOOTING.md                Recovery and capability fallbacks
docs/releases/1.0.0.md                 Public release and pull-request notes
lantern-life-manager/SKILL.md          Runtime router and core procedure
lantern-life-manager/agents/openai.yaml
                                        Interface metadata
lantern-life-manager/references/architecture.md
                                        Project/Hub/coordination contract
lantern-life-manager/references/onboarding.md
                                        Guided interview
lantern-life-manager/references/capability-setup.md
                                        Built-ins, apps, and Skills audit
lantern-life-manager/references/model-routing.md
                                        Dated GPT-5.6 routing
lantern-life-manager/references/safety-and-permissions.md
                                        Approval and safety rules
lantern-life-manager/assets/templates/domain-snapshot.md
                                        Versioned status template
lantern-life-manager/assets/templates/onboarding-checkpoint.md
                                        Resumable setup checkpoint
lantern-life-manager/assets/templates/work-request.md
                                        Cross-Project request template
lantern-life-manager/assets/templates/dashboard.md
                                        Life Manager dashboard template
project-kit/LIFE_MANAGER_INSTRUCTIONS.md
                                        Plus-compatible manager instructions
project-kit/DOMAIN_COORDINATOR_INSTRUCTIONS.md
                                        Plus-compatible domain instructions
project-kit/templates/                  Copies of runtime templates
scripts/validate.py                     Repository and Skill validation
scripts/privacy_scan.py                 Source/archive privacy scanner
scripts/package.py                      Deterministic release builder
tests/test_validate.py                  Validator tests
tests/test_privacy_scan.py              Privacy tests
tests/test_package.py                   Archive tests
tests/test_content_contract.py          Runtime behavior and parity tests
tests/test_docs.py                      Link and documentation tests
tests/scenarios/*.md                    Forward-test prompts
```

---

### Task 1: Repository contract and validator

**Files:**
- Create: `.gitignore`
- Create: `scripts/validate.py`
- Create: `tests/test_validate.py`

**Interfaces:**
- Produces: `parse_frontmatter(path: Path) -> tuple[dict[str, str], str]`
- Produces: `validate_skill(skill_dir: Path) -> list[str]`
- Produces: `validate_repository(root: Path) -> list[str]`
- CLI: `python3 scripts/validate.py [ROOT]`, exit `0` on success and `1` on findings.

- [ ] **Step 1: Write failing validator tests**

```python
from pathlib import Path
import tempfile
import unittest

from scripts.validate import parse_frontmatter, validate_skill


class ValidateSkillTests(unittest.TestCase):
    def test_parses_required_frontmatter(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "SKILL.md"
            path.write_text("---\nname: lantern-life-manager\ndescription: Helps manage life.\n---\n\n# Lantern\n", encoding="utf-8")
            metadata, body = parse_frontmatter(path)
            self.assertEqual(metadata["name"], "lantern-life-manager")
            self.assertIn("# Lantern", body)

    def test_rejects_executable_runtime_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "lantern-life-manager"
            skill.mkdir()
            (skill / "SKILL.md").write_text("---\nname: lantern-life-manager\ndescription: Helps manage life.\n---\n# Lantern\n", encoding="utf-8")
            (skill / "run.py").write_text("print('no')\n", encoding="utf-8")
            findings = validate_skill(skill)
            self.assertTrue(any("executable runtime file" in item for item in findings))
```

- [ ] **Step 2: Verify the tests fail for the missing module**

Run: `python3 -m unittest tests.test_validate -v`

Expected: import failure for `scripts.validate`.

- [ ] **Step 3: Implement the minimal validator**

```python
from pathlib import Path
import re
import sys

ALLOWED_RUNTIME_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".txt"}
REQUIRED_REPO_FILES = {"README.md", "LICENSE", "CHANGELOG.md", "SECURITY.md", "CONTRIBUTING.md"}


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
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
        findings.append(f"{skill_path}: frontmatter may contain only name and description")
    if not body.strip():
        findings.append(f"{skill_path}: body is empty")
    for path in skill_dir.rglob("*"):
        if path.is_file() and path.suffix.lower() not in ALLOWED_RUNTIME_SUFFIXES:
            findings.append(f"{path}: executable runtime file is not allowed")
    return findings


def validate_repository(root: Path) -> list[str]:
    findings = [f"{root / name}: missing" for name in sorted(REQUIRED_REPO_FILES) if not (root / name).is_file()]
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
```

- [ ] **Step 4: Run the validator tests**

Run: `python3 -m unittest tests.test_validate -v`

Expected: `OK` with 2 tests.

- [ ] **Step 5: Commit the validator contract**

```bash
git add .gitignore scripts/validate.py tests/test_validate.py
git commit -m "Add Lantern repository validator"
```

---

### Task 2: Privacy scanner

**Files:**
- Create: `scripts/privacy_scan.py`
- Create: `tests/test_privacy_scan.py`

**Interfaces:**
- Produces: `scan_text(text: str, label: str, forbidden_terms: tuple[str, ...] = ()) -> list[str]`
- Produces: `scan_path(path: Path, forbidden_terms: tuple[str, ...] = ()) -> list[str]`
- CLI: `python3 scripts/privacy_scan.py PATH [--forbid TERM ...] [--forbid-file PATH] [--release]`, exit `0` when clean. Release mode requires an untracked private-terms file.

- [ ] **Step 1: Write failing privacy tests**

```python
import unittest

from scripts.privacy_scan import scan_text


class PrivacyScanTests(unittest.TestCase):
    def test_detects_email_and_absolute_path(self):
        sample = "email person" + "@example.com path /Us" + "ers/example/private.txt"
        findings = scan_text(sample, "sample")
        self.assertTrue(any("email address" in item for item in findings))
        self.assertTrue(any("absolute local path" in item for item in findings))

    def test_detects_caller_supplied_private_term_case_insensitively(self):
        findings = scan_text("Private Example appears here", "sample", ("private example",))
        self.assertTrue(any("forbidden private term" in item for item in findings))

    def test_allows_documentation_words_without_values(self):
        findings = scan_text("Never include passwords, tokens, email addresses, or local paths.", "sample")
        self.assertEqual(findings, [])
```

- [ ] **Step 2: Verify the tests fail for the missing scanner**

Run: `python3 -m unittest tests.test_privacy_scan -v`

Expected: import failure for `scripts.privacy_scan`.

- [ ] **Step 3: Implement text, directory, and ZIP scanning**

```python
from pathlib import Path
import argparse
import re
import zipfile

PATTERNS = (
    ("email address", re.compile(r"(?<![\w.-])[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}(?![\w.-])", re.I)),
    ("absolute local path", re.compile(r"(?:/" + r"Users/|/" + r"Volumes/|[A-Z]:\\\\" + r"Users\\\\)")),
    ("credential-shaped value", re.compile(r"(?:sk-[A-Za-z0-9_-]{20,}|gh[oprsu]_[A-Za-z0-9]{20,})")),
    ("phone number", re.compile(r"(?<!\d)(?:\+?1[-. ]?)?\(?\d{3}\)?[-. ]\d{3}[-. ]\d{4}(?!\d)")),
)

TEXT_SUFFIXES = {".md", ".txt", ".yaml", ".yml", ".json", ".py", ".toml"}


def scan_text(text: str, label: str, forbidden_terms: tuple[str, ...] = ()) -> list[str]:
    findings: list[str] = []
    for description, pattern in PATTERNS:
        if pattern.search(text):
            findings.append(f"{label}: {description}")
    lowered = text.casefold()
    for term in forbidden_terms:
        if term.casefold() in lowered:
            findings.append(f"{label}: forbidden private term")
    return findings


def scan_path(path: Path, forbidden_terms: tuple[str, ...] = ()) -> list[str]:
    if path.suffix.lower() == ".zip":
        findings: list[str] = []
        with zipfile.ZipFile(path) as archive:
            for info in archive.infolist():
                if Path(info.filename).suffix.lower() in TEXT_SUFFIXES:
                    findings.extend(scan_text(archive.read(info).decode("utf-8"), f"{path}:{info.filename}", forbidden_terms))
        return findings
    files = [path] if path.is_file() else [item for item in path.rglob("*") if item.is_file()]
    findings = []
    for item in files:
        if item.suffix.lower() in TEXT_SUFFIXES and ".git" not in item.parts:
            findings.extend(scan_text(item.read_text(encoding="utf-8"), str(item), forbidden_terms))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--forbid", action="append", default=[])
    args = parser.parse_args()
    findings = scan_path(args.path, tuple(args.forbid))
    if findings:
        print("\n".join(findings))
        return 1
    print("Lantern privacy scan passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run privacy tests**

Run: `python3 -m unittest tests.test_privacy_scan -v`

Expected: `OK` with 3 tests.

- [ ] **Step 5: Commit the privacy scanner**

```bash
git add scripts/privacy_scan.py tests/test_privacy_scan.py
git commit -m "Add Lantern privacy scanner"
```

---

### Task 3: Runtime Skill, references, and templates

**Files:**
- Create using `init_skill.py`: `lantern-life-manager/SKILL.md`
- Create: `lantern-life-manager/agents/openai.yaml`
- Create: `lantern-life-manager/references/architecture.md`
- Create: `lantern-life-manager/references/onboarding.md`
- Create: `lantern-life-manager/references/capability-setup.md`
- Create: `lantern-life-manager/references/model-routing.md`
- Create: `lantern-life-manager/references/safety-and-permissions.md`
- Create: `lantern-life-manager/assets/templates/domain-snapshot.md`
- Create: `lantern-life-manager/assets/templates/onboarding-checkpoint.md`
- Create: `lantern-life-manager/assets/templates/work-request.md`
- Create: `lantern-life-manager/assets/templates/dashboard.md`
- Create: `tests/test_content_contract.py`

**Interfaces:**
- `SKILL.md` routes setup, daily coordination, domain work, recovery, capability audit, and model selection to a one-level reference.
- Templates implement `lantern-domain/v1`, `lantern-onboarding/v1`, `lantern-request/v1`, and `lantern-dashboard/v1`.

- [ ] **Step 1: Write failing content-contract tests**

```python
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ContentContractTests(unittest.TestCase):
    def test_skill_routes_every_core_workflow(self):
        text = (ROOT / "lantern-life-manager" / "SKILL.md").read_text(encoding="utf-8")
        for required in ("guided onboarding", "domain snapshot", "work request", "recover", "capability", "model"):
            self.assertIn(required, text.casefold())

    def test_domain_snapshot_is_versioned_and_freshness_aware(self):
        text = (ROOT / "lantern-life-manager" / "assets" / "templates" / "domain-snapshot.md").read_text(encoding="utf-8")
        for required in ("lantern-domain/v1", "Last verified", "Review after", "Supersedes"):
            self.assertIn(required, text)

    def test_runtime_archive_has_no_executable_files(self):
        skill = ROOT / "lantern-life-manager"
        forbidden = [path for path in skill.rglob("*") if path.is_file() and path.suffix.lower() not in {".md", ".yaml", ".yml", ".json", ".txt"}]
        self.assertEqual(forbidden, [])
```

- [ ] **Step 2: Verify tests fail because runtime files are absent**

Run: `python3 -m unittest tests.test_content_contract -v`

Expected: file-not-found failures.

- [ ] **Step 3: Initialize the Skill with the official scaffold**

Run:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/init_skill.py" lantern-life-manager --path . --resources references,assets --interface display_name="Lantern" --interface short_description="A personal life manager for ChatGPT Work" --interface default_prompt="Use $lantern-life-manager to help me set up or coordinate my life."
```

Expected: `lantern-life-manager/SKILL.md` and `lantern-life-manager/agents/openai.yaml` created.

- [ ] **Step 4: Replace scaffold content with the approved runtime contract**

Write `SKILL.md` with only `name` and `description` in frontmatter; keep the body imperative, concise, and under 500 lines. Route to each reference with an explicit “read when” instruction. Require one question at a time during onboarding, all-multi-project setup, append-only Library snapshots, exact-action approval, visible fallbacks, and recovery.

Write the five references with no duplicated source-of-truth rules. Put the complete interview in `onboarding.md`, coordination mechanics in `architecture.md`, capability recommendations in `capability-setup.md`, dated GPT-5.6 guidance in `model-routing.md`, and guardrails in `safety-and-permissions.md`.

Write the domain, work-request, and dashboard templates with exact schemas from the approved design specification. Add a compact `lantern-onboarding/v1` checkpoint template so the approved resumable interview has a durable contract.

- [ ] **Step 5: Run the content and validator tests**

Run: `python3 -m unittest tests.test_content_contract tests.test_validate -v`

Expected: all tests pass.

- [ ] **Step 6: Run the official Skill validator**

Run: `python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" lantern-life-manager`

Expected: valid Skill result with exit code `0`.

- [ ] **Step 7: Commit the runtime Skill**

```bash
git add lantern-life-manager tests/test_content_contract.py
git commit -m "Build Lantern runtime skill"
```

---

### Task 4: Plus-compatible Project Kit and parity

**Files:**
- Create: `project-kit/LIFE_MANAGER_INSTRUCTIONS.md`
- Create: `project-kit/DOMAIN_COORDINATOR_INSTRUCTIONS.md`
- Create: `project-kit/templates/domain-snapshot.md`
- Create: `project-kit/templates/onboarding-checkpoint.md`
- Create: `project-kit/templates/work-request.md`
- Create: `project-kit/templates/dashboard.md`
- Modify: `tests/test_content_contract.py`

**Interfaces:**
- Project Kit instructions reproduce the runtime Skill's manager and domain behavior without requiring Skills.
- Project Kit templates are byte-identical to runtime templates.

- [ ] **Step 1: Add failing parity tests**

```python
    def test_project_kit_templates_match_runtime_templates(self):
        for name in ("domain-snapshot.md", "onboarding-checkpoint.md", "work-request.md", "dashboard.md"):
            runtime = (ROOT / "lantern-life-manager" / "assets" / "templates" / name).read_bytes()
            project = (ROOT / "project-kit" / "templates" / name).read_bytes()
            self.assertEqual(project, runtime)

    def test_project_kit_preserves_manager_and_domain_boundaries(self):
        manager = (ROOT / "project-kit" / "LIFE_MANAGER_INSTRUCTIONS.md").read_text(encoding="utf-8").casefold()
        domain = (ROOT / "project-kit" / "DOMAIN_COORDINATOR_INSTRUCTIONS.md").read_text(encoding="utf-8").casefold()
        self.assertIn("life manager", manager)
        self.assertIn("separate project", manager)
        self.assertIn("domain coordinator", domain)
        self.assertIn("publish", domain)
```

- [ ] **Step 2: Verify parity tests fail for missing files**

Run: `python3 -m unittest tests.test_content_contract -v`

Expected: Project Kit file-not-found failures.

- [ ] **Step 3: Write the Project Kit instructions and copy templates**

Use human-readable instructions that ChatGPT can paste into each Project. Keep the manager responsible for cross-domain prioritization and the domain coordinator responsible for domain truth. Copy the four runtime templates byte-for-byte.

- [ ] **Step 4: Run parity tests**

Run: `python3 -m unittest tests.test_content_contract -v`

Expected: all content-contract tests pass.

- [ ] **Step 5: Commit the Project Kit**

```bash
git add project-kit tests/test_content_contract.py
git commit -m "Add Lantern Project Kit"
```

---

### Task 5: Deterministic release packaging

**Files:**
- Create: `scripts/package.py`
- Create: `tests/test_package.py`
- Modify: `.gitignore`

**Interfaces:**
- Produces: `build_release(root: Path, output_dir: Path) -> tuple[Path, Path, Path]`
- Output: `lantern-life-manager-v1.0.0.zip`, `lantern-project-kit-v1.0.0.zip`, `SHA256SUMS`.

- [ ] **Step 1: Write failing package tests**

```python
from pathlib import Path
import tempfile
import unittest
import zipfile

from scripts.package import build_release

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_builds_clean_skill_and_project_archives(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_zip, project_zip, sums = build_release(ROOT, Path(tmp))
            self.assertTrue(sums.is_file())
            with zipfile.ZipFile(skill_zip) as archive:
                names = archive.namelist()
                self.assertIn("lantern-life-manager/SKILL.md", names)
                self.assertFalse(any(name.endswith(".py") for name in names))
                self.assertFalse(any(".DS_Store" in name or "__pycache__" in name for name in names))
            with zipfile.ZipFile(project_zip) as archive:
                self.assertIn("lantern-project-kit/LIFE_MANAGER_INSTRUCTIONS.md", archive.namelist())

    def test_repeated_builds_are_byte_identical(self):
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            first_paths = build_release(ROOT, Path(first))[:2]
            second_paths = build_release(ROOT, Path(second))[:2]
            self.assertEqual([path.read_bytes() for path in first_paths], [path.read_bytes() for path in second_paths])
```

- [ ] **Step 2: Verify package tests fail for the missing module**

Run: `python3 -m unittest tests.test_package -v`

Expected: import failure for `scripts.package`.

- [ ] **Step 3: Implement deterministic archives**

Use `zipfile.ZipInfo` with timestamp `(1980, 1, 1, 0, 0, 0)`, sorted relative paths, normalized `/` separators, permissions `0o644`, and `ZIP_DEFLATED`. Prefix Skill entries with `lantern-life-manager/` and Project Kit entries with `lantern-project-kit/`. Compute lowercase SHA-256 hashes and write two lines to `SHA256SUMS`.

- [ ] **Step 4: Run package tests**

Run: `python3 -m unittest tests.test_package -v`

Expected: `OK` with 2 tests.

- [ ] **Step 5: Commit packaging**

```bash
git add .gitignore scripts/package.py tests/test_package.py
git commit -m "Add deterministic Lantern packaging"
```

---

### Task 6: Human documentation and license

**Files:**
- Create: `README.md`
- Create: `LICENSE`
- Create: `CHANGELOG.md`
- Create: `SECURITY.md`
- Create: `CONTRIBUTING.md`
- Create: `docs/INSTALL.md`
- Create: `docs/USING_LANTERN.md`
- Create: `docs/PRIVACY_AND_SAFETY.md`
- Create: `docs/TROUBLESHOOTING.md`
- Create: `docs/releases/1.0.0.md`
- Create: `tests/test_docs.py`

**Interfaces:**
- README is the single entry point and routes nontechnical users to Skill or Project Kit installation.
- Documentation links only to existing relative files and current official OpenAI pages.

- [ ] **Step 1: Write failing documentation tests**

```python
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class DocumentationTests(unittest.TestCase):
    def test_readme_answers_first_time_user_questions(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8").casefold()
        for required in ("what is lantern", "install", "project", "privacy", "recover", "unofficial"):
            self.assertIn(required, text)

    def test_relative_markdown_links_exist(self):
        for path in [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]:
            text = path.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
                if "://" not in target and not target.startswith("#"):
                    resolved = (path.parent / target.split("#", 1)[0]).resolve()
                    self.assertTrue(resolved.exists(), f"{path}: broken link {target}")
```

- [ ] **Step 2: Verify documentation tests fail for missing files**

Run: `python3 -m unittest tests.test_docs -v`

Expected: file-not-found failures.

- [ ] **Step 3: Write the human documentation**

Write in warm, direct language. Put “Start here” near the top of README. Explain that Project Kit is likely the current path for personal Plus accounts when Skills is absent. Explain Library as ChatGPT-account storage, the separate-Project architecture, app recommendations, Luna-first routing, exact-action approvals, update/export/recovery/uninstall, and honest limitations. Use the official Skills, Projects, Library, Scheduled Tasks, Data Controls, Apps, and GPT-5.6 URLs.

Use MIT text with `Copyright (c) 2026 Lantern Life Manager contributors`.

Write `docs/releases/1.0.0.md` with the release summary, installation assets, validation commands, privacy posture, and the remaining requirement to verify account-dependent Library behavior in the user's own ChatGPT interface.

- [ ] **Step 4: Run documentation and repository validation**

Run: `python3 -m unittest tests.test_docs -v && python3 scripts/validate.py .`

Expected: documentation tests and repository validation pass.

- [ ] **Step 5: Commit documentation**

```bash
git add README.md LICENSE CHANGELOG.md SECURITY.md CONTRIBUTING.md docs/INSTALL.md docs/USING_LANTERN.md docs/PRIVACY_AND_SAFETY.md docs/TROUBLESHOOTING.md docs/releases/1.0.0.md tests/test_docs.py
git commit -m "Document Lantern for nontechnical users"
```

---

### Task 7: Scenario evaluations and final verification

**Files:**
- Create: `tests/scenarios/01-student-intern-job-search.md`
- Create: `tests/scenarios/02-caregiver-work-home.md`
- Create: `tests/scenarios/03-interrupted-onboarding.md`
- Create: `tests/scenarios/04-cross-project-conflict.md`
- Create: `tests/scenarios/05-consequential-action.md`
- Create: `tests/scenarios/06-confidential-resume.md`
- Create: `tests/scenarios/07-prompt-injection.md`
- Create: `tests/scenarios/08-academic-integrity.md`
- Create: `tests/scenarios/09-recovery-and-migration.md`
- Create: `tests/scenarios/10-capability-and-model-routing.md`

**Interfaces:**
- Each scenario contains an ordinary user prompt, supplied artifacts, and observable acceptance criteria without prescribing exact prose.

- [ ] **Step 1: Write ten scenario files**

Each file must include `User situation`, `User request`, and `Acceptance criteria`. Criteria must test decisions and outputs, including one-question onboarding, separate Projects, snapshot freshness, exact-action approval, untrusted-content handling, truthful résumé work, academic integrity, migration, tailored app recommendations, and Luna-first escalation.

- [ ] **Step 2: Run fresh isolated forward tests**

Dispatch read-only reviewer agents with only the built Skill path and one scenario each. Ask them to use the Skill to respond to the user situation. Do not provide the intended answer or prior review findings. Save no reviewer artifacts inside the repository.

- [ ] **Step 3: Review outputs against scenario criteria and fix transferable failures**

Change runtime instructions only when a failure reflects a reusable behavior gap. Re-run the affected scenario in a fresh context after each fix.

- [ ] **Step 4: Run the complete verification suite**

Run:

```bash
python3 -m unittest discover -s tests -v
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" lantern-life-manager
python3 scripts/validate.py .
python3 scripts/privacy_scan.py . --release --forbid-file "$LANTERN_PRIVATE_TERMS_FILE"
python3 scripts/package.py
python3 scripts/privacy_scan.py dist/lantern-life-manager-v1.0.0.zip --release --forbid-file "$LANTERN_PRIVATE_TERMS_FILE"
python3 scripts/privacy_scan.py dist/lantern-project-kit-v1.0.0.zip --release --forbid-file "$LANTERN_PRIVATE_TERMS_FILE"
(cd dist && shasum -a 256 -c SHA256SUMS)
git diff --check
```

Expected: all commands exit `0`; all tests pass; both archives are built and privacy-clean.

- [ ] **Step 5: Inspect archive inventories**

Run: `unzip -l dist/lantern-life-manager-v1.0.0.zip && unzip -l dist/lantern-project-kit-v1.0.0.zip`

Expected: only reviewed runtime files under one top-level directory in each archive; no hidden, executable, cache, local-path, or repository files.

- [ ] **Step 6: Commit validated release source**

```bash
git add lantern-life-manager project-kit tests README.md docs scripts
git commit -m "Validate Lantern 1.0 release"
```

---

### Task 8: Public GitHub repository and release

**Files:**
- No source-file changes unless the final remote URL must be added to README.
- Generated locally: `dist/lantern-life-manager-v1.0.0.zip`
- Generated locally: `dist/lantern-project-kit-v1.0.0.zip`
- Generated locally: `dist/SHA256SUMS`

**Interfaces:**
- Public repository: `lantern-life-manager`.
- Release tag: `v1.0.0`.
- Release assets: both ZIP files and `SHA256SUMS`.

- [ ] **Step 1: Verify Git identity and source privacy**

Run:

```bash
git config user.email
git log --format='%ae' | sort -u
git status -sb
```

Expected: only a GitHub no-reply email and a clean task branch.

- [ ] **Step 2: Create the public repository without initializing remote files**

Run: `gh repo create lantern-life-manager --public --description "Lantern — A personal life manager for ChatGPT Work" --source . --remote origin && git push -u origin main`

Expected: public repository created and `origin` configured.

- [ ] **Step 3: Push the task branch and create a pull request**

Run:

```bash
git push -u origin agent/lantern-initial-release
gh pr create --base main --head agent/lantern-initial-release --title "Release Lantern 1.0" --body-file docs/releases/1.0.0.md
```

The pull-request body states what changed, why, user impact, validation commands, privacy scan, and remaining live-product smoke-test limits.

- [ ] **Step 4: Merge the reviewed branch and tag the release**

Run:

```bash
gh pr merge --squash --delete-branch
git fetch origin main
git switch main
git pull --ff-only origin main
git tag -a v1.0.0 -m "Lantern 1.0.0"
git push origin v1.0.0
```

Expected: `main` contains the release and tag `v1.0.0` exists remotely.

- [ ] **Step 5: Publish the GitHub release assets**

Run:

```bash
gh release create v1.0.0 dist/lantern-life-manager-v1.0.0.zip dist/lantern-project-kit-v1.0.0.zip dist/SHA256SUMS --title "Lantern 1.0.0" --notes-file docs/releases/1.0.0.md
```

Expected: public release page with three downloadable assets.

- [ ] **Step 6: Verify the public release**

Run:

```bash
gh repo view --json nameWithOwner,visibility,url,defaultBranchRef
gh release view v1.0.0 --json url,assets,tagName
```

Expected: repository visibility `PUBLIC`, default branch `main`, tag `v1.0.0`, and exactly three release assets.
