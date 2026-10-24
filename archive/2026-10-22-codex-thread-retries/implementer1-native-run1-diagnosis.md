# Native run 1: runtime fixture diagnosis and correction

Run1 remains **failed**. No native rerun has occurred. Its B source was
`e0fb1238bd17cc3b29cc7d59ddaa9784c89ef939`, tree
`638bcedaf954b1d6c23033082c257b90eddc452f`. The watcher completed with no orphan
fixture; runtime exit1, wall time8seconds. `TestNativeLiveSwitchReconnect`
passed2.87s; `TestNativeTurnRetryController` failed0.99s at its uncertainty
assertion. Later recovery/opt-out assertions were not reached and are not proof.

## Original evidence retained unchanged

All original files remain under [run-1-e0fb1238](native-verification/run-1-e0fb1238/).
The runtime [JSONL](native-verification/run-1-e0fb1238/runtime.jsonl) says:

```text
turn_retry_native_integration_test.go:179: native uncertainty lost exact intent <nil>
--- FAIL: TestNativeTurnRetryController (0.99s)
```

The `<nil>` is the Store.Load error, not Controller.Step's error. The test
discarded the Step error and did not print phase/reason/native state or the
actual turn/start response. stderr is empty. The native daemon log was in the
test's temporary directory and was not retained by this failing assertion.
Consequently run1 does **not** empirically establish unload/cold state, native
acceptance or actual retry dispatch. The failure happened after the native
initial failure was observed and managed proof scheduled; later cases remain
failed/missing until the next actual run.

Original SHA256s:

| File | SHA256 |
| --- | --- |
| runtime.jsonl | `80e2be2079cedec126bb4b36245b59c68ddc2545fb3e1e3594f617cf04196803` |
| runtime.stderr | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| runtime.exit | `4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865` |
| runtime.elapsed_seconds | `aa67a169b0bba217aa0aa88a65346920c84c42447c36ba5f7ea65f422c1fe5d8` |
| source-evidence.txt | `29ac33a653003c1ee16833fb7caa7b79567a192b6ac171ad78c56ec79a42f1e9` |
| native-sha256.txt | `6576825b283ad7749538e6afb51cab20b3e4e5789274b872af0787005b9b2386` |

Pinned binary `/nix/store/wz4w670930cksh1ivz13y0gn3c23cjzl-codex-package-0.163.0/bin/codex`
reports codex-cli0.163.0. Wrapper SHA256
`dd356114c45b6b78617be9da9c21ab6d284a8d3c7de1e5a39abf45be2cabed8b`;
underlying binary SHA256
`5e538cfe7c25daf382afe195c08b2ffd24415b0cdd7f5456ec0cf1d277c3d1a5`.

## Source diagnosis

The old fixture closes its sole native subscriber immediately after saving the
scheduled retry, recreates a client that makes cold reads, and expects a fresh
automatic dispatch. Pinned native automatic unload permits idle unsubscribed
threads to unload (the accepted design's thread_lifecycle.rs59–65/80–83/559–568
evidence). A client close removes its transport; ReadTurnState/metadata reads do
not resume. Product Check correctly requires loaded idle state and never repairs
cold work. The fixture's initial restart can therefore invalidate its own loaded
dispatch premise. Any such legitimate preflight hold returns an error, which
the old test incorrectly accepts as evidence of send uncertainty before failing
its next assertion. This is source-confirmed fixture composition; the missing
Step error prevents assigning that exact runtime cause to run1 empirically.

The old proxy also deleted an actual RPC error and substituted an empty result
for every armed turn/start response. That could manufacture an uncertainty
shape from a native rejection. It lacked a successful-receipt count or native
turn identity, so it could not prove genuine acceptance. No claim is made that
run1 reached this proxy path; its evidence is insufficient.

Lead accepted this diagnosis and released test-only correction. No production
cold hold, retry admission, native protocol or A API may change to make it pass.

## Corrected fixture contract

The scheduled boundary recreates controller/store from the same durable state
while retaining the original native subscriber. UUID and deadline must remain
identical. Actual client restart still occurs after native acceptance and before
the real retained portal worker, which must settle the exact native submitting
ledger without another submission even if the thread becomes cold.

The proxy records armed start identity and hides only a genuine successful
nonempty native turn receipt. Native RPC errors and missing receipts are logged
boundedly and passed through unchanged. The controller assertion requires
UnknownSendOutcomeError and prints Step error, runtime phase/reason, native
state/error and bounded barrier observations. It requires exactly one armed
start, one successful receipt with the exact thread/client ID and nonempty turn,
and withheld receipt history. The real A writer's schema3 ledger is inspected
read-only for exact submitting UUID/action/text digest, no turn and no steer;
ordinary RequireSubmissionAttemptsKnown must still reject it before recovery.

After real portal resolver/worker recovery, A's ledger must be known, the native
turn must match the intercepted actual receipt, exactly one continuation input
must have the same client ID/text digest, and provider request count must not
increase. No accepted ledger is seeded, no direct-only recovery bypass is added,
and neither retry nor the fixture resumes to repair the dispatch premise.

Fake Unix-WebSocket regression exercises successful receipt, native RPC error
and missing receipt. Normal/race checks and native-tag compile/list are allowed;
native execution remains for a fresh utility after final commits and inspection.
See final source/pin receipt in implementer1-evidence.md for exact final heads.
