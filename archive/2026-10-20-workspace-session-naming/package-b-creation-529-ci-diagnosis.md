# Completed B529 creation CI diagnosis

Exact reviewed/frozen B is `529e075ad07e2d967a8af4902584e37527115454`, tree
`c9c3286858934ba63ff11c9e37879e7803a8351f`, with A801099. Check40175804431
creation job121116105384 failed; fast121116105468 and archive121116105467
succeeded separately, host skipped. Main's completion snapshot is copied without
modification. Independent source review remains accepted with no findings in
`forward-review-20261025/review.md`; execution acceptance is incomplete.

## Preserved original evidence

Fetched the completed job log and run artifact inventory once through read-only
GitHub APIs. Full raw log: `package-b-creation-529-ci-job-121116105384.raw.log`,
909204 bytes /5322 lines, SHA256
`3331d0d7c4277c4cfb50e4afe50d0fc8d8627e421699ab6730d5b0029ad3be97`.
Fetch stderr files are empty; artifact inventory has total_count0. The original
manifest includes hashes of raw evidence and copied CI/source contexts. Raw log
mode is0600. Compact sanitized records are in
`package-b-creation-529-{supported-facts,compact-diagnostics}.json`; full parsed
sanitized observer/browser bundles are retained separately. Parser excludes
quoted diagnostic source and duplicated Nix last-log tails. In particular,
`bundle-truncated` appears in echoed code, not actual emitted evidence.

CI checks out exact529 (raw107/119) and builds creation VM derivation
`/nix/store/c4p49c13v4jf9skfjjsai7xrj9yj502m-vm-test-run-dev-workspace-session-creation.drv`.
Static inspection uses immutable source
`/nix/store/knj9f5a2aclczqgpvgxd14sviglabaxp-source`, independently bound by main's
592-file/mode/NAR receipt. Seven relevant lock/creation/reader source files are
byte-identical to selected10bb and reviewed529. That is source preservation,
not a claim of VM success or reuse of another execution's full input graph.

## Authoritative first failure

The first failed browser command is `fork explicit` with provider `alternate`,
inside "alternate provider, fork and approved-plan destinations preserve source".
The alternate creation/proof completed before the fork command. The plan command
and later native naming-progress/fresh-retry scenarios were never reached.

The browser sends POST `/api/sessions/2026-10-25-explicit/fork` and receives202.
Destination `2026-10-25-explicit-fork`, receipt
`7ce71bc0b270dd3dc1f33fbd29a8161b2ea1c0a62ebb88e1c15ace9ca6ebbcb8`, attempt1,
starts08:27:58.876932207Z. Its first terminal status is failed at
08:28:04.589445668Z, error:

> initialize session: error: another dev-session command is changing 2026-10-25-explicit

Raw4780 contains the terminal status. The unchanged browser `terminal()` assertion
fails at helper111, through `usable()`152 and fork path327; command exits1 at4793.
This is an initialization source-lock refusal after acceptance, not a naming
failure or browser timeout. Earlier automatic naming succeeded in467ms (4541).
The browser's128 retained events/90 dropped records show the accepted POST and
status polling, with diagnosticErrors0 and pageerrors empty. Older running
checkpoint output does not override the actual failed status in the assertion.

## Evidence tiers

The emitted observer bundle at4816 records54 events, dropped0, collectorErrors0.
The matching event shares browser correlation
`790df7b6-0d04-4a6d-aeaf-02612669b274` and active fork context:

- Actual syscall: Ruby TID/PID8634, FD7, authority-relative path
  `2026-10-25-explicit.lock`, runtime kind, `LOCK_EX|LOCK_NB`, result-1/EAGAIN.
  Entry08:28:04.526363Z, strace duration2.009ms, estimated return08:28:04.528372Z.
- Descriptor identity: explicitly unavailable. No witness proves refused FD7's
  device/inode or its same lifetime as the later path. Invocation class is
  unknown; active context/path/time support the initializer association, not
  an independently captured command or call stack.
- Later observation: path identity major0/minor48/inode85; matching kernel FLOCK
  READ owner PID1805, executable class portal, known fixture-service TGID1805.
  Snapshot starts2.478ms after observer arrival; its completion is about12.022ms
  after estimated refusal by wall-clock correlation. It proves a later shared
  owner on the observed path identity, not the holder at refusal or a logical
  portal request/goroutine/acquisition/release interval.

The bundle says attached=false despite parsed syscall events and reports25502
unresolved trace records. Raw trace was intentionally not retained. The exact
announcement/format/signal cause is unknown; do not infer complete attachment,
complete syscall history or absence of other holders. Fifty-three earlier Go
EX refusals on accepted-session occurred during an automatic creation that later
succeeded. They are lock events, not utility calls or evidence of a naming retry
limit breach. A later observer-stop-unavailable marker is secondary: first stop
succeeded and the unit deactivated, then finally attempted stopping the unloaded
transient unit again. It did not cause the first browser failure.

## Source-backed interpretation and limits

Ruby fork has two source EX guards: `verify_creation_source!` before destination
binding (`libexec/dev-session:1446,4044`), and later `with_slug_lock(source_slug)`
while reading the source manifest (`:1499`). Both use the same EX|NB fail-fast
source lock (`:8098–8125,8267–8285`). This evidence cannot select which guard
failed. The Go snapshot mutex is released before launching Ruby
(`creation.go:1005–1008`); the transition FD is the only extra file passed to the
child (`server.go:1609–1625`). No leaked source-FD handoff is proved.

Several existing portal paths can legitimately own SH, including source
observation (`creation.go:252–262`), mutation admission (`server.go:2055,3686`),
provider subscription restoration (`provider_watches.go:100–112`) and retry
reconciliation (`turn_retry.go:255`). Their existence does not identify the
observed owner. `creation_source_lock_test.go:24–110` already covers both real
Ruby source guards: first refusal retains the exact receipt and no native side
effects, explicit retry after controlled release succeeds, source replacement
still refuses. These controlled tests do not identify this CI holder.

Old B37 local failed the plan source guard; B37 CI failed Go candidate reservation
after successful naming681ms. This run failed earlier in fork source validation.
It supplies new syscall/later-owner evidence but does not retrospectively prove
any shared actor, holder or cause across the three failures.

## Smallest justified next step

No production lock/naming/policy or timeout correction is established. Preserve
fail-fast EX ownership, first failure, exact receipt/source identity and saved
settings; do not add automatic fixture retry or accept a green rerun as diagnosis.

Request a bounded architect source-contract consultation through main: determine
whether the VM's first-attempt-ready fork expectation is justified while ordinary
portal SH activity can overlap, and what deterministic fixture readiness or
explicit saved-receipt recovery acceptance would satisfy the existing contract.
Use the existing two-guard controlled tests and this positive later-portal-SH
witness; do not silently add a sleep, retry heuristic, queue or product hook.
The owning portal operation and acquisition/release interval remain the concrete
evidence gap. If resolving it needs product instrumentation or a broader observer,
main must approve that minimum boundary before edits. The attached/unresolved
telemetry can be clarified separately if main requests a diagnostic follow-up;
it is not a production fix.

Main's already active local VM remains with its original utility. I did not read
or poll `/root/oct25_source_verification` or its result/log/handle and launched
no check. Main may assess that utility's completed receipt when naturally
delivered; no duplicate run is proposed. No source/ref/pin edits, tests/builds,
native/browser/live calls, CI waits/reruns/triggers/cancels, C update, claim,
deploy, merge or lifecycle action occurred. User deployment HOLD and C freeze
remain. Implementer1 retains B follow-up ownership after main accepts a proposal.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/)
