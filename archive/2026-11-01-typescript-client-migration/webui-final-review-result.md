# Independent final review and finding disposition

Reviewer0, retained gpt-6-astra/xhigh/read_only, independently reviewed the full
WebUI range63d484fc070dbee633d32624de545e834d483701..aef727cff377c8368268bf61c881d173efe88ef5,
tree204193162e635fe95466cf1c182a5f86bab046f6, all eight commits, at HIGH risk across
general, architecture/repetition, scope/proportionality and risk/compatibility.
Trusted session binding matched; environment markers absent in reviewer shell.
No overrides, nested reviewers, source edits, tests or builds by reviewer.
The complete inbound reviewer report is in this session conversation; this record
preserves findings, independent conclusions and lead decisions.

Result: Blocking0, Important2, Advisory2. Source/history review completed;
runtime/package/browser/API acceptance remains pending. Lead accepts all four
findings for narrow fixes. Important findings remain open; no long checks yet.

## W-R1 — Important, general/risk — Retain partial CVE intentions

Locations: AdminSecurityAdvisoriesPage.tsx149–175; producer
securityAdvisoryAdminApi.ts126–134/171–185; edit hook32–45.
The serial helper records completed/remaining operations and original error.
Create caller converts this to a string, closes form and navigates away, losing
desired B/C after A was accepted. Uncertain work cannot be labelled safely
unperformed. The edit hook retains the draft but discards structured progress.

Required remedy: accepted parent identity, original desired CVEs and structured
partial result stay available through the transition. A small retained view with
explicit detail/reconciliation path and disabled parent creation is sufficient;
no replay/recovery framework. Caller test must prove first accepted CVE followed
by readback/second-write stop retains intention and does not create a second
parent. Use the same presentation for edit where useful.
Owner implementer6; source released. Main owns exact bilingual copy, W catalogs.
Completed means API-accepted writes, not successful subsequent readback.

## W-R2 — Important, architecture — One owner for association validation

Eleven byte-identical isOperationsReference bodies/types occur in nodes, audit,
transactions, clusterResources, lifetimes, oom, monitoring,
clusterResourcePackages, securityAdvisories, securityAdvisoryRelations and
securityAdvisoryUpdates. The shared partial-positive-ID/ten-optional-string-field
contract can drift between screens if corrected independently.

Required remedy: one small WebUI module/type and shared boundary tests; preserve
existing behavior, keep clusterResources numeric refinements local. No generator
or general-schema framework.
Owner implementer6; source released.

## W-A1 — Advisory, general — Preserve unknown sysctl observations

NodeHistoryPanels.tsx148/164–178 renders omitted/null availability as unavailable,
two omitted values as matches, and omitted configured value as not configured.
Required remedy: unknown for missing observations, unavailable only explicit
false, not configured only explicit configured null, compare observed values.
Small rendered table case. Lead accepts fix now, owner implementer6.

## W-A2 — Advisory, risk/copy — Bulk stop requires fresh review

SecurityAdvisoryNodesPanel.tsx239–243/452–472 disables continuation after every
failure, but active en/cs bulk message says safely continue with the rest.
Remaining work can include an uncertain write.
Required remedy: accurate fresh-review/reconciliation guidance and stopped-state
label, not a new continuation mechanism.
Lead accepts fix, owns copy; W inserts exact catalogs, i6 consumes.

## Independent scope and architecture conclusions

Reviewer compared the actual424-file +13312/-9173 handwritten diff with full SDK
migration and explicit temporary-unpublished support. Broad domain work is
justified by actual validation/receipt contracts and unsupported controls.
No backend feature, distribution service, schema framework or speculative
compatibility subsystem found. W-R2 identifies concrete avoidable duplication.

HaveAPI remains transport encoder/decoder; generator SDK owns operations,
namespace/input/describe contracts; WebUI owns auth/language/public isolation,
read-only renewal and domain views. Generic custom call paths are retired.
Central seam preserves receipts and distinguishes local ClientInputError from
post-dispatch uncertainty; base changes reject, credentials read per dispatch.
Anonymous clients/recovery isolated; only GET/OPTIONS retry after validated OAuth
recovery; no write replay. Describe and async receipts retained. TSIG successful
output is scrubbed before validation can retain a receipt. These are source
conclusions, not newly executed evidence.

## Temporary support and real-API test glue conclusions

Relative file dependency, revision tarball and provenance fit explicit user scope.
Reviewer independently checked archive SHA256f3bb42d... and root-lock delta:
only SDK root spec/new entry. Sourcefilter retains archive; public allowlist
excludes it. Local fetchNpmDeps projection/restoration and ordinary offline npm
are narrow existing-tool use. Actual full frontend/package checks still needed.

Reviewer inspected committed Node/Ruby integration glue and reused API
Safety/Bootstrap/TestDb. Inherited-config refusal, exact clean API revision,
unique disposable TestDb, private IPC, loopback mounted Puma, bounded calls and
shutdown-before-success have no source issue requiring broader setup. Proposed
23-call DB-only matrix is useful for actual identity/roles/descriptions/template
rules/count/settings isolation/errors. It does not test WebUI policy, BFF/OAuth,
browser or VPS workers. Startup/cleanup and matrix must still be observed.

## Explicit history, migration and update-stream conclusions

Reviewer inspected complete eight-commit series, messages/diff and all
consolidation/refresh/fold receipts. Independently confirmed343e/636e tree9350af2f
and d0b2/aef tree20419316 equality. Main refresh correctly treated as substantive
owner reconciliation, not global patch equivalence; final refreshed range
reviewed. No obsolete unmerged approach, generic-call layer or tidy/fixup commit
remains. Commit split is reviewable by purpose/owner; whole migration+dependency
is the necessary integration boundary. No transitional wrappers needed solely
for independently compilable intermediate commits.

Exactly one final SDK archive/provenance/manifest/lock/Nix hash stream in aef727c;
earlier package.json edit only extends test:scripts. No redundant pin stream.
Historical candidate evidence is not retained dependency-update history.

No database migrations, persisted-format or backend-configuration migration.
The existing VPS migrations frontend adapter is not DB lineage. No transitional
migration/schema state to preserve. No feature merge/release/deployment claimed.
Rollback restores earlier frontend but cannot undo accepted API writes.

## Verification remaining and narrow-fix policy

Owners/lead supplied quick evidence; reviewer inspected rather than reran it.
After findings fixed/disposed: full unit/script/BFF tests, production build, exact
Nix frontend+BFF/provenance/source/package checks, representative browser/captures,
and bounded real isolated API matrix. Include caller partial-CVE/common-reference/
unknown-display cases. No worker/deployment or complete visual-beta claim.

Direct requested remedies may be inspected and focused-checked by lead without
another full reviewer turn under mandatory-change-review step9. Rerun only
affected lanes if a remedy introduces a new design, expands boundary or changes a
public/cross-project contract. Same reviewer retained if such a rerun is needed.
No rerun requested yet; lead will inspect final code before deciding clearance.

Session remains active; SDK unpublished, no default merge/deploy/lifecycle action.

## Lead focused inspection checkpoint

R1 reviewed actual caller/hook/panel: immediate accepted-parent ref, retains any
post-parent child error including initial preflight failure, original desired
CVEs and accepted/review arrays/error visible, parent creation guarded, stopped
edit retained. Explicit review closes edit and reuses current detail invalidation,
preserving intent; refresh failure visible. Real-helper caller cases exercise
initial preflight failure, first accepted child+failed Show, uncertain second send,
and no second parent; focused path callback tests cover close/refetch/retention.
R2 actual eleven bodies removed in favor of one35-line common rule/type;
domain numeric constraints remain local with focused boundary matrix.
A1 actual render logic distinguishes unknown/unavailable/not configured and
compares only observed strings, eight shape cases.
A2 stopped disabled button uses accurate review-required key; exact en/cs body
describes accepted updates and work to review, no safe continuation claim.
55affected tests plus10final bilingual/path tests and scoped lint pass.

All changes are direct requested remedies inside reviewed boundary, with no
public/provider/dependency contract or expanded recovery design. No affected-lane
review rerun required under step9. Important findings await final shared compiler/
audit evidence and committed source acceptance before closing. Advisory detail
kept at existing533line allowance via two redundant blank removals; no cap growth.

Affected final shared verification PASS: application compiler and26Node validator
tests, actualexit0~69s, nativeoutputrecoveredwithout rerun. Catalog/docs/structural
already pass unchanged. All4findings accepted as implemented/verified narrow
requested remedies; no newdesign/contract or affectedlanererunneeded. Pending
normalownedcommits and historyconsolidation before longtests. I6three source
remedycommits will fold into originalinfra, Wmetadata into originalshared, exact
finaltreeproof and originalreview/remedyrefs retained; no obsolete branch stage.

## Findings closed and final history accepted

All four direct requested remedies are implemented, focused-inspected and
verified as above. Important findings closed; no expanded design/public contract,
so no affected-lane reviewer rerun under step9. Normal owned source/metadata
commits captured exact receipts, then source remedies folded into infra. Final
base63d484fc070dbee633d32624de545e834d483701→headbee19b312ac3f2267053d51bc0e886bdcc05ec93,
nine logical commits, tree5cdbadb887f13437026f2d63e3a8ced4e11712b1. Lead independently
verified pre-fold1f89/finalbee trees identical and empty diff, clean worktree/index.
Actual review-remedy delta is33files +551/-400, not claimed equivalent to original
reviewedaef. Original review/ref/report retained; exact aggregate infra/unchanged
patches/authors/support11blobs and full final series documented in
webui-review-remedy-fold-receipt.json plus range-diffs/series. W metadata/copy is
separate last commit; unchanged single temporary SDK pin is penultimate.
No obsolete code/duplicate-validator/lost-intent branch iteration, duplicate pin
stream or DB/schema/persisted-format migration remains. Combined migration
verification boundary preserved. Long verification may proceed on exactbee head.
No publication/default merge/deployment/session lifecycle authority follows.
