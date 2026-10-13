# Decision ledger

Last updated: 2026-10-13. Accepted means the user selected the direction; it does not mean it has been implemented or tested.

| ID | Date | Phase | Decision | Status |
|---|---|---|---|---|
| [0001](phase-0-core/decisions/0001-development-records.md) | 2026-10-13 | 0 / all phases | Keep phase documentation and a durable decision ledger | Accepted |
| [0002](phase-0-core/decisions/0002-python.md) | 2026-10-13 | 0 | Use Python as the implementation language | Accepted |
| [0003](phase-0-core/decisions/0003-user-hosted-deployment.md) | 2026-10-13 | 0 | Configurable user-hosted deployment; home server is the initial personal target | Accepted; SSH and HTTPS probes passed, Shiroe service untested |
| [0004](phase-0-core/decisions/0004-oauth.md) | 2026-10-13 | 0 | Start with OAuth authentication | Accepted; provider open |
| [0005](phase-0-core/decisions/0005-opencode-interface.md) | 2026-10-13 | 0 | Use OpenCode for the conversational/agent interface | Accepted; integration unverified |
| [0006](phase-0-core/decisions/0006-model-policy.md) | 2026-10-13 | 0 / all phases | Respect environment-specific model restrictions | Accepted constraint |
| [0007](phase-0-core/decisions/0007-core-architecture-candidate.md) | 2026-10-13 | 0 | One service with PostgreSQL, JSONB, initial full-text search, and shared API/MCP logic | Proposed; follows plan preference and survey |
| [0008](phase-0-core/decisions/0008-lc-home-server-target.md) | 2026-10-13 | 0 | Target LLNL LC, initially Tuolumne; retain home-hosted database if connectivity permits | Accepted; SSH and LC HTTPS probes passed; Shiroe integration untested |
| [0009](phase-0-core/decisions/0009-system-hardware-provenance.md) | 2026-10-13 | 0 / all phases | Preserve system and hardware context in provenance | Accepted requirement; representation pending |
| [0010](phase-0-core/decisions/0010-personal-claim-validation.md) | 2026-10-13 | 0 / all phases | Show whether a claim has been personally tested | Accepted requirement; evidence/status design proposed |
| [0011](phase-0-core/decisions/0011-client-traffic-and-artifact-placement.md) | 2026-10-13 | 0 | Bound client traffic; keep raw HPC artifacts on LC and exchange selected research state | Design proposed; later traffic/proxy verification required by user, pending |
| [0012](phase-0-core/decisions/0012-core-invariants-draft.md) | 2026-10-13 | 0 | Core invariant draft: identities, revisions, provenance, validation evidence, writes, artifacts, evolution, and recovery | Proposed specification; reviewable draft, unimplemented |
| [0013](phase-0-core/decisions/0013-private-information-in-version-control.md) | 2026-10-13 | All | Keep personal deployment details and identifying metadata out of commits | Accepted; shared evidence sanitized, private originals ignored |

## Status meanings

- **Accepted:** explicitly chosen by the user, including authoritative requirements from the user-authored plan.
- **Proposed:** a candidate from research or an assistant, awaiting selection or refinement.
- **Rejected:** considered and declined; retain the rationale.
- **Superseded:** replaced by a linked newer record; retain historical reasoning.

## Open decisions and checks

| Question | Current position | Related record |
|---|---|---|
| Which Python framework, MCP SDK version, and database tooling? | FastAPI/Pydantic and the official MCP SDK are candidates; no dependency stack is selected or tested | [0002](phase-0-core/decisions/0002-python.md), [0007](phase-0-core/decisions/0007-core-architecture-candidate.md) |
| Home server or Oracle for the live deployment? | User wants to retain the home database and make that deployment work if possible. Oracle is not selected; moving only the DB would not move the client-facing endpoint | [0003](phase-0-core/decisions/0003-user-hosted-deployment.md), [0008](phase-0-core/decisions/0008-lc-home-server-target.md) |
| What institutional data may leave institutional systems? | User confirms local database storage is acceptable. Applicable transfer procedures, cloud/relay permission, and external inference scope remain distinct from that storage confirmation | [0008](phase-0-core/decisions/0008-lc-home-server-target.md), [0006](phase-0-core/decisions/0006-model-policy.md) |
| Which HPC system and permitted network route? | LLNL LC, initially Tuolumne. SSH-port probe passed. HTTPS probe from LC_LOGIN_NODE_B passed using default trust after the custom-certificate attempt failed. Exact proxy/certificate path not identified; OAuth and Shiroe access untested | [0008](phase-0-core/decisions/0008-lc-home-server-target.md), [SSH result](phase-0-core/validation/2026-10-13-tuolumne-home-ssh.md), [HTTPS result](phase-0-core/validation/2026-10-13-tuolumne-home-https.md) |
| Which OAuth issuer and client registration flow? | Prefer an established provider as a candidate; validate MCP discovery, tokens, refresh, and headless login with actual clients | [0004](phase-0-core/decisions/0004-oauth.md) |
| Can the lab model endpoints drive OpenCode tools reliably? | API compatibility and tool behavior require testing; no model endpoint or OpenCode version has been tested | [0005](phase-0-core/decisions/0005-opencode-interface.md), [0006](phase-0-core/decisions/0006-model-policy.md) |
| What are the exact identity, revision, provenance, and write contracts? | Step 0.2 draft defines immutable revisions, common authorized operations, stale-write checks, atomic commits, and retry receipts; concrete encodings/schemas remain open | [0012](phase-0-core/decisions/0012-core-invariants-draft.md), [specification](phase-0-core/planning/core-invariants-v0.md) |
| How are hardware provenance and personal validation represented? | Requirements accepted; draft proposes immutable run contexts distinct from submitting clients and scoped revision-linked tests with explicit mixed outcomes. Fields and summary vocabulary remain proposals | [0009](phase-0-core/decisions/0009-system-hardware-provenance.md), [0010](phase-0-core/decisions/0010-personal-claim-validation.md), [0012](phase-0-core/decisions/0012-core-invariants-draft.md) |
| How much client traffic and where do artifacts live? | User requires later verification: instrument in 0.5, measure a bounded LC pilot in 0.6, and revisit during literature/experiment development. Verify byte volume, bursts, retries, placement, and enforced limits. Estimates and limits remain proposals, not LC allowances | [0011](phase-0-core/decisions/0011-client-traffic-and-artifact-placement.md#required-later-verification--user-confirmed-2026-10-13) |

A user-run live TCP/SSH-banner probe passed on 2026-10-13; see [the scoped result](phase-0-core/validation/2026-10-13-tuolumne-home-ssh.md). A temporary HTTPS fixture passed [local checks](phase-0-core/validation/2026-10-13-https-fixture-local.md). After [laptop HTTPS success and an LC custom-certificate failure](phase-0-core/validation/2026-10-13-home-https-lc-certificate-failure.md), [LC HTTPS passed using default trust](phase-0-core/validation/2026-10-13-tuolumne-home-https.md). No live Shiroe service, OAuth integration, or agent compatibility test has been performed. Phase 0's completion gate remains open.

Privacy note: personal addresses, accounts, node identifiers, paths, precise times, and server fingerprints have been replaced or omitted where present. Placeholders preserve the reported test outcome; this document is not an unredacted transcript.
