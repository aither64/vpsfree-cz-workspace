# R22: frozen S3 operational artifact

Lead-retained summary of reviewer0's final same-session report, 2026-11-14.
The full report is preserved in the inbound team report. The reviewer performed
no edits, checks, builds, live requests or peer-state access.

## Disposition

All four assigned lanes completed: General, Architecture/repetition,
Scope/proportionality, Risk/compatibility. Overall risk High. No Blocking or
Important finding; one Advisory below. This is final assessment of the complete
frozen private operational artifact, not early advisory review, product branch
readiness, peer adoption, live execution, deployment or integration permission.

Retained reviewer0 matched current session and live roster: review purpose,
ready, read_only, gpt-6.1-sol/xhigh, thread
01a1cbe8-2ad5-7ee0-8c9e-1ab799e21fbd. Both identity environment variables were
absent and trusted binding/current matched. No override, fallback or delegation.
Current mandatory-review, all four references, applicable guidance, copied
codex-web instructions, A42/seams/applicability, source, fixtures, logs, receipt
and USAGE were inspected.

## Exact reviewed object and lineage

Private directory: `/tmp/session-archival-utility-638bef05/S3`.
Reviewed receipt SHA256:
`8d6f94ba0dcdeb5fc5a45ff59821a8f5ebb7f8c14a2aec43edd6076de8c4bac5`.
All 25 listed file hashes, sizes and modes independently matched.

Public committed base: codex-web
`dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`, tree
`c294e99dfc86ac44ded7804fae686a98af2971ae`.
All 146 copied public files were compared to that Git object. Only client.go
differs; removing the exact three-line scoped-read hook restores public bytes.
readLoop, requestConnectedAdmission and writeOfferAdmission remain unchanged.
The new SDK entry has 192 lines and fixed caller 255: 447 lines/18,226 bytes,
plus the three-line hook; focused tests have 371 lines.

- SDK patch: `a2f3ae02c2bd3b0506ac5ab1e090492da9579fa5deada7017b0ca6ed5d58b321`.
- SDK source: `c0c285981aed019e890234949092ddd8200cf9e6d0a58cb9cd2b5a3ed05e0c61`.
- Reviewed caller: `6163a1704801ccfb30da7c94785dc8c8b80de1f252e8e79a4f4ae4a1e4a6b91c`.
- Reviewed binary: `56abc3b0c87b50bef21b4bf98e868629d2fc62cd29318626e949ef979a8d2868`.
- USAGE: `80a63b105e8e99cde6c49371ae4316e5114ce746d956a9790fc7976d612724d6`.

No claim that this derivative is product-committed, merged, released, installed,
adopted or executed. There is no new Git/pin/dependency update stream, database
schema or migration. Existing SQLite formats/import paths/helpers remain.
Earlier M2 allowances and mistakes are historical separate artifacts, absent
from S3 production behavior. R20/R21 production source/artifact boundaries remain
unchanged; no full feature re-review was needed.

## Advisory and lead disposition

General/Risk: caller/main.go:232 initializes Delivery unknown while the
MayBeSubmitting flag is false. A payload/socket/ledger/metadata failure before
state inspection cannot exclude a prior submitting invocation. Existing unknown
Delivery/Notice/USAGE preserve uncertainty and no ledger clearing/resend occurs,
so this is output clarity rather than unsafe dispatch.

Lead selected the smallest remedy: initialize MayBeSubmitting true until an exact
accepted or known-unsent result. Assigned to source owner implementer2 in
c6c7e5d3-6ac1-4b16-bb1f-dea1e90046a6. Preserve the reviewed source/receipt,
compile the caller and reuse the existing focused caller cases. No new SDK
suite, framework, state probe or reviewer rerun is required. Root will inspect
the exact narrow diff/results and final hashes under mandatory-review step9;
the actual remediation and root acceptance are recorded below.

## Source and safety conclusions

The sole consumer is the fixed owner caller for monitor638bef05 and the specified
original utility/active turn. It accepts only an output path, validates immutable
drain text/hash, reserves private output and checks root/utility/project/cwd and
socket/real existing canonical0600 ledger identities. Fresh owner permission,
trusted session binding, exact-lead monitor status/incarnation, full native/socket
epoch and actual portal-open ledger are external owner prerequisites, not locks
or permission inferred from shared metadata.

ObserverOnly/no alternate HistoryReader/shared SQLite and exact identities are
required. Private typed scope binds client/generation/utility, closes cold reads
before Ensure, forces includeTurns:false and preserves default generic behavior.
Expected generation is captured once, never replaced after reconnect. Existing
queue lock and SQLite exact claim preserve message/options/action identity.
Accepted/submitting attempts reconcile rather than resend. New preparation
requires exact loaded active/inProgress turn twice, empty queue and known other
submission state. Only turn/steer is emitted; no resume/start/interrupt/settings/
queue mutation/provider switch/new ID or fallback. Expected active turn is
checked atomically by native admission.

Restoration needs a real claim plus existing unwritten/typed refusal evidence and
atomic state reread. Ambiguous delivery remains unknown; scoped bounded history
checks expected turn/client before accepting. No uncertain-outcome resend was
found. Unsolicited-request no-answer and production transport/writer are unchanged.
Acceptance is pending input only; it does not prove consumption, cell7 termination,
nested poll completion, quiescence or effects resolution. The frozen drain text
preserves those limits and prohibits remote CI cancellation/rerun, arbitrary
process killing and session/utility lifecycle actions.

Scope is proportionate to the demonstrated absent exact-only route: generic SDK
send resumes and may start, while this reuses existing persistence/admission.
The extra exact-turn reconciliation prevents wrong-turn acceptance. No
speculative framework or product growth requiring another cut was found.

## Evidence and limits

Actual offline batch16.877s, caller helpers4.116s and production build4.857s passed.
New entry/scoped reads and real own-temp SQLite were exercised with a wire-only
overlay: accepted/replay, ended/wrongturn, queue/options/identity/generation,
concurrent claim, lost reply/no resend, wrong history, recovery and restoration.
The reviewer independently verified only the wire boundary was replaced.
Production SDK archive/caller were compiled without overlay; build metadata
shows Go1.26.6 and explicit private replacement. Binary/main, including -h,
were never executed. Caller helper tests use own temp files and fake stat data.

The final incoming fixture executes a copied source-exact branch in memory,
not production readLoop. No ordinary-client negative-control execution is visible
in the final S3 test/log. Root's earlier review-packet wording overstated that
point; this paragraph corrects it. Unchanged production readLoop bytes are
independently proven. No new test or transport/live probe was requested.

Documentation placement/preservation passes: USAGE is an individual operator
execution/recovery record, share texts preserve source/drain/build instructions,
decisions live in existing design/rollout/state and raw proof stays private.
No public README/reference addition is useful for this unshipped derivative;
existing product recovery/old-reader boundaries remain. Commands, protected
identifiers and unknown/no-retry warnings are preserved.

After the narrow advisory is reconciled, root may deliberately share the exact
source and review evidence. The owning peer alone decides adoption/invocation
after fresh authority/binding/native/ledger checks. Utility consumption/drain,
complete local effects accounting and ordinary native quiescence/resolution are
separate later gates. No future live result is needed to complete R22.

## Lead verification of the narrow Advisory remedy

Completed under mandatory-review step9, without another reviewer turn. The
reviewed caller and receipt were preserved at S3/history/r22-reviewed before
overwrite. Root compared the complete new caller to that exact baseline: the
only source difference initializes MayBeSubmitting true. SDK, drain, flags,
actionContext, checks and acceptance behavior are unchanged. Existing accepted
and known-unsent delivery still set the flag false.

Existing four caller helper cases and production caller compilation passed
exit0 in4.269s (Go tests0.017s), r22-caller-check.json/log, tool73549 joined0.
Root read the actual diff, command/result and log; no SDK suite or reviewer rerun.
The binary was never executed. Root verified all30 selected receipt file
hashes, sizes and modes, with zero mismatches.

Current selected artifact identities:

- Caller: `d2db786484a5cba41452ed05b4aa6fbf78d7efa0703ada56f688f544cef30caa`.
- Binary: `34602aa4103f899a9ccad92703550e18b97811935ca1e7d0315054d9f4f3a0ff`.
- Receipt: `01c18b3a37c7d8f8cac985a769263ee78f2beb2359e25e42dda81c9ba1abc3e8`.
- Full caller share: `31b6e530d307441164a087bb2dd90e2707110e88c06a8efd7a3b9340e359f5ef`.

SDK/share-SDK, USAGE and frozen drain identities remain as reviewed. Current
production size is447lines/18,249bytes plus the three-line hook; only23bytes
were added by the Advisory fix. The Advisory is reconciled. This lead acceptance
does not claim the reviewer reran on the successor or authorize peer execution.
Deliberate source sharing may proceed; peer adoption, fresh preflight, actual
steering, utility drain/effects accounting and ordinary resolution remain separate.


## R23 packet — frozen S5 fixed804 successor

Final operational-artifact assessment, General and Risk/compatibility affected lanes; retain R22 architecture/scope and unchanged SDK/transport/SQLite conclusions. Overall risk High: exact owner-bound utility steering and durable submission. Retained reviewer0 Sol/xhigh/read_only verified live same-session; no overrides/fallback/delegation.

Requested outcome: deliberate source delivery to the already-approved osctld peer for cooperative end of ONLY monitor8045c95c local observation. Peer own user approved exact local-only end (fba38f26); fixed target/payload/ledger supplied deliberately in bfe14dab, import metadata eb71fbf6. No peer files accessed, no live action by this root. Acceptance is neither consumption nor source36720/current-cell/nested-effect completion; peer owns later adoption/fresh binding/one exact-ID action/accounting. Remote CI and session lifecycle untouched.

Object: `/tmp/session-archival-utility-8045c95c/S5/receipt.json` SHAe3a37e43dfc4fa14b9cbe72e53a7787d30a2231ee8c5d3c6201530ea90d3c8bb. Caller5bb5d7bffd85cf55653cff46d2053bafb684ebf3952619d407e72c968e1ac79e; share1491eb7d0bbfddbe6b90c5f61a2dd4adeedbc2b366fdc201b0f29a70d42c07bc; USAGE24ab3a4d74c4ecccafeb6fcb9b70daf8e89a2e540ad6e80f0dd0bf525bb29e07; new binarybe6a8108b7aa9fe87691d7298aba8a023dc05cc63d3180f4470945fc3d98cf7f NEVERrun. Root inspected actual literal diff/USAGE/drain; no prose change needed. Full peer inputs stored OUR own owner-inputs.json, inputSHA15ef9860755d5b8ab4c8aa64781c496871400e12128ebf19394da51e12ebad5b. Payload2809UTF8B/finalLF SHA1c0649cbbf2ee71afabf392a9355a4a61bffe2c54a30d1ea2ec1a0fe7b543b6a.

Entire change versus final accepted S3 callerd2db7864 is fixed target literals, payloadhash/length and conservative preparation-snapshot notice. MayBeSubmittingtrue retained. literal-proof.json + actual caller-literals.diff establish entire normalized caller byte identity. All150 private SDKcopy files equal accepted S3; actual SDKc0c28598/3lineclienthook unchanged, sdk-final.patcha2f3ae02. Public base committeddd90fb4308ba85617ee2a4267cc835aa9a4f11ce/treec294e99d; this frozen unshipped private successor is not a product repository commit/branch. Original S3 artifact/historical R22 retained; no pin/dependency update stream, DB migration/newformat or generic extension. Product734/a67/f538 R20/R21 unchanged and outside R23.

Quick check: actual caller-check.json/log6.232s exit0, four unchanged pure helpers0.017s + ONE production compile WITHOUT overlay, pinnedGo1.26.6/offline/readonly/private modreplace. Reuse R22 actual SDK entry/scoped path/real own-tempSQLite simulated-wire evidence within unchanged bodies; no SDKsuite or live transport/native acceptance claimed. No main/socket/stat/realledger/proc/provider/CI call. No long check/review wait needed.

Assess literal identity/cross-target leakage, fixed drain wording and fresh exact-owner/root/incarnation/utility/project/cwd/active-turn/real-portal-open-ledger/native-fullsocketepoch prerequisites, exact unchanged send/unknown recovery, share completeness and truthful limits. Documentation routing: individual private execution record USAGE/share -> adopting owner; rationale/limits A42/A45 and state -> this initiative; public product guides unchanged because no shipped interface changed. Preserve no blind retry/new ID/new turn and no false effects proof. Read current skill and only assigned lane references, do review directly, no tests/builds/live/peer access. Return final findings/whole-artifact no-migration disposition promptly.


### R23 final disposition accepted

Retained reviewer0 returned final affected General+Risk assessment: no findings; all15 manifest hashes/bytes/modes independently match, literal-only successor/SDK equality and no-migration/no-newstream conclusion complete. Reuse unaffected R22 lanes. Root accepts source delivery, no live authority/acceptance claim. Frozen receipt e3a37e43dfc4fa14b9cbe72e53a7787d30a2231ee8c5d3c6201530ea90d3c8bb; full deliberate caller share0ab41f23. Peer alone freshadoption/one stableID and actual source36720/cell drain/ordinary resolution.
