# 2026-08-10-update-vpsadminos-consumers

## Goal

Integrate the reviewed guest-kernel failure detection and AMD livepatch runner
initiative into repository default branches, update every workspace consumer
of the vpsAdminOS test framework to the merged revision, and advance the
vpsfree.cz `staging`, `os-staging`, and `production` channels through
`confctl`.

## Affected repositories

- `vpsadminos`: fast-forward the published implementation branch to `staging`.
- `vpsadmin`: fast-forward its final vpsAdminOS input pin to `master`.
- `confctl`: update its direct vpsAdminOS flake input.
- `terraform-provider-vpsadmin`: update its followed nested
  `vpsadmin/vpsadminos` test-framework input while retaining its vpsAdmin pin.
- `vpsadmin-kb-captures`: update its followed nested
  `vpsadmin/vpsadminos` input while retaining the exact vpsAdmin application
  revision coupled to its documentation contract.
- `vpsfree-irc-bot`: update its followed nested `vpsadmin/vpsadminos`
  test-framework input while retaining its vpsAdmin pin.
- `vpsadminos-org-configuration`: fast-forward the deployed runner4
  configuration to `master`.
- `vpsfree-cz-configuration`: retain the deployed runner4 DNS record, update
  vpsAdminOS in channels `staging`, `os-staging`, and `production` with
  generated `confctl` commits, and fast-forward to `master`.

## Approach

1. Fetch every target default branch and use only fresh worktrees owned by this
   initiative. Treat the published `2026-08-09-test-vm-kernel-oops` branches as
   immutable integration inputs.
2. Fast-forward vpsAdminOS `staging` to the reviewed and AMD-validated
   `67fcc1737` series before updating downstream locks.
3. Fast-forward the existing vpsAdmin, runner configuration, and DNS commits
   where their bases still match current defaults.
4. Update direct flake inputs with repository-provided helpers when present.
   For followed inputs, update the nested `vpsadmin/vpsadminos` path so the
   lock graph resolves merged vpsAdminOS without changing an independently
   pinned vpsAdmin application revision.
5. Update the three vpsfree.cz channels only through
   `confctl inputs channel update --commit` and retain its generated commit
   messages unchanged.
6. Run repository hooks and focused lock/evaluation checks, then integrate
   every new feature branch with a fresh default-branch worktree and
   fast-forward-only merge.
7. Push default branches over SSH, monitor triggered GitHub workflows, and
   cancel only superseded runs from obsolete SHAs on the same feature branch.

## Compatibility and deployment

- Consumer changes are flake-lock updates. They introduce no database, API,
  protocol, or persisted-state changes.
- The vpsAdminOS series changes test VM and CI behavior only; it does not
  require a coordinated update of running vpsAdminOS nodes.
- Updating all consumers together prevents mixed test-framework behavior, but
  old consumer revisions remain usable and rollback is a lockfile revert.
- The runner and DNS configuration are additive and already deployed. Merging
  them records the deployed state; it does not require re-registering runners
  1-3.
- The `production` channel update changes a pinned source revision, but the
  merged vpsAdminOS delta has no production runtime or persistent-format
  change. No deployment is authorized by this initiative; only configuration
  source integration is in scope.
- Host KVM/SVM log inspection remains unavailable from this workspace and is
  not a merge gate. GitHub job cleanup is the available validation boundary.

## Testing plan

- Verify every resolved lock graph points to the merged vpsAdminOS revision.
- Run declared repository pre-commit hooks for every new commit.
- Run lightweight flake evaluation or repository-specific dependency checks;
  rely on the already-passed vpsAdminOS AMD lifecycle, generic suite, and prior
  Intel lifecycle for the reviewed implementation.
- Use `confctl` for all vpsfree.cz channel changes and inspect each generated
  commit and channel revision.
- This session is dependency/generated integration work after a completed
  standalone code review, so no additional mandatory change review is needed.
- Monitor default-branch GitHub workflows and investigate any failure before
  accepting it as unrelated.
