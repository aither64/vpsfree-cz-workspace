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
