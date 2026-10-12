# General mandatory change review

Reviewer lane: general  
Model and effort: `gpt-5.6-sol`, `xhigh`  
Risk classification from the review packet: high

Reviewed committed ranges:

- `codex-web`: `269962eb65007581ba69c205634f9e6c14cc39d3..bba2ae1d9796dc7267c0bfc5ee9f072f43d6e92e`
- `dev-workspace`: `bcbaf825d71285cbbd05b56e78bc386f2df480bd..774c2083333b9b71d4abb04d4aa7c79ea0aa897d`
- `vpsfree-dev-workspace`: `c4df3838de8b42083bd43e86bfdff7d45a7e952f..d0ebe39e4cc2e41cb791ad048c60eb1e940c023e`
- `workspace`: `e0d3dee52ac637a96a7d73299aecd753759b484b..bfc80f25864528b5b954daf84c6e8a7d4a8348c7`

No Blocking findings.

## Important findings

### Completed creation receipts permanently consume the 512-receipt allowance

Commit: `5bcf254fa36c305d496f8d762bf0ae7e5f4dccf3`

Evidence: `portal/internal/web/creation_store.go:112-145` loads every valid
`creations/<slug>.json` file into the in-memory map and rejects the store once
the count exceeds 512. `portal/internal/web/creation.go:95-137` rejects every
new slug when the map already contains 512 entries. The only later mutations
at `portal/internal/web/creation.go:140-156` and `portal/internal/web/creation.go:299-347`
change receipt state; neither the implementation nor lifecycle completion
removes a receipt or its completion evidence. The only removals involving
these paths are temporary-file cleanup and test setup.

Every successfully created session therefore consumes one lifetime slot in a
persistent portal store. After 512 creations, the portal returns `too many
session creation receipts` for every new session until an operator edits the
private state by hand. A completed deletion exposes the stale identity problem
earlier: the workspace session and lifecycle journal can be gone while the
receipt still makes an identical request reuse a now-stale ready result and
makes a changed request fail as a conflicting creation request.

Add an explicit, crash-safe retirement policy tied to proven terminal state.
Ready receipts can be retired when their idempotency role is over; failed or
paused receipts need a dismissal or bounded retention path that preserves
retry safety. Cover normal completion, archive/delete, restart, and the capacity
boundary with tests.

### Supported large comparisons can silently lose rename metadata

Commit: `6dcf75681f936872d772df6f44a676cbf70781d3`

Evidence: `portal/internal/repository/review.go:24-30` accepts as many as 5,000
changed files, but `portal/internal/repository/review.go:317-349` invokes
`git diff --find-renames=50% -l1000`. Git exits successfully after skipping
exhaustive rename detection when the rename candidate count exceeds 1,000;
`ReviewReader.git` at `portal/internal/repository/review.go:108-138` discards
stderr on successful commands. The accepted comparison is then returned with
deletion/addition records instead of the required rename metadata.
`portal/internal/repository/review_test.go:108-153` exercises only one rename.

I reproduced the behavior in a temporary repository with two modified rename
candidates and `-l1`: Git emitted `exhaustive rename detection was skipped due
to too many files` on stderr and returned delete/add records; increasing the
limit returned `R053` records. This is the same threshold behavior at a smaller
fixture size.

Make rename detection and the advertised comparison bound consistent, or turn
Git's skipped-detection condition into an explicit unavailable/degraded result
instead of silently returning false metadata. Add a regression above the
chosen threshold using modified rename candidates, since exact renames can be
paired without exhaustive similarity detection.

## Commit series, documentation, and verification

The commit split matches the planned ownership and delivery order: provider
behavior precedes the generic runtime, the organization wrapper pins that
runtime, and the workspace pins the wrapper. Functional tests and docs stay
with their behaviors. The small subject-only typed-event integration commit
`a6babcba26d60d989e193f64a0fd7d4062feaf2e` is adequately explained by its
subject and the provider commit it consumes. I found no abandoned schema,
duplicate input-update stream, fixup history, or unrelated bundled change.

All four exact ranges pass `git diff --check`, and all four review worktrees
were clean during this review. I relied on the packet's recorded successful
quick suites and inspected the relevant tests rather than repeating them.

Residual verification gaps remain by design at this checkpoint: the full live
portal/App Server browser flow, packaged cross-repository integration, and
upgrade/rollback exercise have not run. Question geometry has only a focused
synthetic browser fixture so far. Those checks should run after the Important
findings are resolved or explicitly accepted.
