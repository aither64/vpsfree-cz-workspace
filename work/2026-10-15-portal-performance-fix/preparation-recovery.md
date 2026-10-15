# Unsubmitted integration preparation recovery

Run 074406d2-822a-4079-9ef4-931a802da234 submitted no jobs. Runtime and configuration
merge snapshots are prepared; workspace preparation failed on an unpublished
archive-only shared-master commit. That existing tracking commit was published
unchanged. The ordinary retry now fails because its cached expected workspace
head predates that baseline. The installed driver only refreshes an unset head
or a submitted job returning needs_refresh, so this pre-submission state cannot
reach that existing refresh through the ordinary resume path.

The one-operation loader recover-unsubmitted-preparation.rb invokes the selected
runtime's existing Integration#refresh for the original workspace request. The
ordinary command retains ownership/generation checks and the integration lock.
The installed recipe certifies the generated pin change, retains original refs,
checks the owned clean worktree and publishes with an exact lease. The loader
only replaces the derived expectedHead with that returned certified head. It
does not change requests, reviews, snapshots, approvals, jobs or ledger state.

Guards bind the exact run, owner, slug, workspace, selected package, original
review range, prepare phase, empty run job set and absent workspace snapshot,
approval and successful preparation receipt. It stops with exit 75 immediately
after saving the refresh, before any merge is submitted. The loader applies only
to that exact integration-resume invocation; child Ruby hook commands are inert.

Before execution, retain a private copy and SHA-256 of the integration journal.
Review this completed bounded recovery and its loader independently. After it
returns 75, inspect the native proof and actual branch, capture its new exact
comparison, and resume the same run through the unmodified selected command.
Its check-reuse logic verifies/builds the new derivation as needed. Preserve all
prior evidence and the journal. If a guard or native proof refuses, stop; do not
edit private JSON or bypass a check. This loader is not installed or released.

Invocation, after review:

```
RUBYOPT=-r/home/aither/workspace/ai/vpsfree.cz/work/2026-10-15-portal-performance-fix/recover-unsubmitted-preparation.rb \
  dev-session coordination integration-resume 2026-10-15-portal-performance-fix \
  074406d2-822a-4079-9ef4-931a802da234 --as-is --no-wait --json
```

Recovery is complete only after the original native run finishes its normal
operations. This does not waive deployment acceptance or reservation release
proofs. The application code, native Codex and persistent schemas are unchanged.
