# Detailed verification and revision history

Retained lead state before consolidation into a current summary. Historical
heads and phase descriptions below are evidence, not current status.

---
lifecycle: active
---

# 2026-11-01-api-doc-language-settings

## Status

- Phase: measured allocation correction plus user-requested UI/comment refinements;
  preview remains available.
  exact Settings labels are now English / Česky.
- Identity verified with `dev-session current`; environment and thread binding
  both match this session and workspace.
- Same-session retained roster inspected. Architect `architect0` owns investigation
  and design, with saved workspace-write access; lead owns scoping and acceptance.
- User added linked internal protocol documentation to the proposal scope;
  forwarded to architect for source/layout and navigation design.

## Phase checklist

- [x] Scope and same-session ownership verified.
- [x] Existing renderer/settings behavior established; proposal recorded.
- [x] Revised design accepted and user-facing recommendation prepared.
- [x] Runtime/UI localization and regression coverage.
- [x] English/Czech articles, source-layout migration and packaging.
- [x] Final user-facing writing pass; intended changes committed; quick checks pass.
- [x] Independent final review with whole-branch history/migration conclusions.
- [x] Narrow review fixes folded and verified against reviewed range.
- [ ] Broader checks, feature publication and CI.
- [x] Temporary API preview verified and URL delivered; keep server running.
- Deployment and default-branch integration: not requested.

## Next actions

- Run one full server/documentation/JS-assets batch and separate all-client
  deterministic performance contract. Publish feature, inspect exact-head CI,
  then launch/verify preview and deliver URL. No integration approval exists.

## Documentation

- [Plan](plan.md); accepted architect-owned proposal in [design.md](design.md).
- [Stable session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-api-doc-language-settings/).

## Repositories

- HaveAPI canonical bare clone: `repos/haveapi.git`.
- Feature: `2026-11-01-api-doc-language-settings`, worktree
  `worktrees/2026-11-01-api-doc-language-settings/haveapi`.
- Fresh fetched base: `391b0190241cf195a69b06f7297d3e4eebec5a83`.
- Initial plan/state tracking commit: `8a882dc34`.
- Runtime commit: `aa07bfa91179ffda64d5a101a83ed73b3b77e69b`.
- Final article/packaging commit: `fd61d71ea06a971453c3491370dbc8133b410926`;
  feature worktree/index clean after both commits.
- First published repaired series: runtime `11ffe313ff981be608a3f50bc8efce1b9d869886`,
  articles `442077694c2439db48051d0a2e11aa58cb94261f`.
- Current consolidated series after CI fixes: runtime
  `b6760cd01b360ed4f3b23bb35686d060b8d94e29`, articles
  `f390c9fdc13dbbc4b67adba3a2a87b7584e8b8f9`, verification
  `e7ac8578a2ffd07b3ac7da05a27996191619a8f9` (current final head).

## Execution backlog

| Owner | Deliverable | Dependencies and acceptance |
| --- | --- | --- |
| implementer0 | Locale isolation, request/article/search/CSS/JS behavior; runtime specs | Architect brief; en/cs lookup contract; English/Česky; quick checks; owns hook/env setup and initial Git slot |
| implementer3 | Static ERB/TOCs, validator presentation, catalog/scanner/generated locales | Coordinates helper boundaries and JS keys with implementer0; exclusive YAML/catalog/generation ownership; lead wording pass before serialized commit |
| implementer1 | doc/en and doc/cs articles, faithful translation, source links/copying/gem packaging; packaging/shared-page specs | Shared locale lookup contract; complete-page checks wait for runtime; lead wording pass before serialized commit |
| implementer2 | Temporary representative API preview and reachable URL | Prepare independently; launch final sources after review/checks; keep server running for user |
| lead | Direct final bilingual writing pass, acceptance, tracking, final review/check coordination | Technical drafts settled before wording pass; no overlap with implementers' source edits |
| reviewer0 | Independent final review | All intended commits and quick checks first; explicit assignment required |

Current added milestone owners: implementer1 owns immutable context locale and
renderer/adaptor comment emission + focused tests; implementer3 owns select-only
progressive enhancement, shorter Jazyk label and all new canonical comment
catalog/scanner/generated entries. B supplies key inventory to A2, never shares
catalog edits. A0's perf helper/spec paths remain separate. Existing i18n:health
accepted; no new general literal-classification system. Lead final wording pass,
serialized commits, affected review and final exact-base performance/browser checks.

## Commands run

- `dev-session current`
- `dev-session team list 2026-11-01-api-doc-language-settings --as-is`
- Design-only assignment to retained `architect0` via `dev-session team assign`.

## Results

- Narrow allocation optimization committed/folded into runtimeA. Current clean
  finalthreeheads A`1413f08b703abc2054b5e62bb695a6edd3c123aa`,
  B`03f28971b4a0e74d299d5b208d9d3931e494afb1`,
  guard`613c83a76fce94a9b13122ca74540291d361242f`.
  Only docs_locale English earlyreturn +focusedhelper tests changed; B/guard patch
  bytes unchanged, consolidatedtree equals testedfixup. Hooks/stylepassed,
  locale/search19/19. Bounded actualfixture probe3×8requests/2warmups/setup excluded
  removed871/830 allocations and I18ncalls174→87 in English; Czech unchanged,
  en/csHTMLsha256 identical. This is diagnostic improvement, not hostedgatepass.
  Publishedpreview/source remain reviewede7 until newuserpackages verified.

- User refinement: JS language control select-only with no-JS submit fallback;
  generated comments localized, Czech sidebar Jazyk. User confirmed i18n:health
  was the remembered completeness guard, so no new scanner subsystem is needed.
  Architect finalizes minimal comment-emission/UI packages; existing health
  extraction extends only for new helper calls as needed.

- Exact finalhead CI observation completed: 11/12 runs succeeded (server matrix,
  release build, all clients, i18n/style and ordinary push performance). Explicit
  originalbase391b019→finale7 pair41348052141 failed actual allocation guard after
  all14 cases ran: docs.html_resources13730.60→15630.62 (+13.84%),
  docs.html_actions12940.63→14810.36 (+14.45%), exceeding unchanged10% allowance.
  Correctness passed; timing inconclusive (3/5 agreement), not a timing pass.
  Rust allocations passed, other10cases passed. Pushpair baseline already included
  localization and cannot replace originalbase coverage. Evidence downloaded at
  `ci-watch-artifacts/41348052141/` with full report/samples/source/input receipts.
- No blind retry, budget/reference/calibration change or acceptance waiver.
  Architect owns bounded hotpath diagnosis/brief; A0 supplies read-only allocation
  probe. Current helper eagerly translates English fallback on every call even
  when rendering English, then translates again. New source optimization must
  preserve fallback/interpolation/locale scope, pass focused checks and affected
  independent review before repeated pair. Preview remains stable at reviewede7.

- Actual Chromium/Playwright preview acceptance PASSED: firstvisit cs-CZ without
  cookie, exact English/Česky beforeTheme, language switch retaining resource/
  fragment, cookie after query removal/reload, savedEnglish overriding Czech
  browser, de-DE English fallback, en/cs reference→versions→protocol→reference.
  Programming example localStorage unchanged, localized metadata/choice labels
  verified. No browser errors or local400+ responses. HTTP12 localized pages and
  JS/highlighter/CSS200, manual mount-path cookie navigation passed. Initial
  harness-only H1 expectation corrected to real localized heading, no product edit.
  Owner2 writes final [preview receipt](preview.md); service remains active for user.

- Preview LIVE and lead independently verified HTTP200 + active service:
  <http://aitherdev.int.vpsfree.cz:4567/v1.0/> (internal network/VPN), sample
  `?resource=test#root-test-echo`. Durable user service
  `haveapi-doc-language-preview-20261101.service`, RubyPID3602829,
  invocation `c461dfe3db7b47b4b3062982c6c65bf4`, `0.0.0.0:4567`,
  [preview record](preview.md), `preview.log`. Exact finalheade7ac8578.
  RACK_ENV=production permits real preview hostname; data remains inert in-memory
  fixture. No host/firewall/proxy/project-source/index changes. User URL delivered
  in commentary; browser/HTTP full acceptance still running. Leave service open.

- Final local batch at exact `e7ac8578a2ffd07b3ac7da05a27996191619a8f9` PASSED,
  command exit0 / utility exit0, about197s: full server **994 examples / 0 failures**,
  all-client deterministic **214 / 0**, assets passed. No active test process.
  Evidence limitation: watcher omitted complete raw stdout redirection; available
  streamed CLI transcript is partial/truncated. Summary/status retained with this
  limitation, no tests rerun just for logging. A0 reconciles only owned misplaced
  evidence and task-generated tracked dist output, retaining exact patch/list.
- Preview launch authorized at final head after localpass/review; owner2 starts
  the durable session-owned fixture server and actual browser/HTTP verification,
  retaining it for user. Exact-head CI remains ongoing, owned by fresh CI utility
  after local watcher reconciliation; no parent duplicate log polling.

- Final feature published with explicit old-head force-with-lease, all ordinary
  hooks passed in declared environment. Fresh remote proof featuree7ac8578,
  default391b019 unchanged; no active superseded old-head CI runs to cancel.
- Final push CI includes performance41347981011, server41347981025,
  release41347981033 and i18n41347980957. Additionally dispatched explicit hosted
  quick pair `391b019...→e7ac8578...`, run41348052141, to complete the originally
  interrupted base-to-feature comparison rather than measuring only followups.
- One fresh final-checks Luna/low utility operation launched by A0 at exacte7:
  full server/doc/JS assets then isolated all-client deterministic. Source frozen;
  A0 owns completion, failures or precise restoration of build-only dist outputs.

- [Affected final review](review-followup.md) accepted at finale7ac8578 with no
  findings. Same reviewer/settings/all4 lanes, independently verified actual CI
  archives/receipt/source hashes and packaging-only difference, strict new/legacy
  receipt behavior, source-input checks, final history/no migrations/no streams.
  Prior UI/security/translation conclusions retained; no repeated full review.
- Final exact-head publication and one fresh final-checks watcher batch assigned
  to A0 (server/doc/JS-assets once, then separate all-client contract). Planned
  hosted explicit base391b019→finale7ac8578 quick pair will complete the originally
  interrupted measurement, alongside ordinary push CI. No reruns of failed old
  jobs without changed inputs; no budget/reference waiver.

- A2 new support commit passed source_versions 18/18, style2/2, make doc/hooks;
  actual old CI receipt reconstruction preserved raw hashes and made only the
  recognized packaging input equal. Then A0 folded B buildfix/A testfixup into
  their original owning commits, retained guard as separate logical third commit.
  Final tree `dbc8470a294dc57a5a06f2b164f5522701e36d19` equals tested pre-rebase
  `c1e47a2033dfcaace071849cd2f80c92e216f20f` tree; clean, no conflicts/content edits.
- Fresh default remains base391b019; remote feature remains prior published44207769.
  [Affected review packet](review-followup-packet.md) assigned same independent
  reviewer0/Sol/xhigh/read-only for all four affected lanes at exact finale7ac8578.
  Only seven files /194+18- differ from repaired prior head, mostly regressions;
  no broad rerun before new substantive verification rule review.

- Feature publication succeeded at `442077694c2439db48051d0a2e11aa58cb94261f`;
  fresh remote proof matched and default stayed original base. Required config
  and pre-push signatures renewed without hook/config source changes or bypass.
- Full watcher batch at that head completed exit 1 in 142s: doc generation and
  JS build succeeded, full server RSpec **986 examples / 2 failures** in
  `search_index_routes_spec.rb` (old custom-API-header locale/Vary expectations).
  Final asset step skipped by set-e. `full-checks.log`/status retain evidence.
  Build-only tracked `clients/js/dist` outputs belong to this run and are being
  restored precisely before authored fixes; no repository-wide reset/clean/stash.
- Exact-head CI: client Ruby/Python/Go/PHP/JS, i18n and RuboCop passed; server
  RSpec failed before tests because `make doc` bare I18n load misses CI component
  vendor/bundle. B implements standard-library canonical-catalog schema rendering
  and an empty-gem-environment regression. Server failure log retained.
- CI all-client deterministic contract passed, but paired performance stopped
  **before timing**: raw server gemspec file-selection metadata differs, while
  evaluated dependency projections/runtime inputs are equal. Artifacts/selection/
  source tar hashes/dependency receipt downloaded under
  `ci-performance-41345966685/`; no benchmark was rerun or gate waived. Architect
  scopes a narrowly recognized packaging normalization with original raw evidence,
  replay verification and strict other-input checks; no general Ruby parser.
- Release CI also reached 986 examples with the same two search-test failures;
  exact failure logs saved. These are implementation/check findings, not a reason
  to rerun failed CI without repairs. New build/normalization changes require
  quick committed checks and affected independent review before broader repeats.
- B build correction committed `a8b42a8a1437f187ce1bc59a19f19d904759e371`:
  canonical YAML/stdlib ERB generation, no application gems. Isolated regression
  failed before and passed after; external empty-gem make doc and focused 38
  examples passed; complete en/cs generated schema bytes unchanged. Hooks passed.
- A0 search assertions corrected to verify custom API header independence and
  explicit browser-language key separation; focused 7/7/style passed, authored
  fixup `b9c4be9f` passed hooks. No runtime change. A2's minimal verification
  support draft is 33 comparator lines plus focused replay/source-input tests and
  one owning-guide paragraph; lead direct wording pass completed. It recognizes
  exactly two statements with explicit marker and preserves legacy receipts/raw
  proof/strict other inputs. No generalized parser or performance-budget change.

- Final [review](review.md) completed: no Blocking, Important Python workflow
  stale article filters and Advisory repeated language event handlers. Both
  accepted; owners assigned in serialized Git slots. Reviewer confirms scope,
  locale/auth/search isolation, package compatibility, coherent full history,
  no obsolete approaches, no migrations or repeated dependency streams. Narrow
  direct fixes need focused checks and lead inspection, not another full review.
- Important workflow fix completed in amended B head
  `54bc9366140fb8afed7766d747abd11bfcb1672c`; lead inspected exact delta from
  reviewed B: only four path-filter substitutions. Both event sections select
  existing moved paths once; old paths absent, YAML/whitespace/hooks passed.
  Imported action refs/tooling unchanged by this path-only repair; official
  upstream latest tags were checked without selecting a new runtime ref.
- A0 owns the remaining Advisory single-handler fix and additive-listener
  regression: now completed/folded. Test reproduced 4 navigations before and 1
  after; submit also 1, retained path/query/fragment. Browser assets/syntax passed.
  Authored fixup passed hooks, ordinary autosquash onto original base succeeded.
  Lead range-diff and final tree inspection: exactly 3 affected files versus
  reviewed head (workflow, JS binding and its regression); full whitespace clean.
  B patch stayed byte-identical across rebase, no extra behavior/history/migration.
  Original reviewed range retained in review packet/report; no full rerun under
  reviewer's explicit step9 narrow-fix conclusion.
- Initial SSH feature push refused in mandatory pre-push signature check after
  rebase; remote branch absence verified and default still base. No partial
  publication; A0 verifies unchanged hook/config bytes, signs standard hooks and
  retries normal feature push. No bypass/source/index change.

- Independent final review assigned to retained `reviewer0` (Sol/xhigh, read-only,
  no settings override) with all four lanes, risk high for auth/search/cookie
  coverage. [Review packet](review-packet.md) inventories full two-commit series,
  84-file diff, commit rationale, no migrations, no repeated dependency streams,
  owning guides and quick checks. No integration tests started before review.
- Both commits passed mandatory hooks. B's Python docstring reference triggered
  PythonChecks; documented `uv sync` prepared ignored `uv.lock`/`.venv` via fresh
  Luna/low utility (exit 0, about 3s), after which hooks passed. No lock tracked.
- JS dependencies prepared via fresh Luna/low watcher (`npm --prefix clients/js
  install`, exit 0, 19s); log/status in session. npm reported preexisting dependency
  advisories; no dependency manifest changes were requested or made.
- Isolated frozen benchmark dependencies prepared via fresh Luna/low watcher,
  exit 0 in 53s, 25 dependencies / 70 gems (`benchmark-env.log`/status). No tests
  ran before final review. Full server RSpec plus doc generation/JS build/assets
  covers documentation and ordinary deterministic performance once; separate
  all-client benchmark-shell contract remains required.
- Fresh origin fetch during final review confirmed master still at exact base
  `391b0190241cf195a69b06f7297d3e4eebec5a83` (feature two commits ahead).
- Existing matching Playwright/Chromium tooling is available without installs;
  implementer2 will use actual browser interaction plus separate HTTP checks on
  the final preview after review/checks. Server remains stopped until then.

- Focused runtime checks passed 128 examples (locale/navigation/search/OAuth),
  then an affected 122-example batch including auth failures, code parity and
  exception handling. Browser assets and scoped Ruby style passed.
- A2 final evidence: catalog generation/health passed, scanner 7/7, validators
  18/18, all ERB compile checks, scoped Ruby style 4/4 and whitespace checks.
- B final focused batch passed 43 examples (shared pages, extracted-gem packaging,
  exceptions); scoped Ruby style 7/7, 52 relative source targets, bilingual stable
  IDs/noncomment samples and four schema code blocks per locale match the base.
- Compatibility regressions found by focused checks were fixed: unsupported
  readme/schema aliases remain rejected, missing schema returns 404 while EACCES
  still surfaces. Updated fixture paths use the same normalized article path.
- Transient Bundler load failure traced to concurrent component-shell reinstall;
  no-install prepared root shell succeeded after installer completion. Followup
  commands use that shell. No hooks were bypassed.

- Implementation milestones: source layout moved; five Czech articles drafted;
  locale request/cookie/browser/search and mounted article links implemented;
  static templates/catalog/validator text drafted. Lead's direct bilingual writing
  pass completed on five Czech articles and canonical UI catalog, with small
  grammar/terminology corrections and protected technical content retained.
- First scanner regression checks: 6 examples, 0 failures (implementer3).
  Remaining focused checks wait coordinated catalog/docs generation; no broad
  integration tests or independent final review have started yet.

- Worktree creation's post-checkout hook refused because Overcommit signature
  needed renewal. Reconciled effects: correct clean worktree/branch exists and
  portal registration is present at the expected base. Do not retry creation.
  Implementer0 owns standard hook verification/signing inside the Nix environment;
  no hooks bypassed. `.overcommit.yml` and custom hooks were inspected by lead.
- User requested a temporary API server and URL after completion for visual
  review. Implementer2 prepares its session-owned launch; leave it running.
- Root Nix environment preparation passed (`nix develop -c true`, 59s, exit 0)
  through fresh Luna/low utility `prepare_env`; logs `env-prepare.log` and status.
- Implementer0 completed Overcommit install/config+plugin signing and list check;
  standard executable bare `hooks/pre-commit` is active. Unset `core.hooksPath`
  is expected and caused only an initial diagnostic chain's exit 1.
- Server Nix environment preparation passed through fresh policy watcher
  `server_env`, exit 0 in 29s; `server-env.log`/status. Use the prepared shell
  without installs: `HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash ...`,
  with `BUNDLE_GEMFILE="$PWD/servers/ruby/Gemfile"` for server commands.
- Preview plan uses the existing inert Ruby fixture plus session-local example
  preload on port 4567, already allowed from internal networks/VPN by host policy.
  No firewall/proxy changes; not launched yet. Intended host aitherdev.int.vpsfree.cz.

- Architect verified that `refs/remotes/origin/master` is `391b0190241cf195a69b06f7297d3e4eebec5a83`.
  The bare local `master` (`7835acafdda19779815a0f1ba905d78e0085456d`)
  predates the current documentation UI, so the proposal uses the remote-tracking
  baseline without fetching or creating a worktree.
- Current documentation already has unified preferences, multi-page navigation,
  search and OAuth controls; existing framework and parameter localization can
  be reused.
- Recommendation: server-rendered documentation locale, Settings
  English/Čeština before Theme, cookie/query preference then weighted
  browser language then English; reload retains current page and fragment.
- User removed the visible Automatic option and authorized moving English article
  sources to `doc/en/` alongside `doc/cs/`. Browser detection remains the initial
  behavior without a saved choice. Architect's revision was inspected and accepted;
  source lookup, copying, packaging and repository links move together, while
  public URLs and fragment IDs stay stable.
- Existing example-language preference continues to mean programming language.
  API request/client settings remain independent; generated code stays unchanged.
- Linked internal docs gain Czech article sources with English fallback, stable
  anchors and shared locale navigation. Copying/gem packaging needs to include
  locale directories; machine-readable schema representation is unchanged.
- Lead inspected the design and confirmed current Settings placement,
  documentation-copy behavior and packaging glob against the inspected baseline.
  Architect verified 15 pinned source anchors. This is source inspection, not
  runtime/browser verification. No tests/builds were run or needed for planning.
- The earlier proposal-only phase needed no final change review. The implemented
  runtime and article deliverables now require the normal committed final review.

## Open questions

- Architect is finalizing comment-emission/UI boundaries from visual feedback.
- Application-authored descriptions require their
  owners to supply translations through existing hooks; plain text falls back
  to the supplied original. Full details and future checks are in the proposal.

## Cleanup

- No resources acquired or lifecycle changes requested. Leave the session open.
