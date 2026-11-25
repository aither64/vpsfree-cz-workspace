# node24 kernel investigation synthesis

The [CI duration finding](design.md#ci-duration-finding) explains the nine-hour
workflow age through sequential AMD allocation and unchanged four-hour aging
workloads. At the fixed 20:32:55–57Z snapshot, aged-v5 had waited 4h 37m and run
4h 38m; two other AMD jobs still had no runner/steps. Matched prior successful
aged jobs took about 4h 42m–4h 49m. The earlier bootarg-only `b81c` run lasted
12h 41m overall, with all nine livepatch jobs passing and almost 12 hours of
sequential AMD execution. No new execution-duration regression or hang is
established by this evidence.

The [history](ci-duration-history.md) covers 15 completed push runs and 72 AMD
job records, with cancelled/unexecuted cases separated; strong aged success
samples are only two per variant. The [source analysis](ci-duration-source.md)
confirms unchanged workload/runner logic but different OS/input pins. At the
snapshot the active step remained inside its 350-minute limit; its projected
cutoff was 21:45:02Z (job 21:54:58Z). Inner guest progress remains unobserved, so
these limits are not proof of health or an ETA. Implementer2 retains the sole
observer; no new execution, cancellation or source change is selected. The
completed merge and separate failure investigation are unchanged.

The [module-autoload compatibility review](design.md#module-autoload-compatibility-finding)
finds that ordinary `boot.kernel.moduleAutoload` settings are preserved: activation
and sysctl replay select the same denying/loading wrapper, or empty helper for
silent denial. No runtime fix is indicated. Saved current-head CI passed all 16
autoload examples and all eight generic sysctl examples, but the
[coverage matrix](module-autoload-test-coverage.md) identifies missing explicit
service-restart/policy-switch interaction and silent-mode assertions. The narrow
proposal is to extend the existing fixture, not change runtime machinery.
Explicit conflicting sysctl inputs retain precedence/ordering caveats; unchanged
activation can rewrite `kernel.modprobe` even when service replay is skipped.
This review ran no tests or host operations and leaves the separate CI-failure
investigation untouched.

**Merged:** vpsAdminOS `staging` advanced fast-forward from `55c50465` to
`846bb469505789ba0b2a405fa5905ba6d8253006`. The lead inspected successful
hooks/push and remote feature/staging proof at `2026-10-22T17:19:40Z`; the
repository claim was confirmed released at `17:19:57Z`. The user explicitly
accepted the observed CI failures for this merge; CI remains red.

Root causes, recurrence, solutions and the tests' purpose/usefulness are handed
off to the created
[2026-10-22-ci-failure-analysis session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/),
with its verified four-implementer team, architect and reviewer.
Implementer2 retains this session's current CI observation at 600-second cadence
through terminal status.
The [handoff and proposed lanes](design.md#separate-failure-investigation-handoff)
preserve existing evidence and history pointers. Expanded historical collection
has not started in this session. Earlier blocked-gate/unmerged statements below
are historical; no broader recurrence rate, harmlessness or exclusion of current
contribution is claimed. No deployment, pin change or lifecycle action occurred;
the session remains open.

## Pre-merge evidence and historical checkpoints

Second failed current-head CI job: `kernel/livepatch-qualification@amd-scale-aged-v6`
failed its final dmesg no-fault assertion on `Dying CPU not properly vacated!`
while offlining CPU127. The [pinned-source finding](design.md#amd-livepatch-hotplug-warning-boundary)
identifies a scheduler teardown invariant: only one runnable task and no
migration-pinned tasks should remain. The dump records two runnable tasks but
names only `migration/127`, so the excess task/callback is unknown. This warning
path continues and returns 0; successful offline/online commands and subsequent
progress do not establish harmlessness.

The warning preceded incoming v7 activation; that activation later completed
once in 757.998 seconds within its 1800-second bound. Its execution is excluded
as the cause of the earlier warning. The guest already ran current `846bb469`
OS with the frozen 6.12.95 kernel and v6 livepatch, so generic sysctl boot-state
effects remain unresolved: supervisor presence/down is recorded, but actual
application output and value history are missing. No source repair or rerun is
selected, and the merge gate remains blocked. Implementer2 owns the consolidated
log evidence and existing CI observer; this interpretation launches no new work.

Current accepted source is generic v3
**`846bb469505789ba0b2a405fa5905ba6d8253006`**, tree
`df9bd828d843225df749b7a05ed9529bf17425c9`, on unchanged base `55c50465` and
panic parent `85282623`. [Final independent review](generic-sysctl-final-review.md)
accepted all four HIGH-risk lanes with no findings, including complete history,
no migrations and no repeated update streams. **Normal declared-environment
SSH publication and remote-ref proof are complete; staging remains `55c50465`.**
**The focused `846bb469` VM command passed with durable exit 0: eight of eight
examples and the single test succeeded.** The selected run started
`2026-10-22T11:08:31Z` and ended `11:14:33Z` (362 seconds wrapper elapsed,
353.17 seconds runner elapsed). The lead directly inspected the current log,
exit receipt and clean source. The accepted
[final VM binding receipt](generic-sysctl-focused-vm-846bb4695-receipt.json)
matches all six changed files in the actual frozen runner to exact `846bb469`
blobs and the worktree. The native configuration contains the corrected boot
wait, EINVAL probe and single-attempt assertion; current `expected_success`
at `11:14:33Z` agrees with exit 0 and all eight passing examples. Older
`89587060` diagnostic timestamps are historical. **Exact-head CI `39767770407`
is not green:** product job `119793311317` failed at `2026-10-22T14:42:27Z`
after 3h 6m 41s; other jobs remain active. The conditional merge gate is blocked.
The product summary is 124 passes and six failures. The
[bounded causal finding](design.md#current-product-ci-causal-boundary) separates
five recurring impermanent-dataset mismatches from the nested-container timeout.
No claim, merge, rerun, source edit or broad repair is
selected. The focused 8/8 pass remains separate evidence, and production runtime
behavior is unverified.

The five dataset cases retain kernel/boot identity and container init PID across
successful userspace switching, but report the base dataset instead of the saved
impermanent clone. The same five signatures predate the generic service in
[preserved b81c evidence](os-hardlockup-ci-failure-analysis.md); the inspected
upgrade/export/run-configuration/switcher source is unchanged. This establishes
prior occurrence, not exclusion of a current contribution. Unlike the old
boot-only change, the new service can run during this live-switch path.
Postfailure supervisor/logger presence and down status are recorded, but actual
service output, completion stamps/checks and sysctl readbacks are missing.
Current service contribution and the precise dataset/mount cause therefore
remain unresolved. Implementer2 owns the consolidated failure record. No
material fix is justified by signature matching alone.

The [independent nested-timeout analysis](generic-sysctl-ci-nested-podman.md)
establishes a separate pre-activation failure: the predecessor's container
DHCP client reports a seccomp permission error, interface setup fails, and the
guest has no IPv4/default route. The fixture stops in readiness before target
activation, so the incoming generic sysctl service did not execute in this
failing path. The exact denial mechanism and introducing component remain
unknown. This exclusion does not resolve the five post-switch dataset cases
or satisfy the failed CI merge gate.

The user explicitly approved CI checks about every ten minutes and merging
when done. The lead's recorded scope is **vpsadminos into registered `staging`
after successful exact-head CI**, with a final freshness gate before the short
repository claim. Implementer2 owns the existing watcher cadence and unlocked
target/hook preparation. The merge has not occurred. This approval does not
authorize deployment, pin changes, configuration-repository integration or
session lifecycle actions; older no-integration statements below are historical.

This revision fixes a reproduced missed restart for an ordinary literal
`environment.etc.source` path. Editing its contents at the same pathname
changes the etc renderer's store snapshot while `toString` leaves the generic
service's identity/triggers and run/check paths unchanged. The
[approved narrow correction](design.md#literal-source-content-tracking-correction)
uses `"${file.source}"`, matching the pinned renderer, with a short comment.
Implementer2's same-path regression proof passes: canonical source, identity,
triggers and generated run/check paths now change, with all ten ordinary
variants stable. The coherent v3 commit includes the corrected negative probe
below. No new framework or string-path policy is involved.

The second VM run against frozen `89587060` inputs booted and passed six normal
examples. Two negative assertions exposed an invalid injection: pinned procps
4.0.6 `--system` ignores a nonexistent key's `ENOENT`. Implementer0 corrected
the probe to an invalid integer for a known key (`EINVAL`), and its graph,
render, Ruby syntax and format quick checks pass. These failures do not establish
a service defect, and the old run cannot certify the corrected probe or literal
source fix. Native `unexpected_failure` is explicit; the outer exit status is
unavailable. This is not a passing full VM result.

Commit, final review, publication and the corrected focused VM are complete.
The existing watcher `01a1634c-0553-7530-ba30-b19cfc2307d0` owns only the remaining
exact-head CI `39767770407` jobs; architect0 starts no observer or duplicate
diagnosis. Earlier checkpoints
below remain historical evidence. No production runtime change occurred;
the session remains open, unmerged and undeployed.

Earlier accepted and published implementation checkpoint: the
[generic runit sysctl service](design.md#approved-generic-sysctl-service).
The user selected a normal oneShot service in default/rescue, one application
attempt per start or managed-input change, and unchanged switcher exit semantics.
Early-boot sysctl application stays in place; the later service boot apply is
intentional. A current-input success stamp and custom check report application;
switch exit or supervisor status alone does not. The explicit retry procedure
handles the same-config start/check race. Managed effective sysctl targets trigger
restarts; unmanaged changes do not, and removed keys do not reset live values.

Implementer2 owns the module, registration and serialized Git/publication;
implementer0 owns focused tests and existing configuration documentation.
The generic feature is committed as
**`88486d43f7d47917b6ab796163abf8cd1f0be94a`**, following unchanged panic-policy
commit `85282623` on base `55c50465`; the worktree is clean. All intended quick
checks passed: ten module-graph variants, isolated native runsv behavior,
fixture rendering and Ruby syntax, Nix/MkDocs and normal hooks. See the
[verification packet](generic-sysctl-verification.md).
[Final independent review](generic-sysctl-final-review.md) accepted all four
lanes at high risk with no findings, including complete history and the absence
of migrations or repeated update streams. Normal SSH publication of `88486d43`
is verified; staging remains `55c50465`.

At the earlier `88486d43` checkpoint, **CI and focused VM verification were
incomplete**: exact-head CI `39759039117` had started and the focused VM awaited
its cache prerequisite. The later `89587060` run has since launched, as recorded
above; implementer2 retains verification ownership. Source acceptance and
publication do not prove actual
host application. The earlier direct switch-step proposal is superseded. No
pin update, merge, deployment or host runtime change occurred.

Previously accepted panic-policy source remains unchanged: **paired hard- and
soft-lockup panic declarations,
without an activation hook**, at
**`8528262315b0794a8f50917cf33c53a07fd14030`** on base `55c50465`.
The single v3 commit is clean and SSH-published. Both boot arguments and the
NMI comment remain under the crashdump-enable gate. [Final v3 review](os-hardlockup-v3-final-review.md)
accepted all four lanes with no findings; real enabled/disabled, paired
zero/null overrides, generated sysctl and no-hook checks passed, as did quick
checks and hooks. [Verification evidence](os-hardlockup-verification.md)
records the results. Its [HTTP429 CI preparation failure](os-hardlockup-v3-ci-failure.md)
is separate historical evidence, with no VM assertions executed; it does not
verify the new generic-service commit. Existing CI ownership stays with
implementer2.

The [declaration-only brief](design.md#declaration-only-hard-and-soft-panic-policy)
records the user's chosen scope: vpsAdminOS's current runit live switch does
not automatically apply these declarations. NixOS's systemd sysctl restart
behavior is different. Generic live application is now the separately approved
service implementation above. The v3 source supersedes `14cdf1ca`; the hook
implementation, review and CI below are historical. No pin update, merge,
rollout or host write occurred.

The superseded targeted-hook implementation was committed and published as
**`14cdf1caec606bb6bc88fcb32ac48f707f5dabb0`** on base `55c50465`,
consolidated into one v2 policy commit. It retains the boot arguments and adds
the crashdump-gated hard-lockup sysctl, explanatory comment and targeted
activation hook. The hook applies the final merged value during `switch`/`test`,
honors zero/null overrides, excludes dry activation and reports write errors.
Real module/generated-script checks and isolated mock success/failure checks
passed, as did formatting, parsing and hooks. Checks were repeated after a
rebase that preserved the policy patch. [Final runtime review](os-hardlockup-runtime-final-review.md)
accepted all four lanes with no remaining findings. CI run `39744127896` and
RSpec run `39744127815` were pending at that historical checkpoint; this does
not describe current monitoring. See
[the verification packet](os-hardlockup-verification.md) and
[runtime design](design.md#runtime-hard-lockup-policy-supplement).
No real host activation or sysctl invocation was executed. The accepted
boot-only revision and its CI below are historical and do not certify this
runtime revision. No pin, merge or deployment occurred.

The earlier boot-only vpsAdminOS change was committed and published as
**`b81c43ff6865a033268072f55cd94ad763d0630b`** on staging base `252b80df`.
It adds `nmi_watchdog=panic` beside `softlockup_panic=1` under the same
`boot.crashDump.enable` gate and corrects the option description. Thus it
applies to all crashdump-enabled vpsAdminOS configurations, including consumers
outside the 13 site nodes. Enabled/disabled/override evaluations and quick
checks/hooks passed. [Final review](os-hardlockup-final-review.md) accepted the
source and withdrawal; its commit-message finding is resolved. The amendment
from `f3e91f62` only adds validation prose, with identical source tree and parent.
The [implementation packet](os-hardlockup-verification.md) records publication.
**CI run `39600028637` completed with failure.** The
[final metadata](os-hardlockup-ci-new-result.json), updated
`2026-10-22T01:11:10Z`, confirms all 11 jobs finished on exact head `b81c43ff`:
OS build/cache and all nine livepatch jobs succeeded; the product-test job
failed with 124 tests passed and five failed. That revision's watcher ended.
The accepted
[failure analysis](os-hardlockup-ci-failure-analysis.md) identifies retained
impermanent-container `boot_dataset` mismatches after a live userspace switch.
Unchanged kernel and boot identity show the new boot argument was not executed
in these failing paths, so the evidence warrants no panic-policy edit or rerun.
The exact runtime metadata/mount root cause is unresolved; neither baseline
failure, harmlessness nor data loss is established. Source review remains
accepted, but CI is not green.

The superseded site sysctl commit `8515b682` has been withdrawn from the
published configuration branch. Its base and head now both equal `37a338b2`,
with zero feature commits or diff; see
[withdrawal evidence](hardlockup-configuration-withdrawal.md). No pin update,
merge, deployment or runtime change occurred. The
[move-policy brief](design.md#move-panic-policy-to-vpsadminos) records the
current design. The following configuration results are historical.

The earlier `kernel.hardlockup_panic = 1` source change was committed and
published as **`8515b68288be7f6c78ed010f93d1424c377973fd`** on the
`2026-10-20-kernel-check` configuration feature branch. Effective configuration
checks passed for all **13 nodes**, including backuper2.prg, and
[final independent review](hardlockup-final-review.md) accepted the change with
no findings. The [design](design.md#all-node-hardlockup-panic-configuration) and
[verification record](hardlockup-verification.md) preserve scope and provenance.

The superseded configuration's required system build was attempted and blocked.
After review and the
earlier dry-run, `confctl build` selected all 13 nodes and 26 outputs, then
failed during node5.brq evaluation because this environment lacks
`/secrets/nodes/initrd/ssh_host_ed25519_key`. It exited `1` after 58.12 seconds,
before substitution planning or compilation; no operation remains active.
See the [build log](hardlockup-build.log) and
[result receipt](hardlockup-build-watch-result.json). Successful system builds
remain unverified. No key or source workaround was introduced. This source change
has **not been deployed**, and running node settings are unchanged by this work.
Default-branch integration and runtime activation are not authorized here.
Earlier policy recommendations below describe the decision before this new
instruction and do not override it.

The complete three-month cluster search found **zero hard-lockup reports or
mentions** in the available logs for **July 20, 2026, 00:00:00 CEST through
October 20, 2026, 23:08:52 CEST**. All **1,221 selected files,
557,248,915,782 bytes** were read and independently reconciled. Thirteen
active sources supplied data; 13 inactive directories have no retained data
in the window and are coverage gaps, not negative results.

**No cause of node24's hang has been established. The assigned source
investigation is complete.** The full custom Linux patch inventory and selected
package overlays were accounted for; the subsequent targeted upstream audits
found no source-supported host-wide failure chain. This is a bounded negative
result, not proof that the kernel was healthy.

The subsequent bounded cluster-history investigation found one historical
hard-lockup episode, followed by a new boot, and no demonstrated nonfatal
recovery in the searched records. Source permits recoverable detections, so
this limited sample does not justify enabling panic across the cluster.
The follow-up conclusion below does not change the node24 attribution result.

The complete search of **all discovered retained node24 logs** found **no
hard-lockup reports or diagnostic mentions**. There is therefore no recorded
node24 event to classify as survived or recovered. A node24-only panic trial
is a reasonable option to consider for future evidence capture, with the
limitations below; no configuration change is authorized or performed.

Three definite source defects were identified: a pre-existing syslog namespace
allocation-error NULL dereference, new swap-reporting arithmetic errors, and
an NFS FREE_STATEID allocation-error reference leak. None has a demonstrated
connection to this incident. The configured hard-lockup panic policy is
disabled, so a hard lockup without a crash upload is consistent with policy;
that does not establish that a hard lockup occurred.

## Cluster: complete three-month result

The [completed collection](cluster-hardlockup-three-months.md) searched every
selected snapshot extent for the inclusive window
**2026-07-20T00:00:00+02:00–2026-10-20T23:08:52+02:00**. The sequential pass
read **557.249 GB (approximately 519 GiB)** in **2,344 seconds (39m 04s)**.
One 30-second timeout was resolved by a successful full-file retry; no file
remains incomplete. All reads were fresh, including node24.

The uncapped prefilter produced **253 unique in-window records**:

- **96 boot command-line records containing `softlockup_panic`**. These are
  configured arguments, not soft- or hard-lockup detections.
- **157 boot/version labels** collected for potential episode chronology.
- **Zero hard-lockup mentions, reports or candidate episodes**.

Independent local verification matched all 1,221 manifest entries to completed
reads, byte cutoffs, file identities and match dispositions. Final inventory
had the same **3,477 paths**, with unchanged metadata for **3,464 fixed files**.
All 13 current files retained identity; **263,131,061 bytes** appended after
their snapshot extents were excluded. The
[coverage receipt](cluster-three-month-coverage-receipt.json) and
[final metadata reconciliation](cluster-three-month-final-metadata-receipt.json)
preserve exact accounting and the resolved timeout.

The sources with eligible records were `brq/node5`, `brq/node6`, `pgnd/node1`,
`prg/backuper2`, `prg/node19` through `prg/node25`, `stg/node1` and `stg/node2`.
The [per-host coverage](cluster-three-month-host-coverage.tsv) records the 13
other directories whose retention ended before July 20. Their missing interval
cannot establish that those machines had no events.

Selection used actual first/last timestamps with a conservative metadata
fallback and included overlapping boundary files. All selected candidate
timestamps parsed and fell inside the exact window. This does not certify
arbitrary interior timestamp jumps in excluded old files. Forwarding losses,
pre-cutoff events arriving after the captured file extents, unretained events
and undocumented unrelated aliases also remain outside the evidence.
The result is **no forwarded hard-lockup detection found in the
available retained cluster logs for this window and coverage**, not proof that
no machine stalled.

There is no observed survived/recovered hard-lockup episode to classify in
these three months. The October 2022 staging-node example below is outside
this window. Source still permits recoverable detections; the negative history
does not establish a zero-risk panic policy or guarantee crash capture. No
configuration or policy action was performed or authorized by this search.
The requested collection and independent reconciliation are complete; the
session remains open and node24's original hang remains unattributed.

## Node24: complete retained-log result and policy

The [completed search](node24-hardlockup-history.md) covered all **181 files**
in the discovered node24 corpus: **89,603,613,857 bytes (83.450 GiB)**,
from **April 23, 2026, 00:00:01.261611 CEST** through the fixed current-log
cutoff **October 20, 2026, 21:07:36.802428 CEST**. It took **402 seconds**.
The broad hard-lockup expression matched **zero mentions and zero detections**;
all 19 other matched records were boot/version labels. Consequently this
retention contains **no observed node24 hard-lockup event that it survived**,
and no reported event whose recovery can be classified.

The collector and independent local checker reconciled every manifest entry
with one completed read, its byte cutoff and file identity. There were no
timeouts, errors, partial files or changed rotation metadata. Final directory
inventory contained the same 181 paths, with none new or missing. The current
log retained its device/inode and grew by 2,318,193 bytes after the recorded
359,236,720-byte cutoff; those later appends are explicitly excluded. Exact
accounting is in the [coverage receipt](node24-hardlockup-coverage-receipt.json)
and [snapshot manifest](node24-hardlockup-manifest.tsv).

This establishes **no forwarded hard-lockup detection in the retained node24
logs through that cutoff**. It does not exclude unforwarded events, events
before retention, or data under an undiscovered unrelated alias. The bounded
named-host/IP discovery found only the recorded node24 directory. It also does
not show that the October 20 hang was a hard lockup; its cause remains unknown.

**A node24-only trial of `hardlockup_panic=1` is a reasonable option to
consider if the priority is capture and recovery from another detected
lockup.** Unlike blanket fleet enablement, it limits the operational scope,
and this host's retained history supplies no logged recoverable-detection
counterexample. That absence does not quantify future risk: first-report panic
can still turn a future finite stall into an outage. It also cannot guarantee
a dump; the detector must fire, diagnostics must reach panic, and crash
transfer/capture must succeed. This changes failure policy rather than fixing
the unidentified cause. A trial needs an explicit user instruction and a
defined rollback criterion; the current request authorized the search only.

The full-retention search and independent coverage check are complete. No
episode artifact is needed because there were no candidate episodes. No
additional source audit, collection, test or operational change is required
for this bounded answer. The session remains open.

## Earlier cluster follow-up: can machines survive hard-lockup detections?

**Yes in principle; no recovered cluster example was established by that
bounded search. It did not justify blanket cluster enablement.** These are
separate source and observational conclusions.

At the inspected .95/.113 source, `hardlockup_panic=0` permits the reporting
function to return. It neither repairs the stall nor requires it to be
permanent; a finite loss of timer progress can end. Repeated still-stalled
checks can be silent, and a healthy heartbeat clears the warning state
without a recovery message. Silence alone therefore proves neither recovery
nor persistence. With panic enabled from the start, the first accepted report
requests panic if the intervening diagnostic path completes, even if the
underlying stall would later clear. A finite genuine stall is distinct from
a detector false positive; either can matter to that policy decision.
The [source-semantics audit](hardlockup-recovery-semantics.md) supplies exact
paths and limitations. It does not claim how often either happens here.

The [central-log search](cluster-hardlockup-history.md) covered 13 growing
current logs (approximately 3.822 GB at inventory), followed by 81 historical
files totaling **30,980,043,942 bytes**, with no timeout or search error.
The historical selection represents all 26 retained host directories:
October 15–19 for 13 active sources, sparse latest retained days for 13
inactive sources, and three legacy files. Current-file boundary sampling
extended beyond the initial scan; later append events are not certified as
searched. This is not continuous cluster coverage of the entire retained
2022–2026 period. Approximately 1.08 TiB was inventoried, not scanned.
The proposed broader calendar tranche was not run.

The only matched episode was **stg/node1 on October 28, 2022**:

| Evidence | Conclusion |
| --- | --- |
| Runtime `5.10.147.8`, with a livepatch taint and `Kdump: loaded` | Historical staging-node incident; not node24's 6.12.113/AMD incident and not proof of the old panic policy. |
| Two `NMI watchdog: Watchdog detected hard LOCKUP` lines name CPUs **25 and 33** at kernel uptime about **129.298 s** | Two CPU reports in one episode. A further CPU-25 heading is an NMI backtrace, not a fresh accepted warning or rearm event. |
| Page-fault BUG at uptime **108.280440 s**, followed by watchdog reports about **21.018 s** later | Serious adjacent diagnostics. Collector timestamps differ by microseconds because of batching; they do not give the actual interval between those kernel events or prove causality. |
| CPU 25 (`z_livelist_dest`) and CPU 33 (`mmp`) sampled in queued-spinlock slow paths; RCU stall also reported | Context supports actual stalled execution, but the retained affected-CPU caller stacks are incomplete. It does not establish an irreversible stall or its cause. |
| Last diagnostic at original line `2590123`; next original line `2590124` is a **new Linux 5.10.149 boot**, about **622.215 s** later by collector time | No intervening same-boot host survival or affected-CPU recovery is established in these records. The reset mechanism, reason, panic attempt and exact reset time remain unknown. |

The [independent episode analysis](hardlockup-episode-analysis.md),
[retained context](cluster-hardlockup-stg-node1-20221028-context.txt) and log
artifact preserve the classification, exact original lines and timestamps. No fresh
repeat warning for the same CPU exists from which to infer healthy-heartbeat
rearm, so an old-version reset-state assumption is unnecessary. The episode
does **not** provide the benign/recovered example the user was looking for.
It also does not prove that such examples never occurred elsewhere or that
these CPUs could not have recovered before the reboot.

The practical policy conclusion is conservative: **do not enable
`hardlockup_panic=1` cluster-wide on the strength of this search.** This does
not establish that the current zero policy is optimal. The user's concern
is technically valid because first-report panic can convert an otherwise
recoverable stall into an outage, while the collected sample cannot quantify
that risk. Any later change needs a concrete recovery/capture benefit and a
separately justified limited rollout or pilot with explicit abort/rollback
criteria. No setting, forced lockup, crash, test or deployment was performed.
The original hang remains unattributed, and no further broad scan is required
to preserve this bounded result.
Collection, source-semantics checking and independent episode classification
are complete; the session remains open.

## What the incident evidence establishes

Node24 stopped forwarding logs at **2026-10-20 18:58:26.658330 CEST**. Boot
output resumed at **19:12:04.761663**, a gap of **13m 38.103333s**. Other
nodes continued reaching the collector. Node24 SSH health-check and host
control traffic completed within the last three seconds before the gap.
The gap establishes lost node24 logging followed by a boot; it does not itself
identify the failed kernel subsystem or the exact moment of reset.

The affected boot identifies vpsAdminOS `2abbe3cc`, generation 144, Linux
6.12.113 built on October 18. That OS revision selects Linux
`1dfea587406b7dd79973831d1677fb2418e5e9aa`, the later .113 source after
proactive-swapping removal. The pre-upgrade kernel reported 6.12.95.6, which
includes a livepatch overlay and must not be equated with the .95 boot source
alone. Exact source and livepatch provenance belong to
[the inventory](patch-inventory.md); runtime observations belong to
[the log evidence](log-evidence.md).

The **blinking cursor does not prove that the scheduler was alive**.
Pre-incident boot logs identify a VGA text console and no framebuffer takeover
in the checked boot interval. In the exact incident source,
`drivers/video/console/vgacon.c:475` programs cursor start/end registers and
`vgacon_cursor()` at line 506 sets the cursor position and shape. This is a
hardware-cursor path, so continuing visible blinking is compatible with a
stalled host CPU. There is no live confirmation of the console driver at the
incident. A different driver can behave differently: `fbcon.c:369` flashes a
cursor from delayed work with `console_trylock()`. Consequently the observation
alone neither proves progress nor distinguishes a hard lockup from other hangs.

The completed log scan found no post-upgrade kernel panic, Oops, RCU stall,
lockup, blocked-task, global OOM, storage-fault or hardware-error signature.
That is an evidence limit, not exclusion of those failures: the failure itself
may prevent forwarding diagnostics.

A container NFS timeout appeared **8.420016 seconds** before the final log.
It is a useful discriminator for targeted follow-up, but temporal proximity
does not prove a host-wide failure mechanism. The 174 memory-cgroup OOM records
are tenant-scoped; the last was over 26 minutes earlier. The older NFS blocked
tasks at October 19 02:15 ran on **6.12.95.6**, before the upgrade, while host
control traffic continued. Do not attribute those stacks to the October 20 hang.

## Missing crash upload and configured policy

The user reports that the normal crash-kernel/upload recovery did not happen,
and confirms that sysctls were defined by the configuration and vpsAdminOS
repositories with **no runtime changes**. The final source/precedence trace
therefore supplies incident policy; these values are not left unknown merely
because no live `/proc/sys` read was possible.

| Policy | Incident value and consequence |
| --- | --- |
| Hard-lockup panic | **0**. The NMI watchdog can detect/report a hard lockup without calling panic or entering kdump. |
| Soft-lockup panic | **1**, explicitly set by the crashdump module and observed on the command line. Its timer callback must execute to detect the stall and call panic. |
| Watchdogs | General watchdog and PMU NMI watchdog enabled; threshold **10 seconds**, with soft-lockup detection using twice that threshold. Enabled at boot does not prove NMIs/timers continued at the failure. |
| Other panic controls | Panic timeout **0**; panic on warning, Oops, RCU stall and hung task **0**; crash post-notifiers **false**. Panic timeout 0 does not disable the earlier crash-kexec attempt. |
| SPL assertion policy | Configured `spl_panic_halt=1` calls Linux `panic()` at the exact ZFS pin. It does not select the assertion-thread sleep loop. |

There is **positive evidence that a crash image was loaded**:
`log:1279760` at **18:31:57.333383** and `log:1279973` at
**18:31:59.183362** both say `Kdump: loaded` on 6.12.113. At incident Linux,
`lib/dump_stack.c:62` prints that marker only when `kexec_crash_loaded()` is
true; `kernel/crash_core.c:94–96` tests `kexec_crash_image`.
This establishes image presence about 26.5 minutes before the final log,
stronger than the 4096M reservation or loader parameters alone. There is no
evidence that it was unloaded afterward; presence at the hang and successful
execution are not directly observed.

The missing upload does not distinguish no panic, failure before crash
transfer, or failure within crash-kernel capture/upload. The configured crash
script mounts its NFS destination before saving crash metadata, so absence
of uploaded metadata alone cannot identify which stage was reached. This is
a source-based explanation of the inference limit, not a claim that NFS
caused this failure. Bounded boot scans found no explicit loader failure or
capture/upload result.

The seven upstream printk changes preserve the inspected panic predicates
and ordering: initial printing/optional stack precede early crash kexec;
CPU stop and explicit legacy flush remain afterward. No new namespace/global
wait or pre-kexec regression was demonstrated. Exact source and configuration
proof is in [the platform audit](upstream-platform-audit.md),
[the printk audit](upstream-printk-audit.md), and
[the crash-state excerpts](node24-crash-state-excerpts.txt).

## Accepted custom-source conclusions

| Area | Proven result | Incident implication |
| --- | --- | --- |
| Fake scheduler affinity | Owner patch differs only in subject; complete syscall/custom helper files have identical blobs in .95 and incident .113. | Excluded as newly introduced custom behavior; no supported hang chain. See [source analysis](scheduler-analysis.md). |
| Syslog v20 to v21 port | Normalized additions/removals match; namespace ownership source is identical. Differences in surrounding printk code come from upstream. | No new namespace lock/lifetime regression established. See [syslog/NFS audit](syslog-nfs-audit.md). |
| Syslog namespace allocation failure | A newly allocated namespace's `prb` stays NULL until all setup allocations succeed, but the failure cleanup dereferences it. The exact namespace source blob is identical in both kernels. | A source-proven **pre-existing** defect, with no incident allocation-failure or namespace-creation evidence. Do not name it as the cause or a regression. |
| NFS cold-client guard | Adds only a NULL return before an existing client cancellation path. It adds no wait or lock and does not skip the enclosing server shutdown. Successful NFSv2/v3 mounts already bind the NLM client eagerly. | No supported new hang mechanism. NFS timeout records do not establish use of this shutdown callback. See [syslog/NFS audit](syslog-nfs-audit.md). |
| Memory-view lifetime | Helper source is identical; `/proc/swaps` keeps one CSS reference from successful open through final release, including unread and repeated-read paths. | No reintroduced reference imbalance or new helper lock/progress change. See [memory audit](memory-audit.md). |
| Proactive swap/DAMON retirement | Custom policy/accounting and principal interfaces are removed; selected DAMON/swap files exactly match the new upstream base. Old proactive bookkeeping is in-memory, not state reused by the new boot. | No residual custom worker or persisted-map transition explains the hang. A pressure effect from removing an active policy is unproven. |
| Ordinary swap reporting | Two v1 calculations can wrap from inconsistent counter samples after old bounding code is removed. Results are formatted/returned, not used here for allocation, reclaim or indexing. | Source-proven output regression; no demonstrated kernel hang or userspace escalation chain. See below and [memory audit](memory-audit.md). |
| Packaged ZFS free accounting | Removes a conditional dbuf-mutex → hash-lock edge opposed by lookup's hash-lock → dbuf-mutex order. Existing holds and sync ownership protect accounting reads; BP publication stays locked. Both package modes at the incident OS apply it. | No replacement deadlock/lifetime/writer failure found in the bounded audit; not supported as an introduced regression. See [ZFS audit](zfs-patch-audit.md). |
| Package/config overlays | Exact OS and observed Nixpkgs inputs account for patch selectors; bridge-helper patch changes a path macro, other version-specific NFS/NMI patches do not apply, and default livepatch/eBPF payload selection is empty for .113. | No additional unexamined selected runtime patch in this package scope. Exact binary config and loaded module identity remain uncollected; configured sysctl policy is resolved above. See [packaging audit](packaging-audit.md). |

The complete Linux inventory accounts for 60 old, 61 initial .113,
and 55 incident .113 custom commits: 52 retained bodies, one consolidation of
two old memcg fixes, six removed proactive/DAMON owners, and two added owners
(NLM guard and swap reporting). A potential NFS teardown/callback lifetime concern in the lane
record remains unproven and pre-existing; it is not a supported incident
candidate and does not delay the downstream-delta conclusion.

## Targeted upstream conclusions and coverage

The exact stable range is `296aabce459470a4c1b68ffd0c0c0920e563aaad`
through `7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e`, comprising 7,278
commits and 5,291 touched paths. The upstream phase intentionally examined
selected mechanisms and their final incident-tree callers; it did **not**
audit every commit. [Upstream provenance](upstream-provenance.md) also maps
74 old v6 backport/prerequisite commits into the stable window, preventing
raw stable membership from being mistaken for a newly introduced runtime
change.

| Completed lane | Accepted result |
| --- | --- |
| [Memory/reclaim](upstream-memory-audit.md) | Selected memcg, shrinker, vmalloc, swap, slab and adjacent lifetime/progress paths yielded no new host-wide failure chain. The vmap purge-mutex change already occurs in documented old v6 source. Tenant OOMs do not establish host exhaustion. |
| [NFS/SUNRPC](upstream-nfs-audit.md) | FREE_STATEID has the precise reference leak below. TLS cancellation, transport destruction and inspected NFS/lockd/cache/VFS lock changes yielded no demonstrated host-wide cycle. TLS/RDMA/pNFS use remains unknown. |
| [Scheduler/RCU/locking](upstream-scheduler-audit.md) | 33 selected commits across 17 files, including immediate custom affinity/load-average/cgroup intersections, yielded no concrete new host-progress failure. Core-scheduling wait releases locks/IRQ exclusion; inspected selection counts balance; RCU changes add no new blocking dependency. |
| [Printk/panic](upstream-printk-audit.md) | All seven changes in the selected printk path and their custom namespace intersection were inspected. No new lock/wait cycle or panic-to-kexec regression was found. |
| [Platform/watchdog](upstream-platform-audit.md) | Selected x86 NMI/APIC/TSC/watchdog/crash-transfer files have no direct stable delta; inspected timer-broadcast, ACPI idle and AMD changes yield no concrete new progress failure. Hardware is EPYC 7H12, family 0x17; Zen5-specific changes do not apply. |

Config gating uses explicit recipe values and unchanged Kconfig/build
lineage, corroborated by the initial .113 config. CORE, EXT, PREEMPT_RT,
PSI, LRU_GEN and MEM_ALLOC_PROFILING exclusions are **source-inferred recipe
conclusions**, not recovered incident binary attestation. Observed full dynamic
preemption is not PREEMPT_RT. See [packaging](packaging-audit.md) for exact
strength and limits. Unchanged source or a disabled branch excludes only
that stated mechanism, not the subsystem as a whole.

## Pre-existing syslog defect: precise confidence boundary

At incident Linux `1dfea587406b7dd79973831d1677fb2418e5e9aa`,
`kernel/syslog_namespace.c:128` zero-allocates the namespace.
`syslog_ns_setup_log_buf()` assigns `ns->prb` only at line 70, after the
ringbuffer, data, descriptor and information allocations succeed. An allocation
failure returns to `clone_syslog_ns()` cleanup at line 160;
`syslog_ns_log_buf_free()` dereferences `ns->prb` at line 90.
This is a definite NULL dereference if that setup failure path executes.

The complete source blob is
`e55346ef9a374d12966d4c10ae3d81fb0d9949c1` at both old and incident revisions.
Later cleanup also has stale freed pointers in some failure branches, but the
earlier NULL dereference occurs first; no separately observed double-free is
claimed.

No captured incident trace ties the host hang to this path. Tenant memcg OOM
messages do not establish failure of these `GFP_KERNEL` allocations. A
dedicated fault-injection test could reproduce the error handling defect, but
would not by itself prove that node24 exercised it. Such a test or remediation
would be separate work; neither has been run.

## Swap reporting regression: precise confidence boundary

The final memory audit supplies concrete legal counter interleavings in the
cgroup-v1 branch. With a 1024-page memory limit and 1280-page memsw limit, read
memory usage as zero, then charge 512 resident pages before reading combined
usage as 512. Actual swap may remain zero, but `kernel/sys.c:2892` reports free
swap as unsigned `256 - (512 - 0)`. Conversely, freeing resident memory between
the two reads can make `mm/swapfile.c:3043` compute a wrapped used-swap value.
The earlier wrappers bounded these values.

This proves incorrect output is possible in the source under the stated
conditions. It does not prove that the interleaving occurred on node24, and
the outputs do not feed a kernel allocation or reclaim operation in these
paths. No consumer reaction or host-wide failure chain has been demonstrated.
Keep this actionable reporting defect separate from the hang attribution.

## FREE_STATEID leak: precise confidence boundary

Stable commit `ed1161ab6239761958b38d5667225634fc2be894` adds an active-server
pin to `nfs41_free_stateid()`. In incident `fs/nfs/nfs4proc.c:10630–10643`,
the function holds client and active-server references when its calldata
`kmalloc()` can fail; the immediate `-ENOMEM` return drops neither. No RPC
exists to run the release callback. The proven effect is retained
server/superblock/client resources, with no lock held by the return and no
demonstrated host-wide wait.

The documented old v6 adapter and the old NFS boot variant both clean up those
references on this failure path. This is a source regression relative to those
correct old effective paths; actual historical module/control state remains
qualified. The pristine old stable path's client-reference leak was already
present and must not be confused with those effective alternatives. A later
RPC-task allocation failure invokes cleanup and is **not** this leak.

NFSv4.1 FREE_STATEID activity and failure of this particular allocation are
unestablished at the incident. The nearby timeout does not prove either.
The [NFS audit](upstream-nfs-audit.md) records the complete reference chain
and old-path comparison. Reproducing this leak would verify the leak, not
attribute the host hang without an additional progress mechanism.

## Remaining evidence and next useful step

No kernel build, reproduction, configuration change, deployment or production
mutation has been performed by this investigation. The source identity checks
and source-path checks support the bounded conclusions above. Investigation
and evidence alone require no automatic change review.

Direct recovery-runtime inspection has not been possible through an existing
trusted SSH identity. Current runtime state would still need to be reconciled
with the historical boot. The exact failed liveness probes and recovery/reset
method remain unconfirmed in this evidence record. Sysctl policy and positive
pre-gap crash-image presence are resolved and must not be included among
those unknowns.

The next useful evidence is a trace that distinguishes the failure stage:
all-CPU/NMI or blocked-task stacks at a recurrence; console/BMC evidence of
whether panic and crash-kernel entry occurred; and crash-kernel
device/network/capture output if entry occurred. Exact affected NFS mount
options and operation context would refine the adjacent NFS symptom.
Any future instrumentation or policy change is a separate proposal, not an
operation performed or authorized by this investigation.

Without a concrete source mechanism and trigger, a generic passing stress
test, broad additional release audit, or speculative patch change would not
settle attribution. The assigned source work stops here with the incident
unattributed, the definite defects separated, and the session left open.
