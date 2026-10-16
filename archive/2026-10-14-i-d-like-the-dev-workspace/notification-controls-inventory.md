# Browser-wide controls and click focus — committed handoff

Final runtime: `53f560fe3b898aa4544dae9376fcc7d6b1f33130` (tree `b68072c54f5ce069eba2dcd85ff78cabcd6cc647`), clean.
Eighth sound/menu commit: `74d3f0d9530755882b33b89a53e93c7feae5898f`; ninth focus-only commit: `53f560fe3b898aa4544dae9376fcc7d6b1f33130`.
Parent `469757183ba9491d642b56e91658dc64e390647b` and all seven deployed objects remain byte-identical ancestors.
No source publication, pins, browser/provider/host operations or lifecycle actions.

The eighth commit shares one per-document controller between workspace menu and
full panel, reuses explicit Enable/Disable compensation, and preserves independent
session mute/title/reservation behavior. One strict browser-local sound row lives
in existing IDB v1/sessions: boolean plus fixed MAX_SAFE_INTEGER retention rank.
The new pruner excludes its exact identity; the exact old pruner retains it.
Reads/writes wait for commit and are bounded; timeout aborts where possible.
Unavailable preference requests silent display. All four display branches read
once next to the native attempt, after prior status/receipt work. No audible retry.

The ninth focuses exactly one existing matching view, preferring target member,
without navigation, reload, member/section change or draft loss. Same origin and
strict session slug with optional final slash only; root is distinct. No-match
canonical authenticated openWindow/attentionIdentity path is retained. Focus
rejection/closed client never opens a duplicate. No worker ACK or Test return change.
The original physical Firefox/macOS cause remains unproved; user click acceptance
is separate. User-reported macOS popup visibility is user evidence, not code proof.

## Quick verification

- Eighth: direct Node **48/48 PASS**, five JS/CJS syntax checks, diff, exact focused
  Go `TestNotificationsPageIsSeparateFromIndex` PASS. See
  `notification-menu-final-quick-status.json` and numbered logs0–7.
- Ninth/final: direct Node **52/52 PASS**, three changed JS/CJS syntax checks and
  diff. See `notification-click-final-quick-status.json` and numbered logs0–4.
  Existing Go result binds unchanged template/Go files; no repeated Go run needed.
- Declared cached environment: v24.19.0,
  go version go1.26.6 linux/amd64. No Nix daemon/dependency acquisition.
- Browser fixture **PREPARED, UNRUN**. Both-engine native silent capability,
  shared index/session/menu/panel persistence, keyboard/mobile controls, no-load
  mutation and old-active/waiting-to-current takeover with retained tab/draft.
  Chromium-only synthetic worker options/correlation and actual click-listener
  no-navigation/draft plumbing. Synthetic focus may reject without trusted user
  activation; it does not certify physical Firefox/macOS tab selection or sound.

Initial sound-only/pre-menu checks remain historical stage evidence. The combined
menu test's preliminary failure was a harness synchronization error: WebCrypto
had not yet reached its two cleanup requests; fixed by awaiting those exact
request gates, not a timing retry. Preliminary logs remain preserved.

## Scope and history

Eighth owns 12 paths; ninth owns 5 paths, listed in freeze.json.
Complete **nine** commits are in `notification-controls-series.txt`; full final
base-to-head patch/stat and separate eighth/ninth/affected patches accompany it.
No obsolete new commits or pin streams. First seven remain because they are
supported deployed/consumed history; new8/9 are coherent separate user requests.
No migrations, dependency/vendorHash/lock/API/payload/server-format changes in8/9.
IDB database version/object store remain1/sessions with an optional reserved row;
previously absent data still reads default, corrupt present data fails silent.
The uncommitted two-field stage was never consumed; no dual-format reader exists.
Older loaded notification behavior is outside the new/refreshed-tab contract,
while its pruning cannot erase the new preference. Site data/keys are never reset.
Full earlier feature/private v1 and receipt lineage remains in preserved packets;
no earlier migration/source object was rewritten or removed.

Main direct vpsfree-user-facing-writing/Humanizer copy approvals applied to sound,
combined menu and click guides, with only their exact requested edits and wrapping.
Sound-copy and menu-copy snapshots remain earlier-stage evidence; committed patches
are the final authority. This packet requests retained affected independent review,
including whole-branch history/migration conclusion. **HOLD** publication, pins,
long/browser/provider checks and host/lifecycle operations until lead gates.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/
