# Messaging correction handoff

Ready for lead acceptance and final combined review; not independently reviewed,
not deployed. R branch `2026-11-11-pi-codex-migration-pi-roster-preflight-fix`.
Package base `81510ac37c8f3f3fc091a4d31029af35ebff7b02` retains the accepted
Team base `f1bb4c1b472661f6d76e246f252b8fc46f7df3db` plus owner2's isolated
historical-removal correction. Final head `09608843edffc38523c5c46356cb9d51939ef875`,
tree `48f8f77b927752b7cf7d5d9fc00381ae498bc374`. Normal commits:

- `0219cc654640b4c2731f07ffc14a5f89f0d952fc`: policy observation/mutation split,
  focused state guards and prepared shared SDK child control, runtime guide.
- `7785666ad8774e280100683a1286fb346b2421de`: typed pre-Send effect boundary,
  actual HandleHostCall adapter cases and team delivery guide.
- `09608843edffc38523c5c46356cb9d51939ef875`: shared error heading and assertion.

`committed-source.json` binds all 12 owning files, binary patch and final hashes.
All 15 frozen quick-result input hashes (including owner2's three paths) equal
final committed blobs. Checkout/index were clean on release. No declared hook
framework or active hooks were present; ordinary commits bypassed no hook.

## Verification

Existing declared shell: `tmp/pi-provider-info-q/R-focused-env.nix` (Go1.26.6,
Node22.23.2). Go uses `-mod=readonly`, `-count=1`, `-timeout=60s`, `-v`.
`quick-results.json` hashes every retained original log.

The finite batch ran `go test` on `./internal/piruntime ./internal/web
./internal/teamruntime`, selecting exactly:

- TestSupervisorToolPolicy{PendingPrecedesMutationAndDurableAck,
  InspectDoesNotWriteLoadOrClearHolds,FailureRetainsPendingAndNeverRetries,
  LiveCallbackCanInspectButCannotApply,ReadinessStillRefusesUnsettledState,
  RefusalsAndMaximumDoNotMutate}: PASS, package0.354s.
- TestPi{DeliveryRefusesWithoutAuthorityOrNativeEffect,
  ExplicitReportMakesOneWitnessedAttempt,DuplicateAdmissionCallbackCannotSendTwice,
  OriginalIDsAndTerminalOutcomesAreNeverReplaced}: PASS, package0.034s.
- TestPiSoloAddProductionRouteAndExactPublicationRecovery and
  TestPiAbsentSoloAddProductionRouteAndExactPublicationRecovery: PASS.
- TestPiTeamHostCallbackPreservesKnownPreSendRefusal: initial run refused before
  callback because the inherited settings fixture had canceled its operation
  lifetime. Fitted only the new fixture's owned lifetime/cleanup, then reran
  `go test -mod=readonly ./internal/web -run
  '^TestPiTeamHostCallbackPreservesKnownPreSendRefusal$' -count=1 -timeout=60s -v`:
  all six cases PASS, package6.397s. Actual HandleHostCall with synthetic
  address-scoped runtime ports; no native callback/SDK execution claimed.

An earlier direct resolved-Go invocation failed setup because CC was absent from
PATH; no test ran. Original setup and fixture failures are preserved separately.

Node `--check` passed for `static/app.js` and `pi-runtime/test/fake-worker.mjs`.
Existing `browser_contract_test.cjs --unit https://workspace.example.test` with
the pinned codex-web conversation.js passed32 preparation cases and queue/retry
contracts. No browser/server was launched. Its0.500s tool process joined.

## Remaining evidence and compatibility

`TestPinnedSDKPolicyInspectDuringSharedBashChild` is prepared and compiled,
**not executed**. The single post-review native run must observe the actual SDK
Bash child's PID/starttime/PGID, positive original per-PID predicate branch,
read inspection success and mutation refusal, then explicit release/join.
This uses existing childrenCheck injection, not full production cgroup scanning.
No claim is made about the historical failed subcall/PID.

This series introduces no format, schema, wire capability, migration or pin.
It retains inherited whole-branch creation/roster/native Fork evolution; it does
not certify the whole branch migration-free. Registered branch base is
`b31295bd5bb6f83a3781ca7785b51d03be9ae273`; deployed prior8fe lineage and exact
consumer history remain in the lead's existing state/release evidence. No history
was rewritten, and owner2's81510 correction and all Team bytes are preserved.

The portal consumes callback results and shared browser presentation. Frozen
session supervisors own policy inspection, so portal selection alone is
insufficient. Eligible idle/settled sessions use ordinary explicit runtime upgrade
with a fresh operation UUID; recovery retains its original UUID/predecessor/target.
Existing held-session recovery remains unresolved and excluded. No target read,
message replay, hold clearing, provider/network model trial, upgrade, build, push,
CI, deployment or lifecycle action occurred. All owned tool effects are joined.

Docs: `docs/pi-teams.md` is the user/developer delivery/refusal reference;
`docs/pi-runtime.md` owns policy semantics and supported ready-session upgrade.
Exact final prose and upgrade-link wording received the lead's writing pass;
existing Team prose and upgrade prerequisites remain intact.

Lead owns acceptance, complete branch review and later native execution. Whole
source/index release was reported directly to lead and owner2 before evidence
formatting. Implementer1 retains finding ownership/capacity.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
