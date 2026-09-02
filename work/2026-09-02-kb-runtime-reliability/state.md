# 2026-09-02-kb-runtime-reliability

## Repositories

- `vpsadminos`
  - branch: `2026-09-02-kb-runtime-reliability`
  - worktree:
    `worktrees/2026-09-02-kb-runtime-reliability/vpsadminos`
  - base: `origin/staging`
  - base/head at creation: `f38b0018ee80bb2c36fb7940b4bcfd185f8e7194`
- `vpsfree-kb-contracts`
  - branch: `2026-09-02-kb-runtime-reliability`
  - worktree:
    `worktrees/2026-09-02-kb-runtime-reliability/vpsfree-kb-contracts`
  - base: `origin/master`
  - base/head at creation: `5dd94f1609ecb0742360d6b0b2b8fa99c190a519`

Both project remotes use `git@github.com:vpsfreecz/<project>.git`.

## Status

- Created the independent initiative from current default branches.
- Inspected the retry framework, managed-page runtime workflow, affected KB
  tests, and current Guix image build.
- Narrowed the initiative after the user decided against a Guix mirror/cache:
  implement only classified, visible retries for demonstrated failures. The
  workflow selector is also deferred so this stays a small reliability fix.
- The parent Codex process still has
  `VPSFREE_DEV_SESSION_SLUG=2026-08-18-vpsadmin-password-reset`; all work on
  this initiative therefore uses explicit paths and does not modify the old
  initiative. A separate tmux development session named
  `2026-09-02-kb-runtime-reliability` was created without starting another
  Codex process.
- Implemented and committed the vpsAdminOS classified retry primitive.
- Implemented and committed focused APT and Guix runtime-test retries in the KB
  contract repository, with a separate vpsAdminOS dependency-pin commit.
- Pushed the vpsAdminOS feature branch so the KB lock can pin its exact commit.
- Completed the mandatory standalone change review. Its blocking and important
  findings were addressed with terminal-error classification and focused
  classifier regression tests. Its advisory immediate-success test was also
  added to the framework spec.
- Rewrote and force-pushed the vpsAdminOS feature commit, canceled the
  superseded in-progress CI run, and rewrote the two local KB commits around
  the new framework revision.
- Quick verification and all focused VM integration tests are green. Both
  branches are pushed. vpsAdminOS CI and the KB repository-check workflow are
  green. The KB managed-page runtime workflow also passed its complete suite.

## Commands run

- `bin/dev-session start kb-runtime-reliability --new --no-attach --no-codex`
- `bin/dev-session ... add vpsadminos`
- `bin/dev-session ... add vpsfree-kb-contracts`
- fetched and verified project default branches and SSH remotes
- inspected vpsAdminOS `AGENTS.md`, `osvm`, test-runner retry helpers, driver
  tests, and `image-scripts/images/guix`
- inspected vpsfree-kb-contracts `AGENTS.md`, runtime workflow, flake inputs,
  KB page labels, and APT/Guix call sites
- reviewed official Guix and Cuirass documentation for channel mirrors,
  substitutes, `guix publish`, `guix copy`, signatures, and retained build
  roots
- inspected failed GitHub Actions artifacts from runs `33549880278` and
  `32656346842`, and successful timing from run `33511869919`
- `nix develop .#test-runner --command env TMPDIR=/tmp bundle exec rspec
  -Itest-runner/spec test-runner/spec/test_runner/test_evaluator_spec.rb`
- `nix develop .#vpsadminos --command bundle exec rubocop ...`
- `nix develop .#vpsadminos --command bundle exec overcommit --run`
- `nix develop --command bin/check --allow-missing`
- `nix run .#test-runner -- ls --filter 'tag=kb-runtime &&
  (kbPage=firewall || kbPage=guix)'`
- `ruby tools/test-runtime-retry-classifier.rb`
- `nix develop .#vpsadminos --command nixfmt --check ...`
- `./test-runner.sh test --state-dir=/tmp/vpsfree-kb-runtime-reliability-firewall
  --status-interval=60 --verbose 'kb/firewall#{iptables,nftables,ufw}'`
- `./test-runner.sh test --state-dir=/tmp/vpsfree-kb-runtime-reliability-guix
  --status-interval=60 --verbose 'kb/guix#reconfigure'`

## Results

- Commands inside a guest container do not require distributing a helper into
  the container. A framework retry can re-run the complete host-side
  `osctl ct exec ...` command.
- `wait_until_succeeds` is inappropriate for package installs and multi-hour
  Guix operations because it polls every second and treats every non-zero exit
  as retryable.
- `succeeds_with_retries` is a useful base but currently retries all non-zero
  exits with a fixed delay and has no classification or recovered-flake
  reporting.
- The existing KB Guix helper retries only two `CommandFailed` Git messages. It
  does not classify timeouts, DNS/substitute failures, or Software Heritage
  fallback, and a blind expansion would hide real faults.
- The Guix image build resolves a channel revision with substitutes from
  `ci.guix.gnu.org`, runs `guix time-machine ... system init`, and copies the
  default channel configuration into the image. The image's later runtime
  operation can still need both the historical Git revision and store objects.
- A Guix substitute cache alone cannot fix a missing channel Git commit. The
  reliable design requires a retained Git mirror plus a signed substitute
  server.
- The user chose not to operate that infrastructure. The image builder already
  selects a channel revision with upstream substitutes; tests will retain that
  model and keep custom builds minimal.
- A successful current run completed Guix reconfiguration in about 18 minutes.
  The failed run spent the full two-hour command timeout waiting for Software
  Heritage vault cooking after the upstream Git checkout failed. A separately
  retried time-machine preparation command can fail over much earlier without
  blindly rerunning a long system build.
- Existing `kbPage` labels (`firewall`, `gre`, `guix`, `kvm`) allow selective
  tests, but workflow selection is deferred from this narrowed initiative.
- The older Guix failure in run `32656346842` ended with a substitute timing
  out after 3600 silent seconds and an explicit Guix networking-failure
  diagnostic. The long operation retry recognizes that terminal diagnostic,
  not an earlier DNS warning by itself.
- vpsAdminOS test-runner specs: 25 examples, 0 failures.
- vpsAdminOS RuboCop: the changed spec has no offenses.
- vpsAdminOS Overcommit: Nixfmt and RuboCop passed.
- KB `bin/check --allow-missing`: all syntax, contract, source, inventory, and
  Ruby/Node test suites passed.
- The new classifier suite has 10 tests and 14 assertions. It includes positive
  cases from the observed APT and Guix failures, plus mixed-output negatives in
  which a transient message precedes a terminal package, signature, or Guix
  configuration error.
- Guix preparation now uses an inner GNU `timeout`, so the retried exception
  carries status 124 and the last command-output lines. An SWH fallback timeout
  is retried only when its progress message is at the end of that output.
- The three APT-using firewall scripts (`iptables`, `nftables`, and `ufw`)
  passed together in 685.1 seconds. The DNF-based firewalld and NixOS scripts
  do not use the changed helper and were not rerun.
- The complete Guix script passed all five examples in 2479.1 seconds. Its
  first time-machine preparation succeeded on the first attempt in 1509.8
  seconds, authenticated the pinned channel, and used
  `bordeaux.guix.gnu.org` substitutes. It did not enter Software Heritage
  fallback. Reconfiguration took 190.3 seconds, deployment took 250.6 seconds,
  and both restart checks passed.
- Neither focused VM run exercised a retry. This validates that successful
  commands remain quiet and un-delayed; retry classification is covered by the
  focused unit fixtures instead of requiring an induced external failure.
- The Guix preparation output included small time-machine-specific derivations
  alongside 646 substitute lookup/progress events. It did not require a local
  kernel build. This keeps the existing upstream-cache model and adds no Guix
  mirror or binary-cache infrastructure.
- vpsAdminOS GitHub Actions on `3e42c8b5b`:
  - RuboCop `33636566267`: success
  - RSpec `33636566311`: success
  - CI `33636566365`: success, including the complete test suite and both
    livepatch jobs
- The superseded vpsAdminOS CI run `33634444782` on `f5637250f` was canceled
  after the force-push; already-completed RuboCop and RSpec runs were retained.
- KB GitHub Actions on `2cdee8cf2`:
  - Check `33642947986`: success in 5 minutes 24 seconds
  - Managed page runtime `33642947968`: success in 30 minutes 34 seconds; all
    12 scripts across four tests passed
- The managed runtime log contained no `Retrying` entry. Firewall passed in
  584.5 seconds and Guix passed in 1774.0 seconds on the self-hosted runner,
  confirming the normal success path remains quiet while the complete suite is
  green.
- KB focused test listing evaluates the pinned framework and selects
  `kb/firewall#*` plus `kb/guix#reconfigure` as expected.
- The first direct RSpec invocation failed to find `spec_helper`; a second run
  from `test-runner/` then exposed the documented missing local
  `libosctl/native.so` prerequisite. Building the extension with the documented
  `.#test-runner` shell and using `-Itest-runner/spec` fixed the setup.
- A direct `git commit` correctly failed because the ambient shell lacked
  RuboCop. Re-running the commit inside `nix develop .#vpsadminos` executed all
  required hooks successfully; no hook was bypassed.

## Mandatory change review

The standalone reviewer reported:

- Blocking: the initial predicates searched the entire accumulated command
  output, so an early transient warning could mask a later permanent failure.
- Important: the predicates lacked focused positive, near-miss, and
  mixed-output regression fixtures.
- Advisory: the generic helper should prove that immediate success does not
  consult the classifier or delay and does not log or sleep.

All findings are resolved. A shared pure classifier now selects the terminal
APT or Guix error stanza before recognizing a retryable cause. The focused
suite covers observed positive failures and mixed terminal negatives, and the
framework spec covers the immediate-success path. The review found no
deployment, production-state, or security concern; the change is test-only and
keeps existing APIs compatible.

## Commits

- `vpsadminos`
  - base: `f38b0018ee80bb2c36fb7940b4bcfd185f8e7194`
  - head: `3e42c8b5bfbe8ade426a748ae9f5ecbf7dce12a5`
  - `3e42c8b5b` `test-runner: add classified operation retries`
- `vpsfree-kb-contracts`
  - base: `5dd94f1609ecb0742360d6b0b2b8fa99c190a519`
  - head: `2cdee8cf24cc3304efb326d2e54d7010c078fadc`
  - `0a87a53` `Pin vpsAdminOS classified retry support`
  - `2cdee8c` `tests/kb: retry transient upstream operations`

The KB dependency commit updates `flake.lock`, the contract's recorded
vpsAdminOS revision, and every vpsAdminOS reusable-action ref together. The
functional commit contains only the APT and Guix runtime-test behavior.

## Open questions

- None. The Guix preparation attempt timeout is 30 minutes. The focused run
  completed it in 25 minutes 10 seconds while authenticating 2,398 channel
  commits and using upstream substitutes. That remains bounded well below the
  failed Software Heritage fallback's old two-hour system-operation timeout;
  the managed CI run will also exercise it on the self-hosted runner.

## Cleanup

- Keep both feature worktrees until the initiative is merged or abandoned.
- Keep feature branches after merge unless the user explicitly requests branch
  deletion.
