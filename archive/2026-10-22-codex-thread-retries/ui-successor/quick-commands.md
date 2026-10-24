# B presentation quick commands

CWD: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace`.
Source: final tree `28a9d72044dc3ffa7eb4f817cbb2c4d6c9614d18`.
Final consolidated head: `39497062e0da98a70386355384fa922c0eaa0168`.

```sh
nix develop --no-update-lock-file --command bash -c '
  set -e
  node --check portal/internal/web/static/app.js
  node --check portal/internal/web/retry_activity_browser_test.cjs
  node portal/internal/web/paging_browser_test.cjs
  node --test portal/internal/web/read_cycle_browser_test.cjs
  gofmt -l portal/internal/web/question_browser_test.go portal/internal/web/server_test.go
  cd portal
  TMPDIR=/tmp go test -mod=readonly ./internal/web \
    -run "^Test(ShippedBrowserClientMatchesSessionAPI|PlanDelivery.*|HTTPMutationWaits.*)$" \
    -count=1 -v
  TMPDIR=/tmp go test -mod=readonly ./internal/web -run "^$" -count=1
'
```

Result: PASS, `b-final-quick.log`. The final fixture-only action request barriers
were syntax checked again after this batch, in `b-final-syntax.log`. All product
source and compiled Go test code matched the final tree; the history
consolidation changed no tree bytes. No Playwright fixture execution occurred.
The expensive controlled capture is a separate `capture.sh` command for the
lead's post-review watcher, not part of these compile/quick receipts.
