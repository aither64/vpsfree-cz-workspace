# Activity consumer Settings navigation correction

The lead-assigned bounded harness correction is committed as capacity fixup
`ad0770a8ce6bb3b70645dc196386106a049072e8`, tree
`fd80694f0e28bf619fb297c5826b845f9bffc2d9`, parent
`5f7b13fd32f85ac0f502b42642578b19bbefc67e`. Owning capacity commit is
`8230ee8d8c55efe996a30d2cfe09f1de6a2171a8`. No autosquash or publication occurred;
the runtime source/index were clean at lane return and no process remains owned.
A kept runtime mutations frozen throughout this B package and received the return.

## Cause and exact delta

The retained real Go/Playwright fixture log at
`runtime-postreview-5f7b13fd/retry-activity.log` fails at cjs388 waiting for
`#session-retry-policy` to become visible after selecting top-level Settings.
Desktop failure JSON records no page errors and the Settings URL; mobile was
not reached. The shipped session template defaults to General and puts the retry
panel inside hidden settings-automation. The shipped settings-tab handler reveals
that section only when Automation is selected.

Only `portal/internal/web/retry_activity_browser_test.cjs` changed, 3 insertions
and no deletions. Each of its three Settings navigation points now selects
`[data-settings-tab="automation"]` before policy assertions. The final unsupported
check therefore observes the correct parent section rather than passing because
an ancestor is hidden. Every existing positive/negative policy, shared scope,
keyboard, geometry and deadline assertion is unchanged. No product/UI/template,
API/schema, timeout or other source changed. No product documentation update is
needed for this test navigation correction.

## Actual fixture verification

Command, through the existing Go-created fixture:

```sh
go -C portal test -mod=readonly -count=1 -timeout 5m \
  -run '^TestQuestionBrowser$/^retry_activity_browser_test[.]cjs$' -v ./internal/web
```

The shell is exactly the design's pinned mkShell, using immutable runtime5f7 for
dependency selection, the repository devShell, playwright-test's @playwright/test
module and matching playwright-driver browsers-chromium. PORTAL_BROWSER_TEST=1,
DEV_WORKSPACES_CODEX_PROVIDERS points to this owned output directory's absent
providers file, and screenshots go to its retry-activity directory. No standalone
Node/npm, alternate backend or new test harness was used.

Result: PASS, exit0, Go24.913s; activity subtest24.78s. Both desktop and mobile
report threadReads10, preferenceWrites3, actions2, screenshots=true. All existing
assertions ran. A's four-variant/32-case backend result is retained separately;
the unchanged backend54s batch was not repeated.

The staged source/head/patch were frozen before launch and verified unchanged
after success; the committed tree equals the recorded tested tree. The sole
utility initially belonged to A's extension watcher, so B visibly used the
monitor-skill minimal-output parent fallback. The already-running parent operation
remained owned when the slot later freed; it was not relaunched or duplicated.
Exact command, logs, status and process handle remained accounted for. Source was
not edited during the run. Normal pinned-Nix temporary-message commit preserved
all declared hooks; no hook framework is declared and none was bypassed.

Evidence is under `runtime-activity-harness-correction/`:

- [Structured final receipt](runtime-activity-harness-correction/receipt.json).
- [Actual activity log](runtime-activity-harness-correction/retry-activity.log).
- [Pinned runtime/Go/Node/browser inputs](runtime-activity-harness-correction/browser-inputs.log).
- [Exact tested patch](runtime-activity-harness-correction/tested.patch) and
  `tested-tree`/`tested-source.sha256` with matching final patch.
- `activity.exit`, started/finished timestamps and desktop/mobile screenshot
  artifacts retain operation evidence.

Log SHA256 is `566f755408652388da70a0840b0f5084dae3d7e6dc005d1cceff4148ce0ea6d5`.
Changed source SHA256 is
`f3faeff424f7e79c5f775f40d225ca2941d58b702802f162f8963bd2a2f051ab`.
Original5f7 is retained at
`refs/heads/2026-11-02-session-temporary-service-cleanup-activity-harness-before-5f7`
and its existing source root/receipts remain untouched.

Lead owns direct narrow inspection and A owns any later consolidation and
publication, including its separate CI failure inventory. No independent review
loop, extension/workspace/config edit, pin, build campaign, CI polling, claim,
deployment, default integration or session lifecycle action occurred here.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
