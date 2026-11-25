# Exact-5235 Intel fragment evidence

Read-only acceptance audit of run `41773470432`, attempt 1, Intel job
`126392676335`, source `5235bfd57c92bc05a25946937fe77f9803fe1c93`.
Session/env and clean current source were reverified. The existing watcher
provided one artifact; C launched no fetch, polling, test, build or guest.

Artifact `13301170153` is `os-test-logs-41773470432-1-livepatch-intel`,
267139 bytes. C independently hashed the retained ZIP and matched the raw job's
SHA-256 `45eba6538382eaecd2c41a6a95b60b4787e992461fe9375f9bdc3b454144be7e`.
Sources: [raw job](ci-41773470432-126392676335.log) and the requested extracted
files beneath `ci-41773470432-intel-evidence/`.

## Identity and executed site

The uploaded identity binds exact source `5235...`, input-lock SHA
`604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa`,
normal producer `/nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95`
and site output `aiqijlwh2w2wz79d6hvcqm1p9kzl4lv3-livepatch-candidate-sites`.
The guest's actual module checksum test succeeds against
`7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f`
(shell log lines 50–53). C independently hashed the extracted sites file to
`093cf255a38db5275b62370da8bac1297781e48e2ae3245c1c5b5e1ceeb23ed1`;
the guest checks that same value successfully (lines 59–62).

The schema-1 record selects `livepatch_7:inet_frag_find`, position 0, `.text`,
size 1928, call offset 950 (`0x3b6`), length 5, inline `inet_frag_create`,
callee `vmlinux:mod_timer`, and arg0 `rdi:64`. ABI fields are node 0, timer 56,
lock 96, producing the executed `next=-56(%di)` and `lock=+40(%di)` fetches.

The actual shell command at lines 1100–1105 excludes both printed `U`/`u`,
requires the exact symbol, four fields and `[livepatch_7]`, and returns only
`ffffffffc1bdcf50`. Adding the captured offset yields
`ffffffffc1bdd306`, exactly the registered target probe at line 1109. Its
trace independently labels that address `inet_frag_find+0x3b6 [livepatch_7]`.
The raw lookup prints addresses only; no printed import-type character is
invented from it.

## Observations and completion

| Phase | Executed timer site | node.next | lock | Hits / missed |
| --- | --- | --- | --- | --- |
| Native | `inet_frag_find+0x22f`, `0xffffffff8497ff4f` | `0x0` | `0` | `1 / 0` |
| Current v7 | `inet_frag_find+0x3b6 [livepatch_7]`, `0xffffffffc1bdd306` | `0xffff9533d300b291` | `1` | `1 / 0` |

Each trace has one row and reports entries-in-buffer/entries-written `1/1`.
Explicit kprobe profile queries return `1 0` for native (shell lines 671–676)
and target (1202–1207), matching the observed row counts. Native uses fragment
ID port 49152; target uses 49153, preserving fresh queue creation. The current
queue therefore has a nonzero hash-node link and the lock's held bit set at
the selected timer-registration call, while the native queue has neither.
This is the accepted finite observation, not exhaustive list/race correctness.

Activation completes with enabled 1/transition 0. Normal disable waits until
the patch sysfs directory disappears, then module removal, namespace removal,
trace-instance removal and final unpatched checks all succeed. The existing
post-baseline kernel-fault matcher passes. The sole example succeeds in
9.06 seconds; the test succeeds in 40.78 seconds (raw job lines 390–395).

The guest repeatedly verifies release 6.12.95 and logs
`#1-vpsAdminOS SMP PREEMPT_DYNAMIC Sun Jul 5 16:42:06 UTC 2026`.
The declared source uses the immutable boot archive and native offset, but
these extracted fragment files contain no independent boot-image SHA or notes/
build-ID check, nor a configuration/QEMU boot-store path. That is an explicit
evidence limit; exact boot-byte identity is not re-proven by this case alone.
No additional check or artifact collection was initiated to fill it.

## Relation to the failure and remaining scope

The old `48f2983e` attempt failed before target probe installation because its
module-qualified name query returned the definition and an import alias.
Rejected `65d43ee` filtered only uppercase U. This exact-5235 execution passes
the corrected lookup and reaches the current linked/locked observation with
nonzero hits and zero missed probes, then completes normal removal. Original
failure, rejected review and 57-example host evidence remain in
[the correction receipt](package-c-runtime-symbol-failure.md).

This accepts the recorded fragment witness on this Intel run/module/sites.
It makes no FUSE/TCP, arbitrary-build equivalence or whole-matrix claim. The
user's full final-head CI/integration condition remains with the lead; no
baseline exception or test waiver is supplied here. Application source remains
frozen; C performed no Git, CI, runtime, deployment or lifecycle mutation.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>
