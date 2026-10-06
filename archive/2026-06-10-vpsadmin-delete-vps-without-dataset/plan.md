# 2026-06-10-vpsadmin-delete-vps-without-dataset

## Goal

Find an operational side-channel cleanup path for a vpsAdmin VPS whose
`dataset_in_pool_id` points to a missing dataset record. Normal deletion cannot
load the association, while related state such as IP assignments and exports may
still exist.

## Affected repositories

- `vpsadmin`: source of truth for VPS records, datasets, IP assignments,
  exports, and deletion callbacks.
- `vpsadminos`: operationally relevant because the VPS exists on the node and
  osctld was affected by the missing dataset, but no code change is planned
  unless vpsAdmin cleanup requires it.

## Approach

- Inspect the vpsAdmin model and delete flow around VPS, datasets, exports,
  IP assignments, and node transactions.
- Prefer a safe maintenance/Rails-console style cleanup that uses existing
  vpsAdmin models where possible.
- If a normal destroy cannot be used because of hard association assumptions,
  identify the minimum direct database changes needed to make the object
  deletable or to remove it without leaving exported IP state.

## Compatibility and deployment

- This is an exceptional repair for already-corrupt production state. It should
  not change schema or persisted formats.
- Any cleanup must consider old and new running components seeing mixed state
  while the repair is in progress. The preferred order is to disable/remove
  exports and IP assignments before deleting the VPS record.
- If direct SQL is needed, wrap it in a transaction and verify that no live
  node transaction expects the missing dataset association.

## Testing plan

- Inspect existing model relationships and callbacks.
- Derive concrete verification queries for production before/after cleanup.
- Do not run destructive commands against production from this workspace.
