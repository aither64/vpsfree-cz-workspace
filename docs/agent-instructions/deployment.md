# Configuration and development deployment

Required workspace procedure, selected by the routing table in `AGENTS.md`.
Its rules retain workspace scope and precedence. Paths and commands are relative
to the coordination workspace unless the text specifies another repository.

For `vpsfree-cz-configuration`, update flake inputs through `confctl`, not by
manually editing `flake.lock`. Use
`confctl inputs channel update --commit <channel> [role]` for normal channel
updates. Use `confctl inputs channel set --commit <channel> <role> <rev>` when
an exact unmerged feature revision has to be pinned. Keep changelogs enabled
when they are useful; skip them for noisy `nixpkgs` and `llm-agents` updates.
Keep automated `confctl ... --commit` commit messages exactly as generated;
do not amend or rewrap them to satisfy generic commit-message line length
rules. Edit them only when intentionally making a concise changelog edit.

Deployment does not authorize integration into any repository's default branch;
the Git procedure requires explicit user direction for the repository/target
set before feature-content integration. Build and deploy development
configurations directly from the initiative worktree and feature branch. In
particular, while the workspace
portal is still under development, keep its `vpsfree-cz-configuration` changes
on the dated initiative branch. The workspace application itself is deployed
from its own user profile and must not be added to, pinned by, or iterated
through the system configuration. Do not merge or push configuration changes
to `master` merely to deploy aitherdev. Integrate that branch only after the
user explicitly directs the merge; accepting a plan or deployment result alone
is insufficient.
