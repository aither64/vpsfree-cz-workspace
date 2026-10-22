# 2026-10-22-aitherdev-log-rotation

## Goal

Track this conversation and prevent unbounded growth of aitherdev's local
rsyslog files. The investigation found a 20.3 GiB messages file, missing
rotation, and a repeated Codex error responsible for most recent growth.

## Affected repositories

- vpsfree-cz-configuration: host configuration and reusable operations docs.
- This coordination workspace: initiative records only.

## Approach

Use branch/worktree group `2026-10-22-aitherdev-log-rotation`, starting at
configuration `origin/master`. Add one host-local logrotate rule in
`cluster/cz.vpsfree/machines/aitherdev/config.nix` for messages, warn, mail,
and dhcpd. Rotate daily or above 100 MiB, retaining 14 numbered archives.
Enable compression with delayed compression, missingok, notifempty, inherited
file ownership/permissions through create, and sharedscripts. Send HUP to
the main process of syslog.service using the pinned systemd executable.
Retain the existing hourly timer and existing unrelated rules.

The lead implements this bounded configuration change. The tracking-only
initiative has no native lead thread or usable retained roster; use the
mandatory-review standalone fallback and the installed utility policy.

## Decisions

- User selected 100 MiB and 14 archives during planning.
- Scope is aitherdev only; no shared logging-module policy change.
- Do not truncate logs, force rotation, fix Codex, activate a configuration,
  or archive this initiative. Master integration was initially separate from
  implementation; the user subsequently approved it with "ok, merge it".
- Use existing logrotate validation rather than adding a permanent test suite
  for a small declarative policy change.

## Compatibility and deployment

No input updates, schemas, migrations, public API/CLI or wire-format changes.
Existing files are renamed and recreated during ordinary rotation; HUP makes
rsyslog reopen them without restarting the daemon. The existing oversized file
rotates after a separately authorized activation at the next hourly invocation;
delayed compression leaves its newest archive uncompressed until the following
rotation. Size can overshoot between checks and 14 archives need not mean
14 days. A rollback can read existing logs but cannot restore expired archives.
Deliver the reviewed change on configuration master using the subsequently
approved fast-forward integration. Live activation still needs separate direction.

## Documentation

Extend `docs/operations/aitherdev-disk-retention.md` for operators, covering
policy, inspection, timer granularity, first rotation, and recovery limits.
Keep individual verification and rollout evidence in initiative state/artifacts.

## Testing plan

Run nixfmt and Git whitespace checks, inspect evaluated/generated logrotate
configuration for the four paths and all policy directives, and use logrotate
debug mode without changing live logs. Commit the complete change and obtain
independent final review before running the required aitherdev confctl build.
Use a fresh catalog verification watcher for the uncertain-duration build.
Publish the feature branch, capture its comparison, and integrate the exact
reviewed head after the user's explicit approval. Verify remote master and
release the short repository claim before cleanup and handoff. Complete the
initiative once all requested work is done; retain the session and feature refs.
