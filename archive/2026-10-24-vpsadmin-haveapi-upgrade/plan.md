# vpsAdmin HaveAPI upgrade

## Goal and scope

Current follow-up (2026-11-01): the user requested a separate HaveAPI patch-release
initiative using the same provider and a full team, followed by consumer adoption,
site-specific OAuth setup instructions and relevant configuration channel updates.
The created peer `2026-11-01-haveapi-0321-docs-switch-user` owns HaveAPI master/stable
fixes and actual release publication; this session owns downstream changes.
Lead-to-lead communication is active. A0 owns our bounded design; E2/E1 own product
and site execution once their dependencies are settled. Use **quick verification
only**, retaining mandatory final independent review; no full suite, browser or
system-build campaign and no production deployment. The site setup must generate
shared private material once on api1 and relay via the operator's local machine
to api2, using client ID `api.vpsfree.cz`, Switch user enabled, SSO enabled and
renewable_auto/900-second tokens. The accepted upcoming public extension is
`switch_user_revoke_params: { 'close_sso' => '1' }`; adopt only after actual published
package identity is confirmed. Preserve ordinary logout and all other valid tokens;
sliding documentation-cookie lifetime is outside scope. Site instructions live in
`vpsfree-cz-configuration/docs/operations/vpsadmin-documentation-oauth.md` for
operators; reusable interface behavior remains owned by HaveAPI. [Request and
communication record](haveapi-0321-handoff/request.json).

Previous completed follow-up (2026-11-01): update the existing configuration
`vpsadmin-webui` channel to the reviewed, integrated WebUI main revision if
needed, then merge configuration/master. E1 owns the generated channel change,
normal hooks, exact lock/source scope and affected Newadmin host build; lead owns
acceptance and ordinary FF integration under a short repository claim. Preserve
all other input selections, including product0f and the existing follows graph.
No application/dependency source changes or deployment are included. Routine pin
updates need no product-documentation commit; existing newadmin operations docs
remain authoritative. [Approval and execution scope](integration/configuration/webui-channel/approval.json).


### Finish plan for review: workspace first

[Compact user-review plan](finish-plan.md); technical boundaries are recorded in
[the architect’s finish-plan appendix](design.md#finish-plan-workspace-first-product-defaults-and-react-032-2026-10-31).

1. **Finish and integrate workspace tooling, then the workspace.** E0 finishes
   the existing combined full flake and installed checker, publishes the checked
   provider and hands its exact identity to E1. E1 adds one final provider pin to
   the already combined pointer/repair branch, completes its checks and final
   review/equivalence. Integrate `vpsfreecz/dev-workspace:master` first, then
   `aither64/vpsfree-cz-workspace:master`, with fresh target checks, required hooks,
   short repository claims, SSH publication and remote proof. The user has
   explicitly directed this workspace-first integration order.
2. **Deploy the merged workspace package and release aitherdev.** Prepare the
   exact final package, switch under the existing machine reservation and verify
   the selected profile, portal/conversation health and operation effects. This
   fresh deployment is required because the refreshed consumer changes behavior;
   it is not patch-equivalent to deployedf1d. Reconcile complete deployed lineage
   against the integrated remote defaults, inspect the exact owned claim, release
   it normally and verify release. The existing physical reservation covers the
   workspace application; current evidence does not require application-repository
   merges first. Keep the session, live sources, private files and recovery refs.
3. **Put reusable OAuth logging protection in vpsAdmin defaults.** E2 moves the
   shared frontend/backend/HAProxy policy into the owning product modules for
   API, authentication and PHP WebUI. Keep the existing callback error containment.
   Ordinary product deployments must have the protection without importing the
   vpsFree site configuration. Preserve supported SSL/redirect behavior, native
   useful diagnostics, authentication/session semantics and supported overrides.
   Prove the defaults directly with focused generated-configuration and synthetic
   logging checks. A0 owns the exact module/SSL design before source work.
4. **Reduce site configuration to site concerns.** After the product change is
   reviewed and published, E1 removes redundant copied policy, retains required
   topology/domains/private inputs/Basic authentication and selects one final
   vpsAdmin source revision through the normal channel command. Verify the four
   affected configurations and reuse earlier runtime evidence only with exact
   actual input/derivation equality. No canceled KB/Discourse work is reintroduced.
5. **Update React to the actual HaveAPI0.32.0 release.** E3 can do this alongside
   step3 while workspace verification finishes. Workspace integration remains first.
   Replace the stale0.31.2 dependency,
   regenerate the lock/provenance/Nix dependency hash and preserve current-main
   behavior and auth/retry/mutation contracts. Use the already verified published
   npm artifact, not checked-in tag dist bytes. Run affected quick checks, final
   independent review, then normal unit/build and required Nix outputs. Fold the
   unmerged dependency stream into one final0.32 update and preserve old refs.
6. **Return three corrected application candidates for final review and merge.**
   Retain one active worktree per repository. Every substantive final deliverable
   gets committed quick checks, independent whole-history/migration review and
   its required final checks before publication/readiness. Present vpsAdmin,
   React and site configuration with exact heads and remaining limits. Application
   default merges and deployment remain separately directed; workspace approval
   does not grant them. Preserve existing protected PR/recovery boundaries.

Owners and active paths remain E0 `vpsfree-dev-workspace-services-os`, E1
`workspace-services-os` and `vpsfree-cz-configuration-oauth-clients`, E2
`vpsadmin-oauth-client-logs`, E3 `vpsadmin-webui-031`; architect0 owns technical
boundaries, reviewer0 independent review, lead user-facing prose/acceptance and
integration coordination. No new worktree is needed.

Current status: the user approved implementation on 2026-10-31. A0 is settling
only the protected-redirect composition; E2 owns product defaults, E3 the actual
npm0.32.0 adoption, and E1 the dependent site reduction. Existing workspace tooling
passed its full flake (all nine outputs, complete command56/833 once); the full
installed checker is running. Final E0 publication unblocks E1's sole workspace
provider pin. Workspace integrations/profile verification/release remain first.
Retain one active review alias per repository and existing recovery/private paths.


Workspace-first order explicitly directed by user (2026-10-31): “and let's merge
the workspace changes first, so that you can release aitherdev... include that in
the plan”. Complete the provider/workspace checks, integrate vpsfreecz/dev-workspace
master before aither64/vpsfree-cz-workspace master, verify exact deployed lineage
and reconcile effects, then release the exact aitherdev machine reservation through
the ordinary command and verify release. Final verified profile activation is required: the rebased consumer changes
provider selection and cannot be certified patch-equivalent to deployedf1d.
The recorded physical reservation covers workspace application activation; no
application-repository default dependency currently blocks workspace-first
release. A0 confirmed this from existing receipts and selected runtime policy. Preserve source/private/live recovery and
session openness. Application default merges, deployment and lifecycle remain
outside this workspace-pair direction.

Finish-plan request (2026-10-31): correct shared security-policy ownership so
vpsAdmin provides secure OAuth callback logging defaults, reduce site configuration
to its actual topology/operator concerns, and align React with the intended
released HaveAPI0.32.0 after source/registry compatibility confirmation. A0 prepares
one bounded plan; lead presents it before new implementation. Keep the five
existing final aliases, canceled KB/Discourse scope and live-source boundaries.
Already-running workspace-tooling checks and the existing dependent workspace
consolidation continue independently. Earlier completed source packages retain
their actual verification evidence but are not final-ready under these corrections.

Current consolidation direction (2026-10-31): user requires the changes to be
integrated into one active review worktree per repository. Combine extension
boot-proof/updater/writing siblings and workspace pointer/consumer siblings;
refresh vpsAdmin, React and configuration against current targets. Produce five
coherent final review candidates, preserving deployed source/roots, original refs,
review/migration lineage and protected live paths. Canonical React2e32 and
vpsAdmin33d6 checkouts remain frozen while active; reuse a safe existing React
recovery checkout if needed. Architect owns the brief; implementers own source,
conflicts, checks and commits. Final combined review and required checks precede
feature publication. No default merge, runtime deployment or cleanup is inferred.

KB08 follow-up (2026-10-31): the user accepted the improved articles and asks
that code request a token using username/password literals, with a commented
alternative for an existing token. Update authentication in all six Other-client
examples plus the main Ruby and two backup examples, preserving their remaining
behavior. Architect verifies exact client calls; lead owns bilingual prose; E1
owns normal checks/commit/staging after independent final review. No Basic-auth
substitution, SDK change or live authentication test is requested. KB07 remains
an accepted staged predecessor; production publication is still unapproved.

Current KB task (2026-10-31): rewrite the Czech and English Other clients
sections for end users, with a complete practical token example for each client,
literal placeholder credentials and supported syntax highlighting. Include the
same literal-token correction in the adjacent Ruby example. Keep existing page
IDs, anchors, language markers and unrelated content. Lead owns final bilingual
prose; A0 supplies exact API/highlighter facts; E1 owns bounded offline checks,
normal content commits and additive staging; reviewer0 independently reviews the
committed documentation before staging. No client/highlighter installation,
application change, production KB publication or renewed OAuth project is in scope.
KB staging has been restarted as requested. The devcluster functional deployment
is complete; its confirmed PHP callback logging exposure remains an explicit
limitation of the frozen source, with the separate protection still undeployed.

Current boundary (2026-10-30, supersedes earlier wider client scope): the user canceled KB/Discourse OAuth changes; they were removed from final source and history. The PHP-only feature is reviewed, checked and published. The user explicitly chose to continue only the dev-cluster update, not merge the published branches. The later expanded storage investigation was canceled; the completed1.119GiB cleanup remains recorded.

Current provider correction (2026-10-31): the user wants creation and update to
select OS sources by the same rules and explicitly notes that OS updates can be
desirable. Keep the session checkout, otherwise locally fetched origin/staging,
with no implicit fetch. Supersede the applied-OS pin acc4958 and prepared consumer
13232fe8/package61v; retain their evidence and leave that package uninstalled.
The accepted final design in design.md separates selected guest build inputs from
actual boot-time source exports and host QEMU/virtiofsd. Validate every other
requested layout change and lazily project only selected guest payloads. Untouched
applied descriptors stay exact; services does not realize unrelated node payloads.
Requested targets require their own existing applied proof; unproved legacy targets
refuse before build, while unproved peers do not block a proven target. Retained
start uses proved applied payloads. No schema, export retarget or restart framework.
E0 owns correction/quick/commit/history; parent owns final operator prose. Final
independent review precedes longer checks. E1 refreshes the consumer only after a
reviewed corrected provider SHA, consolidating the pin and preserving the separate
instruction repair. The user subsequently authorized deployment with “you can
deploy it when it'sdone”, clarified as “i mean deploy aitherdev”. Build, check and
prepare the corrected workspace application, then deploy it on aitherdev through
the normal profile switch with the configured machine claim and fresh identity
checks. This approval needs no repeated confirmation. Preserve source33d6,
original3922 recovery and all roots. No default integration, host-system rollout,
production service deployment, guest reboot or lifecycle action is authorized.

Implementation authorized (2026-10-30): the user says "proceed with
implementation" of [the OAuth client protection plan](oauth-client-log-protection-plan.md). This covers source changes, focused
checks, ordinary commits, independent final review, scoped postreview tests
and feature publication. It does not authorize production access/deployment
or default integration. E1 owns site proxy/backend configuration and all Git
assembly in new `vpsfree-cz-configuration-oauth-clients` from accepted249f;
E2 owns disjoint KB package/tests; E3 owns disjoint Discourse package/tests.
Architect confirms exact paths/interfaces and remaining narrow gates before
application edits. React and existing source/config/rollback refs stay intact.

New planning milestone (2026-10-30): the user requests a plan to protect the
remaining OAuth clients identified by the bounded coverage check: legacy PHP
WebUI, Czech/English DokuWiki KB and Discourse. Architect0 owns the concrete
source-backed plan in `oauth-client-log-protection-plan.md`, with parent
context-writing/acceptance. Include edge and backend request/error/application
logging, shared-server protection dependency, diagnostics tradeoffs, regression
checks and deployment/rollback order. React already has bounded callback
protection and is not a target for changes. This authorizes planning only;
implementation, production access/deployment, default integration and incident
response/old-log cleanup are not authorized by this request. Continue existing
default-spec verification and original dev update independently.

Active release milestone (2026-10-30): the user asks to use released HaveAPI
0.32 in vpsAdmin, prepare its `vpsadmin` channel update in
`vpsfree-cz-configuration`, and write deployment instructions that create the
documentation OAuth client beforehand. Existing development-cluster deployment
authorization remains; production configuration is preparation only. No default
integration, production activation or production client/secret provisioning is
authorized. Preserve the current aae/1b deployment and all recovery refs until
the released successor passes normal source/package/native checks and review.

Architect0 owns the exact release/content/compatibility and configuration brief;
implementer0 owns the complete released consumer update; implementer1 owns the
configuration channel, necessary credential-safe routing/hook prerequisites and
operator guide, binding its pin to the final published consumer head. Confirm
normal channel-to-input mapping and use confctl's channel operation. Operator
order is client registration, protected settings/stable session key, then
sign-in activation; preserve existing mail hooks and unrelated services.

User's additional guide request (2026-10-30): scope the deployment guide to
vpsFree.cz and include a concrete `vpsfreectl` OAuth2-client creation command,
client-secret generation with printed JSON configuration, and session-secret
generation. Architect0 verifies actual CLI/field/input behavior; E1 owns the
guide-only followup and offline synthetic checks, with lead context-writing pass.
Preserve the checked/published d002 configuration and its evidence. These are
operator instructions, not authorization to create production clients or keys.
This documentation milestone proceeds independently of the active dev update.

Completed KB addition: the initial client overview is restored in both articles
with local links to the detailed sections. The two lead-authored insertions
passed independent review and are staged as one additional logical revision per
language, with all16 links verified. The version policy and previous revision
history are preserved; no production KB publication occurred. See
[the overview staging receipt](kb-restructure/overview/staging/receipt.md).

Current documentation correction: omit optional API version selectors and stale
version literals from both KB articles, remove main-client ranking, and name the
dynamic and generated TypeScript clients by their behavior. Dynamic examples use
the configured server default; generated clients retain schema compatibility
requirements without copying a numeric API version. Lead owns bilingual prose;
E3 owns the additive06 revision, checks, review and staging. The user chose
vpsfreecz/dev-workspace as the authoritative home for the version rule. E2 owns
its existing writing skill; E1 adapts the old workspace feature to a pointer.
Existing routing applies the shared skill to KB and vpsAdmin. These docs-only
milestones require no runtime package switch or change to the reviewed0.32 target.

The released consumer includes both active generic JavaScript bundles from the
same published npm archive. Its isolated exporter permits only the tracked,
nonexecuted api.rb.example in addition to the existing safe inputs; live/private
configuration and symlink refusals remain. Production configuration uses explicit
API/auth HTTP redirect vhosts because this pinned nginx module omits scoped log
settings from automatic forceSSL redirects. Preserve existing redirect, TLS and
ACME behavior while protecting callback request/response values. These bounded
design corrections and checks are recorded in the existing release briefs.

Completed KB staging followup (2026-10-29): remove avoidable client versions from both
staged API articles, establish a general documentation rule against needless
version references, and investigate the old HTTP 500/User-Agent warning.
The user reiterates that logical changes must be separate wiki changesets,
not merely Git commits. Architect0 owns the technical findings and bounded
design; implementer1 owns the small workspace-instructions feature;
implementer3 owns the supported changeset/release preparation and staging;
the lead owns final bilingual prose. Acceptance requires accurate header and
installation guidance, maintained compatibility links, independently reviewed
committed changes, and verified logical staging revisions where supported.
No production publication, product update, default integration or lifecycle
operation is authorized. Existing development rollout remains complete.
The reviewed result is now staged as four Czech and three English logical
edits, with exact source/render/history checks and unchanged production:
[staging receipt](kb-restructure/install-policy/staging/receipt.md).
The general rule is independently reviewed and published on its workspace
feature branch, ready for merge approval:
[rule publication](documentation-version-policy/publication/receipt.md).

Completed dev milestone2026-10-29 (after accepted90e2/2f6 OAuth rollout): adopted and deployed published formatting-only HaveAPI `1b264e25a73a0ab9bca5f847bd52254f74e0931c`, tree `dcdba06a92fe0d8a577f4cffe46ea69fc8d73a40`, direct parent2f6, through a separate bounded consumer successor. Existing direct dev-deployment authorization below applies; peer handoff is evidence/coordination, not approval. Preserve working90e2/2f6 rollback/client3/3600/key/config and59d/8102 recovery. Architect verifies scope and writes the brief before implementation; final served checks target changed language-example formatting and actual deployed identity, reusing unchanged OAuth acceptance without a full repeat. No default/release/production/lifecycle action.
Final consumer aae07e629883133229a87d62c2ed34e4ce5030d5 is published and deployed. Independent affected review, full8/core8, new five/API package proof, all34services, actual installed lineage and20served-format checks passed; unchanged actual auth/proxy/private inputs bind prior OAuth acceptance. [Final served receipt](devcluster/m8-runtime/style-successor.md), [actual deployed lineage](package-style/vpsadmin/deployed-lineage/receipt.md). No dev rollout work remains; branches stay unmerged and session remains active/open.

Current followup: prepare and deploy the peer session's ready HaveAPI
documentation development revision into this session's HTTPS development
cluster for user testing. Direct user authorization on2026-10-28:
“well you should deploy the haveapi version from the other session into the dev
cluster when it will be ready”. This authorizes consumer preparation and the
development deployment with normal review/verification and rollback; do not ask
for another deployment confirmation. It does not authorize production/default
integration, a HaveAPI release or session lifecycle cleanup.

Architect0 owns the bounded design and verification brief in existing design.md.
The final development candidate is HaveAPI
`5114746f3a9f87e91c704147c0d99dd4f0d32f02`, tree
`5b9c52d0f0d81957bbca227d254e2e5b09b53373`; the initial e5ea M8 and d67
boundaries retain their actual package/test provenance. Follow
[the accepted final-pin brief](design.md#2026-10-29-final-m8-pin-511-and-bounded-verification-reuse).
Select all five sibling gems from this immutable source through ordinary
Bundler/bundix/Nix packaging, generate shared docs with `make doc`, and prove
actual final package/deployed identities. The final producer correction changes
only eight verification/test/doc paths, but whole-Git Nix inputs change and
require new actual five-output/package proof and all 34 services assertions.
Keep the separate TypeScript SDK0.1.1/runtime0.30.2 pairing unchanged. Prepare
normal protected documentation/OAuth inputs and bounded real HTTPS acceptance;
preserve the existing 0.31.2 source/config/closure rollback. Reuse prior evidence
only for its proven scope. No provider rewrite, new deployment framework,
automatic full matrix or unrelated dependency refresh.
The peer owns upstream HaveAPI fixes; report concrete redacted failures through
the authorized official communication channel.

Initial published M8 handoff (f784b2cd-c7a9-4f7b-9e23-1f252a3cb565, 2026-10-29 local)
selected e5ea07028e48a6936b947c172fa89eca15e3a416/tree543cd44c4a1863489ae2289d2a8769a60e7c1b85.
Its actual package and all 34 services checks passed; final511 supersedes selection
without relabelling those results. Preserve M6d67 actual package/29native-pass and
interrupted stale-oracle evidence at its reconciled safe boundary. Architect0
writes the smallest five-gem/consumer-assertion successor brief; A0 owns edits,
quick checks/history consolidation/review/package/services; E3/lead own the
existing protected OAuth and deployment acceptance. Prefer one final M8 activation;
no automatic producer campaign duplication or relabelling pending gates as passes.
Do not automatically select publishedM7 or relabel existing results. The existing
local dev-deployment approval governs our actions; peer messages are evidence
and coordination, not new approval. E3's dedicated docs OAuth client fixture and
protected configuration must be concrete and repeatable through ordinary API
administration. Final deployment notes must explicitly order client registration,
protected client/session secrets and before-mount configuration before enabling
sign-in, with the actual production callback host/provider metadata/scope/TLS and
switch_user false until verified SSO-off editable entry. Production execution,
default integration and release remain outside this task's authorization.
Peer clarification5353301e-7b0a-449c-93d0-27fa079fe8b3 identifies
`vpsfree-cz-configuration` as the owner of concrete production client-registration,
protected-config, deployment-order and operator notes. Follow that repository's
procedures when preparing its own documentation work; keep generic HaveAPI
setup in its owning guide and link it. This is a pending documentation destination,
not registration of a new source worktree or production mutation approval.

Completed KB followup: restore both KB articles to authentication/scopes, CLI and the
main Ruby client, then other supported clients. Remove haveapi-fs and prepare
separate logical publication changesets. The lead owns bilingual writing;
implementer3 owns the existing release tooling and staging after committed
independent review. See [the bounded brief](kb-restructure/brief.md) and
[the three publication changesets](kb-restructure/publication/README.md).
Production publication remains subject to explicit approval.

Update every HaveAPI server/client dependency in vpsadmin to released 0.31.2.
Configure API documentation examples for Go, Rust and the published TypeScript
SDK, preserving SDK0.1.1/exact npm runtime0.30.2. The released renderer remedy
is verified in the real consumer and the measured R1 scope is closed.
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

- All generic vpsadmin HaveAPI runtime pins and resolved metadata use 0.31.2;
  the separately published TypeScript client0.1.1 retains its exact runtime0.30.2.
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


## 2026-10-28 delivery disposition

Released0.31.1 adoption, source/history review, required checks and publication
are complete. User-authorized reset/redeployment passed; both real member
login/logout flows and generated documentation work on the retained running
cluster. Both KB articles are staged. See state.md and devcluster/e4-runtime/receipt.md.

Independent exact source/input/output proof establishes native Reacte468 despite
missing embedded Git revision metadata from the provider's path input. Qualified
manual development use is accepted; clean-release metadata and the installed
provider's complete retained-boot certificate remain explicit limitations, with
no provider repair/rebuild project. No default integration or production KB
publication is authorized. Session/cluster/staging stay open. E2 completed final integration CI monitoring
with exact9697 success at05:29:43UTC; all nine assigned workflows passed. Earlier plans and rollout facts below/above are
historical unless this final disposition retains them.


## HaveAPI 0.31.2 patch adoption — 2026-10-28

User requests upgrade to released0.31.2 containing the Go token documentation
fix. Actual release facts confirm only Go comparison/regressions plus coordinated
version metadata; TS renderer/runtime pairing and generic client runtime code
remain unchanged apart from version constants. Architect owns bounded brief;
A0/C1 own separate coherent successors preserving live0311, E3 KB mechanics and
qualified dev deployment, lead prose/coordination. C intentionally depends on
reviewed/deployed911/e468 source lineage rather than expanding this patch to
new main40653 product changes, under its explicit repository exception.

Acceptance includes actual adopted Go token example with the real automatic
profile boundary, correct package identities, scoped quick/review/checks, own
feature publication and supported dev deployment/source proof. Prior measured
TS remedy and valid client0.1.1/runtime0.30.2 pair are preserved. KB changes only
three generic version literals per language; no terminology regression. No
upstream source work/default integration/PR74 rewrite/production KB authority.


## KB publication preview — 2026-11-01

After the HaveAPI follow-up merges, the user asks to inspect the upcoming KB
edits and ensure logical publication steps. A0 owns the bounded consolidation
brief; E1 owns exact source freshness and local snapshot/diff preparation;
the lead owns contextual bilingual prose and the user preview. Preserve the
accepted KB08 final text unless an actual current-source discrepancy needs a
separate decision. Fold obsolete editorial iterations into a clean sequence
from observed production to the accepted final pages. Exact production approval
is still pending. No wiki write or staging reset/replay is needed to prepare
this initial preview. Retain all prior staged revisions and review evidence.
