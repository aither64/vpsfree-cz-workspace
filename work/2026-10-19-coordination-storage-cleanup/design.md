# Design and verification brief

Design owner: lead; substantive design uses xhigh. No retained team is available
for this externally initiated, initially threadless session. No specialists are
assigned automatically. Final review uses the installed catalog fallback.

## Interfaces and invariants

Extend Collector in libexec/workspace-coordination-gc.rb and its Ruby tests.
The existing gc preview/apply JSON interface and five-minute scheduling remain.
A pending/held/unknown operation is not a completed one. All original source GC
liveness, orphan grace, explicit holds and dirty worktree checks remain intact.

Inventory scratch only under integrations/<validated UUID>/<repository>-<12 hex>
-<12 hex>, bound to a known journal and repository. Only complete integrations
are collectible; hold every driver's existing lock through planning/removal.
Validate Git registration, detached state, canonical repository ownership and
cleanliness; preserve process references, holds, busy resources and live metadata
references. Remove via Git, retain refs and compact journals. Journal optional
payloadGcPending records bind exact path/common Git directory/head before removal
and let a retry finish an interrupted removal even after the directory vanished.
Old source retention bookkeeping remains unchanged and old readers can ignore
this additive journal field. No DB migration or new predecessor schema is needed.

Recognize notification and background-integration root names by their actual
UUID/package-digest suffixes. Unknown names or mismatched targets survive.
Notification workers share their existing owner locks with collection; active
services/workers survive. Undelivered outbox payload dependencies remain rooted.
Future delivery dispatch recreates its selected-package worker root. Background
integration roots survive unfinished journals and active services/drivers.

Recognized workspace Nix profile generations retain the selected generation,
one predecessor, all newer generations after a legacy rollback, and packages
referenced by live operations/preparations/recovery. Prune older generations only
under the existing profile-transition exclusion using nix-env, with exact profile
identity revalidation. Keep separate Codex generation roots. Ordinary Nix GC owns
store deletion; current profile selection is never changed by collection.

## Boundaries and recovery

The local operator is trusted as documented in repository AGENTS.md. Checks
protect ordinary wrong ownership, concurrency and interrupted operations, not a
hostile root operator. Do not collect user feature worktrees, branches, archive
records, cluster state, VM images or unrelated caches. Reducing bulky archived
artifacts and filtering all Git flake inputs is a separate structural improvement;
this change must first end known disposable lifetime leaks without losing records.
The exact bytes reclaimed depend on other live roots and processes.

## Acceptance and checks

Tests must demonstrate eventual cleanup after completion and repeated sweeps,
retention during live references/locks/services, pending notification dependencies,
unknown/dirty/different-repository checkouts, interrupted Git removal recovery,
and profile current/predecessor/live protections. Quick Ruby syntax and focused GC
suite precede final independent review. Existing Ruby coordination/integration
coverage follows review under a fresh watcher. Package/build and dry-run rollout
are chosen once the implementation is settled. No integration approval is inferred.
