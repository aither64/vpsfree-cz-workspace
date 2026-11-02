# aitherdev service-cleanup rollout

Status: preparation only; no machine claim or activation yet.

## Authorization and boundaries

User: "proceed with implementation. aitherdev can be deployed using
vpsfree-cz-configuration." Implement accepted registered-service cleanup and
Resources/Team interface. Existing unregistered services remain excluded.
No default-branch integration or session archive/delete/stop is authorized.
No reboot. Application stays in the workspace user profile; configuration owns
matching host/module runtime and system generation.

## Repository and machine identities

- dev-workspace: git@github.com:aither64/dev-workspace.git, target master.
- workspace: git@github.com:aither64/vpsfree-cz-workspace.git, target master.
- configuration: git@github.com:vpsfreecz/vpsfree-cz-configuration.git, target master.
- Feature branch in all three: 2026-11-02-session-temporary-service-cleanup.
- Physical machine: aitherdev; configuration name cz.vpsfree/machines/aitherdev;
  reservation alias vpsfree:aitherdev. System and app profile share this machine.

## Baseline observations

- Selected package: /nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0.
- Package derivation: /nix/store/2jvhgyq2ilxa4cprlswc7fwh93b3snpx-dev-workspace-0.2.0.drv.
- Its exact src: /nix/store/pw7ffd5bsg55wvcbqwc3vs91h9f1894i-source.
- Active Codex pointer: /home/aither/.local/state/dev-workspaces/codex/current/bin/codex.
- Live system and system profile both resolve to:
  /nix/store/4wpwzqrb3c51bbibwzqavjlc6qjcpiv0-nixos-system-aitherdev-26.05.20261026.718f670.
- Feature workspace baseline 6383e8848c92c06a9d817f8109853b5b61305c89 and config
  baseline c040c14cdbacc07998700b524996a89306188d7f select the same generic runtime:
  c2182254d29c4175c3e9fe4267e5a92dd1da6b79,
  narHash sha256-k6d90hicmnStL/tT6AeBLbYBQ5U7O/pmUls1zGYwsMg=.
- Workspace extension retained at e4e7e95ed39bf514b33f8f8ae61ba9868de060ae,
  narHash sha256-5tnBT6j5LzwkYTffhWQ7mWpDkWMisxbCpFpbtDOjBlc=.

These observations identify the predecessor, not a prepared successor or successful
deployment. Recheck selected generation/claims before activation.

## Required preparation and evidence

- Complete functional source and docs, meaningful quick checks, cleaned complete
  branch series/migration inventory and independent final review.
- Publish exact runtime feature head; use confctl's dev-workspace/devWorkspace
  channel for the config pin and preserve workspace's direct nested override.
- Record exact final/deployed heads, complete input graphs through committed
  flake.lock identities/checksums, effective runtime/extension and source store paths.
- Run bin/check-dev-workspace-deployment against final workspace/config locks.
- Long lifecycle/host/package verification uses fresh pinned watcher, after review.
- Build/copy final committed configuration and application outside machine ownership.
  Retain output paths, derivations, complete source/input graph and recovery roots.

## Activation and verification (not executed)

Acquire only vpsfree:aitherdev near first activation, inspect exact authoritative
claim status, dry-activate then switch prepared system without reboot. Preserve
confctl rollback/generation evidence; prove both live-system and profile paths.
Then ordinary workspace-host switch --source FEATURE_WORKSPACE with held machine
claim and exact verified session identity. Keep existing forward-recovery contract.
Verify selected package/input graph, portal/router/coordinator health, Codex/tmux
continuity and Resources/Team UI. Lifecycle behavior only on disposable installed-
package fixture state; never archive a real session or inspect/stop example units.

## Release and integration

Current selected-runtime guide/thread instructions override older configuration
wording about release without integration or waiting for UI acceptance. Release
this session's exact machine claim promptly only after verified deployment/effects,
settled commands and complete deployed lineage integrated into explicitly approved
remote defaults. Verify status before release and resulting state afterwards.
No separate release/UI permission is needed once conditions hold. A later deployment
needs fresh ownership. Until integration approval/evidence exists, retain the held
machine if deployed. Repository integration uses separate short per-repository claims;
release those before checks/records. Do not mark nonancestor deployed commits literally
merged; retain any reviewed equivalence evidence and migration provenance.

Releasing claims never authorizes session lifecycle operations. Leave session open.
