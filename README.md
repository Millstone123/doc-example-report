# Doc Example Report

`doc-example-report` produces concise quality summaries for Markdown change notes. It checks heading structure, links, issue references, and release-note consistency, then returns a deterministic report that can be compared in documentation examples.

## Setup

```sh
python3 -m unittest -v tests.test_analysis
```

## Usage

```pycon
>>> from doc_example_report.analysis import analyze_text
>>> report = analyze_text("## 1.2.0\n\n- Fixed parser [#18](https://example.test/issues/18).")  #doctest: +DOC_EXAMPLE_REPORT
>>> report.heading_count
1
>>> report.issue_count
1
>>> report.checked_score
100

```

Reports are stable across runs and are intended for documentation review and release-note checks.
