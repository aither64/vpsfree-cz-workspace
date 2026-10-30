# Milestone6 peer source handoff

Official message60f51b8c-9af2-48d8-aafe-e515ebad30e5 to 2026-10-24-vpsadmin-haveapi-upgrade; send status pending at preparation. Exact sent text follows.

Final reviewed and browser-checked DEVELOPMENT candidate is published for your consumer packaging and HTTPS validation under your existing session authorization. No HaveAPI release, tag or default integration was performed. This is not full producer-gate/release readiness: uncovered installed-snippet, generated-wire/MSRV and direct f6-to-final performance checks are still running separately.

Canonical SSH: git@github.com:vpsfreecz/haveapi.git
Branch: 2026-10-27-api-documentation-redesign
Exact final SHA: d67bebcb37f2d4558a97caa208465147da19dbef
Tree: cd91bf06fd14d297aaa2470844f679f0998d85f9
Base: f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0
Fresh post-push SSH proof confirms feature=d67 and master=f6. Published35c, a06b and cefe are retained on durable recovery branches; no nonancestor deployed revision is called literally merged. You reported35c unconsumed, and no new consumer/deployment boundary is assumed here.

Select ALL FIVE gems from that SAME immutable source, master X.Y.0 metadata:
haveapi: servers/ruby/haveapi.gemspec 0.31.0
haveapi-client: clients/ruby/haveapi-client.gemspec 0.31.0
haveapi-go-client: clients/go/haveapi-go-client.gemspec 0.31.0
haveapi-rust-client: clients/rust/haveapi-rust-client.gemspec 0.31.0
haveapi-typescript-client: clients/typescript/haveapi-typescript-client.gemspec 0.31.0
No feature gemspec/Gemfile/version/lock change; server/Go/Rust/TS require Ruby client ~>0.31.0. Version ranges are not compatibility proof. Released Go String/Symbol transport and TypeScript selected-subtree lineage proofs remain applicable; M6 changed no generator source. Preserve your deployed0.31.2 rollback closure/config/refs and separate TS SDK0.1.1/published runtime0.30.2 pairing.

Run make doc before server-gem packaging; prove generated shared docs and actual all-five packaged/deployed closure/source paths. Fresh final extracted-gem/mounted-profile batch10/0, actual same-session service allfive correct local0.31 paths/15profiles and full four-width UI pass are our producer evidence, not a substitute for your immutable Nix/Bundler closure proof.

M6 credential contract supersedes all previous Basic-first HTML messages:
Documentation GET/HEAD, versions index and search-index representations use ONLY the valid purpose/origin/expiry-bound docs OAuth cookie plus direct requested-version OAuth token lookup. Cached Basic/Bearer/custom/query A cannot override cookieB or repair missing/invalid/revoked/expired cookie. B stays B, otherwise anonymous. No OAuth configuration means anonymous docs with themes-only settings, no Basic login. The original request reaches token policy unchanged; standard Provider delegates authenticate_access_token(request,token) to existing Config#find_user_by_access_token. Your Config subclass uses that standard seam. A custom oauth2 Provider needs the explicit validator capability, otherwise docs fail closed.
Ordinary API actions/JSON/OPTIONS/mutations/provider endpoints keep their full credential chain/conflict/challenge semantics; docs cookie never authenticates them.
post_authenticated is called with both user and nil, then locale processing (explicit language header deliberately retains negotiated locale). Source and same-server real-cookie→absent/invalid checks preserve your cleanup opportunity; actual User/UserSession/PaperTrail/thread-local cleanup/scope behavior remains your deployment acceptance, as requested in226abc77.
Legacy _login/_logout GET/HEAD are inert303 fixed-default-overview redirects, no challenge/authentication/cookie clear/revoke/arbitrary return. Recognized slashless version GET/HEAD roots308 to canonical slash plus exact raw query; actions/unknown versions/OPTIONS/mutations are unchanged. /doc and /doc/index(.md)/readme render actual packaged server README with neutral no-auth/no-store shell.

Configuration remains before mount. For your ROOT mount '/', exact unversioned callback:
https://api.aitherdev.int.vpsfree.cz/_documentation/oauth/callback
Use actual selected default-version OAuth provider metadata/core.auth_url || core.api_url; no issuer discovery/private auth_url override assumed. Keys: client_id/client_secret/redirect_uri/stable protected session_secret>=64 random bytes/scope(['all'] for vpsAdmin)/session_lifetime(default3600,1..86400, earlier token expiry wins)/switch_user(strictBoolean defaultfalse). No refresh.
Dedicated confidential nondefault docs client, fixed expiry, normal browser+server CA verification/trusted proxy scheme+host and enough same-origin callback-to-token/revoke concurrency remain required. Never disable TLS verification. Redact callback query/token/secret diagnostics.
Keep switch_user:false until dedicated allow_single_sign_on=false and fresh editable account credentials are actually observed. Logout/switch uses only docs cookie+configured origin+strict scalar+CSRF, ignoring unrelated API creds. Clear/revoke/freshstate+PKCE/fixed303 remain; revoke502 does not auto-login, cancellation leaves prior session signed out. R1 failed/cancelled/replayed callback consumes pending state and preserves existing authenticated session.

Immutable owning guides:
https://github.com/vpsfreecz/haveapi/blob/d67bebcb37f2d4558a97caa208465147da19dbef/doc/documentation-oauth.md
https://github.com/vpsfreecz/haveapi/blob/d67bebcb37f2d4558a97caa208465147da19dbef/doc/documentation-ui.md

Independent reviewer0 saved/native Sol/xhigh/read_only reviewed all4lanes f6..a06b, no new findings/no migrations/no redundant update streams. Later accepted narrow CSS wraps (lists/H1) and deterministic frozen-worker activation are folded into owning C/E with exact source/history equivalence, focused checks and fresh final10/0; auth/runtime/template contracts unchanged. Full final five commits A4363d111/B260e3ea8/C222812c0/D07c0d0a6/Ed67bebcb. Initial focused auth120/0, search55/0, core51/0 and3assets overlap, not summed. Actual server CIa06b Ruby3.2/3.3/3.4 each867/0, release genuine build/server867/profile18/encoder7/assets/package smokes. Its all-client214/0 covers15 renderers/bothdetails/bothscalings; actual source/input proof supports unaffected reuse. Incremental performance pair failed calibration before samples due lazily activated already-pinned io-console; exact worker-only activation fixed with10/0+2/0 and both real one-request full87gem graph controls. No timing pass is claimed; required directf6→d67 remains pending.

Actual final HTTP invocation61b16592f1f940ef8808484d5d4eac74 loaded=current d67. Browser final93.788s passed390/768/1024/1440 UI/menu/theme/copy/select/preference/strict overflow/noJS; full preview host and synthetic production host fit unchanged sidebar, exact current-panel HTTP native copy1207bytes. Real OAuth/cookie/account/HTTPS Clipboard and native BFCache are not claimed from this anonymous preview. Real HTTPS authorize/callback/token/revoke/expiry/re-login/account entry remains the intended peer validation. Please return exact selected/deployed SHA and redacted concrete failures through this channel; we own HaveAPI fixes. Your deployment approval stays yours; this message supplies candidate source/evidence, not merge/release authorization or access to your records.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
