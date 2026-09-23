# Configuration and development deployment

Required workspace procedure, selected by the routing table in `AGENTS.md`.
Its rules retain workspace scope and precedence. Paths and commands are relative
to the coordination workspace unless the text specifies another repository.

In every confctl-managed configuration repository, inspect its defined
channels and the channel-to-input mapping before updating a flake input. For a
normal update to a published upstream revision, run
`confctl inputs channel update --commit <channel> [role]` for the affected
channel and role. Use `confctl inputs channel set --commit <channel> <role> <rev>`
when an exact unmerged feature revision must be pinned. Do not manually edit
`flake.lock` or update the input outside its channel when a channel owns it.
Verify the generated lock diff has the intended revisions and no unrelated
input changes, accounting for expected transitive lock changes.

Keep confctl's generated Git history in the update commit message. Leave its
changelog enabled when useful; use `--no-changelog` for noisy inputs such as
`nixpkgs` and `llm-agents`. Keep automated `confctl ... --commit` messages as
generated, even when a line exceeds generic commit-message width rules. Edit
one only when intentionally making a concise changelog correction.

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
