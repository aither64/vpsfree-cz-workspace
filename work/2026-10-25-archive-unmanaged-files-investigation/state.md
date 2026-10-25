---
lifecycle: active
---

# 2026-10-25-archive-unmanaged-files-investigation

## Status

Implementation complete; archive acceptance and older-reader compatibility passed.
The broader creation CI remains red after two diagnosed lock-contention failures.
The original HaveAPI archive is recovered. No master merge or deployment has been
authorized or executed. Integration readiness is limited by the broader CI result.

- [x] Investigate and recover the original blocked archive (attempt 2).
- [x] Implement readiness before shutdown and durable lead-assisted repair.
- [x] Pass focused checks and resolve independent final review findings.
- [x] Pass packaged archive lifecycle CI and fast checks.
- [x] Pass older shipped portal receipt/continuation acceptance.
- [x] Publish the two-commit branch and capture its comparison.
- [x] Inspect both creation CI failures and record their scope and limits.
- [x] Prepare the consolidated handoff checkpoint.
- [ ] Integration and deployment, pending explicit direction.

## Branch and supported behavior

Only `dev-workspace` changed. Feature branch
`2026-10-25-archive-unmanaged-files-investigation` is published over SSH at
`5e4e99dfecfda94da47c10cd154dfa98269a6533`, with a clean worktree at
`worktrees/2026-10-25-archive-unmanaged-files-investigation/dev-workspace`.

Base and current upstream master are
`9634151b9836311c331a58880fbb4c46133fd98f` (fresh fetch before handoff).
The final series is:

1. `e4f6180fa7340335db0d0db8033d164639985e78` — archive readiness before shutdown.
2. `5e4e99dfecfda94da47c10cd154dfa98269a6533` — durable portal lead-assisted repair.

A confirmed explicit archive checks readiness, asks the retained lead to repair
local blockers, and rechecks after each completed repair turn. It continues while
validation progresses and stops after three cycles without progress or when
operator input is needed. Cancellation, deduplicated native delivery and portal
restart are supported. The lead retains its settings and stays available until
readiness passes; only the normal archive worker stops agents. Other sessions
remain usable during repair. Automatic archival and existing journal recovery
retain their policies. There is no generic auxiliary-file deletion.

## Verification and review

[Verification evidence](verification.md), [initial review](review.md),
[follow-up review](review-followup.md), [recovery](recovery.md),
[design](design.md), [detailed implementation/check history](implementation-history.md).

High risk due to destructive lifecycle operations and private persistent state.
Independent reviewer `/root/final_review` used the installed default development
reviewer fallback, gpt-6.1-sol/xhigh, because this tracking-only initiative has
no retained roster. All four lanes were applied. All four initial findings were
fixed; follow-up review found no new Blocking or Important findings. Direct
subsequent fixture fixes, README alignment and the one-line root-only CLI result
correction were inspected and tested under the narrow-fix policy. No new policy,
proof boundary or production design was introduced after that review.

Final range-diff was inspected against reviewed head f094a94b. The two owning
commits contain the fixes, with no obsolete unmerged approaches, repeated
update streams or migrations. No feature was merged, released or deployed.
The final saved comparison uses the exact base and head above.

## Documentation and limits

Supported behavior, cancellation and recovery are documented in the runtime's
[archive guide](https://github.com/aither64/dev-workspace/blob/5e4e99dfecfda94da47c10cd154dfa98269a6533/docs/session-archive-recovery.md).
The session command list and README verification entry point were updated too.
Incident evidence remains in recovery.md and findings.md. A reusable fixture
lesson is in `notes/dev-workspace/2026-10-25-ruby-package-layout-dependencies.md`.

Preparation is private schema-1 state. Existing lifecycle/cleanup formats are
unchanged. A shipped predecessor portal loaded the candidate shutdown receipt
as an ordinary retryable failure; the candidate then resumed the original intent
and completed native cleanup/archival. This proves the older-reader boundary,
not a full host package rollback. All acceptance ran in disposable VM state.
No live package was switched. No owned VM or verification command remains running.

Preflight is sampled. External writers and later I/O failures can still require
normal journal-owned recovery after shutdown; lead revival for that phase is
outside the accepted design. Committed content and branches retain the existing
archive policy.

## Next action

No verification remains running. Archive/fast CI and the older-reader VM passed;
creation CI remains red. Attempt 1 failed on fallback-name collision with
`session is changing: resource temporarily unavailable`. Attempt 2 failed at
approved-plan creation with `another dev-session command is changing
2026-10-25-explicit`. Both errors come from unchanged nonblocking runtime/source
lock paths, without any archive preparation active. The exact competing holder
was not captured, so their underlying concurrency cause remains unresolved.
The baseline has successful CI runs; this is classified as an existing lock race
by path/behavior inspection, not a reproduced baseline failure. Do not claim a
fully green branch or deployment readiness.

The requested archive implementation is committed, reviewed and published.
A separate investigation should resolve the creation contention before treating
whole-suite CI as green. Integration into master still needs explicit direction.
Keep the initiative active; retain its branch and worktree.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-archive-unmanaged-files-investigation/
