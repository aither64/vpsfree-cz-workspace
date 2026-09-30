# Mandatory review: retained team archive recovery

## Requested outcome

Review commit `b36691d52790dffb5e104900343dca7f841e55e6` in the dev-workspace feature worktree. Determine whether the journal-scoped recovery adapter can safely complete a partially archived retained team without bypassing lifecycle ownership, losing unresolved submission state, recreating members, changing the selected package, or invoking the predecessor executor before final exact proof.

Acceptance requires:

- only an existing exact `tracking_committed` archive journal can enter the path;
- committed archive tracking and recorded complete/abandoned semantics are reverified under creation then slug locks before team mutation;
- the retained root is proved archived before team mutation;
- every outstanding member is prevalidated before any archive or roster mutation;
- archived members are not archived again;
- active members must be exact retained materialized identities and pass ordinary nonforced idle, prompt, queue and ledger checks;
- no replacement, recycle, bootstrap, unarchive, resume, start, deletion or interruption can occur;
- a final exact all-member archive proof precedes the selected predecessor executor;
- retries preserve the journal, exact identities and durable forward progress;
- the selected profile, Codex 0.155.0 process and predecessor lifecycle executor remain unchanged;
- normal archive, forced deletion and ordinary package switch behavior remain unchanged.

## Initiative and repository

- Initiative: `2026-09-29-portal-performance`
- Plan: `work/2026-09-29-portal-performance/plan.md`
- State: `work/2026-09-29-portal-performance/state.md`
- Design: `work/2026-09-29-portal-performance/design.md`, especially the recovery amendment from line 1101 onward
- Stable session: `https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-29-portal-performance/`
- Repository: `dev-workspace`
- Worktree: `worktrees/2026-09-29-portal-performance/dev-workspace`
- Review base: `e58f8f61ce43058aba49361a0b3bd1ecd98af866`
- Review head: `b36691d52790dffb5e104900343dca7f841e55e6`
- Commit: `b36691d session: recover partially archived retained teams`

This is an incremental review of a coherent high-risk follow-up to the already reviewed exact archive proof and ready-creation adapter. Final whole-branch readiness review remains a later gate.

## Commit split and scope

The single commit contains the retained-only policy, its private CLI and host orchestration, direct regression tests, and the operator documentation for that same recovery behavior. They are deliberately bundled because the new destructive recovery route must not exist without its fail-closed tests and operator limits.

Files changed:

- `libexec/dev-session`
- `libexec/workspace-host`
- `portal/cmd/workspace-portal/main.go`
- `portal/internal/teamruntime/runtime.go`
- `portal/internal/workspacecodex/archive_proof.go`
- adjacent Go and Ruby tests
- `docs/dev-sessions.md`
- `docs/workspace-portal.md`

No migrations, schemas, generated clients, public browser APIs, runtime-contract versions, Codex versions, dependency pins or downstream repositories change in this commit.

## Non-goals and rejected alternatives

- No Codex patch or runtime upgrade. Exact SQLite, metadata and filesystem evidence agree.
- No manual roster, SQLite, rollout-file, journal or profile edits.
- No unarchive followed by rearchive.
- No ad hoc private helper invocation outside the owning archive journal.
- No broad lifecycle bypass and no automatic recovery during ordinary switch.
- No active member replacement or fresh-member recovery on this route.
- No weakening of exact archive proof or treating a successful helper exit as proof.
- No earlier-generation rollback.

The selected design reuses the existing archive loop with an explicit retained-only precheck and disables its fresh-member recycle branch. `workspace-host recover-archive` lazily loads the existing dev-session verifier, holds the transition lock, acquires normal creation and slug locks for verification/helper work, then releases those session locks before selected-predecessor replay.

## Compatibility and deployment assumptions

- Persisted roster, journal, creation and submission-ledger formats remain unchanged.
- The selected predecessor and candidate have byte-identical private runtime contracts.
- The App Server stays on pinned Codex 0.155.0.
- Old and new packages can read every state produced by this correction.
- Partial successful member archival is forward progress; retry re-proves it rather than compensating with unarchive.
- Deployment remains blocked until both authorized paused journals complete. The profile is not selected during recovery.
- The owning component is dev-workspace. Current consumers are the generic dev-workspace package, the vpsFree extension pin, and the consuming vpsfree-cz workspace package. Downstream pins are intentionally unchanged until this commit passes review and package verification.

## Documentation

- `docs/workspace-portal.md` describes the narrow recovery command, partial-team completion and retry behavior.
- `docs/dev-sessions.md` describes operator use and prohibitions.
- `work/2026-09-29-portal-performance/design.md` records the evidence, lock order, rejected alternatives and rollout gates.
- Individual live replay evidence remains in the initiative artifacts, not project documentation.

## Quick verification

Passed from the repository's Nix environment:

```text
cd portal && GOFLAGS=-mod=mod go test ./internal/workspacecodex ./internal/teamruntime ./cmd/workspace-portal
ok internal/workspacecodex (5.243s)
ok internal/teamruntime (2.909s)
ok cmd/workspace-portal (0.190s)

ruby -Itest test/workspace_host_test.rb --name "/(recover_archive|workspace_host_loads_dev_session)/"
11 runs, 178 assertions, 0 failures, 0 errors

ruby -Itest test/dev_session_test.rb --name /committed_archive_verifier/
1 run, 14 assertions, 0 failures, 0 errors
```

Also passed:

- `ruby -c libexec/workspace-host`
- `ruby -c libexec/dev-session`
- `gofmt -d` on all changed Go files produced no output
- `git diff --check`

The full archive suite, real-flock integration, package build and live replay have not run yet. They must wait for this review.

## Risk and lanes

- Overall risk: **High**. The change performs destructive Codex archival and durable roster/ledger updates inside a mixed-version, interrupted lifecycle recovery path.
- Reviewer: retained `reviewer0`
- Saved model: `gpt-6-sol`
- Saved effort: `xhigh`
- Access: read-only
- Lanes: General; Architecture and repetition; Scope and proportionality; Risk and compatibility.

Read and follow:

- `/home/aither/.codex/skills/mandatory-change-review/SKILL.md`
- `/home/aither/.codex/skills/mandatory-change-review/references/general-review.md`
- `/home/aither/.codex/skills/mandatory-change-review/references/architecture-review.md`
- `/home/aither/.codex/skills/mandatory-change-review/references/scope-review.md`
- `/home/aither/.codex/skills/mandatory-change-review/references/risk-review.md`

Review the committed diff and surrounding lifecycle/archive code directly. Report findings by severity with file and line references. If there are no findings, say so explicitly and list residual risks or verification gaps. Do not delegate or edit files.
