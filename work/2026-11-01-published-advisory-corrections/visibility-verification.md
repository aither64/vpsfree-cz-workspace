# Advisory visibility correction: delivery and verification

Status: **development preview fixed and verified; receipts frozen**. Exact API `a38c9f871f89312f16d18e158efbbbb340ec53e4`, KB `4fd4f2b8ca737b6b6baaf97998fb9484be4c1e91` and unchanged modern `1c8478bceb3943645ec06ccde895ee4b0985873f` remain clean/pushed. Independent review passed. Local full84/core74/strictKB/native18 and focused1 passed. The standard services update passed319.3s; actual API66, modern24 and legacy21 read-only role checks passed. Cluster intentionally running, shared samples retained, no active owned utility/browser/update/test command. Server alone enforces visibility; no UI runtime change.

Actual services system: `/nix/store/mygq0r3nbd1hyb3ddy1r0sbvmsb7n7l2-nixos-system-vpsadmin-services-26.05pre-git`. Running API package: `/nix/store/rv84rni10460lppzkyznyfx82vjhxw6h-vpsadmin-api-a38c9f871f89312f16d18e158efbbbb340ec53e4`. Applied selection nonpending; node1/config/OS and original modern paired packages retained. Anonymous/member API and both UIs show only published ID2; administrator access to IDs1/2/3 remains. Samples are1draft/rev1,2published/rev2,3retracted/rev2. No advisory writes or mail; final Mailpit4messages are sign-in notices only (0advisory messages).

Open hosted verification limits: API Specs41465157664 core platform-operations239/1 has an unexplained original missing count response; the first envelope/role/child is unknown. The separate exact-case60-request observation passed and does not establish a flaky-test/root-cause finding. KB Managed41465898434 failed its unchanged obsolete HTML readiness match; local strict4fd4 passed. Final one-time snapshot retains integration41465157701 in progress, RuboCop/PHPUnit/i18n and KBCheck successful. No CI wait/retry, source/head/pin rewrite or production/release-green claim. Branches remain unmerged.

| Repository | Base | Final pushed head |
| --- | --- | --- |
| vpsAdmin | `097226b22edf8b59f80b5dfaa55265e9d0cac633` | `a38c9f871f89312f16d18e158efbbbb340ec53e4` |
| KB contracts | `ce2c8cd9358c3636e5d39343e595df813a0b197f` | `4fd4f2b8ca737b6b6baaf97998fb9484be4c1e91` |
| Modern UI | unchanged reviewed source | `1c8478bceb3943645ec06ccde895ee4b0985873f` |

API final two commits: A `163677bd45b5ac0a179a0bfa144bcbd9ada9e231`, B `a38c9f871f89312f16d18e158efbbbb340ec53e4`; tree `101b160ada8bedb4a316618e7d36355e6a427b1c`. KB has one consolidated five-file pin commit; tree `2c13e344ac4cb5907bae4e450ee87d1cc5be0f8f`. Fresh remote defaults remain the exact bases above; own-feature leases matched old API49f5/KB5276 and SSH remote head acknowledgements prove both successors.

Quick evidence: four earlier unchanged full-plugin cases passed, then the two diagnosed full-mode failures were fixed and passed **2/0/0**; core passed **5/0/0**. Native results/actual times are below. Five-file Ruby lint, Nixfmt/whitespace, pinned Node syntax and normal hooks passed. Exact pre-hook candidate patch equals the committed old49f5→newa38c diff. Only eight intended paths changed (+223/-6); two runtime API query owners, docs and existing tests/fixtures. The entire original/final B `webui/` patch is byte-equal (SHA-256 `9a39e1a98a67fd7e94cafec2bfcfe7918b79b823203f5762651139a60f42e09f`), and final PHP/CSS/locales equal old49f5 bytes. **No migrations** in the complete API range; no schema conversion or transitional migration history.

KB quick lock generation passed in12.6s; Nix/JSON/YAML/diff parsing passed. Semantic lock comparison permits only selected `vpsadmin.locked.{lastModified,narHash,rev}` and `vpsadmin.original.rev`. Four source files contain only exact API revision replacement; all other lock nodes/root follows, explicit OS `6bdf458fd9105379860234ff33d352e55844f08f`, capture provenance/assets and page content remain intact. Full strict `bin/check` subsequently passed on exact4fd4 in500.77s after affected review.

Old API49f5 and KB5276 reviewed/runtime ranges remain retained in local refs and original reports. Modern's superseded f7 work was withdrawn; implementer1 proved clean exact1c restoration. The preview intentionally still runs old API49f5 and modern1c847 with its data intact; it is **not yet fixed** at runtime. Source-delivery utilities finished at that checkpoint. The retained affected review then passed with no findings; one fresh utility now owns the released acceptance batch described below, while the preview remains intentionally running.
 Accepted [visibility-design.md](visibility-design.md) and the lead's direct small-edit brief require published-only public/member/support reads, unrestricted authorized administrator history, and silent direct retraction.

## Starting revisions and retained evidence

- vpsAdmin base `097226b22edf8b59f80b5dfaa55265e9d0cac633`; A `9415cf2855a3f9caef6ab68dc7df8405ed9f3ef8`; B/head `49f5a29e5a7d85559d06d31496acb5c08895bcda`.
- KB base `ce2c8cd9358c3636e5d39343e595df813a0b197f`; old single pin `5276b64b9cab0d29bc14968730eccf88c230059d`.
- Old API and KB heads are preserved in exact refs `refs/retained/2026-11-01-published-advisory-corrections/pre-visibility-api` and `.../pre-visibility-kb` in their respective repositories.
- A fresh API `origin/master` fetch remains exactly `097226b...`; no target movement/rebase repair is needed at this checkpoint.
- Running preview remains the old reviewed API49f5 and modern1c847 systems described in [preview-verification.md](preview-verification.md). The old read behavior is confirmed in [visibility-diagnosis.md](visibility-diagnosis.md); do not call the running preview fixed until reviewed activation and fresh access checks complete.

## Delivered changes

The central API runtime change makes `SecurityAdvisory.visible_to` return published rows for nil/non-admin and retain `all` for admins. Existing original/child/projection/outage-link owners consume it. Focused existing model/resource/plugin specs cover reader/state matrices, real retracted reports, original filters/counts/cursors, populated CVE/node/update includes, owned projections and reverse outage filtering. The exact reverse-outage filter requires an additional parent visibility intersection: HaveAPI resource-input authorization does not call Show prepare. The focused reverse-filter request first returned500 because its existing grouped count produced a Hash rather than integer metadata. That branch now uses an advisory-visible link subquery intersected through the existing Outage relation, preserving unique rows/scalar count without changing unrelated outage filters.

Legacy PHP runtime requires no change at this checkpoint: it consumes the API's list/detail scopes. Its existing native browser fixtures/spec now contain an actual retracted report and guest/member negative checks plus admin positive access. These tests are not applied to the user's preview DB. `docs/security-advisories.md` uses the main-authored read-contract paragraph verbatim, wrapped; the lead approved the deterministic test-fixture wording. No new catalogs, endpoints, schemas, revision/locking/mail/storage behavior or generic authorization/cache framework.

## Quick evidence

- Targeted root RuboCop: four touched Ruby files, zero offenses. Nixfmt and whitespace checks passed.
- JavaScript syntax passed using pinned Node through the modern repository input. The root API shell lacks Node; the earlier root-shell invocation exited127 and is a tool-selection issue, not an application check failure.
- Initial `--example` alternation selected **zero examples** in both plugin modes despite exit0. Retain those logs as incomplete tooling evidence, never test success.
- The exact-line full-plugin run exercised six examples: four passed, two failed (0pending,411seconds). The failed child case had a Ruby keyword/positional translation-Hash fixture mistake, now corrected with explicit braces. The failed reverse-filter request returned500 from the existing grouped-count Hash; that request now uses the visibility-scoped subquery described above. Core was not run after the failure. A fresh bounded batch rechecks only those two full-mode failures, then the five core examples; the four unchanged successful full examples remain honestly retained. Targeted final lint covers all five touched Ruby files with zero offenses. No full resource suite or preview activation is authorized before committed affected review.

Private command/result evidence is under `/tmp/2026-11-01-published-advisory-corrections-visibility/`; no credentials or advisory bodies are copied here. Preview data and the running cluster remain intact. The lead owns state/handoff tracking and final review release.

## Final boundary and activation compatibility

The user's later boundary correction keeps visibility entirely in the server. No PHP or React runtime guard/filter is part of this package; implementer1 is restoring modern source exactly to1c847 while preserving its superseded evidence. Legacy changes are fixture/regression coverage only. The API authority must be updated first or with consumers; unchanged UIs then receive only authorized server data. Mixed old/new API instances cannot guarantee the new privacy boundary. No schema or stored-data conversion is involved; restoring the old API remains data-compatible but would re-expose retracted reports, so recovery must preserve the visibility fix. Already delivered content cannot be recalled.

### Focused result after corrections

- Full-mode affected rechecks: **2examples,0failures,0pending**, command558.741s; native RSpec duration537.967s. These are the child/include matrix and outage-link/reverse-filter matrix. Four unchanged full-mode passes from the first exact-line run are retained separately; they were not rerun.
- Core exact-line batch: **5examples,0failures,0pending**, command620.602s; native duration602.778s. Covers model scope, three read matrices and changed retracted-announcement access.
- Native JSON independently parsed; both have zero errors outside examples. The database guard passed and only automatic isolated test databases were used. No live preview DB or fixture mutations.
- Exact commands, native output and actual times are in `quick-fixed-{full,core}.{log,json}` and `quick-fixed-result.md` under the private evidence directory. The utility has ended with no test operation remaining.
- Targeted five-file RuboCop, Nixfmt, whitespace and pinned Node syntax checks passed. Main-approved docs/fixture prose is unchanged.

## Hook and publication effects

Normal scoped A/B commits and interactive consolidation exited0 in140.05s. Both pre-commit runs passed; the first commit-message hook emitted advisory default-width warnings (subject60/body72), while all message lines satisfy the repository/workspace80-character rule. No hook was bypassed. Exact final tree equals the pre-consolidation tree and the complete series remains two logical A/B commits. The first ambient-shell push refused Overcommit configuration trust and changed no remote ref; configuration/custom-hook/Gemfile bytes were verified unchanged, then declared Nix Overcommit0.74.0 `--sign` and the same explicit lease push passed. KB declares no additional hook framework; its ordinary amend preserved its one mechanical pin stream.

Private final source/graph evidence: `source-final.json`, `range-diff.txt`, `final-delta.patch`/`committed-delta.patch`, `kb-graph-proof.json`, normal hook/lock logs and remote acknowledgement. These support review of the whole ranges; they do not replace affected independent review or authorize activation.

## Current-head hosted CI snapshot (no wait)

At the one post-push snapshot for APIa38c: RuboCop41465157645, WebUI PHPUnit41465157710 and i18n41465157629 succeeded; integrationCI41465157701 is in progress and API Specs41465157664 queued. KB4fd4 Managed41465898434 is in progress and Check41465898431 queued. No current-head completed failure was observed, so there is no new failed log to diagnose at this boundary. Both same-branch inventories contain zero superseded active runs; no cancellation or rerun was needed, and no current run was canceled. Queued/in-progress results are pending evidence, not failures or success. Raw snapshots are retained privately; no CI wait/observer was launched.

## Released post-review acceptance

[visibility-final-review.md](visibility-final-review.md) reports no findings on exactAPIa38c/KB4fd4 across all four high-risk lanes and complete history/no-migrations. The lead released full affected API, strictKB, native legacy and the subsequent standard data-preserving preview services update.

One pre-launch snapshot of exacta38c API run41465157664 found full/core foundation successful but required full/core platform-operations and full plugin jobs still in progress. Complete selected-file coverage was therefore unavailable; no CI wait or reuse was claimed. Normal local commands run under one fresh pinned Luna/low utility: full-plugin model/resource/outage files, core model/resource files, exact4fd4 strict `nix develop -c bin/check`, then exacta38c native `./test-runner.sh test 'webui#security-advisories'` after target enumeration. Full/core are sequential to preserve the shared generated bundle. The batch stops on its first actual failure and has no quiet timeout; actual unexpected local kernel building escalates.

Per-command progress/status, exact source/input locks, shell derivations, bundle environment hashes, native RSpec JSON and complete logs are under `/tmp/2026-11-01-published-advisory-corrections-visibility/acceptance/`. The existing preview remains intentionally running on old49f5, with data/fixtures and modern1c unchanged. Only after all necessary acceptance passes will the parent activate the standard services update and prove running closure/readiness plus ordinary API/both-UI roles. Implementer1 is waiting for that verified-ready/utility-slot handoff; no new frontend source or cache behavior is involved.

### Preview update preflight while checks run

Read-only preparation confirms the existing cluster config SHA is unchanged from the accepted preview start: dns disabled only, modern enabled, Mailpit capture enabled. Applied selection remains nonpending with services+node1. The canonical local OS override is still exact823d7b7a84277edfd77f474fc1640a1cf756e8f7; no fetch/ref movement or topology change. Private old-applied/config snapshots are retained for the later activation comparison. No update has run. API changes affect plain application source, with no dependency or source-gem change requiring metadata regeneration; no rake dependency refresh is introduced.

The lead resolved final identity coverage: use the existing live anonymous/member/admin matrix. The preview has no support-role account; support coverage comes from actual `SpecSeed.support` full/core API cases. Do not claim a live support check, create a new account/credential, or change either seeded member's level merely for this matrix.

### Full-plugin acceptance milestone

Exacta38c three-file full-plugin API acceptance passed: **84examples,0failures,0pending,0errors outside examples**. Command1869.93s, native RSpec1845.932s. Native manifest is exactly model/resource/outage spec files. Effective Ruby3.4.9/Bundler4.0.23/RSpec3.13.6/HaveAPI0.32.1/ActiveRecord8.1.4; generated lock SHA-256 `c800cb1e88ed4375cb90049aa84f9f0bca65d36bfe54b9dc331dfed1154419a0`. Source/shell/bundle/native results are retained in acceptance artifacts. The full-mode disposable MariaDB's exact recorded PID/start identity is gone and its data directory pruned. The same utility now owns core-mode acceptance with its separately captured disposable DB; strictKB and native legacy remain next. No preview activation or source/fixture mutation.

### Core acceptance milestone

Exacta38c two-file core API acceptance passed: **74examples,0failures,0pending,0errors outside examples**. Command1494.62s, native RSpec1474.856s. Manifest is exactly model/resource files; actual mode is none. Its separately recorded temporary MariaDB identity is gone and data directory pruned. The same utility has moved to exact4fd4 strict KB validation; native legacy remains next. Both API suites are now complete; no preview activation yet.

### Strict KB acceptance milestone

Exact4fd4 strict `nix develop -c bin/check` passed exit0 in500.77s, with no override or allow-missing option. The same existing utility advanced automatically to exacta38c native legacy `webui#security-advisories`; no second observer, retry or preview update was launched. Native browser counts and owned-guest cleanup remain required before the already-authorized standard services update.

### Current-head CI failure evidence (no rerun)

The later one-time exact-head snapshot found API Specs41465157664 failed on core platform-operations125343963839: **239examples,1failure,0pending**, seed19905, native900.495s. The new child-visibility example `security_advisory_spec.rb[1:3:2]` failed at511: expected requested total_count0, got nil. The preceding HTTP200 and empty-row assertions passed, but `rows = ... || []` does not establish a successful HaveAPI envelope. The original response/role/child tuple was not retained by that failure artifact. Existing CVE/update owners explicitly implement count and HaveAPI0.32.1 Default::Index supports requested count; optional unsupported metadata is not an established explanation. Local exact-source full84/core74 passed. Hosted Ruby3.4.12/Bundler2.6.9/effective lock9a28 differ from local3.4.9/4.0.23/core9ff9. No CI retry or privacy approval follows from this discrepancy; a focused exact-case/seed response diagnosis is released after the current native legacy operation.

API topic aggregate125361043933 failed because the core matrix failed; no independent inventory failure is claimed. RuboCop41465157645, i18n41465157629 and WebUI PHPUnit41465157710 passed. Integration41465157701 was still running at this snapshot; no wait or repeated polling.

KB4fd4 Check41465898431 passed. Managed41465898434/job125346565326 failed kb#kvm's five existing readiness waits. Its retained services-shell log contains576 HaveAPI0.32.1 HTML footers, title `API versions · api.vpsadmin.test`, and zero `API description` strings. The unchanged KB helper92-107 requires that obsolete literal. Guix/firewall/GRE native results are expected_success; no hosted KVM pass is claimed. The lead dispositions this as an unrelated baseline observation issue, outside the five-pin package; no KB runtime/helper change or retry. Exact local strict4fd4 PASS remains distinct.

Failed job logs, native API result/environment and complete KB native artifacts are retained under `acceptance/ci-final/`. The first API log download was blocked by gh's terminal-escape output protection; private file downloads with its explicit output flag succeeded. This is download handling, not a workflow retry. Preview activation remains unperformed while the affected API failure is unresolved.

### Native legacy acceptance result

Exacta38c legacy target passed exit0 in1595.29s; native `expected_success`. The single native RSpec wrapper example contains **18Playwright tests,18passed**, actual607.53s browser wrapper/10.1m Playwright,997.15s native script. The watcher initially summarized the one wrapper example; the parent independently read the actual18-test counts in services-shell.log. Existing native metadata/logs are retained in `acceptance/native-final/`; no guest trace archive survived. Native guest logs record stop, QEMU exit0 and destruction. The acceptance utility has completed; no acceptance stage remains running. Original API hosted count failure remains unresolved, so no preview activation yet.

### Focused hosted-failure diagnosis

One fresh released core run of exact `security_advisory_spec.rb[1:3:2]` with original seed19905 passed **1example,0failures**,306s on unchangeda38c. Its private sanitized60-request observation contains no HTTP200 status:false and no requested child collection missing total_count. Counts are0 for hidden children and positive for authorized rows. Original hosted response/role/child tuple remains unknown; this success is not called proof of a flake or a root-cause fix. Original hosted example failed18.862s into the case, execution13th in the topic; all12 preceding examples were from the same resource spec. No second reproduction or full-topic campaign has been launched. The one required successful-envelope assertion is prepared before its collection count to prevent false empty-list interpretation; it does not change API/runtime policy or weaken counts.

### Development acceptance disposition and update

The lead accepted actual independently reviewed DEV evidence: full84/core74/strict4fd4/native18PASS plus one focused1PASS with60 successful response envelopes/counts. The original hosted-only missing count remains unexplained; this is neither a flaky-test finding nor a claim of green production/release CI. No whole-topic/prefix repetition is added before user preview. The temporary one-line successful-envelope assertion was saved privately as `acceptance/temporary-status-assertion.patch` and only that uncommitted line was restored. Source is clean exacta38c again; no A/B rewrite or D pin refresh.

The parent launched only `vpsadmin-devcluster update 2026-11-01-published-advisory-corrections services` (owned PID2974984, exec77590). A fresh pinned Luna/low observer owns private update status/log observation, without mutating-driver authority. Exacta38c/modern1c clean, unchanged config SHA784e5d3b45d343068435cb931c464dff82d61a84b8a19c9cf692fa39d8cf21ef and canonical local OS823d7b7a84277edfd77f474fc1640a1cf756e8f7 were rechecked before launch. Existing applied selection was nonpending; old config/applied descriptors saved privately. No fetch, reset/stop/force or data/fixture edit. Actual running-source proof and API/both-UI role probes follow command completion.

## Final development handoff — complete

The exact parent services update and effect proofs are recorded in [preview-verification.md](preview-verification.md). API66 wrapped-filter/count/state/child requests, unchanged modern24 read-only role cases and legacy21 pages all passed using normal TLS and existing anonymous/member/admin identities. Anonymous/member lists contain only2; direct1/3 are denied by the server and ordinarily unavailable in the UIs. Admins retain all three and authorized editing access. No support account was created; live support was not run, while actual full/core support cases passed.

Final source status confirms cleana38c/4fd4/1c. Temporary one-line diagnostic assertion remains only in a private saved patch; project source was restored exactly and no Git/pin successor was made. The final Mailpit check after both UI logins has4normal sign-in notices and0advisory messages, compared with0 immediately after update. The earlier historical3-message capture lacks an immediate pre-update baseline, so preservation/removal attribution is not claimed.

Private compact final evidence: `acceptance/preview-update/final-proof.json`, `source-graph-proof.json`, actual runtime/health/applied selections, liveAPI/legacy role results, and `acceptance/ci-final/handoff-snapshot.json`. Native guests completed their recorded stop/QEMUexit0/destroy; no guest Playwright trace survived. All owned acceptance/diagnosis/update/browser commands and observers are terminal; the development cluster intentionally remains running with retained data. No merge, production deployment, reset/stop or session lifecycle action.

Session portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/
