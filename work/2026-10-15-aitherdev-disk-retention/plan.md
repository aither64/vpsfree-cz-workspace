# Aitherdev disk cleanup and retention

## Goal and authorization

Implement the accepted plan: clean confirmed retired temporary tests, track and
schedule the Nix cleanup helper in aitherdev configuration, and collect completed
coordination payloads without losing recovery or history. The user authorized
tracking, implementation and autonomous aitherdev deployment through
vpsfree-cz-configuration. Default-branch integration is not authorized. Do not
remove old .osvm-qemu disks.

The active confctl rewrite initiative owns classification of its retired temporary
data; do not sweep its directories by name. The ad hoc private KB verification
tree can be retired manually after exact runner/guest shutdown. Do not add a KB
retention framework for that one-off tree.

## Components and ownership

- vpsfree-cz-configuration: packaged Python helper, aitherdev Nix/Home Manager
  wiring, daily retention, serialized pressure GC and host runbook.
- dev-workspace: reference-aware coordination payload collection, preparation
  expiry, CLI, scheduler integration, focused tests and runtime documentation.
- workspace: matching nested runtime selection and deployment documentation.
- vpsfree-kb-contracts: original-runtime shutdown inspection only; no code change.

Use new feature worktrees and published dated branches. Initial inspection found
no bound session. This initiative was created with --no-codex to avoid starting a
duplicate conversation. There is no usable retained team; use ordinary lead work
and the installed standalone independent-review fallback, not an invented roster.

## Retention decisions

| Data | Policy |
| --- | --- |
| Completed recognized temporary tests | Seven inactive days; live runs and holds survive |
| Standard Nix profile generations | Seven days, two through current; protect running/booted and post-rollback generations |
| Finished coordination payloads | Collect immediately after their last required reference ends |
| Prepared but unsubmitted operations | Seven idle days; inspection does not renew |
| Compact coordination receipts and history | Retain |

Keep the helper's dry-run default and compatible options. Collect whole recognized
/tmp/**/os-test-* trees only with completion evidence, available run locks, no
process references and no .keep marker. Report unknown layouts. Preserve managed
clusters, deployments and workspace roots for their owning tools. Never delete
store paths manually.

Retain queued/running operations, pending integrations, unresolved attempts,
deployment review/recovery, installed/retained rollback dependencies and shared
payloads until their final required reference ends. Remove worktrees through Git.
Add dry-run/apply JSON GC, completion triggers and periodic retries. Keep immutable
artifacts and the ledger format; put expiry/collection bookkeeping separately.
Existing unused preparations receive a seven-day adoption grace period. Expired
new submissions require preparation; completed request receipt replay remains
idempotent.

## Compatibility and rollout

No database/API/client/protocol migration or coordinated fleet update is intended.
CLI additions are additive; existing ledger/artifact identities remain unchanged.
Use existing generation transition exclusion to serialize collection with old/new
preparations and profile switches. External filesystem/Git commands remain outside
the ledger mutex. Preserve uncertain ownership and package rollback. Old binaries
can read retained compact state; software rollback cannot restore deleted data.

Package the helper with fixed Python/Nix dependencies. Back up the original local
script before managing its compatibility link. Daily retention and pressure GC
share one lock. Application deployment stays in the user profile; configuration
selects its matching host contract. Manage pins through the declared confctl
channel and workspace nested runtime input.

Implement, commit, run quick checks, obtain independent high-risk review, then run
longer checks/builds using fresh utility watchers. Deploy through the native
coordinator, respecting existing reservations. Dry-run collectors before applying
and record exact deletions/reclaimed bytes. Retain unmerged feature branches and
leave this initiative active until explicit integration direction.

## Documentation and verification

Put generic collection/expiry contracts in the runtime coordination guides and
host policy/recovery in configuration operations docs; keep exact rollout and
cleanup evidence here. Reconcile final history, CLI, mixed versions and docs
before independent review.

Cases: age boundaries, profile rollback, running/booted systems, active test locks
and processes, holds/unknown layouts, incomplete scans, shared roots, queued or
uncertain work, reservation release, expiry/adoption, receipt replay, concurrent
preparation, interrupted deletion and rollback. Then package checks, composed
deployment-contract verification and the aitherdev build. Stop unexpected local
kernel builds.
