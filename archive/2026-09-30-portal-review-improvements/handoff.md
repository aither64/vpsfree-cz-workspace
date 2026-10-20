# Portal review integration handoff

## Completed

All seven registered final feature heads are integrated into their configured
remote defaults. Four default branches fast-forwarded; three dependency heads
were already contained. Fresh SSH fetches and merge-base checks prove every
exact head is an ancestor. Configuration and workspace rebases were conflict-free,
range-diff-equivalent and independently reviewed with no findings.

| Repository | Final feature head | Default |
| --- | --- | --- |
| codex-web | d210d3f7cc93981d0ab163b1fcf0718f9587f47e | master |
| dev-workspace | 869b8d4728394127ba949dc76724dce56eae136b | master |
| vpsadmin | 5c76e3290481b297dcd0baa76d246133f0353d8f | master |
| vpsadmin-webui | 534caa83a5f97d2b40b4a126886649b14dc9e8d3 | main |
| vpsfree-cz-configuration | 9824c02b657ad394dce6b81ed10abfbf3aed9d0e | master |
| vpsfree-dev-workspace | 074926d33f7306288f7cfad87c6a85e8a430e750 | master |
| workspace | c3b0361cc4e9ad51d58304b833c0e5cdd4c4b27f | master |

Source feature refs and worktrees are retained. Pre-rebase workspacecd287 and
configurationd24 source objects have retained provenance tags. Shared master
remains on master; unrelated files/index changes were preserved.

## Verification and deployment

The complete independent history/migration review and all nine predeployment
stages passed at their documented heads. No feature-authored database or persisted
migration; selected API's nine upstream migrations retain unknown production
provenance and unproved older-API rollback. Rebase equivalence review and final
comparison/parse/JSON/whitespace/package-evaluation gates passed.

Selected package remains /nix/store/z20g487rcankkgaprsrdya5na079i1rl-dev-workspace-0.2.0,
runtime1227/extension074/workspacecd287. Switch0/70s, actual portal executable and
service health verified; live models show exact gpt-6.1-sol high/xhigh among9.
V4 live acceptance exited0/10s with six summaries, layout/spacing, empty diffs,
history-focus retention, reload reset and no page errors. Its unavailable workflow
sample did not exercise populated counters/run-link focus or nonempty previews.
The earlier terminated v3 remains incomplete; it is not relabeled as a pass.

## CI: initial state only

The user explicitly forbids waiting for post-push CI completion. Initial states:

- [Generic Check36904460292](https://github.com/aither64/dev-workspace/actions/runs/36904460292): in progress.
- [Extension Check36904534674](https://github.com/vpsfreecz/dev-workspace/actions/runs/36904534674): in progress.

No new push-triggered CI applies to configuration/workspace. No new push was
needed for unchanged dependency defaults. No CI-wait watcher was started.

## Held

Shared DNS/configuration deployment remains unpublished even though its source
is merged. Before any later approved publication, rerender/build its four DNS
consumers against9824 and follow the separate deployment gate. No successful
profile-switch retry, system/cluster activation, archive/delete/stop or session
retirement occurred. Session remains active/open.

Details: [integration](integration.md), [state](state.md), [rollout](rollout.md).
Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-30-portal-review-improvements/
