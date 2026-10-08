---
lifecycle: active
---

# Remove software pins from confctl

## Status

Current phase: ready, awaiting merge approval. Implementation, independent
review and local verification are complete. The clean five-commit feature
branch is published at
`cc40679d267165aecfa569128438bb55fe910268`.

Full local RSpec passed (66 examples), as did syntax, formatting, 95-file lint,
114-option documentation generation and stable rendering, package/check builds,
help and disposable custom/example/init/add smoke checks. Final-head CI passed
on Ruby 3.3, 3.4 and 4.0 (66/0 each) and RuboCop (95 files, no offenses).

Local VM results: auto_rollback passed 3/3 and carrier/deploy passed 8/8 at the
patch-equivalent predecessor `3be154b5`. Deploy/flakes passed 23/23 at the final
head. Carrier/netboot passed 8/8 at the final head, including both PXE boots and
kexec generation-selection paths. The retry wrapper and script exited 0 after
2317s; no owned local verification operation remains. Remote integration CI
remains queued, without runner availability evidence.

No review findings remain open. Default-branch integration, release and live
deployment are unauthorized. The session remains active and open.

## Phase checklist

- [x] Verify binding, retained roster, guidance and dedicated worktree.
- [x] Architect walkthrough/design and initial coordination commit.
- [x] Implement the accepted scope after the user's “proceed”.
- [x] Apply the lead's direct prose pass and regenerate references.
- [x] Pass quick checks, commit five units and inventory complete history.
- [x] Independent final all-four-lane review and migration/history assessment.
- [x] Fix, inspect and test two Important and one Advisory findings.
- [x] Fold corrections into owning units; no obsolete/fixup history remains.
- [x] Package/check builds and disposable cluster smoke checks.
- [x] Diagnose first integration failures; correct only two fixture lock URLs.
- [x] Scoped independent committed revision review; tracking advisory corrected.
- [x] Publish final head over SSH with exact lease; final Ruby/lint CI passed.
- [x] Complete both retries; all four local integration suites passed.
- [x] Reconcile remote CI: Ruby/lint pass; VM job remains queued.
- [x] Record locally verified branch readiness.
- [x] Commit consolidated coordination checkpoint.
- [ ] Integrate confctl into master only on explicit repository/target direction.

## Next action

The user may explicitly direct integration of confctl into master. Before that
action, fetch and preserve the reviewed patch under the Git procedure. Remote
Tests run 37766013754 is still queued; its eventual result remains to be recorded.
Keep the feature branch, worktree and session open; no merge or rollout is implied.

Detailed evidence: [verification.md](verification.md),
[review-report.md](review-report.md), [branch-inventory.md](branch-inventory.md),
[scoped review packet](review-fixture-revision.md).

Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-08-remove-software-pins-support/

## Repository and ownership

- Workspace: `/home/aither/workspace/ai/vpsfree.cz`; `dev-session current`, both
  root environment markers and the trusted thread binding agree on this slug.
- Worktree: `worktrees/2026-10-08-remove-software-pins-support/confctl`.
- Branch: `2026-10-08-remove-software-pins-support`; target `origin/master`.
- Initial/fetched base: `1b56616eff41e760327f3a0dbed8875e4aa9dbec`, tagged v3.0.0.
- Final head: `cc40679d267165aecfa569128438bb55fe910268`.
- Final tree: `08f33e1fe5613f7634ba69b38535fb3c35a3c0c9`.
- Final diff: 126 files, +1896/-6991, net removal 5,095 lines. Five coherent units;
  see complete SHAs, rationale and provenance in the branch inventory.
- Architect0: retained gpt-6-astra/xhigh/workspace_write, design owner.
- Implementer0: retained gpt-6.1-sol/xhigh/workspace_write, application owner.
- Reviewer0: retained gpt-6.1-sol/xhigh/read_only, independent review owner.
- Lead: coordination, evidence reconciliation and direct user-facing prose pass.

The accepted [plan](plan.md) and architect's [design brief](design.md) cover the
repository inventory, compatibility, acceptance criteria and verification.
Initial tracking commit `e0a5757e` preceded application commits. The consolidated
material checkpoint records this verification phase; unrelated shared-master
files/index are preserved.

## Review and history

Overall risk is high: intentional removed APIs, persisted generation selection,
retention and rollback. Reviewer0 used its retained saved settings with no
fallback or overrides, thread `01a11a64-d84f-7bf0-a54b-c4727b0527f8`.

Independent final review at `18d8b486` covered all four lanes and the complete
five-unit branch. Two Important findings required actual current-target
validation and stable owned option-declaration labels. An Advisory corrected the
optional init channel delimiter. The lead inspected and tested all three narrow
fixes under mandatory-review steps 8–9; fixes were folded into their owners.
Full corrected RSpec was 66/0, focused tests 27/0, and regenerated declarations
were stable across source hashes and repeated rendering.

The later two-line fixture correction received scoped general-lane review at
`cc40679d`. No Blocking/Important or source findings. Its tracking-provenance
Advisory was corrected. The reviewer independently reproduced final diffs and
range-diff, concluded that unchanged lanes need no reopening, and confirmed
coherent history with no obsolete approaches or unused compatibility paths.
**No migrations:** no database/state conversion, new schema or generation version.

## Integration failure and correction provenance

The first full local batch at `3be154b5` exited 1 after 2331.48s. Auto rollback
and carrier deployment passed. Netboot and deploy/flakes failed before assertions
when bare `nix flake lock` discovered `git+file:///tmp` before fixture Git init.
Those same commands existed at the v3 baseline. Original logs/statuses remain in
`local-integration.*` and `/tmp/confctl-integration-3be154b5.BL3GKB`.

Exactly two commands now lock `path:#{conf_dir}` in carrier/netboot and deploy
base. Placement, copied-lock handling, subsequent Git setup and all assertions
are unchanged. Member formatting/extracted Ruby syntax and parent full RSpec
66/0 plus 95-file lint passed. Active hooks passed; the two lines were folded
into fixture unit 3. Units 1/2 have identical SHAs; units 4/5 retain their patches.

The fresh `fixture_retry_watcher` (gpt-6-luna/low, one operation) owned the exact
failed selectors, previewed before launch, with process-start logs and disposable
state `/tmp/confctl-integration-cc40679d.ZaCvwd`. Deploy/flakes passed 23/23 and carrier/netboot passed 8/8. Parent inspected both
terminal suite logs, successful runner summary, wrapper/script exit 0 and empty
source-status artifact. NixOS and vpsAdminOS PXE plus latest/selected kexec paths
all passed. Retry runner took 2290.03s (wrapper 2317s).
No unexpected local kernel compilation has been observed. No generic timeout or
operation cancellation was introduced.

## Publication and CI

The prior `3be154b5` feature was published; external consumption is unknown.
The final two-line delta changes no API, schema or state behavior. Exact-lease
SSH publication of `cc40679d` succeeded against the recorded predecessor.
Only superseded queued Tests run 37757965480 was cancelled; terminal old runs
and all current-head runs were preserved.

Final-head runs: RSpec [37766013749](https://github.com/vpsfreecz/confctl/actions/runs/37766013749)
and RuboCop [37766013747](https://github.com/vpsfreecz/confctl/actions/runs/37766013747)
succeeded; Tests [37766013754](https://github.com/vpsfreecz/confctl/actions/runs/37766013754)
remains queued. Downloaded final logs confirm the Ruby counts and clean lint.
The runner-inventory API returned 403; this does not prove an offline runner.
Local coverage provides verification while remote scheduling is unresolved.

## Documentation and operational boundary

Implementation documentation is in confctl README, command/options manuals,
input/carrier guides, version-scoped v3 upgrade guidance and the renamed example.
The lead applied the writing skill after technical facts settled, then regenerated
manuals. Existing flake JSON, links and GC roots remain compatible with v3.
Unsupported records are diagnosed and left untouched; broken current cannot
silently substitute another generation or permit unsafe retention.

Operators must migrate legacy configs using retained v3 before upgrading and
update the tool/configuration confctl input together for moduleOptions. Production
configuration/API consumers and optional external netboot readers are not fully
inventoried; that work precedes a later authorized rollout. No all-node update,
production deployment, release, default merge or lifecycle action occurred.

Reusable environment and fixture lessons are in
[the confctl tooling note](../../notes/confctl/2026-10-08-sandboxed-member-checks.md).
Provisional failures and corrected verification assumptions are retained in the
verification record rather than relabelled as successful original runs.
