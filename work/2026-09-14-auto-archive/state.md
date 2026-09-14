---
lifecycle: complete
---

# Automatic session archival

## Current status

Implemented, reviewed, deployed and enabled on aitherdev. The final package is
`/nix/store/smwr2xjkf9qz2v6hmdf2hh7g9iaqdvga-dev-workspace-0.2.0` (user-profile
generation 41). The hourly `workspace-auto-archive@vpsfree-cz.timer` is active;
its service completed successfully. Policy epoch: 2026-09-14T14:23:27Z.
No live session was archived. The initial 18 verifiable sessions received full
new intervals, and all 18 kept the same inactivity and eligibility timestamps
across the final package switch and subsequent service run. No operation is
pending. Legacy/unverifiable sessions are deferred; see deployment.md.

All three exact feature heads are merged and pushed to master. All five
feature/temporary worktrees have been removed, with branch refs, comparisons
and this session record retained. The user explicitly requested that handoff
not wait for default-branch CI; those jobs may finish independently and are
not a remaining task gate. Implementation, deployment, integration and cleanup
are complete. No operator action remains.

The owned session is shell-only: no shared Codex writer was created. It has
no conversation activity identity and is therefore deferred by the worker.

## Repositories and revisions

All retain branch `2026-09-14-auto-archive`. These former worktrees under
`worktrees/2026-09-14-auto-archive/` have been removed:

| Repository | Worktree | Final head | Feature base |
| --- | --- | --- | --- |
| Generic runtime | dev-workspace | 83136101866eb42d9e079f47191308c0549ac9e7 | df21f2ea8fe27efdb2cb8c0330fa31acd0f3a933 |
| Organization extension | vpsfree-dev-workspace | a08a40eeff124bdbcc1ce6b6b06aed1839a9d9fc | 89a03581b13056fa83114e592f2e2993e6a87887 |
| Workspace policy and consumer | workspace | 4078d32de4f731dbab83c4dfa186da58a6764353 | 95a451d18f2a2ff7ed06a9eca9e76f0b5563254c |

All heads are pushed via the prescribed SSH remotes. Generic has two commits:
worker/lifecycle/timer, then portal controls. Organization has one dependency
pin; workspace has a standing-policy commit and a consumer pin. Review fixes
were folded into their owning unmerged commits. Exact final repository
comparisons were captured using dev-session worktree capture-comparison for
all three registrations. Upstream master refs were fetched again after the
final pushes and are unchanged. The workspace feature was rebased onto shared
master 95a451d before its final commits; that advancement was coordination only.

Initial substantive plan/state were committed on shared master at 758834a,
before code commits or deployment. Workspace master has unrelated changes from
other initiatives; none were staged or modified for this work.

## Review

High risk: automatic lifecycle transitions, persisted state, deployment and
rollback. All four required standalone lanes ran with gpt-5.6-sol / xhigh:
general, architecture, scope and risk. Original exact ranges and component
ownership are in review-packet.md; each lane's report is retained.

All Blocking/Important findings were fixed. review-reconciliation.md records
merged findings and focused proof: unknown-activity resets, conversation-bound
holds/results, valid JSON stdout, candidate-owned timer cleanup for an old
initiator, rollback/unregister restoration after timer-stop failure, and
retryable revival sidecar resets. Direct remediations did not introduce a new
contract/design, so no review rerun was needed. The live browser check found a
one-line layout issue; the portal commit now uses its existing checkbox class.

## Verification

- Focused retention: 8 tests / 33 assertions.
- Automatic plus archive tests: 26 / 579; new sidecar-revival retry: 1 / 17.
- Full host tests: 77 / 485, including partial enable and stop failures.
- Relevant Go packages, HTTP control contracts and the Go-owned browser client
  contract passed. Ruby syntax, node --check, gofmt and git diff --check passed.
- Full generic `nix flake check --print-build-logs` passed, including the host
  substrate VM activation/rollback check. Packaged lifecycle tests: 308 / 3246
  with 12 environment-gated skips; packaged host tests: 77 / 470 with 3 skips.
  Focused checks outside the build sandbox covered the changed paths.
- Consuming workspace flake check passed (deployment contract 3 / 14).
- Final consuming `nix build --no-link --print-out-paths --print-build-logs`
  passed, including packaged Go and Ruby checks on the final source.
- Final generic CI passed:
  https://github.com/aither64/dev-workspace/actions/runs/34855523357
- Final organization CI passed, including flake-check and devcluster-check:
  https://github.com/vpsfreecz/dev-workspace/actions/runs/34855633402
- The organization CI before the one-line UI style change passed completely:
  https://github.com/vpsfreecz/dev-workspace/actions/runs/34854515736
- Superseded organization run 34854159188 was cancelled after its head changed.
  Other superseded runs were already complete; current-head runs were retained.
- systemd-analyze --user verify accepted the timer/service. The live user
  manager successfully ran the disabled-policy worker, disabled/re-enabled the
  timer, ran the first enabled scan, and ran again after the final switch.
- Read-only Playwright checks used CA verification and a pin of the verified
  leaf key. Final panel layout was visually inspected; no page errors. The
  shell-only session shows its missing identity, and a normal live session
  displays policy and eligibility. No other session's hold was changed.
- first-scan-results.json proves fresh periods and zero archives;
  restart-results.json proves all 18 unchanged periods survived the switch.

## Deployment and compatibility

Used `workspace-host switch --source` with the initiative workspace worktree.
No vpsfree-cz-configuration change was needed: the application remains in the
user profile. Existing manifest/archive journal formats are unchanged; private
schema-1 policy/observation files are outside the checkout. The pre-feature
package remains rooted in user-profile generation 39 at
`/nix/store/9z5g3q4akpzjc2449r6q6hlivvw1ja0x-dev-workspace-0.2.0`.

The deployed dry run inspected 174 directories: 18 verifiable sessions (14 with
registered repositories, 4 without), 146 lacking lifecycle front matter, eight
without conversation activity, and two without portal manifests. Automatic
archival was enabled only after inspecting this result. The first eligible
recorded date is 2026-09-21T14:23:29Z, subject to unchanged activity and normal
merge/cleanup checks. No production session was aged artificially for tests.

## Investigation notes and cleanup

- Go cgo needs GCC in the Nix shell; browser_contract_test.cjs is launched by
  its owning Go test with fixture arguments. See the focused-toolchain note.
- Playwright's earlier unrooted package disappeared before use. Refetching with
  an explicit output link restored it; see the Playwright GC-root note.
- A disposable delete/recreate fixture initially assumed every mock portal
  command had --cwd. The uploads removal command does not; the fixture was
  corrected and the regression passed.
- Curated review, deployment, browser and scan evidence is retained. Transient
  build logs, raw candidate inventory, observation comparison and the Playwright
  package link were removed after verification. No credentials were copied to notes,
  commits or output; browser credentials were read only at runtime.

Stable portal URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-14-auto-archive/

Implementation tracking stayed in the working tree through review/deployment.
The consolidated integration handoff records the completed work and curated
artifacts. The session stays in work/ for follow-up; archival was not requested.

## Default-branch integration

User authorization: merge into default branches and clean up. Refetched all
three upstream master refs; no upstream advanced. All feature worktrees were
clean and final reviewed heads were unchanged, so no rebase, pin update, review
rerun or redeployment was needed. Shared master 95a451d was an ancestor of
workspace feature 4078d32. Independent repositories used fresh detached target
worktrees; workspace integration used shared master with no staging. Branch
refs are retained.

All fast-forwards were published: generic df21f2e -> 8313610, organization
89a0358 -> a08a40e, workspace 95a451d -> 4078d32 locally and 9de2a6c -> 4078d32
on origin. The exact local and remote feature heads were fetched and proved
ancestors of each origin/master. Canonical bare master refs were synchronized.
Before pushing, the generic target-worktree retention check passed (8/33),
organization target-worktree flake evaluation passed, and workspace deployment
contract passed (3/14). All comparison captures were refreshed before merging.

Temporary target worktrees were removed with non-force git worktree remove.
All three feature worktrees were removed through dev-session worktree remove
without force; it retained repository registrations/heads and closed their
managed tmux windows. Local and remote feature refs remain. No redeployment
was needed because the deployed revisions are exactly the merged revisions.
Default-branch CI at the last observation:
- Generic run 34863456666 passed all jobs:
  https://github.com/aither64/dev-workspace/actions/runs/34863456666
- Organization run 34863538194 passed flake checks; its development-cluster
  check was still running:
  https://github.com/vpsfreecz/dev-workspace/actions/runs/34863538194
- Workspace has no applicable workflow.

Per the user's explicit "no waiting for ci" instruction, no further CI wait
or status polling is required. The organization run remains in GitHub; it was
not cancelled. Both exact-head feature CI runs had already passed.
