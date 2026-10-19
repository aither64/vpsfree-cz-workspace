# Implementer preflight

Read-only inspection by `implementer0`, 2026-10-03. Application implementation
awaits the coordinator's next explicit assignment and architect0's design.

## Identity and prerequisites

- `dev-session current` from this tracking directory printed
  `2026-10-03-automatic-session-slugs`, matching the trusted thread binding to
  `/home/aither/workspace/ai/vpsfree.cz`. Both environment identity variables
  were absent. Calling `current` from the workspace root first found no session;
  resolving it from the intended directory established the required identity
  before reading session files.
- Read workspace `AGENTS.md`, full projects, sessions, lifecycle, documentation,
  verification, Git, and commits procedures; both repositories' `AGENTS.md` and
  README; installed documentation/handoff skills and the runtime's documentation
  skill. Read this initiative's plan/state and relevant reference documentation.
- The two assigned project worktrees were clean at inspection. Shared workspace
  status contains extensive unrelated changes; existing plan/state changes and
  portal metadata remain coordinator-owned. This report is the only written
  file. No tests, application edits, commits, pushes, deployment, or lifecycle
  commands were performed.
- `portal/go.mod` currently selects codex-web
  `v0.0.0-20261002145902-4c170393a96e`. Consumers of the new public helper need
  the agreed dependency update or an isolated temporary Go module override for
  local development. A sibling worktree alone does not change Go resolution.

## Hooks and suitable quick commands

Neither repository declares Overcommit, pre-commit, Lefthook, or Husky; neither
has a configured `core.hooksPath`. Their canonical hook directories contain
only inactive `.sample` files. Both retain mandatory hook instructions if a
framework is added. Nix phases invoke `runHook preCheck/postCheck`; these are
build hooks, not installed Git hooks. No hook installation is needed currently.

Both flakes expose package derivations and checks, without explicit
`devShells`. The following use the default/package derivation development
environment, whose check inputs supply Node and Python/jsonschema; dev-workspace
also supplies Ruby, Git, jq, tmux, and related test tools. Commands are derived
from source and have **not been executed**. Provisioning and any checks of
uncertain duration belong to a fresh verification watcher when authorized.

From the codex-web worktree:

```sh
nix develop .#default -c go test ./codex -run 'Test(SendWithOptionsUsesStartAndSteerProtocolFields|ObserverDisconnectAndCloseCancelQueuedRestoration)$' -count=1
nix develop .#default -c python3 test/codex_protocol_contract.py --coverage-only codex/client.go
nix develop .#default -c node --test test/conversation_browser_contract_test.cjs test/uploads_browser_contract_test.cjs test/sync_browser_contract_test.cjs
```

Add the new ephemeral helper's focused tests to the first command after their
names are established. The packaged suite uses `go test ./...` and the three
browser files above; `paging_browser_contract_test.cjs` exists but is not listed
in codex-web's current flake check phase.

From the dev-workspace worktree:

```sh
nix develop .#dev-workspace -c go -C portal test ./internal/web -run 'Test(Creation|Draft|BrowserCreation)' -count=1
nix develop .#dev-workspace -c go -C portal test ./internal/uploads -count=1
nix develop .#dev-workspace -c node --check portal/internal/web/static/app.js
nix develop .#dev-workspace -c node --check portal/internal/web/static/creation.js
nix develop .#dev-workspace -c node portal/internal/web/browser_contract_test.cjs --unit
```

If Ruby creation behavior changes, a suitable focused entry point is
`nix develop .#dev-workspace -c ruby test/dev_session/creation_progress_test.rb`.
The complete Ruby suites remain `test/dev_session_test.rb`,
`test/auto_archive_test.rb`, and `test/workspace_host_test.rb`.

Packaged verification is `nix flake check --print-build-logs` in each repository,
after committed quick checks and mandatory review. Live Codex tests require
`CODEX_WEB_TEST_BINARY`; real portal browser tests require `PORTAL_BROWSER_TEST=1`
and the documented Playwright environment. Those are later checks, not evidence
from this preflight.

## Existing fixtures and integration seams

| Boundary | Current source and convention |
| --- | --- |
| Public client | `codex/client.go`: `Request` establishes the connection; `ListModels` follows pages. `StartThreadWithSettings` injects persistent instructions/runtime roots. `Subscribe` calls `thread/resume`, registers reconnect watches/history/activity, and returns coalesced change signals. |
| Raw notifications | `Client.readLoop` sees complete RPC messages, then broadcasts a signal. The new helper needs a separate ephemeral notification route registered before starting its turn; ordinary subscriptions discard the message payload. `Interrupt` discovers the turn through persisted-history RPCs, so cleanup should use the utility turn ID directly. |
| Client tests/protocol | Fake Unix WebSocket servers use `serveUnixWebsocket`, `handshake`, `readObject`, and `writeObject`, with controlled notification/RPC order. `test/codex_protocol_contract.py` counts literal RPC call sites across **all non-test Go files** and requires matching corpus multiplicity. Extend requests, responses, and notification cases, then validate against the exact deployed Codex schema. Existing approval fixtures are versioned `0.152.1`; that fixture label is not proof of the deployed protocol version. |
| Receipt acceptance | `web/creation.go:acceptCreation` holds `operationMu` and the destination runtime lock, checks work/archive/worktrees/lifecycle state, generates a random 64-hex receipt ID, saves before launching a worker, and replays a matching slug/request. `creation_store.go` owns separate strict receipt schemas 1–3, private atomic synced writes, restart pausing, and a 512-entry terminal eviction cache. |
| Receipt worker/progress | `initializeCreation` rechecks the package generation under the transition lock. `Server.Close` cancels and joins workers. Completion requires receipt-bound CLI evidence and upload binding. Retry compares receipt ID and attempt; stale progress cannot alter newer attempts. Preserve these proof boundaries. |
| Uploads | `web/uploads.go` serializes acceptance/collection with `uploadCreationMu`. `Store.Prepare` freezes text/IDs into a submission; initial submissions start as `prepared`. `RetainCreations` promotes accepted ones to `pending`, which existing collection retains. `BindCreation` then adopts them into the final slug/thread/epoch. |
| Browser | `index.html`, `app.js`, `creation.html`, and `creation.js` own New session and progress. Creation draft storage is tab-local; the upload scope is shared through local storage. The current success URL guard permits only a single slug segment. Progress assumes a slug-keyed endpoint. Draft helpers are also used by plan creation. |
| Portal tests | `creation_test.go` uses temporary workspace/state, blocking fake Codex clients, fake CLI commands, and exact binding/evidence writers; it already covers nonblocking acceptance, restart, stale attempts, generation changes, foreign destinations, and retirement. `uploads/store_test.go` uses tiny quotas and an injectable clock. Browser unit contracts import exported helpers from `app.js`; HTTP contracts run through `server_test.go`, while Playwright checks are opt-in. |

## Concrete design concerns

1. **Nonblocking acceptance:** `resolveManagedCreation` ignores its context and
   calls `ListModels(context.Background())` synchronously for submitted lead
   overrides before persistence. Resolve how accepted settings are validated
   and frozen without an unbounded pre-acceptance App Server dependency.
2. **Exact handoff:** a predetermined receipt ID must be checked alongside the
   request. Existing slug/request replay alone can return an unrelated matching
   receipt. Preserve frozen IDs across every preparation/receipt write gap.
3. **Pre-slug uploads:** reservation needs durable request ownership and mutation
   checks, including competing tabs. Promote accepted submissions to existing
   `pending` retention and reconcile preparation records before collection.
   Existing retention is keyed by encoded wire text, not preparation identity;
   do not infer ownership from equal prompt text.
4. **Raw text and browser recovery:** the current POST and upload `Prepare`
   trim text; new request identity/naming must retain raw text separately from
   normalized CLI/wire text. Draft persistence currently reports success even
   when optional storage is absent and does not verify read-back. Establish the
   request ID durably before POST, preserve it after response loss, and reject
   changed input under that ID. Extend safe URL guards to the exact new route.
5. **Isolation and cancellation:** avoid persistent start/resume/instruction
   helpers for utilities. Use schema-proven settings to disable built-in tools
   and workspace instructions; an empty dynamic-tool list is not by itself
   proof that built-in tools are disabled. Handle notifications racing the
   turn response, final-message/completion ordering, disconnect, and bounded
   interrupt/unsubscribe cleanup without reconnect-resuming an ephemeral thread.
6. **Capacity and recovery:** completed request-ID mappings must survive normal
   receipt retirement. The new 10,000-mapping limit needs rejection on admission,
   not receipt-cache eviction. Keep preparation state isolated from old strict
   formats and test older collection against retained pending submissions.

The coordinator should link this report from state/portal records. No design
choice was changed by this inspection.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-automatic-session-slugs/>
