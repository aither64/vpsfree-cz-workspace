# Aitherdev message-delivery rollout

The exact reviewed user profile was deployed at 2026-10-25T13:09:24Z. The original
input block is recovered. Post-deployment lifecycle verification passed in a
disposable VM; see post-deployment-lifecycle.md.

The user authorized implementation and aitherdev deployment, then enabled
tracking. The later "merge and release" instruction authorized integration; all
four final heads are now on remote master, with equivalent downstream lineage
proved. The owning machine claim was released at 2026-10-25T15:06:08Z. This rollout used
machine claim b47c3ec9-13cc-4449-b9b8-33753030694b, owner
d6122ac3-11f1-4040-883f-4771abdd35a1. It waited for the storage-retention owner and
was granted at 2026-10-25T12:49:50Z. No other owner's resources were modified.

## Exact source and artifacts

| Component | Deployed revision |
| --- | --- |
| codex-web | 8b60554bc10c2a6bcbf9732a8b77ad959c317036 |
| dev-workspace | 9634151b9836311c331a58880fbb4c46133fd98f |
| configuration | 45683e38d3dc8e3ced20eae553f879e46ec84348 |
| workspace | 72e15700b241d75bcbc1eb8abf04542f70d9792f |

Application profile:
`/nix/store/48011krllhj3428878a8h55sb6x4wky0-dev-workspace-0.2.0`.
Configuration generation `2026-10-25--13-07-30` built successfully at
`/nix/store/4vlqvvpb5s3vqzjsbik75k4wk4ly8r7c-nixos-system-aitherdev-26.05.20261021.da6dc0e`.
Its etc tree differed only in confctl metadata and it had no package closure
change, so no system activation was performed. Native Codex remains 0.163.0;
extension and sibling inputs were preserved.

The predecessor was xjsni6q4ldh2anc8l1vn6zxjf64m4ska, source ec53874b, with archive
policy 3. The candidate preserves that baseline. Independent review confirmed
all baseline blobs and inherited workspace deltas, complete history and pin
consolidation. Final CI 40191223335 passed fast, creation/deletion and archive.
The final profile's packaged checks passed.

The first unselected --no-link build was collected during the ownership wait.
A rooted rebuild from the same exact inputs reproduced the exact profile and
passed before activation. After successful selection and acceptance, task-owned
temporary roots were removed; the installed profile retains the application.

## Activation and checks

The lead ran ordinary `workspace-host switch --source` against the committed
workspace feature checkout, with the exact session slug/workspace and held
DEV_WORKSPACE_CLAIM_ID. Normal compatibility, generation, ownership, lifecycle,
source and registration checks remained enabled. Activation exited 0.
Logs/status are under `/tmp/message-delivery-reliability-2026-10-25/activation*`.

The portal is healthy. Native daemon PID 3387667 was unchanged. SQLite schema 1
is ready, integrity is ok, and both predecessor paths have private schema-4
writer fences. A live canary and identical retry returned the same turn/receipt;
native history has one user message and the expected reply. The deployed naming
child returned a valid name in 2328 ms using its actual openai provider and
immutable catalog, with only an isolated ephemeral turn.

## Original-attempt recovery

Target session: 2026-10-24-context-copy-performance-tests.
Thread: 01a16fb2-77cb-7421-a66c-b7274a178ea2.
Attempt: 3466274b-d2c6-45f9-8ccb-4fe12ca9a382.
Source plan: 01a171ef-b55b-76e0-b926-3e28b706e421.
Plan SHA256: d35959b62010430b2221daf3909deab4917b63970bdcb8d2e31baff04669610a.
Canonical receipt preimage SHA256:
b71a24673fe924f71c272206b231967d0ae23e018e218448591dab0fbdef9e2d.

The original WebSocket acquisition error proves non-transmission. Fresh complete
native history (20 pages) corroborated absence of that UUID and the raw plan
digest. The reviewed one-off script matched the exact row/indexes/empty claim,
took a consistent fsynced private backup, and restored only it to prepared.
The ordinary plan recovery endpoint returned 200/retired:true, removing that stale
attempt without sending its obsolete implementation request. Identical recovery
replay returned the same result. The original row is absent and all 214 remaining
thread send receipts were accepted at the post-repair snapshot. The native PID
and database integrity remained unchanged.

Backups remain outside portal Files in private verification state. They are
forensic evidence, never authoritative restore points over newer receipts.
See pre-activation.json, original-repair-result.json,
original-retirement-result.json, original-retirement-replay.json and
post-recovery-state.json for exact results.

## Recovery and remaining ownership

SQLite state makes package recovery forward-only with submission schema/policy 1
and the preserved archive policy 3. Retain database/WAL, checksummed migration
backups and predecessor fences. Owning supported guidance is codex-web's
submission-storage.md and runtime workspace-portal.md; no rollback was attempted.

All four approved final feature heads are integrated and freshly proved on
remote master; deployed extension ancestry is also verified. Configuration and
workspace deployed source refs remain retained, with independently reviewed
equivalent successors rather than claims that nonancestor old commits merged.
The exact application derivation/output is unchanged after workspace refresh.
See integration-final-heads.json, integrated-lineage.json, refresh review and
workspace-artifact-identity.json. Live health, integrity and daemon continuity
were checked before ordinary release; aitherdev-released.json confirms release.
No later full configuration activation occurred. Release grants no lifecycle
authorization; the session remains open for follow-up.
