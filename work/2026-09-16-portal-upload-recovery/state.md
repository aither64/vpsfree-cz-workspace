---
lifecycle: active
---

# 2026-09-16-portal-upload-recovery

## Status

Implementation authorized; initial coordination session created. No project
changes yet. This external conversation owns the task; the managed session is
shell-only to avoid a duplicate writer.

## Next actions

Commit initial tracking, create isolated worktrees, implement and quick-test,
review, run browser/package acceptance, push/pin, deploy and verify.

## Documentation

Read generic documentation/handoff and user-facing writing skills plus the
complete English humanizer. Owning docs: codex-web README and dev-workspace
README attachment sections. Deployment evidence will be recorded separately.

## Repositories

Planned: codex-web, dev-workspace, vpsfree-dev-workspace, workspace and
vpsfree-cz-configuration. Branch/group: 2026-09-16-portal-upload-recovery.

## Commands run

- dev-session current: no current session; DEV_SESSION_SLUG unset.
- dev-session start portal-upload-recovery --no-attach --json: refused because
  noninteractive Codex startup needs a goal. Existing environment notes explain
  shell-only startup for an already-owned external conversation.
- dev-session start portal-upload-recovery --no-codex --no-attach --json: passed.
- dev-session current with matching slug and workspace environment: verified.

## Results

Planning reproduced the current shared component using a DOM test double and
mock HTTP client: Remove reissues rejected creation, never deletes, and reload
retains the card. Missing-file DELETE 404 also leaves a card. Source confirms
opaque UUID storage paths with a restricted extension; original filename is
metadata. No private emails were read.

## Open questions

The exact rejected filename was not supplied; the plan covers the reproduced
failure independently of which filename validation rule rejected it.

## Cleanup

Session and feature branches stay open. Preserve all unrelated shared workspace
changes. No archive, deletion, default-branch integration or delayed cleanup.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-16-portal-upload-recovery/
