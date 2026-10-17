---
lifecycle: active
---

# 2026-10-17-aitherdev-disk-usage

## Status

Read-only disk-usage investigation in progress. No cleanup or service changes.

## Phase checklist

- [x] Confirm host and filesystem pressure.
- [ ] Measure major directories and large files.
- [ ] Attribute dominant consumers to users, projects, sessions, or services.
- [ ] Reconcile findings and hand off recommendations.

## Next actions

Finish allocated-block scans and investigate the largest consumers.

## Documentation

Plan and state are the only intended deliverables; application docs do not need
changes for this inventory.

## Repositories

No feature branches or project worktrees. Shared coordination checkout stays on
master and contains substantial unrelated changes, which must be preserved.

## Commands run

- `dev-session current`: no current session before creation.
- `dev-session start aitherdev-disk-usage --no-codex --no-attach --json`.
- Identity verified with both literal session environment variables and `current`.
- `df -hT`, `df -i`, `findmnt`, allocated-block `du` scans.
- `journalctl --disk-usage` and pressure-GC service status/journal.
- `sudo -n true`: password required; no privileged mutation attempted.

## Results

- Host: aitherdev; investigator: aither (UID 1000).
- Root ext4: 984 GiB total, 848 GiB used, 86 GiB available, 91% use.
- Inodes: 22% used.
- System journals: 2.8 GiB.
- Last pressure-triggered Nix GC, 2026-10-17 08:53:29–08:55:35 CEST,
  succeeded but deleted zero store paths and freed zero bytes.
- No retained team exists; `team list` reports no valid lead Codex thread for
  this deliberately agent-free investigation session.

## Open questions

Dominant storage consumers and retention reasons are being measured.

## Cleanup

Nothing deleted, garbage-collected, archived, stopped, or reconfigured.
