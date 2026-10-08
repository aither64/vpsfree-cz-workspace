---
lifecycle: complete
---

# Shared workspace file links

Phase: complete. All three exact reviewed feature heads are fast-forwarded
into their remote master branches, with no rebases or new code changes. Master
CI 37607262893 passed both fast and host jobs at the deployed runtime head.
Final comparisons and remote proofs are saved. Deployed host/application and
live acceptance remain valid. Temporary integration worktrees were removed;
all feature worktrees and refs remain. No work or blocker remains. The session
stays open for follow-up; no archive or deletion was requested.

## Phase checklist

- [x] Reproduce 404 and agree tracked shared-file scope.
- [x] Create owned initiative and three registered feature worktrees.
- [x] Implement, document, commit and publish all final changes.
- [x] Pass quick checks and final independent whole-branch review.
- [x] Pass packaged/composed checks, CI and exact aitherdev host build.
- [x] Deploy matching host configuration and application user profile.
- [x] Pass authenticated live API and real Chromium browser acceptance.
- [x] Obtain explicit integration direction and merge exact final heads.
- [x] Collect post-merge master CI result and reconcile final state.

## Ownership and exact final heads

Verified initiative: 2026-10-07-workspace-file-links in
/home/aither/workspace/ai/vpsfree.cz. Complete literal session environment
matches `dev-session current`; retained root thread is
01a1151a-03e0-74b1-9c58-687cf8da58c7. Initial coordination commit: 48a0d980.
No roster was added; the lead owns design and application edits. Temporary
independent reviewer and operation watchers followed installed catalog policy.
Preserve unrelated shared-master changes, all feature branches and worktrees.
Master integration was explicitly approved for these three targets.
No archive, delete or forced interruption was authorized.

All feature branches are `2026-10-07-workspace-file-links`, under
`worktrees/<slug>/<project>`. Each is clean and matches its published feature
tracking ref; see [final status](final-worktree-status.json).

| Project | Reviewed, published and deployed head | Original base |
| --- | --- | --- |
| dev-workspace | 9e8e6e87a5a4844d4639ddf4008de483d1897f4c | e3315a483f3d3536d492ecbe40f2655449cf630f |
| workspace | 70035dfe565058054e30efe2562c655c80dd183c | 48a0d980c24a7e725b40c8854c8e992935639afe |
| vpsfree-cz-configuration | 5447020fccf99705e65a907cfe6e80684a5a1577 | 6f6aff9029cd57e1a0f9201356f7fdc9f6480671 |

Runtime history has three coherent commits: shared file viewer, lifecycle
receipt contention correction, and stable archived-observation fixture.
Each downstream branch has one consolidated pin commit. Full history and
final diffs were independently reviewed: no obsolete implementation paths,
unused transitions or migrations. Both final pins select the identical runtime;
extension 0ff827df, Codex, Nixpkgs, llm-agents, siblings and follows paths retain
previous identities. The final deployment contract passed.

## Behavior, documentation and review

Absolute shared-file links map to `/workspace-files?path=...#L93`. The shared
API serves current contents of tracked regular files within the exact workspace
Git root, under existing UTF-8, size and line limits. Traversal, untracked files,
symlinks, and repository/worktree/session namespaces remain excluded. Existing
session and archive viewers retain their boundaries.

Lasting behavior is in the runtime's `docs/workspace-portal.md` File links
section, with the lifecycle correction in its owning guide. The lead applied
user-facing writing directly. [Design](design.md), [complete branch inventory](branch-inventory.md),
[review packet](review-packet.md), [review evidence](review-result.md) and
[executed rollout](rollout.md) keep temporary scope and deployment evidence here.
Independent reviewer file_link_review used gpt-6.1-sol/xhigh from the installed
catalog because the roster is null. It found no findings at these final heads,
confirmed complete history and matching pins, and explicitly concluded no
migrations. Earlier specialist conclusions cover unchanged final production code.

## Verification evidence

- Focused source-file Go checks passed 2.125s; browser contract, JS syntax,
  formatting and owned diff checks passed with pinned Nix tools.
- Lifecycle contention checks: all three passed 300 repetitions in 34.758s.
- Stable archived observation fixture: passed 500 repetitions in 5.120s;
  unchanged clean baseline reproduced the original failure.
- Final runtime flake check: passed 675s, including VM smoke 257s.
- Final composed flake check: passed 634s; exact aitherdev build: passed 119s.
- CI 37586905151: success at runtime 9e8e6e8; fast passed and feature host job
  skipped. Local VM checks passed independently. All final *-9e8e6e8.exit are 0.
- Post-merge CI 37607262893: success at exact runtime 9e8e6e8 in 11m 1s;
  both fast and host jobs passed. [Final master CI evidence](master-ci.json)
  and master-ci.log/.exit record completion with exit 0 and no running watcher.
- Host deployment passed both confctl health checks. Application activation
  selected exact candidate y0j44svp, all three services active/running, and pending
  Codex transition cleared. [Current deployed status](deployment-status.json).
- Live API: all 15 checks passed, including CA-verified TLS, original 302,
  canonical viewer 200, current tracked contents, authentication, excluded and
  untracked paths, and existing session viewer/API. [API evidence](live-verification.json).
- Real Chromium browser: passed in 4s, including read-only editor, line 93 highlight,
  clipboard/copy-link, gutter navigation to 94, missing-line notice, root AGENTS,
  existing session source, size/binary notices and no page errors.
  [Browser evidence](live-browser-verification.json), live-acceptance.log/.exit.
  [Screenshot](shared-file-viewer.png) was visually checked by the lead.
  Browser development-TLS exception is backed by the separate CA-verified probe.
- Portal validation passed 239 manifests before activation and handoff.

The two verification-driven source corrections fix reproduced baseline issues;
no production proof or test assertion was suppressed. [Historical checkpoints](verification-history.md)
and logs retain intermediate setup, failed and cancelled checks. Fresh operation
utilities observed final checks/deployments and executed the exact prepared live
scripts; the lead owns diagnosis, corrections and acceptance.

## Deployment result and resolved intermediate refusals

Selected host:
/nix/store/gknwlgf8v3lhva6yr1ky8c367fi3sqn2-nixos-system-aitherdev-26.05.20261006.b253099.
Selected application:
/nix/store/y0j44svpcdpqzvjj43n5kg06iqfnxvzv-dev-workspace-0.2.0.
[Rollout](rollout.md) records prior generations, exact units and full evidence.
The user directed deployment, then explicitly approved the three master merges.

Early application attempts refused before selection while another session's root
and later implementer were active. No member was interrupted or forced idle;
the helper restored quiesced terminals. A standalone team readiness probe later
omitted DEV_WORKSPACE_CODEX_HOME and could not prove an archived member; it was
cancelled and did not establish a deployment blocker. The normal launcher supplies
the required context and then completed all preflights and activation normally.

Initial browser evidence used a role selector that excluded CodeMirror's visible
aria-hidden gutter. DOM diagnosis verified the link and cause; correcting only
the fixture selector preserved all real click/navigation assertions. Final browser
acceptance passed. Product code and reviewed heads were unchanged. Prior failures
remain in *.first and *.retry1 artifacts, with live-browser-diagnostic.json/PNG.

## Next action and retained state

Integration and verification are complete for dev-workspace/master,
workspace/master and vpsfree-cz-configuration/master at the exact reviewed
heads. There is no next required action. Retain all feature branches and
worktrees for follow-up. No archive or deletion is authorized.

The prepared deployment wrapper was scoped to the previous profile; its old
selection guard now correctly refuses another run. The live wrapper requires
this deployed profile and completed activation. Use the ordinary stable launcher
for any future authorized forward transition; do not modify private state or
manually relink profiles. There is no pending transition or deployment process.
Completed transient units remain under RemainAfterExit for evidence.

Playwright tools GC root remains retained for follow-up evidence checks. Feature
worktrees and ignored configuration development cache remain available for
follow-up work. No further tracking checkpoint is required under short-session
cadence. Keep the untracked rejection-probe note untracked if repeating the exact
live API script. Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-07-workspace-file-links/.

## Explicit integration approval

The user said "merge" immediately after the handoff naming the three published
feature branches. This authorizes dev-workspace/master, workspace/master and
vpsfree-cz-configuration/master for this initiative. The approved set includes
no other repository, archive, deletion or branch removal. Exact reviewed heads
remain 9e8e6e8, 70035dfe, 5447020f; preserve authorization through a clean
patch-equivalent rebase only, and reassess material changes under normal rules.
Fetching target refs and recording final comparisons precede fast-forward-only
integration. Shared-master unrelated files and index must be preserved.

## Exact-head integration result

User approval "merge" covers the three targets identified in the preceding
handoff. Fresh upstream refs were ancestors of each reviewed final head; no
rebase was necessary. The supported comparison helper captured all three before
integration. Independent project masters were advanced in fresh temporary
attached-master checkouts, tested, and pushed over SSH. Workspace master was
fast-forwarded in the shared root without staging or changing branch.

Final remote masters and retained feature heads are exactly runtime 9e8e6e8,
workspace 70035dfe and configuration 5447020f. [Integration proof](integration-proof.json)
records full SHAs and preservation of 86 unrelated modified files plus unrelated
index entries. Clean temporary target checkouts were removed with non-force Git
commands; no feature ref or checkout was removed.

Integration browser contract passed from its required portal/internal/web CWD;
the deployment contract passed using integrated workspace and configuration.
The first browser command used the repository root and failed its relative
static-file read; corrected CWD passed without product edits. Two temporary
configuration commands overlapped during initial shell setup; one aborted
without mutation. After both exited, the checkout was clean and sequential
fast-forward passed. Incidental workflow lookup/removal commands with the wrong
repository context refused; corrected scoped commands passed. No reset, stash,
force, hook bypass, commit rewrite or scope expansion was used.

Fresh file_link_master_ci_watch observed exact push run 37607262893 at 9e8e6e8.
It completed successfully: fast and host passed; the watch returned exit 0 and
no operation remains. Full master-ci.log/.json/.exit are its evidence outputs.
Workspace has no workflows; configuration has only scheduled/manual daily-update,
so this push triggers no configuration CI. The requested integration, remote
pushes and all verification are complete. Lifecycle is complete; the session
and retained feature worktrees remain available without archival or deletion.
