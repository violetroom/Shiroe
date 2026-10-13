# 0007 — Candidate core architecture from the survey

- Date: 2026-10-13
- Phase / plan steps: 0 / 0.1–0.3
- Status: Proposed
- Decision maker: research reports and assistant proposal; not separately accepted by the user

## Context and proposal

Use one Shiroe application with PostgreSQL owning canonical research state; relational structure for identities, revisions, relationships, and provenance; JSONB for evolving payloads; and PostgreSQL full-text search as an initial rebuildable projection. Store references to externally owned artifacts. HTTP API and MCP share validation, authorization, and application operations; CLI/library use the API.

Preserve immutable evidence revisions, distinguish observation/human assertion/derived result/model interpretation/hypothesis, prevent stale overwrites, and use operation identities/receipts for safe retries. The exact schema, vocabulary, endpoint shapes, performance goals, and concurrency contract are not frozen.

## Why and alternatives

This follows the [plan's initial PostgreSQL preference](<../../sources/Shiroe Development Plan.md>) and the survey's recurring separation of canonical metadata, artifacts, and derived search. Shiroe needs a small custom semantic layer because reviewed trackers, repositories, and agent memories do not establish its complete scientific-state requirements.

The reports recommend deferring graph/vector databases, dedicated search clusters, queues, gateways, and large orchestration stacks until evidence justifies them. MLflow, Git, DataLad/DVC, and agent memory systems are precedents or later integrations rather than proposed replacements for Shiroe's store. These are research dispositions, not blanket user-approved bans.

## Consequences and validation

Specify the core invariants in step 0.2, then choose a concrete Python stack and prototype the shared-state behavior. Verify epistemic/provenance fidelity, conflicting writes and duplicate retries, permissions across transports, migrations, artifact drift, restart/restore, and actual client/machine access.

The accepted language, deployment, authentication, and interface directions are in records [0002](0002-python.md), [0003](0003-user-hosted-deployment.md), [0004](0004-oauth.md), and [0005](0005-opencode-interface.md). They do not imply acceptance of every schema or tool proposal in the reports. No benchmark threshold or dependency version in the reports is an established Shiroe requirement.

## Evidence

- [Prior-art/persistence survey](<../planning/Shiroe Core Architecture Survey_ Phase 0.pdf>).
- [Access/deployment report](../planning/Shiroe_Phase_0_Access_and_Deployment.md).
- [Combined synthesis](<../planning/Shiroe Core Architecture Survey.md>).
- [Vision](../../sources/Vision.md) and [development plan](<../../sources/Shiroe Development Plan.md>).

The user requested an explanation and then explicitly selected several directions. No independent acceptance of the complete proposed architecture, live compatibility result, or Phase 0 completion claim appears in the conversation.
