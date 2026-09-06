# 2026-09-06-portal-config-deployment-policy

## Goal

Prevent development deployments of the workspace portal from advancing
`vpsfree-cz-configuration` `master`, and correct the new-session reasoning
default from `max` to `xhigh`. Building and deploying aitherdev must use the
initiative configuration branch until the user explicitly accepts the portal
work for integration.

## Affected repositories

- Coordination workspace (`aither64/vpsfree-cz-workspace`): add the durable
  orchestration rule to `AGENTS.md`; change the shared portal/CLI reasoning
  default, tests, and operator documentation.
- `vpsfree-cz-configuration`: add the same durable boundary to its local
  `AGENTS.md`, then update only the initiative branch's exact
  `aitherVpsfreeWorkspace` pin and deploy aitherdev from that unmerged branch.

Configuration `master` may advance only to the isolated policy commit. It must
not acquire the portal development pin or any other portal implementation
change.

## Approach

- State that deployment and integration are separate decisions: aitherdev can
  be built and switched directly from a configuration feature worktree.
- Require portal-related configuration changes and exact
  `aitherVpsfreeWorkspace` development pins to remain on the dated initiative
  branch while the portal is still being developed.
- Forbid merging or pushing those commits to configuration `master` merely to
  make a development deployment possible.
- Require explicit user acceptance or an explicit integration instruction
  before the configuration branch is fast-forwarded into `master`.
- Commit the configuration-local rule first and integrate only that policy
  commit. Add the generated portal pin as a later commit on the retained
  feature branch, so the development deployment cannot accidentally advance
  configuration `master` to the pin.
- Change the central new-thread default to `xhigh`. Keep an explicit reasoning
  selection authoritative; when an explicitly selected model lacks `xhigh`,
  retain the existing fallback to that model's advertised default effort.
- Update focused tests and documentation from `max` to `xhigh` and verify both
  portal-created and terminal-created sessions consume the same resolver.
- Develop this reusable workspace-rule change on its own dated workspace
  branch and worktree. Integrate the reviewed workspace change into workspace
  `master` under the existing top-level workflow, but leave the configuration
  pin unmerged while portal development continues.

## Compatibility and deployment

The policy itself changes no runtime state. The reasoning correction affects
only newly created conversations whose effort is not explicitly selected;
existing threads retain their stored settings. It changes no schema, API,
protocol, or persisted format. Existing aitherdev generations remain usable,
and rollback selects the previous portal default. Future portal iterations can
deploy and roll back through ordinary confctl generations without publishing
their configuration branch to `master`.

## Testing plan

- Verify the rule distinguishes development deployment from branch
  integration and names the required explicit acceptance boundary.
- Run the focused Go resolver and web tests plus the workspace package checks.
- Build and deploy aitherdev from the configuration initiative worktree, then
  create one disposable session without an explicit effort and verify `xhigh`.
- Confirm configuration local and remote `master` end at the
  isolated rule commit and do not contain the later portal pin.
- Run Markdown whitespace checks and inspect the focused diff.
- Apply the mandatory documentation/instruction review at `xhigh` if the
  canonical review workflow does not classify the change for a documented
  skip.
