# HaveAPI DELETE protocol correction: final consolidation

Base: `c14e7d3158b91c134c2817b489cd29772fc09f82`. Previous accepted head: `2ac6da81fa313b9df129a9fa8843358d0ef90492`.
Corrected pre-consolidation HEAD: `165000c05c675edf8d04c53ddb8abde0ed8285ae`. Final HEAD: `e9173e20a38de4e4e71bd5f2d4d79967950ca900`.

| Final logical commit | Purpose |
| --- | --- |
| `9818ebc19947322025d6ac552b0d7dd6b8e05ffb` | clients/rust: add embedded protocol runtime |
| `573bc23f570e0dfe6b542f9d6592fa2d0b63976d` | clients/rust: generate clients from saved API schemas |
| `e9173e20a38de4e4e71bd5f2d4d79967950ca900` | clients/rust: add protocol acceptance fixtures |

The runtime folds `45f35176130cd04c18d40320df20162ef99ac70e` into original runtime `0717da05eb2a6dec60e2fce2a57d97b5bb556653`.
Its exact delta matches the runtime fix's stable patch ID
`8d07e618561ffefd39f8865be103f4e52e6aa7b9`. The generator/tooling commit folds docs correction
`6e70c520bc0219b2aa47855948041206333d0638` into `e21d8a929ad8579e47ebaf1bf6c97c5340a664b3`; its owned-path delta matches stable
patch ID `8ceb6033bb3f1ab503289f6e710504947afcbdd3`. Integration folds the accepted
`b80ed05b2f8ef6ec68fc182464fe4133b3663da5`,
`dbc78c47b50f001006e40019b74056aed505ee83` and
`165000c05c675edf8d04c53ddb8abde0ed8285ae` fixes into previous integration `2ac6da81fa313b9df129a9fa8843358d0ef90492`.

The runtime/integration commit messages describe final GET query and DELETE
JSON behavior. The generator message is retained. No source edit or conflict
resolution occurred during consolidation.

Corrected and final trees are exactly `25902e7d68387f9fb033b2f7b90e0a2c7cbe2aed`. `git diff --exit-code`
between those heads passed. The final series contains exactly three feature
commits. The worktree and index are clean; no follow-up fix commits remain.

All three final logical commits explicitly ran `git commit --amend -F` with
prepared message files and required root Nix hooks. Applicable HaveapiI18n,
RuboCop and all commit-message hooks passed without warnings, bypass or hook
configuration changes. No application tests/builds, push, default integration,
publication, dependency/pin/schema change or migration occurred in this
history-only operation. The feature has no published/released/consumed state
requiring intermediate commits, as recorded by the lead.

- [Previous accepted three commits versus final three](haveapi-delete-reviewed.range-diff.txt)
- [Corrected intermediate series versus final three](haveapi-delete-remediation.range-diff.txt)

The actual client owner must regenerate copied runtime/provenance against
this final HEAD, then the lead requests affected-lane review before longer
verification. This record proves consolidation/equivalence; it does not
claim that the corrected DELETE behavior passed long acceptance. No other
intended generator/package edits are pending.
