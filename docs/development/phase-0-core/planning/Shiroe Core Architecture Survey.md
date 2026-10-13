# Shiroe Core Architecture Survey

**Development plan deliverable:** §0.1 — Survey Existing Architectures  
**Date:** 2026-10-13  
**Status:** Decision-support synthesis; **provisional direction, not an implementation approval or Phase 0 completion claim**

## 1. Decision in brief

**Provisional direction:** Build a **single deployable Shiroe service** owning a **PostgreSQL canonical knowledge store**, with constrained identity/revision/provenance tables and **JSONB for evolving type-specific payloads**. Keep large artifacts in their originating systems and store versioned, verifiable references. Begin with PostgreSQL full-text search as a **rebuildable projection**. Expose a **versioned authenticated HTTP API**; have MCP, CLI, client library, and a small Shiroe-owned chat backend use the **same authorized application commands**. Offer remote MCP over Streamable HTTP, with a local stdio adapter only when a client/site requires it. Start with one central persistent deployment and a separate local development mode.

This is the smallest coherent architecture that could meet the plan's distributed completion gate, **not evidence that it already does**. The server language, auth provider, ingress, precise envelopes, API shapes, and HPC connectivity remain to be selected or validated in §§0.2–0.6. **Do not freeze the scientific ontology in Phase 0.**

## 2. Scope and requirements traceability

The [vision](../../sources/Vision.md) and [development plan](../../sources/Shiroe%20Development%20Plan.md) are the controlling requirements; both research reports are evidence and proposals. Shiroe is a connective layer for *literature → projects → experiments → projects → literature*, not a replacement for document libraries, trackers, Git, or agent harnesses.

| Authoritative requirement | Phase 0 architectural consequence | Validation / next section |
|---|---|---|
| Durable knowledge independent of sessions; one store across machines and LLMs | Central canonical store behind a documented service; no agent-local source of truth | §0.5 interfaces; §0.6 cross-machine read/write |
| Stable object identity and inspectable provenance | Stable IDs, immutable revisions, evidence references, actor/activity metadata | §0.2 invariant fixtures; §0.6 lineage tests |
| Distinguish human-authored, observed, derived, inferred, and speculative knowledge | Explicit epistemic category distinct from the identity/provenance mechanism | §0.2 distinguishability tests |
| External raw artifacts allowed; Git important but not the Shiroe database | Artifact URI + version/digest/reference metadata; Git remains source/document/config history | §0.4 Git contract; artifact relocation/mutation checks |
| Evolving schemas/ontologies | Narrow stable envelope, versioned JSON payloads, migrations and old-client compatibility | §§0.2–0.3 schema evolution tests |
| Documented heterogeneous interfaces and deployability | API + MCP + CLI + library + minimal auth; local dev and central server | §0.5 contract tests; §0.6 distributed gate |
| Laptop, workstation, remote server, HPC login node; Codex, Claude Code, generic MCP, CLI/API | Test the *actual* versions, connection origins, policies, credentials, and permissions individually | §0.6 compatibility matrix and site tests |

**Not in §0.1's selection scope:** final literature ontology or extraction tools, scholarly retrieval ranking, project decision workflows, experiment execution/metadata ontology, production-scale search clusters, multi-tenant high availability, or offline multi-master synchronization. Those are later-phase decisions unless a Phase 0 prototype exposes a blocking requirement.

## 3. Architectural precedents worth adopting

Evidence labels: **[D]** documentation/specification or first-party source identified in the reports; **[R]** reported result or vendor/project claim, not reproduced for Shiroe; **[P]** proposed design judgment; **[T]** requires Shiroe prototype testing. A report's documented support is *not* an end-to-end Shiroe verification.

| Precedent | Relevant supported behavior | Adopt / limit |
|---|---|---|
| **[Dataverse](https://guides.dataverse.org/en/6.7.1/installation/prep.html), [Invenio Records](https://github.com/inveniosoftware/invenio-records)** | [D] Separation of structured records, retrieval and artifacts; Invenio UUIDs, revision history and JSON-schema validation | [P] Stable record envelope + revisions; **do not** import repository/publication ontology or full stack |
| **[MLflow tracking server](https://mlflow.org/docs/latest/self-hosting/architecture/tracking-server/)** | [D] Remote client/server, transactional tracking metadata, independently located [artifacts](https://www.mlflow.org/docs/latest/self-hosting/architecture/artifact-store/) | [P] Metadata/artifact separation and remote clients; integrate later for experiments, not Shiroe's canonical scientific state |
| **[W3C PROV](https://www.w3.org/TR/prov-dm/)** | [D] Entities, activities, agents, use/generation/derivation/attribution | [P] Small provenance-inspired schema; PROV alone **does not** define observed vs inferred vs proposed |
| **[Wikibase](https://doc.wikimedia.org/Wikibase/master/php/docs_topics_json.html)** | [D] Statements with references/qualifiers and revisions | [P] Borrow attributable assertion/relationship pattern, not MediaWiki/Wikibase infrastructure |
| **[Letta](https://docs.letta.com/concepts/stateful-agents), [Mem0](https://github.com/mem0ai/mem0)** | [D] Persistent agent memory, shared addressable state or hybrid retrieval; [R] Mem0 benchmark figures describe its managed platform, not necessarily its OSS SDK | [P] Borrow shared-state and retrieval ideas; avoid treating generated memories as undifferentiated scientific truth |
| **[PostgreSQL constraints](https://www.postgresql.org/docs/18/ddl-constraints.html), [JSONB](https://www.postgresql.org/docs/18/datatype-json.html), [FTS](https://www.postgresql.org/docs/18/textsearch.html)** | [D] Relational integrity, transactions, flexible JSON, indexed lexical search | [P] Single initial canonical storage system; **[T]** retrieval quality, latency, migrations and write semantics under Shiroe workload |
| **[DataLad](https://docs.datalad.org/en/latest/basics.html), [DVC](https://doc.dvc.org/user-guide/data-management/remote-storage)** | [D] Version/content-aware datasets and external storage | [P] Preserve externally owned artifact identity and content/version evidence, without copying all bytes |
| **[MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)** | [D] Tools/resources and current Streamable HTTP transport; client implementations differ | [P] Adapter above Shiroe commands, never independent storage or authorization; **[T]** each actual client |

**Benchmark discipline:** No comparative Shiroe throughput, retrieval accuracy, MCP compatibility, or concurrency measurements are supplied. Neither Mem0's published platform benchmark nor hypothetical database throughput establishes suitability for Shiroe. The architecture survey's suggested **≥5 percentage-point Recall@K / ≥10% relative nDCG** trigger for vectors and **200 ms P95** target are *illustrative acceptance thresholds*, not measured performance or database limits; calibrate them before running tests.

## 4. Smallest plausible Phase 0 tooling shortlist

| Boundary | First candidate | Genuine alternative / condition |
|---|---|---|
| Canonical persistence | **PostgreSQL**, relational IDs/edges/revisions/activities, JSONB payload | No equal-priority second store unless prototype falsifies assumptions |
| Initial retrieval | PostgreSQL **tsvector/GIN** lexical projection | **pgvector** only if representative semantic retrieval improves quality enough; specialized OpenSearch later if capability/performance demands |
| Backend + HTTP/MCP | **One app**, sharing command/validation/auth logic; choose **FastAPI + official Python MCP SDK**, **Fastify + official TypeScript MCP SDK**, or **Axum + rmcp** | **Decision pending** maintainers, hosting and tests; do not treat a language-specific framework as selected by the persistence survey |
| Agent access | Streamable HTTP `/mcp` plus limited read/write tools; optional local **stdio-to-HTTP** shim | Older transport only if required by a pinned client; no standing MCP gateway |
| Human/script access | Versioned JSON HTTP API, OpenAPI contract, **one** thin initial-language library and CLI | Code-generation optional; CLI must handle auth, retries and conflict errors |
| Identity/auth | TLS + scoped server-issued pilot tokens; server-enforced object permissions; browser session for Shiroe UI | Existing institutional OAuth/OIDC if policy or chosen hosted product requires it; verify MCP-specific discovery/audiences |
| Deployment | One supervised server process + PostgreSQL, backups, approved TLS ingress; local ephemeral/test database | Compose or native supervision based on host; no default Kubernetes/Redis/broker |
| Chat surface | Small **Shiroe-owned** browser UI invoking backend commands | Hosted ChatGPT or Claude browser connectors are *separate optional integrations*, not automatically supported by local agent MCP settings |

### Client reality check

- **Codex CLI/IDE [D/T]:** documented stdio and Streamable HTTP MCP, with bearer/OAuth configuration; actual executable, host location (including remote editor host), MCP resources, write approvals and token storage **must be tested**. [Codex documentation](https://learn.chatgpt.com/docs/extend/mcp?surface=cli).
- **Claude Code [D/T]:** documented stdio/HTTP MCP, credentials and permission-controlled tools; actual runtime, negotiated revision and headless HPC credentials **must be tested**. [Claude Code MCP](https://code.claude.com/docs/en/mcp).
- **Generic MCP [D/T]:** pin the [official Python SDK](https://github.com/modelcontextprotocol/python-sdk) or [TypeScript SDK](https://ts.sdk.modelcontextprotocol.io/v2/) plus [MCP Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector); do not claim arbitrary client parity.
- **CLI/API [P/T]:** Shiroe-owned, so support is implementable but not present today; validate packaging, JSON output, proxy/CA behavior and durable operation IDs.
- **Hosted/browser [D/T/conditional]:** provider cloud requires provider-reachable ingress or a supported tunnel; local VPN/localhost visibility is insufficient. ChatGPT, Claude remote connectors, and hosted APIs have product-specific OAuth, approval and resource surfaces. [OpenAI remote MCP](https://developers.openai.com/api/docs/guides/tools-connectors-mcp), [ChatGPT plugin auth](https://developers.openai.com/plugins/build/auth), [Claude connectors](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp). **No hosted connector integration was tested.**

## 5. Rejected or deferred alternatives and why

| Option | Disposition | Evidence and reason |
|---|---|---|
| **Git-as-database / Git-only synchronization** | Reject as canonical authority | Violates explicit plan role for Git; agent concurrency, structured authorization, queryable revisions and cross-project relationships need application semantics. Git remains excellent for source and human-authored artifacts. |
| **Client-local SQLite or per-agent memories as authoritative** | Reject for shared-write Phase 0 | Not the specified live central store without a new sync/conflict protocol; Letta/Mem0 remain patterns, not replacements for source-attributed scientific state. |
| **MLflow, Aim, Invenio, Wikibase, Letta or Mem0 as Shiroe itself** | Do not adopt wholesale | Their documented models specialize in runs, repositories, statements or agent memory; none of the reviewed evidence proves Shiroe's cross-layer epistemic and revision invariants. [Aim](https://aimstack.readthedocs.io/en/latest/understanding/overview.html) adds a distinct storage stack; a [reported Aim issue](https://github.com/aimhubio/aim/issues/3422) is **not** a confirmed security advisory. |
| **Graph DB, vector DB, OpenSearch, Redis/job broker** | Defer | [PostgreSQL](https://www.postgresql.org/docs/18/ddl-constraints.html) already supports relations/initial FTS; no Shiroe graph traversal, retrieval or scale benchmark establishes a need for another service. [pgvector](https://github.com/pgvector/pgvector), [OpenSearch](https://docs.opensearch.org/latest/query-dsl/full-text/index/) remain escalation choices. |
| **Direct PostgreSQL clients** | Reject | Bypasses centralized permissions, migrations, provenance constraints, and safe agent operations. |
| **MCP-only canonical interface; mandatory separate MCP gateway** | Reject | CLI/API and UI need stable semantics independent of client MCP capabilities; adapters should use the same commands, and required coding agents already document remote HTTP support. |
| **Premature HA/microservices/Kubernetes; provider tunnels as universal solution** | Defer | No availability or budget requirement supplied. Provider tunnels and hosted-client network origins are not interchangeable with local/HPC access. |

## 6. Assumptions, disagreements and unresolved questions

**Assumptions to falsify:** modest initial metadata volume and concurrency; one allowed permanent server; external artifact bytes and source repositories continue to exist; initial queries are lookup/filter/lexical or shallow relation traversal; authenticated direct HTTP or approved forwarding is possible from **each** target machine; there is no requirement for offline concurrent editing. Neither report establishes the actual HPC site policy, data classification, server budget, operating owner, or availability objective.

**Reconciliation:** The persistence survey recommends *PostgreSQL + JSONB + FTS*; the access survey adds an API/MCP/auth/deployment layer and compares **Python, TypeScript and Rust** without selecting one. These are complementary, not competing stacks. Both favor one canonical service and independently versioned artifacts. The access report qualifies the earlier suggestion that PostgreSQL transactions or REST/MCP parity are sufficient: **lost-update prevention, idempotency, common authorization, and actual client interoperability are additional application-level obligations**.

**Open decisions:** (1) hosting/network path and data/provider policy, particularly HPC egress, proxies, CA trust and SSH forwarding; (2) server/runtime and first CLI library language; (3) institutional SSO vs scoped pilot tokens; (4) whether *chat UI* means Shiroe's own interface only or mandatory hosted ChatGPT/Claude connectivity; (5) principal/project permissions and cross-project evidence visibility; (6) write approval and operation-ID preservation in actual harnesses; (7) acceptable RPO/RTO, response latency, volume and concurrent-client targets; (8) what immutable artifact identity means for files that can change at the same path.

## 7. Prototype checks **before** architecture selection

All tests below are **proposed**, not performed. Fix datasets, versions, pass criteria and reproducible scripts *before* comparing stacks.

| Check | Minimal experiment and acceptance evidence |
|---|---|
| **Envelope and epistemic fidelity** | Store human note, observation, deterministic derivation, model interpretation and hypothesis; retrieve category, exact evidence revision, actor/activity and bidirectional lineage without prose heuristics. |
| **Atomic multi-client writes** | 10–20 simultaneous API/MCP clients attempt stale revisions and duplicate operations. Exactly one accepted transition per precondition; one result per `(principal, operation_id)`; no silent overwrite; same key with changed payload conflicts. Simulate timeout **after** commit and inspect receipt. |
| **Transport and permission parity** | Same get/search/create/revise/relate/operation behavior over HTTP, MCP and CLI; negative tests for unauthorized reads, relation targets, search hits and receipts; tool approval alone never grants Shiroe authority. |
| **Real harness compatibility** | On pinned Codex, Claude Code and an independent SDK client: discover tools, authenticate/refresh, read, create, revise, handle conflicts, retry, reconnect; record protocol revision, tool/resource availability and write approvals. Do not infer browser-hosted behavior. |
| **Cross-machine deployment** | Laptop, workstation, remote server and **approved HPC login node** reach the *same* record/revision; verify DNS/TLS, proxy, credential permissions, no-admin installs, outbound policy, disconnect/reconnect and authorized tunnel if needed. Failure of permitted network access blocks the gate. |
| **Recovery and evolution** | Migrate payload A→B without breaking historical revisions/old client fixtures; backup, destroy and restore canonical DB; rebuild search projections; verify artifact IDs and evidence are unchanged. |
| **External artifacts** | Reference Git revision, mutable FS/HPC path and DataLad/DVC-style versioned object; detect content drift, inaccessible paths and missing bytes without fabricating successful resolution. |
| **Sizing/search baseline** | Representative generated revision/edge corpus; capture P50/P95/P99 lookup, FTS, write and provenance traversal, CPU/storage/index costs, then compare against *predeclared* goals. Only add vector/graph/search service for measured failure or justified quality gain. |

For each run retain client/binary and SDK versions, server commit, DB version, migration version, OS/platform, MCP negotiated revision, identity/auth configuration (not secrets), test fixture and outcomes. In particular, **do not equate a documented SDK feature with functionality in a pinned Codex/Claude binary**.

## 8. Decisions needed next (§§0.2–0.6)

| Plan section | Decide now / produce | Intentionally postpone |
|---|---|---|
| **0.2 Core invariants** | Stable IDs, immutable revision and evidence references, actor vs model attribution, epistemic distinctions, authorized writes, idempotency/compare-and-swap, schema-version contract, backup/restore invariants | Paper/claim/experiment type taxonomy and final relationship vocabulary |
| **0.3 Server architecture** | One-service boundary, canonical vs derived state, DB migrations, transport-independent commands, chosen language after spike, deployment/auth baseline | Vector/graph engines, distributed queues, replica topology |
| **0.4 Git role** | Define Git/file/artifact authoritative boundaries, revision/digest references, import/snapshot contract and drift detection | Full DataLad/DVC orchestration, project/experiment directory conventions beyond necessary prototypes |
| **0.5 Access prototypes** | Pick actual MCP SDK and pinned clients; HTTP/OpenAPI, CLI/library, common tool functions, TLS/auth/permission rules, write receipts and local mode | Multiple SDK languages, elaborate browser chat, hosted connectors unless explicitly required |
| **0.6 Distributed test** | Name the server and four physical environments; obtain site approval; run exact-client, auth, concurrency, failure/recovery and cross-machine tests; publish reproducible pass/fail matrix | Production HA/performance optimization not required to satisfy gate |

**§0.1 outcome:** An evidence-based *candidate architecture and discriminating test plan*. **§0.6 gate remains open** until the required heterogeneous clients demonstrate shared persistent state across the required environments through stable interfaces. The provisional infrastructure can be refined after those tests; the literature, project and experiment ontologies should remain expressly evolvable.

## Source reports and verification boundaries

- **Authoritative inputs:** `Vision(2).md`; `Shiroe Development Plan(2).md` (notably §§0.1–0.6 and the Phase 1 ontology caveat).
- **Research proposals:** `Shiroe Core Architecture Survey_ Phase 0(1).pdf` (persistence/prior-art survey, 27 pp.); `Shiroe_Phase_0_Access_and_Deployment(1).md` (client capabilities, security, deployment and transport survey; dated 2026-10-13).
- **External supporting links:** Linked inline at the relevant claim. Their presence documents the reports' supporting evidence, **not a new independent re-test of every version-specific claim**. Claims marked [D] are capabilities those reports associate with official docs/source; [R] is reported benchmarking; [P] is architectural advice; [T] is still untested in Shiroe. Rolling documentation and current repository branches must be pinned when testing.
