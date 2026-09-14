# Portal reliability review packet

Initiative: 2026-09-13-portal-reliability. Workspace /home/aither/workspace/ai/vpsfree.cz.
Plan/state: work/2026-09-13-portal-reliability/plan.md and state.md.
Each project worktree: worktrees/2026-09-13-portal-reliability/<project>.

| Project | Base | Head |
| --- | --- | --- |
| codex-web | aec4ea2ff13a053e340a2a47616d6fbc89aeeac1 | 62a8b3626f7defcbca343b2408c7dd1fd753cf11 |
| dev-workspace | f41d4220dd1d5ade08ba3bb28f964e9570a11ed9 | f371105cf1d19e8f7fa7fd09aced419e15478c3b |
| vpsfree-dev-workspace | 213a3db57dea9298f61309eb157c0853f2310e9b | a23002ffe2e89f5ecbf35913d074fae2695c8c11 |
| workspace | bfd4fb78732bc747995c2dd715309d7bdd58b984 | 3337cc45f00647b3ed6df575c3318e083e598b70 |
| vpsfree-cz-configuration | 3d9ffa45c7e0388c96434fd3a6127d0a54c0b9ea | 4582592a1d1ca6a1c1aa26fdee67e57332107b4e |

## Requested outcomes and decisions

- Intentionally stopping a cluster must not produce a generic global status error in other windows. Report transition locally; retain last known status, expose real provider failures locally. User chose parallel shutdown of independent VMs. Bound the complete poweroff+shutdown operation, with wrapper cleanup margin; stop and reset share runner wait.
- Returning to a tab should keep a healthy stream and hide brief recovery notices. User selected ten visible seconds before a warning. Access failures remain immediate. Preserve conversation drafts.
- Failed creation must keep the initial request visible and copyable in the portal, including before manifest creation. User chose copy-only; retry uses the unchanged receipt. Preserve pre-acceptance form drafts through HTTP/network errors and reloads.
- Recover initialization of 2026-09-13-auth-email. Read-only probes showed filtered thread/list scans timing out, indexed lookup 3ms, no existing thread for that cwd. Pinned Codex 0.154.0 supports useStateDbOnly; it can return empty for unavailable DB. Preserve loaded/unmaterialized and ambiguity checks; reject observable index inconsistencies. No Codex version update.
- Preserve exact final comparisons independent of opening repository history. User accepted explicit CLI capture after final rebase before integration, with automatic status observation as supplementary capture. Historical recovery requires recorded exact base/head and validates registered head + ancestor base. Recover password-reset comparisons from its existing merge-revisions-20260913.json after review/deploy. Existing durable review links must remain immutable.

## Commit shape and ownership

codex-web: separate optional App Server list flag/protocol tests and conversation sync UX commits. Generic provider owns wire request and reusable sync logic. dev-workspace imports its Go module and embeds its assets, pinned via Go and Nix at the same revision.
dev-workspace: separate dependency pin, workspace-specific identity recovery, creation prompt/draft UX, cluster observation/presentation, and repository capture commits. Capture persistence remains in the existing portal-owned private store; Ruby CLI holds the existing slug lock and invokes the Go capture entry point. Tests and docs accompany owning behavior. No new persistent schema.
vpsfree-dev-workspace: separate concurrent VM stop/budget, nonblocking status protocol, runtime dependency pin. It owns both provider shell helpers and shared Ruby OSVM runner. Portal interprets exit 75 as busy; old portal still reports unavailable, so matched deployment preferred. Running old runners can still be stopped by the new wrapper; no forced restart of unrelated clusters.
workspace: policy requires final capture; separate user-profile package pin. Configuration: confctl-generated exact devWorkspace pin only, for matching host module. No workspace application in system config.

## Verification

codex-web: Go ./... with TMPDIR=/tmp, protocol coverage-only corpus, Node conversation/uploads/sync browser contracts passed. GitHub Check passed at exact head.
dev-workspace: Go ./... passed except one stale text assertion after renaming Last viewed to Saved; corrected and web/repository/cluster suites passed. Final session-page cluster refresh compiled/rechecked with web suite. Ruby dev_session suite 297 tests / 3126 assertions passed; node --check app.js, creation.js, creation_browser.cjs; Ruby syntax passed.
vpsfree-dev-workspace: runner 5 tests; status 47 / 526 assertions; commands 11 /139 assertions passed with fixture testEnvironment. Shell syntax passed. Flake no-build evaluation in progress. Workspace no-build evaluation in progress.
Creation headless browser acceptance and full packaged checks reserved for after mandatory review. Browser fixture covers HTTP failure, lost connection, reload preservation, durable acceptance, copy, unchanged retry receipt.

## Risk, trust boundary, compatibility and deployment

High risk: persisted receipt/comparison state, App Server protocol, host VM shutdown, generation switching and deployment. Four review lanes required; gpt-5.6-sol xhigh. Local host operator is trusted per repository AGENTS; retain ordinary path/identity/concurrency/data-integrity guards. Remote browser clients are untrusted; preserve authentication, Origin checks, input limits, escaped prompt rendering and validated Git identities. Do not invent defenses against a compromised local administrator.

All changes additive or compatible with existing receipt, comparison schema 1, manifest and cluster state contracts. No DB migration, new Codex version or vpsAdminOS coordinated upgrade. No default-branch merges, archive, delete or session stop authorized. User authorized aitherdev deployment from configuration feature branch and profile activation. Rollback reads existing formats; UI improvements disappear. Host module pinned to same runtime commit but application remains user-profile-owned.

Operational dependency: interrupted auth-email creation has a tmux identity in its journal. Installed workspace-host refuses switch while that initialization is unfinished. Root agent is investigating supported use of candidate portal recovery with the existing journal before profile activation. Do not bypass/remove journals or restart shared App Server. Exact original request remains in private receipt; do not copy full private prompts into review reports. Cluster was intentionally stopped and remains stopped. Existing merged password-reset worktrees are retained.

## Non-goals / bounds

No session prompt editing, new resume identity policy, repository object retention/GC changes, rewritten review links, broad cluster lifecycle redesign, or upstream Codex modifications. No automatic merge, archive or cluster startup in other initiatives. Live validation should use isolated fixtures/owned cluster if needed, preserve unrelated running services.
