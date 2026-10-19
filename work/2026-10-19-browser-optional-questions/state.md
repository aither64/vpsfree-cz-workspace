---
lifecycle: active
---

# 2026-10-19-browser-optional-questions

## Status

Implementation coded; focused checks passed. Preparing final dependency pins and independent review.

- [x] User interaction and protocol design agreed.
- [x] Create isolated initiative/worktrees.
- [x] Implement codex-web and portal support.
- [x] Quick checks and initial committed independent review.
- [ ] Final remediation review and longer checks.
- [ ] Longer verification and feature publication.
- [ ] Matching pins and coordinated aitherdev deployment.
- [ ] User review / explicit integration direction.

## Next actions

Commit initial tracking and design. Implement shared question state and controls.

## Documentation

## Repositories

Branches and worktrees all use 2026-10-19-browser-optional-questions. Bases:
codex-web c064ce09; dev-workspace 09a40795; workspace da70912a;
configuration 91639dec. Paths are worktrees/<slug>/<project>.

## Commands run

## Results

No bound current session existed; created this initiative with --no-codex and
--no-attach. Session has no managed roster/lead; preserve threadless ownership.
Configuration worktree checkout succeeded but post-checkout Overcommit failed
outside Nix due to absent bundle. Repair/register from its Nix shell; do not
bypass hooks. Initial tracking belongs only to this initiative.

## Open questions

No product questions remain. Installed workspace-host currently exposes an
older coordination CLI; investigate selected package before deployment, never
bypass machine reservations. No merge approval.

## Cleanup

## Implementation and quick verification

codex-web 803e877c84ec4139e03192699f24af0f350e52ae committed and published.
Added shared optional-question controller/controls and additive transcript fields.
Portal integration and actual-template Playwright regression are written.
Focused Codex async/request-user-input Go tests passed. Existing conversation,
HTTP authorization/response and paging browser contracts passed. Portal focused
Go source-file tests passed using local codex-web and then the published module.
JavaScript syntax checks passed. Broader browser tests await independent review.

Quick command corrections: Nix shell needed gcc for cgo; a temporary Go modfile
requires running go mod edit from portal/, not the repository root. The existing
portal browser_contract_test.cjs needs a server URL and runs through Go's browser
harness, not directly via node --test. These errors were resolved; no hook bypass.
Configuration Nix shell installed Overcommit successfully and registration now
includes its original 91639dec base. Workspace tree is isolated; preserve all
unrelated shared-root changes.

Aitherdev is currently held by lifecycle-lock-reliability. Status is a wait, not
a test failure, and does not authorize bypass. Keep preparing verified delivery.
This conversation is external and threadless: ordinary start without --goal-file
refused as expected; no new native agent was created. Deployment admission will
need the ordinary managed session identity, not a bootstrap owner.
Disposable vendor path: /tmp/2026-10-19-browser-optional-questions-vendor.

## Final review phase

Independent final review launched with standalone Astra/xhigh selected from the
installed default review-purpose role. General, architecture, scope and risk
lanes apply (High: native reply/public transcript, browser persistence and deploy
ordering). Reviewer /root/optional_questions_review is read-only and independent.
Packet/inventory/diffs are in this directory. No migrations, no prior deployment.

A further quick shipped-browser contract found the new questions.js dependency
missing from its temporary module fixture. Fixed the fixture asset list and the
standalone repository-browser asset server, then both targeted quick tests passed.
Folded test-only correction into runtime f2b3e82 (published exact head follows).
Initial review is bound to original db17a984; reviewer is inspecting committed
source; reconcile final delta and generated pin replacements before readiness.

## Independent review findings and reconciliation

Report: independent-review.md. Reviewer found Important R1 (native idle during
unfinished turn permanently unpinned questions) and R2 (definitively rejected
oversized/local failures left an immutable uneditable retry). Both fixed in
codex-web 641907fb3afa2977050fe61331f9a3411c091245, folded into the feature commit.
R1 now uses terminal turn status/current turn identity; idle/sleep/reload/return
regression passes. R2 checks complete UTF-8 encoded envelope against consumer
budget and keeps new locally failed/HTTP400/413 rejections editable; uncertain
network retries retain their identity. Regression tests for all cases passed.
The portal supplies its actual 20,000-byte budget. Parent also fixed custom-client
question storage namespace to use the canonical endpoint identity, matching
existing durable sends. That public-helper change merits affected-lane follow-up.
No original reviewer finding was accepted unresolved. Review explicitly found
no obsolete history, repeated update streams, or migrations.

Current codex-web feature CI: 39320306357 at 641907fb in progress; older
39318379571 at 803e877 completed success. No superseded active run to cancel.

Final committed ranges are in final-inventory.json (one logical commit per
repository), with exact complete *-final.diff. codex-web 641907fb, runtime
911ed529, workspace 29723cf4 and configuration fb6e8929. Final matching-lock check
passed. Original pin updates were consolidated; no deployment consumed earlier
heads. Independent reviewer assigned affected-lane follow-up of final remedial
public-helper/consumer changes under the same saved Astra/xhigh identity.

CI evidence: original runtime db17a984 run 39318730038 failed because the
shipped-browser temporary module fixture did not serve questions.js; its logs
confirm the same failure fixed in f2b3e82. Final runtime 911ed529 run 39320488089
is separate. Cancellation of obsolete active run 39319375729 was attempted per
policy, but GitHub returned HTTP403 (token lacks workflow-cancel access); do not
claim cancellation. No rerun was used instead of diagnosis.

Final remediation review completed with no findings at exact final-inventory
heads. Same independent reviewer confirmed history, pins and no migrations.
Long check utility launched as fresh native 01a155e4-e41e-7dd0-9e32-2622a7f0bd0d
with installed verification_watcher behavior and gpt-6-luna/low, explicitly
danger-full-access/never. It owns run-verification.sh and its process handle.
The parent is not polling its underlying tests.

A genuine ownership handoff is now needed for deferred aitherdev coordination:
the threadless initiative must gain an ordinary native lead. Runtime requires
plan/state/manifest equal their committed baseline before this supported creation.
The following coordination checkpoint records actual code/review/check state
and is allowed by the session procedure's ownership-handoff exception.
