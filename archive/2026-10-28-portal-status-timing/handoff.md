# Portal Codex migration handoff

All four approved feature branches have been merged and pushed to master.
The aitherdev reservation was released at 13:57:26 CET and its released state
verified. Post-merge runtime and codex-web CI passed. The initiative is complete.

The migration completed on October 29 at 13:27:47 CET. The original detached
unit exited 0; journal.json reports accepted, published=true and error=null.
The two earlier pre-publication failures are retained in the recovery history.

Automatic acceptance read all 2724 portal conversations, verified partition
counts of 2724 portal and 4360 stock threads, checked the exact native binary and
private storage, and restored activity data for both reported sessions. The
original confctl message `yes go ahead` was accepted with original attempt
`2a2656f4-3d35-4bee-9a71-14e20bc35669`, turn
`01a187a1-6581-7071-959c-20dca7142893`. Do not resend it again.

Fresh checks confirm portal/native/tmux services running, health HTTP 200, and
both activity endpoints returning timing. Chromium rendered actual Working,
Waiting and Idle durations for both affected sessions. This used a temporary
GET-only loopback proxy to the local operator socket; the external URL requires
user browser authentication and the ambient curl CA bundle lacks its issuer.
No browser mutation or additional message was sent. Autostart displayed Idle and
retains its execution hold. Historical totals remain approximate where past
observations are incomplete. The browser probe completed its assertions but
retained a streaming upstream connection during shutdown; its exact owned Node
process was terminated after browser closure.

Portal Codex 0.165 stores state in
`/home/aither/.local/state/dev-workspaces/codex-homes/vpsfree-cz`.
Stock CLI retains `/home/aither/.codex`; its managed daemon is running separately.
The two retained migration backups were subsequently deleted at the user's
explicit request, reclaiming about 32 GiB. About 88 GiB is now free. Both live
home identities were preserved; portal/native/tmux health and the fresh test
conversation passed post-cleanup checks. The original backup directories are no
longer available. Migration logs, journal, acceptance and verification records
remain, together with the private backup-cleanup.json completion record. The
publication hook had already been removed by the accepted operation.

A subsequent user-requested fresh live session test also passed: automatic naming,
initialization and the exact completed reply PORTAL_STORAGE_SMOKE_OK. Its thread
01a188a2-8d9b-7683-aaca-2309465aae3b exists in the private workspace state database
and its parsed assistant reply is persisted in the workspace rollout. The stock
state database has zero matching rows and no counterpart rollout.
[Test session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-29-portal-storage-smoke-test/)
is retained for inspection.

Final live acceptance confirmed read-only terminal attach/detach and both live
conversation/naming backends initialize successfully and select private SQLite
storage. Prior exact-native naming/provider tests and successful live stock
DeepSeek verification remain applicable to the unchanged binaries. No optional
new naming canary or dormant session execution was needed. The original accepted
confctl turn is independently present in current transcript paging.

- Unit: `portal-codex-home-migration-20261028.service` (finished successfully).
- Operation directory:
  `/home/aither/.local/state/dev-workspaces/maintenance/2026-10-28-portal-status-timing`.
- Evidence: `journal.json`, `acceptance.json`, append-only `switch.log`.
- Host configuration: `584691d9`, generation `2026-10-29--11-47-30`.
- Selected portal package:
  `/nix/store/d0wikyzpr7qk1w2c2zbqgj97qz1m58qn-dev-workspace-0.2.0`.
- Integrated heads: workspace `5fc7000f8`, runtime `cc0d452a`, codex-web
  `f6f4a187`, configuration `584691d9`.
- Workspace deployed `1cb755a3` is not literally an ancestor of master;
  independent review proved its patch-equivalent successor `5fc7000f8` and
  identical deployed derivation. See [integration-lineage-review-result.md](integration-lineage-review-result.md).
- Released aitherdev claim: `0f7f1a64-cb9b-480b-bdf1-345e77f1374a`.

The completed migration's original backup directories were removed under the
explicit later cleanup instruction. Retain the operation's logs/journals and
historical [rollout.md](rollout.md); do not rerun the completed cutover.
All final feature heads are integrated in their remote master branches. Every
short repository merge claim is released, and temporary merge targets were
removed. Feature refs/worktrees are retained. Runtime master CI 40877149430 passed
all four jobs; codex-web CI 40877082705 also passed. No delivery or requested
cleanup work remains. No session archival or reboot was performed. A future
deployment needs fresh machine ownership.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-portal-status-timing/)
