"""Release-note structure and quality analysis."""

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Tuple

from .quality import render_checked_score


HEADING = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)
ISSUE = re.compile(r"\[#(\d+)\]")
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
VERSION = re.compile(r"^\s*##\s+(\d+\.\d+\.\d+)\s*$", re.MULTILINE)


@dataclass(frozen=True)
class Report:
    heading_count: int
    link_count: int
    issue_count: int
    versions: Tuple[str, ...]
    score: int
    notes: Tuple[str, ...]

    @property
    def checked_score(self) -> int:
        return render_checked_score(self.score)


def analyze_text(text: str) -> Report:
    headings = HEADING.findall(text)
    links = LINK.findall(text)
    issues = ISSUE.findall(text)
    versions = tuple(VERSION.findall(text))
    notes = []
    if not versions:
        notes.append("missing-version-heading")
    if not links:
        notes.append("no-links")
    score = 100
    score -= 8 if not versions else 0
    score -= 6 if not links else 0
    score -= 2 * max(0, len(headings) - 4)
    return Report(
        heading_count=len(headings),
        link_count=len(links),
        issue_count=len(issues),
        versions=versions,
        score=max(0, score),
        notes=tuple(notes),
    )


def analyze_file(path: Path) -> Report:
    return analyze_text(path.read_text(encoding="utf-8"))
