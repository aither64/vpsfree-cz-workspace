# Portal Codex migration handoff

Host deployment, implementation, independent review, native/browser checks and
final CI passed. The portal application has not switched yet. Its detached
migration is waiting for native work to become idle and stock CLI PID 3584002
(pts/349, Codex 0.165) to exit normally. This is likely the current chat's CLI.
Do not kill it or stop portal tmux sessions. Keep stock clients closed through
cutover. User-manager linger is enabled, so logout does not cancel the job.

- Unit: `portal-codex-home-migration-20261028.service`.
- Operation directory:
  `/home/aither/.local/state/dev-workspaces/maintenance/2026-10-28-portal-status-timing`.
- Status: `journal.json`; detailed switch output: `switch.log`; automatic
  acceptance and original-message receipt: `acceptance.json`.
- Portal home: `/home/aither/.local/state/dev-workspaces/codex-homes/vpsfree-cz`.
- Stock home remains `/home/aither/.codex`.
- Held aitherdev claim: `0f7f1a64-cb9b-480b-bdf1-345e77f1374a`.

Read status with:

```sh
systemctl --user status portal-codex-home-migration-20261028.service
cat /home/aither/.local/state/dev-workspaces/maintenance/2026-10-28-portal-status-timing/journal.json
```

The job performs the ordinary claimed workspace switch and retained-data split,
verifies all portal histories and both reported activity endpoints, then retries
`yes go ahead` in `2026-10-17-confctl-rust-rewrite-plan` with original attempt
`2a2656f4-3d35-4bee-9a71-14e20bc35669`. It never creates a second attempt ID.
An `accepted` phase means these automatic checks and the durable accepted message
receipt succeeded. Live browser/tmux/provider/naming checks still need observation.
If the unit fails, inspect its journal and journalctl output and resume this exact
operation under [rollout.md](rollout.md); do not replace the job, clear evidence,
restore an old home over new writes, or downgrade the workspace package.

The host is verified on configuration 584691d9, generation 2026-10-29--11-47-30.
The portal candidate is `/nix/store/d0wikyzpr7qk1w2c2zbqgj97qz1m58qn-dev-workspace-0.2.0`
from workspace 1cb755a3, runtime cc0d452a and codex-web f6f4a187.
Keep this source checkout/head unchanged while the detached operation owns it.
Original homes are retained at the operation's partition/stock and partition/portal
paths after publication. No backup deletion is authorized.

All feature branches remain unmerged. Keep the initiative active and the machine
claim held through acceptance and explicit approved lineage integration. No reboot,
forced interruption, session archival/deletion, master integration or backup cleanup
was authorized.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-portal-status-timing/)
