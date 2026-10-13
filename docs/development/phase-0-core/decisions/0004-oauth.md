# 0004 — Start with OAuth authentication

- Date: 2026-10-13
- Phase / plan step: 0 / 0.5
- Status: Accepted; provider and integration details open
- Decision maker: user

## Context and decision

Start with OAuth for authenticated Shiroe access. Select an issuer and compatible client flow during the prototype; no identity provider has been selected. This replaces the research synthesis's proposed scoped-token pilot as the selected authentication direction.

## Why and alternatives

The user selected OAuth for OpenAI compatibility. The assistant clarified that protected hosted ChatGPT MCP integration uses the documented MCP OAuth contract; merely using an OpenAI model does not impose that requirement on every client. OpenCode also documents remote MCP OAuth support, making OAuth useful beyond one model vendor.

Static scoped tokens were considered as a simpler local-client pilot, but were not the user's selection. Browser sessions would be an additional mechanism if a Shiroe-owned UI were later built. VPN/SSH reachability does not define application identity or permissions.

## Consequences and validation

An established, configurable issuer is the assistant's proposed implementation approach; institution-provided or self-hosted identity remain options. No custom authorization server is selected. Shiroe must validate caller identity and enforce its own object/project permissions independently of client tool approvals.

Test issuer discovery, client registration, token audience/expiry/scopes, refresh, and login on the actual OpenCode/Codex clients and headless HPC environment. Capture the supported protocol and package versions rather than treating rolling documentation as tested behavior.

## Evidence

User, 2026-10-13:

> For authentication, lets start with oauth if oai wants us to have it.

Documentation checked in the conversation: [OpenAI MCP authentication](https://developers.openai.com/plugins/build/auth) and [OpenCode MCP OAuth](https://opencode.ai/docs/mcp-servers/). No OAuth flow was run. See [planning evidence](../planning/README.md) for the earlier proposal.
