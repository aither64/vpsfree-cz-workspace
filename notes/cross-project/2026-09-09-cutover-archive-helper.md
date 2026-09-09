# Use the installed archive workflow with cutover session authority

During `work/2026-09-09-guix-test-fix`, the installed `dev-session` exposed
`archive` rather than `finalize`. The older workspace `libexec/dev-session`
could not read the live session authority: `invalid session authority fields`.
The deployed record includes the newer `tmux_identity` ownership field. Do not
remove that field or feed a modified authority record to the older helper.

The installed helper's `archive <slug> --as-is` owns the full completion
sequence: prove exact local/remote feature heads merged, require an idle owning
thread, stop only that slug's clusters, remove clean attached worktrees without
force, record immutable comparison metadata, move tracking, commit only the
work/archive paths, and retire the thread and session. It fetches workspace
master and checks linearity, uses a temporary commit-message file and
`git commit --only`, and retains branch refs.

Inspect the helper shipped by the current workspace profile before choosing
this replacement for older finalize/commit/stop instructions. Its internal
`finalize_locked!` implements the guarded finalization; do not invoke private
methods or bypass the outer ownership and lifecycle checks.

The owning active turn still fails `thread require-idle` with `inProgress`.
Prepare the final tracking and a bounded independent finishing process that
waits for the exact thread to be idle, verifies prepared file hashes and clean
feature state, and invokes the ordinary archive command. Stop on unexpected
errors or changed inputs. Check that the target fork has no running cluster;
never substitute the parent slug. Keep worker output outside the archive.

Verification: inspected the installed archive, merge-proof, non-force removal,
tracking-commit and slug-scoped cluster cleanup paths; the exact idle check
rejected the active turn. Read-only cluster status for this fork was stopped.
Final execution results belong in the initiative record and worker log.
