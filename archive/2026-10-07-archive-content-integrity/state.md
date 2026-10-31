---
lifecycle: complete
---

# Archive content integrity and useful failures

Current phase: implemented, deployed, verified and merged. The original blocked
session is successfully archived. All three exact reviewed feature heads are
in their remote master branches. Host and application activation passed, and
the live API and browser confirmed the corrected Settings behavior. No blocker
or required work remains. User explicitly excluded waiting for post-merge CI;
that run remains in progress and its local watcher was stopped. This initiative
remains open with retained feature branches and worktrees.

Phase checklist:

- [x] Diagnosis, approved plan and separate verified initiative.
- [x] Original archive recovered through ordinary native retry.
- [x] Implementation, documentation and quick checks complete.
- [x] Whole-branch independent review and direct fixes complete.
- [x] Package, browser, matching host build and feature CI verification.
- [x] Matching aitherdev host and application deployed and verified live.
- [x] All three exact final heads fast-forwarded and pushed to remote master.
- [x] Temporary integration worktrees removed; feature branches retained.
- [x] Post-merge CI watcher stopped per explicit user instruction; remote run retained.

## Final revisions and approval

Retained branch in every repository: `2026-10-07-archive-content-integrity`.
Retained worktrees: `worktrees/2026-10-07-archive-content-integrity/{dev-workspace,workspace,vpsfree-cz-configuration}`.
Exact remote master and feature heads:

- Runtime: `9f999f7f713557b261a3d6d1597f8372eabf6518`.
- Workspace: `4d0c62626c36332f7013ba8ff15c52a6f37e0218`.
- Configuration: `23412037590f1d31b85a53410946a18b36db8bc8`.

User “retry and continue, then merge” explicitly approved the previously named
`dev-workspace/master`, `workspace/master` and
`vpsfree-cz-configuration/master` targets. Approval was recorded before
integration. No rebase or content edits were needed; reviewed/deployed heads
were preserved. Exact remote refs and ancestor proofs are in
[integration-proof.json](integration-proof.json). Comparisons were saved before
integration. Shared master stayed on master; 97 unrelated modified files and
unrelated index entries were proved unchanged across its fast-forward. Only
flake.nix and flake.lock changed there. All retained feature worktrees are clean.

## Behavior and recovery

New tracking digests omit permissions and preserve paths, types, bytes and link
targets. Readers still verify deployed legacy digests exactly. Worker failure
paths retain bounded valid UTF-8 causes and deferred results. Settings shows
cause, recovery step and attempt time, collapses technical metadata, and
prioritizes successful archive status over stale cached diagnostics. No schemas
or migrations changed. Extension `0ff827df`, Codex, Nixpkgs and sibling pins
were preserved.

Lasting guidance is in runtime `docs/session-archive-recovery.md` and
`docs/dev-sessions.md`; this deployment is [rollout.md](rollout.md).

Original archive proof matched exactly when only archived state.md was projected
0644 rather than actual 0600. Under authority locks, corrected that proven mode
without changing contents or journal. Ordinary native retry completed exit 0,
tracking commit `2addfb26`; journal/cleanup sidecar absent, runtime retired,
auto-archive timer restored. Evidence: [recovery-mode-proof.json](recovery-mode-proof.json),
[recovery-result.json](recovery-result.json), [live-api-result.json](live-api-result.json).

## Review and verification

Independent reviewer `/root/archive_final_review`, fresh
`gpt-6-astra/xhigh/read_only`, installed default lead_reviewed fallback because
this threadless initiative had no eligible retained reviewer. All four lanes
covered persistent lifecycle proof/cleanup/recovery risk. Two Important findings,
no Blocking: pre-journal generic errors and stale metadata hiding success.
Both directly fixed/folded; reviewer assessed the narrow corrections, no rerun
required. Complete histories accepted: two runtime behavior commits, one pin per
consumer, no obsolete approaches or migrations. Exact review/settings and
remediation evidence: [review-report.md](review-report.md), [review-packet.md](review-packet.md).

Quick checks passed: lifecycle seven regressions/182 assertions, review fixes
two tests/40 assertions, Ruby/Node syntax, shipped Go/browser contract, diff
checks, configuration hooks and matching deployment contract. Runtime and
composed flake suites passed, including local VM checks. Runtime: 401 runs/5408
assertions, zero failures/errors, 12 declared skips. Host: 122 runs/913 assertions,
zero failures/errors, three declared skips. Real Chromium/Firefox regression
passed. Matching host build generation `2026-10-07--17-56-36` passed. Feature
CI `37644340497` passed at exact runtime head (fast passed; host skipped, covered
locally).

Live probes passed: CA-verified authenticated API, authentication refusal without
credentials, archived original/no journal/no saved error, served JavaScript and
installed worker bytes equal reviewed source. Browser confirmed archived summary,
collapsed details, hidden duplicate banner, concrete cause/step/time through a
read-only client fixture, and no page errors. [live-api-result.json](live-api-result.json),
[live-browser-result.json](live-browser-result.json), [deployment-result.json](deployment-result.json).

Post-merge CI `37657712782` at exact runtime head was in progress at the final
read: host succeeded, fast still building. User “no waiting for CI” supersedes
normal monitoring. Local gh watcher was stopped (exit 130 records interruption,
not failed CI); remote run was neither canceled nor rerun. [master-ci.json](master-ci.json).
No observation or deployment operation remains locally running.

## Deployment history and next action

Host: `/nix/store/zw4pi574kh9cmgx2wk8ab8hg9r25ibq6-nixos-system-aitherdev-26.05.20261006.b253099`.
Application: `/nix/store/rr9rzzwcmpvhl2s75r21jb4gmnm4jq3j-dev-workspace-0.2.0`.
Application retry unit `archive-content-application-deploy-20261007-retry1.service`,
invocation `75e1ec2b914c4ca0b1019b99c532f435`, completed exit 0 in 60 seconds.
All five workspace services/timer are active; pending Codex update cleared.

Initial launcher failures stopped before host mutation (zero transient timeout,
ambient Ruby); explicit infinity and repository Nix environment fixed them.
First application attempt deferred on a live busy conversation for 21 checks/
600 seconds. Ordinary retry later succeeded without interruption or bypass.
Browser timer fixture race, noninteractive build prompt, thin-push GitHub errors
and CI PATH omission were investigated; source/failed evidence and reusable
dated notes are preserved. Rollout record links current acceptance separately
from these earlier attempts.

Next action: none required. Session remains available for follow-up; no manual
archive, deletion or session stop was requested. Branches/worktrees are retained.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-07-archive-content-integrity/
