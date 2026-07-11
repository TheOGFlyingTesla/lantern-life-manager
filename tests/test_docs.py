from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class DocumentationTests(unittest.TestCase):
    def test_readme_answers_first_time_user_questions(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8").casefold()

        for required in (
            "how lantern works",
            "install",
            "project",
            "privacy",
            "recover",
            "export",
            "unofficial",
        ):
            self.assertIn(required, text)

    def test_codex_assisted_setup_avoids_system_developer_tools(self):
        guide = (ROOT / "docs" / "CODEX_ASSISTED_SETUP.md").read_text(
            encoding="utf-8"
        ).casefold()

        for required in (
            "--method download",
            "bundled git",
            "bundled python",
            "apple developer tools",
            "xcode",
            "windows",
            "codex itself may require",
            "large download",
            "before installing",
            "project kit",
            "separate browser session",
            "open the actual page",
            "framework-ready checklist",
        ):
            self.assertIn(required, guide)

    def test_codex_setup_requires_no_github_install_or_account(self):
        guide = (ROOT / "docs" / "CODEX_ASSISTED_SETUP.md").read_text(
            encoding="utf-8"
        ).casefold()
        capability = (
            ROOT
            / "lantern-life-manager"
            / "references"
            / "capability-setup.md"
        ).read_text(encoding="utf-8").casefold()

        for text in (guide, capability):
            for required in (
                "do not install github desktop",
                "do not install the github cli",
                "do not ask the user to create a github account",
                "anonymous download",
                "no github account",
            ):
                self.assertIn(required, text)

        self.assertIn("releases/latest", guide)
        self.assertIn("browser download", guide)

    def test_codex_install_hands_off_directly_into_lantern(self):
        guide = (ROOT / "docs" / "CODEX_ASSISTED_SETUP.md").read_text(
            encoding="utf-8"
        ).casefold()
        onboarding = (
            ROOT
            / "lantern-life-manager"
            / "references"
            / "onboarding.md"
        ).read_text(encoding="utf-8").casefold()

        for required in (
            "invoke lantern automatically",
            "fresh task",
            "exact prompt",
            "do not claim setup is underway",
            "$lantern-life-manager",
        ):
            self.assertIn(required, guide)

        for required in (
            "before the first personal answer",
            "starter project map",
            "background setup task",
            "sequential fallback",
        ):
            self.assertIn(required, onboarding)

    def test_browser_project_setup_has_a_human_handoff(self):
        guide = (ROOT / "docs" / "CODEX_ASSISTED_SETUP.md").read_text(
            encoding="utf-8"
        ).casefold()

        for required in (
            "do you see the chatgpt login page in the browser",
            "if not, tell me and i’ll fix it",
            "please sign in there",
            "verify that sign-in succeeded",
            "may i take control of the cursor",
            "create and verify",
        ):
            self.assertIn(required, guide)

    def test_relative_markdown_links_exist(self):
        paths = [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]
        for path in paths:
            text = path.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
                if "://" in target or target.startswith("#"):
                    continue
                relative = target.split("#", 1)[0]
                if not relative:
                    continue
                resolved = (path.parent / relative).resolve()
                self.assertTrue(resolved.exists(), f"{path}: broken link {target}")

    def test_install_docs_explain_both_supported_paths(self):
        text = (ROOT / "docs" / "INSTALL.md").read_text(
            encoding="utf-8"
        ).casefold()

        self.assertIn("skills menu", text)
        self.assertIn("project kit", text)
        self.assertIn("one project per", text)
        for required in (
            "textedit",
            "extract all",
            "notepad",
            "project settings",
            "verify the project",
        ):
            self.assertIn(required, text)


if __name__ == "__main__":
    unittest.main()
