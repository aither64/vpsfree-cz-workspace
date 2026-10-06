# Verification evidence

## Quick checks before review

All commands used repository-pinned Nix Go, GCC and Node tooling.

- Provider: `node --test test/uploads_browser_contract_test.cjs`: 31 passed,
  no skips/failures; `go test ./conversation`: passed.
- Provider/runtime changed JavaScript syntax and diff whitespace: passed.
- Runtime focused `./internal/uploads ./internal/web` selectors for
  TestDefaultPromptFiles, TestPreparationUpload, TestQuotasAreReserved,
  TestSessionPreparation, TestDraftUploadHTTP and
  TestShippedBrowserClientMatchesSessionAPI: passed after final provider pin.
  The shipped Node harness executed from the Go test with Node present.
- Go/Nix provider pin coherence script: passed for
  v0.0.0-20261004200036-3d07cf60cfde.
- Earlier runtime failure: wrong new HTTP status expectation and stale cache
  version assertions; fixed in owning commits, final log passed.

Detailed logs: quick-codex-web-browser.log, quick-codex-web-go.log,
quick-dev-workspace-pinned.log; initial quick-dev-workspace-go.log retained.
Vendor hash generated from pinned `go mod vendor` output; packaged build will
validate the fixed-output hash. No byte quota or generic/store ceiling changed.

## CI

Provider Check run 37230494334: success at exact
3d07cf60cfde5d117a181a9bdb6d90a5860f6f0c. Runtime push/CI pending review.

## After review

Both full `nix flake check --print-build-logs` suites passed at their exact
reviewed heads. Runtime build validated the generated vendorHash. Logs:
packaged-codex-web.log and packaged-dev-workspace.log. Opt-in/real-tmux skips in
unchanged packaged tests are expected; focused upload/preparation selectors and
Node contracts ran rather than skipped.

Pinned Chromium acceptance: passed at 1280px and 375px using the matching provider,
actual host/provider CSS and 50 long filenames. Creation lists expand with page
scroll and every removal/Create action is reachable. Verified full total size
while incomplete, completed count, 51-file rejection, removal/re-add, reload, exact-body
lost-response recovery, cleanup and unchanged 12rem conversation cap.
Log: creation-browser.log; watcher [result](acceptance-result.md), exit 0,
about 7m30s. It did not perform live inference, deployment or real session switch.

Prior-ten-file reader harness: passed all four nonzero phases against exact base
6a972b9ab01077611b2c60e0fc726c185e050315 and current reviewed head. Genuine
unfinished 50-file snapshot was refused by the old strict reader and loader
without state mutation. Current normal recovery and compaction retained all 50
uploaded files, and old strict reader/loader accepted the compact mapping without
mutation. This is format/compaction evidence using existing proof helpers; it
performs no live initialization or installed downgrade. See older-reader.log and
[reader/CI result](reader-ci-result.md), exit 0 in about 19 seconds.

Runtime Check [run 37231243553](https://github.com/aither64/dev-workspace/actions/runs/37231243553)
completed successfully on exact final head 3edc605d81a30a4d49560426e0128b388b856493.
CI JSON records are runtime-ci-before.json and runtime-ci-final.json. Provider
Check [run 37230494334](https://github.com/aither64/codex-web/actions/runs/37230494334)
also passed on its exact final head. No retries or cancellations were needed.

All planned checks passed. Both clean pushed feature branches are ready for
integration on explicit user direction. No deployment or default-branch merge
was performed or authorized. No verification operation remains running.
