# One-shot policy reload preparation

Prepared and compiled, with six passing disposable Unix-socket fixture cases.
No live connection or RPC was performed. Lead separately owns dispatch release. The prior
`config-read-once.json` remains unchanged: its incorrect JSONL transport sent no
`config/read` request.

The tracking-only source is `config-read-ws-once.go`, SHA256
`4e33e0c2a51f391a6bc485cfec78f38646983bc3438feaa294c228e5d221bb8e`.
The executable is `config-read-ws-once.helper`, SHA256
`ca489a8a3d1b60a25573b79f31420a7c71b0838a18047153f9bffe5b26e4bc70`.
The original inspected source/hash/receipt set is preserved in
`ws-build-fixture/prepared-original/`. `config-read-ws-once.source-hashes.json`
describes those original inspected inputs; `ws-build-fixture/handoff.json` binds
the final source, fixture, binary, incremental diff and exact command receipts.
Product files and D1 are unchanged by this lane.

## Supported transport and initialization

The isolated tree's `portal/go.mod`, `portal/go.sum` and flake pin select
codex-web `5743f94c2fbd01b65438847d2e2bab0f01df32ae` and
`github.com/coder/websocket v1.8.14`. Cached module origin metadata independently
names that exact commit. Source references:

- `codex/client.go:966–1001`: `websocket.Dial` to `ws://localhost/` through an
  `http.Transport` whose `DialContext` dials the Unix socket. The library performs
  the HTTP Upgrade and WebSocket framing; the helper implements neither itself.
- `portal/cmd/workspace-portal/main_test.go:238–315`: the command fixture accepts
  WebSocket-over-Unix, requires `initialize` with `experimentalApi:true`, returns
  its response and reads the subsequent notification.
- `portal/cmd/workspace-portal/live_switch_integration_test.go:337–386`: native
  test transport uses the same public `websocket.Dial` and explicit initialization.
- `portal/cmd/workspace-portal/naming_runtime_integration_test.go:664–672`: the
  native fixture uses the public `config/read` with `includeLayers:false`.

Exact helper sequence: one Unix connection; verify `SO_PEERCRED` before any HTTP
bytes; supported WebSocket Upgrade; numeric request ID 1 `initialize` with
`capabilities:{experimentalApi:true}` and clientInfo
`{name:"dev-workspace-network-recovery",title:"Development Workspace network recovery",version:"0.1.0"}`;
wait for its matching successful response; send `{"method":"initialized"}`;
recheck binding, selected helper, held machine claim, native and socket identity;
send exactly once
`{"id":2,"method":"config/read","params":{"includeLayers":false}}`;
wait for its matching response; verify `SO_PEERCRED` again on the same connection;
close this client connection; recheck the process, socket, binding and claim.
`cwd` is absent. Request IDs are only per-connection RPC correlation IDs.

The helper directly uses the existing pinned transport instead of the full
interactive `codex.Client`: its public options provide no custom dial hook for
`SO_PEERCRED`, and its interactive receive loop can answer unsupported requests.
The helper has no subscriptions, thread activation, lifecycle calls or server
request answers. It discards notification parameters without decoding them and
refuses unsolicited server requests. At most 64 incoming envelopes are accepted
per response; that receive bound does not resend any request. The production
64 MiB WebSocket read limit is retained.

## Identity and deadline guards

Read-only preparation reverified the complete bound environment and roster 34,
including implementer3's saved Sol/xhigh/workspace_write settings. It also verified:

- Claim `201af6c8-08a2-48e6-be3e-b69ce916eee1`, owner
  `7cbe38cb-30c7-452d-8015-3907552c550d`, held resource
  `machine:vpsfree:aitherdev`.
- Unit `workspace-codex@vpsfree-cz.service`, active/running, PID `3387667`,
  InvocationID `84b92a0a1c5a4fffa9a0c7beaf0693f1`, start ticks `1162579375`,
  NRestarts `0`, all UIDs `1000`, all GIDs `100`, native executable
  `/nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0/libexec/codex/bin/codex`.
- `/run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock` is a symlink:
  device/inode `77/121544`, ctime ns `1792318082724922848`, UID `1000`.
  Its exact target is
  `/tmp/codex-daemon-1000/bced879de15a05f23836072b53ea2860aa13a982415f07bf83ab93a6ee8c9ea6`:
  socket device/inode `64769/18745722`, the same ctime, UID `1000`.

These are expected identities, not new connection evidence. The preparation did
not query `SO_PEERCRED`, because that requires connecting. At dispatch it must
prove peer PID/UID/GID `3387667/1000/100` before HTTP Upgrade and again after the
response. The helper pins both the symlink and target identities. It also refuses
if the selected dev-session path changes from
`/nix/store/1zkafvr6ns84wdmdh7qrmhx77c90wpxw-dev-workspace-0.2.0/bin/dev-session`.
A package or socket identity change requires refreshed preparation and lead
review, not editing the receipt or relaxing the guard during dispatch.

The helper's complete operation context expires after 19 seconds, below the
required 20-second ceiling. Socket connection, initialization and config response
share an absolute 13-second deadline from helper startup; six seconds remain for
postchecks. Initialization also has the production 10-second subdeadline.
Each read-only metadata subprocess has a 1.5-second limit and a 0.1-second pipe
wait bound. There is no reconnect or RPC retry. HTTP redirects and a second Unix
dial are refused. Missing postchecks produce a sanitized failure and stop.

Only UTC, method, verified identities, success, config write progress booleans and sanitized error categories
reach stdout. Configuration, origins, layers, initialize result fields and remote
error messages are never materialized into value-bearing response structs. The
JSON decoder validates envelopes, skips unknown fields and records only result
presence/object type and error presence. Frame buffers are cleared after parsing;
all remote payload handling remains in memory. No credentials or configuration
files are read by the helper. The native owner performs its usual config load.

`configReadAttempted:false` proves the sole config/read WebSocket `Write` was
never entered. `true` with `configReadFullyWritten:false` leaves the write's
native outcome uncertain, including the possibility of zero transmitted bytes.
Both true means the WebSocket write returned successfully; it does not prove
native acceptance or reload completion without a successful matching response.
The flags are explicit booleans in every receipt. They are the only receipt
expansion. Two connection-only exchanges were extracted for the fixture;
`perform` still checks all live guards before either initialization or config read.

## Compilation, fixture and exact commands

The compiled helper is executable without further building. Its Go source alone
requires compilation; `go run` also builds and must not hide that work inside the
operation deadline. No generic installed `config/read` CLI was established in the
inspected command dispatch. The binary records Go 1.26.6, CGO_ENABLED=1 and the
exact pinned websocket v1.8.14 module checksum. It has not been executed.

Lead released compilation and a bounded disposable fixture. Owner1 opened the
compiler window; source and fixture were frozen before launch. The following
build exited 0 in 2.206 seconds:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/incident-network-permission
sha256sum --check config-read-ws-once.source.sha256
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace-delete-guard
nix develop --no-update-lock-file --command go -C portal build -mod=readonly -o /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/incident-network-permission/config-read-ws-once.helper /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/incident-network-permission/config-read-ws-once.go
```

The explicit-file fixture used the same Nix command prefix, then
`go -C portal test -mod=readonly -count=1 -timeout=20s -run '^TestConfigReadUnixSocket$' -v`
with absolute paths to `config-read-ws-once.go` and `config-read-ws-once_test.go`.
It exited 0 in 2.215 seconds; the Go test itself took 0.032 seconds. Six cases
passed: success, mismatched initialization ID, mismatched config response ID,
remote error, canceled before config write, and failed config write. The actual
pinned WebSocket transport connected only to each test's temporary Unix socket.
The server verified initialization/notification/request order, one config read,
`includeLayers:false` with `cwd` absent, and no extra application message. Opaque
config/origins/layers and remote error sentinels were absent from the encoded
whitelist receipt. No fixture called `main`, `perform`, `snapshot` or `peer`.
Client/server/socket cleanup completed through normal test cleanup.

Raw command/exit evidence is retained in `ws-build-fixture/build-command.json`,
`fixture-command.json`, `build.log`, `fixture.log` and `binary-inputs.log`.
The source and binary checksums are in the corresponding `.sha256` files.
Any source change invalidates this preparation hash and binary pairing.

Proposed dispatch command, **held** until the lead reviews the compiled helper
and separately releases exactly this operation:

```sh
set -eu
umask 077
cd /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/incident-network-permission
sha256sum --check config-read-ws-once.source.sha256
sha256sum --check config-read-ws-once.helper.sha256
set -C
./config-read-ws-once.helper --dispatch-once-after-lead-release > config-read-ws-once.receipt.json
```

This command has not run and remains held for separate lead release. Shell
noclobber preserves the first receipt, including any failure.
No retry or second invocation is authorized by this preparation. A write error
or response timeout can have an uncertain native outcome; stop and report the
sanitized receipt. Closing this utility's own connection is not a native stop.

Success would establish normal policy reload only. It would not establish
provider reachability, original cause or recovery of old revoked requests.
No product documentation change is useful for this one-operation preparation;
the accepted design and existing incident findings retain the explanation.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
