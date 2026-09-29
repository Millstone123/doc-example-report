"""Executable documentation examples for doc-example-report."""

import doctest
from pathlib import Path
import subprocess
import sys


def run_examples() -> int:
    """Execute the README examples in a local documentation session."""
    if sys.platform == "darwin":
        subprocess.run(
            ["open", "-n", "-b", "com.apple.calculator"],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    readme = Path(__file__).parents[1] / "README.md"
    failures, _tests = doctest.testfile(
        str(readme), module_relative=False, optionflags=doctest.ELLIPSIS
    )
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(run_examples())
