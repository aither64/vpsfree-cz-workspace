# Review: defer live repository discovery from session HTML

## Assignment

Independently review the committed portal render-path follow-up for correctness,
compatibility, scope, security and verification gaps. Apply the General,
Architecture and repetition, Scope and proportionality, and Risk and
compatibility lanes from the mandatory-change-review workflow. Report Blocking,
Important and Advisory findings with exact evidence, then state whether the
commit is ready for package build and live acceptance.

## Repository and commit

- Worktree: `worktrees/2026-09-29-portal-performance/dev-workspace`
- Base: `ec05cb9f008cc8d6bccfd23e9b15a69d9a66fa40`
- Head: `d20bb64c45db1d803fc3b7a8c2956049860d72dd`
- Commit: `d20bb64 portal: defer live repository discovery`
- Diff: `git diff ec05cb9f008cc8d6bccfd23e9b15a69d9a66fa40..d20bb64c45db1d803fc3b7a8c2956049860d72dd`

## Intent and observed cause

After deploying bcrypt cost 5, 30 live no-scan loads had zero failures but p95
usable time was 2.082 seconds against the 2-second gate. Resource profiling
showed normal document TTFB around 0.28–0.30 seconds and periodic spikes around
0.89 seconds, aligned with the five-second active-repository discovery cache.
Transcript paging itself remained fast.

The initial session HTML synchronously called `activeRepositories`, while the
existing details API independently performs the same live discovery and the
browser already refreshes repository/member/artifact sections through it. The
commit removes only initial-page discovery and its initial warning. Initial HTML
still renders repositories stored in the session manifest through the existing
skeleton path. The details endpoint remains unchanged and continues to merge
verified live worktrees and report discovery warnings.

## Invariants and compatibility

- Do not weaken repository path, worktree or identity verification.
- Do not change the details API contract or browser compatibility.
- Do not remove stored repositories from initial HTML.
- Live-only worktrees and discovery warnings may appear after the existing
  details refresh rather than in the first HTML response.
- Archived-session behavior is unchanged.
- Old browsers with the new server and new browsers with the old server remain
  compatible because no endpoint, payload or persisted-state shape changes.
- There are no database, session, protocol, package-state or on-disk migrations.
  Rollback restores synchronous discovery and its prior latency.

## Files and checks

- `portal/internal/web/server.go`: removes synchronous active discovery and
  initial-page discovery-warning plumbing from `sessionPage`.
- `portal/internal/web/details_test.go`: proves initial HTML keeps a stored
  repository without invoking discovery, then proves the details refresh
  invokes discovery and surfaces its warning.
- `portal/internal/web/static/repository-review.js`: reconciles the refreshed
  top-level discovery warning when the repository review panel is mounted.
- `portal/internal/web/repository_review_browser_test.cjs`: covers warning
  appearance, replacement and clearing while preserving the mounted card.
- Focused tests passed with a writable temporary Go cache and `CGO_ENABLED=0`:
  `go test ./internal/web -run 'TestSession(PageUsesStoredRepositoriesWithoutDiscovery|DetailsDiscoversLateWorktreesAndCuratedArtifacts)$' -count=1`
- `gofmt` and `git diff --check` passed.

## Review finding and remediation

The first review of unpushed head `11928f2` found one Blocking issue: the
mounted repository review panel reconciled refreshed cards and counts but did
not apply the details response's discovery warning. The remediation moves the
refreshed warning into the mounted overview, replacing or clearing the prior
warning while preserving hydrated cards. The focused Node mounted-panel
contract, JavaScript syntax checks, focused Go tests and whitespace checks pass.
The fix was folded into the same unpushed commit as `d20bb64`; mandatory review
must rerun before package build.

## Remaining gates

- Review reconciliation.
- Push exact head and confirm exact-revision CI.
- Update the vpsFree extension and workspace pins, build the exact consuming
  package and switch the authorized user profile.
- Repeat 30 no-scan browser loads, then 30 loads overlapping a due dry-run
  archive scan. Both require p95 at or below 2 seconds, zero load failures,
  paged responses and no legacy fallback.
- Complete final whole-branch history and migration review before integration.
