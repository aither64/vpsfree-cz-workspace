# Package C: e175 Intel runtime acceptance

This read-only audit covers run `41865572140`, attempt 1, successful main Intel
job `126712393509`, source `e1751c917f216897292ab0b893727a6e5553a540`
(assigned base `2951a632c4254a44747a8da326e3dde897eaa0e2`). Session/env and
the retained implementer3 Sol/xhigh workspace-write roster were reverified.
Only retained artifacts/source were read; no fetch, CI polling, check rerun,
build, VM, application edit, Git mutation or lifecycle action was performed.

## Artifact and selected cases

Independently verified `ci-e175-intel-artifact.zip`: **276764 bytes**, SHA256
`ecf57a418c915c3e3230ea23e65cfdf7d810aae87fc4bdb1ce187fe4065b7206`.
The raw job log lines 457–464 record the same digest/size for artifact
`13349589578`, `os-test-logs-41865572140-1-livepatch-intel`. The 76 listed
members are safe relative paths without traversal or symlinks. Selected copies
and bounded retention/build context are in `package-c-e175-intel-evidence/`.

Raw log lines 261–272 select exactly these 11 cases: fragment; lifecycle
6.12.110, .95-v5 and .95-v6 (`#intel`); NFS transition; v7 performance;
Intel retention-v5/v6; hostile SCTP; Intel TUN; NFS cancellation. Lines 414–415
report **11 scripts / 11 tests successful in 5217.23 seconds**. The raw log
contains 80 successful example events and three successful script-only
lifecycle events. Other than the selected fragment and retention evidence
below, these are case/example completion results, not a fresh semantic audit
of every witness.

The artifact contains neither `kernel/livepatch-6.12.95` main nor
`kernel/livepatch-kernel-identity`. Main selects `livepatch-amd`
(`livepatch-6.12.95-common.nix:500–507`); fragment selects both vendors
(`livepatch-inet-frag.nix:20–22`). **No e175 FUSE/TCP acceptance is claimed**:
those witnesses belong to the AMD row. The separate native identity-case
absence is also expected row scope. No additional artifact was requested.

## Source, producer and guest identity

Raw log lines 108–136 record checkout/full revision; lines 165–166 contain
the source/lock guards, and lines 245–250 agree with the extracted identity:

- Checkout path: `/run/github-runner/runner/vpsadminos/vpsadminos`.
- Source: `e1751c917f216897292ab0b893727a6e5553a540`.
- Input-lock SHA256: `604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa`.
- Normal producer: `/nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95`;
  module: its `lib/modules/6.12.95/extra/livepatch_7.ko`.
- Module SHA256: `7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f`.
- Sites: `/nix/store/aiqijlwh2w2wz79d6hvcqm1p9kzl4lv3-livepatch-candidate-sites`;
  extracted JSON SHA256: `093cf255a38db5275b62370da8bac1297781e48e2ae3245c1c5b5e1ceeb23ed1`.

Fragment shell lines 41–53 show successful guest module and sites byte checks.
The JSON is schema 1, with that module digest, ELF64/EM_X86_64 and build ID
`fd8cbfe4c314ddac8f35d87bee4bb8b909e479d5`.

Actual fragment VM launch metadata (`inet-frag-machine-log.log:11–21`) names
`/nix/store/050sh2hfrnpc8j5abr2npp7bnlxvpb8a-linux-6.12.95-frozen-boot/bzImage`
and system
`/nix/store/jpvhl8dyxm84dihqdzp4wrxx9pbw7fkz-vpsadminos-system-vpsadminos-26.05.git.e1751c9`.
It records direct boot, 2048 MiB and two CPUs. Guest `uname -a` is
`6.12.95 #1-vpsAdminOS SMP PREEMPT_DYNAMIC Sun Jul 5 16:42:06 UTC 2026`;
initial/current/final release checks succeed. `26.05.git.e1751c9` is the
observed system-store version label. Selected logs do not print structured
`sourcePath`, `shortRev` or `dirty` fields. The repository-source derivation
`/nix/store/s0gff2skpfgysvmv03xq1g3dz9cczg3b-test-runner-repository-source.drv`
is logged (raw lines 259–260), but its output source-store path is not.

This establishes the recorded launch path and guest kernel stamp, not an
independent in-guest boot-image SHA or notes comparison. The existing native
kernel-identity guard and its pre-existing wrong-image `readlink` control
limit remain separately scoped in
[the earlier identity audit](package-c-main-runtime-acceptance.md); this Intel
artifact supplies no new result for that case and adds no new requirement.

## Fragment witness actually executed

The captured `inet_frag_timer` record identifies `livepatch_7:inet_frag_find`,
sympos 0, `.text`, size 1928, offset 950 (`0x3b6`), instruction length 5;
`call_observe` / `observe_only`, inline `inet_frag_create`, `arg0=rdi:64`,
callee `vmlinux:mod_timer` sympos 0. The instruction is within the recorded
function bounds. ABI node/timer/lock offsets 0/56/96 produce the executed
`next=-56(%di)` and `lock=+40(%di)` fetches. The consumer validates these
finite namespace/kind/frame/inline/callee/ABI/bounds requirements before boot
(`livepatch-inet-frag.nix:59–82`).

Actual shell line 1091 runs the corrected query:

```awk
$2 !~ /^[Uu]$/ && $3 == "inet_frag_find" && NF == 4 && $4 == "[livepatch_7]" { print $1 }
```

It returns exactly `ffffffffc1ecff50` (line 1096). The unchanged exact-one
consumer validation precedes address use; there is no first-match/dedup
fallback. Line 1100 installs `target_timer` at `ffffffffc1ed0306`, exactly
base + `0x3b6`. This reaches the target observation that failed before probe
installation in the old 48/DS1 history.

| Phase | Actual trace | Node/lock | Profile |
| --- | --- | --- | --- |
| Native | `inet_frag_find+0x22f/0x730`, shell line 658 | `next=0`, `lock=0` | 1 hit / 0 missed, lines 662–667 |
| Current target | `inet_frag_find+0x3b6/0x790 [livepatch_7]`, line 1189 | `next=0xffff954e0ece9641`, `lock=1` | 1 hit / 0 missed, lines 1193–1198 |

Both timer pointers are nonzero; each trace records 1/1 entries. The case
asserts every parsed target observation has a linked node and held lock, every
native observation has neither, and profile hits equal observed rows with
zero misses (`livepatch-inet-frag.nix:141–161`). This proves that property at
the selected timer-registration call for this stimulus; it is not a general
race-freedom or all-traffic claim.

Both events are removed. Patch disable finishes, the patch sysfs entry
disappears, module removal, namespace deletion and trace-instance removal
return 0 (shell lines 1202–1286); final unpatched checks and the cumulative
kernel-health assertion pass. VM exit is 0 and normal runner destruction is
recorded (machine log lines 27–50). The example succeeds in 7.2 seconds and
the case result is `expected_success`.

## Exact predecessor and retention scope

The extracted retention-v5/v6 shell prefixes show successful current module
and sites checks, plus exact released-v5
`b31f64403d9d55f62e3d59e4bbefcbddcbda4fa66a2dc0689f9bb7cd7e927984`
and v6 `960b13f1b461b95e29cccff58ddf0d3f3badf151046eb46eba36a9c8c7e5efe3`
checks. The corresponding runners record retained-predecessor rejection,
successful normal activation/disable, expected callback/transition counts and
CPU-hotplug health checks. These are the 128-task, four-vCPU retention
profiles, not aged/scale qualification.

The audited e175 Intel fragment contract passes with its actual current
producer. No new runtime defect or required-contract gap was found in this
bounded evidence. FUSE/TCP, native identity and remaining matrix acceptance
stay with their owning rows; reused D81/207/A99 host checks are not guest
passes. This receipt makes no whole-matrix or merge-acceptance claim.
