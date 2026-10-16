# Verification evidence

Status: final amended runtime b8a6be26 is committed/published; direct narrow
review remedies and focused checks pass. Refreshed workspace/configuration
pins match, and final mechanical composition review is assigned. Real
Chromium/Firefox template/CSP/root-worker integration passes. Final full packaged
suite failed in the provider-recovery VM; diagnostic investigation is active. Chromium actual native zero-tab
provider/worker/browser-record evidence now passes; final native run and both cleanups are complete. No deployment by this session and no macOS display claim.
Original review and earlier exact-revision evidence are preserved below.

## Runtime source and quick checks

Frozen runtime a7000a2ae803c21274eb65d23ee63d2097fb8829 over
ba8669b14536f72b559abc912bba8eac430111e4. Complete series and private-format
provenance are in review-packet.md. Prepared declared tools: Go 1.26.6,
Node 24.19.0 and Ruby 3.4.9.

- Focused attention/notification/creation/preparation/sensitive Go tests passed
  after rebase, 19.389 seconds.
- Six new browser contracts and 22 existing preparation contracts passed.
- Both Ruby captured-request readers passed their strict preference tests:
  session helper 1 test/5 assertions; host helper 1 test/10 assertions.
- Changed JavaScript/Ruby syntax and diff checks passed.
- Final tracked-tree vendor hash verified by dependency-only forced derivation:
  sha256-iyydGWryLmh8P+YxQcQ2SqGIj1Lds+WBDgsKQV4uFqA=.
  Expected mismatch evidence: vendor-hash-final.log and .status. This is hash
  acquisition, not a failed application test.

## Post-review checks to execute

Preparation-only outbound check: TLS reached both public provider roots from
the host (Firefox root HEAD 406, Chrome FCM root HEAD 404). These expected root
responses establish outbound DNS/TLS/HTTPS reachability only; no subscription or
notification was sent and no provider delivery acceptance is claimed. Details:
`provider-egress.json`.

1. Real Chromium/Firefox notification plumbing with actual template/CSP/root
   worker route; Chromium worker synthetic push with zero tabs.
2. Full Nix packaged check suite, and GitHub feature-branch CI after publication.
3. Final composed workspace/configuration runtime contract and aitherdev builds.
4. Coordinated deployment followed by selected-system/profile health, portal
   UI/API/worker routes and continued Codex access.

No provider acceptance or macOS OS display is claimed by synthetic tests.
The explicit browser enable/subscription and delayed Test action permit actual
Firefox/macOS and Chrome/Chromium background display checks on the user's device.
Record that evidence separately when available.

## First long integration attempt

At e91f22f7, real Chromium/Firefox template/CSP/root-worker plumbing PASS9.693s;
Chromium registered worker handled synthetic push with zero tabs. No real
provider acceptance/OS display inferred. Full flake exited1 after220s:
TestSessionPreparationIndexMakesOnlyNewSessionNameOptional hardcoded v3 asset
while template now uses v4; shipped browser client contract fork body expected
no browserNotificationsEnabled although feature intentionally sends true.
Lead inspected exact failures at preparation_test.go:950 and
browser_contract_test.cjs:1136. Implementer assigned narrow test expectation
updates, exact tests and wider SessionPreparation coverage before rerun.
Evidence runtime-integration.log/.status retained; no blind retry.

Published e91f22f GitHub Check run38646869685 also failed on the same two
expectations. Lead retrieved and inspected failed logs before any rerun;
ci-e91f22f-failed.log confirms both exact failures, no new failure.

## Test expectation remedies at e414ed3

Exactly two assertions changed; no product/dependency/doc/API/schema changes.
Lead inspected e91f22f..e414ed3 and ran both exact Go tests PASS1.222s.
Implementer broader Creation/Preparation/SessionPreparation/Sensitive filter
PASS44.017s, direct Node unit+22 preparation contracts PASS, syntax/diff PASS.
Member's exact shipped-browser test initially met sandbox TCP refusal before
assertion; lead environment ran it unchanged successfully. Source amendment
retains one feature commit, e414ed31806d2b91620d5e5fad8b5b5ee56e07ac.
Published with exact force-with-lease; superseded CI already completed failure,
no running superseded run required cancellation. New CI38647739632 matches head.
Narrow test-only correction directly verified under existing review gate.

Final independent history/composition review PASS at exact e414ed3/988752b7/
0a164903, no additional findings. One coherent commit per feature stream, no
obsolete unmerged history or migrations; matching effective runtime narHash and
preserved extension/siblings/follows. See composition-review.md. Full verification
continues under watcher; this conclusion does not claim tests/deployment passed.

## Final verification PASS

Fresh Luna/low runtime_final watcher ran exact e414ed31806d2b91620d5e5fad8b5b5ee56e07ac.
Runtime real Chromium/Firefox plumbing plus full nix flake check PASS exit0,
1594seconds; includes host-module idempotency and recovery VM, package Go/Ruby
checks. Log ends all checks passed. Evidence runtime-integration-final.log/.status.
GitHub Check38647739632 exact head also PASS exit0, fast success, host skipped
(local full suite covered VM checks). Evidence ci-final.log/.status. Watcher
confirmed head/repo; initial gh repo inference404 corrected to exact supplied
repo/run, not a failed CI rerun. No remaining operation. No actual macOS OS
display claimed. Authorized coordinated build/copy/preparation can proceed.

## Amended final checks

Runtime b8a6be26a75347dcc9ec0fd1330dff886e47c93f: lead15Node contractsPASS199ms and Go Attention/NotificationsPASS0.414s, member15/Go0.443s; syntax/diffPASS. Real Chromium/Firefox template/CSP/root-worker integrationPASS under fresh Luna/low runtime_amended_check watcher. Native real-provider test completed86.6s: both provider accepted and worker receipt0→1 with all portal tabs closed; Chromium browser record1, Firefox record0 under Xvfb. Both shipped Disable cleanups confirmed; no OS/macOS display or actual-click claim. See provider-verification.md.

GitHub Check38661686040 exactb8a6: completed success. Evidence ci-b8a6-final.json/status; no superseded active runs to cancel. Local full flake suite remains running under its watcher; host/recovery coverage is not inferred from CI (host job skipped there).

Final local flake atb8a6 exited1 after36m43s. session-recovery-boot foreign-cgroup subtest timed out901.46s waitingapplied; actual terminalfailed/shared-start after compensation restored original routing. Logs/status runtime-amended-flake.* retained. Original forward and first recovery exceptions are swallowed; exact provider/test files unchanged vs passinge414, query-string models403 also occurs in passinglog and is not diagnosed cause. Architect bounded investigation: recovery-check-investigation.md. No retry or deployment authorized by a green CI; diagnostic evidence is required before accepting a rerun.
