# I1: build.vpsfree.cz container image builder

Read-only investigation on 2026-11-04 by `implementer1`, scoped to the build host
and its referenced builder modules/scripts. No application edits, builds, tests,
CI, live-host access, fetches, pushes, branches, worktrees or commits were made.
Only this assigned evidence file was written. Source behavior below is not proof
of the currently activated production configuration.

## Source identity and evidence limits

All references were read from canonical bare repositories with explicit SHAs.
The short labels below scope every `path:line` reference in this document.

| Label | Repository and exact revision | Selection |
| --- | --- | --- |
| C | `repos/vpsfree-cz-configuration.git`, `f4069909b55fbed907cb658f350ec6a59f97e05a` | Local `refs/remotes/origin/master` at investigation time; no network refresh |
| V | `repos/vpsadminos.git`, `dd188397abe37d0bc33f4c5dfb3605206ce5e326` | C's `vpsadminosOsStaging` lock entry |
| V-current | `repos/vpsadminos.git`, `2951a632c4254a44747a8da326e3dde897eaa0e2` | Local `refs/remotes/origin/staging`; no network refresh |

C's local `refs/heads/master` was `86e19685313270d88e4db30038c056ce4b807abd`;
its build-host directory has no diff against C. V and V-current have no diff in
the two traced builder module directories. No claim is made that either local
remote-tracking ref is the current remote head. Deployment/input pin freshness
needs a separate authorized remote/live check.

Repository guidance read: C/V `AGENTS.md` and `README.md`; V
`docs/specifications/image-repository.md`; workspace AGENTS, sessions,
documentation, projects, verification, git, and team procedures. This is
investigation/evidence, not a completed implementation requiring change review.

## Source selection and schedule

- C `cluster/cz.vpsfree/machines/build/module.nix:3` identifies the NixOS VM
  `build.vpsfree.cz`, target `172.16.106.5`; lines 6–9 select `nixos-stable` and
  `os-staging`. C `flake.nix:114` maps `os-staging.vpsadminos` to
  `vpsadminosOsStaging`; C `flake.lock:1109` / `flake.lock:1126` pin V. The input
  uses `nixpkgsStable` and `nixpkgsUnstable` through follows (C `flake.nix:45`).
- C `cluster/cz.vpsfree/machines/build/config.nix:15` imports V's
  `os/modules/services/misc/build-vpsadminos-container-image-repository/nixos.nix`.
  Its service instance `vpsadminos` is enabled at C host config line 106, and its
  timer at line 134. There is no per-run source fetch in this path.
- V `os/modules/services/misc/build-vpsadminos-container-image-repository/options.nix:116`
  defaults build scripts to the same source tree's `image-scripts`; lines 10–13
  and 124–130 expose a filtered V source tree for NixOS builds. Thus host
  configuration activation selects the module, scripts and default source.
- V `os/modules/services/misc/build-vpsadminos-container-image-repository/nixos.nix:21`
  defaults the timer to **Saturday 04:00:00**. C `environments/base.nix:48` sets
  **Europe/Amsterdam**. V `.../shared.nix:148` configures only `OnCalendar` and
  `timers.target`; it does not explicitly enable persistent catch-up, jitter,
  restart or retries. The separate VM-side cron defaults disabled (V
  `os/modules/services/osctl/image-repository/default.nix:93`).
- V `.../shared.nix:134` defines the root-default systemd oneshot
  `build-vpsadminos-container-image-repository-vpsadminos.service`, with
  `TimeoutStartSec = "24h"`. The installed manual command is
  `build-vpsadminos-repository-vpsadminos` (lines 118–131, 159). It forwards
  arguments to the VM command; the systemd schedule passes none.

## Execution and persistent paths

The host wrapper makes the shared directories, launches `osvm script`, records
its status, runs the site's post-run commands, then returns the saved status
(V `.../shared.nix:118`). The generated Ruby script boots `builder-vpsadminos`,
mounts virtiofs shares, waits for pool `tank` and network, invokes
`build-image-repository-vpsadminos` with a 24-hour command timeout, then stops the
VM; its ensure block kills/finalizes/cleans VM runtime resources
(V `.../shared.nix:65`). These are existing builder operations, not session
lifecycle operations executed during this investigation.

| Host path / resource | Guest path / purpose | Evidence |
| --- | --- | --- |
| `/var/lib/vpsadminos-container-image-repository/vpsadminos/cache` | `/mnt/cacheDir`, generated image outputs | V `.../options.nix:133`, `.../options.nix:258` |
| `/var/lib/vpsadminos-container-image-repository/vpsadminos/log` | `/mnt/logDir`, per-image failure logs | V `.../options.nix:141` |
| `/var/lib/vpsadminos-container-image-repository/vpsadminos/repository` | `/mnt/repoDir`, repository mutated as each image succeeds | V `.../options.nix:149`, `.../shared.nix:29` |
| V `image-scripts` / filtered V source | `/mnt/buildScripts` / `/mnt/vpsadminos` | V `.../options.nix:116`, `.../shared.nix:29` |
| `/var/lib/build-vpsadminos-repository/vpsadminos` | VM state, runtime sockets/logs, `sda.img` | V `.../shared.nix:63`, `.../shared.nix:73` |
| `sda.img`, 60G, created if absent | pool `tank`, dataset `tank/image-repository/build-dataset` | C host config `:118`; V `.../options.nix:245` |

Here `.../options.nix`, `.../shared.nix` and `.../nixos.nix` mean V's
`os/modules/services/misc/build-vpsadminos-container-image-repository/` prefix.

C config allocates 24,576 MiB, 16 CPUs/cores (host config `:118`). V
`osvm/lib/osvm/machine_config.rb:53` defaults disks to preserve existing contents;
`osvm/lib/osvm/machine.rb:1094` reuses a preserved disk, and `:1133` resolves its
relative path under the state directory. Runtime cleanup (`:428`) removes
sockets, not this disk. The user-mode guest network defaults to
`10.0.2.0/24` with `tcp::2222-:22` forwarding (V `.../options.nix:93`).

Guest image selection/tags/GC come from V `os/configs/image-repository.nix`;
`rebuildAll = true` at line 9. Vendor is `vpsadminos`, default variant `minimal`
(lines 11–14); image entries mostly request no explicit variant list. Inner
builder emits `osctl-image --build-scripts /mnt/buildScripts --vpsadminos-dir
/mnt/vpsadminos deploy --build-dataset tank/image-repository/build-dataset
--output-dir /mnt/cacheDir --rebuild [--tag ...] IMAGE /mnt/repoDir` sequentially
(V `os/modules/services/osctl/image-repository/build.rb:130`). CLI supports named
image selection, rebuild/keep-failed overrides and explicit skip-tests; the
scheduled invocation does not skip tests (`build.rb:95`).

V `osctl-image/lib/osctl/image/cli/image.rb:90` selects successful builds, tests
them, and deploys only verified builds (unless skip-tests requested). V
`osctl-image/lib/osctl/image/operations/image/deploy.rb:24` adds available `tar`
and `zfs` outputs (`output_tar`, `output_stream`, compacting missing formats).
The host rsync does not select formats or variants: it copies the whole tree.
Source-gem overlay binds osvm/osctl-image/osctl-repo/libosctl to V sources, rather
than relying only on gem version strings (V `os/overlays/osctl.nix:8`, `:73`,
`:99`; `os/packages/ruby-source-gem-config.nix:30`).

## Publication, credentials and concurrency

C `cluster/cz.vpsfree/machines/build/config.nix:131` runs:

```sh
rsync -av --delete -e /nix/store/...-openssh.../bin/ssh \
  /var/lib/vpsadminos-container-image-repository/vpsadminos/repository/ \
  images.int.vpsadminos.org:/srv/images/
```

The actual executable paths are Nix package references in source, not the
illustrative store path above. The service declares no `User`, rsync no remote
username or identity, and no host-key flags. It therefore uses root/default SSH
configuration unless host-specific SSH configuration overrides the destination
user. Identity selection, private-key provisioning and known-hosts contents are
not established by these source files. No live key files were read. The
`confData.sshKeys.build-vpsfree-cz` entry at C host config `:112` authorizes root
**into the guest VM**; it does not identify the outbound publishing credential.
The source grants root access on the build host to configured admins/builders
through C `environments/base.nix:104`. Destination authorization is I2's scope.

This is direct synchronization with deletion into the served tree: no candidate
directory, integrity receipt, repository-wide atomic swap, publication lock,
revision eligibility test or separate promotion command appears in the path.
The trailing source slash copies contents; archive mode preserves symlinks.

No whole-build lock appears in the wrapper/inner build, nor a writer lock in V
`osctl-repo/lib/osctl/repo/local/{repository,index}.rb`. Systemd prevents a second
instance through the same unit, but manual CLI invocation bypasses that scope.
Fixed VM name, disk/state paths, shares and port forwarding make concurrent
manual runs unsafe. The per-object Ruby mutexes in osvm are process-local.
Downloader `Filelock` calls in `osctl-repo/.../remote/` protect client caches,
not publication. This is source inspection, not a concurrent-run experiment.

Local repository updates copy files into their final paths, modify tag symlinks,
then save the index (V `osctl-repo/lib/osctl/repo/local/repository.rb:24`). Index
save atomically renames one replacement file (V `.../local/index.rb:70` and
`libosctl/lib/libosctl/utils/file.rb:5`), but the image tree is not one atomic
generation. Concurrent writers can overwrite an index loaded before their peer's
changes. Rsync's per-file replacement likewise is not a repository transaction.

## Failure semantics and observability

1. **Aggregate build status is misleading.** V inner `build.rb:176` records each
   `osctl-image` status, but failure only appends diagnostics and warnings and
   continues (`:180`, `:198`). `Builder.run` has no aggregate failure exit
   (`:71`, `:279`). Individual failures can leave a successful outer command.
   Initialization/default-repository subprocess statuses are not checked either
   (`:122`, `:207`, `:264`). Ruby exceptions still fail the process.
2. **Publication follows failure.** V wrapper `.../shared.nix:127` saves osvm's
   status, always runs `postRunCommands` after osvm returns, then returns only
   the saved status. Thus successful subsets/old entries can publish after a
   failed run, and **rsync failure after a successful build is masked**. A hard
   systemd timeout may kill the wrapper before this post-run step.
3. **GC and guest post-build errors only warn**, V inner `build.rb:217` / `:227`.
   GC's individual `local rm` return values are also ignored
   (`os/modules/services/osctl/image-repository/gc.rb:47`).
4. **Successful image logs are deleted**, inner `build.rb:198`. Failed deploy
   logs have timestamp/random names and include `/var/log/osctld` and dmesg
   (`:170`, `:180`). No log/cache rotation is declared in traced builder files.
   OSVM console and other logs use fixed state-directory names (e.g.
   `osvm/lib/osvm/machine.rb:197`, `:1022`), so they are not per-run receipts.
5. **Monitoring sees the outer unit.** C
   `modules/clusterconf/monitor/rules/systemd.nix:44` alerts on failed units and
   `:84` alerts when this builder remains activating for 18 hours (generic
   five-minute alert excludes it). C `modules/system/monitoring.nix:129` enables
   the systemd collector for NixOS VMs. Masked image/transfer failures do not
   trigger these unit-state checks. No last-success/publication-age metric was
   found in this traced path. C host metadata `:64` health-checks nginx/atftpd,
   not image output. Cron mailto at host config `:91` does not itself notify
   for this systemd timer.

## Retention and migration constraints

- V `os/configs/image-repository.nix:251` keeps four matching dated rolling
  versions per configured distribution/variant; it is not a universal four-run
  retention policy. Fixed-version outputs are replaced at their existing paths.
  Cache/log/disk retention is separate and not bounded here. C
  `tools/gc-build-machine.sh:5` rotates confctl system/netboot generations and
  Nix garbage, not container image cache/log/publication generations. C build
  metadata `:50` / `:56` limits carrier generations, also a different namespace.
- Preserve repository schema **v1**, relative image locations, tags and default
  vendor/variant symlinks for mixed old/new clients (V
  `osctl-repo/lib/osctl/repo/version.rb:4`, local `repository.rb:10`,
  `docs/specifications/image-repository.md:1`). Preserve both generated formats
  when present. No database or schema migration is proposed by this report.
- An isolated candidate can use the existing `repositoryDirectory` option and
  same guest `/mnt/repoDir` interface; this is an available seam, not an existing
  promotion implementation. Starting each candidate empty changes current
  semantics: old images survive failed builds today, and rolling GC depends on
  prior contents. Decide whether to seed/snapshot the last-good tree or require
  complete successful regeneration before promotion.
- Keep the old writer disabled/serialized at cutover; a new importer/publisher
  must not race the old direct `rsync --delete`. Retain a known-good served tree
  for rollback. Verify filesystem and destination rename/symlink behavior before
  claiming atomic promotion; no live filesystem evidence was collected.
- Replacing weekly deployed-source selection with checked-out CI source changes
  the trust boundary. Untrusted PR/branch builds must not inherit live publisher
  credentials or mutate persistent shared builder state. OS/kernel/ZFS changes
  can affect the persistent VM disk; do not assume rollback can import state
  created by an upgraded pool. No all-node coordinated update is indicated by a
  builder-only scheduling/publication change.

## Reuse and prioritized suggestions

The smallest useful improvements are: propagate aggregate image and rsync
failures; record source SHA and per-image/build/test/publication outcomes; retain
bounded successful logs; add one build/publication ownership boundary; and
stage/validate before replacing the served tree. Keep these as proposals pending
the lead's synthesis, not implementation authorization.

Existing reuse seams:

- Reuse the builder's `osvmPackage`, build scripts, source, cache/log/repository
  options rather than inventing another VM/image builder.
- V `.github/workflows/image-scripts.yml:7` already accepts dispatch and changed
  image push/PR triggers, uses self-hosted runners (`:33`, `:103`), builds an OS
  closure, detects changed images (`:66`), then runs
  `./test-runner.sh test --state-dir ... -f --jobs auto image-scripts/test@{...}`
  (`:112`). Its existing result evaluation, summaries and failure log upload
  actions provide reporting seams (`:133`). It does not publish container
  repositories; its SSH secret is for the binary cache (`:49`).
- `.github/actions/prepare-test-state/prepare-test-state.bash:23` isolates
  workflow state by repository/run/attempt. That convention is useful for
  candidates, unlike current singleton production paths. Runner provisioning,
  actual capacity and repository/credential isolation were not verified here.
- V `tests/suite/osctl/image-repository-build-service.nix:177` provides fake osvm,
  image/repo package seams and checks forwarding of source/dataset/path/defaults
  (`:262`). `tests/nixos-container-image-repository-eval.nix:1` evaluates the
  NixOS module/package interface. These are existing tests inspected only; no
  tests were run and no coverage of aggregate failure/publication atomicity is
  asserted.

Next dependency: architect/lead combine this builder trace with I2's destination
trace and other runner/client evidence. Actual publisher identity/known-hosts,
active service revision, recent outcomes, target filesystem layout and runner
capacity remain operational unknowns requiring separate authorization/scope.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-container-image-build-pipeline/>
