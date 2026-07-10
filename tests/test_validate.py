from pathlib import Path
import tempfile
import unittest

from scripts.validate import parse_frontmatter, validate_skill


class ValidateSkillTests(unittest.TestCase):
    def test_parses_required_frontmatter(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "SKILL.md"
            path.write_text(
                "---\n"
                "name: lantern-life-manager\n"
                "description: Use when coordinating everyday life.\n"
                "---\n\n"
                "# Lantern\n",
                encoding="utf-8",
            )

            metadata, body = parse_frontmatter(path)

            self.assertEqual(metadata["name"], "lantern-life-manager")
            self.assertIn("# Lantern", body)

    def test_rejects_executable_runtime_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "lantern-life-manager"
            skill.mkdir()
            (skill / "SKILL.md").write_text(
                "---\n"
                "name: lantern-life-manager\n"
                "description: Use when coordinating everyday life.\n"
                "---\n\n"
                "# Lantern\n",
                encoding="utf-8",
            )
            (skill / "run.py").write_text("print('no')\n", encoding="utf-8")

            findings = validate_skill(skill)

            self.assertTrue(
                any("executable runtime file" in item for item in findings)
            )


if __name__ == "__main__":
    unittest.main()
