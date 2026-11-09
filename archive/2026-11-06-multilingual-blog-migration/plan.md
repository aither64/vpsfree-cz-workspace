# 2026-11-06-multilingual-blog-migration

## Goal

I'd like to migrate https://blog.vpsfree.cz from wordpress to a static generator. We should preserve the design, it doesn't have to be 1:1 of course. We must however preserve all content (articles, authors and comments). Existing comments can be added statically, future comments should be provided by discourse that runs at https://discourse.vpsfree.cz. I assume this is supported by discourse? How would it be interconnected? We should also preserve existing article URLs. Both blog and discourse are configured using vpsfree-cz-configuration. I'll be able to give you access to the blog container so that you can extract data. In addition, I would like the blog to support localization in English and Czech, so all existing articles will have to be translated to English. Suggest what static website generator would be appropriate for our usecase and create a plan to implement it. Ask if something is unclear or I forgot to mention it.

## Current correction scope

### P37: remove the redundant receiver startup-generation comparison

User asked why the receiver needed a restart and whether later system upgrades
would repeat it, then challenged the check's usefulness. Source reassessment
found no demonstrated safety property uniquely provided by the cached generation
after root explicitly resumes the selected system under the same immutable
policy. The helper already checks CURRENT policy/system against root control
under transaction locking and enforces ordering. The first request-factory
proposal (design5874/bf37) is superseded; its proof is retained as investigation
history only. Final sufficient brief at design5995 removes only the startup cache
and historical-generation equality, keeping those current-state checks intact.

Owner0 final three-file package: tools/blog-static-release.py, existing actual
Handler/Publication tests and owning operations guide. tools/blog-upload.py must
return byte-exact25b2; no factory/restart hook/selfdependency/newstate/schema.
Tests distinguish pause/no-resume refusal from explicit same-policy resume
admitting new and body/staging-spanning conforming work, with truthful selected
system receipt and monotonic ordering floor; stale compiled policy still rejects.
Documentation must stop promising permanent cancellation after a later resume.
Lead owns finalprose/review/release. P36 corpus delivery stays independent.

P37 delivered: explicit follow-up merge/deploy approval executed. CONFIG0f389
and BLOG567 are merged into their remote defaults. Exact native0ndf installed,
verified and explicitly resumed; genuine normal Actions28 delivery through the
corrected receiver passed and final target receipt binds new system/policy.
All deployment reservations and repository claims released after verification.
No P37 remaining work; recovery data/roots remain intact, session open.

### P36: Czech typo proofreading and navigation separator

User explicitly asks fixing Passkey `technolgii`→`technologii` and merging, then
adds checking all Czech articles for typos and the missing separator in
`Články · RSS English`. Treat known correction+navigation as prompt independent
milestone, broader125-Czecharticle proofreading as read-all contextualaudit and
subsequentcoherentfixbatch. Englishprose translations are trusted/unmodified;
update only required honest sourcebinding/reviewmetadata for editedCzechfiles.
Preserve originalarticle dates/state/identity/URLs/GUIDs/HTML/code/linktargets/
media/author attribution/importprovenance/comments. Typosonly, no stylerenewal,
modernizingfacts/commands or unknown technical-term massreplacement. Lead
appliesuser-facingwritingguidance directly toacceptedcandidateexactworddiffs.

Owner1 handles knownPasskeyfix+necessarylegitimatebindingupdates/ordinarycommit.
Owner0 handles tinytemplate separator+focusedrealHugo check, disjointedit but
index/commitwindow afterowner1. Architect0 records conciseauditpartitions/brief
inexistingdesignEOF, then readonlyauditors owner0/2/3 cover allvisibleCSprose
with contextualfindings, not merelyHunspellunknowns. Leadacceptsproven corrections
before sourceapplication; auditors do not rewriteEnglish/style/code. Independent
finalcommittedreview/quickchecks precede exactmainpush/automaticActionspublication
withexistingarticleobserver. Usermergeapproval covers requestedBLOG corrections,
no CONFIG/system/forum changes or cleanup. Avoid redundantfullsite/native/
featureCI campaign for tinyreadyarticlepublication under existingauthoringrules.


P36 audit reconciliation: all125 unique tracked Czech article paths and report
baseline hashes verified. Lead directly read candidate contexts and accepted124
rows/126 occurrences across54 articles; exact selections in
`p36-czech-accepted-corrections.json`. Owner0 now has the sole implementation,
shared manifest/index/commit window. Retain quotes, attributed abstracts and
ambiguous meaning, including wp592 missing negation, as withheld observations;
this scope is spelling/obvious accidental typography, not historical prose
modernization. Original English bodies and human provenance remain untouched.
No project documentation change is useful for these literal corrections; the
existing author guide owns current-file versus raw-source bindings.

Immediate fixes already merged into main at ccf639 after clean final review.
Automatic MAIN25 built and retained its exact artifact, but delivery failed;
owner3 reconciles target root/floor and bounded rejection paths, owner1 binds
existing artifact and prepares supported deploy-job-only retry. No blind retry
or build rerun; machine hold remains until delivery effects are reconciled.

### P35: WordPress retirement — proposed removal plan, not executed

Inventory completed against freshly fetched clean CONFIGmaster/feature
4771ff84e56de349bdde71bc221c62ccd4190f1b/treeb6f1a48773a20927bec8dab78306bde5788a07af.
Architect0's detailed source inventory/line anchors and rollout rationale are in
[design.md P35](design.md#p35-wordpress-removal-inventory-and-proposed-plan--plan-only).
User requested a plan showing what will go; no implementation/deployment/purge.

Within CONFIG, let `S = cluster/cz.vpsfree/containers/int.blog/`.

| Disposition | Paths / effect |
| --- | --- |
| Delete68files | Entire `S/wordpress.nix` plus `S/packages/` (67trackedfiles: customWPderivation, policyPHP, Czechtranslation and64Flat-themefiles). This is site-local, solecallerwordpress.nix; no overlay/sharedpackage/pin update needed. |
| Remove installed WP runtime | WordPresscore/plugins/themes/translations, generatedWPvhost on8081, wp-blog/core DB updater, PHP-FPM, localMariaDB provisioning/service, cron/init/timer and WP-only SMTP restrictions. Scope is int.blog only. |
| Change3sitefiles | `S/config.nix`, `S/blog-routing.nix`, `S/module.nix`: remove import/serveStatic selector; enabletrue routes bothlanguages8080, enablefalse returns503. Move nginx enable/reload and exactproxy-onlyTCP80/firewall/assertions out of WPmodule. Replace WP/MySQL/PHPhealth with fixedHostCS+ENfrontendhealth. Keep inert account ownership declarations while data is retained. |
| Change3fixtures | `tests/blog-static-module.nix`, `tests/blog-upload-module.nix`, `tests/blog-legacy-module.nix`: assert no WP/PHP/MySQLruntime, correctstatic/503modes and retainedaccounts, unchangedfirewall/publisher/legacy behavior. |
| Change1CONFIGguide | `docs/operations/blog-static.md`: static-only/currentrecovery, orderedWP retirement and version-scoped oldsystem recovery. |
| Change1dependentBLOGguide | BLOG `docs/deployment.md`: replace current promise of serveStatic=false→WP fallback; no BLOGcode/corpus/client/workflow change. |

This is68deletions+7modifiedCONFIGpaths, one dependentBLOGdoc. Keep:

- Staticserving/upload/releasevalidator/retention/currentreceipts/floor, deployment
  key, services and publicproxy/TLS/Discourse unchanged.
- `legacy-routes.nix`/legacy-route data and all540aliases, feed/permalink
  compatibility, Hugo `static/wp-content/`569files/media/licenses/comments/bylines.
- SharedPHP/sessioncleanup/MySQLmodules and otherhosts; no unrelatedpackages.
- OldDB/site/uploads/fonts/secrets/backups and rootedoldsystems/UIDmaps. Preserve
  dormant wordpress/mysql users/groups with predecessoridentitymetadata to keep
  recovery-file ownership stable; norecursivechown/chmod/newdata tmpfiles.

Ordered future work after scope approval:

1. Implement coherentCONFIGcleanup and dependentDOCcorrection with ordinaryhooks.
   Transfer nginx/proxytrust/firewall first; retain exact idempotent teardown for
   the two old WP SMTP chains during firewallreload, never broadflush.
2. Run focusedreferences/format/modulefixtures; finalcommittedindependentreview
   then existing relevantpublisher/legacy tests and nativeint.blog-onlybuild/
   dryactivation/closureunitdiff. No fleetbuild/newpublisherbenchmark required.
3. Before laterdeployment, freshclaim/livebaseline/actualownership/unexpected
   consumers and independentDB/sitebackups/completepreviousstaticrelease. These
   are futurepreflightfacts; no liveprobe was needed to prepare thisplan.
4. Pausepublication, activate static-onlybackend with graceful nginxreload, check
   bothlanguages/feeds/media/redirects/hashidentity, retiredWP/PHP/MariaDBunits and
   absent8081/3306listeners, preserveddata/accounts/modes/current/floor; explicitly
   resume under newsystemidentity. No forumtopicseeding/crawling.
5. Recovery uses retainedstaticrelease/guardedrollback. Retainedcompatibleold
   schema2system+data remains deliberate historicalrecovery; newconfig cannot
   switch routing back to WP. Preserve existing schema/activation restrictions
   and verify oldMySQL0755tmpfiles never widen retained0700 on recovery.

No database migration/deletion. Persistent-data purge and eventual account/oldroot
removal are a separate explicitoperator decision after backup/retention review.
**Status: COMPLETE. User explicitly approved merge/deploy. CONFIGmaster25b2
and BLOGmain63e are merged and independently remote-proved. Actual int.blog
yyf2/compiled25b2 is deployed and publication resumed, serving genuineActions24.1
source63e. Independent live proof confirms no WordPress/PHP/MySQL runtime, all
2401 served files/current receipt/order, both public blogs and preserved data/
accounts/backups/oldroots. Claims released; no purge or lifecycle action. Exact
evidence and recovery directory are in currentstate and release-preparation.**

### P34: archived comment presentation and localized reply phrases

User requests removing all archived commenter-name links (name remains escaped
plain text), removing the original-comments untranslated notice, and translating
index Replies into the blog language. Preserve imported metadata and body HTML/
links/dates/IDs/thread relationships/comment anchors/article bylines. Commenter
website URLs remain in immutable data for provenance but are not rendered.

Settled design at design.md:5388: a small version-bound adapter recognizes exact
pinned native English/Czech integer reply phrases and formats the value for the
page language, leaving unknown/custom phrases as plain discussion links. Preserve
one bounded fixed-origin JSONP batch, shared English identity and local links.
No broader CORS, account/global locale/cookie change, numeric API, backend or zero
fabrication. Supported behavior/fallback live in BLOG docs/discussions.md.

Owner1 committed comments2979913 and count1e3082c7e24c1b341df5d859cc964c1797714294
above live/mainc900. Quick checks and normal hooks passed; retained reviewer0
completed final MEDIUM/allfour affected lanes with no findings, including full37
history/current unmerged two-commit range, no migrations/repeated update streams
and documentation placement. One full/native batch, immutable artifact proof and
ordinary feature publication/exact CI released to owner1. Prior native/Actions
artifacts remain distinct; no unsupported cross-build byte-equality assumption.
User subsequently answered "yes" to concrete reviewed publication. BLOGmain was
fast-forwarded/pushed normally to1e308; automatic Actions22.1/run42665721131
packaged/uploaded/deployed successfully and independent actualmanifest live
postverification passed. All P34 work complete; previous releases/roots/recovery
retained, repository/machine claims released, no CONFIG/forum/system change or
lifecycle cleanup. Current exact receipts/results live in state/release-preparation.

### P32: all-article discussions and integration

Accepted result: all-article embeds/counts live from genuine Actions20.1/c900;
BLOGmainc900, CONFIGmaster4771 and WEBmaster7fec merged with exact remote proof.
Independent review/checks/native/CI and live2401-file/250payload/1490marker proof
passed. All rollout/repository claims released, no remaining P32 operation.
web.int deployment remains user-owned, no cleanup requested. See state.md and
release-preparation.md for exact identities/recovery. Separately registered
workspace project-map branchc379 remains unintegrated/outside approved three-repo
merge scope, so initiative lifecycle stays active. The steps below record the
accepted P32 contract and its original preparation rationale.

Both-language browser pilots are accepted. User explicitly requests allowing
embedding from all articles and merging the current work. Prepare the smallest
BLOG opt-in and affected production-check correction, with the documented exact
host namespaces and shared English topic identity unchanged. Preserve every
preview/origin/draft/unlisted guard and all archived content. Use the existing
content release path, reviewed native output and fresh current-release guards;
retain operator17.1/985d and older recovery payloads. Widen only the two existing
host path rules through normal Discourse application semantics after the operation
is concrete and guarded; preserve Blog10/blank authors/mapping1/topic374 and all
other forum policy. No archive crawling, topic seeding or auth/notification changes.

User's merge instruction authorizes current BLOG→main and CONFIG→master; they
then explicitly approved WEB→master with "Merge WEB too". These merges follow
the retained switch-over/verification-first sequence and ordinary
current-default/independent-review/fast-forward/short-claim procedures. CONFIG
currently diverges from master; prepare reviewed lineage/rebase evidence before
integration, preserving all actual deployed source identities/refs/roots. WEB
deployment remains user-owned. Reconcile any wider integration prerequisite
without silently widening this three-repository/target set. No cleanup is requested.

The verified P29/P31 switchover and both browser pilots satisfy the earlier
verify-before-merge requirement. Use ONE normal protected-main Actions push as
the enabled-content publication boundary, after source review/checks/native/
featureCI and guarded host expansion. Its main-only environment has no reviewer
or wait timer, so do not assume a later manual delivery pause. No preliminary
operator upload is needed. Observe exact main-run artifact/upload selection and
verify the resulting live release; retain operator17.1/985d recovery unchanged.

Architect0 owns the sufficient P32 brief in design.md; owner1 implements BLOG
source/delivery from it, owner3 prepares CONFIG integration and host-write plan.
Lead owns operational release/integration, scope/approval records and writing.

### P31: live Discourse pilot preparation

Inert metadata delivery is now accepted: live985d release985d-55fba3cfd240b057,
operator-local real17.1, rootreceipt9e962749/floor17.1/RESUMED. Lead upload19.978s
and full private/public postverification12.119s passed; all2399files/2401entries,
aither metadata and sharedENsource matched. No agent forum request or global
opt-in change. The user confirms both English and Czech browser pilots work. The reported
CSP/X-Frame-Options console notice reflects normal frame-ancestors precedence. Native
anonymous delivery works from both parent referrers after the user's repair.
Backend76d7/w3 unchanged, prior
16.1/A66 recovery retained. See currentstate and release-preparation.md.


User reports Discourse deployed and pilot hosts set. Verify settings/host records
read-only through existing trusted access, distinguishing missing access from a
product defect. Deliver the accepted985d/ysy native BLOG artifact as operator-local
realCI17.1 with the unchanged authenticated client and fresh16.1 target guards;
keep global embedding/count opt-in false. This safely adds author metadata before
one shared-English pilot. No Actions-artifact, source/rebuild/temporaryworkflow,
forum setting/account/migration or default integration work. Exacttopic creation
and notifications are limited to the selected English pilot; authenticated login/
inline replies require the user's browser. Preserve old content/roots/receipts,
monotonic order and existing maintenance/recovery contracts. Separate read-only
proof, prepared upload, lead-owned mutation and operator browser evidence.

The initial forum SSH authentication refusal was superseded by user-confirmed
root access. Targeted READ ONLY queries found imported topic374 in nonexistent
category-1 despite both host rows selecting public Blog10: the slash-required
path rule failed after native URL normalization. The user corrected both exact
pilot rules to optional terminal slash and moved the existing topic into Blog10,
preserving mapping1 and unlisted state. No agent authored a forum write.
Published source guidance must match both canonical and normalized paths while
preserving reserved namespaces. Owner1's bounded correction620f14c adds the
corrected guide and72-line native Ruby regression above consumed985d. Focused
checks/hooks and retained reviewer0 affected all4 final review passed with no
findings. Ordinary feature FF985d→620f is published with defaultmain unchanged;
exact automaticCI42635047506/#18/attempt1 passed, buildsuccess/deployskipped/
artifacts0. Correction source is ready, awaiting merge approval; it has not
replaced the live985d/operator17.1 package.
No new dependency, client/corpus, global-enable, forum or native build scope.

### P30: Discourse comments and per-author metadata

Final source preparation accepted/published: BLOG985d4eaa74309b219a762dcc02316df4a350065d
and CONFIG0488276abb1c80bb8c13ce45e75cd9ab2bd2fe92. Independent review, scoped
checks, native builds and exact BLOG CI42613369754/#17 passed. Default branches
unchanged; comments/count opt-in remains off. Source and native settings are not
a live forum deployment. Next are Discourse configuration activation, effective
settings/account/host/category checks and a two-domain inline-reply pilot; then a
reviewed enablement release also updates the currently disabled-output production
assertions. All original payloads/roots/refs/services remain, no cleanup or merge.
Current operator steps: [setup checklist](p30-remaining-operator-setup.md).


User requests native comments setup and per-author metadata instead of host-wide
Post author override. Implement truthful article author names and explicit forum
username mapping without changing original author/article data or bylines. Confirmed
current mappings: Jakub Skokan→aither, Pavel Šnajdr→snajpa, Petr Krčmář→krcmar,
Martin Myška→martyet (one article). Michal Janoušek→KerryCZE is retained for future
use only because he has no existing author record; do not invent a new author or
reattribute articles. Remaining authors use the forum's normal configured admin
fallback with host Post author blank. Lowercase forum usernames for the pinned
username_lower lookup. Use a separate optional small map to preserve immutable
original byline projections. Emit all truthful names, select no arbitrary forum
owner for a future multi-author article, and avoid falling back to matching a
public display name accidentally. No identity lookup/API/account service needed.
Architect0 records compact brief, owner1 implements and checks the small package;
lead owns user-facing prose, final review/acceptance and delivery coordination.

Index byline counts currently cover only static legacy comments. User prefers
removing them if adding Discourse counts is too slow. Pinned native /embed/count
supports one public batch request but returns localized forum-reply strings, not
a combined archive total. User explicitly chose labelled Discourse reply counts. Prepare the smallest
one-batch client with exact shared Czech discussion identity on both languages,
truthful forum-only labels, nonblocking fallback and no topic-creation requests.
No new backend/poller/APIkey. Preserve metadata as its own coherent milestone;
count code follows a compact architect brief and owner1 implementation/review.
The user has not touched the listed forum settings, so no override repair is planned.

User explicitly chose full-app embedding for inline replies from both blog
origins, superseding the initial read-only embed implementation choice. Use native
Discourse fullApp/client/site-setting support only, preserve restricted origins,
no custom login/cookie workaround. Later operator pilot must verify login and
posting from both domains; source checks cannot prove cross-site browser auth.
Amend the unpublished owning P30 mode/settings commits after active original
builds join, preserving predecessor evidence under its actual false-mode identity.

User additionally requests declarative embedding/site settings on the Discourse
system in CONFIG where the existing Nix module supports them. Architect verifies
setting ownership and mutable override behavior; hosts/category/user records stay
UI-owned unless an existing appropriate declarative interface is established. No
custom host provisioner or database migration; deployment and merge remain separate.

User subsequently prefers the ENGLISH article URL as the shared discussion
identity after learning it can appear in the forum imported-from link and supplies
the opening-post language. Both blogs must use one actual English canonical for
embedding/counts, with English import-host rules and Czech framing-only. Preserve
all imported Czech metadata and public article URLs; derive counterpart identity
rather than duplicating125 source overrides. Reconcile any existing topic mappings
before live enable, but no topic migration/reimport is authorized. Forum
operator configures hosts, article-body extraction, visibility and category/author
fallback, reconciles any existing TopicEmbed/RSS sources, then tests one published
article on both origins before a reviewed blog opt-in. Metadata work does not enable
the embed or authorize forum topic creation by automated checks. Existing merge
boundary, archive comments and draft/unlisted exclusion remain intact.

### P29: BLOG-only switch-over completed and verified

The user authorized switch-over before merging, then explicitly limited deployment
to the blog and reserved web.int deployment for themselves. The latest reviewed
BLOGa24 is now selected on both public hosts. One unchanged authenticated upload
used operator-local packaging from the accepted sfvx native artifact with genuine
CI42594078633/#16/attempt1 identity; no Actions artifact or main workflow exception
was invented. Existing CONFIG76d7/w3 already supplied the required receiver, so no
backend/proxy activation was needed. All2399 selected file hashes, complete declared
set/input/archive identity,23 private and24 normal-CA public observations passed
with stable current receipt/floor16.1/policy/system/RESUMED brackets. WP, MySQL,
retention, previous A66 recovery and protected backups remain intact.

Web work stopped without a remote target effect. Its unused claim was released;
failed SSH trust and invalid local candidate evidence remain as limits, with no
repair or further investigation. All handles are joined and implementers parked.
The existing BLOG claim remains held for the unmerged deployed lineage. No merge,
cleanup, lifecycle action, protocol/settings change or forum work is authorized.
See [accepted rollout](release-preparation.md) and [final proof](p29-blog-final-proof.json).
Next: user-owned web deployment later; repository integration only on explicit
named direction. The initiative remains active while feature branches are unmerged.

### P28: accurate CONFIG upload history and rollout ordering

User reaffirms switch over and verify before merging. This supplies sequencing,
not immediate default-branch integration. Existing static A66/P25 is already live;
new P26/P27 feature output remains not deployed. User points out CONFIG commit
"blog: replace notification pulls with authenticated release uploads" has no
ancestor adding pulls, and says unused notification-pull history need not remain.
Actual parent8a4 has publication uninstalled/no pull implementation: the abandoned
approach is already absent, but10e66 commit wording is stale. Correct only its
message to "blog: add authenticated release uploads", with final implementation
rationale; preserve every source blob/patch and original deployed revision refs.
Replayed feature descendants get new IDs; never relabel actual deployment/source/
NAR evidence. Owner3 receives bounded reword task2705da72, normalhooks/recoveryrefs/
exact per-commit tree and patch proof, independent full-history review before
lease-guarded feature publication. No runtime/build/sourcepin/default action.


### P27: draft, unlisted and published articles

User approved implementing the three states after discussing Hugo drafts and
unlisted review links. Drafts remain excluded from production and available in
preview. Unlisted review articles render at normal direct URLs but are excluded
from homepage, archives, feeds, search and sitemap, marked noindex and visibly
in review. They are public to anyone with/discovering the URL and in Git; no
access-control service is requested. Published articles use normal discovery.
Preserve URLs through review/publication and settle publication-date semantics
against existing immutable source/audit requirements. Both languages share state;
update authoring skill/checks/observer and tests. Existing imported content keeps
current behavior without bulk metadata migration. BLOG-only package; no CONFIG,
proxy, authentication, runtime or existing no-merge boundary change.
Architect0 owns sufficient design; owner1 will retain dependent BLOG source after
brief acceptance, MAIN owns prose pass, independent committed review precedes
long verification. Normal feature publication/CI, no live article publication.


### User-queued work after retention and public cutover

User explicitly says "further work when you're done"; preserve this sequence.
Do not let it delay the current P25 review/build/deployment boundary.

- Restore the static blog favicon using the same favicon as old WordPress;
  retained WP on8081 remains available for read-only comparison after cutover.
- Update the English-blog link on vpsfree.org in `vpsfreecz/web`, then update the
  corresponding `web` channel input in CONFIG via ordinary confctl channel tools.
- Ensure `vpsfreecz/blog` is included in `aither64/vpsfree-cz-workspace`
  instructions/project guidance; inspect existing entry before adding one.
- Correct the article title "Dvoufaktorové přihlášování s passkey" to use
  "přihlašování"; preserve its published URL/identity and paired translations.
- Create a reliable authoring process in the BLOG authoring skill/docs/checks:
  write article/select title, automatically correct typos, automatically provide
  missing Czech or English translation using consistent rules from the archive
  translations; state all required metadata; optional local preview; commit
  checks must verify both currently supported languages, spelling and metadata;
  non-draft publication should push directly to main instead of a routine
  feature-build cycle, drafts/preparation belong on a feature branch; watch the
  resulting workflow and report success/failure to the user. Investigate whether
  public workflow observation needs gh authentication; when unavailable, consider
  observing the public site for the exact new article within a reasonable timeout,
  honestly distinguishing observed publication from unavailable CI conclusions.

Future design must bind these requirements to actual repository commands,
hooks, validation, preserved URLs/metadata, credentials and current environment.
It must replace contradictory existing authoring requirements rather than add
parallel flows. No speculative service/framework or credentials in docs.
User's desired future authoring publication flow is not a blanket instruction
to merge this entire migration now; current "no merge yet" remains in force until
named integration direction is explicit. New affected project/pin/deployment
scope must follow its own current procedures, review and approval boundaries.

New retention requirement: old release directories and archives must be pruned
under a bounded policy (default five newest completed plus current/recovery/floor
references); preserve audit/control/order/current media/CSS. Daily independent
best-effort cleanup, both existing locks in safe order, no post-upload coupling.
User clarified deployment may wait for prune locks but must never fail solely
because pruning holds them. Keep existing blocking deploy locks, prune skip busy,
short metadata retirement under locks and bulk deletion afterward. Architect
records sufficient design; owner3 owns dependent CONFIG source/meaningful checks/
review/native/final deployment, combined with static cutover. No manual deletion
or unrelated backup/root/ref/session cleanup. Current Actions-delivered content
fully verified privately; public WordPress remains until final generation.
Sufficient retention brief design.md3873 accepted; owner3 source/check/commit
released, native/live deletion held for independent review.

User requires a real visible Actions upload before static cutover. Temporarily
permit only the exact feature push through existing workflow packaging/artifact/
upload gates and environment branch policy, then restore main-only behavior;
no main merge or protection change. Current operator upload is not sufficient
Actions-delivery proof. New genuine workflow run/artifact/selected source/order
must be independently bound; public WordPress stays until success. This explicit
user choice supersedes the initial operator-only delivery path for acceptance.

P22 operator-local feature delivery is accepted: durable selected e1bb release,
2397 exact served files, PAUSED/public WP retained. Owner3 now prepares only
backend serveStatic=true with quick/commit/mandatory review before native switch;
no second proxy deployment or main merge. Recovery and guarded MySQL0700 remain.
P23 removes private development-host/workspace details from README/public docs;
committed5d9 docs-only changes independently reviewed with no findings, owner1
owns feature adoption/publication. Actual deployed site retains e1bb/bi18 identity.

User now explicitly says no merge yet; deploy from the feature branch. This
declines the prior named integration request for now. CONFIG feature16496060 is
the proxy/backend deployment source; no default branch mutation or workflow
main-only bypass. Protected-main automatic delivery remains separate later work.

P22 rollout direction: user confirms blog.int access, will perform one proxy.prg
deployment when given the prepared command, and delegates the backend transition
to the team. Owner3 starts read-only access/key/live preflight; architect records
the bounded live rollout brief before enabled source edits. User explicitly
allows normal nginx reload/restart, superseding the strict prior no-restart
condition. Preserve other proxy sites and verify health/recovery; one user proxy
activation remains planned. No default integration approval or extra host scope
is inferred. GitHub secrets/settings and Discourse UI remain user-owned.

Operator chooses direct pushes into protected `main`: keep force-push/deletion
protection without required pre-update status checks. Checks and build run after
push; deployment job depends on successful build. User confirms that rule is
saved and the environment deployment secret is set. This does not authorize this
session to integrate its feature branch or deploy systems. Target key permissions
and live access remain unverified.

P21 source/local delivery is complete and accepted at CONFIG
`10e66efdffc586bdec8af82b3d0e17df59bee2d7` and BLOG
`e1bb2d2b43aeb7361ac72c4c565919f38daabb65`. Independent review findings were
fixed and directly checked; final native systems, source/input graphs, blog
artifact and full-size private HTTPS upload/retry/order/distinct rollback were
verified. Both exact feature heads are published; defaults unchanged. Exact
BLOG CI42502157095 passed checks/release checks/Nix build, with main packaging,
artifact upload and deploy skipped. No production or default integration follows.
Keep the interactive next step to one deployment key on blog.int and the
matching main-restricted Actions environment secret, then approved live
preflight/deployment. Complete evidence remains linked from state and runbook.

Accepted P21 implementation direction ("ok, well, proceed with implementation"):
Actions builds the site and uploads its release package over authenticated HTTPS
through the proxy
to blog.int, which validates and reports staging/activation success or failure
synchronously. User explicitly requires a deployment secret. Replace
PAT/API-pull/webhook delivery while retaining visible CI failures, the existing
package validator and publication maintenance/rollback controls. The protected-main
workflow holding the deployment secret is the chosen release authority; target
GitHub API checks are removed with the old delivery mechanism. The exact upload
endpoint gets 512 MiB at both proxy and backend; other request limits remain.
Architect0 owns the accepted design checkpoint; implementer3 owns both repos,
quick checks, docs, commits, fixes and dependent post-review verification. Main
lead owns final review invocation and prose refinement. No live deployment or
default integration is authorized by implementation direction. Secret values
stay outside chat and source. Earlier PAT/webhook setup instructions are superseded.

User approved the simpler routing rework ("yup, let's rework it"): both public
proxy domains forward to blog.int:80; WordPress/static cutover, rollback and
webhook routing belong on blog.int. Proxy changes should be limited to the
English hostname/certificate/ordinary forwarding, with one planned deployment.
User subsequently clarified that both proxy vhosts must be unconditional:
remove the temporary English enable option, and let backend 503 indicate that
English is not ready. No proxy feature toggle is needed.
P20 design and affected implementation/review/checks supersede readiness of the
previous port80/8080 proxy-cutover layout. Retain Actions-built artifacts,
WordPress recovery and all publication safety contracts. No live changes or
default-branch integration are authorized by this source rework.

User now delegates actual blog.int/proxy.prg configuration deployments to team once access is provided, while retaining tokens/GitHubhooks and Discourse UI. Preserve availability of all other proxy sites: no nginx shutdown/restart; only validated graceful reload/configuration switches. Investigate actual pinned switch/restart triggers and compare live target before execution. No Discourse declarativejob, extra target or defaultintegration approval inferred. Earlier “user performs all deployments” boundary is superseded for these two targets only.

Retain Actions-built artifacts: user reconsidered building on blog.int and explicitly chose CI build visibility as the reason to keep the current delivery model. No local-build architecture change is requested. Continue interactive operator rollout; distinguish visible CI build failures from target-side delivery/publication status.

Operator interaction: use chat to guide one small rollout step at a time. Keep the full plan and completed/pending evidence internally; do not require the user to read the long runbook. Give concrete commands or settings for the current step, then use the result to choose the next. Team performs approved machine operations after access; the user handles tokens,
GitHub settings and Discourse UI. The user may choose to perform the single
proxy deployment. Secret values never enter chat.

The routing rework is reviewed, locally verified and feature-published at
CONFIG `011151f978eae435e1357ca00611726dbf501943` and BLOG
`7b0f3286ee11737e894f022bde0fce742a8a572d`. Exact BLOG CI42470233945 succeeded;
CONFIG has no applicable feature-push CI. Both native outputs are valid and
explicitly rooted after the documented exact-derivation recovery; the original
confctl output gap remains separately recorded without an invented cause.
All2397 served files equal the accepted BLOG82a artifact. Registered real-nginx
routing passed73 requests, including relative directory redirects and the hook.
Default branches and production WordPress are unchanged. The complete internal
rollout/evidence record is [release-preparation.md](release-preparation.md);
the user receives small concrete steps through chat. Access/live baseline,
credentials/GitHub/Discourse UI, eligible protected-main delivery and cutover
remain future operations. No merge approval is inferred. Session stays active,
unmerged and open with all previews, roots and recovery references retained.

Earlier P18 scope expansion: user directed “well then finish whatever is missing so that we can deploy it”. Prepare missing deployable SOURCE, including admitted activation/rollback and automatic delivery, English TLS/vhost/legacy aliases and Discourse readiness, then user-run rollout plan. Architect0 P18 is settling bounded sufficient implementation briefs; no safety/admission bypass or unsupported live mutation. User retains deployment/live setup execution; no default integration approval is implied. E18/B18 current source windows continue, broad final artifact stays held until final intended source/review.

User accepts all current English translations as reviewed; apply truthful maintainer-approval records, current paired Czech whole-file hashes and production-eligible draft=false without changing prose. Owner3 owns bounded E18.

After current modifications, deliver a production rollout plan including webhook and Discourse. User will execute deployments; team prepares only. Do not infer default integration or production/admin mutations. Explicitly expose the unfinished activation/rollback driver as prerequisite work. Verify user's statement that English DNS should already be set up (owner2 bounded public/internal/TLS facts).

Latest UI addition: remove the finite rack-background cutoff during long scrolling.
Use the existing appearance, preferably a seamless repeatable presentation tile,
with local deterministic asset processing and minimal CSS. Preserve original
WordPress media and content/hash contracts. Architect0 owns D18; source owner and
review/build/focused visual verification follow its sufficient brief.


Latest addition: the user requests production-only Piwik tracking. Czech blog
keeps site4; user supplied English-blog siteID10. Production guard, per-language IDs4/10 and preview/fixture exclusion are now
committed/reviewed/built/runtime-verified/published at6dae with passing CI.
The UI failure was confirmed by the user as uBlock Origin, not a DNS fix request.
Inspect the actual backend and supported user-recovery method only through
trusted admin access; do not guess/reset an account or expose hashes/secrets.
O17 stopped before authentication; further access recovery is no longer needed
for the now-supplied English site ID.
No analytics admin/site creation or password change has been performed.


Keep search input and button on one line, and use readable
`YYYY-MM-DD-english-title` article bundles. Preserve immutable article identity,
translation pairing, public paths, source bytes, feeds and discussion contracts.
Those source changes are complete; current source review/build receipts remain
scoped to their exact revisions.

The user superseded immediate WordPress retirement with a staged transition:
keep WordPress active, prepare/deploy the coexistence system, test the actual
GitHub build/artifact delivery and generated site, then approve public cutover.
Restore initial active WordPress/PHP/MariaDB/cron/packages/health checks; preserve
all data, owners and recovery generation. Remove the unpublished retirement
approach from final history while retaining recovery refs and its scoped evidence.
No default integration or public cutover is inferred from this planning direction.

The user selects a webhook rather than periodic polling: GitHub notifies an
HTTPS endpoint through the existing proxy after successful workflow completion;
the private host authenticates the request and fetches/verifies artifacts using
outbound HTTPS. No inbound SSH is required. Architect0 owns the sufficient D15
receiver/proxy/systemd/staging/admission/recovery brief. Implement only settled
interfaces, preserve the existing public-pointer admission fence and distinguish
safe immutable preparation from activation. No speculative new framework or
manual-pointer bypass. Exact protected-main real artifact tests, credentials,
network reachability, installed admission and cutover remain explicit gates.

Production-only analytics is complete in source at6dae: Czech4/English10, omitted
from all preview/server/fixtures. The existingWordPress tracker remains unchanged.
[State](state.md) owns the single package table, exact heads and current evidence.

## Affected repositories

- User-created `git@github.com:vpsfreecz/blog.git` for content, templates, assets
  and build contract. Remote was initially empty; user approved one-time main initialization from
  reviewed0354dac. All subsequent work stays on the feature branch; no merges.
- `vpsfree-cz-configuration`: existing blog hosting, static artifact selection and
  Discourse embedding configuration. Inspect canonical refs only during planning.
- This workspace: session tracking plus user-requested minimal blog entry in
  docs/agent-instructions/projects.md; feature edit uses an isolated workspace
  worktree. User originally named vpsfreecz/dev-workspace then confirmed the
  workspace project map after receiving its exact link; no duplicate extension
  project list is requested.

## Approach

Planning is accepted and the user has supplied root container access, the blog
repository, an internal DNS request and the English domain. Proceed with source
inventory, repository preparation/scaffolding under the accepted design brief,
and a minimal internal DNS feature change. User additionally requires standalone
agent/human author instructions inside the blog clone and a VPN preview on
port4567. Add those as separate small delivery milestones. Production cutover, forum writes
and further default-branch integration remain prohibited until user approval. The design owner maintains
[design.md](design.md).

Plan agent-assisted publishing as the expected workflow: repository instructions
and a focused authoring skill covering drafts, technical fact verification,
translations, checks and previews. Provide direct documented commands for human
authors too. Previews must not create or modify production Discourse topics;
future session-owned preview servers use `dev-session service run`.

Recommend Hugo on the verified multilingual and static-hosting evidence. Preserve
Czech article paths exactly at `https://blog.vpsfree.cz/`; English uses
`https://blog.vpsfree.org/` at the host root, replacing the initial `/en/` proposal.
Use durable WordPress IDs for provenance and paired translations. Revise the
discussion recommendation to native automatic URL-based Discourse embedding:
both language versions pass one stable original article URL as discussion
identity, separate from their language-specific SEO canonicals. Loading the
production embed can create the topic before anyone replies. Previews disable
production embeds. Archive original public comments statically.

User follow-up asks for zero manual forum work and site-only deployment on push.
Recommend a GitHub Actions publication pipeline independent of system deployment:
build/check Hugo in the pinned environment, transfer a versioned artifact to the
existing VPS, validate it and atomically select it for nginx. confctl manages the
hosting infrastructure and deployment permissions; it does not need to run for
each article. Runner access to the internal backend is an implementation gate;
use VPS-side artifact retrieval if a suitable restricted upload route is absent.

Use the supplied root SSH access for authoritative read-only source inventory;
public samples cannot establish completeness. Preserve source backups
privately in durable operator-managed storage independent of disposable session
artifacts, and generate a public-only projection suitable for Git. Rehearse a
repeatable migration, compare inventories, review English translations, validate
the candidate and prepare reversible deployment before any production switch.

## Decisions

Confirmed by the user in this conversation on 2026-11-06:

- Czech and English versions share one Discourse discussion per article.
- Future commenters use Discourse's existing account/login/registration rules.
- Future article publication should need no manual Discourse topic provisioning.
- Git/Markdown publishing is suitable; a browser editor is unnecessary.
- AI translation drafts are acceptable with human review before publication.
- Translations, particularly articles by Jakub Skokan/aither, should follow the
  language of his earlier announcements. The user permits adopting that general
  style across authors; preserve each author's attribution, facts and viewpoint.
  Reference collections:
  https://lists.vpsfree.cz/mailman3/hyperkitty/list/news-list@lists.vpsfree.cz/latest
  and https://discourse.vpsfree.cz/c/announcements/5 .
- Historical reader comments stay in their original language.
- Future articles will normally be written with agents; authoring instructions
  and skills should streamline that workflow and remain human-friendly.
- An easy local preview server is required.
- A dedicated content Git repository is acceptable, and has now been created.
- Standalone root AGENTS.md, local author guide and optional readable skill must
  let generic agents/humans work from an ordinary clone without this coordination
  workspace. Git permissions/protected publication branch govern publishing.
- When this batch is ready, leave a registered preview reachable through VPN on
  aitherdev.int.vpsfree.cz:4567. No firewall change requested. Real draft preview
  is the default; isolated synthetic fixtures are an explicit demo option.
- The new static website will run on the current blog VPS/container.
- User explicitly waives a formal content/comment freeze because posting is
  rare. Use the captured snapshot and one brief pre-switch check for deltas;
  refresh export only if changes are found. No service stop/read-only WP change.
- The bot may also be updated if needed. User subsequently confirmed feed
  subscriber continuity matters: preserve `/feed/` and stable existing item
  identities. An English feed can be separate.

Hugo and the blog repository are settled. Czech remains on `blog.vpsfree.cz`;
English uses `blog.vpsfree.org`, with language-specific canonicals/hreflang and
shared Czech discussion identities. Future public .org DNS, TLS/proxy and
cross-site forum display/login checks are required. Add `blog.int.vpsfree.cz`
A record for the verified container address to the internal zone. Blog category
and translation-review ownership remain to settle. Default integration and
production blog cutover have not been approved.

## Compatibility and deployment

- Preserve published article URLs, author attribution, original dates, content,
  media and historical comment IDs/threading. Inventory pages, archives, feeds,
  attachments, query URLs and redirects rather than assuming article paths are
  the only public contract.
- Preserve unpublished/private/spam content in private backups without publishing
  it. Do not publish commenter email/IP data, credentials or database dumps.
- Native auto-creation uses one stable production discussion URL shared by both
  languages. It occurs when the production comments embed loads, not only when
  someone posts. Site builds/previews must not activate production embeds, and
  the installed forum must be tested for duplicate-free shared URL behavior.
- Recommend a dedicated public Blog category, selected once on the embedding
  host record. Restrict normal automatic article imports to exact
  `blog.vpsfree.cz` and anchored published-article paths, with narrow category
  creation/reply permissions under the existing account rules. The native
  restriction validates the article source URL, not an authenticated caller:
  anyone may trigger import of an allowed public article. Do not promise Origin
  or Referer is authentication. Validate source/redirect handling on the actual
  installed forum before enabling; the current upstream review is bounded.
- Site releases live in versioned persistent directories with an atomic current
  pointer and a retained previous artifact. CI uses deployment-only permissions;
  protected publication-branch pushes trigger releases, PR checks get no deploy
  secrets. Serialize activation and reject stale releases. Keep artifact/source
  identities in release receipts. System-generation rollback and content-release
  rollback are separate; preserve both recovery contracts and asset compatibility.
- Prepare static serving on the same VPS alongside retained WordPress data.
  Keep the public TLS proxy and proxy-only backend network boundary. Preserve
  `/feed/` for feed subscribers; updating the existing IRC bot's configuration
  is explicitly permitted where needed. Verify feed GUID/polling behavior
  to avoid re-announcing the archive. Inventory verified original CZ identifiers
  https://blog.vpsfree.cz/?p=<id> with isPermaLink=false; preserve them exactly.
  English /feed/ uses stable language-specific URNs, original publication dates
  and reviewed variants only. Replace WordPress-specific health
  checks with static-serving checks. Do the brief pre-switch delta check,
  refresh export only if necessary, validate and switch atomically. Rollback
  retains new Discourse replies and discussion identities; preserve access to
  those replies without requiring them to be imported back into WordPress.
- No cross-service schema/protocol changes are proposed; no node-wide upgrade is
  expected. Nix module/options and deployed versions remain to verify.

## Documentation

### Translation voice brief

Lead inspected the supplied mailing-list collection and aither's bilingual
[primary DNS announcement](https://discourse.vpsfree.cz/t/primarni-dns-servery-primary-dns-servers/258)
and [initial VPS configuration announcement](https://discourse.vpsfree.cz/t/prvotni-konfigurace-vps-skriptem-cloud-init-a-nixos-initial-vps-configuration-with-script-cloud-init-and-nixos/317).
The general category also contains other authors; identify bylines before using
a post as an aither-specific sample. The mailing-list Guix announcement adds a
longer personal technical example. This is a small evidence sample, not a full
voice analysis of every article.

For the future authoring instructions/skill, use direct, practical English with
familiar technical terms and short purposeful paragraphs. Lead with what is
available or what happened, then explain use, reasons and concrete limitations.
Use examples and headings when the source needs them. Address the reader
naturally; retain first-person experience and occasional informal asides where
they exist in the source. Avoid promotional language, artificial enthusiasm and
generic filler. Match the voice without reproducing spelling mistakes or
awkward English. Do not add opinions, jokes, personal experiences, promises or
new technical claims to imitate personality. Preserve chronology, uncertainty,
authorship, commands and links. Leave the original Czech archive unchanged.
Human review checks both source fidelity and voice before publication.

The standalone authoring skill and guide now carry this guidance; later source
reconciliation documents native imported HTML alongside new Markdown.
Apply the vpsfree-user-facing-writing workflow after technical facts are settled,
using the supplied author samples to calibrate the prose.

Readers: blog maintainers, translators and operators. Session design and state
hold this proposal and evidence. Future source repository docs should explain
authoring/translations/import provenance; configuration repository docs should
own repeatable deployment and recovery instructions.

Use the dev-session-documentation and dev-session-handoff skills. Planning and
investigation alone do not trigger mandatory final change review. Implemented
code/configuration and completed substantive operating docs will require that
review after commits and quick checks, before long integration tests.

## Testing plan

Initial planning verified primary Hugo/Discourse/WordPress documentation and
bounded public/configuration samples. Accepted private snapshot evidence later
established the complete corpus; final source checks/review are in state.md.
Installed forum/runtime compatibility remains separately unverified.

For implementation, require ID/count/content and media reconciliation, all old
article URL checks and comment anchors, local links/assets, localized metadata
and translation completeness, representative mobile/desktop rendering, and a
staged Discourse lifecycle test proving shared topic identity and reply behavior.
Rehearse cutover/rollback, use the brief delta check agreed with the user, and
preserve post-cutover forum replies.

## Current implementation milestone after visual feedback

User rejected the generic scaffold. Rebuild from actual original design: navy
sidebar#16273f, serverphoto background#1f3959,230x90logo, Arial/Verdana,
1200desktopcanvas/300sidebar/900main, centered48pxheadings and measuredmobile
menu/layout. D6contains exact metrics and actual screenshots. Theme asset/code
provenance retained; do not invent font/media license claims.

Import snapshot locally to native Hugo index.cs.html bundles preserving visible
content, rawbody provenance hashes, code/media/moreanchors,125routes/GUIDs,6authors,
107approvedcomments/43threads,569uploads bytes andtaxonomies. Private metadata
remains outsideGit. English translation batches62/63articles are proposed by
wordcount were released against a stable sanitizedCSsource/manifest. All125
complete English drafts are now committed and source-hash/raw-code checked,
with main prose checks and independent source review complete. They remain
drafts awaiting human review, visible in preview with a clear label.

Blog initial main0354dac is user-authorized and verified; no furtherdefault
updates/merges and no transition/currentblog changes until separate approval.


## Reviewed source preparation and remaining activation gates

Recognizable original theme, complete public Czech archive/comments/assets,
125 English drafts, standalone author instructions, local/VPN previews and
production-disabled native Discourse rendering are implemented. Reviewed blog
feature head is aeed3a018d895b797e1b8d9b2863dd20c0dec8e0; source checks and
independent high-risk four-lane review found no issues in the source-preparation
boundary. Translation human approval and user visual acceptance remain distinct.

The independent release source candidate uses Actions builds and target-side
artifact acquisition, preserving current WordPress80 and a separate default-off
static8080 module. Artifacts require clean exact source identity, complete payload
hashes and independently verified trusted workflow/API identity. Current/previous
archives/assets/receipts remain locally retained; expired current-SHA artifacts
require the same-source trusted rebuild, never an older fallback or a VPS build.

Automatic pull/activation/rollback remains unavailable pending an implemented,
verified machine-coordination admission contract. The source CLI refuses and
timer enablement fails evaluation; filesystem fixtures do not replace ownership.
Current protected-branch/workflow credentials, outbound artifact reachability,
retained backup and actual forum/topic/account/frame behavior remain operator
gates. No forum setup, public.org DNS/TLS/proxy change, queryalias cutover or
transition is executed here. The user forbids merges until the last step and
requires explicit approval before touching the current blog.


## User refinements after preview acceptance

Center pagination and article images/tables. English gets a translated registration
CTA using the existing visual identity and the correct vpsfree.org registration
link. Audit all English drafts for repeated phrases, particularly repetition between
the index teaser and the opening body paragraph; preserve facts, original author
voice, source technical material, routes and immutable identities. Czech archive
bytes remain unchanged. Apply contextual writing checks before commits.

Explain static search using a generated index searched in the browser; current
search is disabled. The question alone does not allocate a search implementation.
No merges, production WordPress changes or transition are authorized by this
refinement. Keep the existing VPN preview open and verify actual rendered changes.


## Pagefind search and mobile navigation follow-up

The user explicitly requested Pagefind implementation after the earlier static
search explanation. Add local static search with separate language results,
published-only production indexing and useful current draft-preview behavior.
Pin the tool through the existing build environment; include every search asset
in normal hash/release proofs. Use conventional Pagefind UI/index facilities,
maintain authoring/preview usability and document the supported refresh path.
No search backend, CDN, extra infrastructure or production activation is implied.

Move the small-screen sidebar control to the left to match the left sidebar,
while retaining keyboard, focus and desktop behavior. The architect settles the
substantive search brief; implementation owners retain source/check/docs/commit
and findings. Main owns visible copy acceptance, independent review and final
verification/publication coordination. Existing draft/human-review, protected
corpus bytes, feature-only Git and no-production boundaries remain in force.


Additional pagination requirement: current page needs a selected shape/background
and weight, usable links need clear interactive styling and focus, and disabled
navigation must look muted and remain noninteractive. Preserve native Hugo
pagination semantics, centered wrapping controls and stable routes. This is part
of the bounded navigation correction, independent of Pagefind design.


## English blog and KB destinations

The user requests English article links to use corresponding English blog and
KB articles where equivalents exist. Use immutable blog identity and verified KB
<page> translation IDs or actual language links. Preserve mailing-list and other
external URLs. Inventory exact query/fragment/encoded forms, define unmatched and
unpublished translation fallback without broken routes, and keep the verified
mapping offline so builds need no KB network access. Preserve original imported
Czech files, code, source hashes, identities and English prose/draft state.
The prior source-URL parity contract is retained at source level if output routing
can satisfy the request; any intentional translated-output URL change is audited.


## Correct historic KB destinations and mobile sidebar flow

The user rejects remaining Czech KB fallbacks, citing wp490's api#cli, and asks
that all18 occurrences be reevaluated. Missing historical source anchors/pages
alone do not rule out a current English equivalent. Use surrounding article
meaning and actual English sections/navigation (including bounded English KB
search for retired pages), preserving link intent rather than requiring the old
fragment to exist. Reuse the8exact-target inventory and verify all9cli contexts;
retain honest unresolved cases only after semantic reevaluation. No KB writes or
invented translations; corpus/source bytes remain protected.

The small-screen sidebar must expand in normal document flow and use page
scrolling, without its current viewport height cap, nested scroll area or clipped
absolute overlay. Preserve desktop layout, left native checkbox/control and
focus/keyboard behavior. These are separate bounded source packages; Pagefind is
unchanged. Final committed checks/review and focused scrolled runtime evidence
precede feature publication; no merge or production action is authorized.
