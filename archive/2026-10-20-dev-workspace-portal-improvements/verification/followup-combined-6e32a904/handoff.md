# Implementer0 follow-up handoff

B source/Git ownership ended by explicit lead transfer after publication. This
packet describes the exact handed-off source, not imp1's subsequent work.
No B source, index or refs are changed by these session-only preparations.

Published local-check checkpoint: **0ba320a5a7bba9234f4d713bf8e142fe10f000b4**.
SSH feature and clean tree independently confirmed by lead. Default remains
**968646471b1190c16a8cf60ff50736cd0525fa3f**. Current package is not changed.
This is not independent-review, long-browser, package or deployment acceptance.

## Complete branch and deployed provenance

Base: `968646471b1190c16a8cf60ff50736cd0525fa3f`.
Tree: `9a08c6e63515847594c74dd7630f0048f744de3f`.
The base retains integrated citation `52dcd47` and the short merge policy.
Complete diff: 60 files, 3,412 insertions, 390 deletions.

| Group | Exact head | Purpose |
| --- | --- | --- |
| 1 | `4a2fadd106d5eb9a7dcd92fb7ab28fb8cbd94458` | deps: update shared conversation presentation helpers |
| 2 | `db1e91ebd008f479cc1021b25e9756c588c5949a` | team: project full-team names from actual implementer counts |
| 3 | `b006196781869aec5d267b790ef0a839e4aa57dd` | portal: add authorized file downloads and source copy actions |
| 4 | `54169426248448119fd257ffbf3d652b1f3b5172` | portal: keep large artifact catalogs compact and stable |
| 5 | `7d9392e6643e8d856688ee1dc08ba86146f41ddc` | portal: publish session membership before optional enrichment |
| 6 | `5a764b28d654c9b00538f333fd550067da7a121d` | portal: retain member settings through sequential additions |
| 7 | `0ce92e8619f6b1ae9afbe8b6016ba8949c89036c` | portal: present team messages and decorated Markdown |
| 8 | `cee4cca19ad2fcf98ffb1317aff7876d784e26b5` | portal: show delivery recovery beside the composer |
| 9 | `1f162c38138b35bfe9b75b2b7a1af2f18f34e513` | portal: browse eligible session files in a lazy tree |
| 10 | `f6b72ad7af2eeff5673f5afe1e119f152ba0ef6d` | portal: retire paused read cycles and recover on tab resume |
| 11 | `efec474f8b74cd37acf5e2ad57bd3de9fec39dde` | coordination: derive claims from registered repository identities |
| 12 | `c48b5376075a9309a3a4a02f340afda55389a7f4` | portal: measure read stages without logging session content |
| 13 | `0ba320a5a7bba9234f4d713bf8e142fe10f000b4` | test: prepare ordinary Firefox acceptance across fifty native tabs |

[Final series/mapping](final-series.json), [complete series patch](final-series.patch),
[complete base-to-head diff](final-diff.patch), [file inventory](final-names.txt),
[diffstat](final-stat.txt) and [range-diff](range-diff.txt) are independently
inspectable. No default branch was rewritten or integrated.

Before consolidation the complete 13-group head was
`eeb84208ba3108f9c096e68da925fdd5611a7101`; [original series](original-series.json)
and [original patches](original-series.patch) preserve it. Local ref
`refs/safety/2026-10-20-dev-workspace-portal-improvements/before-final-a6e`
retains that exact head.

Exact deployed B `f8f2938b4e2cfd6e5b82657d08f014357817808f` is retained by the
local and SSH-published branch
`2026-10-20-portal-improvements-deployed-f8f2938b`.
The old deployed head is **not a literal ancestor** after the accepted pin
consolidation. Its seven other feature groups have identical stable patch IDs;
the original dependency group now selects final A. The original deployment
receipts, rollout and verification records remain unchanged. A's own deployed
852 safety branch also remains retained by its owner.

Reconstruction: read the original eeb tree into a disposable Git index, apply
only [the final dependency/asset delta](final-pin-and-asset.delta.patch), then
write-tree. The reconstructed and final trees both equal
`9a08c6e63515847594c74dd7630f0048f744de3f`.
Eleven of 13 ordered stable patch IDs match. Differences are solely the final
A pin/generated hashes/dependency body and conversation import v20 → v21 in
the browser recovery group. No rebase conflicts occurred. No extra dependency
commit remains. The two temporary fixup commits were autosquashed.

There are **no migrations** in this branch. Session manifests, lifecycle and
submission journals, coordination ledger and claim record formats are unchanged.
The separate immutable repository-claim capability document is not a state
migration. Supported active held/waiting identity checks refuse incapable or
remapped candidates; they never rewrite frozen resource keys or grant merge
approval. No migration was merged, released, deployed or externally consumed.
The earlier feature behavior was deployed under the exact preserved f8 receipt.

## One final shared dependency stream

A: `6e32a9043ee6367d92bfaf8d3ebdf48036e275f9`.
Go: `v0.0.0-20261021162553-6e32a9043ee6`.
Nix source: `sha256-m4qoKIWexEcOOxoGCF+cqDGm0SBrSRs5eC/f/l3iOyc=`.
Vendor: `sha256-H+MJMRgjG3PViA7REM822Z0s+Lri+gwD52wpwdpng68=`.
The parent utility derived the latter from the exact fresh Go-modules FOD;
its expected fake-hash mismatch is source preparation, not package validation.
The parent independently checked the structured result and build log under
`../followup-vendor-6e32a904/`; its final garbled excerpt is not authoritative.

[Source proof](source-proof.json) compares Go-module handler/client and all
eight embedded assets against exact A Git and Nix source bytes. Shared mounted
v21 imports sync v3/uploads v7; B imports v21. The pin positive/negative checker
passes, with no replace/exclude. Lock siblings/follows, bundled Codex and other
module versions are unchanged. No superseded pin remains in the final series.

## Focused checks and diagnostics

Final combined check logs are [Go](go.log), [deterministic Node](node-focused.log)
and [pin contracts/module identity](pin.log). They ran against the exact final
source tree before its byte-identical history consolidation.

- Go Files/source authorization/download bytes/citations/decorated Markdown,
  optional pending forwarding/member API/team observations, read diagnostics,
  details/limits and fixture journal matrix: PASS 7.043s.
- Deterministic Node read-cycle/providers/attention: PASS 92/92, 6.998s.
- JavaScript syntax, exact pin positive/negative contracts, source identity,
  lock-sibling equality, full-range whitespace and exact tree proof: PASS.
- Earlier Files focused batch: PASS 3.915s. Browser read/core forwarding batch:
  PASS 92 Node cases 6.961s and Go 2.616s against A852, now followed by final A6e
  checks above.
- Dynamic claims: `ruby test/coordination_claims_test.rb` PASS 32/177,
  17.941s; admission PASS 4/13, 0.084s; two focused GC/held-claim cases PASS
  2/19, 2.821s. Two collection/preparation cases PASS 2/12, 2.272s; focused Go
  creation-during-collection/naming-failure PASS 0.237s. All state disposable.
- Diagnostics focused Go PASS 1.605s; final narrow diagnostics PASS 0.165s.
- Firefox preparation: syntax PASS, fixture-journal unit PASS; actual
  `TestFirefoxTabs` explicitly SKIPPED during compilation. No native Firefox
  or headful/display run has occurred.

The initial combined Node command mistakenly included three Playwright entry
scripts. They failed on missing `@playwright/test` before browser launch, while
all intended deterministic cases passed. [Failed invocation log](node.log)
retains the evidence. The corrected 92-case command above passed; Playwright
runs were not retried before review. An ignored Nix eval-cache busy warning
appeared in the concurrent pin check; the checker itself returned zero.

The exact final Go command was:

```sh
DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/portal-followup-absent-providers.json \
nix develop --no-update-lock-file -c go -C portal test -mod=readonly ./internal/web \
-run 'TestPendingRevisionForwarding|TestCitation|TestUserMarkdown|TestMemberConversationUsesOnlyReadySessionMember|TestShippedBrowserClientMatchesSessionAPI|TestTrackingFiles|TestSource|TestArtifactsUseAPassiveAllowlistAndDownloadDisposition|TestTeamStatsHeldSnapshot|TestReadDiagnostics|TestDetailsReadDiagnostics|TestSessionDetails|TestCodexLimits|TestFirefoxFixtureJournal' -count=1
```

The corrected Node command was:

```sh
nix develop --no-update-lock-file -c node --test \
 portal/internal/web/read_cycle_browser_test.cjs \
 portal/internal/web/codex_providers_browser_test.cjs \
 portal/internal/web/attention_browser_test.cjs
```

Ordinary Git hooks were retained; this repository declares no hook framework.
No bypass was used. CI39641137157 was running on the current head at publication.
No superseded same-branch queued/running workflow required cancellation. Old
completed runs were untouched. There was no CI wait or blind rerun.

## Documentation and remaining boundary

Feature and verification guidance is in `docs/workspace-portal.md`. Dynamic
repository identity/candidate behavior is in `docs/coordination.md` and
`docs/coordination-operations.md`. All visible prose and operational errors
received the lead's direct writing pass before their owning commits.

Own source packages are complete and locally checked. Imp1 now owns B
notifications/runtime policy. Lead owns final whole-branch/affected-lane review,
C/config final graph and post-review utilities. Implementer0 retains diagnosis
and fixes in its groups when routed by the lead; it does not touch B during
imp1's ownership. There is no merge, package switch or deployment permission in
this handoff, and no live roster/settings/ledger change was made.

## Prepared post-review browser commands — not executed

All command candidates guard **0ba320a5** and a clean checkout. After imp1's
commits, the final owner must update each guard to the final reviewed exact head
and reconcile the final asset graph before execution. These are preparation
artifacts, not approval to run. Parent uses a fresh retained Luna/low utility.

Exact argv, after final review and source guards are updated:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/followup-combined-6e32a904/post-review-display-prepare.sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/followup-combined-6e32a904/post-review-root-dependencies.sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/followup-combined-6e32a904/post-review-chromium.sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/followup-combined-6e32a904/post-review-firefox50.sh
```

The first command realizes only pinned xvfb-run and its display dependencies,
not the application. The second roots exact existing outputs for the operation;
it refuses missing paths. Neither has been executed here. Parent retains roots
through the operation and owns their later removal. Root preparation is not a
session lifecycle action.

The Chromium command uses repo-pinned Playwright1.59.1 and its exact matching
store browser set, with actual Chromium147/revision1217 executable present.
It overlays the unchanged pinned review assets without writing B source, then
runs only the original portal improvements subtest against the actual Go/shared
assets. It covers Files/native links/source copy/download/refresh retention,
user Markdown/citations/team filters/member-add settings and receipt recovery.
The legacy full `TestQuestionBrowser` command remains separate; this packet does
not expand to unrelated suites.

The ordinary Firefox command uses Firefox155/Geckodriver0.36, one real native
window and 50 tabs, not Playwright/headless visibility mocks. It records real
foreground/hidden transitions, native discard/restore, 35s sustained foreground
updates, pending prompt/retry and a lost-response original-identity send with
one fixture acceptance record written with fsync. The native/model backend is
a stand-in, so this does not establish native Codex or production performance.
No live portal or credentials are used. The runner closes only its owned
browser/driver/profile. Driver chrome-context/native-discard compatibility is
untested and must pass without weakening the assertion.

Pinned preparation identities:

| Dependency | Exact store output |
| --- | --- |
| Node24.19 (repo dev shell) | `/nix/store/l07gdbxylzfl8pbx9pxy6fyg95w4hjwy-nodejs-24.19.0` |
| Playwright1.59.1 | `/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1` |
| Matching browser set | `/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers` |
| Review assets | `/nix/store/hllcfkaav40y98j1v7vl3gkikgpd0w75-workspace-repository-review-assets-1.0.0` |
| Ordinary Firefox155 | `/nix/store/nhqwiw8s88b3zy3pka98gizjgw6i2h8d-firefox-155.0` |
| Geckodriver0.36 | `/nix/store/b5g0k5g2bsvar0y38mn4zdfailhk0b77-geckodriver-0.36.0` |
| xauth1.1.5 | `/nix/store/4nvdi78v3rx435p09bk9hxmnp0z0ig7w-xauth-1.1.5` |
| Pinned xvfb-run | `/nix/store/iyzy0zy23i1njxar2sd1hr4hmk56dalh-xvfb-run-1+g87f6705` |

All except xvfb-run were filesystem-present during preparation; recheck/root
before execution because pressure GC can remove unrooted outputs. No display
exists yet. The repo-pinned Playwright differs from the architect's separate
installed1.61 inventory; the prepared Chromium command uses the matched repo
pair. Firefox50 is raw WebDriver and does not depend on Playwright.

Each prepared shell script passes `bash -n`. Parent records separate stdout/stderr
logs, wall time, exit status and actual assertion results for each operation;
absence of output is not acceptance. No package/browser/full-suite execution,
display realization or new utility was launched by this handoff.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
