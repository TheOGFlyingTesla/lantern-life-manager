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

    def test_install_requires_no_developer_tools_or_account(self):
        guide = (ROOT / "docs" / "INSTALL.md").read_text(encoding="utf-8").casefold()
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
                "no github account",
                "no git",
                "no python",
            ):
                self.assertIn(required, text)

        self.assertIn("releases/latest", guide)

    def test_install_is_one_folder_one_project_one_prompt(self):
        guide = (ROOT / "docs" / "INSTALL.md").read_text(encoding="utf-8").casefold()
        onboarding = (
            ROOT
            / "lantern-life-manager"
            / "references"
            / "onboarding.md"
        ).read_text(encoding="utf-8").casefold()

        for required in (
            "one folder",
            "one local project",
            "start lantern",
            "do not install a skill",
            "extract all",
            "keep the entire lantern folder together",
        ):
            self.assertIn(required, guide)

        for required in (
            "first genuine",
            "starter domain",
            "do not start a task in every domain",
            "on demand",
        ):
            self.assertIn(required, onboarding)

    def test_active_user_docs_are_local_first(self):
        for relative in (
            "README.md",
            "docs/INSTALL.md",
            "docs/USING_LANTERN.md",
            "docs/TROUBLESHOOTING.md",
        ):
            text = (ROOT / relative).read_text(encoding="utf-8").casefold()
            self.assertIn("local", text, relative)
            self.assertNotIn("primary handoff", text, relative)

        readme = (ROOT / "README.md").read_text(encoding="utf-8").casefold()
        self.assertIn("desktop", readme)
        self.assertIn("not supported on the web", readme)

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

    def test_install_docs_are_nontechnical_and_desktop_only(self):
        text = (ROOT / "docs" / "INSTALL.md").read_text(
            encoding="utf-8"
        ).casefold()

        self.assertIn("chatgpt desktop app", text)
        self.assertIn("lantern-desktop-v2.0.0.zip", text)
        self.assertIn("not supported on the web", text)
        for required in (
            "extract all",
            "double-click",
            "local project",
            "start lantern",
        ):
            self.assertIn(required, text)


if __name__ == "__main__":
    unittest.main()
