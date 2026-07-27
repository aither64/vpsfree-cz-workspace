# 2026-07-27-terraform-provider-vpsadmin-issue-11

## Repositories

- `terraform-provider-vpsadmin`
  - branch: `2026-07-27-terraform-provider-vpsadmin-issue-11`
  - base: `origin/master` at `0220361`
  - worktree:
    `worktrees/2026-07-27-terraform-provider-vpsadmin-issue-11/terraform-provider-vpsadmin`
  - remote: `git@github.com:vpsfreecz/terraform-provider-vpsadmin.git`

## Status

- Release candidate is ready for review. Intended changes are committed;
  mandatory change review and all quick, build/package, and release-snapshot
  checks passed.
- The normal integration suite is blocked by a newly pinned upstream vpsAdmin
  API example-validation regression before any provider operation. A
  diagnostic run with the matching unmerged upstream correction passed the
  issue-critical OS-template lookup and reached `Vps.Create`, then failed on an
  unrelated vpsAdmin setup transaction lock.
- Issue #11 is open and reports that provider v1.2.0 sends an empty
  `hypervisor_type` during OS-template lookup, causing VPS creation to fail.
- No pushes, tags, GitHub releases, issue edits, or registry publications have
  been made.
- Proposed release version: `v1.3.0`.

## Commands run

- `bin/dev-session current`
- `gh issue view 11 --repo vpsfreecz/terraform-provider-vpsadmin ...`
- `git --git-dir=repos/terraform-provider-vpsadmin.git fetch --prune origin`
- `gh release list --repo vpsfreecz/terraform-provider-vpsadmin`
- Read Terraform and OpenTofu provider registry version APIs with `curl`.
- `bin/dev-session worktree add ... terraform-provider-vpsadmin ...`
- Read repository `AGENTS.md`, release workflow, dependency versions, tags, and
  the diff from `v1.2.0` to `origin/master`.
- Downloaded the published v1.2.0 Linux AMD64 artifact and inspected its Go
  build metadata.
- Ran controlled HTTP request captures with the exact v1.2.0 and current
  `vpsadmin-go-client` versions.
- Probed the public live API with limits 10000, 1000, and 100, and with an
  explicit empty `hypervisor_type`.
- Inspected pagination fix commit `b9b0acb`.
- `nix build --no-link .#terraform-provider-vpsadmin`
- `nix flake check`
- `nix develop -c make test-integration`
- Used `./test-runner.sh debug ... workflows` and the retained service VM
  journal to diagnose the integration startup failure.
- `nix shell nixpkgs#goreleaser -c goreleaser release --snapshot --clean
  --skip=sign`

## Results

- Verified active session:
  `VPSFREE_DEV_SESSION_SLUG=2026-07-27-terraform-provider-vpsadmin-issue-11`.
- GitHub, Terraform Registry, and OpenTofu Registry all report `v1.2.0` as the
  latest published provider version.
- `v1.2.0` pins `vpsadmin-go-client`
  `v0.0.0-20250513113348-b1fdcb3c20a6`.
- Current `origin/master` pins `vpsadmin-go-client`
  `v0.0.0-20260504133612-45a5170b7190`.
- Current `origin/master` contains multiple functional fixes, dependency
  updates, tests, and CI changes since `v1.2.0`; the next compatible minor
  version is `v1.3.0`.
- The published v1.2.0 binary embeds the expected old client version and was
  built from original release commit `d9203becf6f0`.
- Controlled captures show both old and current clients send only
  `os_template[limit]` after `SelectParameters("Limit")`; neither sends
  `hypervisor_type`.
- The issue's stated cause is incorrect. The actual v1.2.0 failure is its
  `os_template[limit]=10000` request. The live API rejects it with
  `limit: must be between 0 and 1000`.
- Live API requests with `limit=1000` and `limit=100` succeed. An explicitly
  empty `hypervisor_type` fails, but the provider does not send it.
- Commit `b9b0acb` already fixes the actual cause on `master` by using
  `apiPageLimit = 1000` for OS templates and the other affected lookups, with
  regression tests.
- Candidate changes bump the local/install version to `1.3.0` and strengthen
  the OS-template request test to assert `hypervisor_type` is absent.
- Initial `nix develop` checks found a release blocker on `origin/master`: the
  flake selects `go_1_26` but asserts exactly Go 1.26.3, while the current
  followed nixpkgs provides 1.26.5. The candidate removes this unnecessary
  patch-level assertion, keeps the Nix shell on Go 1.26, and corrects the README
  minimum to match `go.mod` (Go 1.25.8 or newer).
- The Nix provider package version is also bumped from 1.2.0 to 1.3.0.
- Candidate commits:
  - `d2987e0` `tests: verify OS template platform is omitted`
  - `243a090` `nix: accept Go patch updates`
  - `90c51c3` `Version 1.3.0`
- No repository hook framework is declared. `git diff --check` passed before
  commit.
- Quick verification passed after the Nix fix:
  - `nix develop -c go test ./vpsadmin -run
    '^TestGetOsTemplateIdByNameUsesAllowedPageLimit$' -count=1`
  - `nix develop -c make test`
  - `nix develop -c make test-get-token`
  - `nix develop -c make build`
- The first parallel `nix develop` attempts failed before running tests because
  the stale exact Go assertion rejected Go 1.26.5. Parallel evaluation also
  reported one ignored busy Nix eval-cache database; subsequent verification
  was run sequentially.
- Mandatory change review:
  - standalone fresh-context reviewer completed after commit `90c51c3`;
  - no blocking, important, or advisory findings;
  - independently confirmed the corrected pagination root cause, request-shape
    regression coverage, release version consistency, commit split,
    compatibility analysis, clean worktree, unchanged remote base, and absence
    of a remote `v1.3.0` tag;
  - residual full integration, Nix build/check, and GoReleaser snapshot checks
    were explicitly deferred until after review.
- `nix build --no-link .#terraform-provider-vpsadmin` passed and produced
  `terraform-provider-vpsadmin-1.3.0`.
- `nix flake check` passed for the host system. It emitted only the existing
  warnings for custom `tests`/`testsMeta` outputs, missing app metadata, and
  checks omitted on incompatible systems.
- The normal integration run failed after 1157.6 seconds while waiting for
  `http://api.vpsadmin.test/`; it never reached authentication, OpenTofu, or a
  provider operation.
- Interactive inspection found the upstream cause in
  `vpsadmin-api.service`: packaged HaveAPI 0.29.8 rejects
  `VpsAdmin::API::Resources::Location::Index` because its example response
  contains undeclared `created_at` and `updated_at` fields. Puma repeatedly
  exits and HAProxy has no healthy API backend.
- The provider's automated flake update commit `0220361` pinned vpsAdmin
  `52933ca65` on 2026-07-27. The matching vpsAdmin correction is commit
  `e0407c301`, but it is currently only on an unmerged branch and is not an
  ancestor of the pinned revision.
- Retained first-failure diagnostics:
  `/tmp/nix-shell.PNV6fe/os-test-runner/os-test-workflows-45b34f16`.
- GoReleaser 2.15.4 snapshot mode passed without signing or publishing. It
  built 13 archives covering Linux, Darwin, Windows, and FreeBSD on the
  configured architectures; every archive and the registry manifest matched
  the generated SHA-256 checksum list. Generated `dist/` files were moved to
  the desktop trash after inspection, leaving the worktree clean.
- Snapshot mode selected `v1.0.0` as its synthetic base because the published
  `v1.2.0` tag is not in current master history. This does not affect a real
  release from a future `v1.3.0` tag, but the exact tag-triggered version must
  be checked again before publication.
- A first diagnostic command using `nix run --override-input vpsadmin ...`
  was stopped after confirming it still evaluated the committed, broken
  `flake.lock`. The test runner invokes child Nix evaluations against the
  checkout, so the runner-level input override does not propagate. The
  corrected diagnostic procedure temporarily overrides the checkout lock and
  restores it after the run.
- With `flake.lock` temporarily overridden to vpsAdmin `e0407c301`, the API
  mounted successfully and OpenTofu began the provider lifecycle. The provider
  resolved `debian-latest-x86_64-vpsadminos-minimal`, produced a valid plan, and
  submitted VPS creation; this is the exact path that issue #11 could not pass
  in v1.2.0.
- The diagnostic override run then failed after 829.01 seconds because vpsAdmin
  rejected `Vps.Create` with `Resource is locked by transaction chain 6
  (Create)`. This occurred after lookup, alongside a concurrently created NAS
  dataset, and is unrelated to the page-limit fix. Later workflow examples
  were skipped.
- Diagnostic override logs:
  `/tmp/provider-issue11-integration-lock-override/os-test-workflows-45b34f16`.
- The temporary lock override was restored mechanically to vpsAdmin
  `52933ca65`; `git diff --exit-code -- flake.lock` passed and the provider
  worktree is clean.
- Final external-state recheck:
  - provider `origin/master` remains `0220361`;
  - no remote `v1.3.0` tag exists;
  - GitHub and Terraform Registry still report `v1.2.0` as latest;
  - issue #11 remains open and unchanged;
  - vpsAdmin `master` remains `52933ca65`, and no open pull request contains
    the example correction.

## Proposed release notes

`v1.3.0`:

- Restore VPS creation against current vpsAdmin APIs by keeping provider lookup
  page sizes within the server's accepted maximum.
- Fix dataset quota, export, VPS state migration, DNS resolver, disk-space
  lookup, and operation-timeout handling.
- Fix `get-token` output and modernize provider tests, integration coverage,
  Go/Nix development tooling, and CI.

Closes #11 based on the corrected root cause: v1.2.0 requested
`os_template[limit]=10000`; it did not send an empty `hypervisor_type`.

## Open questions

- Will the upstream vpsAdmin correction be merged before this provider
  candidate is published, allowing the normal integration suite to pass?

## Publication gate

- Stop for review before any push, tag, GitHub release, issue edit, or registry
  publication.
- Before publishing, merge the upstream vpsAdmin example correction, update the
  provider's vpsAdmin flake input to the corrected `master`, rerun the normal
  integration suite without overrides, and verify the exact tag-triggered
  GoReleaser version/artifacts for `v1.3.0`.

## Cleanup

- Worktree is active and must be retained until the candidate is reviewed or
  the initiative is abandoned.
