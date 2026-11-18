# Package B2: vpsadminos.org confctl adoption

Owner: implementer1. Complete; ready for lead acceptance. Capacity confirmed
after B completion/acceptance. Session
identity/current and both environment values match the trusted binding; live
roster confirms retained Sol/xhigh, workspace-write and full execution access.

## Preparation and scope

- Repository: `git@github.com:vpsfreecz/vpsadminos-org-configuration.git`.
- Branch: retained `2026-11-18-nixos-channel-update`.
- Worktree: `worktrees/2026-11-18-nixos-channel-update/vpsadminos-org-configuration`.
- Fresh fetched default and new package base:
  `72c18d811086dac8e16ec8c7ee6bf8e32ce62123`.
- Prior B head equals fetched `origin/master`; ancestor proof passed. Environment
  scoped `git merge --ff-only origin/master` reported already up to date; no
  merged history was rewritten.
- No repository-local AGENTS/README/docs are present. Workspace routes and skills
  already read remain unchanged. Read current flake and hook configuration.
- Root input `confctl` tracks `github:vpsfreecz/confctl`, currently locked to
  `ff5e017780a35fb97b549db2a51b570193867c3b`. Neither defined channel owns it.
- Exact required new source: `d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49`, freshly
  equal to upstream `refs/heads/master` via SSH `git ls-remote`.
- `nix develop` environment works; Overcommit installed and signed with ordinary
  `bundle exec overcommit --install`, `--sign`, `--sign pre-commit`.

D6 sufficient brief and lead release received; generated update committed. The
project diff is generated `flake.lock` only. Preserve nginx one-time revision
`4077fb98f09d5bd847f848ae4f214a4c5b9f0a9d`, complete original `nixos-26.05`
tracking attributes, root mapping/follows and unrelated input identities. No
manual lock edits, workflows, deployments or fleet evaluation are assigned.

## Verification and delivery

Generated command completed: `nix develop -c confctl inputs update --commit confctl`.
No manual lock edits. New final adoption head:
`fadb89a3f828bc98ea75aa5fcd8de953390c15e2`.
Complete new base→head series: one commit,
`fadb89a3f828bc98ea75aa5fcd8de953390c15e2 inputs: update confctl to d8ab7d4c`.
Generated changelog retained verbatim, including the source commit summary
`d8ab7d4 inputs: skip behind revisions during guarded updates`.
Earlier merged B history remains unchanged; no migration, obsolete adoption,
follow-up pin stream or superseded attempt exists in this new range.

Quick checks passed:

- Only `flake.lock`, three insertions/three deletions. No Nix/workflow source edit.
- Python equality assertions on committed base/head: only selected root node
  `confctl` differs; only `locked.rev`, `locked.lastModified`, `locked.narHash`
  differ. Full original object, nested inputs, root mappings, all follows and
  every other node match exactly. `flake.nix` and workflows byte-identical.
- Exact new confctl source `d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49`, timestamp
  `1795026729`, narHash `sha256-078svbFUIAjS3aZMN4XCkRwUAz0dJf/QtGqZwJxmUxM=`.
  Old source `ff5e017780a35fb97b549db2a51b570193867c3b`, timestamp `1794591356`,
  narHash `sha256-Y7vwZfDEpElVUxEyDdpwHC8/1IapvkMz3/0AFr7U+yw=`.
- Confctl original remains `{owner=vpsfreecz, repo=confctl, type=github}`;
  nested nixpkgs follows `[confctl, vpsadminos, nixpkgs]`, nested vpsadminos edge
  remains `vpsadminos`. Full nested source identities unchanged.
- Entire root `nixpkgs` node (`nixpkgs_3`) remains equal, including exact
  `4077fb98f09d5bd847f848ae4f214a4c5b9f0a9d`, timestamp `1795018498`, narHash
  `sha256-zX+62p0XLF5AbMgzy8JgNBH6cTJSiDovTOSk2NBc0GQ=`, and complete original
  tracking `nixos-26.05`.
- `git diff --check <base>..HEAD` passed; clean worktree/index after commit.
- Required Overcommit Nixfmt/commit-msg hooks passed. TextWidth emitted only a
  nonblocking generated-changelog warning; generated message preserved per
  procedure. No hooks bypassed.

Read-only new-shell smoke runs under fresh installed Luna/low utility; source
path resolved by `nix eval` is `/nix/store/zh2jpdp1hcllnb761v1n61z2yykdkamq-source`.
The fresh utility completed the sole smoke invocation successfully (exit 0) in
22.095 seconds, tested revision `fadb89a3f828bc98ea75aa5fcd8de953390c15e2`.
Exact invocation: `nix develop -c bash /tmp/nixos-channel-update-b2-smoke.sh`.
The script asserted `CONFCTL_SRC` equals the expected source path, printed the
selected executable, ran `confctl inputs ls --json confctl`,
`confctl inputs channel ls`, and `nix eval --offline --json .#confctl.machineNames`.
Log: `/tmp/nixos-channel-update-package-b2-smoke.log`.

Smoke result:

- Selected executable: `/nix/store/vcxb3mrqcr4yrglwf9fmv7q6gc2igviz-confctl/bin/confctl`.
- Selected source: `/nix/store/zh2jpdp1hcllnb761v1n61z2yykdkamq-source` (exact
  confctl `d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49`).
- `nixos-stable/nixpkgs` remains root `nixpkgs`, revision `4077fb98`;
  `os-staging/vpsadminos` remains root `vpsadminos`, revision `52eb4de0`.
- All original 11 managed machine names evaluate; no system evaluation/inventory
  or input-update command was used as a smoke test.
- Nix built only the shell environment derivation
  `/nix/store/9cr3pfnp4sziah8q3gw4n9nmzj68z164-nix-shell-env.drv`.
  No kernel or system build occurred.
- Watcher catalog package remains
  `/nix/store/zdr7y043hi6y4sbfbsixsrlgbvd530nk-dev-workspace-0.2.0`, catalog digest
  `7659519e2fbe326ba88f3f4e4b07169f291b61a907be06e5b9e374d27fced37e`, utility
  `dw_32fc0df129055f50f5e6054c8d971d33430112edeba8b88d`, saved Luna/low,
  danger-full-access/approval never. Its operation session `62435` and all cells
  completed, with no work left running.

Source checks at exact adopted SHA are reused from package C and its independent
review/CI receipts as directed; this adoption does not repeat them. Lock schema
and persisted state are unchanged. Reverting this new pin restores prior tooling
behavior without a data migration; no system activation is needed to load the
new tooling shell.

Publication succeeded with ordinary SSH feature push from `72c18d8` to `fadb89a`;
no force-push or default merge. Fresh `git ls-remote` verifies the retained
feature ref exactly equals `fadb89a3f828bc98ea75aa5fcd8de953390c15e2`.
Git/index/rebase/hook-preparation window is released to lead for integration
preparation. No further feature head mutation without coordination. No source,
metadata or shell-check gaps remain. Runtime deployment/system validation is
outside this dependency-only adoption; none was performed. Lead owns acceptance, independent history
assessment and approved default integration.

## Documentation rationale

This dependency adoption introduces no reusable configuration procedure. Keep
its individual proof here; no project docs change is useful.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-18-nixos-channel-update/)
