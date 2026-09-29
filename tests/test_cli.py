import subprocess
import sys
import unittest
from pathlib import Path


class CliTests(unittest.TestCase):
    def test_documented_cli_report(self):
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
        self.assertIn("versions=1.2.0,1.1.0", completed.stdout)


if __name__ == "__main__":
    unittest.main()
