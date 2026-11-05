# Archive failure: lifecycle-side evidence

Run `41518664500` is settled at exact runtime
`3d76f527a6b88e9d32c202f729a1a0d673b341f2`. Creation succeeded; fast failed on the
separately diagnosed cache transfer. Archive reached its VM and failed in the
existing `2026-10-17-recovery` browser-revive call. B owns the bounded UI proof/fix;
A's support is read-only. No Ruby, receipt, capability or ownership changes were
made, and no VM/CI rerun was requested by A.

## Observed trace and assertions

- The deliberately induced permission denial occurs during archive tracking move.
  Retained journal identity and recovery data are checked before retry.
- The retry reaches `archive: archived` (job-archive.log 5728–5734). The VM's
  `archived()` check passes at 5585–5588: same receipt
  `61fa286918186892130ec761885e103bcc92f6b7d76e4bbf1af0a52ededf725d`, state
  `complete`, and `currentTarget.archived is True`. Archive location, branch and
  unchanged recovery hashes pass next. This is assertion evidence; raw response
  bodies were not printed.
- The next browser call fails before a revive POST: diagnostic line 5606 records
  phase `submit revive`, no page errors and only GET responses. The submit locator
  at 5607–5628 initially resolves, sees a same-page navigation, then remains hidden
  until its 30-second deadline. The final DOM has visible revive-open and no open
  dialog. [The captured diagnostic JSON](archive-browser-failure.json) preserves
  the complete requests, operation timings and DOM snapshot.
- `test/archive_lifecycle_browser.cjs` is byte-unchanged from c218. It waits for
  initial operation response headers, opens the dialog, then tries to submit.
  It does not establish that all operation/detail callbacks have settled.

This subtest creates no registered service. New registered-service native cases
are the following subtest and were not reached. No native registered-service
success is claimed.

## Source-established fields and limits

The successful retry necessarily retains `options.journalExpected=true`:
`prepareLifecycleRetry` with the retained journal applies progress options;
`operation_state.go:329` sets that flag true. Retry start preserves those options
(`server.go:3122`), successful completion copies `completed := started` and changes
state/phase/times (`server.go:3238`), and `lifecycleOperationView` preserves Options.
There is no product assignment resetting the flag false. The captured trace does
not print the exact subsequent GET body, so this is a source-backed invariant,
not a claimed direct body capture.

The real pending lifecycle is empty after completed archive recovery. Independently,
the captured visible revive-open button requires archived state and empty pending
lifecycle under the shipped template. Actual details JSON and the local body's
`data-pending-lifecycle` value at callback time were not captured.

B identifies an unchanged predecessor UI chain: `showLifecycle` interprets the
historical complete receipt's journal flag as current pending archive; the next
details reconciliation reloads the archived page, discarding the revive dialog.
The source invariants and captured navigation/no-POST trace support this chain.
The supported classification is a pre-existing UI history/timing problem, with no
demonstrated core recovery failure. B reports that an actual shipped-handler
regression reproduced the unwanted reload with a completed journal-bearing
archive receipt and a fresh revive dialog; the real pending-archive completion
control passed. After its one state guard in `showLifecycle`, both controls pass,
history/options stay intact and explicit revive submission reaches the mocked
client. This is B's reported deterministic proof, not a new A test run or a
claim that the missing raw CI response was captured. B reports full package
selection passed: 129 Node tests, 10 syntax checks and focused Go asset/navigation/
lifecycle checks. Its local-only consolidated correction is `7302f4dc`, tree
`934f92ba`, clean and returned to the lead for the same reviewer's general/risk
follow-up. See [B's complete receipt](../revive-ui-remediation.md). Publication,
pins and deployment artifacts remain held.

B owns the UI-only fix and bounded whitelisted diagnostics added to the existing
native browser helper, under the lead's grant. No Go, Ruby or receipt changes and
no VM rerun are part of that reported correction.

If direct empirical fields are needed, the precise missing diagnostics are
operation kind/state/receiptId/options.journalExpected/currentTarget.archived,
details archived/pendingLifecycle, local body pending flag and navigation order.
B may instrument the existing helper under its grant. Do not weaken recovery or
replace this with arbitrary delays or a blind full rerun.

## Evidence binding

Verified against the retained checksum inventory:

- `job-archive.log`: `aa8fbaafa677fcd14d2e0f353f1ec2b71dd4128c96977bfea4e92470969f927f`.
- `all-jobs.log`: `f9d98464e5df42d948a776e985cf4e94bb14a97257fc844d8154458d836dfa56`.
- `final.json`: `77502a7ab92374582db26bb3c0a46bb10e6000b1bb394ff290dffaae79c5df08`.
- Successful creation log: `926ee15bd96f270f784286b036e1710410829c54c5543b923895c0f38d0ec235`.

System artifact preparation finished independently and is held. Its exact generation
`2026-11-02--21-41-36` and store/input receipts are in
[configuration-pin.md](../configuration-pin.md). All commands are settled; no copy,
claim, activation or source/Git/pin mutation is in progress under A.
