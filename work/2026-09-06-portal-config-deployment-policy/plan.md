# 2026-09-06-portal-config-deployment-policy

## Goal

Finish the workspace portal as a user-managed, multi-workspace service while
keeping only its privileged HTTPS substrate in the aitherdev NixOS
configuration. Unify CLI and browser sessions, retain system-managed Codex
updates, correct creation recovery and the `xhigh` default, and make initiative
completion mean that every registered feature head is provably merged.

Also provide a safe `dev-session reopen` workflow and use it to restore
`2026-09-05-cgroup-v1-shared-device-fix` with its original retained branches.

## Affected repositories

- Coordination workspace (`aither64/vpsfree-cz-workspace`): hybrid user runtime,
  registry and routing, CLI dispatch, lifecycle enforcement and recovery,
  tests, documentation, and durable agent rules.
- `vpsfree-cz-configuration`: privileged nginx/TLS/Basic Auth substrate,
  wildcard workspace domain, user lingering, and removal of system-owned
  workspace application services and packages.

Both repositories use the existing
`2026-09-06-portal-config-deployment-policy` feature branches. Their default
branches must not receive the portal implementation until the user explicitly
requests integration.

## Approach

- Package the portal, private session engine, public multi-workspace dispatcher,
  cluster helpers, router, and user-systemd units in the workspace flake. Install
  them in a dedicated user Nix profile managed by `workspace-host`.
- Store validated workspace registrations in
  `~/.config/vpsfree-workspaces/registry.json`. Select a workspace from the
  longest matching root or explicit `--workspace NAME`; require the flag outside
  all roots once multiple workspaces exist.
- Run a Host router on a group-restricted Unix socket plus per-workspace portal,
  Codex App Server, and tmux user services. Derive private application runtime
  paths below `/run/user/1000` and reject unknown Host headers.
- Keep Codex sourced from `/run/current-system/sw/bin/codex`. Validate its App
  Server schema and model catalog before adoption, retain a user GC root for the
  last compatible version, and reconcile compatible NixOS updates only after
  active turns become idle.
- Make `vpsfree-cz.workspace.aitherdev.int.vpsfree.cz` canonical. Keep
  `vpsfree-cz-workspace.aitherdev.int.vpsfree.cz` as a redirecting alias and use
  a leaf certificate with both the wildcard workspace SAN and legacy hostname.
- Preserve the existing root-owned unencrypted CA and Basic Auth credentials.
  Remove the workspace flake input, CLI wrappers, portal package, and application
  services from the system configuration.
- Keep new-session reasoning at `xhigh`. Resume an already materialized partial
  creation without reapplying current defaults; apply resolved settings only to
  genuinely new or replacement threads.
- For `complete`, fetch every registered repository, require local and remote
  feature tips to agree, and require that exact head to be an ancestor of the
  configured `origin/<default_branch>`. Report all unmerged or unprovable refs.
  Skip merge proof only for `abandoned`; allow registration-free coordination
  initiatives.
- Add non-mutating `finalize --check` so the portal proves finalizability before
  releasing clusters. Add journaled `reopen`, with an explicit override for an
  abandoned archive, preserving identities while clearing terminal metadata.
- Reconstruct legacy repository registrations from retained branches when
  worktrees are re-added. Use an explicit base when supplied, otherwise require
  one unambiguous merge base with the configured default branch.

## Compatibility and deployment

The one-time service migration quiesces existing Codex activity, replaces the
system portal services with user services, and recreates terminal tmux clients
without changing stored conversations or project worktrees. Historical socket
paths in manifests become diagnostic; live registry and authority data select
the current endpoint.

The existing CA and password remain valid. The server leaf is renewed when its
SAN set changes. Unknown workspace hosts remain inaccessible, nginx continues
to strip Basic Auth before proxying, the shared router socket is limited to
nginx and `aither`, and per-workspace application sockets remain user-private.

The workspace user package is deployed from its unmerged feature worktree. The
configuration feature branch is deployed directly to aitherdev. The user owns
the internal wildcard DNS and aitherdev deployment; portal iteration afterward
requires only `workspace-host switch`, not a NixOS rebuild. Rollback selects the
previous user profile generation and retains the last compatible Codex store
path.

An initiative stays active until all registered branches are merged. Pushing,
testing, deploying, or removing a worktree does not complete it. Pre-merge
follow-up work reuses the same slug and retained branches. Exact ancestry means
squash-only or cherry-picked integration does not qualify.

## Testing plan

- Cover workspace registry validation, Host routing, PWD/flag selection,
  profile switching/rollback, user service arguments, and Codex reconciliation.
- Run Go, Ruby, JavaScript, protocol-contract, and Nix package checks, including
  a mixed-version creation recovery regression and `xhigh` resolver coverage.
- Test finalization with unmerged, merged, divergent, missing, and unprovable
  feature refs; abandoned and coordination-only initiatives; and aggregate
  diagnostics.
- Test reopening current and legacy archives, metadata cleanup, abandoned
  override, dirty/duplicate/live/symlink states, interrupted recovery, and
  retained-branch worktree reuse.
- Evaluate the aitherdev NixOS configuration and verify wildcard/legacy TLS,
  VPN-only nginx, credential permissions, lingering, and absence of system-owned
  portal services.
- Run mandatory change review at `xhigh` after quick checks, then full package
  checks. Deploy the configuration feature branch and wildcard DNS, validate
  both URLs and CLI/browser interoperability, then recover the legacy cgroup
  initiative and verify its two exact branch heads and original base commits.
