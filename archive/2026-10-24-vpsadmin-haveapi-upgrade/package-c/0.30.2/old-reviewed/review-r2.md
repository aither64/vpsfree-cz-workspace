# R2: contradictory HTTP/API success receipt

Review severity: Important; narrow correction assigned by lead on 2026-10-24.
Reviewed old head: `39f8fd7d2bee0c4754f0f9921d97855da7fbdddf`.
Base: `5a2d2bdc3ad7a827038f877d75959916528db844`.

## Diagnosis and minimal correction

The installed library throws an `AsyncError` carrying its validated response
for non-2xx HTTP status even if envelope.status is true. The package adapter
already retains the actual response/envelope/meta as cause, and resultFor
rejects the call while preserving both contradictory signals. OAuth renewal
already requires envelope.status === false; there is no automatic renewal or
replay for these receipts.

The owning defect is `isAmbiguousMutationError`: HTTP 401/403/422 returned false
before considering that the envelope asserts success. Shared durable mutation
settlement consumes this classifier and therefore removed pending protection.
The bounded fix adds one early success-envelope ambiguity check at that shared
seam. ResultFor keeps its original receipt; no new error type, decoder or
transport is introduced, and valid status:false4xx rejection behavior remains.

## Regression scope

Actual installed client/controlled XHR tests cover contradictory 401/403/422:
actual HTTP status, raw success envelope, original AsyncError response/meta,
ambiguous classification, no BFF renewal and one dispatch. New coherent shared
mutation-guard tests use the real request path and existing hook/Web Locks
fixture. They prove retained uncertainty blocks a second submit without another
XHR and that actual status:false401/403/422 rejection releases the guard.

This is within the already reviewed mutation uncertainty boundary, not a new
design. Under mandatory-change-review step 9, lead directly verifies the narrow
remediation; no automatic full reviewer rerun. R1 still blocks all longer suites,
Nix builds/browser integration and publication. No old refs/worktrees/PR mutation.

Focused verification and final amended head pending below. The production commit
will be amended with original author intact, keeping the same dependency commit
and two-commit final history. Preserve the reviewed old range and R2 delta for
lead inspection; regenerate final packet/map/PR74 plan after amendment.

Focused tests passed: 4 files / 67 cases in 7.89 seconds. Command:
`npm test -- src/lib/api/haveapiRequestClient.test.ts src/lib/api/haveapi.call.test.ts src/components/layout/useLocalMutationLocks.haveapi.test.tsx src/components/layout/useLocalMutationLocks.test.tsx`
under the locked `nix develop` toolchain; full output `review-r2-tests.log`.
The new regression file keeps the actual-library/shared-hook boundary cohesive
without growing the existing 489-line durable-lock suite. Shared lock runtime
and storage contracts are unchanged.

Lead directly inspected the minimal runtime diff and accepted this exact
narrow approach before amendment; its direct verification will assess the
final range and logs. Original reviewed diff/series/map/packet/PR74 plan saved
as `reviewed-39f8fd7d-*` artifacts before replacing current packet outputs.

## Final correction and checks

Fresh pinned Luna/low watcher ran `review-r2-quick.sh` (exit 0, 81 seconds):
installed declaration typecheck, scoped lint, direct ESLint on all three changed
TypeScript paths, scoped format, design audit and structural audit passed.
Logs: `review-r2-quick.log`; exact status/time in adjacent `.exit`/`.elapsed`.
Hook inspection remains unchanged: no declared framework and no active hooks;
author/committer identities explicitly checked. Original production author and
author date were retained by `git commit --amend` with original message.

Amended final head: `014f7b9c9f451d6275af73c4af30a24668b77b7b`.
Unchanged dependency commit: `cd3577a6365685273c1b39a724814f7d67931508`.
Current complete range:
`5a2d2bdc3ad7a827038f877d75959916528db844..014f7b9c9f451d6275af73c4af30a24668b77b7b`.
Reviewed old range:
`5a2d2bdc3ad7a827038f877d75959916528db844..39f8fd7d2bee0c4754f0f9921d97855da7fbdddf`.
`review-r2-range-diff.txt` binds both; `review-r2.diff` is the entire narrow delta.
`final.diff`, `final-stat.txt`, `commit-series.txt`, `content-mapping.json`,
`review-packet.md` and `pr74-publication-plan.md` were regenerated for new head.

The new two-commit history contains one final registry update and one production
implementation; no fixup/transitional history, repeated pin or migrations. No
deployment/release/external-use boundary. Worktree clean; no push/PR changes,
BFF changes, wire decoding or lifecycle action. R1 still holds longer checks.
