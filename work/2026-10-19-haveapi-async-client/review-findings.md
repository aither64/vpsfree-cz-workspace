# Independent final review and remediation ledger

Reviewer0, retained Sol/xhigh/read_only; final review at HaveAPI ae0fe397 and
React e35f2720. No long integration has started. Review complete at these heads; all four lanes covered at HIGH risk.
Reviewer verified actual retained gpt-6.1-sol/xhigh identity/settings.
No Blocking findings, three Important findings, no separate Advisory findings.
Source freeze released for the bounded fixes below.

| ID | Severity/lane | Finding | Owner/status |
| --- | --- | --- | --- |
| R1 | Important/general | save/local snapshot loses AsyncResourceInstance Resource-valued input; ordinary server-returned association records also fail Resource input normalization | implementer1 implementing architect-approved local-attribute leaf/normalize fix |
| R2 | Important/general | inherited coerceParams scalar temporaries persist between fields; async Integer {a:7,b:'not-an-int'} sends {a:7,b:7} | implementer0 implementing per-entry existing coercion then one final validation |

R1 references: async/resource_instance.ts83-91 and async/resource.ts137-148,
async commit d6059a15. Direct action normalizes entity before snapshot; save
copies entity internals first. No HTTP after save rejection. Reviewer also
confirmed loaded owner:{id:3,_meta:{path_params:[3]}} fails an ordinary update.

R2 references: parameters.ts196-291; async/authentication.ts19-23. Source defect
also exists in upstream c14e7d3 parameters.js. Fix the new async surface without
silently changing legacy callback coercion. No broader validator rewrite or
new public mode flag is requested.

R3 — Important/risk+compatibility/general: request.ts84-92 drops RequestResult
when selected output namespace is missing; resource_instance.ts122-130 only
latches acceptedUnbound if error.response exists. HTTP201 + status:true +
response:{_meta:{}} rejects protocol then permits a second POST from the same
instance. Owner0 preserves validated success receipt through relevant payload/
namespace failures; owner1 covers guard/materialization with real bundle tests.
Architect confirms minimal definite-success boundary. Ambiguous transport
failures remain distinct; no generalized retry mechanism is introduced.

## Independent conclusions

Exact reviewed ranges: HaveAPI c14e7d3158b91c134c2817b489cd29772fc09f82..
ae0fe39738c3eb10019377d0fce95dc249cdfd16; React
7860521f30826c3886c89c35e8ab6f4e082e0a4b..
e35f2720683d0c63cd10d56b49864800b727b766. Original-base HaveAPI cb3f39f
ancestry includes protected already-upstream 82c9e77/c14e7d3 release work.

Reviewer explicitly accepts complete history: no obsolete unmerged approach,
fixup/tidy commits, abandoned suffix API or transitional source mode. Separate
callback fixture, TS migration and additive async stages are coherent; generated
JS/declarations stay with producing source stages. Source-path release repair
belongs to migration. WebUI's cohesive adapter/pilot commit is proportionate.

One TS/Rollup build dependency+lock introduction, no repeated/superseded pin
stream. Async changes package scripts/docs, not dependency resolutions. WebUI
locks/flake/hashes unchanged. Generated translation catalog unchanged. No
further consolidation required at reviewed heads. NO MIGRATIONS in either
repository, no database/on-disk/server-protocol/schema or transitional edits;
no supported externally consumed state/release boundary. No coordinated rollout
or data rollback needed.

Callback model/returns/throws/hooks/static constructors/loader shapes and usage
without Promise/AbortController preserved in inspected boundary. No broken
existing JS consumer identified. Shared ownership and independent async state,
fixed wrappers, nonthenability and separate completion fit design. Dictionary
policy is justified bounded compatibility seam. React shares one auth/session/
result policy, delegates wire handling, retains fetch default and isolates
candidate install; no unpublished dependency. Technical documentation is
accurate/discoverable and distinguishes fixtures from real runtime evidence.
No additional architecture/scope/auth-boundary issue found.

Reviewer independently reran callback18+async10 suites (28/28) and reproduced
R1-R3 through committed bundle with in-memory XHR. Verified old tar SHA256
46fd526ac02d04fdbc9526c7b7e67cdde0a5cfe730cf865702a4a2b4167bf991,
50 files and byte parity for JS+43 declarations. Trees/whitespace clean.

Remaining gates: fixes+quick regressions+direct lead acceptance, full JS/server
contracts, full WebUI unit/build, actual installed-tar types/Vite/browser proof
and three-engine UMD smoke, feature publication/CI/PR. Node minimum remains a
release prerequisite. No merge/release/deploy/readiness approval from review.
Use skill steps9/10: direct focused inspection suffices for narrow fixes inside
reviewed boundary; only design/public-contract expansion triggers affected-lane
rerun with same reviewer. Preserve original reviewed packet and bind revised
heads/range-diffs/remediation evidence separately.


## Accepted narrow remediation design and initial direct inspection

R1: preserve entity leaves only in local attribute copies, remove premature
new/save copies, normalize described Resource inputs once to their own declared
value_id/default id before scalar snapshot. Null/scalar semantics and generic
request/metadata clone/cycle rules unchanged. Path identity still comes from
path_params. Resource error maps retain safe null-prototype own keys.

R2: async validateParams constructs existing Parameters with empty input/safe
dictionaries; call existing coerceParams once per supplied own declared field,
merge coerced maps on same instance/typeErrors, and validate once against all
fields. No callback Parameters/coercion/policy/arity/shape edit or new mode.

R3: construct raw RequestResult after top-level envelope validation, before
metadata/payload/namespace validation; attach it to those protocol errors.
meta stays empty until validated; data may be undefined for absent payload.
No receipt for invalid JSON/top-level envelope/network failure; accepted-unbound
continues to require HTTP2xx and envelope.status===true. No retry redesign.

Lead directly inspected the focused R1-R3 source and documentation diff; it
matches the accepted seams with no public contract expansion. Required writing
pass applied to resource guide/error wording and raw-receipt guide. Callback
source diff absent. Await combined rebuilt-bundle regressions, normal commit/
fold, final head/range-diff/pack before final direct acceptance. Fix evidence
will retain original reviewed head and revised candidate separately.

## Focused verification before commit

Latest combined source/build checks pass: strict typecheck/build; callback18;
actual-bundle async36 (old10 + core12 + resource14); resource units11; both
emitted-declaration consumers; existing focused Mocha18. Baseline new fixtures
reproduced expected failures against the reviewed old bundle. Resource owner
independently reran its14 actual-bundle cases (323ms), plus unit/type gates.
Source fix tests use actual Parameters and fake XHR, covering repeated scalar
coercion/MFA/cross-field validation, resource IDs/snapshots and one-POST create
guards after missing payload/namespace/invalid metadata, with ambiguity controls.
Shared callback Parameters source unchanged. No integration has launched.

HaveAPI Git slot granted owner0 for exact own/peer-consented paths, normal hooks,
fold into owning unmerged async boundary, fresh SSH fetch assessment and final
committed-head package/byte/checksum receipt. Preserve original reviewed tar and
history evidence; update the new candidate separately. Commit/repack pending.

## Final direct acceptance of narrow fixes

Lead inspected final14-path reviewed-to-final diff, specific source fixes,
actual-bundle scalar/MFA/receipt regressions, resource tests and range-diff.
All findings resolved inside the originally reviewed contract; no API expansion,
callback behavior change, new dependency/mode/retry mechanism or migration.
Under mandatory review steps9/10, no reviewer rerun is needed merely to confirm
these direct fixes. Reviewed original head/packet preserved. Independent history
conclusions retained for unchanged boundaries and narrow folded async fix.

Final HaveAPI head: dc94157808966c12418b4009085fec237a869789.
Upstream remains c14e7d3158b91c134c2817b489cd29772fc09f82 after fresh SSH fetch.
Feature series: fixture34f431e, TS90722e0 unchanged; async8e331fe97819ad0a6591c754aaa270152c8d7564;
guidance dc941578. No obsolete fixup commit retained; normal hooks pass.
Lead verified clean index/tree and full-diff whitespace. WebUI head e35f2720
unchanged and independently reviewed. Final source hashes equal quick-checked
paths; rebuilt committed artifacts remain clean.

New candidate tar SHA256:
de55212e85ceb2bceac77e249272e20e1062afa8aa733df42e02eae981c094b8.
50 files/43 declarations, bytes/docs/links validated. New package in remediation
subdirectory; old reviewed tar retained unchanged. See evidence/remediation/
for source diff/range-diff/series/package and quick-path receipts.

R1/R2/R3 accepted as fixed; post-review integration may start. This is not a
release, merge, deployment or final readiness approval.

## Integration-discovered runner isolation correction

First actual pilot stopped before browsers when package-lock=false disabled lock
resolution and changed96 disposable dependencies. Existing guard caught
Playwright drift; original root unaffected. Full app unit1867/build passed.
Architect selected exact package-lock=true no-save command; fresh npm-only probe
preserved all407 baseline paths and manifest/lock bytes. See verification-results.

Owner1 runner4-path fix retains locked graph and snapshot manifest/lock hashes
before launching consumer tools. New package paths allowed; absent optional
platform paths stay outside baseline. Focused9 script tests cover snapshot file
changes and package name/version/removal drift, baseline mismatch, added candidate
paths and actual committed snapshot selection. No custom resolution/tool pin or
weakened Playwright guard. Lead directly inspected source/tests and applied
required public-prose pass. This restores reviewed isolation inside the existing
boundary; review9/10 permits direct acceptance, no affected-lane rerun needed.
WebUI Git slot granted for normal-hook/identity fixup+fold into pilot commit.
Final committed head/range-diff acceptance and new actual proof still pending.

Runner correction final direct acceptance at WebUI
7c9e26969420106c6d48074029f9df57755b74ec. Lead verified clean tree/index,
full diffcheck, exact4 approved paths and final source hashes/receipt. New nine
runner tests and23 selected scripts/format/docs/structural/pattern gates pass.
Normal app source diff zero; prior full1867/unit build remains applicable.
One cohesive final pilot commit, base unchanged7860521f, no obsolete fixup,
migrations or pin streams. Original e35 review+failure evidence retained.
Under review9/10 no rerun for this correction. Fresh actual package proof now
authorized with exact new ref, same HaveAPI dc941578/de55212e candidate.

## Fixture preview working-directory correction

Locked proof reached type/Vite success then failed before browser launch because
nested Playwright config defaulted preview cwd to its own directory. Owner1
adds explicit snapshot-root cwd to existing webServer config, unchanged command/
port/matrix/no-reuse. One regression loads actual config and resolves its Vite
executable/config path from that cwd. Lead inspected exact3 paths and applied
main-agent dated worklog prose pass; correction stays inside reviewed launch
wiring, no new product/API/design. Git slot granted for checked narrow fix/fold;
final receipt and new proof pending. Full unit/build reuse remains justified by
zero normal app source change. No reviewer rerun solely for this direct fix.

Fixture cwd correction final accepted at WebUI
fbf2a7f70f145a1bb87f659e68c84df0245448c3. Lead verified exact3 approved paths,
clean tree/index/full-diff whitespace and committed checked source receipt.
Runner10/10, fixture TS, seven-case listing, docs117 and formatting pass.
One final pilot commit; fresh main unchanged7860521f; protected dependency/Nix
blobs equal base. Review9/10 direct narrow-fix policy applies; no independent
rerun. Fresh package-only proof authorized from new snapshot with same final
HaveAPI/tar. Original review and failed locked proof retained separately.

## Actual Vite strict-module compatibility finding

Adapter Chromium startup fails ReferenceError Authentication is not defined at
minified asset before fixture initialization. Owner1/architect mapped emitted
bare Authentication assignment to deliberate ambient global preservation in
callback authentication.ts. Vite ESM is strict regardless of strict:false in
the inner UMD. Known ret/v1/v2 globals are exposed on callback paths too.
Raw UMD Chromium+Firefox pass is consistent; do not bypass named import or
minification. This is a package usability defect, not a fixture timeout.

Architect-selected source correction: internal actual-host-global bridge only
for Authentication/ret/v1/v2, preserving live reads, registry identity, values,
timing and returns. Guard globalThis then browser/worker/Node fallbacks, no new
runtime requirement/eval/Function/export/entrypoint, keep original loader shell
and strict:false. Unreachable opts and unrelated quirks unchanged. Owner0 source/
build, owner1 independent strict-wrapper/no-globalThis callback fixtures. Source
release granted; cohesive commit/quick gates before affected general/architecture/
risk review by same retained reviewer. Scope lane need not repeat absent broader
mechanism. Actual minified Vite/browser proof remains mandatory after review.
No source/Git/probe overlap; WebKit read-only diagnosis stays owner0.

Bridge final local gates pass: build/typecheck, callback26 (strict8 included),
async36, resource11, both emitted consumers, Mocha18 self-contained. Peer1
independently strict8/8 against exact built hashba0d03d9 includes direct callback
authenticate through replaced global registry. Main-agent test README wording
accepted. Source retains module evaluation order via authentication import.
Owner0 Git slot granted for coherent fold into callback TS boundary, regenerate
both producing-stage artifacts, full range/tree/hash evidence/new pack. Affected
general/architecture/risk review by original reviewer still required before
long integrations; bridge changes reviewed mechanism, not just a direct fix.

## Affected bridge review complete

Reviewer0 same verified retained Sol/xhigh/read_only completed general,
architecture/repetition, risk/compatibility at HIGH risk; NO findings of any
severity. Original scope conclusions retained. Exact HaveAPI c14e7d3..76f190f,
checked tree157489d9351dae3ff669ee8f4827d272b99d22f7; WebUI fbf2a7f unchanged.
Independently callback26/26 and native-globalThis strict wrapper probe pass;
source/output registry live replacement/exports/module order/global ret/v1/v2
semantics preserved. No new runtime/globalThis/polyfill/eval/Promise requirement.
No reverse runtime cycle, duplicated auth policy, generalized bridge or import
workaround. UMD shell/strict:false/XHR unchanged. Self test scope honest.

Reviewer inspected complete rewritten series/range-diff and confirms no obsolete
iteration/fixup/transitional mode, one unchanged TS/Rollup lock stream, source-
associated stage outputs coherent and no consolidation needed. NO MIGRATIONS,
no protected upstream/history or supported release/state boundary altered.
Independent final tar verification51files/44declarations/55288bytes exact
SHA6efa9263..., all files byte-match committed artifacts, clean/full whitespace.
Pack-owner source provenance limitation retained honestly.

Review is complete for final source; authorize final full JS/server suite due
callback source change, then actual locked/minified named-import plus raw UMD
three-engine proof. Previous dc941 integration/raw browser evidence not reused
to certify final76f190f. Node minimum remains a release prerequisite. No merge,
release/deploy/readiness action follows from review alone.

## Dedicated fixture production-mode/session preconditions

Actual final bridge proof now passes all3 raw UMD engines; four adapter cases
initialize then fail runtime_mode. Owner traces dedicated Vite build omitted
explicit BFF mode, unlike normal production build; no product guard bug.
Fixture config defines BFF mode, actual config/real production resolver regression
passes (runner11). Before rerun owner identified fixture had seeded token but
not validated BFF session identity. Architect approves fixture-only production
helper ordering: bind known synthetic64hexkey using real binding helper, then
remember same session/key/token; assert real runtime OAuth2/token/key before
first API call. No refresh rebind, changed-session/nonreplay remain. Do not
expand to full boot workflow or relax source guard. State synthetic validated
identity and exclude OAuth/bootstrap certification. Lead released exact seam;
source/config/test/docs quick/direct acceptance precedes committed new proof.
This restores existing fixture preconditions inside reviewed boundary, no public
contract/architecture change and no automatic affected-review rerun.

BFF fixture final direct acceptance at WebUI
1ef5b7b079366a94461d5d467d7f6d3969d98217, base unchanged7860521f. Exact6paths
config/fixture/helper/test/dated log only, no product/dependency/Nix change.
Lead inspected source, applied prose pass and verified committed hash/clean tree/
full whitespace. Focused runner12 includes real-mode resolver and real-BFF guard
negative/positive helper test, fixture tsc/list7/docs117/format pass. One coherent
pilot commit; original reviewed/failed heads retained in evidence. Corrections
restore preconditions inside reviewed fixture boundary, no affected-lane rerun.
Fresh actual proof authorized with unchanged final HaveAPI/tar/scoped runtime.

## Final evidence-only outcome commit

WebUI72b852df371710dd829bd07327d42f67af7ebba6 adds only dated worklog final
verification facts after tested1ef5 source. Lead wording pass accepted, docs117/
diffcheck pass. Owner verifies all2307othertrackedblobs/modes/names identical;
no application/config/test/dependency or verification behavior change. Evidence
alone does not trigger automatic final substantive review or rerun. Final series
pilot1ef5 + focused evidence72b852, no obsolete source/fixup/pin/migration stream.
Supported comparison capture saved actual main base7860521f/final72b852.
Original reviewed packet and directly accepted narrow corrections preserved.
Featurepublication/requiredPR/CI authorized, not merge/release/deploy.
