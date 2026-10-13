# 0013 — Keep personal deployment information out of commits

- Date: 2026-10-13
- Phase / plan step: all phases / development records
- Status: Accepted
- Decision maker: user
- Refines: [0001 — Development records](0001-development-records.md)

## Context and decision

The user requested committing the current state while keeping personally sensitive information out of the repository. Shared records use placeholders for personal deployment addresses, login accounts, private filesystem paths, precise activity times, node identifiers, and identifying terminal prompts/server fingerprints.

Preserve outcomes, rationale, public technical references, and accepted-versus-proposed status. Label changed evidence as sanitized rather than claiming it is an exact transcript. Source reports and compressed attachments require content/metadata inspection before inclusion. Public platform names remain where needed to explain the project's target environment.

## Why and alternatives

Unredacted terminal output and deployment examples can identify a person or their infrastructure even without containing credentials. Omitting all validation history would lose useful development evidence; clearly labeled sanitized records retain its meaning.

## Consequences and validation

Pre-sanitization copies of changed documents are retained locally under ignored `.private/precommit-originals/`, with restricted access. They are outside the committed documentation and must not be staged. Ignore private environment files and generated certificate/key files as well. Original user-authored material outside the repository is untouched.

Use a generic project identity for this commit's author and committer to avoid adding a personal name/email through Git metadata. This does not rewrite existing Git history or change the user's global Git settings.

The first commit of development material requires checking staged contents, PDF text/metadata/link targets, and the decoded drawing. Sanitization does not independently verify scientific or connectivity claims; existing provenance limitations still apply. Future commits need the same review because ignore rules do not sanitize document contents automatically.

## Evidence

User, 2026-10-13:

> Can you commit the current state to the repo? Make sure not to put any personally sensitive information
