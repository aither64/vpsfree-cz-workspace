# 2026-10-09-portal-codex-usability

## Goal

Make portal background refreshes quiet, show current model/reasoning as text
with an Edit popup, show credits and banked resets with confirmed redemption,
and attach binary clipboard data without changing native text paste.

## Affected repositories

- codex-web: shared refresh policy, clipboard uploads, compact settings, account
  response and idempotent reset-consumption client.
- dev-workspace: portal consumers, sidebar/reset UI and HTTP account endpoint.
- workspace: select the composed runtime, preserving the extension revision.
- vpsfree-cz-configuration: match the dev-workspace channel and deploy aitherdev.

## Approach

Use resource-specific profiles in one documented browser refresh policy.
Retain successful values and suppress routine background loading notices.
Warnings appear after 30 continuous visible seconds; initial loading after
750 ms and manual history loading after 250 ms. Preserve current polling rates.
Distinguish automatic history maintenance from explicit older-page navigation.
Use a modal settings draft with one atomic Save. Reuse existing upload storage,
limits, progress, retry and durable prompt-attachment handling for clipboard files.
Expose optional account credits/reset details and a guarded reset POST. Persist
the same UUID through retries and reread authoritative limits after redemption.

## Decisions

- Shared code tuning, no preferences screen.
- Closing/Escape discards unsaved model changes; bottom bar has no Apply/Cancel.
- Count-only reset reports may offer confirmed next-available redemption.
- Preserve native text paste, including mixed text/file clipboard payloads.
- Never consume actual reset credits during verification; use mocks with three.
- User requested implementation and deployment; default-branch integration is
  not authorized. Publish feature branches and retain an active initiative.

## Compatibility and deployment

Account/browser interfaces are additive. Keep old account responses usable.
No database, manifest, submission-ledger or upload-format migration is intended.
Validate request/response shapes against the selected workspace Codex package,
currently 0.160.0, rather than relying on system Codex 0.160.1.
Publish codex-web, pin it in dev-workspace, then select the runtime in the
workspace nested input and the configuration dev-workspace channel. Preserve
the vpsFree extension. Check composed locks, build/dry-activate aitherdev, deploy
the host configuration, and switch the separate workspace user-profile package.
Use the forward-only package recovery contract; retain previous state formats.

## Documentation

Owning project references explain refresh tuning, settings editing, reset
safety and clipboard behavior. A session rollout record retains exact pins,
commands and deployment evidence. Readers are maintainers and portal users.

## Testing plan

Fake-clock browser tests cover visibility/focus coalescing, delayed notices,
cancellation, retry and stale-result fencing. History tests retain scroll and
older-item updates. Settings tests cover drafts, atomic Save, dismissal and
uncertain writes. Mock account tests cover three resets, partial details,
expiration, confirmation, reload/idempotency and cache races. Clipboard tests
cover binary-only, text-only, mixed and multiple files and upload limits.
Quick checks precede mandatory committed whole-branch review. Longer checks
use the verification watcher. Deployed account verification is read-only.
