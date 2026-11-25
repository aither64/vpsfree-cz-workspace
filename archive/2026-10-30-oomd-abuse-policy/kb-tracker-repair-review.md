# Final independent KB runtime-correction review

Report from reviewer0, preserved by lead. Scoped to frozen dc608aa8; it does
not certify owner3's later K1 remediation.

## Findings

Blocking: none.

Important K1 — drain completion checks/publication bypass the first-error latch.
Commit dc608aa8a4ed4dbf67ee5551a5a6d0796cef569d.
cluster/lib/devcluster_runner.rb:316-319,330-333,350-354; compare observe/fail_tracking at :149-174.
General/risk lanes.

Each drain block calls observe, but its subsequent lifetime_gone? calls and final
write_processes.call(proved) are outside observe's rescue. lifetime_sample
intentionally raises for denied/malformed/mixed observations; final state
publication can also raise. A failure after successful discovery therefore
unwinds the shutdown ensure and terminates the owning runner/control path instead
of latching the error and retaining a live incomplete drain. This can recreate
the dead incomplete ownership state the repair is intended to prevent.

Smallest outcome: route these separate completion observations and final proof
publication through the existing first-error latch; preserve non-ready/incomplete
ownership and the authenticated control/reaper path. Focused barriers should
inject a completion lifetime-read failure after successful discovery and
final-complete publication failure, checking retained first error, live control
and no ownership/claim/socket release.

For a failure after safe native machine finalization/cleanup, retain those actual
completed effects in evidence; this finding does not require undoing cleanup or
claim that it never occurred.

Disposition: lead accepted K1 and assigned owner3 a narrow fix plus
negative/positive controls. No fix certification is included here; lead owns
direct step-9 verification unless the remedy materially expands the design.

Advisory: no additional finding. No other Blocking/Important issue found in the
reviewed range.

## Review identity and exact scope

Retained reviewer0, gpt-6.1-sol/xhigh/read_only, live same-session roster verified.
Bound current matched 2026-10-30-oomd-abuse-policy with both environment markers
absent and trusted developer binding matching. All four mandatory lane references
and applicable KB/runtime/workspace procedures read. No overrides, fallback,
nested reviewers, edits, tests/builds, CI/runtime actions or old-state mutations.

Repository: vpsfree-kb-contracts.
Direct repair: 7bdee285d62343c653b5a8c5cfdeab2d97ef7f4d..dc608aa8a4ed4dbf67ee5551a5a6d0796cef569d.
Complete final range: ce2c8cd9358c3636e5d39343e595df813a0b197f..dc608aa8a4ed4dbf67ee5551a5a6d0796cef569d.
Verified final tree fb6bd22aed441103b6a907c7ed481d4f6679cb2c, supplied merge-base,
exact two-commit series and all committed quick-input file hashes. Source was
committed/clean at review release; later remediation working-tree contents were
not reviewed as dc608 source.

## All-four-lane conclusions

General: inspected producer/readers, relevant error/race/compatibility tests,
documentation and native quick evidence. K1 exposes a concrete untested drain
boundary. Existing discovery, tracker and join-error tests do not exercise those
separate completion calls. Documentation is discoverable in
cluster/runtime-contract.md and correctly distinguishes control authority,
wait-only obligations, polling limits and old-run refusal.

Architecture/repetition: ProcessReceipt provides one owning validation/access
boundary used by Engine, the live-lease inline Ruby observer and runtime verifier.
JS adds the distinct temporal requirement of stable version/control plus
monotonic lifetime/parent records; it does not reproduce native process authority
or gain signalling rights. Discovered the optional vpsfree-dev-workspace provider
and Portable consumer at canonical master (KB pin ce2c8cd9): they wrap public
status/control or call the selected engine's own ready/live/gone rules, without
parsing legacy process keys. No missing production process-proof consumer found
in the searched KB cluster/tools/lib/runner or extension KB adapter. Fixture
updates are directly supporting consumers.

Scope/proportionality: compared +937/-201 across 12 repair files with the user's
“find the root cause and fix it.” Most growth is focused tests; the implementation
separates the two existing authority roles and supervises the existing
tracker/drain. The demonstrated helper credential transition justifies wait-only
descendant observation. There is no root launch, permission broadening, helper
whitelist/proxy, OSVM fork, new transport/framework or exceptional recovery
mechanism. No unsupported subsystem needs removal.

Risk/compatibility: strict full runner tuple and socket peer checks remain
control authority. Descendants retain stable boot/PID/start and first-proved
ancestry, with anchored/acyclic/unique validation; observations of all tasks and
retained reparented lifetimes remain exit obligations. Reused PIDs are not
traversed as old lifetimes, and lifetime records are not admitted to
matches?/runner_matches? or signal paths. Denied/malformed observation refuses
rather than becoming an empty tree. K1 must close the remaining graceful-failure
gap.

Schema2 deliberately omits runner/children aliases. The exact old-source method
fixture refuses schema2 ready/control/gone/handoff before socket action. New
readers dispatch legacy schema1 through its strict full-identity/incomplete-exit
rules; no old receipt conversion is introduced. Complete new runs must stop under
their owning source before controller rollback. The procfs polling limit is
honestly documented: descendants that fork and escape before observation cannot
be reconstructed. No stronger containment guarantee follows.

## History, generated streams and migration lineage

Complete series, exactly:

1. 7bdee285d62343c653b5a8c5cfdeab2d97ef7f4d — consolidated five-file application pin.
2. dc608aa8a4ed4dbf67ee5551a5a6d0796cef569d — coherent runtime producer/readers/tests/documentation correction.

Full diff: 17 files, +945/-209. The prior mechanical pin assessment is reused for
unaffected content; all five pin files/lock are byte-identical to 7bdee. App remains
f60d41a453b1703e42de4341285bdc6ba339aff0 and OS remains
6bdf458fd9105379860234ff33d352e55844f08f.

No obsolete repair iterations, fixups, redundant dependency/pin/generated streams
or transitional conversion steps remain in this complete series. One final pin
stream remains. Keeping the pin and runtime repair separately is coherent, and
7bdee also identifies the actually consumed immutable historical runtime. Retained
original refs/evidence remain outside the final series.

No database migrations. Process receipt schema2 is an intentional persisted-format
change, not a migration/conversion of existing receipts. Legacy schema1 reading is
required by retained real state, not an obsolete draft shim. State/launch/artifact
schemas and pins are unchanged. The normal-commit receipt records pinned-shell
exit0, no declared hook framework/core.hooksPath and no bypass.

## Evidence and limits

Inspected scoped native results: process/lifetime/receipt 12 runs/76 assertions
PASS including installed-helper exe-EACCES and same-UID exec; corrected join 1/20
PASS; lease 11 cases PASS; verifier 2/38 PASS; concurrent-ready/unexpected tracker
exit 2/33 PASS; discovery 6/65 and runner 6/347 PASS; engine 7/102 PASS; exact old
reader/handoff 1/5 PASS. Final committed hashes bind the source; later test-only
additions have separate results.

Initial shape failures and the first runner batch's join timeout remain failures.
The corrected fixture uses Kernel.raise rather than Thread#raise; its later pass
does not relabel that aggregate green. No complete dc608 suite or real
guest/capture has run. The earlier 7bdee pin-only full-check exception cannot
certify these substantive runtime changes.

The actual installed-helper diagnostic establishes that legitimate
privilege/capability transitions can deny exe while stat/task lifetime
observations stay readable. It does not identify historical PID2989738,
demonstrate a successful network bridge start, or complete the old run.

Old instance f66a2056-c6e7-4300-904a-c7d2758addae/run
ea841826-207a-4419-8e21-ea61bf3ea678 remains governed by its immutable old source.
Four QEMU exit0 and absence of 29 recorded PIDs do not repair complete=false or
authorize claim/socket release. No supported reconciliation for that dead
incomplete run was established by this review. Its claims, evidence and effects
stay separate.

## Verdict

All four lanes and full original-range history review are complete. No Blocking
finding; accepted Important K1 remains in frozen dc608. No additional required
source fix identified. Source clearance remains held until K1's narrow outcome
is directly verified and recorded by the lead. Unaffected review need not be
repeated solely to confirm that fix.

After corrected-source clearance, complete affected suites, fresh dedicated
capacity/resource admission, normal bridge start and immutable guest/source
attestation, four CS/EN list captures, strict output validation, ordinary public
stop/exit/resource proof, visual/media review and exact-final strict hosted Check
remain required. This report certifies no current runtime/capture, old-run release,
deployment, merge, production KB write or session lifecycle action.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/
