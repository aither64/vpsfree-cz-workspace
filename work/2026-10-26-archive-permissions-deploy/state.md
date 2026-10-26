---
lifecycle: active
---

# Archive permission repair deployment

Phase: candidates built; preparing claimed activation.

- [x] Implementation and focused Ruby checks (11 tests / 215 assertions),
  packaged helper check (1 / 3), and focused preflight checks (3 / 68).
- [x] Independent final review and pin/history review: no findings.
- [x] GitHub CI passed at runtime 6ca24ea1; archive VM passed on attempt 2.
- [x] Matching runtime pins committed and published; deployment contract passed.
- [x] Application and aitherdev configuration built.
- [ ] Acquire aitherdev, dry-activate and activate configuration/profile.
- [ ] Verify live effects and disposable cleanup behavior.
- [ ] Integrate three exact heads into remote master and release claims.

## Ownership and authorization

Created a new threadless deployment session through dev-session after explicit
tracking authorization. Existing owned worktrees were moved into its group and
registered without guessed historical bases. No retained team; mandatory review
used the installed catalog fallback. User deployment/merge/release approval is
recorded in plan.md. The original session 2026-10-24-workspace-session-ui is not
owned or modified by this deployment.

## Revisions

All branches: 2026-10-26-archive-permissions. Worktrees are below
worktrees/2026-10-26-archive-permissions-deploy/.

| Repository | Reviewed base | Final head |
| --- | --- | --- |
| dev-workspace | 7e6d7c9cdb3388ab7abc720c034c15c21afbd686 | 6ca24ea1bb6269218a1369c84d78ee9f2d559e81 |
| workspace | 978a2f280185f3ae114c2db13130f13e6976b159 | d952cc45c00899fc652910ae30cecb99c73826cb |
| vpsfree-cz-configuration | 880a6253f8d6cc1368e633f936b174792e86bff7 | 169483a37fd0e6c11ab9b90ad5d8023ed82144dc |

One coherent commit per repository; no obsolete approaches, repeated pin
streams, or migrations. Reviewer /root/archive_review, gpt-6.1-sol/xhigh,
reviewed all four lanes for runtime and general/scope/risk for rollout pins.
Catalog digest 3ff7a2129ed39b4d6774466e53060bbff33d2cd2d893aa168c87cb3d64bd6b41.
Full exact histories and final diffs were reviewed. No findings or reruns needed.

## Verification

CI: https://github.com/aither64/dev-workspace/actions/runs/40392164634
The first archive VM attempt failed in an unchanged lead-repair timing scenario
before the new readonly-cache subtest: portal failure preceded native successful
completion by eight seconds. Logs were inspected; only that failed job was
rerun without source changes and passed including the new archive/revive test.
Logs remain /tmp/archive-permissions-ci-*.log.

Application build: nix build .#packages.x86_64-linux.default; exit 0 in 620s,
including required Ruby verification dependencies. Output:
/nix/store/55dn2f8wf2jj8hp3jy07prjn689gms1m-dev-workspace-0.2.0.
Clean committed source resolves to that same path. Nix emits a dirty-tree warning
for the sparse workspace checkout although git status and diff are clean.
Log: /tmp/archive-permissions-workspace-build.log.

Host build: nix develop -c confctl build --yes cz.vpsfree/machines/aitherdev;
exit 0, generation 2026-10-26--21-47-19. First invocation omitted --yes and
stopped at confirmation without building; corrected once. Log:
/tmp/archive-permissions-aitherdev-build.log.

No live activation or shared merge has occurred. Predecessor system:
/nix/store/7za3la15ys7kq68sggbq6psvjqvqwrf7-nixos-system-aitherdev-26.05.20261021.da6dc0e.
Predecessor profile:
/nix/store/vq113xqpwhz09sc7myd9zciyqvn1lsvv-dev-workspace-0.2.0.

The first attempted registration used the existing unregistered implementation
worktree group's slug and refused before creating tracking. A fresh deployment
slug succeeded through the ordinary CLI; no refusal or metadata was bypassed.

Next: commit initial deployment tracking, acquire machine claim, activate and
verify exact candidates, then integrate and release. Keep runtime feature docs
and configuration procedure unchanged beyond the reviewed implementation/pins.
