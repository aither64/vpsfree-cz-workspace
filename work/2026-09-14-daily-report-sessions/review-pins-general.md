# Configuration pin general review

Reviewed the complete committed configuration range
`249bed1ee28e69a907edd09ea97a1144dbcdefeb..5036135728832d5c375705e3b69949c33460ff7e`
in `vpsfree-cz-configuration` against `plan.md`, `state.md`, and
`review-pins-packet.md`. The review covered the commit series, lockfile graph,
source revisions, and the two API consumers.

## Findings

No Blocking, Important, or Advisory findings.

The range is linear and contains two generated `confctl --commit` updates,
each with one logical purpose: `158516e58d3b28c6f8ce9e3e5313586f2f9fc528`
updates `vpsadminServices`, and
`5036135728832d5c375705e3b69949c33460ff7e` updates
`vpsfreeNotificationTemplates`. Keeping the independently reviewable input
updates separate is consistent with the repository workflow, and their
generated changelog messages accurately describe the source ranges. There are
no fixup or superseded pin commits.

A scalar comparison of the base and head lockfiles found exactly six changes:
`lastModified`, `narHash`, and `rev` for each of the two requested nodes. The
final revisions are vpsAdmin
`9456fae6f181cef2e8982eed462e873095fd49da` and templates
`08402ffd8010384f950b1ec4a1b95de8e5410ba3`; `git ls-remote` confirms both
exact heads on their respective `2026-09-14-daily-report-sessions` remote
branches. The final source-only changes since the original functional review
match the reconciled narrow fixes: variable metadata, parity comments and
registry assertions in vpsAdmin, and the Storage heading in the HTML template.

The lock graph retains
`vpsfreeNotificationTemplates.inputs.vpsadmin = [ "vpsadminServices" ]`,
matching `flake.nix:31-34`. Staging and production vpsAdmin inputs, every
vpsAdminOS and nixpkgs input, and all unrelated inputs are byte-for-byte
unchanged. Consumer wiring also remains correct: API1 includes both the
`vpsadmin` and `vpsfree-notification-templates` channels and owns the scheduler
and replacement template package
(`cluster/cz.vpsfree/vpsadmin/int.api1/module.nix:5` and `config.nix:21`), while
API2 includes only the `vpsadmin` channel
(`cluster/cz.vpsfree/vpsadmin/int.api2/module.nix:5`). `git diff --check` and
`nix flake metadata --no-write-lock-file` completed successfully and confirmed
the resolved lock graph.

## Residual risks and test gaps

- The two intended `confctl build --yes 'cz.vpsfree/vpsadmin/int.api*'` builds
  have not run yet. They remain the required full evaluation/build validation
  for the API1 combined generator/template closure and the API2 generator-only
  closure.
- The configuration feature branch has not yet been pushed. The two source
  revisions are remotely available, so this is an expected delivery step rather
  than a pin reproducibility problem.
- A later deployment still requires an explicit database migration because
  `vpsadmin.databaseSetup.autoSetup = false`. The pin does not change schema
  correctness without the indexes, but production query performance and live
  index-build impact remain outside this review and need the rollout procedure
  recorded in the initiative plan.
