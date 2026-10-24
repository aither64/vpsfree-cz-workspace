# Native run2: sticky loaded error status and missing observation evidence

Run2 B at `3f2153a44e87bcd60c40ac5dcc660f214ccf04fa` failed/incomplete, exit1,
95seconds wall time. `TestNativeLiveSwitchReconnect` passed2.95s. The retry
fixture failed90.21s at line165 waiting for literal loaded idle status. No new
retry-controller scenario passed. All processes ended under watcher ownership.
No native rerun has been launched by B; no timeout was extended.

Original files remain unchanged in
[run-2-3f2153a4](native-verification/run-2-3f2153a4/). Runtime JSONL SHA256
`e51da01b1e78576ec0aba50821d9ce188f16f1798c3d2cb6a3f7a0f85613ac39`;
empty stderr SHA256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
exit SHA256 `4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865`;
elapsed SHA256 `d867d3f88fa20d7cb936ecd93651adeedf473a6177218cd0987f462ff5511cb6`.

## What run2 proves and omits

The fixture passed terminal failure observation and managed proof scheduling
before entering the new loaded-idle wait. The original client was retained.
Its final failure prints the native log warning about PATH helper aliases and
the context timeout, but does not print the last ReadTurnState return or error.
It therefore does not empirically identify systemError versus cold/status/error
as the failed predicate. No automatic dispatch/receipt uncertainty was reached;
none may be claimed as tested. Run1's insufficient diagnostics also remain
preserved rather than reinterpreted as proof of cold unload.

## Pinned-source incompatibility candidate (escalated before changes)

Exact rust-v0.163.0 source was downloaded read-only into owned tracking:

- `native-bespoke-events-01630.rs:1034–1037` handles EventMsg::Error by calling
  ThreadWatchManager.note_system_error before checking whether it affects status.
- `native-thread-status-01630.rs:174–180` sets has_system_error=true and clears
  running/pending request flags.
- The same source147–152 clears has_system_error only when a new turn starts.
- TurnComplete calls note_turn_completed156–158; clear_active_state184–191
  clears running and pending flags but preserves has_system_error.
- loaded_thread_status447–468 returns notLoaded for unloaded, active for running
  or pending requests, then systemError for a loaded error flag, otherwise idle.
- Its exact upstream test619–640 is named
  `system_error_sets_idle_flag_until_next_turn` and expects SystemError until
  the next turn starts.

Thus a loaded quiescent terminal failure can remain systemError indefinitely.
B's Check and A's continuationIdle both require literal idle, as does the
fixture wait. A subscription or warm resume does not clear the sticky flag:
ThreadWatchState.upsert_thread314–331 sets is_loaded only. Sending a dummy turn,
rewriting status or resuming to hide this mismatch would violate the accepted
retry proof contract. No such workaround or product/status edit was made.

Lead accepted this as a material source-backed contract candidate and assigned
architect0 the exact predicate/API design. Product changes remain on hold until
the saved accepted brief and explicit release. Required negative coverage should
retain notLoaded, active/waiting request, wrong/newer turn, nonfailed terminal,
unknown status, native queue/prompt/ledger uncertainty, mismatched binding and
managed admission holds. A loaded systemError alone must never become general
execution permission; exact expected eligible failed-turn identity and all
other fences would still be required if the architect accepts that distinction.

## PATH warning applicability

`native-arg0-01630.rs:313–323` refuses alias creation when CODEX_HOME is under
std::env::temp_dir (here /tmp). Its caller159–163 explicitly prints the warning
and continues with package PATH. Both existing native reconnect/recovery
fixtures also warn yet pass. The B retry fixture reaches native provider failure
and provenance scheduling before the wait and has not requested a tool before
this failure. There is no source or run evidence that helper alias refusal
prevents status clearing or caused this timeout. Do not move onto real user
state or alter native security checks to suppress it.

## Narrow diagnostics prepared, uncommitted

The native fixture now bounds and logs changed ReadTurnState observations
(thread/status/latest turn/status/failure/error), retains its latest polling
result on timeout, logs controller Step/phase/reason/load failures, and caps
the native log tail. A passive setup snapshot records loaded IDs, metadata
error and the private rollout's existence/size. No prompt is exported and no
activation/status-reset is added. Tagged compile-only is the permitted check;
no native rerun/publication or product edit occurs before lead release.
