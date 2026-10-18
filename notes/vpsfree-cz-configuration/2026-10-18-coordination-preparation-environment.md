# Configuration preparation needs the hook environment

Launching `dev-session coordination prepare` in a plain user service can fail
while retaining the configuration source. `git worktree add` creates its checkout
before the Overcommit post-checkout hook reports missing gems. The coordinator
reports exit 75; no machine activation has occurred.

Launch the preparation driver through the configuration's Nix development shell,
from its configuration worktree, with `BUNDLE_PATH` pointing to that worktree's
installed `.gems` directory. The absolute path also works from a retained
checkout. Keep hooks enabled. Inspect the exact retained checkout after failure;
retrying preparation can reuse it rather than invoking its checkout hook again.
Complete the ordinary checkout hook in the prepared environment before activation.

User services also need an existing interpreter path: aitherdev's Python is in
the user Nix profile, not `/run/current-system/sw/bin/python3`.

Evidence and the deployment outcome belong to
`work/2026-10-18-portal-untracked-files/rollout.md`.
