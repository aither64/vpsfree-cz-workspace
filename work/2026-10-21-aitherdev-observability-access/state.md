---
lifecycle: active
---

# Aitherdev observability access

## Current status

Phase: implementation ready, awaiting merge/deployment direction. Independent
review, runtime fixtures, host builds and feature publication complete. Frozen head
`d07b4251172020472b21e8830e92b023849d543f`; clean project worktree/index.
Exact feature head published and remote-verified. No merge, deployment or real
credential provisioning performed; production access remains unverified.

## Phase checklist

- [x] Verify bound session identity and retained team/access.
- [x] Accepted architect design; both implementation packages complete.
- [x] Required hooks, formatting, syntax/evaluation and native actual-group probes.
- [x] Initial independent four-lane final review; A1 test assertion corrected.
- [x] Focused General/Risk final review of corrected production omfile policy.
- [x] Complete proxy integration and corrected logger VM at reviewed d07b4251.
- [x] Complete both affected-host builds at reviewed d07b4251.
- [x] Publish exact tested feature head and verify remote; prepare handoff.
- [ ] Deployment/live acceptance: separate authorization, outside current work.

## Authorization and ownership

User directed "Implement the plan" after selecting random-secret Basic auth.
SSH machine key has no IP restriction. User confirmed the manual key in log root
and personally owns its removal after reader acceptance. Do not edit that file.
No default-branch integration or production activation authorized.

Architect0: design; implementer0: logger/source/tests/docs/fixes; implementer1:
proxy/auth/source/tests/docs/shared registration; reviewer0: independent review;
lead: acceptance, records, user writing and verification coordination. All saved
settings retained. Source/Git owners explicitly released, frozen for review.

## Repository and complete final series

Project: vpsfree-cz-configuration, SSH remote git@github.com:vpsfreecz/vpsfree-cz-configuration.git.
Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-21-aitherdev-observability-access/vpsfree-cz-configuration.
Branch: 2026-10-21-aitherdev-observability-access. Base/origin/master at last fetch:
`38e7c837893695999e588a73f5d2a0088b8257b1`.

1. Logger: `bd54b28c63770b782a4af435ad8dfb9619b6032c`.
2. Proxy/head: `d07b4251172020472b21e8830e92b023849d543f`.

Final tree `b19544c8db2097a2f98a20e5781d7f1f5c6ce6dd`. Ready-series.txt/ready.diff
inventory the complete branch. Fixes consolidated into their owning unpublished
commits; no migrations, dependency/pin update streams, deployed/released or
externally consumed intermediate history. Initial workspace plan commit1ec83cc8.

## Review evidence

Initial reviewer0 gpt-6.1-sol/xhigh/read-only report [review.md](review.md): all4
lanes, no Blocking/Important, A1 advisory only; explicit clean whole-history/no
repeated-stream/no-migrations conclusions. Reviewed072f7e01. Lead checked narrow
fixture fixes via stored diffs/range-diffs; no redundant review for them.

Actual VM then exposed new remote directories0700 root:root/file0640 root:root:
legacy defaults did not control RainerScript omfile. Architect approved explicit6
owner/group/mode action properties, preserving local messages globals, Umask,
inputs/path/template/pipe/HUP/rotation. Native mapped groups100/200 probes PASS,
including existing-metadata preservation. Source and regression fixes committed.

Current retained reviewer0 (same settings, no fallback) completed General+Risk
follow-up at d07b4251: [review-followup.md](review-followup.md), no new findings.
Unaffected architecture/scope conclusions retained; complete final series/history/
no-stream/no-migrations conclusion updated. Prior incorrect creation-policy
assessment explicitly superseded; original reports preserved.

## Verification evidence and remaining checks

- Pinned Nix shell bootstrap PASS (Ruby3.4.9, Overcommit0.73.0, nixfmt/confctl).
  Worktree-add postcheckout exit78 did not undo successful creation/registration;
  fixed ignored local gem environment without bypassing hooks.
- Both packages: active mandatory hooks/Nixfmt/Python/evaluation/whitespace checks
  pass. Pinned nginx1.30.6 syntax and effective SSH15 policy checks pass.
- Final logger quick flake derivation PASS: action+account assertions, rsyslog
  syntax, generated NixOS logrotate validation, helper AST. Root substitution
  is parser-only; actual native GID100 creation/pipeGID200 behavior separately PASS.
- Final full runtime fixtures PASS at d07b4251 (combined build exit0,102s). Previous failures were diagnosed:
  plaintext nginx fixture needed h2c; missing authfile natively returns403;
  logger fixture needed RFC5424 and proper FIFO/socket lifecycle; subsequent
  VM diagnostics exposed and prompted the actual omfile creation-policy correction.
  Do not relabel failed diagnostic hypotheses as acceptance passes.
- Latest failed VM at5d910028 naturally failed129s. Corrected d07b4251 passed
  proxy integration+logger VM after focused review. First logger host-build attempt stopped at interactive Continue prompt/EOF,
  not a configuration error. Fresh noninteractive logger/proxy builds now running. No live probes/provisioning.
- Only CI workflow is scheduled/manual daily dependency update; no automatic
  feature-branch CI. Do not trigger maintenance workflow for this feature.

Detailed evidence: [logger-runtime-diagnosis.md](logger-runtime-diagnosis.md),
[logger-permission-diagnosis.md](logger-permission-diagnosis.md), native probe logs,
original/retry/guarded/runtime verification logs and JSON. Complete prior records:
[progress-history.md](progress-history.md). Original evidence preserved.

## Documentation and next actions

[design.md](design.md) is the architect-owned accepted brief. Project operations
guides docs/operations/log-reader-access.md and prometheus-query-access.md include
provisioning, historical reconciliation, rotation/revocation/recovery and curl
examples, linked from README/MkDocs. Lead contextual writing pass applied.

Fresh acceptance_verification Luna/low utility now owns both long fixture
derivations and logger/proxy confctl builds at d07b4251, with exact pwd+HEAD guard.
Logs acceptance-verification-01..03.log and acceptance-verification-result.json.
Combined fixtures passed exit0 in102s. First logger build prompt/EOF exit1 in35s;
pinned confctl build --help confirmed --yes. Fresh host_build_watcher now runs
only confctl build --yes logger/proxy, logs host-build-01/02.log and host-build-result.json.
All checks passed; exact head published and remote-verified. Next: user direction
for integration/deployment, followed by runtime credential provisioning and live acceptance. No repository
merge claim needed; no integration authorization supplied.

Live prerequisites: user-scoped credential files outside Nix/Git, actual old-log
ACL/readers inventory and reconciliation, verified SSH/HTTPS/ingestion/rotation.
Shell permits home/tmp writes and outbound processes; data is unredacted. Root key
remains user-owned until accepted reader access. Leave session open; no lifecycle
or cleanup action requested. Accidental utility work/verification-artifacts/ JSON
is recorded in detailed history; no deletion performed by lead.

## Final build acceptance

- Both host builds with confctl build --yes passed at frozen clean d07b4251:
  logger generation2026-10-22--00-12-21/about101s, proxy00-13-39/about87s.
- Lead independently verified local generation.json receipts and existing Nix store
  toplevels. Curated full receipt evidence host-build-evidence.json. Utility did
  not save requested complete stdout logs/resultJSON; announced confctl logfiles
  absent after completion. Reported exits and native buildreceipts retained;
  don't fabricate logs or repeat passed builds merely to reconstruct them.
- No local kernel build/cancellation/live operation. Source clean; final comparison
  captured base38e7c837/head d07b4251. All intended local verification now passed.
- Implementer1 assigned only featurepublication with freshfetch, hooks, exact
  remote-head proof/defaultbranch unchanged and no force/merge/deploy/PR.

## Publication and handoff

- Implementer1 fresh-fetched origin in pinned shell; baseline unchanged38e7c837.
  Hook-enabled SSH push created feature branch at d07b4251 with upstream set.
- Remote ls-remote proof: feature d07b4251172020472b21e8830e92b023849d543f;
  default HEAD/master38e7c837893695999e588a73f5d2a0088b8257b1 unchanged.
  Local HEAD/upstream equal, clean tree, no ahead/behind, no force/PR/merge.
- No automatic branch CI exists; no maintenance updater dispatched.
- Captured final comparison and registered design/review/diagnosis/build evidence
  in portal. Source/Git ownership released; no claims/reservations acquired.
- Coding blockers: none. Remaining operations require separate user direction;
  actual credential files, historical metadata/required readers, live SSH/HTTPS,
  ingestion/exporter/rotation acceptance still pending. User then removes manual
  root-key grant. Leave session open, lifecycle active while branch unmerged.

Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-21-aitherdev-observability-access/
Feature: https://github.com/vpsfreecz/vpsfree-cz-configuration/tree/2026-10-21-aitherdev-observability-access
