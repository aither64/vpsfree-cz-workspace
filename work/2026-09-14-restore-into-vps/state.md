---
lifecycle: active
---

# Restore into VPS — investigation

## Session and repositories

Verified DEV_SESSION_SLUG and dev-session current both identify
`2026-09-14-restore-into-vps`. No project branches/worktrees created; inspected
immutable temporary exports of fetched canonical bare repositories.

- vpsadmin origin/master: `f7a17d6e512f0b11e2c908813eb2e780261e20ae`.
- vpsadminos origin/staging (remote default):
  `0beff55b8529b7c33992eeebab82cd9df0f5b53a`.
- vpsfree-kb-contracts origin/master:
  `919577d0c770e47b623c591f8bf0cce4e8d30666`.
- vpsfree-cz-configuration origin/master:
  `b0bb82d13159ce0da15375acf0483ab58572824a`.
- Older vpsadmin-kb-captures bare clone resolves to the same contract commit;
  use the canonical vpsfree-kb-contracts project for implementation.

## Status

Investigation complete; implementation not begun. See `investigation.md` for
source evidence, proposed behavior, alternatives, rollout and test scenarios.

Key findings: current restore is per-dataset rollback preserving descendants;
DatasetTree is per-dataset backup history; GroupSnapshot is scheduling membership;
no historical VPS configuration is stored on Snapshot; from_snapshot transfer
continues to newer data; cross-VPS import needs destination Snapshot identities;
local retention is one snapshot and ordinary rotation can expire old imports.

## Commands and verification

Read workspace/relevant repository rules, handoff skill and canonical KB WebUI
workflow. Fetched affected repositories over SSH. Used git show/archive and rg
for source/spec inspection. Consulted primary OpenZFS documentation and public
KB pages. No implementation or member-facing pages changed, so no tests, CI or
mandatory committed-code review ran. That review is required for implementation.

Checked shared workspace status/index and fetched origin before the initial
research/tracking commit; unrelated changes remain untouched. No hook framework
is declared in the shared coordination checkout. Verified all 19 unique pinned
repository source links, active front matter and artifact registration.

`dev-session artifact --help` is unsupported. Confirmed the runtime manifest
schema accepts artifacts with label and relative path; registered the report
in this session's portal.yml. An initial apply_patch combining delete/add of the
same file was rejected before changes; tracking files were then written directly.

## Open decisions and next step

Discuss restore modes and retention policy. Recommend snapshot-set metadata and
manual atomic capture, then new-VPS restore, then root-only overwrite. Full
hierarchy replacement needs topology-generation and recoverable-switch work.
Decide baseline lifetime/storage budget, pre-overwrite recovery window, and
application-quiescing scope. Prototype empty-container import ordering, mapping,
full OS identity and cutover behavior before promising no vpsAdminOS changes.

## Session remains open

No code pushed, KB written, pins changed, systems deployed, clusters allocated,
or lifecycle actions performed. Temporary source exports remain reproducible
research material outside tracking. Durable artifacts are plan, state, report
and portal manifest. No source credentials or bulk captures were recorded.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-14-restore-into-vps/
