# Proxy baseline correction review

## Requested outcome and scope

The user identified the production proxy dependency override as erroneous and
explicitly selected removal of all overrides: nixpkgs, vpsAdminOS and vpsAdmin.
They also requested removal of the unmerged commit `vpsadmin-config: expose
password recovery on auth proxy`. Implement the approved plan in the retained
initiative `2026-08-18-vpsadmin-password-reset`.

This review covers the correction below and its effects on the existing
configuration series, including eventual shared-proxy deployment compatibility.
The already-reviewed API implementation, KB previews and template content are
unchanged. Do not repeat their complete security reviews. No production deploy,
branch integration, runtime upgrade, cluster operation, session lifecycle action
or new worktree is authorized by this correction. Leave owned environments up.

## Revisions and commits

Workspace: `/home/aither/workspace/ai/vpsfree.cz`.
Plan/state: `work/2026-08-18-vpsadmin-password-reset/{plan,state}.md`.
Configuration worktree:
`worktrees/2026-08-18-vpsadmin-password-reset/vpsfree-cz-configuration`.
All feature branches: `2026-08-18-vpsadmin-password-reset`.

- Original published config head: bb49f262d263760c26a87b73ad9abae1e28cf9fe.
- Fetched current config default: 8ef765d339ac792ef4f01a5c7a160e48600adcaf.
- Rebased pre-correction baseline: a4c43133ee98057e79a3355ecb5d4bad814b4957.
- Review/final candidate config head: 0e0a985ad5daa12ab5ad50fec5ac4cf55b204358.
- Unchanged API head: 050ea5263812a76dc39f14c5b58a0e88714d634d.
- Unchanged notification templates: f944ba03eba5d0d6b58b7eb856f251d1c96f2c11.
- Unchanged KB contracts: baf1f97e5784b76cc15755b6eeb7fc227b91b023.

Inspect a4c43133..0e0a985a for the correction tree; inspect
8ef765d3..0e0a985a for the retained commit series. The default-branch rebase
preserved all five original feature patches exactly (rebase-range-diff.txt).
The route workaround b13a7a8d (rebased d7792d1a) is dropped, rather than reverted.
Merged July baseline-introduction history is preserved. The new cleanup commit
0e0a985a removes baseline declarations/overrides, generated unreachable lock
nodes and documents that exact proxy dependency update/rollback. These changes
are bundled because they describe and implement one machine-channel correction.
Generated API/template pin messages remain unchanged. Original published head
is retained at refs/backup/password-reset-proxy-20260913. No force push yet.

## Ownership and compatibility

The proxy keeps its configured channels nixos-stable, os-staging and vpsadmin,
now resolving to nixpkgsStable 21a67dc4, vpsadminosOsStaging c065fa2f and
vpsadminServices 050ea526. Full hashes are in input-validation.json.
Removing all overrides was an explicit user choice; retaining only the platform
baselines is a rejected alternative. All other retained input graphs are
identical. Removed four root inputs and nine unreachable lock nodes.

The proxy is NixOS, not a VPS node. Its normal channel restoration changes
shared proxy packages/modules at eventual deployment, not cluster node protocol
or schema. The release guide now requires generation-diff review, retention of
the previous generation, and verification of other sites on proxy rollback.
Production deployment remains separate and recovery remains disabled until its
existing rollout checks pass. No runtime rollout or rollback has been executed.

Canonical auth routing/maintenance owner:
`vpsadmin/nixos/modules/vpsadmin/frontend.nix` at API 050ea526, consumed through
vpsadminServices and imported by confctl machine composition. Both production
and admin auth virtual hosts are declared in the shared frontend configuration;
the local copy of the password-recovery route and maintenance expression is
removed. The shared frontend file now equals config origin/master exactly.

## Quick validation complete

- `nixfmt --check` on both changed Nix files; `git diff --check`: pass.
- Active commit hooks: pass (manual commit message body has 72-column warnings,
  within repository's explicit 80-column rule).
- Strict MkDocs build using pinned nixpkgs tools: pass.
- Actual full proxy toplevel derivation evaluation: pass; derivation path in
  private `/tmp/password-reset-proxy-20260913.22Fs24/proxy-drv`.
- `nix eval --json .#confctl.inputsInfo` before/after: all 108 machine mappings
  compared; only proxy's three role mappings change.
- Recursive resolution of every retained root lock input, including follows:
  identical dependency graph/revisions before and after pruning.
- Isolated evaluation of the exact pinned frontend module with actual pinned
  nixpkgs: 18 checks for /_auth, /webauthn and /oauth2/password-reset across two
  auth hosts under normal, selected global production maintenance and local
  instance maintenance. Expected proxy target/503 behavior all pass;
  auth-routes.json records values. Final generated Nginx inspection follows build.
- Initial comparison script assumed human machine names; corrected it to use
  the exported confctl.machineKeys mapping. This was a probe error, not a config
  failure. Ambient rebase hook lacked its gems; pinned Nix dev shell passed.

No application tests were added or repeated for this deletion/configuration
correction. The proxy build and closure-package diff follow completed review;
no local kernel build is expected for this NixOS container.

## Required review lanes

Overall risk: high because the shared production proxy advances frozen
packages/modules and exposes authentication routes. General, architecture,
scope and risk lanes all apply. Use gpt-5.6-sol with xhigh reasoning, perform
review directly, and do not spawn subagents. Inspect relevant repository
AGENTS.md and the matching mandatory-change-review reference. Report concrete
Blocking/Important/Advisory findings, or explicitly no findings and residual
validation limits. Each reviewer writes only its assigned review artifact.
