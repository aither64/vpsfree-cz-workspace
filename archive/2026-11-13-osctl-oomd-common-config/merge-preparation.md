# Package M: original oomd move refreshed for review and integration

Owner: `implementer0`; preparation complete 2026-11-23. Lead reports explicit
user approval, "merge this", after disclosure of the missing-initrd-key build
limitation. This package performs no merge, default push, claim or deployment.
Fresh applicable independent review remains required because the target's
runtime pins changed substantively since [the original review](review.md).

## Exact history and publication

Repository: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`.
Branch: `2026-11-13-osctl-oomd-common-config`.
Feature worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-osctl-oomd-common-config/vpsfree-cz-configuration`.

| Range | Base | Head |
| --- | --- | --- |
| Original reviewed | `08d68a85f24a95b70b2d806f995f04b236e4d89a` | `48e94d18b467d1a3999fb906f0fd726968146267` |
| Refreshed | `baf73377af387a8ef1c90e20b17bb559fcd15c45` | `4fa3c97b83f2b9368b2d4bdb9f7b9630afcdd278` |

Fresh fetch proved original head unmerged. Rebase applied without source
conflicts or patch changes. Complete new series: one commit,
`4fa3c97b cluster: share osctl-oomd tuning across nodes`.
`git range-diff OLD_BASE..OLD_HEAD NEW_BASE..NEW_HEAD` reports
`1: 48e94d18 = 1: 4fa3c97b`; both `git patch-id --stable` results are
`a394a3dbb5ea2fbfc7c3ff54d4c7500611230940`.
No migrations, deployed feature lineage, transitional code, superseded source
approaches or repeated update streams. No input update belongs to this series.

Published over SSH with the exact lease
`--force-with-lease=refs/heads/2026-11-13-osctl-oomd-common-config:48e94d18b467d1a3999fb906f0fd726968146267`.
Fresh `git ls-remote --heads` confirms feature head `4fa3c97b…` and master
`baf73377…`, exactly the full revisions above. Feature worktree is clean.
Only schedule/manual daily-update workflow exists; no push CI to supersede.
`dev-session worktree capture-comparison` saved the explicit refreshed base/head.

## Checks and prepared target

Passed in current `nix develop --no-write-lock-file` shell: RFC
`nixfmt --check` on both changed files, `nix-instantiate --parse` on each,
`git diff --check NEW_BASE..HEAD`, `bundle exec overcommit --diff NEW_BASE`
(Nixfmt), and installed `commit-msg` hook on the final message (all three
checks pass). All 13 existing import routes and channel assignments remain
unchanged; the same consumers listed in [implementation.md](implementation.md)
reach the common module. Enable/verbose stay true; only one common definition
of each tuning remains.

Rebase initially paused because current master's Gemfile.lock required newer
parser gems. Old native `.gems` then failed Ruby ABI loading. Preserved it at
`worktrees/2026-11-13-osctl-oomd-common-config/vpsfree-cz-configuration-gems-before-m-20261123`;
ordinary current-shell initialization supplied a fresh locked bundle. Reran
installed checkout hook and normal rebase; no hook bypass. The rescheduled pick
required restoring only the two owned uncommitted paths to target before replay.
See [local bundle note](../../notes/vpsfree-cz-configuration/2026-11-23-local-gems-ruby-refresh.md).

Clean detached integration target, at exact `baf73377af387a8ef1c90e20b17bb559fcd15c45`:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-osctl-oomd-common-config/vpsfree-cz-configuration-integration-m`.
Its own pinned bundle passes `bundle check`; Ruby 3.4.12, Overcommit 0.76.0,
nixfmt 1.5.0. Normal hooks installed/signed; executable pre-commit, post-merge
and pre-push hooks verified. Creation's checkout hook passed. Hook-ready command
prefix from that directory: `nix develop --no-write-lock-file -c git`.
Lead retains fresh target check, required ownership, merge/default push and proof.

Required full node build remains limited by the previously disclosed external
`/secrets/nodes/initrd/ssh_host_ed25519_key` gap. It was not retried. No secrets,
dry activation or runtime/deployment checks were accessed or performed.

## Actual target inputs and bounded runtime compatibility evidence

Both flake files are byte-identical to refreshed base (empty input diff).
`flake.nix` SHA-256 remains `fd49c6a1506e5241e93f817060736f63d8930554f5bc499462468d9de5fe1e71`;
complete `flake.lock` graph SHA-256 is now
`eb87a4eab405729a89108042b9e5b264eba603175312decda6b2f0e971de3abc`.
This baseline already selects confctl `d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49`,
production OS `ccd51ed38ebffa2e744f7f8847668bc2e3413378`, and staging OS
`e9d55bada43c888ae91139d549d156a0831817de`, replacing the original common OS
`c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62`. This package changes none of them.

At both actual OS revisions, `os/modules/osctl/osctl-oomd.nix` and
`osctl-oomd/lib/osctl/oomd/cli.rb` are respectively identical blobs
`d66b31a4cd51b0637803628c778c6dc80a614f84` and
`a797ba515a24f8212026ac77e4f628f2188e7891`: settings remain JSON freeform,
passed via `--config`; CLI preserves explicit restart_hits and merges both
numeric values. Production watcher lines 47–58 still compare host load with
rolling median times load_multiplier; its default watchdog-disabled path uses
Killer with ordinary restart_hits. Staging watcher forwards both values into
Controller; controller lines 43–53, 83–84 and 353–357 preserve ordinary hit count
and median multiplier while using guarded sampling/scoring. RTNL episode hit
count is a separate nested setting. Current configuration has no nested
rtnl_watchdog override; pre-existing standalone watchdog enablement is untouched.

Relevant upstream context: production adds RTNL/controller support; staging
additionally changes guarded readings/scoring and replaces the old killer path.
These are substantial pre-existing baseline changes, not a mechanical review
reuse claim. Reviewer should inspect the actual pinned interfaces/meaning;
no broad upstream audit was undertaken. No coordinated rollout is introduced
by this configuration-only move; deployment remains excluded.

## Complete refreshed diff

```diff
diff --git a/cluster/cz.vpsfree/nodes/common/all.nix b/cluster/cz.vpsfree/nodes/common/all.nix
index 23326afa..3fd39017 100644
--- a/cluster/cz.vpsfree/nodes/common/all.nix
+++ b/cluster/cz.vpsfree/nodes/common/all.nix
@@ -177,6 +177,8 @@ in
     enable = true;
     settings = {
       verbose = true;
+      restart_hits = 4;
+      load_multiplier = 1.5;
     };
   };
 
diff --git a/cluster/cz.vpsfree/nodes/prg/node25/config.nix b/cluster/cz.vpsfree/nodes/prg/node25/config.nix
index be2dfc3b..9f7c710f 100644
--- a/cluster/cz.vpsfree/nodes/prg/node25/config.nix
+++ b/cluster/cz.vpsfree/nodes/prg/node25/config.nix
@@ -107,11 +107,6 @@
     };
   };
 
-  osctl.oomd.settings = {
-    restart_hits = 4;
-    load_multiplier = 1.5;
-  };
-
   osctl.pools.tank = {
     parallelStart = 10;
     parallelStop = 20;
```

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-osctl-oomd-common-config/)
