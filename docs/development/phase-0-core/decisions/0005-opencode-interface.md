# 0005 — Use OpenCode as the conversational and agent interface

- Date: 2026-10-13
- Phase / plan steps: 0 / 0.5, 0.6
- Status: Accepted direction; integration unverified
- Decision maker: user

## Context and decision

Integrate Shiroe with OpenCode, using custom agents and configurable models for research conversations. OpenCode provides the interaction/agent layer; persistent Shiroe knowledge belongs to Shiroe rather than an OpenCode session.

MCP is the proposed integration boundary, consistent with the plan. The exact agent prompts, tool set, permissions, and model configuration remain to be specified.

## Why and alternatives

The user prefers OpenCode because custom agents can work with different model providers. Building a Shiroe-owned chat application would add conversation, model, and UI maintenance. Hosted ChatGPT/Claude integrations remain optional future clients rather than the selected conversational interface.

The user is willing to modify OpenCode if necessary. The assistant recommends starting with upstream configuration and MCP and modifying it only when a specific capability is missing; no fork or patch is approved or required yet.

## Consequences and validation

Prototype one research agent against the shared service before adding specialization. Read/write approval behavior is a proposed workflow to test, not a selected final policy. Server-side authorization remains authoritative.

Check actual OpenCode version, OAuth login, tools, evidence retrieval, and write/retry behavior with both the lab models and permitted personal models. OpenCode supplements the original plan's Codex, Claude Code, generic MCP, and CLI/API tests; it does not silently replace them.

## Evidence

User, 2026-10-13:

> FOr the chatui, i think it would make sense to make it work with opencode. We can create custom agents that way and integrate whatever models we want.

> We can always modify opencode if we need.

Documentation checked in the conversation: [agents](https://opencode.ai/docs/agents/), [MCP](https://opencode.ai/docs/mcp-servers/), and [providers](https://opencode.ai/docs/providers/). Those documents establish candidate capabilities, not a tested Shiroe integration.
