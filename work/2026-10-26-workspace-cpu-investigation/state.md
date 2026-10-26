---
lifecycle: complete
---

# Workspace CPU optimization

Implemented, deployed on aitherdev without reboot, verified, and integrated into
all three approved remote master branches. All repository claims and the machine
claim are released. Session remains open. Automatic post-merge runtime CI also passed; no work or active claim remains.

## Phase checklist

- [x] Investigation, architect design and bounded implementation packages.
- [x] Implementation, owning docs and meaningful deterministic regression tests.
- [x] Focused quick checks and independent final source/history/consumer reviews.
- [x] All 24 one-off controlled performance runs pass.
- [x] Final artifact builds, required host/recovery checks and feature CI pass.
- [x] System and application activation, health and native continuity verified.
- [x] Exact deployed feature heads integrated into approved remote masters.
- [x] All claims released after fresh deployed-lineage proof.
- [x] Automatic masterCI40416668825 passes all four jobs at the exact integrated head.

## Final revisions and deployment

| Repository | Reviewed base | Final deployed/integrated head |
| --- | --- | --- |
| dev-workspace | deed45f04fc0698b2f2f408b2816ac124913d582 | fffbd0d59fffc09667cb39878d9f7da8bdcd3806 |
| workspace | 83282a493a6961d352b8ad0e2dfa3b17624fd46c | 718bbaa210a4b7912dd2aa4b1bd1e4dc33a78f4b |
| vpsfree-cz-configuration | cba1f93fcf2d0c2be35d4fb3dd868ba537c38656 | 530efc29e5a6e5579c304ec22d3a10062cd0ecc4 |

System generation2026-10-26--23-38-24:
`/nix/store/lk9lkpcnk9lmxz1vwl4lm0xnmkjjhr0f-nixos-system-aitherdev-26.05.20261021.da6dc0e`.
User-profile application:
`/nix/store/lm7xpfxxzr2012y80wq2fnvirlyfakzz-dev-workspace-0.2.0`.
Both system links and embedded configuration revision verified. Deployment exit0,
confctl2/2 health checks pass, all five user services running, portalhealthzOK.
Codex/tmux PIDs, start times and app/tmux socket incarnations unchanged; this
conversation continued. Complete source/input/derivation/closure receipts,
approval, no-reboot command effects and release evidence: [rollout](rollout.md).

User authorized implementation, aitherdev system/application deployment,
verification then integration into the three master targets and machine release.
No session archive/delete/stop or other lifecycle action was authorized or run.
Machine claim9b48f110-4a67-4112-8afd-8a7d4877091b was released23:02:50UTC after
actual verification and fresh exact remote ancestry proof. All three repository
claims were short, separate and released after their merge/push proof. Unrelated
shared files/index preserved; hooks and signature checks were never bypassed.

## Measurements and limits

Controlled20roots×5members=120conversations, valid~3MiB ledger, three alternating
warmed pairs per cell: median whole-cgroup idle CPU fell88.0%/81.3%/85.6% for
0/1/5status consumers, coordinator97.4–97.5%; active CPU84.0% lower. Every
synthetic update observed and notification delivered, zero pending. No repeatable
>20% active latency regression in this bounded fixture. See [results](performance-results.md).

This was a one-off opt-in experiment, skipped by ordinary tests and CI. Routine
regression gates use fake time and deterministic counts. Exact measured pair is
d209..0fd31; later reviewed patch-equivalent rebase preserves a disjoint live
archive repair. Finalfff adds a test-only fixture fix. Native daemon/model,
activity connection and browser rendering CPU are excluded from fixture claims.

Postdeploy live30s combined portal/coordinator2.03952cores versus historical
3.03312cores. Workload and intermediate selected baseline changed; this is an
uncontrolled observation, not a causal savings ratio. Services stable/healthy:
[live verification](live-verification.md).

## Verification and review

Retained independent reviewer0 gpt-6.1-sol/xhigh/read_only: original complete
runtime review, direct narrow remediations, final refreshed history/composition,
archive fixture fix and final consumer refresh all pass. No obsolete history,
transitional schemas, migrations or repeated pin streams remain. Runtime has
four CPU/fixture commits plus one separate existing-base fixture correction;
each consumer has one final pin. [Runtime review](final-review.md),
[consumer review](consumer-review.md), [history/provenance](history.md).

FinalfeatureCI40412890007 atfff PASS archive/fast/creation. Host skipped there;
final recovery VM passed locally, host-idempotency reused only after identical
derivation/input proof. Final app/system built from actual final identities;
oldf23 artifacts retained separately underbuilds/f23 and never relabeled.

FailedCI40406137477 was diagnosed from full trace: direct VM require-idle omitted
--user-state-root and read the fenced legacyJSON rather than selectedSQLite.
Commitfff fixes only the fixture call and adds realSQLite regression coverage;
focused2testsPASS0.182s, independent review and corrected archive CI pass.
Earlier local0fd browser hydration timeout remains unexplained; recorded separate
from the later storage-root cause. No timeout or production parser change made.
[Finding reconciliation](review-findings.md).

## Ownership and next action

Source packages: coordinator implementer0, retry implementer1, cache implementer2,
benchmark/pins implementer3, architect0 design, reviewer0 independent review.
All packages complete; implementer0 postdeploy sample complete. Feature worktrees
clean and retained. No lifecycle cleanup scheduled. Parent owns remaining CI
result acceptance and final tracking checkpoint.

Final automatic masterCI40416668825 passed fast/host/archive/creation atfff;
watcher27461 completedexit0, no active jobs. Evidencebuilds/master-ci.*.
Two hash-verified benchmark exports/binaries were removed after all24runs and
no active units/CWD references; committed fixtures/results retained. All feature
branches/worktrees remain; no session lifecycle cleanup or delayed action.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-workspace-cpu-investigation/
