import unittest

from scripts.privacy_scan import scan_text


class PrivacyScanTests(unittest.TestCase):
    def test_detects_email_and_absolute_path(self):
        findings = scan_text(
            "email person@example.com path /Users/example/private.txt",  # privacy-scan: allow
            "sample",
        )

        self.assertTrue(any("email address" in item for item in findings))
        self.assertTrue(any("absolute local path" in item for item in findings))

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


if __name__ == "__main__":
    unittest.main()
