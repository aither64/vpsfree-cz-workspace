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
- Historical: the first KB-only implementation was reviewed, pushed, and
  validated in CI. Those commits were subsequently superseded when the user
  expanded the change to all workspace consumers.
- Current: packaged the classifiers in test-runner, migrated all direct
  vpsAdminOS and KB consumers, and rewrote the branches into five focused
  commits: framework, vpsAdminOS APT consumers, KB pin, KB APT, and KB Guix.
- Current: after review feedback from the user, introduced the shared
  `container_apt_get` evaluator API and rewrote both feature branches again.
  Those pre-APK heads were committed, locally verified, and pushed.
  Earlier VM and CI results are retained below as historical evidence only and
  do not validate the current heads.
- Completed the mandatory standalone review of the expanded series. Its three
  blocking findings were fixed before long tests: mixed APT diagnostics and a
  permanent Guix error after Software Heritage progress are now terminal, and
  the KB APT and Guix migrations are separate commits.
- Completed a second fresh standalone review after introducing
  `container_apt_get`. It found no blocking issue and one important policy
  duplication in the two opaque fixture wrappers. A shared
  `retry_apt_operation` now owns that policy for both `container_apt_get` and
  fixture execution.
- Rebased vpsAdminOS onto current `origin/staging` at `ee6d2f99d`; KB
  `origin/master` remains at `5dd94f160`.
- Current APK expansion: committed a conservative APK v2/v3 classifier and
  `container_apk`, removed the broad polling helpers, migrated every direct
  vpsAdminOS test operation, and split the stateful ZFS ACL scenario around
  its package installation. DNF/YUM and Portage remain unchanged after the
  cross-consumer investigation.
- Completed the fresh standalone mandatory review for the APK expansion. It
  found one blocking omission: APK v3 can report a truncated download as
  `Software caused connection abort`. The exact transport diagnostic and a
  positive classifier fixture were added and folded into the framework
  commit. The reviewer also found the tracking text incorrectly implied that
  the rewritten APK heads were already published; the publication status and
  ordering are corrected here. There were no other findings.
- Published the APK-expanded heads in dependency order: vpsAdminOS
  `6bdf458fd` first and vpsfree-kb-contracts `46466e8` second. GitHub reports
  the exact vpsAdminOS revision, timestamp, and NAR hash recorded by the KB
  lock. No superseded queued or active workflow remained to cancel.
- Final vpsAdminOS commits on `origin/staging` are `34a973fa8` (retry
  framework), `2101fd6a9` (APT consumers), `04fa96393` (APK framework), and
  `6bdf458fd` (APK consumers). Final KB commits on `origin/master` are
  `34d1a14` (pin), `18cb285` (APT), and `46466e8` (Guix).
- All focused verification, the three selected APK VM samples, and every
  current-head GitHub Actions workflow are green.

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
- `nix develop .#vpsadminos --command overcommit --run`
- `nix develop .#test-runner --command env TMPDIR=/tmp bundle exec rspec
  -Itest-runner/spec test-runner/spec/test_runner/{test_evaluator,retry_classifier}_spec.rb`
- `nix develop --override-input vpsadminos path:... --command bin/check
  --allow-missing`
- `nix run --override-input vpsadminos path:... .#test-runner -- ls --filter
  'tag=kb-runtime && (kbPage=firewall || kbPage=kvm || kbPage=guix)'`
- `nix develop .#test-runner --command env TMPDIR=/tmp bundle exec rspec
  -Itest-runner/spec test-runner/spec/test_runner/{retry_classifier,test_evaluator}_spec.rb`
- `nix develop .#vpsadminos --command bundle exec rubocop ...`
- `nix develop .#vpsadminos --command nixfmt --check ...`
- `bash -n tests/suite/zfs/ugidmap/{acl-ct,run}.sh`
- `nix develop .#test-runner --command bundle exec
  ./test-runner/bin/test-runner ls ...`
- `nix develop --override-input vpsadminos path:../vpsadminos --command
  bin/check --allow-missing`
- `./test-runner.sh test --state-dir=/tmp/vpsfree-kb-runtime-reliability-firewall
  --status-interval=60 --verbose 'kb/firewall#{iptables,nftables,ufw}'`
- `./test-runner.sh test --state-dir=/tmp/vpsfree-kb-runtime-reliability-guix
  --status-interval=60 --verbose 'kb/guix#reconfigure'`
- `nix flake metadata --json github:vpsfreecz/vpsadminos/6bdf458fd...`
- `nix develop --command bin/check --allow-missing`
- `nix develop .#test-runner --command bundle exec
  ./test-runner/bin/test-runner test ... 'docker/alpine#latest'`
- `nix develop .#test-runner --command bundle exec
  ./test-runner/bin/test-runner test ...
  'kernel/vpsadminos#cpu-view-cgroups-v2'`
- `nix develop .#test-runner --command bundle exec
  ./test-runner/bin/test-runner test ... 'zfs/ugidmap'`

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
### Historical first-cycle validation on superseded heads

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
### Current expanded-series validation

- Rechecked all direct test-framework consumers on fetched default branches.
  Only vpsAdminOS itself and vpsfree-kb-contracts contain direct APT or Guix
  operations. The other consumers require no changes.
- Expanded the test-runner commit to package the conservative APT and Guix
  classifiers and `container_apt_get`. The helper owns safe `osctl ct exec`
  command construction and native APT retries; `retry_apt_operation` owns
  classification, three attempts, progressive backoff, and logging. A separate
  vpsAdminOS consumer commit covers all direct APT update/install phases across
  nine scripts without repeating that policy.
- Rewrote the KB branch as an exact dependency-pin commit followed by separate
  APT and Guix commits. The APT change covers firewall fixtures plus the
  libvirt, storage, networking, and NFS KVM scripts without modifying
  executable documentation fixtures.
- The final vpsAdminOS focused RSpec run passed with 38 examples and no
  failures, including the two mixed-output cases reproduced by the reviewer
  and an additional non-APT terminal-output case.
  RuboCop passed for all changed framework Ruby files. Both vpsAdminOS commits
  ran the required Overcommit hooks successfully.
- KB `bin/check --allow-missing` passed with the local vpsAdminOS source
  override and again against the published GitHub revision. GitHub reports the
  same revision, timestamp, and NAR hash recorded in `flake.lock`.
- KB focused test listing evaluates the local framework and selects all 11
  firewall, Guix, and KVM scripts, including all eight changed KB scripts.
- Historical: pushed vpsAdminOS `5e285307d` and vpsfree-kb-contracts `6689a4e` with
  explicit force-with-lease checks against the superseded feature heads. No
  superseded queued or active workflow run remained to cancel.
- Those superseded vpsAdminOS RuboCop and RSpec workflows passed. Full vpsAdminOS
  CI and the KB managed runtime workflow are still pending; the KB Check
  workflow passed.
- A local all-consumer run selected all nine scripts. Its Incus/Debian script
  passed in 814.33 seconds without exercising a retry. The run was then stopped
  when the user requested the shared helper refactor; its result is therefore
  historical and the remaining scripts will be covered by CI.
- After the helper refactor, focused test-runner RSpec passed with 40 examples
  and no failures, full vpsAdminOS Overcommit passed, KB Nix parsing passed,
  and KB `bin/check --allow-missing` passed against the local vpsAdminOS
  worktree.
- Pushed final vpsAdminOS `5579f3259` and vpsfree-kb-contracts `808dddc` with
  explicit force-with-lease checks. The published vpsAdminOS revision,
  timestamp, and NAR hash exactly match the KB lock. Canceled superseded
  in-progress vpsAdminOS CI run `33662773651`; there were no other superseded
  active runs.
- The representative `podman/debian#latest` sample passed in 561.94 seconds.
  It exercised both helper-generated APT commands; neither required a retry.
- The representative `kb/firewall#iptables` sample passed in 492.56 seconds.
  It exercised packaged `container_apt_get` update/install commands and the
  byte-stable fixture through `retry_apt_operation`; neither required a retry.
- Current-head vpsAdminOS RuboCop run `33668693155`, RSpec run `33668693036`,
  and KB Check run `33668720785` passed. Full vpsAdminOS CI run `33668693031`
  and KB managed runtime run `33668720783` are still running.
- The APK investigation found ten direct command sites, all in vpsAdminOS.
  Existing `ct_apk_add` and module-autoload polling retried all command
  failures; commit `33e88a33dd` confirms they were introduced for observed
  transient Alpine DNS and timeout failures. `container_apk` now retries only
  recognized terminal transport diagnostics.
- DNF/YUM has direct consumers in vpsAdminOS and KB contracts, but DNF4 and
  DNF5 expose generic statuses and different diagnostics. The workspace also
  has a recorded permanent RPM scriptlet failure, so no speculative outer
  retry was added. Portage has no direct test-framework consumer and its image
  builder already uses native downloader and mirror fallback.
- APK-focused RSpec passed with 50 examples and no failures. RuboCop,
  Nix formatting, shell syntax, test discovery, and vpsAdminOS Overcommit
  passed. KB `bin/check --allow-missing` passed against the local final
  vpsAdminOS tree.
- After mandatory review, the APK-focused RSpec suite again passed with 50
  examples and no failures, including the exact APK v3
  `Software caused connection abort` fixture. Focused RuboCop and full
  Overcommit passed before the fix was folded into `04fa96393`.
- KB `bin/check --allow-missing` passed against the published vpsAdminOS
  revision after the final repin. All syntax, contract, source, inventory, and
  Ruby/Node suites passed.
- The three deliberately selected APK VM samples passed:
  `docker/alpine#latest` in 621.97 seconds,
  `kernel/vpsadminos#cpu-view-cgroups-v2` with all 141 examples in 1008.32
  seconds, and `zfs/ugidmap` in 372.58 seconds. None exercised a retry, which
  validates the quiet success path; classified recovery is covered by unit
  fixtures. No local kernel build occurred.
- All current-head workflows passed. vpsAdminOS RuboCop `33677205042` and
  RSpec `33677204991` passed. Full CI `33677204997` passed, including the OS
  build, both livepatch jobs, and the full test suite in 44 minutes 40
  seconds. KB Check `33677383030` and Managed page runtime `33677383115` also
  passed.
- The first framework commit attempt correctly failed because the ambient
  shell lacked RuboCop. Re-running the commit inside
  `nix develop .#vpsadminos` executed the required hooks successfully; no hook
  was bypassed.
- The first direct RSpec invocation failed to find `spec_helper`; a second run
  from `test-runner/` then exposed the documented missing local
  `libosctl/native.so` prerequisite. Building the extension with the documented
  `.#test-runner` shell and using `-Itest-runner/spec` fixed the setup.
- A direct `git commit` correctly failed because the ambient shell lacked
  RuboCop. Re-running the commit inside `nix develop .#vpsadminos` executed all
  required hooks successfully; no hook was bypassed.

## Mandatory change review

The earlier review and green CI apply to the superseded KB-only heads. A new
standalone review examined the current expanded five-commit series and found:

- Blocking: a permanent APT fetch error before a transient fetch error could
  still be retried.
- Blocking: Software Heritage progress before a permanent Guix diagnostic and
  timeout termination could still be retried.
- Blocking: the KB APT and Guix migrations had to be split into independently
  reviewable commits.
- Important: prior-cycle state and CI evidence had to be marked historical.

All findings are resolved. APT classification now requires every `E:` line to
be recognized and requires APT output to remain terminal. Software Heritage
classification permits only timeout termination after the final progress
state. The reproduced mixed cases are covered by specs, KB APT and Guix changes
are separate commits, and this state distinguishes historical validation from
current-head results. The reviewer found no deployment, persistent-state,
protocol, or security concern.

The fresh post-refactor review found no blocker and one important finding: the
two byte-stable KB fixture paths still repeated the APT attempts, backoff, and
classifier tuple. This is resolved by the framework's
`retry_apt_operation`; both fixture callers now use that wrapper. The review
confirmed complete direct-consumer coverage, shell-safe command construction,
pin integrity, unchanged fixture bytes, independent retry granularity, and no
deployment or compatibility concern.

The fresh APK-expansion review found one blocking classifier omission: APK v3
can report a truncated transport as `Software caused connection abort`. The
exact diagnostic and a positive fixture were added and folded into the APK
framework commit. Its important tracking finding was also resolved by
correcting the unpublished-head status and enforcing vpsAdminOS-first publish
ordering before validating the KB pin. It found no other blocking, important,
or advisory issue.

## Commits

- `vpsadminos`
  - base: `ee6d2f99d3c2ac51d4cbea54e1922808f345299d`
  - head: `6bdf458fd9105379860234ff33d352e55844f08f`
  - `34a973fa8` `test-runner: add classified upstream retries`
  - `2101fd6a9` `tests: retry transient APT setup failures`
  - `04fa96393` `test-runner: add classified APK retries`
  - `6bdf458fd` `tests: use classified APK retries`
- `vpsfree-kb-contracts`
  - base: `5dd94f1609ecb0742360d6b0b2b8fa99c190a519`
  - head: `46466e83c2293f47bfef3fe516a3b51c2de14c70`
  - `34d1a14` `Pin vpsAdminOS classified retry support`
  - `18cb285` `tests/kb: retry transient APT operations`
  - `46466e8` `tests/kb: retry transient Guix operations`

The KB dependency commit updates `flake.lock`, the contract's recorded
vpsAdminOS revision, and every vpsAdminOS reusable-action ref together. The APT
and Guix runtime-test behavior is split into separate commits.

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
