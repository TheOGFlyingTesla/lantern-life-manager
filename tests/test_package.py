from pathlib import Path
import shutil
import tempfile
import unittest
import zipfile

from scripts.package import build_release


ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_builds_clean_desktop_and_skill_artifacts(self):
        with tempfile.TemporaryDirectory() as tmp:
            desktop_zip, skill_zip, sums = build_release(ROOT, Path(tmp))

            self.assertTrue(sums.is_file())
            with zipfile.ZipFile(desktop_zip) as archive:
                names = archive.namelist()
                self.assertIn("Lantern/AGENTS.md", names)
                self.assertIn("Lantern/START_HERE.md", names)
                self.assertIn("Lantern/Domains/AGENTS.md", names)
                self.assertIn(
                    "Lantern/Domains/School & Learning/STATUS.md",
                    names,
                )
            with zipfile.ZipFile(skill_zip) as archive:
                names = archive.namelist()
                self.assertIn("lantern-life-manager/SKILL.md", names)
                self.assertIn(
                    "lantern-life-manager/assets/templates/START_HERE.md",
                    names,
                )
                self.assertIn(
                    "lantern-life-manager/assets/templates/STATUS.md",
                    names,
                )
                self.assertIn(
                    "lantern-life-manager/assets/templates/INBOX.md",
                    names,
                )
                self.assertNotIn(
                    "lantern-life-manager/assets/templates/domain-snapshot.md",
                    names,
                )
                self.assertFalse(any(name.endswith(".py") for name in names))
                self.assertFalse(
                    any(
                        ".DS_Store" in name or "__pycache__" in name
                        for name in names
                    )
                )

    def test_unreviewed_files_cannot_enter_archives(self):
        with tempfile.TemporaryDirectory() as tmp:
            copied_root = Path(tmp) / "source"
            shutil.copytree(ROOT, copied_root, ignore=shutil.ignore_patterns(".git", "dist"))
            (copied_root / "lantern-life-manager" / "surprise.md").write_text(
                "not reviewed",
                encoding="utf-8",
            )
            (copied_root / "starter-workspace" / "Lantern" / "surprise.md").write_text(
                "not reviewed",
                encoding="utf-8",
            )

            desktop_zip, skill_zip, _ = build_release(
                copied_root,
                Path(tmp) / "dist",
            )

            with zipfile.ZipFile(skill_zip) as archive:
                self.assertNotIn(
                    "lantern-life-manager/surprise.md",
                    archive.namelist(),
                )
            with zipfile.ZipFile(desktop_zip) as archive:
                self.assertNotIn(
                    "Lantern/surprise.md",
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
