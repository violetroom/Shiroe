# 0010 — Show whether a claim has been personally tested

- Date: 2026-10-13
- Phase / plan step: 0 / 0.2; applies across literature, projects, and experiments
- Status: Accepted requirement; evidence/status design proposed
- Decision maker: user

## Context and decision

Shiroe must expose whether the researcher or their project has personally tested a claim. This is distinct from a claim appearing in literature, having a citation, being reviewed by a person, or being judged plausible by an LLM.

The accepted requirement is a visible verification/validation indicator. The storage format and exact status vocabulary remain to be specified.

## Why and alternatives

A bare `verified=true` loses who checked what, under which conditions, and whether the result supported or challenged the claim. A claim can be personally tested and fail. Published support and personal testing are different evidence sources, and neither should imply universal correctness.

## Consequences and validation

The assistant proposes a concise displayed indicator backed by revision-linked validation records, rather than an unsupported boolean. Each completed test should identify the claim revision, tester/acting identity, date, method, test or experiment reference, resulting evidence, applicable hardware/environment context, and scope/conditions.

Candidate display states are **not tested by us**, **supported by our test**, **contradicted by our test**, and **inconclusive**. Preserve multiple or conflicting results instead of letting the latest flag erase them. These labels are proposals, not selected schema enums.

Personal testing must be scoped to the researcher/project and exact claim revision. Tests of an earlier revision remain visible but do not automatically validate a changed claim. Human review, literature support, LLM confidence, software regression checks, and empirical reproduction must remain distinguishable. A planned test does not count as a completed personal test. An automated run can supply evidence when its provenance and outcome are recorded; the indicator must not claim the researcher manually inspected it unless they did.

Proposed checks: preserve supported and contradicted outcomes on different systems, distinguish an untested claim from a tested failure, retain earlier-revision test evidence without transferring status silently, and avoid presenting a citation or model opinion as personal validation. No validation schema, summary rule, or UI has been implemented.

## Evidence

User, 2026-10-13:

> a verification/validation flag should be somewhere to see if we have tested the claim personally.

See [the vision's distinctions between evidence and interpretation](../../sources/Vision.md), [system/hardware provenance](0009-system-hardware-provenance.md), and [the architecture candidate](0007-core-architecture-candidate.md).
