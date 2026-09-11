# Mandatory change review: scope and proportionality

Lane: scope and proportionality
Model/effort: `gpt-5.6-sol`, `xhigh`
Reviewed repository: `vpsfree-dev-workspace`
Reviewed range: `0a9c974994746e2a6d9d74e83cde8abbf0e65f0a..961dadffa8ddfa303d2fef783ff27fd3ad966d83`

The review also inspected the consuming workspace at `f50473c`, the pinned
vpsAdmin and vpsAdminOS inputs, and the current vpsAdminOS worktree consumers
registered in the shared bare repository. The amended final commit only changes
the smoke assertion from an ineffective memory check to bridge-link and local
SSH-forward checks.

## Blocking

None.

## Important

1. **The supported vpsAdminOS source-worktree boundary is implicit, and the
   smallest maintainable contract has not been stated.** Commit `30516d8`
   requires the source-gem overlay shape introduced by vpsAdminOS commit
   `b0c2ea2552ab9b3bcb493a6bdad5f23c698addcc`
   (`dev-clusters/vpsadminos/flake.nix:39-44,69-78`). Switching to the existing
   public `vpsadminos.overlays.all` API would move the minimum to commit
   `6f9b2c755143197bd9c3452e1c0121b22e978c4d`, but would make the boundary
   smaller and owned by vpsAdminOS.

   This is a current-consumer issue rather than hypothetical historical
   compatibility. The workspace has attached vpsAdminOS worktrees at
   `6dc4209c4` (`2026-06-01-shared-vpsadmin-test-helpers`) and `d9c4552dd`
   (`2026-06-10-vpsadminos-nftables-bug`); both predate the source-gem and
   exported-overlay interfaces. After deploying the new user-profile package,
   `vpsadminos-devcluster start` or `update` for either slug selects that
   worktree and fails during Nix evaluation before it can manage the VM.

   A general compatibility layer for every historical overlay/gemset shape
   would be disproportionate. The smallest credible contract is to use the
   current public overlay, explicitly validate or clearly diagnose its absence,
   document the minimum source interface, and record that an older worktree has
   to be rebased or evaluated with its originating package generation. If those
   two attached worktrees must remain runnable with the new package, that is a
   concrete decision to support and test the older pre-`b0c2ea255` shape, not an
   implicit fallback.

## Advisory

1. **Transactional replacement of the complete certificate set is useful but
   is separate hardening unless its preservation guarantee is added to this
   initiative.** `cert_init --force` and `cert_import --force` already removed
   the old files before creating or copying replacements before this commit
   series (`dev-clusters/vpsadmin/bin/devcluster:393-490`). Commit `35a7090`
   adds early returns, so a failed OpenSSL or copy operation now stops the build
   instead of continuing through the locked callback; it does not introduce the
   remove-before-replace sequence.

   A late disk, OpenSSL, or copy failure can still leave no usable local
   development certificate set. Fixing that correctly requires a same-filesystem
   staged set, validation, a multi-file commit/rollback policy, and tests for
   automatic reissue and explicit import. That is materially broader than the
   requested control-flow repair and the certificates are regenerable local
   development state, although replacing the CA can require browser trust to be
   established again. Record this as an accepted pre-existing residual risk or
   schedule a focused credential-transaction change; do not grow this repair
   into a generalized filesystem transaction mechanism solely because early
   returns exposed the old behavior.

## Proportionality decisions for cross-lane findings

- Replacing the private `import (vpsadminos.outPath + "/os/overlays") { ...; }`
  calls with the already exported `vpsadminos.overlays.all` is a proportional
  simplification. It delegates input wiring to its owner and directly addresses
  the demonstrated drift without adding an abstraction.
- The duplicate runner dependency construction has also demonstrated drift, so
  one small organization-owned helper copied into both packaged flake roots is
  proportionate if it is needed to resolve the architecture finding. Adding a
  new vpsAdminOS exported alternate-runner builder in this initiative would add
  an affected repository and public API for only these two internal consumers;
  no current consumer in the packet requires that expansion.
- Checking the existing readiness/PID/socket cleanup and log preparation before
  launch is within the explicit failure-propagation boundary. It is a handful of
  direct return checks around the existing operations, not a new recovery
  framework.
- The command tests and `devcluster-check` app are proportional to the owned
  behavior. They cover the two provider roots, the two network branches,
  packaged defaults and override plumbing, runner loading, retained build links,
  and representative external-command failures. Exhaustively reproducing Nix,
  OpenSSH, or OpenSSL conformance would not be warranted here.

## Residual gaps

- The amended `961dadf` smoke run was still evaluating while this review was
  written. Its final result remains required before deployment.
- No VM was launched as required by the review constraint. Real bridge starts,
  readiness, update ordering, stop/restart, and retained-disk behavior remain
  integration acceptance work.
- The smoke app validates the current pinned vpsAdminOS interface only. It will
  not enforce whichever historical-source boundary is chosen for the Important
  finding unless a deliberate older-interface case is added.
- The shell tests use representative command stubs. They demonstrate provider
  control flow and lock release, but real copy, activation, runner-process, and
  certificate-tool failures remain covered by the planned integration work and
  the explicitly recorded certificate residual above.
