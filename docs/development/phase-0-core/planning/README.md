# Phase 0 planning evidence

## Current specification

[Core invariants v0](core-invariants-v0.md) is the step 0.2 draft: identity/revisions, knowledge categories, provenance and hardware, personal testing, authorized writes/retries, artifacts, evolution, recovery, and bounded retrieval. It includes synthetic future contract checks. The draft is proposed and unimplemented; see [decision 0012](../decisions/0012-core-invariants-draft.md).

## Reports

| File | Purpose | Evidence boundary |
|---|---|---|
| [Architecture survey PDF](<Shiroe Core Architecture Survey_ Phase 0.pdf>) | Prior systems, persistence, identity, provenance, artifacts, and search | Research and proposed architecture; no Shiroe benchmarks |
| [Access and deployment report](Shiroe_Phase_0_Access_and_Deployment.md) | Clients, authentication, networking, deployment, write safety, and test plan | Dated 2026-10-13; documented capabilities are not exercised compatibility |
| [Combined architecture synthesis](<Shiroe Core Architecture Survey.md>) | Decision-support summary tying the two reports to Phase 0 | Historical provisional direction; read the newer decision ledger for accepted choices |

The user supplied these files at repository root. They were organized here on 2026-10-13. The PDF and access report were moved without content changes. The synthesis's two broken uploaded-source links were repaired to point to [the vision](../../sources/Vision.md) and [the plan](<../../sources/Shiroe Development Plan.md>); its findings remain unchanged.

Do not treat the synthesis's scoped-token pilot or custom chat UI suggestions as current selections. Subsequent user decisions choose OAuth and OpenCode. Its previously open language choice is now Python. See [the ledger](../../DECISIONS.md).

## How the survey was commissioned

On 2026-10-12 the user asked the assistant to read the Obsidian vision and plan and propose ChatGPT Deep Research prompts rather than conduct the tooling review itself. Three prompts were proposed:

1. **Architecture/persistence survey:** representative research information systems, trackers, agent memory, provenance/graphs, relational/lexical/vector infrastructure, and Git/artifact metadata. Evaluate stable IDs, revisions, epistemic distinctions, canonical versus derived state, migrations, concurrency, export, and recovery. Test the plan's PostgreSQL preference rather than assuming it; defer later-phase tooling reviews.
2. **Access/deployment survey:** use the first report and project sources to examine API/MCP/CLI/library options, per-client authentication and transport support, concurrent writes/retries, local and central deployment, and possible HPC constraints. Separate documented features from untested Shiroe integration.
3. **Synthesis:** combine the reports into the 0.1 deliverable, preserve evidence links, expose assumptions/disagreements/open questions, and propose checks for 0.2–0.6 without claiming prototypes or Phase 0 completion.

The reports were supplied and discussed on 2026-10-13. The research chats, exact executed prompts, model versions, and browsing traces are not archived here, so this is a summary of the proposed workflow rather than proof of how every report claim was produced.

## Reading the evidence

Use the reports for rationale and alternatives. External links and reported package versions are historical references, not a tested dependency lock. The current conversation checked selected OpenCode/OpenAI/Oracle documentation but did not install clients, contact the home server, verify lab endpoints, or inspect HPC policy. Archive actual versions and test results when prototype work begins.

## Subsequent site clarification

The user subsequently identified LLNL LC/Tuolumne and confirmed that keeping the database on their home server is acceptable from a storage perspective. [LC connectivity notes](lc-connectivity-notes.md) record public documentation checked on 2026-10-13 and distinguish it from an actual network test. See decisions [0008](../decisions/0008-lc-home-server-target.md), [0009](../decisions/0009-system-hardware-provenance.md), and [0010](../decisions/0010-personal-claim-validation.md) for the new deployment and provenance requirements.
