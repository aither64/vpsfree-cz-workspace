# Configuration and development deployment

Required workspace procedure, selected by the routing table in `AGENTS.md`.
Its rules retain workspace scope and precedence. Paths and commands are relative
to the coordination workspace unless the text specifies another repository.

The selected package also provides the authoritative installed guides through
`workspace-host coordination guide`, including before workspace integration.

Before deployment activation or a workspace profile switch, read
[coordination](../coordination.md) in full. Build and copy before taking machine
ownership when supported. Under a claims runtime, acquire the physical machine,
request only the machine, run authorized activation commands and verify actual
results. Repository ownership is never held through builds or live review. Once
deployment and effect verification succeeds and the complete deployed feature
lineage is integrated into approved remote defaults, promptly release the exact
claim owned by this session and verify its released status, without another user
confirmation. Follow [machine retention](../coordination.md#machine-retention) for
source, system/profile and verification evidence and the final ownership check.
Missing proof or uncertain effects keep ownership; idle time or turn completion
does not replace either proof. Pass the held claim and exact session identity to
ordinary workspace-host profile activation.
Release supplies no merge approval. Legacy jobs/reservations keep their original
approval, integration-proof and recovery requirements. Held new claims require
explicit release before lifecycle cleanup.

Legacy automatic reservation release during lifecycle completion is an
implementation behavior, not permission to bypass machine retention or perform
a lifecycle action. Preserve the original recovery contract without initiating
archive, deletion or release merely to finish a deployment.

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

## Workspace runtime selection

The workspace owns generic runtime selection through
`inputs.vpsfree-dev-workspace.inputs.dev-workspace.url` in `flake.nix`.
This direct nested URL keeps the selected extension source independent of the
runtime revision. Extension updates must preserve that selection unless a
reviewed composition change intentionally replaces it. Remove the override only
when the selected extension provides the intended runtime and review proves that
the effective input graph and package/deployment contracts remain equivalent.

Select a published exact runtime revision, then generate the composed lock in
the workspace feature worktree with
`nix flake update vpsfree-dev-workspace/dev-workspace`. Inspect semantic input
paths and locked identities: preserve the extension revision/content hash,
sibling inputs and existing follows paths. Do not add a top-level runtime input,
rewrite the extension's own lock or deduplicate dependency nodes incidentally.
The direct nested runtime must match configuration's `devWorkspace` selection,
managed through its existing confctl channel. Run
`bin/check-dev-workspace-deployment --workspace-root PATH --configuration-root PATH`
against the final locks before deployment. The application still comes from the
workspace user profile; configuration selects the matching host module/runtime
contract and does not install the application.
