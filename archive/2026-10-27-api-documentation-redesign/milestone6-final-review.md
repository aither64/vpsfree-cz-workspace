# Independent final review: milestone6

No new Blocking, Important or concrete Advisory change request found in the exact reviewed source and five-commit series. Prior R1 callback-session preservation and R2 optional-module ownership corrections remain resolved at their source/history boundaries. M6 intentionally supersedes M5's Basic-first HTML identity contract.

This is an advisory final source/history review before broader gates. It does not establish final browser, installed-client/compiler/wire/performance or real-provider HTTPS acceptance, and grants no integration, release, deployment or lifecycle approval.

## Identity and reviewed range

Verified dev-session current from the exact tracking directory:2026-10-27-api-documentation-redesign. Both DEV_SESSION identity markers are absent; the trusted developer binding names that exact session and /home/aither/workspace/ai/vpsfree.cz. Live actual reviewer0 remains ready, purpose review, read_only, saved gpt-6.1-sol/xhigh. CODEX_THREAD_ID and own native session_meta identify01a18193-44f5-7741-8b6e-6893a0e7f14d; latest native turn_context confirms actual gpt-6.1-sol/xhigh. No override, fallback, authoring or nested reviewer.

Risk HIGH. Applied mandatory-change-review, all four complete lane references and applicable workspace/repository procedures, with unchanged guidance reused from this context. Read the complete M6 packet, current plan/state, full M6 design amendment, relayed verbatim milestone6-user-feedback.md and reconstruction receipt. Main-selected labels and the precise token seam were assessed as implementation decisions, not user quotations.

HaveAPI worktree:/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi.
Exact base:f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0.
Exact head:a06b0cfa2abd7560f10cb58ebe99d8eb3f10b8f9.
Tree:ed2764be21718b64e8f9f1bf9e2480798beaa18d.
Actual complete diff:123 files,+8577/-775. M6/portable-test delta versus35c:49 files,+1260/-575. Source/index were clean at inspection and final recheck. Paths below are relative to that worktree.

## Scope and proportionality lane

The verbatim feedback authorizes Resource...; supported visible selects; canonical slashless roots; removing built-in Basic documentation sign-in; README at /doc; dotted resource identity; the exact Overview-sentence deletion; and one title-adjacent menu with direct theme choices and no sidebar widening. The source implements those corrections without introducing an unrelated subsystem. Earlier delivered milestones and subsequent feedback explain the growth; records do not supply a continuous active-work clock, and overlapping member elapsed times were not summed.

The cookie-only documentation identity is a bounded implementation of the user's OAuth-only documentation requirement. Removing API-credential fallback and environment injection gives that identity one explicit owner. The small test-only cookie helper is justified by existing role-filtering/search/performance consumers; retaining a production Basic backdoor would contradict the selected boundary. Capability checks are confined to the documented custom OAuth provider seam and neutral historical-source harness, rather than a general compatibility framework.

The compact search projection, native GET fallback and private HTTP-cache mechanism remain the prior supported boundary. No SPA, service worker, persistent JS index, server snapshot-history cache, live permission polling, provider discovery/refresh protocol, dependency graph or performance-budget expansion was added. Open-page snapshot staleness remains accepted and destinations reauthorize. No speculative hardening or additional framework is required.

## General lane

Inspected the substantive35c-to-final source/tests/docs delta and current final series, reusing prior35c conclusions only for actual unchanged scope.

Presentation: documentation.js:582–614 rebuilds Client options from the selected language and Examples options from the renderer's declared levels. A single supported option stays visible/enabled; zero options alone disables the control. The change listener preserves a saved thorough preference on single-level clients. Asset coverage checks supported options, other-language preferences, scroll restoration and exact copying after effective-panel changes. Existing capability inheritance, renderer IDs, Context/direct rendering and both-level generation remain intact.

views/version_sidebar/brand.erb now contains one native details[data-documentation-menu] with a44px summary, direct theme buttons and conditional account content. documentation.js:146–175 handles positioning, Escape/focus return, outside dismissal and drawer closure; theme choice no longer changes the settings summary into a theme-only name. CSS preserves18.5rem/17rem widths and1100/900px breakpoints, keeps the icon beside the title and permits long-name wrapping. It reduces the brand font and frees one trigger's width. Fake geometry/static assertions support the structure, but actual required-host fit and responsive browser geometry remain pending.

The current resource heading/title/sidebar/directory uses the existing dotted key, while human breadcrumbs retain their separators. Search primary dotted identity is unchanged and optional human label hierarchy uses middots consistently in Ruby/JS fixtures. Search projection/key/ranking/filter/cap/URLs/anchors are unchanged. The placeholder is Resource..., with its accessible version label retained. The exact identified Overview sentence is removed without replacement.

Routes: server.rb:667–681 registers canonical redirects only for declared explicit version roots. Exact PATH_INFO prevents a slash URL loop; GET/HEAD returns308 to a relative server-built URL with SCRIPT_NAME once and original query bytes. Literal header-control bytes are rejected. canonical_routes_spec covers raw encoded query preservation, mounts, HEAD, no loop, unknown versions, actions, OPTIONS and mutations. The legacy _login/_logout GET/HEAD routes now return private/no-store303 to fixed default-version overview with no challenge, authentication, cookie mutation, URL-userinfo trick or arbitrary return destination.

Shared docs: server.rb:602–620 wires /doc,/doc/index[.md],/doc/readme to shared_documentation_helpers.rb:11–15, which reads the existing packaged servers/ruby/README.md with the existing Markdown options and neutral no-store shell. Other technical routes remain. The duplicate README sidebar item is removed. Shared/packaging tests check equivalent landing content, real README feature/code markers, one reference menu, breadcrumbs, aliases, styles/scripts and cache headers through a freshly extracted gem.

The Ruby-version portability sidecar is folded into C's validator spec and expects escaped runtime inspect output. It changes a test expectation, not validator behavior. Actual Ruby3.2/3.3 matrix acceptance is still pending.

Owning doc/documentation-ui.md, doc/documentation-oauth.md and doc/performance.md describe the final supported contract, fixture timing and rollback. Technical behavior is not dependent on private rollout records. Historical source/check/deployment evidence remains in session records. No KB or vpsAdmin WebUI documentation scope was silently added.

## Architecture and repetition lane

HaveAPI remains the provider owning documentation presentation, identity orchestration, optional OAuth client and renderer/adapter contracts. A/B core/generated-example behavior is unchanged at exact commit identity.

documentation_helpers.rb:44–49 owns one documentation authentication orchestration: reset @current_user, obtain it from the private default-nil hook, call normal post_authenticated with that result, then resolve locale. The optional helper overrides only identity/controls. This avoids duplicate hook processing, ordinary-auth fallback and request-header replacement. Core C is usable anonymously without optional OAuth.

Chain#authenticate_oauth2_token at authentication/chain.rb:52 selects only requested-version providers named oauth2 with the explicit token-validator capability, in registration order and preserving deny. Unsupported custom providers fail closed without invoking their ordinary authenticate method. OAuth2::Provider#authenticate_access_token at authentication/oauth2/provider.rb:138 factors its existing config callback and AuthenticationError-to-nil behavior. Ordinary authenticate retains existing extraction/conflict rules. The original request remains a separate argument. This is a small explicit provider boundary, not a mirrored implementation registry or new protocol.

DocumentationOAuthFixture is self-contained test support with no RSpec/spec_helper dependency. It configures the real standard provider and documentation client, then uses the actual cookie writer outside requests. Its version/token lookup map and stable per-role CSRF serve existing authorization/stability tests. It does not mock documentation_authenticated? or store a cached authenticated user in production.

E's neutral harness uses real cookie identity only for HTML on capable candidate sources and real Basic on historical f6. API/OPTIONS/direct-render lanes retain their setup. Cookie issuance/setup is separate from measured page requests; each page still decrypts, validates expiry/purpose, performs token lookup and authorizes. Worker records retain mode/role; lookup-count and raw-body stability assertions preserve meaningful proof. All-client coverage keeps every renderer, both details and both scaling dimensions. Frozen runtime, budget, fixed-reference and failure policy are unchanged. No performance pass is inferred from this source adaptation.

## Risk and compatibility lane

The new documentation identity boundary was reviewed directly. DocumentationOAuth#authenticate:133–148 resets request-local CSRF provenance, checks configured HTTPS origin and GET/HEAD, decrypts the purpose-bound cookie, validates only its token through the requested-version OAuth seam and sets account/CSRF mode only on successful lookup. Missing/invalid/expired/revoked/unconfigured/unsupported sessions resolve anonymous without consulting Basic/Token/custom/API credentials. Conflicting API credentials cannot replace or repair cookie identity, and the original request env/params remain intact.

Root documentation resolves per-version documentation users and describes once with that map. Single-version account presentation uses the actual resulting identity; ambiguous multiversion controls stay hidden. Neutral articles do not fetch identity and expose only a configured single-version Account navigation link.

Ordinary API actions, OPTIONS, mutations and provider endpoints remain on the existing complete chain. Current tests cover Basic/Bearer/custom/query A crossed with cookie B, malformed/conflicting credentials, absent/tampered/expired/revoked cookies, HEAD, requested-version lookup/order/deny/custom capability, original-request preservation and API/OPTIONS separation. They also cover keyed200/304 cookie revalidation, permission-key409 and Set-Cookie/no-store behavior. The documentation cookie alone cannot authenticate API actions.

The additional official peer invariant is satisfied at the provider seam: core documentation_authenticated? unconditionally invokes post_authenticated for both user and nil, then locale resolution. C's unconfigured smoke expects nil hook events; D's same-server sequence runs cookie-member pages followed by absent/invalid-cookie pages and requires [nil] on each latter request. identity_context_spec explicitly asserts nil events for single/multiversion roots; OAuth tests cover successful per-version events and expiry/revocation outcomes. This preserves the hook opportunity needed to clear consumer thread-local User/UserSession and set PaperTrail. It is provider-level evidence, not an independently observed peer deployment or proof of that consumer's actual thread-local implementation. Neutral articles retain their intentional no-auth/no-resource-description path.

Logout/switch ignores unrelated API credentials and retains cookie/origin/strict-scalar/CSRF checks, clear/revoke sequencing, fixed fresh login/state+PKCE, cancellation and truthful502 failure. Existing callback rescue still consumes pending state without deleting an existing valid authenticated session: R1 remains corrected. Cookie format/purpose/key/lifetime/refresh and provider wire behavior are unchanged. switch_user remains false until the dedicated client's fresh editable credential entry is actually verified.

Prior search/cache safety conclusions remain applicable to unchanged code: deterministic whitelist data excludes secrets/private generator schema; cold/conditional network requests authenticate and compare current key before cache success; mismatch409 has no index payload; errors/bootstrap/Set-Cookie are no-store; matching keyed responses alone can use private immutable caching with merged credential/locale Vary. Browser code validates same-origin inert data, constructs URLs/text safely and resets neutral/BFCache loads. Accepted open-page staleness and retained private-cache files are documented.

Compatibility changes are deliberate: Basic/API-credential HTML readers become anonymous; authenticated machine descriptions remain available through ordinary OPTIONS. Legacy documentation login/logout URLs become inert303 redirects. Custom OAuth providers need the explicit validator capability for documentation sessions; their ordinary API authentication is unchanged. README landing and selector behavior change as requested. Reverting to M5 restores the superseded API-credential priority/Basic browser UI; no cookie/database data conversion is required. Remove optional configuration before rollback to code without its methods, and handle dedicated provider-client administration separately.

Actual provider/consumer boundary: the inspected HaveAPI standard OAuth callback is the same interface used by the representative same-session vpsAdmin bootstrap and its Config subclass. The later vpsAdmin8102179/ResumeOAuth2/scope/PaperTrail facts are packet/official-message facts only; no peer records/team/worktree/cluster or deployed consumer was accessed. Its exact five-gem immutable source selection, proxy/CA trust, provider configuration and live behavior still need the peer-owned acceptance workflow. Source-selected sibling gems, published TS runtime0.30.2, independent Rust1.95 MSRV, development Rust and frozen benchmark graphs remain distinct; version numbers do not establish compatibility.

## Whole history, obsolete approaches, migrations and update streams

Reviewed the actual complete five-commit series:
A4363d1114f31cbb5d61411a95f6501bda17b50c0;
B260e3ea8a469c8840164bd8a0f5044238f5472e1;
Cced8e1e1bde7a7e0791b77d804e9642ddd80ddec;
D0cbf6a8a3d7a7af5d4636062c8414ab81550add9;
Ea06b0cfa2abd7560f10cb58ebe99d8eb3f10b8f9.

A/B are the exact previously reviewed commits. C/D/E messages describe the final M6 contracts and match the authoritative message files. C owns final UI/anonymous core, D complete optional cookie/direct-token behavior and its tests/helper, E cache/performance contracts and fixture adaptation. Related tests/docs accompany their behavior.

Independently compared all ten actual C runtime blobs with original-owner core-pre-e, all ten D blobs with optional-pre-e and all ten final blobs with optional-final: exact equality. Main C/D guide snapshots also match actual Git blobs. C contains no optional file/constant/configuration/server dependency or fixture; D introduces the module, four server seams, direct token seam/helper and optional contexts together. The whole OAuth-only escaping spec is absent C/restored D. Stale Basic HTML performance_spec is absent C/D; E introduces the complete cookie/cache replacement. This is a coherent independent boundary, not final-tree-only proof. R2 remains resolved.

Inspected actual C->D runtime/optional seams and retained source-bound smoke.rb/execution/JSON evidence. C's four mounted HTML routes are anonymous/full despite Basic admin, with a themes-only menu and no Basic lookup. D unconfigured is likewise anonymous; configured D's real encrypted member cookie plus Basic admin filters all four pages as member with native CSRF forms and four requested-version cookie lookups. Absent/invalid cookies return anonymous; API GET/OPTIONS remain Basic admin with no cookie lookup, and cookie-only API is401. All112 C/114 D loaded HaveAPI paths, packages0.31.0, methods and templates bind to their actual clean committed snapshot. These are separate-process in-process synthetic HTTPS Rack smokes, not TLS/provider network tests.

Read the first preserved C hook failure. Independently verified the seven authorized intermediate normalizations preserve every nonblank owner-C line, while D restores accepted final specs. The empty optional-only escaping file is deferred whole to D. Original owner snapshots/failed log remain intact; derived correction/replay is explicit. Actual C/D/E normal pre-commit and commit-message hooks pass. No hook bypass or final-source repair is concealed.

Independently proved accepted e7092f321ea6096483b3c7d0fc992b6752cf742e and final a06b0cfa have identical ed2764be trees and empty diff. Aggregate binary full-index base-to-head patches are byte-identical, SHA256cc90fa9324eb54aa6f558827d75ba154a2d9bf1e4fabbfb966021cf3ed078cbe. E's actual path set is exactly eleven; its server/final runtime and nine owner performance snapshots match original-owner bytes. E is substantively changed for cookie fixture/old-source compatibility, so no old-E patch-equivalence claim is made. Original projection and corrected C->D replay evidence report fuzz0/no offsets.

No obsolete unmerged layout/Python-wrapper/per-query-search/Basic-first HTML approach or fixup-only sidecar remains in the final five commits. M6 corrections and the portability expectation are folded into their final owners. Earlier35c and failed/intermediate attempts remain recovery/evidence lineage outside the final range; they are not relabelled final acceptance. Prior original/refreshed-range equivalence is reused only for unchanged actual A/B and previously proved baseline history, not to declare new M6 behavior equivalent to M5. Published35c source/review/browser/runtime receipts and recovery refs remain retained; packet reports the peer never selected/fetched/built/deployed35c, so no extra consumed-state boundary requires preserving its superseded implementation in the final series. A nonancestor preview SHA is not called literally merged.

Migration conclusion: NO MIGRATIONS. Independently inspected the complete changed-path inventory; it contains no migration/schema/seed/persisted-format change. Existing template migration files are unchanged baseline content. No transitional migration or merge/release/deploy/external-use migration boundary needs retention.

Repeated-update conclusion: no feature dependency/channel/input/lock/generated-pin update streams occur in the complete five commits, repeated or otherwise. No feature version/dependency manifest/lock update is present. Upstream0.31 metadata is baseline provenance; the earlier session-only preview lock refresh remains outside this feature series. No redundant pin commit is retained merely because it was published or previewed.

## Evidence and remaining verification

Read the scoped owner0 final51/0, owner1 search/shared55/0 and owner4 OAuth/ordinary-auth120/0 receipts/log results, inspected their meaningful tests and current asset coverage. Packet reports all three existing asset scripts pass. Batches overlap and are not summed. Initial fixture/Host/layout failures remain preserved with scoped corrections; no whole32-case rerun is falsely claimed.

Read exact-final command identity and actual fresh packaging/profile log: a06b0cfa/treeed2764be, make doc,3 extracted-gem packaging+7 mounted-profile examples=10/0, seed50232,11.4075s wall. Current before/after protected inventories contain2,148 equal hashes; I compared those inventories, not rehashed every protected input in this review. No input/dependency refresh occurred. Historical graph/proof remains scoped to its actual source.

Pending on actual final M6:
- Fresh stable loaded-runtime/source-gem capture and browser acceptance for full previewhost/api.vpsfree.cz title fit, unchanged widths, one direct menu, keyboard/touch/theme/account, visible singleton choices, scroll/copy, dotted navigation and page/table/code overflow at390/768/1024/1440.
- Real browser cache/key/neutral/BFCache/fallback behavior at M6; prior35c UI/cache/copy evidence is historical and does not certify the new source. Controlled BFCache handler evidence is not native BFCache proof.
- Required final documentation/asset/ordinary test matrix, including actual Ruby3.2/3.3 after the inspect-expectation repair, with any prior CI reuse bound to exact unchanged files/input graphs.
- Installed dynamic snippets, Python packaging/encoder scope as needed, generated Go/TS wire and Rust development/MSRV runners under the settled reuse plan.
- Deterministic and all-client/both-detail/both-scaling performance plus exact f6-to-final paired campaign through the neutral harness, with unchanged calibrated runtime/budgets/reference and new fixture/source identities.

Real-provider HTTPS authorization/callback/token/revoke/expiry/re-login, actual consumer cleanup/scope behavior and dedicated-client editable account entry remain UNVERIFIED. Synthetic cookie/Rack and120/0 unit evidence do not pass them. Local TLS/private fixture activation remains unauthorized; peer coordination/testing belongs to lead and that peer. Keep switch_user false until its documented precondition is actually observed.

No source/report/input files were written by the reviewer. No tests/builds/dependency installation, auth/browser/HTTP/provider probe, peer contact/access, remote/Git mutation, service or lifecycle action was performed. All commands used for inspection returned; no owned command remains.

Lead may save/reconcile this report and continue the already authorized validation phase under ordinary policy. There is no additional user confirmation or new review framework requested. Material future contract/source changes require only affected lanes; narrow direct remediations use the skill's focused-verification rule. Pending gates and separate integration approval remain.

Stable portal:https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
