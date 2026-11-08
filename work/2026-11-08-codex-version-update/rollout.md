# Codex 0.167.0 rollout

Status: preparation only. No activation, machine ownership or integration yet.
User request authorizes aitherdev deployment using vpsfree-cz-configuration;
no default-branch integration approval has been given.

## Original selection (2026-11-08)

- System and system profile: /nix/store/kycb055vxzjn9jzz4yyfwbgf673z6q8s-nixos-system-aitherdev-26.05.20261026.718f670
- System command: codex-cli 0.165.0.
- Workspace profile: /nix/store/9yibngx0gbiq17waqffcgszk067ngmhb-dev-workspace-0.2.0
- Profile command: /nix/store/9yibngx0gbiq17waqffcgszk067ngmhb-dev-workspace-0.2.0/libexec/codex/bin/codex
- Active command: /home/aither/.local/state/dev-workspaces/codex/current/bin/codex
- Configured target: vpsfree-cz-configuration / cz.vpsfree/machines/aitherdev / confctl.
- Canonical configuration: git@github.com:vpsfreecz/vpsfree-cz-configuration.git, target master.
- Machine identifier: machine:github.com/vpsfreecz/vpsfree-cz-configuration:cz.vpsfree/machines/aitherdev.
- Legacy physical-machine alias: vpsfree:aitherdev (preserve installed bridge).

## Preparation and recovery requirements

Record exact final source/input graphs, system/profile store paths and tested
binary hashes here before activation. Finish quick checks, commits, independent
review and required longer checks first. Prepare builds/copies before machine
claim; lead owns activation coordination. System precedes dependent profile.
Respect native idle-session refusal without interrupting other sessions.
Preserve operation journals, conversations, retained generations and native
roots. Application recovery proceeds forward through original switch attempt.
Reconcile uncertain system effects before further mutation.

Deployment verification must include native daemon identity separately from CLI,
strict-config DeepSeek request, naming, browser/terminal service health and saved
thread continuity. Before release inspect exact owned claim status, reconcile
command effects and prove complete deployed lineage integrated into approved
remote defaults, then release and verify state. Deployment does not grant merge
or lifecycle authorization. No session cleanup is authorized.

## Prepared configuration command plan (not executed)

From configuration worktree, in its Nix environment, after review:

1. `confctl build --yes cz.vpsfree/machines/aitherdev`.
2. Retain returned generation GEN, toplevel, auto_rollback and input identities.
3. `confctl deploy --yes --generation GEN --copy-only cz.vpsfree/machines/aitherdev` outside machine ownership.
4. Acquire and verify exact configured machine claim near activation.
5. `confctl deploy --yes --generation GEN --dry-activate-first --no-reboot cz.vpsfree/machines/aitherdev switch`.
6. Verify live/profile identities and effects before dependent workspace switch.

Pinned confctl help/source inspected by implementer2. Do not disable automatic
rollback, replay uncertain activation, or infer permission for reboot. Preserve
prepared generation and its metadata for original recovery.

## Frozen candidate identity (retrieved, not deployed)

- llm-agents d960982d3b05c294f3cf98cab3e23798548a0ced.
- Output /nix/store/22139ip2k5dfc272a1nv0br2ms0nymbv-codex-0.167.0.
- Derivation /nix/store/9rxjqb3nzbf4b9s0bj3h4yl8igm105is-codex-0.167.0.drv.
- Native output/libexec/codex/bin/codex SHA256 13fc360e1eb73eeabeda7e2d9c6294aa56a0b062adc54a681b9d687a2e905b10; isolated version 0.167.0.
- Upstream source /nix/store/j9bhifsiqjhxknbzmx46884jnr1lffrc-source/codex-rs.
- Source catalog 539696B, SHA256 1384625c0b6b3e67d3c60da29becea2b017f2c283fc1e2d05b8edafb4698eb10.
- Config schema SHA256 66ed795352d32f2464778acd2e332b7fafe644246d540cdceec4663c56cfbc16.
- Fresh installed-policy Luna/low utility retrieved exact source/output from
  cache.numtide.com; exit 0 in 7.84s, no running effects. Runtime owner retains
  launch/log evidence and reconstructed patched-source graph.

mkCodexPackage remains necessary: realized upstream resource rg/bwrap links escape
the runtime root. Catalog equality does not establish native behavior.


## Selected-package native switch constraint

Architect inspected selected9yib command/maintenance sources and installed guide.
There is no supported idle-only/noninterrupting switch flag: native changes route
to maintenance schema2/policy2 regardless of --enable-maintenance. Flags are
--source/--from-candidate/--enable-maintenance/positive --pause-timeout; no flag
can guarantee no deadline interrupts. Current active lead is a participant too.

Accepted update skill/design forbids interrupting other sessions. Therefore final
profile activation must run from an external operator shell after a deliberately
coordinated natural-idle window across all workspaces sharing the user profile,
including lead/members/watchers/native children and pending work. New work must
not enter before ordinary command capture/hold. Preserve ordinary guarded checks;
no private lifecycle/maintenance helper or catalog change is authorized.

Exact supported command, after review/build/copy and held/verified machine claim:

```sh
DEV_SESSION_SLUG=2026-11-08-codex-version-update \
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
DEV_WORKSPACE_CLAIM_ID=EXACT_HELD_CLAIM \
workspace-host switch --source EXACT_PREPARED_WORKSPACE_SOURCE
```

This is not safe to launch inline from the active lead turn under no-interruption
constraint. A large timeout is not an enforcement mode. Existing system/profile
recovery and exact claim requirements remain. Prepare concrete exact outputs and
review before any required operator handoff; no system activation yet.
