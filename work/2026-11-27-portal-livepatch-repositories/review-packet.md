# Final review packet

Historical packet supplied to the independent reviewer. Subsequent corrections,
affected review, approval and final revisions are recorded in review.md and state.md.

Review all four mandatory-change-review lanes: general, architecture, scope,
and risk. High risk classification: new private persisted selection state and
matched host/application rollout; no authentication or lifecycle protocol change.

User outcome: repair unusable Repository tab for the livepatch backport session,
with commits, changesets and file previews, then deploy aitherdev and merge the
three repositories after verification. plan.md, design.md, findings.md and state.md
in this directory retain scope and evidence. The existing 2019 Linux default
produced an 88,014-file diff; evidenced base gives 13 commits and 9 files.

Worktrees are /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-27-portal-livepatch-repositories/:

| Repository | Base | Final head |
| --- | --- | --- |
| dev-workspace | dc035883dbb666d6c958f95302e30c187f6e2d77 | fc29933b21b84f289d8da4d757b9573075e51e57 |
| workspace | 42372c8b82b0fe36379d5c6e6fefe9e41628e5c4 | d0dac2c14 |
| vpsfree-cz-configuration | 47fd816f118ab8e21a576c55026909188f2c3efb | d7ba2ab2831f48330847608443f68c6b02888554 |

Inspect complete base-to-head histories and diffs in each checkout. Runtime has
two commits: 7649c29f explicit base/CLI/persistence/errors/versioned selection,
and fc29933b independent visible history loading. Tests/docs are with their owning
behavior. Each consumer has one mechanical runtime pin; no repeated pin stream,
superseded implementation commit, migrations or released/deployed branch version.
A clean rebase over dc035883 preserved both patches by git range-diff. No migration
from abandoned state formats, manifest changes, lifecycle journal changes or
changes to Linux/vpsAdminOS source are intended.

Acceptance: exact ancestor base remains stable as branch advances, equal-head
empty range, invalid base explicit errors, existing frozen links untouched,
legacy capture retained, clear recovery, archive/revive and identity reuse safe,
healthy cards load without waiting for slow cards, unchanged errors do not loop,
manual refresh and changed-policy retry work, navigation cancellation preserved.
Limits and no-fetch remain unchanged. No new settings UI or global limit increase.
The trusted local operator remains trusted per dev-workspace AGENTS; remote clients
remain untrusted. Do not expand into hostile local filesystem hardening.

Provider/consumers: dev-workspace owns portal Git reader, private state and CLI;
its browser consumes additive comparisonVersion with old-server HEAD fallback.
Ruby invokes the Go bridge under existing session/worktree locks. Site extension
bf12ac71 remains unchanged. Workspace nested runtime and configuration devWorkspace
select fc29933b; bin/check-dev-workspace-deployment passes and lock diffs show only
that input. Configuration only selects the host contract; user profile owns app.

Quick checks passed: Ruby aggregate --name /review_base/ (2 runs, 30 assertions),
focused Go repository and web Test(Repository|Review|StatusObservation|CaptureComparison|ComparisonCapture),
JS/Ruby syntax and gofmt, git diff --check, targeted browser fixture (8.6s).
Final focused Go rerun follows patch-equivalent rebase and two extra regression
assertions for corrupt-state clear and historical capture. Longer package tests,
scoped host build and live-browser acceptance are still pending after this review.

Documentation inventory:
- review-base use/retention and capture semantics → operator how-to/reference →
  dev-workspace/docs/dev-sessions.md (README-linked) → CLI and Go tests.
- card loading, version compatibility/errors → portal user/developer reference →
  dev-workspace/docs/workspace-portal.md (README-linked) → browser and API tests.
- exact rollout/individual evidence → session plan/state and forthcoming rollout.md.
- unchanged reusable site operations → configuration docs/operations/{codex-providers-aitherdev,pi-runtime-aitherdev}.md,
  installed coordination guide and workspace docs/coordination.md.
The previously named workspace-coordination-aitherdev.md is absent from current
configuration; use the existing provider/Pi operational guides and installed
coordination instructions, with site machine-retention policy taking precedence.

No retained reviewer exists: CLI-created session has no valid native lead/roster.
Fallback catalog selected package /nix/store/6x5jdinwd03sacj5zg218q7ks1vxgavf-dev-workspace-0.2.0,
digest 4ae58b06cf34c345d952f2ce0288a78d739c5ee06584292062220a217e7f7922,
default delegated/reviewer purpose review, gpt-6.1-sol/xhigh, read_only.
Review directly, no nested agents. Return concrete severity/file/line findings,
whole-history/migration/repeated-stream conclusions and documentation placement
conclusion. Do not edit source or run long checks/deployment.

## Affected composition review after concurrent deployment

Final corrected runtime is 066691a37851742bbc47179c32b0077b0b0a016f
(two commits b3efe6f2 and 066691a3); review.md records the focused cache and
CI-contract corrections. CI 46027037518 passed at this exact head. Configuration
is 0a2ed34c91c7019e89d6d04195f9da31677b1fc4, one runtime pin on unchanged47fd816f.

A concurrent live profile now selects extension39470c642bace7a09d25194aea30100575c5efe2
through public workspace pin0daa1d840ee820e3dac30ddbb91744e9bee0ca3b. Preserve
that deployed registered-OS-worktree behavior while updating the runtime; the
original bf12 candidate would remove it. Prepared workspace range
db6ea35f2..56b9e263dffd4e2591be41be0a7b97af68b734da contains two distinct streams:
c9e7fa0e5 runtime pin (patch-equivalent to971302e7c over tracking-only master),
then56b9e263d extension pin (same delta as0daa1d840, adjacent runtime context
preserved). All other lock nodes are unchanged. Check final diff and deployment
compatibility, scope, whole-history/no-migration conclusion. No source edits to
the extension are part of this initiative. User approval to include that extra
pin in master is pending; do not treat review as approval.

Quick matching-contract and diff checks pass. Previous host and application
builds passed but the combined application needs one new composition build.
Re-use prior unaffected runtime review; assess affected General/Architecture/Scope/
Risk concerns for this combination, especially preserving active cluster inputs
and compatibility. Do not read other sessions' sensitive tracking. Current live
package is /nix/store/k5whrd72z2v242pfw8j5701g4vr8s0r7-dev-workspace-0.2.0.
