# Prior package-B CI failures: read-only diagnosis

Both prior runs failed on the same two stale consumer-test fixtures. The final
`61de5e28d1cb1936aeb3ef2376cdaf17f6034e4b` tree retains both defects. This is
source-backed applicability, not a current-head CI result or a local rerun.
Source and refs remain frozen for authority review. No test, CI rerun, native
execution, build, deployment or lifecycle action was started for this diagnosis.

## Exact runs and jobs

Both runs are workflow `Check`, attempt **1**, completed with failure.

| Head | Run | Failed archive job | Failed creation job | Failed fast job | Skipped host job |
| --- | --- | --- | --- | --- | --- |
| `cca49782ebd2d5135352cea4cb140548b36f7de9` | [39809331648](https://github.com/aither64/dev-workspace/actions/runs/39809331648) | 119930979546 | 119930979809 | 119930981185 | 119930982719 |
| `85f6f7327e6948a13ad110c4c058d8b96b6ab2b9` | [39802005782](https://github.com/aither64/dev-workspace/actions/runs/39802005782) | 119904960489 | 119904960817 | 119904960951 | 119905034926 |

The failed steps are `Packaged browser archive, recovery and revival`,
`Packaged browser and native session creation`, and `Build package and focused
checks`. All three fail while building their common dev-workspace prerequisite;
the logs do not establish that packaged native/browser VM scenarios executed.
The host jobs are skipped.

Complete relevant failed-step transcripts downloaded through
`gh run view RUN --repo aither64/dev-workspace --log-failed`:

- [cca complete failure log](implementer1-cca-ci-failed.log): 1,300,759 bytes,
  6,547 lines, SHA256
  `c6763c3dfddd1292a31c7bfccd3ca5078ac86b301614006f6646bad93efd120e`.
- [85 complete failure log](implementer1-85-ci-failed.log): 1,284,868 bytes,
  8,449 lines, SHA256
  `279e33df32073c8c6289905394b1aeff4b375f84646500c10459648d4f0934e0`.
- [cca run/attempt/jobs](implementer1-cca-ci-run.json) and
  [85 run/attempt/jobs](implementer1-85-ci-run.json) bind exact job identities.
- Artifact APIs report `total_count: 0` for both runs:
  [cca artifact inventory](implementer1-cca-ci-artifacts.json),
  [85 artifact inventory](implementer1-85-ci-artifacts.json).
  No artifact exists to download; logs provide the concrete failure evidence.

All downloads completed within seconds. No long watcher was needed.

## Failure 1: coordination fixture lacks native provider metadata

Exact failure in both active and idle subcases:

```text
--- FAIL: TestCoordinationNotificationRetainsSettingsAndDeduplicatesNativeDelivery
    --- FAIL: .../active=false
        coordination_test.go:126: loaded provider binding is unavailable
    --- FAIL: .../active=true
        coordination_test.go:126: loaded provider binding is unavailable
```

cca log: archive lines2427–2431, creation4980–4984, fast6275–6279 (and repeated
package variants). 85 log: archive2989–2993, creation6137–6141,
fast8118–8122 (and repeated package variants).

`portal/cmd/workspace-portal/coordination_test.go:42–45` returns
`threadCommandFreshMetadata` plus model/effort. The shared fixture at
`main_test.go:231–235` has no `modelProvider`. The real `coordinationNotify`
send at `coordination.go:110` now goes through managed SendWithOptions;
`workspacecodex/turn_retry.go:226–230` requires a provider at admission, and
`:121–132` rejects the missing field with the exact logged diagnostic.

The test metadata must provide its selected synthetic provider. Production
provider validation must remain strict. This is a fixture omission exposed by
the added managed admission, not evidence that real native provider metadata
is unavailable. A minimal candidate correction is to add `modelProvider` to
this test's metadata (or the shared fixture if its callers require it), then
run both active/idle notification cases. No correction has been applied.

## Failure 2: browser fixture omits the new imported module

```text
--- FAIL: TestShippedBrowserClientMatchesSessionAPI
    server_test.go:4173: browser contract failed: exit status 1
        Preparation browser contracts passed: 29 cases
        Error [ERR_MODULE_NOT_FOUND]: Cannot find module '.../retry.js'
        imported from .../conversation.mjs
```

cca log: archive2460–2475, creation5013–5028, fast6488–6504.
85 log: archive3022–3037, creation6170–6185, fast8331–8347.

`portal/internal/web/server_test.go:4151` copies an explicit dependency list
beside its temporary conversation module. It copies uploads/sync/refresh/
questions/citations, but omits retry.js. Pinned A
`d2d74f931cc50e39345c6c15931748062ee51951` conversation.js:8–9 imports/exports
`./retry.js?v=1`. The imported file is provided by A's assets and has no further
imports. The smallest candidate correction is to include retry.js in the
consumer fixture's copied dependencies, then run the actual browser contract.
Do not edit A or weaken the browser test. No correction has been applied.

## Applicability and focused-check gap

`git diff --exit-code 85f6f73 HEAD -- coordination_test.go main_test.go server_test.go`
(with their full repository paths) is empty; the same is true from cca.
The current A pin and its retry.js import are unchanged. I3 changes only its
settings-owner source, new production-path fixture and accepted recovery-guide
paragraph. Neither prior failure is corrected by I3.

The previous quick/race selectors cover Controller/Retry/TurnRetry, retained
resolver/recovery and selected command settings/provider/initial paths. They
omit `TestCoordinationNotificationRetainsSettingsAndDeduplicatesNativeDelivery`
and `TestShippedBrowserClientMatchesSessionAPI`; the native-tag compile/list
does not execute either. Their absence is a focused-check gap. No broad test
or build is necessary to exercise these two already-observed bounded failures
once lead releases a correction. Targeted correction selectors would be:

```sh
cd portal
TMPDIR=/tmp go test -mod=readonly ./cmd/workspace-portal -run '^TestCoordinationNotificationRetainsSettingsAndDeduplicatesNativeDelivery$' -count=1
TMPDIR=/tmp go test -mod=readonly ./internal/web -run '^TestShippedBrowserClientMatchesSessionAPI$' -count=1
```

The snapshot taken immediately after publication shows new run39814474141 at
head61de queued. It has not been awaited or canceled. Both superseded runs are
completed; there is no superseded active work to cancel.
