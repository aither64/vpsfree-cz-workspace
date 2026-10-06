# Complete OS branch review result

## Independent scope

Retained reviewer0 completed all four HIGH lanes: general,
architecture/repetition, scope/proportionality and risk/compatibility.
Identity: review/read_only, gpt-6.1-sol/xhigh,
thread01a0d230-7536-7ee0-b212-90b3f6847ec0, live roster revision23.
Session/current/environment binding was verified. No overrides, authorship,
nested review, tests/builds/Nix/network/runtime/private reads or edits occurred.

Complete reviewed range: cbfc283d233f77cd6823893f97cf843f69c995a1..
09786fbc20a2d8e134e2e3001d53ef287646e74b.
Tree523c25edbb0bb2675c88b3c5d083aab907d6703a.
Two commits,22 paths,1265 additions/49 deletions. Independently matched
complete binary/full-index SHA256:
27831036572eaed0648b5449c8fbf66367666d30013dea3dc2048b19ce84389e.
See the [packet](storage-os-disabled-review.md) and
[inventory](storage-os-disabled-inventory.json).

## Findings and lead disposition

**Important — resolved by direct step9**, general and risk/compatibility,
originating09786fbc. The following describes the original finding.
The disabled-generation shutdown path depends on the intentionally absent
osctld. The new scenario proves the process/socket absent then calls
machine.stop at tests/suite/system/switch-to-configuration.nix:377.
OsVm::Machine#stop executes poweroff -f. The installed Halt wrapper still
forks osctl shutdown --force, whose missing-socket path waits up to3601 seconds
for the daemon to mark its shutdown marker executable. The framework default
is900 seconds. Non-force confirmation also lists containers through the absent
daemon. Ordinary disabled-generation poweroff/reboot inherits the defect.

Required correction: a supported installed-generation shutdown path,
regression preserving ordinary daemon-backed shutdown, and the existing fixture
exercising that path. Increasing the timeout, restarting osctld or substituting
a test-only forced stop is insufficient. Lead inspected the producer, Halt,
Self#shutdown and Machine.stop and confirmed the finding. At the original review checkpoint, architect0 owned the
bounded correction brief, source release was pending and the VM held.
Earlier progress and final notifications report the same issue.

No Blocking, additional Important or Advisory finding was reported.

## Lane, history and migration conclusions

Apart from shutdown, the reviewer found default/true/custom-runlevel behavior,
final contradictions, raw ZFS handling and parsed destination activation
consistent with the accepted scope. Activity bookkeeping covers
enqueue/running/finish and sticky unknown failures without an observed
lock-order inversion. Startup policy, Services and activity ownership remain
appropriate; no Admin authority protocol or alternate VM engine was added.

Both commits/messages and the complete final diff were inspected:
7f85b137 activity interface replay, then09786fbc disabled startup and consumers.
All15 activity blobs and message independently match consumed8d05;
range-diff1=1. No obsolete approach, fixup, temporary migration or unused
alternate implementation remains. Upstream five commits, OSVM and lock are
preserved; final lock equals cbfc. The new flake delta only exports the focused
check. **No OS SQL/schema migrations**, migration rewrites, retained format
conversions or new activity wire version are present. Companion Admin's three
migrations remain separate.

## Consumers and remaining limits

Actual Admin425d still pins OS8d05 and separately starts NodeCtld. The option
needs generated dependency delivery/composition; it does not exclude NodeCtld
or establish physical exclusion. Existing activity-v1/GC-v1 readers remain
compatible; missing/stopping pools, dead/stale workers and overflow remain
unknown. Old sources lack the option, and old ordinary generations can restart
writers, so format compatibility does not make future owned rollback safe.

Focused19/6 passes and five-check/scenario derivation evaluations are supplied
parent evidence, not reviewer execution. Other check bodies and all eight VM
examples are unrun. Ordinary broad flake validation is baseline-blocked.
Historical36/0 activity specs and3/0 VM retain their original composition.

After correction/disposition, the existing scenario must prove normal-to-disabled
activation, fresh disabled boot with preserved disks, exact booted/current
identities/new boot ID, raw pool completion, absent automatic daemon,
GUID/active property/known payload equality and ordinary return. Direct init
selection does not prove production bootloader persistence. Socket/process
absence is not descendant/delegated GC termination or physical exclusion.
Admin composition/handoff, G2, alias disposition and real payload/history are
separate. This report supplies no publication, pin, package, default integration,
live recovery or physical operation authority.

## Direct remediation and current source disposition

Lead inspected the seven-path correction against the final accepted brief.
The existing halt producer binds an immutable Boolean to the typed final
osctld.enable option. Disabled generations omit container listing and the
shutdown/fork/wait/status/abort path. Common confirmation, reason, logging,
hooks, kexec and runit dispatch remain. The same option gates only the second
osctl shutdown in generated runit stage3; both clock writes and ordinary shell
semantics remain. No runtime discovery, timeout/framework change, public
interface, containment or authority boundary was added. This is the requested
missing-consumer remediation under mandatory review step9; no reviewer rerun
is required.

Fresh exact-source batch passed0/217.826s/parity1: actual module19, activation6,
installed Halt19 and generated stage3four checks; all five check derivations
and the exact owning scenario derivation evaluated. Other check bodies and
the eight VM examples remain unrun. Broad flake validation retains its
reproduced baseline overlay error. All three owned stage PGIDs ended; no signals.

Normal unpublished owning amendment passed0/13.411s/parity1 with Nixfmt,
RuboCop and commit-message hooks enabled and passing. Final HEAD
8e0b2d9fa1876ad2e28ce34e23724f841cacec01, tree39155267633908eadee772caac39cd8c5b74c630,
parent7f85b137 unchanged. Nix reported the expected dirty tree during the
staged amendment; no hook warning/failure remained. Tracked source/index are
clean and foreign64 files/17 directories unchanged. Original097 is preserved
in an explicit backup and the original independent-review artifacts.

Complete final range remains two coherent commits, now26 paths1709+/82-;
the amended unit is11 paths826+/59-. No OS SQL/schema migration was added.
The direct delta is exactly the seven inspected paths, SHA256
f067a4e1b4b392edb8de5cda9170e56e07cf7138fa78a2333a86c970ae043e6e.
See the [final inventory](storage-os-disabled-final-inventory.json),
[final complete diff](storage-os-disabled-final-complete.diff),
[owning unit](storage-os-disabled-final-unit.diff) and
[direct remediation](storage-os-disabled-shutdown-remediation.diff).

The Important source finding is resolved; at this checkpoint the existing
owning VM was the next acceptance step. This disposition permits that disposable test, without
publication, package/guest delivery, default integration or live physical action.

## First VM failure and bounded fixture correction

The first exact8e0 owning VM was waited with exit1/416.137s/parity1. Seven
examples passed; the eighth failed before its stop/fresh-boot/return assertions.
Its unlabelled compound returned1 with empty output, so the first failed
predicate remains unknown. Parent separately reproduced a pgrep self-match
using the exact guest binary and PIDFILE-scoped host-only children; this
establishes a test hazard, not the original failure's precise attribution.

Lead inspected the one-path correction: the same process regex runs in a
separate command and requires exact no-match status1; the unchanged compound
predicates have fixed failure labels. All eight examples, first-seven bodies,
runtime sources and normal stop/boot/system/GUID/property/payload assertions
are preserved. Static checks passed. The normal owning amendment passed
0/13.022s/parity1 with all mandatory hooks and unchanged parent/message.
Current80034c8cc6489db6287b43f439a9617511f14908,
tree497afa5c0863b2dd824664408a0e06cba4c0305d, is clean; original8e0 is retained.

This bounded fixture fix changes no interface, runtime, timeout or authority
boundary and needs no independent affected-lane rerun under the narrow-fix
policy. The original complete review and explicit shutdown step9 remain its
review provenance. The complete history is two coherent commits26 paths,
1709+/82-, with an11-path owning unit826+/59- and no OS SQL/schema migrations.
See the [current inventory](storage-os-disabled-process-final-inventory.json)
and [exact fixture delta](storage-os-disabled-process-check-remediation.diff).

The second once-launched owning VM passed at exact800: exit0/623.055s,
runner620.272s, all8 examples successful, final216.37s, source parity1. Main
verified expected_success, immutable source/foreign parity and zero owned
PGID/prefix processes/FD holders, no signals. The actual unchanged scenario
assertions cover normal activation, installed shutdown, fresh disabled boot
on preserved disks and ordinary return, exact systems/new boot ID and retained
GUID/property/known payload equality. See the [bounded result](storage-os-disabled-vm-result.json).
This does not certify production bootloader persistence or physical exclusion.
Old-byte focused runtime checks carry only for unchanged source.
The broad flake baseline error and all live/physical/G2/alias/default limits
remain. Exact800 feature publication and SSH readback are complete; stagingcbfc
is unchanged and comparison is captured. No default integration or live delivery
is claimed. Admin generated dependency update is active/pending.
