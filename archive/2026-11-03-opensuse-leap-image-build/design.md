# openSUSE Leap 16.1 and shared Leap builder

Current design, revised 2026-11-03 by architect0 after the user's clarification:
“i meant that you should replace the leap-15.5 builder with 16.0”. This supersedes
the dedicated-builder interpretation. Lead accepts and assigns implementation;
architect edits this brief only. No merge or production deployment is authorized.

## Scope, interfaces and implementation boundaries

One implementer owns the narrow vpsadminos package, targeting `staging`.
The image repository configuration belongs to this repository; no site
configuration, dependency pin, shared helper or new abstraction is needed.

| Files | Required final behavior |
| --- | --- |
| `image-scripts/builders/opensuse-leap/config.sh` | Change `RELVER=leap-15.5` to `RELVER=leap-16.0`; preserve `DISTNAME=opensuse` and existing no-op `setup.sh`. |
| `image-scripts/images/opensuse-leap-16.1/{build,config}.sh` | Follow 16.0, with `BUILDER=opensuse-leap`, `SPIN=leap`, `SPINVER=16.1`, `RELVER=$SPIN-$SPINVER`, `ARCH=x86_64`. |
| `os/configs/image-repository.nix` | Keep explicit 15.6/16.0 entries and Tumbleweed; move the unique openSUSE `latest`/`stable` tags to 16.1. |
| `tests/distributions.nix` | Keep explicit `opensuse_leap_16_1` (`opensuse`, `leap-16.1`) in `cgroupAll` and `systemd`, plus existing `latest` coverage. Classification remains subject to actual runtime checks. |

Remove the session-added `image-scripts/builders/opensuse-leap-16.0/{config,setup}.sh`
from the final source/history. Milestone 1 scope is five changed/added files
relative to the original base. Leave the existing device-unit exception
unchanged; the user's separate request for its actual cause and fix is
Milestone 2, governed by [device-unit-design.md](device-unit-design.md).

The actual existing shared-builder consumers are **opensuse-leap-15.6 and
opensuse-leap-16.0**; 16.1 becomes the third. All three have current repository
registrations. Retained public images for older Leap versions have no current
build-script consumers here and do not justify a historical regression matrix.
This is the repository's supported build scope, not an upstream lifecycle claim.

Use two coherent final commits: (1) upgrade the shared builder, independently
improving the existing 15.6/16.0 build environments; (2) add 16.1 scripts,
registration/tag migration and explicit test metadata. Commit 2 depends on
commit 1's modern bootstrap environment. Fold obsolete dedicated-builder
history into this final series under normal Git/review policy; preserve old
tested heads and receipts as historical evidence, not final validation.

## Compatibility, operation and recovery

Target identity remains `opensuse/leap-16.1/x86_64/vpsadminos/minimal`; the
builder's release controls build tooling, while each image's SPINVER selects
its target packages. Existing 15.6 and 16.0 build environments intentionally
move to 16.0. Existing containers, images already published, database/API
contracts, protocols and image formats do not change; no coordinated fleet
upgrade is required. Preserve existing bootstrap sequence, package list,
network/SSH setup, RPM database handling and service adaptations.

Use explicit builder `leap-16.0`, not `latest`/`stable` (which move to 16.1).
The published stable image was verified in the
[repository index](https://images.vpsadminos.org/v1/INDEX.json). The
[official 16.1 package repository](https://download.opensuse.org/distribution/leap/16.1/repo/oss/)
contains the helper's explicit packages, including systemd 257.13; bootstrap
success and cgroup behavior require runtime evidence.

**Builder reuse hazard:** `osctl-image/lib/osctl/image/builder.rb` derives
`builder-<SHA256(name)[0..7]>` only from the name. `UseOrCreate` starts an existing
ID without comparing release metadata. Changing RELVER does not refresh an
already retained Leap 15.5 builder. Tests must use a new session-owned state
directory/fresh disks, not the original failed primary state. Record actual
builder `/etc/os-release`, RPM version and available downloaded-image identity.

For a later authorized rollout, publish/deploy the scripts before scheduling
the new build and recreate the idle, positively identified managed
`opensuse-leap` builder with existing `osctl-image ct ls` / `ct del <exact-id>`
operations. Do not delete unrelated builders or change live containers.
Rollback similarly requires the matching recreated builder; reverting the
config alone can leave a 16.0 container cached. Restoring old default tags
changes future image selection, not containers already created. No automatic
builder-migration logic is part of this change.

## Evidence and remaining uncertainty

Original 15.5-builder run at `fe9182dd2fb1ba627c30d54c39c1acd7b140df69` reached
package installation but reported missing Lua exec/execute APIs and fatal
libgio unpack ENOENT; their causal chain was not proven. The dedicated 16.0
revision `aa963dce42859ae4251cdfaded91920d67b3a46e` subsequently passed all 15
image tests without those errors; extraction identified builder Leap 16.0 /
RPM 4.20.1. See [primary result](image-test-leap16-builder-result.md) and
[extraction result](candidate-extract-recovery-result.md). These support the
toolchain choice but do not replace final shared-builder regression.

The same old candidate passed focused start-stop; four focused cases were not
run. Preserved shell evidence (`aa963dce4-device-units-shell.log`, lines 253–417)
shows repeated eth0.device exit 3, loaded but inactive (dead), then polling
timeout. Dummy0 steps were not reached. See [matrix result](candidate-matrix-result.md).
The earlier proposal to extend expectedFailure is withdrawn following the
user's request for an actual openSUSE fix. Similarity to an existing exception
does not establish cause. Milestone 2 owns diagnosis and a real fix; preserve
this failure evidence and do not count it as acceptance.

## Acceptance and shortest verification path

1. Verify exactly three intended shared-builder consumers, no dedicated-builder
   references, unique tags and the expected image metadata. Run `bash -n` on
   changed scripts, native image/builder config parsing, `git diff --check`,
   repository hooks and focused test discovery in the repository Nix environment.
2. Commit both logical changes, obtain affected independent review and explicit
   whole-series/no-migrations conclusions before the long regression run.
3. Through a fresh utility watcher, run the normal image tests for all three
   affected releases in fresh state. A session-only 8 GiB module may use the
   already established `VPSADMINOS_CONFIG` interface: import a separate module
   recording the exact final revision and set only
   `boot.qemu.memory = lib.mkForce 8192`. Preserve the historical AA revision
   and export modules; do not relabel their results. No source test changes.

```sh
env VPSADMINOS_CONFIG=<absolute-session-8GiB-module> ./test-runner.sh test \
  --jobs 2 --stop-on-failure --no-destructive \
  --state-dir /tmp/2026-11-03-opensuse-leap-image-build-shared-leap \
  'image-scripts/test@opensuse-leap-{15.6,16.0,16.1}'
```

This is one native pattern and one aggregate batch. At most two VMs require
16 GiB RAM/shared memory and 8 vCPUs, plus runner/host reserves; verify headroom
before launch and lower jobs to 1 if needed. The prior 24 GiB run/export exposed
host memory pressure; an 8 GiB export succeeded. This justifies trying the
bounded sizing override, not claiming a full image build already passed at
8 GiB. If genuine guest OOM appears, stop and adjust sizing from evidence;
do not change test semantics. Retain final 16.1 output for focused checks.

Each release must complete its package transaction and normal image suite.
Inspect logs for Lua/scriptlet/unpack errors even on exit 0. Stop unexpected
local kernel builds to investigate substitution; diagnose failures before
retrying. Fresh VMs establish new builder creation, so do not reuse the
original state's cached `opensuse-leap` container. Record final source, config
and builder identity, command/results and native logs.

4. Coordinate with Milestone 2 for the actual device-unit fix and finish the six candidate-backed checks
   in [candidate-checks.md](candidate-checks.md): start-stop, systemd-rundir,
   netif-routed, cgroup mounts v1/v2 and device units. Use the final 16.1 artifact
   and existing explicit per-VM URL preparation; do not revive the rejected
   URL-only native-batch optimization. The baseline has no repositories-tank
   setter: DB default creation precedes pool-active and manual URL writes are
   persisted across test VM restarts. Preserve the service-absence and URL
   readback assertions, hashes and exact-script result evidence.

No new product prose is needed for the conventional release/builder change.
Lead updates tracking and assigns source changes/verification; implementer
owns application edits and failure diagnosis. This brief is not deployment
or integration approval.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-opensuse-leap-image-build/
