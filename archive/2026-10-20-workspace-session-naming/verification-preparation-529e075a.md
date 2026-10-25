# Final529 verification preparation

Static preparation on 2026-10-25 for clean published B
`529e075ad07e2d967a8af4902584e37527115454`, tree
`c9c3286858934ba63ff11c9e37879e7803a8351f`, with A
`801099102ef9af4a82c1f3853c53d6b442ecd4dc`. Current session/environment and
retained architect0 Astra/xhigh/workspace-write settings were reverified.
This note records commands for a lead-assigned watcher after final review;
none was evaluated, compiled or executed for this preparation. The deployment
hold remains: C113d/7510 frozen; no claims, copying, activation, integration or
session lifecycle action.

## Collector probe

[collection-probe-plan.md](collection-probe-plan.md) now binds the exact final529
head. B37..529 changes 16 files, but the production host/collector/preparation/
switch, coordination fixture, portal server/creation/preparation/authority,
retry-worker and naming-helper files used by the probe are byte-identical.
The three executable probe artifacts are unchanged and match their preserved
originals; the plan records their hashes and source anchors. No material design
deviation or prototype change is needed.

B37's collection receipt (23.396 seconds, exit 0) remains historical; its creation
VM failure also remains preserved. All earlier receipts retain their original
heads. Final529 probe execution is pending the watcher's authoritative result.
The probe covers actual collector plus HTTP admission/reservation/handoff and
ordinary preparation/package exclusion. It does not establish a usable native
conversation during collection, native naming, browser usability or activation.

## Preserved two-browser message-delivery check

The intended check is the entire existing
`TestQuestionBrowser/message_delivery_browser_test.cjs` subtest, not a new
browser harness. At final529:

- `portal/internal/web/question_browser_test.go:124–130` requires
  `PORTAL_BROWSER_TEST=1`; otherwise the parent skips. Lines 270–288 dispatch
  each selected script through Node and fail on a nonzero result.
- `portal/internal/web/message_delivery_browser_test.cjs:3–8` imports
  `@playwright/test` and loops over Chromium and Firefox. Chromium explicitly
  selects `channel: "chromium"`, requiring full Chromium. Lines 95–97 close
  each browser and make any failure nonzero. Neither engine has a skip path.
- `flake.nix:82–96` supplies Go, Ruby, Git, Nix, Node and jq in the repository
  default shell, but does not provide Playwright modules or browser variables.
  `README.md:397–410` requires readonly Go modules and an absent
  `DEV_WORKSPACES_CODEX_PROVIDERS` fixture path on a configured host.

The following environment adds matching Playwright modules/browsers from B's
own locked Nixpkgs input to that default shell. It does not use a registry
Nixpkgs, npm installation or downloaded unpinned browser. B's root Nixpkgs lock
is `a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4`, NAR
`sha256-r2f1oUwixlgq9zOdYLqJLfS/lWBT60/IITjhTKI59JU=`. The local immutable source
`/nix/store/nqkh6j5xlyvlw4hlrw4ybpq1cis79szf-source` was matched by its store NAR
hash, without flake evaluation or fetching. In that source:

- `pkgs/top-level/all-packages.nix:2953–2955` exports `playwright-test` and
  `playwright-driver` from the same driver definition (version 1.59.1).
- `pkgs/development/web/playwright/driver.nix:121–134,179–194` installs
  `@playwright/test` below `lib/node_modules`; the supplied CLI wrapper uses
  that module path and the matching driver's browser bundle.
- The same file at `:162–165,230–266` exposes the browser bundle with full
  Chromium and Firefox enabled. The recipe uses these exact package interfaces.

After review and lead release, the watcher runs this once from the final clean
checkout. Preserve its outer log, exit status, JSONL and stderr. Existing output
files cause refusal rather than overwriting a receipt. Shell realization may
fetch/substitute dependencies at that later authorized verification step;
availability and execution have not been proved by this static preparation.

```bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-workspace-session-naming/dev-workspace
test "$(git rev-parse HEAD)" = 529e075ad07e2d967a8af4902584e37527115454
test -z "$(git status --porcelain --untracked-files=all)"
export naming_browser_artifacts=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-workspace-session-naming
naming_browser_tmp=$(mktemp -d /tmp/workspace-message-delivery.XXXXXXXX)
trap 'rmdir -- "$naming_browser_tmp"' EXIT
export DEV_WORKSPACES_CODEX_PROVIDERS="$naming_browser_tmp/absent-providers.json"
test ! -e "$DEV_WORKSPACES_CODEX_PROVIDERS"

nix develop --no-write-lock-file --impure --expr '
  let
    f = builtins.getFlake "path:/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-workspace-session-naming/dev-workspace";
    pkgs = import f.inputs.nixpkgs { system = "x86_64-linux"; };
  in f.devShells.x86_64-linux.default.overrideAttrs (previous: {
    nativeBuildInputs = (previous.nativeBuildInputs or []) ++ [ pkgs.playwright-test ];
    NODE_PATH = "${pkgs.playwright-test}/lib/node_modules";
    PLAYWRIGHT_BROWSERS_PATH = "${pkgs.playwright-driver.browsers}";
    PORTAL_BROWSER_TEST = "1";
  })
' --command bash -s <<'BROWSER_CHECK'
set -euo pipefail
set -o noclobber
browser_json="$naming_browser_artifacts/verification-message-delivery-529e075a.jsonl"
browser_stderr="$naming_browser_artifacts/verification-message-delivery-529e075a.stderr"
test ! -e "$browser_json"
test ! -e "$browser_stderr"
test "$PORTAL_BROWSER_TEST" = 1
test ! -e "$DEV_WORKSPACES_CODEX_PROVIDERS"
go -C portal test -mod=readonly ./internal/web \
  -run '^TestQuestionBrowser$/^message_delivery_browser_test[.]cjs$' \
  -count=1 -timeout=10m -json >"$browser_json" 2>"$browser_stderr"
jq -e -s \
  --arg parent TestQuestionBrowser \
  --arg child TestQuestionBrowser/message_delivery_browser_test.cjs '
    all(.[]; .Action != "skip") and
    any(.[]; .Action == "run" and .Test == $parent) and
    any(.[]; .Action == "pass" and .Test == $parent) and
    any(.[]; .Action == "run" and .Test == $child) and
    any(.[]; .Action == "pass" and .Test == $child) and
    any(.[]; .Action == "pass" and (.Test // "") == "")
  ' "$browser_json"
BROWSER_CHECK

test "$(git rev-parse HEAD)" = 529e075ad07e2d967a8af4902584e37527115454
test -z "$(git status --porcelain --untracked-files=all)"
```

Acceptance requires command exit 0 **and** the explicit non-skip event checks.
`-count=1` prevents cached success. On this frozen script, successful completion
means both engine loops ran every existing assertion; a missing browser/module
or either engine's failure is a failure, not a reason to omit it. The ten-minute
Go bound is its ordinary default made explicit, not a synchronization change.
Do not change the script, override executables, disable browser validation or
weaken assertions to obtain success. A changed source head or setup failure
returns to the lead with evidence before any changed command or retry.

This proves the preserved message-delivery browser scenarios against real
templates/assets/CSP and controlled API responses: unknown delivery, explicit
duplicate confirmation, replacement identity, preserved drafts, reload behavior
and known-unsent retry identity. It does not prove native delivery, provider
availability, real session creation, every other TestQuestionBrowser script or
live deployment health. Those remain separate checks.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/
