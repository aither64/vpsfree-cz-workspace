# Fixed-root metadata observer

The parent subsequently ran this probe on the actual host. Loaded enumeration
did not contain the old root; exact-target read/turns/idle probes reported
thread-not-loaded. [Observation](../root-observation.md) records the frozen
method-labelled result and limits. The old root and its journal remain untouched.

The preparation details below describe the prototype at authoring time. No App
Server connection or execution occurred during architect preparation.

The failed public `thread observe` is composite: runtime `ObserveThread` first
calls `ListThreadActivity` → SDK `ReadThreadMetadata` (`thread/read`), then
`RequireThreadTurnsIdle` (`thread/turns/list`, with `thread/read` fallback).
Both can propagate the unprefixed `thread not loaded` RPC error. Selected 0.160
source has that diagnostic in both `read_thread_view` and
`load_thread_turns_list_history`. Later pending-request/queue failures have
explicit prefixes. The aggregate error does not identify which RPC failed.
The old metadata helper's `excludeTurns` argument is not the selected read
contract's `includeTurns`; this probe explicitly sends `includeTurns: false`.

The module pins SDK commit `4c170393a96ed0a6ac2e43488d073f6fcab36132`, version
`v0.0.0-20261002145902-4c170393a96e`. All six checksum lines are copied exactly
from the existing consuming runtime's `portal/go.sum`; there is no replace
directive. The executable checks build metadata and refuses a different SDK
version or any module replacement. It accepts no arguments and has one fixed
socket/thread/cwd matching the diagnosed fixture.

SDK4c's `ObserverOnly` request allowlist omits `thread/loaded/list`. Following
the parent's explicit clarification, only loaded enumeration uses the ordinary
SDK public `LoadedThreadIDs` API and its existing client policy. It has no watches,
subscriptions, nonblocking-input policy or activity recorder and is then closed.
All target probes use a separate `ObserverOnly` client. The SDK is unchanged.
No new raw WebSocket client or permission exception is introduced.

The output is newline-delimited JSON, with timestamps and one labelled row for:

1. Fixed socket, target, cwd and SDK version.
2. Loaded enumeration: target membership and total count only; other IDs omitted.
3. Explicit metadata-only `thread/read`: exact returned ID/cwd, source equality,
   identity match, ephemeral/paginated and idle-status metadata.
4. SDK `HistoryMaterialized`, only after an exact ID/cwd/source match. It performs
   another metadata read and a path `stat`; no rollout payload is opened. Failure
   is unknown, never `materialized: false`. Otherwise this step is marked skipped.
5. `thread/turns/list` with limit 1, descending and `itemsView: notLoaded`:
   count and recognized latest status only, no turn items/content.
6. SDK `RequireThreadTurnsIdle`: turns-list and, on failure, its existing read/stat
   fallback. It proves only the SDK turns-idle check, not pending/queue emptiness.

Each step has a ten-second context; the SDK handshake can occur inside a probe.
An initialization/transport failure is reported as such rather than proof the
labelled RPC reached the server. Exact known target diagnostics retain their
RPC code/message; arbitrary messages are omitted. No prompts, preview, history,
raw errors, authentication, queued inputs or thread content are printed.
There is no resume/start/watch/subscription/turn/queue mutation or durable
submission-ledger access. The program writes only JSON to stdout and a fixed
configuration refusal to stderr. It does not save a report or modify private files.

## Parent command

Use the same aitherdev SSH, `sudo -H -u aither`, prepared runtime Nix environment
as earlier actual-host checks. From this module directory:

```sh
GOWORK=off GOTOOLCHAIN=local go test -mod=readonly ./...
GOWORK=off GOTOOLCHAIN=local go run -mod=readonly .
```

The first command exercises only two pure diagnostic-redaction tests; it never
calls `main` or connects to a socket. Go compilation/module caches are ordinary
build outputs and should remain outside the old fixture. The second command
connects to the exact retained socket and must be run only by the parent under
the assigned read-only investigation. Freeze stdout outside `/tmp/pcp-oct02-a`
in the parent's private evidence location. Do not put credentials in argv or logs.
The Go exit status reports completion of observation, not recovery acceptance:
individual failed probes remain explicit JSON rows even with process exit 0.

Preparation checks passed `gofmt` parsing and static assertions for exact direct
read methods/options, absent mutating/file-content APIs, passive target-client
selection, build pin and six consumer checksums. The two Go tests, compilation
and actual-host observation are prepared but were not run by the architect.

## Interpretation and next decision

Observations are sequential and are not an atomic ownership proof. Consistent
loaded membership plus exact, fresh/unmaterialized and idle metadata can support
the parent's reassessment of the held same-root driver. False membership plus
`thread not loaded` reads supports current unavailability, not deletion or
authorization to replace it. Conflicting or incomplete probes stay uncertain.
Never broaden `IsThreadNotFound`, reset attempts, or retry the old failed receipt
to turn this observation into a repair.

The parent chose two fresh fault slugs in the retained private runtime through
the separately reviewed provider boundary. Both real cases subsequently passed:
[fault results](../verification-corrected-faults.md). Old evidence and all five
timings remain unchanged. This observer supplies no recovery authority and does
not authorize replay, replacement or repair of the unavailable old root.
