# Exact f60d fallback capacity/cache plan (no image admission)

Source: f60d41a453b1703e42de4341285bdc6ba339aff0, tree
f6656bd2c1d49f308c6cc1697ad3fb1c44d2be5c. The exact-head hosted CI is actively
running tests, so local duplicate images/guests remain held. This document is
read-only preparation, not runtime acceptance or a resource claim.

## Native capacity

Pinned testsMeta requests alerts 2 machines/12 CPU/16 GiB RAM and shm; legacy
browser 3 machines/16 CPU/24 GiB RAM and shm. Preserve these supported sizes.
The unmodified pinned ResourcePool, with no TEST_RUNNER_* overrides, reports
77.2 GiB usable RAM, 39.1 GiB shm and 96 CPU after its default 8 GiB RAM/shm
reserves. The later final can_reserve? probe observed 78.6 GiB RAM with the same
shm/CPU budget and accepts each scenario sequentially.
See shared-f60-{resource-pool,admission-probe}.json. This is a fresh probe, not a
reservation; refresh immediately before any later guest admission.

Fresh df before dry-run: root/store/tmp share one filesystem with
175,055,798,272 bytes available; /dev/shm has 50,613,551,104 bytes available.
The 20 GiB shared root reserve remains mandatory. Final df is retained in
shared-f60-df-final.txt. Owner3 was notified; KB heavy work remains unadmitted.
No foreign cleanup, fixture reduction or profile/root deletion is proposed.

## Exact inputs and cache plan

Pinned vpsAdminOS source: /nix/store/zd7z6pw3pkk6099kjvjryqq5xxgblygw-source
(revision 8e44a5124439b1f3048ffc56b1717614a5360358). Complete unchanged lock graph
is in shared-final-history.json.

Nix drv evaluation needed one source-copy-only import-from-derivation:
/nix/store/sw6qkwx0bjavdz30pv9k716jirwkgwg2-vpsadmin-source-unknown.drv.
Its output /nix/store/1d173shma9rmllpxliq8wpg4qrpw41j0-vpsadmin-source-unknown
occupies 23,154,688 allocated bytes. It copies source and patches script
interpreters; no image/guest/kernel or dependency expansion was realized.
The four feature/schema source hashes match exact f60d bytes;
shared-f60-source-ifd-equivalence.json and shared-f60-source-ifd.json preserve
that evidence. This unavoidable evaluation allocation is recorded explicitly.

Exact test derivations:

- /nix/store/nnx5inaa3zbkb9m4bd8pxkvm5d8b7vg1-os-test-alerts-incident-escalation.json.drv
- /nix/store/bz4qw5l516mmaqkhincqak1yr68dmzsw-os-test-vpsadmin-webui.json.drv

Exact dry-run command (exit 0; no image realization):

```sh
nix build --dry-run --json --no-link \
  '/nix/store/nnx5inaa3zbkb9m4bd8pxkvm5d8b7vg1-os-test-alerts-incident-escalation.json.drv^*' \
  '/nix/store/bz4qw5l516mmaqkhincqak1yr68dmzsw-os-test-vpsadmin-webui.json.drv^*'
```

Native plan: 197 derivations to build, 48 substitutions; 198.8 MiB compressed /
304.0 MiB unpacked. Linux 6.18.45 and its modules are substitutions, not planned
kernel compilation. Stop and investigate if an owned actual build later differs.
The exact final top-level profiles, service root images and node squashfs paths
are in shared-f60-machine-inputs.json. None is realized locally. The dry-run JSON,
full native plan and five image derivations are shared-f60-dry-run.{json,log},
shared-f60-test-derivations.json and shared-f60-image-derivations.json.

## Disk estimate and shortest conditional fallback

Nix does not report the allocated output size of unbuilt closures. Previous
owned equivalent-layout images measured service roots 4.95/5.60 GiB apparent,
3.33/3.90 GiB allocated, and 0.40 GiB node squashfs each. These are planning
observations, not exact final image sizes or runtime proof. Current image
builders derive their size from installed closure, inode/5.2% filesystem
allowance and 512 MiB extra; node data disks remain sparse 20G each.

Conservative provisional envelopes, pending actual completed measurements:

- Cached new closures plus both retained final image outputs: 15 GiB.
- One-job build temporary closure/root copies: 10 GiB additional peak.
- Alerts runtime: 28 GiB (full logical 20G node disk + service root copy and logs).
- Browser runtime: 48 GiB (two full logical 20G node disks + service root copy/logs).

The runtime envelopes deliberately budget the full logical data disks despite
sparse allocation. With both run artifacts retained, these provisional envelopes
plus the shared 20 GiB reserve total 121 GiB, below the observed 163.0 GiB free.
This is an estimate, not final admission: actual closure/image size can differ,
and other host activity changes free space.

If hosted equivalent proof is unavailable and lead releases the fallback, build
only the alerts test derivation first with --no-link --max-jobs 1 --cores 4.
Measure actual store/image/temp growth and recheck the 20 GiB reserve before any
runtime. Run only alerts/incident-escalation with native one-job scheduling and
stop-on-failure, retaining failed evidence/effects. Reassess before building the
browser derivation and running only webui#incident-escalation. No full-tag local
campaign. Do not duplicate an equivalent hosted scenario already executing.
Fresh default ResourcePool and shared disk coordination precede every admission;
all source, build and runtime effects stay owned through terminal receipts.

## Shared KB accounting update

Owner0 has no active or queued heavy LOCAL image build, guest, browser/capture
run or runtime reservation. The 25/28/48 GiB envelopes above are unadmitted
planning estimates and must not be counted as held allocations in owner3's KB
proposal. Current retained small dependencies: root .gems 37,791,909 bytes,
API .gems 76,534,156 bytes, source-only IFD 23,154,688 allocated bytes and prior
PHPUnit cache 9,605 bytes. Captured foundation evidence is 1,210,076 bytes; only
small hosted-CI evidence/observer-log growth remains pending. No dependency
expansion or explicit final-image GC pin is planned. Latest root/store/tmp
free observation is 163,174,195,200 bytes; /dev/shm 50,613,551,104 bytes. These
are shared-host observations, not an allocation or admission. The 20 GiB shared
reserve remains. Lead and owner3 received this same accounting; source f60d is
unchanged. No KB admission or four-PNG capture proof is inferred from native CI.

Owner3 later received lead admission for exact KB7bdee full-screenshots bridge
capture: 68 GiB new runtime peak plus the 20 GiB shared floor, native watcher47933,
with max-jobs1/cores4 and four guests. Owner0 acknowledged to lead and owner3:
there is no backend heavy local allocation or pending reservation against these
bytes. Only hosted integration observation/small evidence growth remains owned.
Any future backend local fallback requires fresh coordination; the earlier
planning envelopes do not reserve capacity. No cleanup, resizing or duplicate
local scenario was started.

Fresh owner0 confirmation for owner3's later reviewed source56d716e proposal:
no current/pending heavy local allocation or runtime reservation. Since the prior
confirmation only the authorized single live-log404 diagnostic and small evidence
writes occurred; no package/image realization, dependency expansion or guest
launch. Earlier owner0 envelopes remain unadmitted estimates. The lead and owner3
received the same fresh accounting; no backend held-growth addition is needed.
The existing hosted integration observer is the only owned active verification
operation. Any future owner0 heavy local action requires fresh coordination.
