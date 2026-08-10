# 2026-08-07-vpsadminos-test-failures

## Repositories

- `vpsadminos`
  - branch: `2026-08-07-vpsadminos-test-failures`
  - worktree: `worktrees/2026-08-07-vpsadminos-test-failures/vpsadminos`
    (removed after merge)
  - base: `8d5fe0058f5f4db3840c7d8043c7aba3b88ccca4`
  - head: `ccd22b65fc4a1f69ca464825c20ea839d3dd1dea`
  - merged into `staging` by fast-forward at the same head
- `vpsadminos-org-configuration`
  - inspected read-only through canonical bare repository at `origin/master`
  - no branch or worktree created
- Consumer rollout target:
  `837baf04054c6ee0e71d288b8870ac42a6990c38` on vpsAdminOS `staging`
- Consumer branch: `2026-08-07-vpsadminos-test-failures` in every repository
- Consumer worktrees under
  `worktrees/2026-08-07-vpsadminos-test-failures/`:
  - `vpsadmin`: original base `63c2c44f6`, rebased onto `95f8d9ca7`, head
    `4b340a7240`, merged into `master` by fast-forward at the same head;
    post-merge CI passed and both worktrees were removed
  - `confctl`: base `b6d7245`, head `9eaa0ee73f`, merged into `master` by
    fast-forward at the same head; post-merge CI passed and both worktrees
    were removed
  - `terraform-provider-vpsadmin`: base `6e35529`, head `1275e4282e`, merged
    into `master` by fast-forward at the same head; post-merge CI passed and
    both worktrees were removed
  - `vpsf-status`: base `e68cbaa`, head `5739e1f226`, merged into `master` by
    fast-forward at the same head; post-merge CI passed and both worktrees
    were removed
  - `vpsfree-irc-bot`: base `d17a852`, head `b41dbafd81`, merged into
    `master` by fast-forward at the same head; post-merge CI passed and both
    worktrees were removed
  - `web`: base `8603ad0`, head `9c76351dfe`, merged into `master` by
    fast-forward at the same head; post-merge CI passed and both worktrees
    were removed
  - `vpsadmin-kb-captures`: base `fe07bdf`, head `f54352d56b`, merged into
    `master` by fast-forward at the same head; feature and merge worktrees
    removed

## Status

Implementation, mandatory review, integration testing, and the requested
default-branch merge are complete. The two focused commits are pushed to the
initiative branch and `staging` was fast-forwarded to the same head. The
mandatory standalone review found two blocking issues; both were fixed and
autosquashed.
Follow-up review found no remaining blocking, important, or advisory findings.
All feature-branch exact-head workflows passed. Post-merge RuboCop and RSpec
also passed; post-merge CI encountered a new Fedora 44 package-script failure
unrelated to these commits. No runner configuration change was made.

A follow-up rollout updated all lock-bearing workspace users
of the test framework from vpsAdminOS `31b3dff4306cce8904ac45630a931a7b72d36507`
to `837baf04054c6ee0e71d288b8870ac42a6990c38`. The latter contains the runner
fixes, the Fedora runtime-test mitigation, current Nixpkgs inputs, and packaged
gem updates. Downstream vpsAdmin application revisions remain unchanged.

All seven lock-only commits are published and fast-forwarded into their default
branches. Every GitHub workflow passed at the merged head, and all feature and
merge worktrees were removed while retaining the feature branches. The KB
capture repository has no GitHub workflow; its local static checks and
runtime-equivalent cluster closure build passed.

## Commands run

- inspected run, job, step, runner, and artifact metadata with `gh`
- downloaded and inspected artifact `os-test-logs-31210461594`
- inspected all failed machine console, shell, lifecycle, and test-runner logs
- compared successful full-suite runs of the identical commit
- inspected `test-runner` resource accounting and `osvm` QEMU lifecycle code
- inspected the GitHub runner NixOS configuration from
  `vpsadminos-org-configuration`
- queried historical Prometheus node metrics through the anonymous Grafana
  datasource proxy for `gh-runner2.int.vpsadminos.org`
- attempted read-only SSH and direct node-exporter access to runner2; both were
  unavailable from this session, so Prometheus supplied the host evidence
- fetched `vpsadminos` origin and confirmed `origin/staging` remains at the
  inspected head, so no rebase was required
- read the repository guidance and mandatory change review workflow
- implemented stable initial memory and `/dev/shm` capacity, cgroup-aware
  headroom, 8 GiB default reserves, capacity diagnostics, and oversized-test
  warnings
- implemented QEMU signal logging and synchronized PID/reaper cleanup
- built `libosctl/native` using the repository CI helper procedure after the
  first test-runner spec invocation could not load the extension
- ran the full OSVM spec suite in the `vpsadminos` Nix shell: initially 96 and
  finally 97 examples, 0 failures
- ran the full test-runner spec suite with the CI-required `TMPDIR=/tmp`:
  176 examples, 0 failures
- ran RuboCop on all changed Ruby files: 9 files, no offenses
- ran `nix develop .#vpsadminos --command overcommit --run`: all hooks passed
- pushed the feature branch over SSH and monitored all exact-head workflows
- inspected the retained full-suite log for resource limits, QEMU lifecycle
  failures, cleanup errors, and final test counts
- compared the protected runner3 duration with two earlier successful runner3
  runs of the same suite
- checked the public Prometheus target inventory; runner3 is not scraped, so
  host memory low-water metrics were unavailable for the integration run
- fetched `origin/staging`, created a fresh temporary merge worktree, and
  fast-forwarded `staging` from `8d5fe0058` to `ccd22b65f`
- ran `nix develop .#vpsadminos --command overcommit --run` in the merge
  worktree: all hooks passed
- fetched immediately before pushing and confirmed the remote target had not
  advanced, then pushed `staging` over SSH
- monitored all post-merge workflows and downloaded artifact
  `os-test-logs-31251769077` after the VM suite failed
- correlated every post-merge failure with Fedora 44's
  `udisks2-2.11.2-1.fc44` update transaction and verified normal QEMU exits
- removed the clean feature and temporary merge worktrees after verifying both
  remote refs; retained the downloaded artifact only under `/tmp`
- created isolated worktrees and the same-named feature branch for all seven
  lock-bearing test-framework consumers
- updated each lock from `31b3dff4306cce8904ac45630a931a7b72d36507` to
  `837baf04054c6ee0e71d288b8870ac42a6990c38`, preserving each indirect
  consumer's existing vpsAdmin revision
- verified every consumer commit changes only `flake.lock`, resolves the exact
  requested vpsAdminOS revision, and leaves its worktree clean
- installed or signed each declared hook framework and committed with all
  hooks passing; confctl and vpsfree-irc-bot pushes used their pinned Nix
  shells because ambient Overcommit rejected the worktree-local signature
- enumerated CI-tagged tests with the updated runner: 134 vpsAdmin entries, 5
  confctl, 2 vpsfree-irc-bot, and one each for the Terraform provider,
  vpsf-status, and web
- ran `nix develop -c bin/check` in vpsadmin-kb-captures: contract, annotation,
  inventory, and both test suites passed
- diagnosed a bare KB `cluster-config` build failure as an invalid diagnostic
  invocation: the source default intentionally contains no runtime CA, while
  `bin/devcluster` generates the CA and passes its ignored directory through
  impure evaluation; repeated the build with that supported runtime input and
  successfully built both the runner and complete cluster configuration
- pushed all seven feature branches over SSH and began monitoring every
  exact-head GitHub workflow in the six repositories that have CI
- detected that vpsadmin `master` advanced to `95f8d9ca7` while its initial
  feature CI was running, rebased the lock-only commit without conflict,
  refreshed the changed API bundle, reran all hooks and the 134-test
  enumeration, and force-pushed with a lease
- cancelled only superseded vpsadmin CI run `31320376221`, whose old head
  `e64c313401` no longer matched the published branch head
- fetched the KB capture default branch, fast-forwarded it in a fresh detached
  merge worktree, reran `nix develop -c bin/check`, fetched again, pushed
  `master` at `f54352d56b`, and removed both KB worktrees while retaining the
  feature branch

## Commits

- base: `8d5fe0058f5f4db3840c7d8043c7aba3b88ccca4`
- `a351e2172` — `test-runner: account for initial host memory use`
- `ccd22b65f` — `osvm: handle signaled qemu exits safely`
- consumer commits, all titled
  `flake: vpsadminos 31b3dff43 -> 837baf040`:
  - vpsadmin `4b340a7240` after rebase onto current `master`
  - confctl `9eaa0ee73f`
  - terraform-provider-vpsadmin `1275e4282e`
  - vpsf-status `5739e1f226`
  - vpsfree-irc-bot `b41dbafd81`
  - web `9c76351dfe`
  - vpsadmin-kb-captures `f54352d56b`

## Mandatory change review

The fresh standalone review reported two blocking findings:

1. The oversized-test warning interpolated `TestResources#to_s`, so it printed
   an object identity instead of requested resource values.
2. `signal_qemu` checked the PID under the lifecycle mutex but called
   `Process.kill` after releasing it, while the reaper called blocking `wait2`
   outside the mutex. That left a narrow PID-reuse race.

Both findings were fixed before integration testing. The warning now uses
`TestResources#summary` and its spec asserts the exact requested values. QEMU
reaping now polls `wait2(..., WNOHANG)` under the same mutex that protects
actual signal delivery; the reaper clears the PID before unlocking. A
deterministic concurrency spec holds the reaper inside `wait2`, queues a
signaler on the mutex, then verifies that no signal is sent after reaping.
Fixes were autosquashed into their owning commits. The final full spec suites
and Overcommit hooks pass. The same reviewer verified the rewritten head and
reported no remaining findings. The full VM CI run now also passes. Direct
cgroup-v1 headroom coverage remains a test gap; cgroup v2 is covered.

## Consumer rollout validation

All non-VM feature-branch workflows for the initial consumer heads passed.
The vpsadmin runs listed first were superseded by a required rebase and are no
longer validation for its current head:

- superseded vpsadmin Client Specs `31320376247`
- superseded vpsadmin Webui PHPUnit `31320376224`
- superseded vpsadmin i18n health `31320376236`
- superseded vpsadmin libnodectld Specs `31320376258`
- confctl RuboCop `31320392406`
- confctl RSpec `31320392398`
- vpsfree-irc-bot RSpec `31320391730`

Exact-head VM workflow IDs:

- vpsadmin CI `31326791937` at rebased head `4b340a7240`
- confctl Tests `31320392402`
- terraform-provider-vpsadmin Integration Tests `31320375797`
- vpsf-status Integration Tests `31320375811`
- vpsfree-irc-bot Integration Tests `31320391729`
- web Integration Tests `31320376385`

All feature VM runs passed. The initial vpsadmin CI run
`31320376221` was cancelled after `master` advanced and the lock commit was
rebased. Replacement CI run `31326791937` passed at `4b340a7240`. Fresh
RuboCop, API, client, WebUI, i18n, migration, and libnodectld workflows passed
at that exact head, including all API shards in run `31326791945`. The VM run
waited for shared-runner capacity, started at 17:54 UTC, and completed after
about 4 hours 26 minutes.

vpsadmin `master` was fast-forwarded to `4b340a7240` after a fresh fetch, a
full six-hook Overcommit run, and enumeration of 134 CI-tagged tests. The push
triggered post-merge CI run `31339595176`, Webui PHPUnit run `31339595200`,
i18n health run `31339595180`, libnodectld Specs run `31339595184`, and Client
Specs run `31339595177` at that exact head. The four fast workflows passed.
The full VM run started on `gh-runner2.int.vpsadminos.org` immediately after
another six-hour job released it. It passed after 7 hours 23 minutes 45
seconds, within recent runner2 successful durations of 4 hours 45 minutes to
7 hours 24 minutes. Remote `master` and the retained feature branch were then
verified at the exact merged head, and both worktrees were removed.

Terraform provider `master` was fast-forwarded to `1275e4282e` after a fresh
fetch and merge-tree runner enumeration. Post-merge Integration Tests run
`31322295752` passed at that exact head. Both worktrees were removed after
remote-ref verification; the feature branch was retained.

vpsfree-irc-bot `master` was fast-forwarded to `b41dbafd81` after a fresh
fetch, merge-tree Overcommit run, and runner enumeration. Post-merge RSpec run
`31322693412` and Integration Tests run `31322693413` passed at that exact
head. Both worktrees were removed after remote-ref verification; the feature
branch was retained.

web `master` was fast-forwarded to `9c76351dfe` after a fresh fetch and
merge-tree runner enumeration. Post-merge Integration Tests run `31322897309`
passed at that exact head. Both worktrees were removed after remote-ref
verification; the feature branch was retained.

confctl `master` was fast-forwarded to `9eaa0ee73f` after a fresh fetch,
merge-tree Overcommit run, and runner enumeration. Post-merge RSpec run
`31323810818`, Tests run `31323810819`, and RuboCop run `31323810830` passed
at that exact head. Both worktrees were removed after remote-ref verification;
the feature branch was retained.

vpsf-status `master` was fast-forwarded to `5739e1f226` after a fresh fetch,
merge-tree Lefthook run, and runner enumeration. Post-merge Integration Tests
run `31324173031` passed at that exact head. Both worktrees were removed after
remote-ref verification; the feature branch was retained.

## Results

Run 31210461594 tested commit `8d5fe0058` on
`gh-runner2.int.vpsadminos.org`. The build job passed. The full suite ran 75
tests/265 scripts; 71 tests passed and these four failed:

- `cgroups/devices-v1`
- `ctstartmenu/setup`
- `osctl/ct-image-fetch`
- `podman/ubuntu#latest`

The four tests did not reach a product assertion failure. Their QEMU processes
were terminated by a signal, which closed the OSVM machine shell. Three QEMUs
actually disappeared together at 19:19:49-50 UTC: the two first reported
failures plus `osctl/ct-console`; the latter recovered after restarting its
machine and ultimately passed. The two replacement test QEMUs then disappeared
together at 19:20:58 UTC. Guest consoles contain no panic or shutdown, and
OSVM logged an empty QEMU exit status, which is Ruby's `nil` exit status for a
signaled child.

The common root cause is runner memory exhaustion:

- runner2 reported 96 GiB total memory and no swap;
- the test-runner default 4 GiB reserve therefore exposed 92 GiB to the
  scheduler, and the scheduler filled all 92 GiB at suite start;
- QEMU RAM is backed by `/dev/shm`; pre-test shared-memory use was already about
  5.8 GiB, which stable-capacity scheduling does not subtract;
- the raw 60-second sample at 19:19:43 UTC, six seconds before the first kills,
  showed 85.83 GiB shared memory and 9.03 GiB available memory;
- during the job, shared memory peaked at 93.83 GiB and available memory fell to
  1.21 GiB, below the configured 4 GiB reserve, with no swap safety margin.

The scheduler accounts declared VM RAM but not the runner's existing memory,
QEMU/virtiofsd overhead, or concurrent Nix evaluation/build overhead. A 4 GiB
reserve is insufficient on runner2 when the pool is filled.

The tested change is not implicated. The exact same commit passed all 75 tests
in CI runs 31190238532 and 31198648330 on runner3, and each of the four named
tests passed in both runs. Commit `8d5fe0058` only changes the container image
repository overlay consumption and adds an evaluation check.

The trailing `OsVm::MachineShellClosed`, EOF/IO errors, and
`Process.kill: no implicit conversion from nil to integer` are secondary
effects. The OSVM reaper clears `qemu_pid` after the signaled exit; cleanup then
races and attempts to kill the now-nil PID. This obscures the terminating
signal but did not kill the VMs or cause the test failures.

The implementation now caps scheduled memory and `/dev/shm` using initial
availability, adds an 8 GiB reserve, reports terminating signals, and safely
coordinates cleanup with QEMU reaping.

## Integration validation

All workflows for exact head
`ccd22b65fc4a1f69ca464825c20ea839d3dd1dea` passed:

- RuboCop run 31221018947
- RSpec run 31221019023
- CI run 31221018961

The full VM job ran on runner3. Its startup diagnostics reported 100.0 GiB
assigned, 99.0 GiB initially available, an 8.0 GiB reserve, and a 91.0 GiB
memory limit. It completed all 265 scripts and 75 tests successfully in
2846.47 seconds. The log contains none of the original `MachineShellClosed`,
`qemu_exit`, cleanup `TypeError`, or oversized-test warning signatures.

The two earlier successful runner3 runs used the old 96.0 GiB limit and took
2881.27 and 2246.48 seconds. The protected run is within that observed range,
so this sample shows no clear throughput regression from the lower cap.

Runner3 is absent from the public Prometheus target inventory. Consequently,
the integration run proves suite correctness and successful scheduling but
does not provide host memory low-water data. A future run assigned to runner2
would be the direct validation of the original host's measured headroom.

## Merge and post-merge validation

After a final fetch confirmed that `origin/staging` was still the feature
branch base, a temporary merge worktree fast-forwarded `staging` to
`ccd22b65fc4a1f69ca464825c20ea839d3dd1dea`. Repository hooks passed in the
merged tree and the branch was pushed over SSH.

Post-merge workflows at the exact `staging` head produced these results:

- RuboCop run 31251769070 passed in 36 seconds.
- RSpec run 31251769078 passed in 4 minutes 33 seconds.
- CI run 31251769077 built successfully, then reported 71 successful tests and
  four failed tests after 3508.59 seconds on runner3.

The CI failure is unrelated to the scheduler and OSVM commits. Five Fedora 44
scripts failed across four tests: `docker/fedora#latest`,
`incus/fedora#latest`, `podman/fedora#latest`, `snap/fedora#hello`, and
`snap/fedora#lxd`. Every script failed while running `dnf -y update` because
the repository had begun serving `udisks2-2.11.2-1.fc44`. Its `%post` device
scan received `Permission denied` inside the unprivileged container, returned
status 1, and caused the RPM transaction to fail.

All four test VMs shut down normally with QEMU `STATUS: 0`, followed by the new
safe `kill` log with `SIGNAL: NONE`. There were no signaled QEMU exits,
`MachineShellClosed` errors, cleanup `TypeError`s, or evidence of renewed
memory exhaustion. The run again selected a 91.0 GiB scheduler limit.

The failed job was not rerun because the currently published Fedora package
made the failure deterministic across every Fedora test. A rerun would not
validate this change. The feature-branch full suite for the identical commit
had already passed before that repository update. The Fedora issue and
containment options are recorded in
`notes/vpsadminos/2026-08-08-fedora-44-udisks2-container-update.md`.

## Fedora 44 follow-up investigation

Fedora update `FEDORA-2026-ae4aff6b6f` promoted
`udisks2-2.11.2-1.fc44` to stable at 01:36 UTC on 2026-08-08, several hours
before post-merge CI began. The Fedora dist-git release commit does not change
the failing `%post`; it only bumps upstream udisks from 2.11.1 to 2.11.2 and
removes a patch included upstream. Upstream 2.11.2 contains bug and security
fixes, not a container policy change.

The failure is a latent Fedora packaging bug. Fedora added the existing
`/run/udev/control` socket guard in 2019 to skip udev retriggering when udev is
unavailable in containers and rpm-ostree systems. vpsAdminOS deliberately
provides the socket so systemd can monitor udev events and device units, but an
unprivileged container cannot scan all devices through its restricted sysfs.
The socket-existence test is therefore insufficient, and `udevadm trigger`
returns nonzero. DNF correctly reports the failed RPM scriptlet.

The regular Fedora image build should not be blocked. Its update runs in a
chroot where `/proc`, `/sys`, and `/dev` are mounted but `/run` is not shared,
so no udev control socket is present and the Fedora guard skips retriggering.
The current Fedora 42 builder is also unaffected by this 2.11.2 update. A
refreshed Fedora 44 image is the preferred immediate mitigation: it can install
the security-fixed package safely during the chroot build and prevents live
test containers from performing the broken upgrade transition. This still
needs verification with `image-scripts/test@fedora-44` and the affected VM
scripts.

The preferred upstream fix is for Fedora's udisks2 scriptlet to explicitly skip
containers and treat both udev refresh commands as best-effort. Fedora 43 has
the same update in testing, so a corrected build should cover both releases and
gain container gating. A Fedora-only `dnf upgrade --exclude='udisks2*'
--exclude='libudisks2*'` is an acceptable short-lived CI fallback, but not a
published-image solution because 2.11.2 includes a CVE fix. Global
`--noscripts`, relaxed sysfs/device access, and hiding the udev socket were
rejected as unsafe workarounds.

## Open questions

- Whether the QEMUs were selected by the kernel cgroup OOM killer or another
  host-side OOM policy cannot be distinguished from the retained artifacts;
  the OSVM log records only `exitstatus`, not `termsig`, and runner journals
  were inaccessible. The memory exhaustion and external signal termination are
  independently established.
- The new scheduler accounts for baseline host use and reserves another 8 GiB.
  Direct runner2 validation remains useful because GitHub assigned the green
  integration run to runner3 and runner3 has no public host metrics.
- The cgroup-v1 capacity path is implemented but does not yet have the direct
  unit coverage present for cgroup v2.

## Cleanup

- The vpsAdminOS and all seven consumer feature branches remain available
  locally and remotely after merge.
- Every initiative feature and temporary merge worktree was removed after its
  post-merge evidence was recorded. Ignored per-worktree build and gem caches
  were removed with their worktrees and can be regenerated normally.
- Downloaded post-merge artifacts remain only under `/tmp` for automatic
  system cleanup; the combined manual deletion command was rejected before
  execution, so no unrelated path was touched.
- No superseded workflow needed cancellation.
