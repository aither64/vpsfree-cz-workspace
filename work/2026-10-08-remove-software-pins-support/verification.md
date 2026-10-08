# Verification evidence

## Current result

The published final head is `cc40679d267165aecfa569128438bb55fe910268`.
Independent final all-lane review and direct verification of its three fixes
are complete. Scoped independent revision review of the two fixture lock
commands found no Blocking or Important issues. Full local RSpec (66/0),
95-file lint, stable 114-option documentation, package/check builds, help and
disposable custom/example/init/add smoke checks passed.

Local integration at predecessor `3be154b5` passed auto_rollback (3/3) and
carrier/deploy (8/8). Netboot and deploy/flakes failed before assertions at
pre-Git fixture locking. Exactly two explicit path arguments correct that
boundary; both corrected suites now passed at the final head (deploy/flakes 23/23;
carrier/netboot 8/8). Parent inspected terminal logs and exact status artifacts.
Final-head CI runs are RSpec 37766013749, RuboCop 37766013747 and Tests
37766013754. Final-head Ruby 3.3/3.4/4.0 matrix passed (66/0 each); lint passed (95 files,
no offenses). The superseded queued Tests run37757965480 is cancelled; current
Tests37766013754 remains queued without runner assignment.
No live deployment or default-branch integration occurred.

## Initial pre-review quick checks

| Check | Result | Evidence |
| --- | --- | --- |
| Full repository-shell RSpec | 58 examples, 0 failures; 23.24 seconds | rspec-final.log |
| Real root moduleOptions evaluation | 114 public options; all required representatives; no pin options | initial2-options.json, options-markup-final.log |
| Rake confctl-options | exit 0, useful nonempty generated reference | options-markup-final.log |
| Rake md2man:man | exit 0, no raw_html warnings after literal markup fix | man-markup-final.log |
| Final base-to-head whitespace | clean | parent git diff --check |
| Ruby/runner/netboot and extracted fixture syntax | 87 files plus extracted fixture passed | implementer report |
| Ruby lint | 94 files, no offenses | implementer report, commit hooks |
| Nix formatting | 27 changed files passed | implementer report, commit hooks |
| Source audit | no supported pin/backend/prefetch/example-flake APIs remain | implementer tracked-tree audit |
| All five commits' hooks | pre-commit and commit-msg passed | implementer report |

Provisional failures were not accepted as passing evidence: initial option
extraction fragment (fixed), one incorrectly launched empty RSpec capture
(incomplete), and initial RSpec factory double/mock-lifetime setup failures
(fixed before full pass). See state.md and the sandbox/tooling note.

## Post-review verification

Narrow remediation quick checks are complete: full RSpec66/0 (22.96s), focused
27/0, changed Ruby lint/syntax, actual optional init block parser, all114 real
owned declaration paths, identical repeated reference rendering and clean diff.
Logs: rspec-remediation.log, options-remediation.log, man-remediation.log,
options-remediation-repeat.log; remediation-source.sha256 records source freeze.

Completed: package/Nix RSpec builds, packaged help, custom/raw/precedence smoke,
renamed-example/init/add smoke, lock preservation and exact-head publication.
CI Ruby matrix and lint passed.

Remaining: remote integration CI scheduling/result and explicit merge direction.
Local four-suite coverage is complete. No additional local checks are indicated.

Unfinished operations remain prospective. Production migration and third-party
netboot consumer inventory remain outside this implementation and must precede
a later authorized rollout. No live machine, release or default branch is changed.

## First monitored package/smoke batch

Exact3be154b5 package and Nix RSpec check builds passed (exit0), packaged help
passed, clean source/index. No unexpected local kernel build observed. Batch
failed only when the non-Git snapshot was passed to builtins.getFlake as a bare
absolute path: Nix attempted git+file:///tmp before source evaluation. The root
cause matches notes/cross-project/2026-10-06-explicit-path-for-exported-flakes.md.
Parent corrected only verification snapshot/fixture URLs to explicit path:;
application source remains unchanged. New watcher will run only the failed and
skipped smoke checks; successful build/help is not repeated. Initial logs/status
remain post-review-batch.*, package-build.*, flake-smoke.* and package-help.*.

## Disposable fixture correction

Smoke2 passed explicit-path source and custom output evaluation but actual CLI
relative-installable discovery failed in its non-Git configuration. Repository
fixture helpers create Git repositories; smoke3 does the same and stages source
plus generated lock files. No product source changed. Initial two failures are
retained as fixture failures, not application passes.

## Published-head CI

Exact feature head `3be154b5f86125146e444d5fb6aa60916e99b77d` was pushed
over SSH with the declared shell and active hooks. RuboCop run37757965407
and the full Ruby3.3/3.4/4.0 RSpec matrix run37757965524 succeeded with all
jobs/steps green. Integration Tests run37757965480 is queued. These are the exact-head runs to monitor, not a
moving branch query. No default-branch integration or deployment occurred.

## Final local smoke result

Custom/raw smoke at exact head `3be154b5` passed (flake-smoke3.exit=0):
actual `ls -L` custom metadata, raw flake=false paths, follows identity, later
channel/per-machine precedence, machine keys/input metadata, impure/lock-guard
arguments, conflicting-role grouping and actual import through computed `-I`
mappings. Repository and disposable locks stayed unchanged.

Renamed-example and real CLI init/add fixture commands also completed: machine
names/keys/build plans plus `ls`, `ls -L` and `inputs ls`; fixture lock checks
passed. The batch exited1 only on the parent-written final expected-name set:
it assumed all five skeletons were enabled, while example/cluster/cluster.nix
intentionally includes only the two NixOS entries. Parent inspected that source,
corrected the assertion to the two enabled names, and ran the assertions against
completed captures (passed). Initialized fixture contains nested/smoke as
expected. A direct tracked fixture source/lock diff was empty for both.
No Nix/CLI commands were repeated after their successful completion.

Evidence: flake-smoke3.log/.exit, example-init-smoke3.log/.exit and retained
fixture /tmp/confctl-flake-smoke.DzYDRO. Batch status1 and prior logs are kept;
the corrected assertion pass does not relabel the original batch status.
No application changes, live machines, profiles, roots or deployments occurred.

Fresh Luna/low ci_watcher now observes the three exact published-head run IDs.

Integration queue investigation: GitHub runner-inventory API returned403
(Resource not accessible by personal access token). This proves no runner
availability state; do not label the runner offline. Existing exact-head
workflow remains observed without relaunch or cancellation.

The exact integration run remained queued >10minutes with no runner assignment.
Parent selected local CI-tagged suite execution (same four selectors, jobs2,
explicit disposable state) rather than waiting solely on unavailable scheduling
evidence. GitHub workflow remains untouched; only the observation process stops.
Local KVM read/write access and sufficient available memory were verified.
Fresh watcher owns execution and unexpected-kernel escalation.

Completed exact-head CI artifacts inspected by the parent: RSpec final JSON
confirms all three Ruby matrix jobs succeeded (66/0 each); RuboCop final JSON
and log confirm success,95 files/no offenses. Tests final observation remained
queued, no failure logs available. CI watcher stopped only its observation
process on parent direction; no remote workflow was canceled. Fresh local
integration watcher owns local-integration.sh and its isolated state/logs.

Local integration failure investigation: carrier/netboot and deploy/flakes
initial `nix flake lock` run before fixture Git initialization, reproducing
bare-source /tmp discovery refusal. Parent inspected each failed suite log
and baseline: both have the same setup boundary. auto_rollback first example
passed and has no such exception in its own log; watcher combined attribution
was corrected. Remaining batch continues at frozen3be154b5. Implementer0 owns
a scoped explicit-path fixture proposal, no application evaluator change.

Local auto_rollback completed successfully: all3 VM examples passed,979.87s.
Carrier/deploy remains active; netboot and deploy/flakes failed before fixture
locking, not during deployment assertions. Their exact2-command explicit-path
fix proposal is accepted and source remains frozen until the batch returns.

## First local integration batch: completed

Exact3be154b5,2331.48s, runner and wrapper exit1. auto_rollback passed3/3
(979.87s); carrier/deploy passed8/8 (1737.64s). carrier/netboot failed364.6s
and deploy/flakes229.22s at the diagnosed initial bare lock. No kernel
compilation/cancellation; source-status empty and all owned processes exited.
Logs local-integration.log/.exit/.batch-exit; per-suite evidence in
/tmp/confctl-integration-3be154b5.BL3GKB. Source freeze released for the accepted
two explicit-path commands; no other runtime or fixture behavior changes.

Narrow fixture correction: exactly2files,+2/-2 inspected against3be154b5 and
source hashes. nixfmt/extracted Ruby syntax/whitespace passed; declared-shell
fullRSpec66/0,22.83s and95-file RuboCop0. Logs fixture-fix-rspec/rubocop.
Correction folds into the fixture unit before scoped final revision review
and failed-selector retry; no runtime or protocol changes.

Retry milestone at finalcc40679d: deploy/flakes completed23/23. Carrier/netboot
passed NixOS PXE example5/8 in573.98s within its600s limit and continued to
vpsAdminOS PXE. These observations do not yet establish overall batch success.

## Corrected integration retry: completed

Exact final head cc40679d, fresh utility gpt-6-luna/low, wrapper elapsed2317s.
Runner elapsed2290.03s; wrapper/script exit0. Parent inspected selection capture
(exactly carrier/netboot and deploy/flakes), empty source-status, successful
runner summary and terminal suite logs. Deploy/flakes passed23/23 in1245.46s;
carrier/netboot passed8/8 in2290.0s. Both NixOS/vpsAdminOS PXE and latest/selected
kexec paths passed. No owned run remains and no unexpected kernel compilation
or cancellation occurred. Evidence: fixture-integration-retry.* and
/tmp/confctl-integration-cc40679d.ZaCvwd.

All four local suites are green, using unchanged predecessor coverage for
rollback/carrier deployment and final-head retries for the two corrected files.
No passing suite was needlessly repeated. Final source/index is clean, head,
tree and published ref agree, and base-to-head whitespace remains clean.

Remote Tests37766013754 remains queued at final inspection, no runner assigned.
This is incomplete automated scheduling evidence, not a test failure or a green
CI claim. Ruby matrix/lint CI succeeded at the exact final head. The branch is
locally verified and ready, awaiting explicit confctl/master merge approval.
No production rollout, integration, release or session lifecycle action occurred.
