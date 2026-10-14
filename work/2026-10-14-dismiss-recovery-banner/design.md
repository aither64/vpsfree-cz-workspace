# Recovery notice dismissal

The lead owns this bounded design and application implementation. The reader is
the portal user who wants to browse a completed conversation without continuing.

## Interface and invariants

POST /api/sessions/<slug>/dismiss-recovery accepts {noticeId}. Recovery responses
add noticeId and noticeDismissed only for a waiting notice. The endpoint shares
origin/generation checks and the recovery operation lock; it verifies ordinary
session identity and refuses unfinished lifecycle work, changed identities and
non-waiting states. It never calls a native activation or submission method.

A separate private root-thread record uses existing atomic/synced record helpers.
Its identity includes the exact workspace/session tracking incarnation and native
socket epoch. Existing waiting sessions derive a deterministic initial notice ID;
successful runtime restoration assigns a fresh ID even if only tmux was lost.
Dismissal is idempotent for one exact notice. Existing execution-permission and
runtime contract schemas are unchanged. Corrupt/mismatched notice metadata must
never hide a banner. Stopped/recovering/failed states are never suppressed.

The browser displays a waiting-only X with an accessible label, persists via POST,
and hides only after success. Subsequent older reads of the same notice must not
undo a successful dismissal. The server supplies initial visibility to prevent
a flash on reload. Root and member pages share dismissal for this session.

## Verification and deployment

Focused Go tests cover repeated/stale acknowledgements, paused empty/queued/goal
states, read/restart persistence, socket/restoration reset, storage failure and
identity/origin refusals. Browser coverage verifies keyboard/mouse X, polling,
reload/failure, paused controls, unsent drafts and mobile layout. Quick syntax and
focused contract checks precede committed independent review. Packaged/Playwright
checks and builds follow review, under fresh verification watchers.

Publish exact branches; select the same dev-workspace revision in workspace and
configuration locks. Preserve extension/sibling selections. Check final deployment
composition. Build outside claims; admit system then user-profile activation using
coordinator jobs and the owning aitherdev reservation. Recovery uses the original
candidate or a compatible forward successor, never a backward profile switch.
Default-branch integration requires a separate explicit instruction.
