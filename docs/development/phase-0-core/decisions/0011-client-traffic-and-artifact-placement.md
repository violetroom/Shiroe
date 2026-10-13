# 0011 — Proposed client traffic and artifact placement

- Date: 2026-10-13
- Phase / plan steps: 0 / 0.2, 0.3, 0.5, 0.6
- Status: Design and limits proposed; later traffic/proxy validation required by the user
- Decision maker: assistant proposal; detailed limits and placement not yet selected by the user
- Related: [0007 — Candidate architecture](0007-core-architecture-candidate.md), [0008 — LC/home target](0008-lc-home-server-target.md)

## Context and proposal

The user asks how communication works, how much traffic to expect, and what resides on the server versus the client:

> I want to avoid accidentally throttling the llnl proxy

Use authenticated HTTPS API/MCP operations initiated by the client. Search at the server and return bounded records/excerpts on demand. Keep lab-model interaction between the client and the authorized lab endpoint; model prompts, token streams, and complete chat transcripts should not automatically pass through the home Shiroe service. Explicitly saved knowledge does go to Shiroe. OAuth discovery/refresh and MCP setup also generate some traffic.

| Location | Proposed contents and ownership |
|---|---|
| Home Shiroe service | Canonical shared claims, project/experiment records, observations, interpretations, relationships, revisions, validation records, and system/hardware provenance; rebuildable search indexes and backups |
| Home literature storage | Selected permitted papers and extracted text when the user chooses server-side ingestion; fetch/index there to avoid routing a corpus through LC |
| Client machine (LC or personal) | OpenCode session, selected fetched context, source checkout and Git-owned human-authored files, experiment scripts, working files, and local results awaiting explicit registration |
| LC retained project storage | Raw HPC outputs, traces, checkpoints, large logs, and datasets; referenced by Shiroe rather than automatically copied home |

A client is whichever machine runs the agent/CLI, including an LC login node. A cache is not the authoritative shared database. Human-authored files retain their Git ownership; Shiroe indexes explicit revisions rather than replacing that source of truth. Do not build full database replication or a general offline sync engine initially. Reuse fetched context within a session; any persistent cache must respect revisions and permissions.

An experiment registration should contain its configuration, source revision, system/hardware context (or an existing immutable context ID), compact metrics, interpretation, personal-validation evidence, and artifact references. References need location/system, identity/hash where practicable, retention/availability information, and access requirements. Keep raw evidence in durable retained storage rather than relying on temporary scratch. Mark inaccessible/missing evidence explicitly; the home server cannot assume it can dereference an LC path. A summary alone is not a substitute for reproducibility evidence.

## Traffic estimates

These are illustrative application-payload calculations, not measurements or institutional allowances. An exchange means request plus response. Aim for roughly 10–100 KB for ordinary metadata/text operations; record size and tool-use frequency determine actual volume.

| Assumed daily workload | Assumed average payload per exchange | Total payload |
|---|---|---|
| 50 exchanges | 20 KB | 1 MB |
| 500 exchanges | 50 KB | 25 MB |
| 2,000 exchanges | 100 KB | 200 MB |

Units are decimal. HTTP/TLS/MCP/OAuth overhead, retries, heartbeats, and any explicit document transfers add traffic. Multiple agents and clients add together. A single accidentally uploaded 10 GB trace dwarfs all three examples. No actual Shiroe traffic profile exists yet; the [passed health probe](../validation/2026-10-13-tuolumne-home-https.md) demonstrated reachability only.

## Proposed initial controls

- Start with one LC client and at most two in-flight remote operations. Avoid continuous polling and reconnect loops; use bounded retries with backoff, respect server retry guidance, and use safe write identities to prevent duplicate registration.
- Limit ordinary JSON requests and response pages to approximately 100 KB each. Search returns summaries/IDs; fetch specific evidence only when requested. Larger records need explicit pagination or a deliberate larger operation, not silent loss of scientific content. Apply limits to total bytes as well as item counts; do not let pagination silently fetch an entire corpus.
- No automatic raw-artifact, directory, repository, chat-history, or full-corpus upload/download. Document retrieval is a separate deliberate operation. Do not automatically dereference artifact URLs or LC paths.
- Batch compact result registrations after jobs complete through the login-node client; no per-timestep or per-rank remote reporting. Jobs retain results locally if the server is unavailable. Save only changed state and avoid repeatedly submitting identical hardware descriptions.
- Count bytes sent/received, calls, retries, connection counts, and peak rates without logging research contents or tokens. Aggregate usage across participating agents/clients. Propose a configurable 100 MB/day automatic stop for the initial LC pilot, with explicit resume and locally retained pending results; this is an arbitrary project guardrail, not an LC-approved safe threshold. Request-size, concurrency, and daily-budget limits address different failure modes.

## Why and alternatives

The source plan explicitly permits external artifacts. Bounded retrieval and result registration preserve shared knowledge without turning the API into a bulk-transfer path. Full replication and background file synchronization generate avoidable traffic and complicate conflict handling. Live job telemetry grows with ranks, timesteps, and retries. Small on-demand exchanges are the simplest initial design; compression and more sophisticated caching can follow measured need.

## Consequences and validation

Define artifact and evidence contracts in step 0.2. The client and server implementations must enforce the chosen limits; an agent instruction alone is insufficient. Prototype with synthetic metadata and run a short single-client LC pilot, checking actual transfer sizes, bursts, caching/revision behavior, pagination, retry behavior, and budget enforcement. Do not stress-test the institutional proxy. Server/payload counters may omit TLS and intermediary overhead; distinguish those from actual network measurements.

[LC's external-transfer guidance](https://hpc.llnl.gov/services/green-collaboration-environment/guidelines-external-data-transfers), checked 2026-10-13, warns that large HTTP(S) transfers can overload the institutional web proxy and directs users to contact LC for such transfers. It recommends SLIC resources for external bulk transfers. It gives no numeric safe API bandwidth/request threshold. Use LC-supported guidance for any future bulk-transfer workflow rather than designing around a guessed allowance or bypassing its proxy. The page also states outgoing data must follow applicable review/release processes; the user's accepted home-storage choice does not resolve every future artifact transfer.

No client transport, byte limiter, cache, or traffic benchmark has been implemented in this proposal. The exact values and protocol behavior remain open.

## Required later verification — user confirmed 2026-10-13

The user requested:

> Lets document that this is something to verify later in development

Add traffic instrumentation during step 0.5 and complete a small representative LC-client pilot during step 0.6, before claiming distributed integration complete. Revisit the measurements when literature ingestion or experiment registration is introduced in later phases.

- [ ] Measure uploaded/downloaded bytes, request frequency, concurrent connections, peak rates, retries, and session totals for ordinary search, record retrieval, and writes. Record client versions, node, workload, configured limits, and whether counters include protocol overhead.
- [ ] Verify server/client data placement: large raw artifacts and full chat histories are not automatically transferred; selected records and evidence references remain sufficient to trace results.
- [ ] Verify pagination, repeated retrieval, concurrent agents, outages, and retry behavior against local fixtures first; demonstrate byte/concurrency limits and budget exhaustion without losing pending writes.
- [ ] Run the bounded LC pilot without stress-testing the proxy. Record latency, errors, and any observed throttling; revise estimates and limits from evidence. Client success alone cannot establish spare capacity or absence of impact on the shared proxy; obtain LC guidance if workload or observed behavior warrants it.

Save results in this phase's `validation/` folder and link them from the phase index and ledger. These checks are pending; the user's instruction accepts the need for later verification, not the proposed numeric limits or complete storage design.

## Evidence

- User's traffic/storage question and proxy-load constraint, 2026-10-13.
- [Source development plan](<../../sources/Shiroe Development Plan.md>): core principles, steps 0.2 and 0.4 permit artifact references and distinguish Git-owned files from Shiroe state.
- [LC/home HTTPS result](../validation/2026-10-13-tuolumne-home-https.md).
- [LC external-transfer guidance](https://hpc.llnl.gov/services/green-collaboration-environment/guidelines-external-data-transfers).
