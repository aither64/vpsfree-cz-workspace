# Archive content integrity rollout

Status: host and application deployed, live acceptance passed, all three exact
reviewed feature heads merged and pushed. User excluded waiting for post-merge
CI; its remote run remains in progress. No deployment or observation is running
locally.

Runtime `9f999f7f713557b261a3d6d1597f8372eabf6518`, workspace
`4d0c62626c36332f7013ba8ff15c52a6f37e0218`, configuration
`23412037590f1d31b85a53410946a18b36db8bc8`. Both consumers select the same
runtime. Extension, Codex, Nixpkgs and sibling inputs stayed fixed. No schemas
or migrations changed. Final runtime/composed flake suites, real Chromium/Firefox
regression, matching host build and exact feature CI `37644340497` passed.
Independent review/direct findings are in [review-report.md](review-report.md).

## Activation performed

From the exact configuration feature worktree, through its Nix shell:

```sh
confctl deploy --yes --no-interactive --dry-activate-first cz.vpsfree/machines/aitherdev switch
```

Guarded host unit `archive-content-host-deploy-20261007-retry2.service`, invocation
`b0c6e05c31654c95ae7a56147abf6810`, completed exit 0 in 95 seconds. Two health
checks passed, none failed. Selected host:
`/nix/store/zw4pi574kh9cmgx2wk8ab8hg9r25ibq6-nixos-system-aitherdev-26.05.20261006.b253099`.
Starting host was `794pz5dv69bkn0vcgr5l52xj9j93dkkz` with the same system version.

Application command:

```sh
workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-07-archive-content-integrity/workspace
```

Guarded application retry unit `archive-content-application-deploy-20261007-retry1.service`,
invocation `75e1ec2b914c4ca0b1019b99c532f435`, completed exit 0 in 60 seconds.
Selected exact expected application:
`/nix/store/rr9rzzwcmpvhl2s75r21jb4gmnm4jq3j-dev-workspace-0.2.0`.
Starting application was `yc881ddhy7sr4k2f59jfqwjq6b1wr4p3`.
The pending forward Codex update cleared. Codex, portal, router, tmux and the
auto-archive timer are active. Fresh Luna/low utilities observed parent-launched
activation; they did not deploy or make retry decisions. Normal idle, ownership,
generation and journal refusals were preserved.

Initial host launcher attempts stopped before mutation: zero transient-unit
timeout killed the shell, then missing ambient Ruby stopped the contract check.
Explicit infinity and the workspace Nix shell resolved those. First application
attempt deferred while another live conversation was inProgress; 21 read-only
checks over 600 seconds remained busy. No forced interruption, rollback relink
or private journal rewriting occurred. The ordinary later retry succeeded.
Earlier busy result is retained as `deployment-result.json.busy`; current
[deployment-result.json](deployment-result.json) reports actual final activation.

## Live acceptance

`run-live-verification.sh` completed exit 0. Authenticated CA-verified HTTPS
confirmed the original session is archived, with no journal or saved error;
unauthenticated access was refused. Served app.js and installed archive worker
bytes match final reviewed source. The real browser confirmed concise archived
Settings, collapsed technical details and no duplicate failure banner. A
read-only browser response fixture confirmed concrete failure, recovery step
and attempt time, with full details available when expanded. It did not mutate
server state; the browser restored the actual archived page and had no page errors.
The API probe verifies TLS; browser development-certificate exception is recorded
separately. Artifacts:
[live-api-result.json](live-api-result.json), [live-browser-result.json](live-browser-result.json),
[recovered-settings.png](recovered-settings.png),
[concrete-failure-settings.png](concrete-failure-settings.png).

## Integration

User “retry and continue, then merge” approved the previously named three master
targets. All exact feature heads fast-forwarded and were pushed over SSH; no
rebase or reviewed-content changes were needed. Exact local/remote proofs:
[integration-proof.json](integration-proof.json). Shared workspace master retained
97 unrelated modified files and unrelated index entries. Temporary target
worktrees were removed; feature branches and worktrees retained.

Post-merge runtime CI `37657712782` remained in progress at final inspection:
host passed, fast still building. User “no waiting for CI” stopped local
monitoring; exit 130 belongs to the interrupted watcher, not a failed CI run.
Remote CI was left running without cancellation or retry. [master-ci.json](master-ci.json).
No required operator action remains; this session remains open for follow-up.
