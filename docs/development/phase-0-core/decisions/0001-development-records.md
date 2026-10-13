# 0001 — Keep phase documentation and a decision ledger

- Date: 2026-10-13
- Phase: 0; applies to all development phases
- Status: Accepted
- Decision maker: user

## Context and decision

Keep a repository development directory with an index for every phase, planning artifacts, and writeups for important decisions. Use a global ledger linking numbered phase-local records. Future agents must be able to recover rationale without relying on this conversation.

The user explicitly requested the recordkeeping approach; `docs/development/`, Markdown indices, and the record format are implementation choices made to fulfill that request.

## Why and alternatives

Conversation-only knowledge is difficult to retrieve and can disappear from future agent context. A single mutable summary would lose alternatives and the reasons for changes. Plain Markdown and original PDF/Markdown artifacts are sufficient; a documentation application or generated site is unnecessary for the current task.

## Consequences and validation

Significant future decisions must include rationale, alternatives, provenance, status, and checks. Preserve superseded records and update the ledger and phase index. Documentation does not establish that a proposed system works.

## Evidence

User, 2026-10-13:

> The idea is that future agents will be able to understand how we got here and I can look back on why we made a decision if its ever relevant.

The [development plan](<../../sources/Shiroe Development Plan.md>) also requires reports describing decisions, rejected alternatives, implementation, evaluation, failures, stable interfaces, and open questions after each phase.
