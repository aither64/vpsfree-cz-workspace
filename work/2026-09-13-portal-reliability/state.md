---
lifecycle: complete
---
# Portal reliability implementation

Implementation, requested recovery and deployment are complete. On September 14
the user requested merging all five repositories into their default branches.
All five default branches have been fast-forwarded and pushed. All default-branch
CI passed; no implementation, review, deployment or cleanup work remains. Keep
the session and feature branches for follow-up; no archive, delete or session
stop was requested.

Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-13-portal-reliability/

## Ownership and revisions

All project branches are `2026-09-13-portal-reliability`; worktrees are under
`worktrees/2026-09-13-portal-reliability/<project>`. The shell-only initiative was
created with `dev-session start portal-reliability --no-codex --no-attach --json`
because ordinary initialization was broken. It retains tmux session $21 and has
no separate Codex thread. Initial tracking commit: bfd4fb7. The shared root remains
on master with unrelated concurrent edits preserved.

| Project | Final pushed head |
| --- | --- |
| codex-web | `6335da93acdcc82cc26200d2fbc7f479655aa7c3` |
| dev-workspace | `e9ed544bf66ba8be07b4fca27aede6e6fd1bfe0a` |
| vpsfree-dev-workspace | `916223fce1c5b7b78578ca8a16aaaa472c68b08c` |
| workspace | `9638606e9a6070def6604eac07dfe9c0d300e64f` |
| vpsfree-cz-configuration | `249bed1ee28e69a907edd09ea97a1144dbcdefeb` |

Reviewed bases: codex-web aec4ea2; runtime f41d422; organization initially 213a3db,
then explicitly fetched/rebased onto 9f31422; workspace final review over 7b00c83;
configuration 3d9ffa45. The workspace feature was rebased as shared master advanced.
All five exact final feature heads are merged into remote master.
Workspace integration reached master at 9638606. The final rebase over bf177af
retained both functional patches exactly, as verified with git range-diff.
The other four final feature heads did not need rebasing.

## Decisions and review reconciliation

User selected ten visible seconds before recovery warnings, copy-only display of
accepted requests, and concurrent independent VM shutdown. Retain authoritative
thread discovery. The measured auth-email scan took 61.265 seconds; extend nested
deadlines to 180/210/240 seconds. Rejected useStateDbOnly: a partial index can omit
existing rollout history even when an unrelated indexed canary exists. The proposed
indexed API and optimization were removed from the final commit series.

Overall review risk was High for persisted state, host VM shutdown and deployment.
All general, architecture, scope and risk lanes ran with gpt-5.6-sol/xhigh. Original
heads/packet and reports are in review/. Architecture and risk reruns cover the new
provider contract and shared full cluster renderer; no further rerun is required
for their direct cache-eviction fix. All findings are resolved:

- Risk Blocking: unsafe indexed absence/uniqueness proof removed entirely.
- General/Risk: full cluster refresh replaces cards, including absence, and
  delegates controls. Shared template owns badge rendering. Follow-up Important
  cache bug fixed by evicting each absent or successfully released provider;
  regressions cover running -> busy -> absent -> recreated/busy and multiple providers.
- Risk: first exact comparison base/head is immutable; conflicting captures
  reject, identical pairs are no-ops, and fallback cannot replace exact state.
- Architecture/General: explicit captures wait for the writer lock within context;
  supplementary observation logs failures and runs after readable primary status
  with its own one-second budget. Removed redundant state-endpoint observation.
- Architecture: runtime owns additive busy exit 75 and release ceiling 180 seconds;
  organization owns shutdown.json (120 grace, 10 kill, 20 cleanup), consumed by
  Ruby and shell and validated against the runtime ceiling.
- General: form draft also restores model and effort.
- Scope: final capture rule covers the separate workspace integration workflow.
- Architecture advisories: one normalized approved-plan prompt projection and
  shared cluster badge rendering. No outstanding accepted-risk finding remains.

## Recovery and deployment

Auth-email recovery used the installed private CLI derived by installed
Host.dev_session_invocation with its current generation/token/transition checks.
Only --portal-command pointed at the reviewed candidate; original goal SHA, exact
failed attempt 3, receipt ID and request binding were verified first. The CLI
completed in 57.26 seconds. Receipt is ready and thread
01a09dca-ba5b-7f80-8d5e-ccade3fb0823 contains exactly one matching original prompt.
The normal profile switch then succeeded. Stable sync and an exact-thread resume
under the shared transition lock rebound the temporary portal executable to the
deployed package; no message was resubmitted and no thread was replaced.

Deployed profile generation 38: mk77xsg4qrk075smiyazc2vqb18p5b2y. Shared App Server
PID 1090021 stayed running. Configuration generation 2026-09-14--04-42-31 built,
dry-activated and switched successfully; both health checks passed. Retain previous
generations for rollback. No schema migration or coordinated node update is needed.
The system application remains user-profile-owned; configuration only pins the
matching host module.

Password-reset comparisons recovered through the stable CLI from its existing
merge-revisions-20260913.json. All four exact bases/heads are verified by the portal
without warnings. Its branches, worktrees and durable review links were preserved.

## Verification and cleanup

See validation.md for exact CI links, counts, deployed store paths and live results.
Current-head codex-web, runtime and organization CI passed. Packaged Go/Ruby tests,
workspace deployment contract, provider tests and creation/repository Playwright
checks passed. Real dual bridge guests stopped concurrently in 86.46 seconds, with
both QEMU exits successful and no runner timeout termination. Guest boot was slow;
stop waited for the shells, then completed within the shared grace period. Forced
reaping is covered by the focused stuck-poweroff test, not claimed from the live run.
Live browser saw scoped transitions, stopped and absent states without JS errors.
Our test cluster was reset, and all of its VM/runner/socket/state resources are gone.
Other sessions' clusters were untouched.

No superseded active CI remained to cancel. All product worktrees are clean.
Temporary testing scripts/binary, generated
configuration shell helpers and the four temporary integration worktrees are removed.
Keep retained feature branches, worktrees, private comparison data and this initiative.
The user has authorized default-branch integration. No additional approval is pending.

## Operational lessons

- Canonical organization bare clone lacks a fetch refspec: use explicit master
  fetch and exact force-with-lease SHA. Resolve the dependency-only rebase conflict
  with the final runtime pin; push before downstream flake fetches.
- Keep Nix source, Go module and vendor hash pins aligned. See
  notes/dev-workspace/2026-09-13-indexed-initialization.md.
- Configuration Nix shell must start at its worktree (Gemfile); confctl build/deploy
  needs --yes noninteractively when deployment is already authorized.
- Existing repository browser fixture omitted sync.js. Temporary route fix made
  all checks pass; see notes/dev-workspace/2026-09-14-repository-browser-sync-route.md.
- HTTPS routing returned expected unauthenticated 401; the local curl CA bundle
  lacks the portal issuer. Browser application checks used the portal Unix socket.

## September 14 default-branch integration

User explicitly requested all default branches, including configuration. See
integration.md and merge-verification.json for final heads, captured comparisons,
validation and exact remote ancestry proofs. All five merges are pushed; all local
packaged checks and aitherdev configuration build passed. The application and
system store paths exactly match the active deployment, so no restart or switch
was needed. All five Repositories views preserve their saved comparison without
warnings. Default-branch CI passed: codex-web 34820231658, runtime 34820446172
(both fast and host jobs), organization 34820482649 (including packaged provider
evaluation and runner loading). merge-ci.json records exact heads, job results
and links. No superseded active runs require cancellation. Lifecycle is complete,
but tracking stays under work/ and the session remains open for follow-up.
Retain all feature branches and original feature worktrees until the user asks
for archival. No next operator action is required.
