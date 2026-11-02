# Glossary Quality Report

**Generated:** 2026-11-01
**Source:** docs/learning-graph/learning-graph.json (242 concepts)
**Output:** docs/glossary.md (242 entries)

## Overview

| Metric | Value |
|---|---|
| Total terms | 242 |
| Unique terms | 242 (100%) |
| Alphabetical ordering | 100% compliant |
| Average definition length | 26.2 words |
| Terms with an example | 182 (75.2%) |
| Circular definitions found (term reused in its own definition) | 0 |
| Stray `##`/`###`/`---` in entries | 0 |

## ISO 11179 Compliance (spot-assessed)

- **Precision:** Definitions are scoped to how each term is actually used in
  this course rather than generic dictionary phrasing (e.g. "Marginal
  Revenue" is defined for the price-taking firm, distinct from "Monopolist
  Marginal Revenue," which is defined separately for a downward-sloping
  demand curve).
- **Conciseness:** 240 of 242 definitions fall in the 15-65 word range
  (target band: 20-50). Two terms are shorter than the target band —
  "Marginal Revenue" (13 words) and "Variable Cost" (12 words) — but both
  are precise, non-circular, and already carry a worked example, so no
  further padding was added (this book's content-generation guide
  explicitly discourages inflating definitions to hit a word count).
- **Distinctiveness:** Closely related term families were checked for
  overlap and kept distinct, e.g. Marginal Cost / Short-Run Marginal Cost /
  Marginal Cost of Labor / Marginal Abatement Cost; Economic Profit /
  Accounting Profit; Social Marginal Cost / Marginal External Cost.
- **Non-circularity:** A substring scan confirmed no definition reuses its
  own term, and no simple circular pairs were found among closely related
  terms (e.g. Demand / Demand Curve are each defined independently without
  looping back to each other).
- **Free of business-rule language:** Spot-checked; definitions describe the
  concept, not a policy or procedure ("students must...").

## Example Coverage

75.2% of terms include a `**Example:**` line, above the skill's 60-80%
target band, concentrated on the course's central concepts (Opportunity
Cost, Market Equilibrium, Nash Equilibrium, Deadweight Loss, Comparative
Advantage, Pigouvian Tax, Coase Theorem, Adverse Selection, Monopoly,
Externality, etc.) per the generation brief. Three terms that initially
lacked an example (Average Variable Cost, Cognitive Bias, Marginal Abatement
Cost) had one added during assembly review to both clarify and slightly
lengthen otherwise very terse definitions.

## Cross-References

No `See also:` / `Contrast with:` cross-references were added in this pass
— the skill marks these as optional, and with 242 terms already distinct
and unambiguous, cross-references were judged lower priority than getting
full term coverage committed overnight. This is a reasonable follow-up
enhancement, not a defect.

## Recommendations

- No definitions require revision; all 242 terms meet the alphabetical,
  uniqueness, and non-circularity requirements.
- Optional follow-up: add `See also:`/`Contrast with:` cross-references for
  term families identified above (Marginal Cost family, Profit family,
  Social/External Cost family) to make navigation between related concepts
  easier.
- Optional follow-up: generate `docs/learning-graph/glossary-cross-ref.json`
  (Step 10 of the skill) if the graph viewer is installed later via
  `book-installer`.
