# 2026-07-27-terraform-provider-vpsadmin-issue-11

## Repositories

- `vpsadmin`
  - branch: `2026-07-27-terraform-provider-vpsadmin-issue-11`
  - base: `origin/master` at `52933ca65`
  - worktree:
    `worktrees/2026-07-27-terraform-provider-vpsadmin-issue-11/vpsadmin`
  - remote: `git@github.com:vpsfreecz/vpsadmin.git`
- `terraform-provider-vpsadmin`
  - branch: `2026-07-27-terraform-provider-vpsadmin-issue-11`
  - base: `origin/master` at `0220361`
  - worktree:
    `worktrees/2026-07-27-terraform-provider-vpsadmin-issue-11/terraform-provider-vpsadmin`
  - remote: `git@github.com:vpsfreecz/terraform-provider-vpsadmin.git`

## Status

- The reviewed changes have been fast-forwarded and pushed to both default
  branches. vpsAdmin `master` is at `cba29b57c`; terraform-provider-vpsadmin
  `master` is at `1daa01a`.
- Provider Go Tests and Integration Tests on `master` are green.
- Lightweight tag `v1.3.0` points to provider commit `1daa01a`. The signed
  GitHub release is public, and Terraform Registry has ingested it. OpenTofu
  Registry has ingested and deployed its `1.3.0` download metadata; its
  Cloudflare-cached versions list is still serving the preceding release.
- vpsAdmin RuboCop, i18n health, and all 26 API-spec jobs are green. Its
  selected VM integration workflow remains intentionally non-blocking; the
  user explicitly requested that this several-hour run not delay release.
- Issue #11 is open and reports that provider v1.2.0 sends an empty
  `hypervisor_type` during OS-template lookup, causing VPS creation to fail.
- Issue #11 has not been edited or closed.
- Released version: `v1.3.0`.

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
- Pushed `2026-07-27-terraform-provider-vpsadmin-issue-11` over SSH.
- Inspected GitHub Actions runs `30280042318` and `30280042039`, including the
  failed integration log and uploaded diagnostic artifact.
- Created an isolated vpsAdmin worktree from `origin/master` at `52933ca65`.
- Compared vpsAdmin example-correction commits `9ad43e4ec` and `e0407c301` and
  their parent file contents with current `origin/master`.
- Cherry-picked only `9ad43e4ec` onto the isolated vpsAdmin branch.
- Ran the vpsAdmin API smoke spec and RuboCop in `nix develop .#api`.
- Computed the clean local vpsAdmin commit's NAR hash and committed the
  provider's mechanical `flake.lock` update.
- Ran `nix flake check` with the vpsAdmin input overridden to the identical
  clean local commit, avoiding a pre-review remote push.
- Ran the mandatory cross-project fresh-context review. Inspected the retained
  diagnostic integration logs to resolve its blocking concurrency finding.
- Added `-parallelism=1` to all state-changing OpenTofu workflow commands and
  checked the edited Nix expression with `nix-instantiate --parse`, `nixfmt
  --check`, and `git diff --check`.
- Pushed the reviewed vpsAdmin development branch and verified that the
  provider's committed GitHub input resolves without an override.
- `nix develop -c make test-integration`
- Pushed the reviewed provider follow-up commits and monitored all triggered
  GitHub Actions through provider integration success.
- Created fresh detached merge worktrees under
  `worktrees/2026-07-27-terraform-provider-vpsadmin-issue-11/merge/`.
- Fast-forwarded vpsAdmin `52933ca65..cba29b57c`, repeated the API smoke spec
  and targeted RuboCop checks, and pushed the detached head to `master`.
- Confirmed `nix flake update vpsadmin` made no provider diff after the
  vpsAdmin merge because the existing lock already names merged commit
  `cba29b57c`.
- Fast-forwarded terraform-provider-vpsadmin `0220361..1daa01a`, then repeated
  `make test`, `make test-get-token`, `make build`, `nix flake check`, and the
  Nix provider package build in the fresh merge worktree.
- Re-fetched provider `master`, verified it had not advanced, and pushed the
  detached release-candidate head to `master`.
- Waited for provider default-branch Go Tests and Integration Tests to pass.
- Re-fetched tags and `master`, verified `v1.3.0` was absent and the release
  target remained `1daa01a`, created a lightweight tag, and pushed it over
  SSH.
- Monitored the tag-triggered Release workflow through success.
- Downloaded all GitHub release assets and verified every archive and registry
  manifest against the published SHA-256 checksum file.
- Imported the signing key returned by Terraform Registry into an isolated
  temporary GnuPG home and verified the detached checksum signature.
- Queried Terraform Registry and OpenTofu Registry version/download APIs.
- Monitored OpenTofu's scheduled metadata updater and generated API sync
  through success, then inspected its source metadata and public cache headers.
- Recorded the reusable OpenTofu cache diagnostic in
  `notes/terraform-provider-vpsadmin/2026-07-27-opentofu-registry-cache.md`.
- Removed the two clean detached merge worktrees and their empty `merge/`
  parent directory. The initiative feature worktrees were retained through
  release review, then removed on the user's cleanup request. Local and remote
  feature branches were retained.

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
  - `c9c22a8` `flake: vpsadmin 52933ca65 -> cba29b57c`
  - `1daa01a` `tests: serialize provider workflow mutations`
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
- Development branch publication:
  - pushed to
    `origin/2026-07-27-terraform-provider-vpsadmin-issue-11`;
  - local and remote heads both resolve to
    `1daa01ab113295e2e0e47d75843150aba0801496`;
  - the provider worktree remains clean.
- GitHub Actions Go Tests run
  `https://github.com/vpsfreecz/terraform-provider-vpsadmin/actions/runs/30280042318`
  passed:
  - Go 1.25.x passed in 41 seconds;
  - Go 1.26.x passed in 47 seconds;
  - provider and token-helper tests passed in both jobs.
- GitHub Actions Integration Tests run
  `https://github.com/vpsfreecz/terraform-provider-vpsadmin/actions/runs/30280042039`
  failed after 19 minutes 11 seconds. The test phase took 1127.74 seconds.
- The failed attempt's logs and artifact
  `terraform-provider-vpsadmin-test-logs-30280042039` were inspected before
  deciding against a rerun:
  - the workflow waited 909.04 seconds for `http://api.vpsadmin.test/`;
  - the final error was `OsVm::TimeoutError` from
    `wait_for_vpsadmin_api`;
  - HAProxy returned HTTP 503 throughout the wait and the API description was
    never served;
  - no authentication, OpenTofu, or provider operation began.
- The CI artifact does not include the service VM's systemd journal, so it
  cannot directly show the HaveAPI exception. It reproduces the identical
  API-unhealthy symptom against the same locked vpsAdmin revision
  `52933ca65`; the matching local run's retained journal directly identified
  the undeclared example fields as the cause.
- The failed workflow was not rerun because neither its head nor its locked
  integration inputs changed, and the inspected evidence shows the same
  deterministic upstream startup blocker already diagnosed locally.
- The dependency trigger is confirmed:
  - vpsAdmin declares `gem 'haveapi', '~> 0.29.6'`, which permits patch
    releases through 0.29.x;
  - automated dependency commit `575ff7937` updated packaged HaveAPI and its
    client from 0.29.6 to 0.29.8;
  - HaveAPI 0.29.8's stricter documentation validation rejects example
    response fields outside declared output schemas.
- vpsAdmin branch `2026-06-15-vpsadmin-events` contains commit `9ad43e4ec`
  `api: correct location and address examples`. Its parent versions of both
  touched resource files exactly match current `origin/master`.
- Commit `e0407c301` on the unrelated `2026-07-24-ct-start-hang` branch carries
  an identical two-file patch. The isolated initiative branch will backport
  `9ad43e4ec` only; no event or container-start work is included.
- vpsAdmin backport commit:
  - `cba29b57c` `api: correct location and address examples`;
  - exactly two resource files changed, with the same patch as `9ad43e4ec`;
  - the vpsAdmin worktree is clean.
- vpsAdmin quick verification:
  - `nix develop .#api -c bundle exec rubocop
    lib/vpsadmin/api/resources/location.rb
    lib/vpsadmin/api/resources/ip_address.rb` passed with no offenses;
  - `nix develop .#api -c bundle exec rspec
    spec/smoke/api_boot_spec.rb` passed 5 examples with no failures;
  - the test shell confirmed HaveAPI 0.29.8.
- Default-branch integration:
  - vpsAdmin `master` was fast-forwarded and pushed to
    `cba29b57ceacb2fd57864e03fb97a710f8168fe2`;
  - vpsAdmin RuboCop and i18n health passed on the default branch;
  - vpsAdmin API Specs run
    `https://github.com/vpsfreecz/vpsadmin/actions/runs/30288855306`
    passed all 26 jobs on the default branch;
  - the multi-hour vpsAdmin CI run
    `https://github.com/vpsfreecz/vpsadmin/actions/runs/30288856228`
    remains in progress and was not made a release gate, as requested;
  - terraform-provider-vpsadmin `master` was fast-forwarded and pushed to
    `1daa01ab113295e2e0e47d75843150aba0801496`;
  - provider Go Tests run
    `https://github.com/vpsfreecz/terraform-provider-vpsadmin/actions/runs/30289132439`
    passed for Go 1.25.x and Go 1.26.x;
  - provider Integration Tests run
    `https://github.com/vpsfreecz/terraform-provider-vpsadmin/actions/runs/30289131511`
    passed in 22 minutes 36 seconds; its test evaluation, summary, and cleanup
    steps all succeeded.
- Release publication:
  - lightweight tag `v1.3.0` and provider `origin/master` both resolve to
    `1daa01ab113295e2e0e47d75843150aba0801496`;
  - Release workflow
    `https://github.com/vpsfreecz/terraform-provider-vpsadmin/actions/runs/30290875926`
    passed, including GPG import and GoReleaser;
  - public release:
    `https://github.com/vpsfreecz/terraform-provider-vpsadmin/releases/tag/v1.3.0`;
  - the release is neither a draft nor a prerelease and contains 13 provider
    archives plus the registry manifest, checksum list, and detached signature;
  - all 14 entries in `terraform-provider-vpsadmin_1.3.0_SHA256SUMS` verified;
  - the manifest declares registry protocol `5.0`;
  - GPG verification returned a valid signature from key fingerprint
    `7AF4 99EA 2F8B D595 B456 F345 1C85 E54D B0A1 2B16`;
  - Terraform Registry already lists `1.3.0` and its Linux AMD64 download
    metadata resolves successfully;
  - OpenTofu Registry metadata source lists `1.3.0`, discovered at
    `2026-07-27T18:07:34Z` with 13 targets;
  - OpenTofu metadata updater
    `https://github.com/opentofu/registry/actions/runs/30291745776`
    passed, including the `v` namespace job;
  - OpenTofu generated API sync
    `https://github.com/opentofu/registry/actions/runs/30292861801`
    passed and explicitly generated `vpsfreecz/vpsadmin`;
  - OpenTofu's direct `1.3.0/download/linux/amd64` endpoint returns HTTP 200
    with the expected filename and SHA-256
    `1012808661c979e496d7f93a24a09c5b63ab826e9ea03ade9534e9c30ae16d04`;
  - the OpenTofu versions endpoint at the observed Prague Cloudflare edge
    remains a cache hit containing `1.2.0` as latest. Its response advertises
    `cache-control: max-age=14400`; waiting for this third-party cache expiry
    would take hours and was stopped in line with the user's request not to
    wait on multi-hour validation;
  - OpenTofu's official `Bump Provider and Module Versions` workflow is
    nominally scheduled every 15 minutes, although recent GitHub-scheduled runs
    have occurred approximately hourly. No manual third-party workflow dispatch
    was attempted.
- Cleanup:
  - removed
    `worktrees/2026-07-27-terraform-provider-vpsadmin-issue-11/merge/vpsadmin`;
  - removed
    `worktrees/2026-07-27-terraform-provider-vpsadmin-issue-11/merge/terraform-provider-vpsadmin`;
  - removed the clean initiative feature worktrees with
    `bin/dev-session worktree remove`;
  - removal discarded only ignored transient contents:
    `api/.gems/`, `api/Gemfile.lock`, and the locally built provider binary;
  - `bin/dev-session list` reports zero worktrees for the initiative;
  - retained all local and remote feature branches as required.
- Provider input update commit:
  - `c9c22a8` `flake: vpsadmin 52933ca65 -> cba29b57c`;
  - full commit ID:
    `c9c22a887bd792a5c2a9e03ac56792266e0009f0`;
  - only `flake.lock` changed;
  - the locked NAR hash was computed from the clean vpsAdmin Git commit;
  - `nix flake check --override-input vpsadmin git+file://...` evaluated the
    identical commit and passed all host-system checks.
- Mandatory cross-project change review:
  - one fresh standalone reviewer inspected both committed branches;
  - no API, schema, state, protocol, WebUI, deployment, security, commit-split,
    backport, or dependency-pin finding was reported;
  - one blocking test-harness race was found: the workflow's independent VPS
    and exported-dataset graph roots ran concurrently and the retained
    diagnostic log proved that their vpsAdmin transaction chains collided;
  - the review packet contained an incorrect guessed full provider commit ID;
    the correct `c9c22a8` ID is recorded above.
- The blocking review finding is fixed in separate provider commit `1daa01a`
  `tests: serialize provider workflow mutations`. Every workflow `apply` and
  `destroy` now uses `-parallelism=1`, matching the provider's operational
  guidance and preventing unrelated vpsAdmin resource locks from preempting
  provider behavior.
- Quick verification of the review fix passed:
  - every state-changing workflow command was enumerated and found serialized;
  - `nix-instantiate --parse tests/suite/workflows.nix`;
  - `nixfmt --check tests/suite/workflows.nix`;
  - `git diff --check`;
  - the locally overridden test runner evaluated the committed suite and
    listed `workflows`.
- The same standalone reviewer verified commit
  `1daa01ab113295e2e0e47d75843150aba0801496` resolves the blocking finding:
  all nine apply/destroy commands are serialized, the commit is focused, and
  no new blocking, important, or advisory finding was introduced.
- vpsAdmin branch publication:
  - pushed
    `origin/2026-07-27-terraform-provider-vpsadmin-issue-11`;
  - local and remote heads both resolve to
    `cba29b57ceacb2fd57864e03fb97a710f8168fe2`;
  - the provider's normal GitHub lock resolves that revision with NAR hash
    `sha256-v1hSoTf6gW1Jlhyz+xcHOGSqSN2a2O4n0+JnrJOxnUQ=`.
- The normal provider integration suite passed without any input override:
  - one `workflows` script passed in 1287.18 seconds;
  - all 8 ordered examples passed;
  - API readiness succeeded, proving packaged HaveAPI 0.29.8 accepts the
    corrected examples and vpsAdmin mounts normally;
  - the issue-critical initial apply resolved the OS template, created the VPS,
    created the NAS dataset/export, read data sources, and allocated IP
    addresses in 110.78 seconds;
  - serialized updates converged without drift;
  - mount and export recreation, imports, SSH-key deployment, and final
    destroy/IP release all passed;
  - the prior API-startup and transaction-lock failures did not recur.
- Provider GitHub Actions Integration Tests run
  `https://github.com/vpsfreecz/terraform-provider-vpsadmin/actions/runs/30285167821`
  passed on head `1daa01a` in 17 minutes 59 seconds.
- No new Go Tests workflow was selected by the lockfile/test-harness-only
  follow-up push. The earlier Go Tests run
  `https://github.com/vpsfreecz/terraform-provider-vpsadmin/actions/runs/30280042318`
  remains green for both Go 1.25 and 1.26; provider Go source did not change
  after that run.
- vpsAdmin GitHub Actions on head `cba29b57c`:
  - RuboCop passed:
    `https://github.com/vpsfreecz/vpsadmin/actions/runs/30283484539`;
  - i18n health passed:
    `https://github.com/vpsfreecz/vpsadmin/actions/runs/30283489832`;
  - API Specs passed all 26 jobs:
    `https://github.com/vpsfreecz/vpsadmin/actions/runs/30283484104`;
  - selected integration CI remained in progress at handoff:
    `https://github.com/vpsfreecz/vpsadmin/actions/runs/30283484831`.
- Monitoring of the vpsAdmin integration workflow was stopped at the user's
  explicit request because that workflow takes several hours. It was still in
  its `Run tests` step with no reported failure when monitoring stopped.
- The vpsAdmin fix branch has not yet been pushed. This preserves the required
  ordering in which the standalone change review happens before a push can
  start GitHub integration workflows. After review, push vpsAdmin first and
  verify that the committed GitHub lock resolves to the same revision and NAR
  hash before running provider integration.

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

- What is the eventual result of the still-running vpsAdmin selected
  integration workflow?

## Publication gate

- The user authorized and the development branch received one push for CI.
  Stop for review before any tag, GitHub release, issue edit, or registry
  publication.
- Before publishing, merge the upstream vpsAdmin example correction, update the
  provider's vpsAdmin flake input to the corrected `master`, rerun the normal
  integration suite without overrides, and verify the exact tag-triggered
  GoReleaser version/artifacts for `v1.3.0`. The development branch may
  temporarily pin the reviewed vpsAdmin feature commit to prove the combined
  fix before either branch is merged.

## Cleanup

- Complete. Both project feature worktrees and both detached merge worktrees
  have been removed.
- The durable plan, state, and troubleshooting notes remain in the workspace.
- Local and remote feature branches remain at the merged commits:
  - vpsAdmin: `cba29b57ceacb2fd57864e03fb97a710f8168fe2`;
  - terraform-provider-vpsadmin:
    `1daa01ab113295e2e0e47d75843150aba0801496`.
