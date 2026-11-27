# B delivery evidence

Owner: implementer1. Session remains open; no merge, deployment or live runtime
mutation performed. Independent review is recorded in `review.md`; direct R2/R3
corrections are complete below. Campaign release and acceptance remain lead-owned.
The stable session page is
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-23-pi-message-delivery/.

## Source and history

Final provider history and the single consumer dependency stream are consolidated.
B source and required local check follow-ups, including narrow R2/R3 corrections,
are complete for lead acceptance. The failed full-web result remains distinguished
from its passing exact follow-ups below. The history window is released.

- codex-web base/default/deployed: `3209aa7bf93e2c7067b07494d1b254741812d714`.
  Final provider: `21d9c251297ba15e1702b58f4737d07bd1aa1d30`.
  Separate native SQLite initialization fix/final head:
  `db79231a4e5513bf439493efab75378bc7d84c04`.
  Lead published with the exact old `1707ef0d` lease and verified remote equality.
  Final CI run `45304027274`, attempt 1, succeeded (lead authoritative report).
- Provider history is one owning optional-API/browser commit plus one separate
  diagnosed initialization-race fix. Published development-only `0b3237f` and
  `2459f8c`, `9bf8c58` and `1707ef0d` were consolidated by explicit lead direction;
  they were never merged,
  deployed or a supported independent consumer boundary. Their old CI is not
  final-head evidence. `9bf8c58` red CI remains diagnosed failure evidence.
  Range-diff preserves the init-only commit exactly; `git diff 1707ef0d db79231a
  -- codex docs/submission-storage.md` is empty. Its stable patch ID is
  `2116c7ffbce9eff023ea9353bcb2103174ef36d2`. The provider latch is a substantive
  correction, not an equivalence claim for the entire old head.
- dev-workspace deployed/published base:
  `f3bd843f9858b87cef66d0949706f8af16ba9b13`; remote default last fetched
  `0abe5fe48955b1bcdc8cc368fcb27e11e0676f70`, eight inherited commits behind.
  Preserve that inherited deployed series, accepted A `e50ff02e`, C identity
  `60900b4a`, and C checked input `74f4a6f4` in whole-branch review.
- B dependency commit: `82de924708e51e41ab9693759e75bccfc94cb9e9`, parent C `74f4a6f4`.
  It amends unpublished `7e11253f4e16081a7f6a3fb60aea232a1eb5d7ce` through an alternate
  index, preserving staged B behavior and unstaged V. Exactly five Go/Nix/vendor
  files select final `db79231a`; no intermediate
  dependency pin commits or sums. Unrelated lock nodes and existing old sums
  are preserved. Final pseudo-version is
  `v0.0.0-20261124011639-db79231a4e55`; NAR hash is
  `sha256-soMfL5rH6S56o2Uh76UvOwoLG8yflFDmt1GSp8LLu5o=`.
- Focused R2 prerequisite: `b4f3f288d4b7c74c791696967cba297ce448c93a`, parent
  unchanged dependency `82de9247`; exactly one line in the existing runtime
  conflict-key check, extracted from the previously reviewed B commit.
- B behavior: `835aadce5147933c63f5910490bb90c89eef53ba`, parent `b4f3f288`.
  This replaces reviewed `e6b85c6b1aee3fcfcdc55deaca0a77115e54ce37`: R2 is extracted
  and R3 folded into B. 34 files, 3646 insertions / 24 deletions. Source scope is the new
  `portal/internal/inputdelivery/` package, `web/pi_input_delivery.go` and tests,
  server/local resolver hooks, actual composer plus existing Pi mode confirmation
  hooks, retained/hydrated/HTTP/browser contracts, queue preflight/host fences,
  runtime contract and two owning docs. Exact file list is
  `git show --format= --name-only 835aadce5147933c63f5910490bb90c89eef53ba`.
  No C/native source is in this commit. Before committing, staged source/fixture
  hash, whitespace and formatting were checked; the ordinary Git commit did not
  bypass hooks (repository declares no hook framework). All V changes stayed
  unstaged.
- Latest I1 checked/released dev-workspace head:
  `474872b602afa0813e6a17a951646b5cf5a91a06`, one-file F4 fixture correction,
  exact parent I0 P4 `329eef86e18a0f88ad651f91dbc1a3450c5dedc9`, whose parent
  remains `176706a605119b64f4efd24f0b2f25957caa7298`. No history rewrite.
- Earlier I1 P2-local checked/released head:
  `09f44a72fe384d5a9756b880711c826c4e0f76c1`, P2 local correction after I0's
  F3 `1cbeeb50972adf5e2b57ef08961f1550f689631b`, whose parent is
  P1 `06680120cd3004afe785043c47781e15cbae66b7`.
  P1 is the normal focused tracing commit after F2 `ea17a752b27afe1a7a73336b8c100e8fb79e7f48`
  and P0 `b0d2411f4737abb24e5c81b26666b6a2949db2b5`,
  whose parent is `79dd02b09e25e38d8d833185d0e4c3acc7fef7b5`. No ancestry rewrite
  was made for F2 or P1. Earlier F fixture prerequisite `26dbaf84`, B `835aadce`, R2/R3
  and the single dependency stream retain their identities/ancestry. Original
  worktree/index are clean; history window released. H's actual browser inputs
  and five pins are unchanged; F2 only changes a different fixture test body.

## Implemented boundary

Shared opt-in delivery routes/helper/mount are neutral and preserve legacy
message, native queue and retry contracts. The actual Pi composer uses the same
helper, preserves the visible full selection/scope/mode and in-flight draft/file
edits, and never converts a legacy or uncertain durable attempt to another path.
Both consumers latch the initially verified full selection separately from latest
polled metadata. Polls cannot silently adopt a changed opaque digest; an explicit
page refresh or successful settings/mode save plus exact same-scope confirmation
is required. Late, failed and wrong-scope reads cannot re-arm. Focused tests cover
poll-before-Send with equal visible settings and zero POST, re-arm and draft/files.

The private indexed SQLite queue acknowledges only local durable ownership after
strict local auth/scope/settings and ordered upload pinning/reread. It takes no
runtime lock and calls no native/host/transcript proof at admission. Immutable
original requests coexist with durable negative identities in one transactional
authority. Native dispatch has one durable claim and fresh actual execution
evidence; all post-claim recovery is original-reference lookup only. A proved
successor changes execution evidence, not admission. Retired Unknown stays
Unknown and deduplicated, leaving only its ordering/capacity barrier.
Positive native Pending alone gets a 200 ms original-ref lookup interval during
the first persisted dispatch second, then two seconds. Unknown/errors stay at two
seconds; reads/restart never renew the window. Eligible Pending ordering is due
time then sequence, preserving peer progress. The 250 ms scheduler tick and call
cost remain; no strict public Sent latency claim is made.

The store gates connection lifetime, reads, writes, commit checkpoints and close
under package transition admission. Terminal close cancels/joins callers and
defers an EX-blocked close inertly until process exit, without later retry or
checkpoint. Preflight opens only a private DB+WAL byte-copy under existing EX
writer/close exclusion, omits SHM, and retains work/refusal/disposition identities
through existing `portal_delivery` claims and exact `piPortalDelivery: 1` fences.

## Checks and raw evidence

- Provider Nix quick checks: complete `go test -mod=readonly ./conversation/...`
  passed (0.147 s); both JS syntax checks passed; full flake browser list
  **115/115** passed (1.793 s) after the final latch.
  Narrow malformed/forbidden negative-proof guard passed afterward.
- CI failure reproduced with exact
  `go test -mod=readonly ./codex -run '^TestConditionalSteerConcurrentClientsShareOneClaim/database=true$' -count=30 -timeout=45s`:
  3/30 SQLITE_BUSY. New 16-client fresh-open regression failed 3/10, including
  initial PRAGMA/connection setup. Init-only existing private file lock releases
  before predecessor migration/native/normal transaction work.
- Fixed exact concurrency/cold-open/cancellation batch 30 iterations passed
  (11.031 s); lock-order/focused batch 10 passed (3.652 s). Full native codex suite
  passed (28.513 s) with
  `nix develop --command env TMPDIR=/tmp go test -mod=readonly ./codex -count=1 -timeout=60s`.
  The initial full run exposed an existing Unix socket pathname overflow under
  Nix's longer TMPDIR; shortening only TMPDIR fixed that verification limit.
  Final collision/cleanup-focused checks and owning conversation suite passed.
- Final vendor hash authority: [B-latched-vendor-hash.log](B-latched-vendor-hash.log)
  is explicitly a captured excerpt from completed session 1869, not a complete
  saved transcript. It records expected old `UcR9...` and actual
  `sha256-AHXwgkh+p23Ecq0MS/gpfVY1x8QnePpWk73kD3yueHk=`. Corrected exact
  `nix build --no-link --print-build-logs path:/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-23-pi-message-delivery/dev-workspace#packages.x86_64-linux.dev-workspace.goModules`
  passed (exit 0), full output in
  [B-latched-vendor-corrected.log](B-latched-vendor-corrected.log). Earlier provider
  vendor logs are milestone evidence only.
- Matching pin check passed through `bash nix/check-codex-web-pin.sh`.
  This source script is not executable; an initial direct invocation refused
  permission and was corrected without source or hook changes.
- Focused B Go tests passed for real HTTP admission while an exclusive runtime
  lock is held; zero native calls; exact ordered upload pinning/reread race;
  original ID and stale new selection/header boundaries; negative-proof restart,
  late original POST and explicit new ID; successor binding revision and actual
  execution claim; original-only crash recovery; retirement/capacity/history;
  native-free negative-only preflight; denied/deferred/repeated close and actual
  EX-held terminal shutdown/WAL recovery.
- Final-pin curated focus passed inputdelivery 0.175 s, web 14.415 s, cmd 3.908 s:
  `nix develop --command env -u PORTAL_BROWSER_TEST -u DEV_WORKSPACES_CODEX_PROVIDERS -u DEV_WORKSPACES_PI_PROVIDERS -u NODE_OPTIONS GOWORK=off TMPDIR=/tmp NODE_PATH= DEV_SESSION_REQUIRE_RUNTIME=0 go -C portal test -mod=readonly ./internal/inputdelivery ./internal/web ./cmd/workspace-portal -run 'TestPending|TestDurablePortal|TestPortalDeliveryComposer|TestComposerHandoffRetains|TestPiTeamPreflightRubyHostAndActualScannerKeepRetiredFence|TestPiTeamPreflightRetainsNegative|TestPiCreationRuntimeReadinessRefusesUnresolved/deadline' -count=1 -timeout=45s`.
  Deterministic cadence/window/restart/followUp-steer-peer tests passed before the
  owning batch. The exact scanner fixture separately passed in 3.774 s.
- Actual-source Node composer contracts and syntax checks passed. Hydrated
  browser fixture source reuses the existing Pi-page/request-inventory harness
  via `portal_delivery_browser_test.cjs`, registered in `TestQuestionBrowser`.
  It is syntax-checked, with execution intentionally after final review.
  The later exact hydrated H execution is recorded below.
- Backend-retention Ruby: **21 tests / 464 assertions**, green. The full file
  found an existing contradictory-current-runtime key bug; keying by
  workspace/slug instead of workspace/slug/incarnation repairs the existing exact
  regression. New host fence tests: **2 tests / 20 assertions**, green.
- First default owning Go/Ruby batch: queue passed (2.946 s); web exceeded the
  insufficient 180 s package budget after 167 s of earlier cases, while the
  ordinary deadline subtest was 1 s into its expected 2 s wait. That exact subtest
  passed independently (2.134 s), without source changes. The command scanner's
  existing Ruby fixture wrongly expected a binding-less CURRENT runtime without
  terminal lifecycle proof to pass. It now proves refusal, restores the authentic
  original binding for positive/read-only/capability checks, and preserves the
  missing-creation-fence assertions. The initial chained Ruby host suite did not
  run. [B-owning-quick.log](B-owning-quick.log) retains the raw failed batch; its
  passes are not represented as a complete owning-suite pass. Final source-correct
  owning run uses the stock 10-minute package budget and per-test progress.
  No native SDK, hydrated browser or performance campaign ran.
- Full Ruby host milestone [B-ruby-host-final.log](B-ruby-host-final.log):
  346 tests / 5101 assertions, 5 failures, 0 errors, 2 existing skips. All five
  failures were tmux Unix-socket pathname overflow under the long Nix TMPDIR.
  Exact five passed with `TMPDIR=/tmp`: 5 tests / 314 assertions, 10.740 s.
  Filter: `--name '/test_failed_creation_candidate_(missing_authority_uses_original_live_terminal|authority_never_overwrites_existing_record|authority_rejects_changed_terminal_tuple|authority_publication_interruption_reuses_exact_record|authority_rechecks_context_before_publication)/'`.
  Existing skips are `archive_recovery_test.rb:12` and `:132` (owning Go CLI
  supplies executable fixtures); these are not new skips.
- [B-owning-final.log](B-owning-final.log) is a setup failure before tests: watcher
  omitted the required `nix develop --command` prefix and GCC was unavailable.
  No source or quick-green result is claimed. Exact final Nix/env compile preflight
  then passed all three packages (0.017/0.067/0.052 s), with GCC 15.2 wrapper,
  Go 1.26.6, Ruby 3.4.9, Node 24.19 and tmux 3.6a resolved; see
  [B-owning-preflight.log](B-owning-preflight.log).
- Final stock-10m JSON owning batch: exit 1, raw
  [B-owning-verified.log](B-owning-verified.log). Executable B input hash is
  `a00a953750c21604ff399cde19eaf5364d2a6b178588897409cdd9eb6b829478`
  (sorted staged non-Markdown paths plus five pins, each pathname NUL + bytes).
  Inputdelivery passed (3.212 s; 18 top-level tests); command/preflight passed
  (64.418 s; 185 top-level passes, 2 top-level skips). Web completed in 495.650 s:
  724 top-level passes, 18 top-level skips, 2 top-level failures. Counts including
  subtests are retained in JSON, not confused with top-level test counts.
  Its launcher retained Nix/PATH and short TMPDIR but mistakenly set empty
  NODE_PATH. The lead identified the unconditional APIRequestContext test's
  `require('playwright')` after launch. The selected package module path resolves
  Playwright 1.59.1, independently confirmed from the current flake's nixpkgs.
  The other failure was the existing shipped-client test's explicit dependency
  copy list missing the new `deliveries.js` import. The production route serves
  that module; adding it to this private fixture list is the only post-freeze
  source delta (one line in `server_test.go`). Ruby was not reached.
  Exact launcher command:
  `nix develop --command env -u PORTAL_BROWSER_TEST -u DEV_WORKSPACES_CODEX_PROVIDERS -u DEV_WORKSPACES_PI_PROVIDERS -u NODE_OPTIONS GOWORK=off TMPDIR=/tmp NODE_PATH= DEV_SESSION_REQUIRE_RUNTIME=0 sh -c 'go -C portal test -mod=readonly ./internal/inputdelivery ./internal/web ./cmd/workspace-portal -count=1 -timeout=10m -json && ruby test/workspace_host_test.rb --verbose'`.
- Both exact failing tests then passed (5.930 s):
  `nix develop --command env -u PORTAL_BROWSER_TEST -u DEV_WORKSPACES_CODEX_PROVIDERS -u DEV_WORKSPACES_PI_PROVIDERS -u NODE_OPTIONS GOWORK=off TMPDIR=/tmp NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules DEV_SESSION_REQUIRE_RUNTIME=0 go -C portal test -mod=readonly ./internal/web -run '^Test(PiAcceptanceFollowupScope|ShippedBrowserClientMatchesSessionAPI)$' -count=1 -timeout=45s -json`.
  Pi follow-up scope passed all five subcases (4.640 s); shipped-client HTTP/API
  contract passed (1.230 s). Full output:
  [B-owning-browser-repaired.log](B-owning-browser-repaired.log). No broad Go
  repeat or whole-package green claim substitutes for that recorded failed run.
  Final B executable/fixture hash after the copy-list correction:
  `e37a8666814fc4df95467146da8a7c29b4bcb44e73fc8e8624c0efbd020786bd`.
- Full Ruby host follow-up passed once under the same Nix/curated environment
  and selected module path, with `TMPDIR=/tmp` and `ruby test/workspace_host_test.rb
  --verbose`: **346 tests / 5405 assertions, 0 failures, 0 errors, 2 existing
  skips**, about 113 s. Raw [B-ruby-host-verified.log](B-ruby-host-verified.log).
  Both skips require executable fixtures supplied by owning Go CLI tests.
  This replaces the earlier long-TMPDIR Ruby failure with actual complete proof.
  All verification utilities and their owned tool sessions have completed.
  Exact command:
  `nix develop --command env -u PORTAL_BROWSER_TEST -u DEV_WORKSPACES_CODEX_PROVIDERS -u DEV_WORKSPACES_PI_PROVIDERS -u NODE_OPTIONS GOWORK=off TMPDIR=/tmp NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules DEV_SESSION_REQUIRE_RUNTIME=0 ruby test/workspace_host_test.rb --verbose`.

## Review and compatibility inventory

New portal queue schema 1 only; earlier unpublished fixture variants are
disposable. No native receipt, legacy SendRequest, native worker artifact codec,
shared native queue or existing SQLite schema migration. Negative identities and
retired disposition are in the final new queue v1 directly. The init lock is a
reconstructible private coordination file, not a receipt/schema change.

Owning docs: `docs/workspace-portal.md` (composer behavior),
`portal/internal/agentbackend/README.md` (API/storage/retention/recovery), shared
`docs/reference.md` (canonical provider contract), and shared
`docs/submission-storage.md` (native init lock). Lead directly rewrote the new
public prose/strings. The consumer API pointer targets matching published source
`db79231a` while the provider remains unmerged.

V's disjoint tagged real HTTP/Manager/supervisor/native SDK campaign source is
implementer0-owned; it and the narrow supervisor context seam are excluded from B.
V was committed after B, then amended for R1 and replayed unchanged after R2/R3.
Whole-branch independent review in `review.md` covered inherited history, A/C/B/V,
both provider commits, final pins, queue schema provenance, docs and fixture source.
The exact post-review correction provenance is below; no longer campaign ran here.

Documentation placement: the shared public API is authoritative in provider
`docs/reference.md`, linked at the exact matching provider head by
`portal/internal/agentbackend/README.md`. That README owns queue storage,
continuation, ambiguity, negative proof, retirement, cadence and package recovery
for maintainers. `docs/workspace-portal.md` owns user-visible composer and legacy
behavior. `docs/submission-storage.md` owns the native init lock and lock order.
Lead directly applied final prose passes; factual diffs agree with the source.

Remaining verification is explicit: lead acceptance of direct review corrections,
other applicable browser cases, real native SDK/restart/fairness/performance campaign, latency measurements and
applicable package/VM integration are not claimed complete. The default run's
18 web / 2 command top-level skips are existing opt-in browser/native/immutable
fixture or child-only cases; one nested foreign-owner check needs root. No B
queue tests were skipped. Lead owns the complete review/campaign packet and
publication. No merge, deployment, native schema migration or live mutation.
B has reported completion for acceptance and capacity; review fixes remain B's
responsibility, with no implicit next package queued.

## Narrow review remediation R2/R3

Lead explicitly assigned R2/R3 after the independent final report in `review.md`.
R3 delegates the existing web namespace helper to
`inputdelivery.ConversationScope`; the JSON array, SHA256 and prefix are unchanged.
The existing namespace test now pins
`pi-workflow-v1:3a6553beb792a8ce9ce1c9183401878aab947344c344f5f41076f2508680e21d`
for its fixed fixture and both web/public entry points. No API or persisted bytes
change. No product-documentation rewrite is useful for this owner consolidation.

Focused R3 checks passed (4.088 s), raw `B-R3-scope.log`:
`nix develop --command env -u PORTAL_BROWSER_TEST -u DEV_WORKSPACES_CODEX_PROVIDERS -u DEV_WORKSPACES_PI_PROVIDERS -u NODE_OPTIONS GOWORK=off TMPDIR=/tmp NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules DEV_SESSION_REQUIRE_RUNTIME=0 go -C portal test -mod=readonly ./internal/web -run '^Test(PiWorkflowDescriptorNamespaceUsesDurableScopeOnly|DurablePortalStableScopeRecoversAcrossOldBrowserGeneration|DurablePortalExistingIDSurvivesSelectionAndCapabilityChange|DurablePortalNegativeAdmissionProofSurvivesRestartAndLateOriginalPOST)$' -count=1 -timeout=45s`.

Exact existing runtime-key Ruby regression passed: 1 run / 13 assertions,
0 failures/errors/skips (0.029341 s), with
`nix develop --command env TMPDIR=/tmp ruby test/workspace_session_backends_test.rb --name test_current_runtime_projection_joins_original_or_successor_authority`.
R2 extracted that one-line contradiction fix into a prerequisite before B without
changing its existing tested final content. Implementer0 released revised V
`55f6adb1705acb229c338749139b03c372fcceec` before this history window began.

Authorized detached preparation worktree:
`worktrees/2026-11-23-pi-message-delivery/dev-workspace-r2-preparation`, based at
`82de924708e51e41ab9693759e75bccfc94cb9e9`; retained clean and detached at final
`ab3b1656`. Ordinary commits/cherry-picks/amend and hooks were used. Before
switching the original worktree, the captured and committed R3 patch was verified
and only those two owned working files were restored; the original was clean
before detaching and repointing its own feature branch. Shared master OID remained
unchanged. No broad reset, clean, stash, commit-tree, provider/pin or peer-ref edit.

Old range: `82de9247..55f6adb1` (reviewed B plus separately corrected R1 V).
New range: `82de9247..ab3b1656`: R2 `b4f3f288`, B `835aadce`, V `ab3b1656`.
Raw range-diff: [B-R2-R3-range-diff.log](B-R2-R3-range-diff.log). It shows only the
key fix extraction and R3 helper/test delta in B, with revised V equal.
Implementer0's R1 delta is separately retained in
[B-R1-owner-range-diff.log](B-R1-owner-range-diff.log), old `b16c0343` to `55f6adb1`.

Extraction/tree proof: after the standalone R2 commit and cherry-pick of old B,
intermediate `f82d7475c85a93c09868b3f9b81fb298f9fc330b` and original `e6b85c6b`
had identical tree `944fb8da150b03e80b49fdf7bda746b71c34de1c` before R3.
The complete final diff `55f6adb1..ab3b1656` is byte-identical to the captured
two-file R3 patch, SHA256
`4d6d0fabde5d80c35c8f6dcc6ea74351cc6e32a68cdb131cccfb2f148bfdbc4e`.
R2, all native V files and five pins have zero final-tree delta. The revised V
patch ID before/after replay is exactly
`dbad6a5949820c57eec1319c9f6edba4a249184a`. A/C, the single dependency commit and
all eight inherited deployed commits retain their exact identities/ancestry.

The exact existing Ruby regression on standalone `82de` fails with the expected
missing conflict (1 test / 9 assertions / 1 failure), then passes after only R2
(1 / 13 / 0 failures/errors/skips). Raw
[B-R2-prerequisite-before.log](B-R2-prerequisite-before.log) and
[B-R2-prerequisite-after.log](B-R2-prerequisite-after.log).
Final prepared head passed namespace compatibility (Go 0.057 s) and the exact
Ruby runtime regression (1 / 13, 0.033420 s), raw
[B-R2-R3-final-focused.log](B-R2-R3-final-focused.log). Same curated Nix environment
as the R3 command above; Go filter was exactly
`^TestPiWorkflowDescriptorNamespaceUsesDurableScopeOnly$`, timeout 30 s, followed
by the exact Ruby command above. No broad Go/Ruby repeat, new reviewer invocation,
native execution, schema or public-contract change. No live/lifecycle actions.
Completion and capacity were reported to lead and the history window released.

## H: hydrated composer preparation

Lead assigned H after R2/R3 acceptance. Its initial phase was preparation only,
with execution held for the lead's shared watcher slot and native-bootstrap gate.
During preparation no browser, dependency build, native worker or new test harness was launched;
no source or Git/index changes were made. The released execution result below
completes H and confirms capacity again.

Owning case: `TestQuestionBrowser/portal_delivery_browser_test.cjs`. The existing
Go fixture provides a disposable TLS server and actual portal HTML/assets. Its
five-line wrapper selects `PI_MESSAGE_ONLY=1` and `PI_DURABLE_ONLY=1` in the
existing `message_delivery_browser_test.cjs`, which runs both Chromium and
Firefox. Browser-controlled delivery HTTP covers native-transcript-unavailable
admission, queued status/reload, stale selection preserving draft, durable
negative proof/new explicit ID, lost-reply exact-ID recovery and truthful Unknown.
It checks zero legacy sends, page errors and unexpected request inventory. This
is a hydrated UI test with controlled delivery replies, not native dispatch or
SQLite/restart proof; the separate B/V tests own those boundaries.

Declared inputs were resolved from this repository's locked nixpkgs, without
building. `nix/workspace-portal.nix` declares `playwright-test` and its ordinary
preCheck NODE_PATH; the opt-in fixture additionally needs the browser store:

- Node: `/nix/store/l07gdbxylzfl8pbx9pxy6fyg95w4hjwy-nodejs-24.19.0`.
- Playwright test/module: `/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules`.
  Both `require.resolve('@playwright/test')` and `require.resolve('playwright')`
  pass under Nix, version 1.59.1.
- Core driver: `/nix/store/2xc3ahwfjaa3k3wpn4gslgws25swsyd7-playwright-core-1.59.1`.
- Browser root: `/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers`.
  Chromium expected path `chromium-1217/chrome-linux64/chrome` resolves to
  `/nix/store/6bplgf8qcq92qqp2bs6p0kxnp87lg21x-playwright-chromium/chrome-linux64/chrome`.
  Firefox expected path `firefox-1511/firefox/firefox` resolves to
  `/nix/store/bl197pyw5xzwr4c4asgkzd9ndb7cq9f1-playwright-firefox/firefox/firefox`.
  Both exist and pass executable access checks. Chromium uses the existing
  `channel: 'chromium'` launch; Firefox uses its declared default executable.
  Headless launch is existing fixture behavior; no display is needed.

Prepared exact command, cwd the registered dev-workspace worktree:

```sh
nix develop --command env \
  -u DEV_WORKSPACES_CODEX_PROVIDERS -u DEV_WORKSPACES_PI_PROVIDERS \
  -u NODE_OPTIONS -u PLAN_PRESENTATION_ONLY \
  GOWORK=off TMPDIR=/tmp DEV_SESSION_REQUIRE_RUNTIME=0 PORTAL_BROWSER_TEST=1 \
  NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules \
  PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers \
  go -C portal test -mod=readonly ./internal/web \
    -run '^TestQuestionBrowser$/^portal_delivery_browser_test[.]cjs$' \
    -count=1 -timeout=3m -v
```

Expected healthy duration is tens of seconds to two minutes (estimate, not a
measurement); Go timeout is three minutes. Run once through the lead-sequenced
fresh watcher, retain full log, stop expansion on the first failure/launch error
or timeout, and diagnose only the observed failure before any repeat. A timeout
requires accounting for/joining owned Node/browser children before reporting a
terminal result or using the slot again; it is not native acceptance evidence.
No compile repeat was needed: the exact final ab3 web test package already
compiled in the R3 focused check, and H introduces no Go or browser source change.
All browser paths are present; no missing prerequisite identified in preparation.

Lead released the exact H one-shot after prior bootstrap effects joined. Fresh
installed-policy Luna/low utility `h_hydrated_once` owns the run and full
`H-hydrated-once.log`; no other check/build or native campaign was launched.
Launch head `ab3b1656b80f35e26c33691ab2a21df035f73af6`, provider `db79231a`, web tree
`455f8fdf4ba98303c5cceb6632f24455af6b8389`. Hash of the six browser inputs
(`portal_delivery_browser_test.cjs`, `message_delivery_browser_test.cjs`,
`question_browser_test.go`, `static/app.js`, `static/pi-plan.js`,
`static/pi-workflow-ui.js`, each pathname NUL + bytes) is
`e2478e85f8b439613226f0a15426f80f623bcdedb06ebb37df337e1c294594f4`.
Source/Git mutation window stayed with implementer0; H made no source/index edits.

H passed on its first and only invocation: case
`TestQuestionBrowser/portal_delivery_browser_test.cjs` 15.54 s, parent test
15.63 s, package 15.695 s, total watcher wall 37 s, exit 0. Full stdout/stderr:
[H-hydrated-once.log](H-hydrated-once.log). The exact command above was executed
unchanged; argv is retained here and in the watcher receipt, rather than printed
as a header in that raw output log. The existing two-engine loop completed with
its durable-composer assertions; no fix or repeated run was needed.

The Nix wrapper realized its small `nix-shell-env` derivation; it did not build a
browser, application or missing dependency. TLS fixture certificate warnings
were logged, while the asserted browser/page/request checks passed. This is
hydrated controlled-HTTP UI evidence, not native delivery or latency evidence.
Post-run browser-source hash remained exactly `e2478e85...c294594f4`, with no web
working diff. Watcher tool session 83171 exited 0; its terminal report joined all
owned sessions/cells and bounded process inspection found no matching owned test,
Node or browser children. Shared utility slot released; lead received completion,
effects and capacity. Native V Recovery/Performance remains lead-held. No live,
session, package or lifecycle change was performed.

## F: exact CI lifecycle fixture correction

Lead assigned F after H acceptance. Source CI run 45319857029 attempt 1, head
`971070c53bc640d9bf691d51e2011a68247e8632`, fast job 138195516715 failed both
`DevSessionTest` and inherited `CommunicationTest` cases named
`test_waiting_lifecycle_rejects_a_new_conflicting_journal`. Downloaded raw log:
`/tmp/2026-11-23-pi-message-delivery-ci-45319857029-fast.log`, lines 4144–4154.
No CI job was rerun or canceled by F.

The fixture writes a newly conflicting deletion journal with plain `File.write`.
Under umask 022 that creates mode 0644. The existing Pi lifecycle selector at
`workspace-session-backends.rb:875` reads it with the unchanged private mode-0600
guard, rejecting before the intended unfinished-operation refusal. F changes
only that fixture line to `File.open(path, 'w', 0o600) { |file| file.write('{}') }`.
No production guard/helper, journal format or real lifecycle operation changes.

Exact reproduction/corrected command (registered dev-workspace cwd):

```sh
nix develop --command env TMPDIR=/tmp DEV_SESSION_REQUIRE_RUNTIME=0 \
  DEV_SESSION_SKIP_REAL_TMUX_TESTS=1 bash -c \
  'umask 022; ruby test/dev_session_test.rb --name "/\\A(?:DevSessionTest|CommunicationTest)#test_waiting_lifecycle_rejects_a_new_conflicting_journal\\z/" --verbose'
```

Before: 2 runs / 6 assertions / 2 expected failures, no errors/skips (0.097106 s),
[F-fixture-before.log](F-fixture-before.log). After: 2 runs / 8 assertions /
0 failures/errors/skips (0.118016 s), [F-fixture-after.log](F-fixture-after.log).
Patch SHA256 `7b5d2b27fdaa2376ee6f75bad87e8735d7b09b16a97ee7786f87fb0fd25026d6`.
Source/check work completed without index/history mutation during implementer0's
first V amend window. After its release, clean own detached preparation at
`worktrees/2026-11-23-pi-message-delivery/dev-workspace-f-preparation`, based at
unchanged B `835aadce`, created focused prerequisite
`26dbaf8447431bb598877464d3cd7b7720b0882e` (one file, one insertion/deletion).
The same exact two-case command under umask 022 passed on that standalone
prerequisite: 2 runs / 8 assertions / no failures/errors/skips, 0.099419 s;
[F-prerequisite-focused.log](F-prerequisite-focused.log).

Implementer0's revised V `e4d6f3ec6a0fbb64df75d90a622276b7e5927f6b` replayed
unchanged as final `389c0503d798f0ae5522d3dc260e0959ee7106c5`. Old range
`835aadce..e4d6f3ec` to new `835aadce..389c0503` shows the added F prerequisite
and V equal: [F-history-range-diff.log](F-history-range-diff.log). V stable patch
ID before/after replay is exactly `8a7e9b093ef1e8aa040f0b7f8103b77c7354abf4`.
The entire final diff `e4d6f3ec..389c0503` is byte-identical to the captured
one-file F patch above; production, native, web and pins have zero final-tree
delta. The separately owned V change from published CI head `971070c5` to revised
`e4d6f3ec` is retained in [F-V-owner-range-diff.log](F-V-owner-range-diff.log).
Do not describe that V correction as tree equivalence to the old CI head.

Normal Nix environment, hooks, commit and cherry-pick were used; no reset, clean,
stash, commit-tree or hook bypass. The original owned fixture change was restored
only after capture/commit/equivalence proof; original was clean before its own
feature branch was repointed. Original/index and detached F preparation are clean;
shared master OID is unchanged. A/C/R2/B/provider/pins and eight inherited deployed
commits retain exact identities/ancestry. Both history window release and capacity
were reported to lead and implementer0; no further F source/index mutation planned.
No app rebuild, broad Ruby campaign, new harness, push, CI rerun/retrigger/cancel,
native run or live/session/lifecycle action. Lead owns final publication and CI
handling; old failed CI remains diagnosed evidence, not a rerun-based pass.

## F2: offline-vendor recovery CLI fixture

Lead allocated F2 before P1 instrumentation; P1 production edits were not yet
allocated at that checkpoint. Exact CI run 45326414962 fast job 138216973541 failed
`TestPiMovedTrackingRecoveryPublicEntryAndRealOwners` at source 79dd. Downloaded
log `/tmp/2026-11-23-pi-message-delivery-ci-45326414962-fast.log`, lines 9154–9192,
shows the nested `go test -mod=readonly -c` ignoring the package vendor mode and
attempting module lookup with `GOPROXY=off`.

Only `portal/internal/web/pi_lifecycle_test.go` changes: the existing nested
compile uses explicit `-mod=vendor` when the module's `vendor/modules.txt` exists,
otherwise retains explicit `-mod=readonly`; unexpected stat errors fail the test.
No helper, production control, network enablement, skip or assertions changed.
This fixture-only correction needs no product-documentation rewrite.

Disposable proof root: `/tmp/pi-message-delivery-f2.IJYuXF`. A git archive of exact
79dd supplies source. The evaluated Nix goModules output was absent locally, so
`go mod vendor` populated only that disposable copy from already pinned cached
modules with `GOWORK=off GOPROXY=off GOSUMDB=off`; no module files changed and no
missing dependency or app/native build was requested. Existing web test binaries
were compiled from unchanged/corrected source with explicit readonly mode, then
the exact one test ran with the disposable module as cwd. The nested selected CLI
test compilation and complete existing Ruby/Go public-entry/real-owner assertions
remain real.

Before correction, with a vendor tree, `GOFLAGS=-mod=vendor`, fresh
`GOMODCACHE=/tmp/pi-message-delivery-f2.IJYuXF/empty-modcache`, `GOPROXY=off` and
`GOSUMDB=off`, the exact case reproduces CI's disabled-module-lookup failure in
0.21 s: [F2-offline-before.log](F2-offline-before.log).

Repaired ordinary checkout command:

```sh
nix develop --command env GOWORK=off GOPROXY=off GOSUMDB=off TMPDIR=/tmp \
  DEV_SESSION_REQUIRE_RUNTIME=0 go -C portal test -mod=readonly ./internal/web \
  -run '^TestPiMovedTrackingRecoveryPublicEntryAndRealOwners$' \
  -count=1 -timeout=60s -v
```

Passed: case 14.80 s, package 14.862 s, with original checkout `go.mod`/`go.sum`
hashes unchanged; [F2-checkout-after.log](F2-checkout-after.log). An earlier
invocation omitted `./internal/web` and stopped before compiling/running tests
(`no Go files in portal`); preserved [F2-checkout-setup-failure.log](F2-checkout-setup-failure.log),
then corrected without interpreting setup failure as a source result.

Repaired offline-vendor command (Nix invoked from registered source worktree):

```sh
nix develop --command env \
  -C /tmp/pi-message-delivery-f2.IJYuXF/source/portal/internal/web \
  GOWORK=off GOFLAGS=-mod=vendor GOPROXY=off GOSUMDB=off \
  GOMODCACHE=/tmp/pi-message-delivery-f2.IJYuXF/empty-modcache TMPDIR=/tmp \
  DEV_SESSION_REQUIRE_RUNTIME=0 /tmp/pi-message-delivery-f2.IJYuXF/web-after.test \
  -test.run '^TestPiMovedTrackingRecoveryPublicEntryAndRealOwners$' \
  -test.count=1 -test.timeout=3m -test.v
```

Passed once: case 41.84 s; [F2-offline-after.log](F2-offline-after.log). Fresh
installed-policy Luna/low watcher `f2_offline_vendor` tool session 80873 and its
owned cell completed exit 0; no outstanding work was reported. The module cache
contains only eight zero-byte lock files, no fetched modules. Disposable module
files remain byte-identical. No unmodified retry or broad package/CI rerun.

Captured one-file patch SHA256
`a898eebb0e977fd495cd3eecb43016b5bd899cadffdfac72d7c819d31f2f5d59`;
7 insertions / 1 deletion. After implementer0 released P0
`b0d2411f4737abb24e5c81b26666b6a2949db2b5`, F2 was committed normally as
`ea17a752b27afe1a7a73336b8c100e8fb79e7f48`, exact parent P0. Only the captured
fixture path was staged; ordinary hooks were not bypassed, gofmt/diff checks were
clean, and original tree/index are clean. No previous history was rewritten.
Completion, Git window release, settled effects and capacity were reported to
lead and implementer0. No source/index/build/push changes outside this fixture or
actual session/lifecycle actions. At F2 completion, P1 trace instrumentation was
still unallocated; lead subsequently released the explicit package below.

## P1: local admission and dispatcher trace boundaries

Lead explicitly released P1 after accepting F2 and capacity. Completed normally
as `06680120cd3004afe785043c47781e15cbae66b7`, exact parent
`ea17a752b27afe1a7a73336b8c100e8fb79e7f48`. Only
`portal/internal/web/pi_input_delivery.go` and
`portal/internal/inputdelivery/store.go` changed: 128 insertions / 12 deletions.
No tests, pins, schema, public interfaces, SQL, native calls, authorization checks
or lock ordering changed. Named return values support bounded deferred outcomes;
existing return values, cancellation and authority remain unchanged. Near-code
comments explain the commit/claim endpoints and grouped admission boundary; no
product documentation or visible strings needed changing for this instrumentation.

Standard `runtime/trace` regions use prefix `pi.delivery.` with these exact
suffixes:

| Source/boundary | Region suffixes |
| --- | --- |
| Local resolution/joins | `resolve`, `resolve.transition`, `resolve.ready_join`, `local_join`, `verify`, `selected` |
| Admission | `admit`, `admit.resolve`, `admit.uploads`, `admit.store` |
| Store | `store.registration_wait`, `store.gate_admission`, `store.connection_wait`, `store.sql_callback`, `store.commit`, `store.update` |
| Dispatcher admission | `dispatch`, `dispatch.foreground`, `dispatch.session_admission`, `dispatch.selected`, `dispatch.continuation`, `dispatch.lease` |
| Effect callback | `dispatch.effect`, `dispatch.message_lock`, `dispatch.bind_verify`, `dispatch.uploads`, `dispatch.claim`, `dispatch.checked_input` |
| Original-reference recovery | `lookup` |

Driver tasks `pi.delivery.dispatch` and `pi.delivery.lookup` log the saved original
ID. `trace.IsEnabled()` guards task allocation and admission conflict
classification. Standard trace operations handle disabled tracing; no metadata
serialization, observer, timer, configuration or retained state was added. There
is no quantitative overhead claim. Events contain original IDs, constant phases
and bounded outcomes only, with no message, file, credential or mutable-state
contents:

- `pi.delivery.commit`: queued/committed only immediately after the real `COMMIT`
  Exec returns nil. Existing-ID, conflict and rollback paths cannot emit it.
- `pi.delivery.cas`: original ID, from/to, SQL-error or won/error booleans;
  `pi.delivery.claim` only after queued-to-dispatching UPDATE and RowsAffected=1,
  explicitly `won_post_commit_upper`.
- `pi.delivery.{resolve,admit,dispatch,lookup}.outcome`: error boolean and, where
  available, phase; admission distinguishes ok/error/conflict.

Do not sum nested regions. Store gate admission ends at callback entry or refusal,
before connection wait/SQL. SQL callback includes its existing Go validation/JSON
work. Session admission includes lock waiting plus owning validation, and lease
spans its pre-callback proof. No exact runtime-lock grant is claimed. Checked-input
port time remains a grouped native boundary; P0's independent receipt/witness and
native commit-write observation establish separate native evidence. Initial/final
local and selection checks remain distinct by call order around admission uploads.

All checks used the registered repository's Nix environment with short temporary
paths and the declared Playwright module, with no native browser/runtime flag:

```sh
nix develop --command env \
  -u PORTAL_BROWSER_TEST -u DEV_WORKSPACES_CODEX_PROVIDERS \
  -u DEV_WORKSPACES_PI_PROVIDERS -u NODE_OPTIONS \
  GOWORK=off TMPDIR=/tmp DEV_SESSION_REQUIRE_RUNTIME=0 \
  NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules \
  bash -c 'set -e
    go -C portal test -mod=readonly ./internal/inputdelivery -count=1 -timeout=45s
    go -C portal test -mod=readonly ./internal/web -run "^TestDurablePortal" -count=1 -timeout=60s
    go -C portal test -mod=readonly -tags=pi_native_fixture ./internal/piruntime -run "^$" -count=1 -timeout=30s'
```

Passed with tracing disabled: store 2.810 s, focused native-free web 11.308 s,
tagged piruntime compile 0.061 s (no tests run), including committed P0 source.
Raw [P1-quick.log](P1-quick.log). Existing store cases cover denied/canceled gate,
commit failure, immutable admission and restart/CAS recovery; no new mirror tests.

One trace smoke used the same wrapper, with these commands instead:

```sh
go -C portal test -mod=readonly ./internal/inputdelivery \
  -run '^Test(IndexedAdmissionIsImmutableAndSurvivesRestart|DeniedTransitionDoesNotOpenOrCloseSQLite|TerminalCloseCancelsAndJoinsTransitionWaiters|AcceptedNativeWithFailedQueueCommitUsesOriginalLookup)$' \
  -count=1 -timeout=30s -trace=/tmp/pi-message-delivery-P1-store.trace
go -C portal test -mod=readonly ./internal/web \
  -run '^TestDurablePortal(SuccessorClaimsFreshExecutionAndPreservesAdmission|LookupRequiresExactRetirementAndPreservesSafeRefusal)$' \
  -count=1 -timeout=45s -trace=/tmp/pi-message-delivery-P1-web.trace
go tool trace -d=parsed /tmp/pi-message-delivery-P1-store.trace > /tmp/pi-message-delivery-P1-store.parsed
go tool trace -d=parsed /tmp/pi-message-delivery-P1-web.trace > /tmp/pi-message-delivery-P1-web.parsed
```

Passed once: four store cases 0.344 s, two web cases 2.470 s, both trace parses
exit 0; [P1-trace-quick.log](P1-trace-quick.log). Region counts balance by name:
store 124 begin/end across six types, web 80 begin/end across 29 types including
Store regions. Actual successful-COMMIT and won-claim markers appear in both;
web trace contains six Driver tasks. Trace artifacts remain disposable in `/tmp`.
This is instrumentation correctness smoke, not target-pass latency evidence.

Tested source SHA256, over sorted path + NUL + bytes for these two files, is
`76215f60e1a5e286d81cb823e227aeda02c36eb4a1c56918172881e1c31ae999`;
commit staged exactly that frozen source. Gofmt and whitespace checks were clean;
ordinary Nix Git commit used no hook bypass. Original tree/index are clean,
all parent-owned tool sessions joined exit 0, and Git/source window is released.
No utility, native diagnostic, application build, performance cell, broad suite,
CI push/rerun or session/lifecycle action occurred. Capacity is available after
lead acceptance; there is no implicit next package. Lead owns affected review of
committed P0/F2/P1 before the single three-minute four-input StageDiagnostic.

## P1 followup: four-ID measured local stages

Bounded read-only attribution of the lead-owned StageDiagnostic at exact source
`06680120cd3004afe785043c47781e15cbae66b7`; the native run and trace parsing were
already complete. Raw `/tmp/2026-11-23-pi-message-delivery-stage-06680120.log`
reports case 59.51 s / package 59.680 s, exit 0. Artifact root is
`/tmp/pi-message-delivery-stage-06680120.KZPkOb/`; actual fixture workspace is
`/tmp/TestPiMessageDeliveryNativeStageDiagnostic909447311/001/workspace`.
Lead confirmed process scan/effects settled. The utility source-text SHA typo
does not change the actual 0668 artifact provenance.

Existing `trace.parsed` (3,078,301,832 bytes) was streamed through targeted
Region/Task/Log filters; binary trace was not reparsed or the full text loaded
into memory. The bounded raw `P1-events.txt` has 7,496 target lines (including
Category=originalID and HTTP request/response logs). This extract is not globally
ordered; event timestamps pair regions/tasks. `P1-four-ID-table.json` retains
the four correlated absolute endpoints and category durations. These are data
extracts, with no added analysis runner/framework.

All IDs below are the full 32-character original ID ending in the shown suffix.
POST request log, HTTP task, nil-COMMIT event, Driver original-ID task and won-CAS
event correlate uniquely. Native commit-write frames additionally match member,
native ID and generation from each sample; matching frame UUID return logs prove
full successful writes. All four samples are Sent with independent Accepted/count1.

HTTP categories below are **mutually nonoverlapping elapsed wall time**, not CPU
time. Five joins are resolver ready-identity plus four local joins; selection has
two calls. SQL callback excludes its nested COMMIT region. Other is the remainder
of the HTTP task, so each column partitions its task duration (rounding aside).

| HTTP category, ms | 1007 lead | 1008 architect0 | 1009 implementer0 | 100a observer0 |
| --- | ---: | ---: | ---: | ---: |
| Five ready/local joins | 191.149 | 214.284 | 218.246 | 227.409 |
| Two selections | 34.644 | 30.038 | 30.589 | 32.322 |
| Uploads | 1.121 | 14.431 | 0.804 | 0.830 |
| Store initial mutex wait | 0.006 | 0.007 | 0.005 | 8.976 |
| Store gate admission | 0.128 | 0.240 | 0.155 | 0.185 |
| Store connection mutex wait | 0.004 | 6.238 | 0.004 | 0.005 |
| SQL callback excluding COMMIT | 2.117 | 1.726 | 4.809 | 2.036 |
| COMMIT region | 3.969 | 2.648 | 3.556 | 3.360 |
| Other HTTP | 5.933 | 10.047 | 10.756 | 9.859 |
| HTTP task total | 239.071 | 279.659 | 268.924 | 284.981 |

Five joins consume roughly 80% of POST time here. COMMIT regions are only
2.648–3.969 ms; the SQLite/fsync boundary is not the principal local admission
cost in this diagnostic. Trace logging overhead is present and not quantified.
No percentile, sustained-load conclusion or target-pass claim follows.

Pipeline table is start–end offset in ms from each original HTTP task start.
Lease includes effect/callback and therefore overlaps later rows; do not add those
totals. Session admission groups lock waiting and owning validation.

| Pipeline span | 1007 | 1008 | 1009 | 100a |
| --- | ---: | ---: | ---: | ---: |
| Driver | 245.502–1304.670 | 298.333–2094.991 | 275.257–711.823 | 298.623–2693.733 |
| Foreground | 245.903–246.008 | 298.622–298.642 | 275.552–275.576 | 299.078–299.111 |
| Session admission aggregate | 246.012–755.496 | 298.645–1763.237 | 275.578–435.680 | 299.114–2134.037 |
| Selection | 756.009–765.715 | 1771.846–1787.552 | 446.020–456.849 | 2137.937–2151.607 |
| Continuation | 765.728–766.993 | 1787.572–1788.892 | 456.877–460.251 | 2151.626–2152.605 |
| Lease inclusive | 767.001–1304.560 | 1788.900–2094.870 | 460.267–711.725 | 2152.610–2693.641 |
| Effect callback inclusive | 811.913–1304.551 | 1825.400–2094.862 | 504.767–711.719 | 2192.236–2693.633 |
| Message lock | 811.921–811.927 | 1825.415–1825.418 | 504.778–504.782 | 2192.244–2192.247 |
| Bind + Verify | 811.931–1172.343 | 1825.420–1972.521 | 504.785–585.326 | 2192.248–2545.190 |
| Upload validation | 1172.362–1173.238 | 1972.527–1975.438 | 585.331–586.033 | 2545.196–2545.994 |
| Claim callback | 1173.241–1177.722 | 1975.445–1987.256 | 586.037–590.658 | 2545.998–2550.611 |
| C checked-input port | 1177.728–1304.492 | 1987.261–2094.839 | 590.662–711.697 | 2550.616–2693.612 |

| Exact boundary | 1007 | 1008 | 1009 | 100a |
| --- | ---: | ---: | ---: | ---: |
| HTTP task ID | 84 | 83 | 85 | 82 |
| HTTP task start, trace ns | 2100009789051904 | 2100009788891904 | 2100009789114944 | 2100009788736064 |
| Successful COMMIT event, trace ns | 2100010027679232 | 2100010068195008 | 2100010057340096 | 2100010072961984 |
| Won claim event, trace ns | 2100010966731264 | 2100011776092160 | 2100010379728192 | 2100012339287744 |
| Successful COMMIT offset, ms | 238.627 | 279.303 | 268.225 | 284.226 |
| COMMIT to Driver start, ms | 6.875 | 19.030 | 7.032 | 14.397 |
| COMMIT to won claim, ms | 939.052 | 1707.897 | 322.388 | 2266.326 |

The HTTP trace task is contained by the fixture complete-body sample interval.
Outer-minus-task duration bounds the unresolved start offset, but cannot split
entry/exit overhead: 0.010136 / 0.016753 / 0.019797 / 0.006486 ms, plus trace
quantization. Actual successful-COMMIT event offsets are within this epsilon of
the outer start. Native frame-enter trace logging formats its full handle after
the actual write-entry hook; use the correlated sample hook, not that later trace
log, for the acceptance upper endpoint.

| COMMIT to matched native acceptance-write upper, ms | Lower | Upper |
| --- | ---: | ---: |
| 1007 | 1477.888 | 1477.898 |
| 1008 | 2160.347 | 2160.363 |
| 1009 | 809.633 | 809.652 |
| 100a | 2803.602 | 2803.609 |

Original-ref production lookups: 1007 181.916 ms (Sent), 1008 158.765 ms
(Sent); 1009 17.143 ms (Pending), then 478.138 ms (Sent); 100a 18.404 ms
(Pending), then 134.289 ms (Sent). These are Driver-task inclusive elapsed
intervals. P0 owns the nested Manager, persisted native witness, hook and question
evidence; no native-operation completion or question progress is inferred here.

The dominant pre-native measured boundary for later IDs is session admission
(160.102–1834.923 ms), with unresolved wait versus validation. Bind+Verify is
80.541–360.412 ms; checked port is 107.578–142.996 ms. Lease pre-callback proof
is 36.500–44.912 ms. An exact runtime-lock grant marker is the smallest separate
boundary if lead needs that split; it is not implemented or implicitly allocated.
For local joins, the next unmeasured leaf split is `piReadySessionIdentityLocked`
calling `piRetainedRootIdentityLocked` versus preceding binding/authority reads;
`local_join` also includes `projectPiConversationAdmission`. No leaf optimization
is established by these grouped durations.

Routine P2 safety clarification: reusing the earlier own-Verify snapshot
across Store.Resolve would remove the fresh post-Resolve scope/access boundary
before refusal/upload effects. `piSessionUploads` is not a fresh auth join and
can AdoptInitial/SessionScope/Prepare using the supplied snapshot. That proposed
reuse was rejected. A different proposed private ordering, exact-ID/profile check
then read-only Resolve capture then mandatory fresh verifyCurrent before exposing
**any** row/conflict/refusal/error or entering selection/reject/uploads, has no
concrete invariant break found in the inspected owning path. Resolve is SELECT/
decode/comparison only; final post-upload full tuple checks must remain. Moving
private SQL before the provider own full Verify is an explicit ordering delta
for architect/lead acceptance, not an authorized edit or target-pass prediction.
Resolver/shared HTTP verification remains before that private read.

Completion: attribution and bounded safety clarification reported directly to
architect0/implementer0 and lead. No source/index/native/build/test/push/rerun,
200-sample or 100k work occurred. Architect recorded the sufficient conditionally
accepted private-ordering correction brief; implementation still requires lead's
explicit package release. No active utility/tool or effect remains owned
by I1. Capacity is available for an explicitly allocated next package. I0 meanwhile
committed F3 as `1cbeeb50972adf5e2b57ef08961f1550f689631b` atop 0668; its later
fixture correction is not covered by this already-completed native diagnostic.

## P2 local: reuse the fresh post-Resolve admission

Lead accepted the attribution and explicitly released this complete source
package against the final P2 local brief. Normal focused commit
`09f44a72fe384d5a9756b880711c826c4e0f76c1`, parent
`1cbeeb50972adf5e2b57ef08961f1550f689631b`, changes only
`portal/internal/web/pi_input_delivery.go` and its existing test file:
247 insertions / 10 deletions, including 225 test lines. No previous history,
provider/pins, SQL/store, public API, browser, schema, native call or receipt changed.

Private `verifyCurrent` performs the complete original Verify contract and returns
the freshly proved local admission; public Verify remains its error-only wrapper.
For Admit, exact bound identity, the existing canonical scope encoder and host
profile are checked before private Resolve. Its result/error remains private until
mandatory full fresh verification afterward. Authorization failure overrides
existing status, conflict, negative proof, absence, storage error and cancellation.
Only then are outcomes processed, using the returned admission for new selection.
This preserves the post-Resolve scope/access barrier before Reject or upload/catalog
effects. No earlier authority is reused or cached. The final post-upload local and
selected reread/full-tuple equality and separate native dispatch proofs remain.

The only removed work is one discarded full local join per new POST. No measured
latency improvement or target pass is claimed. Existing trace names remain truthful:
`pi.delivery.verify` now brackets that same full contract in verifyCurrent after
the private read, and `admit.resolve` still brackets only Resolve. Near-code comments
explain result/error precedence; no product prose or public contract needed changing.

The two new focused tests use existing disposable real handler/store fixtures and
the existing transition Gate, with no sleeps or production hooks:

- Three cheap-boundary cases prove different identity, a bound noncanonical scope
  and a missing current profile refuse before any Store call.
- A 36-cell matrix covers existing exact row, changed-request conflict, authentic
  durable refusal, not-found, injected gate/read error and canceled request, each
  with access/scope/generation revocation after the private SELECT and through
  both direct provider and actual HTTP handler calls. Saved access is revoked by
  removing its valid role value; `read_only` message permission remains unchanged.
  Each denial returns no status/proof, performs exactly the one Resolve Store
  access, performs no selected read or native Bind/dispatch/lookup/inspect, and
  preserves upload catalog bytes/existence. The direct path asserts exact fresh
  authorization errors, overriding even the captured durable refusal proof.
- Existing old-ID coverage now also repeats the original POST with CheckedInput
  false and with a retained runtime lacking the optional checked-input interface.
  Settings changes, stale new selection, immutable negative IDs, restart,
  successor/retirement, native-lock-held zero-RPC admission, ordered uploads and
  final selection changes during preparation retain their existing regressions.

An initial compile-only failure used an invalid Go equality comparison against the
slice-containing DeliveryStatus struct in two assertions. Corrected those to
DeepEqual before executing tests; [P2-local-focus.log](P2-local-focus.log) retains
the failure, with no passing source/test claim from that launch. Corrected new
tests passed in 8.463 s; [P2-local-focus-after.log](P2-local-focus-after.log).

The final frozen source used the exact owning environment:

```sh
nix develop --command env \
  -u PORTAL_BROWSER_TEST -u DEV_WORKSPACES_CODEX_PROVIDERS \
  -u DEV_WORKSPACES_PI_PROVIDERS -u NODE_OPTIONS \
  GOWORK=off TMPDIR=/tmp DEV_SESSION_REQUIRE_RUNTIME=0 \
  NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules \
  bash -c 'set -e
    go -C portal test -mod=readonly ./internal/web -run "^TestDurablePortal" -count=1 -timeout=75s -v
    go -C portal test -mod=readonly -tags=pi_native_fixture ./internal/piruntime -run "^$" -count=1 -timeout=30s'
```

Passed once: affected native-free durable web suite 19.558 s; tagged piruntime
compile 0.059 s, no tests run. Raw [P2-local-owning.log](P2-local-owning.log).
No broad Go/Ruby repeat or native run. Unchanged Store source retains P1's checks;
this package does not substitute compilation for native/performance acceptance.

A shortest faithful red proof used `go test -overlay` with only the production
file mapped to exact parent 1cbeeb source, retaining the new regression tests.
The original repository files and index were never switched. Under the same Nix
wrapper, the selected filter was:

```sh
go -C portal test -mod=readonly \
  -overlay=/tmp/pi-message-delivery-P2-local-overlay.json ./internal/web \
  -run '^TestDurablePortalAdmissionFreshAuthorizationOverridesEveryPrivateOutcome$/^(existing|refusal)$/^direct$/^access$' \
  -count=1 -timeout=30s -v
```

Both old-source cases fail in 2.321 s as intended: an existing saved status returns
success after revocation, and an authentic negative proof beats fresh denial.
The launcher verifies Go exit 1, and the captured failure names/messages establish
regression rather than setup failure; [P2-local-old-regression.log](P2-local-old-regression.log).
The repaired complete owning suite above covers both plus the full matrix.

Tested sorted-path + NUL + file-bytes SHA256 is
`4e525671bedf90a224a5e1779a31daf7c5856e5ac94360f1142c2b887db02132`;
the commit guard checked exact equality and staged only those two paths. Gofmt,
whitespace and ordinary Nix commit/hooks passed without bypass. Tree/index were
clean at release and all own tool sessions settled. I0 received explicit source,
check and index release with the full head and now owns the allocated N1 combined
API/runtime/driver/mock window. No further I1 source/index edits or checks planned.
Tracking evidence is the only post-release I1 write. Capacity is confirmed for an
explicitly assigned next package. No app build, push, native diagnostic/benchmark,
200-sample campaign or session/lifecycle action occurred. Lead owns affected review,
rebuilt exact candidate and corrected performance verification; no implicit rerun.

## P3: corrected-probe stage comparison

Read-only comparison of exact e6626ff692bc99c3d9efb0fe428333dfe29759fc after
accepted P2-local/N1 source. Lead owns the corrected native probe (package
59.896 s, passed), exact candidate/provenance and settled-worker check. I1 waited
for the explicit events-ready receipt before reading the utility output. The
one utility transform completed exit 0 in 77.297 s; no full 3 GB text file was
written. I1 consumed only ready `events.txt` (7,975 lines / 1,140,078 bytes) and
the existing JSONL under `/tmp/pi-message-delivery-corrected-probe-e6626ff6.MrNuiB/`,
plus the prior 0668 four-ID table. No trace binary reparse, native/test/build or
source/index mutation. Bounded per-ID endpoints are `P3-four-ID-table.json`.

Each ID below is the complete 32-character original ending in its suffix. POST
task, successful COMMIT, Driver and won claim correlate by full ID; native
commit-write frame additionally matches member/native ID/generation and a full
successful frame return. Native hook uses the sample's original saved write-entry
time, not the later formatted frame-enter trace log.

HTTP elapsed categories below are disjoint. SQL excludes nested COMMIT; Other
is the complement. Each column partitions its HTTP task, not CPU usage.

| HTTP boundary, ms | 1007 lead | 1008 architect0 | 1009 implementer0 | 100a observer0 |
| --- | ---: | ---: | ---: | ---: |
| Four ready/local joins | 146.111 | 161.189 | 159.021 | 170.993 |
| Two selection reads | 31.426 | 30.292 | 28.647 | 26.024 |
| Uploads | 0.903 | 0.753 | 0.567 | 0.562 |
| Store registration wait | 0.005 | 4.294 | 2.599 | 5.760 |
| Store gate admission | 0.147 | 0.190 | 0.172 | 0.206 |
| Store connection wait | 0.005 | 0.007 | 0.006 | 10.448 |
| SQL excluding COMMIT | 2.059 | 2.293 | 2.351 | 2.606 |
| COMMIT region | 11.665 | 3.090 | 3.231 | 4.808 |
| Other HTTP | 6.224 | 13.855 | 12.529 | 11.878 |
| HTTP task total | 198.545 | 215.963 | 209.123 | 233.286 |
| Successful COMMIT offset | 198.052 | 214.055 | 208.671 | 231.868 |
| COMMIT to Driver start | 5.441 | 11.060 | 16.255 | 14.282 |

Exactly four joins per POST are observed, versus five in 0668. This confirms
the intended call-count reduction. HTTP outer sample endpoints are
198.560457 / 215.981615 / 209.146544 / 233.292876 ms. Task start lies inside
that complete-body interval with unresolved entry/exit widths bounded by
0.015369 / 0.018671 / 0.023152 / 0.007244 ms, plus trace quantization.
COMMIT remains a small fraction of HTTP time, although the lead region is
11.665 ms in this probe. No zero-overhead or percentile claim is made.

| Driver elapsed span, ms | 1007 | 1008 | 1009 | 100a |
| --- | ---: | ---: | ---: | ---: |
| Foreground admission | 0.030 | 0.026 | 0.017 | 0.024 |
| Session admission aggregate | 2014.120 | 345.719 | 1313.669 | 617.782 |
| Lease inclusive | 612.042 | 232.558 | 561.030 | 607.704 |
| Effect callback inclusive | 580.308 | 186.943 | 517.494 | 557.815 |
| Required positive preflight | 323.644 | 47.454 | 386.407 | 417.079 |
| Claim callback | 13.123 | 5.247 | 17.402 | 6.820 |
| Checked C port | 242.542 | 133.324 | 112.996 | 132.672 |
| Lease before callback | 31.720 | 45.601 | 43.528 | 49.882 |

Lease/effect totals include their child rows and must not be added. Session
admission includes lock wait and owning validation; no exact grant timestamp is
claimed. N1's preflight is the required fresh positive preclaim proof, replacing
the earlier Bind plus immediate Verify; observed costs are not an authority to
drop it. Original-only production lookup intervals are:

- 1007: 3116.785–3482.401 ms (365.615 ms, phase=sent error=false).
- 1008: 1123.627–1139.553 ms (15.926 ms, phase=pending error=false); 1378.646–1977.286 ms (598.641 ms, phase=sent error=false).
- 1009: 2377.671–2395.816 ms (18.145 ms, phase=pending error=false); 2625.699–2850.587 ms (224.888 ms, phase=sent error=false).
- 100a: 1879.643–1893.032 ms (13.389 ms, phase=pending error=false); 2122.615–2572.737 ms (450.121 ms, phase=sent error=false).

| COMMIT to matched native acceptance-write upper, ms | Lower | Upper |
| --- | ---: | ---: |
| 1007 | 3195.798 | 3195.814 |
| 1008 | 1126.092 | 1126.111 |
| 1009 | 2368.999 | 2369.022 |
| 100a | 1749.321 | 1749.328 |

The original and corrected four-message workloads differ: original 0668
admission/claim order was implementer -> lead -> architect -> observer; corrected
e662 is architect -> observer -> implementer -> lead. The corrected question is
a real accepted competing operation, replacing the old invalid quiet-interval
answer. These four IDs therefore cannot establish a causal per-ID latency delta,
marginal percentile improvement or sustained target pass.

Global ordering below uses earliest queue HTTP task trace clock `2103184519784576` ns
as time zero. Successful session admission returns while owning EX; the code
defers release through lease completion. Consequently admission-region end to
lease-region end is a **minimum proved EX-held subinterval**. Driver TaskEnd is
not used, because deferred release precedes that later event.

| Original, in actual order | Proved EX-held interval, ms | Other proved dispatch EX overlapping own admission, ms |
| --- | ---: | ---: |
| 1008 | 571.439–824.671 | 0.000 |
| 100a | 864.308–1493.862 | 253.232 |
| 1009 | 1539.582–2125.921 | 882.786 |
| 1007 | 2218.504–2847.841 | 1469.124 |

This proves at least 1469.124 ms of lead's 2014.120 ms admission aggregate,
882.786 ms of implementer's 1313.669 ms, and 253.232 ms of observer's 617.782 ms
coincide with another dispatch's definite ownership of the same EX lock. Those
overlaps prove EX was unavailable to this request, not exact mutex wait: pre-lock
checks and scheduling before acquisition have no separate marker. Post-grant
validation cannot run then. Architect's first aggregate has no such overlap.

Real question POST task102, response UUID
`ce9bef71-295e-4ee8-8d23-be64b9c4e6f0`, spans global 519.774–3455.177 ms
(2935.403 ms); it returns 202 with sequence1. Its HTTP interval overlaps
2098.461 ms of the other dispatches' proven EX ownership; that is not question
EX hold. I0's owning proof, confirmed by child178 Parent=102, places
Manager.InspectNativeOrigin at trace 2103187410873408–2103187908442944 ns,
global 2891.089–3388.659 ms: 497.570 ms is a proved question EX-held subinterval.
The remaining roughly 339.373 ms is unclassified; the whole POST is not an exact
lock-wait or hold measurement.

I0 places the question's actual native send at global +4278.513 ms, after all
four queue timed endpoints. It cannot explain their earlier dispatch waits. The
question's capture/origin proof overlaps lead's asynchronous input-wait-to-commit
interval, but timing alone does not establish which controller/native activity
blocks which. I0 owns its native acceptance/witness and cancellation-tail facts;
the question is genuinely admitted/accepted, not evidence of starvation.

Dominant remaining measured stage is session admission, with substantial overlap
while EX is unavailable and required preflight/checked-port work in proved holds. No safe
further B correction is established. The precise unresolved native boundary is
controller waiting versus identity/RPC/read work inside the required 47–417 ms
preflight, plus the separate post-Pending receipt continuation. Removing probes,
weakening EX/witness, caching authority or moving an unready request past claim
is not justified. Architect receives the stage table/constraint; no new marker,
profiler, campaign or production change is proposed by this package.

Comparison complete; all I1 extraction tools settled, source/index unchanged,
capacity confirmed available for explicit allocation. Lead owns acceptance and
subsequent review/source/verification sequencing.

## F4: bounded retained-start refusal parsing in creation VM

Lead explicitly allocated the independent fixture correction after P2/P3 capacity.
Initial source head is `176706a605119b64f4efd24f0b2f25957caa7298`; P4 Go/Node/docs
changes belong to I0 and remain untouched. I0 explicitly released the window at
P4 `329eef86e18a0f88ad651f91dbc1a3450c5dedc9`. F4 is committed normally as
`474872b602afa0813e6a17a951646b5cf5a91a06`, exact parent that P4 head. Only the
owned Nix file was staged; its tested source/patch hashes match. The guard also
proved P4 changed neither this Nix file nor the Ruby/helper fixture inputs, so the
focused evidence retains its exact source scope without repeating unchanged checks.

CI run 45348306901 creation job 138288188603 failed generated line1241/helper52
at session_source in the proxy-created-root source-permission/client recovery
stage. Raw `/tmp/2026-11-24-pi-message-delivery-ci-45348306901-creation.log` has
the exact status1 two-line output: bounded retained-start contention JSON then
the same-slug ordinary busy refusal. The later READ-lock rows are explicitly a
subsequent non-atomic sample, not proof of the original failed flock holder/cause.
No lock policy, production behavior or portal-lifecycle change is inferred.

Sole owned source is `nix/tests/session-creation.nix`, 134 insertions / 2 deletions.
Pure session_source_refusal preserves exact plain refusal for start/sync. The
diagnostic form requires start, status exactly integer1, exactly two lines with
only optional final newline, diagnostic prefix plus valid JSON object, requested
EX|NB, the exact existing fixture authority path and explicit noncausal
interpretation. Its byte bound includes the diagnostic newline, matching the
existing emitter's 8192-byte limit. Malformed/duplicate/nonfinite JSON, wrong
scope/operation/refusal/status, extra output and oversized UTF8 refuse. Sampled
holders and sample/path status are not retry authority. No substring/last-line
matching, success conversion or new retry/deadline/action was introduced.

Source-local pure cases cover old plain forms, normalized actual diagnostic,
optional newline, unknown holder observations, required fields, wrong action/path/
slug/status/type, extra/duplicate lines, malformed/ambiguous JSON and exact byte
limits. A fake clock/execute transport drives the **actual** session_source loop:
plain refusal -> diagnostic refusal -> unchanged successful bytes, sync plain
compatibility, persistent busy at the original deadline, unknown first-attempt
failure, invalid result and transport exception. Globals are restored in finally;
no VM/CLI command is executed by these regressions.

Native-free before proof executes the original helper definition extracted from
the source against the **exact actual CI output** parsed from the assertion tuple.
It reproduces start failed on attempt1 without sleep; the old plain-refusal
control retries once and preserves success bytes. [F4-before.log](F4-before.log).
Original file SHA256 is
`0d0743aa727be75387291bad379123956307a07861fb7f6542667dce86bdf54f`;
actual output SHA256 is
`8dee2efc18f23c010287ac58c9ad1d2a2f1d8d87879efff6ee7e3381b8bd8eb8`.
Its diagnostic line is 917 bytes, within the existing emitter limit.

After proof runs the actual source-local helper/classifier/regression definitions
through source-derived Python AST under the owning Nix environment, with
TMPDIR=/tmp and DEV_SESSION_REQUIRE_RUNTIME=0. Whole testScript Python syntax,
all pure cases and exact actual-CI replay pass: three identical command attempts,
timeouts20/19/19, logical sleeps0.25/0.25 and unchanged success bytes. Persistent
busy keeps the existing 20-second budget/integer timeout behavior (77 instant
fake attempts, stopping when less than one integer second remains). No real
wait or extra runtime retry was tested or added. [F4-python.log](F4-python.log).

AST comparison against the original source proves the loop is unchanged except
the refusal predicate and relocated refusal literal. The source before the helper
and every byte from browser onward are identical, preserving all original
commands, deadlines, timeout/sleep/error/success paths, identity/team/source-native
PID/permission and managed-client-pane assertions. This is source preservation,
not a substitute for lead's later creation-VM verification.

Focused owning production-contract command:

```sh
nix develop --command env TMPDIR=/tmp DEV_SESSION_REQUIRE_RUNTIME=0 bash -c 'umask 022
ruby -Itest test/dev_session_test.rb --name "/\Atest_retained_start_contention_diagnostic_(with_shared_holder|with_exclusive_holder|unlocked_retains_identity_without_output|failures_preserve_real_refusal_and_cli_classification)\z/"'
```

Passed 8 runs / 394 assertions / no failures/errors/skips, 5.924070 s:
[F4-ruby-after.log](F4-ruby-after.log). The existing aggregate loads NullTmux before
these cases, which also occur in the inherited CommunicationTest namespace. A
first direct ordinary_readiness_test.rb invocation lacked that fixture constant
and reached zero assertions (4 setup errors); [F4-ruby.log](F4-ruby.log) is retained.
Only the load command was corrected, with the same four-name filter and no Ruby
source change or broad run. These existing SH/EX/unlocked/diagnostic-failure cases
preserve manifest bytes, retained identity, no journals/authority/native effects
and outer-lock release. All disposable holder children joined through their tests.

`nix-instantiate --parse nix/tests/session-creation.nix` exited0, with no build:
[F4-nix-syntax.log](F4-nix-syntax.log). Focused whitespace check passes. Tested
source SHA256 is
`bd679fdf2262e14645b13df9522d7f47192518eade52d1bda88e2111a9b53022`;
captured one-file patch SHA256 is
`47745c5bfa99adbcf602a8845d8e7fbd7c6942f81791e597058049d1d92c7607`.
All checks and the normal Nix Git commit tool are settled exit0. Ordinary hooks
were not bypassed; tree/index are clean and source/index window is released.
P4's exact commit/parent and every unrelated path remain preserved. No native/app
build, VM/CI rerun, push or live session/lifecycle action occurred. Completion,
release and capacity are reported to lead and I0. Lead owns affected combined
review and exact-candidate creation verification. F4 is complete for acceptance;
capacity is available only for an explicitly assigned next package.


## D1: configuration environment and exact runtime pin

D1 source is complete at configuration `85d20879bc15eca9b47cb874bb32c61310e9699d`,
parent `12232ae36f043d6d12b0806231703951dbd08b12`. Only generated `flake.lock`
changed (7 insertions / 7 deletions). The configuration tree/index are clean and
released. The original registered base was `11d6d55924d531d6311dc5a98283d980c9818bb0`.
Fresh fetch found default `12232ae3` had selected installed runtime `f3bd843f`;
lead directed ordinary rebase before any pin mutation. This merged default
lineage is preserved; there is one feature pin update. [Base refresh](D1-base-refresh.log).

The original checkout post-checkout exit78 was a missing ambient locked bundle.
The existing hooks were already installed; no worktree recreation, hook bypass,
hook configuration/source change or Gemfile/lock change was needed. The declared
`nix develop --no-write-lock-file` tools shell installs ignored local `.gems`,
`.bin`, `.bundle` and supplies pinned packaged confctl. With `BUNDLE_FROZEN=true`
and `TMPDIR=/tmp`, Ruby3.4.12, bundle check, Overcommit0.76.0, RuboCop1.75.8 and
Nixfmt1.5.0 pass. Initial setup stopped at unsupported `confctl --version`
(version unknown); supported `--help`, hook inventory, actual git pre-commit hook
and exact channel listing passed in the bounded follow-up. Logs:
[D1-environment.log](D1-environment.log), [D1-environment-ready.log](D1-environment-ready.log).
The fresh Luna/low setup utility joined its command/session67466; no effects remain.

Ran exactly in the declared shell, with standard generated changelog/editor/hooks:

```sh
confctl inputs channel set --commit dev-workspace devWorkspace 75c810a2eb0f8631dd4450e9dc3947bd491f501d
```

The ordinary temporary GIT_EDITOR performed read-only precommit full input-path
graph comparison, exact target dependency-graph/NAR checks, JSON and Nix parse,
`git diff --check`, and unchanged Gemfile.lock assertion. It saved a copy of the
generated editor buffer without modifying its bytes. Committed message content
matches that buffer after ordinary Git comment/whitespace cleanup. Standard pre-commit Nixfmt and
commit-message hooks passed; generated changelog text-width warnings were retained
as prescribed. [Command and hook log](D1-pin.log),
[unaltered generated message](D1-generated-message.txt). The fresh Luna/low pin
utility joined PTYsession59469 exit0, about14seconds. No retries or active effects.

Semantic graph changed only `devWorkspace` and `devWorkspace/codex-web` identities:

- Runtime: `f3bd843f9858b87cef66d0949706f8af16ba9b13` →
  `75c810a2eb0f8631dd4450e9dc3947bd491f501d`,
  `sha256-D6FQJgob+8FPkggZuWIogCILA6k7xf07yQ7X7sgRhpM=`.
- codex-web: `3209aa7bf93e2c7067b07494d1b254741812d714` →
  `db79231a4e5513bf439493efab75378bc7d84c04`,
  `sha256-soMfL5rH6S56o2Uh76UvOwoLG8yflFDmt1GSp8LLu5o=`.

All root siblings, follows edges, Pi/native Codex and policy inputs are unchanged.
The generated configuration lock SHA256 is
`d0c031b4d066b62b23391cf3f90b5172a6370e77f25f969baa8a05a3540c8540`;
Gemfile.lock remains `47c7ad427ae4d97ec6190d3c188193b83aaed407b9d9e1b88b93cc2a1ad5ec6c`.

Postcommit deployment checker passed against workspace
`9f4cec40df39a3f3bfb19de4864ea2128e0f4ccd` using its existing
`bin/check-dev-workspace-deployment --workspace-root WORKSPACE_CHECKOUT --configuration-root CONFIGURATION_CHECKOUT`.
It proves exact runtime/site agreement, not system artifact equivalence:
[D1-postcommit.log](D1-postcommit.log).

Aitherdev key is `m_cz_vpsfree_machines_aitherdev_0b1e0938`. Exported
`confctl.inputsInfo.KEY` before/after metadata is retained in
[before](D1-effective-inputs-before.json) and [after](D1-effective-inputs-after.json).
Those labels are not the effective graph: pinned confctl's metadata lookup uses
raw lock node names. Actual root follows/mapping selects `home-manager_2` and
`llm-agents_2`; the initial labels c47b2cc6/91ff550f do not establish those identities.
No confctl fix was included or allocated. The exact installed configuration source
`109d789f0a4ee875f8bd27a0b72ea76c38ee234a` lock and candidate root graph give:

| Actual root role | Installed configuration source | Candidate configuration |
| --- | --- | --- |
| devWorkspace | f3bd843f9858b87cef66d0949706f8af16ba9b13 | 75c810a2eb0f8631dd4450e9dc3947bd491f501d |
| nixpkgsStable | 94c3211b0ee8ba969a3f12eb4aff8ba0f72971dd | 0dc498bfe49baeb18b0f9891e800b53bb2603193 |
| home-manager → home-manager_2 | e28654b71096e08c019d4861ca26acb646f583d8 | e28654b71096e08c019d4861ca26acb646f583d8 |
| llm-agents → llm-agents_2 | 60037f203e5f2dd1f318318c93e78a9a5e42646a | 5330ee115c06d2b43f49e902130125eab579b22f |

The non-runtime differences already exist in refreshed default1223; D1 preserves
all of them unchanged. Full NAR identities and exact host proof are in
[D1-host-impact.json](D1-host-impact.json), not inferred from revision labels.

Host gate is **settled without a build** using the existing exported exact-machine
`toplevel` derivation and targeted ordinary `nix derivation show` of its existing
etc/system-path/unit/sudo input derivations. Command:

```sh
nix eval --raw --no-write-lock-file --option allow-import-from-derivation false .#confctl.toplevel.m_cz_vpsfree_machines_aitherdev_0b1e0938.drvPath
```

It produced `/nix/store/ky6b3qd7aj2zv3b2xk8vdymm082x7vfn-nixos-system-aitherdev-26.05.20261122.0dc498b.drv`.
No host derivation was built or realized; imported source paths were substituted. This
parent-owned read-only evaluation is joined exit0 (session99261); all subsequent
short derivation reads are complete. Newer `nix derivation show` has a versioned
JSON wrapper (`derivations`, `structuredAttrs`); initial narrow parser assumptions
and an unrealized sudo-input direct read were corrected by reading the existing
leaf derivation's text. No command/build/source retry occurred.
Raw evaluation stderr: [D1-aitherdev-eval.log](D1-aitherdev-eval.log).
Raw targeted derivations: [toplevel](D1-aitherdev-toplevel-drv.json),
[etc/system-path](D1-aitherdev-host-drvs.json),
[selected](D1-aitherdev-selected-drvs.json),
[units](D1-aitherdev-units-drvs.json), [sudo text input](D1-aitherdev-sudo-input-drv.json).

| Host artifact | Installed and candidate result |
| --- | --- |
| Pi helper and session entry package | Exact `/nix/store/xhc71rg58zl44927y9j43s2l23f1r606-workspace-pi-host` |
| workspace-pi-session@ template | Exact `/nix/store/8q48nsnsf05ps2k23n6j4kfl90k8h789-unit-workspace-pi-session-.service/workspace-pi-session@.service`; full text also equal |
| Portal drop-in | Exact `/nix/store/br5i21gaprqanx42ng5c99180d34ng9g-unit-workspace-portal-vpsfree-cz.service/workspace-portal@vpsfree-cz.service`; full text also equal |
| Full sudo policy | Candidate sudoers-in text equals installed `/run/current-system/etc/sudoers` byte-for-byte, including wheel/helper rule order |
| Whole-system Codex | Candidate `/nix/store/9l2h4fpdabglhjkrpy5hr2kgqzf6jzxb-codex-package-0.171.0/bin/codex` differs from installed `/nix/store/naycl3an1c85vhzabscy8qdbr7m1am8c-codex-package-0.170.0/bin/codex`; candidate is not built |

Installed system remains
`/nix/store/k79k3l35lnhfikw65zwnacag112w7z9p-nixos-system-aitherdev-26.05.20261121.94c3211`.
The whole-system candidate is unbuilt
`/nix/store/3q2gc2hyfrp8kq3xiyj4kfvf1jcimarj-nixos-system-aitherdev-26.05.20261122.0dc498b`.
Required Pi host artifacts are identical; the accepted brief's profile-only path
is supported, leaving the installed system/Codex selected. No feature-required
host upgrade is demonstrated. Lead owns that deployment decision and the composed
workspace package build/review/activation. Routine pin/environment work needs no
configuration prose change; all individual evidence stays outside configuration Git.

D1 source/check/host-impact package is complete for acceptance; capacity confirmed.
No source/index changes remain, and no tools/utilities/processes/effects are active
or uncertain. Config index/window is released. No host build, activation, profile
switch, dry activation, reservation/claim, push, merge, reboot, native session
operation or lifecycle action occurred. Session remains open.


## D0 refresh: one final archive-fix pin per repository

Complete for acceptance, both source/index windows released; capacity confirmed.
D1's unpublished75c810 pin heads are superseded by one final3961d728 pin stream
per repository. Fresh SSH fetch confirmed defaults unchanged; neither default nor
shared master was rewritten. Full exact source/range/tree receipt is
[D0-refresh-final-source.json](D0-refresh-final-source.json).

| Repository | Fresh default/base | Previous unpublished head | Final head |
| --- | --- | --- | --- |
| Workspace | cc2c42510f5a596574739e611fff5e91049f07fc | 9f4cec40df39a3f3bfb19de4864ea2128e0f4ccd | dbb6c4bcc711ab3718646e266a4a6379003b42df |
| Configuration | 12232ae36f043d6d12b0806231703951dbd08b12 | 85d20879bc15eca9b47cb874bb32c61310e9699d | 844ffe5ed7b3bd541872a57112d7cabff81ab778 |

Workspace changed only its existing nested runtime URL and generated lock via
`nix flake update vpsfree-dev-workspace/dev-workspace`, then normal
`git commit --amend -F` in its declared Nix environment. Final base-to-head scope
is two files9+/9-. Configuration used ordinary empty-range
`git rebase --onto origin/master 85d20879bc15eca9b47cb874bb32c61310e9699d`
to reconstruct the unpublished one-commit stream at its existing default base,
then ordinary declared-shell
`confctl inputs channel set --commit dev-workspace devWorkspace 3961d7285abc6c996206bc50a7cd68977086312b`.
Final scope is generated flake.lock7+/7-. Confctl regenerated the full unchanged
format/changelog from merged basef3bd843f to3961d728; no hand-edited lock/message,
hook bypass or source/helper change. Ordinary pre-commit Nixfmt and commit-message
hooks passed with the expected generated-text-width warnings. Copied editor buffer
and committed message match after ordinary Git comment/whitespace cleanup.

Both branches have exactly one commit above their fetched default, and neither
old75c810 feature-pin commit is an ancestor of its final branch. No obsolete
intermediate pin remains in the final series. Old/new range-diffs:
[workspace](D0-refresh-workspace-range-diff.log),
[configuration](D0-refresh-configuration-range-diff.log).
They show only the expected runtime identity/original URL/hash/timestamp delta
and updated final commit messages. Final workspace tree is
`6c73d2526b9a64db526340fb14fea6fab71d5b49`; configuration tree is
`5aab123f2fdb8724bf85f6196e38590e16d36ecc`.

New runtime identity is `3961d7285abc6c996206bc50a7cd68977086312b`,
`sha256-NA5oB8Dyh+VLA7dYjOWLrN2RzVrkDIojwwuM0u6OmtM=`. Provider stays exact
db79231a4e5513bf439493efab75378bc7d84c04 and its existing NAR. Semantic comparison
of all direct input paths plus all follows edges (38 workspace /67 configuration)
proves old75c810→new3961 changes only the runtime identity; each final default→head
stream also contains only the expected existing codex-web3209→db792 identity change.
The extensionbf12ac71 identity/NAR, native/Pi dependencies, site/model/provider/team
policy and all sibling/follows edges are unchanged. Precommit config editor also
compares the entire selected runtime dependency graph with its exact committed lock.

Quick checks passed in declared environments: workspace Nix parse plus existing
Ruby deployment contract4runs/19assertions, no failures/errors/skips,1.398907s;
whitespace checks; config JSON/graph/Nix parse and actual standard hooks; final
existing cross-lock/site checker confirms3961d728. Both trees/indices are clean.
Logs: [workspace update](D0-refresh-workspace-update.log),
[workspace graph](D0-refresh-workspace-graph.log),
[workspace quick/commit](D0-refresh-workspace-quick-commit.log),
[config reconstruction](D0-refresh-configuration-base.log),
[config pin/hooks/precommit graph](D0-refresh-configuration-pin.log),
[generated editor message](D0-refresh-generated-message.txt),
[final cross-lock/site proof](D0-refresh-crosslock.log).

Runtime3961 is exactly one commit above75c810 and changes only Go/docs/tests.
[Exact host-source/input proof](D0-refresh-host-source-proof.log) confirms no host
module/package/helper/session-entry/wrapper/native source or flake/lock change.
D1's concrete installed helper/template/drop-in/sudo comparison is therefore reused
for its exact unchanged host source/input scope; no new system diagnosis or build
was run. The existing profile-only preparation conclusion and preserved installed
system/Codex remain supported. Application lifecycle-fix behavior belongs to lead's
parallel affected runtime review, not a claim made by these mechanical pin checks.

Final SHA256: workspace flake.nix
`05eda9d143b2cbeca2f6ff5e6d8f2e461d60680b930e84be52fa22123cd88505`, workspace lock
`9b4b77529acc1f55031ac7fee4673a3ed3e691d3886545aa6f5392fddfdd0784`, config lock
`b259fca72d93453306d8c14ab1fa81603e346498cd762fb48b8fc15ce986d966`.
All checks and ordinary commit/rebase commands joined; no active or uncertain
effects. No long build, app/native campaign, profile/system activation, claim,
merge, push, service/archive/lifecycle action occurred. Lead owns review/build and
separately authorized deployment execution. Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-23-pi-message-delivery/


## M1: configuration integration target preparation

M1 complete for acceptance; capacity confirmed. No merge, push, repository claim,
resource release, profile/system activation or session/service/lifecycle action
was performed. Lead owns the approved integration critical section and subsequent
machine release verification.

Prepared fresh detached target:
`worktrees/2026-11-23-pi-message-delivery/configuration-integration-target`, HEAD
`12232ae36f043d6d12b0806231703951dbd08b12`, clean tree/index. Feature remains
`844ffe5ed7b3bd541872a57112d7cabff81ab778`, clean, directly above1223. Exact SSH
remote `git@github.com:vpsfreecz/vpsfree-cz-configuration.git` master equals1223
before creation and at final read-only verification. No default branch checkout
or source/lock/rebase change. [Exact receipt](M1-final-preparation.json).

Ordinary `git worktree add --detach TARGET 12232ae3...` ran inside the existing
configuration's declared frozen-bundle Nix environment, so its post-checkout hook
loaded successfully on the first attempt. Copied only the owning feature's ignored
`.gems` into the target; target's own declared shell created local ignored
`.bin/.bundle` with matching target paths. No dependency/lock/hook-config edits,
hook bypass, trust weakening or unrelated checkout mutation.

Target bundle check, Ruby3.4.12, Overcommit0.76.0, RuboCop1.75.8, Nixfmt1.5.0 and
supported confctl help pass. Canonical common hooks are active and executable;
post-checkout/pre-commit/post-merge/commit-msg SHA256 is
`247d2a1d4fc3d57c2bfc906697f298f703a57d44491db6d2a2b16315e322be12`.
`overcommit.configuration.verifysignatures=1` remains enabled. Actual target
pre-commit trust/framework load and post-merge hook run pass with empty index;
this does not claim new full lint coverage. The accepted feature's actual Nixfmt
commit proof is retained; target/feature `.overcommit.yml`, `.git-hooks/`, Gemfile,
Gemfile.lock and flake.nix are identical, so no signing or new hook change is needed.
[Full setup](M1-target-setup.log), [hook inventory](M1-target-hooks.log).

Whole final series/diff remains the accepted D0 mechanical result: one generated
flake.lock7+/7- pinf3bd→3961 and expected transitivedb792; no superseded unmerged
pin, migration, source or input-graph delta. Accepted review's history/migration
conclusion applies to these unchanged exact heads. No extra test/build was run.

Lead's normal commands after repository claim and fresh target/feature/clean/remote
checks are `git merge --ff-only 844ffe5ed7b3bd541872a57112d7cabff81ab778`, then normal
`git push origin HEAD:refs/heads/master` and exact fresh remote proof, from the
prepared target under `BUNDLE_FROZEN=true TMPDIR=/tmp nix develop --no-write-lock-file`.
Inspect hook results even when merge exits0; retain detached target. Feature
comparison command was supplied for lead if needed:
`dev-session worktree capture-comparison 2026-11-23-pi-message-delivery vpsfree-cz-configuration --as-is`.
It was not run by M1. All setup/final command sessions (66689/70234) joined exit0;
no active or uncertain effects. Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-23-pi-message-delivery/


## P8-F: preserve the final audit failure boundary

Complete for acceptance at `ca7637c920b9f9bb71a3c639010c2505d47da3b0`, parent
`3961d7285abc6c996206bc50a7cd68977086312b`; capacity confirmed. Exactly the existing
tagged integration/fixture files and narrow supervisor_test.go helper changed,
176 insertions/24 deletions. The architect explicitly accepted the third file
and a single unexported Load-function dependency for deterministic native-free
coverage. Lead retains combined acceptance/review and any later candidate/200 run.

The final audit writes synced JSONL begin/end rows for Idle, History,
receipt_directory and memory, with the exact member/full execution handle where
applicable. On failure, Idle preserves the state returned by THAT Load, its
iteration and errors.Is/context class, Go error type, first512bytes of original
error detail and explicit truncation flag, before the same original Fatal.
The original aggregate remains partial/not_completed; failed stages never emit
an end row. The error classification does not identify a native leaf cause.
No arbitrary message/history/credential content is copied.

One shared waitIdleResult owns the original Load/context/1ms wait loop. Existing
waitIdle remains its fatal wrapper; the tagged fixture forwards to the same loop.
No extra RPC, observation, poll/retry/drain, timer, production hook or live action.
Final receipt/native history/at-most-once/health audits, question workload,
foreground timing/fairness limits and failure status are unchanged.

The existing CompletionEvidence child-process test now covers six cases: original
incomplete/late-hold refusal; a fatal History stage with begin/no end; same-helper
Held and canceled Load results preserving exact state/handle/iteration/original
error/type/context with exactly one loader call; successful Idle emits its end
before a later deliberate child Fatal. This proves evidence survives an actual
Fatal; the shaped test loader does not recreate or attribute the old native cause.

Final exact checks in the owning Nix shell, with TMPDIR=/tmp:

```sh
GOWORK=off DEV_SESSION_REQUIRE_RUNTIME=0 go -C portal test -mod=readonly -tags=pi_native_fixture ./internal/piruntime -run '^TestPiMessageDeliveryCompletionEvidence$' -count=1 -timeout=30s
GOWORK=off DEV_SESSION_REQUIRE_RUNTIME=0 go -C portal test -mod=readonly -tags=pi_native_fixture ./internal/piruntime -run '^$' -count=1 -timeout=30s
```

Passed0.442s (six native-free child cases) and0.063s (tagged compile, no tests).
Gofmt and diffcheck pass. [Final source/check/commit raw log](P8-F-final-commit.log).
Earlier quick-green evidence before the narrow original-error clarification is
retained in P8-F-quick.log/P8-F-final-quick.log; no broad/native run occurred.
Normal `git commit -F` staged only the three owned paths, without hook bypass;
the repository declares no hook framework. No schema/migration/pin/API or production
behavior changed, and no merged history was rewritten.

Commit tool8574 joined exit0; all checks/effects settled. The index was empty and
own Go files clean at release. I0's two unstaged JS files were SHA256-verified
unchanged across the commit. Explicit source/index release to I0 was delivered
with message d93498a9-f1a8-4e9e-b27a-e4506dec1710; no further source/index mutation
belongs to P8-F. Lead completion receipt c152e344-3c71-4204-939a-b41c5c2b9ee6.
No build/profile/deployment/merge/claim/native/session lifecycle action occurred.
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-23-pi-message-delivery/


## D2-P: optimized runtime pins and integration targets

Complete/released/capacity confirmed. Workspace `68c12c44e6d5e1d0282c04b093c078ed9942996f`
(parent fresh merged default `dbb6c4bcc711ab3718646e266a4a6379003b42df`, tree
`bb3e177e330abbfd5e1d73f9faea02a269a156c8`) changes only existing nested URL and generated
lock5+/5-. Configuration `b0433dedbee3a1cbce4f75523de0237f1fd870c6` (parent fresh merged
default `844ffe5ed7b3bd541872a57112d7cabff81ab778`, tree
`0d13c752a93b5db0abaa0476ad3361e413aea0a5`) is ordinary generated lock3+/3-.
Both clean; one new pin stream per repository, earlier3961 pins already merged,
no default rewrite, intermediate unmerged pin or migration.

Both select `b07fec04174ef5303356fea54a326bce578d30e6`, NAR
`sha256-CUJne9MagJK773fpnM/zFskAPXe1j4cn3ivo350u5MA=`. Semantic38/67direct paths and
all follows edges show runtime identity only changed; extensionbf12, db792 provider,
upstreamSDK a22, native/site/team/model/claim inputs are unchanged. Fresh fetch and
ordinary declared-shell rebase were no-ops. Workspace uses nestedURL+nixflakeupdate;
configuration uses exact `confctl inputs channel set --commit dev-workspace devWorkspace b07fec04174ef5303356fea54a326bce578d30e6`, unedited generated3961→b07 message/changelog.
Precommit semantic/JSON/Nixparse and real Nixfmt/hooks pass (generated width warning
retained); workspace parse+existing Ruby contract4/19 pass1.342726s, final cross-lock
site check passesb07. No full app/SDK/system build; declared shell realized only the
patched SDK source derivation. [Full exact source/target receipt](D2-P-final-source.json).
Logs: D2-P-workspace-{base,update,graph,quick-commit,target}.log,
D2-P-config-base.log, D2-P-configuration-pin.log, D2-P-config-crosslock-target.log;
D2-P-generated-message.txt retains editor buffer (ordinary Git comment cleanup).

Fresh detached clean targets under own session group are
`workspace-integration-target-d2` @dbb6c4bcc and `configuration-integration-target-d2`
@844ffe5e. Workspace omits work/archive with ordinary per-worktree sparse checkout;
config was created inside declared Nix/frozen bundle/TMPDIR=/tmp shell, first
post-checkout hook passed. Its own ignored local gems/tool paths are ready, bundle
check/Overcommit/RuboCop/Nixfmt/confctl help and precommit/postmerge trust load pass,
signature verification remains1. Final fresh SSH defaults equal exact parents.

[D2-P-host-source-proof.log](D2-P-host-source-proof.log) confirms unchanged relevant
host module/paths/helper/package/session-entry/Codex-wrapper source and locks.
Intentional SDK source patch is confined to mkPiWorker; upstream input unchanged.
Architect accepted reuse of exact D1 installed host-artifact proof; profile-only
path retained, no host system upgrade or repeated system evaluation/build.
All command sessions joined, no active/uncertain effects. No actual merge, push,
claim, profile/system activation, native/service/session lifecycle action occurred.
Lead owns review/build/approved integration/deployment. Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-23-pi-message-delivery/


### D2 canonical-SDK pin refresh

Final/released: workspace `f618f0e698e66825fe1ab9d4f4d5948e71de6aa1` above
`dbb6c4bcc711ab3718646e266a4a6379003b42df`, tree
`cab0f328e7c0340f0ac3141c3b3185e6fec05beb`; configuration
`d8225a89541e12835ac47f179f4b13f7de00ee60` above fresh default
`4694ca977a6816687e932b2b921a3e103f059224`, tree
`4521039b8a9d4335fa26a79317b9f5c9291c7aae`. These replace only unmerged68c/b043
pins with one final commit per stream; neither obsolete head is an ancestor.
Workspace normalamend2flakes5+/5-; config ordinary empty-range rebase then generated
confctl commit3+/3-, full3961→e61 changelog unchanged. No merged/default history rewrite.
Both select published runtime `e61d3b7e59f07f89df50d23e23d7800d4b13cabf`, NAR
`sha256-EhJ65DcpmTpl+ftuyf7EI0D4z8nrJGS4hni7tzMyKrc=`. Graph38/67directpaths plus
all follows proves runtime-only identity delta, preserving extension/provider/Pi
upstream/native/site/team/claim inputs. [Exact final receipt](D2-refresh-final-source.json)
and D2-refresh-{workspace,configuration}-range-diff.log retain old/new provenance.

Declared workspace Nix parse and existing Rubycontract4/19 pass1.302158s; config
precommit graph/targetdepgraph/JSON/Nixparse/diffcheck and real Nixfmt/commit hooks
pass, generated width warning retained. Final cross-lock/site checker passes e61.
Logs: D2-refresh-workspace-{update,graph,quick-commit}.log, D2-refresh-config-base.log,
D2-refresh-configuration-pin.log, D2-refresh-generated-message.txt,
D2-refresh-crosslock.log. All effects/commands joined; no app/SDK/system/native build.
Config integrationtarget-d2-sdk is clean detached4694 with declared local ignored
gems/tooling, signatures1 and actual precommit/postmerge trust passed; workspace
integrationtarget-d2 remains clean detacheddbb6/sparse. Final SSH defaults equal
parents. Source/index windows released, capacity confirmed.

Fresh4694 retains unrelated three OS-role locks/node OOM changes; architect's exact
Aitherdev-import reconciliation confirms no relevant host-input delta. Relevant
host module/helpers/entry/Codex wrapper/locks also remain unchanged3961→e61:
D2-refresh-host-source-proof.log. D1 installed host proof/profile-only route reused
within this scope; no whole-system eval/build. No migrations/defaultpush/merge/
claim/activation/lifecycle action. Lead owns final review/composed batch/integration/
authorized deployment. Completion report d94b4ef0-e775-4ca2-abf8-5a76a42f7dcf.


D2 final feature publication: ordinary non-force SSH pushes to
`refs/heads/2026-11-23-pi-message-delivery` completed for workspacef618f0e6 and
configurationd8225a89. Fresh independent ls-remote equality verified both exact
heads; defaults remain dbb6/4694, both feature checkouts clean. Logs:
D2-refresh-workspace-publication.log and D2-refresh-config-publication.log.
Exact-branch GitHub Actions API reads before/after publication return no runs
in either repository; no superseded active run to cancel, no CI wait/rerun.
All push/remote/check sessions joined exit0, no uncertain effects/default push,
claim/merge/activation or source/index mutation. Lead report9485a89d-2be7-4a38-bcd5-a968208f10ad.


### D5-M compact delivery receipts

Provider normal commit `b67d86a889cf3ac88d78f03d2dcd5f061f95d0b2` directly above
`db79231a4e5513bf439493efab75378bc7d84c04` (tree
`2f6379368e02dd4f4174afd49fabd0c8db38d71a`), 8 files, 163+/39-;
ordinary SSH feature publication joined and fresh remote equality verified.
Runtime normal commit `96b00bd09ef0d07ec784b22a67492c0a40ff201e` directly above
I0 D4 `ecdf23555a9226dcac85aaf880dc56e7a75b798e` (tree
`9b34255df246a04f0e40263ac50e2a0b3cc061d3`), 8 files, 27+/17-;
publication held for D6/review. Both were clean at explicit source/index release;
I0 acknowledged and owns the next D6 window. All own tools/checks joined.

The shared keyed renderer keeps literal messages beside small status labels,
preserves action focus, announces status changes, and presents validated POST
responses before the authoritative collection refresh. A view-local generation
and one dirty follow-up prevent an older GET removing or regressing that response.
Failed fresh reads retain the evidenced row. Both consumers leave global errors
alone. Existing six wire states, IDs, actions, browser storage and worker/native
semantics remain unchanged; Accepted means input confirmation, not response
completion. The provider reference contains the lead-approved API explanation.
No migrations, compatibility scaffolding, obsolete intermediate pins or history
rewrite. Full runtime branch series remains e61 -> ecdf (D4) -> 96b (D5).

Provider syntax plus existing delivery/conversation Node contracts passed 8/8
in 1.75s, including mounted race/focus/changed announcements, wrong scope,
destroy, failed refresh, original admission recovery, and consumer newer-error/
draft preservation. The example import version check passed 0.021s using pinned
Go + stdenv.cc; the first Go-only shell lacked gcc and was corrected once.
Runtime syntax/composer contracts, existing positive/negative pin contracts,
Nix parses and diff checks passed. Neither repository declares a hook framework
or has active non-sample hooks; ordinary git commits ran without bypass.
Raw logs under `/tmp/pi-message-delivery-D5-`: provider-quick.log,
example-quick.log, runtime-quick.log, provider/runtime-commit.log,
provider-push.log, runtime-pin.log and vendor.log.

Only the codex-web lock node changed: NAR
`sha256-QezhmlDrsAPt860BSR5tj8HwLSvKn8Ji1gBVkL3OQpU=`, matching Go version
`v0.0.0-20261124175117-b67d86a889cf`. All other input nodes/follows unchanged.
Ordinary `go -C portal mod vendor -o /tmp/pi-message-delivery-D5-vendor/vendor`
then `nix hash path` produced recursive vendor hash
`sha256-TceRTXhJn/eEp3si1Fpx1u+lm6fPdRpyMLf+IfXIVgo=`; only the existing
vendorHash literal changed. No application/SDK/native build was run.

Synthetic actual-CSS Chromium geometry passed both shared and portal themes at
1000px/360px: short receipt 29.78px, desktop message/status on one row, complete
literal long text wrapped without horizontal overflow; all six states/actions
and failed refresh retained rows. Script `/tmp/pi-message-delivery-D5-geometry.cjs`,
raw `...-geometry.log`, screenshots `...-{shared,portal}-{1000,360}.png`.
Narrow portal screenshot visually inspected; lead also inspected both portal
sizes. This uses page.setContent/source assets and synthetic client data, not a
hydrated/live portal or native-progress proof; no server/service was launched.
No peer content, live storage/action, native effect, deployment, claim or merge.
Lead owns combined D5/D6 review and any longer verification/publication.


### D5 actual durable consumer coverage and D6 history refresh

Final runtime base `e61d3b7e59f07f89df50d23e23d7800d4b13cabf`; complete
three-purpose series is unchanged published D4
`ecdf23555a9226dcac85aaf880dc56e7a75b798e`, refreshed D5
`5f42669cfa73fab70e409b28a2b22bc0a7c761ad`, then D6
`9b2b96ab31193294448e3f8737db55143060f7b3` (final tree
`0eabbc54bcfd81d162635cca49767ba3ddc9119d`). Only unpublished D5/D6
were rewritten, using a normal Nix-shell commit and autosquash/replay; no
conflicts, hook bypass, merged-history rewrite, default-ref mutation or push.
Old D5 `96b00bd09ef0d07ec784b22a67492c0a40ff201e` and D6
`c5f3fd85b9325b591ec8d4b6dee2bf01ecbd72f3` remain in feature backup refs
ending `pre-consumer-correction-d5` and `pre-consumer-correction-d6`.
No migrations or additional dependency-update stream.

The Important consumer fixture finding is corrected only in the existing
`message_delivery_browser_test.cjs`: the actual shared renderer uses
Unconfirmed. Valid saved status/receipt objects now prove the exact original
row advances Queued to Accepted without replacing its mounted node, clears the
global Queued notice, and remains Accepted beside a different queued row that
becomes Unconfirmed. Exact-ID locators keep multiple rows unambiguous. Existing
selection refusal, draft retention, lost admission reply and same-ID recovery
assertions remain. Actual selected provider shape checks accepted queued/sent/
unknown objects and rejected a foreign-ID receipt and an unknown object carrying
a receipt; fixture syntax and diff checks passed before freezing.

The sole lead utility CLI8760 completed both actual related existing browser
modes: durable composer Chromium/Firefox PASS (Go subtest 15.87s), independent
Pi activity Chromium/Firefox PASS (19.04s). Exact existing TestQuestionBrowser
message_delivery subtest runs used PI_MESSAGE_ONLY=1; durable explicitly unset
PI_ACTIVITY_ONLY, and activity explicitly unset PI_DURABLE_ONLY. Both modes
exited 0; self-captured command/pre-hash/post-hash/final all 0, 59 seconds.
Raw `/tmp/pi-d5-consumer-correction/run.log` SHA256
`b68d6ae3aeb859259053e31dabd7aca70dbcf84a8d32ab692c2ea52ab79216cd`.
Prepared literal script SHA256
`0f75ae3b5eaa10e8739aa597ca7272b78fc39422c65a1fb059e7c9b469ddfe37`;
modes script `a2448cb170015fa1abc21f7c785fd81f37077e7f8f237bdc5afdd6cd8ede5226`.
Final fixture SHA256
`d2c150d591a19d2ddc2a928f34fb7547c8f91638815ab7bc0d34c504bed3f00e`
matches the green frozen input. No Codex repeat: product and team fixture bytes
remain identical to its retained final green receipt. Prior failures remain.

Full old/new three-commit range-diff in the same temporary root marks D4 and
D6 equal; D5 only adds the intended fixture correction (23+/3-). Recursive
mode/type/object/path tree comparison proves all 1140 nonfixture entries
identical to old c5, including every product, provider pin, lock and doc byte.
Raw `range-diff.txt`, `final-series.txt` and `history-receipt.json` retain the
comparison; range-diff SHA256
`e149d14808f8a8a43b45ba89b83c708a12a103cf9a07c1a214865610ff272e46`.
Source/index clean and released; every command/client/test joined. Runtime
publication is held for combined final review; I1 received the new SHA and
continues to wait for its publication before dependent pins. No live peer,
native, lifecycle, build or deployment effects. No product-doc change is useful
for this test-only correction. Lead owns review acceptance and next allocation.


Final publication followed lead's accepted completed review and direct Important
remediation inspection. Normal nonforce SSH push to
`git@github.com:aither64/dev-workspace.git` fast-forwarded only
`refs/heads/2026-11-23-pi-message-delivery` from ecdf to exact final 9b. Fresh
remote feature equality confirmed
`9b2b96ab31193294448e3f8737db55143060f7b3`; remote HEAD/master stayed
`e61d3b7e59f07f89df50d23e23d7800d4b13cabf` before and after. Ordinary final
capture-comparison succeeded once for that exact e61→9b range. Source/index
remained clean; every Git, messaging and GitHub client joined. I1 received the
exact publication/NAR-resolution prerequisite. Branch run inspection found only
current-head CI `45462741613` active, so no superseded cancellation was needed;
completed ecdf success `45450318337` was retained. No CI retrigger, watcher or
wait, and no default push, merge, claim, build or deployment. Package complete
for acceptance; capacity available. Lead owns CI and subsequent delivery.


### D7-P matching feature deployment pins

Complete/released: workspace `6687dc442c94ebebb54dc0a7f010a807ba9b7926`, parent
`f618f0e698e66825fe1ab9d4f4d5948e71de6aa1`, tree
`5523557f1c03cfd17b3018c27b0b534994d98081`, two flakes 9+/9-; configuration
`bebb4abef50ba4f69860e95833a9b68f73613731`, parent fresh default
`ce54d0c9175d10a8f9223446c498f8f3ffb08e70`, tree
`3d4704839375d6043fd9539d923012b19bd763c5`, generated lock only 7+/7-.
Both ordinary SSH feature pushes and fresh remote equality joined successfully;
defaults unchanged. One new pin per stream, protected merged f618/d822 retained;
config ordinary rebase advanced to ce54 preserving its unrelated geminabox files.
No history rewrite, obsolete intermediate pin or migration. Both trees/indices
clean at release; no active effects. Runtime dependency was published/reviewed
`9b2b96ab31193294448e3f8737db55143060f7b3`, not earlier interim D5/D6 heads.

Both locks select runtime NAR `sha256-KcQBDXdtLM9gU18S/JHwM6J/0NNjTRjlYaWtTbbbTpw=`
and provider b67 NAR `sha256-QezhmlDrsAPt860BSR5tj8HwLSvKn8Ji1gBVkL3OQpU=`.
Complete direct-path graphs (38 workspace/67 configuration) prove exactly those
two expected identities changed; every sibling, native/SDK/Node/catalog/policy/
team/claim input and follows edge preserved. Cross-lock/site checker and complete
runtime locked-identity equality pass. Existing workspace Ruby deployment test
passes 4 runs/19 assertions in 1.416909s; Nix/JSON parses and diff checks pass.
Configuration normal frozen-bundle confctl set --commit ran Nixfmt and message
hooks successfully; generated width warnings retained. It committed directly
without invoking the proposed GIT_EDITOR guard, so exact final graph/parse
verification ran immediately afterward. Generated message remains intact:
inputs: set devWorkspace to 9b2b96ab, e61->9b with the three runtime commits.
Workspace has no declared active hook framework. Scoped feature CI lists are
empty for both repositories; no cancellation or wait. Raw commands/results:
`/tmp/pi-message-delivery-D7-{workspace,config}-{baseline,pin,quick,commit,push}.log`
(where applicable), `...-crosslock.log`, `...-host-boundary.log`, and
`...-config-generated-message.txt`; graph guard and input snapshots also in /tmp.

Fresh ce54 has unchanged full input graph and Aitherdev module/config/site bytes
versus D2 d822; only unrelated geminabox package files advanced. Final runtime
seven host/helper/Codex-wrapper files are byte-identical e61->9b; flake wiring
changes only provider URL and root lock only codex-web. D1 host-proof anchor hash
2af3ddc5149f6ace966a34eede6b975edce494f66eae72ba3e98fc427ee0ce68 verified.
Reuse accepted D1/D2 helper/template/sudo/drop-in boundary; preserve installed
native Codex, do not assert excluded system-candidate equality. No whole-system
eval/build, application/SDK/native build, claim, activation, default integration,
peer action or lifecycle operation. Lead owns mechanical review/composed batch
and separately authorized feature profile deployment. Session stays open.


### D8 final-CI asset and extracted-callback remediation

Accepted direct narrow remediation of CI `45462741613`, failed fast job
`138689458545`: unchanged raw `/tmp/pi-d7-ci-fast-job.log` SHA256
`a58a5781c9fb145a008278701b861b45d9b6967d83d3fd734a6f28f2884a1a15`,
sanitized `...-plain.log` SHA256
`20c89f74d19bdbea4231ef6f069b8da0b617c3372430b05cd221bdfb3b7ccc15`.
New normal commit `b0b246f60d79300b2981e764677d597501a54df9`, exact parent
published `9b2b96ab31193294448e3f8737db55143060f7b3`, tree
`997c4fb33f1ddd913692b8abdf8294860092137d`. Four files 7+/4- only:
index and automatic-archival now select the same app v84 as session; the two
extracted successful-apply callback fixtures explicitly supply the display
collaborator and transcript-failure state. Test assertions and production
JavaScript remain unchanged. App SHA256
`8a76bc703a2ae6bcf9292911e137622f83fae72ce158e50a10f39f6cbb297c02`.
All template entrypoint imports and extracted callback/render dependencies were
audited: the activity lane already supplies its updater, submission-notice
extraction ends before renderThread, and only the two corrected callback mounts
were missing the dependency. No guard weakening or cache-policy change.

Declared-Nix syntax checks for both fixtures and app passed; existing independent
read-cycle/mounted 27 cases passed (0.443s). Actual Go tests, with -mod=readonly,
-count=1 and -timeout=1m: TestBrowserAssetVersionsForRetryAndQuestionUI PASS0.03s,
TestComposerHandoffRetainsOriginalIntent PASS0.73s,
TestShippedBrowserClientMatchesSessionAPI PASS1.30s; package2.120s. Full literal
command was reported to lead; complete stdout/stderr retained in
`/tmp/pi-d8-focused-quick.log`, SHA256
`c8724b3465cba34dd39f2562a969d9895078fac5b0976dfedbad625c843a47e6`.
Committed diff `/tmp/pi-d8-committed.diff`. Normal hooks/no bypass, source/index
clean/released, no new browser/native/build campaign. Lead inspected the exact
committed diff and quick log under mandatory-review step9 and accepted it; no
new design, public contract or authority. No product documentation change needed.
Complete branch retains D4 ecdf → D5 5f426 → D6 9b → D8 b0 above e61. No
migrations, merged/published-history rewrite or superseded pin stream added.

Authorized ordinary nonforce canonical SSH feature push9b→b0 joined exit0.
Fresh direct feature equality b0 and unchanged remote HEAD/master e61 proven
before/after; exact e61→b0 comparison captured once. I1 received the exact final
published SHA for matching pin/NAR resolution. Current-head Check `45466397506`
was queued, untouched. Superseded9b Check `45462741613` was still in progress;
only its cancellation was submitted and accepted. One bounded subsequent read
still showed creation in_progress, fast completed/failure, archive completed/
success, host skipped. Cancellation terminal state is not claimed; lead owns
that remaining CI operation. No CI retry, current-run cancellation, watcher or
wait. Every own local/Git/GitHub/messaging client joined; no own executing effects.
Capacity available; lead owns final pins/build/CI/deployment.


### D8-P final CI-fixture runtime pin refresh

Final workspace `bba97150423c0e144b9bcfffe751e86deef37a33`, protected parent
`f618f0e698e66825fe1ab9d4f4d5948e71de6aa1`, tree
`27c1f9272820a7fd4720c57a496baca1252af3ad` (two flakes 9+/9- from parent).
Final configuration `fd72518d6073b2be523800e07c1eb5ddec5df91f`, protected fresh
parent `ce54d0c9175d10a8f9223446c498f8f3ffb08e70`, tree
`162d9aa0b383c031311def8f92b4c22a96f4ab5c` (generated lock 7+/7-).
One final new logical pin per stream: normal workspace amend replaced 6687;
ordinary empty-range rebase plus confctl regeneration replaced bebb. Old heads
are retained in local backup refs ending D7-workspace-6687/D7-config-bebb and
are not final-branch ancestors. Protected defaults/merged history unchanged;
no migrations. Old/new range-diff logs retain exact consolidation provenance.

Both pins select published `b0b246f60d79300b2981e764677d597501a54df9`, NAR
`sha256-Om83sEFPXnNsMm3ZDBKaVjp9peakaZ/KvcXOhgc/FII=`. Compared with accepted
D7 final trees, only runtime identity/lastModified/NAR and nested URL change:
workspace 5+/5-, configuration 3+/3-. Graphs 38/67 paths plus all follows retain
provider b67/Qezh and every other selected dependency. Final runtime flake/lock,
host/helper/session-entry/Codex-wrapper files are identical 9b->b0, so D7 host
boundary proof reuses without system evaluation/build. Existing cross-lock/site
checker and complete runtime/provider locked-identity equality pass.

Declared workspace parse/Ruby contract passes 4/19 in 1.401154s. Configuration
ordinary exact confctl set --commit runs normal Nixfmt/message hooks; generated
e61->b0 changelog retains all four runtime commits and width warnings. JSON/Nix
parses, full graph comparison and diff checks pass. No manual lock/message edits
or hook bypass. Both canonical SSH feature rewrites used explicit expected-old
leases, joined successfully and fresh ls-remote equals final heads; remote defaults
remain f618/ce54. Final trees/indices clean; all command effects joined and source/
index windows released. Scoped own-branch CI reads return [] for both; no cancel,
watcher, retry or wait. No runtime/provider source edit, build/evaluation campaign,
native/live action, default merge, claim or activation.

Raw `/tmp/pi-message-delivery-D8-` logs: workspace baseline/pin/quick/commit/
range-diff/push, config pin/quick/range-diff/push/generated-message.txt,
crosslock.log, source-equivalence.log, runtime-published.log and CI JSON.
Lead owns direct mechanical comparison, composed default plus five checks,
final CI and authorized profile deployment. Prior 9b/6687/bebb/qgkimh artifacts
remain old candidate provenance; no deployment occurred from those heads.


### D9-E required creation smoke and explicit extended campaign

User-authorized reduction replaces the parked timing-only package. The partial
browser timing prototype remains saved as `/tmp/pi-d9-timing-prototype.patch`
SHA256 `c2b64679045ac7730604501c7653ffe15045b575897852354cb32b8f50feb36f`;
only its owned helper changes were restored. Browser helper and existing helper
tests are unchanged from b0; no timing/parser was retained.

New normal commit `2392f0bf3246ef3421630afb7e72dbb17192940d`, exact published
and deployed parent `b0b246f60d79300b2981e764677d597501a54df9`, tree
`1e598a37d641a4f3af5e7968e046cfc62fd1d5b0`. Four owned paths only, 426+/403-
including mechanical indentation; ignoring whitespace, 47+/24-. One shared
fixture now takes extended?false. Required checks.session-creation remains the
actual Codex/Pi essential gate; explicit packages.session-creation-extended uses
true and is absent from checks and dynamic fast selection. Distinct VM names.
Workflow job/step says Session creation smoke; its build command is unchanged.

Smoke runs exact public Codex explicit-primary Solo create plus existing proof,
and Pi strict TLS/public pi-create plus existing pi_proof/instruction checks.
Original IDs, exact native/stored acceptance witnesses, count-one original input,
settings/namespace/CA, visible response, follow-up and reload remain authentic.
Attachments, managed ascending input, naming/providers/teams/forks/plans/settings,
transport/delete/maintenance, Pi CLI/cold reconnect and both repeated finish
calls remain extended-only in their old order. A final assertion requires both
completed backend cases. The maintenance target is excluded from smoke's VM
additionalPaths AND generated script store context, not just skipped at runtime.
No production guard, protocol, deadline, receipt, polling or recovery change.

Quick checks passed: both Nix parses; both actual evaluated Python scripts compile;
selector/AST/context checks; unchanged browser-helper syntax and 29 tests (0.278s);
Ruby workflow YAML parse; diff check. Selecting true reconstructs the previous b0
scenario operation/assertion AST exactly after removing only new summary bookkeeping
and normalizing two scope labels. Selecting false has exactly two browser calls,
one proof per backend and no maintenance/finish/reconnect call. One final-source
Nix evaluation binds both generated scripts, check enumeration, paths and string
contexts. Earlier exploratory checks incorrectly treated a drop-in filename as a
store dependency and mixed receipts across the lead README rewrite; corrected
proof uses precise store paths from one evaluation, with no source/assertion
weakening. No VM, browser, build or CI execution was launched.

Raw helper log `/tmp/pi-d9-helper-quick.log` SHA256
`9bf3bdd2a4e29d8aeb5a3334f9522fcc07973bf7238e796d7fb37e02b4ac207b`;
final evaluation `/tmp/pi-d9-eval.json` SHA256
`20da447f026f6519cca00a393b3a9fe8f8bd053749743108630b94f96a6481ed`;
selector proof log `/tmp/pi-d9-selector-quick.log` SHA256
`47c1129242873140bafc6301d0808d9656095f679bdced21669989c95d488da9`.
Literal focused source proof: `python3 /tmp/pi-d9-selector-proof.py` (script SHA256
`ecfada7c8e10d7962432e8fc77fe7591745ea0f58581f495d89c15c2a9690b90`).
Full diff `/tmp/pi-d9-committed.diff`, whitespace-independent diff
`/tmp/pi-d9-logical.diff`. Changed source hashes: fixture
`98703a907b8a0a2a1b8ab0cc5425a9896da06d3e606a6d226a1ea1c2781f68e3`,
flake `d7223abccd91ea1464d0dad367329bb4a518b5c4ac898e3cffd8556455ccfe49`,
workflow `596c1247eaca0b613e818b3af9edbd0099a726e64aca6f94cfafd2af64b545e4`,
README `f6ec2ff7a72e48f09d4dbbef05156109d3a2049cbaa6e3d2dece4474ef4f895b`.

README's owning verification explanation and exact commands distinguish required
smoke from manual Extended session lifecycle/recovery. Lead applied final writing
pass; factual comparison preserves scope and live-configuration limitation.
Manual command: `nix build --no-link --print-build-logs .#session-creation-extended`.
Required command: `nix build --no-link --print-build-logs .#checks.x86_64-linux.session-creation`.
Source/index clean and released; all own clients joined, publication held.
Complete series e61→ecdf→5f426→9b→b0→2392; no migrations, pin stream or
published-history rewrite. b0 deployment/pins remain independent. Lead owns final
independent review before one allocated essential VM; no timing target has yet
been measured or claimed. Goal remains about five minutes complete creation job,
ten-minute upper bound; provisional cold estimate near six minutes is not proof.


### Deployed-feature integration preparation and fresh baselines

No merge/claim/default push. Fresh provider/runtime defaults remain db792/e61;
clean detached targets are `codex-web-integration-target-deployed` and
`runtime-integration-target-deployed` under this session's worktree group, with
exact intended deployed heads b67/b0. Runtime's later CI-only feature head is
excluded. Declared Git/runtime shell readiness passed; neither repository declares
an active hook framework. Configuration default advanced ce54->e1fd157e through
three OS-role input updates; shared local workspace master advanced f618->e6c5f9ce
through three tracking-only commits. Initial nonancestor gates were reported;
lead explicitly authorized independent patch-equivalent feature successors.

Workspace successor `d5a26e5006caabdffbc29c4c6ec69efbbd82ceb9`, parent
`e6c5f9ce57b118331de3bce8feb8db01f7fa314a`, tree
`9888a6c236e2b29ab3f0c9839baaf76c2a080652`, replaces deployed bba on its feature
ref. Configuration successor `217c1b968d18a816609ff3d50996f458a31de913`, parent
`e1fd157eb19738134b97dfd16532e57024610efe`, tree
`90997c762b485c04b8d5cccbb417096cf74ab221`, replaces deployed fd on its feature
ref. Exact leases and fresh SSH remote feature equality passed; remote defaults
remain f618/e1fd and shared local master remains e6c5. Deployed heads retained in
backup refs ending deployed-workspace-bba/deployed-config-fd. Both range-diffs
are `=`; stable patch IDs match old/new: workspace92e5d691f7352744baf85a0ab9dc94c723802387,
configc0de463eb2e3e028d3956f4e173ecb795f9a8437. One pin commit per stream; no
migrations, semantic conflicts or merged/default history rewrite.

Workspace pin files are byte-identical to deployed bba. The successor's actual
default derivation is exactly `/nix/store/n0x0lm4mr7j7238r13kzmwih66g6bp8l-dev-workspace-0.2.0.drv`;
its queried output is exactly deployed `/nix/store/fl8dvbx9rpr2xqr9ybzir53s4yf05pzd-dev-workspace-0.2.0`.
This read-only derivation/output metadata proof required no app rebuild. Config
full graph against fresh default has only expected b0/providerb67 changes;
against deployed fd, only the three baseline OS-role identities differ, with
all edges and all source/options/imports unchanged. Aitherdev selects
nixos-stable/home-manager/llm-agents/dev-workspace, excluding those OS-role
inputs; the accepted host boundary remains unchanged. Cross-lock/site, parse
and whitespace checks pass; earlier applicable quick results retained.

Fresh configuration detached target `configuration-integration-target-deployed`
is clean at e1fd. Its declared frozen-bundle Nix environment passes bundle check,
Overcommit0.76.0/RuboCop1.75.8/Nixfmt1.5, actual empty-index precommit trust and
postmerge hook execution without bypass. Root workspace remains shared master;
no broad status/reset/stash/switch or shared index/content mutation. All commands
joined; no tests/build/CI, machine/profile/lifecycle action or cleanup.

Exact target/base/intended-head receipt and literal gated lead merge/push commands:
`/tmp/pi-message-delivery-integration-targets.json` and `...-commands.txt`.
Old/new ranges, stable patch IDs, range-diff paths/hashes and migration conclusions
are in `...-equivalence.json`; lead owns independent equivalence acceptance and
integrated-lineage certificate. Other /tmp integration logs cover rebases,
range-diffs, config graph/target/hooks, cross-lock and feature pushes; deployed/
successor .drv and output metadata are retained. Lead must recheck targets under
short claims only after explicit integration approval, use the shared nonblocking
tracking lock for workspace, and integrate exact deployed runtime b0 only.


### D9-F essential application contracts and extended verification

New normal commit `e86cf8631ad8296a8eff2baea67f7ab8f0bf3025`, exact parent
`2392f0bf3246ef3421630afb7e72dbb17192940d`, tree
`cce949df1156f0565720ebebfc0b7eb32c0ee8db`. Six owned paths, 161+/41-.
Combined E/F review range is deployed/published b0
`b0b246f60d79300b2981e764677d597501a54df9` → 2392 E → e86 F. Full current
series above merged base `e61d3b7e59f07f89df50d23e23d7800d4b13cabf` is
D4 ecdf2355 → D5 5f42669c → D6 9b2b96ab → D8 b0b246f6 → D9-E 2392f0bf →
D9-F e86cf863. No migrations, repeated pin stream or published-history rewrite.
The deployed b0 profile/pins are unchanged; this package does not repin or deploy.

Only `test -e rubyChecks.all` was removed from the checked application's
checkPhase. An exact source reconstruction proves every other application
check/options/tool/preCheck byte unchanged, including Go/Node/auth/input/receipt/
assets/pin/protocol coverage. Essential Ruby uses the same unchanged shard validator
and five whole existing 0/1 suites: workspace_host, coordination_claims,
machine_identity, coordination_admission, integration_certification. Full Ruby
still aggregates all 14 original shards. Every shard definition, full aggregate,
validator and unsharded diagnostic runner remains byte-identical. The new aggregate
is separately exported; no full-Ruby dependency remains in either checked package.

The actual workflow builds exactly twelve routine targets in one invocation:
package, ruby-essential-verification, package-check-separation, codex-package,
pi-worker, pi-runtime-host-unit, pi-runtime-host-environment, ruby-source-filter,
host-module, host-auth-benchmark, host-package-contract, generic-source. Ordered
Pi source preparation and all-check no-build evaluation are unchanged. Essential
application contracts and Session creation smoke remain independent required jobs.
Full Ruby plus three package-composition variants, archive/recovery and the three
host lifecycle checks retain their original selectors under dispatch-only jobs.
All flake exports and normal full flake check remain available. The strengthened
owning separation check reads actual job installables/gates, requires exact unique
aggregate references and whole single shards, preserves all production/devshell/
composition/checked-assets/tool assertions, and checks absence of full Ruby from
both checked application input graphs. No silent missing-target filtering.

Focused quicks passed: four Nix parses and diff/style inspection; actual
`nix build --no-link --print-build-logs .#checks.x86_64-linux.package-check-separation`
(built only tiny nd28fzawidxvkq09nfa6c9lb3h0yhhgn derivation), affected final repeat;
workflow YAML job gates/permissions/refs; exact essential5/full14 input/context
and unique timings-path proof; exact remaining app check and full Ruby source
preservation. Final separation log `/tmp/pi-d9f-separation-final.log` SHA256
`c21b7295e1d265585f2189494f405a280d8e91d82be8dd8c4e0465e9e4acfb83`;
coverage log `/tmp/pi-d9f-coverage-quick.log` SHA256
`c05b5d71bec7310293092076344ea721faa66c95522b13b841def87cc95ea823`;
metadata `/tmp/pi-d9f-eval.json` SHA256
`fc2384e25f27a456cf21d79fa127a175a60f74a315fa7cc76c342e3abcc2b016`.
Initial introspection failures were context-bearing splitString search input and
Nix outPath JSON coercion; the proof plumbing was corrected, with no runtime or
assertion weakening. No full Ruby, application/SDK, VM or browser campaign ran.

Official upstream latest checks found checkout v7.0.1 current and installer
v32.1.0 newer. Lead scoped the compatible installer update into this workflow
change: all five uses now v32.1.0; checkout unchanged. Official release adds
installer hash validation enabled for the default installer. Its action manifest
retains extra_nix_config appended to nix.conf via INPUT_EXTRA_NIX_CONFIG,
composite bash/Linux execution, and no new required input. Actual extra config,
permissions contents:read and KVM/job settings are retained. Sources:
https://github.com/actions/checkout/releases/tag/v7.0.1 ;
https://github.com/cachix/install-nix-action/releases/tag/v32.1.0 ;
https://github.com/cachix/install-nix-action/blob/v32.1.0/action.yml .

README's existing verification section carries the lead's final prose: actual
application/Ruby scope, two required jobs, exact full Ruby/composition/archive/
host manual commands and relevant-change integration requirements. Existing
fake-command and live-configuration/deployment limitations remain. Factual match
and whole six-file diff were inspected before the normal Nix commit. Source hashes:
workspace-portal `b21b50d38b482a494282748b5b823bf5925aa02ff168482c2325715b8d4ac740`,
ruby-checks `3bc3c01389e77e1945cbf40bfcbf8dc10af10bfbf6a89e065b624d40e789c2f2`,
separation `cd6e74b9ed5b6a2187f452a699b47bb2ab5ec7a8fe9cc70218328cfd531ef8e8`,
flake `31e1a6c98df6e2140b4b01d4a54f405fa056caf91db2545f56462a5848627640`,
workflow `f2a8f5f0d8a1b7cb78af03cd42de96f62193cfcab6dcb316cdf0f9ddbed3eef3`,
README `2e78d682c4643979fdd462f67a77ef9b611a8b7ea861f9e57e53f6793ab3cedc`.
Full committed diff `/tmp/pi-d9f-committed.diff` SHA256
`de14392d3e7cdb1b1e45ce269416717cb48fcd47b43ab643340541950f09c880`;
combined E/F `/tmp/pi-d9-ef-combined.diff` SHA256
`123cae0f6814e49113eca738ab4b5efe7f3d801f1feebe8a83209c84d466e2a4`.

Every own command/client/check joined, source/index clean and released,
publication held. No CI poll/retry/cancel, default mutation, live session action,
claim or deployment. Lead owns combined final independent review and one exact-head
CI verification; latest direction avoids a duplicated local VM. Cold complete
required-pipeline elapsed remains unmeasured here; no five-minute performance
claim. Capacity is available after package acceptance.


### R-D9-1 narrow review remediation

Blocking finding: the Pi worker contract's Python prelude still required the old
jq-generated workflow selector and master-host gate. Executing only that exact
extracted prelude reproduced `ambiguous workflow filter` against the new workflow
before worker contracts. Removed that obsolete prelude and its now-unused jq
native input; the authoritative actual-selector/gate checks remain in
package-check-separation. One nearby workflow-reader audit now finds only that
owner. SDK/Node equality assertions and every remaining worker/auth/receipt test
are byte-exact, preserved suffix SHA256
`677c8c001cf157350f8c5858bae4756dc288b8febcc6a9eb840f2562502dc0ac`.

Normal unpublished F amend yields `c8eb7b74c078d62077889a6dbb5da57ad19dafc4`,
unchanged E parent `2392f0bf3246ef3421630afb7e72dbb17192940d`, tree
`f3167ce62f157e28d1151d919342755d01f9e42e`. Exact old F e86/treecce949df remains
in `2026-11-23-pi-message-delivery-pre-r-d9-1-f`. Only
nix/tests/pi-worker.nix changes (1+/16-); all 1140 other tree entries are identical.
No published history or E/b0 change; no migrations. Normal hooks/no bypass,
source/index clean/released and all clients joined. Publication held.

Focused extracted-prelude reproduction/source preservation, Nix parse/diff and
actual owning separation check passed. Actual pi-worker nativeBuildInputs evaluates
to python3-3.13.15 only. No worker/SDK/app/VM/CI campaign ran; commit environment
realized only a tiny nix-shell-env derivation. Source log
`/tmp/pi-d9-r1-source-quick.log` SHA256
`2a0302e0cc1d027b20a5dd17a1f8356b45eb4dbc5b6ae52db95812f7a6332f34`;
owning check `/tmp/pi-d9-r1-owning-check.log` SHA256
`c21b7295e1d265585f2189494f405a280d8e91d82be8dd8c4e0465e9e4acfb83`.
Worker file SHA256
`7083b9d35604678bc3c3aeedd0d5a88cc3fd1fa2ec47a5bb705cd9726afd0266`.
Range-diff `/tmp/pi-d9-r1-range-diff.txt` SHA256
`7860cbdbb31a7006af74f0403eb280980ec913fb23f2fe7869fb8c5819b6695f`;
owning diff `/tmp/pi-d9-r1-worker.diff` SHA256
`4a52c7722af2ad38616f9aac699c767cab22d28b70d055fc844525e215a883fa`.
Combined current review range is b0→2392 E→c8 F; prior packet remains equivalent
outside this narrow fix. Lead owns step9 direct inspection and continuing review.
No action-version/prose scope, deployment effect or new performance claim.


### D9-E/F final review acceptance and feature publication

Lead accepted reviewer0's completed four-lane/history/migrations/docs review at
`c8eb7b74c078d62077889a6dbb5da57ad19dafc4`, with no open findings and
R-D9-1 directly resolved. Ordinary nonforce canonical SSH feature push joined0,
b0→c8. Fresh direct remote feature equality proves c8; remote HEAD/master remained
`e61d3b7e59f07f89df50d23e23d7800d4b13cabf` before and after. One ordinary
capture-comparison succeeded for complete e61→c8. Narrower deployed b0→c8 range
remains in the existing E/F evidence without replacing that complete comparison.
Source/index clean and released; all Git/API/message clients joined. No default
write, claim, pin refresh, local VM/app/SDK/Ruby campaign or deployment occurred.
Deployed b0 profile/pins remain separate and untouched.

New exact-feature Check run `45479418749`, workflow `354263807`, attempt1,
head c8, URL https://github.com/aither64/dev-workspace/actions/runs/45479418749 .
One bounded new-head job read observed Session creation smoke
`138748235659` and Essential application contracts `138748236074` in_progress.
Extended Ruby and package composition `138748237523`, Extended host lifecycle
`138748237922` and Extended session archive/recovery `138748237935` completed/
skipped as selected for a push. No success or timing result is claimed from this
initial status. Old b0 successful run45466397506 was left intact. No retry,
retrigger, cancellation, wait or watcher. Lead owns monitoring/diagnosis of this
one required essential VM and the complete cold required-pipeline measurement.
Publication package complete for acceptance; capacity available.


D9 exactheadCI45479418749/c8 COMPLETE SUCCESS. Requiredcreationjob6m44 andessentialcontracts10m03, threeextendedjobsskippedasdesigned. Requiredpipelineelapsedfromruncreationtolastrequiredcompletion 606s, total~10m06; near5targetNOTmet. Smokeraw/tmp/pi-d9-ci-smoke.log confirms both codex/pi completion, actualVMscript192.55s(Codex78.80/Pi72.62). ActualoneVMsuppliedbyCI, no duplicate localcampaign. Solefastlog/tmp/pi-ci-duration-c8-fast-138748236074.log SHA f677787e44eab4e9b3f40412f880a813a546fc416a64c06cee906030ef31c63f: checkedappcheckPhase~5m13, Go web240.598s/workspacecodex85.563s; essentialRubycompletedbeforecheckedappstart, nofullRuby/variantbackdoor. RemainingD10speedworkparkedatusernewdeliverypriority; no5minclaim.


## D11 image3 clarification and exact observation

Four boundedGETs all200/allclientsjoined, source sensitivityordinary verified.
CurrentcollectionsoleSentrow originalID/receiptID joins appliedtranscript
userMessageoriginalID; receiptturn matches user+assistant entry, latest/current
turn and body/page/activity nativeidentity. Activityidle/latestcompleted,
metadataPendingfalse,2turnmessages/0tools. Start1.616safteradmission, reply/turn
complete15.503safteradmission; rowabout3h old. This is publictranscriptprojection
proof with ownedaccepted witness, not an independentnativehistoryread or general
latencyclaim. Identifying/private data onlyverifiedignored/untracked0600localfile;
no peer IDs/messagebodies retained here. User then explicitly recognized delivered
andanswered, identifying remainingstatusbar as problem. No resend/retry/drop or
nativeeffect performed.

Source-onlyI0 confirms durableStore.list exposesopen+100terminal, renderer removes
only IDs absentfromcollection; no durable transcript-observationretirement.
Legacyreceipt view already has observationseam. Actualhandofftrace didnotprove
an idleforgottenstart; userclarification closesdeliveryinvestigation.

D11sufficientbriefin design.md allocated onecompleteI0package: sharedview
observeTranscript exactscope/originalID/receiptturn vs applieduserentry; only
sentmatchingtuple hidden inview, no storage/poll/gate/metadata/input change.
Both actualconsumers/arrivalorders/tests, no manualdismiss mechanism necessary.
Provider/runtimepins/cache/docs/historyevidence ownedsamepackage; no nativecampaign.


### D11 shared status retirement and consolidated provider selection

Provider `30bf3636e14ae45547c79f2091a3897eb3b635ed`, parent deployed
`b67d86a889cf3ac88d78f03d2dcd5f061f95d0b2`, tree
`ac3a466087118d38ae997054d4d18b0a678b6ed2`, committed and published by ordinary
SSH feature push; fresh equality and unchanged remote default db792 proved.
Runtime final `d15735fa9695aaed3cb45c073e01b8ef4e6904c8`, parent functional
`315d2a3f6a9b72cb6bb358cd63da658b578e5b5b`, tree
`0f49c78a6bb315dbcb9349f9e2d95fc533ed1b92`, is committed but publication held.
The functional tree `4d30f1350bf3da27fe6fda5b30e621fafc6fbebf` equals the tested
pre-consolidation tree exactly. All source/index windows released clean; every
own client/command joined. No browser/native/app/SDK build or deployment ran.

The shared observeTranscript(entries, scope, threadId) method hides only sent rows
whose validated original/receipt identity matches an applied userMessage's original
ID and turn. Observations stay in mounted memory. Current thread rebinding clears
and disables that old filter; foreign/stale calls cannot erase or establish it.
Non-sent/retired-unknown/changed tuples remain visible, raw metadata and admission
are untouched, read errors remain visible, surviving actions retain focus. Both
actual consumer sites reuse applied history when metadata arrives and observe
current successful applications. No storage, timer, sender, receipt, worker,
protocol or effect-gate change. Provider child cache3/example24; runtime parent31
and all three app template caches85. Lead final prose lives in existing provider
reference and portal guide, including precise API/fence, durable labels and
preserved legacy instructions/completion limits.

Provider mounted/shared/actual consumer checks passed13/13 (1.927s), including
both initial arrival orders, both POST/transcript orders and real native rebinding;
final nine shared-observation cases passed separately. Exact example checks passed
0.018s. Initial fixture lacked its required custom-client basePath and the first
example command inherited vendor-mode GOFLAGS; both were corrected at their
owning fixture/command boundary without weakening assertions. Runtime against the
new selected provider passed27 read-cycle cases, actual source consumer guard,
all three previously failed D8 Go tests plus owning composer contract (four Go
tests, package2.293s), syntax, pin positive/negative and actual-pin checks, Nix
parse/diff. Browser fixture now asserts exact sent-row retirement on applied user
input/reload while unknown rows and send gates persist; its actual browser run
is still a lead-owned post-review requirement, not claimed passed.

Runtime quick `/tmp/pi-d11-runtime-quick.log` SHA256
`3e01028b9f030ad4224598dc38b738f6fef0ba66e3d110ce2c56feb5981015e0`;
provider example `/tmp/pi-d11-provider-example-quick.log` SHA256
`35923bad641aca560049144670864a1ce6d7ff44d2b70166dc060104c0ea941b`;
final shared `/tmp/pi-d11-provider-observation-final.log` SHA256
`8389e9bb2647cea2f056fa7d5a8cd5390f257efc9dde1c0e2dd37c814138fa6d`.
Go selects `v0.0.0-20261124205019-30bf3636e14a`; NAR
`sha256-ikva/n0dPpjZKgtJhbKlLwYgs4qJNzbfhTlHPQTOuy4=`; vendor
`sha256-V0q/615pZtlpgNCnweuoWwymMbo5leamACHBcZVF2CE=`. All other lock
nodes/modules/checksums were preserved. Provider7 paths130+/10-. Runtime final
oldc8→head13 paths60+/22-, including the separately authorized output flag.

One final provider selection stream was folded into owning D5
`4412f3de642e1f9e69f15f3282dd5657aa5c5260` above unchanged published ecdf.
D6 `e2f659ef04be523c9b9179f4479ecac40cc2efcf`, D8
`ba57427b1e2552f53dd87f3273f3dd57ec785963`, D9-E
`b4e98cb2d74671e4438a4ebda3e9883e9a3f61c1` and D9-F
`643086d9b8a9764b9e2ee5a4751b2a5f051d3eea` are patch-identical to their old
9b/b0/2392/c8 commits. Normal autosquash/replay had no conflict or hook bypass.
Backups pre-d11-c8, pre-d11-b0, pre-d11-b67 and pre-d11-consolidation retain the
exact old reviewed/deployed heads and tested pre-rebase tree. Old deployed b0 is
now a retained nonancestor, not literally merged; D11 is a substantive successor
awaiting its own verification/deployment. No obsolete final fixup, redundant pin
commit, migration or master rewrite. Full series is e61→ecdf→4412→e2f→ba57→
b4e9→6430→315d→d157; provider db792→b67→30bf.

The final focused CI logging commit changes exactly two lines: direct
`go test -json ./...` and its literal owning assertion. No tests/options/env/exit
semantics or D9 historical patch changed; no pipe/parser or extra Go run. Nix
parse and actual tiny separation check passed. Output quick log
`/tmp/pi-d11-ci-output-quick.log` SHA256
`ddf885f72d6fb1513a440e63aad6c14159d74b7bffc5e1a61c5a564778e90042`.
The next already required CI alone supplies per-case timing evidence.

Review artifacts: `/tmp/pi-d11-range-diff.txt` SHA256
`b4dd63a69689cb53c76b7776e62de0b182ae9e4eec2823609ff44d6f1e2e9716`;
`/tmp/pi-d11-history-receipt.json` SHA256
`a2446faccade15506db88338b869e83cb008240342b296ddfbf2704f6bf5ec3d`;
`/tmp/pi-d11-runtime-final.diff` SHA256
`2f3b5d9830879cf9e20c6af54d7649932e5b782bdc85f65b2cd17aa187fc1441`;
`/tmp/pi-d11-provider-full.diff` SHA256
`d5e548ead795508fe831f5ec0b73fcb0cf5daed69ec5ce2cf9ae6d44c942cddc`.
Lead owns final combined review, one affected browser batch/final CI and any later
matching pins/build/deployment. No runtime publication, new downstream pins,
merge/claim/worker restart or performance promise. Capacity after acceptance.

D11 affectedactualbrowser PASS on reviewed runtime d157/provider30bf.
One freshLuna utility ran ONLY literal selfcapturing /tmp/pi-d11-browser/run.sh
SHA4439706458e299dd0696a8da5753c8acba6268e254f3d8c94a9b9fa9e55b192f.
Command0/preidentity0/prehash0/postidentity0/posthash0/final0/41s;
existingdurableCJS Chromium/Firefox subtestPASS17.59s, no activity/Codexmatrix.
All13absoluteinputs and HEAD/tree/cleanindexbefore/aftermatch, no sourcechange.
LogSHA25b64d38c9137be9c74ea8ac346f47029867f4828c1572d221cd0403f3c80cd6;
resultSHA0ca1bf6c9317fe21231ed3394ce12cc2eb2ac81eedf0e6649998649ee851742d.
Utility73497/allcellsjoined/finalreportreceived; no remainingeffects. No native/
peerinput/service/appSDK/VMcampaign. Earlierbriefprefixecddb1cd was stale;
owningfinalfullSHA443970 authoritativeconfirmedquiescent BEFORElaunch, no repeatedrun.
Browser covers actualrendered matchedsentretirement/reload+unknowncontrols and
unchangedsendgates. Finalruntimepublication+pins/CI/composed/deploymentremain.

### D11 final review, browser proof and feature publication

Lead accepted the exact runtime d157/provider30bf final four-lane review with no
findings. The sole affected durable browser batch used script SHA256
`4439706458e299dd0696a8da5753c8acba6268e254f3d8c94a9b9fa9e55b192f`:
exit0/41s, required subtest PASS17.59s, both Chromium and Firefox, exact head/tree
and all13 frozen inputs unchanged before/after. Raw
`/tmp/pi-d11-browser/run.log` SHA256
`25b64d38c9137be9c74ea8ac346f47029867f4828c1572d221cd0403f3c80cd6`.
Lead's utility73497 and all owned cells joined; no additional check was launched.

Canonical SSH feature push joined exit0 using exactly
`--force-with-lease=refs/heads/2026-11-23-pi-message-delivery:c8eb7b74c078d62077889a6dbb5da57ad19dafc4`
and source `d15735fa9695aaed3cb45c073e01b8ef4e6904c8`. Fresh direct remote
proof confirms final feature equality and unchanged master/HEAD
`e61d3b7e59f07f89df50d23e23d7800d4b13cabf` before/after. No default push;
e61 and published ecdf remain ancestors. Runtime tree remains
`0f49c78a6bb315dbcb9349f9e2d95fc533ed1b92`. Raw receipts:
`/tmp/pi-d11-publication-{remote-before.txt,fetch.log,push.log,remote-after.txt}`.
I1 received the exact reviewed/published SHA and matching-pin dependency release
(message `5b26961e22d342db97426fdd406fd545`). The e61→d157 comparison capture
succeeded after the first command was refused while that same handoff command
still held the session lock; no comparison effects occurred on the refusal,
and no contended retry loop ran. Success receipt:
`/tmp/pi-d11-publication-comparison-after-join.log`.

One bounded exact-head CI API read found run `45488722202`, workflow
`354263807`, attempt1, head d157. Required jobs `138780969175` (Session creation
smoke) and `138780969776` (Essential application contracts) were in progress;
all three explicitly extended jobs were skipped. This is startup metadata, not
terminal verification. Raw `/tmp/pi-d11-publication-ci-runs.json` and
`/tmp/pi-d11-publication-ci-jobs-45488722202.json` retain the snapshot. No watcher,
rerun, cancellation, native call, deployment, merge, claim, pin or lifecycle
operation was performed. Old c8 CI was already completed success per lead.
No source/history/test changes in publication; existing no-migration and
reviewed/consolidated lineage conclusions remain unchanged. All own publication,
comparison, API and messaging clients joined; runtime/provider windows released.
Lead owns matching-pins/build/deployment, subsequent approved integration and
machine release. Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-23-pi-message-delivery/


### D11-P final display-retirement matching pins and integration preparation

Complete/released final workspace `c6534049f84fea7a017e9ad8828a96236ba8c748`,
parent shared-local-master `e6c5f9ce57b118331de3bce8feb8db01f7fa314a`, tree
`d912eac749bdc4b2996aa5cbab17fd7ffa7216c9`, two flakes 9+/9-. Configuration
`1c81a4d76857e9ccbd638a6a0f29e50d39f6fc41`, parent fresh default
`f1d38b49a108420520646ce18e4e2990a319453a`, tree
`47fd27d9213ef8d70ec86d022e3605ada339c77b`, generated lock only 7+/7-.
Both canonical SSH feature rewrites used explicit d5/217 old-head leases;
fresh remote equality passed, defaults unchanged f618/f1d, shared master e6c5
and unrelated dirty records/index untouched. Both feature trees/indices clean;
all command clients joined. Scoped own-branch CI lists [] for both, no watcher,
cancel or retry. No default merge/claim/profile/worker/lifecycle action.

Both locks select reviewed/browser-verified/published runtime
`d15735fa9695aaed3cb45c073e01b8ef4e6904c8`, actual resolved NAR
`sha256-bBzdiTmCUUA+Qjk24q5i5hGZCm1WIIr5OeITuYColPo=`, and provider
`30bf3636e14ae45547c79f2091a3897eb3b635ed`, NAR
`sha256-ikva/n0dPpjZKgtJhbKlLwYgs4qJNzbfhTlHPQTOuy4=`. Complete 38/67 direct
path graphs plus follows compare with fresh bases: only intended runtime and
provider identities change, exact committed runtime subgraph matches, every
other sibling/extension/native/SDK/Node/catalog/model/team/claim/policy identity
and edge preserved. Cross-lock/site and full locked-runtime/provider identity
equality pass. Runtime owner selects Go30bf and vendor
`sha256-V0q/615pZtlpgNCnweuoWwymMbo5leamACHBcZVF2CE=`; no duplicate Go/vendor
build was run here. Workspace existing Ruby4/19 passes1.344589s plus parse/diff.
Config ordinary frozen-bundle exact channel set --commit passed Nixfmt/message
hooks, preserved generated e61->d157 full eight-commit changelog and width
warnings; JSON/Nix parse/graph/diff pass. No manual lock/message edit or bypass.

One final logical pin per stream replaces superseded unmerged d5/217 (neither
is an ancestor); deployed bba/fd and prepared d5/217 backup refs retained. Old/new
range-diffs and migration/history conclusion are in existing
`/tmp/pi-message-delivery-integration-equivalence.json`: intentional reviewed
runtime/provider refresh, not patch-equivalent to the old deployed b0 application.
New verified D11 deployment is required; no old fl8 equality claim applies.
The earlier patch-equivalent pin-only rebases remain in the saved D11-prior
integration artifacts. No migrations/default or merged-history rewrite.

Fresh configuration baseline e1fd->f1d adds only vpsadminServices/Webui identities,
with unchanged edges and all source/options/imports; Aitherdev selected roles
exclude those inputs, preserving earlier three OS-role advances. Exact seven
host/helper/session-entry/Codex files and worker/SDK source are unchanged b0->d157;
runtime lock changes only browser provider, provider native catalog is unchanged.
Accepted D7/D8 profile-only host boundary reuses; no full system eval/build or
native Codex/worker upgrade. The new composed application build is lead-owned.

Clean detached integration targets: existing codex-web-integration-target-deployed
at db792 ->30bf; runtime-integration-target-deployed at e61 ->d157; new
configuration-integration-target-d11 at f1d ->1c81. Config target's declared frozen
bundle, Overcommit0.76/RuboCop1.75.8/Nixfmt1.5, actual empty-index precommit and
postmerge trust hooks pass without bypass. Existing commands/targets JSON updated
in /tmp; commands explicitly require new deployment verification first, then
lead-owned short claims/merges/push proof, with shared workspace staying master
and its nonblocking tracking lock. No integration was executed. Raw D11 logs cover
runtime-published, host-boundary, workspace pin/quick/commit/range-diff/push,
config target/hooks/pin/quick/generated-message/range-diff/push, crosslock and CI
JSON. User approved deploy-then-merge-four-masters-and-release sequence; lead owns
mechanical acceptance, composed checks, deployment and later claimed integration.

## D12: outstanding status list independent of loaded history

Implementation delivered for final independent review, with both source/index
windows clean and all own effects joined. Provider normal new commit
`2547d535eefd4154afef4125ea0fb76e5894a8b6`, parent merged
`30bf3636e14ae45547c79f2091a3897eb3b635ed`, tree
`c33f3f021fb7aecee49e43e03476ecc1b6c80105`, 9 paths185+/104-, is published over
canonical SSH; fresh remote feature equality and unchanged default30bf proved.
Runtime normal new commit `65544340f94ebb112872743738f84c1a7022b06a`, parent
merged `d15735fa9695aaed3cb45c073e01b8ef4e6904c8`, tree
`e3f0543d4eb45af85f32a818e885a02d74b338ec`,13 paths180+/50-, remains
publication-held. No merged history rewrite, repeated unmerged pin stream,
schema migration, native/backend change or downstream pin mutation.

The generic HTTP handler validates the entire provider collection before copying
only non-sent statuses to its response. Validation, ordering, settings, scope,
selection, capacity and provider-owned data remain intact. Exact-ID GET and
create-or-get POST still return successful receipts. The shared mounted view also
omits validated sent rows from older servers and immediate POST results; raw
metadata, sender recovery, generation fences, errors and actions are unchanged.
D11 observation state and both consumer call sites are removed. The public
observeTranscript method remains a documented no-op returning false for shipped
consumers. Child cache4/example25, portal parent32 and all app caches86 are updated.
Lead supplied and accepted final prose in provider docs/reference.md and runtime
docs/workspace-portal.md; surrounding recovery and legacy warnings remain.

Provider declared Nix quick command used GOFLAGS=-mod=readonly/GOWORK=off,
`go test -mod=readonly ./conversation -run 'Test(DurableDelivery|RetiredDelivery)' -count=1`,
syntax, `node --test test/deliveries_browser_contract_test.cjs test/conversation_browser_contract_test.cjs`
and the example Go package. All passed: Go .019s/example.020s,10 Node cases.
Coverage includes validation-before-filter, malformed sent/duplicate/scope/count
refusals, provider nonmutation, direct receipt recovery, both actual mounted
arrival orders, POST/old-GET/failed-refresh races, preserved raw metadata/focus,
two successes older than initial history, explicit older-page load and destroy/
fresh mount against both current and older servers. Provider quick log
`/tmp/pi-d12-provider-quick.log` SHA256
`0df7ab2a436af63b0ffef28be6de2008bd9836ea620aa769de148801ae285a3e`.

Runtime fake-backed real HTTP regression passed2.07s: two initial fixture native
witnesses produce retained successes; collection omits both, direct GET/repeated
POST return exact original status/receipt, changed wire conflicts, and not_sent,
pending, unknown and queued remain visible. Repeated list/recovery leaves saved
admissions, statuses and SQLite db/WAL bytes unchanged, with zero additional
native sends/binds/lookups/inspections. The three D8 Go contracts and existing-ID
selection/capability recovery also pass (five Go tests, package5.551s);27 existing
read-cycle/mounted cases and syntax/actual composer Node contract pass. Raw
`/tmp/pi-d12-runtime-quick.log` SHA256
`a59751d008faf5da424bfc5a48d4194a254669300ea0557c7b564eaf6f77664e`
retains an outer login-shell exit1 after all checks passed: /etc/bash_logout
referenced unset __ETC_BASHLOGOUT_SOURCED under the wrapper's nounset option.
The corrected nonlogin wrapper ran the owning Go
TestPortalDeliveryComposerPreservesSelectionAndDraft (.209s), syntax and diff,
exit0: `/tmp/pi-d12-runtime-final-quick.log` SHA256
`ce67cc0b7c405102862e326f9970e7c20a376387a0cce2ced63cfdf6893f79d9`.
No product change or test assertion weakening addressed that wrapper issue.

Exact provider Go version `v0.0.0-20261125081347-2547d535eefd`, NAR
`sha256-rLBeHQVPUfmqPw0tMjkenkp+BA0Xi2VX/iMz+4wiT9c=`, vendor
`sha256-wTZJfjvS+bI2KqIw6KX0ghBrozUjbUbgY9PDzJGV/6g=`. The vendor tree was
created in a disposable source copy; only codex-web lock node/module selection
changed. Existing positive/negative and actual-pin checks, Nix parses and diff
checks pass: `/tmp/pi-d12-runtime-pin-quick.log` SHA256
`b8a6c32d373355351291471bfe2c96358d5e1ed926ec653d26b0f43a3ea61789`.

Complete one-commit lists `/tmp/pi-d12-{provider,runtime}-series.txt`; full diffs
`/tmp/pi-d12-provider-final.diff` SHA256
`0920580191b63cf4a88ed35a7ff5448913a010b7e32e38f1b2017a5d452504dc`
and `/tmp/pi-d12-runtime-final.diff` SHA256
`0378b231fdef167a6f84d30b16e697af8b7490283d140e7355dc66a0e0556d08`.
Lead receives exact review packet message5319859fbc024ff3afae976a39d2e423.

Browser preparation only: argv
`["/run/current-system/sw/bin/bash", "/tmp/pi-d12-browser/run.sh"]`, runtime CWD
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-23-pi-message-delivery/dev-workspace`.
Script SHA256 `a555607862e3e9b7336601a178fab90c1eeb9834952d2210b14649cb8745434d`;
13-input absolute manifest SHA256
`fb77263565edd92943035c63cbc8b2ef281dec5c94ec72b7453b7cb253befefe`.
Same retained pinned Nix/Go/Node/Playwright/full browser stores as D11. Only
TestQuestionBrowser/message_delivery_browser_test.cjs, PI_MESSAGE_ONLY=1 and
PI_DURABLE_ONLY=1, explicit unset PI_ACTIVITY_ONLY, Go timeout3m, both engines.
Script self-captures /tmp/pi-d12-browser/run.log and run.result, exact head/tree/
clean and pre/post hashes even on failure, original command/final exit+seconds,
and refuses a duplicate capture. The durable fixture now checks two historical
successes remain absent before older reads, after explicit wheel history load
and after reload for both server versions; unknown controls and original-ID/lost
reply/draft assertions remain. It fails D11's first unobserved sent transition.
No browser execution, app/SDK/VM build, live peer/native operation, CI monitoring,
deployment, merge/default push, machine claim or lifecycle action was performed.
Next: lead final review, one affected browser allocation, exact final runtime
publication, then I1 matching pins and lead delivery workflow. Session remains open.

### D12 final review, browser verification and runtime feature publication

Lead accepted reviewer0's completed four-lane final review of provider2547/runtime
6554, including complete history, no migrations and documentation, with no findings.
The sole affected actual Chromium+Firefox batch passed exit0/36s, with all
command/pre/post identity and13 hash checks zero; runtime head65544340/treee3f0
was unchanged. Raw `/tmp/pi-d12-browser/run.log` SHA256
`f4ec5361bf61758ae77affea150b0ea944e25d65e4e0904649148bc8c409614b`;
result SHA256
`99fc0c3d693742fa661a68198c4aab27c3ea9572dbb4fc54c023dc6f5fa64966`.
Lead's watcher44846 and every operation client joined; no extra check launched.

Normal canonical SSH NONFORCE feature push from merged
`d15735fa9695aaed3cb45c073e01b8ef4e6904c8` to reviewed
`65544340f94ebb112872743738f84c1a7022b06a` joined exit0. Fresh direct remote
feature equality is65544340; default master and HEAD remained d157 before/after.
Runtime remains clean at tree`e3f0543d4eb45af85f32a818e885a02d74b338ec`.
No default write or history rewrite. Raw publication receipts:
`/tmp/pi-d12-publication-{fetch.log,push.log,remote-before.txt,remote-after.txt}`;
push log SHA256
`9c805a370bf1b8f0e24f27f23f1b85bae474d849bedb5beec5e21c3f843368ad`.
Full current d157→65544340 comparison captured once, exit0:
`/tmp/pi-d12-publication-comparison.log`. I1's reviewed/published dependency handoff
message`6cd1c42143284032b71f2f4cfa4e82f2` joined exit0, receipt turn
`01a211d0-f3b7-7840-9c91-8dec5f9c0f93`; matching-pin work may proceed under its
existing allocation.

One bounded own-branch CI listing found exact-head run`45576326506`, workflow
`354263807`, attempt1, head65544340, in progress. Jobs`139075066557` (Essential
application contracts) and`139075066676` (Session creation smoke) were in progress;
all three explicitly extended jobs skipped. No superseded active own-branch run
was present, so none was canceled. Snapshot only, no terminal CI claim, watcher,
wait, retry or retrigger. Raw `/tmp/pi-d12-publication-ci-runs.json` and
`/tmp/pi-d12-publication-ci-jobs-45576326506.json`. URL:
https://github.com/aither64/dev-workspace/actions/runs/45576326506

All own publication/comparison/API/message clients joined, source/index clean and
released. No extra source/test work, build, peer/native call, downstream pin,
claim, merge, deployment or lifecycle action. Lead owns remaining final CI,
matching composed build/deployment and any separately authorized integration.
Stable session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-23-pi-message-delivery/


### D12-P new follow-up pins and integration preparation

Complete/released workspace `09ea6f43a9ddd17317c0ae96481c46b0c1c24695`, parent
tracking-only shared master `3a17e487e55f91f48da5e8fe697d578afea1181a`, tree
`ea4067cd9ed5b3712182088d523969d1271a3f15`, two flakes 9+/9-.
Configuration `d5055ec0b2ea22de976f6703208f5526c3e185ca`, parent fresh default
`5b68d1216ecee31848785da18737ec0ae796db59`, tree
`f2d2f3e3ef0610693ebb64eae00467edfa09f004`, generated lock 7+/7-.
Both are NEW normal follow-up commits, with merged D11 c653/1c81 preserved as
ancestors; no amended/consolidated merged history or migration. Normal nonforce
canonical SSH feature pushes joined and fresh remote equality passed. Defaults
unchanged c653/5b68, shared local master3a17 untouched, feature trees/indices
clean. All own effects joined/windows released; workspace09ea stays frozen for
the lead's composed batch. No CI watcher, default write, claim, merge, deployment,
worker/protocol/state or lifecycle action by this package.

Publication prerequisite independently verified before mutation: reviewed runtime
`65544340f94ebb112872743738f84c1a7022b06a`, actual NAR
`sha256-X44N4WDWs9siT8ocCWNC5ZcR2a0qyVy+fJHyG21Xpe0=`, with provider
`2547d535eefd4154afef4125ea0fb76e5894a8b6`, NAR
`sha256-rLBeHQVPUfmqPw0tMjkenkp+BA0Xi2VX/iMz+4wiT9c=`. Full 38/67 direct-path
graphs plus follows against fresh bases prove only the intended runtime/provider
identity changes. Exact committed runtime subgraph, complete locked runtime/
provider equality, and existing cross-lock/site checker pass. Extension bf12 and
all unrelated SDK/Node/native/catalog/model/team/claim/policy identities and edges
remain unchanged. Runtime owner Go version is
`v0.0.0-20261125081347-2547d535eefd`, vendor
`sha256-wTZJfjvS+bI2KqIw6KX0ghBrozUjbUbgY9PDzJGV/6g=`; no duplicate Go/vendor
build was run here.

Workspace declared Nix parse and existing Ruby deployment contract pass 4/19 in
1.366298s; diff checks pass. Configuration ordinary exact channel set --commit
preserves generated d157->655 one-runtime-commit message, normal Nixfmt and message
hooks pass with generated width warnings retained. JSON/Nix parse, graph and diff
checks pass. No hand-edited lock/message or hook bypass. The final seven host/
helper/session-entry/Codex files, worker/SDK builder source and native catalog are
unchanged d157->655; flake wiring changes only provider URL. Reuse the existing
host-boundary proof without another system evaluation/upgrade campaign.

Fresh configuration changes only three excluded OS-role identities 5ccf->cf53;
all source/options/edges and relevant Aitherdev selected closures are unchanged.
Fresh shared workspace changes one archive tracking commit/four records only;
unrelated dirty files/index preserved. Own verified identity and saved roster
(Sol/xhigh/workspace_write) were checked before preparation. Merged-head backup
refs added without removing existing refs. D11 proof/receipts remain intact.

Clean detached integration targets: provider existing target at merged30bf for
2547; runtime existing target at mergedd157 for655; new
configuration-integration-target-d12 at5b68 ford505. Config declared frozen-bundle
Nix setup, bundle check, Overcommit0.76/RuboCop1.75.8/Nixfmt1.5 and actual empty-index
precommit/postmerge trust checks pass. New D12-only target/history/commands JSON/
text files live under `/tmp/pi-message-delivery-D12-integration-*`; commands enter
the declared environment before the lead's short claim and leave shared workspace
on master with its nonblocking tracking lock. No integration was executed.
Other D12 /tmp logs retain baseline proof, runtime publication, host boundary,
workspace base/pin/quick/commit/push, config target/hooks/pin/quick/generated message/
push and cross-lock. Lead owns mechanical acceptance/composed checks, deployment
and any later explicitly directed claimed integration/release.

## D13-P: prevent a proven initial-ID conflict from becoming transport Unknown

Normal new runtime commit `9bf34aa1963e3ba226ec678237cee3dacb2e7a25`, parent
protected merged `65544340f94ebb112872743738f84c1a7022b06a`, tree
`810336d4a4698085b2a092a2f3eca6742a9e8e2b`, is committed and publication-held.
Exactly3 owned paths104+/4-: six-line pi_teams.go precheck, existing actual host
fixture extension, and the short lead-written Host callbacks paragraph in
docs/pi-runtime.md. Source/index windows released clean; all own check/command
clients joined. No R source work or existing-held recovery was performed.

The creating-member path now checks its immutable nonempty initial ID before
settings lookup, ready proofs, reservation or materialization. A different ID
returns existing ErrPiConflict with stage initial_reservation and no-effect still
intact. Existing preSendRefusal supplies unattempted evidence; the actual host
handler returns normal result/nil transport error. The reservation authority
retains its own conflict check. Same-ID and empty reservation continue through
original materialization/lookup/send. No missing-receipt inference, generic error
conversion, callback ledger, native guard or hold-clear change.

Old-source actual-host regression fails for both UUID and compact original caller
inputs: conflict returns a nonnil transport error (Go2.373s, exit1). Log
`/tmp/pi-d13-p-red.log` SHA256
`725e0e750f505d76ca485cdd8b757db4130fd2766a4bf04fa3ce7cc6697d95f0`.
After the fix, the full existing host fixture passes21.438s:18 principal cases
plus26 invalid-origin negatives. Conflict returns result/nil, refused at
initial_reservation with unattempted materialization and no native result.
Snapshots preserve every actual regular domain record's bytes/inode/mode/mtime,
roster/binding and caller receipt, with zero new Create/Send. Same-ID acceptance
and no-replay retry, empty reservation, policy-held/created-empty, uncertain
creation/proof, cancellation and genuine Send-Unknown cases retain their rules.
Green log `/tmp/pi-d13-p-green.log` SHA256
`68dae41d57120a80d2dc737d236f55648c3f89338e32c0bdea7fb70e015a59bd`.

Commands use declared nix develop with GOWORK=off and GOFLAGS=-mod=readonly:
`go -C portal test -mod=readonly ./internal/web -run '^TestPiTeamHostCallbackPreservesKnownPreSendRefusal$' -count=1 -timeout=1m -v`;
`go -C portal test -mod=readonly ./internal/teamruntime -run '^TestPi(FirstAssignment|Roster|Delivery)' -count=1 -timeout=1m -v`
passes.121s; existing isolated fake-worker callback tests
TestActualNativeHostCallbacksGateOnOriginalReceiptWithoutSendDeadlock,
TestCallbackProjectionAndRawArgumentsAreBounded and
TestForwardedCallbackCancellationAndDisconnectRetainUnknown pass7.368s, including
abort/disconnect holds and ordinary successful result/unload. The already-existing
pinned SDK `/nix/store/nvwxl97fj19gvy9bnvr8s485jpn5hjmm-pi-1.5.2` was supplied only
to those existing synthetic fixtures; no package build or live/native campaign.
Domain/callback log `/tmp/pi-d13-p-domain-callback-quick.log` SHA256
`7382b1729f7092da362dea0e357d51943ba51c3a9e282256eb185c803854ec1f`.
Gofmt/diff checks pass. No hook framework or active hooks; no bypass.

Complete6554→9bf one-commit series `/tmp/pi-d13-p-series.txt`; full diff
`/tmp/pi-d13-p-final.diff` SHA256
`7a4e8ba518a607d0117f29de8582b36f1f307364c16ffb4ebf2f963dbb6c3df8`.
No migrations, pin update, history rewrite or provider/browser/downstream edit.
Lead supplied and accepted final prose; all30s/Unknown/legacy/recovery warnings
remain. This prospective portal prevention supports existing unheld sessions
through the unchanged normal-result interface. It does not restore an already
held supervisor. No live peer/runtime mutation, replay, hold reset, upgrade,
publication, default write, claim, deployment or lifecycle action occurred.
Packet message`cf20fbc95fab48b7ab63505b1bce92d8` delivered to lead for acceptance
and combined final source/recovery review sequencing. Capacity after acceptance;
R remains architect-owned and unreleased. Session stays open.


### D13-R CLI recovery selectors

Focused normal commit `26d56e23a475a9bbf160836a26c5a2c531e8c404`, parent
`9bf34aa1963e3ba226ec678237cee3dacb2e7a25`, tree
`3c1086168fdd470028e721dff16710b21d748752`, only
`portal/cmd/workspace-portal/pi_runtime_upgrade.go` and its existing test file,
226+/28-. Parser-only scope; no new help path or product docs. The command accepts
mutually exclusive recover-team-conflict + member, preserving exact lower UUID
or compact32 original ID, ordinary request UUID, generation, private socket and
Origin. Request uses recoverTeamConflict/member. Ready requires exact disposition
recovered-team-conflict and TeamMessageID, with no legacy input echoes. Unfinished
preparing/starting replies have no completion fields and retain the same-request
reconciliation error. Ordinary and retirement replies reject TeamMessageID.
Strict unknown/trailing JSON and one-request/no-redirect behavior remain intact.

After I0's settled public type/parser compile checkpoint and explicit source/
first-index handoff, declared Nix gofmt and focused command passed:
`GOWORK=off TMPDIR=/tmp go -C portal test -mod=readonly ./cmd/workspace-portal -run '^TestPiRuntimeUpgradeCLI' -count=1 -timeout=45s`, package 0.160s.
Tests extend actual Unix mock-HTTP cases for exact UUID/compact selector, sender,
ready/pending/starting replies, wrong/normalized IDs, legacy echoes, unexpected
fields/trailing data, malformed responses, scope/generation/request mismatches,
mutually exclusive/missing/duplicate flags, request UUID-only, socket permissions
and Origin guards. Invalid selector cases prove zero HTTP requests; all valid
attempts prove one request. No native or real operator/runtime action occurred.

Raw `/tmp/pi-message-delivery-D13-R-CLI-quick.log`, commit/message files and
preserved-core.json retain evidence. Ordinary commit joined, CLI paths clean and
index empty; all three I0 unstaged core files' SHA256 bytes matched before/after.
Explicit source-freeze/index release delivered directly to I0 and lead. I0 owns
core continuation/index; no further own mutations/checks/publication. The passing
compile included I0's uncommitted stable public type/parser checkpoint; CLI commit
alone depends on those forthcoming core fields, and whole-series acceptance waits
for I0's complete core commit and lead review. No migration, provider/pin/docs
change, live input/upgrade/hold/retry/Stop/service/lifecycle effect or CI/build
campaign. Saved roster and exact bound identity verified; capacity reported.


### D13-R final committed recovery package and prepared verification (I0)

Final runtime `813817fcc4244a5025d001c3d22c21530f480494`, tree
`2416486568a575cbc940264966f35ccb106122fd`, directly follows unchanged prevention
`9bf34aa1963e3ba226ec678237cee3dacb2e7a25`; merged base
`65544340f94ebb112872743738f84c1a7022b06a` remains an ancestor. The complete review
range is 655..813 (P + one coherent R commit); R is 9bf..813. All source/index
operations and check clients joined; runtime worktree and index are clean.
Publication remains held. Provider, workspace/configuration pins, deployment,
claims and live sessions were not changed.

R implements the original-ID team-conflict selector, finite native-origin/domain
proof, exact predecessor Stop/drain journal, retained-empty creating projection,
strict CLI and selected-package reader capability. Completed and lost-final-reply
recovery after later input uses positive publication and original history-prefix
proof; it does not attach, Load, clear a later hold or republish. Unknown effects
retain refusal. The only new persistent format is this private operation journal,
fenced by exact `piTeamConflictRecovery: 1`; no migration or old-journal rewrite.
Old input-retirement codec and privileged `libexec/workspace-pi-host` are unchanged.
The only new capability descriptor field is in
`portal/internal/session/runtime-contract.json`, installed as
`share/workspace-portal/runtime-contract.json` by nix/workspace-portal.nix462.
The privileged helper reads the separate `share/dev-workspace/pi-runtime.json`
(libexec/workspace-pi-host168); R changes neither that manifest builder nor the
worker/protocol sources or installed helper protocol. No system update or actual
privileged-host execution was performed or claimed.

History provenance: CLI26d and core43c3 are retained at
`backup/pi-d13-r-cli-26d56e23` and
`backup/pi-d13-r-preconsolidation-43c3deee` (core tree806b706d). Their initial
consolidation230872 had that exact tree. The necessary catalog preparation was
retained at `backup/pi-d13-r-final-preconsolidation` (e88810d4/tree8957cac6).
The final original-selection preparation was normally committed as750bf00d and
retained at `backup/pi-d13-r-retained-selection-preconsolidation`; autosquash
produced813 with EXACT tree equality to750bf (diff exit0). Only five fixture files
differ fb499..813: P2 central seed, R temporary worker, R integration test, P6 test
helper and owning web exporter. Every production/core/doc byte is unchanged in
that follow-up. CLI paths equal26d. Neither merged655 nor P9bf was rewritten;
obsolete CLI26d is provenance, not a claimed final ancestor. Full diff/range-diff
artifacts below cover final history; no obsolete final fixup remains.

Focused checks passed in the declared Nix environment with `GOWORK=off`,
`GOFLAGS=-mod=readonly`, `TMPDIR=/tmp`, pinned Pi path only for the finite
old-protocol in-process fake (no SDK worker launched). Literal main Go selection:
`go -C portal test -mod=readonly ./internal/web ./internal/session ./internal/piplan ./internal/piruntime ./cmd/workspace-portal -run "Test(PiTeamConflict|TeamConflict|PiRuntimeUpgradeRoute|PublicationsRetain|PiRuntimeUpgradeCLI|PiWorkflowPreflight|UpgradeProofCannotBeFabricated|ReadMemberAdmissionOnlyUsesOriginalRecords|InspectRetainedConversations|CurrentRuntimeReader)" -count=1 -timeout=45s`.
Web3.595s/session0.018s/piplan0.088s/piruntime13.766s/CLI0.593s passed. Final required
post-read slots/runtime identity recheck passed the affected
`go -C portal test -mod=readonly ./internal/piruntime -run '^TestTeamConflict' -count=1 -timeout=45s`
in12.852s. This covers faithful finite old-op admission/refusals, shared read
capture, all required interruption boundaries, lost Stop/final replies, original
receipt/history preservation, marker/source/retained-inventory guards, later input
and independent hold, publication-read error and changed-prefix refusal.
`ruby test/workspace_session_backends_test.rb --name /team_conflict_recovery/`
passed1run/9assertions; Ruby syntax passed both changed helper files. Earlier P
checks remain scoped to their unchanged product paths.

The exact retained g7 provider catalog is not synthetic. A native-free setup
caught the central helper's inapplicable p3 selection before any native launch.
The final fixture now loads the original `piproviders.LoadInstalled` catalog and
FULL Default chain/budget/categories, projects account bindings with the owning
codec BEFORE Ensure, and freezes every member through FreezePiCreationSelection.
Only nil/empty-array representation uses the existing copyPiSelection convention;
no catalog bytes/digest or selection semantics are replaced. The same exporter
has explicit lead_reviewed mode with original model/high and exactly reviewer0,
read_only; solo defaults remain. The temporary worker registers exact native
provider/model identities as faux, asserts provider/model/API routing, rejects
non-faux inference, blocks fetch and uses only temporary auth. No production
provider catalog, worker or admission predicate was changed.

Native-free final preparation: owning exporter with
`PI_CENTRAL_CATALOG_MODE=lead_reviewed PI_CENTRAL_APP_ROOT=<retained-g7-output> PI_CENTRAL_CATALOG_FIXTURE=/tmp/pi-d13-r-native/catalog.json`
passed0.058s. The literal focused selector
`go -C portal test -mod=readonly -tags=pi_native_fixture ./internal/piruntime -run '^Test(PiTeamConflictRetainedSetup|TeamConflictRetainedWrapperPreparation)$' -count=1 -timeout=45s -v`
passed0.267s (both PASS; old pinned Node executes --check only, no SDK import or
inference). The initial nil-array red log is retained separately; no expensive
run was used to diagnose it. All final tagged fixture source compiles in this
quick. Supplied final docs and replay-health addendum are in docs/pi-runtime.md;
existing ordinary/Unknown/30-second/legacy/recovery warnings are preserved.

Prepared ONLY, NOT EXECUTED: `/tmp/pi-d13-r-native/run.sh` takes exactly one
argument, the independently reviewed candidate app output supplied by the lead
after its build. Literal invocation is
`/tmp/pi-d13-r-native/run.sh "$PI_USABILITY_PACKAGE"` with that variable bound to
the exact candidate build receipt. Candidate capability is checked before either
command. No candidate was built by I0. The script has literal runtime CWD, final
HEAD/tree/33-source-file and21-retained-input pre/post hashes, strict exact catalog
hash, full Ruby selector
`nix build --no-link --print-build-logs .#checks.x86_64-linux.ruby-verification`,
then only
`go -C portal test -mod=readonly -tags=pi_native_fixture ./internal/piruntime -run '^TestPiTeamConflictRetainedWorkerRecovery$' -count=1 -timeout=3m -v`
inside the declared Nix shell. It rejects skip-as-green and records original
command/pre/post/Ruby/native/final exits and elapsed seconds. Raw paths are
`/tmp/pi-d13-r-native/{run.log,run.result,ruby.log,native.log}`; run.log/run.result
do not exist at preparation completion. No watcher or background effect remains.
Lead owns final review, candidate build and the ONE accepted Ruby/native batch.

Fixture proof boundary: retained Node
`/nix/store/gf597zf0ysgbngwb92baxgxjd02px6jh-nodejs-22.23.2/bin/node`, SDK
`/nix/store/nvwxl97fj19gvy9bnvr8s485jpn5hjmm-pi-1.5.2` and production worker graph
`/nix/store/y3a1wlsbp8gj3j5raq7b9nm806a4fpvc-dev-workspace-pi-worker/libexec/pi-runtime`
come from original g7 metadata; manifest freezes their exact inputs/hashes.
The in-process predecessor's seven RPC-owning Go sources (supervisor,
conversation, callbacks, callback_types, workflow_observation, worker, protocol)
and four immutable team sources (roster, initial_assignment, addition, removal)
are byte-equivalent e61..813, asserted while producing the manifest. This is not
an executed old supervisor binary or systemd host; host terminal/drain remains
synthetic, with actual shared fixture-worker exit at the existing fake host seam.
The integration source asserts recovered public page/activity, fresh selection
and collection canEnqueue, retained IDs/reservation/history/receipts, one later
input once, then the same recovery UUID again without repeated effects. Actual
execution is pending independent review. No real held session has been recovered,
no original assignment resent, and no live eligibility/operation approval is
implied.

Artifacts:
- `/tmp/pi-d13-r-final-quick.log` — SHA256 `21e4a49ba45e25971b12f6438bbd5c3558207dc77cd02fb4aa82452f4d746c9c`.
- `/tmp/pi-d13-r-final-ruby.log` — SHA256 `1cba2816ce9ea79705d19802a452f86bb306fa1357ede0a443e229b856ae88df`.
- `/tmp/pi-d13-r-final-static-recheck.log` — SHA256 `1a722d3e25df06c27d3121455a6126ab4d35ba06a899c4a36088288623f580fe`.
- `/tmp/pi-d13-r-native/original-catalog-export.log` — SHA256 `21d2c54bf0f790c484605e1db77329d3fc84c99f5899e4d10484c5963964a425`.
- `/tmp/pi-d13-r-native/original-setup-final.log` — SHA256 `0db7457df29aa909e085a4bf524a66dbd3d50460035698d84eab9109a67ad18c`.
- `/tmp/pi-d13-r-native/run.sh` — SHA256 `f67ce24beba21c3e63b37afe1938c2fceabbc0aa3f52bb64f2ca8e7cd3ff2206`.
- `/tmp/pi-d13-r-native/manifest.json` — SHA256 `affad42cf53366bddd676f0b3df02952fb4baa56baf733ea8037ce33c21dd75a`.
- `/tmp/pi-d13-r-native/catalog.json` — SHA256 `ae8f48f8f11075db5a907b5347c76c0eeb349bc65a4f0995f92b05181e4ba094`.
- `/tmp/pi-d13-r-full.diff` — SHA256 `1929eeefbc666f677eb6e2136af3111aa372e5776099726c84872fca70238005`.
- `/tmp/pi-d13-r-range-diff.txt` — SHA256 `1286822e466cdf11a4ff5543fc8d12ea33ffd3bef5081464ba6323d1e7590927`.


### D13-R review remediation — final5d6b04 (R-D13-1 / R-D13-2)

The final committed recovery head is
`5d6b04d501c18fe0fc8b999df58dd54afc6f33e6`, tree
`92628ba98881691af02cf3919468cdd0d88cd1f0`, directly above unchanged prevention
`9bf34aa1963e3ba226ec678237cee3dacb2e7a25` and merged base
`65544340f94ebb112872743738f84c1a7022b06a`. Complete series remains two commits:
P9bf and ONE coherent R5d. No migrations, external pin stream or merged-history
rewrite. Reviewed813 remains at `backup/pi-d13-r-reviewed-813`; normal fixup
`9e73d593e5e3c93189b6e9b8ac805bd10e2d808b` is retained at
`backup/pi-d13-r-review-fixes-preconsolidation`. Its tree equals final5d exactly
after ordinary autosquash. Earlier backups and receipts remain intact.

The exact813..5d delta is four paths,371 insertions/5 deletions: owning recovery
source/test, `piruntime/successor.go`, and five supplied lines in
`docs/pi-runtime.md`. R1 requires every mapped creating owner to pass the existing
positively empty predicate before reservation/Stop. The new regression has valid
persisted two-entry history and a positively verified original Accepted initial
receipt while its slot remains creating; it refuses with no reservation or data/
host/publication effects. The old813 code fails this genuine fixture.

R2 uses the existing pure successor constructor once and admits that SAME candidate
before current-pointer publication or retention. The prepared and largest terminal/
complete journal encodings, including writePrivate's newline, must fit1MiB.
A valid per-record capture exceeding the aggregate bound now refuses with unchanged
current runtime/records/retention and zero Stop/start/publication. Old813 red changed
the current request and retained both packages before failing serialization.
The near-limit regression proves the admitted candidate is the published candidate
and its longest normalized complete receipt fits. An unused128KiB drain extension
is omitted, while changed required host identity or missing required proof refuses.
Optional drain invocation evidence remains optional and is never manufactured.

Every saved schema1 phase now requires identity-only SourceHost, joined to the
original runtime's launch/digest/unit/boot/invocation/cgroup. Full returned Stop
receipt validates before identity comparison and normalization; existing terminal
and physical-drain validators remain mandatory. Missing/null/invalid SourceHost
refuses in both recovery and retained inventory without mutation. There is no nil
adoption/enrichment or old813 reader/rollback compatibility claim. No supported
external R journals predate this unreleased package. Journal-ABSENT after current-
code reservation still reconstructs under full original proofs using its exact
saved candidate/UUID, with size admission and required fence before the first
journal and any Stop. Completed replay remains observational. The released input-
recovery formats, P and merged655 are unchanged.

Final focused quick (declared Nix environment, original SDK, GOWORK=off,
GOFLAGS=-mod=readonly,TMPDIR=/tmp):

```sh
go -C portal test -mod=readonly ./internal/piruntime \
  -run '^Test(TeamConflict|ExplicitSuccessor|UpgradeReservation|UpgradePredecessor)' \
  -count=1 -timeout=60s -v
```

PASS32.360s, exit0. Includes original old-protocol refusals, all12 interruption
checkpoints (including reservation-before-journal and lost Stop reply), later-input/
independent-hold completion replay, both review regressions, required-identity
refusal in all three phases, and affected ordinary successor/upgrade checks.
Formatting/diff checks pass; normal commit hooks were preserved (no declared hook
framework). Rebase changed history only; exact final-tree equality preserves this
quick's source identity. No long check, build, native run, publication or live
runtime action was performed. All command clients joined; source/index are clean
and released for lead's targeted independent R2 follow-up. R1 is a narrow direct
remediation. Package findings ownership remains I0; publication is held.

The existing postreview command remains PREPARED ONLY:
`/tmp/pi-d13-r-native/run.sh "$PI_USABILITY_PACKAGE"`, where lead supplies the
exact reviewed candidate package. It runs full Ruby once, then only the retained
recovery fixture with3m Go timeout. Script bytes/catalog are unchanged. Manifest
now binds final5d/tree926 and34 source hashes (adds successor.go) plus21 immutable
inputs. Original813 manifest/script/catalog are preserved under
`/tmp/pi-d13-r-native/reviewed813/`. All seven old-side RPC source files and four
immutable team files remain byte-equal e61..5d; retained Node/SDK/worker paths and
fixture limitations from the prior appendix are unchanged. This is an in-process
source-equivalent predecessor with retained worker inputs and synthetic host Stop/
drain, not an old supervisor binary/systemd host execution. No run.log/run.result
exists. No real held session has been recovered.

| Raw artifact | SHA256 |
| --- | --- |
| `/tmp/pi-d13-r-r1-red.log` | `873bd5c7bcc66b671da2846cc3429f22194e49270fb02a6853a1991319151bfe` |
| `/tmp/pi-d13-r-r2-red.log` | `d097b1637c041c9165dfab0dc96b4bca0afc061785ebffc94307dfc11498eac9` |
| `/tmp/pi-d13-r-r1-r2-final-green.log` | `13ec1cc24f7d552cf2f0e00fbdffa5d93cb7493452d41b7eca6de5c344cd4ebd` |
| `/tmp/pi-d13-r-review-fixes-history.json` | `3504fc3e219df14e1b15128283100a9b2d46263d99bc027e917f1053a9189c2a` |
| `/tmp/pi-d13-r-review-fixes.diff` | `304246802cc5142679ad4ffa3f44e977e1c1f71e9ac276544ef0450b75ab1a31` |
| `/tmp/pi-d13-r-review-fixes-range-diff.txt` | `07ca4a8cfdbf2fbc6711e5e88a075cba8d9f109d23f81470c93aeeda6ecc9b31` |
| `/tmp/pi-d13-r-full-final.diff` | `0a651136a4e7294f5fa3764227f2911a1ce62994d20665bb00516f0c5d8d5e2c` |
| `/tmp/pi-d13-r-native/run.sh` | `f67ce24beba21c3e63b37afe1938c2fceabbc0aa3f52bb64f2ca8e7cd3ff2206` |
| `/tmp/pi-d13-r-native/manifest.json` | `fd959ef57c865932e2fb283e3a3de9502ab9b62c6121e19d9af784a6d1879e62` |
| `/tmp/pi-d13-r-native/catalog.json` | `ae8f48f8f11075db5a907b5347c76c0eeb349bc65a4f0995f92b05181e4ba094` |


### D13-R reviewed final5d feature publication

Lead accepted R1 direct remediation and the independent affected-lane R2 follow-up
without new findings at exact final5d/tree926, then released this publication.
Ordinary NONFORCE SSH push to `git@github.com:aither64/dev-workspace.git`, feature
`refs/heads/2026-11-23-pi-message-delivery`, advanced65544340 to
`5d6b04d501c18fe0fc8b999df58dd54afc6f33e6` and joined exit0. Fresh direct remote
reads before/after prove exact feature equality and unchanged remote default
`refs/heads/master` plus symbolic HEAD at
`65544340f94ebb112872743738f84c1a7022b06a`. No rebase/amend/source/index mutation
occurred; local HEAD/tree926 stayed frozen and clean. No default write or live
operation by I0. Publication receipt `/tmp/pi-d13-r-publication.json`, SHA256
`790b7830b238180d51b33b756c1596e1a0aa2b6019964d3fed3cb6c3342cc249`.

The final independently REVIEWED/PUBLISHED dependency was delivered directly to
parked I1 under its already assigned downstream package: stable message
`7800c6a532804dd19a9b1162cb3afee6`, client joined exit0. Root owns required longer
verification/build/deployment sequencing; this handoff does not authorize any
live recovery. Current R findings ownership remains with I0.

One bounded exact-head CI run/jobs listing (no watch, wait, rerun or cancel):
Check, `.github/workflows/check.yml`, workflow354263807, run45606148620, attempt1,
head5d6b04d501c18fe0fc8b999df58dd54afc6f33e6, initially in_progress/no conclusion.
https://github.com/aither64/dev-workspace/actions/runs/45606148620

- Job `Essential application contracts` (139177396636): in_progress, conclusion None.
- Job `Session creation smoke` (139177397251): in_progress, conclusion None.
- Job `Extended Ruby and package composition` (139177399164): completed, conclusion skipped.
- Job `Extended host lifecycle` (139177399235): completed, conclusion skipped.
- Job `Extended session archive/recovery` (139177399817): completed, conclusion skipped.

Raw listing: `/tmp/pi-d13-r-ci-runs.json` SHA256 `a451c3e56c234eefae1f325dfd3eee6b959aaec6debb00d448db47199333fbd3`; jobs `/tmp/pi-d13-r-ci-jobs.json` SHA256 `94d258e423bfac72eed127a256e6dc2a21cd24e37c7e816cde037340c8b29d86`. All publication/messaging/listing clients joined; source/index released clean and frozen. No I0 verification campaign was launched.


### D13-D final recovery runtime follow-up pins

Complete/released workspace `113fae6d1bb46a750e3fcf971b466b9df4c7bd1a`, parent
fresh shared local master `a755bfa7f2fd1ab010e7dd719f581d35e15fde4d`, tree
`175da44642713bddc38444f9d4b258ac4fed9e1c`, only two flakes 5+/5-.
Configuration `3cae39470781184f498eadc1e12639c6af616a1c`, parent merged/fresh
default `d5055ec0b2ea22de976f6703208f5526c3e185ca`, tree
`5267fc1205b1186e7d6322e023e34be7ef72244b`, generated lock only 3+/3-.
Both are NEW normal follow-up commits; merged09ea/d505 remain ancestors. There
is one new pin per stream, no intermediate pin, merged-history rewrite or migration.
Ordinary nonforce canonical SSH feature pushes joined and fresh feature equality
passed. Defaults remain d433/d505, shared master remains a755; unrelated records
and index untouched. Both feature trees/indices clean; all own effects joined.
No runtime/provider/CLI/core source edit, CI watcher, app/system build, default
write, claim, merge, deployment, live/native/operator/Stop or lifecycle action.

The final independently reviewed/published dependency was checked directly:
`5d6b04d501c18fe0fc8b999df58dd54afc6f33e6`, actual NAR
`sha256-TjO+YS5IrsexXYl8O9b4P52PiCa1uBBPHusy0SPTKFw=`. Publication receipt
SHA256790b7830b238180d51b33b756c1596e1a0aa2b6019964d3fed3cb6c3342cc249
matches the owning I0 packet. Full 38/67 direct-path graphs plus every follows
edge against fresh bases change ONLY runtime identity/NAR. Provider2547 and its
NAR rLBe remain unchanged; complete selected runtime subgraph matches the committed
source. All extension/native/SDK/Node/catalog/model/team/claim/policy inputs and
edges are preserved. Existing cross-lock/site and complete locked runtime/provider
identity equality pass. Workspace declared Nix parse/Ruby deployment contract
passes4/19 in1.370550s; diff checks pass. Config ordinary exact confctl set --commit
runs Nixfmt and message hooks successfully, keeping generated655->5d two-commit
changelog and width warnings. JSON/Nix parse/full graph/diff pass; no manual lock
or generated-message edit or hook bypass.

Fresh baseline preserves the later accepted d433 team/site instructions and catalog
behavior selected in qgza; additional d433->a755 is archive/tracking records ONLY.
No product/flake/input delta beyond that accepted baseline. No regression to old
historical6n59 metadata is claimed. Seven privileged host/helper/session-entry/
Codex-wrapper source files, worker/SDK builder source and runtime flake/lock bytes
are unchanged655->5d. The application DOES add expected piTeamConflictRecovery
marker1 plus workspace-host admission guard and recovery inventory/journal support;
this is not an all-metadata equivalence claim. Existing host dependency boundary
reuses without native/system upgrade or evaluation campaign. An initial read-only
check named a nonexistent pi-runtime/package.json, stopped with no edits/effects,
and was corrected to actual worker source/SDK builder paths and complete lock.

Existing clean detached runtime target at655 is prepared for5d; configuration target
atd505 for3cae; provider2547 is already integrated and has no new merge. Config
frozen-bundle/Nix environment and actual precommit/postmerge trust readiness passed
in this package's preparatory phase. D13-only integration-targets/history JSON and
literal commands in /tmp preserve earlier D11/D12 receipts. Commands enter declared
environments before any later lead-owned short claims; shared workspace stays
master with its nonblocking tracking lock and unrelated files/index preserved.
No integration or recovery command was executed. Raw `/tmp/pi-message-delivery-D13-`
logs retain baseline proof, host-boundary, runtime publication/target lock,
workspace base/pin/quick/commit/push, config pin/quick/generated-message/push,
cross-lock and target/hook preparation. Lead owns mechanical acceptance, required
Ruby/native/CI/composed verification, deployment and separately approved recovery.


### D13-R actual seed correction — final878

Root's first actual native attempt at published5d failed before native owner
creation: line220, “Pi creation team disagrees with reserved identities”,0.110s.
The recovery entry supplied only TWO variadic settings flags; the conflict path
requires THREE. It therefore took the ordinary synthetic p3-model selection path
against the actual exported gpt-6.1-sol/high catalog. This failed before candidate
loading. The separate postcheck failed because generic pn candidate was collected
during the757-second Ruby/native batch. Root owns candidate retention; no missing
candidate was treated as evidence of a successful preparation.

Two fixture paths only now share `teamConflictSeed(t,prepareOnly)`, with all three
flags in that wrapper once. The ordinary centralNativeSeedWithUpgrade entry
forwards prepareOnly=false unchanged. Preparation follows the ACTUAL constructor,
loads original and current package catalogs, validates the original frozen intent,
then returns its actual fixture/intent/team/current-catalog tuple before target
profile/server/attachment/Create/Send. It does not reconstruct a parallel intent.
The existing in-process fake Ensure is disclosed; no Node worker/inference or
systemd/native host runs. Existing assertions check original complete chain/account
selection and the exact lead/reviewer0 team, plus no member-owner directory and
zero successor starts/Stops. The old2-flag wrapper reproduced EXACT220 failure in
this quick0.128s; corrected3 flags pass0.137s on the SAME inputs. An intermediate
assertion expected1 but the upgrade counter starts0 after base Ensure; final test
correctly asserts0/0. No native retry was used to diagnose setup.

Inputs were retained original g7, SDKnvw, exported catalog ae8f48f8f11075db5a907b5347c76c0eeb349bc65a4f0995f92b05181e4ba094,
and root-retained composed HNQ preparation package. Native-free command, from the
runtime worktree's declared Nix shell with GOWORK=off/GOFLAGS=-mod=readonly and the
same PI_CENTRAL_APP_ROOT/PI_PROBE_PACKAGE/PI_CENTRAL_CATALOG_FIXTURE values:

```sh
PI_USABILITY_PACKAGE=/nix/store/hnqjj1nq0f5fz4qrphkyf7qk10b5lxwc-dev-workspace-0.2.0 \
  go -C portal test -mod=readonly -tags=pi_native_fixture ./internal/piruntime \
  -run '^TestPiTeamConflictRetainedSetup$' -count=1 -timeout=30s -v
```

Final coherent R is87835ef85e7cdc81254ba47aff888445d87a66bd, tree
c119c768bf3d2f76eea4b23f9fd55c58fe47512e, directly above unchangedP9bf. EXACT
published5d..878 delta is two fixture files39+/22-; product/core/guard/wire/docs/
pins and migrations have ZERO change. Normal fixup97453affddf8f4827b5a388822c3481b7f7d4ab7
is retained at backup/pi-d13-r-seed-fix-preconsolidation; its tree equals final878.
Published5d remains at backup/pi-d13-r-published-5d6b04. Whole series remains P+ONE R;
merged655/P were not rewritten. Root directly accepted this narrow correction
within the independently reviewed fixture contract; no new review campaign.

Final committed Ruby derivation EXACTLY equals the passed root run:
/nix/store/3vds79w6w6xpk16p2gj0wg5hi3g021x3-dev-workspace-ruby-verification.drv,
output /nix/store/9971w2d8k3ghd77g8kgz8m17c00kr607-dev-workspace-ruby-verification.
Root has retained that output; reuse is justified by exact derivation/input/output
identity, not source resemblance. No full Ruby rerun by I0. The two portal test
files are outside rubySource's owning filter. The final evaluation receipt is
/tmp/pi-d13-r-seed-final-ruby-paths.json.

Root released exact-lease feature publication. CanonicalSSH push878 joined exit0
with --force-with-lease=refs/heads/2026-11-23-pi-message-delivery:5d6b04d501c18fe0fc8b999df58dd54afc6f33e6.
Fresh direct remote reads prove feature878 and unchanged master/HEAD65544340 before/
after. Source/index/HEAD remain clean and frozen. ROOT-ACCEPTED/PUBLISHED exact878
+NAR dependency supplement delivered I1 message04dc42530cfd43848adb640a69cd845b,
client joinedexit0. No default/deploy/live operation by I0.

One bounded branch/exact-head CI listing found Check workflow354263807,
.github/workflows/check.yml, run45610165292 attempt1, exact878, in_progress;
https://github.com/aither64/dev-workspace/actions/runs/45610165292 . No obsolete
active ownbranch run exists in the bounded listing; nothing was canceled. Jobs:

- Essential application contracts (139191302959): in_progress, conclusion None.
- Session creation smoke (139191303504): in_progress, conclusion None.
- Extended session archive/recovery (139191305717): completed, conclusion skipped.
- Extended host lifecycle (139191305953): completed, conclusion skipped.
- Extended Ruby and package composition (139191306374): completed, conclusion skipped.

Prepared ONLY native-only literal argv:
`/tmp/pi-d13-r-native/run-native.sh "$PI_USABILITY_PACKAGE"`. Root supplies its
FINAL newly composed deployment output after I1 final pins/build; HNQ is only
preparation evidence. The script runs only TestPiTeamConflictRetainedWorkerRecovery
with3m Go timeout and preserves original command/pre/post/elapsed/final status in
native-only.result plus distinct native-only.log/native-only-run.log. Skip cannot
count as success. Manifest binds878/treec119,34 source/26 immutable-input hashes,
original production worker graph, exact passed Ruby identity and HNQ preparation
metadata. Old-side seven RPC sources/four immutable team sources still equal e61;
synthetic host/drain limitation remains. Root owns execution and final candidate
identity; no actual native-only output exists at handoff.

Original5d actual native.log/run.log/ruby.log/run.result/run.sh/manifest/catalog
are byte-preserved under /tmp/pi-d13-r-native/prior-run-5d/; original actual logs/
result remain at their earlier paths too. No failure evidence was overwritten.
All I0 command/messaging/check/evaluation/publication/listing clients joined;
source/index released clean+frozen, current R findings ownership retained.

| Artifact | SHA256 |
| --- | --- |
| `/tmp/pi-d13-r-seed-red.log` | `b72973b17d672f46917390c5794bdfb344c3594da9607ef96a86c1ca41d5e1ea` |
| `/tmp/pi-d13-r-seed-final-green.log` | `f2bcd9ed9b8d41bfa251422411e5c27342aa83242b2edf1b0291bb09407b11b8` |
| `/tmp/pi-d13-r-seed-history.json` | `5a08f09a11aaa20e5b136a10f1dbecaa1736330ef6d75369a88e2b8457564d9a` |
| `/tmp/pi-d13-r-seed.diff` | `58330fb66e84c2a8b532e4e260399fcf5652b831b0447bfa769f40c8167f4438` |
| `/tmp/pi-d13-r-seed-range-diff.txt` | `051c00ec52a9dbee370e58ca98fa77d7a7768b0bb4527070b4287a10641305ec` |
| `/tmp/pi-d13-r-878-full.diff` | `ff1b017ad0e7c4fb1d915b316057c3b6ee2783ef47587ac16e30aa8359cfa421` |
| `/tmp/pi-d13-r-seed-final-ruby-paths.json` | `bc6effc89887260362104199a283ed17155778dc1179595b1ed115825b374df0` |
| `/tmp/pi-d13-r-seed-publication.json` | `bccd8a24c10a0a9cd6ebc4672d7936dd1902c2bebb8c3fb9919f9771ed04bc12` |
| `/tmp/pi-d13-r-seed-ci-runs.json` | `d3325516bbd54f63e4a3af07a67330e26e3e2f5d87e88953c6ae53ac08ecbaa7` |
| `/tmp/pi-d13-r-seed-ci-jobs.json` | `2776bb341a505234fb8d3a4f481b5c0b6b6c675f41369456af7416a614471f68` |
| `/tmp/pi-d13-r-native/run-native.sh` | `fef82b38ab96f16a56bdda8a357dcfe6d1c612d6ed77712eb3e8ac71c17ba66b` |
| `/tmp/pi-d13-r-native/manifest.json` | `1d12e6503ed90220523d3cb1eadd7d19d7461418e7980e8fc145f35d85307d33` |


### D13-D final two-fixture correction pin supplement

Final/released workspace `a1c5f613e85fe4e50a17fbce7dfafe07fd3cf385`, parent
accepted fresh `a755bfa7f2fd1ab010e7dd719f581d35e15fde4d`, tree
`19f8a11db1278bb0005604bc3373cf7994b36a5d`, two flakes 5+/5-.
Final configuration `d0ef67887f70b660416d09f4e1fa2e3e23de5f91`, parent protected
merged `d5055ec0b2ea22de976f6703208f5526c3e185ca`, tree
`3f1a5c82cfde03c5839d45f32e75031aa7774104`, generated lock 3+/3-.
Only the UNMERGED113/3cae pin streams were consolidated by normal amend/ordinary
empty-range rebase plus confctl regeneration. One final pin per source; obsolete
pin heads are not ancestors. Merged09ea/d505 history remains unchanged. Old113/
3cae retained in backup refs and 5d in backup/pi-d13-r-published-5d6b04; exact old/
new ranges are in D13-final range-diff logs/history JSON. No migrations. Explicit
expected-old SSH leases passed, fresh feature equality passed, defaults remain
d433/d505 and shared mastera755 unchanged. Both feature trees/indices clean;
all clients joined/source-index windows released.

Runtime exact root-accepted/published `87835ef85e7cdc81254ba47aff888445d87a66bd`,
NAR `sha256-6Otulu3vNrcoD2FeLH0CpHaE4NX3WAnylL+ZUs2xo9A=`. Publication receipt
SHA256bccd8a24c10a0a9cd6ebc4672d7936dd1902c2bebb8c3fb9919f9771ed04bc12
and direct remote equality verified before mutation. Full38/67 path+follows
comparisons against accepted113/3cae change ONLY runtime identity/lastModified/NAR;
provider2547 and every other input/edge stay identical. Complete committed target
subgraph, locked runtime/provider equality and existing cross-lock/site checker
pass. Existing declared Ruby deployment quick passes4/19 in1.285775s plus parse/
diff; config normal Nixfmt/message hooks pass, generated655->878 two-commit
changelog and width warnings preserved, JSON/Nix parse/graph/diff pass.

Exact5d->878 diff contains only the two accepted integration fixture corrections.
Product/core/guard/wire/docs, flake inputs, marker1/recovery inventory, host helpers,
worker/SDK/native and all policies are byte-identical to the earlier accepted
candidate. This does not erase expected D13 application contract changes versus
D12. The later accepted site/team baseline remains intact. No application/system/
native build or full Ruby rerun was performed here; root owns the final composed
app/native-only attempt and exact full-Ruby derivation/input reuse proof. Prior
5d/HNQ preparation remains historical provenance, not final deployment proof.

Refreshed D13-final integration target/history/command receipts use clean detached
runtime655->878 and configurationd505->d0ef, provider2547 already integrated, shared
mastera755->a1c5. Existing hook readiness reused unchanged. All declared environments
are prepared outside any later lead-owned short claim; no merge/default push,
claim, deployment, operator/live/native/peer/CI watcher or lifecycle action ran.
Raw `/tmp/pi-message-delivery-D13-final-*` logs retain publication/source equivalence,
workspace pin/quick/commit/range-diff/push, config pin/quick/generated-message/
range-diff/push, cross-lock and integration receipts. Earlier D11/D12/D13 proof
files remain intact. Lead owns final mechanical acceptance/artifact verification,
authorized deployment and later integration/recovery decisions.


### D13-R asynchronous trigger receipt — frozen c93

The second root-owned full native attempt on878/rooted appirz returned valid
Pending+nil at the trigger Send, then the fixture failed its immediate Accepted
assertion (Go4.970s;pre0/native1/post0/final1,9s). Owning input_delivery_v1 returns
Pending after positive same-process enqueue ACK and writes the exact Accepted
receipt asynchronously. It never promises immediate acceptance. Background
portal diagnostics were printed at cleanup; their individual event timing/cause
is unclassified and not used as proof of the input outcome.

The narrow correction changes ONE existing fixture file23+/2-. It submits the
original trigger once, accepts initial Pending/Accepted only, then uses existing
bounded centralWait plus read-only Manager.Lookup. Exact conversation/original
ID/send action/SubmissionDigest covers original message, pi-delivery-v1:steer,
Retry=false and frozen settings. Lookup must match ref/generation/settings/input;
only Accepted with matching native ID, nonempty native entry and exact effective
message digest succeeds. Pending/Unknown keep waiting; mismatch/NotSubmitted/
other states fail, and timeout remains failure. No resend, Retry POST, Load or
new helper/test/diagnostic abstraction. All later held+dropped-once, history,
receipt, capability, domain, empty-owner, recovery and zero-extra-send assertions
remain unchanged. Architect settled the wait contract; root directly inspected
and accepted the correction within the reviewed fixture contract.

Declared Nix quick compiled the native-tagged external test and ran the existing
pure exact-receipt bytes, five crash/no-redispatch checkpoints, invalid witness/
terminal refusal, compact ID and exact spelling tests. PASS0.231s/exit0; no Node,
SDK model or native worker ran. Regex:
`^Test(ReceiptCrashBoundariesNeverRedispatch|ReceiptRejectsInvalidWitnessAndKeepsRefusalTerminal|ReceiptRetains32HexOperationIdentity|OperationIDsKeepExactSpellingAndRejectPaths|RetainedReceiptV1ExactBytesUnchanged)$`,
with -mod=readonly,-tags=pi_native_fixture,-count=1,-timeout=30s.

Final localc93d6894e6d4530dbdb8b1c0a5b8f314912fb818/tree
e345631404f3c624ac1381aeb3cc4d6ef792943f remains P+ONE R above unchangedP9bf.
Normalfixupaab9a3dea5da5ef29375cb4aaaebf79abb26b417 retained at
backup/pi-d13-r-pending-fix-preconsolidation has EXACT final tree after autosquash;
published878 retained backup/pi-d13-r-published-87835e. No migrations or product/
core/guard/wire/docs/pins change. No publication/CI/pin/build refresh until full
exact native case is positive. Root owns next run and final artifact bridge.

Committedc93 Ruby drv/output EXACTLY equal passed3vds/9971 from the prior appendix;
final identity receipt below. No Ruby rerun. The rooted diagnostic candidate is
/nix/store/irz2rkr0fvh2v2gffbjypwj0rnbryja2-dev-workspace-0.2.0, product source878.
Current compiled Go/CLI/Ruby test source is c93; only fixture wait semantics differ.
Manifest hashes consumed package/worker/model/provider/contract metadata and the
retained Node/SDK/worker graph. This is accepted diagnostic-candidate input
coverage, not final packaged-binary execution. Seven old RPC-owning sources and
four immutable team sources still equal e61; synthetic host/drain limits remain.

Prepared-only exact argv:
`/tmp/pi-d13-r-native/run-native.sh /nix/store/irz2rkr0fvh2v2gffbjypwj0rnbryja2-dev-workspace-0.2.0`.
Same full exact selector/3m Go timeout; exactcandidate enforced; status/selfcapture
paths remain native-only.log/native-only.result/native-only-run.log. Manifest
bindsc93/treee345,34source+26actual immutable hashes. HNQ preparation metadata is
retained separately, outside execution prerequisites. Prior878 actual failure
log/result/runlog/script/manifest/catalog are byte-preserved in prior-run-878.
No I0 native execution or real held-session recovery occurred. All I0 clients
joined, source/index clean+frozen/released, findings ownership retained.

| Artifact | SHA256 |
| --- | --- |
| `/tmp/pi-d13-r-pending-quick.log` | `2d16bbe0c28637bd73521f720087848b308bae535489afe0275eee642320818e` |
| `/tmp/pi-d13-r-pending-history.json` | `8efa19143074cde3865bf49f0a536c29f285086f08a8b7df69df562955e3d51c` |
| `/tmp/pi-d13-r-pending.diff` | `2ed4d852d090ac6822360fbb70ba03d02e596e28d6834726fbb399521f59aea9` |
| `/tmp/pi-d13-r-pending-range-diff.txt` | `c7ddf082199e6c7070d28cc3adafedd6712c206fe3a839887f3011c9fc6e0088` |
| `/tmp/pi-d13-r-pending-final-ruby-paths.json` | `bc6effc89887260362104199a283ed17155778dc1179595b1ed115825b374df0` |
| `/tmp/pi-d13-r-native/prior-run-878/native-only.log` | `c3279d75d86a8f1804d0d5f0efd7b859e11f4ce8b0cc1d15adb6b702d02a47c7` |
| `/tmp/pi-d13-r-native/prior-run-878/native-only.result` | `f9b146aa42ff88a77603e6436cde63384178204d27137cbf98404b4c444c56f6` |
| `/tmp/pi-d13-r-native/run-native.sh` | `d602fa315062efeb3fc7b01f9bc8ab1c04c8e81f5fdee50e85e5d1bed45740a6` |
| `/tmp/pi-d13-r-native/manifest.json` | `46b03ef79fcd7dc8e49d3805cd8f386eb5b7600ab54189790a404cbe888018ee` |


### D13-R c93 CLI-build deadline diagnosis

Root's third actual native attempt on unchangedc93/rooted appirz passed the
positive original trigger Accepted+witness and held+dropped-once prefix, then
failed before recovery request/Stop at the ordinary current-source CLI build:
signal:killed, test20.04s/Go20.107s; pre0/native1/post0/final1/elapsed37s.
Actual outputs/script/manifest/catalog are byte-preserved in prior-run-c93 before
any overwrite. This is scoped prefix progress, not full recovery success.

The source chain newP6NativeFixture -> supervisorFixture constructs a20-second
context; f.Context goes directly to exec.CommandContext for `go build` in the
existing case. Outer go test -timeout3m does not extend it. The deadline is a
concrete kill mechanism consistent with20.04s. A bounded kernel journal query
12:20:01..12:22:01UTC found no OOM/out-of-memory/killed-process entries. The test
did not record historical ctx.Err, so do not claim retrospective absolute OOM
exclusion. No wider memory investigation or timeout increase was performed.

Preferred unchanged-source preparation, NOT executed by I0, from the runtime
worktree CWD:

```sh
env GOWORK=off GOFLAGS=-mod=readonly TMPDIR=/tmp \
  /nix/store/i4bv0lvk0gfzllcy2kqgz3iam0aw4c4i-nix-2.34.8/bin/nix develop \
  --command timeout --kill-after=5s 60s go -C portal build -mod=readonly \
  -o /tmp/pi-d13-r-native/workspace-portal-cache-prep ./cmd/workspace-portal \
  > /tmp/pi-d13-r-native/cli-cache-prep.log 2>&1
```

Samec93 ordinary CLI/module flags/Nix Go/default GOCACHE; no native/profile/
fixture/model starts. Estimated compile10-45s (not measured here), hard compile
bound60s plus5s termination grace; any nonzero/timeout stops before native.
Nix environment evaluation precedes this deadline. This warms the build cache;
the test still builds/uses its OWN temporary output. It does not consume this
external binary or substitute installed appirz CLI. Root owns preparation/next
one full native launch; further source/context changes need concrete evidence.

The requested remainder-of-THIS-case read found no other premature async
Accepted assumption. Later input sends message+ID without Delivery. The session
alias forwards unchanged through pinned2547 generic handler, which passes empty
Delivery to the Pi adapter's ordinary synchronous send path. Its HTTP202
expectation remains valid; duplicate original-ID POST and transcriptcount1/
receipt preservation checks stay unchanged. No other same-case async adapter
send remains. Product/core/pins, source/index/HEADc93/treee345 are unchanged;
no own build/native/CI/publication or Ruby rerun. All bounded read clients joined.

| Preserved artifact | SHA256 |
| --- | --- |
| `/tmp/pi-d13-r-native/prior-run-c93/native-only.log` | `488dbd05914bc2316ccbc7d3a22e07a12dd8d3da3f2c5fddf6cd6f81cab1c66b` |
| `/tmp/pi-d13-r-native/prior-run-c93/native-only.result` | `3f6e13176fb3f5abb0d2e9edcbda1ffddd464fcb1ea61e9abe327e92f7462be1` |
| `/tmp/pi-d13-r-c93-kernel-oom-window.log` | `218eff66f0248062e60c9505a8f3162151c544191d8c292cdc99c752f959d594` |


### D13-R shared factory selection — frozen fccf

After successful same-source CLI cache preparation, root's next exactc93/appirz
case passed ACK/witness/held and CLI build, reached recovery, then failed the
fixture beforeStop guard: predecessor lacked sharedHost (Go9.251s,13s total,
pre0/native1/post0/final1). The public CLI EOF followed that fixture fatal;
physical kill/base Stop did not complete. Actual attempt bytes are preserved
under prior-run-c93-cachewarm (not merged with the earlier20s compile failure).

Concrete source cause: newSupervisor chooses its start factory ONCE from the
metadata Protocol at construction. NewP6NativeUpgradeFixture used nonshared
newP6NativeFixture -> Ensure, then the conflict helper patched metadata to2.
That did not replace the already-selected per-conversation factory. No intervening
base.Start/supervisor replacement was found. The correction selects the existing
shared fixture path BEFORE Ensure for conflict recovery only. A thin private
upgrade helper reuses all existing upgrade setup; the ordinary exported entry
still passes false, conflict passes true. Retained/candidate metadata wrappers
are still supplied before first Create. No production supervisor/worker/drain or
protocol change, per-conversation equivalence or new harness.

Before the existing physical kill/base Stop, the guard now binds captured
supervisor.ref to exact original f.Runtime and current host.base.s to that same
pointer. It requires nonnil sharedHost.shared, both retained members' actual
workerProcess.host pointers equal that host (unwrapping the one existing dispatch
counter), loaded original generation/shared topology, and matching actual plus
saved PID/start tuples. Only that exact process is killed/joined. Existing full
manager host terminal/drain and native/domain proofs remain intact.

Consumer trace: shared factory -> startShared serializes one workerHost under
hostMu -> host.attach per exact identity -> init. workerProcess.Call emits bounded
newline JSON schema/id/identity/op/body. Generated retained-faux wrapper imports
original protocol.runWorker and persistence, and loads original pinned SDK. That
runWorker maintains slots by canonical identity, supports multiple distinct init
calls, validates trustedSessionBinding generation/nativeID/callbackSubject, and
keeps replies/HostBridge callbacks identity-bound. The existing fixture's per-slot
ModelRuntime/response/sessionOptions injection does not replace this framing or
initialization loop. No alternate shared entrypoint or newer RPC is required.
Candidate Start sees candidate Protocol2. Actual shared physical proof is enforced
at beforeStop in the next root run; static preparation does not claim execution.

Native-free actual RetainedSetup PASS0.131s; existing generated predecessor/
successor wrapper Node--check plus strict legacy/shared topology-record check
PASS0.235s. Native-tagged code compiles. No SDK/model/native worker run by I0.
Finalfccf765dee02dd2d5d89e863a27dca1cf602225c/tree
102022404f49283a9cb8f64e6a7548987e274d59 is P+ONE R above unchangedP9bf; EXACT
c93..fccf TWO fixture files45+/4-. Normalfixupb5dd56537016d9972e5d9f804099f163ca5a8d5c
retained at backup/pi-d13-r-shared-fix-preconsolidation has exact final tree;
c93 is backup/pi-d13-r-diagnostic-c93; published878/all earlier refs retained.
No migrations/product/core/guard/wire/docs/pins changes.

Committed Ruby drv/output EXACTLY reuse passed3vds/9971; no Ruby rerun. Same
rootedappirz consumed metadata, retained worker/Node/SDK hashes remain unchanged.
Current test/CLI sourcefccf differs from appirzsource878 only in three_test.go
files. Seven old RPC and four immutable team sources still equal e61. This stays
an accepted diagnostic source/input boundary, not final packaged-binary proof.

Prepared-only argv remains:
`/tmp/pi-d13-r-native/run-native.sh /nix/store/irz2rkr0fvh2v2gffbjypwj0rnbryja2-dev-workspace-0.2.0`.
Script bytes unchanged; manifest bindsfccf/tree102,34 source+26 immutable hashes.
Root owns direct inspection and next full native launch. Source/index clean,
frozen/released; all I0 clients joined. Publication/pins/CI/build remain paused.

| Artifact | SHA256 |
| --- | --- |
| `/tmp/pi-d13-r-native/prior-run-c93-cachewarm/native-only.log` | `c988779ebb98e681c9aa1e393364fae93f1aadd3ce5951df7a455bb5993445dc` |
| `/tmp/pi-d13-r-native/prior-run-c93-cachewarm/native-only.result` | `817389e1d01f9253342896cea7304cd0da395f769280b19223f29b50f870976f` |
| `/tmp/pi-d13-r-shared-preparation.log` | `8cce3a11178a6904d4019dc92f774d26e17322f1c573fd409d214363baedf75f` |
| `/tmp/pi-d13-r-shared-static.log` | `311977a9ba2afaf618bc7c286a843e615694da2417589bd11bba0467afb9aa78` |
| `/tmp/pi-d13-r-shared-history.json` | `2d56eb35e23d2df18d8196c8a9a00e85e3722b6349ebddfccbb9b1f17c6b7e9f` |
| `/tmp/pi-d13-r-shared.diff` | `a87bab2cb100cfaf293fd0cf2d146f175c36e9fb4204656ad455f743dbb8353d` |
| `/tmp/pi-d13-r-shared-range-diff.txt` | `e387f213f8f8b950ba47d2fbd8197f0808aea3240c0bcb8bfd906bc4da091211` |
| `/tmp/pi-d13-r-fccf-full.diff` | `d52e8849c6f84b28a570b54094696580e34890b63ab4a0f4a90cd8b1d8d9bedd` |
| `/tmp/pi-d13-r-shared-final-ruby-paths.json` | `bc6effc89887260362104199a283ed17155778dc1179595b1ed115825b374df0` |
| `/tmp/pi-d13-r-native/run-native.sh` | `d602fa315062efeb3fc7b01f9bc8ab1c04c8e81f5fdee50e85e5d1bed45740a6` |
| `/tmp/pi-d13-r-native/manifest.json` | `2d1814f593475d8c1ca02a836e7453c910921cd3fa234257278faf8922468826` |


### D13-R allocated503 diagnostic — empty planned history path

Root released ONE known-short disposable SDK diagnostic, not final verification.
The existing failure path gained bounded HTTP/error/journal/status/mapping and
Stop/start/attachment/ACK/Publish/physical-load-start counters in two_test.go
files only. No production logging/API/harness change; original effects and
assertions were retained. Native-tag compile/no-test check passed0.058s first.
HEAD remainedfccf, with exact diagnostic dirty-source hashes captured separately.
Original rootfccf actual artifacts are byte-preserved in prior-run-fccf.

The one diagnostic used SAME rootedappirz, originalg7/SDKnvw/catalog, declared Nix
GOWORK=off/GOFLAGS=-mod=readonly, exact full-case selector,45s outer Go timeout and
unchanged20s fixture context. It failed at10.726s,13s command elapsed, exit1;
client47472 joined. Postrun all34 diagnostic source and26 immutable-input hashes
match preflight. No retry or confirmatory SDK run was made.

Before cleanup, observed:

- Journal settled; SourceHost and saved normalized terminal Stop join exact source.
- Source Inspect stopped/terminal, successor Inspect ready/running; ctx.Err=nil.
- Starts1,Stops1,physical loadStarts2; creates/sends/configures0.
- Attachments2,ACKs2; Publish calls0/success0.
- Both mappings loaded/heldempty at successor generation; same physical PID/start.
  Lead persisted; reviewer remains unpersisted.
- Manager Upgrade returned resultPhase ready with ErrScope; HTTP503 body remained
  generic ServiceUnavailable. Ready runtime is not published authority.

This places the earliest failure after the second Load and before Publish,
inside upgrade.go's immutable mapping comparison, rather than Stop, shared
factory, terminal/drain or attachment. Source trace identifies the empty-owner
planned history path mismatch: conversation.go supplies EmptyProven and omits
HistoryFile for an unpersisted empty owner; retained session.mjs uses original
SDK SessionManager.create with the SAME native ID. Pinned SDK session-manager.js
newSession always chooses a newDate timestamped filename. Original initialization
and successor Load are seconds apart, so that unsaved filename changes.
conversation.go applyObservedMetadata saves it; sameUpgradeMember unconditionally
requires the original HistoryFile. Other compared identity/instruction/settings/
policy fields remain unchanged through this path. The finite fake retained its
old filename and missed the actual SDK behavior.

Reported consequential decision BEFORE core edits to lead and architect.
Relaxing this comparator alone is insufficient: partial-load mapping/afterimage
fences and completed-replay verifyTeamConflictCompletion also freeze that path.
Any correction must stay scoped to positively proved EMPTY owners, preserving
same native ID/HistoryRef/reservation, absence of original history, persisted
histories/prefixes exactly, all uncertainty fences and aggregate journal bound.
Changing old RPC/worker sources would affect the accepted e61 predecessor source
equivalence and cannot be assumed. No new core/worker edit was made. Architect
clarification message7bdfd459-411d-4c50-abfa-82fbbda33a33 joined; decision pending.

Source/index window retained by I0 for current package; HEADfccf unchanged, index
empty, only two uncommitted diagnostic_test.go changes. Those changes and raw
receipts are preserved below. No publication/CI/pins/build/Ruby/live-peer action.
All diagnostic children/effects/read/messaging clients joined. A confirmatory
focused SDK check remains unused until a proved correction is settled.

| Artifact | SHA256 |
| --- | --- |
| `/tmp/pi-d13-r-503-diagnostic-compile.log` | `1f17f84670f628505f11f706c5adf99ce64a49429f3c1c164773487f5f129bd5` |
| `/tmp/pi-d13-r-503-diagnostic-inputs.json` | `004a06160097954e0136fddaf6be3c0eca80daeac1d26e0d993216a4be91d1e4` |
| `/tmp/pi-d13-r-503-diagnostic.patch` | `84d37942dc0e725498ef93670d30b1c6ca6cc0622ce005779bd2ec2fb502e31d` |
| `/tmp/pi-d13-r-503-diagnostic.log` | `ee3fe5ca6d0d62dc674fdac74833a427076b1a043d5e5bf383fbd070d92d616e` |
| `/tmp/pi-d13-r-503-diagnostic.result` | `48fad15f40d40a0746e7d94719ad7366e86ee254d36aa01043221f0ee7c1e26f` |
| `/tmp/pi-d13-r-native/prior-run-fccf/native-only.log` | `62c8cc7cfacde557a97b16c610a99abe1f811724e5f378c646b7c83c537b4bd1` |
| `/tmp/pi-d13-r-native/prior-run-fccf/native-only.result` | `817389e1d01f9253342896cea7304cd0da395f769280b19223f29b50f870976f` |


### D13-R empty-locator product correction — committed4f764f

Lead released the architect's consequential three-seam empty-load contract.
Final local4f764ff6cc0f7b26fffdfcd3108ace5a75971c98, tree
f679c9ff8511617584431fd3408a47f0e050b1fc, directly above protectedP9bf, remains
P+ONE R from merged655. EXACTfccf..4f has four owning paths315+/95-: recovery
helper, upgrade private comparator hook, existing finite fixture and owning
recovery guide. Expanded existing test indentation accounts for part of the
count. No source publication/pins/CI/app build or SDK check has run on this core.

Only a journal-sealed originally positive empty/creating owner at exact successor
generation may replan its unsaved HistoryFile within its canonical member-owned
history directory. A temporary comparison copy normalizes only that field; every
other immutable stays exact. Ordinary sameUpgradeMember is unchanged; the nil-R
hook delegates its exact comparison. Interrupted afterimage replay uses the same
R rule, original mapping capture/hash unchanged. No rename/history rewrite,
new journal field, size allowance, codec/migration or generic path exception.

Before Publish, the R helper rebinds the saved proof's generation to the exact
successor and REUSES emptyLifecycleMember: same native/creation/HistoryRef,
initial settings/instructions/policy, no pending/held/persisted state or receipts,
positive VerifyCreation(nil), matching snapshot and idle workflow. Original and
new planned locators must both be absent; exact slots/reservation are reread.
Originally persisted owners keep exact files/prefixes. Published/completed retry
uses original-empty's ZERO original prefix: it validates the current owned locator
and immutable identity while allowing later persisted input or an independent
hold. It adds no fresh empty/native read, Load, clear, Publish or mutation. Exact
original receipt hashes and persisted original-prefix checks remain.

The finite empty Load now chooses a DIFFERENT planned filename, reproducing
oldcore ErrScope0.498s before the fix. Green firstsuccess/sameUUID plus14 existing/
new interruption cases (including after EACH owner Load) passed9.347s. The final
finite batch passed33.604s, including R1 genuine persisted-creating refusal, R2
aggregate journal size/required SourceHost, later published replay and15 new
prepublication afterimage refusals: persisted file, native/creation/historyRef,
foreign/noncanonical path, settings/policy, pending/held/persisted state, input,
old/new locator materialization and changed reservation. Refusals preserve bytes
and do not repeat Stop/start or publish. Existing completion test now covers BOTH
originally persisted and originally empty owners, completed and lost-final-response
phases, later valid persisted history + Accepted reserved input + independent hold,
and zero calls to EITHER worker during historical replay. Pure ordinary-successor
and fabricated-proof checks remain green; SDK-backed successor tests were excluded
from pre-review allocation. Commands ran through the declared Nix development
shell with GOWORK=off, GOFLAGS=-mod=readonly, TMPDIR=/tmp and
PI_PROBE_PACKAGE=/nix/store/nvwxl97fj19gvy9bnvr8s485jpn5hjmm-pi-1.5.2:

```sh
go -C portal test -mod=readonly ./internal/piruntime \
  -run '^Test(TeamConflict|UpgradeProofCannotBeFabricated|ExplicitSuccessor(PreservesHistoryAndNeverDispatchesHistoricalSocket|UnknownStartRetainsCurrentRequestAndGeneration|PreparationRetainsGenerationAndRefusesDescriptorRepair|PreconditionsRejectWithoutNativeOrRecordChanges))' \
  -count=1 -timeout=90s -v
go -C portal test -mod=readonly ./internal/web ./internal/session \
  -run '^TestPi(TeamConflict|RuntimeUpgrade)' -count=1 -timeout=45s -v
```

Consumer quick: existing PiTeamConflict/PiRuntimeUpgrade domain/route tests
PASS3.867s; session authority/projection PASS0.026s. No SDK/model/native worker
was launched. Diagnostic-only93 lines were removed from the worktree; their
patch/log/input identity remain in the prior503 appendix. Product docs use lead's
supplied paragraph in the existing recovery section, preserving positive proof,
Unknown, no-Create/Send, irreversible Stop, sameUUID and historical replay warnings
and anchors. No new guide or user-visible error was added.

Normalfixup080f14e7fd3d2aa25613581e10f7d7fa43ef1631 is retained at
backup/pi-d13-r-empty-locator-preconsolidation; its exact tree equals4f after
ordinary autosquash. fccf retained backup/pi-d13-r-diagnostic-fccf, published878,
c93 and all earlier reviewed/published refs/provenance remain intact. P9bf and
merged655 were not rewritten. No migrations or repeated pin stream. Seven old RPC
sources and four immutable team sources still equal e61. No branch-iteration
journal compatibility shim or old-R rollback support is claimed.

Changed product semantics require the lead-allocated LIMITED independent general,
architecture/repetition and risk/compatibility review of committed4f plus prior
whole-series conclusions before another SDK run. Source/index are clean, frozen
and released; all mutation/check/evaluation clients joined. I0 retains findings
ownership. No extra check campaign or operator/live recovery is authorized.

Final committed Ruby drv/output exactly match passed3vds/9971; no Ruby rerun.
Prepared-only native argv remains
`/tmp/pi-d13-r-native/run-native.sh /nix/store/irz2rkr0fvh2v2gffbjypwj0rnbryja2-dev-workspace-0.2.0`.
Script is unchanged; manifest now binds current4f/treef679 with34 source and26
immutable metadata/worker/SDK/Node hashes. It explicitly marks appirz product
source878 as DIFFERENT from current compiled Go4f, while consumed immutable
metadata/worker inputs are unchanged. This is the accepted diagnostic input
boundary, not final packaged-binary execution or blanket app equivalence.
After review, root should warm the SAME current4f ordinary CLI build cache outside
the20s fixture lifetime before its one full native run; product Go changed since
prior cache preparation. Use the prior declared-Nix60s/5s recipe with a fresh
output path workspace-portal-cache-prep-4f764ff6. The test still builds its own
binary. Final real artifact/input bridge follows only after full native success.

| Artifact | SHA256 |
| --- | --- |
| `/tmp/pi-d13-r-empty-locator-red.log` | `50e5885c903b044d67f14c479289e1ae44f0569b6c49ad1235904893b55ee82d` |
| `/tmp/pi-d13-r-empty-locator-first-green.log` | `656ee6854e31d13419d6dd390e748d7afee909f9bbb9e4603ed6036b1ad2ac6c` |
| `/tmp/pi-d13-r-empty-locator-core.log` | `4b4ec7d7e6d0cdd49d97cb7bc9a72f7979fc40944a26d504c7911bf0dc62afd8` |
| `/tmp/pi-d13-r-empty-locator-consumers.log` | `2d8d4150604f0caf9a8ba35137c49229cfc59b5539d77ed3a5da4788004aa023` |
| `/tmp/pi-d13-r-empty-locator-history.json` | `505bcc0c901dc0a39eaed7966dde296d1e59fb0c6e973d0eeb08afd01ea746e5` |
| `/tmp/pi-d13-r-empty-locator.diff` | `00d1f4be3103e07e96d9abf31e0f24a02ac5dc59cff138f5bdeacc1c05f65af0` |
| `/tmp/pi-d13-r-empty-locator-range-diff.txt` | `f506653d0bd0894689b919aee4e3164c64912f9b4fd44a6836e8412bfe6750ac` |
| `/tmp/pi-d13-r-empty-locator-full.diff` | `b6463199c0d636b721f565904192f42ab9fa0712b3223a203af52ee4c00a713c` |
| `/tmp/pi-d13-r-empty-locator-final-ruby-paths.json` | `bc6effc89887260362104199a283ed17155778dc1179595b1ed115825b374df0` |
| `/tmp/pi-d13-r-native/run-native.sh` | `d602fa315062efeb3fc7b01f9bc8ab1c04c8e81f5fdee50e85e5d1bed45740a6` |
| `/tmp/pi-d13-r-native/manifest.json` | `ca5ff1d56994d7462520fb302be222c9c876b0e84824bfe225534c168efb676c` |


### D13-R immutable fixture capability wiring (91cafd4c)

Final frozen runtime head `91cafd4c0c50ffb7208498a605707c4c3b1b1174`, tree
`f3bff8f5008ade6561a92856eec22a25ac48488c`. The4f..91 delta is exactly two
fixture files,18 additions: restore the owning conversation-identity and checked-input
readers in the existing immutable-root branch before Ensure, and assert actual
manager-reader identity/checked-input/delivery tuples against owning readers for
BOTH saved original and candidate packages in the existing conflict constructor.
Synthetic defaults remain false. No product/guard/worker/protocol/schema/docs/pin
change or weaker public-admission/history/no-replay assertion.

The prior4f run reached successful recovery and same-UUID replay,1Start/1Stop,
zero Create/Send/Configure, preserved data/bindings, clear exact loaded selection,
and fresh page/activity HTTP200 decoding, then failed public deliveries admission.
These are scoped assertions and control-flow evidence for completed publication;
no direct durable journal dump was retained and no stronger activity classification
is claimed. Populated selection/settings plus empty deliveryModes proves the local
CheckedInput=false predicate. supervisorFixture's synthetic readers remained false
because the immutable branch restored only transcript/inputDelivery/activity.
Both actual g7 and irz declare identity/checked-input/input-delivery1. This was a
fixture wiring mismatch; asynchronous waiting cannot change that constant reader.

Faithful native-free old-red used the actual existing
TestPiTeamConflictRetainedSetup entry after adding its constructor assertion:
FAIL0.125s, original g7 identity declared=true/configured=false. Restoring exactly
the two production readers made the SAME selector/inputs PASS0.170s (test0.11s).
Both used declared Nix, GOWORK=off, GOFLAGS=-mod=readonly, TMPDIR=/tmp and the
same g7/SDK/catalog/irz inputs frozen in the manifest. The bounded Go command was:

```sh
go -C portal test -mod=readonly -tags=pi_native_fixture ./internal/piruntime \
  -run '^TestPiTeamConflictRetainedSetup$' -count=1 -timeout=45s -v
```

Preparation uses the existing in-process fake Ensure and returns before native
Create/Send/attachment or public server/profile work. No SDK worker/model/real host
or native case was executed by I0. Product prose remains correct and needs no
change for this test-input correction. Root owns affected review and next native.

Normal fixup `4f096ff9` is retained at
backup/pi-d13-r-admission-preconsolidation; its exact final tree equals91.
Prior4f is retained at backup/pi-d13-r-admission-4f. P9bf and merged655 unchanged;
series remains P+ONE coherent R, no migrations/repeated pin stream. Published878
and all earlier backups/provenance remain. Source/index clean and frozen; all
clients joined. No publication/CI/pin/appbuild/live action.

Committed Ruby evaluation exactly equals PASSED derivation3vds/output9971; the
retained output exists. No Ruby rerun. Manifest now binds91/treef3bf,34 source
hashes and26 immutable inputs; all immutable hashes and seven old-RPC/four team
source byte equivalences to e61 were rechecked. Rooted irz deriver is exactly
32rf1pbhy3bf7shpi8ym2yqbh23k6pv4. Its packaged product source878 differs from
current compiled Go as explicitly recorded; unchanged consumed metadata/worker/SDK
identity is the accepted diagnostic boundary, not final packaged-Go execution.

Prepared-only native command (NOT launched):

```sh
/tmp/pi-d13-r-native/run-native.sh /nix/store/irz2rkr0fvh2v2gffbjypwj0rnbryja2-dev-workspace-0.2.0
```

Current-source ordinary CLI product bytes are unchanged from4f cache preparation.
The test retains its own ordinary build/error propagation and20s fixture context.
Prior actual4f failure files were preserved byte-for-byte before manifest refresh
in /tmp/pi-d13-r-native/prior-run-4f-admission; native log SHA
425d54f8683d4de00a12d62817c770bb00d32aea8747699ba827ef8fb2434ead,
result1bfc4f84c9ede657599967a57cba7c30b528783b9c2810e92389ab3f73d3c11d.

| Artifact | SHA256 |
| --- | --- |
| /tmp/pi-d13-r-admission-red.log | 63a33bfa4aa05665fc9727bdfc1ec5d5709c56e0d576fe4598dafcdcde0a85b2 |
| /tmp/pi-d13-r-admission-green.log | 944a27b01954ca0acedae566dd8280fe9bb727f19f3bec947c66df7325682da9 |
| /tmp/pi-d13-r-admission-history.json | a558bd53587d21a21288ec1fa0c2818dec629bd19781bfccffd73e24a84bd92a |
| /tmp/pi-d13-r-admission-diff | 4024e791dea5027a605131223a2c65901543aaa1e3dd225537b519b12ea945e3 |
| /tmp/pi-d13-r-admission-range-diff.txt | 2201b0a1c0aca294887cc056c11dcc1d58398cd26752f67abb681b222230a27c |
| /tmp/pi-d13-r-admission-full.diff | e0d2bde70267c2ab4bbc28d0ad565162415c25eb3cc547f82a466d576fecbb60 |
| /tmp/pi-d13-r-admission-final-ruby-paths.json | bc6effc89887260362104199a283ed17155778dc1179595b1ed115825b374df0 |
| /tmp/pi-d13-r-native/manifest.json | fe904d3720277f87a4f37d5b0102000bf60f6ba0adb801dcec243cd35a34fb03 |
| /tmp/pi-d13-r-native/run-native.sh | d602fa315062efeb3fc7b01f9bc8ab1c04c8e81f5fdee50e85e5d1bed45740a6 |


### D13-R successful retained native and final source publication (91cafd4c)

Root accepted reviewer0's limited general/architecture4f..91 review with NO
FINDINGS, retaining unaffected prior whole-series/risk/history conclusions.
Root's ONE full native session88587 joined0: pre/native/command/post/final all0,
15s elapsed, Go11.266s/Test11.20s, no SKIP. This covers recovery, same-UUID replay,
fresh public admission and one later ordinary send under the exact case's retained
history/no-replay assertions. Scope remains current-source Go91 + rooted irz
immutable worker/Node/SDK/metadata, faux inference and synthetic host drain;
no final packaged-Go, real restore/systemd/deployment or live-peer claim.

Successful raw files preserved byte-exact in
/tmp/pi-d13-r-native/passed-run-91cafd4c before publication; all prior failed-run
subdirectories remain untouched. Log SHA
cd2de1192231ddb24366168b7b0a40b5d8df939313c04d212c68bbcb3d7b33e8;
result8c68e5b93f03f629225433242aed9c706e0ce93156d05ec3e0814552fb362ab9.
Manifestfe904d37 and scriptd602fa31 unchanged (full hashes in preceding appendix).

Canonical SSH git@github.com:aither64/dev-workspace.git feature
refs/heads/2026-11-23-pi-message-delivery published exact
91cafd4c0c50ffb7208498a605707c4c3b1b1174/treef3bff8f5008ade6561a92856eec22a25ac48488c
with explicit exact-old lease87835ef85e7cdc81254ba47aff888445d87a66bd; push joined0.
Fresh before/after ls-remote proves default symbolic HEAD/master unchanged
65544340f94ebb112872743738f84c1a7022b06a and final remote feature EXACT91.
No source/index/HEAD change, rebase or default write. Publication receipt
/tmp/pi-d13-r-publication-91ca.json SHA
0719b31263764212d308bc4f13687d81b45a5e827724521c7a527c649d3b5042.
P+ONE R and all published/reviewed backups remain as recorded; no migrations.

Direct dependency release delivered/joined0 to parked I1 under stable message
ac56e169-cb10-4671-9773-9de55bd112cb with ROOT-ACCEPTED/REVIEWED/PUBLISHED exact
source and fresh equality receipt. I1 owns actual exact-source NAR resolution and
final pin supplement; no NAR guessed here or878 product-equivalence claim.

ONE bounded CI branch snapshot returned exact91 Check run45624384631 in_progress:
https://github.com/aither64/dev-workspace/actions/runs/45624384631 . No obsolete
active own-branch runs; no cancellation, watch or retry. Snapshot
/tmp/pi-d13-r-publication-91ca-ci.json SHA
9d8431d7c70897ba6413be956be4361cc2fed53028ef4b6bbb02a2bdb8b16ff9.
Root retains final CI/composed/artifact/consumed-input bridge and approval ownership.
No appbuild, Ruby/native rerun, deployment, lifecycle or live operation by I0.


### D13-D final91ca product-fix pin supplement

Final/released workspace `9d302f8fa4ad70f0281d5cbd8b5bd0f84b2ac0fc`, parent
accepted fresh `a755bfa7f2fd1ab010e7dd719f581d35e15fde4d`, tree
`3413ed932d6e25c1ba5a4af4e8b385a69fd3950c`, two flakes5+/5-.
Configuration `9bdb0c68b47ceebde450fcdf018727b382cacc09`, protected merged parent
`d5055ec0b2ea22de976f6703208f5526c3e185ca`, tree
`38de6433c58591509ec0932cce42485c95f4d8fd`, generated lock3+/3-.
Consolidated only unmerged a1c5/d0ef through normal amend/empty-range rebase plus
owning confctl generation; one final pin per stream. Prior pin heads absent as
ancestors and retained in backup refs; merged09ea/d505 history intact, no migration.
Canonical SSH explicit-old-lease feature pushes joined successfully; fresh remote
equality passed, defaults remain d433/d505 and shared mastera755 unchanged. Feature
trees/indices clean and all own clients joined/windows released.

Final independently reviewed/root-accepted/published runtime
`91cafd4c0c50ffb7208498a605707c4c3b1b1174`, NAR
`sha256-w8rK1jDoPlHI8Z/Im0Zeo/1qA5OkgCMhZEYCXOF6vSk=`. Direct remote proof and
publication receipt SHA0719b31263764212d308bc4f13687d81b45a5e827724521c7a527c649d3b5042
verified before mutation. Graph38/67 plus follows versus accepted prior pins
changes ONLY runtime identity/lastModified/NAR; provider2547 and all other selected
inputs remain unchanged. Exact runtime subgraph, full runtime/provider locked
identity equality and cross-lock/site checks pass. Existing Ruby deployment quick
passes4/19 in1.410211s plus parse/diff; config normal Nixfmt/message hooks and
JSON/Nix parse/graph/diff pass, generated655->91 two-commit message and width
warnings preserved. One ignored Nix evaluation-cache SQLite busy warning remained
in passing cross-lock output; no rerun.

The reviewed R empty-locator product fix plus fixture changes mean91ca is NOT
product-equivalent to878. Host helper/template/native-Codex/input-lock/SDK builder
and marker boundaries remain unchanged; recovery product behavior changes and is
explicitly recorded. Root owns final artifact/source91ca and consumed worker/SDK/
Node bridge to diagnostic irz, required CI/native/composed acceptance and exact
full-Ruby derivation/input reuse. No app build, full Ruby or native rerun here.
Root's retained native pass is not claimed as a real-host restoration or final
packaged-Go proof by this pin package.

New D13-91ca integration targets/history/commands under /tmp use runtime clean
655->91, config clean d505->9bdb, provider2547 already integrated, shared master
a755->9d. Earlier D13/D12/D11 artifacts and backup refs remain intact. Exact old/
new base/head range-diffs and consolidation/migration conclusions retained.
Declared environments prepare before any later lead-owned claim; no default
write, claim, merge, live/operator/recovery/Stop/deploy/CI watcher or lifecycle action
was run. Raw `/tmp/pi-message-delivery-D13-91ca-*` logs cover publication, host/input
boundary, workspace pin/quick/commit/range-diff/push, config pin/quick/generated
message/range-diff/push, cross-lock and integration receipts. Final pin findings
remain with I1; root owns subsequent verification/deployment/authority decisions.


### D13-D deployed9d equivalent workspace successor e7

After root's activation21159 joined/released source9d, ordinary feature-only
rebase a755..9d onto fresh shared master172c1457646b06fe082364ebf4d2f9aba7199d09
completed conflict-free. Entire a755..172c changed only six work/archive records;
no product/input delta. New head e7b876f69aca4554d52a3ac19ed097263847ad43,
tree3fae54ef27913bedf33fcebf8a599bf5f903fa06. Both pin files are byte-identical.
One final unmerged pin; ordered patch-ID cd6447c1239308d93ba81ae93c38dd51301f67d4
is identical, range-diff '='. Backup ref
backup/2026-11-23-pi-message-delivery-D13-deployed-workspace-9d preserves exact9d.
Merged history unchanged; no migrations. Deployed9d is represented by the proven
equivalent successor, not claimed as a literal ancestor.

Canonical Git-flake no-build metadata reads prove exact old/new app plus all five
check derivation/output identities equal the successful built9d batch. App drv
/nix/store/s6qiklxmmdz409qlg26643mf0g8rafb1-dev-workspace-0.2.0.drv, output
/nix/store/1zn1a51qrsin83fszrprdjp45208vsj4-dev-workspace-0.2.0. The initial plain
path resolver diagnostic used a different source representation and is not used
for equivalence. JSON parse, diff and crosslock/site pass; prior Ruby4/19
1.410211s retained for identical inputs. No rebuild or review campaign.

Canonical SSH feature publication with explicit old9d lease joined0; fresh feature
equals exacte7, default remains d43347c1. Runtime91/config9bdb features and defaults
655/d505 reconfirmed unchanged. Detached runtime/config targets remain clean and
ancestral; declared environments/hooks/trust receipts reused unchanged. Shared
master remains172c; logical staged index fingerprint is unchanged. No shared
source/index/default mutation, claim, deployment, live/native action or lifecycle
operation. Feature source/index clean; all own effects joined/window released.
Comparison captured for finale7. /tmp/pi-message-delivery-D13-rebase-* contains
fresh baseline, exact6 drv/output pairs, equivalence/history, range-diff,
publication and current target/literal-command receipts. Root owns final fresh
claims/merge/push proof after recovery; final pin findings remain I1-owned.


### D14 qualified historical terminal refusal — committed review packet

Base/merged predecessor91cafd4c0c50ffb7208498a605707c4c3b1b1174 → NEW normal
commite603577081496c5af264791c09406d1e96150f00,
tree396c8fe8eb8228becb6276fa1a6f24bbd43c29fe. Exactly one follow-up above merged91;
no merged-history rewrite/fixup/consolidation or pin changes.13 files715+/19-.
No migrations, new journal fields, schema, public wire, adapter or worker/SDK change.
Existing schema1 journals keep their read support and nil-proof evidence digest
byte identity; new Kind `caller_policy_refused` is deliberately unreadable by91.
No supported branch-iteration compatibility shim/source registry was introduced.

Requested result: all-callback settlement can recognize ONLY an earlier NONSELECTED
team_message terminal result from the qualified original saved legacy producer.
The selected callback still needs initial_conflict; all owners/native origins,
Accepted input, exact original history/prefix, reservation, empty-member and other
unknown-effect proofs remain. A READY target or absent receipt gives no proof.

The R-local parser/projection requires unique original call/following result,
exact native ID/name/arguments/origin and explicit isError=false. One JSON text
block equals details with exactly disposition=held/stage=caller_policy/reason=held/
materialization=unattempted; strict duplicate-aware codec refuses any other shape
or tuple. The transient result-entry ID/hash is included in existing evidence digest;
raw body is never journaled. Domain retains owning binding/roster/intent/envelope/
lookup checks; contradictory receipt refuses. Aggregate independently checks exact
original source eligibility, call/selector/target/proof and absent receipt.

Producer eligibility uses ONLY validated original saved Start, existing g7/e61
fixed graph provenance, never target/profile/capability labels. Existing private
Config reader-style seam lets finite tests declare exactly one synthetic producer;
nil hook chooses strict production verifier. Finite fixtures do not depend on g7
being installed or claim execution of that legacy producer. Frozen producer trace
is separate from synthetic parser/consumer verification; peer material remains
only in ignored/untracked0600 private records and is absent from source/tests.

Supplemental exactinteger piTeamConflictTerminalRefusal:1 plus basecap1 is required
before new-kind reservation and on any saved new-kind resume. Existing full-phase
journal size admission is unchanged. Existing retained traversal flags both readers
for prepared/settled/complete journals; sourcekind team_conflict_terminal_refusal
flows through owning scanner/Ruby TEAM_SOURCES/selection+activation target guard.
Old journals still require only their old capability. No journal deletion,
conversion or rollback to an incapable package is supported after new Kind exists.

Faithful old-red: existing finite Unix-supervisor history carries original Accepted
user, earlier READY-target/missing-receipt exact typed terminal reply, distinct later
selected initial conflict. Before consumer wiring it refused doubleErrHeld0.287s;
after wiring it settles both without changes/effects. Parser21cases PASS0.036s.
Final focused TeamConflict core PASS37.991s, production web domain PASS5.123s and
preflight scanner PASS0.075s. Required gap follow-up PASS4.502s/core +1.221s/web:
new-kind Published/complete replay after appended legitimate input+independent hold
makes zero worker/attachment/Load/clear/Publish calls and preserves original prefix;
read errors/changedprefix refuse. Source/selected/unknown/orphan/duplicate/foreign
result and contradictory Accepted/NotSubmitted/Unknown receipt cases refuse.
New target-version and all5 checkpoint inventory cases pass; no reservation/retention/
Stop effects on incapable initial target, and incapable saved replay remains fenced.
Existing R1 persisted-creating, size/SourceHost, old-protocol and old-journal tests pass.

Declared-Nix quick commands (already joined; no SDK/model/live runtime):

```sh
GOWORK=off GOFLAGS=-mod=readonly TMPDIR=/tmp \
  PI_PROBE_PACKAGE=/nix/store/nvwxl97fj19gvy9bnvr8s485jpn5hjmm-pi-1.5.2 \
  go -C portal test -mod=readonly ./internal/piruntime ./internal/web ./cmd/workspace-portal \
  -run '^Test(TeamConflict|PiTeamConflict|PiWorkflowPreflightClaims.*(TeamConflict|TerminalRefusal))' \
  -count=1 -timeout=90s -v
ruby test/workspace_session_backends_test.rb
```

Owning Ruby inventory PASS23runs493assertions0.550s/no skips. Final committed
full Ruby derivation is /nix/store/f6f76jl1rfvyibvb9dll0h2i4rp70dic-dev-workspace-ruby-verification.drv, output/nix/store/3b238sl6jh4q9hhi3ckqzdjxb5fpc6kc-dev-workspace-ruby-verification. This DIFFERS from prior passed
3vds/9971: no full-suite reuse/pass claimed. Read-only Nix evaluation joined0;
no build/fullRuby/SDK/native/capture/live recovery/CI/publication was run.

Literal existing full-Ruby-only recipe, prepared for root AFTER final review:

```sh
/nix/store/i4bv0lvk0gfzllcy2kqgz3iam0aw4c4i-nix-2.34.8/bin/nix build \
  --no-link --print-build-logs .#checks.x86_64-linux.ruby-verification
```

Use repo cwd at frozene603, verify exact drv/output above, preserve aggregate
all10file/unique-shard coverage. Do not substitute old3vds evidence.

Existing retained native full case is unchanged. Prepared-only literal selection,
after root builds/qualifies the exact D14 target with BOTH exactinteger markers1:

```sh
env GOWORK=off GOFLAGS=-mod=readonly TMPDIR=/tmp \
  PI_CENTRAL_APP_ROOT=/nix/store/g7wvpp2nc9cvsa8pdf1azfdib80kkcjm-dev-workspace-0.2.0 \
  PI_PROBE_PACKAGE=/nix/store/nvwxl97fj19gvy9bnvr8s485jpn5hjmm-pi-1.5.2 \
  PI_CENTRAL_CATALOG_FIXTURE=/tmp/pi-d13-r-native/catalog.json \
  PI_USABILITY_PACKAGE='<exact reviewed D14 candidate output>' \
  /nix/store/i4bv0lvk0gfzllcy2kqgz3iam0aw4c4i-nix-2.34.8/bin/nix develop --command \
  /run/current-system/sw/bin/bash -c 'go -C portal test -mod=readonly -tags=pi_native_fixture ./internal/piruntime -run "^TestPiTeamConflictRetainedWorkerRecovery$" -count=1 -timeout=3m -v'
```

No new harness/nativecase is needed for a new native protocol: none changed.
This SAME native case covers overall recovery/public monitoring/admission/later-send
regression; D14 terminal-result/new-kind logic is covered by faithful finite tests
and separately qualified frozen producer trace. It does not itself claim an executed
old supervisor/systemd host or real peer recovery. Root decides affected acceptance
and refreshes existing source/immutable-input manifest for actual target/markers;
current old1zn cannot supply the new reader. Current source must bind Go/CLI and
retained exact Node/SDK/worker graph; final packaged source/metadata/input bridge
and fresh operational preflight are separate readiness obligations.

Documentation routing: terminal proof, supported reader/rollback and recovery
warnings → operator how-to/reference → docs/pi-runtime.md existing recovery section.
Supplied lead paragraphs inserted with only permitted positional wording
"identified in this section"; factual compare matches code, all anchors/Unknown/
no-resend/history/30s/input-retirement warnings preserved. No README/newguide needed.

Review requested: limited affected general + architecture/repetition + risk/
compatibility on91..e603; retained reviewer0 Sol/xhigh. Highest risk is positive
nondispatch proof and persistent reader dependency. Confirm old-evidence digest
compatibility, no migration/history rewrite, exact source qualification and aggregate
unknown/selector refusal. Lead owns invocation/acceptance and all long checks,
publication/pins/builds/fresh claims/recovery. Source/index frozen and all clients
joined. This packet grants no operational retry. I0 retains findings ownership.


### D14 R-D14-1 direct remediation — finale5cddad3

Accepted Important R-D14-1 is fixed in e5cddad35dbce4e48b49682e796d9890e01b1ec2,
tree484d996c49d9bbc9ed0c32681707b8297c4e3028. This supersedes the earlier packet's
statement that any existing Accepted/NotSubmitted receipt is contradictory to a
later refusal. An exact original operation receipt and a later same-ID invocation
refused before dispatch can both be valid. Receipt precedence is restored; only
mismatched/malformed/Unknown/read-error receipts refuse. The terminal proof is
projected/used only when the exact target receipt is genuinely absent.

The production delta deletes the blanket present-receipt projection rejection and
filters optional result projection to absent receipts. Existing immutable envelope,
ref/digest, original settings, phase and witness/native history validation remains.
Receipt-backed settlements retain their original Kind/evidence digest and do not
gain a supplemental capability dependency. No new behavior boundary, schema,
journal field, producer eligibility, target guard or product prose was introduced.
The supplied owning prose still matches these facts without amendment.

Genuine regressions replace the incomplete presence-only negative fixture. The
runtime fixture has a valid codec-loaded Accepted operation receipt with exact
same-ID/envelope/digest/settings, a native consumed-user entry and matching witness,
then a later same-ID native tool call with the exact unattempted refusal, plus the
distinct selected initial conflict. It first prepares an original base-kind D13
journal with no projection and supplemental reader unavailable; D14 pre-Stop replay
must retain exact journal/evidence/receipt/history bytes and make zero Stop/start/
publication/data effects. The production domain also preserves matching Accepted
and NotSubmitted classifications while Unknown and changed immutable input refuse.

Old-red on reviewed e603: runtime0.443s rejects projection compatibility assertion;
production domain1.292s rejects valid matching Accepted as immutable conflict.
After the narrow fix, focused runtime/parser/strict negatives/digest regression
PASS1.283s and web domain PASS2.721s. Final absence-only positive and all-phase
supplemental-reader/retention checks PASS3.215s. All checks use the same declared
Nix readonly-module/finite-worker environment as the previous packet. No native
SDK/model/live session, full Ruby/build, publication/CI/pin or operation was run.

Normal fixup f1fa1303 is retained at backup/pi-d14-r1-preconsolidation; its exact
full tree equals final e5 (diff exit0). Original reviewed e603 remains at
backup/pi-d14-reviewed-e603 and is provenance, not a claimed final ancestor.
Only the UNMERGED D14 range was autosquashed; merged91 is unchanged as exact parent.
Final range91..e5 has ONE D14 commit. e603..e5 is exactly4files156+/13-.
No migrations or repeated pin streams. All source/index clean/frozen and children
joined. Root owns direct mandatory-review step9 acceptance; prior four-lane/full
history/docs conclusions are retained subject to this narrow inspected fix.

Committed final Ruby re-evaluation joined0 and exactly matches e603 f6f76/3b238:
/nix/store/f6f76jl1rfvyibvb9dll0h2i4rp70dic-dev-workspace-ruby-verification.drv
→ /nix/store/3b238sl6jh4q9hhi3ckqzdjxb5fpc6kc-dev-workspace-ruby-verification.
This is still DIFFERENT from old passed3vds; no full-suite pass/reuse is claimed.
The fullRuby-only recipe and SAME nativecase in the preceding packet remain the
prepared commands, bound now to frozen e5 and a future exact capable D14 target.
Root owns actual launch/target/consumed-input bridge after acceptance; no new harness.

| Artifact | SHA256 |
| --- | --- |
| /tmp/pi-d14-r1-red.log | 2572c857400b0e62be3809448e9ce5bc06b4bfbb25cfa6ec2c03fc4385c6d152 |
| /tmp/pi-d14-r1-green.log | ff2778570191b86d889693c7324ad875ae47cbeaccbd16074ebe65b3a03c0b47 |
| /tmp/pi-d14-r1-absence.log | 2bcdc3adcd8e9a865c0dc07711bb2d6b7948266e5e3d410420edfcbdd227f9f0 |
| /tmp/pi-d14-r1-history.json | ea118193516565205f58d4958b2f7b641a1af5dad1c1e7769865a2d8c7a20155 |
| /tmp/pi-d14-r1.delta.diff | 3862e528cb6d3a296221f3ca2ac407b9cf04899406088c7811efc3a172457ff7 |
| /tmp/pi-d14-r1.full.diff | a90aaa9ee25f90a0ddafdac095e015ff467dc73531f1391f75f7caff9f387ada |
| /tmp/pi-d14-r1.range-diff.txt | dcfcb246acc1437514ef1de5ebc63c6c1c3b5bc9a9b55bad7108d6d8cf2799f4 |
| /tmp/pi-d14-r1-final-ruby-paths.json | 7790b970ec90450b4c872a84a96b93634a9ed1cad7943ad24f091d97d016c72f |


### D14 finite tool/stage extension — final8729bded

Frozen final8729bded7422102cb1fdb6f880d296ac4cb970c4,
treea163810aa43bee2103ba0fcfe0809f371052a365, exact parent merged91ca.
The e5..872 delta is ONLY5Go/tests/docs paths249+/93-. Overall91..872 remains
ONE D14 owning commit (13files1020+/25-). Reviewed e603/e5 backups retained;
normal fixup51e8552d is backup/pi-d14-policy-pairs-preconsolidation and exact
full-tree equality to872 passed exit0. Merged91/default history untouched.

Accepted finite contract: actual tool in {team_message,report_to_lead}, actual
stage in {caller_policy,recipient_policy}; fixed disposition=held, reason=held,
materialization=unattempted. Text/details must agree exactly through the same
strict parser/unique native call+result/Accepted input/origin/history/fixed original
producer proof. Report arguments have no target and normalize exactly to lead.
No other tuple, arbitrary result, selected callback or unknown effect is accepted.
Never-reset zero-effect producer state supplies positive nondispatch authority;
a stage name or missing receipt alone does not. Qualified original g7/e61 graph
and absence-only projection/valid receipt precedence stay unchanged.

The UNPUBLISHED Kind is now terminal_policy_refused; no caller-only spelling
alias, iteration reader/migration, new journal field/schema or supplemental marker
was retained. Existing final piTeamConflictTerminalRefusal:1 still gates this
exact finite contract alongside base1. D14 has produced no new-kind live journal;
old91 journal formats/read behavior remain supported. Size admission naturally
includes the final Kind spelling. Reader/inventory/Ruby plumbing is unchanged
from the reviewed implementation. Seven old RPC/worker source files remain byte-
identical to e61; no public CLI wire, worker/SDK, native operation or UI change.

One synthetic linear history contains ALL FOUR tool/stage pairs and a distinct
selected initial conflict. On e5 it reproduced Held refusal0.202s. Final firstgreen
core0.653s/web1.520s; complete affected finite batch core44.809s/web6.385s/scanner
0.051s PASS0/no skips. It includes strict duplicate/extra/null/type/stage mismatch,
wrong actual name, caller-selected report target, selected misuse for BOTH tools,
attempted and genuine unfinished unknown-effect refusals before reservation/effects.
Both tools' production domain tests retain valid Accepted/NotSubmitted precedence;
Unknown/immutable mismatch refuse. Genuine Accepted same-ID retried native callback
and old D13 prepared journal pre-Stop/evidence-digest regression remain green.
All-phase including complete reader inventory and Published replay after later input/
independent hold pass. No further optional checks or expanded campaign was added.

Supplied first terminal paragraph replaced exactly with the finite tool/stage and
valid receipt wording; supplemental-reader paragraph, all anchors/Unknown/no-resend/
history/input-retirement/30s/replay warnings remain. Technical facts match source.
Docs remain in existing recovery how-to/reference; no README/new guide required.

Committed Ruby re-evaluation joined0: EXACT passed f6f76jl1rfvyibvb9dll0h2i4rp70dic
→3b238sl6jh4q9hhi3ckqzdjxb5fpc6kc drv/output; retained output exists. Root's full
Ruby708s PASS at e5 may be reused by this exact identity, not tree equivalence.
I0 did not rerun full Ruby. Literal prepared fullRuby/native-case recipes from the
preceding packet remain, frozen now to872 and a future exact capable target.

Limited affected independent general/architecture/risk review is required now;
prior scope/history/reader-plumbing conclusions and direct R1 acceptance retained.
No native/live capture/publication/pins/build/CI/claim/operation was run in this
extension. Saved local matrix closes identified class gaps only; Accepted native
Bootstrap is still not certified. Any future root-allocated observation must record
callback index/tool and Settle versus Accepted-creation/Bootstrap stage rather than
return another generic first error. No observation is allocated/run by this packet.
All children joined; source/index clean/frozen/released, I0 retains findings.

| Artifact | SHA256 |
| --- | --- |
| /tmp/pi-d14-policy-pairs-red.log | 09f460585c405524852f5b45abe5bb1b7165abf590ab97485cf520a1282dac3b |
| /tmp/pi-d14-policy-pairs-first-green.log | a07127bebcd1ded368869dd88d4bceab7e70e6cc6da4feaec37dcd9d98fa0440 |
| /tmp/pi-d14-policy-pairs-focused.log | 8d523cfebd3583bbda13b4d86c7dc6f92f8155c7b4ec9a098f0a7c8a17877c83 |
| /tmp/pi-d14-policy-pairs-history.json | 498523ff5c9f319ae116a0f30eb7d3af395d12f8db3fc38aca0aa6093d967b72 |
| /tmp/pi-d14-policy-pairs.delta.diff | f74263c22d8248a90b7f5b1746a01507ac51f24971d64bf1d3529c265eb5e12c |
| /tmp/pi-d14-policy-pairs.full.diff | d3bd79a0e8b9ebd18bf87bab15b70221e3e6f99652961a867e28fd22ab770f6f |
| /tmp/pi-d14-policy-pairs.range-diff.txt | 447705c769bd289d4ec2757d4a1f3d3845fc2e1ba4f14dc6ca70df40c9f99fca |
| /tmp/pi-d14-policy-pairs-final-ruby-paths.json | 7790b970ec90450b4c872a84a96b93634a9ed1cad7943ad24f091d97d016c72f |


### D14 protected-f6 rebase and publication — b3dd92cc

Root accepted reviewed8729 and released clean rebase onto protected
f6d60bf87002fb1896599f35f0284743c16d7e6f. Final committed/published
b3dd92cc6f61f697fc61c12fa0b5246511e93f4f, tree
d25c1eab998e1f9763fc0dfd511ec45ac98393d4, exact parentf6.
Protected series remains P9bf34aa1 / R91cafd4c / f6d60bf8 + ONE D14.
No conflicts, functional adjustments, migrations or repeated pin streams.
Published8729 and earlier e603/e5/preconsolidation backups remain retained.

Old91..8729 -> f6..b3 range-diff is `=`; ordered stable patch ID
6d5aa4dd5d47bb344a36295176c8b7358b6b0394 matches. All13 D14-owned
file blobs are byte-identical to reviewed8729; independent archive baseline
behavior is retained. Full finite passing evidence reuses this exact file proof.
Only released focused rebase checks ran: mixed four-pair/refusals, genuine
receipt/old-prepared replay and digest core0.019s; domain3.821s, PASS0; diffcheck0.
Final Ruby eval joined0 EXACT f6f76jl1rfvyibvb9dll0h2i4rp70dic ->
3b238sl6jh4q9hhi3ckqzdjxb5fpc6kc; output exists, root full PASS708s reused.
No Ruby rerun or native/app build.

Canonical SSH feature first fast-forwarded91->8729, then exact-old8729-lease
push publishedb3 EXIT0. Fresh SSH before/after feature equality verified;
default/master and remote HEAD remain exactf6 unchanged. Source/index clean.
ONE bounded new-head CI listing: Check45655170251 in_progress. Only obsolete
active own-branch8729 run45653991356 cancellation requested (not watched to
terminal); no other cancellation, CI watch or retry. Direct I1 dependency
message57ab5a46-16fe-4566-a3db-d0f2c0e06916 delivered with ROOT FINAL ACCEPTANCE
PENDING limited baseline/history noninterference follow-up; no functional pins
released by I0 and no NAR guessed.

Standalone diagnostics remain scoped refusals with zero durable/PID changes,
not all-callback live eligibility. Root selected the normal owning public Upgrade
preflight for later verification; no weaker proof or attachment repair.
No further capture/GET/native/send/recovery/default write/claim/deploy/lifecycle
action ran. Source frozen; all owned children joined; I0 retains findings.

| Artifact | SHA256 |
| --- | --- |
| /tmp/pi-d14-rebase-equivalence.json | 21f19f95af35e0360389141f6bdf7c8f5f612a989cd0b5be6c3be4b1e76ba086 |
| /tmp/pi-d14-rebase.range-diff.txt | 973e66364a03004727c1b027e777da301e24f5af824ecc220bf2649104d3bdb9 |
| /tmp/pi-d14-rebase-core.log | 7e879d1513c9ac4ed5a31e78455bcb1541060d568264047cdaaa9b104d837eff |
| /tmp/pi-d14-rebase-web.log | f11cb825ce57932097f4f98960ffaa78e78ce087123c0d69469063c3ea9b794f |
| /tmp/pi-d14-rebase-ruby-paths.json | 7790b970ec90450b4c872a84a96b93634a9ed1cad7943ad24f091d97d016c72f |
| /tmp/pi-d14-rebase-publication-before-push.txt | 4f6c212fb93aab662c995cb475947a610251cceb2bd63e960831c2ee00e61557 |
| /tmp/pi-d14-rebase-publication-after.txt | 887b91e749b088ffaea69de060b79251a346d6ccbf63b5050dce5e024a6aeb63 |
| /tmp/pi-d14-rebase-publication.json | c6a38f9616a116ded6549459aa227575dc6fba5c09d55074e4dcf2067ec13d4d |
| /tmp/pi-d14-rebase-ci-list.json | 6e68b4406fd2f9dabc8bc5aeec97fd47088befa1cf4e5ccef7d9e934bbb17a1e |
| /tmp/pi-d14-rebase-ci-cancel.txt | b81c8f3e9a13e3a9b30362b57e3d6d4a9470246912bc417aa52dbc572b72a52f |


### D14 final pins and tracking-baseline handoff

Final reviewed/published runtimeb3dd92cc6f61f697fc61c12fa0b5246511e93f4f,
treed25c1eab998e1f9763fc0dfd511ec45ac98393d4 above protectedf6, independently
verified by canonical SSH before real NAR resolution. NAR
sha256-Xcck5ZVs7KrU5sDGQoadfGIXv1wvyWSNbgikonso6mM=; sourceib1r7yay50r9spsz9j0pbdk56f4hs1zh.
No8729 consumption. Accepted APJA source proof1148blobs=f6 and extension112blobs
=bf12 preserved; normalized extension-tool paths do not imply behavior delta.
All3APJAarchivefiles remain byte-identical in finalb3. Host helper/template/native
Codex/export sources and runtimeinputlock unchanged. Intended D14 markers
piTeamConflictRecovery=1 and piTeamConflictTerminalRefusal=1 present; no claim of
all-metadata equality or live callback eligibility.

One NEW normal follow-up each, no merged rewrite/consolidation/migrations:
workspace0c9e96358168f084e992bc84eae1b2222316f0b2 above acceptedf174, tree
0b735b4532acd1055bd7eada8b4fd79eab609df4 (2flakes5+/5-); configuration
3d522c45890240665b58f25d0071d17ed387374e above acceptedfdcb, tree
18f9e4cbaaedb357ff934127abf3a3772c5a3052 (owning confctl exactset--commit,
generatedlock3+/3-). Complete38/67nodes and all other identities/edges/follows
unchanged; only final runtime identity/time/NAR and workspace original exact URL
change. Provider2547/extensionbf12 preserved. Normal NONFORCE canonical SSH feature
pushes joined0; fresh exactfeature0c9/3d/defaultf174/fdcb equality proved. Both
sources/indices clean/frozen, root got committed quick-green heads immediately.

JSON/Nix parse/diff/completegraph/crosslock/site PASS. Existing Ruby deployment
quick4runs19assertions1.425581s PASS/no skips. Config normal hooks PASS/generated
width warning preserved. FullRuby root-owned exactf6f76/3b238 PASS708s retained,
not rerun byI1. No app/native/systembuild/evaluation campaign or CIwatch. New
clean detached runtimef6/configfdcb targets and declared environments are ready;
config hooks active/signed and Nixfmt+RuboCop PASS. Initial configworktree checkout
hook lacked ambient gems after completed checkout; inspected clean effects then
normal frozen-Nix install/sign/run joined0, no bypass or sourcechange. Comparison
capture command-lock refusal was retried only after other capture joined; both
final comparisons captured. All own commands/effects joined.

Final workspace integration prep STOPPED when shared master advancedf174 to
a5785088973ce914bfe6db001149f6adbbcb5971 (1commit,1012work/archivepaths only,
no product delta). Shared staged index changed concurrently; own commands never
wrote it. No rebase of root's active buildinput0c9 or default/claim intervention.
Root needs to release source/read window and allocate equivalent successor before
workspaceFFcommands. Package parked at this explicit dependency; no next work.
/tmp/pi-message-delivery-D14-{final-pins,graph-proof,integration-targets,
integration-baseline-movement}.json plus D14-integration-commands.txt and raw
quick/publication/patch receipts retain exact histories/sources/NAR/commands.
Earlier deployment proofs/backups untouched. No claims/defaultwrites/live/native/
deploy/lifecycle byI1. Product docs need no update for these mechanical pins;
reviewed D14 runtime owns behavior documentation. Root owns mechanical lock
reconstruction, final artifact/native/CI/approval/recovery/deploy/integration;
final pin findings remain I1-owned.


### D14 required native PASS and root-operation preparation

Root's ONE native run2234 joined EXIT0: pre/native/command/post/final all0,
elapsed52s; exact TestPiTeamConflictRetainedWorkerRecovery PASS13.95s/noSKIP.
Frozen b3/tree d25 and final g5/actual source/immutable input pre/post guards
passed. Raw log /tmp/pi-d14-native/native-only.log SHA256
856112f595d0f4034ef740f034b50245974387c3c5daad5754f27c658ad757f1; result
SHA256 a22c99b06743ddb928275182f41565bcae36aa6fb714c4f681c3516b4b8862b5.
This covers finite retained native recovery/replay/public admission/later send.
It does not induce the new terminal class (finite four-pair+qualified producer
proof remains separate), execute an old supervisor binary, prove real systemd
drain, or certify live peer eligibility/recovery. Root also reported exact-b3
CI45655170251 SUCCESS; I0 did not start another CI observation.

Concrete D14 root-operation command/identity/verification recipe prepared in
ignored+untracked0600 private/d14-recovery-{command,command-identity,verification-recipe}.json.
D13 command/audit untouched; same original argv tail/UUID/selector/source identity,
only executable changes to exact g5. New record executionAuthorized=false pending
NEW user approval; D13 authorization does not carry. Fresh root profile/binding/
all-owner/worker continuity and exact durable before/after phase are still required.
Nonzero/EOF/timeout requires effect reconciliation, never retry/new UUID/resend.
I0 performed no live/native/GET/attachment/operation/activation/build/default/claim
action. Source/index b3 frozen; all prep children joined; root owns approval,
activation, ONE normal public request and integration.


### D15 committed continuation correction — review handoff

Owner I0; source/index frozen and released. Runtime worktree
`worktrees/2026-11-23-pi-message-delivery/dev-workspace`, branch
`2026-11-23-pi-message-delivery`. Consumed base
`b3dd92cc6f61f697fc61c12fa0b5246511e93f4f` is unchanged. Final head
`fd03ce2a879fe071e73be0e9353ba0ccbe1de249`, tree
`41f6f94b033f4f1c20a31132caa05fab69acf0cb`; clean worktree, normal commits/hooks.

Complete new series (oldest first):
- `85e1edf964d7e93348a7b22b7a96c1e19b0527e4` — phase-specific settled/complete
  drain replay, owning core regressions/comments and historical-drain guide text.
- `fd03ce2a879fe071e73be0e9353ba0ccbe1de249` — recovery-only newer-reader/frozen
  execution-target guard, owning HTTP tests and continuation guide text.

Combined delta: five owned paths, 396 insertions/8 deletions. Production changes
are only `portal/internal/piruntime/team_conflict_recovery.go` and
`portal/internal/web/pi_runtime_upgrade.go`; their existing owning test files
and `docs/pi-runtime.md` supply the remaining scope. No source/dependency pins,
new framework, schema, field, Kind, capability, wire, H0, worker or CLI change.
No migrations. No superseded D15 approaches or repeated dependency/update streams
remain. Full unmerged history above protected f6 is consumed D14 b3 followed by
these two focused corrections; b3 and its final review/native receipts stay
protected because the retained operation has consumed its journal/execution
contract. D15 does not rewrite that target or operation.

Accepted end-of-design.md invariants: prepared first settlement still proves
terminal identity, fresh drain and offline equality; settled/preparing keeps
fresh drain. Settled/exact-starting uses immutable historical Stop while ordinary
Ensure owns exact readiness/attachment/Load. Published replay retains history/
mapping/receipt checks without host/native/drain/Load/clear/Publish; complete
without publication refuses. The HTTP exception is only a valid team recovery
for the current saved UUID, preserves the complete saved Start and validates
current selected reader independently. Ordinary/retirement target rules stay.

Meaningful tests-only old-red on b3: same populated successor cgroup rejects
starting and partial-Load continuation using production verifyCurrentDrainAt;
newer-reader HTTP case passes real admission/package validation, reads saved
Start exactly once and fails the old guard before Manager. Definitive log
`/tmp/pi-d15-old-red.log`, SHA256
`0419d7a99eeefa9e735a1474ccb7b3440df7a883a8eb7f8247b393f068677675`.
Earlier fixture/setup runs are retained separately and are not this receipt.

Related quick-green on the exact committed source, before commit bookkeeping:

```sh
PI_PROBE_PACKAGE=/nix/store/nvwxl97fj19gvy9bnvr8s485jpn5hjmm-pi-1.5.2 \
PI_START_RECOVERY_PACKAGES=/tmp/pi-d15-package-inputs.json \
nix develop .. --command go test -mod=readonly ./internal/piruntime ./internal/web \
  -run '^(TestTeamConflict|TestPiRuntime(Upgrade|Recovery)|TestPiTeamConflict)' \
  -count=1 -timeout=90s -v
```

From runtime `portal/`, EXIT0: core48.513s, web25.341s; no skips/failures.
`/tmp/pi-d15-green.log` SHA256
`22e852740d20458a29ae148794c33b00edd06b3838584f8a352404917a608dc5`.
Gofmt and final base-to-head diffcheck pass. New production-drain regressions
cover same-group starting/partial Load, fresh prepared/settled-preparing refusal,
changed Stop/SourceHost/successor/Start/selector/current/phase/history/receipt,
failed handshake, capability refusal and zero-host/drain historical completion
with later input/independent hold. HTTP cases cover unchanged full Start/result,
wrong scope/binding/profile path/predecessor/generation, stale current reader,
propagated saved-capability refusal, and ordinary/retirement target/profile-only
refusals. Existing same-UUID checkpoints include no-journal reservation replay;
D14 mixed pairs, receipt precedence and old-prepared digest cases remain green.
The finite fake worker uses pinned package metadata, without SDK/model execution.
HTTP actual saved capability validation remains covered by owning Manager tests;
its fake backend only checks route preservation/propagation.

Final committed Ruby rebind (evaluation only, no rerun):
`/nix/store/f6f76jl1rfvyibvb9dll0h2i4rp70dic-dev-workspace-ruby-verification.drv`
→ `/nix/store/3b238sl6jh4q9hhi3ckqzdjxb5fpc6kc-dev-workspace-ruby-verification`.
This exactly matches root's retained full PASS708s. Rebind receipt
`/tmp/pi-d15-ruby-rebind.json` SHA256
`7790b970ec90450b4c872a84a96b93634a9ed1cad7943ad24f091d97d016c72f`.

Documentation routing/fidelity: recovery operator/reference and supported
continuation → README-linked `docs/pi-runtime.md` existing team-conflict section
→ implementation and finite checks above. Root's final writing-skill prose is
applied unchanged; existing anchors, original selector/UUID, no-resend, later
input/hold, reader-marker/rollback and legacy-source warnings remain. Individual
execution evidence stays in session/private records, absent from product docs.

Risk high: persisted recovery and compatible-reader continuation. Proposed
review lanes general, architecture/repetition, scope/proportionality and
risk/compatibility; root owns retained reviewer assignment and acceptance.
Owning component is piruntime Manager, consumed by the existing web Upgrade
handler and CLI/public request; no backend-neutral interface change. Existing
D14 review conclusions remain scoped to unchanged files/behavior. New reader
artifact/native/composed/CI and actual continuation remain unrun for D15 and
root-owned after review. No publication, native/live call, build, operation,
claim/default/lifecycle mutation by I0. No all-callback live/recovery success
claim. All preparation/check commands joined; HOLD feature push pending review.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-23-pi-message-delivery/


### D15 accepted publication and parameterized native preparation

Root accepted reviewer0's exact b3..fd03/tree41f6 four-lane review, with no
findings and explicit history/migration/documentation conclusions. No source
changes followed. Canonical SSH normal nonforce feature publication joined0:
`b3dd92cc6f61f697fc61c12fa0b5246511e93f4f` →
`fd03ce2a879fe071e73be0e9353ba0ccbe1de249`. Fresh remote default remained exact
`f6d60bf87002fb1896599f35f0284743c16d7e6f` before/after; source/tree41f6 clean.
Direct I1 dependency delivery joined, message4f94c47f-84f1-4459-9a95-4c21b7538827.
Publication receipts `/tmp/pi-d15-publication-before.txt` SHA256
887b91e749b088ffaea69de060b79251a346d6ccbf63b5050dce5e024a6aeb63,
`/tmp/pi-d15-publication-after.txt` SHA256
dbcc2e8015c1f60b31e48e7a062bbae42936897c07d665e9140233fb8c8db344.

ONE exact-fd03 CI listing: run45680366014 in_progress,
https://github.com/aither64/dev-workspace/actions/runs/45680366014 . No watch,
retry or cancellation. `/tmp/pi-d15-ci-list.json` SHA256
b6663737b5c8cce73ce503b22cb38a61393f1f73db85bd8fec4a3f0b0fda6657.

Existing proven native runner copied to NEW `/tmp/pi-d15-native/` outputs,
preserving all D14 files. Same exact TestPiTeamConflictRetainedWorkerRecovery,
pi_native_fixture/count1/3m and explicit PASS/noSKIP enforcement. New manifest
binds fd03/tree41f6 and all1148 tracked hashes, rechecks unchanged originalg7,
worker/Node/SDK/catalog and old-equivalent supervisor/team sources; Ruby exact
f6f76/3b238 reuse unchanged. Candidate app/deriver/source remain unbound pending
root qualification; the precheck explicitly refuses while unbound. No SDK/native
execution. Prepared argv template:
`bash /tmp/pi-d15-native/run-native.sh <ROOT-qualified-reader-app>`.
Runner SHA256 b55ec62aaaeca3778d9360a4bd96ba9c4f2ad0f4e2345ee9ac96ab0c11e22596;
unbound manifest SHA256
7bfff8341828c1bd8dd360c3ae07be99f76511645fdb9fbcfe6b97cb1290d8bc;
unchanged catalog SHA256
ae8f48f8f11075db5a907b5347c76c0eeb349bc65a4f0995f92b05181e4ba094.
These hashes describe preparation, not artifact-bound execution readiness.
Allowed CLI cache warm first used repository root and refused for missing go.mod;
corrected command uses `go -C portal build`; logs remain separate under the new
prefix. Its output never substitutes the native test's own temporary CLI.
Operational command/recipe preparation is deferred until the actual reader
artifact exists, while original g5 Start/profile generation/digest/UUID and all
prior operation results stay untouched. Root owns artifact qualification,
activation, continuation and integration; no new live/probe/effect work by I0.


### D15 artifact-bound native gate and current-operation preparation

Root qualified reader `/nix/store/zygngjm2willvbg0bzsvciq2fmhjq278-dev-workspace-0.2.0`,
actual deriver `/nix/store/s10mb9zmy4mw02rz231a6vlzyjaz3h7y-dev-workspace-0.2.0.drv`,
actual source `/nix/store/2vy7dcrvvlr56966j8f2bhmnbyjab6fv-source`.
All1148 fd03 blobs and all9 fixed metadata files match; both reader markers are
exact integer1. Existing native runner's read-only input check passed with this
binding; manifest SHA256 ec86cc2767e1b970df8c080b91b9f9297f9d0b6c4bf2d219404c6f3d0d5a9b49.
Originalg7/Node/worker/SDK/catalog/Ruby inputs remain bound. Qualification proof
hash is informational; helper normalization is independent.

Root ONE native run94816 joined0: pre/native/command/post/final all0, elapsed36s,
TestPiTeamConflictRetainedWorkerRecovery PASS11.78s/noSKIP. Root also accepted
app+fivechecks91s and exact-fd03 CI45680366014 terminalSUCCESS (essentials and
creation success; three extended jobs skipped). I0 did not run SDK/CI again.
Native limits remain finite old-source-equivalent supervisor, synthetic host
termination/drain, no old-binary/real-systemd/live restoration or terminal-class
induction claim.

New private D15 command/identity/recipe mode0600, ignored+untracked. Exact original
argv tail/UUID/selector/source/origin/socket preserved; only executable changes
to readerZyg. Whole saved Start/profile generation/digest/application stay G5.
Original D14 record/results untouched; D15 executionAuthorized=false pending
root release within existing approval. Command SHA256
64bca18cbbe0fa04e791471e14bf94f5c7a0bdd379cca3cbe1b01aa9c957a9fd;
identity SHA256 721114fa85696209bfa8147d333105802de85455b9bb7fd66a047b4c71e6a8b3;
recipe SHA256 f1dbc495c11cb4ad49da022438387a77ebc88444e4afafc6599ba367f36d8332.
The selected reader must be Zyg after activation, while successful saved result
AppStorePath and execution Start remain G5; no journal retargeting.

Root-released fresh LOCAL before-reader-switch snapshot joined0. Selected reader
stillG5; exact current settled/Stop-present/starting phase, Start/runtimeConfigSHA,
current pointer/authority/unloaded owner mappings/history/receipts/binding/roster
unchanged from last joined local afterimage. All8 Pi runtime identities captured;
target supervisor identity and non-target7/system/native Codex unchanged. No
pre-Stop reset. Private d15-reader-switch-before.json SHA256
c191bbe51dbd937870d2521bad4358b38262732c92d99427413431f253565ffe.
Existing local snapshot adaptation private/d15-recovery-beforeimage.py SHA256
fb0ce5f46f3ee616d1f40c5373b2c9133a48431a095bcdba1e9efa5ac2f7e46f
supports before-reader-switch and after-reader-switch modes. After root signal,
the latter verifies selectedZyg, exact actual portal argv with only reader artifact
replacement and all8 continuity, then saves a fresh current-operation beforeimage.
No HTTP/native/H0/probe/attachment/Load/operation by I0; all commands joined.
Root owns activation, ordinary continuation and integration; I0 retains local
post-switch/phase/effect/history verification and any failure diagnosis.


### D15 reader-switch refusal: bounded local effects reconciliation

Root original activation28016 joined EXIT1/32s with only reported error
`session backend compatibility: Pi current runtime and ready authority disagree`.
No recovery request followed. I0 did not run the success-only post-switch mode.
Fresh bounded local reconciliation joined0: selected profile remains G5; portal
PID/start/argv match before-switch baseline. All8 Pi runtime unit/PID/start/worker
tuples, system and native Codex unchanged. Exact identified files and durable
inventory (history/receipts/binding/roster/authority/owner mappings), raw runtime
and saved journal unchanged. Current remains settled/Stop-present/starting with
exact frozen G5 Start/runtimeConfig/digest/UUID. These checks show no observed
selected-reader/portal/runtime/durable effects within their scope; they do not
certify unrelated transition state. Private mode0600 ignored+untracked receipt
`d15-reader-switch-failed-after.json` SHA256
75785f12aa09fce17f1e2fecb807badc14733fca36563f9abb8612534899e9a2.
Root received first result promptly; routine factual join sent to architect0,
who owns compatibility source investigation. I0 retains exact effects diagnosis.
No H0/native/HTTP/probe/attachment/repair/retry/operation/source action. Source
fd03/tree41f6 remains clean/frozen. Machine remains held under root authority.


### D15 package-selection continuation — committed affected-review packet

I0 package complete; source/index frozen and released. Runtime worktree
`worktrees/2026-11-23-pi-message-delivery/dev-workspace`, feature
`2026-11-23-pi-message-delivery`. New focused commit above accepted fd03:
`3a60fc316b41461283dd11a1b39affb1da41e2bd`, tree
`323cd6cd07c517350dd7ec00d68a868e7b002497`. Clean worktree; normal hooks.
New range `fd03ce2a879fe071e73be0e9353ba0ccbe1de249..3a60fc316b41461283dd11a1b39affb1da41e2bd`:
12 owned paths, 576 insertions/29 deletions. Full unmerged series above protected
f6, oldest first:
- b3dd92cc6f61f697fc61c12fa0b5246511e93f4f — consumed D14 typed terminal proofs.
- 85e1edf964d7e93348a7b22b7a96c1e19b0527e4 — historical drain replay.
- fd03ce2a879fe071e73be0e9353ba0ccbe1de249 — newer reader/frozen target.
- 3a60fc316b41461283dd11a1b39affb1da41e2bd — package-selection continuation.

No migrations, persisted fields/schema/Kind change, authority mutation, pins or
repeated update streams. No obsolete unmerged iteration/fixup commits. Prior b3,
D15 commits, qualified Zyg and failed activation records remain unchanged: b3's
G5 journal/execution is consumed; fd03's reviewed reader artifact/activation
attempt is retained. This separately focused third correction is explicitly
lead-authorized; prior accepted four-lane reviews remain scoped to old changes.
No push, long check or operational action in this package.

Implementation follows the accepted end-of-design.md brief and its normal-path
amendment. The existing Go retained R pass completes all mandatory journal,
source/successor/Start/SourceHost/Stop and mapping identity/codec validation and
claims. Only additional unfinished-transition qualification may omit its optional
projection (afterimage, actual history/receipt or saved-target capability failure).
Cancellation remains an error and mandatory traversal continues. A positive exact
current settled/starting relation becomes schema3 piRuntimes.teamConflictRecovery,
with only requestId/sourceGeneration/bindingRevision/phase=settled. Ruby strictly
validates shape and joins ready predecessor authority/current binding. Mismatch
requires positive proof and exact candidate-reader piTeamConflictRecoveryTransition1
alongside base1. Matching ready/current authority keeps prior behavior. New marker
qualifies only switch candidate reader, never frozen G5 execution target. No
readiness/publication/no-effect assertion follows from omission.

Meaningful old-red: actual finite recovery settled/currentstarting in a populated
same cgroup, production Go inventory → old Ruby rejects exact current-runtime /
ready-authority mismatch; Go0.768s/noSKIP. Log
`/tmp/pi-d16-owning-old-red-final.log` SHA256
f9ef28003270e056f8270fe4d165052e2fdd37743ae70631441c2cd4a7f58c0a.

Checks (declared Nix shell; explicit PI_PROBE_PACKAGE pinned metadata and
PI_START_RECOVERY_PACKAGES=/tmp/pi-d15-package-inputs.json, B exact G5):
- Related Go core/cmd batch: all unchanged baseline R cases passed; sole new
  public fixture setup failure isolated. Cmd preflight projection/actual existing
  Ruby scanner bridge PASS3.973s. Core full batch53.748s is retained as partial
  evidence, not an overall green receipt.
- Accepted amendment: TestTeamConflictPublishedTransitionKeepsNormalAuthorityPath
  PASS0.79s (settled but Published, later valid user entry + independent hold;
  inventory ordinary match succeeds, mismatch without projection refuses).
  TestTeamConflictTransitionInventoryRefusals PASS4.79s: excluded phases, static
  source/Stop/selector/Start corruption, omission for extra mapping/history/receipt
  or unsupported target qualification, unchanged durable bytes/zero host/drain.
- Final exact failing public fixture fixed and rerun ONLY:
  `go -C portal test -mod=readonly ./internal/piruntime -run '^TestTeamConflictPackageSelectionTransition$' -count=1 -timeout=45s -v`
  PASS2.304s/noSKIP. Real owning inventory is reread at every Ruby boundary by the
  existing subprocess fixture. Public --from-candidate entry rejects old candidate
  before profile selection, checks exact unselected executor/current profile,
  exclusive revalidation and selected activation capability. No synthetic success
  boolean replaces journal proof. Durable owner/runtime bytes remain unchanged.
- Ruby backend current_runtime/team_conflict: 4 runs/70 assertions/0fail/0skip,
  0.063s. Ruby host affected existing candidate/creation/selected tests:
  8 runs/106 assertions/0fail/0skip,1.399s. Strict null/extra/missing/duplicate/type/
  phase/source/binding/authority/marker refusals and normal match retained.
- Gofmt, Ruby syntax and final base-to-head diffcheck pass. No SDK/model execution:
  finite supervisor/worker fake with immutable saved-target metadata. Fixture
  setup failures (declared sorted account scope, required workspace directories,
  actual selected predecessor/exact candidate identity and Minitest nil assertion)
  are preserved separately; production guards were never relaxed for setup.

Final logs: /tmp/pi-d16-public-joined.log SHA256
8b2958a4d1d2db30b4810a35b716b69eec24bcdfc57ee2e29d546b85ab3e36d4;
/tmp/pi-d16-affected-green.log (one resolved public fixture failure plus passed
amendment cases) SHA256 7cd0beeaf8f69ce8b3e3d1072e86a1de90197cdfa1ba00529c5dc6e7743744c7;
/tmp/pi-d16-ruby-backend-green.log SHA256
bf4a70e272f1736fd9d359639322f6e7f8c8a19a96a96a764188253c03d5c06e;
/tmp/pi-d16-ruby-host-green.log SHA256
37b532b9560ec4444dfddbb12ce86e57fbaeb3829151f0da733a9bc7b2c00380.

NEW exported full Ruby identity, evaluation only:
`/nix/store/s56c14cllrb2afc7x42dn3jmr1y7yhd4-dev-workspace-ruby-verification.drv`
→ `/nix/store/pw1vprwvs3ipvyqdhh0j37zz0ii8sakp-dev-workspace-ruby-verification`.
Owning literal recipe after review:
`nix build --no-link --print-build-logs .#checks.x86_64-linux.ruby-verification`
from frozen runtime worktree, with exact drv/output precheck. Receipt
/tmp/pi-d16-ruby-rebind.json SHA256
2f0b3646d69e37e96b508539bfc2db62fd35a50674ae19a7003318cb61820289.
Old full Ruby f6f76/3b238 PASS708s has OLD input scope and cannot cover this change.
Root owns new full Ruby and justified package/composed checks after review.
Worker/Node/SDK/provider sources are unchanged; no additional callback/native
campaign is allocated. New artifact metadata intentionally adds exactly the
transition marker instead of claiming prior nine-file equality.

Documentation routing/fidelity: operator recovery/package selection reference →
README-linked existing docs/pi-runtime.md team-conflict section → retained pass,
Ruby gates and finite evidence above. Exact lead-supplied humanized paragraph
applied with line wrapping only, no factual mismatch; existing anchors, UUID /
selector/no-resend, later-input/hold and rollback/legacy warnings remain. Individual
failed switch and target identities stay private/session evidence. Scope high
(persisted continuation/mixed readers/host selection); root invokes retained
reviewer for all affected lanes and whole-series/history/migration conclusions.
The reusable interface owner is piruntime retained inventory → existing CLI
preflight schema3 → Ruby backend/host switch consumers. No H0/SDK/worker or public
recovery API change. Live eligibility remains unknown; root owns machine,
corrected candidate --from-candidate activation, sameUUID continuation/integration.
All check/prep children joined. HOLD publication pending review acceptance.


### Package-selection review accepted and feature published

Root accepted retained reviewer0 exact3a60/tree323c all four lanes plus complete
history/migration/docs, NO FINDINGS (review.md; /tmp/pi-d16-reviewed.json).
I0 publication joined0: normal NONFORCE canonical SSH feature FF fd03 →
3a60fc316b41461283dd11a1b39affb1da41e2bd, clean tree323cd6cd07c517350dd7ec00d68a868e7b002497
pre/post. Fresh remote default remains f6d60bf87002fb1896599f35f0284743c16d7e6f.
No rebase/source change. Direct I1 receipt b6f83fd0-648b-456c-b772-9fc3fb4ae442
joined, explicitly no functional pin mutation until root allocation.

ONE exact-newhead CI listing returned run45689485677 in_progress:
https://github.com/aither64/dev-workspace/actions/runs/45689485677 . No obsolete
active run was listed; none canceled. No watch/retry/current-head cancellation.
Publication-before SHA256 dbcc2e8015c1f60b31e48e7a062bbae42936897c07d665e9140233fb8c8db344;
publication-after SHA256 3a98fa106b46cba0d39cb5677fd698a494de51cc17a4a02f0c1444474cdc7c30;
CI listing SHA256 add8459993d2aaafc17cbb2ad5c1d52793df7823ad8c4cb830833002bc9ce1cd.
All /tmp/pi-d16-* records preserve older D15 artifacts/attempts. Earlier failed
aggregate batches remain partial evidence; exact corrected case is green, no
aggregate PASS claim. Root owns new full Ruby s56→pw1 and later artifact/ops
allocation. All I0 commands joined; source/index frozen, parked/capacity available.
No native/app/live/activation/recovery/default/claim/lifecycle action by I0.


### D16 qualified reader operational preparation and fresh local gate

Root qualified reader /nix/store/gdjizaalss4banjmls2l3ah7ljdb3m3q-dev-workspace-0.2.0,
actual drv /nix/store/7jl6nlppkfrc96lkg55dz32757w4cp57-dev-workspace-0.2.0.drv,
actual src /nix/store/5pnplssw3qqbjj0yii5dj27d9wzmx5vr-source, runtime3a60/tree323c.
Root composed app+fivechecks PASS112s/postidentity0; source proof all1148 blobs,
eight fixed metadata files equal G5, only runtime-contract addition is exact
piTeamConflictRecoveryTransition1. Base/terminal/transition are all integer1 on
reader; execution stays frozen G5/lydin73/ib1 without a new target marker.
No native rebind/run allocated for this package-selection-only delta.

Root reported exact CI45689485677 terminalSUCCESS (essential+creation; three
extended skips), helper supplement PASS and reconciled full Ruby s56→pw1 success.
Original watcher60029 EXIT127/711s remains preserved: root-edited executing shell
launcher caused read-offset/log corruption. Recovered daemon log, exact valid
output/deriver and offline cached confirmation with builds/substitution disabled
establish the successful Nix output without rerunning suites; authoritative
receipt /tmp/pi-d16-ruby-reconciled.json. I0 launched no long check or extra poll.

NEW ignored+untracked0600 command/identity/recipe/script preserve all D13/D14/D15
records. D16 argv tail/UUID/selector/source/origin/socket exactoriginal; only CLI
executable becomes GDJI. readerProfile is distinct from full frozen G5 Start /
profile generation/digest/runtime-config/Stop-present execution. Success
AppStorePath remains G5. authorizationfalse, no inherited audit; root alone
releases the already-approved operation. Literal canonical activity, thread/page
and deliveries GET routes, full URLs and original scope/socket/origin are saved
privately from owning source contracts; no GET was performed or released here.

Private artifact hashes:
- d16-recovery-command.json c5d004689ac83fbdba74f1c20ecbc673f05dcbc40a910cf5415cc527ac16cef8
- d16-recovery-command-identity.json c27ceab7642ab23c54ffe28fcfaa89754dd293d24cbbabe36f6a670676aff7d6
- d16-recovery-verification-recipe.json 207a6fa3a25ba3157e4ce533fe38fe21e4ffa8dcfda37bc68e87b4be0f9facc4
- d16-recovery-beforeimage.py ef4cfa3da821169546276314ea50351c1632878cc6a2a05763626379bcd6a740

After root joined final gates, I0 executed ONE allocated LOCAL before-reader-switch
snapshot, joined0/0.828s. G5 still selected; actual full portal argv and normalized
13 fields match. All8 Pi tuples captured; exact G5 successor identity retained,
non-target7/system/native Codex unchanged. Exact current journalsettled/Stop-present /
starting runtime/whole Start/UUID/current pointer/authority/unloaded maps/history /
receipts/binding/roster inventory match last saved failed-switch afterimage.
No pre-Stop reset. d16-reader-switch-before.json SHA256
06ad4b7472b7c443191ff23bd6bf4b60abad0c9a08046e0ae1909da3867bb977.
No after-switch beforeimage exists yet. No HTTP/H0/native/Inspect/attachment /
operation/activation by I0. Root may execute its public exact-source GDJI
--from-candidate switch under held machine; I0 awaits its joined result before
post-switch local mode. All clients joined; source/index3a60 remains frozen.


### D16 activation joined and post-switch recovery beforeimage

Root original switch42461 joined EXIT0/163s, no retry/intervention and driver
hash unchanged. I0's bounded wait inspection found both exact original processes
already exited; saved result/log confirmed completion. Former lock cause was not
observed and no cycle/self-lock conclusion is claimed. Private wait receipt
SHA256 35e9ad086cbe29859c592d465a6a5cac60a04c339a1e674c14fa51d68f7ee6b4.

Initial after-reader-switch LOCAL mode refused at the extra full-argv expectation,
before writing a fresh beforeimage. Exactly two --cluster-provider helper prefixes
changed from old2kp tools to qualifiedbh1 tools; normalized13 configuration/executable
fields matched only the G5→GDJI reader change. Refusal private SHA256
95a362f4bd225b53fc1343796148def1f9e1eb570db693b4b41f212967f46f63;
direct fresh-baseline normalized13 join SHA256
d3e6e92088e16c4da1f12caab7424a1a001522602bd9cd96ac85c6b1ad3552dc.

Root accepted only the two exact declared vpsadmin/vpsadminos descriptor paths
using /tmp/pi-message-delivery-3a60-pins-final.json /artifact_helper_supplement.
I1 confirmed same extension source nma/bf12/all19 canonical inputs, normalized
whole-tool derivation/extension descriptors with only declared source/output path
rendering, and intentional copied contract transition1 addition. Those two
executables were not separately byte-compared; no whole-closure/all cluster
behavior equality claim. Old script and refusal records remain preserved.
Only the exact two expected private argv values changed; other argv and actual
normalized13 checks remain strict. Corrected script SHA256
7790cc15e1c3796a234b95fb01f3a9aaf51eec8b07e680f8c4157dae5a2f53d1.

ONE root-released corrected after-switch LOCAL run joined0. GDJI selected;
full expected argv/normalized13 pass. Frozen G5 whole Start/profilegen/digest /
runtime-config/UUID/journalsettled/Stop-present/currentstarting, current pointer,
authority/unloaded maps/history/receipts/binding/roster remain exact. All8 Pi
identities, non-target7/system/native Codex continuity match fresh D16 baseline.
Fresh private d16-recovery-before.json SHA256
494207468aecda5442932a460950372518f93deb5abd66c0768a4d659b35f157.
Command hash c5d004689ac83fbdba74f1c20ecbc673f05dcbc40a910cf5415cc527ac16cef8
unchanged/authfalse. All clients joined. No HTTP/H0/native/Inspect/attachment /
operation by I0. Root owns approval binding and one ordinary sameUUID request;
I0 remains parked for its result and local phase/effect/history reconciliation.


### D16 ordinary continuation positive: exact local completion proof

Root ONE ordinary sameUUID request17972 joined EXIT0/11.320698s; unchanged driver,
original argument tail/target/UUID, no Send/new request/private operation. Root
bound existing approval to the exact fresh beforeimage and preserved the
preauthorization record. Public result ready/recovered-team-conflict names frozen
G5 target and exact saved successor/previous/selected operation.

I0 first local read promptly confirmed journalcomplete/Stop retained, exact
saved Start/current successor and published ready authority, sixLoaded mappings.
Durable current.Phase=starting remains the existing intent marker and is not a
failure alongside that positive completion/authority proof.

Detailed owning-recipe LOCAL verification joined0/0.841s, PASS18/18. Whole journal
matches saved evidence except Phase completion; Stop/Start/profilegen/digest /
UUID/selector unchanged. Six loaded mappings retain native IDs/CreationID/HistoryRef,
settings/initialsettings/instructions/policy. Five persisted histories keep exact
paths/prefixes and no suffix/user entry appeared. Proved-empty owner stays
unpersisted with both old/new planned locator absent in its exact owned directory,
receipt-free and original reservation unchanged. All110 original receipt files
byte-identical, no new receipt. Binding/roster/reservations unchanged. Exact G5
supervisorPID/start/unit identity did not restart; one new observed shared-session
worker serves the six mappings as the owning Load afterimage. Non-target7/system /
native Codex exact; GDJI selected and strict fullargv/normalized13 remain correct.
Seven identified file changes all fit permitted afterimages; no unexpected durable
change. No HTTP/H0/native/Inspect/attachment/replay/operation by I0.

Fresh ignored+untracked0600 private d16-recovery-after.json SHA256
9db2cfada097d3ac2aa15d14b44efb49b5e9851da4fc8f73c2a329036c056c7c.
All commands joined. Root received proof before target GETs and owns those three
exact ordinary monitoring/threadpage/deliveries requests. No monitoring/admission
restoration claim is made by this local proof alone. Source/index3a60 stays frozen;
root retains integration/claim/machine authority and I0 retains failure diagnosis.


### D16 first public activity404: bounded route/transport classification

After accepting local18/18 completion, root issued only the first prepared
activity GET and preserved its404 body. Page/deliveries were not requested.
I0 inspected only saved request/recipe/body and owning route sources. Exact
canonical /codex/conversations/<saved slug>/activity is mounted; slug/defaultlead
parsing is valid and namespace recomputes exactly from accepted conversation
identity. Unix socket/URL path/Host/scope follow the recipe. The driver omits
Origin, which pinned codex-web2547 explicitly permits for GET/HEAD.

Body is exactly JSON error `conversation is unavailable`: pinned backend handler
emits it for either ResolveBackend failure or resolved operations Verify failure,
before activity execution. Plain missing-route errors differ. Therefore no
literal route/transport correction or alias retry is justified, and missing
resource/generation/admission/native-verification cause cannot be inferred from
that body. Smallest missing evidence is the existing logger line for this exact
GET (`resolve conversation` versus `verify resolved conversation`, underlying
error). No new request/native/H0/probe/operation or source edit by I0. Local
complete/authority/sixLoaded proof stands; monitoring/admission remain UNPROVED.
Private route diagnosis SHA256
c3e2f5742b2c7a28186adfd61f8f7f751e0f52f72c699c17c503d2e1275a9fd7;
original404 preserved. Root received concrete classification promptly.


### D16 first404 owning gate identified from one log window and static catalog join

Root released ONE existing portal journal window,22s around the saved response
mtime, restricted to owning unit/saved portalPID. Read joined0:12records, one exact
activity match. Diagnostic names `resolve conversation: Pi runtime operation unavailable`,
not returned Operations.Verify; activity404 total71.15ms, admission/native_wait
unmeasured. Raw private receipt SHA256
869852ed60a7bda893dce2675d79225d30b8c334d6be73a97f7265ee9986854f.
No adjacent target subcause was logged and no second log query was made.

Adjacent owning source exposed the deterministic pre-BindRead lead-access gate:
projectPiConversationAdmission calls piSavedAccessLocked; original lead wire lacks
explicit Access, so it currently requires the selected reader's installed team
catalog digest to equal the saved creation intent's DirectTeam catalog digest.
Exact local immutable/static join: saved team catalog differs from GDJI, but
matches the original retained G7 image; current-reader and original catalogs differ.
That mandatory gate returns ErrUnavailable before read binding. It is not a route,
namespace, Origin or transport defect. Private predicate receipt SHA256
c30b79c125b4a7f0b43dafd87ad88c55f11495b9a66fd6e1cf1ef4a39d740261.

Root and architect0 received the source/predicate facts. Architect notes correctly
that later BindRead can itself perform a native identity/capability read; no claim
that resolver binding is wholly local or that later native gates are proven.
The established early lead catalog failure suffices as the current blocker.
Smallest forward-remedy boundary is an architect-owned compatible original access
proof from validated original catalog/Start, preserving current reader/frozen G5
execution and complete operation state. No new default grant, state edit, alias
retry or operation replay is justified. I0 made no source edit/additional HTTP /
H0/native/Inspect/probe/repair. Original404, completed journal/authority/sixLoaded
and local18/18 proof preserved; monitoring/admission remain UNPROVED.


## D17 retained lead access — committed quick-green, held for review

I0 delivered one focused commit above deployed `3a60fc316b41461283dd11a1b39affb1da41e2bd`:
`c72734bfadc411359587d18e45ec8618dd7f3213`, tree
`5f2fa4408bd003edeb1b07ef9052b1bfde07a9b1`. Runtime source/index clean and frozen;
no push, build, native/live request, activation or recovery replay allocated/executed.
Six owning files: three production Go owners, retained-catalog fixture prerequisite,
strict finite retained-lead tests, and the supplied eight-line Pi team guide paragraph.
Diff 562+/32- includes 477 lines of strict metadata fixture/owning finite tests;
production delta 74+/32-. No migrations, new persisted fields, schema, capabilities,
protocol or package-selection change.

The shared retained-lead-role lookup preserves the current-catalog fast path.
For differing team catalogs, it reuses the original ready creation-journal/intent/
ReadInitialStart tuple join even when provider catalogs match; canonical original
root plus strict Managed installed catalog must prove saved catalog/team/role and
explicit access. Saved-access and team participant consumers share it; participant
still overrides model/effort/instructions from saved configuration before policy.
The global new-preset/source-team matcher remains exact-current. Fork/nonlead,
current binding/authority, provider and native/read verification stay mandatory.
Existing initial/per-request original package roots and ReadInitialStart retention
were confirmed by architect0/lead; no new retention mechanism. Actual later live
BindRead/Verify eligibility remains unknown and root-owned.

Tests-only old-red on unchanged3a60: actual activity resolver with strict A/B
catalogs, equal provider digest, original creation Start/journal and a current
successor authority returns404 before BindRead/Verify/Activity (all0), after owning
ready-session admission passes. `/tmp/pi-d17-old-red-fixed-fixture.log` SHA256
`6c96b7cee62aabfad21cfa1a4f8301c511c5b15b32426ae172fb313557461a41`.
The tests-only fixture at that milestone SHA256
`28ee0c0fd902a7e8c17580e650a805ef5e01d5b7cb9d4570719655610354b7e5`.
Setup-only attempts and failed partial batches remain separate; no aggregate pass
claim applies to those. Canonical native identity generation, sorted derived model
inventory and correct existing write-operation semantics were fixed in test setup.
Optional upload materialization was excluded from this activity/admission fixture;
retained runtime and original creation bytes remain strict before/after assertions.

Final related batch, same bytes normally committed (Git bookkeeping only followed):

```sh
PI_CATALOG_OLD=/nix/store/g7wvpp2nc9cvsa8pdf1azfdib80kkcjm-dev-workspace-0.2.0 \
PI_CATALOG_NEW=/tmp/pi-d17-retained-provider-metadata \
nix develop --command go -C portal test -mod=readonly ./internal/web \
  -run '^(TestPiRetainedLead|TestPiAdmittedActivityHTTP|TestPiReadyCatalog|TestPiRetainedModel|TestPiTeamAdmission|TestPiTeamActivity|TestPiForkWholeTeamSelectedReadonlyAndUnstartedReservation$)' \
  -count=1 -timeout=60s -v
```

EXIT0,12.638s,noFAIL/noSKIP. Log `/tmp/pi-d17-final-quick-green.log` SHA256
`053ff7366b9537693dcb64d5861fab4539cb078f17994ab871afd93e0fd65804`.
Current provider fixture is a strict temporary metadata input: original G7
provider/models copied, only first model evidence_ref given a synthetic suffix;
not an application artifact or native qualification. This gives genuinely distinct
provider digests for the existing retained-provider test; G7/GDJI have equal provider
digests and were invalid inputs for that mismatch test. No Nix build was needed.
Actual HTTP reaches BindRead/Verify/activity exactlyonce with no transcript or
native mutation. Original RO/WW remain exact through owning write-required plan
admission and participant/settings checks. Covers 26 provenance negatives, original
base/projected team digests, later read-binding/Verify/scope/authority refusal, and
existing current-catalog/nonlead/fork controls. Gofmt and diffcheck pass.

Ruby read-only eval JOINED0 on committed c72734bf:
`/nix/store/s56c14cllrb2afc7x42dn3jmr1y7yhd4-dev-workspace-ruby-verification.drv`
→ `/nix/store/pw1vprwvs3ipvyqdhh0j37zz0ii8sakp-dev-workspace-ruby-verification`.
`/tmp/pi-d17-ruby-identity.json` SHA256
`2f0b3646d69e37e96b508539bfc2db62fd35a50674ae19a7003318cb61820289`.
Exact unchanged inputs permit reuse of root's reconciled successful D16 Nix output;
no old711s runner rerun. Prior SDK/worker/native receipts retain only their actual
unchanged-input scope; no new native execution claim.

Full source series above default f6d60bf87002fb1896599f35f0284743c16d7e6f:
b3dd92cc6f61f697fc61c12fa0b5246511e93f4f →
85e1edf964d7e93348a7b22b7a96c1e19b0527e4 →
fd03ce2a879fe071e73be0e9353ba0ccbe1de249 →
3a60fc316b41461283dd11a1b39affb1da41e2bd → c72734bf.
Protected exact consumed/deployed package revisions and frozen operation targets
remain intact; no fixup/tidy iteration, repeated dependency stream or migration
introduced by D17. Lead owns full retained history review and final acceptance.

Documentation routing: retained historical permissions → operators/developers,
reference → README-linked `docs/pi-teams.md#retained-settings-and-caller-authority` →
shared helper and HTTP/participant/permission tests. Supplied final prose copied
verbatim with wrapping; surrounding warnings/anchors and runtime recovery guide
unchanged. Individual live effects stay in existing private D16 receipts. Rollback
to prior reader preserves data but still refuses differing historical team catalogs.

Next: retained independent final affected review, then root-controlled publication,
artifact/selection and bounded ordinary public reads. I0 source/index frozen and
capacity available; findings/fixes remain owned. Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-23-pi-message-delivery/


D17 final review accepted by root: retained reviewer0 all four lanes/history/docs,
no findings at exact c72734bf/tree5f2fa440; review.md and
/tmp/pi-d17-reviewed.json own that acceptance. Released feature publication joined0:
canonical SSH ordinary nonforce FF3a60→c727. Fresh direct remote protected master
remains exact f6d60bf87002fb1896599f35f0284743c16d7e6f before/after, local clean
head/tree unchanged, no rebase. /tmp/pi-d17-publication.json binds source and logs.
I1 dependency receipt joined0 (a627cf10-e257-4168-8457-f9fc00491f30); pins remain
parked pending root allocation. ONE bounded exact-head CI list joined0: Check
45701141102 in_progress at c727, https://github.com/aither64/dev-workspace/actions/runs/45701141102.
No obsolete run listed, no cancellation/watch/retry. All I0 publication clients
joined. No fullRuby rerun/native/app/live/operation/default/claim/lifecycle action.
Completed G5 recovery stays complete and must not be replayed; root owns new reader
artifact/selection and ordinary three GET verification. Source/index frozen, I0
parked with capacity available and findings/dependent preparation ownership retained.


D17 reader-only local continuity completed after root original activation joined0
(elapsed3744s; YG3 selected). Fresh before snapshot c733e482613dada5c102eccbb6b2bac3b30426d609e833bb8846dca144fea7ec
remains immutable. First allocated after attempt stopped BEFORE runtime reads at
private script900614b6 source-worktree guard: independent reviewed UI head had
advanced to2268853e8f482c40fe6bbf744e7ecc9b9469fadd/treef60dac46253e83fe220e0b3262a8cdb592e62ab7,
while selected YG3 still embeds c727/pq07. Refusal68740af2 preserved. Root accepted
only this freshness expectation correction. Distinct private derived script
722e795011c2980f599fdc6ce2e89bb8ff82dc5ddb89e1170f095821a581083e and identity
eb27c1b56bac93cc0f8132d78b33dc2b8910a6c80c784920e789c29df19179cb preserve all
other original900614b6 bytes/assertions, including c727 immutable-reader identity.

ONE newly allocated local after execution JOINED0/PASS. Private afterimage
d17-reader-switch-after.json SHAe4b773f62db81dd118284a4a6ddd7b66d6f12df9fbfdbe4102deb330bb8724bb
(mode0600, ignored/untracked). Full argv changes exactly five entries: executable,
--dev-session and --package-root GDJI→YG3; two --cluster-provider BH1→0my declared
helper renderings. Normalized13 changes only PortalExecutable/PackageRoot.
All other full argv/config fields exact. JournalCOMPLETE/Stop/wholeG5Start/UUID/
digest/runtime/readyauthority, sixLoaded/nativeIDs/settings/instructions/policy,
histories/110originalreceipts/reservations and entire identified/durable inventory
remain exact. All8 Pi tuples, target supervisor/sharedworker, non-target7/system/
nativeCodex unchanged. No baseline reset, record adoption or operation replay.
Original script900614b6, baselinec733e482, reciped62417bf and refusal68740af2 remain
byteexact. No HTTP/H0/native/Inspect/attachment/operation/source/index action by I0.
All clients joined; root received localPASS before its canonical3GET release.
Root alone creates public authorization copy and executes reads; recipe still
HTTPAuthorizedfalse. I0 parked for public-result semantic diagnosis.


D17 root canonical public batch joined0: three exact ordinary GETs200, no
POST/Send/recovery replay requested. I0 saved-response semantic verification
PASS11joins; private d17-public-semantic-summary.json SHA
df959eccf2b1711052f3c72a0df12cea58abe123e68b6314a006ff0bf9c795d8.
Exact retained lead thread/scope, saved model/effort/provider, page idle with
inputDeliverytrue and metadataPendingfalse, and deliverycanEnqueuetrue/nonempty
selection/steer+followUp establish observed monitoring/history-read/input admission.
Frozen G5 completedafterimage proof reused; reader YG3 remains independent.
Observed activity2026-11-25T22:33:47.859Z (8.922ms before responsefinish), request
1.422818s; page1.898603s, deliveries0.495270s. All responses/hashes join root's
exact authorized recipe copy and beforec733/aftere4b; immutable originalreciped624
remainsHTTPAuthorizedfalse. Counts complete for returned root-thread scope; timing
coverage explicitly incomplete before worker attachment20:17:41.114Z. Earlier
timing and whole-team coverage not repaired/proven. Historical interrupted/error
row predates coverage/read window; no current read/enqueue block observed.
No new message/turncompletion tested or authorized, and no I0 HTTP/native/live
inventory/operation/source mutation. All clients joined; parked for root-owned
UI qualification/integration/release. Full bodies/native IDs/message content remain
private; original D16success/refusal/404 records preserved.


D18 final UI reader-only continuity: prepared scriptc7c37fc0/identity2aa3f903/
recipe8ae6b58f accepted, exact helper0my→s58 proof21c22f56 accepted by root. Three
clean freshness tuples runtimee310/91bc, workspaceb095/b318, config0b648/973 are
independent of previous immutable YG3/c727 and final3Y9/e310 artifact identities.
Root released ONE fresh local BEFORE only after peer-command preparation: joined0,
private before SHA f25f68d8eebb886dad923d1d84624c6448f3d3de0da47bbea7026ec4217c55b5.
No later content delta required adoption/classification; no reset to older data.
After root sole final switch49541 joined0/152s and selected3Y9, ONE released local
AFTER with unchanged script joined0/PASS. Private after SHA
30813817ab75d862d2f66310c31c153cfcf4d93c25a86f7b907171872ac36d8c.
Full argv changes exactly executable/--dev-session/--package-root YG3→3Y9 plus two
--cluster-provider0my→s58 declared renderings; normalized13 changes only
PortalExecutable/PackageRoot. All other argv/config fields exact. Entire identified
and durable inventory, completed G5 journal/Stop/Start/UUID/digest/runtime/ready
authority, sixLoaded/native IDs/settings/instructions/policy/history/original110
receipts/reservations remain exact freshbefore. All8 Pi identity tuples, target
supervisor/sharedworker, non-target7/system/nativeCodex exact. All three source
freshness tuples passed pre/post. Before/after mode0600/ignored/untracked, recipe
8ae6b58f unchanged/HTTPAuthorizedfalse. No I0 HTTP/native/Inspect/operation/replay/
source/index/claim/lifecycle action, no retries/adoption. All clients joined; parked
for root canonical3GET saved semantic verification. Root retains activation,
public authorization, integration and machine release.


D18 root canonical3GET batch47534 joined0/all200; I0 saved-response semantic
PASS11joins. Private summarySHAf5729d0986c37a6fb1a511ccb41bc1a3542f5c89705454778fda3d0527d8f4ef.
D18 page/deliveries are byte-identical to accepted D17 exact lead-native/scope/
selection/frozen-settings positives; fresh activity joins same thread/latest turn.
Page idle/inputDeliverytrue/metadataPendingfalse; enqueuecanEnqueuetrue with
valid selection and steer/followUp, exact saved model/effort/provider. No current
read/history/enqueue admission blocker observed. G5 completion/Start/Stop/binding
proof reused from immutable local after30813817; no new inventory or replay.
Activity observed2026-11-26T08:27:54.474Z,5.415ms beforefinish, request1.304879s;
page1.782543s and deliveries0.473987s. Allresponse hashes join rootbatch
789eef6fb66ec10b83debadb9ed0a1ffcafab90c50a8065bb03be762f998e638.
Timing remains root-thread only and coverageIncomplete before workerattachment
2026-11-25T20:17:41.114Z; no historical/whole-team timing backfill claim. Retained
interrupted/error row predates coverage/read window. No new prompt/modelturn
completion tested or authorized. No I0 live HTTP/native/operation/inventory/source
change. Root authorization copy and original immutableHTTPfalse recipe remain
separate; all clients joined. I0 parked; root owns integration/machine release.
