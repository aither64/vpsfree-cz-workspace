# Refresh hook dependencies after rebasing onto a new bundle

A rebase can start in a valid Nix shell and then fail in Overcommit's
`prepare-commit-msg` hook after Git checks out a newer default branch.
The shell was entered with the old Gemfile.lock, while the hook now reads
upstream's new lock and cannot find the newly required gems.

Enter the repository Nix shell again, run `bundle install`, and inspect the
hook configuration before updating its signature with `overcommit --sign`.
Keep hooks enabled throughout recovery.

Git can leave the failed patch staged and also reschedule it in the rebase
todo list. In that case, `git rebase --continue` asks for a commit. Commit
only the staged patch using the original commit message through the normal
hooks, then continue. If the rescheduled duplicate becomes empty, inspect
that state and use `git rebase --skip` for that duplicate only.

Verified while rebasing vpsfree-cz-configuration onto updated Overcommit and
net-imap dependencies. The original patch was retained once and the remaining
feature commits replayed successfully.

Related initiative: `work/2026-08-18-vpsadmin-password-reset/`.
