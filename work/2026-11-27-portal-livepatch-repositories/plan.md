# Repository comparison implementation plan

Status: implemented, reviewed, verified, deployed and merged on 2026-11-27.
See [state.md](state.md) and [rollout.md](rollout.md) for delivered revisions and results.
The sections below retain the approved execution plan.

## Outcome and scope

Make the repository tab useful for the livepatch backport session: compare each
Linux branch against its verified starting point, keep healthy repositories
responsive, and explain individual failures. Deliver the verified fix to aitherdev
and merge the implementation and matching deployment changes.

The user added: “aitherdev can be deployed using vpsfree=cz-configuration, the plan
should merge it when it's done and verified.” The intended repository is
`vpsfree-cz-configuration`. The planned integration set is:

| Repository | Change | Integration target |
| --- | --- | --- |
| `dev-workspace` | Review base, loading, error handling, tests and docs | `master` |
| workspace (`aither64/vpsfree-cz-workspace`) | Matching composed runtime pin | `master` |
| `vpsfree-cz-configuration` | Matching `dev-workspace` channel input for aitherdev | `master` |

No Linux/vpsAdminOS source changes, Codex upgrade, codex-web change, site-extension
source change, default-branch changes or lifecycle redesign are planned. The user
later approved preserving deployed extension 39470c6 through its workspace pin. Recheck current
source before implementation; the diagnosis used the installed source recorded in
findings.md. Preserve unrelated changes and use initiative feature worktrees.

## 1. Add an explicit repository review base

Use a small versioned portal-owned record alongside existing comparison state,
not a new portal.yml field. Current Ruby manifest validation rejects unknown
repository keys; keeping this setting separate avoids changing lifecycle manifests
and old-package manifest readers.

Expose a supported CLI operation, provisionally:

```text
dev-session worktree review-base <slug> <name> --as-is --base <full-SHA>
dev-session worktree review-base <slug> <name> --as-is --clear
dev-session worktree review-base <slug> <name> --as-is --json
```

The last form reads the setting. Share validation and persistence through the Go
portal command bridge, following capture-comparison's Ruby wrapper and session
locking. Mutation is for active sessions; archived comparisons remain readable.

- Bind the record to the existing session/repository scope identity. Do not allow
  a reused slug or retargeted registration to inherit another repository's base.
- Store an exact SHA, resolve it locally as a commit, and verify it is an ancestor
  of the current registered head. Recheck registration/head before writing.
- Use existing atomic-write and locking conventions. Refuse malformed or stale
  settings explicitly. No fetch, checkout, filter, maintenance or ref mutation.
- Keep initial_base_sha and default_branch unchanged. Initial base is evidence
  for choosing a setting, not a universal replacement for ordinary merge bases.

Resolution order for new history/comparison views:

1. Existing durable link or snapshot: retain its original immutable pair.
2. Valid explicit review base: compare that SHA to the verified current/final head.
3. No setting: preserve existing automatic merge-base/saved-pair/fallback behavior.

If an explicit base is missing or ceases to be an ancestor after a rebase, report
that condition instead of silently reverting to origin/master. New commits on the
same branch continue to use the fixed base. Setting base equal to head is a valid
empty comparison.

Do not overwrite existing exact-pair records. Explicit-base views use the existing
content-addressed durable review descriptors; they must not conflict with or write
into the legacy automatic per-head comparison slot. Ensure automatic observation
and capture-comparison follow the selected policy consistently. Preserve the
existing explicit historical capture contract and old comparison links.

Primary code: internal/repository/review.go, internal/web/repository_review.go,
repository_comparisons.go, portal command dispatch, and libexec/dev-session.

## 2. Isolate loading and make failures actionable

Replace the browser's sequential eight-repository history batches with a small,
bounded queue using existing per-repository endpoints. Load visible/requested cards
first and defer off-screen histories and totals. Render each completed card
immediately. Retain existing card layout, Compare, Local commits, Refresh commits,
feedback and cancellation behavior; add no new settings screen.

- Preserve server process/request budgets and file/blob limits. Separate history
  success from totals or file-preview failure, as the current contract requires.
- Carry typed timeout/cancellation, unavailable-object, missing/invalid-base and
  size-limit failures through Resolve/Pair and the HTTP mapper. Preserve the
  existing error text field for older clients; distinguish retryable failures.
- Stop requeuing a failed unchanged history on every 15-second head poll. Retry on
  explicit Refresh or changed comparison inputs; resume cancelled reads normally.
- Add an opaque comparison-version field to state/history responses so a CLI base
  change invalidates new-view caches even when HEAD stays the same. Keep `head`
  and older-server fallback. Do not replace an already open frozen comparison.
- Reuse/coalesce immutable pair calculations by canonical repository, exact input
  SHAs and policy identity where needed. Keep routine status observation from
  repeatedly launching expensive merge-base reads under a one-second deadline;
  use completed valid results and the explicit pre-merge capture path. Validate
  automatic capture behavior with the existing tests before changing it.

Do not increase global timeouts or size limits to accommodate the wrong 88k-file
comparison. Reassess timing only after correct-base behavior is measured.

## 3. Compatibility and documentation

Keep manifest, lifecycle journal and existing saved-review schemas unchanged.
The new setting has its own versioned file. Older packages ignore it and retain
old browsing behavior; manifests and old/new durable descriptors remain readable.
Clearing the setting restores automatic selection without changing Git history.
Archive/revive should retain the setting for the same identity; deletion/reuse
must not apply it to a new identity. Test these transitions with disposable state.

An older package will not honor an explicit base. Record that limitation rather
than claiming full browsing equivalence after a software downgrade. Application
activation/recovery follows the selected workspace transition contract; do not
assume that selecting an older user-profile generation is permitted.

Update dev-workspace's portal and session guides with selection precedence, CLI
examples, limits, error meanings, private-state retention and recovery. Keep rollout
SHAs, per-branch base evidence and deployment results in this session. Configuration
needs its normal channel update, not a deployment-report documentation commit.
Apply the workspace writing skill to new user-visible errors/help before commit.

## 4. Verify and review the completed change

Start with focused tests in the repository's Nix environment:

| Area | Required evidence |
| --- | --- |
| Pair selection | Diverged default plus explicit base; ordinary branch unchanged; equal base/head; invalid/missing/non-ancestor base |
| State and links | Existing per-head record conflict avoided; old links unchanged; base change with same head; concurrent head change; clear; archive/revive; identity reuse; older-reader behavior |
| Browser | Healthy visible card completes while another history is blocked; totals failure preserves history/Compare; failed unchanged inputs do not loop; navigation cancels reads; existing controls stay consistent |
| Errors and partial clone | Timeout is not reported as missing HEAD; limits remain enforced; missing blob affects preview without hiding file metadata; no lazy fetch |
| Baseline regression | At the recorded linux-core head, exactly 13 commits and 9 files instead of the 2019 comparison |

Use focused `go test -mod=readonly` for repository/web packages, the applicable Ruby
CLI tests, and existing browser fixtures. Do not launch full suites to validate the
plan. Before final independent review, commit all intended source/docs/tests, pass
quick checks, and consolidate obsolete fixes and repeated pin updates. Supply the
complete history and state-format/compatibility inventory to the reviewer.

After review and remediation, run the packaged application checks and relevant
browser/lifecycle integration coverage, the workspace composition check, and the
scoped aitherdev build. Publish development branches and inspect their relevant CI.
Use the monitor skill for long checks. No unexpected local kernel builds.

## 5. Prepare matching deployment inputs

Pin the final published dev-workspace feature revision in both consumers:

- Workspace: preserve extension selection, set the direct nested runtime URL, and
  run `nix flake update vpsfree-dev-workspace/dev-workspace` in its feature worktree.
- Configuration: in its Nix shell, use
  `confctl inputs channel set --commit dev-workspace devWorkspace <revision>`.
  Preserve its generated commit message and inspect semantic lock changes.
- Run `bin/check-dev-workspace-deployment --workspace-root <workspace-worktree>
  --configuration-root <configuration-worktree>` against the final locks.

Build the final committed `cz.vpsfree/machines/aitherdev` configuration and composed
workspace application. Preserve prepared generations and recovery evidence. Confirm
both consumers select the same generic runtime and unrelated inputs are unchanged.
Recheck the final pin changes under the required review/history policy.

## 6. Deploy, repair the affected views, then merge

Follow configuration's docs/operations/codex-providers-aitherdev.md and the
current workspace coordination/lifecycle rules. Prepare outside execution claims;
acquire the aitherdev machine claim for activation and release it after deployment effects are settled and verified under the workspace machine-retention policy.
Resolve any unfinished original operation before starting a conflicting transition.

1. Through the configuration feature worktree, dry-activate and deploy the prepared
   aitherdev system without reboot. Check live-system and system-profile identities
   and preserve confctl's rollback mechanism.
2. Switch the workspace user profile from the matched workspace feature worktree,
   using `workspace-host switch --source` with the held claim and session identity.
   The system selects the host contract; the application remains in its user profile.
3. Check portal/router/coordinator health and conversation continuity. Do not use
   live session creation/archive operations as test fixtures.
4. Inventory all 13 Linux registrations again. For each, record branch, observed
   head, verified intended base and its provenance; use existing initial_base_sha
   where supported by the branch evidence. Recover missing bases from exact retained
   evidence, never infer them from today's master. Apply settings through the new
   CLI with per-registration/head checks, preserving unrelated livepatch work.
5. In the actual browser, verify history, totals, branch and individual commit
   comparisons, file previews, refresh and a saved link. Check a vpsAdminOS card
   loads independently. Reproduce the 13-commit/9-file baseline at its recorded
   immutable head; compare advancing live heads against independently counted Git
   results. Report any unavailable branch or blob separately.
6. Once source review, required checks, CI and deployed smoke checks pass, fast-forward
   and SSH-push dev-workspace/master, then the matching workspace/master and
   vpsfree-cz-configuration/master branches. This merge-after-verification outcome
   is part of the user's requested plan. Capture comparisons before integration,
   take short repository claims, and preserve unrelated shared checkout changes.
7. Verify the exact final heads on remote defaults and the deployed/pinned lineage.
   If a rebase changes a head, update dependent pins and repeat affected checks and
   review before merging. Retain feature refs, release claims through normal tools,
   and record the completed delivery. Do not archive the session automatically.

## Execution ownership and stopping points

The current conversation created a tracking-only session with no native lead roster.
Do not invent or borrow a team. At implementation start, check live same-session
identity and roster; use supported ownership for subsequent reviews/deployment and
record a design brief before code changes. Routine planning needs no independent
change review. Mandatory final review applies to the completed implementation.

The plan has no unresolved product-choice blocker. Per-branch historical base
verification, current source/roster checks and prepared generation identities are
execution prerequisites. If a required base lacks evidence, keep that repository's
failure explicit while completing the generic fix and healthy repositories.
