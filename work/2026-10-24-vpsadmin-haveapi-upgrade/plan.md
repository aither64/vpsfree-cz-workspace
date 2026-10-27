# vpsAdmin HaveAPI 0.30.2 upgrade

## Goal and scope

Update every HaveAPI server/client dependency in vpsadmin to released 0.30.2.
Configure API documentation examples for the Go SDK and the published Rust
SDK from crates.io. Verify the released documentation performance remedy in
the real consumer before closing the existing R1 blocker.
Carry forward the vpsadmin-webui work from 2026-10-19-haveapi-async-client into
this session's own branch, replacing the custom client with the published async
TypeScript npm client. Update KB manuals:vps:api with Python, Rust and
TypeScript clients, preserving supported existing clients.

## Affected repositories

- vpsadmin: Ruby dependencies, lockfiles, generated Nix dependency metadata,
  documentation configuration, and targeted verification.
- vpsadmin-webui: authorized takeover provenance and published-client migration;
  architect confirms the repository's registration and local PR requirements.
- Knowledge base: local bilingual candidates and guarded review manifests;
  assess vpsfree-kb-contracts ownership before adding repository scope.
- haveapi and generated-client repositories: read-only release/API references
  unless investigation establishes a separately approved need to edit them.

## Approach and owners

The retained Full-team architect (architect0) owns investigation and design.md,
including package boundaries and acceptance checks before implementation.
The lead assigns complete packages to ready retained implementers, serializes
Git operations and overlapping edits, and owns session records and final
member-facing writing. reviewer0 performs independent final review after all
intended substantive changes are committed and quick checks pass.

## Compatibility and deployment

Inventory server/client protocol assumptions, authentication, asynchronous
completion, error handling and mixed-version behavior. Preserve persisted
state and supported API behavior; no database migration is intended. Record
any migration discovered and its deployment/consumption provenance. Carry prior
WebUI source without changing the old session. Prefer incremental deployment;
record ordering and rollback constraints in design and owning project docs.
No production deployment or default-branch integration is currently requested.

## Documentation

Developers need dependency and client adapter rationale in owning project docs;
members need accurate install/import links and supported examples in the API KB
article. Lead applies the user-facing-writing skill after facts settle. Prepare
complete local candidates and exact staged review before requesting production
publication approval. Temporary rollout and review evidence stays here.

## Acceptance and verification

- All vpsadmin HaveAPI runtime pins and resolved metadata use 0.30.2.
- Go/Rust documentation examples use correct published client profiles.
- WebUI uses the published async npm client and preserves login, session,
  errors, action completion, list/pagination and existing UI behavior.
- KB names Python, Rust and TypeScript clients with verified package links and
  usable examples, retaining language mapping and markup.
- Repository hooks and targeted quick checks pass; commit complete deliverables,
  inventory complete history/diff/migrations, then independent final review.
- Run longer applicable checks only after review with a fresh Luna/low watcher;
  publish feature branches and repository-required PRs without merging.
- Production KB promotion requires user approval of the exact staged bundle.

## Decisions

The user's takeover direction authorizes carrying forward the prior WebUI work.
The user additionally permits reusing existing vpsadmin-webui PRs; prefer
matching PRs and record exact source/head ownership and history provenance.
Do not alter unrelated old-session repositories or lifecycle/records.
Do not archive or stop this session as part of completing the task.


## User steering — 2026-10-25

The user owns the performance remedy in another session. This session keeps
its review evidence and external dependency without implementing a HaveAPI fix.
The Rust SDK is now published on crates.io; verify release identity and replace
the current API profile's Git source and KB installation guidance with registry
installation, preserving exact old provenance in historical receipts. Run
focused rendering/configuration checks, commit the change and send affected
ranges to the same independent reviewer. No API runtime/version/SDK source
changes outside this adoption are intended.


## User steering — 2026-10-26

Adopt released HaveAPI 0.30.2 across the existing vpsAdmin server/client and
React client scope. Verify release/source identities, preserve supported Rust
registry guidance, update affected KB versions, and validate the performance
remedy against the original consumer request/auth scenarios. R1 is only resolved
by accepted source and actual new measurements, not the release number alone.
Consolidate superseded unapplied dependency streams while retaining reviewed
old/new ranges and previous failure evidence. Complete committed-deliverable
review before long integration/performance campaigns. No provider fix or
production/default integration/deployment is requested by this instruction.

## User testing cluster — 2026-10-26

User direction, relayed by architect0's direct user thread in this conversation:
"when you'll be done, start vpsadmin dev cluster. I'd like to test both user interfaces."
After current verification, start this exact session's native development cluster
using its final vpsAdmin/React feature sources and bridge networking. Expose and
verify both legacy PHP and new React interfaces plus API/OAuth/BFF wiring.
Architect owns source/ownership/effective-input design first; implementer3 will
own execution after an accepted brief. No production deployment, default merge,
foreign-cluster change, session reset/stop/archive or private helper is authorized.
Native status preparation created only this owned stopped cluster's config and
socket stub; no VM/runner was started. Preserve that state. Exact OS/provider
source graph and cached kernel availability are preflight gates, not assumed
equivalent to standalone package checks.

## Accepted postreview verification disposition — 2026-10-26

Actual consumer timing/auth/locale/output acceptance closes R1. Representative
SDK compilation covers 26 complete programs (20 actual plus six labelled synthetic
nested/nullable fixtures), not all 168 generated programs. C normal units,
production and Nix package checks pass. Current pinned browser run is 60/62;
the same two mobile transaction-expansion click failures reproduce on the exact
complete pre-upgrade base with its own app/fixtures/install and the identical
rooted runtime. Lead accepts this specific existing mobile interaction residual
as nonblocking for the scoped HaveAPI upgrade and development testing, without
a clean-browser claim or an asserted CSS root cause. Preserve tests and evidence;
an unrelated layout fix is not added to this upgrade.

Complete A core/full topics and legacy checks before cluster startup. E remains
prepared, with accepted native-source selection distinguished from standalone
package builds; fresh exact graph, capacity, native collision/ownership and
physical-host hold contract classification precede activation. See state.md,
design.md and devcluster/preflight.md for current owners and remaining gates.

## User-requested launcher fix — 2026-10-26

User explicitly directs "so fix it" for the development-cluster launcher bug:
SSH can consume the remaining machine-name input in prove_full_applied_boot,
while finish_boot records complete coverage. Add vpsfree-dev-workspace source
scope, canonical git@github.com:vpsfreecz/dev-workspace.git, in this session's
own worktree. Architect0 owns bounded design; implementer1 owns source/tests/
component documentation/hooks/commits. Fix stdin isolation and require actual
complete guest proof before full certification, with meaningful draining-SSH,
complete-coverage and failure regressions. Preserve existing state/schema/policy
and supported recovery unless an explicit design need is established.

Commit intended fix and pass quick checks, then independent final review before
longer provider checks. Fixtures must use disposable state, never this running
cluster. Publish ordinary feature branch after required gates. No default merge,
installed package switch, physical-host deployment, live guest-root/envelope
repair, cluster restart/stop/reset or lifecycle cleanup is authorized by this
source-fix request. Keep both interfaces available for testing. HaveAPI upgrade
verification remains accepted for its exact inputs; isolated integration refresh
and PR74 history approval remain separate work.


## Consolidated delivery checkpoint — 2026-10-26

The requested cluster is running original70a/Reactf10; verified TLS, real OAuth
login/logout and independent four-guest current closure/root checks support
current manual testing. Preserve it and all ordinary roots. The old launcher
boot-record defect is documented; the reviewed/published/CI-green F source fix
is not installed and does not repair that record. No further live probes assigned.

The isolated vpsAdmin successor898..2c preserves upstream Faraday2.15.1 and
Guzzle7.16.1 and passed final independent review plus proportionate affected
services/auth/PHP/browser checks. Published as a distinct refresh branch/alias;
original live checkout/ref/locks/config and guests remain unchanged. Owner2
observes nine exact-head CI runs, stopping with a pending handoff if only the
long integration remains. Seven workflows initially succeeded; API/integration
still active. No new broad campaign is planned.

User decisions still required: repository/target default integration, protected
PR74 exact history rewrite, and exact staged KB production publication. No
default merge, runtime installation/live evidence repair or lifecycle action
is authorized. See state.md for exact heads, owners, receipts and acceptance limits.


## User replacement milestone — 2026-10-27

Adopt released HaveAPI0.31.0 in place of the pending0.30 upgrade stream. Add
TypeScript examples in the servers/ruby documentation configuration using
vpsadmin-typescript-client analogously to existing Go/Rust SDK profiles; verify
the owning repository/config interface before implementation. Update both API KB
candidates with the generated TypeScript SDK and a short factual distinction
from generic callback/Promise JS/TS clients. Retain unaffected client guidance.

Architect0 owns bounded design and file/package boundaries; implementer2 verifies
release/client facts; implementers own separate source packages after design.
Lead owns final bilingual KB wording. Consolidate superseded unapplied upgrade
history while preserving exact consumed70a/f10 refs and live checkout/config/lock
bytes. Commit and quickcheck intended deliverables, independently review full
final histories and migration provenance, then run proportionate affected checks
with fresh utility monitoring. Prior0.30 results are not0.31 proof. No live cluster
update, provider installation, default merge or production KB write authorized.


## Explicit postcheck redeployment and KB staging — 2026-10-27

User requests redeploying this session's devcluster when sourcework is done and
permits cluster reset; also requests seeing KB articles in staging. Architect0
prepares currentselectedpublicruntime/sourcebinding plan; E3 executionprep and
verification, lead mutatinglaunch. Apply finalreview/checks first, then exactnew
sources/completeinputgraph/capacity/cachedkernel/ownershippreflight. Bridge; small
TLS/memberlogin/TypeScriptdoc verification, no new broadcampaign. No session
lifecycle/defaultintegration/production/hostprofileswitch authorized. Foreign KB
stage owner2026-09-13-auth-email with pendingrelease must be preserved until
supportedhandoff or explicit disposition; no privatebypass/queue assumed.


## A31-R1 measured upstream issue — 2026-10-27

Final consumer review found repeated full-description normalization in the newly
enabled TypeScript generator. Qualified anonymous full GET with explicit nil
user/session, no Authorization/cookie, correct full-help/EN contract returned200
in15.23135s wall/15.21839s CPU. Historical0.30.2 anonymous4.23s has separately
recorded conditions; no identical-benchmark/SLA claim. BroadAintegration and
redeployment held; no member/admin/warms repeated. Wrong new anonymous absence
assertion is a narrow Btestfix; member privacy remains required.

Prepare a concrete minimal upstream HaveAPI fix in a fresh own worktree: select
only relevant action/provider/metadata before recursive normalization, preserve
existing auth/alias/collision/frozen/context behavior, add meaningful regression
tests in existing documentation suite. Architect owns brief; implementer2 source/
tests/quick/hooks/commit/packet; independent review before longer checks. No new
cache/framework/consumerfork/Nixoverlay, no altered0.31 archive/tag/release/default
merge. User was asked asynchronously whether another HaveAPI session already owns
the fix; incorporate answer and avoid duplicate source work if so. New released
artifact or exact dependency exception needs disposition before consumer adoption.


## User takes upstream fix ownership — 2026-10-27

User will fix HaveAPI in another session and requests a link to any existing
patch. Stop this session's upstream implementation/check/review/publication;
export current completed patch and honest verification state only. Preserve
source/refs/roots, no cleanup or other-session contact. Consumer031 adoption and
authorizedredeploy stay pending corrected release and remaining affectedgates;
Cpublished/KBreviewed candidates remain accepted for their exactinputs.


## 0.31.1 availability and automatic adoption — 2026-10-27

User says0.31.1 release is in progress and may take hours: check about every
10minutes and upgrade when available; also watch for legitimate KB staging
release by user. E2 owns a fresh pinned-policy availability utility first check
now/600s cadence, public package registries+ordinarykb-stage status only. Return
first actionable transition and retain all partial availability facts; no mutable
latest assumption, forced staging ownership or duplicated polling. Normal source
owners then adopt exact published0.31.1, consolidate pending upgrade history,
verify fix/source/config and affected final review/checks. Repeat qualified
documentation role/locale measurement on actually adopted artifact to close
A31-R1; prior0.31.0 raw/qualified timing remains historical. KBlead updates final
wording/versions/manifests; E3 stages when legitimatelyfree and redeploys only
after accepted finalsourcegates with parentnative reset/start. No new upstream
source work, release/tag/defaultmerge/PR74force or productionKB permission.
