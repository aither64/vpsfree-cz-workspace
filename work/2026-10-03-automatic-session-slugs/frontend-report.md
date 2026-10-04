# Frontend browser/progress report

Frontend implementation, quick verification and main-context prose review are
complete. The authorized 16-path browser request/progress unit is committed as
`51dca869fe50c20b6669d4770856fca0971fc9c2`:
`portal: recover requests while preparing session names`.
The runtime worktree and index are clean. No push, browser/binary integration,
deployment, default-branch integration or lifecycle action was performed.
Independent review and the post-review release gates remain coordinator-owned.

Session: `2026-10-03-automatic-session-slugs`; retained implementer0
`gpt-6.1-sol` / xhigh / workspace_write. `dev-session current` and the saved
same-session roster match the trusted binding; both session identity environment
variables are absent. Assigned runtime worktree only:
`worktrees/2026-10-03-automatic-session-slugs/dev-workspace`.
Current owning HEAD is `51dca869fe50c20b6669d4770856fca0971fc9c2`; its parent
is the coordinator's dependency commit
`07a98d059368f19adafc7cdc0562a2b01c912374`, above accepted runtime helper
`c347fba` and exact deployed ancestor
`4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4`. All prior ancestors are preserved.
No dependency/pin paths or other initiative records were edited by this unit.

## Delivered files and contracts

- `portal/internal/web/static/preparation.js`: bounded New session record in
  the existing tab draft key. Canonical random-v4 ID, verified writes/readback,
  full serialized request snapshot, ordered attachment IDs and per-draft scope;
  same-body retry through GET-before-POST after uncertainty; one in-flight
  submission; exact acceptance and verified draft/selection removal.
- `portal/internal/web/static/app.js`: initial prompt first, optional name and
  advanced settings in Options; tab-owned upload component storage; inputs/files
  locked after an attempted submission; visible request ID and recovery control;
  no catalog/upload discovery dependency for attempted recovery. A migration
  notice is limited to an older draft with concrete cached file selections;
  old shared metadata is never adopted or deleted. New managed
  defaults use the empty model/effort pair. Saved explicit overrides remain
  exact when discovery fails. Plan/fork settings behavior stays on its existing
  branches. CLI preview requires an explicit name and uses known local team
  defaults when no override is selected.
- `portal/internal/web/{preparation.go,server.go}` and
  `templates/{index.html,creation.html,session.html}`: explicit preparation page
  data with request/receipt/accepted-time identity, escaped server-rendered raw
  prompt, optional custom-name limits, recovery controls, additive asset and
  cache versions. Preparation rendering no longer invents a session with a UUID
  slug. Shared app version is 20; preparation version 1; creation version 2.
- `portal/internal/web/static/creation.js`: existing progress component handles
  both preparation and legacy receipt pages. Stable phase labels, exact receipt
  and accepted timestamp checks, current-attempt retries and monotonic attempt
  rendering. Only ready status with an exact dated canonical path can navigate;
  uppercase/underscore custom names retain their syntax. Gone/conflict/cancelled
  preparation states cannot redirect. Text is assigned through textContent.
- `portal/internal/web/server_test.go`: two obsolete static expectations now
  assert optional managed New defaults and the current preparation progress copy;
  unrelated concrete preset/plan/interaction checks are preserved.
- `portal/internal/web/preparation_test.go`: nonzero HTTP tests for explicit
  preparation identity/escaping and optional New session name placement/limits.
- `portal/internal/web/{browser_contract_test.cjs,preparation_browser_contract_test.cjs}`:
  the existing shipped-browser Go harness awaits the 15 new pure contract cases.
  No new Nix registration or generalized test/storage framework.
- `test/creation_browser.cjs`: actual Chromium fixture uses shipped scripts and
  pinned conversation assets. Generated/default/custom names, uppercase canonical
  navigation, model discovery failure, duplicate/lost POST, catalog change during
  uncertainty, two tab scopes, old global pointer exclusion, attachment-only
  transfer, receipt retry, XSS/unsafe URL rejection, storage write/removal failure,
  and retained plan/legacy creation behavior. Explicit prerequisites fail when
  absent. It performs no inference and remains unexecuted pending review.
- `docs/{session-preparations.md,workspace-portal.md}` and `test/README.md`:
  lasting browser ownership/recovery and entry guidance. The coordinator's
  aggregate Ruby entry correction is preserved. The coordinator completed its required direct visible-prose pass;
  those edits are preserved in this commit.

## Verification evidence and exact quick commands

Checks were executed by the coordinator in the permitted repository-derived
Nix environment. Native member daemon refusal was not bypassed. Logs were read
without rerunning checks:

- Initial focused Go batch: three nonzero tests PASS, package 1.037s, including
  both new HTTP cases and `TestShippedBrowserClientMatchesSessionAPI`.
  Initial direct Node entry: all 15 preparation cases PASS.
  Logs `/tmp/automatic-session-slugs-frontend-focused-{go,node}.log`.
- Broad default Go web/uploads/session batch completed in 55s. All other cases
  passed; web failed only two obsolete static expectations. Their New-session
  required-control/progress-copy assertions were narrowly corrected without
  changing unrelated preset, plan-dialog or interaction assertions.
  Log `/tmp/automatic-session-slugs-frontend-regression-go.log`.
- Final five nonzero focused Go selectors PASS, package 0.998s. This includes
  both corrected static tests, the two HTTP cases and the shipped harness
  running all 15 expanded migration cases. Direct 15 cases also PASS.
  Logs `/tmp/automatic-session-slugs-frontend-final-{go,node}.log`.
- Focused aggregate Ruby: 16 runs, 223 assertions, zero failures/errors/skips,
  1.368s. Selector `/portal_fork|portal_creation|preparation_reservation/`.
  Log `/tmp/automatic-session-slugs-frontend-regression-ruby.log`.
- Coordinator reports all six JS/CJS syntax checks, final gofmt of four Go paths
  and diff whitespace checks PASS. Its final app.js count-copy clarification
  changed prose only; the syntax rerun passed afterward. The required writing
  skill was applied directly to labels, errors, docs and entry guidance.

The accepted migration follow-up preserves old cached metadata and shows its
notice only with concrete older-draft/file-selection evidence. Refreshed tests
prove notice persistence, distinct new scopes, missing/fresh evidence and absence
of old-pointer lookups during attempted recovery. The source barriers were
respected; parent formatting/prose edits are included. No further broad repeat
was required solely for the narrow assertion/notice/prose changes; packaged full
verification remains post-review.

Commands from the runtime repository root, through the retained profile:

```sh
nix develop /tmp/automatic-session-slugs-runtime-env -c env TMPDIR=/tmp GOWORK=off \
  go -C portal test -mod=readonly ./internal/web \
  -run '^(TestSessionPreparationPageHasExplicitIdentityAndEscapedRawPrompt|TestSessionPreparationIndexMakesOnlyNewSessionNameOptional|TestShippedBrowserClientMatchesSessionAPI)$' \
  -count=1 -v
nix develop /tmp/automatic-session-slugs-runtime-env -c \
  node portal/internal/web/preparation_browser_contract_test.cjs
nix develop /tmp/automatic-session-slugs-runtime-env -c env TMPDIR=/tmp GOWORK=off \
  go -C portal test -mod=readonly ./internal/web \
  -run '^(TestNewSessionShowsConcretePresetLeadSettings|TestBrowserClientShipsMessageAndLifecycleInteractions)$' \
  -count=1 -v
```

The first Go selector selects three tests; the correction selector selects two.
The first entry's shipped-browser harness invokes the new Node cases plus
existing plan/fork/session API contracts. Together those selectors match the
final five-test passing batch. The standalone Node entry selects all 15 expanded
preparation cases. Use the same environment for individual
`node --check` calls on `static/{app,creation,preparation}.js`, the two contract
CJS files and `test/creation_browser.cjs`; those are syntax checks, not behavior
or browser evidence. No member edits to `nix/workspace-portal.nix` are needed.
Published helper pins permit GOWORK=off; the temporary local workspace is no
longer required for this unit.

## Browser fixture prerequisites and pending release gates

After committed-source mandatory review, the coordinator may run:

```sh
nix develop /tmp/automatic-session-slugs-runtime-env -c env \
  PLAYWRIGHT_MODULE=/nix/store/0k9k01y3zfnkbh71jq6vx08g572qjrpr-playwright-core-1.63.0 \
  CHROMIUM_EXECUTABLE=/nix/store/g0yvxs8p2ijrvmxpd5mim1ni0fyk9bnh-chromium-154.0.8037.57/bin/chromium \
  CODEX_WEB_SOURCE=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-03-automatic-session-slugs/codex-web \
  node test/creation_browser.cjs
```

The provider source must be the exact checked `ca0f3bc980ca99454d000761aeee37b4b9bbafc3`
assets. The prepared browser/tool environment is provisioning evidence only.
This local fixture does not replace packaged/browser deployment checks or the
public helper's exact-binary isolation/teardown proof. Those remain post-review.
`team_settings_browser_test.cjs` also launches Playwright and remains outside
quick checks. Real frontend browser assertions have not run yet.

## Compatibility and remaining release gates

Old unsubmitted drafts migrate their text/settings to a new verified request
ID. They cannot safely inherit the globally shared upload pointer. The current
implementation shows the approved notice only with an actual older draft plus
valid cached shared scope/file-selection evidence. A private boolean preserves
that notice across reload without further old-pointer reads. The draft obtains
an independent scope; old cached metadata is untouched and unsubmitted server
files remain subject to normal expiry. Tests assert unchanged old metadata,
missing/fresh evidence, notice persistence, distinct scopes and no pointer lookup
for attempted recovery. No accepted/uncertain files are released or deleted.
The follow-up is accepted scope, not a protocol/design expansion.

Attempted inputs remain locked even after 404 or pre-admission HTTP failure;
only identical retry is offered. Starting a distinct fresh tab allocates a new
identity; it does not recycle the uncertain ID. Clearing browser site data can
lose local recovery metadata, so the visible ID/tab must be retained if storage
fails. No server-owned receipt/catalog/journal schema changes occur here.

## Commit and hook evidence

Committed exactly the authorized 16 application paths in one focused browser
request/progress commit. The index was empty before staging; final staged and
committed inventories matched the explicit assignment. Dependency pins, helper
sources and coordination records were excluded. Final `git status --short` and
`git diff --cached --name-only` returned empty output.

Before committing, reread workspace commits/git procedures and repository
AGENTS. No declared hook framework was found; `core.hooksPath` is unset and the
canonical bare repository's hooks directory contains only `.sample` hooks.
The normal `git commit -F` path was used with a temporary message file and every
message line at most 80 columns. No hooks were bypassed.

Remaining verification: mandatory independent review, packaged full checks,
actual Chromium fixture, exact candidate-binary isolation/teardown proof and
assembled deployment/canaries. None is claimed from unit tests or fixture code.
Session/refs remain open; external coordinator owns publication and tracking.

Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-automatic-session-slugs/
