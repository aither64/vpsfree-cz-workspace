# Final affected browser-fixture review

Verified session2026-10-14-i-d-like-the-dev-workspace, workspace/home/aither/workspace/ai/vpsfree.cz.
Runtime worktree: worktrees/<slug>/dev-workspace. Complete deliverable committed,
clean110d1f71a6fd8671cc9316f509d61ed56cf740b3. Affected range:
6c7d3851b005b47357e43688efccddde56f4e53b ->110d1f71a6fd8671cc9316f509d61ed56cf740b3.
Complete own range832d9f1a6a21337dd44063ddf39f7a88cfc95450..110d.

Requested outcome remains global menu Enable/Disable/sound with title markers
independent, and focus-only existing-tab reuse. This revision changes only
portal/internal/web/notifications_browser_test.cjs. No product behavior/copy,
permission/subscription action, stored preference or native click logic changes.

Original accepted substantive review at53f plus direct sole-Advisory step9 at6c
is retained: notification-controls-review.md, -review-dispositions.md and
-source-gate.json. This is a new final review of the affected integration-test
correction, not a confirmation rerun of the Advisory remedy or unchanged source.
Risk medium: bounded hand-written browser test logic. Requested lanes: general,
architecture/repetition, scope/proportionality; retain prior risk/compatibility
conclusions for byte-unchanged product. Read mandatory skill/applicable references.
Retained reviewer0 Sol/xhigh/read_only; roster17 verified, no overrides/fallback.

First6c browser run FAILED without assertion location; fullflake unrun. Fresh
one-shot diagnostic on unchanged6c FAILED at297:65 expect(toggle).toBeFocused()
after pointer-driven sound save and Escape; knownCheckboxObserved=false. The
tracking-only preload changed only safeError in memory; all fixture actions and
assertions unchanged. Keep the original unlocated failure's cause unknown. See
notification-controls-browser-failure.md and diagnostic bundle/run/summary.json.
The native-popover/disabled-control focus precondition concern is source-supported;
actual pre-Escape active element was not captured. No physical/macOS cause proven.

Accepted architect addendum in design.md separates pointer dismissal from known
keyboard restoration. Final test keeps every sound persistence, panel rendering,
layout, no-load permission/subscription/API mutation and worker assertion. It now
asserts popover closed after pointer/save Escape, then explicitly focuses toggle,
opens with Enter, checks Operations autofocus/inside state, and asserts Escape
closed it and returned focus. Earlier keyboard test remains. No sleeps, timeout
increase, check/uncheck change or product refocusing handler. Keyboard focus
continuity through temporarily disabled save remains an unproved separate concern.

Quick: fixture syntax, all53 actual-module Node contracts, clean+range diff checks
PASS at110d; notification-controls-fixture-quick-status.json/logs0..3. No redundant
Go rerun (Go/template unchanged), no actual browser execution on new head yet.
Prior exact6c CI38773215915 fast PASS/host skipped is version-bounded history,
not new-head browser/package execution. Finite both-engine check follows review.

History: exactly9 logical commits, first7 deployed objects unchanged. Owning
eighth93d3f32f72705fb0f7e70cd66d92005ad172ea57 amended; ninth110d replayed with
unchanged stable patch-ID936d8a9b985a4f827b1ad03f85b0be742140cd62. Preserved
pre-fixture-final-6c7d3851/pre-fixture-controls-1630502 refs and all old packets,
failed logs and diagnostic. Inspect full series/final diff and concise implementer
fixture inventory when available; no redundant fixup or dependency stream added.
Source/import/module/vendorHash inseparable first boundary remains unchanged.

No migrations or format conversions. Additive optional sound singleton in existing
IDBv1 is already reviewed; new revision changes no persisted content. Supported
consumed6e1/4ed/469 state/keys/outbox/cleanup/coordination obligations remain.
6c is published but unconsumed as product. Current consumers still select469:
workspace1b2764bb77a6ebf2dc6e21e16a2ebe3ca656a1a0 after patch-equivalent rebase
onto72511fb2; configuration40172e5f on130. No110d composition supplied. Final
consumer/history review, preparation and ordered authorized activation separate.

Please return findings and explicit affected/history/migration conclusions only.
No tests/builds/browser/network/polling/nested agents/writes/operations. Keep
session and reservation1956d2a0 open. Lead persists report as
notification-controls-fixture-review.md. No merge/release/lifecycle approval.
