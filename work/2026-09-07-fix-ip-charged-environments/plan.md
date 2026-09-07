# 2026-09-07-fix-ip-charged-environments

## Goal

Add an interactive vpsAdmin maintenance task that repairs owned VPS-purpose IP
addresses whose `charged_environment_id` is missing. The task must identify the
correct environment without assuming Production, preserve existing cluster
resource accounting, show the complete proposed change set, and require an
explicit operator confirmation.

## Affected repositories

- `vpsfree-maintenance-tasks`: new dated repair task and its validation code.
- `vpsadmin`: read-only implementation and disposable-test reference. No source
  changes are planned.

## Approach

- Discover owned addresses with no charged environment in `any` or `vps`
  networks. Include unassigned addresses and addresses on VPS interfaces;
  exclude export networks and export interfaces.
- Select the current VPS node environment for assigned addresses. For
  unassigned addresses, select the environment of the network's primary
  location and require the `networks.primary_location_id` and primary
  `location_networks` row to agree.
- Group addresses by owner and IP resource (`ipv4`, `ipv4_private`, or `ipv6`).
  Recalculate the expected use in every environment using all charged owned
  addresses plus userless addresses charged through a VPS. Compare the result
  to `ClusterResourceUse` for each `EnvironmentUserConfig`.
- Refuse an entire owner/resource group if the environment cannot be selected,
  accounting rows are missing or ambiguous, an out-of-scope uncharged address
  makes the calculation incomplete, or expected and recorded totals differ.
  Never rewrite cluster resource limits or uses.
- Print every safe change with IP, owner, assignment, VPS details when
  assigned, chosen environment, and selection reason. Print blocked groups and
  their evidence separately, then accept only an exact interactive `yes`.
- Run online by acquiring vpsAdmin application resource locks, then database
  row locks. Rebuild and compare the plan after confirmation; abort on any
  change. Apply safe rows atomically, verify them before commit, and always
  release locks.

## Compatibility and deployment

- The task changes only existing `ip_addresses.charged_environment_id` values.
  It does not change schemas, APIs, on-disk formats, protocols, generated
  clients, or NixOS configuration.
- Old and new vpsAdmin processes can read the repaired rows. Mixed-version
  operation is safe because the column already exists and is used by current
  ownership accounting.
- The task runs online. Application and database locks protect against API,
  supervisor, and scheduled-task writers; a stale post-confirmation plan causes
  a full rollback.
- Rollback can restore the previous null values from PaperTrail, but doing so
  reintroduces the disown failure. Resource totals remain untouched throughout.

## Testing plan

- Check Ruby syntax and exercise the task against a disposable vpsAdmin API
  database.
- Cover Production, Staging, and Playground; mixed environments for one user;
  assigned and unassigned addresses; an assigned VPS outside the network's
  primary environment; export exclusions; accounting conflicts; missing or
  inconsistent primary mappings; cancellation; stale-plan detection; rollback;
  PaperTrail attribution; unchanged resource uses; and idempotent reruns.
- Run the repository's available local checks, then the mandatory change review
  with `xhigh` reasoning before longer validation.
