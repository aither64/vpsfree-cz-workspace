# 2026-09-07-fix-ip-charged-environments

## Goal

Add an interactive vpsAdmin maintenance task that repairs owned VPS-purpose IP
addresses whose `charged_environment_id` is missing. The task must identify the
correct environment without assuming Production, reconcile numerical IP
resource accounting with the repaired inventory, show the complete proposed
change set, and require an explicit operator confirmation.

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
- Treat a plain numerical mismatch as a proposed accounting correction. Create
  or update the environment's IP `ClusterResourceUse` with admin override so
  recorded use matches the IP inventory. Do not change the
  `UserClusterResource` allocation; its `free` value may become negative.
- Refuse an entire owner/resource group if the environment cannot be selected,
  an already charged contributor is structurally inconsistent, accounting
  ownership or row targets are ambiguous, an out-of-scope uncharged address
  makes the calculation incomplete, a required environment config or user
  resource is missing, or a use is disabled, unconfirmed, or admin-locked.
  Structural IP checks include positive size, address/prefix integrity,
  availability in the charged environment, agreement between VPS and charged
  environments, and userless IPs linked to hard-deleted VPS rows.
- Print every safe change with IP, owner, assignment, VPS details when
  assigned, chosen environment, and selection reason. For each accounting
  correction, print the contributing IP IDs and sizes, resource/config row IDs,
  quota, total use, and free capacity before and after. Do not print user
  logins. Distinguish unassigned, VPS, export, and invalid contributors. Print
  the actual created or updated accounting row IDs after commit. Print blocked
  groups and their evidence separately, then accept only an exact interactive
  `yes`.
- Run only in a maintenance window with API, scheduler, supervisor, and other
  IP/accounting writers stopped. Require an explicit `--writers-quiesced`
  assertion and reject active transaction chains both before preview and under
  the database transaction. Application and row locks are additional safety
  checks within that window. Rebuild and compare the plan after confirmation;
  abort on any change. Apply safe rows atomically, verify them before commit,
  and attempt to release every lock. Print the committed accounting IDs before
  lock cleanup; if cleanup fails, report that the database work committed,
  print every cleanup failure, and return an error for operator intervention.

## Compatibility and deployment

- The task changes existing `ip_addresses.charged_environment_id` values and
  creates or updates the corresponding `cluster_resource_uses` values. It does
  not change schemas, APIs, on-disk formats, protocols, generated clients, or
  NixOS configuration.
- Old and new vpsAdmin processes can read the repaired rows after the
  maintenance window. Both tables and their accounting semantics already exist
  in current deployments.
- Deployment requires stopping API, scheduler, and other IP/accounting writers;
  draining transaction chains; stopping the supervisor; running the task with
  `--writers-quiesced`; and restarting writers only after the task exits. The
  task refuses to proceed while staged, queued, or rollbacking transaction
  chains remain.
- The preview and completion output contain IP, VPS, environment, and database
  row IDs. Operators must retain it as restricted operational evidence because
  it is the audit record for `ClusterResourceUse`, which has no PaperTrail.
- The database transaction rolls back IP and accounting changes together on
  failure. PaperTrail records the IP changes. The task output is the audit
  record for `ClusterResourceUse`, which does not use PaperTrail.
- A rollback after commit must restore both the prior IP charged environments
  and the prior resource-use values. Restoring only the IP fields would make
  accounting inconsistent again.

## Testing plan

- Check Ruby syntax and exercise the task against a disposable vpsAdmin API
  database.
- Cover Production, Staging, and Playground; mixed environments for one user;
  assigned and unassigned addresses; an assigned VPS outside the network's
  primary environment; export exclusions; accounting conflicts; missing or
  inconsistent primary mappings; cancellation; stale-plan detection; rollback;
  PaperTrail attribution; over-allocation with negative free capacity; creation
  and update of resource uses; unchanged user allocations; and idempotent
  reruns.
- Cover malformed and dangling accounting links, unexpected accounting row
  targets, admin locks even when totals match, invalid charged contributors,
  owner/VPS mismatches, export contributor labeling, active transaction-chain
  refusal, and post-commit reporting of actual accounting row IDs.
- Run the repository's available local checks, then the mandatory change review
  with `xhigh` reasoning before longer validation.
