# Codex root-retirement rollout — 2026-10-31

Status: reviewed source; packaged verification/builds running. No machine claim or deployment yet. User authorized aitherdev system/user-profile deployment and three named master integrations after verification. No reboot, forced GC, native pruning or session lifecycle action.

## Exact sources and input graph

Runtime c2182254d29c4175c3e9fe4267e5a92dd1da6b79; composed workspace 6fa6c0f218f5ee2d887f1669bec86cfec6959a91; configuration 2e1d9e957a5c11fda47bdea8f12dffbafa8064ee. Complete flake.lock graphs, follows, hashes and remote/target mappings are saved in rollout-inputs.json; final review binds these exact ranges in final-review.md. W pre-deployment old/new equivalent range is retained there and in downstream-report.md. No deployed replacement mapping yet.

Machine: canonical vpsfree:aitherdev, alias aitherdev/aitherdev.int.vpsfree.cz, selector cz.vpsfree/machines/aitherdev. Claim pending prepared artifacts.

## Before activation

System/profile: /nix/store/hsci7shrxm3a5gy642jzhp7yd54adgni-nixos-system-aitherdev-26.05.20261026.718f670
Application: /nix/store/413w4bai6br4c2vq08gx9diq55iasvqk-dev-workspace-0.2.0
Current Codex: /nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0
Legacy numeric links: 168 (refreshed before work).

## Verification and prepared artifacts

See verification-brief.md for exact bounded related batch and commands. Fresh standalone watcher native thread 01a1927a-6015-7753-ae8f-127164726a5e, gpt-6-luna/low from pinned utility policy, explicit danger-full-access/never launch. Full events verification-watcher.jsonl; final result verification-watcher-final.txt and verification-builds-result.json. First native watcher attempt stopped on root-directory current lookup before checks; exact directory identity reverified, no owned command remained. No diagnostic/test retry was substituted for a failure.

Application/system/generation output identities pending build completion. Copy preparation, dry activation and system/profile switch use exact retained generation as prepared in downstream-report.md; lead owns all activation and copy commands. Verify both /run/current-system and system profile. Application selection remains separate and forward-only.

## Acceptance and integration

Pending: identity/composition, current Codex, recognized numeric-root retirement after pending settles, profile preservation, portal/router/coordinator health, naming/conversation/tmux continuity and read-only process-root evidence. Ordinary Nix GC only.

Pending: runtime then workspace/config FF integration under one short repository claim each, hooks and fresh remote ancestry; complete deployed lineage proof then authoritative machine release/status. No lifecycle cleanup follows.

### Packaged verification milestone

Step 1 passed (110s): host 240 tests/2711 assertions/3 skips, collector 46/251/0 skips, coordination shards 33/251 and 38/232/0 skips. Outputs qfajwpimawzx2kw0ig8wd4j0z21sgqds host, 6l2x43n2q2895bv4k6wymb8g863zfk53 collector, 1cp778bmyqb7jdyjy34z3bs8y245cd8j / 5vg8mx4z77c31ml8zr253wdfjzhmvvrj coordination. Exact command/revision/log hash in verification-builds-result.json. Application build follows.

- Composed application/deployment-contract build PASS (step 2, exit 0, 665.0s). Outputs reported: /nix/store/lj06g3r6zap4c5ypvcs4masm4vxra68y-dev-workspace-0.2.0, /nix/store/iasfvhynvz5l91l4hqj842xvsf8xd7f4-dev-workspace-deployment-contract-tests. Exact output/derivation receipts remain in watcher result; session-creation VM now running.

- Exact runtime feature CI passed: https://github.com/aither64/dev-workspace/actions/runs/41211584912 at c2182254, fast/creation/archive jobs success, host job skipped by workflow. Consumer branches list no runs. This is CI evidence, not a substituted exact-derivation receipt for ongoing local VM/build.

- VM timing reassessment: exact CI creation job/run proves SAME check derivation `2sma25j1bh8862lwrij0zpcwhk44sj7p` and driver `08zdpg38y1mwaj11008z0xzqw7qrvhfq` as local step 3. CI passed at exact runtime c2182254 with identical input graph; raw CI log retained. Parent accepted reuse in creation-ci-reuse.json and directed watcher to cancel owned local duplicate safely, then stop batch. This is not a test failure/rerun or gate waiver. System build moves to fresh utility after cancellation reconciled.

### Prepared system

System build PASS, 105s, source configuration 2e1d9e957a5c11fda47bdea8f12dffbafa8064ee. Confctl retained generation `2026-10-31--16-46-44`, toplevel `/nix/store/4wpwzqrb3c51bbibwzqavjlc6qjcpiv0-nixos-system-aitherdev-26.05.20261026.718f670`; auto-rollback `/nix/store/yl9vnin9wlv04cip0sqpkisk80xmccwh-auto-rollback.rb`. Exact config lock hash 1e5f7e9af62ffa70e3f94e4a0d63f2ba5f36760e1ffe499c201aacf247e05e5e. Full generation inputs/revs/store paths retained in prepared-system-generation.json and graph in rollout-inputs.json. Copy-only exact retained generation launched by lead; no activation or claim yet.

### Deployment queue

Exact-generation copy-only exited 0; log system-copy.log confirms prepared generation and c2182254 input. No activation occurred. Machine request submitted, exact claim `3c12e227-c653-4437-901d-f4bb1eb2daa2`, owner `faf54592-575a-499b-ae77-f37c0562b9f7`, fresh status waiting. Foreign aitherdev reservation holds resource. No owned machine/repository claims held, no active command. Resume only after authoritative held status; stable user-profile and system generation remain unchanged by this session.

### Granted-claim stale-composition check

At 18:26 grant, exact claim held owner faf54592… confirmed. No unfinished own jobs. System/profile still hsci7sh…, but application now `/nix/store/blwbq3jy7p8xpb3ajqmivylc4gdm4dvi-dev-workspace-0.2.0`; shared master c83620f6 selects extension e4e7e95e while runtime stays original 6f54d0c7. Current Codex unchanged 2rqwqch…. Do not select older lj06g… composition; it would revert extension/tooling. No own activation performed. Exact claim released at 18:28 and released state verified. W owner refreshes only owned runtime pin onto current shared base, preserving extension; rebuild/review affected composition then fresh claim. Config/system generation and runtime source unchanged.

- Post-wait exact reuse check by implementer1: unchanged runtime four Ruby drvPaths and VM 2sma25… exactly match passed receipts; unchanged configuration system derivation 42a2ii9r9s7h0969gwdxjzhgiasl4jcr equals deriver of prepared copied 4wpwzq… . New W graph hash68485a53… and app2jvhgy…/contract3wlzx… derivations differ, so fresh W build required. Full graph hashes/paths in downstream-report.md/downstream-refresh-inputs.json.

- Refreshed composed app build PASS775s, app0q7rc75dh4mjrxpb37m1hchfwcbmpa7a (deriver2jvhgy…), contractnlp2zb… (deriver3wlzx…). Full watcher result retained. Dirty warning investigated: HEAD/worktree raw lock equal hash68485a53, clean staged/unstaged/status. Watcher hash540163a3 is canonical compact graph+newline, not raw bytes; exact same graph. Lead fresh eval matches both expected drv paths. Clarification/binding in refreshed-build-acceptance.json. No rebuild/source change needed.

### Verified deployment

Fresh machine claim19b5ff77-f6d9-496a-8ef1-5aacaa473acb held by exact owner; dry-activate and no-reboot system switch exited0, health2/2. Both live/system profile4wpwzq…. App switch source final7a0a8fd1 exited0, selected0q7rc…, current Codex unchanged2rqwq…0.165.0; compatibility probe PASS. Predecessor helper created last legacy220 link during transition, new writers removed. Periodic collector migrated all legacy links before explicit preview acquired lock. Final directory/registered legacy roots0, current unchanged, read-only Nix lists6 Codex exe process roots. Collector inactive/ExecMainStatus0, preview retry=false/no Codex actions or preservation; journal has no per-action JSON, so migration is established by before/after inventory and unit result. No forced GC/native pruning.

All five services active, health portal/routertrue, models8, session thread unchanged01a17d9b…69 entries, tmux$50 and identity unchanged, CodexPID1906/tmuxPID1917 unchanged, no pending transition/failed units. Exact catalog/hash and acceptance limits in activation-before/after.json. No unfinished switch/copy command. Ready for previously approved three-master integration; physical machine held until verified remote lineage.

### Integrated lineage / release prerequisites

All exact deployed final heads now equal fresh remote master heads: runtime c2182254, W7a0a8fd1, C2e1d9e95; retained extension e4e7e95 also equals its remote master. No deployed nonancestor replacement or substantive successor. Three FF/SSH pushes and exact remote proof completed; all repository claims released before this record. Shared workspace merge held nonblocking tracking lock and preserved unrelated changes/index. Config hooks remained enabled through ordinary Nix-shell merge/push.

Fresh live recheck still selects system/profile4wpwzq…, app0q7rc…, currentCodex2rqwq…, legacy0/no pending/all5servicesactive. No unfinished commands. integrated-lineage.json binds fresh remote proof and complete input/deployment receipts. Authoritative exact machine claim held by this owner immediately before release.

- All exact final heads integrated as proved in integrated-lineage.json; authoritative machine19b5ff77… released18:53:07 and verified released, no reservations/held claims remain. Session stays open; retained refs/worktrees untouched. Post-merge CI41231374089 runs exactc2182254 under fresh utility; resource release did not wait for duplicate CI.

### Durable graph provenance

The full immutable input graphs remain in committed `flake.lock` objects at each final source head; rollout-inputs.json is an untracked inspection copy. These exact graph objects retain all transitive locked identities and follows/edges and are reconstructible after disposable evidence removal:

- dev-workspace: source `c2182254d29c4175c3e9fe4267e5a92dd1da6b79`, full graph Git blob `3241e81b46111b10a97fac7f3fabd8134840c0dd` (`git show c2182254d29c4175c3e9fe4267e5a92dd1da6b79:flake.lock`).
- workspace: source `7a0a8fd1317c9dc17b79a99c1a27e182ac988ab1`, full graph Git blob `f805a56f80ca841184c6ee34ce759ec8c008abd5` (`git show 7a0a8fd1317c9dc17b79a99c1a27e182ac988ab1:flake.lock`).
- vpsfree-cz-configuration: source `2e1d9e957a5c11fda47bdea8f12dffbafa8064ee`, full graph Git blob `20c65df7cba689321a8075bff277f4b8c4e67906` (`git show 2e1d9e957a5c11fda47bdea8f12dffbafa8064ee:flake.lock`).

### Final verification and completion

Post-merge runtime run41231374089 at exactc2182254 completed SUCCESS: fast/archive/host/creation all passed. Fresh watcher ended, no active command. Final remote default heads rechecked equal deployed/final R/W/C; all claims released/no reservations, root directory0/current app unchanged. No subsequent live operation. Delivery complete, session remains open, feature refs/worktrees retained. Final tracking checkpoint contains compact Markdown evidence and exact immutable graph object references; raw logs/JSON remain untracked/disposable.
