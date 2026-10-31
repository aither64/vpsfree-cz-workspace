# Design and verification brief

## Clipboard filename follow-up

Approved behavior: number every pasted file from one, per original filename and
session, continuing across messages/reloads. Insert the number before the last
extension; dotfiles and extensionless files append it. Picker/drop names stay
unchanged. The lead owns this bounded shared-component change.

codex-web owns admission/name reservation and File cloning. Reserve names before
starting transfers, seed from the complete authorized upload catalogue and local
drafts, and retain per-name high-water counters beside the existing draft key.
Keep counters after submit/remove/clear. New scopes have their own sequence.
Trim generated stems at Unicode boundaries to fit 255 UTF-8 bytes while preserving
the extension. Retain sourceName in pasted draft entries; reselecting the original
file reconstructs its assigned name without changing IDs, size/checksum validation
or retry receipts. Browser metadata is additive; no server API/schema migration.
Old draft arrays remain readable. Old bundles ignore the new fields; a paused
renamed file must be selected under its assigned name in those bundles. Recovery
deploys a compatible forward fix under the existing package policy.

Quick provider contracts cover distinct bytes, batch admission, catalogue
collisions, counters across clear/remove/reload, recovery identity/prefix checks,
Unicode/length, legacy drafts and native mixed paste. Representative portal
browser checks exercise repeated image.png in both composers and a restored
creation draft. Publish provider, pin runtime, preserve extension, align workspace
and confctl inputs, review the full committed series, then run affected package
and browser checks, build/dry-activate/switch aitherdev and the separate user profile.
Live smoke is read-only; no banked reset or real session creation is used.

The lead owns this design and implementation (unmanaged/threadless initiative,
no retained team). The change uses xhigh design effort.

## Interfaces and ownership

codex-web owns `refresh.js`: exported immutable resource profiles and a small
notice controller with injected clock/timers, visibility reset and destruction.
Existing controllers keep their domain-specific scheduling and mutation recovery.
All ordinary portal refresh timings read the policy rather than scattered literals.
The shared sync controller coalesces resume hints using last successful freshness;
stream reconnection still demands a new authoritative read.

Automatic history repair retains existing cursor and generation safety and retries
read failures with capped backoff. Loading notices are reserved for manual reads.
All warnings use 30 continuous visible seconds, except access/user-action errors.
Initial loading uses 750 ms; manual history loading uses 250 ms.

Model selectors move into a native dialog, with one Save and a close control.
The bar renders the last server-confirmed pair independent of catalog refresh.
Drafts survive background reads, not dismissal. Save keeps existing idle checks,
atomic pair update and uncertain-write reread. Mode controls preserve their semantics.

`mountUploads` accepts a textarea `pasteTarget`. Clipboard Files use the existing
add path, preserving native text paste by never canceling a paste that contains
text. File items and the file list are alternative sources, avoiding duplication.
Listeners are removed on destroy. Clipboard text paths/URLs are not uploaded.

Account types preserve nullable/unreported credit details and reset detail rows.
The main codex bucket remains the selected allowance. The new reset client uses
`account/rateLimitResetCredit/consume` with UUID idempotencyKey and optional
creditId. Portal adds an exact-origin checked account-level POST. A verified
browser retry record is written before sending and survives response loss/reload;
unknown outcomes block new redemption attempts until the retained attempt resolves.
Account reads never redeem. Reset success invalidates the shared limits cache,
fences pre-mutation reads and triggers an authoritative read; never infer counts.
Confirmed redemption is operator-only; all tests use mocks with three credits.

## Compatibility and recovery

Optional account fields and browser options preserve old callers. Existing
conversation.Client is unchanged. No database, ledger, upload, manifest, journal,
runtime-authority or cluster schema migration. New browser bundles require reload.
The selected workspace Codex binary, not system PATH Codex, owns protocol checks.
Deployment order is codex-web publication, dev-workspace dependency pin, workspace
nested-runtime selection and matching confctl dev-workspace channel selection,
host activation, then separate user-profile package switch. Preserve the extension
and live Codex under compatible package switching. Recovery selects a newer fixed
package; the existing forward-only lifecycle policy remains in force.

## Acceptance and checks

Text paste remains native. Binary/mixed paste produces ordinary attachment cards
without duplicates and keeps Send gated on upload readiness. Background resume
retains values without banners for short failures. Persistent warnings expose
Retry. Model Save updates one confirmed pair; dismissal performs no mutation.
Sidebar displays optional credits/counts and a confirmed detail/next-reset action.
Expired rows are not actionable; authoritative count may exceed detail rows.

Quick: Node contract/syntax checks, focused Go tests, protocol corpus coverage,
format/hooks and diff checks. Account/browser fixtures cover reload retries,
duplicate submits, nullable fields, rejected origins and late cache results.
After committed whole-branch review: packaged Nix suites and real browser fixtures,
selected-binary schema validation, configuration build/dry-activation and deployment
smoke checks. Long checks use a fresh Luna/low watcher. Live limits checks are
read-only. No production reset-consumption request is permitted during testing.

## Review remediation

Reset actions use one origin-scoped Web Lock around the complete load/check/save/
consume/remove sequence for both Use and Retry. No Web Locks or unreadable storage
disables redemption. Other tabs learn pending attempts through storage events;
a Use click that discovers an unresolved attempt blocks rather than resending it.
Unknown outcomes retain the attempt. Automatic history repair resumes after a
background pause while failed manual older-page reads still require Retry.
The compact account dialog includes the ordinary allowance windows and reset times.

## Visual follow-up brief

This bounded portal presentation correction is lead-owned. Use existing colors
and typography: account lines match muted limit metadata, with a 12px top gap
and a small line gap. The summary is plain text. Information and pencil buttons
use 28px targets and 16px stroke icons, muted foreground, transparent background,
and visible hover/focus states. Keep Account details and Edit Codex settings as
accessible names and tooltips.

A shared portal formatter rounds finite numeric credit balances to whole
credits with locale grouping in both views. Preserve unlimited/unreported
fallbacks. Only display formatting changes; account JSON and redemption logic
are untouched.

Move the mode toggle and its status into the attachment/Send group, preserving
the existing attachment/Send/Queue order. Center both action groups vertically.
Keep the model summary and pencil together, with Interrupt beside them. Allow
groups to wrap without clipping at narrow widths. Keep stable element IDs and
controller ownership. Bump portal asset query versions together.

Existing browser fixtures will verify rounded balances, spacing, icon-only
accessible buttons, vertical centers and left-group placement at desktop/narrow
widths. Mock all account mutations. Retain the previous deployed heads as rollout
history; consolidate only unapplied corrections. No migrations or API changes.

## New-session clipboard correction

The approved bounded correction is lead-owned. Pass the Initial request textarea
as pasteTarget when mounting creation uploads. Reuse codex-web handling; keep
native text and mixed paste, readiness gating, tab-local persistence and frozen
creation recovery unchanged. No API or persisted-format changes or migrations.

Extend the existing usability browser fixture with the index form: actual
clipboard text insertion, binary image/file and mixed events, deduplication,
held-upload submission gating, reload restoration, file-only request encoding,
and immutable pending-request behavior. Use only the disposable server and
intercept all creation POSTs and account mutations. Bump app.js query versions
consistently and update the attachment README. No clipboard permission API is
added to the product. Retain already deployed commit history; publish the fix,
review the whole branch, check affected packages and redeploy matching host/profile
pins. No live reset use or default-branch integration.
