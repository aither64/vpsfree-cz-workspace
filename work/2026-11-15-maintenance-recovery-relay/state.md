---
lifecycle: active
---

# Maintenance recovery communication

## Status

- [x] Create native endpoint and verify active, unheld conversation.
- [x] Record approved exact pair and deliver repair plus review evidence.
- [x] Original lead accepted rollout ownership and reported source-first order.
- [ ] Receive actual source and final activation results.
- [ ] Verify final profile/native/portal effects in the external conversation.

Native thread: `01a1dc60-d09b-7982-adc1-f96626469181`.
Pair grant: `f38332bbf46704fcfd4f518cf999b356`.
Peer: `2026-11-11-session-archival-failures`.

User authority is the external conversation's 2026-11-14 message beginning
“well, resolve it...” and saying “you can communicate with that session if
needed... I want it to successfully finish its job. you can track this session
if it is needed for communication.” The exact pair was installed with that
quoted source through ordinary `dev-session communication allow`.

The external repair conversation owns plan/state/portal records. The native
endpoint owns only [peer-status.md](peer-status.md). No application worktree,
machine/repository claim or deployment action belongs to this endpoint.

## Evidence and next action

Original maintenance `b4682829-f783-4cb1-91e1-5b4b39a4b77b` is cancelled at
revision55 with continuations and restoration complete. Portal recovery is
active and executionHeld false; source services remained unchanged. See the
[repair record](../2026-11-14-maintenance-recovery-coordination/state.md) for
exact package, checks, review and CI evidence.

Messages d461b3ce-af3a-49d2-8bca-e7c6abf9f44f (initial repair),
351faab5-3e0b-4ac9-817a-b769e53e4414 (CI finding),
be71501f-f0b3-45f9-b8f9-4717fd73aad0 (test correction/checkpoint), and
9248f1c3-24f7-4096-a651-e5177f08e069 (review disposition) were delivered.
Original lead checkpoint: 27fda6f7-285a-43c2-90c6-d82646378316.

The original lead's architect/source owner are composing repaired same-native
D/e32 and final349 successors. The intended order is compatible source
selection, ordinary full activation to the already-testedp71 artifact, then the
final repaired observer-aware policy2 composition. Await deliberate milestones;
no additional live repair was requested here. Completion remains unclaimed.

Stable URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-15-maintenance-recovery-relay/
