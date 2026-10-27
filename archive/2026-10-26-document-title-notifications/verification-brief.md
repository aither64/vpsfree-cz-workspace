# Post-review verification batch

Refreshed exact-source batch after fixture correction. Original logs remain in
verification/. Prepared commands only. Do not launch before lead accepts independent final
review. One fresh retained-policy Luna/low utility owns the related batch.
Workspace root /home/aither/workspace/ai/vpsfree.cz.
All sources under worktrees/2026-10-26-document-title-notifications/:
- dev-workspace d2099c62656bc2a36c306918a92832ba1e1a0cc0
- workspace e3b44a8b59c656e0ecec0bd692ad7f72963f7e61
- vpsfree-cz-configuration 514e6a06ef72c3c2b4c50a592ff58b3d6fcd7cd2

Use explicit full-access execution, no source edits, diagnosis, retry, deployment,
acceptance or nested agents. Keep per-command logs under this session's
untracked verification-refreshed/ directory. No credentials/environment dumps.
Report each command exit, elapsed time, exact revision, artifact path and bounded
failure evidence; preserve still-running tool handles. Cancellation allowed for
an unexpected local Linux kernel build only: stop exact owned run and report
why it appears to be a kernel build. Do not cancel other sessions' processes.
Expected batch about 10–20 minutes depending on existing CI and caches; reassess
at 20 minutes with stage/remaining work, no automatic quiet-output timeout.

Independent commands can run concurrently when safe:

1. In workspace feature checkout:
   nix flake check --no-update-lock-file --print-build-logs
   Then (only if pass) nix build --no-update-lock-file --no-link
   --print-out-paths .#default
   Capture exact application output. Checks include composed catalog/source and
   deployment-contract fixtures; package runs its own Go/Node/Ruby checks.
2. In configuration feature checkout:
   nix develop --no-update-lock-file -c confctl build --yes cz.vpsfree/machines/aitherdev
   Retain exact confctl generation and system path. No deploy/copy/activation.
3. In runtime feature checkout:
   nix shell github:NixOS/nixpkgs/a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4#xvfb-run
   -c nix develop --no-update-lock-file -c env
   FIREFOX_BINARY=/nix/store/nhqwiw8s88b3zy3pka98gizjgw6i2h8d-firefox-155.0/bin/firefox
   GECKODRIVER_BINARY=/nix/store/b5g0k5g2bsvar0y38mn4zdfailhk0b77-geckodriver-0.36.0/bin/geckodriver
   PORTAL_FIREFOX_TABS_TEST=1 PORTAL_FIREFOX_READ_BUDGET_TEST=1
   DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/document-title-notifications-absent-providers.json
   xvfb-run -a -s '-screen 0 1920x1080x24'
   go -C portal test -mod=readonly ./internal/web
   -run '^TestFirefox(Tabs|ReadBudget)$' -count=1 -v
   This is existing fixture/runner with native hidden tabs and synthetic backend.
4. Observe existing CI only:
   gh run watch 40394771174 --repo aither64/dev-workspace --exit-status
   Confirm exact head d2099c62656bc2a36c306918a92832ba1e1a0cc0 and required fast,
   session creation/archive jobs. Do not dispatch or retry. Fetch failed job logs
   for bounded failure evidence, without diagnosis. Host job was skipped on feature
   push; do not treat skipped jobs as passed.

No machine or repository claim is needed for this batch. Native utility identity:
dw_261a10738ad06c003118fa86a9c9a7ce71a28ba2529d3b2b, from catalog digest
3ff7a2129ed39b4d6774466e53060bbff33d2cd2d893aa168c87cb3d64bd6b41.
