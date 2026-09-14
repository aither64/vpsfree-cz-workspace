---
lifecycle: complete
---

# Portal question composer fix

## Current status

Implemented and pushed the approved question/composer behavior and downstream pins.
Quick checks and the Chromium regression passed. All four mandatory review lanes
report no findings. Both feature CI runs passed.
Packaged checks and the assembled site build passed. Deployment to aitherdev
succeeded as profile generation 39, and HTTPS/asset/browser checks passed.
All three changed repositories are fast-forward merged and pushed to master at
the exact reviewed/deployed heads. Local integration checks passed. Runtime
default CI passed; extension default CI was still running when the user explicitly
requested no waiting for workflows. No further CI monitoring is owned by this
session. Canonical archival performs the remaining clean-worktree removal and
records terminal lifecycle; all branch refs are retained.

## Repositories

All worktrees use branch `2026-09-14-portal-planning-question-controls` under
`worktrees/2026-09-14-portal-planning-question-controls/` and are registered in
`portal.yml`:

| Repository/worktree | Review base | Committed and pushed head |
| --- | --- | --- |
| dev-workspace | e9ed544bf66ba8be07b4fca27aede6e6fd1bfe0a | df21f2ea8fe27efdb2cb8c0330fa31acd0f3a933 |
| vpsfree-dev-workspace | 916223fce1c5b7b78578ca8a16aaaa472c68b08c | 89a03581b13056fa83114e592f2e2993e6a87887 |
| workspace | f523eddf3e1d1cdebf445992318247030e11c7f3 | 1e01e557cac5527666d5b1e35fa52fadcdbb81af |

The codex-web worktree is unchanged at base/head
`6335da93acdcc82cc26200d2fbc7f479655aa7c3`; its unchanged feature branch was pushed for archival ancestry verification.
The workspace feature was rebased onto shared master before its pin commit;
its initial registered base was `8fed27b0e5210a47c66d461a8ca8d35d6b15cdf2`.
All project worktrees were clean before canonical archival. All changed default
branches are now integrated and pushed; see integration-results.json.

## Investigation and decisions

- The host portal, not codex-web, owns this layout. Existing full composer hiding
  covered completed plans only; questions merely compacted controls below 600px
  height. Real deployed assets matched the investigated upstream base.
- Original fixture reproduced the bug at 1440x1000, 1280x720, 1280x540 and 390x844.
  See `investigation.md`, `layout-results.json` and `deployed-assets.json`.
- User approved all answerable questions in both modes, with one existing
  Interrupt control moved into the first question header. Priority is questions,
  completed-plan decisions, ordinary composer. Preserve DOM, drafts, uploads and
  focus; other approvals and unanswerable cards retain ordinary controls.
- Deployment uses the assembled site package through the stable installed
  `workspace-host switch --source` command. No system configuration or
  vpsfree-cz-configuration change is needed. User authorized deployment but asked
  to retain unmerged branches and the open session.
- No schema, protocol, authentication, origin, persisted format, Codex package or
  codex-web pin changes. Existing state remains compatible with rollback.

## Commands and verification

- Created this owned initiative using
  `dev-session start portal-planning-question-controls --no-codex --no-attach`.
  Initial plan/state committed as `bf37c8f` before project mutations. Use both
  `DEV_SESSION_SLUG=2026-09-14-portal-planning-question-controls` and
  `DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz` for current lookup.
- Fetched upstream before feature pushes and downstream pins; preserved unrelated
  shared-master working tree and index changes. Read repository-local AGENTS.md.
- JavaScript syntax checks for app.js and question_browser_test.cjs passed in Nix.
  Focused Go tests `TestShippedBrowserClientMatchesSessionAPI|TestImplementPlan|TestPlanDecision|TestSession`
  passed with `GOWORK=off GOFLAGS=-mod=mod` in the Nix development shell.
- Real-renderer Playwright regression passed in 22.07 seconds. It uses actual
  template/CSP/assets, open SSE and the upload handler, with controlled thread and
  pending responses. Covered blocking/async Plan/Default questions, repeated and
  changed snapshots, failure/reconnect/retry/removal, draft/focus/selection,
  Interrupt, uploads, other approvals and plan priority. Five viewports passed;
  640x360 represents the CSS viewport of 200% zoom, not actual browser zoom.
  `browser-results.json` and `verification-notes.md` contain details and commands.
- Nix flake evaluation (`nix flake check --no-build --print-build-logs`) passed
  for organization and site pins. `git diff --check` passed. No declared custom
  executable hooks were found; commits used message files and no hook bypass.
- Generic CI [34826487311](https://github.com/aither64/dev-workspace/actions/runs/34826487311)
  passed its fast checks; host VM job is intentionally skipped on feature pushes.
- Organization CI [34826644831](https://github.com/vpsfreecz/dev-workspace/actions/runs/34826644831)
  passed flake checks and development-cluster checks. Site has no CI workflows.
  No CI failure or rerun occurred. Automatic CI started after pushes needed by
  downstream immutable pins; local long checks remain behind the review gate.

## Mandatory review

Applied mandatory-change-review with fresh standalone general, architecture,
scope and risk reviewers, all `gpt-5.6-sol` at `xhigh`. Risk classified high
conservatively for live deployment and old/new browser assets; the change itself
adds no state or security contract. Exact commits and lane rationale are in
`review-packet.md`. All four lanes have no Blocking, Important or Advisory findings. No conflicting
findings require reconciliation, and no remediation or rerun is needed. The
review gate is satisfied for the exact heads above; proceed to packaged checks.

Coverage limits: browser test is opt-in and Chromium-only; a replacement on a
later page within one multi-question request and mixed asset combinations were
not separately automated. No live Codex App Server question was submitted.
These limits do not affect unchanged protocol/answer encoding. Browser coverage,
source review and exact deployed asset verification are the acceptance evidence.

## Deployment and cleanup

Rollback profile is generation 38,
`/nix/store/mk77xsg4qrk075smiyazc2vqb18p5b2y-dev-workspace-0.2.0`;
see `pre-deployment.json`. Router, portal, Codex and tmux services were active;
private static asset requests returned HTTP 200 and Cache-Control no-store.
Deployment and post-deployment validation passed; generation 38 remains retained
for the stable `workspace-host rollback` command. No rollback was needed.

User subsequently authorized default-branch integration and cleanup. Archive
through dev-session after merge/CI verification, retaining branch refs. Follow-up tracking remains in the working tree under the short-session
checkpoint policy. Durable browser setup/fixture lessons are in
`notes/dev-workspace/2026-09-14-playwright-full-chromium.md` and
`notes/dev-workspace/2026-09-14-question-browser-fixture.md`.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-14-portal-planning-question-controls/

## Packaged verification and deployment start

- Generic `nix flake check --print-build-logs` passed, including package tests,
  extension/namespace/host contracts and host-module-idempotency NixOS VM.
- Site `nix flake check --print-build-logs` passed: 3 tests, 14 assertions.
- Site `nix build --no-link --print-out-paths` passed and produced
  `/nix/store/9z5g3q4akpzjc2449r6q6hlivvw1ja0x-dev-workspace-0.2.0`.
- Organization flake and devcluster checks passed in feature CI; no redundant
  local run. Host migration VM is not applicable because its behavior/contract
  is unchanged. No local kernel build occurred.
- Authorized `workspace-host switch --source` from the stable installed helper
  against the clean site feature worktree completed successfully after reviews.

## Deployment result and handoff

- Active profile: `profile-39-link`, package
  `/nix/store/9z5g3q4akpzjc2449r6q6hlivvw1ja0x-dev-workspace-0.2.0`.
- The helper validated the active Codex 0.154.0 App Server contract, retained its
  generation root and activated the package without forcing a busy session.
  No system configuration deployment, default-branch merge or lifecycle action.
- Verified the public HTTPS endpoint with the actual local CA and hostname:
  health and this initiative return 200; unauthenticated static assets return
  401. Router, portal, Codex and tmux services are active.
- Public app.js SHA-256:
  `9d997d8986c526c5397cd690c579a2477ebb2c2074c2eb5be3f4bb9486baec3f`.
  Public style.css SHA-256:
  `683cd10bf05b676e12f7cdbf1263009bfd3f651bf4cf5bbb0cef2eeb5110491a`.
  Both match the exact reviewed source and return `Cache-Control: no-store`.
- The live Chromium smoke check passed for this owned initiative: Handoff and
  Repositories tabs work, all eight observed asset responses are 200, no page
  errors and no mutation attempts. Question behavior is proven by the committed
  real-renderer regression plus matching deployed assets; no live user question
  or conversation was answered or interrupted.
- The first live Chromium launch rejected the private CA because the SPKI
  allowlist used the root CA, which is omitted from the served chain. Fixed the
  harness by first verifying the live TLS leaf with CA/hostname validation and
  pinning that leaf key in Chromium. It then passed. No blanket TLS bypass or
  credential exposure. Reusable lesson:
  `notes/dev-workspace/2026-09-14-browser-private-ca-leaf-pin.md`.
- One smoke invocation entered the shared-root Nix shell by mistake. It was
  interrupted during environment construction and rerun in the intended generic
  feature worktree. No repository or deployed profile changed from that attempt.
- All four worktrees remain clean at the reviewed heads. Stable
  `dev-session current` with both explicit environment identities and
  `dev-session url` were verified after the switch. Registered branches remain
  unmerged; lifecycle stays active. No further test/deployment work is pending.
- User action: reload an existing portal tab to obtain the new assets. Existing
  pages can retain old JavaScript until reload. Branch integration remains for
  later explicit direction; the session is open for follow-up.

## Integration authorized

User requested “merge into default branches and clean up”. Explicitly fetched
master for all project repositories and origin for the shared workspace. All
feature heads are unchanged and descend from current defaults. Shared master is
still f523edd and is the workspace feature's reviewed base. Existing reviews and
tests therefore apply without remediation or reviewer reruns. Preserve unrelated
shared working-tree/index changes. Capture comparisons before fast-forward merges.

Saved pre-merge comparisons for generic and organization against their recorded
bases. The workspace comparison captured its actual remote-master base 8fed27b,
which includes four pending shared coordination commits before reviewed base
f523edd. A narrower second capture was refused because snapshots are immutable
per head; preserve the valid original snapshot. Unchanged codex-web has identical
base/head, so no comparison can be stored. Its retained feature ref was pushed
at the unchanged SHA so canonical archival can prove all registrations remotely.
No product changes or review reruns are needed. Durable capture behavior is in
`notes/dev-workspace/2026-09-14-comparison-capture-unchanged-branches.md`.

Integration uses fresh detached target worktrees (recorded in
`runtime-merge-worktree.txt` and `extension-merge-worktree.txt`) with fast-forward
merges from origin/master. Full packaged checks are running there; the site
feature deployment-contract check passed again (3 tests, 14 assertions).
The unchanged codex-web feature push also passed CI run 34832597554.

## Final integration and cleanup

- dev-workspace master: df21f2ea8fe27efdb2cb8c0330fa31acd0f3a933.
- vpsfree-dev-workspace master: 89a03581b13056fa83114e592f2e2993e6a87887.
- workspace master received 1e01e557cac5527666d5b1e35fa52fadcdbb81af through
  shared-master fast-forward, without staging or altering unrelated edits.
- codex-web remains unchanged at 6335da93acdcc82cc26200d2fbc7f479655aa7c3;
  its registered feature ref points to the same already-merged revision.
- Fresh temporary integration worktrees for runtime and extension were removed
  with non-force git worktree remove after testing/pushing. All three packaged
  checks passed; no source/reviewed head or deployed package changed.
- Runtime default CI 34832869276 passed both fast and host jobs. Codex-web
  unchanged-branch CI 34832597554 passed. Extension default CI 34833078027 was
  still in progress. User explicitly said “no waiting for workflows”; stopped
  monitoring and proceeded with archival. Earlier feature CI and fresh local
  packaged integration checks passed for that exact extension head.
- Removed reproducible raw build/browser logs and temporary integration path
  records, retaining concise results, reviews, scripts, deployment evidence and
  exact revision records. No credentials, caches or bulk captures are retained.
- Canonical `dev-session archive` is the requested cleanup operation. It proves
  exact remote ancestry, removes all four clean registered worktrees, preserves
  branches and comparisons, commits tracking under archive and retires session
  runtime. The portal URL remains stable and becomes read-only.
- Active deployed profile remains generation 39. No redeployment or rollback is
  needed because merged source heads equal the reviewed deployed revisions.
