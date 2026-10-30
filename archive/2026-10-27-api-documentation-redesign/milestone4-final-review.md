# Independent final review: milestone 4

Report supplied by reviewer0 through the lead channel before the user's pause;
saved by the lead after explicit resumption. This preserves the report's reviewed
range. Later narrow R2 remediation and lead verification belong in an addendum,
without changing the original finding or pretending the old split was correct.

Reviewed exact HaveAPI range
`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0..ab5b11188941d1c8c918951cdee162e9aa9f68cf`;
final tree `c3c3e04337bcf9669dbb79611d72a65c686af9e0`, clean source/index,
110 files +6488/-711. Repository/worktree: `git@github.com:vpsfreecz/haveapi.git`
at `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi`.
Paths below are relative to that worktree. Prior `final-review.md` remains the
separate 82a7 snapshot report.

Identity and workflow: independently checked session-local dev-session current
== 2026-10-27-api-documentation-redesign, both DEV_SESSION identity variables
absent and trusted exact binding matches. Live same-session roster verifies
reviewer0, review purpose, ready, saved read_only, gpt-6.1-sol/xhigh and native
thread 01a18193-44f5-7741-8b6e-6893a0e7f14d. CODEX_THREAD_ID and own native
session_meta/turn_context confirm that identity and actual gpt-6.1-sol/xhigh.
No overrides, replacement or nested agents. Applied mandatory-change-review
with all four complete lane references and applicable workspace/repository
guidance, plus retained documentation/security/writing guidance. Risk HIGH.

## Findings, in severity order

**Blocking R2 — C cannot load without the later optional OAuth commit
(general/history, architecture).** In C=d25dd61260a5768552bac5f6a8a201bb4c28d540,
servers/ruby/lib/haveapi/server.rb:11 requires haveapi/documentation_oauth;
:338–345 defines documentation_oauth; :468 registers DocumentationOAuth::Helpers;
:609 mounts the client. Yet git ls-tree d25dd612
servers/ruby/lib/haveapi/documentation_oauth.rb returns no entry. That file is
introduced only in D=6049fc333e57baca4c97e9eb482f0c6b332041ba. D has no server.rb
delta. Therefore loading the Ruby server at C raises LoadError before its UI can
run; C also depends on a constant that has not been introduced. The final tree
has all files, so final-tree equality and passing final-head packaging do not
detect this broken commit boundary. The advertised independently reviewable
UI/auth split is not currently valid. C's documentation_helpers.rb correctly
calls ordinary authenticated? before D, demonstrating that these four server
seams belong to D rather than the UI contract. The previously reviewed
C=4fc31687 did not contain these OAuth server seams.

Smallest fix: redistribute exactly the existing server.rb require/configuration/
helper-registration/mount hunks from C into D. Preserve the final tree, held
OAuth implementation/provider/spec/guide objects, accepted messages and input
graphs. Do not fix R1 or otherwise resume OAuth work. Rebuild the affected
history with ordinary hooks, verify C has no reference to the absent optional
module and can load through its ordinary provider path, verify D owns the
complete optional integration, prove final tree/aggregate patch equality and
updated complete five-commit boundaries. Keep earlier refs/receipts. This is a
narrow history correction; lead focused inspection/proof suffices under the
skill's narrow-fix rule if no design/final-source change is introduced. R2 must
be resolved before long integration gates or branch-readiness claims.

**Important R1 — invalid/missing/replayed OAuth callback clears an existing
valid documentation session without logout CSRF (risk/general), carried OPEN
from final-review.md.** Current D=6049fc33,
servers/ruby/lib/haveapi/documentation_oauth.rb:181–189 and :207–209;
CSRF-protected sign-out at :212–219. An unsolicited callback GET fails
pending-state validation, then the rescue unconditionally expires the
authenticated cookie. Prior local Rack proof demonstrated admin sign-in ->
unsolicited callback GET 400 with session max-age=0 -> signed-out next page;
no token disclosure or API-authorization bypass was shown. Current module,
complete provider subtree, both OAuth specs and owning guide have exactly the
same Git objects as 82a7, so that finding/proof remains applicable. No new auth
probe was run.

Disposition: user's explicit OAuth hold remains controlling. Defer the existing
narrow source fix until resumed; keep R1 open and block OAuth rollout/integration.
This is not correctness acceptance. Unconfigured HTTP visual behavior is
unaffected. Do not initiate provider/TLS/private-fixture/cross-session work. The
existing recommended fix remains preserving a pre-existing valid session when
a callback fails while consuming only pending state, with focused preservation
regressions when resumed.

No other Blocking, Important or concrete Advisory change request found in the
final source. Pending acceptance gates below are not reported as passed.

## Distinct lane conclusions

General: Inspected final routing, search extraction/fallback/cache dispatch,
JS validation/loading/matching/reset/rendering, account/theme/current-resource
markup, validator tables/CSS and meaningful focused coverage, plus complete
commit series and input/history receipts. The final non-OAuth implementation
matches the original redesign and later additions. Placeholder,
resource-first/action-second/parameter-third priority, native GET fallback,
mounted URLs and parameter anchors remain consistent. Current resource appears
above its action navigation. Account/visibility/status placement is separated
without altering existing link/form/CSRF hooks. Validator subtable preserves
typed values, message/unknown metadata fallback and escaping; outer column
selectors now target direct cells. The focused profile correction appropriately
moves action prose/sample assertions to resource pages while preserving overview
initialization/package assertions and admin/member/locale/adapter-input coverage
at both details. R2 prevents accepting whole-branch readiness despite the correct
final tree.

Architecture/repetition: HaveAPI remains the owning provider for document
metadata/presentation and generator-gem adapters. Search Index is a deterministic
whitelist projection with parent indices, not a second declaration registry or
private generator schema export. Ruby fallback and JS suggestions consume that
same projection; representative shared ordering fixtures address the deliberately
duplicated small matching rule across languages. No framework/service/server
historical snapshot cache is introduced. Browser loader deduplicates concurrent
forms and retains one document's loaded representation; ordinary private HTTP
caching owns cross-navigation reuse. C/D server integration boundaries need R2.
Core/adapters and E request-local Context ownership behavior are patch-identical
to the previous reviewed groups; no additional ownership or abstraction finding.

Scope/proportionality: Compared plan.md's verbatim original user request,
recorded visual milestone4 decisions and phone/tablet requirement with actual
110-file +6488/-711 range and milestones. The prior review ended at 82a7
(12:02+01); milestone4 owner delivery commits are 13:14–13:17+01, followed by
source/input/history refresh. Those timestamps show observable delivery but are
not an uninterrupted active-work clock; do not infer a stall from them. The user
explicitly rejected repeated whole-API downloads. Compact whitelisted data,
parent references, lazy loading and ordinary HTTP caching meet that request
without a SPA, persistent JS index, service worker, Cache API, permission-revision
framework, live polling or shared server cache. The documented page-snapshot
freshness is a bounded contract; do not harden it into speculative instant
revocation. O(metadata) projection work on versioned HTML is intentional and
must pass the existing budgets. No additional subsystem-removal request. R2 is
an actual incoherent commit boundary, not a line-count concern.

Risk/compatibility: New retained metadata boundary reviewed directly.
render_version_documentation authenticates through the existing HTML seam and
describes once before index dispatch. Index extraction lists only names/labels/
types/paths/aliases/method/direction/provider context, excluding prose, defaults,
examples, validators, identity, token/CSRF and generator-private models. Key
includes format/version/mount/locale/visibility and projection content. On a
cold/conditional network request, current auth and current key equality precede
cache success; mismatch is 409 without data. Matching keyed responses alone can
be private/max-age=86400/immutable with ETag and merged Cookie/Authorization/
configured-locale Vary. Bootstrap, errors and detected Set-Cookie changes stay
no-store; normal full HTML is no-store. Existing request-local Context resource
cache remains separate from this HTTP representation.

Browser code validates same-origin canonical representation configuration, one
inert JSON script, envelope/format/version/base-path/key, row shapes/parent
bounds/direction and valid scalar strings. It builds URLs from the known base
with query APIs and text with DOM APIs, rather than adopting response HTML. It
never accepts an arbitrary metadata URL. Pending loads deduplicate, document
generation guards suppress stale suggestions, reset aborts/invalidates old
completions, and pageshow.persisted forces a no-store current bootstrap on next
intent. Neutral pages use current with no fabricated authorized view or extra
render-time discovery. Open-page staleness and private HTTP cache retention are
explicitly documented and accepted; destinations reauthorize. R1 remains open in
held OAuth. No new data migration, machine coordination, wire request change or
rollback data conversion is introduced. Rolling old/new UI/asset workers may
produce a cold/error fallback; prior code ignores new display/index choices.
Remove optional OAuth configuration before rolling back to code without it; no
instant browser-cache erasure is promised.

## Actual consumers and input boundaries

Reconfirmed same-session vpsAdmin at clean
08c3bd7e3cb4dc324a0381df6a1eec190daab1a7. Both api/Gemfile and
packages/api/Gemfile retain haveapi ~>0.29.9. No application/pin change is in
scope. The retained API bootstrap uses HaveAPI::Server and existing Basic/Token/
OAuth providers; generator consumers remain the HaveAPI-owned Go/Rust/TypeScript
adapters. Prior actual Go-client/Terraform discovery is retained only for its
unchanged request-contract scope. No other session records/teams/clusters were
inspected. Preview still needs explicit five-source-gem version/path selection;
a mount or a different bundle's success is not proof. Existing preview is an
older HTTP snapshot, not final ab5b acceptance.

Independently compared current prepared Ruby locks to the retained before locks:
server, Go documentation acceptance and Rust differ only in expected local PATH
versions/internal HaveAPI constraint and owned checksum labels; external graph/
checksum/platform/Bundler text is exact. Root tools lock is unchanged. npm
package-lock is exact except local package versions. uv.lock is exact except
editable haveapi-client 0.30.0 -> 0.31.0. Rehashed all 310 inputs from the
final-fold input manifest against actual session files: all match, no missing/
changed files. This includes preserved external runtime/MSRV/frozen/preview
boundaries; it is input proof, not test-result reuse.

Read loaded-identities evidence: server/Ruby-client/Go/Rust/TypeScript local
sources are 0.31.0 under this checkout; root/server/Rust JSON 2.21.2 and distinct
Go acceptance JSON 3.1.0 remain separate, Rust gem home isolated with Fiddle
1.1.8. Local JS build/install/runtime and Python editable metadata report 0.31.0.
The prescribed published TS runtime remains 0.30.2 with bundle SHA256
96450c40a55ec7b7af4fca903d045bd0fc7ba1216efe12c3fee9b3e6a09e9198,
distinct from local source. Independent Rust 1.95 MSRV and development 1.99
remain distinct. Frozen benchmark declarations/locks/budgets/reference are
unchanged. No source-only rebase relabels the old 0.30 runtime as new verification.
Upstream 0.31 metadata follows its existing baseline; no new feature version/pin
update was introduced.

## Whole history, equivalence, migrations and update streams

Reviewed all five current commits: A4363d111, B260e3ea8, Cd25dd612, D6049fc33,
Eab5b1118. Independently verified A, B and E full-index patches are byte-identical
to prior reviewed counterparts b6a60aa7,2053a5b2,82a7f2ab. C owns final UI/search/
control/table changes and the profile route test adaptation. D's implementation
is unchanged, but its four server integration seams were mistakenly retained
in C: R2 means the full series is not currently independently executable/
reviewable as advertised. Final-tree equality cannot certify that property.

No superseded monolithic-layout/Python wrapper/per-query HTML-enhancement
iteration or fixup-only feature commit remains; new compact search replaces
the prior enhancement directly. That obsolete-history consolidation conclusion
is separate from R2's misplaced seams. Existing test fixture JSON is test data,
not a dependency or behavior registry.

Independently reconstructed comparisons from Git (read-only): 09ef7905 and
same-base consolidated 4f80b23c both tree
0f551c74ceb590cdff9b19980fc480ceb9d314e5 with empty inter-head diff. Both
feature aggregate patches and refreshed f6e5c375..a0c78d1c are byte-identical,
SHA256 ea0f7ef5d5f57278ff21a439156e7684c869a55b7171fd67da503e59e0d1d5f6.
The actual 4f80b23c..a0c78d1c final delta equals 2f515626..f6e5c375 upstream
delta byte-for-byte, SHA256
426ab56641ee6c91a1cc596a5d46f318eeaff081b6a2d0bb6f64d8ec85c96cf3;
five range-diff pairs are '='. Upstream's 24 paths do not overlap the prior
feature's 109 paths. The final accepted profile-test delta a0c78d1c..ab5b1118
has SHA256 74ddf85e523065f7a245b00e70457a76936191377986330149a38ce904e8ce23.
c5badd08 and final ab5b1118 have identical c3c3e043 tree and empty diff. Current
feature aggregate SHA256 is
2907070a7852ee24c31fa8efe9572c0a6336ae4ac21cc8823ce8f502179039c1.
Earlier original/refreshed range proofs and recovery refs remain preserved; no
rewritten nonancestor runtime head is called literally merged.

Inspected original-owner four-partial Basic/final restoration receipts and
current C->D control diff: auth-method/form/CSRF/link behavior is restored without
a new OAuth flow. The zero-fuzz projection receipt certifies those partials, but
does not catch the separately misplaced server.rb seams. R2 requires an updated
whole-series ownership proof. Do not overwrite old receipts to conceal it.

No migrations: current full base-to-head path inventory contains no database
migration, schema/seed or persisted format change; no transitional lineage or
migration merge/release/deployment/external-use boundary needs retention. No
repeated dependency/channel/lock/generated-pin update streams in the complete
feature series. Upstream release/version synchronization is baseline provenance,
not feature churn. No feature release/default integration/external SDK publication
is evidenced; retained HTTP captures remain preview provenance. No fresh remote
readiness claim: this review performed no fetch, push or integration.

## Verification gaps and disposition

Read actual final-head extracted-gem log: ab5b1118/treec3c3, haveapi0.31.0,
3 examples/0 failures, 9.75s wall, seed60317. Read the original 51-example focused
failure receipt and narrow corrected profile7/0 receipt; the other 44 successful
cases retain only their proven unchanged-file/input scope, no whole-batch rerun
is claimed. Owner focused UI56/0, search28/0, three asset scripts and lint/ERB
receipts provide pre-review evidence. I inspected the relevant coverage and did
not rerun broad checks. The evidence helper's missing FileUtils is a separate
preparation issue and does not alter final application bytes or these conclusions.

Still unverified: complete final documentation/asset target; Python encoder and
installed local npm+wheel/sdist snippets; generated Go/TS wire and Rust
development/MSRV acceptance; deterministic performance; all-client/both-detail/
unrelated-resource/selected-action scaling; exact refreshed baseline f6e5c375
versus final candidate paired quick performance through the neutral harness;
final-source HTTP preview/source-gem graph; real browser cold/warm cross-navigation
HTTP-cache request counts, changed/mismatched keys, neutral/BFCache reset and
390/768/1024/1440 touch/keyboard/theme/overflow/code/validator acceptance. Unit
loader tests cannot prove actual browser caching or viewport geometry. New
projection allocation must meet the unchanged performance gate; smaller overview
work is not evidence of resource-render speed. Dynamic installed harness still
defaults to thorough panels; do not claim identical simple/thorough real-wire
coverage without evidence.

Real-provider HTTPS OAuth/callback/revocation/expiry/re-login remains
HELD/UNVERIFIED, never passed by stubbed proof or unconfigured HTTP preview. R1
deferral remains explicit and does not waive it. R2 blocks long gates now; after
the narrow seam/history correction is independently inspected by lead and
recorded, authorized non-OAuth gates can proceed without a redundant full review
if final source/design/input scope is unchanged. Material final-source/cache/auth
contract changes require the relevant affected lanes. This report supplies no
merge or deployment approval. Session remains open.

No source/report/input files were written, no dependency installs, auth probes,
browser matrix, compiler/integration/performance gates, merge/deploy or lifecycle
action was performed by the reviewer.

## Reviewer preparation addendum

After independently reading completed
`verification/quick-packaging-ab5b1118/receipt.md` and
`performance-ab5b1118/receipt.md`: exact f6e5c375 baseline/ab5b1118 candidate
exports and generated docs are now PREPARED, with neutral harness and frozen
availability identified. Retained gem SHA256
a6bb22115c557b6733dd3d30efa52c9f3e7f0f15e03865f248c03cf675431820
is the already-tested 0.31.0 package; corrected FileUtils metadata stage reused
it without rebuilding/repeating packaging. Corrected metadata/export/availability
operation passed13.313s; calibrated benchmark Ruby
`/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby` and71 available
specs/noHaveAPI remain separate from component graphs. Receipt reports2148
protected hashes unchanged; reviewer personally rehashed the310 current-fold
subset earlier (all equal), not all2148. Availability/archives are preparation
only; no pilot/measurement/scaling/compiler/wire/gate is passed. Retain all
pending measured/runtime/browser acceptance limits and R2 hold. All requested
lanes are complete; R2 narrow correction remains with main/owners, R1 open/held.

Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/

## Lead narrow-remediation addendum after resumption

Blocking R2 is resolved by direct inspection under mandatory-change-review's
narrow-fix rule. New range is the same base
`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0` through
`9f68dad5436799d82e9c9e1c69e73866a279e9a6`. The final tree remains
`c3c3e04337bcf9669dbb79611d72a65c686af9e0`, with no final-source/input/design
change. A/B remain exact; C is `0f0399141d23cfecc33f7ba209e5acacc81e60c2`,
D `aafcfa0975ee0d19a57797b5e7c4c9150a8a38a5`, E the new head. Existing
independent source/lane conclusions remain applicable; no redundant broad
review was requested.

Lead independently verified the old/new final empty diff; committed C's server
hash equals the original owner's Basic projection and contains no optional
references/module. The actual C-to-D diff now adds the exact require, complete
configuration/accessor, helper registration and mount blocks, plus the HTML
authentication helper switch. Actual D server matches the owner's pre-E restored
projection. Both clean committed snapshots pass isolated require and mounted
overview/resource Basic documentation smoke (200 each), with loaded paths bound
to their own snapshots, Basic provider exercised twice, C loading no optional
module and D loading its own unconfigured module. Lead read the source-bound
smoke JSON and actual committed diff. No module was borrowed from the final tree.

The remediation receipt
`history-R2-server-split-20261028t135920z/receipt.md` preserves original-owner
projection/replay, staged and committed proofs, failed temporary fixture setup
logs, successful smoke logs, normal C/D/E hooks, final-tree/aggregate equality
before atomic move, E patch identity and all 2,148 unchanged protected hashes.
All previous refs and incorrect intermediate-split receipts remain historical.
No migrations or feature update streams were introduced. Current complete
five-commit series now satisfies R2's requested ownership/loadability boundary.

R1 remains OPEN under the user's OAuth hold. Non-OAuth acceptance gates and
the separately selected final-source HTTP preview/browser verification may
proceed. This addendum supplies no default-branch integration, publication,
production deployment, OAuth activation or session lifecycle authorization.

## Subsequent user authorization

After the historical report and R2 closure, the user explicitly authorized
coordination with `2026-10-24-vpsadmin-haveapi-upgrade`: this session supplies
development HaveAPI and fixes bugs; that peer updates vpsAdmin and deploys its
HTTPS development cluster for OAuth testing. No HaveAPI releases. This
supersedes the prior implementation hold for the assigned narrow R1 fix and
agreed account UI/flow; it does not alter the original review finding or claim
the fix is already complete. Local private TLS/OAuth fixture activation is not
part of the new plan. R1 remains open until focused remediation evidence.
