# Run integration checkouts in the configuration Nix shell

`git worktree add --detach` runs the repository's post-checkout hook. Outside
the declared Nix shell, Overcommit could not load its Gemfile dependencies and
returned exit 78 after creating the worktree. The checkout itself existed at
the intended base; creating it again was unnecessary.

Create temporary configuration worktrees through `nix develop --command git`
from the feature checkout. If the hook already failed, verify the new checkout's
head and clean status, then rerun its checkout through the same Nix environment.
The retry passed without changing source or bypassing hooks.

Evidence: [session state](../../work/2026-10-04-session-archive-reliability/state.md).
