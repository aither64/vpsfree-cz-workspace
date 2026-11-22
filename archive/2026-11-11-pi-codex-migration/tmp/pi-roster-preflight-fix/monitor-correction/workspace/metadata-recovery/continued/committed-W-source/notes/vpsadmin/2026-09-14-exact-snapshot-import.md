# Exact snapshot import is not the existing VPS copy path

For `work/2026-09-14-restore-into-vps`, source inspection at vpsAdmin
`f7a17d6e512f0b11e2c908813eb2e780261e20ae` and vpsAdminOS
`0beff55b8529b7c33992eeebab82cd9df0f5b53a` found:

- osctld local transfer with `from_snapshot` sends that snapshot, then a newer
  base snapshot. It is not an exact historical restore.
- `Dataset::Send#confirm_block` preserves Snapshot IDs across pool copies of
  one logical Dataset. A new logical Dataset needs distinct destination
  Snapshot records and explicit transport identity mapping.
- The clone `keep_snapshots` integration scenario has a pending retention
  assertion. The option does not prove retained restore baselines.
- Site hooks set local VPS min/max snapshots to one, and rotation uses original
  capture time. Historical imported baselines need explicit protection.

Use snapshot-only send/receive and destination-owned history for the proposed
feature; validate rollback after source rotation/deletion. These are source-level
findings, not a tested implementation.
