# RuboCop runner compatibility: findings and implemented fix

Investigated on 2026-10-30 by architect0. The original investigation used only
read-only source/API access and session documentation. Session identity and
workspace binding were verified before investigation and this design update.
Repository guidance was read from canonical bare objects and immutable GitHub
content; remote workflow content and Actions logs below establish tested
revisions.

## Current authorization and status

The user authorized implementation and integration with: "ok, implement the
fixes. merge it after verification." The lead confirmed integration targets
`vpsfreecz/vpsadminos` → `staging` and `vpsfreecz/security-advisories` →
`2026-07-13-security-advisory-automation`. Initial tracking commit:
`fea9ffee4b405435fb0667303f35d096d0856c59`.

Implementer0 completed the three-file package, quick checks and required hooks.
Reviewer0 reviewed the exact complete branches with no findings. All three
feature CI jobs passed on Ubuntu 26.04.1 with Ruby 3.4.12: vpsadminos RuboCop
checked 1,494 files and security-advisories RuboCop checked 29 files, both
without offenses; security-advisories RSpec passed 262 examples with no failures.

The lead fast-forwarded and SSH-pushed these unchanged reviewed/verified heads
to the approved defaults, confirmed the exact remote heads, and released both
repository claims:

| Repository / target | Integrated exact head |
| --- | --- |
| vpsadminos / `staging` | `4dfed86538fcfaf7f5b43fdf2afcb2cadd4aa58d` |
| security-advisories / `2026-07-13-security-advisory-automation` | `7b6c71807e3c5a41f585fd1d9563e151ada71244` |

See [implementation.md](implementation.md) for changes, hooks and quick checks,
[review.md](review.md) for independent whole-branch/no-migration conclusions,
and [verification.md](verification.md) for exact CI run/job links and integration
proof. Temporary integration worktrees were removed; feature refs/worktrees
and the session remain retained. The lead's watcher is observing post-merge
default-branch runs at this reconciliation checkpoint; [state.md](state.md)
owns their current status. Architect0 changed only this brief. The original
diagnostic evidence below remains historical evidence for the fixed failure.

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

## Selected fix and alternatives considered

vpsadminos now sets `ruby-version: '3.4'` in the existing setup-ruby step in
`.github/workflows/rubocop.yml`, preserving the Ruby minor series and linter
command. This confines the patch-selection policy to CI and leaves the
repository's developer tooling version file and its other consumers unchanged.
The job selects `ubuntu-26.04`, and `.github/workflows/rubocop.yml` appears in
both push and pull-request path filters. Its final-head Actions run resolved
Ruby 3.4.12 and passed setup, Bundler and RuboCop; see
[verification.md](verification.md).

Changing `.ruby-version` from `3.4.0` to `3.4` is also sufficient for this
workflow, but applies a floating patch policy to every consumer of that file.
Choose that only if project-wide patch tracking is intended and local version
manager support is checked. It is broader than needed for the reported CI
failure. An exact pin to `3.4.12` works with the published Ubuntu 26.04 asset,
but needs ongoing updates and can repeat this failure on a future image.

The short-term workaround is `runs-on: ubuntu-24.04`, preserving Ruby 3.4.0.
Its binary exists, and the earlier run proves this combination worked with the
same original workflow and action. This fallback was not selected or exercised
for the final revision; pinning the older image defers patch maintenance.

security-advisories now applies the same `'3.4'` and `ubuntu-26.04` policy to
both RuboCop and RSpec workflows; both final-head jobs passed. At investigation
time, the latest October 20 runs used Ubuntu 24.04.5: the original exact
`3.4.0` configurations were susceptible, not observed Ubuntu 26.04 failures. See
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

## Retained implementation and verification contract

The following authorized brief governed implementer0's completed package.
Its quick-check, review, final-head CI and integration requirements are met in
the evidence linked above; it does not describe pending implementation work.

| Package | Files and acceptance |
| --- | --- |
| vpsadminos CI | `.github/workflows/rubocop.yml`: add explicit quoted `ruby-version: '3.4'`, select `runs-on: ubuntu-26.04`, and add `.github/workflows/rubocop.yml` to both push/PR path lists. Preserve Bundler caching, linter arguments, permissions and Ruby minor series. |
| security-advisories CI | `.github/workflows/rubocop.yml` and `.github/workflows/rspec.yml`: replace exact `3.4.0` inputs with quoted `'3.4'` and select `runs-on: ubuntu-26.04` in each job. Preserve test commands, caching, permissions, concurrency and trigger behavior. Independent from vpsadminos. |

Repository commits/review remain separate; there is no shared interface or
rollout ordering dependency. No changes to `.ruby-version`, Gemfiles, lockfiles,
RuboCop settings, application code, other workflows or repository defaults are
part of this package. Refer any required scope adjustment through the lead.

The explicit runner image is a lasting choice for these jobs, avoiding a
temporary verification branch, extra matrix/job, or repeated reruns hoping for
the new `ubuntu-latest` image. It also makes future OS changes deliberate.
The Ruby patch floats within 3.4; Ubuntu release selection is fixed at 26.04.

Trigger inspection at the audited default revisions found no branch filters
in these workflows. vpsadminos filters push/PR events by Ruby, gemspec, Gemfile
and RuboCop configuration paths; adding its workflow path lets this workflow
edit trigger on its feature branch. security-advisories has unrestricted push
and pull-request events plus `workflow_dispatch`, so both changed files run on
ordinary feature pushes despite its nonstandard default branch. No PR, default
branch mutation, new manual trigger or branch-filter widening is required for
pre-merge verification. Implementer must confirm this remains true at the
fresh implementation bases.

Quick checks: inspect the final workflow diff and YAML, verify action refs and
current 3.4 asset support, and use each repository's declared hooks when
committing. Keep source/test commands intact. No new unit tests are needed for
these declarative version/runner/trigger changes. Final independent review
follows complete committed changes and passing quick checks, before long CI
verification; include the whole base-to-head series and explicit no-migration
conclusion. The lead releases feature publication after review, using ordinary
feature pushes to start the jobs. No repository merge claim is needed for
implementation, review, feature publication or CI.

Longer acceptance: the lead's fresh verification watcher observes all three
Actions jobs on the final committed feature heads. Require job logs identifying
Ubuntu 26.04, resolved Ruby 3.4.x (currently 3.4.12), successful Bundler setup,
and successful execution of the real RuboCop/RSpec command. A queued, skipped
or 24.04 run is insufficient. Record each final source SHA, action SHA, runner
image, Ruby version and run/job URL; inspect any failure before retrying. This
is a single bounded batch of three jobs, not a broad repository test campaign.
No VM, kernel, deployment or production tests are needed for this CI-only
change. Merge only after the quick checks, independent review and this Actions
acceptance pass; the lead follows fresh-target/claim/fast-forward integration
procedure and verifies the exact final heads in the two approved remote
defaults, releasing each merge claim before further CI or record updates.

Compatibility: this selects a newer patch of the same Ruby minor in hosted CI;
gem resolution and linter/test execution passed there. Keep RuboCop's
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
stored here. Original run evidence proves the diagnosis; asset/source checks
alone did not validate the fix. The subsequent successful final-head runs,
independent review and exact remote integration are recorded in the linked
implementation, review and verification evidence.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-rubocop-runner-compatibility/)
