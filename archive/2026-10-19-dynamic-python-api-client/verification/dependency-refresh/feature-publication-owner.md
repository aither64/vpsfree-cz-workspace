# Dependency refresh feature publication

Published only the reviewed feature branch by normal non-force SSH push.
Master remains unchanged; no merge, tag, version, registry or release operation was performed.

- Base/master: `c1823f3d70365b0442d0e2171bdf83bd4c6dbe31`.
- Published/local/upstream head: `a8ea3132e7efe601aaa8965afe648459b3dab5c5`.
- Tree: `9a596258d912ca2075c36ded30d11b3984c656ae`.
- Claim `342cd062-0205-45c7-b636-20d958b8fa75` was authoritatively held at revision 2 before fetch and again before publication. Claim release remains with the lead.
- Exact session/environment and retained implementer1 workspace-write identity verified.
- Canonical SSH origin fetch and push URLs verified; fetched master and both prior remote heads were the expected base.
- Explicit comparison captured with the exact base/head before publication.
- Ordinary root Nix environment and installed Overcommit pre-push entrypoint used; verifySignatures remained 1, with no hook bypass or hooksPath override. Push exited 0. No pre-push test hooks are configured in `.overcommit.yml`.
- Remote ls-remote proves the feature head; upstream tracking points to origin/2026-10-19-dynamic-python-api-client. Worktree and index are clean; all four frozen component lock hashes are unchanged.
- All owner command handles have completed. No local check was repeated and no watcher was started. No superseded active same-branch CI runs were found; no cancellation was needed.
- Existing recovery refs and stash were preserved. Full four-commit review and no-migrations conclusion remain unchanged.

## Published series

- `67ecb6797c2794113b078044395d7a2ed54dfda2 flake: use Ruby 3.4 in native development shells`
- `7b7697e5c2dbb82d120cb5fa321d67b489d59a3e flake: nixpkgs fe13242281a -> 02c087f3fe6`
- `18331877660ed0f736a25b29914756da89df0df9 clients/python: refresh certifi and Ruff dependencies`
- `a8ea3132e7efe601aaa8965afe648459b3dab5c5 clients: bind test servers to their own bundle lockfile`

## Initial read-only CI observation

These are initial snapshots, not a wait for CI. The lead owns subsequent monitoring.

| Workflow | Run | State at detail read | Jobs |
| --- | --- | --- | --- |
| clients/python | [39499463957](https://github.com/vpsfreecz/haveapi/actions/runs/39499463957) | success | integration: success; checks (3.14): success; checks (3.15): success; checks (3.12): success; checks (3.11): success; checks (3.13): success |
| RuboCop | [39499463888](https://github.com/vpsfreecz/haveapi/actions/runs/39499463888) | success | rubocop: success |
| i18n health | [39499463892](https://github.com/vpsfreecz/haveapi/actions/runs/39499463892) | success | i18n health: success |
| clients/go RSpec | [39499463966](https://github.com/vpsfreecz/haveapi/actions/runs/39499463966) | in_progress | rspec / RSpec (Ruby 3.3): in_progress; rspec / RSpec (Ruby 3.4): in_progress; rspec / RSpec (Ruby 3.2): in_progress |
| clients/ruby RSpec | [39499463910](https://github.com/vpsfreecz/haveapi/actions/runs/39499463910) | in_progress | rspec / RSpec (Ruby 3.2): in_progress; rspec / RSpec (Ruby 3.4): success; rspec / RSpec (Ruby 3.3): in_progress |
| release | [39499464715](https://github.com/vpsfreecz/haveapi/actions/runs/39499464715) | in_progress | Validate, test and build: in_progress |

## Evidence

- [feature-publication-preflight.json](feature-publication-preflight.json), SHA256 `229178438aeb81d3709f025a7ff0679e57486f5283f19d8d6b3f1aaaf48669af`.
- [feature-publication-push.log](feature-publication-push.log), SHA256 `4fbc6d1fdb70002b5884cc1df424b85b033c84bdb23386467e2a856178bc7499`.
- [feature-publication-proof.json](feature-publication-proof.json), SHA256 `a6416294e5a8d64f424b2b4f4d52d33df1587a9218071904696c9ae722fbf6bf`.
- [feature-publication-ci-runs.json](feature-publication-ci-runs.json), SHA256 `72c733994f8116bdb277769b51fddef571ae06adc42f6df30b0b0f4ac3cb65b3`.
- [feature-publication-ci-jobs.json](feature-publication-ci-jobs.json), SHA256 `0a802773b5e35a774bd809defd34310a41f64dd5decf55add82ad6cafb00a6b3`.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-dynamic-python-api-client/
