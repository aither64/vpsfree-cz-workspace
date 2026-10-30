# Independent review of committed checkpoint 82a7f2ab

Reviewed range: `2f5156262baaf137800c17a9321e617c2b5df1d5` ..
`82a7f2abcc1ecfc361097d30de39e93aca026d64`.
Tree: `88c140470b161a66237ae891cae7e1be197677e1`.

Reviewer: retained `reviewer0`, read-only, `gpt-6.1-sol` / `xhigh`, native thread
`01a18193-44f5-7741-8b6e-6893a0e7f14d`. Reviewer independently verified the
thread-bound session, live roster and native model/effort. No overrides,
fallback or nested reviewers. All four mandatory lane references and applicable
guidance read. Overall risk high. This report was returned through the session
channel and saved by the lead; the reviewer made no file writes.

This review covers the completed checkpoint, not subsequently requested
milestone4 search caching/navigation/layout changes. It supplies no merge,
deployment or lifecycle approval.

## Findings

No Blocking findings in this snapshot.

**Important R1, risk/general: invalid callbacks clear an existing OAuth
documentation session without valid state or sign-out CSRF.**

Commit `ef3e5ae933d78d87b7501bf38e60d21c55a2ac0b`,
`servers/ruby/lib/haveapi/documentation_oauth.rb:181`, failure rescue at line
207; contrast CSRF-protected logout at line 212. Missing pending state raises
Failure, whose rescue unconditionally clears the authenticated session cookie.
An unsolicited top-level GET to the configured callback, or replay of a
successful callback, therefore signs out an existing reader without knowing
state, code, token or CSRF nonce. It loses the documentation session; it does
not reveal a token or bypass API authorization. The unconfigured HTTP preview
is unaffected.

The reviewer confirmed this on the exact head using an in-memory extension of
the existing OAuth RSpec group: sign in; verify admin identity; request callback
without parameters and with a foreign Referer; observe 400 and session
`max-age=0`; request docs again and observe lost identity. Token transport was
called once. One case passed in 0.204s, proving the undesirable behavior. No
network provider, TLS listener, dependency preparation or source edit occurred.
Existing replay coverage checks response/exchange count but not preservation
of an existing authenticated session.

Smallest fix when OAuth work resumes: preserve an existing authenticated
session on callback failure, while still consuming pending state. Add focused
unsolicited/mismatched/cancelled/replayed callback regressions and retain valid
failure responses and successful CSRF-protected logout. No new store or OAuth
subsystem is needed.

**Decision:** respect the user's explicit hold on all further OAuth work and
activation. Keep R1 open and defer the narrow fix until that work is resumed.
This blocks OAuth rollout/integration and is not correctness acceptance.
Authorized unconfigured/non-OAuth verification may continue after findings are
recorded. No other concrete advisory change requests were raised.

## Lane conclusions

General: the snapshot implements the original redesign and recorded user
additions: resource pages, example detail/variants/preferences, themes, shared
shell, directory/breadcrumbs/action tracking, client inventory, validators,
identity/visibility and bounded metadata search. Reviewer inspected routes,
templates/assets, adapters, authorization/context boundaries, tests and guides.
No further non-OAuth defect found. HTML GET selection remains separate from
OPTIONS/action dispatch. Parameter anchors match result links. Native/no-JS
and error fallbacks remain. Protocol text/schema are not rewritten.

Architecture: HaveAPI owns rendering, Context, search/presentation and optional
docs authentication. Client IDs/availability remain authoritative; class-owned
language metadata avoids a second behavioral registry. Generator adapters own
their emitted syntax and retain request resolution/validation. Search/nav use
the same authorized request description, not the complete private generator
model. The resource snapshot cache is request-local, keyed by raw identity and
canonical path, preserving copying/isolation. No cross-user cache exists in this
reviewed snapshot. Static library URLs are presentation data. No additional
architecture finding.

Scope: reviewer compared actual user requests/additions, 103-file +5233/-700
diffstat, recorded delivery and concrete preview milestones. The records do not
support a reliable uninterrupted active-work clock or elapsed-time stall
conclusion. Surviving mechanisms match explicit scope: no SPA, executor, search
service, refresh flow, database session store or OAuth-provider protocol change.
Conventional HTML search, Net::HTTP and ActiveSupport are proportionate. R1
must not expand into speculative hardening. New reusable client-side search is
outside this report and remains with the architect.

Risk/compatibility: R1 remains open. Otherwise cookie injection is confined to
version HTML GETs, uses requested-version ordinary auth/hooks, preserves
explicit credentials and excludes OPTIONS/actions. Purpose-bound encrypted
cookies keep tokens out of UI/preferences. Search excludes defaults, examples
and validator values, and the browser reconstructs safe text/links. Context
detail is additive for old adapters; updated built-ins require its reader.
Request contracts, schemas and persisted API state are unchanged. Rollback to
older code removes optional OAuth config first; older UI ignores preferences.

Actual consumers inspected: HaveAPI renderer/profile/generator interfaces;
same-session vpsAdmin `08c3bd7e3cb4dc324a0381df6a1eec190daab1a7` with
`haveapi ~> 0.29.9`; its Basic/Token/OAuth chain and access-token resume path;
canonical client manifests/docs. The Go client is generated by HaveAPI and is
consumed by the Terraform provider; these request contracts and pins are
unchanged. vpsAdmin application code is unchanged. Candidate source needs
explicit matching dependency selection, not merely a mount. No other session
records, team or cluster accessed.

## History, migrations and update streams

Complete reviewed series:

1. `b6a60aa7461af957bdb16e5b44dbb5a2a723df15`: core/dynamic examples.
2. `2053a5b2aefc7d2b52089e7a7a4ca49425b4ef8f`: generated adapters/fixture.
3. `4fc31687079303a66c3340ddce3fb5684a798ed9`: final reference UI/search.
4. `ef3e5ae933d78d87b7501bf38e60d21c55a2ac0b`: optional OAuth.
5. `82a7f2abcc1ecfc361097d30de39e93aca026d64`: performance/cache.

Tests/docs stay with behavior; common shell/DOM/search/browser wiring is a
coherent UI contract. Core, generated adapters, auth and performance are
separately reviewable. No obsolete Python-wrapper/layout/filter iteration or
fixup-only history remains. Earlier iterations survive in recovery records.

Reviewer independently checked original `e60bbd01` and first consolidated
`0ac34505` share tree `07dc4d2230e71745206da765d507097e3883e0db`; original,
consolidated and first refreshed feature patches share stable patch ID
`a0f9c53c1a6faa68eb8a43fd3f5cb5092cfad212`. Upstream `2fc2b8f8..2f515626`
and its application `0ac34505..415fc521` share patch ID
`d5ecc78bf488e8bf2637c0d4e9c1a0056a50f178`; prior five range-diff pairs are
equivalent. Complete old `0babefa4` and reviewed `82a7f2ab` share final tree
`88c140470b161a66237ae891cae7e1be197677e1` and aggregate patch ID
`24fa442b950e4ffe0c43a8cf9acedf525ad64a55`. Final receipt/provenance folds
user additions and explicit-thorough Go fixture into their owning groups.
OAuth module/provider-reader/specs/guide stayed unchanged during that refresh;
controls restore on the final identity template. Recovery refs and dirty-source
preview receipts retained; no nonancestor preview SHA called literally merged.

**No migrations.** Original/refreshed/final changed-path inventories contain no
database migration, schema, seed or persisted-format change. JSON-schema sidebar
is presentation only. No transitional migration or external-use boundary needs
retention. **No repeated dependency/channel/lockfile/generated-pin streams.**
No feature release/default integration/external SDK publication evidenced.
Worktrees clean. Local upstream is `2f515626`; reviewer did not fetch or claim
fresh remote readiness.

## Verification limits

Owner quick checks and exact-head package 3/0 are evidence, not rerun wholesale
by the reviewer. Inspected coverage includes isolation, mounts, search
escaping/ranking/caps, semantic validators, snapshot ownership, strict old/new
performance shapes, replay/body proofs. Fixed budgets/reference/runtime and one
root GET remain; a smaller overview does not prove faster resource rendering.
Unrelated-resource and selected-action scaling remain required.

Pending: full emitted compilation/wire, frozen all-client/both-detail and both
scaling gates, exact baseline/candidate paired performance, final committed-source
preview refresh and full browser matrix. Dynamic installed-package acceptance
extracts thorough panels by default; simple fragments have focused syntax/type
and shared-body coverage. Do not claim equal real-wire coverage without evidence.
Current screenshots bind dirty-source captures, not final committed runtime.

Real-provider HTTPS authorize/callback, revocation, expiry/re-login and rollout
remain **held/unverified**. Stubbed security tests do not replace them. R1 and
held integration prevent declaring the whole branch OAuth-ready. With R1
explicitly recorded/deferred, authorized non-OAuth verification may proceed.
Milestone4 requires applicable affected-lane and updated whole-history review
after its committed implementation.
