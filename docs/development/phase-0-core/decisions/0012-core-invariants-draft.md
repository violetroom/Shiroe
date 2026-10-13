# 0012 — Draft the core identity, provenance, and write contracts

- Date: 2026-10-13
- Phase / plan step: 0 / 0.2
- Status: Proposed specification; requirements traced to accepted plan/user decisions
- Decision maker: assistant draft under the user's instruction to continue to the next step
- Refines: proposals in [0007](0007-core-architecture-candidate.md), [0009](0009-system-hardware-provenance.md), [0010](0010-personal-claim-validation.md), and [0011](0011-client-traffic-and-artifact-placement.md); does not supersede accepted requirements

## Context and proposal

Use [Core invariants v0](../planning/core-invariants-v0.md) as the reviewable step 0.2 deliverable. It defines stable object identity and immutable revisions, a narrow record envelope, distinguishable knowledge categories, evidence/activity attribution, execution-context revisions, and personal-testing summaries backed by scoped validation evidence.

It also specifies common authorized operations across clients, stale-write preconditions, atomic commits and retry receipts, independently identified external artifacts, explicit schema evolution, recovery boundaries, and bounded retrieval. Names/enums and schema layouts remain proposals; a draft does not freeze the later scientific ontology or select the Python framework.

## Why and alternatives

These contracts make the source plan's invariants testable before selecting storage and API details. In-place evidence edits lose historical meaning; last-write-wins updates lose concurrent work; a free-standing verified flag hides tester, conditions, failures, and contradictions. Bare file paths cannot identify reproducible evidence. The draft uses explicit revisions and evidence links to address those problems without requiring a full event-sourced system, graph database, or general offline synchronization engine.

## Consequences and validation

Architecture and prototypes should be evaluated against the draft's synthetic scenario matrix, then refine the contracts from actual findings. Personal testing applies to a named researcher/project scope and exact claim revision; support, contradiction, and mixed outcomes do not imply universal correctness. Run hardware and submitting-client hardware remain separate. Traffic verification remains required later, with numeric limits provisional.

No service/schema implementation or contract test has run. Remaining implementation choices include identity encoding, permission scopes, version policy, receipt retention, and backup/recovery objectives. The user has authorized drafting the next plan step, not independently accepted every design detail. Preserve this status until decisions are explicitly selected.

## Evidence

- User, 2026-10-13: “Alright let's continue to the next step.”
- [Source plan, step 0.2 and core principles](<../../sources/Shiroe Development Plan.md>).
- [Source vision](../../sources/Vision.md).
- Accepted requirements and pending designs in [0009](0009-system-hardware-provenance.md), [0010](0010-personal-claim-validation.md), and [0011](0011-client-traffic-and-artifact-placement.md).
- [Research synthesis](<../planning/Shiroe Core Architecture Survey.md>) as historical design evidence, not implementation validation.
