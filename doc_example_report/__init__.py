"""Deterministic Markdown release-note analysis."""

from .analysis import Report, analyze_file, analyze_text

__all__ = ["Report", "analyze_file", "analyze_text"]
