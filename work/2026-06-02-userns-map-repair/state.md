---
lifecycle: active
---
# User Namespace Map Repair State

## Initiative

- Slug: `2026-06-02-userns-map-repair`
- Branch: `2026-06-02-userns-map-repair`
- Started: 2026-06-02
- Status: maintenance script committed, mail wording and formatting fixes
  pushed to `origin/master`.

## Worktrees

| Repository | Worktree | Base |
| --- | --- | --- |
| `vpsfree-maintenance-tasks` | `worktrees/2026-06-02-userns-map-repair/vpsfree-maintenance-tasks` | `7070705d` (`origin/master`) |
| `vpsfree-maintenance-tasks` | `worktrees/2026-06-02-userns-map-repair/vpsfree-maintenance-tasks-master` | local `master` |

## Commands Run

- `git -C repos/vpsfree-maintenance-tasks.git fetch --prune origin`
- Initial worktree creation failed because the bare repository HEAD was not
  pointed at a local branch.
- `git -C repos/vpsfree-maintenance-tasks.git update-ref refs/heads/master refs/remotes/origin/master`
- `git -C repos/vpsfree-maintenance-tasks.git symbolic-ref HEAD refs/heads/master`
- `git --git-dir=repos/vpsfree-maintenance-tasks.git worktree add -b
  2026-06-02-userns-map-repair
  worktrees/2026-06-02-userns-map-repair/vpsfree-maintenance-tasks
  origin/master`
- `git -C worktrees/2026-06-02-userns-map-repair/vpsfree-maintenance-tasks
  commit -F <tmpfile>`
- `git --git-dir=repos/vpsfree-maintenance-tasks.git fetch --prune origin`
- `git --git-dir=repos/vpsfree-maintenance-tasks.git worktree add
  worktrees/2026-06-02-userns-map-repair/vpsfree-maintenance-tasks-master
  master`
- `git -C
  worktrees/2026-06-02-userns-map-repair/vpsfree-maintenance-tasks-master
  merge --ff-only 2026-06-02-userns-map-repair`
- `git -C
  worktrees/2026-06-02-userns-map-repair/vpsfree-maintenance-tasks-master
  push origin master`
- `git -C
  worktrees/2026-06-02-userns-map-repair/vpsfree-maintenance-tasks-master
  fetch origin master`
- `git -C
  worktrees/2026-06-02-userns-map-repair/vpsfree-maintenance-tasks-master
  commit -F <tmpfile>`
- `git -C
  worktrees/2026-06-02-userns-map-repair/vpsfree-maintenance-tasks-master
  push origin master`
- `git -C
  worktrees/2026-06-02-userns-map-repair/vpsfree-maintenance-tasks
  merge --ff-only master`
- `git -C
  worktrees/2026-06-02-userns-map-repair/vpsfree-maintenance-tasks-master
  commit -F <tmpfile>`
- `git -C
  worktrees/2026-06-02-userns-map-repair/vpsfree-maintenance-tasks-master
  push origin master`
- `git -C
  worktrees/2026-06-02-userns-map-repair/vpsfree-maintenance-tasks
  merge --ff-only master`

## Repository Instructions Read

- `worktrees/2026-06-02-userns-map-repair/vpsfree-maintenance-tasks/AGENTS.md`

## Findings

- Existing task `2023-09-22-fix-vps-userns-map/fix_vps_userns_map.rb` handles
  only a VPS whose `user_namespace_map` row is missing. It aborts when the
  current map exists, so it does not handle cross-owner map mismatches.
- Follow-up after a failed production repair of VPS `16229`: the VPS was
  manually returned to osctl user/map `83`, while vpsAdmin still recorded
  `user_namespace_map_id=199`. This is tolerable only as a short-term
  quarantined state. Start/stop/restart use the node's current osctl container
  config and do not consult the vpsAdmin map, but operations that create, move,
  chown, or map datasets trust `vpses.user_namespace_map_id`.
- Risky operations while runtime map and DB map differ include VPS user
  namespace map changes, owner changes, migration, clone, replace, VPS create
  or receive paths derived from this VPS, and creating new datasets under a
  zfs-map-mode VPS. Those paths queue `userns_map_use`,
  `userns_map_disuse`, `vps_chown`, or ZFS `uidmap`/`gidmap` operations using
  the DB map ID and entries.
- `libnodectld` tracks osctl users by the DB map ID string exported by
  `Node::Rpc#list_vps_user_namespace_maps`. A node restart or fresh
  `OsCtlUsers` setup will rebuild user tracking from vpsAdmin's map ID when no
  local user-list config exists, not from the live container's osctl user.
- Use a VPS maintenance lock to block non-admin write operations if this state
  has to remain temporarily. Admin operations bypass `maintenance_check!`, so
  operators still have to avoid the risky paths explicitly.
- Recommended short-term recovery is to make vpsAdmin metadata match node
  reality again by setting VPS `16229` back to map `83`, then fix vpsAdmin API
  serialization so a non-admin VPS owner can still read the VPS when the nested
  `user_namespace_map` belongs to another user. The least invasive API change
  is to avoid serializing the nested `user_namespace_map` for non-admin VPS
  output, or otherwise expose only the map ID from the VPS row. Keeping the DB
  on map `199` while the node uses map `83` is riskier because later
  transactions trust the DB map.
- Alternative operational workaround, when an API deploy is not practical, is
  to create a new map owned by the VPS owner with the same effective uid/gid
  mapping as map `83`, create the matching osctl user named after that new map
  ID, chown the stopped container to that osctl user, and set
  `vpses.user_namespace_map_id` to the new map. vpsAdminOS `osctl ct chown`
  only rewrites ZFS `uidmap`/`gidmap` when old and new osctl users have
  different maps, so identical maps avoid the ZFS stale-ID failure mode. If the
  old host IDs cannot be represented in the owner's existing namespace, this
  requires an explicit temporary owner namespace alias with the same offset as
  the old namespace; keep it locked/documented and remove it after a real
  remap is possible.
- Concrete operation classification for `vpsAdmin=199`, node/runtime data
  map `83`:
  - Expected hard-fail or failed repair semantics: operations that execute
    `osctl ct chown` to a map different from actual map `83`, i.e. changing
    `user_namespace_map_id`, changing VPS owner, the maintenance repair chain,
    and admin clone-to-different-owner. These are the operations that ask ZFS
    to rewrite dataset uidmap/gidmap and hit the stale-ID problem.
  - Expected to complete but propagate the mismatch: migration, same-owner
    clone, and replace. vpsAdmin queues `userns_map_use` for DB map `199`, but
    `osctl ct send config` exports the source container's actual osctl user
    (`83`) unless an override is passed; vpsAdmin does not pass such an
    override. The destination import therefore creates/uses osctl user `83`
    and the DB still says `199`.
  - Expected to complete but create bad new data: creating new zfs-map-mode
    datasets under the VPS. The storage create transaction stamps new datasets
    with DB map `199` uidmap/gidmap while the container uses `83`.
  - Expected not to notice this mismatch: start, stop, restart, password
    change, rescue boot, reinstall, rollback, resource changes, hostname,
    DNS resolver, feature changes, mount script regeneration, network changes,
    soft delete/revive, and hard delete. Hard delete may leave unrelated osctl
    user tracking cleanup warnings, but `userns_map_disuse` is tolerant of
    deletion failure.
- Production symptom row:
  - VPS `16229` / `gemini` belongs to `bsasoft` (`user_id=662`).
  - Current `user_namespace_map_id=83` belongs to `Dangar` (`user_id=320`).
  - Map `83` is also used by Dangar's VPS `10673`, so the fix must not alter
    or delete map `83`.
- vpsAdmin production revision `f2dc568ff` has
  `TransactionChains::Vps::Update` support for `user_namespace_map_id` changes,
  including node-side use/chown/disuse transactions.
- `TransactionChains::Vps::Update` applies the change immediately and has no
  hook for user notification or maintenance-window scheduling. The script now
  defines `TransactionChains::Maintenance::Custom` and queues the same
  use/chown/disuse transactions after an optional
  `Transactions::MaintenanceWindow::Wait`.

## Validation

- Added
  `2026-06-02-fix-vps-userns-map-owners/fix_vps_userns_map_owners.rb`.
- Committed as `6b1fec61b9d096f03fd0480e1d91a328bdcbe91e`.
- Local `master` fast-forwarded from `7070705d` to `6b1fec61`.
- `origin/master` now matches local `master` at `6b1fec61`.
- `git push` succeeded. GitHub reported existing Dependabot security notices
  for the repository default branch.
- Follow-up committed as `af478bb19086303395a8753cdc2f4a6c8cc20e51`.
- The follow-up changes custom finish-window mail rendering to show only the
  selected finish day/time, mirroring vpsFree mail-template migration wording,
  instead of listing all generated temporary fallback windows.
- `origin/master`, local `master`, and `2026-06-02-userns-map-repair` all now
  point at `af478bb19086303395a8753cdc2f4a6c8cc20e51`.
- Follow-up validation:
  - `ruby -c
    2026-06-02-fix-vps-userns-map-owners/fix_vps_userns_map_owners.rb`
    passed.
  - `ruby
    2026-06-02-fix-vps-userns-map-owners/fix_vps_userns_map_owners.rb --help`
    passed.
  - `git diff --check` passed.
  - ERB render check verified Czech and English custom finish mails include
    the selected `04:00` finish time and omit generated fallback windows.
- Formatting follow-up committed as
  `5e4532a366987b0816930ad70f71c0ec20fc5073`.
- The formatting follow-up removes hard-wrapped lines from the inline mail
  paragraphs so generated mail does not break mid-sentence in the web UI.
- `origin/master`, local `master`, and `2026-06-02-userns-map-repair` all now
  point at `5e4532a366987b0816930ad70f71c0ec20fc5073`.
- Formatting validation:
  - `ruby -c
    2026-06-02-fix-vps-userns-map-owners/fix_vps_userns_map_owners.rb`
    passed.
  - `ruby
    2026-06-02-fix-vps-userns-map-owners/fix_vps_userns_map_owners.rb --help`
    passed.
  - `git diff --check` passed.
  - ERB render check reproduced the Czech custom finish mail for VPS `16229`
    and verified there is no break between `interní`/`konfiguraci`, no break
    between `úterý`/`od`, and no generated fallback window text.
- The script supports:
  - `--vps ID` to repair selected VPSes, repeatable;
  - `--map ID` to force the owner map for one selected VPS;
  - `--[no-]mail`, enabled by default;
  - `--[no-]maintenance-window`, enabled by default;
  - `--finish-weekday DAY` with `--finish-time HH:MM` or
    `--finish-minutes N` to use a migration-style temporary finish window
    from `VpsMaintenanceWindow.make_for`;
  - `--reserve-minutes N`, default `15`;
  - `--admin-login LOGIN` for transaction-chain audit metadata;
  - `--dry-run`.
- Notification mails are inline in English and Czech. They describe an
  internal VPS configuration repair, not user namespace maps.
- The script skips notification when `user.mailer_enabled` is false, matching
  existing maintenance mail scripts.
- `ruby -c
  2026-06-02-fix-vps-userns-map-owners/fix_vps_userns_map_owners.rb`
  passed.
- `ruby
  2026-06-02-fix-vps-userns-map-owners/fix_vps_userns_map_owners.rb --help`
  passed after moving `require 'vpsadmin'` behind option parsing.
- A standalone ERB render check for both inline mail templates passed.
- Option validation checks passed for:
  - `--finish-weekday 3` without finish time;
  - `--finish-weekday 3 --finish-time 23:45`;
  - `--finish-weekday 3 --finish-time 04:00 --no-maintenance-window`;
  - `--finish-weekday 3 --finish-time 04:00 --finish-minutes 240`.
- `git diff --no-index --check /dev/null
  2026-06-02-fix-vps-userns-map-owners/fix_vps_userns_map_owners.rb`
  produced no whitespace warnings.
- Production execution was not attempted locally.
