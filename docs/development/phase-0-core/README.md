# Phase 0 — Core and distributed knowledge infrastructure

Status: in progress. Architecture survey reports have been supplied and reviewed; step 0.2 has a reviewable core-invariant draft. Core service implementation and live service validation have not started. The user-run preliminary SSH-port and HTTPS probes from Tuolumne passed; the distributed Shiroe completion gate remains open.

## Purpose

Define how agents and clients on different machines interact with the same persistent research state. Establish identity, provenance, evolving schemas, shared interfaces, authentication, and recovery before building the literature layer.

## Plan and progress

| Detailed plan step | Scope | Current state |
|---|---|---|
| 0.1 Survey Existing Architectures | Research existing state, provenance, storage, search, and access patterns | Reports available and reviewed; candidate architecture remains provisional |
| 0.2 Define Core Invariants | Specify stable IDs, knowledge categories, provenance, interface and recovery guarantees | Draft available with hardware context, personal-testing summary rules, and future contract scenarios; proposed, unimplemented |
| 0.3 Initial Server Architecture | Choose boundaries, persistence, schema evolution, and implementation stack | Python selected; framework and architecture details open |
| 0.4 Define Git's Role | Define authoritative source/artifact boundaries and indexing references | Plan and survey guidance available; contract pending |
| 0.5 Prototype Access Interfaces | CLI, API, MCP, client library, OAuth, local development, and deployment | OAuth and OpenCode directions selected; no prototype; add traffic instrumentation and enforce selected limits |
| 0.6 Distributed Integration Test | Demonstrate shared persistent state across machines and required clients | Gate not run; SSH-port and HTTPS probes passed; authenticated integration and representative LC traffic/proxy checks required |

## Records

- [Planning reports and research history](planning/README.md).
- [Core invariants v0 — step 0.2 draft](planning/core-invariants-v0.md), with [decision record 0012](decisions/0012-core-invariants-draft.md).
- [LC/Tuolumne connectivity notes](planning/lc-connectivity-notes.md).
- [User-run Tuolumne-to-home SSH-port result](validation/2026-10-13-tuolumne-home-ssh.md).
- [Temporary HTTPS fixture and setup](../../../tools/https-probe/README.md), with [local validation](validation/2026-10-13-https-fixture-local.md).
- [Initial laptop HTTPS success and LC custom-certificate failure](validation/2026-10-13-home-https-lc-certificate-failure.md).
- [User-run Tuolumne-to-home HTTPS success using default trust](validation/2026-10-13-tuolumne-home-https.md).
- [Proposed client traffic limits and artifact placement](decisions/0011-client-traffic-and-artifact-placement.md); proxy load must be measured in the prototype.
- [Phase decisions](decisions/README.md) and [global ledger](../DECISIONS.md).
- [Authoritative plan snapshot](<../sources/Shiroe Development Plan.md>).

## Completion gate

> Multiple clients on different machines can access the same persistent Shiroe knowledge store through stable interfaces.

The plan names laptop, workstation, HPC login node, and remote server; clients include Codex, Claude Code, a generic MCP client, and CLI/API. OpenCode is an additional selected interface; its selection does not silently remove the original compatibility targets.

## Work remaining

Review/refine the core-invariant draft, proceed to step 0.3 architecture and concrete storage/API choices, select and test the Python/OAuth stack, and build a small shared-state prototype. Record actual conflict/retry, provenance, schema evolution, restart/restore, and client/machine results before claiming this phase complete.

Before completing step 0.6, execute the [required traffic and artifact-placement checks](decisions/0011-client-traffic-and-artifact-placement.md#required-later-verification--user-confirmed-2026-10-13). Measure representative use, verify safeguards locally, and record a bounded LC pilot's results. Revisit these checks when later phases introduce literature or experiment workflows; the health probe does not satisfy them.
