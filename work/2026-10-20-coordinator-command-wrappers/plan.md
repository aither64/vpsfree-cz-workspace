# Logged coordination commands

Implement the accepted design in generic dev-workspace and the workspace's
instructions. The coordinator owns resource exclusion, optional machine
reservations, process records and notifications. Sessions own their commands,
Git hooks, review, deployment choices and effect verification.

New commands execute in existing worktrees without coordinator-generated source
or target copies, hook-framework discovery, signing or Nix evaluation. Normal
exit records success/failure and releases execution locks. Interrupted execution
retains exclusion until explicit owner resolution. Explicit machine reservations
remain until released. Existing operations, integration journals, deployments,
reservations and uncertain-effect recovery retain their original contracts.

Add bounded versioned command metadata and package capability checks; share
resource exclusion with legacy work. Freeze the old workflow for new work while
allowing exact retained runs and jobs to continue. Preserve forward-only package
recovery and lifecycle fencing. Update generic documentation and workspace
instructions; package the existing integration guide for legacy recovery.

Verification: focused Ruby and CLI checks, command/resource concurrency,
interruption and idempotency, old/new operation coexistence, lifecycle and package
compatibility, disposable Git/Overcommit hook behavior and disk/latency checks.
Commit intended changes and run independent mandatory review before longer
integration checks. Publish feature branches and inspect CI. Runtime selection,
default-branch integration and initiating-session recovery are not authorized.

Compatibility: no rewriting old snapshots, jobs or activation receipts; preserve
all roots required by live/recovery work. New metadata must prevent selection of
an incompatible package. Old and new executors must not run conflicting work.
No database, external API, daemon protocol or project schema changes are planned.
New local CLI/API capability and persistent command records are additive.

Documentation readers: workspace agents and operators. Supported behavior and
failure semantics belong in generic coordination guides; local workflow rules
belong in the workspace instructions. Session evidence stays here.

Deployment scope added by the user: "you can deploy aitherdev using
vpsfree-cz-configuration and verify that it is working". Prepare exact feature
runtime selection in this initiative's workspace and configuration worktrees,
preserve extension/sibling inputs, review applicable changes, build/copy outside
claims and activate aitherdev through supported owned coordination. Select the
matching composed application profile and verify system/profile identities,
portal/router/coordinator health and disposable command behavior. Keep feature
branches and machine ownership for review. No default-branch integration or
recovery/cleanup of another session is authorized.

The current installed coordinator predates command wrappers. This external
threadless initiative cannot use ordinary managed-owner admission, and initial
bootstrap refuses a ledger containing other owners. Investigate the supported
transition route before activation; do not invent ownership, bypass a reservation,
hand-edit ledgers or run direct confctl activation around coordination. Continue
independent pin/build preparation while resolving this compatibility boundary.
