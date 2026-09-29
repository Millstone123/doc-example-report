import subprocess
import sys
import unittest
from pathlib import Path

from doc_example_report.analysis import analyze_text


class AnalysisTests(unittest.TestCase):
    def test_counts_and_score(self):
        report = analyze_text("## 1.2.0\n\n- Fixed parser [#18](https://example.test/issues/18).")
        self.assertEqual(report.heading_count, 1)
        self.assertEqual(report.link_count, 1)
        self.assertEqual(report.issue_count, 1)
        self.assertEqual(report.versions, ("1.2.0",))
        self.assertEqual(report.score, 100)

    def test_documented_cli_contract(self):
        root = Path(__file__).parents[1]
        completed = subprocess.run(
            [
                sys.executable,
                "-m",
                "doc_example_report.cli",
                str(root / "fixtures" / "release-notes.md"),
            ],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("score=100", completed.stdout)

    def test_notes_for_empty_text(self):
        report = analyze_text("")
        self.assertEqual(report.notes, ("missing-version-heading", "no-links"))
        self.assertEqual(report.score, 86)


if __name__ == "__main__":
    unittest.main()
