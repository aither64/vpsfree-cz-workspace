# Final review: delivery checkpoints

Requested outcome: independent progress checks that catch disproportionate scope
and excessive verification early, based on actual user requests/steering,
diffstats and working time. Acknowledge authorized CI fixes/user scope additions;
challenge excessive implementations. Reassess small docs/fixes after 30 working
minutes without delivery and simplify optional work autonomously. Existing idle
sessions stay idle. Full accepted scope is in plan.md and design.md here.

Read the shared workspace AGENTS.md and applicable project/session/documentation,
Git, lifecycle and verification procedures, plus each affected repository's
AGENTS.md. Read the mandatory-change-review skill and all four lane references:
general, architecture, scope/proportionality, risk/compatibility. Perform review
directly without subagents. Inspect scope/diffstats/time before detailed hardening.

Repositories (absolute prefix `/home/aither/workspace/ai/vpsfree.cz`):

- `worktrees/2026-10-26-delivery-checkpoints/dev-workspace`:
  base `120c7b9c4a55c63d168b0859099a6829505bbcdf`,
  head `f8b94441a6b5066973a72284955b793b301c60ac`.
  One commit, `progress: inspect scope and working time before delivery advice`.
  10 files, +583/-71 including tests/docs. Generic runtime owns evidence,
  scheduled policy compatibility and optional progress state.
- `worktrees/2026-10-26-delivery-checkpoints/workspace`:
  base `32c42e3edf4925acf48628b29fff8852720feb45`,
  head `f34fec1303139dd91a8faeaba97f6c2dce775276`.
  Two commits: `098324dbe` site policy and `f34fec130` runtime selection.
  Policy is 4 files, +52/-9; pin is two files, +5/-5. Default branch's initial
  tracking commit is excluded. Site catalog supplies observer/lead/review policy;
  shared AGENTS instructions also cover retained leads/reviewers.

Inventory: no obsolete branch iterations or migrations. No new behavior merged,
released, deployed or externally consumed. One dependency update stream selects
runtime f8b94441; no repeated pin updates. Preserve previous deployed stock
observer compatibility. Runtime behavior/tests/docs are one logical change;
site policy and mechanical pin are separate reviewable commits.

High classification due to persisted optional state and scheduled instruction
compatibility; advice cannot mutate source, cancel tests or waive approvals.
Local operator is trusted to administer the host (runtime AGENTS boundary).
Preserve wrong-session validation, idle scheduling, pending send identity and
owned-turn timeout. Fields remain optional schema 1; earlier observer packages
read/drop new fields and retain earlier resolution semantics. Supported rollout
is forward; package switching remains untouched.

Use existing activity counters with explicit incomplete coverage and per-member
values, never a new timing service or sum of overlapping clocks. No universal
diff line limit. Existing ordinary Git comparisons provide stats; source paths
allow read-only inspection. Exact original stock observer text gets a scheduled
turn policy update; custom saved instructions/model/effort/access are retained.
Do not create a general roster migration, custom verification framework, new
approval gate or broad refactor. No configuration/host activation in this patch.

Quick checks passed in the runtime Nix shell:
`go test -mod=readonly ./internal/progressobserver ./internal/repository
./internal/web -run TestProgress -count=1` (all three packages, including idle,
manual settings and browser presentation tests). Concern/evidence tests repeated
after the final concern-key fix. Workspace Nix parse and strict catalog eval,
and Git whitespace checks passed. No declared hook framework. One composed
package build follows review; no long test suite reruns before review.

Docs: runtime `docs/dev-sessions.md`; site `AGENTS.md`,
`docs/agent-teams.md`, `docs/agent-instructions/verification.md`. Runtime selection
preserves the extension SHA/hash and other inputs. Deployment needs matching
configuration runtime channel per the existing deployment procedure; not yet done.

Reviewer selection: unmanaged initiative, no valid managed lead thread/roster.
Installed default development team delegated's review-purpose role resolves to
gpt-6.1-sol/xhigh; use exactly this in a fresh standalone thread. Do not change
session teams. Write the final report only to this initiative's review.md. Include
explicit whole-branch history, migration and repeated-update conclusions.
