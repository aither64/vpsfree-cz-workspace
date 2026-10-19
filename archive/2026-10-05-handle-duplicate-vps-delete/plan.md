# Friendly error for repeated VPS deletion

## Goal and authorized scope

Implement the user-approved narrow plan: replace the unexpected server error
for repeated soft deletion with a specific localized ordinary API error. The
user authorized implementation with "Implement the plan." Include the exact
reviewed source feature pin in vpsfree-cz-configuration. No default-branch merge,
production activation, migrations or session lifecycle cleanup is authorized.
Raw supplied emails remain outside version control.

## Changes and ownership

Architect0 replaces design.md with the narrow design before source edits.
Implementer0 edits vpsadmin and the generated configuration channel pin.
Reviewer0 performs independent final review after committed source changes and
quick checks. The lead owns user-facing wording, tracking and acceptance.

VPS Delete checks requested soft_delete/current soft_delete after owner/account
and maintenance checks but before generic VPS-state rejection and lifetime
expiration lookup. Return ordinary error! (HTTP200/status:false), localized via
errors.vps_already_marked_for_deletion:
EN: This VPS is already marked for deletion.
CS: VPS už je označeno ke smazání.

No helper, lifetime rewrite, locking change, chain reuse, successful no-op,
nil-safe state_id change or concurrency test infrastructure is included.
Retain admin soft-to-hard deletion, existing unauthorized/not-found policy and
in-flight HTTP423 responses. This supersedes the broader retry proposal.

## Compatibility and configuration

No new schema, persisted format, route/input, client generation or node protocol.
Existing clients receive a normal actionable API error. Old API workers retain
old behavior until all workers update; software rollback restores old behavior.
Use fresh upstream source/config feature worktrees so old baselines cannot
downgrade already-deployed changes. Pin only channel vpsadmin/role vpsadmin,
which maps to vpsadminServices, using confctl's generated exact feature commit.
Preserve other inputs/follows and generated changelog. The cumulative old-pin to
new-pin delta may include migrations already upstream; establish live provenance
before any future activation. The duplicate-delete fix adds none.

## Verification and documentation

Focused resource regression tests: owner/admin repeat in EN/CS, no transition
call or changed deadlines/logs/chains; admin lazy:false from soft_delete still
hard-deletes; auth, maintenance, owner suspension, suspended soft delete and423.
Run relevant locale validation, lint and hooks. Inventory complete base-to-head
history/final diff/migrations and run mandatory independent final review. Follow
required WebUI documentation impact workflow for visible error text; limit any
updates to reported impact. Publish source feature then generate config pin.
Inspect full lock diff/cumulative version inventory and build both API host
configurations via fresh verification watcher. Source/config integration and
production deployment remain separate user-directed steps.

## Tracking

Initial plan/state were committed as af907458 before project work. Preserve
normal tracking cadence; current decisions and results stay updated in working
records. Session stays active and open.
