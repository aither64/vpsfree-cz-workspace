# Aitherdev portal rollout

Status: executed. Both authorized paused archive journals completed through the
reviewed forward-recovery packages, aitherdev system configuration now uses the
reviewed portal-authentication cost, user-profile generation 73 selects the
final application package, and both 30-load performance gates pass. The site
application remains selected from the user profile; `vpsfree-cz-configuration`
owns only the separately deployed host module and aitherdev nginx policy.

## Preconditions

- Commit and pin the reviewed `codex-web`, `dev-workspace`, and
  `vpsfree-dev-workspace` feature revisions into the workspace feature worktree.
- Complete focused checks, mandatory independent review, package checks and
  browser compatibility checks before switching the live profile.
- Record the exact four feature heads, consuming `flake.lock`, current
  `workspace-host status` package and switch generation in `state.md`.
- Check pending lifecycle/package journals and current authority generation.
  Resume an unfinished transition before any conflicting switch.

## Prepared switch

From this workspace, build the complete consuming package from
`worktrees/2026-09-29-portal-performance/workspace`. Inspect the pin-chain diff
and package metadata, then run:

```sh
workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-29-portal-performance/workspace
```

After the switch, confirm `workspace-host status`, portal and App Server service
health, session/team/authority access, a bounded page on the target conversation,
older-history loading, composer and pending/queue behavior. Run the 30-load
browser benchmark without a scan and with overlap from the scheduled archive
worker. Record all samples, failures, p95, response sizes, CPU and lock errors
without recording conversation content.

## Recovery

`workspace-host rollback` intentionally refuses older package generations
because team registration is forward-only. If the switch is interrupted, retry
the supported switch path first. If the new package fails acceptance, prepare
a **newer** package that restores the previous application behavior while
retaining current state readers and site composition. Review and switch to that
newer recovery package. Do not retarget profile symlinks, edit generation
markers or truncate state by hand.

## Execution record

- Pre-switch package: `/nix/store/zpfyl4kkdmv6c7r8a0r6rl1s4wpikkla-dev-workspace-0.2.0`.
- Exact feature chain: `codex-web` `d210d3f7cc93981d0ab163b1fcf0718f9587f47e`, `dev-workspace` `e58f8f61ce43058aba49361a0b3bd1ecd98af866`, `vpsfree-dev-workspace` `9c9833579e148e108b5811d618c81ec497b809bf`, workspace `50c3dcf74f7eb816671caf4efd365f9c466e387a`.
- The generic runtime package build passed in 3m14s. Codex-web, generic runtime, and vpsFree extension CI passed for their exact feature heads.
- The complete consuming workspace package build passed at `238ee9a684579e732fd3bab3c37409c892a05ebe` in approximately 176 seconds.
- At initial preflight, `workspace-host status` confirmed the old package was active and the portal, App Server, router, and tmux services were running. No unfinished package-transition artifact was found before the switch.
- The first watcher correctly refused because it inspected the dirty coordination checkout instead of the clean source worktree. No switch command ran.
- The corrected switch verified clean source head `238ee9a684579e732fd3bab3c37409c892a05ebe`, then failed closed before activation because archive journals for `2026-09-26-codex-queue-ledger-capacity` and `2026-09-27-architect-lead-policy` remain paused at `tracking_committed`.
- Both affected records are already under `archive/` with `lifecycle: complete`; the remaining journal work is runtime retirement. The latest scheduled worker retry deferred the first because a team member thread is already archived and the second because multiple threads share its archived tracking cwd.
- At that refusal, the old package remained active. Manual repair/resumption touched other sessions and therefore waited for the user's explicit authorization; the lifecycle gate was not bypassed.
- The user explicitly authorized recovery of both named journals. The corrected consuming package passed at `50c3dcf74f7eb816671caf4efd365f9c466e387a`; `candidate-workspace-package` resolves to `/nix/store/yhnzp6nmq4ngmlvh0wxxhzkbpzda4c0y-dev-workspace-0.2.0`, and its runtime contract matches the selected predecessor byte-for-byte. Dev-workspace Actions run `36641815619` and vpsFree extension run `36641987050` passed at their exact corrected heads.
- The September 26 and September 27 journals then completed through the reviewed retained-only recovery path. Both archived tracking directories and every retained member remain archived, both journals are absent, and the selected profile stayed unchanged during recovery.
- Aitherdev system generation `2026-09-30--04-04-18` deployed generic dev-workspace host-module revision `ec05cb9f008cc8d6bccfd23e9b15a69d9a66fa40` and the site-only bcrypt cost 5. Build, dry activation, switch, service health, exact hash cost, file ownership/mode, unchanged password, correct/wrong password behavior, HTTP 401/200 behavior and reconciler idempotence passed.
- The final application package built from pre-cleanup workspace head `ff30f388dfa61ca1232f2a4391cea61ff865efd6` as `/nix/store/5dzn1p13lcqfgp6lqdii20swa0v3346g-dev-workspace-0.2.0`; `workspace-host switch --source` selected it as user-profile generation 73. Portal, App Server, router and tmux services are active, and App Server remains Codex 0.155.0.
- Final no-scan acceptance passed 30/30 loads with p95 usable 1.617 seconds, 34 paged responses, zero legacy responses and zero HTTP errors. After a seed and 65-second metadata-cache expiry, the dry-run archive scan overlapped the browser process for about 14.3 seconds; all 30 loads passed with p95 1.558 seconds, 35 paged responses, zero legacy responses and one incidental HTTP error.
- Final history cleanup consolidated repeated pin-only commits. Extension head `6a0a2eb873e7cb376092c74bdf82fc2c51c349da` has the same tree as the tested head. Reviewed workspace head `c3944c68e7efc29de9219862074defe8d6547ebc`, and its final range-diff-equivalent merged rebase `35bd0094dcca589de1e9d32a559b383c684faa2c`, resolve it with identical feature-owned flake blobs; the package derivation and output remain unchanged. No new switch or system deployment is required for those commit-identity-only rewrites.
- Post-merge GitHub Actions passed at exact codex-web head `d210d3f7cc93981d0ab163b1fcf0718f9587f47e` (run `36665559076`), generic dev-workspace head `d20bb64c45db1d803fc3b7a8c2956049860d72dd` (run `36665563820`) and vpsFree extension head `6a0a2eb873e7cb376092c74bdf82fc2c51c349da` (run `36665570069`). The consuming workspace and configuration repositories expose no workflow run for their merged heads.
