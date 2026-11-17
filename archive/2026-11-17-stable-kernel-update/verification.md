# Final verification plan and evidence

Committed final-review candidate (review passed with one Advisory; narrow fix in progress): OS
5a59f3059ca6ada368deeeeca6dba5034468be93, Linux
3bba27296b6f4f4a2b1568d65cea6037368f229b. Quick results and complete
unchanged flake/source graph in [catalog evidence](catalog-evidence.md), patch
correspondence in [Linux evidence](linux-port.md).

## Product check selection and stopping condition

After mandatory independent review, publish OS topic. Existing ci.yml triggers
on the catalog change and builds ci-toplevel. Lead evaluated ci-toplevel.drvPath
and it is identical to explicit ci-toplevel-kernel-6_12_118:
/nix/store/smzzgsm45k9qiir8sv7wwfrn8z4f4174-vpsadminos-system-vpsadminos-26.05.git.5a59f30.drv.
Prefer this existing remote build and test run over duplicate local kernel builds.
Observe exact run/attempt/head through runtime monitor and collect actual build
and test input/source evidence before reusing results. If no run appears, build
fails, or targeted cases are absent, diagnose and select the smallest faithful
follow-up; do not claim an unrun check. No arbitrary build wall timeout.

The existing ci selector includes osctl/nfs-cancellation, system/boot/stage-2,
kernel/module-autoload and zfs/boot-modes, all tagged ci. NFS forces stable and
asserts release/source revision; the other three have no explicit unstable
kernel override. The branch name does not select unstable, and ci.yml's normal
push profile sets VPSADMINOS_CONFIG empty. No ignored os/configs/tests.nix or
local.nix override was found in the final own source before review.

Coverage: boot/module behavior, NFS teardown/cancellation/client isolation and
built-in/external ZFS data operations. The full normal CI may cover more;
required claim remains bound to the tested source and actual cases. Stop when
exact target closure succeeds and applicable selected cases pass, with final
review and no unresolved material findings. Diagnose failure logs rather than
blind retry. Unexpected local kernel compilation should be investigated; this
task intentionally changes kernel sources, but remote runner/cache is preferred.

## Current evidence

- Skill/docs/links/metadata/examples, normal hooks, Nix source realization,
  selector identity/retained entries and source patch checks pass.
- All intended changes committed and clean. No long build/test yet.
- No CI or deployment result claimed. No integration approval requested/granted.

Remote existing CI workflow resolved read-only before publication:
`vpsfreecz/vpsadminos`, workflow `162100852`, `.github/workflows/ci.yml`,
state active. A future observed run must bind exact candidate head and positive
run attempt; do not follow moving branch latest state as final proof.

No source changes since review release: lead rechecked final OS head, clean
status and exactly two logical commits. Review source identities remain current.

Before OS publication, remote branch runs query remains empty (expected; no
push yet). No existing CI is silently pending behind review.

Independent final review passed source/process/catalog/history with one narrow
documentation Advisory, no Blocking/Important findings. A1 export clarification
is being folded into P; final OS head/derivation will change while Linux pin and
flake graph remain equal. Bind CI to the resulting final head and new derivation
rather than assuming the original revision-bearing OS closure is identical.

## Published current final head and operations

Final ba7e99b5e3d435826bd387e64f1c1a6ec173169c retained after user reversed
unpublished README removal. Local/remote clean and equal; no superseding push.
Both ordinary/explicit target closure now
/nix/store/1xz2kh8yvxaijd57mwkdk2wb0d1mgif8-vpsadminos-system-vpsadminos-26.05.git.ba7e99b.drv.
Main CI run44120817659 attempt1, workflow162100852. Runtime observer
e499c41c-7ad3-48cb-a40b-aef8502bcaf9 acknowledged runtime-ci, durable observing.
Companion docs run44120817623 observer34708386-f302-4679-99e4-1cc1fc8fdc2d;
qualification run44120818064 observer21973214-5205-477b-a4f5-f0ba3dc97d15.
No redundant native watcher/local compile. MCP ownership refusal resolved via
supported CLI using independently verified exact native caller/root environment,
no session identity adoption or policy bypass. Build/VM outcome remains pending.

## Documentation CI passed

Runtime operation34708386-f302-4679-99e4-1cc1fc8fdc2d observed workflow418457005
run44120817623 attempt1 conclusion success on exact final OS
ba7e99b5e3d435826bd387e64f1c1a6ec173169c. Durable terminal event and accepted
lead-turn receipt verified. Evidence:
https://github.com/vpsfreecz/vpsadminos/actions/runs/44120817623/attempts/1

Main CI44120817659 attempt1 remains in progress, currently NixOS persistent
activation prerequisite; target closure compilation/runtime not yet proven.
Qualification44120818064 attempt1 remains queued. Both exact-head runtime-ci
observers remain registered. No failures or source edits, no duplicate watcher
or tests, no integration/deployment/lifecycle action. Next: main CI outcome
and actual target/selected-case evidence.

## Failed qualification attempt

Exact run44120818064 attempt1 failed during producer capture (job134174364543,
step6), before consumer qualification. Discovery succeeded; final row-receipt
closure failed consequently. Root cause/relevance not yet known. Read-only D2
owner architect0 inspects failed logs and unchanged/changed input provenance
before proposing remediation. No blind rerun. Main target CI remains active.

## Qualification failure classified

[Exact failed-attempt diagnosis](qualification-failure.md) accepted. Selected
retained6.12.113 campaign; pre-existing evidence guard failed before producer
realization. Workflow/tools/target/locked inputs unchanged. Unrelated baseline
CI staging collision, not kernel compile/runtime failure; qualification remains
failed/unrun and is not reused as coverage. No cleanup/rerun or workflow edit.
Main exact-target CI progressed to toplevel build16:15:11Z; outcome pending.

## Final completed CI evidence — package V

Owner: implementer0. This receipt supersedes the earlier pending product-check
status above; it does not change review/source history or authorize integration.
Read the completed exact-attempt job metadata/logs, not a moving branch result.

- Repository/workflow/run/attempt: `vpsfreecz/vpsadminos`, workflow `162100852`,
  `.github/workflows/ci.yml`, run `44120817659`, attempt `1`, **success**.
- [Exact attempt](https://github.com/vpsfreecz/vpsadminos/actions/runs/44120817659/attempts/1).
  Both job records bind OS `ba7e99b5e3d435826bd387e64f1c1a6ec173169c`.
- Build job `134171356716`, `gh-runner3.int.vpsadminos.org`: success,
  `2026-11-17 16:00:37–17:17:43 UTC`; build, checks, cache copy and profile-generation
  steps all success.
- Test job `134223368327`, `gh-runner1.int.vpsadminos.org`: success,
  `2026-11-17 17:17:45–19:37:07 UTC`; run-tests, evaluate-results, summary and cleanup
  steps all success. Successful whole-suite full-log artifact upload is skipped
  by workflow policy; run artifact API returns zero artifacts.

### Actual build and input identity

Build log checkout/final HEAD lines 105–133 bind the exact final OS commit.
The test log independently prints `Source: ba7e99b5e3d435826bd387e64f1c1a6ec173169c`
and tree `3d07ec50b7dc1cd298e6b52631c0e40ca62a8a23` (lines 248–249), matching
read-only local Git identity. Fresh SSH `git ls-remote` reads independently confirm
OS topic at that head and Linux topic at
`3bba27296b6f4f4a2b1568d65cea6037368f229b`.

Build actually ran `make OUTPUT=ci-toplevel toplevel` with empty
`VPSADMINOS_CONFIG` (build log 441–457). Its built system derivation (537, 730):
`/nix/store/1xz2kh8yvxaijd57mwkdk2wb0d1mgif8-vpsadminos-system-vpsadminos-26.05.git.ba7e99b.drv`.
This exactly matches the previously proven ordinary/explicit `.118` target
identity in [catalog evidence](catalog-evidence.md). Realized `BUILD_OUT` (739,
804), also copied to the binary cache (793):
`/nix/store/8abp9lh9skqgrjz2j3zm5spi1cnky5qv-vpsadminos-system-vpsadminos-26.05.git.ba7e99b`.
Cache copy and generation registration succeeded; this is the CI cache profile,
not a production deployment.

The build log records the actual final Linux source derivation (462, 680):
`/nix/store/ppllxmkasqg8mws4rryw1a20b0kcz3r9-3bba27296b6f4f4a2b1568d65cea6037368f229b.tar.gz.drv`.
It built both Linux 6.12.118 package paths (717, 722):
`/nix/store/61h04f41dsq8sgxj87kiyx5s2hr97chm-linux-6.12.118.drv` and
`/nix/store/3slqrmfmm3jqz8x99rcvi2qr10y3w1dq-linux-6.12.118.drv`.
Cache-copy log includes both kernel outputs and dev outputs
`/nix/store/1g6kr0gqjvsyd8akxg2w5d3w7r1qbc3m-linux-6.12.118-dev` (759) and
`/nix/store/j11d2aiaij1av4l7wzlkw33hmzbfw1mg-linux-6.12.118-dev` (769), as required
by the existing CI closure.

Test log 253 and 296–313 prints stable `6.12.118`, exact Linux revision above,
raw archive hash `sha256-tXgl0RdF3YigscvXI/tD5QHbujUV+6bVW+KIyESG93U=`, retained
ZFS `481845fca6ae3f61ca2262c1a5693a58ae364650`, its existing hash and
`zfs235-free-account.patch`. These match the reviewed/fixed-output source and
unchanged complete locked input graph in catalog evidence; V changed no pin,
flake input, configuration or migration.

### Actual selected tests and results

The test log explicitly records `Native suite: ci`, empty `Configuration:`,
`Native test pattern: <whole suite>`, tag `ci`, and prebuild enabled (244–248,
366). The selected list includes all four named cases (609, 659, 680, 713), and
subsequent running/terminal-result lines prove they executed:

| Actual case | Successful examples | Terminal success UTC / duration | Evidence in sanitized test log |
| --- | ---: | --- | --- |
| `osctl/nfs-cancellation` | 66/66 | `19:28:16`, 4726.68 s | running 857; examples span NFS 3, 4.0, 4.1 and 4.2; terminal 5368 |
| `system/boot/stage-2` | 4/4 | `18:45:14`, 48.97 s | running 2583; examples 2609–2614; terminal 2629 |
| `kernel/module-autoload` | 16/16 | `19:09:16`, 227.33 s | running 4429; examples 4624–4871; terminal 4932 |
| `zfs/boot-modes` | 2/2 | `19:00:29`, 113.96 s | running 3250; external example 3302; builtin example 3440; terminal 3441 |

All requested example indices are present exactly once with successful results.
NFS includes post-publication NFSv3 failure cleanup, cold NLM shutdown, blocked
mount/lock cancellation, processless child namespaces, sibling isolation,
terminal admission/idempotence, daemon restart and 25 stop/restart cycles for
each tested NFS version. Stage-2 covers boot records and absence of console
modprobe errors. Module-autoload covers disabled/enabled requests, activation,
explicit host loading and runtime toggling. Both ZFS examples boot and verify
provider resolution, release equality and payloads through snapshot, clone,
rollback, send/receive and cleanup in their exact-head test source.

Final log 5378–5379: `Run 324 test scripts of 110 tests in 5264.1 seconds` and
`110 tests successful`. Independently counted 110 unique terminal successful
tests; final statuses report zero expected failures and zero unexpected results.
The existing nonempty-result/unexpected-result evaluator succeeded. This records
actual selected results rather than inferring coverage from the workflow title.

### Evidence limits and retrieval

Successful job output includes per-example results, not detailed guest shell
stdout. It does not print raw `uname`/security-evidence output or individual VM
kernel paths. The exact-head NFS fixture forces the stable kernel and its
mandatory before-suite checks require `uname -r == 6.12.118` and
`kernelSourceRevision == 3bba27296b6f4f4a2b1568d65cea6037368f229b`; its 66 passing
examples establish those checks completed. This is enforced test evidence, not a
separately retained guest transcript. ZFS examples likewise enforce configured
release/module-provider identity, but explicitly do not attest already-loaded
module bytes. Stage-2 and module-autoload use normal default selection in the
logged empty override profile; no separate runtime identity assertion/transcript
is available for those guests. Do not claim every one of the other 110 CI tests
used this stable kernel; some intentionally select other versions. No production
rollout/rollback or full ZFS suite is established here.

Job logs retrieved once successfully from `actions/jobs/134171356716/logs` and
`actions/jobs/134223368327/logs`; attempt-specific job-list API establishes their
membership in attempt 1. Initial one-time native downloader was stopped by the
`gh` escape-output guard with no log data and no surviving operation. The
observed guard was resolved using `gh api --allow-escape-sequences` with output
redirected locally; control sequences stripped before bounded inspection. Both
successful retrievals completed exit 0; no observer, polling, rerun or test.
Disposable local files:

- `/tmp/stable-kernel-v-run.json`, `/tmp/stable-kernel-v-jobs.json` — exact metadata.
- `/tmp/stable-kernel-v-build.raw` (89,825 bytes), `.log` (845 lines); raw SHA256
  `7611e6d03bef5ad1b493fc3a8f9be117e63ff40207806e9e02683660f76db4df`.
- `/tmp/stable-kernel-v-test.raw` (1,040,113 bytes), `.log` (5,538 lines); raw SHA256
  `b52e20c4039e6bd8d43534eea2fe0e50119dbc01bcf58bd7ba96464fc1a81941`.

All V operations joined; no source/index/commit, new test/build, remote mutation,
integration, deployment or lifecycle action. No migrations and no pin changes in
V. The separately diagnosed retained-6.12.113 qualification failure remains
failed/unrun, outside these passing results; no rerun or expanded investigation.

## M-prep: mechanical target refresh, parked for publication instructions

Owner: implementer0. User authorized merging vpsadminos into staging; lead owns
the repository claim and final fast-forward/push. No claim or default mutation
occurred during this preparation. Selected runtime guide read in full from
`/nix/store/3shank2g0lxy3xnlh282djq0kjsbzanr-dev-workspace-0.2.0`, coordination
catalog `sha256:dd6201266035c6c6eedb0a3f39890a9b5e9ee3ad316345149ba700af9ee2f2bf`.

Fresh fetch found staging advanced from original base
`a7d71a54a15496976cb0fccebb8a1b589f24f5e2` to
`42baba6117bebcde3d04555a71377381df197925`, one automatic exporter dependency
commit (`puma` 8.1.1 -> 8.1.2). Only exporter Gemfile.lock/gemset.nix differ;
no feature-path overlap. Under lead-authorized routine refresh, backed up old
reviewed/published `ba7e99b5e3d435826bd387e64f1c1a6ec173169c` at
`refs/heads/backup/2026-11-17-stable-kernel-update/os-before-staging-refresh` and
cleanly rebased both commits with `--no-update-refs`, ordinary hooks/no bypass.

Prepared old/new reviewed ranges:
`a7d71a54a15496976cb0fccebb8a1b589f24f5e2..ba7e99b5e3d435826bd387e64f1c1a6ec173169c`
-> `42baba6117bebcde3d04555a71377381df197925..ba6837de511ef9364fa4126e24c91de0251f33ad`.
Native range-diff both `=`; ordered stable patch IDs match exactly:
`2db8d4efb037274f546e2db40ec70a0e3229aef9`,
`b998184fc36308eed8109b439721dbe324a0df0b`.
Prepared two commits: `b7450cfdd2ab3f742291c891148f7fd23cb754a7` (process),
`ba6837de511ef9364fa4126e24c91de0251f33ad` (catalog).
No migrations or intermediate pins. Final trees differ from old published head
only in the two exporter baseline files. Complete flake.lock, kernel catalog,
Linux builder/config and ZFS owner source files byte-equal.

The same full native profile evaluation used by R confirms stable/external,
retained and unstable Linux drv/source records unchanged. All ZFS built-in,
external and user drv/source identities match the accepted CI receipts; displayed
patch root path reflects the new repository snapshot but patch bytes and
resulting derivations remain identical. Stable Linux
`/nix/store/3slqrmfmm3jqz8x99rcvi2qr10y3w1dq-linux-6.12.118.drv`, external Linux
`/nix/store/61h04f41dsq8sgxj87kiyx5s2hr97chm-linux-6.12.118.drv`, ZFS built-in
`/nix/store/x4468m97719ik8lpjfjmck2gki0znrf8-zfs-builtin-2.3-vpsadminos-6.12.118.drv`,
external `/nix/store/1fwpcyi837hv9nam8zfzzx3s33dz3gvq-zfs-kernel-2.3-vpsadminos-6.12.118.drv`,
and user `/nix/store/vpvdy6pbvk68j5kl9djr2za8pj9w71zz-zfs-user-2.3-vpsadminos.drv`.
Immutable drv identity retains the complete corresponding input/configuration
scope; source identities and full locked graph remain as the R/V receipts above.
Raw evaluated receipt: `/tmp/stable-kernel-m-kernel-identities.json`.

Prepared Git-flake OS closure derivation differs as expected with exporter base
and source revision:
`/nix/store/r3xbryiglfsld4ll0c67z20xd9as43i6-vpsadminos-system-vpsadminos-26.05.git.ba6837d.drv`.
The accepted full CI tested the old exact OS closure, not this refreshed whole OS.
Its preserved kernel/ZFS/input and unchanged test-source results are reusable
within their proven scope; no blind full CI or runtime retest was run here.

Quick checks: range/tree/patch-ID proofs, diff check, narrow
`overcommit --diff 42baba...`, skill quick_validate and make doc (0.97 s) all pass.
First narrow hook attempt found GC'd declared nixfmt; restored only the exact
missing declared tools from caches and repeated the failed hook successfully.
No shell/source/tooling redesign. Git, make, Ruby, Nixfmt and MkDocs outputs are
pinned by `/tmp/stable-kernel-merge-tools*`; environment prefix
`source /tmp/stable-kernel-merge-env.sh` uses declared exact paths and source
worktree `.gems`, with GEM_PATH/RUBYOPT unset. No all-files scan or test/build.

Fresh owned target:
`worktrees/2026-11-17-stable-kernel-update/vpsadminos-merge-target`, clean detached
HEAD at exact staging `42baba6117bebcde3d04555a71377381df197925`.
Declared Overcommit trust prepared; ordinary post-merge and pre-push hook
invocations pass. There is no declared pre-merge-commit file; ordinary ff-only
merge invokes the installed post-merge hook and does not create a commit.
Comparison captured new base -> prepared head. Lead's later critical section
would recheck refs/cleanliness before `git merge --ff-only FINAL` and
`git push origin HEAD:refs/heads/staging` from this target using the prefix.
No merge/push/claim/default ref or Linux mutation performed by M-prep.

**Parked:** user now requires uniform Linux branch-only publication instructions
and a naming scheme before OS integration. Lead/architect own the sufficient
correction brief; no source change is invented here. Prepared feature remains
clean at `ba6837de511ef9364fa4126e24c91de0251f33ad`; remote topic remains old
published head. No feature force-push yet. All owned commands joined; source-edit
capacity confirmed for the separately dispatched correction. Existing target and
receipts are retained; no cleanup or lifecycle action.

## Post-integration current head

Remote staging integrated exactf33f5fd10b53232b5670862f832f4ec5ea835e84 after
D3 review/no findings, fresh target checks, ordinary ff-only merge/hooks/push and
remote proof. Repo claim explicitly released/verified before CI/records. New
staging main CI44167132711 attempt1 workflow162100852 on exactf33f5fd is queued,
registered runtime-ci observera4162505-8c79-4f38-89d7-f611018ed671. Prior passing
source/kernel/runtime evidence remains bound to original exact receipts and
unchanged derivations; no new-head whole-system success inferred yet.

## D5: exact integrated-head CI lost its runner

Owner: architect0; bounded read-only diagnosis, 2026-11-17. No code fix is
justified by the available evidence, so no new implementation brief was added
to design.md. No CI mutation, rerun, build, SSH, deployment or lifecycle action.

[Main CI run 44167132711 attempt 1](https://github.com/vpsfreecz/vpsadminos/actions/runs/44167132711/attempts/1),
workflow `162100852`, tested OS
`f33f5fd10b53232b5670862f832f4ec5ea835e84`. Runtime observer
`a4162505-8c79-4f38-89d7-f611018ed671` reported terminal failure; D5 did not
register another observer.

- Build/cache job `134336075924` **passed**, 20:32:50–20:37:38 UTC, on
  `gh-runner1.int.vpsadminos.org`.
- Test job `134350733756` started 20:39:45 UTC and was marked failed by GitHub
  at 21:39:53 UTC on the same named runner, ID `10650`, label `self-hosted`.
- Step 4 “Prepare test state” passed at 20:39:51 UTC. Step 5 “Run tests” still
  has API status `in_progress` and null completion. Upload, result evaluation,
  summary and cleanup steps remain pending in the terminal job metadata.
- Check-run `134350733756` has one failure annotation:

> The self-hosted runner lost communication with the server. Verify the machine
> is running and has a healthy network connection. Anything in your workflow that
> terminates the runner process, starves it for CPU/Memory, or blocks its network
> access can cause this error.

This establishes runner communication loss, not a specific test failure. The
listed process/resource/network conditions are GitHub's possibilities; none is
proved. The roughly one-hour terminal interval is not the configured test timeout:
the unchanged workflow gives an ordinary full `ci` job 360 minutes and its run
step 350. No failing assertion, last completed test, guest failure or runner-local
resource event is available yet.

### Evidence availability and exact comparison

One job-log API request returned HTTP 404 with Azure `BlobNotFound`; it was not
repeated. A separate full-attempt archive read succeeded but contains only
`1_Build OS and populate binary cache.txt` and its `system.txt`, no test logs.
The attempt artifacts API returned an empty list. Thus absent test artifacts
cannot distinguish a failing workload from a runner/host interruption. Raw reads
were redirected before sanitization; disposable paths:
`/tmp/stable-kernel-d5-44167132711-job.log` (215-byte error response),
`/tmp/stable-kernel-d5-44167132711-attempt.zip` (5,823 bytes, build logs only).

Accepted prior run `44120817659` at
`ba7e99b5e3d435826bd387e64f1c1a6ec173169c` passed. Its test job
`134223368327` used the same named runner and passed 17:17:45–19:37:07 UTC;
its build job `134171356716` passed on runner3. Earlier V records retain its
110-test result and exact derivation/input scope.

Direct old/new Git blob/tree comparison proves these inputs identical:

| Path | Same object at prior tested and current head |
| --- | --- |
| `.github/workflows/ci.yml` | `e68b5b301d71e475420615517ec7512a4797973d` |
| `.github/actions/prepare-test-state` | `ba83f4a9d56c7f67246869b723f524a8dff645d3` |
| `test-runner` | `c31aa3c79a51fc505e4ebad5f16a04970a644e1a` |
| `tests` | `cd8a336af599e2a33d15ccd5856314fd9d5c193c` |
| `flake.lock` | `3db52b818025eaedb416fff0ac082d62af632ff6` |
| `flake.nix` | `74a87d96d5e3acdb95a44b322b7f551a9b283ee5` |
| `os/packages/linux` | `a428f62427c11570387a485b0298af56f7cd76a8` |
| `os/packages/zfs` | `6484b1f04ad36076890d58f1fdc0677fe9dfb9fb` |

The entire head-to-head delta is publication instructions in AGENTS/runbook/skill
and baseline exporter `puma` 8.1.1 → 8.1.2 in its Gemfile.lock/gemset. Linux
6.12.118 source, catalog/hash, configuration/builders, tests and locked Nix graph
are unchanged. This supports reuse within the already recorded kernel/input
scope; it does not prove this interrupted suite or the new whole OS passed.
There is no evidence linking communication loss to the kernel port or puma
change, and no evidence excluding workload-induced resource exhaustion either.

### Authoritative host and bounded inspection handoff

Configuration sources, rather than the GitHub label alone, establish the endpoint:

- `vpsfree-cz-configuration` at base `9c6a0313...`,
  `cluster/org.vpsadminos/cluster.nix`: unmanaged mirror
  `org.vpsadminos/int.gh-runner1`, FQDN `gh-runner1.int.vpsadminos.org`, address
  `172.16.4.21`, container `27535`.
- Owning `vpsadminos-org-configuration` locally retained `origin/master`
  `15352aeb13c4011b5dd1a1f78d1fdcb08f7c2420`,
  `cluster/org.vpsadminos/int.gh-runner1/module.nix`: same FQDN/address;
  adjacent `config.nix`: GitHub runner name is that FQDN, imports
  `configs/gh-runner.nix`.
- Its `environments/base.nix` enables SSH and root access for configured
  admin/builder keys. Intended endpoint is therefore
  `root@gh-runner1.int.vpsadminos.org` (`172.16.4.21`), not a guessed runner label
  or physical node. Reachability and current deployed revision remain unverified.
- `configs/gh-runner.nix` declares `services.github-runners.runner`, user/group
  `github-runner`, runtime `/run/github-runner/runner`, job marker
  `/run/github-runner/runner/job-active`, and separate GC service
  `github-runner-nix-gc`. Do not read its credential file or process environments.
- The exact OS prepare-state script computes
  `/tmp/os-test-runner-109335108-44167132711-1` from repository ID `109335108`,
  run and attempt. `test.log` is the stream log. The default state root is `/tmp`;
  no workflow override is declared. Verify service namespace/PrivateTmp before
  treating host `/tmp` as the service's `/tmp`.

Smallest next package, if lead assigns implementer0: one bounded read-only host
inspection. Use ordinary trusted SSH configuration with batch mode and a short
connection timeout; failure to connect is an access finding, not permission to
try unrelated hosts. First establish uptime/current time and list only
`github-runner*` units. Inspect the actual runner unit's `MainPID`, state,
`Result`, `ExecMainStatus`, `WorkingDirectory`, `RuntimeDirectory`,
`StateDirectory` and `PrivateTmp` fields (expected unit naming must be verified).
Read bounded UTC journal excerpts for runner and GC units in
20:35–21:45 UTC; read kernel/OOM/reboot evidence for the same interval. Record a
reboot or absent prior-boot logs honestly.

Then inspect only the exact runtime and attempt-state roots: marker timestamps,
current related runner/test/QEMU processes, tail of the exact `test.log`, and
recent diagnostic filenames under the actual runner working directory's `_diag`
if present. With PrivateTmp, resolve the live service's view via its verified
MainPID or reported namespace rather than broad `/tmp` searches. Preserve any
still-running job and its files even though GitHub is terminal. Read only the
few diagnostics relevant to run/job/time, redact tokens/headers/URLs, and return
last test/progress plus runner disconnect/resource evidence. No service restart,
process kill, state cleanup, runner repair, rerun or expanded fleet inspection.

The inspection is the next evidence source needed to choose recovery. D5 does
not authorize that SSH execution itself. The exact-head build/cache is green;
exact-head runtime suite completion and cause of runner loss remain unresolved.

## I5: runner-local causal inspection

Owner: implementer0, bounded read-only assignment after accepted D5. Trusted SSH
`root@gh-runner1.int.vpsadminos.org` succeeded with `BatchMode=yes`,
`ConnectTimeout=10`, `ConnectionAttempts=1`, `StrictHostKeyChecking=yes`. No
access provisioning or SSH trust override. Configuration source inspected
read-only at org-config `15352aeb13c4011b5dd1a1f78d1fdcb08f7c2420`; that revision
has no AGENTS.md (commands derived from config and existing runner-GC note).
Current deployed system reported by readlink:
`/nix/store/5m6ig5my7vfb1mi5wxx01lsrhici5qw9-nixos-system-gh-runner1-26.05.20261021.da6dc0e`.
Do not infer that this is the retained config Git head. Observations made
21:46:04–21:48:09 UTC on 2026-11-17; host uptime about 30 days, no reboot during
this CI interval.

### Observed causal sequence

Actual unit is `github-runner-runner.service`. It reports failed/failed,
`MainPID=0`, `Result=signal`, `ExecMainStatus=6` (ABRT), empty ControlGroup,
`PrivateTmp=yes`, WorkingDirectory/RuntimeDirectory `/run/github-runner/runner`,
StateDirectory `github-runner/runner`. Journal, bounded 20:35–21:45 UTC:

- 20:37:38: prior exact-head build completed Succeeded.
- 20:39:45: runner started `Run test suite`, matching failed job `134350733756`.
- **21:39:53.387319:** `Runner.Listener[3666593]` unhandled
  `System.IO.IOException: Disk quota exceeded` while writing
  `/var/lib/github-runner/runner/_diag/Runner_20261104-190345-utc.log`.
  Stack is the runner's diagnostic write/flush path.
- 21:39:53.429170: systemd reports main process killed, status `6/ABRT`;
  21:39:57.779388: service failed with result `signal`.

This directly connects runner communication loss to a runner diagnostic write
rejected for quota/capacity, followed by its abort. It is an infrastructure
failure, not an observed failed test assertion. The precise quota property,
which path filled it, and whether an earlier exception was being logged are not
established. Container-visible kernel journal query found no matching OOM/panic/
reboot entry in that bounded interval; this does not exclude physical-host events
outside that journal's visibility. Reported 91.5G memory/6.3G swap peaks are the
long-lived unit's aggregate, not this job's proven peak or an OOM diagnosis.

### Capacity recovery and unfinished-work accounting

At 21:47:25 UTC, `df -h` for `/var/lib/github-runner/runner`, `/tmp` and `/nix/store`
reports the same `tank/ct/27535` backing dataset, 352G size / 28G used / 325G
available. At 21:48:09, it reports 24G used / 329G available (7%); `df -i` shows
2,981,501 used / 689,622,470 free (1%). `findmnt -T` identifies ZFS
`tank/ct/27535[/private]`, root mount. No numeric ZFS quota was guessed or changed.
The failure-time capacity is not reconstructed from these later samples.

Existing `github-runner-nix-gc.service` was already active when first inspected.
A final bounded GC journal read shows **21:47:51.772551**: `46756 store paths
deleted, 360.3 GiB freed`; systemd marks it Finished at 21:47:51.801157. This
supports substantial automatic capacity recovery after failure; I5 did not
start GC or delete anything. Current ample capacity does not prove the original
write could succeed before that collection or establish the exact quota limit.

No processes under runner user remain. Global bounded comm-only process read
also finds no Runner.Listener, Runner.Worker, test-runner, QEMU or virtiofsd.
Failed service has no MainPID/cgroup, so no live namespace can be entered. A
service-specific `/tmp/systemd-private-*-github-runner-runner.service-*` lookup
found no surviving private root; exact host
`/tmp/os-test-runner-109335108-44167132711-1` is absent too. No live original job
or preserved exact-attempt test.log/test-result files were found. Runtime
job-active marker is absent. These are observations after unit failure, not a
claim that I5 cleaned or canceled the job.

Relevant persistent diagnostics remain: Runner log (~4.67 MB), and exact worker
`Worker_20261117-203946-utc.log` (~316 KB). Read only bounded tails. Runner job
renewal continues through 21:28:53; worker tail reports successful console-batch
uploads through 21:29:41, then no terminal record in the tail. These records do
not retain the actual last named test or any terminal test count. No token,
credential file, process environment or unrelated job payload was read.

### Actual reads, evidence limits and next action

Remote read-only commands were `date -u`, `uptime`, `readlink`, narrowly filtered
`systemctl list-units/show`, bounded UTC `journalctl` for runner/GC/kernel,
comm-only `ps`, exact marker/state `stat/find/tail`, and `df -h`/`df -i`/`findmnt`.
First SSH batch exited 1 because the no-match kernel `journalctl -g` status
stopped a fail-fast script after its causal journal reads, before planned state
reads. A bounded continuation completed those remaining reads exit0; cheap final
capacity/worker/GC-boundary read exit0. All SSH/tool sessions joined, stderr empty,
no surviving or uncertain effects. Sanitized local evidence:
`/tmp/stable-kernel-i5-runner.log`, `...-state.log`, `...-final.log`; raw bounded
captures retained locally mode0600. No source/index/commit/pin/migration edit,
service/process mutation, restart, kill, cleanup, rerun, claim or deployment.

The exact f33f5fd build/cache remains passed; this interrupted exact-head runtime
suite remains **incomplete**, with no recovered selected-case terminal coverage.
Prior accepted 110-test run's scoped evidence is unchanged and must not be
relabeled as this attempt. No kernel/Puma causal connection was observed, and no
source fix is justified by this inspection.

Smallest next action: separately assign the runner operator bounded capacity/
quota-headroom assessment and, if authorized, ordinary runner service recovery.
Before any mutation, use the normal ownership/resource requirements, recheck
automatic GC terminal state and absence of original processes, preserve diagnostic
evidence, and establish adequate reserve for the expected workload. No destructive
cleanup is indicated by current capacity. A later intentional test rerun should
follow runner health/recovery verification under its own authorization; I5 does
not start it or prescribe an unmodified blind retry. Lead owns that decision.

### User disposition after I5

User explicitly said "well it already passed on the previous branch, so let it
be". Leave runner and failed attempt unchanged; do not recover or rerun for this
task. Earlier passing110-test evidence and exact unchanged input/derivation scope
remain recorded above. Current interrupted attempt remains failed/incomplete,
not a new successful test result. No further verification work assigned.
