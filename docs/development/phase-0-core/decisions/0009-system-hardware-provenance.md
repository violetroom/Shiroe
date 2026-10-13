# 0009 — Preserve system and hardware context in provenance

- Date: 2026-10-13
- Phase / plan steps: 0 / 0.2; later experiment capture in Phase 3
- Status: Accepted requirement; representation pending
- Decision maker: user

## Context and decision

System and hardware context must be representable in provenance. Measurements and conclusions from execution must remain attributable to the environment that produced them, so later readers can judge reproducibility and comparability.

## Why and alternatives

A system name alone cannot establish what hardware, allocation, software, or configuration produced a result. Hardware and resource differences can explain changes in performance or behavior. The source plan already includes machine provenance in Phase 3; the user explicitly wants this requirement included in the shared provenance design now.

## Consequences and validation

Proposed 0.2 representation: link an execution or validation activity to a versioned execution-context record. Record the actual experiment system/node context separately from the client/login machine that submits the metadata. Candidate fields include system identity, node role, CPU/APU/GPU model, memory, interconnect/topology, resource allocation and job ID, OS/software/build versions, and relevant configuration. These are candidates, not a finalized mandatory field list for every knowledge object.

Retain how and when context was collected and whether it was measured, reported by the user, or taken from documentation. Unknown details remain explicit; do not infer actual run hardware solely from a published platform description. References must preserve the context used for an earlier result after configuration or hardware changes.

Human notes and literature assertions need not manufacture an execution environment. An inference activity may have a different environment from the experiment it interprets. Full automatic HPC capture belongs to later experiment work; Phase 0 establishes that the representation and links are possible.

Proposed check: attach two observations from different execution contexts and retrieve the exact context for each, even after a newer context is recorded. No provenance schema or collector has been implemented.

## Evidence

User, 2026-10-13:

> system/hardware should be in the provenance information.

See [the development plan's machine-provenance and HPC reproducibility requirements](<../../sources/Shiroe Development Plan.md>) and [the core architecture candidate](0007-core-architecture-candidate.md).
