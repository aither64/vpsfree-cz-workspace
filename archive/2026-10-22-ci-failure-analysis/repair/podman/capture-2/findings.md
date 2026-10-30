# VM2: original permission denial not reproduced

**NOT REPRODUCED under the diagnostic image and ptrace:** PID164 at
`podman-sandbox/trace.log:230` sets NNP successfully; line231 installs the
140-instruction seccomp filter successfully. No captured sandbox-entry EACCES
supports a product patch. Native/guardian0 means capture/retention succeeded,
not that the original failure was fixed or nested continuity passed.

## Actual call evidence

All eight complete same-PID pairs return0 for
`prctl(PR_SET_NO_NEW_PRIVS,1,0,0,0)` and
`prctl(PR_SET_SECCOMP,SECCOMP_MODE_FILTER,{len=140,...})`:

| PID | NNP line | Filter-install line |
| --- | ---: | ---: |
| 164 | 230 | 231 |
| 169 | 248 | 249 |
| 168 | 257 | 258 |
| 166 | 266 | 267 |
| 174 | 277 | 278 |
| 178 | 318 | 319 |
| 179 | 328 | 329 |
| 198 | 521 | 522 |

The first manager's `chroot`, supplementary-group/GID65534 and UID100 changes
succeed at lines224–228. The same sequence is recorded for169/168/166. The
only captured EPERM is PID149's `prlimit64(RLIMIT_NOFILE,...)` at line135;
it precedes the dhcpcd entries and is not their EACCES. Do not assign it as the
incident cause. Entry metadata belongs to the wrapper's `cat`, not a failing
dhcpcd task: `entry.txt` records UID0, NNP0, seccomp2/filter-count1 and mapped
IDs, before tracing. Later successful NNP is an observed change, not evidence
that every task had the entry process's state or final capabilities.

`guest-addresses.txt:6` records192.168.1.114/24;
`guest-routes.txt:2` records the DHCP default route via192.168.1.1.
`network-journal.txt:18–24` records lease and route creation. Resolver contents
are captured; DNS resolution/external endpoint and nested Podman continuity
were not tested. No APT, Podman install or target activation occurred.

## Trace and service qualifications

The raw trace is106,496 bytes,535 lines, SHA256 recorded in `SHA256SUMS`.
It ends without a newline in the middle of a clone result at line535, about
10.39 seconds after initial ifup exec. Ifup PID132 has no terminal exit record;
its last recorded operation waits for post-up child197 at line502. Do not infer
ifup success/failure or complete lifecycle coverage from this prefix.

The service has `Result=timeout`, while `ExecMainStatus=0` and DHCP address/route
are present. At journal line25, the imposed60-second systemd startup timeout
terminates the wrapper; line26 onward records strace's broken output pipe.
That supplies an observed instrumentation boundary, not the original DHCP
failure. Pipe-tail loss is consistent with killing the traced service/output
reader together, but exact lost events/bytes are unknown. The32-MiB cap was not
reached. `trace-retention.txt incomplete=false` means bounded byte-copy success;
it does **not** establish a flushed/complete trace or ifup lifecycle completion.
Ptrace can also change task scheduling/state; no untraced control was run.

## Identity and exact source boundary

Archive SHA256 is
`e0a89f751487eadf0e198f7251550e92aba100ddb8d3c8bd920140b557281ad4`,
dhcpcd binary SHA256
`a9215b8a2efc63481ef781069917e1bae2b293744d544fd18566c7abb37a955c`,
and INDEX SHA256
`0572fb88a58d8db3c4e042f4da7ab01bcb7a12402c5a9c12267d087274295bc6`
(`image-cache-hashes.txt:4,6`, `dhcpcd-hash.txt:2`). These match VM1's diagnostic
sample. Package versions also match: dhcpcd-base1:10.1.0-11+deb13u4,
ifupdown0.8.44+deb13u1, systemd257.13-1~deb13u1 and libc2.41-12+deb13u4.
This is observed repeatability of that sample, not equivalence to the original
incident's unavailable archive. Native disk cleanup has removed archive bytes;
only hashes/provenance observations were retained, so no later mutable fetch
is presumed identical.

The prepared w9ik JSON directly depends on kernel derivation
`g4hykqld77rwdz59m6zyfsmx2q7vmm9s-linux-6.18.49.drv`. The retained recipe selects
Linux `fbda79346b89b2d2486edd22e4bbbca0154d96b7` and produces the actual rooted
fmdhcn kernel, whose bzImage SHA256 is98e767f3...d65a69. Captured binary config
has AUTH_GUARD_CORE/AUTH_GUARD=y and SECCOMP_FILTER=y. Dmesg records credential
guard enabled, but no rejected transition is present and complete runtime layer
enablement/state was not captured. Do not substitute compile configuration for
the failed task's guard state.

Exact immutable local sources and hashes are retained in
`source/local-exact-source-manifest.json`, with official pinned URLs. The
selected source routes are:

- [NNP EACCES mapping](https://github.com/vpsfreecz/linux/blob/fbda79346b89b2d2486edd22e4bbbca0154d96b7/kernel/sys.c#L2711):
  rejected mutation returns EACCES.
- [NNP helper](https://github.com/vpsfreecz/linux/blob/fbda79346b89b2d2486edd22e4bbbca0154d96b7/kernel/auth_guard.c#L5678):
  begins a transition, then expects/applies the NNP mutation.
- [Transition result wrapper](https://github.com/vpsfreecz/linux/blob/fbda79346b89b2d2486edd22e4bbbca0154d96b7/kernel/auth_guard.c#L5123)
  accepts only VALID; [reservation](https://github.com/vpsfreecz/linux/blob/fbda79346b89b2d2486edd22e4bbbca0154d96b7/kernel/auth_guard.c#L1341)
  can return BUSY/UNAVAILABLE/INVALID. A non-VALID result is a source-compatible
  entry rejection, not evidence it happened in the incident.
- [Filter entry](https://github.com/vpsfreecz/linux/blob/fbda79346b89b2d2486edd22e4bbbca0154d96b7/kernel/seccomp.c#L2284)
  separately maps failed guarded begin/expectation to EACCES. Ordinary NNP/
  namespace-capability preconditions and earlier filter/LSM outcomes remain
  competing incident mechanisms. They did not deny these recorded successful
  calls.

There is no explicit ptrace exemption in these wrappers or literal ptrace test
in auth_guard.c. That bounded source observation does not prove ptrace-neutral
execution through the rest of the kernel or rule out timing changes. Do not
turn it into either a bypass explanation or a guard-bug conclusion. The local
canonical clone now has the exact source object; it is a promisor clone. Earlier
plain exact-source reads may have lazily materialized requested blobs, without
an explicit fetch/ref edit; final retained reads set GIT_NO_LAZY_FETCH=1. Two
official raw requests returned429 and were not retried. No history/authorship
search, build or source edit occurred.

## Owning-fix decision and remaining evidence

**No kernel, LXC, dhcpcd or target-side product fix is justified by this run.**
There is no measured denied entry/policy to repair. The completed fixture fix
owns evidence retention; the observed tail-loss/byte-copy qualification is a
diagnostic limitation, not a networking repair. Keep sandbox confinement and
the original upgrade/nested continuity assertions intact.

Recoverable now: raw trace prefix, credentials transitions, actual LXC/default
profile bytes, config/dmesg, package/image hashes, retained JSON/input recipes,
exact kernel source and service/network observations. Inspecting those records
can refine candidate mechanics without another run. Original failing-task
call/arguments/guard state and original archive bytes were not retained and
cannot be reconstructed from a current successful sample or package labels.
No additional original archive has been located; a separately supplied exact
historical archive would change that limitation.

If the lead selects one next diagnostic, the minimum discriminating owner is
the **unchanged predecessor kernel's native observation boundary**, alongside
the fixture owner: one fresh container start with original networking ExecStart
and no ptrace, preserving/validating the selected image archive before startup.
First check exact-binary tracepoint/probe availability without a kernel rebuild.
A bounded native syscall-entry/exit capture must identify both prctl commands,
args and errno for the actual dhcpcd PID lineage; capture guard transition result
and credential/NNP/filter state at the failed entry if that symptom recurs.
An EACCES syscall alone still needs the corresponding guard/outer-policy result
before selecting a component fix. Compare named supported source mechanisms,
not an arbitrary introducer search. If it passes, report another nonreproduction;
do not retry until failure or disable seccomp. Probe feasibility, exact commands,
one-start timing, resources and lead scheduling remain separate selection work.
No such run or probe is authorized by this findings document.

Any later trace writer adjustment should retain explicit EOF/flush/lifecycle
qualifiers and avoid treating below-cap copies as complete. Preserve original
ExecStart parent/exit semantics. It must not silently add another startup or
claim a plain DHCP success proves old-to-new nested workload continuity.

## Effects and retention

`post-result-reconciliation.json` records native1077821/birth1201472525 absent,
no original group or declared own-root process/open-FD references, no managed
disks/sockets/kernel UNIX references, lock available, and native QEMUexit0/
destroy. Unreadable unrelated-UID FD tables are explicitly qualified. Owner3's
independent `post-result-independent.json` supplies a separate bounded proof.
After lead acceptance and cleanup direction, all55 retained manifest entries
were verified and all48 native case evidence files matched their retained
copies. Only stopped attempt2 `state`, `vm-scratch`, `metadata-scratch` and
`preparation-scratch` were removed; [cleanup.json](cleanup.json) records exact
paths, before/after allocation and unchanged nine prepared/input/shared-runner
roots. Compact raw evidence, source and both effects proofs remain. The clean
isolated fixture checkout had already been removed natively under its earlier
serialized authorization; its existing receipt was confirmed, with no new Git
operation. No session lifecycle action or store/GC operation occurred.
