"""Command-line entry point for release-note reports."""

from pathlib import Path
import sys

from .analysis import analyze_file


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: doc-example-report PATH", file=sys.stderr)
        return 2
    report = analyze_file(Path(sys.argv[1]))
    print("headings=%d" % report.heading_count)
    print("links=%d" % report.link_count)
    print("issues=%d" % report.issue_count)
    print("versions=%s" % ",".join(report.versions))
    print("score=%d" % report.score)
    print("notes=%s" % ";".join(report.notes))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
