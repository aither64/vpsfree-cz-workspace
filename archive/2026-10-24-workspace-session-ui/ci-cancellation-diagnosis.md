# CI cancellation failure diagnosis

Recorded 2026-10-25 by implementer0, read-only source investigation. The lead
accepted this as strong evidence of an unrelated baseline fixture/transport
race. The exact goroutine ordering in the failed run remains unproven.

## Observed failure

- Feature head: `45deeeacf119eb733852a5df21abd6e030262e26`.
- Baseline: `b3a6eb2fc0b41cf0cb965bf4c39991815d9df734`.
- CI run [40136013348](https://github.com/aither64/dev-workspace/actions/runs/40136013348),
  fast job `120997564897`.
- [Saved failed log](ci-fast-failed.log), lines 1876–1881: web tests passed;
  `TestRetireThreadPersistedEmptyRootRefusesUnsafeEvidence/cancel` failed at
  `portal/internal/workspacecodex/client_test.go:1247` with:

  ```text
  cancellation changed find session conversation: Codex App Server disconnected: failed to get reader: use of closed network connection
  ```

The fatal error-class assertion precedes the retained-attempt and zero-archive
assertions. The failed run does **not** prove that those effect assertions passed.

## Baseline equality

`git diff --exit-code` between these revisions returned success for
`portal/internal/workspacecodex`, `portal/go.mod`, `portal/go.sum`, and
`flake.lock`. Both revisions contain these exact Git objects:

| Path | Equal object ID |
| --- | --- |
| `portal/internal/workspacecodex` tree | `28c35b0414ae97983e8c0fe0ad26fe3876f525cd` |
| `portal/internal/workspacecodex/client.go` | `8642a734e0e5dadc9ae8a2c959f617ff3a8755e4` |
| `portal/internal/workspacecodex/client_test.go` | `5ed876f27415623d71cedf65cf08fe9e69742a4d` |
| `portal/go.mod` | `53f4dcd7b631edac498fc658955ace8b02650275` |
| `portal/go.sum` | `60b7df9070caffaddc4c373919eba18eb2534abb` |
| `flake.lock` | `d5cb89fae62b268af86043cfda87cd75a6b0c2ea` |

Unchanged relevant pins: codex-web
`v0.0.0-20261024144044-11ec57d2203f`, full revision
`11ec57d2203fc735696fe75a837d47da55a5c6af`; coder/websocket `v1.8.14`.
Their module checksums are respectively
`h1:cod93lovFHu5adtEqQy7QyE1E5YIFJrTkCnjB3phFgw=` and
`h1:9L0p0iKiNOibykf283eHkKUHHrpG7f65OE3BhhO7v9g=`.

## Source-supported mechanism

1. The fixture calls `f.cancel()` when it receives `thread/loaded/list`
   (`client_test.go:1011–1015`), before writing its reply at line 1159. Peer
   receipt does not establish that the client's write cleanup has completed.
2. Pinned coder/websocket `conn.go:171–176` registers a context cancellation
   callback that closes the connection while a write is active. Its
   `write.go:276–277` clears that callback on frame-write exit.
3. Cancellation overlapping write cleanup can therefore close the socket.
   Pinned codex-web `codex/client.go:1216–1219` forwards read failure to
   `markDisconnected`; line 1533 sends the pending RPC the wrapped disconnect
   error seen in CI.
4. `requestOn`, lines 1148–1161, selects between its response channel and
   `ctx.Done()` without cancellation priority. If both are ready, the returned
   error can be the transport failure instead of `context.Canceled`.
5. `workspacecodex/client.go:805–807` returns a loaded-list error before archive
   or attempt clearing. Both cancel assertions, at test lines 1246 and 1313,
   use the same fixture and are susceptible to this error-class race.

These unchanged paths explain the observed failure without a portal UI
regression. This investigation did not reproduce the failure or establish the
unique scheduling sequence of the CI attempt.

## Follow-up and limits

No application or test change was made. The lead decided to preserve the
unchanged lifecycle/client tests within this portal scope. No broad acceptance
of transport errors, timing sleeps, or production cancellation changes are
implemented or recommended as an unreviewed workaround.

The initial bounded follow-up proposal was to distinguish actual cancellation
from its narrowly identified closed-connection transport consequence while
retaining canceled-context, attempt-retention and zero-archive requirements in
both tests. This remains a proposal requiring separate evidence and review.
First use lead-owned watcher verification to stress the two cancellation cases
and complete the native remainder; retain diagnostics if the failure recurs.
Revisit the diagnosis if that evidence shows a current functional regression.
A green rerun alone cannot establish the cause of the original failure.

No tests, CI reruns, source edits or Git mutations were performed by this
investigation. The lead reported local package PASS at the exact feature head
and composer Chromium PASS; implementer0 did not independently rerun them.
Paging fixture diagnosis remains assigned to implementer1.

Identity was reverified with `dev-session current` and both matching environment
values before writing this record. A command fenced by a package-generation
transition was retried through the stable command and printed the bound slug.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/>
