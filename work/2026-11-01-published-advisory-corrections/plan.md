# 2026-11-01-published-advisory-corrections

## Current merge-preparation scope

The user's later “well then continue, prepare for merging” and requested
configuration channel update authorize published feature preparation only.
Final API942c, KBf977, configc410 and unchanged modern1c/client0b are committed,
quick-checked and independently reviewed. Required local acceptance passed:
strict final KB and the affected three admin browser cases; other successful
native/API evidence is reused only within the reviewed actual-input boundary.
The incidental VPS navigation repair and its test-context correction stay in
one independent logical C commit. Complete histories have no migrations or
obsolete repeated pin stream. [State](state.md) owns exact sources, remaining
receipt/freshness work and CI status; [handoff](handoff.md) owns the prepared
interfaces/rollout/recovery summary. No merge, production operation, preview
mutation or session lifecycle action is authorized by preparation.

## Goal

# Implement corrections to published security advisories

The user explicitly requests a NEW workspace session using the SAME provider
(`codex-lb`, verified for source session `2026-10-30-linux-cve-review`) and a full
team. Implement this in your own session, with its normal architect, implementer,
review and verification workflow. Start work; this is an implementation request.

User direction, in order:

> well, this is insanity. vpsadmin must allow us to edit texts and statuses of
> published advisories. we must be able to correct mistakes. start a new workspace
> session using the same provider and a full team. ask it to implement the changes
> we need.

> update of the original advisory shouldn't trigger emails

> for that we have the advisory updates resource...

## Required result

Allow authorized corrections to the ORIGINAL text and structured node-status
rows of an already published vpsAdmin security advisory. An edit must never send
email, republish, reset to draft, create another advisory, or append an advisory
update automatically. The existing `security_advisory_updates` resource remains
the separate announcement mechanism with its existing explicit mail choice.

Use the smallest conventional change in existing owners. Investigate and record
the design before implementation, then implement, check, commit, independently
review the full branch/history, run appropriate tests and push the feature branch.
Preserve authorization, optimistic `expected_content_revision` concurrency,
publication identity/state/original timestamp and existing update history. Keep
draft editing compatible. Ensure affected-node counts and stored affected-user/
VPS projections become consistent when node conclusions change; a visible table
fix with stale member data is incomplete. Respect transaction/locking and failure
semantics, including concurrent/stale edits and rollback. Test published text and
node correction, unchanged publication identity/history, no mail, unauthorized
and stale edits, and derived projection consistency. Do not introduce a new
schema/framework or API variant without a concrete need. Check existing WebUI
edit flows as well as API behavior, and update owning docs/clients only as needed.

Primary repository is `vpsadmin` (canonical SSH remote
`git@github.com:vpsfreecz/vpsadmin.git`). Determine its correct current feature
line/base containing security advisories rather than assuming a stale default.
The source inspected by the originating session was
`ff730be468e366ee346dc6d02dc0fe57c3f8677c`; treat it as an investigation reference,
not an instruction to use a stale base. Follow repository-local AGENTS and current
workspace procedures. Any necessary security-advisories client follow-up must
preserve its draft-sync protections; do not weaken guards to conceal server refusal.

## Settled evidence deliberately shared by the originating lead

The current token has node-update permission: read-only OPTIONS on
`/v7.0/security_advisories/165/node_statuses/2134?method=PUT` succeeded200.
An actual ordinary node PUT on advisory165, row2134/node120, with revision13 and
the approved correction returned409:

> security advisory can only be changed while it is a draft

The one request was:

```json
{"node_status":{"expected_content_revision":13,"state":"mitigated","vulnerable_until":"2026-10-18T23:22:51Z","mitigated_since":"2026-10-18T23:22:51Z"}}
```

Immediate coherent readbacks confirmed the complete published advisory and all
13 node rows unchanged, still revision13, publication timestamp
`2026-10-31T20:43:09Z`. There were no retries or uncertain effects. A previous
ordinary parent-text PUT also returned the same draft-only409 and changed
nothing. This is a state restriction, not missing token permission.

Retained source references:

- `api/lib/vpsadmin/api/resources/security_advisory.rb:582` routes node PUT
  through `mutate_draft`; helper near105 invokes the model.
- `api/models/security_advisory.rb:62` locks and rejects non-drafts before checking
  expected revision. The node route has no published exception.
- `webui/pages/page_security_advisory.php:22` and169 use the ordinary node PUT;
  parent text editing and Post update are separate actions.
- Stored affected projections are rebuilt separately near
  `api/models/security_advisory.rb:151`; publish calls rebuild near127 and the
  resource exposes a separate rebuild near402. Do not use republish as a repair.
- `security_advisory_update` create takes separate localized summary/message,
  optional state/publication time and `send_mail`. It does NOT modify original
  parent responses, node rows or affected projections.

The originating session incorrectly substituted 15 text correction posts for
updating97 structured node conclusions. The user rejects that substitution.
Those posts now exist as update IDs1–15 and must be preserved unless the user
separately requests changing them. No structured correction has been applied.
Do not redo CVE assessments/research or author more explanatory substitutes.

Original operation constraints: no email notifications; four NFS advisories with
backuper (IDs150,151,154,155) remain drafts and must not be published or edited by
this development session. No production data mutation, token issuance/rotation,
deployment, default-branch integration or session lifecycle cleanup is authorized
by this implementation request. Prepare the reviewed implementation and report
the exact interface, validation, compatibility and deployment requirements.

## Communication and session boundaries

The user explicitly directed the originating lead to start this session and ask
it to implement this work. Cooperate through `session_communication` with the
originating session `2026-10-30-linux-cve-review` once the exact-pair runtime grant
is established. Preserve your own settings and scope. Ask your own architect and
implementers through your own verified roster. This brief shares the facts above;
it does not grant access to the originating session's files, transcript, team,
worktrees or credentials. Request any missing evidence by lead-to-lead message.
Do not infer merge/deploy/lifecycle authority from a peer message. Keep both
sessions open.

## User scope expansion (2026-11-01)

User explicitly answered Yes to published CVE-link and node-add/remove corrections,
then added: “well and publication time should be editable as well. plus we
should be able to retract/delete an advisory”. This supersedes the initial
conservative immutable-time/CVE/membership scope. Correction requests remain
silent and revision/authorization protected; retract/delete are explicit actions,
not correction side effects. No production data operation, deployment, default
integration or session cleanup is authorized. Architect owns delta design before
additional implementation; all complete deliverables need new final review.
Existing update history stays intact during corrections/retraction. Lead settled
conventional hard-delete semantics for the explicit Delete action only: remove
advisory-owned rows/links, never referenced nodes/VPS/users/outages/mail/logs.
Corrections may also edit retracted originals. Follow ordinary model nullable
timestamp/CVE rules rather than invent published-only restrictions; editable
WebUI supports empty CVE edits if API permits, draft creation contract retained.
Direct silent retract keeps publication/history/projections. Orphan-race parent
locks and expected_state on all six draft-sync mutation types are necessary
supporting invariants; no schema/framework or production operation.

User additionally directed “and we also handle vpsadmin-webui changes if
appropriate”. Architect will inspect its current advisory UI and fresh owning
line, then define necessary matching app/client/tests/docs work with its local
procedures. This is distinct from legacy vpsadmin/webui; no speculative redesign
or general client migration authorized.

## Affected repositories

Primary: vpsadmin, canonical git@github.com:vpsfreecz/vpsadmin.git.
Architect will establish the current advisory feature base from fresh refs.
Security-advisories requires a bounded client follow-up to preserve draft-sync
protections across concurrent publication; its existing preflight guards stay
intact. Architect will establish its fresh canonical base.

vpsfree-kb-contracts is a verification-only pin/check follow-up required by the
canonical WebUI workflow. No advisory controls/pages/captures are currently
bound; validate the exact final source without inventing documentation changes.

## Approach and owners

1. architect0 (Astra/xhigh): investigate current owners/base and write design.md,
   including atomic projection refresh and independent implementation boundaries.
2. Assigned Sol/xhigh implementer(s): implement complete packages, focused tests,
   owning docs, quick checks and commits. Serialize overlapping files and Git.
3. reviewer0 (Sol/xhigh): mandatory independent final full-branch/history review
   after committed deliverables and quick checks, before longer integration tests.
4. Lead: accept evidence, coordinate verification, push feature branch and record
   exact interfaces, compatibility and deployment requirements.

## Decisions and limits

Silent original corrections use existing authorized interfaces and expected
content revisions. Add optional expected_state checked under the same lock:
publishing leaves the revision unchanged, so this is necessary for draft-only
clients to reject concurrent publication. WebUI supplies rendered state and
security-advisories sync supplies draft; retain old-server compatibility only
where old draft-only refusal makes omission safe. No new endpoint or schema. Announcements remain separate advisory updates with explicit
mail choice. Preserve publication identity/state/time and all update history.
No production mutations, credentials, deployment, default integration or session
cleanup. Both sessions remain open. Exact-pair runtime communication grant is
active; communication grants no peer filesystem access or operational authority.

## Compatibility and deployment

Assess existing API/WebUI flows and persisted projections, transactional locking,
stale writes and rollback. Prefer no schema or new API variant. Draft editing
remains compatible. Deployment is prepared only; API/WebUI ordering and rollback
requirements will follow the verified design. No configuration pins are changed.

## Documentation

Readers: advisory administrators and API/client maintainers. Update existing
advisory documentation where correction behavior belongs; keep this rollout's
revisions and evidence here. Apply user-facing writing skill directly before
committing visible prose. Check KB contracts if WebUI changes require it.

## Testing plan

Cover published text and structured node correction; unchanged publication and
update history; no mail; authorization and stale/concurrent edits; transactional
rollback and affected-node/user/VPS projection consistency; draft compatibility.
Run quick checks before review, then risk-appropriate longer checks using a fresh
verification watcher. Inspect branch CI after push. Exact commands come from
repository instructions and architect's brief.

## User-approved visibility correction (2026-11-02)

User reported anonymous visibility of retracted/draft advisories, then agreed
to the lead recommendation: only published advisories are public/member-readable;
drafts and retracted advisories are admin-only, including lists/direct URLs and
related reads. Retract remains silent, preserves original/history for admins,
and differs from permanent Delete. Actual first anonymous probe confirms drafts
already404/omitted, retracted200/listed; do not invent a reproduced draft leak.
API is authority; both UIs follow the same rule and stale public content must not
render from a known nonpublished record or trigger child fetches. Scoped source/
tests/docs, quick checks, committed affected independent review then bounded
role/state/browser checks and same-session devcluster update are required.
Preserve running cluster data/three synthetic fixtures; no reset/stop/production
or default integration. Earlier reviews/results retain their immutable scope.

Authoritative accepted execution boundaries: [visibility-design.md](visibility-design.md).
Implementer0 retains all API/legacy/KB Git; implementer1 owns modern only. New
focused regressions/quick checks precede committed affected review; longer
API/core/browser/strict KB acceptance and preview update follow that gate.

### Server-only visibility boundary (later user correction)

The user explicitly rejected duplicate client-side visibility enforcement:
“the visibility is handled by the server completely. the UIs shows what the
server sends them, it is useless to implement retracted advisory hiding also in
UIs”. This supersedes the new modern public filters/cache guards and their test/
doc package. Restore exact reviewed/running modern1c847; preserve f7c4 as rejected
candidate evidence. Only the API owns the published-only non-admin policy, with
related query intersection/regressions. UIs display server results; administrators
retain authorized retracted access, without an extra public-route state policy.
Existing standalone UI implementation remains unchanged. API/KB review, relevant
checks and running preview update still required; no frontend framework/campaign.

## Requested configuration channel update (2026-11-02)

User additionally requested “vpsadmin channel update in vpsfree-cz-configuration”.
Prepare one normal confctl-owned channel/input update in a new session-owned
configuration feature worktree after inspecting actual channel/role mapping.
The requested advisory feature is unmerged; use exact final published feature
revision via confctl channel set rather than accidentally selecting upstream
master without the feature. Keep generated changelog/message, hooks and one
logical pin stream; inspect unrelated/transitive graph changes and run relevant
nondeploy validation. No manual lock editing, production activation or default
integration is authorized. Implementer1 owns config-only package; implementer0
retains API/legacy/KB. Current APIa38c candidate readiness is limited by unknown
hosted count failure, pending integration and fresh API master1d4869 vs reviewed
097; current pin preparation is not unconditional release readiness. Any final
API successor needs a consolidated mechanical channel refresh/equivalence check.

Accepted mechanical mapping: channel `vpsadmin`, role `vpsadmin`, root input
`vpsadminServices`. Pin current verified candidate `a38c9f8` using the declared
confctl command. The 17 declared host names indicate channel membership, not
that every service package changes. Preserve separate staging/production role
inputs and the independent WebUI source pin; inspect expected transitive follows.
Use parse/semantic graph and bounded channel/host/options evaluation, without
fleet builds or deployment. Keep the result on its owned feature branch.

## Authorized merge preparation continuation (2026-11-02)

User followed the readiness report with “well then continue, prepare for
merging”. Continue feature preparation through necessary diagnosis, patch-equivalent
API reconciliation, narrow owning test-helper repair if required, consolidated
API/KB/config heads, quick checks, applicable independent affected review, and
risk-based verification. This is not default-branch integration or deployment
approval. Preserve current DEV runtime/data and the rejected frontend-policy
boundary. Retain old reviewed/deployed ranges and input provenance; no source
identity or green rerun alone proves that the hosted count failure was harmless.

Architect0 records the bounded brief in existing design.md. Implementer0 owns
API/legacy/KB and their Git/tests; implementer1 owns only final config regeneration
and one end-package modern/client freshness snapshot. Serialize utility use and
all same-repository source/Git operations. Reuse successful checks only within
their proven source/effective-input scope; assess changed bundle inputs before
selecting repetitions. No optional broad campaign or unrelated framework repair.

## Proven integration navigation correction (2026-11-02)

Final integration's3failedWebUI scripts have a proven common wrong destination:
Restart/Shutdown succeeds, then existing origin-only same-host referrer resolves
to Overview instead of the explicit VPS fallback under strict-origin policy.
The owning PHP helper reproduces this deterministically. The accepted TOPdesign
brief permits the smallest helper/existing-unit correction: ignore only origin-
only targets with empty/missing query, preserve meaningful root queries and
filtered/paginated same-host URLs and all existing validation/auth/header/CSRF
behavior, use canonical list fallback where required. No new UI concept/copy,
policy framework, timeout change or production action.

Implementer0 owns separate logical C (independent VPS navigation fix), quick PHP
checks/hooks/commit and one final consolidated KB pin, then affected review and
only3failednative scripts (15–25min) with actual selector/input proof. Existing117
successes/advisory18/API/KVM evidence remains source-scoped; no135script/4.5h
repeat by default. Implementer1 refreshes one config pin after stable API handoff.
Actual KB contract drift determines impact; no capture/staging/publication without
reported need. Source edits may affect live-mounted DEV PHP; record actual effect
without an extra cluster activation or changes to APIa38c/modern1c/storeddata.

## Fresh HaveAPI0.32.2 target boundary (2026-11-03)

Master advanced to5586ea8 after the navigation fix's quick checks. Its13dependency/
tooling paths change HaveAPI server/client/generator/exporter inputs, not owning
application or C paths. The accepted TOPdesign brief permits compatible A/B/C
refresh after canonical0.32.1→0.32.2 source/release inspection: ordinary dispatch,
resource/input/output/count/auth/rootOPTIONS owners unchanged; documentation,
locale handling/packaging and TS generation changed. Actual five-gem published
hash provenance is checked. No schema migration or concrete advisory/sixguard
contract break found. C stays a separate logical commit; old.32.1 proof is scoped.

Verify actual loaded.32.2/effective full-core locks/NAR/derivation/graph and final
feature metadata/read/mutation evidence; use normal hosted coverage when available.
Existing exporter safety/snapshot checks and REQUIRED services-up verify changed
packaged schema/protocol/clientdocs. After committed quick/source review, native
package is services-up plus3failedWebUI scripts, no135script replay by default,
then strict finalKB pin and only necessary drift remediation. Stableconfigrefresh
follows finalAPI handoff. No production/cluster/ReferrerPolicy/auth changes.

Actual modern consumer inspection found no production dependency on Services'
TSgenerator: config70bd uses handwritten fetch/nohaveapi-client; feature1c uses
npm-lockpinnedhaveapi-client0.32.0/handwrittenAsyncClient adapters. Production
frontend/BFF args do not include vpsadmin/generator; follow is localization/module/
VM context. No newfrontendbuild/regeneration or code is needed from this update.
