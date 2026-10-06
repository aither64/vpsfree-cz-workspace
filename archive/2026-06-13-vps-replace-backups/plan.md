# 2026-06-13-vps-replace-backups

## Goal

When an admin replaces a broken VPS, preserve the old VPS backup datasets for
the replacement VPS by default. Existing backup snapshots should remain
available under the replacement VPS ID/dataset, backup ZFS datasets should be
renamed to the replacement dataset path, and future backups should be able to
continue incrementally from the old VPS lineage.

The old behavior remains available per replace call:

- `preserve_backups=false` disables the whole backup switching flow.
- `preserve_backup_history=false` still moves existing backup datasets and DB
  state, but skips the replace-time continuity snapshot and therefore does not
  guarantee incremental continuation from the old source.

## Affected Repositories

- `vpsadmin`
  - API action `vps#replace`.
  - `TransactionChains::Vps::Replace::Os`.
  - storage snapshot/rename transactions and nodectld commands.
  - API, model, nodectld, and integration tests.
- `vpsadminos`
  - osctld/osctl local `ct cp` gains generic `from_snapshot` support.
  - osctld remote send already has `from_snapshot`; vpsAdmin uses that existing
    general-purpose interface for remote replacement.
  - osctld can transfer an existing snapshot to the replacement, then sends its
    own temporary transfer snapshot incrementally and cleans up only temporary
    osctld snapshots.
- `vpsfree-cz-configuration`
  - production `DatasetInPool.create` hook must understand replace context and
    skip backup provisioning when existing backups are being moved.

## Current Design

### Replace API

`vps#replace` accepts:

- `preserve_backups`, default `true`.
- `preserve_backup_history`, default `true`.

With `preserve_backups=false`, vpsAdmin skips the new flow completely: no
replace snapshot, backup catch-up, backup dataset rename, DB backup rewire, or
selected-snapshot transfer. Hooks receive
`preserve_existing_backups: false` and may create fresh replacement backup
state as before.

With `preserve_backups=true`, vpsAdmin records existing backup DIPs before
replacement dataset hooks run, passes replace context into hooks, renames old
backup datasets on disk, and rewires DB rows to the replacement dataset IDs.

With `preserve_backup_history=true`, vpsAdmin also creates a continuity
snapshot on every source dataset. It uses the standard datetime group snapshot
name, labels the snapshot as created for VPS replacement and mentions both VPS
IDs, then stores the confirmed snapshot name in the database for later
transactions. This snapshot is created through `Dataset::GroupSnapshot` in
strict mode, bypassing user snapshot count limits and scheduled snapshot
rotation.

### Backup Catch-Up

After the continuity snapshot is created, every existing old backup DIP is
caught up using `TransactionChains::Dataset::Transfer`, not
`Dataset::Backup`. This reuses normal transfer selection and handles the same
states as a real backup run:

- no old source snapshots;
- source snapshots that are not yet backed up;
- no backup head/tree yet;
- a shared backup head that can continue incrementally;
- a backup head from an older history, for example after reinstall;
- multiple backup pools at different points.

Rotation is intentionally skipped.

### Replacement Transfer

vpsAdmin does not post-copy-send the continuity snapshot into the replacement
dataset. Instead, it passes the snapshot name to osctld:

- same-node replace: `Transactions::Vps::Copy` -> `osctl ct cp
  --from-snapshot`.
- remote replace: `Transactions::Vps::SendConfig` -> `osctl ct send config
  --from-snapshot --no-snapshots`.

osctld then:

1. Creates its own temporary base snapshot as before.
2. Sends the selected continuity snapshot first.
3. Sends the temporary base snapshot incrementally from the continuity
   snapshot.
4. Tracks only temporary osctld snapshots in the copy/send log, so cleanup
   removes osctld snapshots but preserves the vpsAdmin snapshot.

For remote replace, `snapshots: false` is deliberate. It prevents osctld from
sending all existing old snapshots while still allowing the named continuity
snapshot to be preserved.
Remote replacement uses osctld's deterministic receive placement from the
target pool and VPS ID. vpsAdmin verifies that deterministic on-disk state with
`Storage::RecvCheck` before creating replacement-side snapshot rows.

### DB And On-Disk Alignment

After osctld has copied/sent the replacement dataset and before backup DB
rewiring, vpsAdmin appends `Transactions::Storage::RecvCheck` for each
replacement DIP and the continuity snapshot. The replacement-side
`SnapshotInPool` is created only after nodectld verifies the snapshot exists on
the replacement ZFS dataset.

The final DB rewire then:

- physically renames only topmost old backup datasets to the replacement
  dataset paths;
- fails with a clear exception if replacement backup DIPs already exist on
  pools where old backup DIPs will be moved;
- edits moved backup DIPs to point at replacement dataset IDs;
- keeps old source snapshots attached to the old source when a live old source
  `SnapshotInPool` remains;
- points moved backup and replacement DIPs at replacement-side `Snapshot` rows
  when needed;
- moves backup-only snapshots by editing their `dataset_id`;
- rewires or removes backup plans, backup actions, repeatable tasks, and group
  snapshot metadata so future scheduled backups use the replacement source DIP
  and moved backup DIP.

Integration tests verify DB snapshot rows against actual ZFS snapshot names for
the source, backup, and replacement datasets.

### Hook Context

`DatasetInPool.create` hooks receive:

- `purpose: :dataset_create`, `:vps_clone`, or `:vps_replace`;
- `source_dataset_in_pool:` when the new dataset is derived from an existing
  source DIP;
- `preserve_existing_backups:` when replace will move existing backup paths for
  that source DIP or an ancestor path.

Production and test hooks skip backup provisioning when:

```ruby
purpose == :vps_replace && preserve_existing_backups
```

The replace chain no longer creates then destroys hook-created replacement
backup DIPs. If such DIPs already exist, it raises.

## Compatibility And Deployment

- New vpsAdmin sends `from_snapshot` to osctld for default replace calls.
  Remote send already supports that option; same-node local copy requires the
  new vpsAdminOS/osctld support before local backup-history-preserving replace
  calls can use the default behavior.
- Remote receive streams are ordinary osctld sends into deterministic container
  dataset placement from target pool and VPS ID. No vpsAdmin-specific target
  dataset receive override is introduced in vpsAdminOS.
- Operationally, update vpsAdminOS on nodes before enabling the new default
  vpsAdmin replace behavior on same-node replacements. `preserve_backups=false`
  can be used when backup switching should be skipped.
- Production hooks are backward compatible with old vpsAdmin because the new
  hook keyword arguments have defaults and a `**` catch-all.
- New DB rows use existing tables; no schema migration is needed.

## Testing Plan

- Focused vpsAdmin API/model specs for:
  - replace API defaults and explicit disables;
  - same-node and remote chain payloads;
  - backup preservation/history switches;
  - hook context and conflict failure;
  - group snapshot label, confirmed-name recovery, and snapshot-limit bypass.
- Focused nodectld specs for:
  - dataset group snapshot label, confirmed-name recovery, and snapshot-limit
    bypass;
  - dataset rename/rollback;
  - VPS copy/send_config `from_snapshot` payloads;
  - replacement snapshot recv checks.
- Focused vpsAdminOS specs for:
  - osctld local-transfer and send logs with `from_snapshot`;
  - local copy sends selected snapshot before temporary base;
  - remote send sends selected snapshot before temporary base;
  - osctl CLI flags for copy/send.
- Integration tests:
  - same-node `vps/replace-with-backups`;
  - remote `vps/replace-with-backups-remote`;
  - both tests verify source, backup, and replacement DB snapshot rows against
    on-disk ZFS state and run a post-replace backup to prove incremental
    continuation.
- Run repository hooks before committing and watch GitHub Actions after push.
