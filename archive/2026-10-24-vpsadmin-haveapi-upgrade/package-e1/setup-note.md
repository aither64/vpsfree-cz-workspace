# Configuration worktree hook setup

The first ordinary worktree-add created the linked branch/check-out at exact
fcc7fc97 but its installed Overcommit post-checkout could not load the locked
gems outside the declared configuration shell. No hook was bypassed.
`nix develop` completed the documented local gem setup (48.867s); then the
ordinary same worktree-add registration path validated the existing branch/path
and recovered registration without a second Git add/checkout. All owned
handles completed. Enter the declared configuration environment before later
Git operations that invoke this repository's hooks.
