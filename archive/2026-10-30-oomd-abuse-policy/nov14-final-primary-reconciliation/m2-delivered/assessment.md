# M2 delivered-artifact assessment (2026-11-14)

Disposition: **execution held**. Source-only assessment of the complete delivered
`main.go` (408 lines, 12,532 bytes), SHA256
`d3eaf20c9e65ca25bd1daf4011fcd4927a1691667b6a69a45dc1652cc2c32545`.
No compilation, tests, native/provider calls or peer-file access performed. Peer
build/test claims are not local verification. Root retains acceptance and any
later independent final assessment; this is not implementation authorization.

## Decisive dependencies

1. **Passive inbound behavior is unproved (main.go:386).** Our installed dd90
   `codex/client.go:945–1077` constructs an in-memory client, dials only the given
   Unix socket and sends `initialize` (experimental API) plus `initialized`.
   The fresh watch map is empty (`restoreWatched`, line 1836); these calls do not
   launch a server, start a turn, subscribe, or cold-resume a thread.
   `ReadTurnState` (`turn_state.go:36–95`) really uses `historyRequest`, which
   delegates to the supplied gate (`history_reader.go:84–88`). Thus each capture
   performs six guarded read RPCs, with no recursive gate or hidden resume.
   However, `ObserverOnly` defaults false. The ordinary `readLoop` at
   `client.go:1416–1430` can call `rejectUnsupported` for an incoming server
   request; `rejectUnsupported` at 1650–1688 writes an error response directly,
   outside M2's gate. No nonblocking-input policy is configured, so that separate
   auto-answer path is disabled. Simply setting `ObserverOnly:true` is not an
   applicable fix: dd90's observer allowlist at 1130–1135 refuses
   `thread/backgroundTerminals/list`. Minimum dependency: pinned native evidence
   that initialize and these read handlers never attach this connection or route
   server requests to it, or an already-supported passive policy that admits this
   method. Do not invent a transport/client change to bypass the dependency.

2. **Exact row identity/command mapping is not established (main.go:24,
   211–234).** `callID` is the outer `functions.exec` call
   `call_78784388a337495bb0a86a631d6184ab`, not a proven public background-terminal
   `itemId`. Retained own accounting distinguishes outer `call_…` IDs from native
   command `exec-…` IDs; 99295 has no retained terminal native item ID. The pinned
   transcript decoder copies native item `id` directly (`client.go:4495–4517`);
   it supplies no outer-to-native substitution. The background-list handler/schema
   is not in the inspected packaged Go contracts, so its exact mapping remains a
   dependency, not a claim that the endpoint is absent. Require pinned producer
   proof of `itemId`, `processId`, command serialization and thread/turn scope.
   The literal correctly includes `--repo vpsfreecz/vpsadmin`, but byte equality
   is useful only if the handler returns the original shell body rather than
   shell-wrapped argv or another documented display form. Do not loosen this to
   substring matching, strip arbitrary shell wrappers or equate PID/handle alone
   with ownership. If native `itemId` differs, the current code refuses
   `identity-conflict` when 99295 is present: safe refusal, not a useful positive
   lookup. Minimum correction, if proven necessary, is the exact source-backed
   expected ID/command representation, or explicitly classify a handle-only
   candidate as unresolved; never manufacture the missing mapping.

## Remaining bounded checks

- **Guards/types:** `ThreadMetadata.Source` is `any`, ProjectID is `*string`,
  ForkedFromID is string in installed `client.go:524–537`. Utility must have exact
  ID/cwd/project, source string `vscode`, no fork parent, and latest turn equal to
  the original, terminal and loaded (main.go:77–113). Non-string source refuses.
  Root metadata captures only ID/cwd: Root.Source/Project/ForkParent remain empty,
  and the guard does not assert them. This is an exact-root metadata cross-check,
  not a fresh monitor-incarnation/ownership proof; lead's public preflight supplies
  that binding. Root may be active; equality of the before/after reduced snapshot
  can safely refuse if the parent changes turn/status during the read. No rule
  requiring idle root should be inferred or added.
- **Bounds/stability:** three literal read methods and owner/utility thread IDs;
  background listing is utility-only. Four pages, 32 rows/page, 128 rows total;
  missing/null/wrong-shaped data/cursor, duplicate item/process IDs and
  nonadvancing cursors refuse. Before/after identity/latest-turn snapshots and
  socket `lstat` device/inode checks fail closed on observed change. This is not
  an atomic terminal inventory or retained-generation proof: list changes during
  pagination or a same-socket reconnect can escape those comparisons. Since no
  outcome proves effects, retain that limit rather than add a snapshot framework.
  The 30-second context bounds requests, not guaranteed whole-process wall time
  through local file writes/close. No retry loop beyond bounded cursor traversal.
- **Output:** main.go:372 uses new exclusive mode-0600 output, and line394 checks
  encoding/close errors. Existing final-path files/symlinks refuse; invocation
  must supply a canonical new output beneath our existing private parent. Argument
  errors can still create that diagnostic file before network calls. No raw
  unrelated rows, prompts or server error strings are emitted; candidate command
  and cwd are capped at 512 bytes. Socket/guard failures override any partial match;
  consumers must read Outcome/Complete, not merely presence of Match. No fsync or
  atomic receipt guarantee is claimed. Default output path should not be used by
  an invocation packet lacking the private cwd/path binding.
- **Semantics:** `EffectsProof` remains false (zero value); Notice correctly says
  every outcome is read evidence only. Exit 0 means matching listed tuple, not
  terminal receipt/completion, and exit2 can mean not-listed or refusal. A complete
  negative listing cannot settle whether 99295 exited, was evicted or was never
  exposed by this interface; a positive only locates its tracked tuple after the
  mapping dependency above is satisfied. No outcome grants another native action,
  resolves a8, rewrites terminal INCOMPLETE, or changes remote CI evidence.

## Minimum next dependency

Lead has received peer transport/build contract 2140bce2 (Go1.26.6, module dd90,
`h1:w7r/pzWLCevSAArjYC6bHOHJ/w6CLTeAbfa66BAESeY=`); it remains supplied evidence,
not an executed build or permission. Obtain only the two missing native contract
proofs above and bind any eventual build/invocation to our own immutable source,
installed dependencies, registered socket and private output. A one-shot public
library diagnostic can be proportionate given the absent existing endpoint;
its value is locating a live tracked tuple, **not** manufacturing the absent
terminal receipt. No broader client/framework, method expansion or automatic
follow-up is justified. a8 remains held; 3b remains resolved. Stop here.
