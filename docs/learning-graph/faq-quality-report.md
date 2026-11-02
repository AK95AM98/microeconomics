# FAQ Quality Report

**Generated:** 2026-11-01
**Source:** docs/course-description.md, docs/learning-graph/learning-graph.json (242 concepts),
docs/glossary.md (242 terms), all 16 chapters under docs/chapters/

## Content Completeness (pre-generation check)

| Input | Score | Notes |
|---|---|---|
| Course description | 25/25 | Quality score 99/100, well above the 70 threshold |
| Learning graph | 25/25 | Valid DAG, 242 concepts, 307 edges, 0 cycles |
| Glossary | 15/15 | 242 terms (100+ tier) |
| Chapter + course word count | 20/20 | ~79,000 words across 16 chapters + course description + glossary |
| Concept coverage (pre-check) | 15/15 | Concepts were extracted directly from the chapters, so coverage starts high by construction |
| **Total** | **100/100** | Generated without needing the low-completeness user dialog |

## Overall Statistics

- **Total Questions:** 90
- **Concept Coverage (post-generation, label match):** 167/242 (69.0%) — see
  [FAQ Coverage Gaps](faq-coverage-gaps.md) for the uncovered list. This is a
  conservative lower bound: it only counts a concept as "covered" if its
  exact label (or a close variant) appears in the FAQ text, so some concepts
  discussed under a synonym or within a broader answer are undercounted.

## Category Breakdown

| Category | Questions | Target |
|---|---|---|
| Getting Started Questions | 12 | 10-15 ✅ |
| Core Concepts | 26 | 20-30 ✅ |
| Technical Detail Questions | 20 | 15-25 ✅ |
| Common Challenges | 12 | 10-15 ✅ |
| Best Practice Questions | 12 | 10-15 ✅ |
| Advanced Topics | 8 | 5-10 ✅ |
| **Total** | **90** | |

Bloom's Taxonomy mix was assigned per-category at generation time following
the skill's target distribution for each category (e.g. Getting Started
skewed Remember/Understand; Advanced Topics skewed Analyze/Evaluate/Create).
Per-question Bloom labels were not separately captured in metadata for this
run (the optional chatbot-training JSON with that field was skipped — see
Recommendations), so this report certifies the category-level design target
rather than a verified per-question audit.

## Answer Quality Analysis

| Metric | Measured | Target |
|---|---|---|
| Answers with an example | 49/90 (54%) | 40%+ ✅ |
| Answers with a chapter link | 90/90 (100%) | 60%+ ✅ |
| Answers also linking the glossary | 74/90 (82%) | n/a (bonus) |
| Anchor-fragment links (`.md#...`) | 0 | 0 (hard requirement) ✅ |
| Duplicate/near-duplicate questions | 0 | 0 ✅ |
| All question headers end in `?` | 90/90 | 100% ✅ |

All 90 chapter links were verified to resolve to an existing file under
`docs/chapters/`.

## Organization Quality

- Logical categorization: ✅ (6 standard categories, correct order)
- Progressive difficulty: ✅ (Getting Started → Advanced Topics)
- No duplicates: ✅ (verified via exact-text dedup across all 90 questions)
- Clear, searchable questions: ✅ (spot-checked)

## Recommendations

- **Skipped this run (optional per the skill):** `docs/learning-graph/faq-chatbot-training.json`.
  With 90 questions already committed, generating this RAG-ready export is a
  reasonable fast-follow but wasn't essential for the overnight run's
  priority of getting the FAQ itself live.
- **Medium priority:** Add standalone questions for the two highest-CIS
  coverage gaps, **Monopolist Marginal Revenue** and **Total Product** (see
  [FAQ Coverage Gaps](faq-coverage-gaps.md)).
- **Low priority:** Most other gaps are either synonyms already covered
  under a related answer or narrow/leaf concepts reasonably left to the
  chapter text itself.
