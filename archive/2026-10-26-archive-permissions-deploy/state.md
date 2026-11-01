---
lifecycle: complete
---

# Archive permission repair deployment

Complete: deployed and verified on aitherdev, all three exact final feature heads
merged into remote master, and all resource claims released. No remaining work
or blockers. Feature branches and session worktrees remain available.

- [x] Implementation, quick checks and independent review.
- [x] Exact-head GitHub CI and final host/profile builds.
- [x] Configuration dry activation, system activation and profile switch.
- [x] Live cleanup behavior, portal health and conversation continuity.
- [x] Three fast-forward integrations with fresh remote proof.
- [x] Resource release verified; temporary merge checkouts removed.

## Final revisions and deployment

| Repository | Final head on remote master |
| --- | --- |
| dev-workspace | deed45f04fc0698b2f2f408b2816ac124913d582 |
| workspace | 83282a493a6961d352b8ad0e2dfa3b17624fd46c |
| vpsfree-cz-configuration | cba1f93fcf2d0c2be35d4fb3dd868ba537c38656 |

Branch in all repositories: `2026-10-26-archive-permissions`. Worktrees are under
`worktrees/2026-10-26-archive-permissions-deploy/`. Fresh SSH remote queries
confirmed those exact master heads before machine release.

Confctl generation `2026-10-26--21-54-20`, built, copied, dry-activated and
switched from the configuration feature worktree:
`/nix/store/njn47bvwsflix88ndbpvrcvvznqvvfsb-nixos-system-aitherdev-26.05.20261021.da6dc0e`.

Selected workspace profile:
`/nix/store/vky6fqnaimgpi8vm2pi0362w0lz5m6zb-dev-workspace-0.2.0`.
Stable workspace-host switched with the exact session identity and held machine
claim. The deployed package and system identities matched after integration;
the final lock contract also passed. Extension, Codex and all sibling pins stayed
unchanged. Recovery follows ordinary forward package recovery and confctl system
generation recovery; no schema or migration changed.

## Verification and review

[Final CI](https://github.com/aither64/dev-workspace/actions/runs/40399435667)
passed at `deed45f0`: package/focused checks, creation VM and archive VM all
passed on their first attempt. The host job is intentionally skipped on feature
branches; actual aitherdev configuration build and live checks passed. CI log
explicitly confirms the readonly-cache archive/revival subtest succeeded.

Focused implementation checks: 11 tests / 215 assertions; packaged helper check:
1 / 3; focused preflight checks: 3 / 68. The final composed package build passed
its required checks and reused the identical successful Ruby verification
derivations. Confctl switch health checks passed (systemd and firewall, 2/2).
Installed-code smoke testing removed two disposable entries from read-only cache
directories while preserving retained Markdown content, directory/file modes,
and the external symlink target. Disposable test data was removed.

Portal `/healthz` returned `{"ok":true}` and the session page HTTP 200.
System and user service managers reported no failed services. Codex App Server
MainPID `3387667` and InvocationID `84b92a0a1c5a4fffa9a0c7beaf0693f1` were
unchanged across deployment. Active Codex stayed at 0.163.0:
`/nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0`.

Original independent reviewer `/root/archive_review`, gpt-6.1-sol/xhigh, reviewed
all four lanes and both pin histories without findings. A bounded final
refreshed-history review also found no findings; see [review.md](review.md).
Replacement reviewer thread `01a17a00-3c5f-7240-956e-f173f5f156e8` used the same
catalog model/effort with danger-full-access/never because native continuation
of the original reviewer was unavailable. Installed catalog digest:
`3ff7a2129ed39b4d6774466e53060bbff33d2cd2d893aa168c87cb3d64bd6b41`.
All final histories have one logical feature commit each; no obsolete history,
repeated pin streams, or migrations remain.

Logs are `/tmp/archive-permissions-` with suffixes `ci-final-watch.log`,
`ci-final-archive.log`, `workspace-build-final.log`, `aitherdev-build-final.log`,
`aitherdev-dry-activate.log`, `aitherdev-switch.log`, `profile-switch.log`, and
`installed-smoke.log`. Configuration keeps its native `.confctl` generation and
logs in the feature worktree; no deployment evidence was committed there.

## Integration and release

User approval: “deploy aitherdev using vpsfree-cz-configuration. when verified,
merge and release.” It covers runtime, workspace selection and configuration
selection into remote master. Later “you can track this session” authorized
tracking; earlier implementation intentionally had none. Initial tracking commit
is `368304f85`. Final evidence is maintained under the normal tracking cadence.

Each repository had a separate short claim covering target checks, fast-forward
merge, ordinary hooks, SSH push and remote proof, released immediately afterward:

- Runtime: `de18dc83-c42d-4348-bb5f-583cd65783c2` — released.
- Workspace: `8c86a924-93d9-48f7-bffe-a9db92272e8a` — released; shared tracking
  lock held during integration and unrelated working/index changes preserved.
- Configuration: `dc0fbf0e-79f5-4800-9e15-a2293b0e95c5` — released; required
  Overcommit Nixfmt/RuboCop checks passed and hooks stayed enabled.

Machine claim `1192598e-084d-43d4-8bfd-d891a3412ed6`, owner
`10097839-5b85-4ee8-a360-1e6908cfbaf1`, covered `machine:vpsfree:aitherdev`.
Deployment effects and complete deployed feature lineage were verified, then
release was confirmed by authoritative status at 2026-10-26T21:16:47Z.
No uncertain or unfinished deployment command remains.

## Baseline and recovery history

Original runtime review/CI covered `7e6d7c9c..6ca24ea1`. Before activation,
another session deployed and merged background-title fix `d2099c62` and its pins.
The archive patch rebased cleanly to `deed45f0`; range-diff reports equality and
stable patch ID stayed `926bb807a8ff07de69a04fc4a7a43f6b34475be0`.
Independent exact-tree reconstruction confirmed unchanged archive behavior and
preservation of the disjoint newer baseline. Both obsolete pin commits were
replaced with one generated final update each; no old candidate was activated.

Final reviewed workspace range was `368304f85..de68ca7ea`. A later tracking-only
master commit advanced it to `42a6f6d17..83282a493`; range-diff is identical and
Nix resolves the exact same verified/deployed package. Approval/review reuse is
limited to that equivalent rebase. Final comparisons were captured explicitly
for all repositories without inventing historical registration bases.

Earlier CI at `6ca24ea1` passed after one archive-job rerun: its first attempt
failed in an unchanged lead-repair timing scenario, before the readonly-cache
case; native success occurred eight seconds after portal failure. Logs were
inspected before rerun. The final `deed45f0` run needed no retry.

The original incident was owned mode-0500 generated dependency directories in
session `2026-10-24-workspace-session-ui` (519 read-only cache directories).
Tracking pruning failed before archive journal creation. This rollout did not
retry or mutate that session's archive operation.

A new threadless deployment session was created after tracking authorization;
our existing worktrees were moved into its group and registered through ordinary
commands. Starting with the old unregistered group slug refused before tracking
creation; no metadata refusal was bypassed. Retained feature refs remain intact.

## Documentation and next action

Runtime `docs/session-archive-recovery.md` contains the lasting cleanup contract.
Existing workspace deployment/coordination procedures and configuration
operations documentation cover this rollout; routine pin updates needed no new
configuration docs. No further action is required for this task. The session is
complete and remains open; no archive or delete was requested.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-archive-permissions-deploy/)
