# Serialize development-shell entry within one worktree

During `work/2026-09-12-nfs-cancellation`, concurrent `nix develop` invocations
ran the vpsAdminOS shell hook against the same `.gems` directory. One Bundler
startup failed with `cannot load such file -- bundler/rubygems_ext` while the
other shell reinstalled Bundler. A concurrent Nix evaluation also reported an
ignored SQLite cache busy error.

Enter one shell for related formatting, lint and test commands, or let one
shell's setup finish before starting the next. The following serial entry
reinstalled Bundler and the focused RSpec suite passed (213 examples). This is
shared build-directory contention, not a missing committed gem dependency.

Overcommit's temporary index isolation also rejects new files left in
`git add -N` state outside the commit (`Entry ... not uptodate. Cannot merge`).
Before a partial commit, remove only those owned intent-to-add entries from
the index with `git reset -- <paths>`; their working files remain intact.
Stage them normally for their own later commit. Do not bypass the hooks.
