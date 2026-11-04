# vpsAdminOS integration preparation

Preparation complete at 2026-11-03 21:52 +0100. Git operations returned to the
lead. No repository claim, merge, default-branch update, push, tests, CI action
or cleanup was performed in this preparation. Target retained for the lead's
final fresh checks after required tests/review.

## Identity and instructions

- `dev-session current` and both environment values match
  `2026-11-03-opensuse-leap-image-build` in
  `/home/aither/workspace/ai/vpsfree.cz`.
- Read workspace Git/commits procedures, repository AGENTS and hook config,
  workspace `docs/coordination.md`, and the selected runtime coordination guide
  in full. The CLI guide's `--help` form is unsupported; the ordinary
  `workspace-host coordination guide` succeeded.
- Selected package:
  `/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0`.
- Coordination catalog:
  `sha256:b17a5618c6ce3988022bd02962d4dad95d735568fc4b2717ce462364e41eab6d`.
- Lead relayed user approval, “when done, you can merge it”, scoped to
  vpsadminos → staging after final checks/review. Lead owns the approved merge
  critical section; this record only certifies preparation.

## Exact repository and checkouts

- Canonical common Git directory:
  `/home/aither/workspace/ai/vpsfree.cz/repos/vpsadminos.git`.
- SSH origin: `git@github.com:vpsfreecz/vpsadminos.git`.
- Source worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-opensuse-leap-image-build/vpsadminos`.
- Feature branch: `2026-11-03-opensuse-leap-image-build`.
- Exact source/remote feature head:
  `742eb30cb1a8b6766c85e915d26b0400e38244b1`.
- Source tree: `19f423e70ff439867d4bb27e8ed07b9c95fdb703`.
- Prepared target:
  `/tmp/2026-11-03-opensuse-leap-image-build-vpsadminos-target`.
- Detached target and fetched/SSH-verified `refs/heads/staging`:
  `dd188397abe37d0bc33f4c5dfb3605206ce5e326`.

Created the new target with ordinary `git worktree add --detach --quiet` inside
the repository Nix environment. No target path existed beforehand. Target and
source have empty porcelain status; source remains attached to its feature
branch at the expected head. Target is detached, shares the canonical Git
directory and has the expected SSH origin. Staging is an ancestor of the final
feature head. Fresh fetch and `git ls-remote` found neither head/base movement.

## Environment and mandatory hooks

Target `nix develop` completed successfully, installing its own ignored `.gems`
cache (44 gems) and preparing Overcommit 0.74.0. Reviewed `.overcommit.yml`
enables Nixfmt/RuboCop and the custom Nixfmt hook. Existing installed common hooks
were already executable; no reinstall or bypass was needed. `overcommit --sign`
completed in the target's Nix environment; signature verification remains 1.

- `GEM_HOME`:
  `/tmp/2026-11-03-opensuse-leap-image-build-vpsadminos-target/.gems`.
- Overcommit: the target `.gems/bin/overcommit`.
- Ruby: `/nix/store/z30vypx0r6mgbfs0a86m6vd3s7pk07sb-ruby-3.4.11/bin/ruby`.
- Nixfmt: `/nix/store/7kcwslr98ahgivprci1qfzgmi6mrgjds-nixfmt-1.5.0/bin/nixfmt`.
- Verified executable `pre-commit`, `commit-msg`, `post-checkout`, `post-merge`
  and `pre-push` hooks all have SHA256
  `a81910ebf3fd7a535b81cc3497d14bbed38190d6e2a6473ee71f04634c516cc5`.
- Configuration trust signature:
  `e3f2ddb1e18d2a523f15e00a16db7d86774bbeb8ab9d8c576ae6c48add48389d`.
- Custom Nixfmt hook trust signature:
  `88afa3f1dd658c4d8ba603683f332e26814f9e0db33153c438ed6244ebabdc14`.

`AGENTS.md`, `.overcommit.yml`, `.git-hooks`, `Gemfile`, `Gemfile.lock`,
`flake.nix` and `flake.lock` have no base-to-feature differences. The prepared
environment/hook inputs therefore match both sides of the intended fast-forward.
Linked worktrees share hook trust/configuration; Git contents remain clean.

Logs: [worktree setup](merge-preparation-worktree.log), SHA256
`5d08988aa2fa2bb501dffcbf3a607b1f1a252330737198f500bc1a63d3196f4e`;
[environment/hooks](merge-preparation-hooks.log), SHA256
`4b828619ab311ddd0baf4287ce30018b407d309fa67094aa959b6e629227c355`.
Both setup commands exited 0; no operation remains running.

The lead should enter this target's `nix develop` **before** acquiring ownership,
then use that prepared environment for the final fresh target/feature/cleanliness
checks, ordinary fast-forward/hooks, non-force SSH push and remote proof. Inspect
post-merge hook output as well as Git status. Release the exact claim before
records/CI/cleanup; stop and return to unlocked preparation if the baseline or
hook trust needs intervention. No claim or lifecycle action is authorized by
the existence of this prepared checkout alone.
