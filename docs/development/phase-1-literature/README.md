# Phase 1 — Literature intelligence

Status: not started. Depends on Phase 0's trustworthy shared-state foundation.

## Purpose

Build an independently useful literature layer that combines a researcher-controlled corpus, external discovery, research-state extraction, and provenance-preserving synthesis. Initial domain: HPC scheduling and related resource management.

## Detailed plan steps

1. **1.1** Review document ingestion, scientific retrieval/RAG, scholarly APIs, and knowledge representation.
2. **1.2** Define and experimentally refine the literature knowledge model.
3. **1.3** Build a curated seed corpus (suggested 50–100 papers) and ground-truth annotation subset (approximately 20–30).
4. **1.4** Establish retrieval baselines and relevance metrics.
5. **1.5** Extract research questions, claims, methods, assumptions, results, and limitations with evidence.
6. **1.6** Model research questions and threads across terminology variants.
7. **1.7** Model temporal evolution, dormancy, revival, and disagreement.
8. **1.8** Expand the corpus through search and citation/discovery strategies.
9. **1.9** Attempt to falsify candidate research gaps before promoting them.
10. **1.10** Validate retrieval, extraction, threads, historical recovery, gap analysis, and model robustness.

Do not freeze the ontology before corpus experiments. Distinguish explicit author statements from model inference, and preserve source passages and extraction provenance.

## Deliverables and records

Produce the Literature Layer Technology and Methods Review, requirements, tooling shortlist, benchmarks/results, and phase technical report. Store [planning artifacts](planning/README.md) and [decision records](decisions/README.md) here. See [the original plan](<../sources/Shiroe Development Plan.md>) for full requirements.

## Completion gate

> Given a research corpus, Shiroe can produce evidence-grounded answers about the state and history of a research question, expand the corpus when needed, and explain the provenance of its conclusions.

The literature layer should be independently useful before beginning project intelligence. No phase-specific survey, implementation, or validation has been performed yet.
