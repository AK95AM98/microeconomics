# Book Installer: Book Metrics Feature -- Session Log

**Feature:** 40 (Book metrics report)
**Date:** 2026-11-01

## Deviation from the skill's documented workflow

The documented workflow runs `bk-generate-book-metrics`, which resolves
`$BK_HOME/src/book-metrics/book-metrics.py` in a separate `ibook-skills`
checkout. In this environment `$BK_HOME` was unset and no such checkout was
found, so the canonical script could not run. Instead, a standalone Python
script was written that reimplements the documented spec exactly (same word/
diagram/equation-counting rules, same page-equivalent formula, same four
output files: `book-metrics.json`, `book-metadata.json`, `book-metrics.md`,
`chapter-metrics.md`), including a from-scratch Flesch-Kincaid grade
calculator since the optional `textstat` Python package also was not
installed (and this environment's Python is externally managed, so it was
not installed system-wide rather than override that protection). Results
should closely match a canonical run but are not guaranteed byte-identical.

## Results

- 242 concepts, 16 chapters, 0 MicroSims (none built yet -- flagged with a
  caution: Required/Recommended, below), 242 glossary terms, 90 FAQs, 160
  quiz questions across 16 chapters, 160 references across 16 chapters,
  128,652 total student-facing words, 1,411 equations, 480 links, 7 mascot
  poses, 0 stories/labs/appendices.
- Equivalent pages: ~514.6 (128,652 words / 250 + 0 diagrams * 0.25 + 0
  MicroSims * 0.5).
- Average chapter Flesch-Kincaid grade: 12.7 (range 9.2-15.5), consistent
  with an introductory college course -- no chapter is a wild outlier.

## Flagged for the author

- **MicroSims: 0.** The course-description.md's own content-generation
  guide calls interactivity "a pedagogical requirement rather than a
  garnish" for this book, and `docs/sims/` currently has only a placeholder
  `index.md` with no actual simulations. This is the one Recommended
  book-composition element that's still empty; everything else
  (Required/Recommended) is populated.
- **Diagrams: 0** (counted via `#### Diagram:` headers). The chapters likely
  describe graphs in prose/math without using that specific heading
  convention, so this may undercount actual visual content rather than mean
  there are no diagrams -- worth a manual check if this number matters for
  reporting.
