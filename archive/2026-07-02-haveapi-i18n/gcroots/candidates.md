# Nix GC root cleanup candidates

Source scan:

```sh
nix-store --gc --print-roots
```

Raw output:

- `work/2026-07-02-haveapi-i18n/gcroots/print-roots.txt`
- `work/2026-07-02-haveapi-i18n/gcroots/print-roots.stderr`

Disk context at scan time:

- `/nix/store`: 742G used, 192G available, 80% full.
- `.dev-clusters`: 61G on the host filesystem. This is mostly VM state, not
  Nix store closure size, but old cluster resets can reclaim it.

## Low-risk Nix GC roots

These are stopped vpsAdmin devcluster config roots. Removing the symlink does
not delete VM state or cluster config; it only allows Nix GC to collect build
closures that are no longer otherwise rooted. Rebuilds recreate the link.

The new `devcluster gcroots --cleanup` command removes these roots while
keeping running cluster roots.

```sh
dev-clusters/vpsadmin/bin/devcluster gcroots --cleanup \
  2026-05-29-security-advisories \
  2026-06-06-vpsadmin-user-timezone \
  2026-06-13-vps-replace-backups \
  2026-06-14-vpsadmin-incident-filtering \
  2026-06-15-vpsadmin-events
```

Candidates:

- `.dev-clusters/vpsadmin/clusters/2026-05-29-security-advisories/result-config`
  -> `/nix/store/dg89bhgsbk5lm4iqds9p0aycj14dxvxl-os-test-vpsadmin-devcluster-2026-05-29-security-advisories.json`
  closure size: 13.6 GiB.
- `.dev-clusters/vpsadmin/clusters/2026-06-06-vpsadmin-user-timezone/result-config`
  -> `/nix/store/5lal3h89qriqv3jyrbqmyby1sxf28ad1-os-test-vpsadmin-devcluster-2026-06-06-vpsadmin-user-timezone.json`
  closure size: 14.0 GiB.
- `.dev-clusters/vpsadmin/clusters/2026-06-13-vps-replace-backups/result-config`
  -> `/nix/store/ga5mjs5ak7mv22gmpba9z09f50klp631-os-test-vpsadmin-devcluster-2026-06-13-vps-replace-backups.json`
  closure size: 14.3 GiB.
- `.dev-clusters/vpsadmin/clusters/2026-06-14-vpsadmin-incident-filtering/result-config`
  -> `/nix/store/1m9kdk8axvy5z9za59s6av6bv947vd4m-os-test-vpsadmin-devcluster-2026-06-14-vpsadmin-incident-filtering.json`
  closure size: 13.9 GiB. The cluster status is stopped with a stale `ready`
  marker.
- `.dev-clusters/vpsadmin/clusters/2026-06-15-vpsadmin-events/result-config`
  -> `/nix/store/9r2bkr5hyfnnxmxrgilvgdvmwlplxym2-os-test-vpsadmin-devcluster-2026-06-15-vpsadmin-events.json`
  closure size: 13.8 GiB.

Keep for now:

- `.dev-clusters/vpsadmin/clusters/2026-07-02-haveapi-i18n/result-config`
  -> `/nix/store/05p0dhs0vp0r91hmi8jxmawkwzi77z4j-os-test-vpsadmin-devcluster-2026-07-02-haveapi-i18n.json`
  closure size: 13.9 GiB. This cluster is running with PID 449455.

Also low-risk if these old build outputs are not being inspected:

```sh
rm -f \
  result \
  worktrees/2026-05-30-dev-vpsadmin-clusters/vpsadminos/result/test-runner \
  worktrees/2026-06-10-vpsadminos-nftables-bug/vpsadminos/result/test-runner
```

- `result` -> `/nix/store/x9plcv7jpddjb0ffjqdyhfia7nx1d5mj-vpsadmin-devcluster-runner`,
  closure size: 106.9 MiB.
- `worktrees/2026-05-30-dev-vpsadmin-clusters/vpsadminos/result/test-runner`
  -> `/nix/store/6s1hv2shq0kbs1477k058sly11f631qr-test-runner`,
  closure size: 96.6 MiB.
- `worktrees/2026-06-10-vpsadminos-nftables-bug/vpsadminos/result/test-runner`
  -> `/nix/store/dy4izzag9365y139ksz866vrricaw8r3-test-runner`,
  closure size: 101.7 MiB.

## Safe if no old test is running

There are 126 `/tmp` roots from old test-runner, confctl, and nix-shell
directories. Their mtimes are from May and June 2026. A process scan for common
test-runner/confctl/nix-shell patterns found no matching live job except the
currently running devcluster and the scan command itself.

These are good cleanup candidates after a final check that no local tests are
running:

```sh
rm -rf \
  /tmp/confctl-option-guard-deploy-flakes \
  /tmp/confctl-option-guard-deploy-flakes2 \
  /tmp/confctl-option-guard-deploy-flakes3 \
  /tmp/confctl-test-runner-deploy-flakes-split \
  /tmp/nix-shell.* \
  /tmp/os-test-runner* \
  /tmp/tmp.Lfnix4frTo \
  /tmp/tmp.uQyrAh7UlB \
  /tmp/vpsadmin-devcluster-bridge-helper-check \
  /tmp/vpsadmin-devcluster-config-check \
  /tmp/vpsadmin-test-runner-ruby-gems* \
  /tmp/vpsadminos-image-test-json* \
  /tmp/vpsadminos-local-repro-* \
  /tmp/vpsadminos-test-runner-*
```

## Safe only after confirming rollback artifacts are obsolete

The scan found 366 confctl generation roots inside old feature worktrees in
this coordination workspace:

- 37 roots under
  `worktrees/2026-05-30-dev-vpsadmin-clusters/vpsfree-cz-configuration/.confctl/generations`.
- 329 roots under
  `worktrees/2026-06-15-vpsadmin-events/vpsfree-cz-configuration/.confctl/generations`.

These can pin large system closures. They are removable once those feature
deployment generations are not needed for local inspection or rollback.

The scan also found confctl/result roots outside this workspace under:

- `/home/aither/workspace/confctl`
- `/home/aither/workspace/nixos/havefun-cz-configuration`
- `/home/aither/workspace/nixos/vpsadminos-org-configuration`
- `/home/aither/workspace/nixos/zima-engineering-configuration`
- `/home/aither/workspace/vpsadmin`
- `/home/aither/workspace/vpsf-dev`
- `/home/aither/workspace/vpsfree.cz/vpsfree-cz-configuration`

Do not bulk-remove those from this initiative unless the corresponding
worktrees/deploy generations are known to be obsolete.

## Do not remove manually

- Live process roots (`/proc/...`): 1932 entries at scan time.
- System profiles under `/nix/var/nix/profiles`.
- Current Home Manager root:
  `/home/aither/.local/state/home-manager/gcroots/current-home`.
- User profile generations under `/home/aither/.local/state/nix/profiles`;
  use normal Nix profile history cleanup instead of deleting links by hand.
