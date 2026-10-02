# Updating the extension lock without a default shell

The site extension flake exports a packaging library and has no default dev
shell or package. `nix develop -c nix flake lock --update-input dev-workspace`
updated the lock while evaluating the flake, then exited because its default
shell was absent. Do not assume that exit means the lock stayed untouched.

Inspect the owned flake/lock diff first. For an environment-backed repeat, use
`nix develop <generic-runtime-worktree> -c nix flake lock --update-input
dev-workspace` from the extension worktree. This retains the extension CWD and
uses the generic runtime's declared tools. In this initiative it completed and
only the intended generic runtime lock node changed.

Related initiative: `work/2026-10-02-portal-creation-performance/`.
