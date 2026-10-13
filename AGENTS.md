# Working on Shiroe

Before planning or implementation, read `docs/development/README.md`, `docs/development/DECISIONS.md`, and the relevant phase index. Follow accepted decisions and the user-authored vision and plan; proposals and research reports are not implementation approvals.

For significant development choices, add a numbered decision record to the relevant phase's `decisions/` folder and update the ledger in the same change. Record rationale, alternatives, evidence, consequences, and unresolved checks using `docs/development/decision-template.md`. Do not infer user acceptance from an assistant recommendation or elapsed time.

Preserve decision history. A changed decision gets a new record linked to the superseded record. Keep planning reports separate from implementation and validation evidence, and update phase status only when the stated completion gate is demonstrated.

Deployment addresses and model providers belong in user configuration, not application defaults. Keep credentials out of these documents and source control. The initial home-server target is a deployment preference, not proof of network reachability or institutional permission.

Keep personal deployment addresses, account names, private filesystem paths, and identifying terminal prompts out of commits. Use explicit placeholders and label redacted evidence as sanitized. Store any necessary private originals under ignored `.private/`; never stage that directory or generated credentials/certificates. Check document metadata and compressed attachments before committing them.
