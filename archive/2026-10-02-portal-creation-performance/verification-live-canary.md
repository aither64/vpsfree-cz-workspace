# Deployed portal creation canary

Passed on 2026-10-03, wrapper exit 0. The supported user-profile switch selected
`/nix/store/xl9mvbb5j19anfbx6qj3lrw8k7a9vnz2-dev-workspace-0.2.0`. Parent verified
all four workspace user services and nginx active, the selected Codex unchanged,
36 retained root identities and all three owned member identities/settings exact.

A fresh Luna/low utility ran one real Full-team creation through the production
portal API, using its Unix socket and canonical Host/Origin. It retained the
canary session `2026-10-03-portal-creation-performance-canary`.

| Measurement | Result |
| --- | --- |
| History before creation | 3,482 active and 79 archived rollouts |
| Accepted | 2026-10-03T07:32:23.344408583Z |
| Ready | 2026-10-03T07:32:30.907336925Z |
| Acceptance to ready | 7.562927961349487 seconds |
| Acceptance to first assistant | 10.037591934204102 seconds |
| Ready to first assistant | 2.4746639728546143 seconds |
| Assistant turn completed | 2026-10-03T07:32:33.430Z |

The root and three members reached ready with the frozen Full preset. Exactly
one initial user message was present, the model completed its turn, and no tools
were used. Live phases included preparing the session, conversation initialization
(0.3 seconds), terminal setup, each of the three members and initial-request
submission. Final readiness required the normal receipt/manifest/roster proof.
No retry, replay, interruption or cleanup occurred.

The deployed runtime is 924c0ec2, SDK 4c170393 and extension 8f8d8ecf. Workspace
source 1b670e03 built the package; the subsequent clean rebase 93389c33 is
patch-equivalent and evaluates to the same exact xl9 output. No new package or
activation was needed for that coordination-only base advance.

Full result, status and events remain in the initiative's private verification
directory under live-canary. Result SHA256:
`ddfc582347cd5d841d7cc6147e21fa8e8ae8d261dfb448718d9ad7c527827a50`.
The five isolated measurements remain separate evidence at their original
candidate; this is the final-package measurement against actual production history.
