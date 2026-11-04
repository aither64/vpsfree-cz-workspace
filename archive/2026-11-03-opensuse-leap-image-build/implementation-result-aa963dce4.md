# Implementer0 result

Implementation and quick checks are complete; feature branch is published.
The primary image test passed at the stable-builder final head: all 15 guest
tests succeeded. Candidate extraction completed; the lead's matrix watcher owns
all six focused checks and loopback server. Their results remain pending;
no production image publication or default-branch integration.

The first export-only debug boot stalled before a guest shell; the candidate
was not started. Watcher native exit is reconciled and the disk is retained.
See [bounded diagnosis/recovery](export-lockup-diagnosis.md): exact cause is
unknown. The single separate 8 GiB export recovery completed successfully and
closed natively; it does not prove a kernel/KVM fix. Primary passed
configuration/evidence and project source remain unchanged.

## Scope and source

- Repository: `vpsadminos`, target `origin/staging`.
- Branch: `2026-11-03-opensuse-leap-image-build`.
- Worktree: `worktrees/2026-11-03-opensuse-leap-image-build/vpsadminos`.
- Fetched initial base: `dd188397abe37d0bc33f4c5dfb3605206ce5e326`.
- Final base: `dd188397abe37d0bc33f4c5dfb3605206ce5e326`.
- Final head: `aa963dce42859ae4251cdfaded91920d67b3a46e`.
- Final tree: `d4a264295678a50eac25732074dc942e637850e4`.
- Full series: one commit, `image-scripts: add opensuse-leap-16.1`.
- Fresh fetch before publication: target unchanged. Published via SSH in the
  repository Nix environment with explicit force-with-lease against `fe9182dd2`.
  Remote `git ls-remote` verified the exact final head. Worktree clean; no PR,
  default-branch merge or deployment.
- Six files, 25 insertions and 1 deletion. New build script is identical to
  16.0 (blob `334b1935f5c3e4590586038fbebd5b3e42befa41`); image config changes
  `SPINVER=16.1` and points to the dedicated `opensuse-leap-16.0` builder.
  The new builder has `DISTNAME=opensuse`, explicit `RELVER=leap-16.0`, no-op
  setup `:`, and matching 100644 modes.
- Image repository retains Leap 15.6, 16.0 and Tumbleweed; 16.1 uniquely owns
  openSUSE latest/stable. Explicit 16.1 distro entry joins cgroupAll/systemd.
- No shared-helper, existing-builder, older-image, lockfile, pin, migration,
  API/protocol or persistent host state changes. No coordinated node upgrade.
- No dependency/channel update streams or superseded feature commits. Upstream
  changes since the architect's inspected base are preserved without edits.

## Quick evidence

- `bash -n` on both new image files and both new builder files: passed.
- `nix-instantiate --parse` on both changed Nix files: passed.
- `git diff --check`: passed.
- Native config parser resolves builder `opensuse/leap-16.0` and target image
  `opensuse/leap-16.1`, x86_64. Existing builders/helper/16.0 image diff is empty.
- Worktree registration succeeded despite the post-checkout Overcommit signature
  refusal. The reviewed configuration was signed by the lead's fresh watcher;
  see [hook setup result](hook-setup-result.md). No duplicate worktree add.
- Active installed Overcommit pre-commit/commit-msg hooks verified. Full
  `nix develop --command overcommit --run` passed both Nixfmt and RuboCop, exit 0.
  Broad repository Ruby checking exceeded the expected quick duration; original
  process stayed with implementer until it completed, with no duplicate.
- Commit used a temporary message file and active hooks: pre-commit Nixfmt passed;
  final stable-builder commit-msg hooks all passed without warnings. Earlier
  full Ruby/Nix lint evidence applies to unchanged Ruby/Nix source and config.
- Ambient push was refused locally by the config-signature check; running push
  in the same repository Nix environment as signing/commit passed. No hook bypass
  or source/signature changes were needed.
- Three lead-watched discovery commands passed, exit 0; raw
  [discovery log](test-discovery.log) confirms the image test, three distro cases
  and both cgroup cases. Its initial summary incorrectly reported no cgroup
  cases; lines 19/20 list `cgroups/mount-v1#opensuse-leap-16.1` and
  `cgroups/mount-v2#opensuse-leap-16.1`. Lead notified to reconcile the summary.

No project documentation update is useful for this conventional version
addition. The accepted [design](design.md) records compatibility and rollout
constraints; this file holds temporary execution evidence.

## Review advisory: message-only amendment

The original reviewed range is
`dd188397abe37d0bc33f4c5dfb3605206ce5e326..f0e1656cd840cdd2c5180340241f798614fe23d1`.
The new range is
`dd188397abe37d0bc33f4c5dfb3605206ce5e326..fe9182dd2fb1ba627c30d54c39c1acd7b140df69`.
Only commit-message validation prose and line wrapping changed, as directed
by the lead. Original review report/range remain intact; backup ref
`refs/backup/2026-11-03-opensuse-leap-image-build/reviewed-f0e1656` retains the
old head.

Both heads have tree `05b7f416e90b321f7d9c81a21198ed8d5b1625a5` and stable
patch ID `dc1ebce3445cca71f54e16c869dd4af154d42501`. `git diff old new` is
empty; `git range-diff` shows only the message changes. No migrations or update
streams; no source changes or new runtime verification claims.

Active Nixfmt/pre-commit and commit-msg hooks passed for the amendment. Fresh
fetch confirmed staging unchanged. Push used the repository Nix environment and
explicit `--force-with-lease` against the old exact feature head; remote
`ls-remote` confirms new head `fe9182dd2fb1ba627c30d54c39c1acd7b140df69`.
Lead owns refreshed comparison capture. Only old-head branch runs `41685417848`
and `41685417717` were cancelled; GitHub confirms both completed/cancelled.
No current-head run was cancelled.

## Stable Leap 16.0 builder revision

The user requested Leap 16.0 as the builder; the lead accepted architect0's
updated [design](design.md). Tumbleweed was never applied. The substantive new
range is
`dd188397abe37d0bc33f4c5dfb3605206ce5e326..aa963dce42859ae4251cdfaded91920d67b3a46e`,
replacing the reviewed/failed same-base `..fe9182dd2fb1ba627c30d54c39c1acd7b140df69`
range. `git range-diff` shows exactly the two conventional builder files, one
image-local builder reference, and matching commit-message rationale.
Incremental diff: three paths, 4 insertions and 1 deletion. New stable patch ID
`085f1f9ab37f75dd48e6df9566b9029afc99fc5d` differs from the earlier
`dc1ebce3445cca71f54e16c869dd4af154d42501`; this is a substantive revision
requiring real affected-lane review, not an equivalence claim.

Backup ref
`refs/backup/2026-11-03-opensuse-leap-image-build/failed-leap-builder-fe9182d`
retains the failed/reviewed head; the original `reviewed-f0e1656` ref and review
report remain intact. Earlier source was only published and used in a disposable
test; no candidate image was completed, no production deployment/migrations or
externally consumed update stream exists. The single logical final commit
contains the fix without superseded intermediate source commits.

Preserved original failure: [native log copy](failed-leap-15.5-test-runner.log),
132714 bytes, SHA256
`1dae03c64a78ccd895a53a06de0d39feee657a349c05506f4a867e716e3ae929`.
The old-builder debug attempt ended incomplete at Pry because non-TTY stdin
closed; it produced no package/Lua probes and has no active effects.
No further old-builder inspection is needed. The fresh stable-builder retest
passed; glibc, systemd and libgio install normally, bootstrap returns 0, and all
15 guest tests pass. Complete successful runner/shell/console output contains
no Lua nil exec/execute, scriptlet failure, libgio unpack/cpio failure or skipped
posttrans signatures. Nonfatal ACL Operation-not-supported warnings remain.

Preserved successful native copies before extraction/debug can replace them:

- `successful-leap-16.0-test-runner.log`, 41074 bytes, SHA256
  `13af14d632a2ed7b3d672998e6ad08abe939f98ff55a70d9309a3c7e82e8a175`.
- `successful-leap-16.0-machine-shell.log`, 124262 bytes, SHA256
  `5f17909f9446d4ea90a628ceb5c7bee0a9b0fa84b5c18430db20993d0c58a059`.
- `successful-leap-16.0-machine-console.log`, 4686 bytes, SHA256
  `03b3d74e035a7bbc93009ccbeb913425170ea15cb259ea4670f09928e2ce385c`.

See [primary result](image-test-leap16-builder-result.md) for command/elapsed
evidence. Builder identity and archive hashes are recorded in the completed
[extraction receipt](candidate-extract-recovery-result.md), produced using the
unchanged fixed [Ruby input](candidate-extraction-aa963dce4.rb).

`test-revision.nix` now names the exact final head. After affected-lane review,
the lead's fresh watcher ran the existing primary command:

```sh
env VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/test-revision.nix ./test-runner.sh test --no-destructive --state-dir /tmp/2026-11-03-opensuse-leap-image-build-image image-scripts/test@opensuse-leap-16.1
```

Current-head CI runs `41690940390` (CI) and `41690940549` (images) are untouched.
Only superseded `fe9182dd2` runs `41686911774` and `41686911788` were cancelled;
GitHub confirms both completed/cancelled. The implementer did not launch the
primary test, debug, focused checks or server; the lead retains watcher ownership.

## CI scope and image-publication dependency

Read-only run metadata confirmed earlier `fe9182dd2` push events:
`41686911774` uses `.github/workflows/ci.yml` (`CI (ci)`), and `41686911788`
uses `.github/workflows/image-scripts.yml`. No CI status polling or new runs
were performed for this inspection.

On this branch, general CI defaults to suite `ci`, tag `ci`, empty test pattern,
`--jobs auto`, `--prebuild`, and `--test-config tests/test-configs/ci.nix`.
No unstable configuration is selected. That test config only changes
Docker/Podman registries, not container-image repositories. The OS build/cache
job precedes its native suite; prebuild prepares VM/test closures, not new
distribution images.

The explicit Leap 16.1 matrix addition schedules these six `ci` scripts through
the existing all/cgroupAll/systemd groups: `dist-config/netif-routed`,
`dist-config/start-stop`, `dist-config/systemd-rundir`, `cgroups/mount-v1`,
`cgroups/mount-v2`, and `systemd/device-units`, each with
`#opensuse-leap-16.1`. Each creates a container with `osctl ct new` from the
default repository (`https://images.vpsadminos.org`, defined in
`osctld/lib/osctld/db/repositories.rb`). There is no candidate import or
public-image availability guard in these scripts.

The separate changed-image workflow orders OS build/cache, changed-image
detection, then `image-scripts/test@{detected-images}`. Its detector falls back
to merge-base after a force-push, so the source diff selects
`opensuse-leap-16.1`. The image test builds its candidate directly, without a
`ci` tag filter. It does not publish that candidate, and there is no dependency
ordering the general CI workflow after image publication.

Therefore the native `ci` suite can schedule explicit 16.1 fetches before a
public 16.1 image is available; those cases cannot pass that prerequisite until
the image is served. Local disposable-candidate checks prove candidate behavior
independently, but do not make the stock public-repository CI suite ready.
Any later authorized rollout must publish the tested explicit image before
requiring these matrix cases to pass (and before treating new latest/stable
tags as usable). No image publication, workflow/source change or production
availability probe was performed here; this records the source-defined ordering
dependency, not a live repository-availability claim.

## Existing candidate reuse mechanism

The configured primary run reached the actual package bootstrap and failed.
In its native `test-runner.log`, line 1444 shows glibc's Lua script calling
missing global `exec`; lines 2156–2167 show systemd triggers calling missing
`rpm.execute`. The fatal transaction error at lines 2179–2184 is libgio
`2.84.4-160100.3.1` failing to unpack
`/var/cache/gio-2.0/gnome-mimeapps.list` (ENOENT), after successful download.
Zypper aborted and returned 8, correctly propagated by the shared helper.
This is a package transaction/compatibility failure, not evidence of a missing
upstream package or failed network transfer. Its libgio causal chain remains
unproved. The old `leap-15.5` builder's direct RPM identity/API inspection
ended incomplete; its [prepared batch](bootstrap-builder-inspection.md) remains
historical evidence, not an instruction to retry.
RPM upstream documents `rpm.execute` as added in
[RPM 4.15](https://rpm.org/wiki/Releases/4.15.0).
The accepted stable-builder revision above addresses the observed API
incompatibility; no path workaround, skipped scriptlet or blind rerun was added.

The primary test stores candidate files inside the VM at
`/tank/image-scripts/output/opensuse-leap-16.1-x86_64-vpsadminos-minimal-archive.tar`
and the corresponding `-stream.tar`. Run it with `--no-destructive` and an owned
`--state-dir` to preserve its data disk. Existing `test-runner debug` reopens that
test/state tuple, and `machine.pull_file` returns a host path to an extracted
candidate. Record its SHA256 with the candidate commit when available.

Existing `osctl-repo local init`, `local add --archive`, and `local default`
construct a disposable repository; serve it over HTTP and redirect the focused
test VM's default repository URL. Sources: `docs/container-images/repositories.md`,
`tests/suite/osctl/ct-image-fetch.nix`, `osvm/lib/osvm/machine.rb:726`, and the
test-runner man page's debug/disk sections. Repository export/pull completed
successfully; focused candidate consumption is owned by the active matrix watcher.

Completed export identity at source `aa963dce42859ae4251cdfaded91920d67b3a46e`:

- Builder `d5ddc633`: openSUSE Leap 16.0, RPM 4.20.1. Existing cached stream
  SHA256 `d279c082fb997e17996af6fe00f8b54d23a847247c2498090a24b3f26538dbe2`.
- Built candidate archive SHA256
  `254523b59106db1d27bcf98e43e942c8ea1d7f0c15238542ca17e21612017214`.
- Exported repository tar: `/tmp/2026-11-03-opensuse-leap-image-build-candidate-repo.tar`,
  169820160 bytes, SHA256
  `36069c59b286fdeb81988e87482b519bb8fcea62a916e0a1d0eaac819e0c57d3`.
- Export native JSON `/nix/store/8vnrdmp1xjdj4jnl21ynjvzahamsd9l5-os-test-image-scripts-test-opensuse-leap-16.1.json`,
  8192 MiB/4 CPUs, SHA256
  `a13371204163888ce6725a904b213ceda6cbf8c16c0f568c4eb3e4fb7aad2a77`.
- Same retained disk: 10737418240 bytes, device 64769, inode 33618419. Export
  runner exited 0 at 20:14:38 +0100; no watchdog message in this recovery.

These are completed extraction results only; the six focused scripts remain
pending. No cause for the previous guest boot lockup has been established.

The stock focused tests create containers with `osctl ct new` from their default
repository. `--test-config` has no generic candidate import or pre-test hook;
its existing consumers configure Docker/Podman. Do not run stock focused tests
against the public repository and claim candidate coverage. Exact bounded debug
follow-up instructions are in [candidate checks](candidate-checks.md); no generic
infrastructure or production publication is proposed.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-opensuse-leap-image-build/
