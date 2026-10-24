# 2026-10-19-haveapi-async-client

## Goal

I'd like to add support for async in haveapi javascript client. should it be a separate package, or be included in the same package? currently the client is callback-based. suggest a solution and an implementation plan.

I'd also like to know what haveapi client is used in vpsadmin-webui, if any. would it benefit from async support in haveapi client in javascript?

## Affected repositories

- `haveapi`: inspect JavaScript package, asynchronous operations and compatibility.
- The separate React `vpsadmin-webui`: inspect its actual client dependencies
  and design a supported adoption path. Legacy WebUI and console integration
  are explicitly out of scope per user direction.
  `repos/vpsadmin-webui.git` exists despite its omission from the project map;
  inspect its retained refs read-only and state their freshness limitations.
- User explicitly authorized implementation with "Implement the plan" after
  accepting TS authoring for both clients and backward compatibility as a gate.

## Approach

Architect `architect0` owns source investigation and the proposed design in
`design.md`. The lead owns scope, evidence acceptance and tracking. Inspect
canonical repository refs without using other sessions' worktrees. Compare an
separate Promise-based client object in the existing package with a separate
package, preserving the existing callback client. Focus consumers on the new
React WebUI.

## Decisions

- Retain the current team and saved member settings.
- Implement on session-owned feature branches, publish those branches after
  verification. No release, deployment or default-branch integration is authorized.
- Planning and investigation do not trigger mandatory final change review.
- Revised recommendation following user feedback: keep one `haveapi-client` npm
  package and export a separate `AsyncClient` object/class. Give its methods
  ordinary names (`setup`, `authenticate`, `request`, resource action names),
  all Promise-based for remote operations. Preserve existing `Client` callback
  and callback-free calls. This supersedes repeated `Async` method suffixes.
- User runtime direction: support up-to-date browsers, not EOL ones. Preserve
  existing Node entry points; do not expand scope into a separate runtime rewrite.
- Use a fixed `{ value, response }` result for Promise action invocations so
  dynamic API members named `then` cannot be invoked by Promise assimilation.
  Resolve initialization/authentication without returning the dynamic client.
- Promise invocation settles on the API reply. Server-side queued work requires
  a separate completion contract; a successful receipt does not prove completion.
- The React `vpsadmin-webui` already owns a Promise-based TypeScript fetch client
  and has no npm HaveAPI dependency. User explicitly wants it to be able to use
  the new client if possible. Future adoption is a design goal: include types,
  cancellation, metadata/envelope/error access and header/token extensibility;
  preserve WebUI-owned OAuth recovery and non-replayed writes. Plan a bounded
  integration trial before a broad client migration.
- Legacy PHP WebUI and console integration are excluded from this initiative;
  prior source findings are historical context only.
- User selected TypeScript authoring for BOTH the new AsyncClient and existing
  callback-based Client (called "sync client" in the request). Compile both to
  ordinary JavaScript and generate declarations in the same npm package;
  script-tag/CommonJS consumers need not install TypeScript. Preserve Client's
  callback signatures, overloads, return values, hook order, local synchronous
  throws and fire-and-forget semantics. Migrate its implementation in reviewable
  stages without mixing unrelated behavior fixes. Share a typed protocol core
  under independently owned callback and Promise client/resource surfaces.
  Dynamic endpoint schemas require explicit types/generation independently of
  the source language. Update source/build guidelines deliberately for the TS
  migration; modern browsers remain the target.

## Compatibility and deployment

The proposal must cover callback signatures, return values, initialization,
authentication, resource/action helpers, errors, Node/browser packaging and
minimum runtime support. Distinguish JavaScript Promise support from server-side
asynchronous API actions. Identify any protocol, persisted-state or deployment
implications and confirm whether mixed old/new clients can coexist. No rollout
is authorized by this planning request.

## Accepted execution defaults

- Both clients and production helpers use TypeScript. Existing Client remains
  callback-compatible, including return values, synchronous local exceptions,
  callback arguments/hooks, callable objects and fire-and-forget behavior.
- Keep gulp as build entry; compile using tsc (ES5 output, ESNext modules,
  declaration emit), bundle with Rollup to unchanged dist/haveapi-client.js.
  Preserve browser global HaveAPI, AMD and CommonJS named exports; no default
  wrapper, new engines restriction, or eager async primitive use by Client.
- Initial packages: implementer0 hook/env/build/type scaffold and core/auth;
  implementer1 original-bundle compatibility fixtures and actions/resources.
  Architect owns final interface brief. Serialize build/export/index/commits.
- Callback parity precedes typed shared-core extraction and async execution
  packages. New async resources/save/explicit association loading use Promises.
- Run committed-deliverable final independent review after quick checks, before
  long server/browser integration. Watchers run uncertain-duration verification.
- Report specific unavoidable compatibility changes or disproportionate
  preservation costs to the user before changing the compatibility contract.

## Documentation

Readers: the user and future implementers. Findings and implementation boundaries
belong in this session's `design.md`; accepted public client behavior and examples
would go in the HaveAPI JavaScript documentation during implementation.

## Testing plan

This pass uses source and dependency inspection with exact revision evidence.
The design must specify callback regression coverage, Promise success/error
semantics, initialization/authentication, browser/Node entry points and async
action waiting. Do not run builds or integration tests merely for planning.

## Follow-up: explicit callback name

User requests `CallbackClient` alongside `AsyncClient`, retaining `Client` for
compatibility. Use the existing callback constructor as both public names,
preserving identity, statics, prototype and runtime name. Generated declarations
must expose both value and instance type names. Owner0 handles source/build/docs;
owner1 handles independent loader/type coverage. This additive HaveAPI-only
change has no state, schema, protocol, dependency or deployment-order change.
Rollback removes the new name; existing `Client` consumers remain supported.
After quick checks and a focused commit, obtain independent final affected
review and run relevant final artifact checks before publishing the feature.
No release, merge or WebUI change is included.

Naming addition f5320eae is independently reviewed with no findings and
passes installed-tar three-loader/both-type-consumer proof. Publish that exact
head; upstream moved fromc14e7d3 toc58704a0 during this follow-up (release-tooling
fixes), so retain behind2 provenance and reconcile before later approved
integration rather than altering this verified candidate for publication.

Naming publication complete: exact f5320eae JS39313715870 and
i18n39313715770 both passed. Source unchanged and clean; no watcher remains.
All branch integration/release/deployment gates remain separate.

## Approved HaveAPI integration

User explicitly directs merging HaveAPI client and keeping WebUI PR open.
Scope only HaveAPI refs/heads/master. Owner0 prepares latest-base clean rebase,
patch/tree equivalence, quick checks and lineage; lead accepts and submits
coordinated fast-forward integration. Substantive conflict resolution requires
report/applicable review before mutation. No WebUI integration, release, version,
deployment or lifecycle action. Session stays active for open WebUI branch.

## Necessary coordinator preparation blocker

HaveAPI rebase19c20c9 is reviewed and all five CI workflows passed. Supported
coordinator prepare cannot start a job because it chooses its Ruby3.4 interpreter
inside HaveAPI Ruby3.3 shell. Safe dependency-only fix ruled out by independent
diagnosis. Prepare narrow dev-workspace correction and regression under architect
boundary; no installedstore/ledger edits or directmerge bypass. Any sharedruntime
activation remains a separate concrete decision after implementation/review/checks.
WebUI stays open, exact clientsource frozen; no release/deployment/lifecycle scope.

User approved separate runtimefixintegration/adoption with “yes”. Integrate
dev-workspacefix via coordinator, prepare normalcomposedworkspace/configfeature
pins preservingcurrentdeployedbaseline, review/check/build before queuedruntime
activation. Then finishHaveAPIcoordinatormerge; WebUIPRopen. Architectdesign
precedespinimplementation; no unnameddefaultbranchintegration implicit.

Runtimeownershipgate: currentHaveAPIsession cannotnormallyreleasemachinewhile
WebUI PRstaysopen, because reserve freezesallregistrations andfinish requires
exactintegration/catalogresolution. Do not unregister/alias/archive/editcatalog
or submitindefinitehold. Prepared ordinaryseparaterollouthandoff with source
preservation/currentfrontier/normalpinschecks/queue/recovery. Need explicit
ownershipsplitdirection beforestartinganothernativeinitiative; original
HaveAPI/runtimeupdateapprovals retained.

## 2026-10-20: production WebUI client replacement

User explicitly corrected the next step: “well no trial, just replace the original
solution in vpsadmin-webui with the new client”. This supersedes the pilot-only
production-default/dependency boundary. Implement normal application adoption
of HaveAPI AsyncClient and remove superseded generic transport/protocol code,
while retaining WebUI-specific BFF/OAuth/session/retry/domain policy. Architect0
owns design; implementer1 owns production migration and docs; implementer0
owns independently bounded package/dependency/contract work after design.
Use a reproducible unreleased dependency; no npm publication is inferred.
Keep PR74 open. No WebUI main integration or deployment is authorized.
Mandatory committed-deliverable review precedes long verification.

## 2026-10-20: project README and release audit

User requests updated project README and confirmation that release preparation
handles the TypeScript-authored callback/async clients and distributed JavaScript
plus declarations. Architect0 owns bounded design/audit; owner0 independently
checks actual version/build/pack/installed-smoke/release workflow and fixes
concrete release-code gaps, owner1 owns root/client/release documentation updates
after the brief. Main owns final prose/acceptance. No version/tag/npm release,
manual dispatch, default merge or deployment is authorized by this request.
WebUI consolidation still awaits the earlier exact published-history permission.
Avoid re-pinning its already-exact f94 dependency for unrelated root documentation.


User scope correction: keep the root README as a project overview, consistent
with other clients. Its only task change is the JavaScript and TypeScript
client-list label. Usage details remain in clients/js/README.md and release
mechanics in doc/agent-instructions/releases.md. No root client API paragraph.
