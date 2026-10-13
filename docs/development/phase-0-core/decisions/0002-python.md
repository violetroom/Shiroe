# 0002 — Use Python

- Date: 2026-10-13
- Phase / plan step: 0 / 0.3
- Status: Accepted
- Decision maker: user

## Context and decision

Use Python as Shiroe's implementation language. This selects the language, not a framework, dependency version, ORM, package manager, or migration tool. Clients continue to use documented network interfaces; research code and model providers remain independently selectable.

## Why and alternatives

The user has the most familiarity with Python. The assistant also favored it for evolving research representations and future scientific-document integrations. TypeScript/Fastify was considered for a UI-heavy application; Rust/Axum for compiled distribution and stronger compile-time guarantees. Neither supplied a reason to outweigh the maintainer's Python familiarity.

## Consequences and validation

FastAPI/Pydantic and the official Python MCP SDK are candidates from the survey, not accepted framework choices. Select a maintainable, pinned stack and validate shared authorization, API/MCP mounting, migrations, and client behavior before implementation claims.

## Evidence

User, 2026-10-13:

> I think Python probably makes the most sense here for the language and I have the most familiarity with it so lets go with that.

See the [access report's tooling shortlist](../planning/Shiroe_Phase_0_Access_and_Deployment.md) and [core architecture candidate](0007-core-architecture-candidate.md).
