---
lifecycle: active
---

# 2026-10-28-files-tab-limit-diagnosis

## Status

- Implementation phase: user said "Implement the plan". Architect is finalizing
  the accepted lazy-directory brief; implementer packages follow that boundary.
  No default-branch integration or actual activation is authorized yet.
  Source diagnosis and read-only inventory are complete; inspected sessions are
  unchanged. Production Files behavior remains unchanged pending delivery.

## Phase checklist

- [x] Verify session identity, environment and retained team roster.
- [x] Assign source investigation and recommendation to `architect0`.
- [x] Establish exact limits, failure behavior and running-package evidence.
- [x] Assess the recommendation and prepare findings for the user.
- [x] Inventory active/archive tracking roots and identify limit-triggering sessions.
- [x] Explain largest file contributors and report evidence versus inference.
- [x] Reconcile design with user's lazy/collapsed-directory preference.
- [ ] Finalize decision-complete implementation brief and initial tracking commit.
- [ ] Runtime implementation, focused checks and feature commit/publication.
- [ ] Dependent workspace/configuration pins and quick deployment-contract check.
- [ ] Whole-branch independent final review and findings resolved.
- [ ] Longer package/browser/composed workspace/aitherdev verification.
- [ ] Integration approval and exact final feature heads integrated.
- [ ] Deployment approval, activation, usability verification and machine release.

## Backlog

| Owner | Deliverable | Acceptance and dependencies |
| --- | --- | --- |
| architect0 | Complete: `design.md`, root cause and proposed solution | Deployed source identity, count vs metadata behavior, API/UI chain, minimal fix and checks; no application edits |
| lead | Complete: findings and handoff | Inspected design and immutable deployed HTTP/UI/limit source, plus canonical scanner/adapter; triggering session remains uninspected |
| architect0 | Complete: `file-inventory.md` | All nine outliers, observed counts and top contributors, archive raw-data breakdown and policy caveat; metadata only, no peer worktree/transcript/content access |
| architect0 | Final implementation brief | Fix API/page/resource/UI/compatibility contracts before source implementation |
| implementer0 | Runtime execution package | Source, tests, docs, hooks, quick checks, commit and review fixes; depends on brief and initial tracking commit |
| implementer1 | Delivery pins/preparation | Workspace+configuration feature worktrees, exact matched pins, contract and build prep; depends on published final runtime head |
| reviewer0 | Independent final review | Committed complete series, quick checks, all applicable lanes, pin consolidation and no-migrations conclusion |

## Next actions

- Commit this initial substantive implementation plan/state on shared master,
  preserving unrelated changes. Accept final architect brief and assign runtime
  implementation; delivery owner may prepare isolated environments meanwhile.

## Documentation

- [Plan](plan.md); [diagnosis and proposed solution](design.md).
- [Session file-count inventory and contributor evidence](file-inventory.md).
- No product documentation change: findings only, no application behavior change.
- Session portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-files-tab-limit-diagnosis/

## Repositories

- `dev-workspace`, read-only; no registered feature branches or worktrees.

## Commands run

- `dev-session current`: matched `2026-10-28-files-tab-limit-diagnosis` and both
  environment markers matched the thread-bound workspace identity.
- `dev-session team list ... --as-is`: retained `delegated_4` roster;
  `architect0` ready with saved workspace-write access.
- `dev-session team assign ... --to architect0 --message-stdin`: queued
  successfully with UUID `d4a0770a-f6dc-4463-aefe-7f2c9337e1e4`.
- Initial assignment used an invalid human-readable message ID and was rejected
  before delivery; retried with the required stable lowercase UUID.

## Results

Follow-up final inventory: 374 public tracking directories (114 active,
260 archive), 381,370 directory entries examined in 25.8 seconds without following
symlinks or reading file content; no scan errors. Nine directories exceed listing
budgets (five active, four archive). Largest active roots:
`2026-10-17-confctl-rust-rewrite-plan` 90,735 regular files (~12.87 GiB logical),
`2026-10-24-vpsadmin-haveapi-upgrade` 80,853 (~5.19 GiB),
`2026-10-09-evaluate-confctl-rewrite-language` 63,554 (~3.39 GiB).
Dominant path categories are build/compiler caches, dependency trees and repeated
verification fixtures, rather than ordinary notes. All nine exceed 5,000 files;
the largest three also exceed both metadata budgets. No metadata-only offender.
Exact producers/byte duplication and necessity of each copy are not established.
The final nine-session table and archive-specific breakdown are in
`file-inventory.md`; active `2026-10-20-kernel-check` is near the cap at 4,987.
Final metadata check was 2026-10-28 14:23:22 UTC; this live inventory is not atomic.

The four archive outliers predominantly contain raw JSON/log/text/research/fixture
data, not Markdown bulk. The storage-retention guide explicitly retains
predecessor archive policy until compaction. This is a compatible explanation,
not proof of the exact historical policy of each archive or a current lifecycle
defect. Private receipts and lifecycle history were not inspected.

`ListTrackingFiles` recursively includes regular files even when ignored or
unregistered. The running source uses a 5,000-file cap and separate 4 MiB
traversal-metadata and estimated-output budgets. Exceeding a budget returns
`nil` plus `ErrTrackingFilesLimit`, discarding discovered entries; the adapter
maps it to `ErrReviewLimit`, and HTTP returns 503 without a files array. The
browser renders only successful arrays, leaving the initial tree empty. Listing
reads no file contents: a large file's size alone cannot trigger this error.

Runtime/profile package:
`/nix/store/a3r70kgqaf46185cjmjgalza67vpg0hd-dev-workspace-0.2.0`.
Deriver: `/nix/store/7xb8zyd1g0cv5xvlsnlw2lll07c4bn33-dev-workspace-0.2.0.drv`.
Source: `/nix/store/pzmrjkkvi3vh0qw649420xk8jw263ilx-source`.
Relevant scanner/adapter/limits/HTTP files and Files UI block match locally
available origin/master `4a002f52c3b55099540aa99708d5fcf29f7b2456`.
This is not a claim that the entire deployed tree has that Git revision.

Primary recommendation, revised after user steering: true lazy directory
browsing. Initially list root children, leave directories collapsed, fetch direct
children on expansion, and bound huge individual directories with continuation.
Avoid recursive pre-scans and total descendant counts. Preserve direct-link
selection, confinement, ignored-file visibility and independent preview/download
guards. Partial recursive results are now only an optional interim mitigation.
Raising limits alone postpones failure. See `design.md` for API compatibility,
references and proposed acceptance cases. This supersedes the earlier interim
recommendation at the end of `file-inventory.md`.

Evidence checks were source inspection only; no application tests/builds run.
Mandatory independent final change review is not triggered by investigation,
planning and findings alone. No substantive product deliverable was changed.

## Open questions

- Initial source diagnosis did not verify the affected session. Follow-up now
  explicitly authorizes read-only inventory of session tracking files; worktrees,
  teams, transcripts and private runtime state remain outside scope.

## Cleanup

- No runtime changes, deployments or repository claims. Leave the session open.
