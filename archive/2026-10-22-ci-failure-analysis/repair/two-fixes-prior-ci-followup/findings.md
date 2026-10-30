# Prior cb4 CI: two distinct failures beyond fetch/aging publication

Run [40174698311](https://github.com/vpsfreecz/vpsadminos/actions/runs/40174698311),
attempt1, exact head `cb4dcaaa397cad1f18c8f3c067b95bb8036072dd`.
These are **prior-head results**, not verification of `96facc497`.
Metadata was read first; only the two completed failed jobs were investigated.
The run-level API response still said queued; exact completed job metadata and
artifact evidence identify the observations below, without inferring whole-run
completion or observing the other running jobs.

## Native suite: cross-sample procfs inode assertion

Job121115448755, native artifact12595363719 (3,438,135bytes), SHA256
`bf9dda95159d2e99479ff191cf036b5a264045858a24f9237b0b5f47c5cce08c`.
`native/test.log:5032–5037` reports317scripts/109tests,107success and2failures:
only impermanence@v1 and@v2. Preparation succeeded and guests ran; this does not
match the earlier HTTP429 prebuild failure.

Both retained case `test-runner.log:5–6` JSON records precede the failure at
line11: `impermanence proc changed across import` on the first candidate import.

| Case | Same PID | Same start ticks | Before proc `[dev,ino]` | After proc `[dev,ino]` |
| --- | ---: | --- | --- | --- |
| v1 | 2808 | 6855 | `[29, 7694]` | `[29, 11274]` |
| v2 | 2823 | 6798 | `[29, 7077]` | `[29, 9648]` |

For both cases, device29 stays the same and only proc inode changes. PID/birth,
root dev+inode, mount namespace identity, cgroup, root mount rows, dataset
name+GUID+mountpoint+origin, mountpoint/private identities and payload markers
are equal across these observations. Each individual sample has stable root/
namespace and unchanged birth-before/after. This supports continuity at these
observations; it does not certify the later reload/new-writer/cleanup assertions,
which were not reached after this failure.

Source boundary: `tests/suite/upgrade/impermanence-from-2abbe3cc1c10.nix:76–79`
defines identity as stat dev+inode. Lines108–157 pin proc/root/namespace FDs only
within a single probe. Lines159–164 start a separate Ruby process for each
sample, so those FDs do not remain held across the userspace switch. Lines225–226
then require `proc` equality across the two samples alongside PID/birth and
root/namespace/dataset authentication. That unsupported cross-sample procfs
inode-stability assumption is the immediate fixture failure. Procfs inode/dentry
recreation after closing a sample is a plausible mechanism; the logs do not
prove eviction/recreation or its trigger. They do not demonstrate a restarted
container, wrong dataset/root or payload loss, and do not prove every product
property correct.

Narrow next recommendation: architect-owned fixture identity design that keeps
strict authenticated process/root/namespace continuity while accounting for the
actual lifetime of the procfs handle. Prefer retaining the relevant identity
handle across the transition if practical, or independently justify an equally
strict lifetime/identity contract. Do not simply drop `proc`, accept mismatches,
or weaken PID/birth/root/dataset/payload assertions. No source change or run is
selected by this finding.

## Aged-v6: cumulative kernel-health failure after aging

Job121115448797, aged-v6 artifact12599466808 (743,061bytes), SHA256
`e964147fa63ed90c5026ec84af8800d2eb5d5066bd7bc88d672beb8ee41c9342`.
Retained `aged-v6/os-test-kernel__livepatch-qualification__amd-scale-aged-v6-0921d60d/test-runner.log:103–110`
shows the failed negative dmesg health assertion, not the earlier strict
counter-publication comparison. Lines151–164 show an RCU-preempt stall on
CPU97, PID30382/insmod, with the NMI stack in `smp_call_function_many_cond`;
lines179–190 continue through page attributes/text ROX and module loading.
Earlier nfnetlink_queue pre-patch refusals are recorded, then livepatch7 later
completes (lines202–204). Their relationship to the stall is not established.
Post-transition hotplug health observation is logged at309. Aging observation
was passed; delayed aging-counter publication is not this run's first failure.

The strict health check correctly exposes a retained stall report. Its kernel,
host-scheduling, instrumentation or module-load cause is unresolved within this
bounded evidence. Do not attribute it to a particular patch or loosen the health
predicate. A separately selected investigation may start from this exact
stack/event window; no broad kernel investigation, new probe or retry occurred.

## Bounded retention

Transferred4,181,196bytes total; only eight named summary/failure log/result
members were unpacked (944,444bytes). Full native archive contents would be
36,764,113bytes, so they were deliberately not unpacked under the32MiB cap.
No images/full state or additional artifacts were retrieved. Artifact member
metadata is retained separately. No earlier758 artifact was duplicated.
No source/Git/Nix/build/VM/probe/rerun/cancel operation occurred.

Selected retained hashes:

- `artifact-12595363719.zip`: `bf9dda95159d2e99479ff191cf036b5a264045858a24f9237b0b5f47c5cce08c`
- `artifact-12599466808.zip`: `e964147fa63ed90c5026ec84af8800d2eb5d5066bd7bc88d672beb8ee41c9342`
- `native/test.log`: `7640ea3f406d969f271e03a01f64fee3dd628446eabeef94278a8297ce090296`
- `aged-v6/os-test-kernel__livepatch-qualification__amd-scale-aged-v6-0921d60d/test-runner.log`: `aea8f76f3a4f6ba58da2e49ab52fdf9e3ff0f3a79878314754054f1ed8e6cf23`
