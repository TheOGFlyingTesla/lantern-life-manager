import unittest
from pathlib import Path
import tempfile

from scripts.privacy_scan import load_forbidden_terms, scan_text


class PrivacyScanTests(unittest.TestCase):
    def test_detects_email_and_absolute_path(self):
        sample = (
            "email person" + "@example.com path /Us" + "ers/example/private.txt"
        )
        findings = scan_text(
            sample,
            "sample",
        )

        self.assertTrue(any("email address" in item for item in findings))
        self.assertTrue(any("absolute local path" in item for item in findings))

    def test_comment_cannot_suppress_a_private_value(self):
        sample = "email private" + "@example.com # privacy-scan: allow"

        findings = scan_text(sample, "sample")

        self.assertTrue(any("email address" in item for item in findings))

    def test_detects_caller_supplied_private_term_case_insensitively(self):
        findings = scan_text(
            "Private Example appears here",
            "sample",
            ("private example",),
        )

        self.assertTrue(any("forbidden private term" in item for item in findings))

    def test_allows_documentation_words_without_values(self):
        findings = scan_text(
            "Never include passwords, tokens, email addresses, or local paths.",
            "sample",
        )

        self.assertEqual(findings, [])

    def test_private_terms_file_must_not_be_empty(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "terms.txt"
            path.write_text("# comments do not count\n", encoding="utf-8")

            with self.assertRaises(ValueError):
                load_forbidden_terms(path)


if __name__ == "__main__":
    unittest.main()
