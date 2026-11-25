# Exact-5235 AMD main runtime acceptance

Read-only audit: source `5235bfd57c92bc05a25946937fe77f9803fe1c93`, base
`742eb30cb1a8b6766c85e915d26b0400e38244b1`, run `41773470432` attempt 1,
AMD job `126392676329`. Binding/env/retained Sol/xhigh roster and clean source
were reverified. No test, build, guest, CI polling/fetch or application/Git change.

## Artifact and identity

Artifact `13315369933`: 1669038 bytes; C independently matched ZIP SHA-256
`65c49c79ac99f5e3f4b96553ef794458f52044b9690d7d92ad7d6a279001c5df`.
Only the supplied selected files and ZIP were copied to
`package-c-amd-runtime-evidence/`. Its identity names exact `5235...`, lock SHA
`604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa`,
normal producer `/nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95`,
module SHA `7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f`
and sites `aiqijlwh2w2wz79d6hvcqm1p9kzl4lv3-livepatch-candidate-sites`.
Extracted sites independently hash to
`093cf255a38db5275b62370da8bac1297781e48e2ae3245c1c5b5e1ceeb23ed1`.
Guest module/sites/exact v5/v6 hash assertions all return status 0 (shell 59–90).
`test-result.txt` is `expected_success`; the runner records all 39 examples passed.

Here **shell/runner** mean the original main case files under
`package-c-amd-runtime-evidence/os-test-kernel__livepatch-6.12.95-9f465251/`.

## FUSE

The captured manifest names original `fuse:fuse_copy_finish`, position 1,
preprologue offset 5, and current caller return offset 878 (`0x36e`). Actual
U/u-filtered exact-module lookups resolve callee base `0xffffffffc0d652a0`;
both phases install `0xffffffffc0d652a5`. The live kprobe list confirms
`fuse_copy_finish+0x5 fuse` (shell 9776–9826, 10082–10132), preserving the
validated original safe entry rather than an interior call hold.

| Phase | Configured exact caller return | Actual held caller frame |
| --- | --- | --- |
| Boot-to-current | `0xffffffffc0d6588e` | `fuse_copy_page+0x36e/0x610 [fuse]` |
| Current abort | `0xffffffffc1adface` | `fuse_copy_page+0x36e/0x630 [livepatch_7]` |

Those predicates are written before installation (shell 9794/10100). Both
phases assert held Y/one hit, nonzero arg0 copy state and zero missed probes;
the boot reference-entry probe also has one hit/zero misses (9866–9918,
10145–10179). The caller frames are actual `/proc/<pid>/stack` output.
Before that hold, forced activation returns EBUSY, leaves no candidate module,
and preserves the live resend helper (shell 9639–9718). Subsequent clean
activation remains at transition 1 while the old caller is held; release
resumes the helper, yields `completed`, and allows transition 0 (9940–9994).
Resend/fatal/consume/abort states complete; current connection abort resumes to
`aborted`, and close exits successfully (10000–10255). The example passes in
23.92 seconds (runner 29–30).

Limits: these observations support hold/unwind integration and caller visibility;
no standalone reliable-unwinder return code is logged. `FR_LOCKED` clear comes
from the statically validated selected call after successful unlock, linked by
exact return PC, rather than a live flag read. Source checks caller return
before count/capture/hold; host negatives cover selector/return-offset/namespace/
ordinal/ambiguity contracts. No dedicated runtime unrelated-caller negative
exercise is logged or claimed.

## TCP

The current descriptor selects `tcp_write_xmit+0x7f9`, RAX:64 `needed`, RBX:32
`reordering`, R15:32 `mss`. Actual base `0xffffffffc1b164c0` plus the offset
gives installed `0xffffffffc1b16cb9`, confirmed as candidate `livepatch_7` in
the kprobe list; rendered fetches match the manifest (shell 15031–15118).
PID 18872 owns one socket, `198.51.100.1:58424 -> 198.51.100.2:9002`, fd 3;
the event filters that PID and UINT_MAX reordering (15013–15082).

All **232 samples** have `needed=2199023256532`, `reordering=4294967295`,
`mss=512` (runner 46–291). The completed result is independently greater than
UINT_MAX. Per-CPU overrun, commit overrun and dropped-event fields are zero;
the pre-filter kprobe profile is **294 hits / 0 missed**, exceeding the 232
accepted rows (shell 15464–15510). This proves the accepted wide-value property,
without claiming exhaustive arithmetic/race equivalence.

The receiver drains into a file and publishes status after `socat` returns.
Receiver termination/status, status 0, exact 8388608-byte length and full `cmp`
against the prepared 8 MiB zero payload all succeed; sender result is also
8388608 (shell 15140–15190). Normal receiver completion supplies EOF evidence,
rather than relying on the sender count. The example passes in 8.53 seconds.

## Separate existing boot-identity guard

Owner: `tests/suite/kernel/livepatch-kernel-identity.nix`, tag `ci`, registered
at `tests/all-tests.nix:243`. Its runtime contract is configured booted-kernel
store-path equality plus notes byte equality. Frozen-archive build-side SHA
checks are separate; no new guest-image SHA requirement is inferred.

The AMD ZIP listing contains no identity case. Root supplied the already-retained
original native artifact `13305053333`, same run/attempt/head: 3204585 bytes,
independently matched SHA
`ea963e32e88a62ca3e65c6b44f510bdec6593208d59757732c3565c3e3fee13f`.
Only `os-test-kernel__livepatch-kernel-identity-01903708` runner/shell/console
were extracted separately under `package-c-amd-runtime-evidence/native-kernel-identity/`.

Actual configuration is **6.12.95**. Native shell 50–64 names
`/nix/store/050sh2hfrnpc8j5abr2npp7bnlxvpb8a-linux-6.12.95-frozen-boot/bzImage`
and notes `m6gw1jc4kdc0j6f2xr2901agkgmmss1k-livepatch-kernel-notes-6.12.95`.
Notes `cmp` and booted-path equality succeed (95–107); normal wrapper
load/status/unload/reload/retry and wrong-notes load/unload/status refusals
with active protection retained are real. Six examples pass.

The wrong-image negatives at native shell 225/245 also emit `readlink: command
not found` (230/250) before generic refusal. They fail closed but do not isolate
image-mismatch rejection from the missing tool environment. That stronger
negative proof is not claimed. The owning source is byte-identical base→5235:

- Identity test blob `1036ac7a4b075324b9d79c72c5aadbd88f753054`: line 32
  resolves the underlying tool; lines 74–86 invoke it directly (81).
- `os/modules/services/livepatches/default.nix` blob
  `936d937e6efd64e5ad9c963e5303f2559a4ad6cd`: line 368 uses unqualified
  `readlink`, 369 compares notes, and 370–372 emit generic refusal.

This is a pre-existing control/environment weakness in unchanged source, with
no new-feature source cause demonstrated. No base VM rerun is claimed. The
positive guard executes in its own frozen .95 guest; it does not independently
hash the image bytes of the separate main FUSE/TCP guest.

## Remaining scope

Other main successes include exact v5/v6 transition/failure anchors (runner
1–6), SVM repair (7–8), occupied/unshadowed SUNRPC refusals (25–28), NFtables
batch holds (39–40), SUNRPC worker/drain/callback ownership/shadow allocation
(299–306), and final transition/kernel health (325–326). These are recorded
case successes; the detailed audit here is FUSE/TCP plus the identity guard.

No whole-matrix or later updated-image native result is inferred. The lead owns
remaining CI, baseline decisions and final acceptance; the updated-image native
device unit is not waived. Original failures, rejected correction and host
records remain intact. Source stays frozen and the session remains open.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>
