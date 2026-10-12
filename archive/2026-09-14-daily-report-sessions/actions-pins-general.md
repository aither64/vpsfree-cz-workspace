# Final generated configuration pins: General review

Reviewed the exact committed configuration series:

- `vpsfree-cz-configuration`
  `249bed1ee28e69a907edd09ea97a1144dbcdefeb..3f213d5ebf922ab5522690ab28b3fdfa9b3bed1d`
  - `6e0021ac74b3bfcb69b09a23a7a0df7c3c869f47` pins
    `vpsadminServices` to
    `014fbc78422f3660b295add7a50f35cc7acdf0c8`.
  - `3f213d5ebf922ab5522690ab28b3fdfa9b3bed1d` pins
    `vpsfreeNotificationTemplates` to
    `6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333`.

I compared the series with `plan.md`, `state.md`,
`actions-pins-review-packet.md`, the functional-review reconciliation, and all
three repository `AGENTS.md` files. I inspected each commit and its generated
message, the complete lockfile diff, the source histories and remote feature
refs, the flake input graph, and the API host channel consumers.

## Findings

No Blocking, Important, or Advisory findings.

The branch is exactly two linear commits above the unchanged configuration
base. Each commit has one independently reviewable generated input update, in
the intended order, and only `flake.lock` changes. The first commit changes
only the `lastModified`, `narHash`, and `rev` fields of `vpsadminServices`; the
second changes only those fields for `vpsfreeNotificationTemplates`. The
generated messages accurately list the source ranges and retain the repository
format without manual rewriting. There are no fixup commits, repeated updates
to either input, handwritten configuration changes, or changes to another
lock node.

The source pins resolve to the reviewed and pushed feature heads. Direct remote
ref checks returned `014fbc78422f3660b295add7a50f35cc7acdf0c8` for vpsAdmin
and `6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333` for the notification templates.
The vpsAdmin feature is two commits above its current source base
`5ac49802f892da6fd37a88c8349b9cc7ea826538`; the lock update from
`791ab3aa89e2f613979da6090b89785c78245db5` deliberately also takes the two
scheduled dependency commits already present in that base. The template
feature is two commits above
`f944ba03eba5d0d6b58b7eb856f251d1c96f2c11`.

The consumer topology is unchanged. In `flake.nix`, the template input still
follows `vpsadminServices` for its `vpsadmin` input. API1 selects both the
`vpsadmin` and `vpsfree-notification-templates` channels, installs the template
package in replacement mode, and owns the scheduler. API2 selects the
`vpsadmin` channel without the external template channel. The final lock graph
contains the expected two source revisions and the expected follows edge.

`git diff --check` passed, all three lockfile revisions parse as JSON, explicit
per-commit pin/follows assertions passed, and `nix flake metadata
--no-write-lock-file --json .` completed successfully. The configuration
worktree has only the previously recorded untracked `.bin/` and `.bundle/`
development-shell directories; they are absent from the committed series.

## Residual risks and pending validation

- The local configuration feature now intentionally diverges by two commits
  from the published baseline-pin head
  `5036135728832d5c375705e3b69949c33460ff7e`. The remote still points to that
  exact old head, so the planned explicit leased push is required before the
  final pins are available remotely.
- The two `cz.vpsfree/vpsadmin/int.api*` configuration builds have not yet run
  for this regenerated head. They remain the planned long validation after the
  General and Risk pin reviews; the successful metadata check establishes that
  the generated locked inputs are fetchable but does not replace those host
  builds.
