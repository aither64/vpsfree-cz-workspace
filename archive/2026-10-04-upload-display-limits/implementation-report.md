# Upload display and prompt limits implementation report

Implementer: implementer0. Application writes are finished for the original
coordinator's bounded assignment. No commit, push, provider pin/vendor refresh,
independent review, packaged check, real-browser execution or deployment was
performed by this member. The coordinator owns final writing, formatting,
verification, commits, dependency refresh, state and portal updates.

Session identity was verified with `dev-session current` from this tracking
directory: `2026-10-04-upload-display-limits`. Both `DEV_SESSION_SLUG` and
`DEV_SESSION_WORKSPACE` were absent, matching the trusted thread binding to
`/home/aither/workspace/ai/vpsfree.cz`. A first check from the workspace root
reported no current session; checking from the intended directory resolved it
before reading or editing session-owned files.

Both application worktrees started clean on branch
`2026-10-04-upload-display-limits`, at the recorded design bases:
codex-web `32775fa7fdd9bc9b41aef74b7f195e5c3bc0f8d5` and dev-workspace
`6a972b9ab01077611b2c60e0fc726c185e050315`. Required workspace routes,
repository instructions, project documentation and the documentation skill
were read. Only this report was written in coordination records.

## Changed behavior and paths

**codex-web (six paths):**

- `conversation/assets/uploads.js`: dedicated summary in the existing render
  path. Empty selections hide it. Nonempty selections show singular/plural
  count, full selected byte total through `fileSize`, and acknowledged ready
  count while incomplete. Errors stay in their notice. Removing/failed-removal
  entries remain counted until removed; completed files awaiting removal stay
  complete. No readiness, serialization, removal or persistence logic changed.
- `conversation/assets/uploads.css`: summary shares muted detail/notice style,
  margins and explicit hidden styling. The shared 12rem composer cap remains.
- `conversation/assets/conversation.js`: import and re-export use
  `uploads.js?v=4`.
- `conversation/assets/conversation.css`: shared CSS import uses
  `uploads.css?v=3`.
- `test/uploads_browser_contract_test.cjs`: extend the shipped component fixture
  for full-size partial transfer, acknowledgement, zero-byte completion failure
  and retry, restored paused/missing/deleted entries, removal failure/inflight
  retention, lock/unlock, accepted-selection clear and preserved server files.
  The existing external-controls and removal/persistence tests remain. DOM card
  lookup uses its class rather than child position. Generic IDs explicitly keep
  the 100/101 boundary.
- `docs/reference.md`: summary and selection contract draft for direct lead
  writing review.

**dev-workspace count/recovery:**

- `portal/internal/uploads/store.go`: exported `DefaultPromptFiles = 50`, used
  in `DefaultLimits().Files`.
- `portal/internal/web/preparation_store.go`: preparation snapshot validation
  uses that same Go-owned default.
- `portal/internal/web/static/preparation.js`: schema-2 browser drafts accept
  50 ordered IDs. All other draft validation stays intact.
- `portal/internal/uploads/store_test.go`: real-default 50-file send/steer/queue
  and preparation claim/replay, 51 rejection, byte-quota and expanded-reference
  rejection. Synthetic content is small; existing custom 10-file fixtures stay.
- `portal/internal/web/preparation_test.go`: new
  `TestSessionPreparationFiftyFilesRecoveryAndCompaction` uploads 51 ready files,
  rejects a 51-file admission, accepts 50, reloads its actual persisted snapshot,
  reads status, replays, conflicts on changed/reordered input, retries with the
  same receipt and wire text, and compacts after creation proof/upload binding.
  The full preparation validator also rejects 51 IDs. Existing template asset
  assertions now match preparation/creation JS v3.
- `portal/internal/web/preparation_browser_contract_test.cjs`: 50-ID attempted
  draft survives lost response and reload, status 404 resends the exact body,
  receipt identity and verified draft/selection cleanup remain. 51, duplicate,
  malformed and body-mismatched IDs are rejected.
- `README.md`: draft 50-file limit and preserved 20,000-byte prompt/reference
  and 61,024-byte creation-form limits. This same file includes the display
  explanation for the layout commit; stage its relevant hunks separately.
- `docs/session-preparations.md`: draft compatibility guidance distinguishes
  the preceding 10-file reader from packages predating preparation. It requires
  normal durable snapshot-free terminal compaction and verified draft cleanup;
  unresolved work keeps a compatible reader. The forward-only package switch
  policy is retained. The existing older compatibility baseline does not prove
  the 10-to-50 reader boundary.

**dev-workspace layout/cache and browser acceptance:**

- `portal/internal/web/static/style.css`: only
  `#creation-uploads.codex-upload-composer` overrides `max-height: none` and
  `overflow-y: visible`; specificity wins over the later shared stylesheet.
- `portal/internal/web/static/app.js`: provider entry uses
  `conversation.js?v=12`.
- `portal/internal/web/static/creation.js`: its formerly unversioned provider
  import now uses that same v12 entry.
- `portal/internal/web/templates/{index,session,creation,source-file}.html`:
  affected references advance to style v4, uploads CSS v3, conversation CSS v5,
  app v22, preparation v3 and creation v3 as applicable. Unrelated versions stay.
- `test/creation_browser.cjs`: actual host/provider CSS served as `text/css`,
  production stylesheet order, viewport metadata, and creation page/form/action
  classes. At 1280px and 375px, 50 long-name cards retain their full 50 KiB total
  before completion acknowledgement; all 50 removal actions and Create session
  are reachable through the existing page scroll container. It asserts creation
  max-height/overflow/geometry, restored/removal totals, file 51 rejection,
  exact-body 50-file lost-response/reload recovery, verified cleanup with server
  files retained, and the actual conversation component's 12rem scroll cap.
  The local fixture performs no Codex inference.
- `test/README.md`: draft explanation of these additional fixture assertions.

`portal/go.mod`, `portal/go.sum`, `flake.nix`, `flake.lock` and
`nix/workspace-portal.nix` are untouched. Refresh them only after the coordinator
commits/pushes the reviewed codex-web revision and assigns its exact pin.

## Quick verification and evidence

Member-run `git diff --check` passed in both worktrees after source writes.
No member-run Go/Node test or formatting result is claimed.

Resolving flake tools through this sandbox failed (exit 1) on daemon access:

```sh
nix eval --impure --raw --expr '(let flake = builtins.getFlake "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-04-upload-display-limits/dev-workspace"; pkgs = import flake.inputs.nixpkgs { system = "x86_64-linux"; }; in pkgs.go.outPath + ":" + pkgs.nodejs.outPath)'
```

Error: `/nix/var/nix/daemon-socket/socket`: Operation not permitted. A read-only
`nix-instantiate` tool lookup also failed for the same reason. No build was
launched. Per coordinator instruction, stop tool lookup here; the host can run
the pinned environments without changing this member's permissions.

The coordinator ran these focused commands in pinned Nix tooling on the draft:

- codex-web `node --test test/uploads_browser_contract_test.cjs`: 31 tests,
  31 passed, zero skipped; see `quick-codex-web-browser.log` (381.946ms).
- codex-web `go test ./conversation`: passed; see
  `quick-codex-web-go.log` (0.112s).
- dev-workspace upload `TestDefaultPromptFiles` selector: passed; see
  `quick-dev-workspace-go.log` (4.138s).
- Focused web run initially failed three assertions: new 51-file HTTP expectation
  and two existing asset-version assertions. The existing HTTP contract returns
  409 `invalid preparation prompt`, so the test now expects 409. Both old v2
  asset expectations now match v3. The 3.632s failed run is preserved in
  `quick-dev-workspace-go.log`; a successful rerun is pending.

Host wrapper commands were not supplied in the member messages/logs. The entries
above name the known inner commands/selectors and evidence, not an invented
exact wrapper transcript. Source writes are finished; the coordinator can
format and run the following quick commands using each repository's pinned
Go/Node toolchain (include Node in PATH for Go browser tests):

```sh
# codex-web root
node --check conversation/assets/uploads.js
node --check conversation/assets/conversation.js
node --test test/uploads_browser_contract_test.cjs
go test -mod=readonly ./conversation -count=1

# dev-workspace root: format the changed Go paths before final checks
gofmt -w portal/internal/uploads/store.go portal/internal/uploads/store_test.go portal/internal/web/preparation_store.go portal/internal/web/preparation_test.go
node --check portal/internal/web/static/preparation.js
node --check portal/internal/web/static/app.js
node --check portal/internal/web/static/creation.js
node --check portal/internal/web/preparation_browser_contract_test.cjs
node --check test/creation_browser.cjs
node portal/internal/web/preparation_browser_contract_test.cjs
go -C portal test -mod=readonly ./internal/uploads -run '^(TestDefaultPromptFiles|TestPreparationUpload|TestQuotasAreReserved)' -count=1 -v
go -C portal test -mod=readonly ./internal/web -run '^(TestSessionPreparation|TestDraftUploadHTTP|TestShippedBrowserClientMatchesSessionAPI)' -count=1 -v
git diff --check
```

Require nonzero selector execution and no Node skip. New upload test names:
`TestDefaultPromptFilesSubmissionAndPreparation` (three subtests) and
`TestDefaultPromptFilesRetainsByteAndReferenceBounds`. The new web case starts
`TestSessionPreparation` and is included in the listed web selector.

## Hook status

Checked both assigned worktrees with hidden-file-aware framework searches and
`git config --show-origin --get core.hooksPath`: no declared Overcommit,
pre-commit, Lefthook or Husky framework, and `core.hooksPath` is unset (lookup
exit 1 means absent). The actual `git rev-parse --git-path hooks` directories
are `repos/codex-web.git/hooks` and `repos/dev-workspace.git/hooks`; both contain
only Git `*.sample` hooks, with no active hook. No hooks were installed or
bypassed. The private review-ui package declares build/test scripts, no hook
framework. Recheck hook state before the coordinator's first commit.

## Scope, deviations and remaining work

No material design deviation or source drift from the recorded bases. The
creation page's previously unversioned provider import was discovered and
versioned with its parent script to complete the actual host cache chain.
The original coordinator's separate generated-dependency commit split takes
precedence over design.md's earlier grouping of pins with layout.

Preserved schemas, wire/API fields, digest/request identity, replay ordering,
compaction logic, byte/transport/reference bounds, generic 100-ID bound,
1,000 scope-file and 10,000 category bounds, transfer concurrency and retention.
No migrations or package/lifecycle helpers changed. The test's manual ready
receipt/proof models durable completion using existing fixture helpers; it
does not establish live App Server or deployment acceptance.

Remaining: lead's direct user-facing writing review of interface copy,
`docs/reference.md`, README, preparation compatibility guidance and test README;
Go formatting and final quick rerun; focused commits; exact provider pin/vendor
refresh; whole-branch inventory and independent final review. Keep application
files available for any required test fixes before calling the branches ready.

Only after final review, the lead's fresh utility watcher may run longer checks:

```sh
# Each repository root, separately
nix flake check --print-build-logs

# dev-workspace root, with exact resolved prerequisites and matching pinned source
PLAYWRIGHT_MODULE=/exact/playwright/module CHROMIUM_EXECUTABLE=/exact/chromium/bin/chromium CODEX_WEB_SOURCE=/exact/pinned/codex-web node test/creation_browser.cjs

# Existing older pre-preparation compatibility fixture, separately after review
bash test/preparation_compatibility.sh
```

The specific 10-to-50 older-reader experiment still needs the isolated preceding
reader at `6a972b9ab01077611b2c60e0fc726c185e050315`; the existing
`924c0ec...` runner is insufficient. No cross-version experiment or installed
package switch was run. No real-browser/layout or packaged evidence is claimed
from fixture source or syntax checks.

Proposed functional commit split: codex-web summary/contracts/cache/tests;
dev-workspace 50-file count/recovery/contracts/tests; dev-workspace creation
layout/host cache/browser coverage. Follow with the coordinator's separate
generated exact-provider dependency update. No commit/push/integration approval
is inferred from this report.

Stable session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-04-upload-display-limits/
