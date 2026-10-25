---
lifecycle: active
---

# 2026-10-25-archive-unmanaged-files-investigation

## Status

Investigation and recommendation complete. The fix is proposed, not implemented.

- [x] Identify the blocking files and archive invariant.
- [x] Trace failure ordering and inspect operation evidence.
- [x] Verify the installed discovery code in disposable state.
- [x] Reconcile findings and prepare handoff of the proposed solution.

## Next actions

Report the repair option and prevention proposal. Any later repair or runtime
implementation is a separate work item. No blockers remain for this investigation.

## Documentation

[Findings and proposed solution](findings.md). No owning-project documentation
change is appropriate until supported archive behavior is changed.

## Repositories

No feature branches, worktrees, source edits or deployment changes. The installed
cleanup source matches local canonical `dev-workspace` master
`52dcd471186ef874c5c93f4133744195d4815454` byte-for-byte.

## Commands run

Read the installed archive cleanup/executor and canonical portal/tests/docs;
inspect `systemctl --user show` and `journalctl --user` for the reported unit;
inventory the blocking directory without changing it. Start this separate
tracking-only initiative with `--no-codex --no-attach`.

## Results

See [findings.md](findings.md) for paths, evidence and limitations. An initial
inline fixture invocation omitted the helper's `pathname` dependency and failed
before exercising discovery; the saved reproduction loads it explicitly.

The saved [reproduce.rb](reproduce.rb) completed with exit 0 using the installed
Ruby 3.4.9. It reproduced sibling gem-cache refusal, accepted the same files
inside a canonical registered checkout with `clean: false`, and still refused a
loose sibling symlink. The fixture ran in 0.326 seconds; its temporary directory
was removed automatically. No full archive/revival or proposed fix was tested.

## Open questions

The exact command/agent that created the sibling cache is not established. The
safe cleanup policy for arbitrary auxiliary data is a proposed behavior change,
not an existing supported operation.

## Cleanup

The affected HaveAPI initiative, its worktrees and cache remain untouched. No
archive retry, deletion, recovery-state edit, package switch or deployment.
This tracking-only initiative remains open for follow-up.
