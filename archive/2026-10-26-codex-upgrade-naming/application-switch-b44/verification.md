# Naming-high deployment verification

Passed bounded read-only verification at 2026-10-27T18:17:57.962249+00:00. All synchronous checks returned successfully; no watcher or asynchronous verification was launched.

- Actual original switch receipt: exit 0, 71.236 seconds, 2026-10-27T18:14:13.169904+00:00 to 2026-10-27T18:15:24.405520+00:00. Original PID `2726830` no longer exists. Evidence: `switch.meta`, `switch.exit`, `switch.log`.
- Selected profile/workspace-host and actual running portal/router: `/nix/store/yi4hlb3s8lmm8w2bv34z35yhy6fmqk29-dev-workspace-0.2.0`. Portal PID `2729478`/start `1243262252`, router `2729342`/start `1243260095`, active/running and exit status 0. Exact producer `/nix/store/mxjsrcc523ir5kswgh7np50a42xsw8cg-dev-workspace-0.2.0.drv` uses `/nix/store/f9a2xjlviyvw12a64mq4q0l1lscwa5y8-source`, the previously accepted immutable **b44/Luna high** source. No live naming inference was used to establish effort.
- Native retained: PID `3555077`, start `1241457907`, actual `5rm5…/libexec/codex/bin/codex`. Tmux `435397`/`842484713` and user manager `4239`/`4036366` unchanged from owner1's recent snapshot. Portal/router restart is expected; native and terminal manager did not restart.
- Both system pointers match `/nix/store/zdjxfv18sgqndks3ijzlfnfb2psz7b0x-nixos-system-aitherdev-26.05.20261026.718f670`, accepted clean configuration `843be64072f04e6352447980a26dbf68bb0666e0`, generation `2026-10-27--18-53-57`.
- Public portal Unix health and canonical-Host router Unix health: HTTP 200, `{"ok":true}`. Own session page and served `app.js?v=61`: HTTP 200. Asset equals immutable b44 source bytes, SHA256 `2f3e7f46c4f39cf3b65ce969614bee3cb7d79f498961947c40b0f359eb3c7e06`.
- Exact claim `2ecc0cfa-f985-4b77-91de-38b36eeab0fc` remains held by `a846b5e2-83c9-4675-96f7-c5e5af8c1165`, revision 1; untouched.

Actual evidence: `status-after.txt`, `services-after.txt`, `user-manager-after.txt`, `identities-after.json`, `producer-after.txt`, `producer-source-after.json`, `claim-after.json`, HTTP body/status files and `effects-after.json`. Owner1 baseline: `../configuration-system-deploy-b44/before.json` and `effects.json`.

## Limits

The public interface has no exact pending-transition status reader. No private pending file was read and no absence is inferred from historical inactive units; successful original completion and exact actual identities are the completion evidence. Root-owned user-manager executable is unreadable; PID/start/service continuity is verified without privilege. Known TLS issuer failure was not repeated or bypassed. No JavaScript, send, Continue, dismiss, CPU/foreign-session read/action, naming/provider inference, test/build or probe was performed. Later UI work is a separate milestone. No source/Git/selection/reconciliation/claim/merge/release/lifecycle mutation was made by this verification.
