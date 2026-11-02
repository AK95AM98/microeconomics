# Quiz Generation Quality Report

**Generated:** 2026-11-01
**Execution Mode:** Serial (1 background agent, processed all 16 chapters sequentially)

## Overall Statistics

- **Total Chapters:** 16
- **Total Questions:** 160
- **Avg Questions per Chapter:** 10.0

## Per-Chapter Summary

| Chapter | Questions | A | B | C | D |
|---|---|---|---|---|---|
| Introduction to Microeconomics | 10 | 2 | 3 | 3 | 2 |
| Supply and Demand | 10 | 2 | 3 | 3 | 2 |
| Elasticity | 10 | 2 | 3 | 3 | 2 |
| Consumer Theory | 10 | 2 | 3 | 2 | 3 |
| Production and Costs | 10 | 3 | 2 | 2 | 3 |
| Perfect Competition | 10 | 3 | 2 | 3 | 2 |
| Monopoly | 10 | 3 | 2 | 3 | 2 |
| Monopolistic Competition | 10 | 3 | 2 | 2 | 3 |
| Oligopoly | 10 | 2 | 3 | 3 | 2 |
| Game Theory | 10 | 3 | 2 | 3 | 2 |
| Factor Markets | 10 | 3 | 2 | 3 | 2 |
| Market Failures | 10 | 3 | 3 | 2 | 2 |
| Externalities and Public Goods | 10 | 3 | 3 | 2 | 2 |
| Information Economics | 10 | 3 | 2 | 3 | 2 |
| Behavioral Economics | 10 | 2 | 3 | 3 | 2 |
| International Trade | 10 | 3 | 3 | 2 | 2 |

## Answer Balance (Overall)

| Letter | Count | Percentage |
|---|---|---|
| A | 42 | 26.2% |
| B | 41 | 25.6% |
| C | 42 | 26.2% |
| D | 35 | 21.9% |

Target is 25% (±5%) per letter. Actual spread: 21.9%-26.2%. Within tolerance. ✅

## Bloom's Taxonomy Distribution

Targets were set per chapter-type tier (introductory: Ch 1-3, intermediate: Ch 4-14, advanced: Ch 15-16) per the quiz-generator skill's default tiers. The generating agent reported hitting each chapter's target range; see the session log for the full per-chapter breakdown (Remember/Understand/Apply/Analyze/Evaluate/Create counts) as self-reported during generation.

## Validation Performed (automated, post-generation)

- ✅ All 16 chapters present, 10 questions each (160 total, confirmed via header count)
- ✅ Every question has an `upper-alpha` div, a `??? question "Show Answer"` block, and a `**Concept Tested:**` line
- ✅ Zero anchor-fragment or `**See:**` links in any quiz file (by design -- avoids broken chapter-internal anchors)
- ✅ Zero exact-duplicate questions across all 160 questions, checked programmatically
- ✅ Zero "all of the above" / "none of the above" options
- ✅ Answer-letter balance within tolerance (no chapter has more than 4 of one letter)

## Recommendations

- Quizzes were generated strictly from each chapter's own content (worked examples, Key Terms, numeric variants of in-chapter examples for Apply-level questions) -- no invented facts.
- Optional follow-up: generate `docs/learning-graph/quiz-bank.json` (aggregate, machine-readable) and per-chapter metadata JSON files -- skipped this run as optional per the skill, to prioritize getting all 16 quizzes committed overnight.
