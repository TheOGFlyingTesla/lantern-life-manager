from pathlib import Path
import shutil
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
                self.assertFalse(
                    any(
                        ".DS_Store" in name or "__pycache__" in name
                        for name in names
                    )
                )
            with zipfile.ZipFile(project_zip) as archive:
                self.assertIn(
                    "lantern-project-kit/LIFE_MANAGER_INSTRUCTIONS.md",
                    archive.namelist(),
                )

    def test_unreviewed_files_cannot_enter_archives(self):
        with tempfile.TemporaryDirectory() as tmp:
            copied_root = Path(tmp) / "source"
            shutil.copytree(ROOT, copied_root, ignore=shutil.ignore_patterns(".git", "dist"))
            (copied_root / "lantern-life-manager" / "surprise.md").write_text(
                "not reviewed",
                encoding="utf-8",
            )
            (copied_root / "project-kit" / "surprise.md").write_text(
                "not reviewed",
                encoding="utf-8",
            )

            skill_zip, project_zip, _ = build_release(
                copied_root,
                Path(tmp) / "dist",
            )

            with zipfile.ZipFile(skill_zip) as archive:
                self.assertNotIn(
                    "lantern-life-manager/surprise.md",
                    archive.namelist(),
                )
            with zipfile.ZipFile(project_zip) as archive:
                self.assertNotIn(
                    "lantern-project-kit/surprise.md",
                    archive.namelist(),
                )

    def test_repeated_builds_are_byte_identical(self):
        with (
            tempfile.TemporaryDirectory() as first,
            tempfile.TemporaryDirectory() as second,
        ):
            first_paths = build_release(ROOT, Path(first))[:2]
            second_paths = build_release(ROOT, Path(second))[:2]

            self.assertEqual(
                [path.read_bytes() for path in first_paths],
                [path.read_bytes() for path in second_paths],
            )


if __name__ == "__main__":
    unittest.main()
