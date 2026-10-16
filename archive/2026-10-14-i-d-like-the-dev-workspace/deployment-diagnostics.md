# Prepared deployment: waiting for machine ownership

Status: approved and queued; no activation by this session.

Reviewed published heads:

| Repository | Head |
| --- | --- |
| dev-workspace | 0b403305e085aa01884cf56acea7c717f78f7e86 |
| workspace | 823d2b61b06de1a0cbe7e8b31b90f5907ecd7926 |
| vpsfree-cz-configuration | 0420df1c5272ff48441c14885a5f7fd042b5dcdb |

Source and final history/composition reviews pass. Applicable automated checks
pass: focused Ruby, full recovery VM (five scenarios/two reboots), required full
flake suite and exact-head CI. See verification-diagnostics.md. The historical
b8a6 failure remains unexplained; original evidence and new diagnostic limits
are retained. Physical/macOS display and actual click are not verified.

Machine and profile build/copy preparation both exited0. The initial wrapper
attempt failed locally on unsetPS1 before any coordinator call; the corrected
environment loader reused the unchanged requests. No hooks were bypassed.

| Preparation | Snapshot |
| --- | --- |
| Machine | sha256:c844583ba9e9a85ffae18e45ffa3979770f16cebaebc313ff8a4b3ef02daeb61 |
| Profile | sha256:7905794f6d4d079f5f978ad95c5611a992d227deaae7cdb07a3f1036cfc9a850 |

Candidate application package:
`/nix/store/6c8sb9k5b601c821mphi2ahdw2a6lfvl-dev-workspace-0.2.0`.
Prepared coverage matches all reviewed heads and unchanged extension/Codex pins.
The selected predecessor is hycsrx1 under catalog26007c67; full exact values and
expected live identities are in machine/profile-diagnostics-prepared.json.

Fresh approvals use the actual retained user instruction authorizing aitherdev
deployment, without default-branch integration or reboot:

- machine8bb5b35b-ad39-413e-909e-57f073c40acd
- profile882727ff-d844-4324-b8bc-5b16f384f5b3

Ordered jobs under existing requested reservation1956d2a0:

| Job | ID | State at coordinator revision586 |
| --- | --- | --- |
| Machine activation | 2e8a96bc-ff7d-4cf9-82bd-fa9277528cd0 | waiting_resource, foreign machine ownership |
| Profile activation | 19311887-f1d8-497d-89a2-dce6b5926f1d | waiting_dependency on machine job |

Aitherdev remains in integration-performance's deployed_review hold. Resource
contention is not a failed check. Keep waiting interruptibly and read status when
steered. If the accepted frontier changes, refresh the affected source/review/
preparation before activation. Do not bypass ownership or use old snapshots.
Previous canceled jobs and their evidence remain intact.

After exact successful activation, use live-native-0b403305 with
LIVE_PROFILE_PREPARED naming the genuine profile-diagnostics-prepared.json.
The fixture refuses stale proof, checks selected package and served asset hashes
before Enable/Test and afterward, and preserves uncertain cleanup profiles.
No live browser/credential/subscription operation has run from this fixture yet.

No default-branch merge, reservation release or session lifecycle action is
authorized. Keep the session active/open and preserve all snapshots and receipts.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/
