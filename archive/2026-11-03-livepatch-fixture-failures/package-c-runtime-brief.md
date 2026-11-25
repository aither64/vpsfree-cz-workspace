# Package C focused runtime brief

No build, VM or dispatch has been performed by C. The only realized output
in the refreshed preflight is the exact signed 5.3 KiB published site metadata.
Current reviewed/reconciled head is
`5235bfd57c92bc05a25946937fe77f9803fe1c93` on
`742eb30cb1a8b6766c85e915d26b0400e38244b1`; see
[DS1 reconciliation](defined-symbol-review-reconciliation.md).

## 5235 refresh: local execution remains blocked

As of 2026-11-04T04:27:37Z, binding/env/retained roster and the exact clean head
were reverified. AMD EPYC 7551 exposes 64 CPUs, SVM and nested KVM (`nested=1`);
`/dev/kvm` is readable/writable. The native resource detector reports 63.8 GiB
usable memory and 39.1 GiB shared memory after ordinary reserves, with 139 GiB
disk available. These are host preconditions, not live KVM acceptance.

The current declared fixture still selects normal producer
`/nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95` and site
output `aiqijlwh2w2wz79d6hvcqm1p9kzl4lv3-livepatch-candidate-sites`.
The module independently hashes to
`7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f`.
Published site metadata has NAR size 5416, no references and a
`cache.vpsadminos.org` signature. It was substituted with signature checks,
`max-jobs=0` and empty builders, then checked for schema 1 and matching digest.
The owned ordinary root is `package-c-5235-preflight-sites` in this directory.
[Declared paths](package-c-5235-input-paths.json),
[signed site metadata](package-c-5235-sites-cache.json).

With import-from-derivation disabled, the full fragment configuration evaluates
to `/nix/store/gkgbxsdi6gd7a30chmll2i540n8fyidz-os-test-kernel-livepatch-inet-frag.json.drv`
(output `/nix/store/zg1prfx4ns9ikn6hcnkx8g7f3ajpcpr0-os-test-kernel-livepatch-inet-frag.json`).
The **single combined dry-run request** plans 73 builds and 83 fetch paths,
9.6 MiB download/155.6 MiB unpacked. It includes the following blocking builds:

- `/nix/store/n0p9jpf4hxabq0l2hq9li6im0lrm4vkz-util-linux-2.42.2.drv`
- `/nix/store/icvglgqkdya2cgpn0zspkcmlv5xjiyl3-nix-functional-tests-2.34.8.drv`
- `/nix/store/riy6wi71n9qxi63fxrb5zm4cm0ih5i9m-nix-2.34.8.drv`
- `/nix/store/hpjypr6g0sfaa3ygahvcmi5vgxb33b7m-linux-6.12.95-frozen-boot.drv`
- `/nix/store/zv08ymyy94q7k8lhg675mybszda46s98-linux-6.12.95.drv`
- `/nix/store/sp29nf66lg6slc9qkzbrjpz9r5gjywva-zfs-builtin-2.3-vpsadminos-6.12.95.drv`

The frozen-boot derivation restores archives; the separate `zv08...` derivation
is a source-kernel build. Its output paths include
`/nix/store/1rb784fkpjvwn8lagf576j66p155il7b-linux-6.12.95-dev` and
`/nix/store/lasxgw6y0zf5c1rk6icarwbn831rj5al-linux-6.12.95`.
The plan also lists source/configuration generation, ordinary OS/image outputs
and the small IPv6 fragment helper
`170hna1qrbw9ylplimg8qy8xn9ln6mrx-livepatch-test-ipv6-fragment-partial-1.drv`.
No planned build was started.
[Complete dry-run list](package-c-5235-full-dry-run.log),
[selected derivation output map](package-c-5235-missing-output-paths.txt).

Scope limits are explicit: this proves the fragment closure is cold. Main
FUSE configuration evaluation stops at its required hash/validity check for
the missing declared v5 output
`/nix/store/n4d1ckknkikj0gw8yyx3q8wayipnr93y-livepatch_5-exact-predecessor.ko`.
The exact v6 output
`/nix/store/ih964l97vj8906s0v58y6pk1p7jv4c07-livepatch_6-exact-predecessor.ko`
is also absent. Public cache metadata returns null for both; their bytes were
neither realized nor replaced. The main/TCP shared configuration closure is
therefore incomplete, not claimed dry-run complete.
[Main evaluation failure](package-c-5235-main-eval.log),
[predecessor cache metadata](package-c-5235-predecessor-cache.json).

The selected final runner output `pswxbm2vy5gb4wqqjbzn2kasa100mzvc-test-runner`
is not realized. The combined request reported these three derivation-path
metadata strings as unknown, so their subclosures are not claimed inspected:
`98acngpcrjaamlcrimvxf6mr82y8bmp7-test-runner.drv`,
`bqa0dfrhsvg4zb7bzipvlydaihrkgfdv-livepatch_5-exact-predecessor.ko.drv` and
`cyknqlv4drzizh6zkfaxxa1fhfbv4g60-livepatch_6-exact-predecessor.ko.drv`.
Only the declared producer/module and signed site metadata were validated
locally; no scratch SDK/JSON stood in for package or VM proof.

The lead accepted STOP. No further local evaluation, dry run, realization,
build, VM or environment investigation is planned. The shortest supported
route is reviewed unfiltered remote CI on exact `5235...`, retaining all nine
rows and every focused property. It provides no focused-before-full ordering
and no test waiver. The conditional local recipe below remains unlaunched.

## Earlier preflight history

Source/metadata inspection started at clean
`4fc0f375de34f92dd59aef94080e874b302c720c`. Review then required the narrowly
assigned R1/R2 corrections. The lead reconciled those narrow fixes at final
head `efc5f8fe87f7b0ddc09b5946047e1c231d23db67`; see
[review-reconciliation.md](review-reconciliation.md). This retains the original
independent review plus the stated narrow remediation checks, without claiming
a new full-head review. No historical candidate or new runner mode.

## Initial efc preflight (retained evidence)

Read-only preflight confirmed that final head and a clean worktree. Metadata
evaluation and dry runs completed; no realization, build or VM was launched.
The host exposes AMD EPYC 7551/AMD-V and a readable/writable `/dev/kvm`.
The actual native resource detector, loaded with the cached declared Ruby
3.4.11 interpreter, reports 55.1 GiB usable memory and 26.4 GiB usable shared
memory after the existing reserves; 64 physical/logical CPUs are exposed
(the normal scheduler budget applies its 1.5 CPU factor). Disk has 145 GiB
available. This is preparation evidence, not a live KVM capability result.

The final declared runner is not realized. Its dry run needs only three
wrapper derivations, with the runner/native dependencies already cached:
`6mc5fzniyndabb62k7f0psw26d2j3m97-test-runner.drv`,
`n1y72phnpbk21caq0l95d1xrsmna6k24-test-json-runner.drv` and
`n8vfc8ycglpnvkkqjghc5nfyhyv7s888-test-runner.drv`.
[Runner dry run](package-c-preflight-runner.log).

The declared candidateSites closure is **not warm**. Its exact dry run lists:

- `/nix/store/n0p9jpf4hxabq0l2hq9li6im0lrm4vkz-util-linux-2.42.2.drv`
- `/nix/store/icvglgqkdya2cgpn0zspkcmlv5xjiyl3-nix-functional-tests-2.34.8.drv`
- `/nix/store/riy6wi71n9qxi63fxrb5zm4cm0ih5i9m-nix-2.34.8.drv`
- `/nix/store/hpjypr6g0sfaa3ygahvcmi5vgxb33b7m-linux-6.12.95-frozen-boot.drv`
- `/nix/store/asfl9yry0hdavkhmv9ib8xcd4msknniz-livepatch-candidate-sites.drv`

It also lists 52 substitutable paths, 1.5 MiB download/128.3 MiB unpacked.
The frozen-boot derivation restores archived bytes; its name is not evidence
of a kernel compilation. Its retained Nix/util-linux support dependencies
would nevertheless require local builds under the current cache plan.
[Site closure dry run](package-c-preflight-sites.log).

This derivation selects the normal producer
`/nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95`; its module
was independently rehashed as
`7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f`.
Its declared site output
`/nix/store/aiqijlwh2w2wz79d6hvcqm1p9kzl4lv3-livepatch-candidate-sites/sites.json`
does not yet exist. Full configuration evaluation reads and hashes that exact
file, so the complete image/configuration closure remains unevaluated behind
this packaging barrier. Scratch SDK/JSON evidence was not substituted.

The lead selected the existing unfiltered `ci` workflow on this exact head,
with `test_pattern` empty, as the supported remote route. It includes the
AMD FUSE/TCP examples and all nine livepatch rows but does not provide focused
FUSE-before-TCP-before-matrix ordering. Remote closure availability is not
proven by this local preflight. All planned focused properties remain required
in the AMD main/Intel rows. Local realization is held; the conditional focused
command below is retained only as a later failure-diagnosis recipe and is not
cleared to launch.

## Route and ordering

Existing local/admin-runner support is sufficient: opt in to livepatch test
discovery, select `kernel/livepatch-6.12.95`, and use the existing exact
`VPSADMINOS_LIVEPATCH_EXAMPLE_FILTER` for each short diagnostic. These runs
are **focused diagnostics**, not the full main suite or qualification matrix.
Qualification rejects the example filter by design.

There is no safe narrow invocation through the current GitHub workflow inputs.
A nonempty `test_pattern` disables `livepatch-lifecycle`; the native test job
does not set livepatch discovery or prepare module/sites/predecessor variables.
Dispatching that native pattern is not FUSE/TCP acceptance. A must not add an
unsupported environment assumption to the remote launch.

After review: prefer local focused FUSE, then TCP, then the remaining probe
cases below if preparation can use the declared cached closure. Launch the full
nine-row remote workflow after these pass. If local preparation requires an
unexpected kernel/old-toolchain build or suitable runner capacity is unavailable,
stop that path and use the existing unfiltered nine-row workflow as the
smallest supported remote alternative. Its AMD main row includes both cases;
do not claim that alternative provides a focused-before-full ordering.

The current shell reports AuthenticAMD EPYC 7551, AMD-V, and a readable/writable
`/dev/kvm`. This establishes basic local eligibility, not guest/KVM acceptance.
Keep native CPU feature, resource admission and configured machine-shape checks.

## Exact preparation and first two invocations

Run from the registered vpsAdminOS worktree after the review gate. Set the local
shell variable `reviewed_head` to the lead-recorded final amended/reviewed SHA.
Prefer the
already captured normal producer/sites from the **same exact-head** CI build
when available. Otherwise the following existing attributes capture one current
artifact for this diagnostic batch. Preparation is a separately monitored
operation; inspect its planned closure before realizing it.

```sh
set -euo pipefail
reviewed_head=5235bfd57c92bc05a25946937fe77f9803fe1c93
: "${reviewed_head:?lead must supply the exact reconciled final head}"
[[ "$reviewed_head" =~ ^[0-9a-f]{40}$ ]]
test "$(git rev-parse HEAD)" = "$reviewed_head"
test -z "$(git status --porcelain)"
runtime_root=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-livepatch-fixture-failures/package-c-runtime-${reviewed_head:0:8}
test ! -e "$runtime_root"
mkdir -p "$runtime_root"
unset VPSADMINOS_CONFIG VPSADMINOS_ONLY_LIVEPATCH_TEST \
  VPSADMINOS_LIVEPATCH_SINGLE_SERIES_MODULE VPSADMINOS_LIVEPATCH_MODULE_NAME \
  VPSADMINOS_LIVEPATCH_EXAMPLE_FILTER
export VPSADMINOS_ENABLE_LIVEPATCH_TEST=1
VPSADMINOS_LIVEPATCH_CORRECTED_MODULE=$(nix-build tests/fixtures/livepatch -A corrected --no-out-link)
export VPSADMINOS_LIVEPATCH_CORRECTED_MODULE
module=$(readlink -e "$VPSADMINOS_LIVEPATCH_CORRECTED_MODULE")
VPSADMINOS_LIVEPATCH_CORRECTED_SHA256=$(sha256sum "$module" | cut -d' ' -f1)
export VPSADMINOS_LIVEPATCH_CORRECTED_SHA256
VPSADMINOS_LIVEPATCH_CORRECTED_SITES=$(nix-build tests/fixtures/livepatch -A candidateSites --no-out-link)
export VPSADMINOS_LIVEPATCH_CORRECTED_SITES
site_sha=$(nix eval --impure --raw --expr "let s = builtins.fromJSON (builtins.readFile $VPSADMINOS_LIVEPATCH_CORRECTED_SITES/sites.json); in assert s.schema_version == 1; s.module_sha256")
test "$site_sha" = "$VPSADMINOS_LIVEPATCH_CORRECTED_SHA256"
VPSADMINOS_LIVEPATCH_RELEASED_V5_MODULE=$(nix-build tests/fixtures/livepatch -A releasedV5 --no-out-link)
export VPSADMINOS_LIVEPATCH_RELEASED_V5_MODULE
VPSADMINOS_LIVEPATCH_PREDECESSOR_MODULE=$(nix-build tests/fixtures/livepatch -A shippedV6 --no-out-link)
export VPSADMINOS_LIVEPATCH_PREDECESSOR_MODULE
producer=$(nix eval --impure --raw --expr 'toString (import ./tests/fixtures/livepatch {}).candidateProducer')
test "$module" = "$producer/lib/modules/6.12.95/extra/livepatch_7.ko"
printf 'Source: %s\nInputs: %s\nProducer: %s\nModule: %s\nSHA256: %s\nSites: %s\n' \
  "$(git rev-parse HEAD)" "$(sha256sum flake.lock | cut -d' ' -f1)" \
  "$producer" "$module" "$VPSADMINOS_LIVEPATCH_CORRECTED_SHA256" \
  "$VPSADMINOS_LIVEPATCH_CORRECTED_SITES" > "$runtime_root/identity.txt"
cp "$VPSADMINOS_LIVEPATCH_CORRECTED_SITES/sites.json" "$runtime_root/sites.json"

VPSADMINOS_LIVEPATCH_EXAMPLE_FILTER='transitions exact FUSE splice and resend states safely' \
  ./test-runner.sh test --test-config tests/test-configs/ci.nix \
  --state-dir "$runtime_root/fuse" --fresh --jobs 1 --stop-on-failure \
  --prebuild --tag livepatch-amd -- kernel/livepatch-6.12.95 \
  2>&1 | tee "$runtime_root/fuse.log"

VPSADMINOS_LIVEPATCH_EXAMPLE_FILTER='hardens a legacy TCP sysctl table and wrapped socket' \
  ./test-runner.sh test --test-config tests/test-configs/ci.nix \
  --state-dir "$runtime_root/tcp" --fresh --jobs 1 --stop-on-failure \
  --prebuild --tag livepatch-amd -- kernel/livepatch-6.12.95 \
  2>&1 | tee "$runtime_root/tcp.log"
```

Each invocation is its own fresh monitored operation with the captured identity
environment, not a fresh checksum expectation. Preserve `pipefail` and actual
exit status. Verify the named example actually executed and passed; zero
executed examples or a name mismatch cannot count. Keep the wrapper's packaged
native runner; the spec-only development-shell `RUBYLIB` repair is unnecessary
for this established `./test-runner.sh` route.

## Required result evidence and next selectors

- FUSE must resolve the original callee, hold only the intended return PC,
  retain nonzero copy-state and the original `fuse_copy_page` stack frame, have
  zero missed probes, complete the old-to-current transition and current abort/
  close/resend cases, and leave no kernel fault. The selected call's validated
  successful unlock path is the existing `FR_LOCKED` semantic boundary; there
  is no additional live flag-field reader. Report that distinction accurately.
- TCP must log the one intended sender socket/PID and actual comparison
  observations with `reordering=4294967295`, positive MSS, completed needed
  value above UINT_MAX, nonzero rows, no ring overrun and no missed probes.
  Require receiver EOF/exit 0, exactly 8388608 bytes and full expected-payload
  comparison, alongside sender success. Delivery alone cannot replace the
  arithmetic sample.

Use the same main command/environment with a new case-specific state directory
and the exact existing filter below, serially:

| Purpose | Exact example filter |
| --- | --- |
| SVM post-fentry repair | `repairs legacy and future nested-SVM x2APIC bitmaps` |
| NFT post-fentry hold | `holds complete NFtables batches across activation and removal` |
| SUNRPC entry/claim/release | `gives a SUNRPC removal callback sole ownership before worker claim` |
| SUNRPC allocation | `fails SUNRPC TLS shadow allocation closed and reaches no-agent TLS` |

For fragment ordering, keep the same captured identity, **unset** the example
filter and run the identical runner options against
`kernel/livepatch-inet-frag` in `$runtime_root/inet-frag`. Require native
unhashed/unlocked and current linked/locked timer observations with zero misses.
Before the full main/qualification/matrix run, keep the example filter unset;
all existing predecessor/vendor/profile coverage remains required.

## Duration, cache and stopping conditions

Planning estimates, not measured VM durations: warm-cache FUSE 5–10 minutes,
TCP 2–5 minutes, fragment 2–5 minutes; the remaining focused cases several
minutes each. Initial package/image preparation is separate. The measured B
all-nine metadata pass alone took about nine minutes; reuse the same captured
site store output rather than regenerate it per case. No deadline is extended
and no test profile is reduced: keep explicit 20/30/60-second waits, the
runner's ordinary 900-second command default and native cleanup limits.

Known cold-cache risks are the ordinary producer's builtin-ZFS plain-kernel
`dev` edge, archive-restored boot outputs whose recipe retains old Nix/tool
dependencies, the packaged runner, new helper/image closures and resolver
Python packages. Raw scratch SDK/JSON evidence is not a replacement for a
successful declared Nix image closure. A helper compile is expected; an
unexpected Linux kernel build is a stop-and-diagnose condition. Do not solve
it by rebuilding the frozen boot kernel, pin changes or source edits here.

Stop on identity/schema/ABI mismatch, zero selected cases, wrong host CPU
precondition, failed hold/unwind/probe/data assertion, kernel warning/fault,
lost trace events or unsafe/uncertain native cleanup. Preserve the first
failure and do not dispatch the full matrix until it is reconciled. If a
resource wait or preparation exceeds its expected phase, report the exact
blocked stage and reassess; silence alone does not authorize killing a run.

## Logs and ownership

The exact native main-test directory is
`$runtime_root/{case}/os-test-kernel__livepatch-6.12.95-9f465251/`.
Keep `test-runner.log`, `machine-console.log`, `machine-shell.log` and
`config.json`, plus the top-level case log and identity/sites record. Retain
failed trace diagnostics and original command status; the guest's transient
`/run/livepatch-*` files disappear with its normal teardown.

The fresh watcher owns its exact launcher/handle and logs; the parent owns
cancellation decisions and diagnosis. Runner/evaluator native `ensure` cleanup
owns guest stop/kill, destructive default disk removal and machine cleanup;
keep default destructive behavior and use a fresh state directory. Do not
kill guessed QEMU/Nix PIDs, alter another run's locks, force a failed livepatch
transition, or start a retry while command effects are uncertain. Reconcile
owned processes/guest state and terminal status before releasing verification
ownership or scheduling the next operation. Session lifecycle is unchanged.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>
