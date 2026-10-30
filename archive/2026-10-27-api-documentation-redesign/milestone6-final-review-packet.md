# Milestone6 final review packet

FINAL PACKET. Source, serial commits, logical history and bounded quick package
verification are complete. Source/index are clean; no active command remains.
Prior35c report remains separate. Final review precedes broader gates.

## User scope and accepted result

The user reviewed milestone5 and corrected these requirements:
Exact original messages: [milestone6-user-feedback.md](milestone6-user-feedback.md).

- Placeholder `Resource...`, replacing literal ellipsis.
- Client and Examples selects remain visible/enabled, listing only available
  options, including a single option. Preserve saved thorough/other-language
  preferences and scroll/copy behavior.
- Recognized slashless version GET/HEAD roots redirect308 to canonical slash
  URLs, preserving query/mount and same-origin relative Location. API action,
  unknown-version, OPTIONS and mutation routes keep their contracts.
- Remove built-in Basic documentation sign-in; offer OAuth when configured.
  Docs identity uses only its valid documentation cookie. Conflicting API
  credentials cannot override or repair it. Ordinary API/OPTIONS/provider
  authentication and Basic/token/OAuth example code remain available.
- `/doc` opens the existing packaged server README, with index/readme aliases,
  neutral no-auth/no-store shell and one sidebar reference menu.
- Dotted canonical resource identity in sidebar/page/directory/search; human
  breadcrumbs can retain slashes, optional search label hierarchy uses middots.
- Remove exactly the useless Overview sentence identified by the user.
- Keep sidebar width unchanged and icons beside title. ONE44px native settings
  icon opens ONE menu with direct theme choices and conditional OAuth/account
  controls. No nested theme/account menus, wider sidebar, required-host truncation
  or icons moved below title. `172.16.106.40:4567` and `api.vpsfree.cz` must fit
  at normal desktop sidebar width; arbitrary long names may wrap safely.

Main approved visible/accessible copy: Documentation settings, Theme, Sign in,
Account, existing theme choices, Sign out/Switch user. Main owns final guides.
Accepted design: design.md 'Milestone6: OAuth-only reference identity and final
navigation corrections'. No provider protocol/refresh/discovery/key/lifetime,
new cache framework, dependency graph, budget/reference or release change.

## Architecture, auth and fixture boundary

C core owns documentation_authenticated? orchestration: reset/set current_user
from private documentation_authenticate defaultnil, post-authenticated/locale
once. Core controls defaultnil. Root resolves per-version docs users and
aggregates once; ambiguous multi-version account controls remain hidden.
D overrides only private identity hook/controls; cookie decrypt/purpose/expiry/
origin checks and direct requested-version OAuth token lookup happen per network
request. Chain#authenticate_oauth2_token selects only capable OAuth providers;
OAuth2::Provider#authenticate_access_token factors its existing token callback.
No request env/header/param injection/restoration or ordinary API fallback.
Unsupported providers fail closed; ordinary API parsing/conflicts stay intact.

CookieB plus Basic/Bearer/custom/queryA staysB; absent/invalid cookie is anonymous.
Logout/switch uses cookie/origin/strictscalar/CSRF and ignores API credentials.
Preserve revoke/clear/fresh303state+PKCE, truthful502, cancellation and R1
pending-only callback rescue. Compatibility_login/_logoutGET routes redirect303
without challenge, authentication, cookie mutation or arbitrary return targets.
This intentionally supersedes M5's explicit-credential-first HTML behavior.

Tests formerly using Basic for filtered HTML now use the small self-contained
DocumentationOAuthFixture. It mints cookies via the actual configured writer
outside requests, with deterministic per-role CSRF and fixture token/lifetime;
each page still decrypts/looks up/authorizes. No mocked docs identity in actual
acceptance/performance. Candidate neutral harness enables this real fixture only
for documentationHTML; old f6 keeps genuineBasic through bounded capability
setup. API/OPTIONS/direct render scenarios, dimensions/counters/registry/bounds,
frozen runtime/locks/budgets/reference stay unchanged. Samples record mode/role;
no normalization removes crypto, token work or CSRF stability requirements.
E changes materially for this compatibility, so old E patch identity is NOT claimed.

## Exact repository/history

Session2026-10-27-api-documentation-redesign; tracking plan/state/design and
receipts alongside packet. HaveAPI worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi`.
Canonical remote git@github.com:vpsfreecz/haveapi.git;
branch2026-10-27-api-documentation-redesign.
Basef6e5c3750c747b33ec869c54ca220bf6f1d9d2d0.
Final HEAD a06b0cfa2abd7560f10cb58ebe99d8eb3f10b8f9;
tree ed2764be21718b64e8f9f1bf9e2480798beaa18d.
Complete five-commit series in order:

- A4363d1114f31cbb5d61411a95f6501bda17b50c0 core examples.
- B260e3ea8a469c8840164bd8a0f5044238f5472e1 generated adapters.
- Cced8e1e1bde7a7e0791b77d804e9642ddd80ddec UI and anonymous documentation core.
- D0cbf6a8a3d7a7af5d4636062c8414ab81550add9 optional OAuth and direct-token seam.
- Ea06b0cfa2abd7560f10cb58ebe99d8eb3f10b8f9 cache/performance contracts and fixtures.

Lead independently proved empty e709-to-final diff, equal tree and byte-identical
aggregate binary full-index base-to-head patch, SHA256
cc90fa9324eb54aa6f558827d75ba154a2d9bf1e4fabbfb966021cf3ed078cbe.
All source/index clean. Reconstruction receipt and all supporting original/derived
snapshots, staged/committed proofs, hooks and smokes:
history-m6-final-20261028t180031z/receipt.md.
Accepted clean sidecar head e7092f321ea6096483b3c7d0fc992b6752cf742e,
tree ed2764be21718b64e8f9f1bf9e2480798beaa18d. Finaldiff123files,+8577/-775;
M6+portabletestdelta vs35c49files,+1260/-575. Owner0f9d032a3,owner1e8c176d0,
owner329e0d9fb andowner4e7092f32 are committed with ordinary hooks and accepted
source-byte equality; worktree/index clean before reconstruction.

Retain published35c1fb964735639c0873aacf078e18569f05f9bc/tree756b and all
review/browser/HTTP/runtime receipts as historical scope. Narrow test-only
266dcb1852c8bac8735af684ce48380d2851a658 corrects Ruby3.2/3.3 Hash#inspect
assertion and belongs finalC. CI failure40723980063/attempt1 retained; oldRuby3.2/
3.3 each846/1, Ruby3.4/release846/0. The test now expects escaped runtime inspect;
11focused pass/lint/hooks. New final CI matrix must prove actual3.2/3.3.

Logical groups remain A core examples, B generated adapters, C UI/anonymous core,
D complete optional OAuth/token seam/helper/role tests, E performance/cache and
fixture compatibility. Owner0 supplies authoritative current C/D pre-E and final
variants, no M5 Basic-default assumptions; owner1 exact core-C/optional-D patches
isolate three OAuth contexts. Actual committed boundary/load behavior must be
proved, not inferred from final tree. No whole-parent reversal shortcut. Future
E shared-path inventory and precise optional test dependencies must be explicit.
Owner0 authoritative package:
/tmp/2026-10-27-api-documentation-redesign-m6-auth-history-final-3mu27sp4/.
Ten runtime snapshots, exact11D examples across5mixed specs and9E paths; stale
Basic HTML performance_spec deletedC/absentD/fullcookie+cacheversionE. Allseven
patches replayfuzz0/nooffset and reconstruct28ownerfiles. Main guide override:
/tmp/2026-10-27-api-documentation-redesign-m6-guide-history-wg66d9z8/ has exact
core-C/optional-D guide bytes, restorationpatch d04540924bae8f4c4d3a4e2315661252674ff9a64c21ee0cbbe3cd974fc949c8.
C guide has no absentOAuthguide link/accountpromise; D restores exactfinaltext.
New main-authored C/D/E messages describe finalcontract and are authoritative,
replacing old Basic-first/compact-theme prose; A/B remain exact.

The first scratch C hook attempt stopped with RuboCop layout errors after D test
removal and one empty OAuth-only escaping example group. HaveapiI18n passed; no
commit occurred. Bounded correction authorizes intermediate blank normalization
and defers the entire current_user_html_escaping_spec file to D, which restores
its complete accepted bytes. No final-source change or bypass is authorized.
Original projections and failed log remain preserved; owner2 must bind corrected
derived snapshots and actual final equality in its completion receipt.

No migrations: complete base-to-head changed-path inventory has no migration,
schema/seed/persisted-format change, including no externally used intermediate
migration. No repeated feature dependency/channel/input/lock/generated-pin update
streams. No feature version/dependency manifest/lock change. Upstream0.31 metadata
is baseline provenance; prior session-only preview lock refresh is outside this
feature series. Independent whole-series/history/migration conclusions REQUIRED.

## Focused source checks and docs

All existing prepared Nix/component graphs reused; distinct batches overlap:

- Owner0 27paths: final51/0 seed59034,18Ruby lint,7ERB; prior core50/0 and narrow
  role/counter/shape+Basic19/0 retained at actual scope. Profile fixture initial
  Host/non-HTML setup failures corrected, no claimed whole32batch rerun.
  verification/m6-owner0-source-ready-20261028t173502z/receipt.md.
- Owner1 9paths:55/0 seed50232,7Ruby lint; exact3optional role/index/neutral cases
  and C/D patches. verification/milestone6-search-shared/receipt.md.
- Owner3 exact3asset paths: all3existingasset scripts, syntax/whitespace pass;
  source-ready hashes retained. No final browser geometry claim yet.
- Owner4 9paths:120/0 seed16029 including ordinaryBasic/Token/OAuthAPI,8Ruby lint;
  real-cookie helper/read/lookup/filter/stability and credential-crossmatrix.
  verification/milestone6-oauth-source-ready.md.
- Actual committed C smoke: four mounted HTML routes remain anonymous/full
  despite Basic admin, themes only, no Basic lookup; inert legacy303; API GET and
  OPTIONS still admin. D unconfigured is anonymous; real encrypted member cookieB
  plus Basic adminA filters all four pages as B, with native CSRF forms and actual
  requested-version token lookup. Absent/invalid cookie is anonymous; API/OPTIONS
  stays A without cookie lookup, cookie-only API401. Separate processes bind all
  112 C /114 D loaded HaveAPI paths and templates/packages to clean snapshots.
  These are synthetic in-process HTTPS Rack requests, no listener/TLS exchange.
- Exact-final make doc + fresh extracted-gem packaging/profile10/0, seed50232,
  11.4075s wall. Actual log/command in history-m6-final-20261028t180031z/
  final-packaging-profile.log and .execution.json. All2148 current protected
  hashes match before/after; no input refresh. Lead read receipts/logs/results.

Main read final UI/OAuth guide text and implementation facts, applied required
writing skill; owners verified facts/links. doc/performance.md explains lasting
fixture/identity measurement semantics. Temporary reports/rollout provenance stay
in this session. No KB or provider deployment docs were silently changed.

## Consumers and later acceptance

HaveAPI provider/public contracts and representative same-session vpsAdmin
consumer remain as prior packets. Peer2026-10-24-vpsadmin-haveapi-upgrade owns
immutable five-gem consumer pins and HTTPS devcluster. No peer records/team/
worktree/cluster accessed. Prior35c source handed off, then peer told defer final
pin/activation for M6; peer officially reports35c never selected/fetched/built/deployed, no consumer
boundary. Its own user explicitly authorized deploy-on-ready; it is preparing
all5gem+make-doc/HTTPS inputs and awaits our exact reviewed M6 successor. Main
sent settled docs-cookie-only/API-separation/README/slash contract in reply
7f5332c3-44a8-4690-b7f2-bef2f0167aa1, no peer records accessed.
No HaveAPI release/default integration authorized. Actual callback contract and
provider origin/config/trust/concurrency remain documented, not live-proved.

Official peer message226abc77-1ae8-4c71-a25d-92352d57eb26 supplies one concrete
consumer invariant: vpsAdmin8102179 uses the standard OAuth2.with_config with a
Config subclass; its token lookup delegates ResumeOAuth2 and existing
pre_authorize filters roles/scopes. Its api.rb117–126 post_authenticated hook
clears thread-local User/UserSession on nil and sets PaperTrail identity.
Valid and nil docs identity must both retain ordinary post-hook/locale
processing across successive worker requests. These are packet-supplied peer
source facts, not independently inspected deployment. Reviewer0 and owner4
received this for existing-code/evidence mapping; no new test or source action.

M5 finalHTTP26/browser all4width+cache/copy/control/fallback passed on35c,
not M6. Backend currently captured35c but templates/assets read activeworktree;
no finalM6 runtime claim until refresh. Real HTTPS/token/revoke/account-entry/
clipboard acceptance remains peer-owned. Switch defaultsfalse until dedicated
client's fresh editable credential entry is actually checked. New docs-only
identity contract must accompany successor pin handoff.

Old35cCI actual release build+make test proves docs846/0, generatedprofile18/0,
Pythonencoder7/0 and assets at that exact source/CI graphs only. Standalone
installed dynamic and Go/TS/Rust documentation wire/MSRV runners remain unrun.
Architect's CI reuse mapping guides later gates, with final source/input proofs;
no status-only or historical-source relabeling. Frozen exactf6→final paired,
all-client/bothdetail/bothscaling and ordinary performance remain required.
No broader gates before this final affected source review.

## Review selection

RiskHIGH: changed docs identity/provenance, direct provider token seam, cookie
session operations and neutral performance fixture compatibility. Retain eligible
reviewer0 savedgpt-6.1-sol/xhigh/read_only/native01a18193-44f5-7741-8b6e-6893a0e7f14d,
verify live/native actual settings; no overrides or nested reviewers. All four
complete mandatory-change-review references apply. Inspect changed auth/UI/
fixtures/contract/docs plus complete final series/migrations/update streams;
reuse unchanged35c conclusions only at proven scope. No report/source/input
writes, checks/auth/browser/provider/remote/service/lifecycle actions by reviewer.
Report exact findings byseverity, distinct lanes/history and residual limits.
Source review is separate from deployment, measured/runtime acceptance or merge.

Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
