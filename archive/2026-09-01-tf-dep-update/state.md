# 2026-09-01-tf-dep-update

## Repositories

- Repository: `terraform-provider-vpsadmin`
- Branch: `2026-09-01-tf-dep-update`
- Worktree:
  `worktrees/2026-09-01-tf-dep-update/terraform-provider-vpsadmin`
- Base commit: `ba1dd51ffeff80edb167f10b2a5b7a82112f8b9f`

## Status

- Current phase: complete.
- Intended commit split:
  1. Go modules, supported toolchain, helper terminal package, Nix hashes, and
     build documentation.
  2. GitHub workflow dependency and supported-version updates.
  3. Provider version 1.5.0.

## Commands run

- `bin/dev-session current`
- Inspected the repository's local `AGENTS.md`, module manifests, release
  workflow, dependency graph, release history, and prior v1.4.0 release state.
- Queried current upstream Go module and GitHub Action versions.
- Scanned current `master` with `govulncheck` using Go 1.25.8 and Go 1.26.6.
- `bin/dev-session worktree add 2026-09-01-tf-dep-update
  terraform-provider-vpsadmin --as-is --branch
  2026-09-01-tf-dep-update --base origin/master`
- Updated both module graphs with Go 1.26.6 in the repository Nix shell and
  ran `go mod tidy` in each module.
- `nix develop -c make fmt`
- `nix develop -c make test`
- `nix develop -c make test-get-token`
- `nix develop -c make build`
- Ran `go vet ./...` in both modules.
- `nix develop -c make docs` followed by an idempotence diff.
- Built both Nix packages and verified provider version 1.5.0 and helper
  version 0.1.0.
- Ran `actionlint` and `goreleaser check` with current nixpkgs tools.
- Ran provider and helper `govulncheck` scans with Go 1.26.6.
- Ran both module test suites with Go 1.26.7 and Go 1.27.0.
- Built complete GoReleaser snapshots with Go 1.26.7 and Go 1.27.0.
- Compared the 13 snapshot targets with the published v1.4.0 assets.
- Ran the mandatory fresh-context change review after the intended commits
  and quick checks.
- `nix develop -c make test-integration`
- Pushed `2026-09-01-tf-dep-update` to the SSH `origin`.

## Results

- The verified session slug and environment variable both resolve to
  `2026-09-01-tf-dep-update`.
- The provider remote uses SSH and fetched `origin/master` at `ba1dd51`.
- The repository declares no hook framework.
- The v1.4.0 Go 1.25.8 build baseline has 15 reachable known vulnerabilities,
  including standard-library TLS, X.509, HTTP and URL paths plus gRPC,
  `x/net`, and `x/text`.
- With Go 1.26.6, the current source still has three reachable dependency
  vulnerabilities: gRPC v1.81.1, `x/text` v0.37.0, and `x/net` v0.54.0.
- `get-token` has no reachable advisory call but requires `x/crypto` v0.51.0
  only for the deprecated `ssh/terminal` compatibility package. Its replacement
  `x/term.ReadPassword` has the same interface and documented behavior.
- The current Nix development shell uses Go 1.26.6. Go 1.27 is released, so
  the supported CI window becomes Go 1.26 and 1.27.
- A Go 1.26.7 GoReleaser snapshot built the same 13 platform targets published
  by v1.4.0. The earlier plan assumption that `windows/arm` required Go 1.26
  was incorrect: neither v1.4.0 nor the current GoReleaser matrix publishes
  that unsupported target. The release workflow therefore uses current Go
  1.27 while Go 1.26.6 remains the minimum supported source toolchain.
- `goreleaser check` initially rejected the pre-existing deprecated
  `archives.format` property. The workflow commit migrates it to `formats`,
  and current GoReleaser 2.15.4 now validates the configuration.
- Dependency commit: `d569530` (`deps: update Go modules`).
- Workflow commit: `1fdf3b0` (`github: update workflow dependencies`).
- Release commit: `29b47dd` (`Version 1.5.0`).
- Both Go module graphs are tidy. Provider tests, helper tests, provider build,
  both vet runs, documentation idempotence, Nix package builds, evaluated
  versions, actionlint, GoReleaser validation, Go 1.26.7 tests, Go 1.27.0
  tests, and diff checks pass on the committed tree.
- Provider and helper `govulncheck` scans report no vulnerabilities. The helper
  graph contains `x/term` and no longer contains `x/crypto`.
- The Go 1.27.0 snapshot built the same 13 platform targets as v1.4.0. Its
  318 MB `dist/` directory contained only reproducible build output and was
  removed after inspection.
- The mandatory review found no blocking or important issues. Its only
  advisory was that the GoReleaser action was commit-pinned while its
  downloaded GoReleaser executable still floated within major version 2.
  The workflow now pins GoReleaser v2.15.4; `actionlint` and
  `goreleaser check` pass after the change. The advisory fix was autosquashed
  into the workflow commit before publication.
- Residual review risks are covered by the integration suite, default-branch
  CI, signed release verification, and clean Terraform/OpenTofu installs.
- The complete integration suite passed all eight workflow examples in
  1916.36 seconds. It covered environment preparation, resource and data
  source creation, IP allocation, convergent updates, mount and dataset-export
  recreation, imports without drift, SSH-key deployment, and final resource
  and IP-address cleanup.
- The feature worktree is clean at `29b47dd`.
- Feature-branch GitHub Actions runs:
  - Go Tests: `33493529754`, successful for Go 1.26.x and 1.27.x.
  - Integration Tests: `33493529772`, successful in 29m26s after waiting
    approximately one hour for the shared self-hosted runner.
- Fast-forwarded `master` from `ba1dd51` to `29b47dd` in the fresh
  `worktrees/2026-09-01-tf-dep-update/master/terraform-provider-vpsadmin`
  worktree. Provider tests, helper tests, and provider build passed there
  before pushing `master` over SSH.
- Default-branch GitHub Actions runs:
  - Go Tests: `33501222900`, successful for Go 1.26.x and 1.27.x.
  - Integration Tests: `33501222876`, successful in 24m03s after waiting
    51 minutes for the self-hosted runner.
- Published lightweight tag `v1.5.0` at `29b47dd`, matching the repository's
  existing tag style.
- Tag GitHub Actions runs:
  - Release: `33507760689`, successful in 6m41s.
  - Go Tests: `33507760588`, successful.
  - Integration Tests: `33507760627`, still queued for shared self-hosted
    capacity at cleanup time. It targets the same `29b47dd` already validated
    by successful feature and default-branch integration runs, so it is an
    additional duplicate check rather than a release blocker. It has not
    failed and was left queued without cancellation or rerun.
- GitHub published a non-draft, non-prerelease v1.5.0 release containing the
  same 13 platform archives as v1.4.0, plus the registry manifest, checksum
  list, and detached signature.
- Imported the public key served by Terraform Registry into an isolated
  temporary keyring only after verifying fingerprint
  `7AF499EA2F8BD595B456F3451C85E54DB0A12B16`. The checksum signature is valid,
  all 13 archives and the manifest match the signed checksum list, and the
  manifest declares protocol 5.0.
- Terraform Registry and OpenTofu Registry both list 1.5.0. Clean pinned
  initializations succeeded from both registries; Terraform reported
  `self-signed` and OpenTofu reported `signed`, both with key ID
  `1C85E54DB0A12B16`.
- Removed all temporary release-verification, temporary GPG, Terraform-init,
  and OpenTofu-init data. The first ambient GPG attempt created a new empty
  `/home/aither/.gnupg` and keybox daemon; both were removed after confirming
  they were created by this verification attempt.
- An archive verification search accidentally placed Markdown backticks in a
  double-quoted shell pattern, causing harmless command substitution and a
  `command not found` diagnostic. The archive was unaffected. The quoting
  lesson is recorded in
  `notes/cross-project/2026-09-01-rg-backtick-shell-substitution.md`.

## Open questions

- None.

## Cleanup

- Removed the feature and temporary `master` worktrees after confirming both
  were clean.
- Kept local and remote branch `2026-09-01-tf-dep-update`, local `master`, and
  lightweight tag `v1.5.0`, all at `29b47dd`, as required by workspace policy.
- Archived this initiative's plan and state under
  `archive/2026-09-01-tf-dep-update/`.
