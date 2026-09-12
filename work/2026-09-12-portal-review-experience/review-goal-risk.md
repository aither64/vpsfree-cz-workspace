# Risk and compatibility review: plan goal normalization

Reviewed `f5d587823368e530c5d9f52a17e1befed9fd54e1..d3bfd0f5a7c419c9df0ed53aa5f1acb77f8e10c2` in `dev-workspace`, including the Ruby CLI's goal reader, request binding and completion-evidence writers, and the portal's receipt loading, conflict reconciliation, retry and completion-proof consumers. Risk classification remains **High** because the change reconciles persisted cross-process request identity across an installed package upgrade. This was a read-only review; I did not run tests.

## Findings

No Blocking, Important or Advisory findings.

The normalization in `portal/internal/web/creation.go:24` matches the CLI boundary implemented by `libexec/dev-session:3610`: it removes only NUL, HT, LF, VT, FF, CR and ASCII space, while preserving nonbreaking, full-width and other Unicode whitespace. Fresh plan-derived goals are stored in that canonical form at `portal/internal/web/creation.go:507`, so the preceding portal generation can still read and prove receipts created after an upgrade using its exact digest comparison.

For deployed receipts that retain the pre-normalization goal, `creationGoalDigest` changes only the digest input used at the three recovery boundaries: canonical-session conflict detection (`portal/internal/web/creation.go:211`), completion evidence (`portal/internal/web/creation.go:364`) and CLI request binding (`portal/internal/web/creation.go:696`). This is the same equivalence already imposed before binding, journal creation, submission and evidence by Ruby `String#strip`. Changes to internal content or to non-stripped boundary characters therefore still produce a different SHA-256 digest.

The surrounding proof remains exact. Binding validation still checks schema, workspace, slug, operation kind, receipt ID, completed-deletion history, source thread and identity, model and effort. Completion additionally checks evidence schema and identity, tracking device/inode, destination thread, canonical manifest state and manifest goal digest. Plan text, plan digest and plan turn ID remain frozen in the unchanged request snapshot; fork behavior is excluded from goal-digest normalization. A normal GET can therefore reconcile the retained failed receipt to ready without incrementing its attempt or invoking the CLI, while retry remains available for partial recovery with missing completion evidence.

No persisted schema, CLI argument, manifest, strict journal, evidence format, Codex protocol or public API changes. Rollback is safe: newly validated plan receipts store the stripped goal that the old portal compares directly, while an older raw receipt remains blocked under the old package and becomes recoverable again after rolling forward.

## Material gaps

- The reported focused tests cover the real Ruby `read_goal` method and synthetic reconstruction of the deployed receipt/binding/evidence state, but the retained real fixture has not yet completed its package-upgrade reconciliation. That acceptance run is the strongest remaining check that the captured on-disk identities match the modeled regression.
- Full installed-package upgrade/rollback acceptance is still pending. Inspection shows compatible receipt and proof formats, but the targeted quick checks do not exercise a live rollback after a newly normalized plan receipt is created.
- The organization and workspace immutable pin updates were outside this runtime range and were described as mechanical. Their exact revision and package build remain delivery verification rather than a finding in this review.
