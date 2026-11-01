# Package C final review input — HaveAPI 0.30.2

Complete committed React deliverable with quick checks passed and retained final
review accepted. Lead directly accepted the narrow OPTIONS test correction.
Postreview unit/build/Nix checks passed. Fresh rooted browser proof has60/62
passes with two mobile click timeouts; see latest result below. No branch publication has occurred. Current architect scope: dated2026-10-26 C3 addendum in
work/2026-10-24-vpsadmin-haveapi-upgrade/design.md; plan/state remain lead-owned.

## Repository and complete history

Repository git@github.com:vpsfreecz/vpsadmin-webui.git, target main.
Worktree worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-webui.
Own branch dev/vpsadmin-haveapi-upgrade.
Exact full range:
`5a2d2bdc3ad7a827038f877d75959916528db844..f10d3d48c4f21cc39187c3667ffffd9952404c11`.

1. `02b45a7de7eec8966b6a2ade16a46fbb9e1b6c83`
   deps: adopt the released HaveAPI 0.30.2 client.
   Root manifest/lock, normal frontend dependency hash, registry provenance and
   source-security guards/tests are one final dependency stream.
2. `f10d3d48c4f21cc39187c3667ffffd9952404c11`
   api: use the released HaveAPI AsyncClient in production.
   Carried adapter/policy, actual-client fixtures, R2 correction/shared guards,
   normal browser assertions/coverage and current technical docs/work log belong
   to the production adaptation. Original authors and dates retained exactly.

No fixup/transitional history or repeated dependency updates remain. Superseded
0.30.1 selection was folded into the one final0.30.2 dependency commit. No
released/deployed/consumed state boundary requires it in the final series.
Complete series final.diff/commit-series.txt/final-stat.txt and source mapping
content-mapping.json are adjacent. Inspect the whole series and final diff,
including original takeover/R2; require explicit history/consolidation and
no-migration conclusions.

Prior reviewed/R2-closed range:
`5a2d2bdc3ad7a827038f877d75959916528db844..014f7b9c9f451d6275af73c4af30a24668b77b7b`.
Retained local recovery/review ref:
`refs/heads/dev/vpsadmin-haveapi-upgrade-reviewed-0301` at exact014f7b9c.
Its packet/diff/series/source map/R2 receipts and PR74 plan are preserved under
0.30.2/old-reviewed/. Earlier reviewer head39f8fd7d and accepted R2 exact delta
remain in their historical receipts; lead closed R2 by direct verification under
mandatory-change-review step9. 0.30.2/range-diff.txt binds old/new complete series;
0.30.2/old-new.diff is the exact release/doc delta. Source/R2/BFF/coverage equality
is proven by empty0.30.2/runtime-unchanged.diff. Initial C3 pre/post-consolidation tree equality is historical at
`0aa1152064b123562dceb311fc56efa50fd7fc05`; see consolidation.json. The script-only
correction below changes current tree to `e1084bb80dd07140719034ab908a6f62daff855b`.

## Outcome, scope and provenance

All normal authenticated/public/fallback-description requests use actual npm
AsyncClient. Library owns transport, wire serialization and validation. WebUI
retains live per-request auth/language, public isolation, BFF identity/renewal,
one bounded read retry, no mutation replay, domain results/meta and uncertain
operation guards. Contradictory HTTP failure/status:true receipts remain
ambiguous with raw HTTP/envelope/AsyncError cause retained; shared guards prevent
duplicate submission while valid status:false4xx rejections release protection.
No pilot, toggle, second decoder/fetch transport, archive dependency or BFF edit.

Exact npm haveapi-client0.30.2 resolves ordinary registry artifact with integrity
in packages/haveapi-client-provenance.json. Source321ce8256ad4704efaed04f4f2aa1ea4c2a3b4b8,
tagv0.30.2, release workflow40238928168/attempt1. Registry metadata, subject SHA512,
all53 source-file matches and installed file matches verified. Package.json and
bundle version string alone changed from0.30.1; declarations/runtime behavior
are unchanged. All other root entries, exact XHR1.8.0 and BFF lock retained.
New normal npmDepsHash sha256-sY3OQDFdisOzhJO4dhwlsjvGxlhog8crhqU3tHcI4IY=.
Source guards remain data-driven and unchanged for this identity refresh.

Original carried source8772bab21cd8739bf4672cdf4976aea2a6e59de3 relative to
7860521f30826c3886c89c35e8ab6f4e082e0a4b is content provenance, not literal
ancestry. Its obsolete pilot/vendor series was never replayed. Seven current-
main overlaps remain reconciled and unchanged by C3: WORK_LOG, API_CONTRACTS,
REQUIREMENTS, E2E coverage, structural ledger, nodes.test and tsconfig.e2e.
Original author Jakub Skokan and both original C commit author dates preserved.

## Quick verification and evidence limits

0.30.2/setup.log: locked Node24.21.0/npm11.19.0 lock/install/prefetch passed38s.
0.30.2/quick.log: fresh pinned Luna/low watcher, exit0 in132s:

- Eight focused files/123 cases: actual-client adapter, auth renewal, public
  isolation, protocol/API receipts, abort/timeout, node/VPS blocking contracts,
  and R2 shared guard/no duplicate behavior.
- Six source-security tests passed.
- Full ci:quick passed: installed declarations and other scoped typechecks,
  lint/format/design/structural/csp/i18n/other normal gates. E2E72 adopted/195
  deferred retained; structural allowances unchanged.
- Production npm audit0 vulnerabilities;409 registry signatures and101
  attestations verified.

Six preexisting optional/bundled missing-URL prefetch warnings retained. Full
package builds still establish cache completeness. Only dated verification prose
was updated after the broad quick run; final design/source checks follow the
consolidated commit. Source checks do not perform network signature verification.
Controlled XHR fixtures are actual library behavior, not live API/OAuth proof.

Current documentation: docs/design/HAVEAPI_CLIENT.md and PACKAGING.md plus
2026-10-26 work log/index aligned to0.30.2; previous2026-10-24 adoption/R2 record
explicitly historical. Existing current API contracts/architecture/requirements
and other production docs remain valid. No member-facing UI/catalog/BFF copy.
Project behavior stays in the repo; temporary history/publication plans stay here.

## Review and remaining gates

Inherited whole-branch risk high: authentication/transport/mutation uncertainty.
Current new delta is release/provenance/docs only. Lead resolves retained reviewer
settings and affected mandatory-change-review lanes; earlier review is evidence
for unchanged code, not approval of new identity. Ownership: HaveAPI supplies
RequestSpec/AsyncClient/AsyncError; WebUI request adapter translates errors;
haveapi.ts owns application admission/renewal/projection, consumed by domain
wrappers. BFF config/session/OAuth remain separate protocols; legacy PHP client
upgrade belongs to package A. No provider logic copied into the frontend.

No migrations: no database/schema/persisted-format/wire change; no new release,
deployment or external consumer. Mixed0.30.1/0.30.2 wire compatibility retained.
Matching frontend/BFF rollback preserves session store/credentials. Server R1
performance adoption/authorization/locale/input-ownership proof belongs to A/B;
version adoption alone does not certify it.

After independent committed review: full unit suite, normal production build,
Nix frontend/provenance/source/package checks and ordinary desktop/mobile browser
fixtures for public overview, authenticated home, renewal/expiry, failures and
VPS action state. No live member mutation/deployment is authorized. Own branch
may publish only when lead coordinates acceptance; PR74 protected rewrite still
requires exact published-commit approval under pr74-publication-plan.md. PR74,
PR63, old source refs/worktrees/records remain untouched. No merge/lifecycle action.

Historical clean-source receipt for prior reviewed757f7fd8 (before script fix):
`/nix/store/6pjw8m1fx4c0v24yvhxw78mj1kfg5193-source`
passed actual package-source check (15required files), with no package build.
Postcommit design audit passed136docs/75requirements,257routes/64API modules.
See0.30.2/final-source-quick.log. Clean worktree and final diff whitespace passed.

## Postreview narrow script assertion correction

Retained final reviewer accepted prior head757f7fd8; first long batch stopped
at one obsolete GET/rawdescription script assertion (227/228script cases passed),
before BFF/rootunit/build. Lead assigned test-only correction to the already
reviewed OPTIONS discovery contract: configured payload + complete success
envelope at four supportedpaths. Only scripts/e2e-haveapi.test.mjs differs from
that reviewedtree. No production/fixture/sourceguard/BFF/R2/dependency change.
Currenthead `f10d3d48c4f21cc39187c3667ffffd9952404c11`, tree
`e1084bb80dd07140719034ab908a6f62daff855b`. Dependency02b45a7d unchanged;
original productionauthor/date retained. Five targetedscript cases, scopedlint
andformat passed. See0.30.2/options-test-fix.md/.diff/-range-diff.txt and focusedlog.
Reviewed757f7fd8 ref preserved at dev/vpsadmin-haveapi-upgrade-reviewed-0302;
originalpacket/diff/source-map/input/PR74snapshot in0.30.2/reviewed-757f7fd8/.
No new migrations or consumed-state boundary. Lead direct step9 verification
accepted the test-only correction; postreview execution resumed below.

## Reconciled postreview verification

Exact unchanged cleanf10: script228/228, BFF57/57, Vitest303files/1899cases and
normal production build all PASS (batch1-resume exit0,317.854s). Ordinary Nix
frontend/BFF/provenance/source/package-contents PASS (batch2 exit0,96.127s),
with matching fullf10 clean build-info and complete source/derivation/NAR graph.
Actual build resolves cache completeness;15source files/370public assets passed.

The explicit nine desktop/mobile browser files produced62launch failures
(31perproject), all before application assertions: NixOS cannot load the generic
Linux cached Playwright Chromium1228 (browser exit127). Batch3 exit1,53.163s.
No retry/runtime substitute/source edit; browser acceptance remains blocked.
All owned operations reconciled, Vite exited, no listener on52847. A0 retains
its sole watcher; C used authorized parent-monitor fallback throughout.

See0.30.2/postreview-results.md, final-nix-identity.json, normal-build-info.json,
postreview-reconciliation.json, final-postreview-preflight.json and
browser-runtime-blocker.md. Source/history/PR74mapping remains exactf10,
two commits/authors/dates unchanged, no migrations. Publication/PR74 rewrite
remain gated; recovery proposal is verification environment work only.

### Accepted FHS recovery and pressure-GC finding

The accepted session-local same-browser FHS setup/version/hash probe passed
without app/Git/host/browser/security changes. Subsequent batch3-fhs yielded
31/31desktop app passes and31mobile prelaunch ENOENT errors. Host pressure
GC journal confirms deletion of the unrooted FHS runtime during that batch.
This is a runtime retention failure; no app assertion failed. All command
handles/Vite/listeners reconciled; no repeat yet. Full original and FHS run
receipts retained. See0.30.2/browser-fhs-gc-correction-plan.md and fhs-gc-journal.log.
Proposed continuation roots the identical FHS output and runs only the remaining
mobile selection after version/hash/root probes, awaiting lead direction.
Overall browser gate remains open; all source/history identities unchanged.

## Latest actual browser and retained-artifact result

Fresh full62case run on the current persistently rooted FHS closure completed
exit1 in393.23s: all31desktop and29mobile cases passed; two mobile user/admin
transaction-expand clicks timed out with pointer interception. No launch/setup
failure. This fresh result stands alone; no combination with old31desktop proof.
All185runtime NARs/sizes/references stable before/after, same pinned/browser/
source hashes, roots registered. Failed screenshots/videos/traces/contexts
retained with checksums. See0.30.2/browser-full-rooted-failures.md and
browser-full-rooted-reconciliation.json. No source fix or retry performed.

All5normal package/check outputs restored to original exact drv/output paths;
frontend/BFF and both sources match original NARs,1796derivation JSON identical,
all outputs/sources present with owned registered roots. See
0.30.2/nix-retained-restoration-receipt.json. Retain roots for later cluster
preparation; no cluster/deployment action occurred. All C operations reconciled,
localport free, execution capacity released. Cleanf10/source/history/migration/
PR74mapping unchanged. Browser acceptance remains open pending lead disposition.

## Publication checkpoint

Ownbranch dev/vpsadmin-haveapi-upgrade published overSSH and independently
verified at exactf10 after lead release. Main andPR74alias remain unchanged.
No exacthead CI triggered by feature-only push (workflow filters); no manual
dispatch/PR/default action. See0.30.2/publication/receipt.json and ci-observation.json.
Final protected old/newPR74rewrite plan is refreshed in pr74-publication-plan.md;
exact authorization pending. Current60/62accepted preexisting residual retained.
