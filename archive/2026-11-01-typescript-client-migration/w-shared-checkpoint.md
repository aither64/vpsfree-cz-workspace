# W shared source and focused verification checkpoint

## Current temporary SDK delivery checkpoint

The user explicitly authorized temporary unpublished SDK support for refinement.
It is committed as `18471d10fd30ce5c1f01581e960bb79c76a911ab`, parent
`a9e2049f5f3445691e4025bca496e342443494f2` on refreshed main `63d484fc`.
The 11 owned paths and committed/worktree SHA-256 bytes match
`/tmp/w-unpublished-sdk-committed-manifest.json`; the index is empty. The only
remaining dirty source is i4's exact checked receipt fixture, deliberately
excluded. W returned the sole Git turn for its owner fixup and history fold.

The ordinary `file:vendor/vpsadmin-typescript-client-0.3.0-99ee06654ef9.tgz`
dependency consumes the unchanged 337,414-byte verified candidate. Compact
provenance, npm-generated lock and existing source-checker negatives bind the
bytes; all other upstream dependency records and the BFF graph are preserved.
The existing frontend fetchNpmDeps projects only that SDK package record for
remote fetching, restores the canonical lock, and uses a writable cache for local
offline installation. Source filtering and public install allowlist are unchanged.

Clean npm ci passed (410 packages, 18.2 seconds), installed ESM passed and four
policy suites passed 38 tests. Source-checker tests passed 10/10. The necessary
fake-hash probe reported actual hash
`sha256-utOpabPprstf97qzc/yre2O/EW36u6SsfS0o2Aas36k=`. Its real FOD builds at
`/nix/store/6ri6jdfd2py0n3b2v0xwspxdsc1bwppl-vpsadmin-webui-frontend-1.0.0-npm-deps`;
the cache lock compares byte-identically to the canonical root lock. Refreshed
ci:quick audits pass; after i4's six complete-receipt mock corrections, the final
typed tail passes application/tooling, E2E 100 checked/182 deferred and BFF 6/6.
Evidence: w-unpublished-sdk-prep-complete.log, w-unpublished-sdk-final-quick.log,
w-final-typed-tail.log and their result records. No unchanged archive checks were
rerun. No full frontend/Nix package, browser or real API matrix has run yet.

The SDK stays unpublished. No default merge/tag/release/publication/deployment
was performed. Intended package source/docs and quick checks are complete;
independent committed review and its owned fixes precede the longer checks.
Update/rollback guidance is in PACKAGING.md, with identities in HAVEAPI_CLIENT.md
and the migration work log. Lead-applied writing review is retained.

## Earlier shared-source milestones

Session: 2026-11-01-typescript-client-migration, implementer2.
Source committed as `343e4ec28c243c7fa8904488aceef252ec390306`, parent
`0713ba1bce9e439a2e7acc22f5a6530e94dea143`, in the assigned WebUI worktree.
The sole Git turn is returned. Exact 84 added/modified/deleted paths and all
committed/source SHA-256 bytes match `/tmp/w-committed-manifest.json`; index empty
and worktree clean. Git reports 82 changed files because two pairs are renames.
No merge, publication or deployment was performed.

Current W-owned source list: `/tmp/w-owned-paths.txt`, 84 explicit paths,
including the authorized DashboardPage nullable-count boundary and existing
test:scripts registration for nested pure integration safety tests. The root
SDK dependency/lock/hash remains excluded while final dependency delivery is
unresolved; the user explicitly directed that the SDK stay unpublished.

## Exact SDK input

Current SDK source: 99ee06654ef956a09b52749f4cd02d1435362087.
Generator: eea3ae5e82c3db23d5f5bc9f1a5e7784117c4e1b.
Archive: artifacts/package-s/candidate-99ee066/vpsadmin-typescript-client-0.3.0.tgz.
SHA-256: f3bb42d0392fb738f5c70fe1415cc8742ab943a31c2ed2a85af5ccbd385d831f.
Integrity: sha512-6Q74ddIgGzeav9mvPubc33g5Sd+Ni7ZOLtKnNVzP/sW1Cxmw59nLiib50H27HBYc0UgoVfjlxuqH0WmX7hR3jw==.
Independent digest and exact installed inventory/bytes verification passed for
all 1360 package files (1352 built files plus source/provenance/package records).
No machine-local archive path was added to the root manifest or lock.
Old 383e/b650 archives and receipts remain preserved. Only generator commit
provenance changes from accepted b650 bytes; generated/built files and dependencies
are identical. The user directed "Keep the SDK unpublished for now"; no SDK
default merge, registry publication or tag is authorized. Architect found no
supported existing nonpublication pin (dist untracked, prepack without prepare).
No delivery mechanism is added. Final dependency delivery remains an explicit
prerequisite; the next review is scoped committed source/candidate verification,
not clean-checkout/CI/Nix or ready-for-use acceptance.

## Shared exports

- sdk.ts: async getApi(): Promise<VpsAdminApi>; sync getPublicApi(): VpsAdminApi.
- apiOutput.ts: narrowApiResult(result, narrow, context); ApiOutputError with
  post-dispatch phase and complete original result/cause.
- apiErrors.ts: HaveApiError, ClientInputError, uncertainty/expiry and receipt/count
  helpers. The transitional haveapi.ts is deleted; no reexport ghost remains.
- apiRequestPolicy.ts: complete RequestSpec to RequestResult policy; generated
  calls never pass through historical namespace projection.

The source preserves output namespace, header/signal/timeout options, per-request
credentials/language, public isolation, BFF renewal and no automatic write replay.
Malformed post-dispatch output retains uncertainty and receipt evidence. Failed
anonymous discovery preserves its own cause without claiming an unsubmitted
mutation was sent. Namespace wire conversion stays entirely in the generator.

## Focused checks

Historical pilot on exact b650 SDK installation, from the WebUI worktree (the
legacy tests in this command were subsequently migrated/retired):

```sh
nix develop --command npx vitest run \
  src/lib/api/apiOutput.test.ts src/lib/api/apiRequestPolicy.test.ts \
  src/lib/api/sdk.test.ts src/lib/api/sdk.wire.test.ts \
  src/lib/api/haveapi.test.ts src/lib/api/haveapi.call.test.ts \
  src/lib/api/haveapi.refresh.test.ts src/lib/api/haveapiRequestClient.test.ts
```

Passed: eight files, 109 tests, 7.85 seconds, start 19:01:11 local. The actual
HaveAPI package serialized/decoded controlled in-process XHR, including custom
metadata, exact output namespaces, action receipts, renewal/no-write-replay,
public isolation, contradictory HTTP/envelope results, transport/abort/timeout.
This is focused unit acceptance, not a live backend or browser certification.

Earlier source batch: 25 shared tests plus 17 config tests passed (42 total).
TypeScript 5.9 full checking passed, last output w-source-typecheck.log. Scoped
ESLint passed on 29 adopted files; format passed on 66 reviewed files; catalog
parity passed with 8370 keys per language; design inventory/audit passed with
68 API modules, 162 documents and 76 requirements. config.ts was mechanically
formatted/adopted as required by its existing changed-source quality policy.

## Documentation and remaining scope

WebUI API_CONTRACTS, ARCHITECTURE, CONFIGURATION, HAVEAPI_CLIENT,
DOMAIN_COVERAGE, IMPLEMENTATION_INVENTORY, REQUIREMENTS and the dated migration
work log describe the shared boundary and staged dependency readiness. Shared
catalog insertion uses the exact lead-approved copy. Its dormant entries change
no rendered control; actual React control impact follows the domain owners.
The canonical KB workflow was inspected; legacy PHP pinning is not React proof.

I4 completed the exact-successor network pilot: `nix develop -c npm test --
src/lib/api/networks.test.ts` passed 36 tests in 8.61 seconds, including six
actual-XHR cases; `nix develop -c npm test --
src/pages/app/admin/cluster/NetworksPage.test.tsx` passed 12 tests in 14.01
seconds. These cover mounted generated OPTIONS, current auth, false/zero receipt
fields, unsupported absence, preserved 403, malformed field rejection and null
metadata protocol failure with original envelope/data/HTTP200 in error.result.
An initial test expectation confused the application error projection with the
raw runtime receipt; source inspection resolved it without a runtime/generator
change. No duplicate network run was performed by W. I3 completed the VPS list/start pilot and its bounded view changes: nine focused
files passed 142 tests on b650; full current typecheck exited zero. The model is
generated-backed, guards a positive safe row ID and preserves optional/null
hostname/scalars and partial associations without full User/Node assumptions.
Includes, count=false, limit=0 and whole receipts survive. Malformed relations
raise ApiOutputError with the receipt. Source-backed Start framing is vps:{} plus
blocking metadata; missing action receipt and missing namespace remain separate
failures, both preserving the appropriate uncertainty. W and architect confirmed
the canonical framing from immutable source; no provider/executor workaround.
No duplicate W run of the network or VPS suites. Broad domain source was released
after these accepted pilots; all domain owners have since completed source.

## Complete-source boundary

Shared actionStates/public/Location models now use generated-backed views and
receipt-preserving guards. All legacy production imports/calls are gone; whole-src
scan is clear and haveapi.ts is deleted. Wrapper-only unwrap tests were retired;
call/renewal/transport tests were migrated to complete RequestSpec policy tests.
Later overlapping batches passed 65 transport/policy, 74 error/policy and 35 final
namespace/auth/receipt cases. Counts are not additive. Latest docs/sourcechecker
batch passes: inventory 257 routes/72 API modules, docs 162/76 requirements,
catalog 8,376 keys in each language, sourcechecker 6/6. No global compiler was
launched by W; lead owns the one final source snapshot watcher and its log
w-final-source-typecheck.log.

That actual compiler snapshot reported 57 diagnostics in 13 files: W fixed its
duplicate test import and authorized dashboard nullable-count normalization;
the six affected error-mapping tests pass. I4/i7/i6 fixed their exact diagnostic
groups with focused source evidence. The corrected full application compiler and
remaining quick audits pass (82.1-second related batch). Failed replacement
invocations before source checking are not new source evidence. Final tail passes
in 38 seconds: strict E2E 94 checked/183 deferred, BFF 6/6 and five targeted Node
suites 42/42. Logs: w-final-remaining-quick.log, w-final-quick-tail-fixed.log and
their result records. Latest scoped checks pass on 32 ESLint / 69 formatted files.

Manual structural review preserves the original baseline and existing allowances.
The three reviewed i5 scopes were tightened; reviewed DNS model 537 to 518 and
advisory page 535 to 533. Resolved IpAddressDetail, VpsNetwork and both Locations
entries were removed. NodeDetail/VpsStorage stay at 627/505 after reviewed source
corrections. The final audit passes: 26 raw, 25 accepted, zero unaccepted/invalid/
aggregate failures. Independently verified final source hashes/counts for the
four additional corrections: Header 496, nodes 498, NodesPanel 500, Datasets 958.
DatasetLookupInput was adopted after exact-source owner ESLint/Prettier passed;
the complete 32-file scoped ESLint and 69-file formatting checks also pass.

Remaining W delivery: scoped independent review and owned follow-up fixes;
final supported dependency pin/lock/npmDepsHash after delivery is resolved
SDK publication occurs; shared explicit-path commit when lead grants Git turn;
final committed independent review and then longer checks. I0 owns test-only
guarded actual API bootstrap/harness, with no database or HTTP run before review.
No merge, deployment, registry publication or session lifecycle action performed.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/

## Final review follow-up in progress

Independent review of aef727cff377c8368268bf61c881d173efe88ef5 accepted the temporary SDK/Nix package and history/migration boundary. Four narrow findings (two Important, two Advisory) remain with i6: partial CVE intent/accepted-parent recovery, shared association guards, honest unknown sysctl observations and stopped-batch copy.

W reread the locked terminology guides through Nix at a65a4dfeb92a59df4a80a737a20bcbf8558793ff and inserted the exact lead-approved seven new keys/three replacements in both advisory catalogs, preserving placeholders. DOMAIN_COVERAGE registers operationsReference as a pure included-reference guard; WORKFLOWS drafts the actual partial-CVE/sysctl/stopped-node failure contracts. No shared runtime/dependency changes.

Review follow-up is committed as 1f89a74d3f62ec53c5df446bfacb251aa2f08951, parent8b6efe773e8f79d57612558371d3a5aefdb8b5de after the three i6 source commits. Exact7paths/blob/source SHA256 receipt: /tmp/w-review-committed-manifest.json. W returned soleGit ownership; index/worktree clean. All accepted source bytes preserved.

Affected audits pass once: en/cs8393keys, catalog structure, inventory257routes/73API modules, docs177/76requirements, structural26raw/25accepted/0unaccepted/0invalid/0aggregatefailures. AdvisoryDetail is533 with unchanged533 allowance and reviewed d583d4a84b2465132952fcca723f5186b3cb343dec9de523d6e11df2fa1f8abb hash. The final affected application compiler and26Node validators pass in about69seconds; evidence w-review-fixes-quick-fixed-recovered.log. The two fixture-only sysctl typing corrections are included in i6 source without changing product behavior.

Lead accepted all four narrow remedies under the existing review rule. I5 next consolidates source/metadata into the reviewed logical streams with exact finaltree preservation. No source/package/dependency/archive changes are pending from W, no cap growth, and no long checks ran before remedy acceptance/commits. W retains owned follow-up fixes; lead owns final history/acceptance/state/portal.

## Nix lock-map follow-up checkpoint

Actual full Nix verification on1ab98533 reached the canonical lock comparison, then the pinned Rust fixer panicked because the local SDK had no remote cache-map entry. Architect-owned correction is committed as7cad7ffb3a0a294c30349680e2eb4f80c63a3926, parent1ab9853312a95b5448e99fd6f83f846453de17a5. Exact5paths and protected7input SHA256 proof: /tmp/w-nix-map-committed-manifest.json. W returned sole Git; index/worktree clean.

The frontend uses the existing npmHooks.override interface with a small upstream-prefetch delegate. Only successful map-cache extends its transient map via the existing source checker after recomputing the verified local SDK SHA512; remote entries preserved, matching map idempotent, invalid/conflicting data refuses before writes. Unchanged upstream fixer/offline npmci/canonical lock and BFF hook retained; no copied hook, Rust patch or cache-index writer.

Quick12sourcechecker cases pass; actual pinnedfixer passes on disposable canonical lock plus explicit478remote-entry fixture map extended by the verified SDK, with lock SHA256585e8f48b194d8165731ca546fb709c94d531ee48224de9fff805416cb8b0f8e byte-identical. Nix parse, frontend custom/BFF default hook evaluation and docs177/76 audit pass. The earlier6ri6cache output is now absent; eval expects the same output/hash, not a package success claim. Actual cache/hook/package evidence awaits committed affected all-four-lane packaging review and fresh Nix watcher.

Archive/root manifest+lock/BFF graph/application JS/node_modules were not edited or reinstalled; existing runtime/unit/Vite evidence stays distinct. No release/default merge/deploy/session lifecycle action. Lead owns reviewer assignment, verification queue/state/portal; W owns concrete ensuing packaging fixes.
