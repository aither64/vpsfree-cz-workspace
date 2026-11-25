# Loader-CSD runtime audit: 9805 / 41972655273

**CI RED / diagnostic readiness INCOMPLETE; unchanged clean source.** The first
example exception is `INCOMPLETE: host schedstats unreadable or disabled`.
The early host gate stops before workload and the first full host snapshot.
No straightforward local implementation defect is established by the retained
data, so C made no application/control edit or new check. Missing host capability/
clock facts return to root; no setting change, weaker gate or retry is authorized.

Session/env and retained implementer3 Sol/xhigh/workspace-write roster were
reverified. This is a local artifact/source audit only; no Git/index mutation,
network/API/CI, build/eval/ELF, guest/runtime or lifecycle action occurred.
All read clients are terminal and C owns no process. The session stays open.

## Binding and independent verification

Canonical run `41972655273`, attempt1, push, exact published/reviewed source
`9805ea20e336aa6e2559f5f7af73de36fce3ecc8`, completes failure at
2026-11-05 05:30:09Z. Build127064224290 succeeds on runner3 in12m16;
target127068416320 fails on runner4 /2.338.0, 05:25:58–05:30:08Z; native is
skipped. Only `kernel/livepatch-qualification@amd-scale-aged-v5/default` runs:
one example20.9s, one test/script101.02s, unexpected_failure. See
[canonical gh-camelCase run](ci-loader-csd-41972655273/run-final.json) and
[test summary](package-c-loader-csd-runtime-evidence/test.log:10).

C independently verifies ZIP artifact13391071816: **183243bytes**, SHA256
`e38e0b4274f32b45bf11650c8cbb585395e895048eb544ea5b5286d745978f2a`.
All20 members are safe unique relative regular files, no symlinks/traversal.
The [inventory](package-c-loader-csd-runtime-evidence/inventory.txt) and selected
small files are retained in `package-c-loader-csd-runtime-evidence/`; console/
shell evidence is bounded numbered windows/indexes, not whole extraction.
The host samples.log is only318bytes/two lines and was read completely.

[Captured identity](package-c-loader-csd-runtime-evidence/livepatch-identity.txt)
and lifecycle raw:278–283 bind source9805 and lock SHA
`604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa` to normal
producer `/nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95`,
module `lib/modules/6.12.95/extra/livepatch_7.ko`, SHA
`7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f`.
Sites are `/nix/store/aiqijlwh2w2wz79d6hvcqm1p9kzl4lv3-livepatch-candidate-sites`;
extracted JSON SHA is independently
`093cf255a38db5275b62370da8bac1297781e48e2ae3245c1c5b5e1ceeb23ed1`.

[Guest guard windows](package-c-loader-csd-runtime-evidence/guest-guards-and-setup.txt)
show status0 for initial6.12.95, corrected module SHA (shell:89–94), sites SHA
(:98–103), released-v5 SHA
`b31f64403d9d55f62e3d59e4bbefcbddcbda4fa66a2dc0689f9bb7cd7e927984`
(:107–112), and v6 SHA
`960b13f1b461b95e29cccff58ddf0d3f3badf151046eb46eba36a9c8c7e5efe3`
(:116–121). v5 insertion returns0 (:4746–4750); its enabled1/transition0 and
6.12.95.5 guards pass. Frozen `/sys/kernel/notes` SHA
`1e4432629c0f1a1e9c6b175495217859279f98ded2beca091834ec059e42108a`
passes twice, including loader setup (:5088–5092). No independent full guest
boot-image SHA is claimed. The normal candidate is transferred/checked, not
activated by this attempt; checked v6 bytes do not mean v6 was loaded.

[Actual launch](package-c-loader-csd-runtime-evidence/os-test-kernel__livepatch-qualification__amd-scale-aged-v5-cb9686d6/machine-log.log:7):
05:28:18Z, QEMU PID1242587/start ticks148866501, direct boot,128CPUs/cores,
one thread/socket and16384MiB:

- QEMU `/nix/store/kanckc6ljipqzjsrvj4aqaf87a4rhswr-qemu-host-cpu-only-for-vm-tests-10.2.4/bin/qemu-kvm`
- Kernel `/nix/store/050sh2hfrnpc8j5abr2npp7bnlxvpb8a-linux-6.12.95-frozen-boot/bzImage`
- Initrd `/nix/store/h3v4nwmsn39wph7apj7q6bg8hn58rv3x-initrd/initrd`
- System `/nix/store/9smj8banaysa458yphm9qkh2050qzwmm-vpsadminos-system-vpsadminos-26.05.git.9805ea2`
- Squashfs `/nix/store/ybyf33rjyrm00df23ixahn0g7ai83inx-squashfs.img`

The case config declares100000tasks/300s and exact diagnostic naming selector.
That does not establish workload population or aging. `OTHER_ARGUMENTS` is
omitted in launch metadata; the literal naming pair is source/config-expected,
not an independently recorded argv observation. Actual vCPU labels were never
sampled, so naming success and the guest-APIC-to-owned-TID join remain unproved.

## First failure and exact early boundary

All original case timestamps below are +0100, converted to UTC here.

| Time | Recorded operation/result |
| --- | --- |
|05:29:23|Example starts; runner:3|
|05:29:41–42|Existing dying observer native/notes/nop/OFF/enable readbacks succeed; shell:4881–5074|
|05:29:42.629011Z|Host request `guest ready wall=1793856582.6290112`|
|05:29:44.603876Z|Sampler writes stop reason `INCOMPLETE: host schedstats unreadable or disabled`|
|05:29:44|Example fails20.9s with that exact primary exception; runner:4–9|
|05:29:45|Generic evaluator exception; secondary|
|05:29:58|Native runner returns failure after101.02s; lifecycle raw:307|
|05:30:02|Evaluation reports one unexpected failure; secondary|

[Host files](package-c-loader-csd-runtime-evidence/loader-host/status.txt) show
request, test-child `1236817 148854433`, two-line launch/stop log and error;
there is no ready.txt, guest-map.txt or window-complete.txt in the ZIP.
The sampler launch line repeats declared QEMU PID/start/exe/topology and says
**expected_naming**, not observed identity/labels. No `sample begin/end` record,
TID start identity, schedstat counter, gap/cadence measurement or vCPU map exists.
They are unavailable, not zero.

Exact committed9805 `loader_host_sched.sh:150–167` checked the job/child
stat/start/direct-parent predicates, parsed the exact case launch record,
opened QEMU/child proc directories and resolved a store-path child executable.
The child's actual resolved exe value, job PID and full ancestry are not logged.
The first complete QEMU pid/start/exe, ancestry, TID/label and statistics
snapshot occurs only at :174; it was **not reached**. Thus the earlier launch
line is insufficient to claim those later validations passed.

The error text is coarser than its possible failing statements. Source :168
sets that reason; :169 reads `/proc/sys/kernel/sched_schedstats`, :170 requires
literal1, then :171 obtains `getconf CLK_TCK` and :172 validates positive decimal.
The same reason remains active until snapshot174. The artifact gives neither
sysctl read result/value nor CLK_TCK command/value, and the raw job contains no
separate helper stderr identifying one. Therefore unreadable/missing sysctl,
disabled/non1 value, or unavailable/invalid clock-tick result are **not
individually resolved**. Absence of stderr does not prove a particular value.
Do not report verified0, permission denial or a kernel configuration defect.

The Ruby early handshake consumes this explicit error, before reading/validating
its guest-to-host mapping or creating the new loader trace instance. The existing
dying observer was prepared at address0xffffffff8f4ed123, but never entered its
recording/hotplug window. State/stress, task population,300s aging, CPU127 hotplug,
candidate activation/EBUSY loop, CSD/IPI setup/window, attempt/PID markers and the
LC1 corrected command were **not executed**. No fault/counter/zero-loss or LC1
runtime acceptance follows. The compact console has v5 patch complete and no
recorded new watchdog/warning signature; the cumulative health assertion was
not reached, so this is not kernel-health qualification.

## Recovery and scope of completion

The original exception is preserved through failure handling. Existing recovery
batch returns0 (shell1:668–675). With workload never started, the older dying
observer is disabled/read back, unregistered/absence checked and its owned
instance removed/absence checked, all status0 at05:29:44–45Z
([release windows](package-c-loader-csd-runtime-evidence/earlier-observer-release.txt)
and [cleanup index](package-c-loader-csd-runtime-evidence/cleanup-command-index.txt)).
This needs no manufactured drain wait. The new loader instance was never
created, so there was no new event teardown to accept.

QEMU stop starts05:29:48Z; guest `poweroff -f` returns0. QEMU exits0 and destroy
completes05:29:58Z, kill action SIGNAL NONE. Console:150–160 shows normal runit
shutdown/powerdown. This is failed-VM teardown, not qualification. The sampler
wrote its own stop line before failure cleanup; no normal host-window completion
was recorded. Exact workflow EXIT source waits/reaps the sampler and preserves
the already-nonzero test status; the step completes, but there is no separately
logged sampler PID/wait-return receipt. No cancellation was requested or recorded.

## Classification and handoff

**Named prerequisite: enabled/readable usable host scheduling statistics and a
valid host CLK_TCK under the actual runner4 job user/environment.** This failed
before stress. Retained evidence does not select one specific host setting or
show a local format/path/PID/control-flow bug. C therefore stops with clean
unchanged9805, not a speculative source fix. Minimum next package is a separately
owned, supported **read-only runner capability preflight** of the exact sysctl
read/value, CLK_TCK availability/value and relevant permissions; root chooses
it. Enabling stats, host infrastructure/SSH changes, weaker readiness, new APIs,
retries or four-hour advancement require separate scope and were not done.

Four application hashes remain qualification5c4db809…caf72,
helper6b85cedd…8045c, workflowffce88c8…f2ed7, common8acb93d5…c0509, matching the
published source; final HEAD/status check is9805/clean. Earlier b361 loader/TLB
fault, bda1 scheduler warning,13b enable timeout, LC1 review/35host controls and
all old captures remain distinct. This run supplies no recurrence or causal
claim for any of them. Source roots/refs and primary645927/14400 remain untouched.
