# Deployment preparation watcher report

- Result: **passed**. The driver exit marker is `0`; system preparation exit is `0`; profile preparation exit is `0`.
- Run identity: parent-owned `run-deployment-preparation.sh`; PID/process group `3512563` from `deployment-preparation.pid`. The watcher only observed it and did not launch, resume, approve, deploy, diagnose, retry, or cancel it.
- Elapsed time: approximately **3 minutes 38 seconds**, from PID record timestamp `2026-10-20 11:53:35.974 +0200` to driver exit marker timestamp `2026-10-20 11:57:14.230 +0200` (UTC 09:53:35–09:57:14).
- Exact source revisions: configuration `316a071cd6cc3dd090661edac5a0e8d0d927d2c5`; workspace `0383f0bc057e81b6a96acef6ede63ab95e7522bc`; runtime/dev-workspace `1395387ff02729256ba52cc7c9ded74397cbe1a6`.
- System preparation produced prepared artifact `sha256:e034b9c5e706021eaf7643d5a48f6e701d02c4a69d8f91f28f4581d9367337ee` for `vpsfree:aitherdev`.
- Profile preparation produced candidate package `/nix/store/p4snvm49g56zn23qfxh5d29xfv2x31hl-dev-workspace-0.2.0`, artifact `sha256:52f9859a38a966b1d7e17af481de1bf4595eb89206e2f30fc513443d1160ca9f`, with expected profile token `508669d8eb26674a96ac88f8bdc90783b9f0bded95917529b7d3ed79b28b7b02`.

## Evidence paths

- `deployment-preparation.pid`
- `deployment-preparation.exit`
- `deployment-system-prepare-request.json`
- `deployment-system-prepare.exit`
- `deployment-system-prepare.log`
- `deployment-system-prepare.stdout`
- `deployment-profile-prepare-request.json`
- `deployment-profile-prepare.exit`
- `deployment-profile-prepare.log`
- `deployment-profile-prepare.stdout`

Profile log excerpt: `Codex App Server protocol contract is compatible`; `local semantic observation protocol contract passed`; `compatible Codex: 0.163.0`. No failed exit or unexpected local kernel build was observed. No operation remains running; no cancellation was taken.
