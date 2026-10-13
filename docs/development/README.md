# Development history

This directory records what Shiroe is intended to do, what was researched, which choices were accepted, and what remains uncertain. It is the entry point for future development agents and retrospective review.

## Read first

1. [Vision snapshot](sources/Vision.md) and [development plan snapshot](<sources/Shiroe Development Plan.md>).
2. [Decision ledger](DECISIONS.md), which distinguishes accepted choices from proposals.
3. The active phase index and its linked planning reports and decision records.

The user-authored vision and plan control project intent. Explicit subsequent user decisions refine that intent. Research reports and assistant recommendations provide evidence and proposals; they do not silently change requirements.

## Phases

| Phase | Purpose | Status |
|---|---|---|
| [0 — Core](phase-0-core/README.md) | Shared service, identity, provenance, interfaces, and distributed access | In progress: survey reviewed; core invariants drafted; prototypes pending |
| [1 — Literature](phase-1-literature/README.md) | Evidence-grounded literature retrieval and research-state modeling | Not started |
| [2 — Projects](phase-2-projects/README.md) | Persistent project reasoning and literature linkage | Not started |
| [3 — Experiments](phase-3-experiments/README.md) | Reproducible experiments and evidence feeding back into research state | Not started |

Each phase has a `planning/` folder for surveys, PDFs, specifications, and evaluation plans, and a `decisions/` folder for important choices. The phase index explains its scope, plan steps, deliverables, and completion gate. Add implementation and validation evidence when it exists; an empty phase does not need placeholder reports.

The phase indices follow the plan's detailed numbered sections. Its closing high-level roadmap uses different numbering in places; the original snapshot is preserved rather than silently reconciled.

## Maintaining the record

- Use [the decision template](decision-template.md) for choices that affect architecture, interfaces, deployment, scientific validity, or project scope. Routine edits do not need a record.
- Allocate the next globally unique four-digit ID from the ledger, even when the record belongs to a later phase. Use `NNNN-short-title.md` and keep the ID stable.
- State the decision date, status, decision maker, rationale, alternatives, consequences, evidence, and outstanding validation.
- Add a row to the ledger and a link in the phase's decision index in the same change.
- Preserve the original rationale when changing a choice. Write a new record, mark the old one superseded, and link both directions. Rejected proposals remain available.
- Update phase indices with actual progress and test results. Keep planned checks distinct from checks that passed.
- Preserve source reports as historical evidence. Explain corrections in a new document or decision record rather than rewriting their conclusions.

The initial records were reconstructed from the development conversation on 2026-10-13. Selected user statements are quoted in records; the full conversation transcript is not archived here. See [source provenance](sources/README.md) and [Phase 0 research history](phase-0-core/planning/README.md).

## Privacy of shared records

Personal deployment addresses, accounts, private paths, node identifiers, and identifying terminal details are omitted or replaced with explicit placeholders. Sanitized evidence preserves reported outcomes and is labeled accordingly. Necessary private originals remain locally in ignored `.private/`; they are not repository evidence available to other users. See [decision 0013](phase-0-core/decisions/0013-private-information-in-version-control.md). Substitute actual values before running the example commands; documentation IPs do not identify a live deployment.
