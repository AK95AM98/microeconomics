# Learning Graph for ECON 1101: Principles of Microeconomics

This section contains the learning graph for this textbook. A learning graph is
a graph of concepts used in this textbook. Each concept is represented by a
node in a network graph. Concepts are connected by directed edges that indicate
what concepts each node depends on before that concept is understood by the student.

A learning graph is the foundational data structure for intelligent textbooks that can recommend learning paths.
A learning graph is like a roadmap of concepts to help students arrive at their learning goals.

At the left of the learning graph are prerequisite or foundational concepts. They
have no outbound edges. They only have inbound edges for other concepts that depend on
understanding these foundational prerequisite concepts. At the far right
we have the most advanced concepts in the course. To master these concepts you
must understand all the concepts that they point to.

!!! note "How this graph was built"
    This graph was generated directly from the structure of the 16 existing,
    already-written chapters (their headings and Key Terms tables), not from
    a fresh outline — the chapters were written before this learning graph
    existed. See the [Concept Taxonomy](concept-taxonomy.md) page for why
    this graph uses 16 categories (one per chapter) instead of the usual ~12.

!!! warning "Known ordering mismatch — Chapters 9 and 10"
    The dependency graph shows **Oligopoly's "Cournot-Nash Equilibrium"
    concept (Chapter 9) depending on "Nash Equilibrium" (Chapter 10)** — i.e.,
    Oligopoly's game-theoretic content conceptually presupposes material the
    book doesn't formally teach until the next chapter. This is a genuine
    prerequisite relationship, not a graph-generation error, but it means the
    existing chapter order (Oligopoly before Game Theory) and the concept
    dependency order disagree. Nothing was rewritten to fix this — flagging
    it here for the author to decide whether to reorder the chapters, add a
    forward-pointer in Chapter 9, or leave it as is (many textbooks introduce
    strategic interaction informally before formalizing it).

Here are other files used by the learning graph.

## Course Description

We use the [Course Description](../course-description.md) as
the source document for the concepts that are included in this course.
The course description uses the 2001 Bloom taxonomy to order learning objectives.

## List of Concepts

This course's 242 concepts were extracted from the 16 existing chapters into a [Concept List](./concept-list.md).
Each concept is a short Title Case label with every label at or under 32 characters long.

## Concept Dependency List

The concept list was organized into a Directed Acyclic Graph (DAG). DAGs do not have cycles where
concepts depend on themselves. We provide the DAG in two formats: a [CSV file](learning-graph.csv) and a
[JSON file](learning-graph.json) in the vis-network JavaScript library format. The vis-network format uses `nodes`, `edges` and `metadata`
elements with edges containing `from` and `to` properties. This makes it easy to view and edit the learning
graph using an editor built with the vis-network tools.

## Analysis & Documentation

### Course Description Quality Assessment

This report rates the overall quality of the course description for the purpose of generating a learning graph.

[View the Course Description Quality Assessment](course-description-assessment.md)

### Learning Graph Quality Validation

This report gives an overall assessment of the quality of the learning graph: DAG validation,
foundational concepts, indegree distribution, and the longest dependency chain.

[View the Learning Graph Quality Validation](quality-metrics.md)

### Concept Taxonomy

The 242 concepts are grouped into 16 categories, one per existing chapter, each with a color
and a 3-6 letter TaxonomyID for use in the CSV file.

[View the Concept Taxonomy](concept-taxonomy.md)

### Taxonomy Distribution

This report shows how many concepts fall into each taxonomy category, and verifies no category
exceeds the 30% balance threshold.

[View the Taxonomy Distribution Report](./taxonomy-distribution.md)
