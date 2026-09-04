# 2026-09-03-webui-vps-ipv6

## Goal

Restore the public IPv6 route and interface-address controls on the WebUI VPS
details page for ordinary members at IPv6-capable locations. Preserve the
existing authorization rules for address discovery and assignment.

## Affected repositories

- `vpsadmin`: expose the Location IPv6 capability to permitted non-admin API
  readers and add API/browser regression coverage.
- `vpsfree-kb-contracts`: pin the vpsAdmin feature revision, assert the restored
  member controls, and regenerate the bound Czech and English screenshots.
- `vpsfree-cz-configuration`: pin the production `vpsadmin` channel to the
  reviewed vpsAdmin revision using `confctl`-managed input metadata.

## Approach

The regression was introduced by security-hardening commit
`a45273a0c3788d52265fc7f9093ec43c3e121308`, originally committed as
`31c831d461de30f0291dcface6523cc8b4c2ca91` on branch
`2026-05-23-fixes`. VULN-92 treated `Location#has_ipv6` as sensitive topology
solely because a legacy Index whitelist omitted it. The remediation made Show
enforce the same whitelist, and API specs codified the removal without tracing
the WebUI's nested `VPS -> Node -> Location` consumer. Admin responses bypass
the whitelist, which explains the role-dependent behavior.

- Classify `has_ipv6` as non-sensitive capability metadata and centralize the
  Location output field sets used by core Index/Show and requests-plugin
  overrides.
- Return `has_ipv6` to all callers already permitted to read locations,
  including requests-plugin anonymous readers. Keep `domain` and other
  administrative fields restricted; direct WebUI use of `Location#domain` is
  confined to administrator-only cluster pages.
- Leave PHP selection and API allocation authorization unchanged.
- Cover direct Location responses, the exact nested VPS include used by the
  WebUI, an IPv6-disabled vpsAdmin browser fixture, and an IPv6-enabled KB
  contract fixture.
- Add stable WebUI documentation landmarks for the existing “Manage host
  addresses” and “Add host addresses” actions. Define a semantic path for that
  sequence and bind the affected Czech and English IP-address instructions.
- Fetch the complete production KB inventory read-only, prepare exact bilingual
  annotation candidates and guarded release manifests, and validate them. Do
  not publish either production page without separate approval.
- Record the reusable lesson that output-whitelist reductions require consumer
  discovery and an explicit sensitivity classification for each removed field.
- Update the configuration channel with `confctl inputs channel set --commit`;
  do not edit its flake lock manually.
- Integrate the provider and consumers with fresh default-branch worktrees,
  fetching and rebasing feature branches when required, and use
  fast-forward-only merges. Merge vpsAdmin first, then the KB contract and
  configuration consumers that pin the resulting revision.

## Compatibility and deployment

The API response change is additive. It changes no database schema, persisted
state, generated client, daemon protocol, NixOS option, or vpsAdminOS behavior.
Old clients ignore the additional field. Deploying the API first immediately
fixes the existing WebUI; rollback is state-safe but reintroduces the missing
controls. No coordinated node update is required.

The contract repository pins the pushed vpsAdmin feature commit immutably.
The configuration channel will pin the same exact commit. The additive API
response remains safe when API/WebUI/configuration revisions overlap: old
clients ignore the field, existing WebUI clients recover the IPv6 controls as
soon as the new API is deployed, and rollback reintroduces only the original
display regression. The configuration update changes no host protocol, node
state, database schema, or deployment ordering requirement.

The user authorized merging all affected repositories into their default
branches. Merging the configuration revision does not authorize deployment or
production KB publication; those remain separate operational actions.

## Testing plan

- Run focused Location and VPS API specs, Ruby syntax/style checks, and all
  required Overcommit hooks from the repository Nix environments.
- Run the vpsAdmin IPv6-disabled member browser assertion.
- Capture the KB networking scenario in Czech and English against its dedicated
  cluster, preferring bridge networking and recording any required local-network
  fallback, then run `bin/validate --update` and `bin/check` and inspect the
  screenshots.
- After all intended commits and quick checks, run the mandatory high-risk
  review with General, Architecture, Scope, and Risk/compatibility lanes.
- Resolve review findings, run `webui#vps-user-core`, push both feature
  branches, and monitor their GitHub Actions results.
- Run the configuration input update through `confctl`, inspect the generated
  diff and changelog, and perform focused configuration evaluation for affected
  vpsAdmin service hosts.
- Review the expanded committed cross-repository series at high risk before any
  new long integration/evaluation run, then monitor feature-branch CI.
- Resolve the review blocker for unbound host-address instructions with focused
  vpsAdmin landmark tests, contract checks, and validated bilingual KB
  candidates. Re-pin both consumers to the remediated vpsAdmin head and rerun
  every review lane affected by the new documentation contract.
- From fresh integration worktrees, fast-forward the current default branches,
  run repository-appropriate pre-push checks, push, and monitor resulting CI.
