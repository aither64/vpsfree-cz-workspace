# React postreview execution selection

Prepared only; no command below launched by this preparation. Source frozen at
`55a813b44edb915c7ed5ce68366d6d797a551606`, tree
`a9de950ca24ba002143a24744e6d8c1091e6a067`, clean. Combined reviewer0 source
gate and lead capacity/publication release remain prerequisites. No merge,
deployment, lifecycle or extra dependency allocation is authorized here.

## Hosted required coverage

Repository AGENTS requires npm tests/build and relevant audits, but does not
require them to run locally. Current `.github/workflows/ci.yml` supplies:

- Required nonbrowser checks: pinned Node install; root critical-threshold and
  BFF high-threshold production audits; `npm run ci:quick`; `npm run ci:tests`
  (script, BFF and complete unit suites). Audit artifacts uploaded.
- Production build: locked toolchain check and `npm run build`; summary binds
  `GITHUB_SHA`.
- Chromium script regression: locked Chromium and `npm run test:scripts:browser`.

`.github/workflows/e2e-smoke.yml` automatically supplies PR desktop Chrome,
mobile Chrome and mobile WebKit jobs with independent artifacts. Broad/nightly
are separate main/manual signals; do not dispatch them. Both CI and smoke run
on PR updates, not ordinary feature push alone. Update existing PR115; no new PR.
Accept only actual terminal successful commands at exact final feature head,
including logs/artifacts/retry state. Earlier b67 runs remain historical. Do not
repeat successful local full `ci:pr` or restore BFF dependencies for this package.

## Publication after release

From the canonical React worktree, verify clean exact head and fresh SSH main.
Fetch argv (each entry is one operand):

```json
["git","fetch","origin","+refs/heads/main:refs/remotes/origin/main","+refs/heads/dev/oomd-abuse-policy:refs/remotes/origin/dev/oomd-abuse-policy"]
```

Expected main40653dff and remote featureb67c7917. If main advances, rebase with
normal hooks and prove old/new range equivalence; substantive conflicts return
through lead's affected-review boundary. Rebind exact head everywhere before
publication. Do not blindly use the old lease if another writer changed remote.
With unchanged reviewed head/base/lease, exact push argv:

```json
["git","push","--force-with-lease=refs/heads/dev/oomd-abuse-policy:b67c7917e8758e707e0b88512f055eab9fbd8529","origin","55a813b44edb915c7ed5ce68366d6d797a551606:refs/heads/dev/oomd-abuse-policy"]
```

Verify SSH remote/PR head. Refresh PR115 title/body with REQ-051, selected-type
contract, quick results, review and historical/current evidence distinctions.
Write actual body to a temporary file and use `gh pr edit 115 --body-file FILE`
with separate literal argv `edit`, `115`. Preserve existing PR;
no merge/deploy action. Find automatic run IDs by exact `headSha` and event,
then a fresh native Luna/low watcher observes those IDs, not moving latest.
No duplicate workflow dispatch. Cancel only genuinely superseded nonterminal
same-branch runs after verifying headSha differs from current published head.

## Local affected browser batch after capacity release

Existing pinned browser store root is present, including Chromium1228/headless
shell and ffmpeg. Preparation only inspected symlinks; no browser or build ran.
Use retained closure rather than downloading browser engines. Root frontend
deps already restored; BFF deps/build artifacts remain unnecessary.

Worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/vpsadmin-webui`.
Environment additions (unset inherited storage/session state; no service token):

```json
{
  "CI":"1",
  "PLAYWRIGHT_BROWSERS_PATH":"/nix/store/bcf8w1529mgspizwjsp3iwvaq26plrgj-playwright-browsers",
  "PLAYWRIGHT_HTML_OPEN":"never",
  "PLAYWRIGHT_HTML_OUTPUT_DIR":"/home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-oomd-abuse-policy/react-rework-verification/browser-report",
  "E2E_BASE_URL":"http://127.0.0.1:5197"
}
```

Preflight exact source/head/tree, pinned CLI1.61.0, browser executable existence,
free local port5197 and no pre-existing server. CI mode prevents server reuse.
No policy-relaxation/container shortcut or shared host/storage state needed.
If port busy, do not stop a foreign process; select/record another free port.
Do not restore dependencies or substitute browsers implicitly on failure.

Fresh watcher receives exact argv, separate environment and log/result paths:

```json
["nix","develop","--command","npm","run","e2e","--","e2e/specs/app/vps_incident_summary.spec.ts","--project=chromium","--project=mobile-chrome","--workers=2","--retries=0","--max-failures=1","--output=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-oomd-abuse-policy/react-rework-verification/browser-results"]
```

`npm run e2e` starts the owned Vite dev server. Six cases × two projects =12:
EN/CS owner+admin detail(8), existing admin overview combined filters(2), old-API
normal overview(2). Detail asserts server counts, inclusive unscheduled cooldown,
history, admin-only isolated nullable save/exemption; overview asserts explicit
selector+both filters. Current spec explicitly captures `memory-summary.png`
before mutation and `memory-overview.png` after combined filters. All are
synthetic API data/identities; no backend enforcement/mail/authorization proof.

Logs: `react-rework-verification/browser.log`; command/head/tree/elapsed/exit
receipt alongside. Keep failed first attempt and diagnose before affected retry;
do not present an incomplete failed batch as12passed. Watcher does not edit,
diagnose, retry, install, deploy or launch nested agents. Exact argv is passed
as operands, with no prose punctuation added. No quiet timeout invented.

## Captures and final evidence

Visually inspect actual current-source desktop/mobile images, especially long
Czech heading/type, generic indicator wrapping, shared state/exemption/help and
combined filters. Select admin detail EN desktop, admin detail CS mobile and
admin overview desktop/mobile from this batch; copy exact bytes/hash into the
feature's new incident-escalation screenshot directory only after acceptance.
Show representative implemented desktop/mobile with a synthetic-data label.
No screenshot polish or additional UI product changes are in scope.

Current screenshots and evidence docs can form a separate routine evidence
commit after source proof. Bind capture source SHA/tree and exact image hashes;
if final commit adds only images/docs, prove runtime/test/toolchain identity and
still observe automatically triggered exact final-head workflows. Old b67 images
remain only under original Git ref/session historical directory; never publish
them as current shared-interface proof. Required npm tests/build use exact hosted
outcomes; no full local duplicate. Update PR115 with actual outcomes/screenshots
and residual fixture-vs-real/backend limitations. Preserve complete source,
capture, publication and CI ranges; no main integration or deployment.

[Review packet](react-rework-review-packet.md) ·
[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
