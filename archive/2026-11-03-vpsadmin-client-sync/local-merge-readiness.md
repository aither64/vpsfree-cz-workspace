# Local merge readiness — 2026-11-04

> Historical local-preparation snapshot. All six candidates are now integrated; workspace final head advanced equivalently to08ec23ca. Current results are in [phase2-integration.md](phase2-integration.md).

All six local feature worktrees and prepared targets are clean. Each feature has
one reviewed documentation commit; no obsolete history, repeated update streams
or migrations. Workspace and WebUI refreshes have independent local-readiness
addenda and separately reconstructed Git trees. No defaults have been changed.

| Repository / target | Prepared local base | Final local feature head |
| --- | --- | --- |
| vpsadmin / master | 942c6eaed41331f823d8e0f670ed239e2b308440 | 4ac49f49e63545200df8afa920c6eafda8722523 |
| vpsadmin-go-client / master | 7bc136e1d72f15174229bea2bb7de284174512f2 | af9a819ca35f6de5556092679b4df7cb72e7aa89 |
| vpsadmin-rust-client / main | 49e45527a5683ffe4c03d1b46a74ac137ffa2f9f | 823a4f8450fce4947310fc81bcdebdca91d9ffae |
| vpsadmin-typescript-client / main | c53cb4dabb0b3aac8d05834478872d2cfa698fa7 | 2da950a98fa13468b36d03b13fb5e81cca206e0e |
| vpsadmin-webui / main | babe51421bd1df61a548e7b2f047053df14ff3eb | 47b6992e28c16585aa6247bd75413637a7ca6388 |
| workspace / master | 0a523edf603adc37a62d51236ab273fd2a6302a0 | 9627ae2c84df71702ca74ea0cf8138b473b9eca3 |

HaveAPI stays excluded: its clean owned feature equals public-baseline f29c1e46
with zero diff. The rejected policy commit and all original source/review evidence
are preserved. Existing site workspace routing suffices; no extension feature.

All prior checks remain tied to their actual heads. Latest WebUI audit passed
at47b6992e (exit0/6s,179documents/76requirements/257routes/74modules), with101scoped
links/whitespace checks. Required audit/dependency/toolchain inputs were checked
unchanged; no npm setup was repeated. Final local reviewer0 reports no findings.
API root/API bundle checks and normal post-merge hook probe pass under the
prepared exact-store environment; no installation is needed inside merge claims.
Other candidates retain unchanged independent review/CI evidence.

## Wait and later continuation

The migration completion condition is satisfied by the user and the peer's
terminal noticebd479620-ec09-480c-9645-8e27e3296c66. Conditional approval for these
six targets is retained. Latest user direction is to prepare everything locally
and wait for GitHub recovery. All network/auth probes, publication and integrations
are stopped. No background retry, active command, watcher or resource claim remains.

The user-authorized SSH retry still exited128 with Permission denied(publickey).
No credentials/configuration were changed.47b6992e and9627ae2c are local only;
remote features were last successfully observed atfa7d7732 and839b8485 respectively.
Cached public objects and API metadata are not fresh SSH proof.

On resumption: verify SSH access/current remote targets; refresh only if needed,
retaining reviewed lineage. Publish the two rebased features with their exact
old-head leases; update existing PR127 and observe actual new-head automatic CI
(including public broad-smoke branch/PR triggers). Do not relabel old CI. Then
perform API-first sequential FF integrations under one short repository claim at
a time, ordinary hooks, SSH push and remote proof; release before CI/records.
Workspace additionally uses the nonblocking tracking lock after its repository
claim. Fresh checks inside claims remain required. No deployments or lifecycle
operations are authorized. Keep this session open and retain feature refs.

Ready commands and exact environments are in owner packets:
[API](vpsadmin-local-ready.md), [Go/workspace](phase2-go-workspace-packet.md),
[Rust/HaveAPI](phase2-rust-haveapi.md),
[TS/WebUI](phase2-webui-final-refresh-review.md).
[Independent reviews](phase2-review-result.md).

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-vpsadmin-client-sync/)
