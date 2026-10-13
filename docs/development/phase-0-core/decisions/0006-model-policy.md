# 0006 — Respect environment-specific model restrictions

- Date: 2026-10-13
- Phase: 0; applies to all layers
- Status: Accepted constraint
- Decision maker: user

## Context and decision

On lab machines, use the institution-hosted models required by the user's environment. On other machines, the user can use self-hosted or external models, subject to restrictions on the data being processed. Model endpoints and credentials belong in environment-specific configuration.

## Why and alternatives

The user states that lab models are mandatory on lab machines while other environments offer model flexibility. One globally hardcoded provider would fail this requirement and the plan's multi-model intent. The same persistent research state should remain usable from permitted client/model combinations.

## Consequences and validation

The assistant proposes explicit OpenCode provider allowlists and permitted routing for auxiliary model calls as well as the main agent. These configurations support the workflow but do not establish institutional policy or prevent every possible data transfer.

Phase 0 storage/retrieval can be independent of model credentials. Future server-side extraction or inference needs its own permitted model configuration; an OpenCode lab profile does not automatically control jobs running on the home server. Data restrictions continue to matter when institutional evidence is accessed from a personal machine.

Still needed: lab endpoint/protocol details, available model IDs, tool-calling behavior, effective configuration, and institutional permission for offsite storage and inference. No provider was called or tested.

## Evidence

User, 2026-10-13:

> On the lab machines, I have to use their hosted models but I can use self hosted/external models on other machines.

See [OpenCode provider configuration](https://opencode.ai/docs/config/), [providers](https://opencode.ai/docs/providers/), [deployment record](0003-user-hosted-deployment.md), and [the source plan's compatibility requirements](<../../sources/Shiroe Development Plan.md>).

## Subsequent clarification — 2026-10-13

The user confirmed local database storage is acceptable in [0008](0008-lc-home-server-target.md). This resolves that storage question for the intended deployment; permissions for external inference, cloud relays, and particular outgoing data remain separate. The requirement to use lab-hosted models on lab machines is unchanged.
