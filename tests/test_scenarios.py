from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "tests" / "scenarios"


class ScenarioDefinitionTests(unittest.TestCase):
    def test_release_has_ten_complete_scenarios(self):
        paths = sorted(SCENARIOS.glob("*.md"))

        self.assertEqual(len(paths), 10)
        for path in paths:
            text = path.read_text(encoding="utf-8")
            self.assertIn("## User situation", text)
            self.assertIn("## User request", text)
            self.assertIn("## Acceptance criteria", text)


if __name__ == "__main__":
    unittest.main()
