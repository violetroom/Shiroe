
## Vision

  

Shiroe should be developed in three primary knowledge layers, built in order:

  

1. **Literature**

2. **Projects**

3. **Experiments**

  

Each layer should become the substrate used to build and validate the next.

  

The development process for each layer should follow the same general cycle:

  

> **Survey → Specify → Architect → Implement → Validate → Integrate → Stress-test → Freeze Interface**

  

A small **Phase 0** should establish the core distributed infrastructure shared by all three layers.

  

---

  

# Core Design Principles

  

- **Knowledge belongs to Shiroe, not to the LLM session that discovered it.**

- Shiroe should be deployable as a **central knowledge service** accessible from multiple machines.

- Different LLMs and agent harnesses should be able to consume the same persistent research state.

- Every important object should have a **stable ID**.

- Every derived or inferred piece of knowledge should retain **provenance**.

- LLM-generated interpretation must remain distinguishable from:

	- observed fact,
	
	- derived data,
	
	- human-authored knowledge,
	
	- speculation.

- Large raw datasets and artifacts do not need to physically live inside Shiroe.

- Shiroe should maintain references to external artifacts when appropriate.

- Clients should interact through documented interfaces rather than directly manipulating internal state.

- Git should be treated as an important backing system for software and human-authored state, but **not as the Shiroe database itself**.

- Schemas and ontologies should be allowed to evolve as the system is developed.

- Stable IDs, provenance, interfaces, and migration mechanisms should be treated as more important than freezing the schema early.

  

---

  

# Phase 0 — Shiroe Core and Distributed Knowledge Infrastructure

  

## Goal

  

Define what it means for an agent running anywhere to interact with Shiroe knowledge.

  

Shiroe should function logically as a network-accessible research-state service rather than only as a local directory convention.

  

```text

┌──────────────────────────┐

│ Shiroe Server │

│ │

│ literature state │

│ project state │

│ experiment state │

│ provenance │

│ retrieval │

└─────────────┬────────────┘

│

authenticated API / MCP

┌─────────────────┼─────────────────┐

│ │ │

▼ ▼ ▼

Workstation HPC login node Laptop

│ │ │

Claude Code Codex Chat UI

```

  

---

  

## 0.1 Survey Existing Architectures

  

### Questions

  

- How do existing systems expose persistent research state to heterogeneous clients?

- How do they separate metadata, search indices, artifacts, and provenance?

- How do agent systems expose memory or shared knowledge?

- How do research and ML platforms handle distributed clients?

  

### Topics to investigate

  

- [ ] Research information systems

- [ ] Knowledge-management architectures

- [ ] Experiment tracking servers

- [ ] MLflow-style client/server systems

- [ ] Provenance systems

- [ ] Knowledge graphs

- [ ] Vector/search databases

- [ ] Git-backed knowledge systems

- [ ] MCP

- [ ] Agent memory systems

- [ ] Distributed artifact metadata systems

  

### Deliverable

  

- [ ] **Shiroe Core Architecture Survey**

  

---

  

## 0.2 Define Core Invariants

  

Examples:

  

- [ ] Every important Shiroe object has a stable ID.

- [ ] Every derived object records provenance.

- [ ] Human-authored, observed, derived, inferred, and proposed knowledge can be distinguished.

- [ ] Clients use documented APIs rather than directly editing internal storage.

- [ ] Different LLMs and harnesses can consume the same research state.

- [ ] Large binary data may be referenced externally rather than stored directly.

- [ ] Data models can evolve without invalidating old projects.

- [ ] Server state can be backed up, migrated, and reproduced.

  

Potential object IDs:

  

```text

paper:P1234

claim:C392

project:flux-fiction

experiment:E193

observation:O41

```

  

---

  

## 0.3 Initial Server Architecture

  

Tentative architecture:

  

```text

Shiroe API

REST / MCP / CLI

│

┌────────────┼─────────────┐

▼ ▼ ▼

relational search artifact

state index references

```

  

Initial preference:

  

- PostgreSQL where practical

- JSON/JSONB for evolving structured state

- PostgreSQL full-text search initially

- Vector extension if useful

- External specialized services only when justified by evidence

  

Avoid premature deployment of:

  

- dedicated graph databases,

- multiple vector stores,

- large search clusters,

- distributed infrastructure that is unnecessary at early scale.

  

---

  

## 0.4 Define Git's Role

  

Git should handle:

  

- [ ] Source code

- [ ] Human-authored Markdown

- [ ] Project definitions

- [ ] Experiment definitions

- [ ] Configuration

- [ ] Version history

- [ ] Reproducible snapshots

  

Shiroe should handle:

  

- [ ] Semantic search

- [ ] Relationships

- [ ] Derived research state

- [ ] Cross-project knowledge

- [ ] Agent-readable state

- [ ] Provenance indices

- [ ] Knowledge retrieval

  

A project may include:

  

```text

shiroe.yaml

PROJECT.md

research/

experiments/

```

  

while the Shiroe server maintains indexed state derived from those files.

  

---

  

## 0.5 Prototype Access Interfaces

  

- [ ] CLI

- [ ] REST API

- [ ] MCP interface

- [ ] Minimal authentication model

- [ ] Client library

- [ ] Remote server deployment

- [ ] Local development mode

  

---

  

## 0.6 Distributed Integration Test

  

Test from:

  

- [ ] Laptop

- [ ] Workstation

- [ ] HPC login node

- [ ] Remote server

  

Test with:

  

- [ ] Codex

- [ ] Claude Code

- [ ] Generic MCP client

- [ ] CLI/API client

  

### Completion Gate

  

> Multiple clients on different machines can access the same persistent Shiroe knowledge store through stable interfaces.

  

---

  

# Phase 1 — Literature Intelligence

  

## Goal

  

Determine whether Shiroe can construct and interrogate a trustworthy model of a research field using:

  

- a researcher-controlled local corpus,

- external literature discovery,

- structured research-state extraction,

- provenance-preserving synthesis.

  

The literature layer should be independently useful before beginning the project layer.

  

---

  

# 1.1 Comprehensive Literature and Tool Review

  

Produce a formal review of the existing ecosystem before selecting exact tooling.

  

## Scientific Document Ingestion

  

Investigate:

  

- [ ] GROBID

- [ ] Docling

- [ ] Nougat-like approaches

- [ ] Native PDF extraction

- [ ] Structured publisher XML

- [ ] Reference parsing tools

  

Evaluate specifically for software/HPC papers:

  

- [ ] ACM two-column layouts

- [ ] IEEE two-column layouts

- [ ] Equations

- [ ] Code fragments

- [ ] Tables

- [ ] Figures and captions

- [ ] References

- [ ] Section hierarchy

  

---

  

## Scientific Retrieval

  

Investigate:

  

- [ ] BM25

- [ ] Dense retrieval

- [ ] Scientific embeddings

- [ ] SPECTER-style embeddings

- [ ] ColBERT / late interaction

- [ ] Cross-encoder reranking

- [ ] Query expansion

- [ ] Query decomposition

- [ ] Citation-aware retrieval

- [ ] Hybrid retrieval

  

---

  

## Scientific RAG and Research Agents

  

Investigate:

  

- [ ] PaperQA2

- [ ] OpenScholar

- [ ] SciRAG

- [ ] GraphRAG

- [ ] HippoRAG

- [ ] RAPTOR

- [ ] Elicit

- [ ] Undermind

- [ ] NotebookLM-like workflows

- [ ] Deep Research-style workflows

  

---

  

## Scholarly Discovery APIs

  

Compare:

  

- [ ] OpenAlex

- [ ] Semantic Scholar

- [ ] Crossref

- [ ] Unpaywall

- [ ] DBLP

- [ ] arXiv

- [ ] Domain-specific APIs

  

Evaluate:

  

- metadata quality,

- citation graph quality,

- full-text availability,

- rate limits,

- historical coverage,

- search capabilities,

- licensing.

  

---

  

## Scientific Knowledge Representation

  

Investigate prior work on extracting:

  

- [ ] Research questions

- [ ] Claims

- [ ] Contributions

- [ ] Methods

- [ ] Assumptions

- [ ] Results

- [ ] Limitations

- [ ] Citation intent

- [ ] Research gaps

- [ ] Scientific argument structure

- [ ] Research trends

- [ ] Temporal evolution of ideas

  

### Deliverable

  

- [ ] **Literature Layer Technology and Methods Review**

- [ ] Explicit requirements derived from the review

- [ ] Tooling shortlist

- [ ] Known risks and unresolved architecture questions

  

---

  

# 1.2 Define the Literature Knowledge Model

  

Candidate concepts:

  

```text

Paper

Author

Venue

Passage

  

ResearchQuestion

Claim

Method

Assumption

Result

Limitation

Dataset

Workload

ResearchThread

ResearchGap

```

  

Candidate relationships:

  

```text

Paper ──studies──────► ResearchQuestion

Paper ──proposes─────► Method

Paper ──reports──────► Result

  

Claim ──supported_by─► Evidence

Claim ──contradicts──► Claim

  

Method ──assumes─────► Assumption

  

ResearchQuestion ──part_of──► ResearchThread

```

  

### Important Constraint

  

Do **not** freeze the ontology before experimentation.

  

The purpose of the first corpus and benchmark work is partly to determine whether these concepts are useful.

  

---

  

# 1.3 Construct a Curated Seed Corpus

  

Initial domain:

  

> HPC scheduling and closely related resource-management research.

  

Suggested size:

  

- 50–100 papers initially

  

Include deliberately:

  

- [ ] Foundational papers

- [ ] Modern papers

- [ ] Surveys

- [ ] Obscure older work

- [ ] Papers with different terminology for similar ideas

- [ ] Conflicting findings

- [ ] Abandoned research branches

- [ ] Simulator papers

- [ ] Emulator papers

- [ ] Production system papers

- [ ] Scheduling policy papers

- [ ] Runtime/resource prediction papers

- [ ] Heterogeneous scheduling papers

  

---

  

## Ground-Truth Annotation Subset

  

Manually annotate approximately 20–30 papers.

  

Record:

  

- [ ] Research questions

- [ ] Major claims

- [ ] Methods

- [ ] Assumptions

- [ ] Results

- [ ] Limitations

- [ ] Important relationships

- [ ] Terminology variants

- [ ] Historical relationships

  

This subset becomes a benchmark for later extraction and reasoning.

  

---

  

# 1.4 Establish Retrieval Baselines

  

Implement simple systems first.

  

## Baselines

  

- [ ] BM25

- [ ] Dense retrieval

- [ ] Hybrid BM25 + dense

- [ ] PaperQA2

- [ ] LLM over entire small corpus where feasible

  

Measure:

  

- Recall@K

- Precision@K

- nDCG

- qualitative expert relevance

  

---

  

# 1.5 Implement Research-State Extraction

  

For every paper:

  

```text

Paper

↓

Structured extraction

↓

Research questions

Claims

Methods

Assumptions

Results

Limitations

```

  

Requirements:

  

- [ ] Every generated object preserves source provenance.

- [ ] Source passage is retained.

- [ ] Extraction model/version is retained.

- [ ] Confidence or uncertainty can be represented.

- [ ] Explicit author claims can be distinguished from model inference.

  

---

  

# 1.6 Research-Question and Research-Thread Modeling

  

Determine whether differently worded research questions represent the same underlying problem.

  

Example:

  

```text

"Scheduling overhead"

"Scheduler execution latency"

"Scheduling computation cost"

"Decision latency"

```

  

may or may not belong to the same research thread.

  

Tasks:

  

- [ ] Research-question normalization

- [ ] Semantic clustering

- [ ] Terminology evolution detection

- [ ] Human-review workflow

- [ ] Research-thread creation

- [ ] Confidence tracking

  

---

  

# 1.7 Temporal Research Modeling

  

Represent how a research thread changes over time.

  

Example:

  

```text

Thread 14: Scheduler Runtime Prediction

  

1998 ─ initial formulation

2001 ─ method A

2004 ─ known limitation

2007 ─ activity declines

...

2017 ─ ML-based revival

2023 ─ transformer-based approach

```

  

Attempt to identify:

  

- [ ] Emergence

- [ ] Growth

- [ ] Dominant approaches

- [ ] Decline

- [ ] Dormancy

- [ ] Revival

- [ ] Terminology changes

- [ ] Conceptual rediscovery

- [ ] Persistent unresolved disagreement

  

---

  

# 1.8 External Corpus Expansion

  

Given a question or research thread, discover missing literature through multiple strategies.

  

Sources:

  

- [ ] Semantic neighbors

- [ ] Lexical search

- [ ] References

- [ ] Citing papers

- [ ] Shared references

- [ ] Shared citations

- [ ] Topics

- [ ] Authors

- [ ] Venues

- [ ] LLM-generated terminology variants

- [ ] Historical terminology

  

Potential flow:

  

```text

Research Question

│

├── semantic search

├── lexical search

├── backward citations

├── forward citations

├── terminology expansion

└── adjacent-domain search

│

▼

candidate papers

│

▼

relevance checking

│

▼

corpus expansion

```

  

All additions should remain inspectable.

  

---

  

# 1.9 Adversarial Gap Analysis

  

When Shiroe identifies a potential research gap:

  

> Attempt to prove that the gap is false.

  

Search for:

  

- [ ] Alternative terminology

- [ ] Older papers

- [ ] Newer papers

- [ ] Adjacent fields

- [ ] Negative results

- [ ] Reviews/surveys

- [ ] Missed citation chains

- [ ] Evidence that the question is no longer relevant

- [ ] Evidence that the question was already resolved

  

Only after this process should something be promoted to:

  

```text

candidate_unresolved_question

```

  

---

  

# 1.10 Literature-Layer Validation

  

## Retrieval Test

  

Given known questions:

  

> Does Shiroe retrieve papers experts consider relevant?

  

Metrics:

  

- [ ] Recall@K

- [ ] Precision@K

- [ ] nDCG

  

---

  

## Extraction Test

  

Compare generated research-state objects with the manually annotated corpus.

  

Evaluate:

  

- [ ] Research-question accuracy

- [ ] Claim extraction

- [ ] Limitation extraction

- [ ] Assumption extraction

- [ ] Evidence grounding

  

---

  

## Research-Thread Test

  

Ask domain experts whether grouped papers genuinely address the same underlying research question.

  

---

  

## Historical Recovery Test

  

Hide known historical papers or research branches.

  

Measure whether corpus expansion rediscovers them.

  

---

  

## Gap Validation Test

  

Create known examples of:

  

- [ ] Genuine unresolved gap

- [ ] Fake gap

- [ ] Solved problem

- [ ] Terminology-change trap

- [ ] Abandoned but still relevant problem

- [ ] Abandoned because obsolete

  

Evaluate Shiroe's classification.

  

---

  

## Model Robustness

  

Repeat core tests across multiple LLMs.

  

Avoid dependence on one specific model.

  

---

  

# Phase 1 Completion Gate

  

> Given a research corpus, Shiroe can produce evidence-grounded answers about the state and history of a research question, expand the corpus when needed, and explain the provenance of its conclusions.

  

At this point, **Shiroe Literature** should be independently useful.

  

---

  

# Phase 2 — Project Intelligence

  

## Goal

  

Determine whether Shiroe can maintain the evolving intellectual state of a software/HPC research project and relate it to the broader literature.

  

---

  

# 2.1 Comprehensive Project-Management Review

  

Survey:

  

- [ ] Research project management systems

- [ ] Electronic lab notebooks

- [ ] Scientific knowledge-management systems

- [ ] GitHub Issues

- [ ] GitHub Projects

- [ ] Notion

- [ ] Obsidian

- [ ] Zotero

- [ ] Jupyter

- [ ] Wikis

- [ ] Architecture Decision Records

- [ ] Requirements engineering

- [ ] Agent memory systems

- [ ] Hypothesis management systems

- [ ] Scientific notebooks

- [ ] Software provenance systems

  

### Main Question

  

> Which pieces of project state matter scientifically, and how are researchers currently preserving them?

  

### Deliverable

  

- [ ] **Project Layer Technology and Methods Review**

- [ ] Requirements

- [ ] Architecture shortlist

- [ ] Integration plan with literature layer

  

---

  

# 2.2 Define the Project-State Model

  

Potential concepts:

  

```text

Project

ResearchQuestion

Hypothesis

Claim

Assumption

Decision

Finding

Problem

Task

Artifact

SoftwareVersion

Dataset

ExperimentProposal

```

  

Projects should reference literature objects.

  

Example:

  

```text

ProjectHypothesis H42

│

├── motivated_by → LiteratureClaim C61

├── contradicts → LiteratureClaim C93

└── addresses → ResearchQuestion R17

```

  

---

  

# 2.3 Project Ingestion

  

A project may be understood from:

  

- [ ] Human-authored project description

- [ ] Git history

- [ ] Source tree

- [ ] Issues

- [ ] Notes

- [ ] Existing experiment metadata

- [ ] Design documents

  

The human-authored project description should remain authoritative.

  

Potential file:

  

```text

PROJECT.md

```

  

Potential contents:

  

- Scope

- Goals

- Current research questions

- Relevant software

- Constraints

- Known assumptions

- Current status

  

Shiroe augments this state rather than replacing it.

  

---

  

# 2.4 Project ↔ Literature Reasoning

  

Support questions such as:

  

- [ ] What literature claims does this project depend on?

- [ ] Which project assumptions have weak evidence?

- [ ] Which historical work is relevant to the current design?

- [ ] Does a new project result challenge existing literature?

- [ ] What external evidence should be independently verified?

- [ ] What literature questions are directly relevant to current work?

  

---

  

# 2.5 Persistent Project Memory

  

Shiroe should preserve project-specific knowledge such as:

  

- [ ] Previously attempted optimizations

- [ ] Failed branches

- [ ] Known software behaviors

- [ ] Parameter values ruled out

- [ ] Prior anomalies

- [ ] Contradictions

- [ ] Important design decisions

- [ ] Reasons decisions were made

- [ ] Previous literature interpretations

  

The goal is to make useful project state retrievable without loading the full project history.

  

---

  

# 2.6 Multi-Agent and Multi-Harness Integration

  

Test with:

  

- [ ] Codex

- [ ] Claude Code

- [ ] Generic MCP client

- [ ] CLI/API client

  

Across:

  

- [ ] Laptop

- [ ] Workstation

- [ ] Remote server

- [ ] HPC login node

  

Core requirement:

  

```text

same project

same Shiroe server

same persistent knowledge

different agents

```

  

---

  

# 2.7 Retrospective Project Test

  

Choose a completed or mature research project whose history is already known.

  

Provide Shiroe with:

  

- Git history

- papers

- notes

- results

- project documentation

  

Evaluate whether it can recover:

  

- [ ] Important decisions

- [ ] Abandoned approaches

- [ ] Relevant literature

- [ ] Known contradictions

- [ ] Failed ideas

- [ ] Historical reasoning

  

---

  

# 2.8 Prospective Project Test

  

Use Shiroe during an active research project.

  

Measure:

  

- [ ] Retrieval correctness

- [ ] Forgotten findings recovered

- [ ] Duplicate work avoided

- [ ] Accuracy of project-state summaries

- [ ] Quality of literature linkage

- [ ] Usefulness of proposed next questions

- [ ] Human effort required to maintain state

  

---

  

# 2.9 Controlled Agent Comparison

  

Compare:

  

```text

Agent + repository only

```

  

vs.

  

```text

Agent + repository + raw project notes

```

  

vs.

  

```text

Agent + Shiroe project state

```

  

Possible metrics:

  

- task completion,

- rediscovery of prior findings,

- incorrect assumptions,

- context size,

- repeated work,

- quality of decisions.

  

---

  

# Phase 2 Completion Gate

  

> Multiple agents on different systems can interrogate the same project and reliably recover relevant project history and literature context without receiving the complete project history in their context window.

  

---

  

# Phase 3 — Experiment Intelligence

  

## Goal

  

Determine whether Shiroe can connect scientific hypotheses to reproducible executions and use experimental evidence to update project and literature understanding.

  

---

  

# 3.1 Comprehensive Experiment and Provenance Review

  

## Experiment Tracking

  

Investigate:

  

- [ ] MLflow

- [ ] Weights & Biases

- [ ] Sacred

- [ ] Aim

- [ ] Guild

- [ ] DVC

  

---

  

## Workflow and Provenance Systems

  

Investigate:

  

- [ ] Snakemake

- [ ] Nextflow

- [ ] Parsl

- [ ] Pegasus

- [ ] ReFrame

- [ ] Spack

- [ ] Containers

- [ ] Nix

- [ ] Guix

  

---

  

## HPC Reproducibility Requirements

  

Study how to capture:

  

- [ ] Machine architecture

- [ ] Node topology

- [ ] CPU/GPU model

- [ ] Scheduler/job metadata

- [ ] Compiler version

- [ ] Compiler flags

- [ ] Runtime/library versions

- [ ] MPI configuration

- [ ] Environment variables

- [ ] Build configuration

- [ ] Source revision

- [ ] Patches

- [ ] Workload traces

- [ ] Random seeds

- [ ] Job scripts

- [ ] Scheduler policy

- [ ] Resource requests

- [ ] Timing/environment state

  

---

  

## Research Artifact Standards

  

Investigate:

  

- [ ] ACM artifact evaluation

- [ ] SC reproducibility expectations

- [ ] IEEE/ACM artifact badges

- [ ] FAIR principles

- [ ] Existing HPC reproducibility guidelines

  

### Deliverable

  

- [ ] **Experiment Layer Technology and Methods Review**

- [ ] HPC provenance requirements

- [ ] Proposed experiment data model

- [ ] Integration architecture

  

---

  

# 3.2 Define the Experiment Object

  

An experiment is more than a result file.

  

Potential structure:

  

```text

Experiment

├── motivation

├── research question

├── hypothesis

├── expected discriminating outcome

├── project-state snapshot

│

├── software provenance

├── machine provenance

├── environment

├── workloads

├── configuration

├── execution plan

│

├── runs

│ ├── run

│ ├── run

│ └── run

│

├── raw-result references

├── derived metrics

├── observations

├── interpretation

└── resulting project-state changes

```

  

---

  

# 3.3 Cross-Machine Experiment Reproducibility

  

Shiroe should understand differences such as:

  

```text

Experiment A ran on system X.

Experiment B ran on system Y.

  

Compiler, topology, runtime, or scheduler configuration differs.

```

  

The system should preserve enough information for agents and researchers to determine whether experiments are directly comparable.

  

---

  

# 3.4 Experiment Proposal

  

Given:

  

```text

Literature state

+

Project state

+

Previous experiments

```

  

Shiroe should help answer:

  

> What uncertainty should we reduce next?

  

A proposal should include:

  

```text

Experiment proposal E91

  

Research question:

...

  

Motivation:

...

  

Literature evidence:

...

  

Project evidence:

...

  

Competing hypotheses:

...

  

Manipulated variable:

...

  

Controlled variables:

...

  

Expected discriminating outcomes:

...

```

  

Human approval remains required before execution.

  

---

  

# 3.5 Result Ingestion

  

Pipeline:

  

```text

Raw results

↓

Analysis

↓

Observations

↓

Interpretation

↓

Hypothesis update

↓

Project-state update

↓

Literature comparison

↓

New uncertainty

```

  

---

  

# 3.6 Close the Full Shiroe Loop

  

```text

Literature

↓

Project

↓

Hypothesis

↓

Experiment

↓

Observation

↓

Project update

↓

Literature comparison

↓

Next question

```

  

---

  

# 3.7 Retrospective Experiment Validation

  

Select experiments with known historical outcomes.

  

Give Shiroe only knowledge available before the experiment.

  

Ask it to:

  

- [ ] Identify the important uncertainty

- [ ] Propose candidate experiments

- [ ] Rank the experiments

- [ ] Explain expected discriminating outcomes

  

Compare its recommendations against what researchers actually performed.

  

---

  

# 3.8 Prospective Experiment Study

  

Use Shiroe during active research.

  

Evaluate:

  

- [ ] Experiment usefulness

- [ ] Reproducibility completeness

- [ ] Provenance capture

- [ ] Forgotten experimental findings recovered

- [ ] Quality of experiment recommendations

- [ ] Quality of result-to-literature linkage

- [ ] Human trust

- [ ] Human maintenance burden

  

---

  

# Phase 3 Completion Gate

  

> Shiroe can connect literature, project hypotheses, experiment definitions, reproducible executions, observations, and resulting updates to project knowledge across heterogeneous systems.

  

---

  

# Cross-Cutting Compatibility and Robustness Testing

  

Maintain a permanent compatibility matrix.

  

| Dimension | Example Variants |

|---|---|

| LLM | OpenAI / Anthropic / local open-weight |

| Harness | Codex / Claude Code / MCP client |

| Machine | laptop / workstation / HPC |

| Project | Flux Fiction / other HPC project |

| Corpus | small curated / expanded |

| Connectivity | local / remote |

| Model context | small / large |

  

Not every Cartesian product needs to run on every commit.

  

Representative combinations should be tested periodically.

  

---

  

# Documentation Required After Every Phase

  

At the completion of each phase, write a technical report describing:

  

- [ ] What was surveyed

- [ ] What requirements were derived

- [ ] What architecture was selected

- [ ] Which alternatives were rejected

- [ ] Why those alternatives were rejected

- [ ] What was implemented

- [ ] How it was evaluated

- [ ] What failed

- [ ] What interfaces are considered stable

- [ ] What open questions remain

- [ ] What lessons should influence the next phase

  

These reports should serve both as internal design records and as source material for future publications.

  

---

  

# High-Level Roadmap

  

```text

PHASE 0 — CORE

0.1 Requirements

0.2 Distributed architecture survey

0.3 Server/API architecture

0.4 Identity + provenance model

0.5 CLI/MCP/client prototype

0.6 Distributed integration test

  

PHASE 1 — LITERATURE

1.1 Comprehensive review

1.2 Literature requirements

1.3 Architecture design

1.4 Ground-truth corpus

1.5 Baseline retrieval

1.6 Research-state extraction

1.7 Research-thread modeling

1.8 External discovery

1.9 Gap falsification

1.10 Validation

1.11 Multi-model test

1.12 Freeze literature interface

  

PHASE 2 — PROJECT

2.1 Comprehensive review

2.2 Project-state requirements

2.3 Architecture design

2.4 Project ingestion

2.5 Literature linkage

2.6 Persistent project memory

2.7 Agent interfaces

2.8 Retrospective project test

2.9 Prospective project test

2.10 Distributed/multi-agent validation

2.11 Freeze project interface

  

PHASE 3 — EXPERIMENT

3.1 Comprehensive review

3.2 HPC provenance requirements

3.3 Architecture design

3.4 Experiment representation

3.5 Execution/provenance capture

3.6 Result ingestion

3.7 Project-state updates

3.8 Experiment recommendation

3.9 Retrospective validation

3.10 Prospective experiment study

3.11 Cross-machine reproducibility

3.12 Full-system evaluation

```

  

---

  

# Long-Term Research Questions

  

Possible research questions emerging from Shiroe development:

  

## Literature Intelligence

  

- Can LLM systems reconstruct research questions across decades despite terminology changes?

- Can temporal research-state modeling identify dormant or abandoned research directions?

- Can adversarial retrieval reduce false claims of research gaps?

- Can research-question-centric retrieval outperform document-centric RAG for scientific synthesis?

  

## Project Intelligence

  

- Can explicit research-state representations improve the effectiveness of coding/research agents?

- Can persistent project memory reduce duplicated work and forgotten findings?

- How much project history is necessary to make good research decisions?

- Can Shiroe select relevant context more effectively than simply increasing model context size?

  

## Experiment Intelligence

  

- Can literature and project state be used to recommend experiments that reduce scientific uncertainty?

- Can agents reliably connect experimental observations back to claims in the literature?

- Can structured provenance improve reproducibility across heterogeneous HPC systems?

- Can historical experimental records be used to predict which experiments are most useful to perform next?

  

---

  

# Ultimate System Goal

  

Shiroe should eventually maintain a continuously evolving representation of:

  

```text

Scientific State

│

▼

Project State

│

▼

Experimental State

│

└──────────────► updates Project State

│

└──────────────► reinterprets Scientific State

```

  

The objective is not simply to store papers, projects, or experiments.

  

The objective is to make the evolving state of scientific knowledge:

  

- explicit,

- searchable,

- reproducible,

- attributable,

- shared across machines and agents,

- and useful for determining what research should happen next.