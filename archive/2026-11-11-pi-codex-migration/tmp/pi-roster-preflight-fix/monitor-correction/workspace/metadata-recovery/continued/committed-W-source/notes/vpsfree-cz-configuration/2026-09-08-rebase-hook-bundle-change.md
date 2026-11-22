# A rebase can change the bundle required by Git hooks

During the password-recovery rebase, `nix develop -c git rebase origin/master`
loaded the old worktree's development shell, then checked out a newer default
branch whose Gemfile required `rubyzip-3.6.0`. The prepare-commit-msg hook could
not load that target bundle and stopped before creating the replayed commit.

Run `nix develop -c bundle install` after the target checkout so the declared
hooks can load its exact bundle. Do not bypass hooks. In this failure mode Git
leaves the patch staged and reschedules the same `pick`; a plain
`git rebase --continue` then refuses the staged changes. Inspect the index and
todo, confirm the staged paths contain only that replayed patch, restore only
those paths from the current HEAD, and continue the rescheduled pick inside
the updated development shell. Preserve any unrelated worktree changes.

Verification: the missing bundle installed successfully and replay resumed
with the existing hook entrypoints enabled. The rebase log records the final
result in the related initiative state.

Related initiative: `work/2026-08-18-vpsadmin-password-reset/`.
