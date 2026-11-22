# P1-F: restore legacy queue error stages

Owner: implementer0. Completed 2026-11-12 for lead acceptance.
Commit `ee0c866317419209b859b27a09026d63e722c4c7` over
`f9b9b4831b23aab5ddf61316eefdd02edca1cc7c` in C (`codex-web`).
Only `conversation/backend_codex.go`, `conversation/handler.go` and new
`conversation/queue_compat_test.go` change: 161 insertions / 3 deletions,
including 135 lines of regression fixtures. P7 remains parked.

## Cause and correction

The original handler at C `dd90fb4308ba85617ee2a4267cc835aa9a4f11ce` handled
`Client.Queue` errors through `serverError` (503), then `ObserveQueue` errors
through `uploadError` (500 for an ordinary filesystem error, or the bounded
application UploadError response). P1's neutral queue operation merged these
stages into one error return and classified it with `readError`.

Consequently, an UploadError originating from native queue dispatch incorrectly
became a public attachment error (400); an ordinary post-acceptance observation
error incorrectly became a native service error (503). The D upload contract
tests exposed both regressions. Error type alone cannot recover the stage.

A private `legacyQueueError` now carries that stage and unwraps the original
cause. Only the legacy Codex adapter creates it. Common POST queue error handling
restores the two original mappings for this wrapper; neutral errors retain their
existing handling. Callback order remains Prepare → native Queue → original
native ObserveQueue → forward projection; native failure prevents observation.

Fixtures cover generic and wrapped UploadError causes at both stages, exact
HTTP status/body, no disclosure of private details, native cause logging,
`errors.Is`/`errors.As` cause retention, success projection after native
observation and unchanged neutral mapping. No public signature, DTO, optional
support, native Codex behavior, browser asset, schema or receipt change.
The nearby source comment explains the stage invariant; product documentation
needs no change because this restores its existing compatibility promise.

## Checks and exact inputs

All terminal results were inspected before reporting success. Actual C cwd was
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-pi-codex-migration/codex-web`.
Its package-derived environment ran:

```sh
nix develop .#packages.x86_64-linux.default --command bash -ec \
  'gofmt -w conversation/backend_codex.go conversation/handler.go conversation/queue_compat_test.go;
   go test -mod=readonly ./conversation \
     -run "^(TestLegacyQueueErrorStagePreservesHTTPContract|TestNeutralQueueErrorMappingUnchanged)$" -count=1 -v'
nix develop .#packages.x86_64-linux.default --command \
  go test -mod=readonly ./conversation/... ./cmd/codex-web-example -count=1
```

Both exit 0. New exact cases: package 0.016 s; existing focused suite:
conversation 0.129 s, example 0.020 s. The current C worktree retained P6's
uncommitted asset edits; none were staged or edited by P1-F.

D consumer verification used a separate `git archive` of committed
`67e08f2f10faa288aefb7e97e2d3eb19d8819eb6`, plus a separate C archive of `f9b9b48…`
with only the three P1-F files overlaid. Actual tool cwd was
`/tmp/2026-11-11-pi-codex-migration-p1-f/d-source/portal`. The exact cached D
environment avoided the parked current D flake:

```sh
nix develop /nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv --command bash -ec \
  'cp go.mod consumer.mod; cp go.sum consumer.sum;
   go mod edit -modfile=consumer.mod \
     -replace=github.com/aither64/codex-web=/tmp/2026-11-11-pi-codex-migration-p1-f/c-source;
   go test -mod=readonly -modfile=consumer.mod ./internal/web \
     -run "^TestSubmissionFailureAfterNativeDispatch$/^queue$/^(native-error|post-acceptance-observation)$" -count=1 -v'
```

Exit 0, package 0.224 s; each unchanged consumer case passed in 0.09 s.
`queue/native-error` retains 503 / `Codex service is unavailable`;
`queue/post-acceptance-observation` retains 500 / `file operation failed; retry shortly`.
No shared D module/pin or partially written peer Go source was used or changed.

SHA256 provenance (isolated C overlay, checked worktree files and committed blobs agree):

| Input | SHA256 |
| --- | --- |
| C `conversation/backend_codex.go` | `fa69c0ca8aa59e3da407abeca9df41bc7cd933770bd5147cece444b3eaf0ea54` |
| C `conversation/handler.go` | `90f25947fe8669d58c40c5e22881651c6b950b536505c1bd3468a1d84862bb74` |
| C `conversation/queue_compat_test.go` | `b2ad0557ce676d9859f991f872fcfa4e5efa60bc6cc6c17b66c8472368030ee8` |
| D temporary `consumer.mod` | `89abf54c96a66ef9a7c025180f7e3c3b4d3bbf7676d23af3d5871a9f31b8d035` |
| D temporary `consumer.sum` | `434e3dd9b9c9831e0534fbdfe92404fc92279ec69a47bc3161cb6eb258bd1069` |
| Unchanged D `submission_validation_contract_test.go` | `9ad87b42865ed610237faea61ad83e1160bd88c9a290f5b1fbc67cf9404838c9` |

Normal file-message commit ran with no bypass; no declared hook framework or
active hooks were found. Commit/whitespace checks pass. Index empty and owned
working diff empty at window closure; P6's two files stayed unstaged.

This is one focused follow-up to P1's already published C head, consumed by the
accepted D pin. No history rewrite, migration, deployment, model call or lifecycle
action occurred. No root suite/full web suite/CI rerun or C push was launched.
Lead owns whole-branch review/publication sequencing; P6 appends to this commit,
then P7 can consume the final published C head and consolidate its pin stream.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/)
