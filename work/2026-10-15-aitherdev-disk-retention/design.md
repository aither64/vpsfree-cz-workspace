# Design and verification brief

The lead owns design and implementation. Destructive host/persisted-state work
requires independent general, architecture, scope and risk/compatibility review
after committed deliverables and quick checks.

## Host cleanup

Adopt the local Python helper in configuration, preserving daemon-store selection
and symlink/profile snapshot revalidation. Default to seven days/two generations.
Add whole completed temporary test-tree collection using completion/inactivity
age, run-lock exclusion, live process references and .keep holds. Unknown layouts
remain untouched. Keep managed roots delegated to their owner. Daily retention
and pressure GC share a host lock. Package fixed interpreter/tool paths and
migrate the local launcher with a backup.

## Coordination GC

Add a collector and workspace-host coordination gc dry-run/apply JSON CLI.
Traverse immutable snapshot/artifact references from nonterminal jobs,
held/unresolved reservations, pending integration journals, valid unsubmitted
preparations, active workers and retained package generations. Collect only known
runtime-owned payloads outside that live set. Keep compact immutable metadata and
receipt replay; never rewrite sealed hashes.

Track age and interrupted collection in a separate versioned private file. New
preparations establish freshness; inspection does not. Legacy unused preparations
get a seven-day grace period. Reject expired submissions with preparation-required
feedback. Needed payloads require ordinary source validation/preparation.

Take existing transition exclusion, revalidate references before deletion, skip
busy Git resources and remove worktrees through Git. Keep external commands out
of ledger transactions. Preserve active/uncertain worker and recovery paths.
Completion/cancellation/reservation release wake collection; sweeps retry busy or
interrupted work. Finished work has no retention delay.

## Integration and acceptance

Update the workspace nested runtime and configuration's dev-workspace channel to
one published feature revision; preserve extension and unrelated pins. Existing
strict ledger, snapshot, artifact and adapter formats stay unchanged. Additive
bookkeeping is ignored by old readers; existing transition locks exclude old
writers. Rollback cannot restore deleted disposable data, but preserves all
live/recovery state.

Acceptance: focused retention/concurrency cases, independent whole-branch review,
package checks and aitherdev build, native coordinated deployment, dry runs,
measured cleanup and live service/queue verification. Publish without merging.
