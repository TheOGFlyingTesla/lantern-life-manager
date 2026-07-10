from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class DocumentationTests(unittest.TestCase):
    def test_readme_answers_first_time_user_questions(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8").casefold()

        for required in (
            "what is lantern",
            "install",
            "project",
            "privacy",
            "recover",
            "export",
            "unofficial",
        ):
            self.assertIn(required, text)

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


if __name__ == "__main__":
    unittest.main()
