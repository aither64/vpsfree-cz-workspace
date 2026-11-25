# React CI fixture remediation — terminal packet

Clean PUBLIC **6c6792a62d5bb1193b1ce96c0d6ff9167341de49**, tree **c591e51b6e701b19b5ec5daf2284ef0696f9bd16**; canonical SSH repository
vpsfreecz/vpsadmin-webui, feature dev/oomd-abuse-policy, [PR333](https://github.com/vpsfreecz/vpsadmin-webui/pull/333).
Main remains `4499f90fe11df0e4df6f23e5fa54829e2254ec1b`. Same session/roster44/Sol-xhigh/write/fullaccess verified.

## Original failure and concrete closure

Run **45460130475/attempt1/workflow369520612/head65812a**, job138680132828
Required nonbrowser checks, failed step **Run unit, script and BFF suites**.
The chained npm run test:scripts phase had244tests,227PASS/17FAIL; unit and BFF
phases later in ci:tests did not execute. The required quick entry, Production
build and Chromium script regression passed on that exact original source.
Complete original logs and job/step identities are run.stdout/failed.stdout.
No blind rerun or environment problem is inferred.

Two test-fixture defects were reproduced before changes with selected failing
cases in repro-results.json/repro-*.stdout, preserving original failure output:

1. All15design-docs tests failed setup: the fixture did not create newly required
   `src/routes/adminIncidentRoutes.tsx`. Exact child stderr in missing-route.stderr
   proves ENOENT, rather than merely asserting1!=0. Add an empty module beside
   existing route fixture modules; the setup assertion now includes child stderr.
2. Both checkout/Gitless missing-core-root negative tests selected
   inventory.adopted[0]. The new adminIncidentPolicies fixture sorts first but is
   not an INITIAL_ROOTS core path. The production gate correctly reported an
   unadopted new path, not a missing mandatory root. Import the already exported
   INITIAL_ROOTS and select its first actual mandatory entry. The required-root,
   minimum, baseline and negative assertions are not weakened.

Independent [review](../nov24-react-registry-adoption/review.md) at immutable658
identified exactly these two Important GENERAL findings, no other application,
SDK/auth/architecture finding. Root accepted direct step9 remediation and owns
final two-file inspection; no automatic reviewer rerun absent scope expansion.

## Narrow fix, exact checks and retained scope

Only **scripts/design-docs.test.mjs** and
**scripts/e2e-type-coverage.test.mjs** differ from658: +5/-3lines. No production
application, routes, metadata/classifiers, gate logic/budget, registry/lock/hash,
HaveAPI/BFF, docs/copy/catalog/screenshot or migration change. All other blobs/modes
are exact; this packet is the technical causal record. Existing worklog101/fullquick
facts and root PR prose remain unchanged and keep their original inputs.

Both COMPLETE affected Node test files passed **31tests/0failure** in
**17.240s**, including all17original failures and the other14cases.
No sum is presented as a new244-test pass. `npm run lint:scoped` passed45adoptedfiles,
`npm run format:check` passed82reviewedfiles, diffcheck0. Actual checked file hashes
match committed bytes. Original101/fullquick and old production/browser successes
remain literal658/source scope; no app/browser/system/build campaign was replayed.
No long utility was needed for these known quick checks.

## History, publication and CI

One normal owning-UI amend-F exited0, preserving original author/date and leaving
exactly TWO purposes: unchanged registrySDK **b8908402c3d27d324b3752ee05d6dfd15f74c728**, then
completeUI **6c6792a62d5bb1193b1ce96c0d6ff9167341de49**. No migration, fixup or repeated dependency stream. Preserve
reviewed658 at refs/evidence/implementer2/nov24-ci-reviewed-65812a; all earlier refs
remain. affected.diff/final-full.diff/final-series.txt bind complete final scope.
Normal hooks context retained; no declared framework/activehook/no bypass.

Fresh scoped fetch, actual658lease guard and one SSHpush0/3.936s.
Independent SSH and canonical immutable GitHubcommit/tree exact, main4499 unchanged.
PR333 OPEN actualnewhead and unchanged rootbody readback exact; supported comparison
exited0 exact4499..6c6792. No default, release, npm or deployment action.

One finite60-run same-branch CI inventory:

| Run | Workflow | Observed status |
| --- | --- | --- |
| 45461616406 | Playwright broad smoke (pull_request) | queued |
| 45461616579 | CI (pull_request) | queued |
| 45461616646 | Playwright smoke (pull_request) | pending |
| 45461602060 | Playwright broad smoke (push) | queued |

Old658 CI45460130475 remains FAILED. Both old broad runs45460129891 and45460113586
were SUCCESS at the inventory. Superseded smoke45460129979 appeared inprogress;
the allowed cancellation raced with an already terminal run and returned1.
One exact readback reconciled **completed/cancelled**; do not call that successful
execution or attribute the cancellation to our refused request. No unresolved
mutation, wait/watch/dispatch/rerun, current-CI success or final readiness claim.
Root owns required successor-CI disposition.

All current native handles 30825,85395,26183,15314,15084,16100,9399 joined, no unknown effects.
No service/runtime/host/profile/claim/lifecycle/cleanup action; diagnostic scratch
under this packet remains retained. Source/index/Git/effects/capacity **RETURNED
ROOT ONLY**. Implementer2 retains fixes. Deployed f7 and all registry adoption
historical receipts remain unchanged.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
