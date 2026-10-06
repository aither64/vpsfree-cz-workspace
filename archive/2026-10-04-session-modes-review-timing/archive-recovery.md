# Recovery of the blocked archive

The user authorized finishing or reviving the exact blocked session and asked to
preserve why its archive failed. The simplest safe recovery finishes the already
committed archive instead of reversing its tracking transition.

[Original incident evidence](archive-recovery-evidence.json) preserves the
schema-2 journal at `tracking_committed`, exact retained root/member identities,
original failed portal receipt, and journal SHA-256/private backup location.
[Reusable diagnostic note](../../notes/dev-workspace/2026-10-04-team-archive-root-retirement-order.md)
records the archive ordering defect, the CLI helper-context failure, and proposed
regression coverage for the future implementation fix.

Selected helper retained-member reconciliation passed normal idle, identity,
materialization and submission checks under the normal tracking/transition
locks. Only the three recorded members were archived; no force, recreation,
journal removal or tracking alteration was used. The matching CLI archive
retry needs a terminal confirmation and explicit canonical Codex home.

Attempt artifacts:

- [Retained-member reconciliation and terminal refusal](archive-recovery-result.json).
- [PTY retry with missing Codex-home context](archive-resume-result.json).

Full local logs remain alongside these result artifacts. Private copies of the
original journal and exact one-off recovery scripts remain under
`~/.local/state/dev-workspaces/recovery-evidence/2026-10-04-session-modes-review-timing/`.
Final matching retry completed successfully with exit 0 in 121.436 seconds,
invocation `12dd8733a1e6490b9d899b95b2d0d69c`, at
`2026-10-04T17:57:42Z`. [Final recovery result](archive-resume-with-home-result.json).
Parent verified the journal is absent, the archived tracking directory remains,
the active tracking directory is absent, and the selected workspace profile was
unchanged. The archive implementation itself remains a later task.
