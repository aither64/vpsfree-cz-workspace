# Configuration preparation environment

The first system snapshot preparation returned an error before any activation:
its detached source checkout ran Overcommit without the configuration repository's
declared Ruby dependencies. The exact original request, error log and result are
retained. Its failure is consistent with the already documented configuration
worktree post-checkout requirement; the generated source commit/push had passed
hooks inside the repository's Nix shell.

The corrected system2 preparation runs the same reviewed source through
`nix develop --command dev-session coordination prepare ...` from the configuration
worktree, giving source-retention hooks the declared environment. It uses a new
preparation request ID and preserves the failed attempt. There is no reservation,
activation, replay, hook bypass or source change. The original application build
continues under its observer. With that utility still occupied, the parent visibly
supervises the corrected system preparation until a fresh observer can take it.
