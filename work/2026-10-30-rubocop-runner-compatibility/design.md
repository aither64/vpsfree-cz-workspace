# RuboCop runner compatibility: findings and proposed fix

Investigated on 2026-10-30 by architect0. Investigation and recommendation only;
no project edits, fetches, branches, commits, workflow reruns or deployments.
Session identity and workspace binding verified before investigation. Repository
guidance was read from the canonical bare repository; remote workflow content
and Actions logs below establish the tested revisions.

## Confirmed cause

vpsadminos fails while installing Ruby, before Bundler or RuboCop runs.
`ubuntu-latest` selected Ubuntu 26.04. The workflow inherits the exact version
`3.4.0` from `.ruby-version`, but ruby-builder has no Ubuntu 26.04 binary for
that old patch release. The missing download returns HTTP 404.

| Evidence | Exact revision and observed result |
| --- | --- |
| [Failed run 41072754123, attempt 1](https://github.com/vpsfreecz/vpsadminos/actions/runs/41072754123) | Push to `staging`, source `05201326975fc19d20a545c52f651cce0420dbc9`, 2026-10-30. Ubuntu 26.04.1, image `ubuntu-26.04` version `20261025.179.1`. |
| [Failed job 124120814797](https://github.com/vpsfreecz/vpsadminos/actions/runs/41072754123/job/124120814797) | `Set up Ruby + Bundler cache` fails; `Run RuboCop` is skipped. |
| [Successful run 40296454481, attempt 1](https://github.com/vpsfreecz/vpsadminos/actions/runs/40296454481) | Push to `staging`, source `d9be8c4bada590c0405df85444600d40e6f3caa6`, 2026-10-26. Ubuntu 24.04.5, image `ubuntu-24.04` version `20261012.334.1`. Ruby 3.4.0 installs; RuboCop reports `1494 files inspected, no offenses detected`. |

Both runs used `ruby/setup-ruby@v1` resolved to
`7f797815d8adceb1c412e7abefdd1ab4abc47a5f`, and identical RuboCop workflow blob
`44346d2c88ed0fd1c00963e4275e3d98a5da1c9b`. Both source revisions have
`.ruby-version` equal to `3.4.0`. The workflow uses `ubuntu-latest`,
`actions/checkout@v6`, `ruby/setup-ruby@v1` with `bundler-cache: true`, then
`bundle exec rubocop --parallel --force-exclusion`.

Failed download:
`https://github.com/ruby/ruby-builder/releases/download/ruby-3.4.0/ruby-3.4.0-ubuntu-26.04-x64.tar.gz`

The error explicitly says:

```text
Error: Unavailable version 3.4.0 for ruby on ubuntu-26.04
Only the latest patch release of each series is built for newer runner images.
ruby-3.4.12 is available on ubuntu-26.04: use ruby-version: '3.4.12', or '3.4' to always use the latest 3.4.x release.
Cause: Unexpected HTTP response: 404
```

This proves a missing prebuilt Ruby/runner combination, not a lint offense,
dependency-resolution failure, corrupted Bundler cache or general lack of
Ubuntu 26.04 support in the action.

## Upstream corroboration

- [GitHub runner rollout announcement](https://github.com/actions/runner-images/issues/14748): `ubuntu-latest` migration to Ubuntu 26.04 runs from October 19 to November 19, 2026. Old and new images can therefore appear during this transition.
- [setup-ruby README at the executed revision](https://github.com/ruby/setup-ruby/blob/7f797815d8adceb1c412e7abefdd1ab4abc47a5f/README.md#supported-platforms): Ubuntu 26.04 is supported, but newer runner images have builds only for the latest patch of each series. It recommends a short version such as `'3.4'` or an explicit older runner image. Ubuntu 26.04 supports CRuby 3.2 and newer.
- [Ruby 3.4.0 release assets](https://github.com/ruby/ruby-builder/releases/tag/ruby-3.4.0): Ubuntu 22.04 and 24.04 assets exist for x64 and arm64; Ubuntu 26.04 assets are absent.
- [Ruby 3.4.12 release assets](https://github.com/ruby/ruby-builder/releases/tag/ruby-3.4.12): Ubuntu 26.04 assets exist for x64 and arm64, as well as 22.04 and 24.04.
- [Installer source at the executed revision](https://github.com/ruby/setup-ruby/blob/7f797815d8adceb1c412e7abefdd1ab4abc47a5f/ruby-builder.js): constructs a runner-specific download URL and emits the observed error on 404. Its available-release hint checks the newer patch's asset with HTTP HEAD before recommending it.
- [Version selection source](https://github.com/ruby/setup-ruby/blob/7f797815d8adceb1c412e7abefdd1ab4abc47a5f/index.js): an explicit `ruby-version` input overrides `.ruby-version`; a short series selects its latest stable matching release.
- The official latest action release is [v1.335.0](https://github.com/ruby/setup-ruby/releases/tag/v1.335.0), published October 24. Its tag and the moving `v1` branch both resolve to the executed SHA above. Upgrading the action alone cannot fix this exact Ruby pin.

Older pinned action revisions can separately misclassify a new hosted image as
self-hosted, or lack current Ruby releases. That is not the observed failure:
[this revision's platform table](https://github.com/ruby/setup-ruby/blob/7f797815d8adceb1c412e7abefdd1ab4abc47a5f/common.js#L183-L228)
includes Ubuntu 26.04 x64 and arm64. HaveAPI's RuboCop `v1.335.0` is the same
revision and passed on that image. Its other workflows retain some older
`v1.333.0`/`v1.330.0` pins whose image compatibility was not established by this
audit; do not infer either success or failure for them. A fixed action revision
requires maintenance as future runner images/releases arrive.

## Smallest durable recommendation

For vpsadminos, add `ruby-version: '3.4'` to the existing setup-ruby step in
`.github/workflows/rubocop.yml`. Keep the Ruby minor series and existing linter
command. This confines the patch-selection policy to CI and leaves the
repository's developer tooling version file and its other consumers unchanged.
It currently resolves to Ruby 3.4.12. The action and binary availability are
verified; this proposed workflow change has **not** been executed or tested.

Changing `.ruby-version` from `3.4.0` to `3.4` is also sufficient for this
workflow, but applies a floating patch policy to every consumer of that file.
Choose that only if project-wide patch tracking is intended and local version
manager support is checked. It is broader than needed for the reported CI
failure. An exact pin to `3.4.12` works with the published Ubuntu 26.04 asset,
but needs ongoing updates and can repeat this failure on a future image.

The short-term workaround is `runs-on: ubuntu-24.04`, preserving Ruby 3.4.0.
Its binary exists, and the earlier run proves this combination worked with the
same workflow and action. No new run of the current source has been performed;
pinning the older image defers the patch-maintenance problem.

For the separate repository audit, apply the same `'3.4'` CI policy to
security-advisories' explicit `3.4.0` inputs in both RuboCop and RSpec workflows.
The completed audit confirms their latest October 20 runs used Ubuntu 24.04.5;
they are susceptible configurations, not observed Ubuntu 26.04 failures. See
[repository-audit.md](repository-audit.md) for source/run identities and all 23
other managed repositories. vpsadmin and confctl already select series `3.4`;
HaveAPI RuboCop selects `3.2` with the current action release. Specifically,
[vpsadmin run 41081549557](https://github.com/vpsfreecz/vpsadmin/actions/runs/41081549557/job/124151697420)
passed on Ubuntu 26.04.1 with Ruby 3.4.12, and
[HaveAPI run 41056402040](https://github.com/vpsfreecz/haveapi/actions/runs/41056402040/job/124064915203)
passed there with Ruby 3.2.11. These support the series-selector recommendation
without validating a vpsadminos change. confctl passed, but its image could not
be established because the log API returned 503 twice. No Ruby minor upgrades
are justified for those repositories by this diagnosis. Nix-provided Ruby jobs
do not take the failing ruby-builder download path.

## Proposed implementation and verification brief

No implementation is authorized. If requested, the independent boundaries are:

| Package | Files and acceptance |
| --- | --- |
| vpsadminos CI | `.github/workflows/rubocop.yml`: explicit quoted `ruby-version: '3.4'`; preserve Bundler caching, linter arguments, permissions and Ruby minor series. |
| security-advisories CI | `.github/workflows/rubocop.yml` and `.github/workflows/rspec.yml`: replace exact `3.4.0` inputs with quoted `'3.4'`; preserve test commands and job behavior. Current pins confirmed by the completed audit; independent from vpsadminos. |

One implementer can handle these small edits. Repository commits/review remain
separate; there is no shared interface or rollout ordering dependency.

Quick checks: inspect the final workflow diff and YAML, verify action refs and
current 3.4 asset support, and use each repository's declared hooks if changes
are committed. vpsadminos currently filters push/PR triggers to Ruby, gemspec,
Gemfile and RuboCop configuration paths: a workflow-only or `.ruby-version`-only
edit does not trigger it. Include the workflow's own path in both trigger lists
when implementing this workflow fix so its push exercises the actual job.

Longer acceptance: run the changed RuboCop workflow (and the two affected
security-advisories jobs if changed) on Ubuntu 26.04. During the staged
`ubuntu-latest` rollout, verify the actual image in the job log; a green 24.04
run alone does not validate 26.04. Require successful Ruby installation,
Bundler setup and the real lint/test command at the final workflow revision.
Record resolved Ruby/action versions and run URL. No VM, kernel, deployment or
production tests are needed for this CI-only change. New workflow runs remain
outside the current investigation authorization.

Compatibility: this selects a newer patch of the same Ruby minor in hosted CI;
gem resolution and linter/test execution must still pass there. Keep RuboCop's
existing `TargetRubyVersion: 3.2`, which is a source-analysis setting rather
than the Ruby binary selection. No persistent formats, databases, migrations,
APIs, clients, protocols, Nix module contracts or running node versions change.
No fleet coordination or deployment is required. Recovery is to pin the CI
runner to Ubuntu 24.04 if the newer Ruby patch exposes a separate failure;
reverting only the Ruby input on Ubuntu 26.04 restores the known 404. No state
conversion or data rollback is involved.

## Evidence commands and limits

Used read-only `gh run list/view`, `gh api` workflow contents at exact source
SHAs, job logs, upstream action source/tags/releases and release asset metadata.
Successful job logs were read directly from
`repos/vpsfreecz/vpsadminos/actions/jobs/121483574376/logs`; ANSI sequences were
stripped before displaying selected lines. No full logs or credentials are
stored here. Existing run evidence proves the diagnosis; asset/source checks
support the recommendation but do not claim a successful run of a proposed fix.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-rubocop-runner-compatibility/)
