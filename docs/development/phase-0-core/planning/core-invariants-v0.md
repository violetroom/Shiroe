# Core invariants v0 — step 0.2

- Date: 2026-10-13
- Status: draft specification for review; no implementation or contract tests yet
- Decision record: [0012 — Core invariant draft](../decisions/0012-core-invariants-draft.md)

The [vision](../../sources/Vision.md) and [development plan](<../../sources/Shiroe Development Plan.md>) require stable identity, provenance, distinguishable knowledge categories, documented heterogeneous interfaces, external artifact references, evolution, and recovery. The user additionally requires hardware/system provenance, visible personal claim testing, and later traffic verification. Those requirements are accepted. The concrete contracts below are proposals that make them testable; exact names, wire formats, database layout, and the scientific ontology remain open.

## Scope and authority

Shiroe owns committed shared research records. Clients own their sessions and working files; Git owns versioned source and human-authored files, which Shiroe may index with exact source references. Raw artifacts may remain in their originating systems. Search indexes, caches, and displayed validation summaries are projections that can be rebuilt from canonical records.

Phase 0 defines a common record envelope and operations. Paper, project, claim, experiment, observation, execution-context, and validation records below are illustrative kinds, not a frozen domain taxonomy or a commitment to implement all later-phase workflows now.

## I01 — Stable identities and explicit revisions

Each important record has an opaque stable object ID. Every committed representation has a separate immutable revision ID. Names, filenames, paths, DOIs, and Git hashes may be aliases or source references; renaming or relocating a record does not replace its Shiroe identity. IDs survive backup/restore and deployment relocation and are not reused for another record.

An object ID resolves its current revision. A revision ID resolves the exact historical representation, including its provenance and payload schema version. Updating a record appends a revision with its predecessor; it does not rewrite earlier evidence. A reference used as evidence pins a revision, while an explicit navigational link may follow the current object. These two link meanings must remain distinguishable.

Withdrawal/archive is an attributed state change that preserves history. History is immutable through ordinary edits; exceptional permanent deletion/redaction requires a separately defined maintenance contract, including backup consequences. Phase 0 does not promise that an archived object is physically erased.

## I02 — A narrow common envelope

Each revision exposes the following information, independently of the client that retrieves it:

| Information | Meaning |
|---|---|
| Object and revision IDs | Stable identity and exact representation |
| Record kind and payload schema version | How to interpret the payload |
| Predecessor revision, if any | History of the same record |
| Server commit timestamp and authenticated recording actor | Who committed it and when; client-reported event times are separate |
| Provenance/activity reference | Source, method, and attribution for this revision |
| Scientific content and epistemic category, when applicable | What is stated and what kind of knowledge it is |

Statements with different epistemic meanings must be separately identified or explicitly labeled within a structured payload. A project container or hardware description need not pretend to be a scientific hypothesis. Unknown data must be marked unknown rather than fabricated; required information and permitted unknowns are specified by each versioned payload schema.

## I03 — Knowledge category is separate from attribution and confidence

Proposed categories for statement-bearing records:

| Category | Example |
|---|---|
| Reported assertion | A paper's author reports a result; this is not our observation |
| Human assertion | A researcher states a judgment or note |
| Observation | A recorded measurement or directly observed event |
| Derived result | A computation from identified inputs using an identified method |
| Interpretation | An explanation or synthesis, whether written by a human or model |
| Hypothesis/proposal | A conjecture or proposed action to investigate |

Categories do not assert truth. Authorship, evidence strength, model confidence, human review, and empirical validation are separate dimensions. An LLM explanation cannot become an observation just because it is saved by a human. Extracting a published measurement remains a reported result until separately reproduced. Existing client labels do not determine the trusted classification automatically.

## I04 — Provenance explains the source and transformation

A revision's provenance identifies the activity that created it, its responsible actor, method, event time where known, and inputs at exact revisions or externally identified versions. A direct observation links its run and evidence; a derivation links its inputs and processing method/code revision; an interpretation links the passages or observations it interprets. A human assertion may have no external evidence but still has attribution and may not be presented as supported fact.

Record the authenticated recording principal independently from scientific authors/testers and client-reported harness/model metadata. A model name is not an authenticated user. Imported attribution is explicitly reported/imported rather than independently verified. Preserve collector/source and known/unknown status for provenance details. Do not automatically capture secrets or an entire process environment as provenance.

Internal evidence references must identify existing permitted targets or fail validation. External evidence may be unavailable, with its availability stated explicitly. Missing evidence must not silently become an empty, apparently complete provenance chain. Relationship changes that affect interpretation also carry attribution and exact endpoint revisions when scientifically relevant.

## I05 — Execution context preserves system and hardware

An observation or empirical validation links an immutable execution-context revision for the actual run. Include relevant system identity, node role, CPU/APU/GPU description, allocation/resources, memory, interconnect/topology, OS, compiler/build/dependencies, job ID, and configuration as applicable. Record how and when details were obtained; uncollected values remain unknown. This is a context contract, not a requirement that every field be meaningful for every activity.

Keep the submitting client context separate from the execution context. A Tuolumne login node submitting a result is not evidence that the computation ran there. Platform documentation alone does not establish a run's allocation or hardware. Reuse a context revision by reference when unchanged; configuration changes create a new context revision rather than rewriting earlier runs.

Human notes and literature assertions need no invented execution environment. A model inference may have its own context distinct from the experiment it explains. Automated collectors and complete experiment execution belong to later phases.

## I06 — Personal testing is evidence-backed and scoped

A validation record identifies the exact claim revision, researcher/project scope, performer and recording actor, method/test reference, time, execution completion status, conditions, evidence revisions/artifact references, and execution context when applicable. Proposed scientific outcomes are `supported`, `contradicted`, and `inconclusive`. An execution that failed before evaluating the claim is recorded as failed execution, not scientific contradiction.

The displayed indicator is derived from visible, completed empirical validations for the selected claim revision and researcher/project scope. The UI states whose testing it summarizes. It can expose both `personally_tested` and a result summary; neither is an independently editable truth flag.

| Applicable evidence in that scope | Display summary |
|---|---|
| No completed empirical validation | Not personally tested |
| Support and no contradiction | Supported in recorded tests |
| Contradiction and no support | Contradicted in recorded tests |
| Both support and contradiction | Mixed results |
| Only inconclusive outcomes | Tested; inconclusive |

Show conditions and outcome counts, including inconclusive results, alongside the summary. Separate contexts remain visible; support on one system is not universal verification. Automated tests may count when attributed to the researcher/project with method and evidence, but must not imply manual inspection. A software regression check counts only if it actually evaluates the identified scientific claim under recorded conditions; a passing general test suite is not personal validation of every claim. Human review, citations, planned tests, and model confidence alone never set the personal-testing indicator.

Changing a claim produces a new revision whose indicator starts without applicable tests. Older-revision tests remain accessible and explicitly labeled; copying a status onto a new claim revision is not a new empirical test. Validation corrections append revisions; summaries use current non-withdrawn validation records while retaining their history.

## I07 — One authorized contract across interfaces

HTTP API, MCP, CLI, and the Python library use the same application operations and validation/authorization rules. Clients may differ in presentation but not in object identity, scientific semantics, or accepted write behavior. They do not directly edit database tables or internal files. Local development exercises the same contract, using an isolated test store.

Operations authenticate and authorize the caller for reads, writes, search, relationship targets, history, provenance, and write receipts. Evidence traversal cannot leak inaccessible records. A summary based on permitted evidence states its visibility/scope without exposing hidden evidence or claiming completeness beyond that scope. Agent tool approval does not grant server authorization. OAuth provider, permission granularity, and discovery flows remain step 0.3/0.5 choices.

## I08 — Writes are atomic, conditional, and safe to retry

An update includes its expected current revision and a caller-generated operation ID. The server checks the precondition and atomically commits the revision, its provenance/relationships, and operation receipt. A competing update from the same base conflicts explicitly; the server never silently accepts the last writer over another writer's changes. A failed transaction leaves no partial canonical records.

The same authenticated actor repeating the same operation ID and normalized command receives the original result, even after a lost response. Reusing the ID with different command contents conflicts. An existing receipt is checked before reapplying an update's now-stale revision precondition, with current authorization still enforced. New intention means a new operation ID. Creates also use operation IDs so retries cannot create duplicate objects. Different IDs do not automatically deduplicate scientifically similar records.

A receipt identifies the operation, affected object/revision IDs, and commit time. A timeout leaves the outcome unknown until a receipt lookup or identical retry resolves it. Clients retain the pending command locally; they must not label an unconfirmed write as committed. Define and advertise receipt retention/retry windows during architecture work; after that window, verify state before replaying an uncertain command. No unlimited exactly-once delivery guarantee is implied.

## I09 — Artifact identity is separate from location

An artifact reference records its owning system, location, identifiable version/content digest where available, type/size where known, and access/retention information. A path by itself is a locator, not immutable scientific identity. Unverified identity remains explicit; resolve/check operations distinguish available-and-matching, changed, missing, inaccessible, and unchecked evidence. Failure to access a file is not proof that it is missing.

Raw bytes may stay in durable LC storage. The home server cannot assume it can dereference an LC path. A new file at the same path does not replace historical evidence silently; observed drift changes availability/integrity state, not the original content identity. Long-term evidence retention is part of the artifact owner's responsibility and must not rely solely on temporary scratch.

Git imports pin repository identity, commit, and path (and available content identity). Uncommitted changes require a separately identified snapshot. Source/Git updates do not silently overwrite indexed Shiroe state; reconciliation creates an attributed revision under the same write contract. Exact import/export formats belong to step 0.4.

## I10 — Evolving schemas preserve historical meaning

Payload schema versions and interface versions are explicit and independent. Supported historical revisions remain readable/exportable with their schema information. Migrations preserve object/revision identities, attribution, and original evidence; transformed views are distinguishable from the original representation. Clients receiving a schema they cannot interpret say so rather than guessing or silently dropping fields.

Reject unsupported write versions explicitly. Partial updates must not erase fields an older client does not understand. Publish capabilities and compatibility boundaries before accepting clients; exact version policy belongs to step 0.5. Search/cache rebuilds do not alter canonical records or become a migration of scientific meaning.

## I11 — Recovery covers canonical state and its boundaries

A backup/export must preserve objects, revisions, relationships, provenance, schema definitions needed for interpretation, and receipts within the supported retry window. Restore into a fresh deployment must retrieve the same scientific identities and history, then rebuild derived search state.

Database recovery alone does not recover external artifact bytes, Git repositories, OAuth configuration, or deployment credentials. Inventory and test those boundaries separately. Backup frequency, retention, storage protection, and acceptable data loss/recovery time remain deployment choices for step 0.3; an acknowledged write is persisted, but survives disaster only to the extent of the configured recovery strategy.

## I12 — Bounded retrieval and deliberate transfer

Reads/search expose revisions and explicit pagination/size boundaries. No silent truncation of scientific evidence and no automatic full-corpus traversal are allowed. Raw files, full chat histories, and entire source trees are not automatically synchronized as a side effect of ordinary record operations in the proposed initial design.

Request/response limits, concurrency control, bounded retries, and usage counters must be enforced by implementations rather than only agent prompts. Preserve pending updates when a budget stops traffic. Numeric limits remain proposed in [0011](../decisions/0011-client-traffic-and-artifact-placement.md); the user requires measurement during steps 0.5–0.6 and later workflow development. This specification does not establish an LC-safe threshold.

## Review examples and future contract checks

These are synthetic scenarios and pass criteria, not tests already run or real scientific results. Use small local fixtures first; distributed measurements follow only after the prototype exists.

| Check | Expected behavior | Invariants |
|---|---|---|
| Rename a claim and retrieve its first revision | Stable object ID; original text and provenance still available | I01–I02 |
| Import a paper assertion, derive a statistic, and write a model explanation | Three distinguishable categories; exact sources/method and model attribution retained | I03–I04 |
| Submit two observations made on different systems through the same login client | Each observation retrieves its actual run context; updating hardware information changes neither earlier context | I04–I05 |
| Add support and contradiction for one claim on different hardware | Personal testing is true in the selected scope; mixed results and both conditions remain visible | I05–I06 |
| Revise that claim; add only a citation or planned test | New revision is not personally tested; earlier empirical validations remain labeled by revision | I01, I06 |
| Record a run that fails before measuring the claim | Failure remains visible; no automatic contradicted/tested indicator | I06 |
| Two clients update one base revision | One accepted transition, one explicit conflict, no lost update | I07–I08 |
| Drop a response after commit, retry the exact command, then change its payload under the same ID | Original receipt/result returned once; changed command conflicts | I08 |
| Attempt unauthorized reads through search, history, relations, and receipt lookup | Every interface enforces the same boundary; no hidden evidence leaked | I07 |
| Replace an artifact at the same path or lose access to it | Detect/report drift or access failure without changing original evidence identity | I09 |
| Upgrade a schema while an older client edits a known field | Historical meaning remains accessible; unknown fields survive or update rejects explicitly | I10 |
| Restore a backup into a fresh deployment and rebuild search | Same IDs, revisions, provenance, relationships, and retained receipts; external evidence availability checked separately | I01, I09–I11 |
| Reach response/traffic limits; disconnect during result registration | Explicit bounds and locally retained pending state; no automatic bulk fetch or retry storm | I08, I12 |

## Decisions left for architecture and later phases

Choose concrete ID encodings, payload schemas, transaction/storage layout, receipt retention, permission scopes, OAuth issuer, backup objectives, and interface compatibility policy in steps 0.3–0.5. Develop the domain ontology and automatic literature/experiment capture in their own phases. The scientific contract above should guide those choices without selecting a framework or adding distributed infrastructure prematurely.

Step 0.2 has a reviewable draft. It is not frozen, accepted in full, or implemented; Phase 0's distributed completion gate remains open.
