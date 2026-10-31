# Final review: New session clipboard attachments

Initiative 2026-10-09-portal-codex-usability, created by this conversation,
threadless without a retained roster. Parent owns design and application code.
Read plan.md, design.md, state.md and final-inventory.md. Worktrees are under
../../worktrees/2026-10-09-portal-codex-usability/. The inventory gives all four
exact bases/heads, complete 14-commit series and final diffs. Earlier 11 commits
were deployed, so retained as consumed provenance. No unconsumed fixups,
obsolete approach, compatibility shims or migrations.

## Requested outcome and boundaries

Binary files/images pasted into New session Initial request become ordinary
attachments, like existing session messages. Native text insertion/undo and
mixed clipboard default behavior stay intact. Existing readiness gates, file-only
requests, scope/IDs, tab-local persistence and frozen recovery stay intact.
Creation mount omitted pasteTarget; the bounded fix supplies form.elements.goal.
No shared handler, API, state, permissions or protocol changes. No clipboard
permission prompt is added. Existing limits/quotas apply. Early paste before
upload initialization retains the existing handler behavior; no new buffering.

## Changes and evidence

Runtime fbf3493 adds the mount option, directly supporting browser coverage,
README clarification, and app.js v28 cache references. Workspace/config exact
runtime pins are separate generated/consumer commits. Only dev-workspace and
respectively devWorkspace lock nodes changed; provider 860d515 and extension
0ff827df remain unchanged. New browser case uses the disposable server; every
creation POST and account/reset mutation is intercepted. Real keyboard text
paste/undo, image/binary/mixed events, deduplication, held PATCH gating, reload,
file-only body scope/IDs and locked pending recovery are covered.

Quick checks pass: Node syntax for app/fixture, git diff --check, focused Go
ResetCreditBrowserContracts/AutoArchive/NewSessionSettings/Preparation tests
(0.245 seconds), config Nixfmt/message hooks. Composition checker passes at fbf3493.
Sources are committed, clean and published. Long browser/package checks and
exact CI 37962866775 follow this review; do not treat them as already passed.

## Review policy and deployment

All four lanes: general, architecture, scope, risk/compatibility. Overall high
because matching deployment/composition is included; code correction is bounded.
Reuse independent reviewer 01a120fd-34cd-7272-8ae1-1222ee2f1773; native metadata
verified gpt-6-astra/xhigh, matching current installed lead_reviewed catalog.
Session roster command refuses because this intentionally threadless initiative
has no valid lead thread; do not create or reconfigure a team. Reviewer remains
read-only and performs all lanes itself, with whole-history/no-migrations
conclusions. Trusted local operator boundary from local AGENTS applies.

README Prompt attachments is the owning feature explanation. Session rollout.md
owns exact operations/history. Reuse existing host dry-activation/switch followed
by separate workspace-host user-profile switch; preserve native Codex and all
three actual resets. No live reset redemption or test session creation. No
merge/default-branch approval. No destructive cleanup.

## Post-review narrow fixture remediation

Review was performed on the fbf3493d/39c2f260/5733563c snapshot. The first real
browser run then exposed the harness's old derived trusted origin; it now uses
its actual TLS fixture origin before serving. Parent inspected the one-line
harness-only change and reran quick checks under review step9. No product,
API or ownership change. Only unconsumed source/pins were consolidated. Current
inventory/diffs identify c650a4c7/97ab907c/557c97a7; series length remains 14.
Config generated history remains, with its net predecessor corrected after
consolidation. Exact current CI 37963716009 and fresh retry watcher are active.
Failed run and diagnosis are retained in state.md and review.md; no broad review
rerun is needed for this narrow test initialization correction.
