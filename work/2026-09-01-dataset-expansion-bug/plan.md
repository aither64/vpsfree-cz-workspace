# 2026-09-01-dataset-expansion-bug

## Goal

Prevent automatic dataset expansion from publishing a stale pre-expansion
refquota, and make every dataset-expansion notification render immutable size
values from the expansion operation instead of mutable dataset status.

## Affected repositories

- `vpsadmin`: update nodectld's in-memory storage-status snapshot, define the
  mail variable contract, update automatic and manual expansion callers, and
  add regression coverage.
- `vpsfree-mail-templates` (upstream repository
  `vpsfree-notification-templates`): render all expansion sizes from the new
  explicit mail variables.
- `vpsfree-cz-configuration`: pin the resulting vpsAdmin and notification
  template revisions so the fix can be deployed, without deploying it.
- Top-level workspace: maintain this initiative's plan, state, and any durable
  setup lessons.

The implementation branches were initially stacked on
`2026-08-31-vpsadmin-notifications` because the expansion templates use that
initiative's declarative notification layout. That base subsequently merged;
the initiative branches were already direct descendants of the resulting
default branches and were fast-forwarded into them without changing commit
IDs. Exact base and integration commits are recorded in `state.md`.

## Approach

1. In `NodeCtld::DatasetExpander`, update the in-memory `refquota` property to
   the new byte value after `zfs set` succeeds and before queuing the expansion
   event. Leave the property unchanged when ZFS rejects the change.
2. Extend `vps_dataset_expanded` with explicit integer MiB variables for the
   original quota, new quota, cumulative added space, and referenced space.
   Keep the dataset and expansion objects for identity and workflow state.
3. Require callers of the expansion-mail chain to provide `new_refquota`.
   Automatic event processing obtains it from the immutable expansion event.
   Manual expansion chains provide their already-computed target values; a
   repeated manual expansion also provides the post-operation cumulative added
   space because the database edit runs after mail rendering.
4. Update the Czech and English text templates to use only the explicit size
   variables. Preserve all visible prose, wrapping, links, and markup.
5. Replace the diagnostic PoCs with maintained node and API regression specs.
6. Commit and push focused changes, update dependency/configuration pins with
   repository-supported commands, run the mandatory fresh-context review, and
   then run the broader verification and selected configuration builds.

## Compatibility and deployment

- No database migration, API contract, node message schema, persisted-state
  format, or ZFS on-disk change is introduced.
- The node change is compatible with old supervisors because it only corrects
  an existing storage-status value. Mixed old/new nodes are safe.
- New API code with old templates is safe: the additional variables are
  ignored. New templates with old API code are unsafe because the explicit
  variables would be absent, so the service/API update must precede template
  reconciliation.
- Deploy the service role that consumes node events first, then the remaining
  API/reconciler services and notification templates. The node rollout is
  independent and may happen before or after the service update.
- Roll back notification templates before rolling back API services. The node
  fix can be rolled back independently, though doing so restores the stale
  status race.
- No coordinated vpsAdminOS machine update is required. This initiative does
  not deploy or activate any configuration.

## Testing plan

- libnodectld specs:
  - successful expansion updates pool accounting and the in-memory refquota;
  - failed expansion leaves both unchanged and queues no event;
  - the storage-status payload following an expansion contains the new quota.
- API specs:
  - the mail chain exposes all explicit values and uses the primary dataset's
    referenced space;
  - live supervisor processing passes the exact event target;
  - batch processing deduplicates mail and passes the latest processed event
    target;
  - first and repeated manual expansion pass their computed target values and
    repeated expansion passes cumulative added space.
- Template checks render the representative 290 -> 319 GiB / +29 GiB case in
  Czech and English and confirm that only ERB expressions changed.
- Run focused RSpec and RuboCop checks before commits, then mandatory change
  review, full API/libnodectld suites, flake checks, selected configuration
  builds for API services, staging node, and `node19`, and pushed-branch CI.
  Stop and investigate if a configuration build unexpectedly starts a kernel
  build.
