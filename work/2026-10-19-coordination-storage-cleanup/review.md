# Final independent review: coordination storage cleanup

## Findings

1. **Important — risk/compatibility, general: a partially removed integration
   checkout cannot resume collection.**

   Location: `dev-workspace/libexec/workspace-coordination-gc.rb:279` and
   `:416–437`, introduced by `5cac3f8eda428f837b4789de1130704394022504`.
   The test at `test/coordination_gc_test.rb:403` covers interruption only after
   Git has finished removing the directory.

   `payloadGcPending` is written before invoking Git, but a retry uses its saved
   removal identity directly only when the directory is entirely missing. If
   removal stops after deleting one tracked file, the directory still exists.
   Planning follows the ordinary checkout path and rejects the deletion as
   `retained worktree has local changes`. Every subsequent sweep makes the same
   decision and leaves the pending record and remaining payload indefinitely.
   If `.git` was already removed, `git -C PATH rev-parse` fails instead, with the
   same inability to finish. This is a normal interruption of recursive removal,
   especially relevant to the multi-gigabyte checkouts motivating the feature.

   I reproduced the surviving-`.git` case in the repository's Nix shell using
   its existing disposable fixture, without editing repository files. The
   injected Git-removal interruption deleted the fixture's tracked `base` file
   and raised after the pending record was persisted. A second apply returned:

   ```json
   {"secondSweepRemoved":0,"preservationReasons":["retained worktree has local changes"],"pendingStillPresent":true}
   ```

   The focused diagnostic completed in 0.64 seconds: one test, five assertions,
   confirming the stranded state. The `.git`-absent variant is established by
   the subsequent `git -C` call and has not been exercised by this diagnostic.

   Recommended boundary: distinguish an already-journaled removal from first
   admission. Resume only the exact saved path/common-directory/HEAD, with its
   unchanged detached Git registration. Use that saved identity when `.git`
   has disappeared. If checking remaining contents, permit deletion changes
   caused by the pending removal while retaining newly added or modified data;
   alternatively resume the already-authorized Git removal under that exact
   pending intent and its documented ownership boundary. Do not turn ordinary
   dirty or unrecognized worktrees into force-removal candidates. Cover both
   partial cases and a changed-identity/new-edit rejection, then fold the fix
   into the cleanup commit. The documented automatic interrupted-removal
   recovery contract at `docs/coordination-operations.md:233` must match the
   implemented boundary.

No other Blocking or Important finding was identified. Resolve this finding or
record an explicit accepted decision before starting long verification. The
review does not authorize default-branch integration or production cleanup.

## Reviewed scope and identity

Standalone reviewer thread `01a15329-cb74-7402-932a-efe55a1d4d93`, task
`/root/retention_review`. Its native turn context records `gpt-6-astra`, `xhigh`,
`danger-full-access`, and approval policy `never`. The installed catalog's
default development team is `lead_reviewed`; its review-purpose role specifies
the same model/effort and read-only review behavior. The packet records why no
retained reviewer was available. No nested agent was launched and no application
file was edited.

Risk classification: **high**, because cleanup is destructive and must preserve
persisted recovery state and live package references. Reviewed all four lanes:
general, architecture/repetition, scope/proportionality, risk/compatibility.
Read the packet, plan/design/state, applicable workspace/repository instructions,
mandatory-review skill and all lane references, relevant collector/driver/host
code, tests, and owning coordination documentation.

Exact complete branch ranges reviewed:

| Repository | Base | Final head |
| --- | --- | --- |
| dev-workspace | `8385699aabcc2cfc74b585ca653a4658ff3eef75` | `957dc29fce880790f49921e59f6e5f88baa5e348` |
| workspace | `92a9a8d3c88e91b81d7a752fc29d1b807ed9d02f` | `e295c2200895d0d56bd9f8b3582fdce6d3eac451` |
| vpsfree-cz-configuration | `95a8b88d383c177fc65bf67d51c901a69c0b2847` | `dd2d0b4f17e6ee2a1df614fe45f623c7dfe56262` |

All three supplied bases are ancestors of their heads. Their worktrees were
clean and `git diff --check` passed during this review.

## Whole-branch conclusions

- **No obsolete unmerged approach remains.** Runtime commit `5cac3f8` owns
  completed scratch and idle worker-root collection, its recovery bookkeeping,
  focused tests and operations documentation. Commit `957dc29` separately owns
  workspace profile-history policy with its tests/documentation. These are
  independently reviewable changes; supporting tests/docs belong with their
  respective behavior. No fixup stream or abandoned intermediate protocol is
  retained in the reviewed series.
- **No repeated dependency-update stream exists.** Workspace has one nested
  runtime-selection commit (`e295c22`); configuration has one generated
  `dev-workspace/devWorkspace` channel update (`dd2d0b4`). Both select
  `957dc29` and the same source hash. Each lock changes exactly that runtime
  node; the workspace also changes its existing nested URL. The extension
  revision, sibling nodes and follows structure remain unchanged. The two
  repositories are distinct consumers, not redundant intermediate updates.
  The generated confctl message is appropriately retained as generated.
- The previous consumer pin is `5c799c17`, immediately before runtime review
  base `8385699`. I inspected the intervening baseline commit too: it changes
  only provider-recovery test fixtures, not installed application behavior.
- **No migrations.** There are no SQL/schema migration files or transitional
  migration versions in these branches. Per the packet, no feature migration
  has been merged, released, deployed or externally consumed. The optional
  `payloadGcPending` field is additive mutable journal bookkeeping; it does not
  create an intermediate versioned schema. No lineage consolidation is needed.

## Compatibility, ownership and scope

The generic runtime is the correct owner. It already owns collection scheduling,
the per-user ledger, profile-transition admission, integration/notification
locks and Git removal. The change reuses those mechanisms and introduces no
new scheduler or speculative cross-project interface. The workspace composes
the runtime through its selected extension and supplies coordination policy;
configuration selects the matching host/runtime input through its declared
channel. Application deployment remains through the user profile.

Integration readers load and preserve the complete journal object rather than
rejecting unknown top-level keys. The source `retention.json` format is unchanged;
the older collector does not consume the new pending field. Switching back to
older code would leave that pending cleanup for a newer collector, as documented.
Removed disposable data cannot be restored by software rollback. Runtime package
selection remains forward-only; retaining a predecessor is not a new rollback API.

The existing exclusive profile guard excludes cooperating preparations and
profile selection. Integration locks cover the journal edits; busy drivers
defer collection. Notification locks and service probes prevent releasing roots
for workers known to be active. Undelivered payload metadata remains traversed,
and dispatch recreates the selected worker package root. The new completion
predicate also preserves schema-2 runs whose continuation is not complete.
Profile pruning delegates generation deletion to `nix-env`, rechecks selection
and generation target, keeps current/predecessor/newer generations and marked
package references, and leaves separate Codex roots intact.

The review uses the documented trusted-local-operator boundary. It does not
require resistance to hostile root/filesystem manipulation. The finding above
concerns interruption of the collector's own operation within that boundary.
User feature-worktree deletion, branch deletion, cluster/VM/KB cleanup and broad
archive/source restructuring remain outside the delivered scope.

## Verification and residual gaps

The packet reports the passing complete focused suite (30 tests, 143 assertions),
syntax checks and composed deployment contract. I inspected the tests and ran
the additional bounded partial-deletion diagnostic described above. I also ran
a read-only in-memory notification-lock recursion probe through 2,000 owners;
it did not demonstrate a stack failure. Neither probe changed application files.

Long packaged checks, real systemd worker interaction, and the disposable native
Nix-profile exercise remain pending by design. The profile tests mock `nix-env`,
and fixture mode suppresses systemd/process probes, so those tests alone do not
prove the installed Nix/systemd behavior. GC-specific schema-2 continuation
coverage is not explicit in the new focused cases. Keep these as verification
limits; do not claim production readiness or measured reclaimed bytes from this
review. The parent owns finding reconciliation, tracking/portal updates, any
remediation and subsequent verification.
