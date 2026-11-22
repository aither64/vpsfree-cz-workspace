# External conversation and retained deployment ownership

Observed during [portal file-link work](../../work/2026-10-18-portal-untracked-files/state.md)
with selected runtime qxj0iagbq0s2fp8747hfhghvpfam0x6j and Codex 0.163.0.

A new `dev-session start ... --no-codex --no-attach` creates a shell-only
initiative with explicit empty repository/artifact lists, but no retained
conversation. It can own tracking and worktrees; automatic deployment admission
requires the exact retained native conversation. For external supervised work
that will deploy, starting the retained conversation at creation avoids a later
adoption step. Its initial request can assign coordination standby and leave
implementation with the external lead.

Later supported `start --goal-file ORIGINAL --as-is --no-attach` preserves
ordinary tracking but requires its explicit scope and tracking baseline to be
committed, plus proof of threadless conversation/runtime absence. A live shell
from `--no-codex` prevents that absence proof. In this initiative, the deliberate
startup stop/restart of the owned idle shell removed tmux/authority, but `stop`
then returned `workspace-portal: exact recovery identity is required` for the
empty thread ID. Inspection confirmed the shell had stopped; the error did not
mean the operation had no effect. No tracking or worktree content was removed.

Resuming the original native-start command created a root and then refused
worktree synchronization while a registered checkout was temporarily detached
for a rebase. An owned detached input-regeneration scratch also caused an
unproven-worktree warning. After completing the rebase and removing that clean
scratch, the exact original `start` retry succeeded. The original goal, creation
journal and retained root were preserved. No private metadata was edited.

Finish rebases and remove owned detached preparation worktrees before starting
or retrying native session initialization. Keep required plan/state baselines
stable during creation recovery. Read actual state after a failed lifecycle
command instead of assuming an error proves no effect. Stop/restart here was an
initialization transition, not closing the initiative after work or handoff.
