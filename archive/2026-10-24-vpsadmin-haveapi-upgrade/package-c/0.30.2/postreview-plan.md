# Package C postreview execution plan

Current-head plan after script-only correction. Prior head757f7fd8 batch1 failed
and was reconciled before this narrow fix; no retry/new batch below launched.
Lead must directly verify the fix and explicitly release the slot before any
long command at exact headf10d3d48.
Owner implementer1 retains diagnosis and source/Git follow-up; utilities execute
only assigned commands. No push, PR74 rewrite, merge, deployment, live OAuth,
real member mutation, server or lifecycle operation.

## Immutable test identity and preflight

Worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-webui`.
Branch dev/vpsadmin-haveapi-upgrade, target main; base5a2d2bdc.
Exact head `f10d3d48c4f21cc39187c3667ffffd9952404c11`, tree
`e1084bb80dd07140719034ab908a6f62daff855b`.
Root npmDepsHash `sha256-sY3OQDFdisOzhJO4dhwlsjvGxlhog8crhqU3tHcI4IY=`;
HaveAPI0.30.2 integrity/source in packages/haveapi-client-provenance.json.
Prior reviewed757f7fd8 cleaned source was
`/nix/store/6pjw8m1fx4c0v24yvhxw78mj1kfg5193-source`; reevaluate current clean source
in batch2 after release, rather than transferring that old tree identity.
Node24.21.0/npm11.19.0 from existing locked nix develop; Playwright1.61.0,
existing browser cache revision1228. See planned-input-identity.json for exact
file hashes, root locked revisions and source tree. The complete committed
flake.lock is the authoritative recursive input graph, not only its two roots.

Immediately before each batch require matching exact HEAD, clean tracked/index
state and matching hashes from that receipt. If code/lock/head changes, return
to owner/lead before running; do not rewrite or refresh the tested boundary
silently. Do not rerun quick audits/typechecks already passed solely for waiting.
No npm install needed: root and BFF dependencies were installed and actual53
HaveAPI files checked against the verified tarball. If setup is missing or
changed at execution, parent diagnoses; watcher does not repair or retry.

Each uncertain batch gets a FRESH gpt-6-luna/low utility under pinned catalog
840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa and matching
native identity dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12. Recheck
installed execution policy and launch explicitly danger-full-access/never.
Serialize these operations, respecting utilities.max_concurrent=1; never reuse
an old watcher or let it edit app files/tracking/Git. Complete stdout/stderr,
exit status, elapsed time and exact command/revision kept under this directory.
No automatic retries or arbitrary quiet-run timeout. Unexpected kernel build
stops/escalates the exact owned operation. Parent interprets failures and owns
all subsequent choices. Utilities never launch mutation drivers.

## Batch 1: normal test suites and production frontend build

From the canonical worktree, one fresh watcher runs:

```sh
nix develop -c bash -c 'npm run ci:tests && npm run build'
```

ci:tests invokes repository script tests, BFF tests and the full root Vitest unit
suite; it does not rerun ci:quick. This validates the originally changed source
checker/tests and inherited BFF/session contract as well as all app consumers.
The normal build uses VITE_RUNTIME_MODE=bff from package scripts. Preserve full
logs, suite counts and dist/build-info.json; require full expected commit and
clean state. Check no public/config.local.js or local .env overrides exist and
no caller VITE_BUILD_SHA/VITE_BUILD_DIRTY override can falsify provenance before
launch. No build on a deployed host, secret injection or application deployment.

## Batch 2: immutable Nix packages and exact provenance

One separate fresh watcher runs the ordinary package/check outputs in one
cache-sharing invocation, with no out-link:

```sh
nix flake metadata --json --no-write-lock-file . > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-vpsadmin-haveapi-upgrade/package-c/0.30.2/nix-flake-metadata.json
nix build --no-link --print-build-logs --json \
  .#frontend .#bff \
  .#checks.x86_64-linux.provenance \
  .#checks.x86_64-linux.source-contents \
  .#checks.x86_64-linux.package-contents > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-vpsadmin-haveapi-upgrade/package-c/0.30.2/nix-build-results.json
```

The output JSON paths above are beneath the verified tracking root.
package-contents already depends on both packages;
listing frontend/BFF exposes their outputs without rebuilding them twice.
No NixOS VM/module/system build or fleet activity in this batch. Cache warnings
for six bundled optional URLs are resolved only by this actual build result.

After successful build, capture full frontend/BFF output and .drv paths through
nix eval, full recursive derivation/input graph through
`nix derivation show --recursive .#frontend .#bff`, and NAR identities. Require
frontend build-info.json and BFF share/vpsadmin-webui-bff/build-info.json to
agree on exactf10d3d48, dirty=false. The package check verifies the public/runtime
file boundary; preserve that result and underlying source/dependency hashes.
Source/provenance checks are required package acceptance, although their pure
logic had quick fixtures. No unnecessary rebuild after successful same-input
result. Any uncertain build remains accounted for by its watcher until completion
or parent response; never call an incomplete build a failed test by elapsed time.

## Batch 3: bounded desktop/mobile ordinary browser fixtures

Use one fresh browser watcher after review and prerequisite batches. Run pinned
existing Playwright-managed Chromium, not --container or policy-changing flags.
No browser/system-policy edits. Existing binary/cache paths were inspected,
but runtime shared-library readiness is unverified until launch; report any
setup failure to owner rather than switching runtimes or installing packages.

Bind output files below to absolute paths under package-c/0.30.2 at launch.
Check loopback port52847 is still unused; if busy, stop and parent selects a new
free loopback port without killing/reusing any foreign server. CI=1 forces the
native Playwright webServer to refuse reuse; explicit retries0 prevents opaque
reruns. Clear E2E_STORAGE_STATE, E2E_CHROMIUM_EXECUTABLE_PATH and E2E_IGNORE_HTTPS_ERRORS
from the launch environment; never provide live sessions/accounts. The harness
starts this worktree's local Vite server and owns its native lifetime.

```sh
nix develop -c env -u E2E_STORAGE_STATE -u E2E_CHROMIUM_EXECUTABLE_PATH \
  -u E2E_IGNORE_HTTPS_ERRORS \
  CI=1 E2E_START_SERVER=1 E2E_BASE_URL=http://127.0.0.1:52847 \
  PLAYWRIGHT_JSON_OUTPUT_FILE=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-vpsadmin-haveapi-upgrade/package-c/0.30.2/browser-results.json \
  node scripts/playwright.mjs test \
  e2e/specs/public/overview.spec.ts \
  e2e/specs/app/authenticated_home_smoke.spec.ts \
  e2e/specs/app/header_session_limit.spec.ts \
  e2e/specs/app/session_expiry_redirect.spec.ts \
  e2e/specs/app/sync_indicator_error_retry.spec.ts \
  e2e/specs/app/vps_create_failures.spec.ts \
  e2e/specs/app/vps_creation_progress.spec.ts \
  e2e/specs/app/blocking_action_progress_modal.spec.ts \
  e2e/specs/app/action_state_detail_page.spec.ts \
  --project=chromium --project=mobile-chrome --workers=2 --retries=0 \
  --reporter=list,json --output=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-vpsadmin-haveapi-upgrade/package-c/0.30.2/browser-artifacts
```

Browser JSON and artifact paths above are absolute session-local outputs. Retain traces,
screenshots and video on failure under existing config. No app file edit needed
for command-line output overrides. Do not use broad/full/nightly/PR selectors;
explicit nine specs bound scope. They cover:

- Public overview and authenticated home, including ordinary native XHR and
  anonymous/auth header separation already asserted by those specs.
- Synthetic session.json token generations, inactivity interaction/reload and
  logout/expired background response; manual query retry after a fixture error.
- Missing create receipt, in-flight cross-tab guard, transport loss/reload and
  no duplicate create; accepted/pending/failed/unavailable VPS creation state.
- Blocking VPS start progress, first-read completed/failed receipts, Tasks
  tracking, and action cancellation dialog/endpoint with synthetic API replies.

Fixtures deliberately target local/api and route-controlled responses. This is
a normal app-entry browser test in local Vite dev mode, separate from production
build/package proof. It certifies neither live OAuth exchange nor production
permissions/task completion. OAuth401 renewal/race/no-replay behavior remains
covered by actual-library controlled-XHR tests/full unit suite; existing browser
session workflow does not invent a live-provider proof. No new browser test or
source extension is proposed solely to wait for review.

## Completion/hold

Parent receives each result and records exact head, sources/locks/.drv/output
identities, counts, failures and limits in the existing C3 receipt/review packet.
No extra Git commits needed for evidence alone. A concrete finding returns to
lead for source assignment; no ad hoc Git edit by a watcher. All remaining
postreview actions are still pending explicit lead release. PR74 protected
rewrite plan remains a separate user approval gate even after checks pass.
