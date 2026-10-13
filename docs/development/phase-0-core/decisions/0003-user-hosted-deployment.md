# 0003 — Support configurable user-hosted deployment

- Date: 2026-10-13
- Phase / plan steps: 0 / 0.3, 0.5, 0.6
- Status: Accepted direction; initial target unverified
- Decision maker: user

## Context and decision

Each end user will set up their own Shiroe server. Deployment location must be configurable, with no dependence on a particular home address, cloud provider, or institution.

The initial personal target is the user's Debian/OpenMediaVault home server, administrative SSH target `HOME_SSH_USER@192.0.2.10`. The user reports Compose support, several existing services, and sufficient available storage. These are user-provided deployment facts, not independently inspected hardware, service availability, or permission evidence. The SSH target is not the client-facing Shiroe URL and does not select the application's runtime identity.

Oracle Cloud remains a conditional alternative. The user has not selected a cloud migration and intends to verify institutional data-sharing rules.

## Why and alternatives

User rationale: reuse existing home infrastructure and storage while avoiding a possible institutional issue with cloud storage. The product must remain usable by others hosting their own instances.

Assistant analysis: clients reach the Shiroe API/MCP endpoint, not PostgreSQL. Moving only the database to Oracle leaves the home application as the client network destination and adds an application/database network dependency. Moving the application and database together may simplify reachability if the cloud endpoint is permitted. A relay is another possible route but introduces an extra dependency and data-transit question. These are options, not approved deployment changes.

## Consequences and validation

Compose is available for this target and is a proposed portable deployment mechanism. Configure public URL, database connection, OAuth issuer, and storage paths per deployment; exact configuration keys are not specified yet. Preserve existing OMV services when deployment work is authorized.

Still open: actual HPC site, permitted egress/proxy/forwarding route, home HTTPS ingress and DNS, residential address stability, institutional permission for offsite research state, and backup/recovery requirements. The data question includes personal-server storage, cloud storage, relays, and research-derived metadata, not just raw datasets. No server connection or live probe has occurred.

## Evidence

User, 2026-10-13:

> I think it should be configurable by the end user because each user will setup their own server.

> For my implementation, I will host it locally on [SSH target redacted]. That is my home server.

The user stated that cloud data-sharing permission would need verification (paraphrased to omit personal context).

See the [access/deployment report](../planning/Shiroe_Phase_0_Access_and_Deployment.md) and [model policy](0006-model-policy.md). Institutional rules and target-site network policy have not been supplied.

## Subsequent clarification — 2026-10-13

The user identified LLNL LC, initially Tuolumne, confirmed that local database storage is acceptable, and reaffirmed the home-server preference. [0008](0008-lc-home-server-target.md) records these refinements. The earlier uncertainty above is retained as history; the network route remains untested.

Privacy note: personal addresses, accounts, node identifiers, paths, precise times, and server fingerprints have been replaced or omitted where present. Placeholders preserve the reported test outcome; this document is not an unredacted transcript.
