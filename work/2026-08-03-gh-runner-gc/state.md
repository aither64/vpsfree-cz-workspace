# 2026-08-03-gh-runner-gc

## Repositories

- `repos/vpsadminos-org-configuration.git`
  - inspected `origin/master` at `91f92d9`
  - no branch or worktree created
- `repos/vpsadminos.git`
  - branch: `2026-08-04-ci-store-churn`
  - base: `origin/staging` at `33e1608e0`
  - worktree: `worktrees/2026-08-03-gh-runner-gc/vpsadminos-ci-store-churn`
- `repos/vpsadmin.git`
  - branch: `2026-08-04-ci-store-churn`
  - original base: `origin/master` at `6fb60827f`
  - rebased base: `origin/master` at `d0efecb36`
  - worktree: `worktrees/2026-08-03-gh-runner-gc/vpsadmin-ci-store-churn`

### Uniform follow-up worktrees

All follow-up branches are named `2026-08-04-stable-test-source` and use
worktrees beneath `worktrees/2026-08-03-gh-runner-gc/`:

- vpsAdminOS: `vpsadminos-stable-test-source`, based on `staging`
  `9c52c991a`;
- vpsAdmin: `vpsadmin-stable-test-source`, based on `master` `1907e1990`;
- confctl: `confctl-stable-test-source`, based on `master` `9648e9f`;
- terraform-provider-vpsadmin:
  `terraform-provider-vpsadmin-stable-test-source`, based on `master`
  `ae1551a`;
- vpsf-status: `vpsf-status-stable-test-source`, based on `master` `9c19b23`;
- vpsfree-irc-bot: `vpsfree-irc-bot-stable-test-source`, based on `master`
  `af553fd`;
- web: `web-stable-test-source`, based on `master` `26e8584`.

## Status

### Uniform framework follow-up

The user rejected relying on vpsAdmin-specific workflow paths for source
stability and required review before any further default-branch integration.
Fresh branches named `2026-08-04-stable-test-source` have been created from
current defaults in isolated worktrees under
`worktrees/2026-08-03-gh-runner-gc/` for vpsAdminOS, vpsAdmin, confctl,
terraform-provider-vpsadmin, vpsf-status, vpsfree-irc-bot, and web. No
`vpsadmin-events` ref or worktree is in scope.

The implementation target is one immutable flake source per test-runner
command, propagated through test discovery and every configuration build. The
existing live-log placement under prepared state is retained, while the small
vpsAdmin selector files will return to their original locations. Shared action
references will use `@staging`; flake locks remain exact by design.

No project branch will be merged before user review. All review heads will be
pushed together after quick verification and the mandatory standalone review,
then every triggered workflow will be monitored to completion.

Two temporary empty `[skip ci]` guard tips were pushed only to make exact
dependency commits reachable for lock generation without starting long CI:
`829f845fe` in vpsAdminOS and `796adcbbf` in vpsAdmin. Consumers pin the
functional parents (`31b3dff43` and `3f9b68adb`), not the guards. Both guards
will be removed with lease-protected force-pushes before reviewed-head CI and
will not remain in final review history.

### Uniform framework implementation

vpsAdminOS (`origin/staging` `9c52c991a` -> functional head `31b3dff43`):

- `5365ec24a test-runner: pin repository source per invocation`
  - resolves one immutable flake source for each `ls`, `test`, or `debug`
    command and uses it for discovery and every per-test evaluation;
  - protects the source with a unique indirect GC root under the command state
    directory, locks live roots, removes abandoned roots safely, and cleans up
    in `ensure`;
  - maps relative and in-repository absolute test configuration paths into the
    snapshot while preserving external absolute path behavior;
  - adds Nix-backed RSpec coverage for source immutability, mutable `test.log`
    exclusion, GC-root lifetime, exception cleanup, abandoned-root cleanup,
    nested invocations, path mapping, and discovery/executor source identity.
- `fbe37909f tests: enforce NixOS disk image reuse`
  - extends the evaluation-only flake check so changed test names and changed
    machine names reuse an identical base image;
  - proves a real disk input change (`additionalSpace`) produces a distinct
    image while labels remain fixed;
  - runs the image-reuse check early in the main CI workflow and includes
    `flake.nix` in that workflow's path trigger.
- `31b3dff43 test-runner: harden repository source lifetime`
  - resolves and roots the snapshot through one `nix-build --out-link`
    operation, closing the temporary-root gap between two Nix processes;
  - serializes source-root reservation and scavenging with a shared registry
    mutex, publishes each entry lock while that mutex is held, and retains the
    entry lock for the invocation lifetime;
  - uses one per-user runtime registry across unique CI state directories so a
    later invocation can reclaim roots abandoned by `SIGKILL` or runner crash;
  - exports the frozen path as `TEST_RUNNER_REPO_ROOT` for the invocation so
    image-script VMs mount the snapshot rather than the mutable checkout;
  - builds the wrapper for the host platform, independently of a requested
    test-evaluation `--system`, preserving cross-evaluation behavior;
  - adds concurrent-invocation and real `Process.exit!` crash cleanup coverage.

Consumer commits:

- vpsAdmin: `893e53d0b` restores selector scratch to its original workflow
  paths and relies on the framework snapshot while retaining the live log in
  prepared state; `0f7d3b1f3` follows shared actions from `@staging`;
  `3f9b68adb` is the sole dependency commit and pins final vpsAdminOS head
  `31b3dff43`.
- confctl: `36d3780` follows shared actions from `@staging`; `b6d7245` is the
  sole dependency commit and pins `31b3dff43`.
- terraform-provider-vpsadmin: `f249b37` follows shared actions from
  `@staging`; `6e35529` is the sole dependency commit and pins vpsAdmin
  `3f9b68adb`, transitively vpsAdminOS `31b3dff43`.
- vpsf-status: `4bc0ab2` is the sole dependency commit and pins vpsAdmin
  `3f9b68adb`, transitively vpsAdminOS `31b3dff43`; its shared actions already
  used `@staging`; `e68cbaa` updates its security-advisory fixture for the
  required vpsAdmin content-revision contract found by reviewed-head CI.
- vpsfree-irc-bot: `c4f2341` follows shared actions from `@staging`;
  `d17a852` is the sole dependency commit and pins vpsAdmin `3f9b68adb`,
  transitively vpsAdminOS `31b3dff43`.
- web: `8603ad0` is the sole dependency commit and pins vpsAdmin `3f9b68adb`,
  transitively vpsAdminOS `31b3dff43`; its shared actions already used
  `@staging`.

No `vpsadmin-events` branch, ref, worktree, or file was modified.

### Uniform framework quick verification

- vpsAdminOS focused RSpec after the final source-lifetime change: 19
  examples, 0 failures.
- vpsAdminOS full test-runner RSpec after review fixes: 171 examples,
  0 failures. This includes concurrent live invocations and cleanup after a
  forked invocation uses `Process.exit!` to bypass `ensure`.
- vpsAdminOS RuboCop on all changed Ruby/spec files: no offenses.
- vpsAdminOS Nix image-reuse check built successfully at
  `/nix/store/nhb58azi0pckj2hk0zvbbprl74k2j5xx-nixos-test-disk-image-reuse`.
- vpsAdminOS `nixfmt --check`, actionlint, and full Overcommit hooks passed.
- vpsAdmin selector regression test: 16 runs, 55 assertions, passed.
- vpsAdmin actionlint and full Overcommit hooks passed after installing the
  repository API bundle in its documented Nix development shell.
- confctl actionlint and full Overcommit hooks passed.
- terraform-provider-vpsadmin and vpsfree-irc-bot actionlint passed;
  vpsfree-irc-bot bundled Overcommit hooks passed.
- vpsf-status Lefthook was installed and its pre-commit i18n check passed.
- Flake metadata resolves direct vpsAdminOS pins to `31b3dff43` and all
  transitive vpsAdmin pins to `3f9b68adb` / vpsAdminOS `31b3dff43`.
- Metadata-only `./test-runner.sh ls` smoke tests passed in vpsAdmin, confctl,
  terraform-provider-vpsadmin, vpsf-status, vpsfree-irc-bot, and web. No VM
  test was started. A live vpsAdmin evaluation exposed exactly one locked entry
  in `/run/user/1000/os-test-runner-repository-sources-1000`; the shared
  registry had no entry roots or locks after all commands completed.
- vpsAdminOS metadata evaluation listed all `image-scripts/test@*` cases while
  the immutable-source environment was active; no image or VM was built.
- No precise 40-character shared-action revision remains in any of the seven
  follow-up worktrees.

### Mandatory review of the uniform follow-up

The fresh-context reviewer initially reported three blocking findings and one
important finding:

- source resolution and GC-root attachment used separate Nix processes;
- an entry lock pathname was visible before its flock was held, allowing a
  concurrent scavenger to mistake it for stale;
- image-script tests read the original `TEST_RUNNER_REPO_ROOT` and exposed the
  mutable checkout to their VM;
- abandoned roots lived under unique CI state directories and could not be
  discovered by later invocations.

Commit `31b3dff43` addresses all four findings with one rooted Nix build, a
serialized shared registry, lifetime-held entry locks, a per-user runtime root
location, crash/concurrency regression coverage, and invocation-scoped export
of the frozen source. On follow-up, the reviewer confirmed those issues were
resolved and then found that the consumer history retained intermediate pin
commits and that the wrapper build had incorrectly followed the requested
test-evaluation `--system`. The histories were rewritten to contain one final
pin commit per consumer, and `31b3dff43` now uses the host platform for the
wrapper while leaving `--system` to test evaluation. Focused and full tests,
RuboCop, nixfmt, actionlint, Overcommit, flake metadata, the image-reuse check,
all six consumer `ls` smokes, and all image-script metadata enumeration passed
afterward. The same reviewer completed a final pass with no blocking,
important, or advisory findings and declared all seven functional heads ready
for reviewed-head CI. The remaining gaps are the intended GitHub workflows,
VM/integration behavior, concurrent runner/GC operation, and peak-store
measurement. No merge is authorized before user review.

### Reviewed-head publication and CI

After the final review, the temporary guard tips were removed locally and
lease-protected force-pushes changed the two existing remote review refs to the
reviewed functional heads. The other five review refs were created. Published
heads are:

- vpsAdminOS `31b3dff4306cce8904ac45630a931a7b72d36507`;
- vpsAdmin `3f9b68adb97b7f43df929a85fc172d9d11e15211`;
- confctl `b6d72453cbf94f94b9712575cf474ed077228189`;
- terraform-provider-vpsadmin
  `6e355293501278fe918007eeac9f1bb06b78c775`;
- vpsf-status `e68cbaaf75a6f4c9ee27fdddb07d42ef44cca338`;
- vpsfree-irc-bot `d17a8520766a5010cc826ce02b0c7a74a3d988d4`;
- web `8603ad09435350db1843d4710bb51272bf881324`.

confctl and vpsfree-irc-bot initially rejected ambient `git push` because the
pre-push hook used an Overcommit installation that did not accept the
development-shell signature. Both unchanged configurations were re-signed and
the pushes passed when `git push` ran inside each repository's Nix shell. The
reusable note was updated in
`notes/confctl/2026-08-04-overcommit-worktree-signature.md`.

Moving the guarded vpsAdminOS and vpsAdmin refs backward did not emit push
workflow runs. vpsAdminOS CI was therefore dispatched explicitly as run
`30917125042`. The many-hour vpsAdmin CI suite was not dispatched, per the
user's instruction. A fresh vpsAdmin API Specs workflow was dispatched as run
`30917010124` to replace the previously failed evidence. All exact-head runs
triggered by the other five pushes are being monitored to completion.

The fresh API Specs run passed all 26 topic shards. vpsf-status integration
run `30916922629` failed its seventh and final example after the first six
passed. The downloaded artifact showed a precise compatibility error:
`SecurityAdvisory#publish!` now requires `expected_content_revision:`, while
the vpsf-status security-advisory fixture still called it with only
`published_by:`. This was not a source-snapshot, image-reuse, runner, or GC
failure. Commit `e68cbaa` passes `advisory.content_revision`, matching current
vpsAdmin model and API specs. The metadata smoke, `git diff --check`, and
Lefthook pre-commit checks passed. The mandatory reviewer reported no blocking,
important, or advisory findings on the incremental commit. Replacement head
`e68cbaaf75a6f4c9ee27fdddb07d42ef44cca338` was pushed and Integration Tests
run `30920474166` passed, including the corrected seventh VM example.

The final exact-head workflow audit found ten runs, all completed successfully:

- vpsAdminOS CI `30917125042` (explicit dispatch because removing the guard
  tip did not emit a push run): build/cache population and full test suite;
- vpsAdmin API Specs `30917010124` (explicit dispatch): all 26 topic shards;
- confctl RuboCop `30916987486`, RSpec `30916985450`, and Tests `30916985408`;
- terraform-provider-vpsadmin Integration Tests `30916922990`;
- vpsf-status replacement Integration Tests `30920474166`;
- vpsfree-irc-bot RSpec `30916988440` and Integration Tests `30916983136`;
- web Integration Tests `30916917691`.

The many-hour vpsAdmin CI suite did not trigger from the guard removal and was
not dispatched, as requested. No project default branch was changed or merged.

Investigation complete. Implementation of the two confirmed vpsAdmin and
vpsAdminOS CI store-churn fixes is committed in isolated feature worktrees.
The existing `2026-06-15-vpsadmin-events` worktrees and branches are explicitly
out of scope and will not be changed by this initiative.

The vpsAdminOS branch is pushed at `9c52c991a`; vpsAdmin pins that exact
revision. Mandatory review and all follow-up quick checks are complete. The
vpsAdminOS CI run `30891197889` (attempt 2) passed on pushed head `9c52c991a`.
The user chose this as the long integration gate rather than waiting several
hours for the full vpsAdmin suite. vpsAdmin run `30891748611` was intentionally
cancelled after about 100 minutes to release its runner for that gate; all four
auxiliary vpsAdmin workflows passed. The vpsAdmin branch was subsequently
rebased onto current master and lease-protected force-pushed. Both repositories
are integrated with linear history: vpsAdminOS `staging` is at `9c52c991a` and
vpsAdmin `master` is at `1907e1990`.

## Implementation

### vpsadminos

- `d2b1555e1 tests: reuse identical NixOS disk images`
  - removes test and logical machine names from raw image derivation identity;
  - adds an evaluation-only flake check proving equivalent configurations
    share an image and different disk inputs remain distinct.
- `9c52c991a ci: keep test log outside flake source`
  - writes live suite logs beneath the prepared per-run state directory in
    both the main CI and changed-image workflows.

### vpsadmin

- `336347a19 ci: keep workflow scratch outside flake source`
  - writes changed-file selection under `RUNNER_TEMP`;
  - prepares test state before preview and stores selected tests and the live
    suite log beneath it;
  - keeps result evaluation, artifact upload, and cleanup on those paths.
- `1907e1990 flake: vpsadminos 0b102133b -> 9c52c991a`
  - generated by `tools/update_vpsadminos_flake.sh` and changes only
    `flake.lock`.

The reported temporary roots were legitimate and transient. A later
`nix-store --gc --print-roots` reported zero temporary roots. Nix 2.34.8 uses a
locked per-process temporary-root file and removes it as stale when it can take
an exclusive nonblocking lock, so stale unlocked files are not treated as live
roots.

Two persistent contributors were identified:

- system profile generations 28 through 44 remain GC roots because the runner
  invokes plain `nix-collect-garbage`, which does not prune profile generations;
- `root/channels-1-link` retains a legacy root channel environment even though
  the runner configuration and inspected vpsAdminOS workflows use flakes; it
  can be removed after confirming `nix-channel --list` is not operationally
  required;
- a completed vpsAdminOS build leaves `os/result/toplevel` in the persistent
  runner workspace, rooting the full most-recent vpsAdminOS closure until a
  later checkout removes it.

The August 2026 job hooks intentionally suppress the timer while a workflow job
is active. This prevents the previously observed live-build collection race,
but it also means a continuously busy runner can miss every timer opportunity.
The 75 percent threshold additionally leaves only 25 percent burst headroom for
one job.

The follow-up found that a single full vpsAdmin integration job can itself
create a legitimate live set close to or larger than a 500 GiB runner store:

- the vpsAdminOS NixOS test-machine builder includes the test name in the raw
  disk-image derivation and output filename, preventing tests with identical
  services configurations from reusing a base image;
- a representative services image occupies approximately 3.3--3.9 GiB of
  physical store space locally;
- full vpsAdmin CI currently runs 118 tests, so services images alone project
  to approximately 390--460 GiB before other closures, DNS images, and runtime
  writable copies;
- every per-test `config.json` is a `nix-build --out-link`, so completed tests
  continue to root their image and referenced closure until workflow-level
  state cleanup;
- the workflow writes `changed-files.txt`, `selected-tests.txt`, and a live
  `test.log` inside the checked-out flake. The test framework evaluates the
  repository repeatedly using a path-valued `builtins.getFlake`. The vpsAdmin
  source filter does not exclude those files, so the growing `test.log` changes
  the flake/source snapshot while the suite is running. A canceled-run artifact
  showed 14 distinct `vpsadmin-source-unknown` derivations among 19 started
  tests, causing dependent packages, system closures, and images to churn too;
- the same artifact showed 19 distinct disk-image derivations and 23,301
  `copying path ... to local` operations after only 19 tests had started.

The events branch is the workload trigger rather than the only affected code
path. Its workflow, flake lock, and test-runner wrapper currently match master,
but history rewrites and changes matching full-selection rules repeatedly
launched the complete suite. From 2026-07-29 through the follow-up inspection,
the branch started 42 CI runs: 30 canceled, 6 failed, 5 succeeded, and 1 was
still active. Assigned canceled runs inspected from August 2--3 all uploaded
their logs and successfully removed their unique test-state directories, so
leaked `/tmp` state is not the primary cause.

Live host evidence supplied by the user agreed with this classification:
`/tmp` used only about 6.2 GiB while the shared filesystem containing
`/nix/store` used about 550 GiB. This rules out writable VM copies as the main
retained space and points to the store-resident raw image outputs and their
closures.

## Commands run

- created clean `2026-08-04-stable-test-source` feature worktrees for all
  seven affected repositories from their current default branches
- repaired confctl's worktree-local Overcommit signature after its
  post-checkout hook rejected the newly created worktree

- `bin/dev-session current`
- `git status --short --branch`
- fetched `vpsadminos-org-configuration` and `vpsadminos`
- inspected runner configuration, job hook scripts, GC script, tests, and
  runner-related history
- evaluated nixpkgs `6d65bfc1...#nix.version` (`2.34.8`)
- inspected upstream Nix tag `2.34.8`, especially `src/libstore/gc.cc` and
  `src/libstore/unix/pathlocks.cc`
- inspected vpsAdminOS workflows, `os/Makefile`, and `test-runner.sh`
- attempted read-only SSH to `root@gh-runner1.int.vpsadminos.org`; rejected by
  host authentication, so live evidence was supplied by the user
- compared vpsAdmin events and master CI workflows, flake inputs, test files,
  and branch history
- queried vpsAdmin GitHub Actions runs, jobs, step outcomes, runner names, and
  logs with `gh`
- downloaded and inspected a canceled vpsAdmin integration log artifact
- inspected vpsAdminOS NixOS image construction, Nix evaluation, per-test
  output links, disk preparation, and workflow state cleanup
- measured representative local NixOS services images with `du`
- created isolated `2026-08-04-ci-store-churn` branches from freshly fetched
  `vpsadminos/staging` and `vpsadmin/master`
- `nix build .#checks.x86_64-linux.nixos-disk-image-reuse --no-link
  --print-out-paths` (passed twice, including after formatting)
- `nix flake check --no-build --show-trace` (blocked by the pre-existing
  `overlays.all` list output, before reaching project checks)
- `nix develop --command nixfmt --check tests/make-test.nix
  tests/nixos-disk-image-reuse-check.nix flake.nix` (passed after formatting)
- `nix shell nixpkgs#actionlint -c actionlint .github/workflows/ci.yml`
  in both repositories (passed)
- `ruby tests/ci-selection-test.rb` in vpsAdmin (16 runs, 55 assertions,
  passed)
- vpsAdminOS `nix develop --command overcommit --run` (passed)
- vpsAdmin `nix develop --command overcommit --run` (passed after verifying
  and re-signing the unchanged custom API i18n hook and installing the API
  bundle in `nix develop .#api`)
- `./test-runner.sh ls services-up` in vpsAdmin with the feature pin (passed)
- pushed both feature branches to their SSH remotes
- started vpsAdmin CI run `30891748611` on `gh-runner2.int.vpsadminos.org`
- requeued vpsAdminOS CI run `30891197889` after review; its quick RSpec and
  changed-image workflows passed on the same head
- attempted read-only SSH disk sampling on all three runners as the ambient
  user; authentication was rejected, so peak usage cannot be sampled directly
  from this session
- cancelled vpsAdmin CI run `30891748611` at the user's direction after its
  partial logs were uploaded and test state was cleaned up successfully
- downloaded and inspected partial vpsAdmin artifact
  `vpsadmin-test-logs-30891748611`

## Integration evidence

The intentionally cancelled vpsAdmin run provided a useful apples-to-apples
churn sample. Forty tests started and 36 produced results before cancellation.
Their logs referenced exactly one `vpsadmin-source-unknown` derivation and seven
distinct `nixos-test-disk-image` derivations, compared with 14 source
derivations and 19 disk-image derivations after only 19 started tests in the
pre-fix artifact. `copying path ... to local` activity also fell from 23,301
operations in the 19-test pre-fix sample to 9,005 operations in the 40-test
post-fix sample.

One partial-suite test failed before cancellation:
`storage/restore-remote-interrupted-recv`. Its node-102 pool-create transaction
remained unsigned, unstarted, and queued for 15 minutes while the corresponding
node-101 transaction completed. No service failure or Nix store/build error was
reported. This is a runtime node-readiness/transaction-delivery failure outside
the source/image churn changes; the user explicitly chose not to wait for or
use the full vpsAdmin suite as an integration gate.

vpsAdminOS CI run `30891197889` attempt 2 passed. Its toplevel build, binary
cache copy, profile-generation update, full test suite, result evaluation, and
test-state cleanup all completed successfully on reviewed head `9c52c991a`.

Before integration, vpsAdmin `master` advanced to `d0efecb36` with the
independent `packages: update gem dependencies` commit. The feature branch was
rebased without conflict. Its commits are now:

- `336347a19 ci: keep workflow scratch outside flake source`
- `1907e1990 flake: vpsadminos 0b102133b -> 9c52c991a`

The full vpsAdmin Overcommit suite, flake-pin metadata check, test-runner list
smoke test, actionlint, and `git diff --check` all passed after the rebase.

## Integration

- fast-forwarded vpsAdminOS `staging` from `33e1608e0` to `9c52c991a` in a
  fresh target-branch worktree and pushed it to `origin/staging`;
- fast-forwarded vpsAdmin `master` from `d0efecb36` to `1907e1990` in a fresh
  target-branch worktree and pushed it to `origin/master`;
- retained both local and remote `2026-08-04-ci-store-churn` feature branches;
- cancelled redundant feature-branch workflow copies after the identical head
  was pushed to master. Master workflows may continue independently and are not
  part of the user-selected integration gate;
- cancelled the duplicate vpsAdminOS staging CI and RSpec runs because the same
  commit's feature-branch runs had already passed; the staging changed-image
  workflow completed successfully before cancellation;
- vpsAdmin master Client Specs, libnodectld Specs, WebUI PHPUnit, and i18n
  health workflows passed on `1907e1990`. Master CI run `30904642236` continues
  independently and is not being awaited at the user's direction.

## Mandatory change review

The standalone fresh-context review found no blocking issues. It found one
important scope gap and one advisory regression-test weakness:

- vpsAdminOS `image-scripts.yml` still wrote `test.log` in the checkout;
- the negative image-reuse case changed its labels as well as its disk input.

Both findings were fixed and folded into their owning commits. The image
workflow now uses prepared state, and the negative check holds test/machine
labels constant while changing only `additionalSpace`. The vpsAdminOS branch
was force-pushed with rewritten unmerged history, the old generated vpsAdmin
pin commit was dropped, and one replacement pin commit was generated for the
new exact head. Targeted image evaluation, actionlint, hook checks, and the
vpsAdmin metadata smoke test passed after these fixes. The same reviewer then
confirmed that no blocking, important, or advisory findings remained, that the
commit split was focused, and that the vpsAdmin pin matched the reviewed
vpsAdminOS head exactly. The only remaining validation gap is the full workflow
run and its peak-store behavior.

## Results

Recommended durable changes in `vpsadminos-org-configuration`:

1. Have the root maintenance path prune profile generations with an explicit
   retention policy, initially `--delete-older-than 14d`.
2. In the completed-job hook, remove Nix-store output symlinks from the just
   completed workspace, release the coordination lock, and synchronously invoke
   the existing conditional GC helper as `github-runner`. The Nix daemon allows
   an unprivileged client to request ordinary liveness-respecting collection,
   so no sudo or other new privilege path is needed. Root remains responsible
   only for pruning the root/system profile generations.
3. Keep the periodic timer as a fallback, but make the completion boundary the
   primary collection opportunity so sustained queues cannot starve GC.
4. Replace or supplement the percentage threshold with measured minimum free
   space sufficient for the largest observed workflow burst. If a single live
   job can consume more than that headroom, enlarge the runner store; active
   temporary roots cannot safely be collected.

Recommended vpsAdmin/vpsAdminOS changes, in order:

1. Move `changed-files.txt`, `selected-tests.txt`, and especially the live
   `test.log` outside the repository/flake source, preferably under the prepared
   state directory, and point result evaluation and artifact upload at the new
   path. This should make every per-test evaluation use one stable source.
2. Stop including `testAttrs.name` in the NixOS base disk-image derivation and
   filename. Use a stable machine-role name; Nix will still distinguish images
   whose actual machine configurations differ. Add a test proving identical
   configurations share an image and different configurations do not.
3. Consider unlinking the per-test config output link once its machines have
   stopped and its logs/results are durable. This reduces live roots, although
   it does not reclaim space during a job while runner-wide GC remains
   intentionally deferred.
4. Measure a full run after fixes before deciding whether the runner disks still
   require enlargement. Limiting concurrency alone will not solve store growth
   because completed-test output links currently retain all earlier images.

One-time recovery should be performed as root at an idle boundary under the
existing coordination lock: prune generations according to the selected
retention, remove stale completed-job result symlinks, then collect garbage. Do
not remove temporary-root files manually.

## Open questions

- Select the rollback retention period. Fourteen days is the proposed initial
  value; capacity and deployment frequency may justify a different value.
- Measure the largest per-job increase in `/nix` usage and set an absolute free
  space reserve from that evidence.
- Decide whether generic runner-level output-link cleanup or explicit `always()`
  workflow cleanup is preferable. Runner-level cleanup covers every repository;
  workflow cleanup is narrower but easier to omit.
- Decide whether the stable repository snapshot belongs in the generic test
  runner or only in each workflow. Workflow scratch paths need fixing either
  way.
- Determine how many distinct vpsAdmin NixOS services configurations remain
  after removing the test name from the disk-image identity; this establishes
  the true post-fix peak-space requirement.

## Cleanup

- Removed the two implementation and two temporary integration worktrees after
  verifying that all four were clean.
- Retained the local and remote `2026-08-04-ci-store-churn` branch refs in both
  repositories. Their refs and the target-branch refs resolve to the same final
  heads.
- A temporary upstream Nix source checkout was made under `/tmp` for read-only
  source inspection; it is not part of the workspace.
