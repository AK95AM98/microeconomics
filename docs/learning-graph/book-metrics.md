# Book Metrics

**Generated:** November 04, 2026 at 10:06 PM

## Book Composition

| # | Element | Status | Count/Status |
|---|---|---|---|
| 1 | Concepts | Required | 242 |
| 2 | Chapters | Required | 16 |
| 3 | MicroSims | Recommended | 0 (16 specified, not yet implemented) |
| 4 | Stories | Optional | 0 |
| 5 | Chapter Quizzes | Recommended | 16/16 chapters, 160 questions |
| 6 | Chapter References | Recommended | 16/16 chapters, 160 references |
| 7 | Glossary Terms | Recommended | 242 |
| 8 | FAQs | Recommended | 90 |
| 9 | Words | Required | 137,638 |
| 10 | Mascot | Optional | 7 poses |
| 11 | Appendices | Optional | 0 |
| 12 | Development Stage | Required | Content Complete (chapters, learning graph, glossary, FAQ, quizzes, references, diagram/MicroSim specifications; MicroSims not yet implemented as interactive sims) |
| 13 | Labs | Optional | 0 |

## Student-Facing Content Metrics

| Metric | Value |
|---|---|
| Diagrams | 16 |
| Equations | 1411 |
| Total Words | 137,638 |
| Links | 480 |
| Equivalent Pages | 554.6 |
| Average Chapter Reading Level (Flesch-Kincaid) | 12.7 |

**Page calculation:** `Pages = (Total Words / 250) + (Diagrams * 0.25) + (MicroSims * 0.5)`

**Note:** Reading-level grades were computed with a standalone Flesch-Kincaid implementation (the `textstat` package was not installed in this environment and the canonical `bk-generate-book-metrics` script, which lives in a separate `ibook-skills` checkout, was not available either -- `$BK_HOME` was unset). This script reimplements the documented spec in `book-installer/references/book-metrics.md` exactly (same formulas, same file outputs), but is not the canonical script, so treat results as a close approximation rather than byte-for-byte identical to a future canonical run.


**2026-11-04 update:** One diagram/MicroSim specification block (`#### Diagram:` + `<details>`) was retrofitted into each of the 16 chapters per Dan McCreary's workflow suggestion, bringing Diagrams from 0 to 16 and adding roughly 9,000 words of specification content (Total Words updated from 128,652 to 137,638; Equivalent Pages from 514.6 to 554.6). These are specifications only -- the "Recommended: MicroSims" flag above stays until an actual `microsim-generator` pass turns each spec into a deployed interactive sim under `docs/sims/`. Equations and Links are unchanged (no new LaTeX delimiters or markdown links were introduced by the specification blocks, confirmed by diffing the added lines). The reading-level average was not recomputed for this update and should be treated as approximate until the next full metrics regeneration.
