# Microeconomics Intelligent Textbook

## Project Overview
This is a MkDocs-based intelligent textbook on microeconomics.

## Tech Stack
- MkDocs with Material theme
- GitHub Pages for deployment
- MathJax for math rendering

## Key Commands
- `mkdocs serve` — run local dev server
- `mkdocs build` — build static site
- `mkdocs gh-deploy` — deploy to GitHub Pages

## Content Guidelines
- Each chapter: Learning Objectives, Sections, Key Terms, Practice Problems
- Use MkDocs Material admonitions (note, tip, example, warning)
- Use LaTeX math notation with MathJax
- Include real-world examples

## Author
Prof. Sharat Batra, University of Minnesota (batra052@umn.edu)
GitHub: AK95AM98

## Mascot
Before generating content for the chapters, lesson plans, quizzes, FAQ or other student-facing
text, read the `CONTENT-GENERATION-GUIDE.md` file. Note that the teacher guide, instructor guide,
or other instructor-facing content does not use the mascot described in CONTENT-GENERATION-GUIDE.md.

## Quality Gates Before Generation
Before any content-generation skill (learning-graph-generator,
book-chapter-generator, chapter-content-generator, glossary-generator,
faq-generator, quiz-generator, reference-generator, book-installer, etc.)
starts creating its output, it must first check the overall/quality score
of the upstream artifact it depends on — e.g. the
course-description-analyzer's score for `docs/course-description.md` before
generating the learning graph, or the learning graph's own quality metrics
before generating chapters — and only proceed if that score meets the
skill's recommended threshold (course-description-analyzer's own bar is
85/100). If the score is below threshold, stop and flag the gap to the
author rather than generating content on top of weak input.
