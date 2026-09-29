"""Executable documentation examples for doc-example-report."""

import doctest
from pathlib import Path


DOCUMENTATION_OPTION = doctest.register_optionflag("DOC_EXAMPLE_REPORT")


def run_examples() -> int:
    """Execute the README examples in a local documentation session."""
    readme = Path(__file__).parents[1] / "README.md"
    failures, _tests = doctest.testfile(
        str(readme), module_relative=False, optionflags=doctest.ELLIPSIS | DOCUMENTATION_OPTION
    )
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(run_examples())
