# B529 creation refusal: completed CI and closed local VM

Source remains reviewed/frozen at B `529e075a`, tree `c9c32868`, with A `801099`.
Both runs used creation derivation
`/nix/store/c4p49c13v4jf9skfjjsai7xrj9yj502m-vm-test-run-dev-workspace-session-creation.drv`.
Their first failures are separate runtime observations, not interchangeable causes.

| Evidence | Completed CI | Closed local batch |
| --- | --- | --- |
| First failed action | fork explicit, alternate | plan explicit, alternate/development; prior fork passed |
| Accepted operation | POST source `/fork` returned202 | POST source `/implement-plan` returned202 |
| Attempt1 terminal failure |08:28:04.589445668Z, explicit-fork |09:19:33.383810269Z, explicit-plan |
| Original error |initialize session: another dev-session command is changing 2026-10-25-explicit |same source-busy category |
| Actual failed syscall |Ruby8634 FD7, source explicit.lock, EX plus NB, EAGAIN,08:28:04.526363Z |Ruby12106 FD10, same source-relative path, EX plus NB, EAGAIN,09:19:33.335000Z |
| Later path snapshot |0:48 inode85; portal1805 READ, about12.022ms later |0:53 inode85; portal1820 READ, about5.180ms later |

These are real source-runtime lock refusals after acceptance. They are not
naming failure or browser timeout. Earlier automatic naming succeeded467ms in
CI and1077ms locally. Later naming-progress/fresh-retry VM scenarios were not
reached. CI terminal assertion is raw4780/command4793; local assertion2516/
command2529, propagated at3113. Both assertions preserved the first failure.

The syscall PID/FD/path/mode/result/timing are recorded. Refused-FD device/inode,
same lifetime as the later path and original holder remain unproved. Later
portal READ evidence identifies a shared owner at that snapshot only; it does
not identify the logical request/goroutine or acquisition/release interval.
Browser correlation/phase is temporal context, not a captured call stack.

CI observer54 events/local64: dropped0, collectorErrors0, but attached=false and
unresolved25502/46217. Raw trace was deliberately not retained; complete attachment
or history cannot be claimed. Browser128 retained with90/124 dropped, diagnostic
errors0. Earlier53/63 Go EX contention events belonged to an automatic creation
that later succeeded; they are not utility calls. No actual bundle-truncation
marker was emitted: those text matches were echoed code. Both first observer
stops succeeded and the unit deactivated; later stop-unavailable is a secondary
repeat-stop diagnostic, not the first failure.

Seven relevant source files are byte-identical to deployed10bb and reviewed529.
Ruby fork has two source EX guards; the CI event cannot select one. Plan uses
expected-source validation before destination initialization. Existing
`TestAcceptedForkSourceSharedLockRefusalAndReceiptRecovery` covers both real Ruby
fork guards, exact receipt retention, explicit retry after controlled release,
no native side effects and source replacement refusal. Go snapshot mutex release
before Ruby is not a source-runtime ownership handoff. Existing portal SH callers
include observations, mutations, provider restoration and retry reconciliation;
none is selected as the actual holder by this evidence.

**Smallest next step:** retain the first VM assertions and defer a sequencing
patch until a real source-wide admission/settlement seam is demonstrated.
Architect0's static consultation found an independent possible SH reader:
RecoverSessions scans ready sources every second and retry reconciliation takes
SH (`main.go:389`, `turn_retry.go:148–159,255–259`). This is a possible caller,
not attribution of either failure. Browser drain/close, readiness, native
completion and HTTP202 cannot prove source-wide exclusion. I know no existing
barrier that supplies it. A bounded component plan refusal/same-receipt recovery
coverage extension is an option for main, not a native VM fix or acceptance.
No production lock/naming/policy change is justified; do not add sleep, automatic
retry, timeout increases or a product hook. Main decides any further design or
instrumentation boundary before edits/execution. No rerun is proposed.

Originals and hashes are preserved in `package-b-creation-529-*-original-manifest.json`
and `package-b-creation-529-evidence-manifest.json`. CI raw909204 bytes, SHA256
`3331d0d7c4277c4cfb50e4afe50d0fc8d8627e421699ab6730d5b0029ad3be97`;
artifact inventory0. Local raw610025 bytes, SHA256
`2fdbebacf05cfbb2489179f0ca7bcc2c93593dc54c7ebef409fbd88eb4e08e1a`;
closed result/wrapper are copied too. Detailed CI-only analysis is preserved in
`package-b-creation-529-ci-diagnosis.md`; tiered sanitized values for both runs
are in `package-b-creation-529-combined-supported-facts.json`.

Local native31.038s and Chromium/Firefox32.964s passed separately, creation VM
failed2346.833s, wrapper exited1 after2437s. CI fast/archive succeeded separately.
Neither set certifies creation/full acceptance or explains old B37 holders.
Old B37 local plan and CI post-naming candidate-reservation failures remain
separate historical evidence. I read the local artifacts only after main
confirmed closure. No source/ref/pin edits or tests/builds/native/browser/live/
CI actions occurred; remaining-check driver is unexecuted/unreleased. User
DEPLOYMENT HOLD, C freeze and B follow-up ownership remain.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/)
