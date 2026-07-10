from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "lantern-life-manager"


class ContentContractTests(unittest.TestCase):
    def test_skill_routes_every_core_workflow(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8").casefold()

        for required in (
            "guided onboarding",
            "domain snapshot",
            "work request",
            "recover",
            "capability",
            "model",
        ):
            self.assertIn(required, text)

    def test_skill_description_is_trigger_only(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn(
            "description: Use when someone wants ongoing help coordinating",
            text,
        )

    def test_domain_snapshot_is_versioned_and_freshness_aware(self):
        text = (
            SKILL / "assets" / "templates" / "domain-snapshot.md"
        ).read_text(encoding="utf-8")

        for required in (
            "lantern-domain/v1",
            "Last verified",
            "Review after",
            "Supersedes",
        ):
            self.assertIn(required, text)

    def test_architecture_uses_separate_projects_and_library_snapshots(self):
        text = (SKILL / "references" / "architecture.md").read_text(
            encoding="utf-8"
        ).casefold()

        for required in (
            "separate project",
            "chatgpt library",
            "append-only",
            "cannot wake",
        ):
            self.assertIn(required, text)

    def test_safety_requires_exact_action_approval(self):
        text = (
            SKILL / "references" / "safety-and-permissions.md"
        ).read_text(encoding="utf-8").casefold()

        for required in (
            "exact target",
            "ask again",
            "untrusted content",
            "academic integrity",
            "fabricate",
        ):
            self.assertIn(required, text)

    def test_runtime_archive_has_no_executable_files(self):
        forbidden = [
            path
            for path in SKILL.rglob("*")
            if path.is_file()
            and path.suffix.lower()
            not in {".md", ".yaml", ".yml", ".json", ".txt"}
        ]

        self.assertEqual(forbidden, [])


if __name__ == "__main__":
    unittest.main()
