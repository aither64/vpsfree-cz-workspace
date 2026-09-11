---
lifecycle: active
---

# 2026-09-11-devcluster-packaging-investigation

## Current status

All repairs are committed, pushed, reviewed and deployed in the user profile.
Both providers passed final live bridge acceptance, including retained data.
Final local flake checks, packaged smoke and organization CI passed. vpsAdminOS
unit/lint CI passed. Broad OS CI has three unrelated suite failures, investigated
in ci-investigation.md; Intel livepatch remains in progress. Both clusters are
stopped with all five disk images retained. Keep branches unmerged and the
session open. The password-reset session remains untouched; its OSVM input needs
the companion commit before retrying vpsAdmin. No reset, merge, archive or delete
is authorized.

All worktrees are under worktrees/2026-09-11-devcluster-packaging-investigation/,
with branch 2026-09-11-devcluster-packaging-investigation:

| Project | Current head | Role |
| --- | --- | --- |
| vpsfree-dev-workspace | 19238ca67ad822b362ae60f0cf7e7b4b27d60397 | Persistence follow-up reviewed and pushed |
| workspace | 7f083fb38d7c24f910e9de54da4c1f49ff504d8e | Final persistence pin committed, pushed and deployed |
| vpsadmin | 8d0ccafd5b307115ddc4b1f24152ba30ed52e893 | Unmodified validation input, local branch |
| vpsadminos | e6c4c5cfa27ce3b139bba6475be80cfead4b8df4 | OSVM persistence primitive reviewed and pushed |

Active package: /nix/store/qvdcxfks49mhgpamiy07qr0h95skzpia-dev-workspace-0.2.0.
Generic runtime and its dependencies unchanged. Initial coordination commit f50473c.
The original investigation and the implementation history below record how the
scope progressed; this status and plan.md control current work.

## Investigation history

Investigation started September 11. The process had no DEV_SESSION_SLUG and
`dev-session current` returned no session. Created this separate initiative with
`dev-session start devcluster-packaging-investigation --no-attach --no-codex
--json`; the target session remains untouched.

## Commands run

- Committed initial tracking as shared-workspace `f50473c` after fetching origin
  and verifying shared master matched origin/master; no unrelated paths staged.
- Fetched organization upstream; FETCH_HEAD is `0a9c974994746e2a6d9d74e83cde8abbf0e65f0a`.
  This bare clone has no remote.origin.fetch mapping, so existing origin/master
  is stale; used the freshly fetched HEAD for the current-source comparison.
- Ran independent installed-payload `nix eval --offline --impure
  --no-write-lock-file` probes for both `cluster-config.drvPath` and
  `runner.drvPath`, overriding inputs to the original logged OS and vpsAdmin
  revisions. No source/default-branch update was needed to reproduce.
- Repeated evaluation with isolated copies containing proposed package assets
  and current OS runner dependency arguments. Used generated temporary SSH
  fixture material and an empty certificate fixture directory for evaluation.
- Inspected runner-build dry run, then built both temporary runner derivations
  and executed them without arguments to exercise Ruby/library loading only.
- Ran existing devcluster_status_test.rb from an isolated source copy through
  pinned Nix Ruby with the actual installed runtime contract.
- Probed the actual lock function with a failing callback command and marker.

- Read target tracking and original cluster-start.log.
- Inspected installed stable wrappers and extension catalog.
- Inspected organization extension source, local AGENTS.md and workspace config.

## Results

- Both configurations fail on absent defaults. vpsAdmin runner separately fails
  on the shared source outside its nested flake root.
- vpsAdminOS runner first fails on an uncalled overlay function. Correcting it
  exposes missing vpsadminosRubyGemConfig; adding that resolves dependency eval.
- An additional vpsAdminOS probe with the dependency fixes but the original
  `../lib` reference reproduces the same invalid-store-path error as vpsAdmin.
- With all temporary packaging/dependency corrections, both cluster config
  derivations and both runner derivations evaluate. Both runner packages build
  and show expected usage with exit 2, proving their Ruby dependencies load.
- Existing tests: 46 runs, 516 assertions, zero failures/errors/skips,
  49.202217 seconds, seed 26910.
- Lock callback probe returns zero after a deliberate `false` and executes the
  following marker. Original target logs corroborate build failure followed by
  launcher execution. Add explicit failure propagation to the repair scope.
- Evaluating vpsAdmin config performed a small source-preparation derivation.
  Runner builds involved four wrapper/bundle/stub derivations. No VM closure or
  Linux kernel was built and no VM was started.
- Findings, source history, recommended minimal repair, alternatives,
  compatibility constraints and the required two-provider acceptance matrix are
  in `investigation.md`. Full VM startup/update/restart is explicitly unverified.

## Investigation handoff (superseded by implementation below)

If implementation is requested, reuse this initiative and create an organization
extension worktree. Implement package boundaries, OS runner compatibility and
failure propagation, then commit/quick-check/review before live integration.
Use the stable dispatcher for candidate deployment and separate bridge clusters;
do not reset/adopt the password-reset session. No user input is needed to finish
the investigation report.

## Cleanup

Temporary evaluation/build/test scratch was created under
`/tmp/devcluster-packaging-probes-rraotntg`. Useful sanitized results are in the
report and evidence artifact; transient copies and generated SSH fixture keys
were removed at handoff. The first scratch removal encountered read-only shared
directories inherited from the Nix store copy; made only owned scratch
directories writable and completed removal. Built Nix outputs may be
garbage-collected normally.
No follow-up tracking-only commit is due on this short investigation; leave the
report/state/portal and durable note changes available in the working tree.

No other session files or clusters modified; no VMs or kernel builds started.
Keep this session open for follow-up; no archive/delete requested.

## Implementation phase (September 11)

The user approved implementation and user-profile deployment, with feature branches
retained and no merges. Reusing this explicitly selected initiative despite the
process lacking DEV_SESSION_SLUG; stable commands use the explicit slug.
The initial tracking commit is f50473c. Plan updated for the approved execution.

- Organization worktree: worktrees/2026-09-11-devcluster-packaging-investigation/vpsfree-dev-workspace,
  branch 2026-09-11-devcluster-packaging-investigation, base 0a9c974994746e2a6d9d74e83cde8abbf0e65f0a.
- Workspace feature worktree: worktrees/2026-09-11-devcluster-packaging-investigation/workspace,
  same branch name, base shared master f50473c. Shared checkout stays on master.
- Investigation-only scope statements above describe the completed prior phase;
  this implementation phase and updated plan now control the work.

### Implementation progress

- Committed package assets/docs as 55830a7 and OS runner dependencies as 30516d8.
  Package install checks and full package build passed. Its inherited generic
  checks passed (285 Ruby / 2737 assertions, 73 host / 438 assertions, declared
  sandbox skips; Go packages passed). Initial install test used coreutils/cmp;
  corrected it to diffutils/cmp before accepting the build.
- Failure propagation and actual-command regression tests committed as 35a7090:
  6 tests / 110 assertions pass, 46.4 seconds. Existing status/lifecycle tests
  also pass: 46 tests / 516 assertions, 49.9 seconds.
- Verified official action tags over SSH: checkout v7.0.1 and install-nix-action
  v31.11.1 remain latest. CI smoke step retains those refs.
- Added locked smoke inputs: vpsAdmin 8d0ccafd5, OS staging 3eaf7b732 and status
  587cd65b. The main nixpkgs/generic runtime inputs remain unchanged. Compared
  OS changes since the original diagnostic pin; latest staging includes kernel
  updates, so live VM builds still require an explicit cache check.
- Validation input worktrees registered under this initiative, same branch:
  vpsadmin at 8d0ccafd5 and vpsadminos at 3eaf7b732. No application edits.
  The OS post-checkout hook refused its changed signature after checkout was
  created. Inspected .overcommit.yml, retried registration successfully and
  entered its Nix shell to sign the verified configuration normally.
- The first packaged smoke invocation evaluated config drvPath and text in
  separate Nix processes. Consolidated them using --apply to avoid duplicate
  expensive machine evaluation, stopped the superseded invocation and started
  the final version. This is a test-runtime improvement, not a failed result.
- Corrected smoke test decoding: Nix fromJSON rejects writeText content carrying
  store context. Return raw text through nix eval --json, decode in Ruby instead.
- Override assertion initially used node1.memoryMiB. Inspection after its failure
  found vpsAdmin uses this for DB seed total_memory but hard-codes QEMU memory
  (test.nix:1614). This pre-existing limitation is outside the packaging repair;
  test supported bridge and SSH-forward overrides for both providers instead.
- Both expected Linux 6.12.109 kernel outputs are advertised by configured caches
  (nix path-info reports substitution, 13.5 MiB combined download). Full actual
  closure dry-run remains required before live starts.
- General review found no Blocking/Important issues and one Advisory: OS docs
  incorrectly mention a refresh step. Will remove that word from the OS section.

### Review reconciliation

All four fresh review lanes used gpt-5.6-sol/xhigh, high risk due to host lifecycle,
persisted cluster state and deployment. Reports are review-{general,architecture,
scope,risk}.md. Initial heads: general/architecture/risk 54b1d7a, scope 961dadf.
No Blocking findings. Reconciled findings:
- Architecture Important: exported overlays + shared local runner constructor.
  Implemented; no vpsAdminOS API change. Rerun architecture for this new helper.
- Risk/scope Important: implicit minimum OS source interface. Documented minimum
  6f9b2c755 (or compatible newer) and operator rebase requirement. Runner interface
  evaluation is forced before cluster-config builds, with a direct missing-overlay
  error. Older retained branches require source update; state/disks stay compatible.
- Risk Important: unchecked ready/PID/socket/log prep under conditional locking.
  Added explicit returns and regression with retained readiness + failed cleanup.
- Risk Important vs scope Advisory: transactional forced certificate replacement
  predates this range. Accepted as an existing residual, not a claimed guarantee:
  cert init/import --force (including documented encrypted-CA fallback) can lose
  old credential files if replacement fails late. This repair stops subsequent
  build/deploy work on failure; it does not promise atomic credential replacement.
  Full staging/rollback is separate credential hardening, outside the accepted
  packaging/failure-propagation boundary. No use of --force certificates is needed
  for live acceptance; do not replace another session's shared CA here.
- Risk Advisory: per-cluster config replacement now uses a same-directory temp
  file and removes that temp on failed jq/mv; original config survives parse error.
- General Advisory: removed nonexistent OS update refresh phase from docs.
- Narrow lifecycle remediations passed focused tests: 7 runs / 118 assertions,
  no failures/errors/skips, 52.9s. No reviewer rerun merely for these direct fixes.
- Smoke at 961dadf completed: both providers, bridge/local, default/override,
  eight configurations plus both built/loaded runners pass. Shared runner helper
  follow-up needs its own build/load verification before deployment.
- Committed remediation series was reworded only (no tree change): current head
  d2380cb, dependency builder 447d37c, failure propagation 8c3c7e2, assets55830a7.
- Initialized only this initiative's two configs through installed stable config
  commands. Shared credentials were already present; existing certificate covers
  every configured domain. No CA/key replacement needed or performed.
- Bridge probes: .41/.53/.61/.62/.71 did not respond; br0 up and no cluster QEMU
  processes found. Fresh probes will precede launch if time has elapsed.
- Actual OS config dry-run:90 small derivations,20 substitutions; no kernel
  compilation. Inspected linux-6.12.109-modules derivation: a buildEnv symlink
  union with depmod over cached kernel and ZFS outputs; modules-shrunk only copies
  the selected module closure. NixOS kernel advertised by cache.nixos.org and OS
  kernel by cache.vpsadminos.org. vpsAdmin actual-config dry-run still underway.
- Final shared-helper packaged smoke at tree d2380cb completed successfully:
  eight actual packaged configuration cases and both runner builds/loads.
- vpsAdmin actual-config dry-run completed:256 derivations (configuration files,
  app closures, module unions, initrds and disk images),33 substitutions/247.5MiB.
  No Linux kernel derivation will compile; both kernel outputs are cached.
- Minimum-interface negative check and independent reviewer probe on an actual
  retained pre-minimum OS worktree fail before configuration construction with
  the intended diagnostic. No older worktree or its state was modified.
- Architecture and risk reruns at exact head d2380cbe77f711627ba461ef9359724b6255a5db
  completed with no Blocking/Important/Advisory findings. Original architecture
  finding resolved; deliberate minimum-source contract verified. No other lane
  rerun needed for direct checks/docs/config-temp remediations. Rerun reports added.
- Full flake check and branch CI are next, followed by consumer pin/profile build.
- Organization feature pushed at d2380cb; Check workflow34622101634 running:
  https://github.com/vpsfreecz/dev-workspace/actions/runs/34622101634.
- Workspace pin generated with nix flake update vpsfree-dev-workspace. Recursively
  compared resolved lock dependency graphs (including follows/node renames): generic
  runtime bcbaf825d71285cbbd05b56e78bc386f2df480bd and package nixpkgs
  d58a46e3bc02d91ebe04667f8397752a749c0024 unchanged with all their dependencies.
  New lock nodes belong only to the development-cluster smoke inputs.
- Workspace deployment-contract check passed:3 tests/14 assertions. Candidate
  package build in progress. Pin is a mechanical dependency update, so no extra
  mandatory review lane is required beyond the reviewed consumer contract.
- Full local nix flake check completed successfully; extension suites 46/516,
  7/118,10/33,38/191,31/125,42/194,43/825 (one declared skip), and inherited
  generic runtime Go/Ruby checks passed (285/2737 with12 skips,73/438 with3 skips).
- Workspace feature2c81615 committed and pushed. Its candidate package built at
  /nix/store/aq0akirnaxra9nrqgmdx3lacnn7mqv7l-dev-workspace-0.2.0; checks passed.
  Workspace repository has no branch Actions run. Organization CI passed flake
  check and is running the packaged smoke step.
- Prebuilding both dry-run-reviewed VM closure derivations while CI runs; no
  deployment or VM startup yet. This uses only this initiative's configuration,
  worktrees and existing credentials, and cached kernels.
- Candidate and previous runtime-contract.json are byte-identical. KVM read/write
  and qemu-bridge-helper access are available; allowed bridges include br0.
- Existing portal HTTPS endpoint responds401 at the authentication boundary.
  Ambient/system curl trust rejects its private issuer before any switch;
  an unauthenticated --insecure probe establishes reachability only. No credentials
  sent and no TLS configuration changed. Durable curl-trust note records this.
- CI34622101634 passed on exact organization head d2380cb in10m5s, including
  full flake check and packaged smoke. No failure/rerun/superseded run occurred.
- Both VM closure builds completed successfully. Repeated dry-runs using the
  actual site-config candidate package select the exact prebuilt configs:
  OS /nix/store/0846i5ggq5gd70z0pc8hpgd84lq1gfz2-os-test-vpsadminos-devcluster-2026-09-11-devcluster-packaging-investigation.json
  vpsAdmin /nix/store/75li7w6qsj3m2hcs0zdpw2harmkmqpdb-os-test-vpsadmin-devcluster-2026-09-11-devcluster-packaging-investigation.json.
- Starting approved workspace-host switch from workspace feature worktree.
- Profile switch completed successfully: aq0akirnaxra9nrqgmdx3lacnn7mqv7l,
  Codex generation22 with compatible0.154.0, previous profile retained. Portal,
  router, Codex and tmux services active. No system configuration deployed.
- Timer-triggered workspace-codex-reconcile-pending crossed the transition lock
  at18:38:49 and was rejected18:39:03 with the designed superseded-generation
  diagnostic. Rerunning that service under the new generation; not an app defect.
- Fresh .71 address probe was clear; stable vpsadminos-devcluster single/bridge
  start launched for this initiative, with private transient logging.
- OS cluster start completed successfully, status running/ready on bridge and SSH
  reachable. First boot had a long quiet early phase; investigated before treating
  it as failure. A short isolated one-vCPU/no-disk kernel probe produced normal
  boot output and expected missing-root panic. It does not indicate a kernel bug.
  The managed VM subsequently became ready without configuration changes/retry.
- Reconciliation retry completed Result=success/ExecMainStatus=0 after startup
  released its lifecycle lock. Recorded this expected-generation refusal in notes.
- OS container create/start/stop/data-marker checks are running over stable SSH.
- OS acceptance: osctld healthy, tank pool active, Alpine packaging-smoke created,
  started, stopped without forced kill and restarted. Container marker survived;
  host marker written under /tank. Updating hostname to dev-os1-updated through
  this initiative's config to exercise an actual closure change.
- Found separate existing generic-dispatch behavior: stable SSH passes command
  arguments, but system_env!/Open3.capture3 closes stdin. A bash -s stdin script
  exits0 without executing. Re-ran via safely quoted bash -c command arguments;
  real checks passed. Do not claim stdin/interactive SSH repaired; generic runtime
  pin is explicitly unchanged. Durable note records cause/workaround/follow-up.
- OS real update succeeded: copied and activated new toplevel
  yn0cw40bn14c43amz5i4nr60d7nyjd48-vpsadminos-system-dev-os1-updated-26.05pre-git.
  No kernel build. Verifying both markers, then stopping/restarting the VM.
- OS markers survived live update. Runtime hostname remains dev-os1 until reboot,
  while /run/current-system changed to the updated-hostname toplevel; restart now
  exercises activation of that configuration at boot.
- OS stable stop completed, runner exited and result-config GC root removed.
  Tank disk retained. Stable restart with single/bridge now in progress.
- OS restart passed: hostname dev-os1-updated, osctld healthy, host and Alpine
  container markers unchanged. Container was stopped after VM boot and was
  explicitly started again for the marker check. Final stable stop succeeded;
  OS tank disk retained, runner/GC root removed. OS acceptance complete.
- Fresh probes of vpsAdmin .41/.53/.61/.62 addresses were clear. Starting stable
  single/bridge vpsAdmin cluster now (services, node1 and default two DNS VMs).
- First vpsAdmin start exited1 after all four VMs reached runner readiness: the
  automatic node refresh attempted SSH before node1's bridge address was ready
  and received255/No route to host. VMs remain owned/running; failure propagation
  correctly stopped refresh. Added a bounded harmless SSH readiness probe for
  services/node refresh and a transient-transport regression, now quick-testing.
  This real live failure extends the repair within its startup boundary; record
  new review/CI/profile heads before accepting repeated start.

SSH readiness follow-up committed as 3d83a8392cd77fb7e92587ed4ea1a5cc665bd3fb. Focused actual-command tests: 8/124 pass; bash syntax and diff checks pass. High-risk four-lane review requested before deployment.

Deployed-base vpsAdmin diagnostics: manual refresh passed after bridge SSH became reachable. MySQL, API, supervisor, both DNS bind/nodectld units, node osctld/nodectld and tank pool healthy. Corrected the acceptance CLI URL-specific credential config inside this disposable services VM; seeded API node query passed. VPS creation validation ongoing.

## Readiness review remediation

General and risk found that ConnectTimeout cannot bound authentication/session stalls.
The follow-up now sets BatchMode=yes and IdentitiesOnly=yes and uses coreutils
timeout with a five second per-attempt bound capped by the remaining 120 second
deadline, plus a one second forced-kill grace. A stalled attempt returns its
non-255 error immediately. Actual remote actions are still never retried.
The probe reuses machine_host/ssh_opts, independently of the public SSH command.
Coreutils was already a runtime dependency; no new configuration/dependency/state
contract. A real hanging SSH stub now proves timeout124, no remote action and lock
release. Full actual-command suite9/130 passes, syntax/diff clean.
Reviewed original 3d83a839 is retained in history by Git but amended into final head:
9e8783d68fdf40de04683e419d4f373bc27e3730

Rerun general, risk and architecture on this narrow change from original readiness
head; scope remains the same bounded readiness behavior. No live use of new code yet.

Final readiness reruns at 9e8783d: general, architecture and risk report no findings; prior Important timeout issue resolved. Scope review accepted bounded behavior. All use gpt-5.6-sol/xhigh. No outstanding blocking/important findings. Full flake, packaged smoke and branch CI now rerun. Upstream organization master remains0a9c974; workspace rebase onto shared masterf50473c is already up to date after fetch (remote masterb5e74dd).

vpsAdmin base acceptance: API created VPS3 (Alpine,1GiB RAM,2GiB disk, no assigned IPs). The first512MiB request failed expected seeded environment minimum; no package defect. API stop/start passed; container /root/packaging-marker and host /tank/devcluster-packaging-marker survived. Stopping the owned cluster before follow-up profile deployment; retained disks will test restart compatibility.

Final workspace pin1c534c2 pushed, package built at /nix/store/x20iwwg5ap9cx1qxwj44xfjcdxxrd2sg-dev-workspace-0.2.0; extension tools0w1zl4fzvbvjsbhl66bw9yg07l2pzrxx. Full final local flake check and deployment contract3/14 pass. New live configuration dry-run requires no VM build; runtime contract byte-identical. Both owned clusters are stopped with all disks retained. CI34627082837 is in packaged smoke step; local packaged smoke running. No superseded active branch runs to cancel (previous run completed successfully).

Final CI34627082837 passed in10m9s on9e8783d; durable ci-result.json captured. Final local packaged smoke passed all eight config cases and both runner loads. Supported user-profile switch completed to x20iwwg5ap9cx1qxwj44xfjcdxxrd2sg; Codex generation23/0.154.0 compatible. Prior aq0akir profile retained. Started final vpsAdmin bridge acceptance on retained disks.

After final switch: router, portal, Codex, tmux and reconciliation units healthy; no failed user services. Stable portal URL reconfirmed. Read-only ancestry check confirms the password-reset session's recorded OS input2166e593 (September7) already contains the supported6f9b2c755 interface; the minimum is not an additional blocker for that recorded input. Final vpsAdmin start is booting all four VMs using unchanged prebuilt configmj9dbxpd / output75li7w6q.

## Persistence extension after live restart

The final bridge restart proved SSH waiting works, then exposed osctld socket/pool
readiness. The new node wait observes both ZFS import and osctld active state before
any filesystem/device mutation, with a180-second process timeout and one second
forced-kill grace. Actual remote-script tests cover delayed and never-ready pools.
Focused command suite11/139 passes. Initial new test failed only because the fake
nodectld socket was absent; fixed the fixture to model it without writing host /run.

The same restart exposed a distinct data-loss behavior in upstream
osvm/lib/osvm/nixos_machine.rb: prepare_disks unconditionally deletes and recopies
the NixOS root disk. Services MySQL had no VPS rows after reboot while node CT3
retained its files. Only this initiative's disposable data was affected. The
password-reset session remains untouched.

Extend the affected vpsAdminOS repository from validation-only to an implementation
branch: add an opt-in preserve_root_disk keyword on NixosMachine, default false for
ordinary isolated tests. Copy new roots atomically, continue preparing extra disks,
and retain explicit destroy/reset behavior. The organization runner requests this
option for NixOS guests and refuses an OSVM input lacking it before any VM starts.
This intentionally raises the vpsAdmin provider's OS input minimum to the new
feature revision. Pin it in packaged smoke inputs; current/older standalone OS
provider sources still use the previous overlay minimum. Keep all branches unmerged.
No production daemon, schema, protocol, kernel or coordinated node update changes.
The generic workspace runtime remains unchanged.

For retained NixOS roots, configuration closures must be copied/activated with
update while the VM is running before restarting with a changed configuration.
Do not restart existing NixOS disks using an older provider/OSVM combination: its
fresh-image policy can erase them. No root data conversion is required; existing
complete images are reused. Follow-up tests will create a new API VPS record in
the fresh fixture database and prove both its row and container data survive a
full stop/start. The earlier orphan CT3 is retained as evidence, not reset.

Publish reviewed OSVM feature first, update organization test pin and consumer pin,
then deploy the user-profile package. Use the already reviewed deployed provider
for independent configuration-update checks while preparing this fix; do not run
the new runner before mandatory review.

Persistence review packet covers org9e8783d..19238ca and OS3eaf7b732..e6c4c5cfa. General/architecture/risk lanes running; scope follows when a slot frees. All sol/xhigh. OSVM111 specs and hooks pass; provider commands11/139 and runner contract3/7 pass. Companion OS feature published to resolve exact test pin; OS branch RuboCop green, RSpec/CI running. No new VM start uses unreviewed code.

### Persistence review acceptance

All four standalone lanes (gpt-5.6-sol/xhigh) reviewed organization 9e8783d..19238ca
and vpsAdminOS 3eaf7b732..e6c4c5cfa with no findings. Reports are
review-persistence-{general,architecture,scope,risk}.md. Remaining acceptance is
actual packaged runner loading and retained-root/DB/container restart. The
accepted compatibility limits are existing-root completeness, required running
guest closure update before changed-config boot, and destructive old-runner
rollback. No new protocol/state schema or production node update is required.
Removed owned generated libosctl/tmp before the final source evaluation.

Final generated workspace pin 7f083fb changes only organization source and the
test-only devcluster-vpsadminos node. Recursive generic dependencies are identical.
Deployment contract passed 3 tests / 14 assertions. This mechanical pin update
meets the mandatory review skip criterion; functional heads were reviewed in all
four lanes. Fetch completed; an initial rebase correctly refused the uncommitted
pin, then after committing rebase onto shared master was already up to date.
Organization feature CI 34631425856 is running at 19238ca. No superseded active
branch runs existed. OSVM RuboCop and RSpec CI passed; OS full CI 34630335805 continues.

Final full local flake check passed, including command suite 11/138 in the Nix
sandbox and runner contract 3/7; focused ambient count was 11/139 because of the
lock timing assertion. Existing generic sandbox skips remain declared. Workspace
package build passed at /nix/store/qvdcxfks49mhgpamiy07qr0h95skzpia-dev-workspace-0.2.0,
organization tools /nix/store/rp7la245cxkzg68mwpims5mbsc9bp42x-vpsfree-dev-workspace-tools-0.1.0.
Runtime contract is byte-identical to the deployed predecessor.

Final live update with OSVM source e6c4c5cfa passed on all four vpsAdmin VMs.
Verified API VPS1/hostname and read-only host/container markers after the update.
Two initial check invocations mistakenly passed local Python orchestrators as
remote Bash; both failed parsing before checks, corrected by running Python
locally. Corrected checks passed. Final packaged smoke passed all eight
configurations and both runner builds/loads. Stopping vpsAdmin for deployment;
standalone vpsAdminOS remains stopped with retained disks.

Organization CI 34631425856 passed at final 19238ca; ci-result.json updated.
Final profile switch succeeded to qvdcxfks49mhgpamiy07qr0h95skzpia. Router, portal,
Codex, tmux and reconciliation path/timer active, no failed user services.
Both clusters were stopped during the switch. The vpsAdmin final bridge restart
is now running; all three NixOS root images existed before start. The prior
shutdown waited for each DNS nodectld systemd stop timeout (90 seconds), an
unchanged guest-service behavior. No force-stop/reset was used.

For context on the broad OS CI duration, inspected previous staging CI
34398676068: its test suite ran about55 minutes and failed kernel/livepatch-kernel-identity
and osctl/nfs-cancellation; both livepatch vendor jobs passed. This is baseline
evidence only, not an explanation or waiver of any current feature result.
Final installed-package standalone OS restart added to acceptance after the
shared-runner changes. Initial inode comparison during vpsAdmin config evaluation
was pre-launch only; repeat it after successful startup for actual reuse evidence.

Final-restart command correction: omitted --network selected local despite the
retained bridge config. Stopped the owned OS VM normally and sent TERM to the
verified owned vpsAdmin runner during start (PID2264659, complete own tuple
checked) so it entered cleanup. No disk reset occurred; all NixOS root image
inodes/sizes match before start. Repeat both starts explicitly with --network
bridge. This operator invocation error is not accepted as bridge evidence.

Correction to the preceding network diagnosis: source and QEMU arguments prove
only the OS provider defaults to local; vpsAdmin was already on bridge. The
vpsAdmin interruption was unnecessary. Its cleanup stopped services before
node1 completed Stage1, leaving set-clock DNS retries without its services VM.
Verified node1 QEMU's parent2264659, name, exact owned tank image/socket and
Stage1 state before considering TERM to QEMU2266102. The guard refused the
action because Stage2 had started meanwhile; no QEMU signal was sent. Let
normal cleanup complete and verify retained data after retry. No other
session/process was signaled. Keep this interrupted attempt separate
from successful lifecycle acceptance.

Node1 remained in the set-clock retry loop after services shutdown, before
runner shell readiness. The normal machine.stop call waits for that shell with
the inherited900-second default before its fallback. Reverified the exact
owned QEMU tuple/parent and sent TERM to node1 QEMU2266102 to end the interrupted
disposable test, using the same VM termination action as the runner fallback.
No disk file was reset or removed. Final bridge acceptance must verify host and
container markers after this interruption as well as NixOS database persistence.

Final installed-package OS acceptance passed on explicit bridge networking:
start returned0, hostname dev-os1-updated, osctld running, host marker retained,
Alpine packaging-smoke container started and its marker retained. Stopping it
with disks retained. The corrected vpsAdmin bridge retry started only after the
interrupted prior runner exited and status confirmed stopped.

Final vpsAdmin bridge start returned0 with automatic SSH/service-seed/pool
refresh; no manual refresh was needed. API VPS1/hostname survived the complete
stop/start, as did host and container markers. Services mysql/API/supervisor,
both DNS bind/nodectld units, node osctld/nodectld and active tank pool passed.
Current node closure z0jb05xb0sayd46swvd26pa9643sj8ff and services closure
iqq7sqz5m90579j5p5fvnqkk49m5idrh match the final pre-stop update. Final live runner
PID2284737 reused all three NixOS root image inodes/sizes. API lifecycle check
on retained VPS1 is running before final cluster shutdown.

Retained VPS1 passed API stop and start; both host/container markers passed
again afterward. Started final vpsAdmin stop. Workspace feature has no GitHub
Actions runs; local deployment contract/package checks cover the consumer pin.
For the longer OS CI, job metadata identifies gh-runner1 (suite) and gh-runner2
(Intel livepatch). Read-only SSH probes as the current user and root were denied;
no remote command ran or runner state was changed. Continue through GitHub CI
results/artifacts. Do not assume current failures match the previous baseline.

Final vpsAdmin stop returned0. Both stable status commands report stopped/bridge.
Config GC roots are absent, with four vpsAdmin disk images and one standalone
OS disk image retained. An initial stronger assertion about PID/readiness file
removal failed: vpsAdmin used its existing120-second stop fallback and retained
stale PID/ready markers; its runner process is gone. Repeating the idempotent
stop command clears those stale markers without changing disk data. No session cleanup,
archive, branch deletion or integration is scheduled. Broad OS CI still pending.

Stop-path investigation: each DNS nodectld service can wait90 seconds, while
the existing provider allows120 seconds for the complete sequential shutdown
then kills the owned runner/socket processes. Final stop log explicitly reports
killed after timeout. This predates the reviewed changes and also occurred on
the pre-retention shutdown that the subsequent successful restart validated.
Record as an existing graceful-shutdown limitation; do not claim all vpsAdmin
stops were graceful. The API/container stop/start itself completed normally.

After idempotent stop cleanup, both providers have no runner PID/readiness files
or config GC roots, and a process inventory finds no owned runner, QEMU or
virtiofsd process. All five disk images remain. All four project worktrees are
clean at the recorded heads. No final-code changes followed mandatory review.

Broad OS suite completed with76/79 tests passing, three failed scripts. Full
feature and preceding staging artifacts were inspected; see ci-investigation.md.
Livepatch missing-file and NFS hard/soft mismatch reproduce the baseline; current
NFS cleanup also faults in rpc_cancel_tasks. Memory-view setup failed on Alpine
DNS/index/package404. All affected fixtures use the unchanged OS machine class.
NixOS driver integration and OS driver integration passed. Treat these as
separate OS/test issues, with no blind rerun or unrelated kernel changes here.
Intel livepatch CI still running.

## Handoff

Implementation and installed-package live acceptance are complete. Final remote
feature heads exactly match the clean local worktrees. Both providers are stopped
on bridge, with no owned runner/QEMU/virtiofsd processes and all disks retained.
The password-reset session needs OSVM commit e6c4c5cfa (or a compatible backport)
in its selected OS input before retrying; this initiative did not touch it.

Generic SSH stdin forwarding, DNS graceful shutdown, and the broader OS CI
failures are separate follow-ups documented here. The Intel livepatch job uses
an unchanged OS machine/kernel test and remains in progress; do not report the
whole OS pipeline as green. No current-head workflow was cancelled or blindly
rerun. Repository runner-status API access is also unavailable (403); no further
credential/access changes were attempted.

Removed seven owned credential-bearing temporary scripts/logs after preserving
sanitized results. No generated source scratch remains. Useful review, smoke,
CI and live evidence is linked from the portal manifest. No session archival or
branch/worktree deletion is authorized or scheduled.

Consolidated September11 end-of-day coordination checkpoint: preserve the deployed
implementation, reviews, live acceptance and known CI limitations while feature
branches remain unmerged. This is the first tracking-only checkpoint after the
initial commit. Shared master was fetched and is linear; only this initiative's
records and its own durable notes will be staged. The workspace feature remains
at its deployed head and will rebase again before any future integration.

Read-only handoff check found no dedicated vpsAdminOS worktree under the
password-reset slug. Select or attach a source containing the companion OSVM
fix there; do not assume an existing OS checkout can simply be rebased.
