# Final source review packet

Session: 2026-10-05-handle-duplicate-vps-delete. Review owner reviewer0, saved
gpt-6.1-sol/xhigh, read_only; no model/effort override. High risk classification
conservatively covers VPS destructive-action authorization/error semantics and
channel rollout compatibility, despite the bounded guard. Applicable lanes:
general, architecture/repetition, scope/proportionality, risk/compatibility.

## Requested outcome and boundaries

The user approved implementation after reducing the broader idempotency plan
to a friendly ordinary error. Review plan.md and architect-owned design.md,
plus state.md evidence. Exact text: EN “This VPS is already marked for
deletion.”; CS “VPS už je označeno ke smazání.” Main-agent writing skill applied.

Guard requested soft_delete/current soft_delete after restricted lookup,
maintenance and owner-state checks, before generic VPS-state/lifetime expiration
lookup. Return HTTP200/status:false, no state mutation. Preserve admin
lazy:false hard-delete escalation, unauthorized/foreign/maintenance/account
precedence, active/suspended deletion and ResourceLocked423.

Non-goals: concurrency/idempotency, chain reuse, helpers, generic lifetime changes,
new locks, success no-op, nil-safe state_id, new inputs/schema/protocol, WebUI
controls/layout or lifecycle docs rewrite. In-flight/stale reads retain existing
behavior; message describes stored state, not successful node work.

## Source scope

Worktree: ../../worktrees/2026-10-05-handle-duplicate-vps-delete/vpsadmin
(source root under /home/aither/workspace/ai/vpsfree.cz). Base
6cda3e3667b1a4610d040f20566954f5c714c823. Head/complete committed inventory will
be appended before assignment. One logical behavior commit bundles the guard,
its two translations and regression specs, inseparable for the error contract.
No superseded broad approach was ever coded. No migration/schema edits.

Documentation checked: source docs/README.md, object-lifetimes/transactions,
required development/testing/localization guidance. Existing brief and immediate
ordered guard express the bounded choice; no general project documentation
rewrite useful. Visible API error may surface through existing WebUI handler.
Canonical vpsfree-kb-contracts/docs/webui-change-workflow.md requires exact
feature pin/check after reviewed source publication; no KB writes/production
publication, page edits or screenshots presumed.

## Verification and follow-on scope

Quick checks: changed-file RuboCop passed, locale normalization/health passed,
diff whitespace clean. Full existing vps_write_spec.rb had134passing examples and one new suspended-
owner fixture failure (unpaid account denied by payments auth plugin). Corrected
using existing mark_user_paid_until! fixture helper. Final exact staged Delete
group rerun passed18examples/0failures via isolated MariaDB,1m47s. Logs:
vps-write-specs.log, delete-regressions.log. Final staged git diff HEAD SHA256
119a5bf92c93d293228c78080c9ebd56e294687e916f57532e1862795ca3e6fe.
Lint/locale normalization-health passed; no other failed checks remain. Source hooks
signed and active; no bypass. Member sandbox socket restriction resolved for
tooling via lead execution of prescribed commands, without authored-source
takeover or saved access changes.

After source review, publish exact source branch and pin channel vpsadmin / role
vpsadmin -> vpsadminServices in configuration using generated confctl set commit.
Configuration base e179a58ee3f7ceb4cf0b253d368c8ad94967b2d5 already pins source
f9beb46e5206864bca9d37672e1419cf03661467. Delta to source base is three upstream
commits: f73f9a5e0 WebUI dependencies, 76bbced55 CI evidence, 6cda3e366 CI topic
partition. No migrate/schema delta. Inspect full cumulative source pin delta
before claiming readiness, and exact generated pin after preparation. Preserve
nixpkgsStable/vpsadminosStaging follows and unrelated inputs.

API int.api1/int.api2 build targets only; shared service pin has other consumers
(WebUI etc), no fleet deployment implied. Production/staging roles remain
unchanged. No source/config/default branch merges or activation authorized.
Mixed API workers are compatible but old workers retain old error until updated.
No new state for rollback from this fix; any cumulative pin dependency behavior
needs ordinary provenance. Actual live config/database provenance is unknown;
API autoSetup=false, no migrations or production adjustments authorized.

## Required review conclusions

Review committed complete base-to-head history and final diff directly, all
selected lane references and repository instructions. Explicitly conclude on
obsolete history, follow-up fixes/compatibility paths and no-migration lineage.
Do not rubber-stamp supplied conclusions. Report findings by severity with
file/line/commit and residual risks/test gaps. Stay read-only; no nested agents.

## Committed final inventory

Source HEAD b4ef8535a629ee8c9cd753afecdb05e0895d0eea. Complete series from
base6cda3e3667b1a4610d040f20566954f5c714c823: one commit b4ef8535a,
api: report repeated soft deletion as a localized error. Final diff fourfiles,
128insertions/0removals: resources/vps.rb5lines, en.yml1,cs.yml1,
vps_write_spec.rb121. Clean worktree/index. No migration/schema paths; no
new migrations whose merged/released/deployed/external provenance needs support.
No obsolete broad design, helpers, compatibility paths or follow-up commits
remain. All declared precommit hooks passed; commit-msg hooks passed with
nonblocking72column warnings, message follows required<=80columns. No bypass.
Exact source feature not yet published. Configuration/contract worktrees remain
at registered bases without edits; their follow-on mechanical pin/check phases
are deliberately sequenced after this source review.

## Final downstream inventories (mechanical pins)

Configuration basee179a58ee3f7ceb4cf0b253d368c8ad94967b2d5 ->
headb5d9d0941eb14d2cc077d6527ff548f50640bc50, sole generated commit
inputs: set vpsadminServices to b4ef8535. Only flake.lock3insertions/3deletions
locked source rev/time/hash; fullnode comparison proves no other nodes/follows/
production/staging changes. All hooks passed and generated changelog preserved.
No schema/migration paths in own branch or cumulative f9beb46e5..b4ef8535a
source delta. Clean history/worktree, no superseded commits.

KBcontracts baseaaecac90b9b4f6403a929af774634be7056b2b77 ->
head873758fd6aec0c03f50a94600e0ceab97946f255, sole commit contract: pin reviewed
VPS deletion error fix. Fivefiles8insertions/8deletions: flake.nix/lock,
captures.json, contract/navigation.yml, contract/pages.yml. Four authored files
identical to base after oneSHAreplacement; locknodeonly source revision/time/
hash+original rev, all follows/otherinputs unchanged. No controls, fingerprints,
page bodies, media or runtime logic changed. JSON/YAML parse+reference agreement,
staticNixparse and whitespace passed; no declared/active hooks. Extra config-
shell Nixfmt rejected unchanged KBbaseline equally; not a requiredKBhook and no
formatting expansion. No migrations/schema in own branch or cumulative source
a65a4dfeb92a59df4a80a737a20bcbf8558793ff..b4ef8535a delta. Cumulative22commits
are17upstreamdeps,1upstreamOAuth,3upstreamCI,1reviewedfix; WebUIchangedpaths only
composer.lock/php-packages.nix. No semantic/control/page code changes.

Both pins are mechanical review exemptions, not new substantive deliverables.
Please independently inspect complete committed histories/finaldiffs before
whole-branch readiness, explicitly conclude obsolete history/migration lineage
and intended exactrevision/follows preservation. This is a scoped readiness
inventory follow-up, no source rereview or new feature review lane. Required
KBbin/check, twoAPIbuilds and exactsourceCI are next; no activation/merge.
