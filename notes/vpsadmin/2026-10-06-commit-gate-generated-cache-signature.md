# Reconcile generated cache and hook signatures before focused commits

In `work/2026-10-05-network-ipv4-left-counter`, strict owned-path commit
preflight stopped on an untracked `webui/.phpunit.cache/test-run-history`
created by the authorized PHP tests. Move that generated history into session
evidence rather than weakening the staging gate or committing it as source.

The next attempt stopped on Overcommit's stored configuration signature.
The lead and implementer compared `.overcommit.yml` and every custom pre-commit
hook with the exact branch base; all were byte-identical. After inspection,
`nix develop .#vpsadmin --command bundle exec overcommit --sign` succeeded.
Normal hooks remain mandatory. The precise reason the stored signature changed
was not established; repository Git configuration and hook signature records
are shared between worktrees, so another signature write is a possible cause.

When a failed commit has already staged files, verify the staged set and restore
only its owned paths to the index's HEAD state before retrying a wrapper that
requires a clean index. Preserve working-tree edits and unrelated staged files.
The repair and subsequent commit results are recorded in the initiative state.
