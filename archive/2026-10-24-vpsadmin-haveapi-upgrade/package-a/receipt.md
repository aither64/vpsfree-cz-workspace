# Package A: released HaveAPI dependencies

Status: implemented, locally checked and committed as
`ff44d95ebe9794341185ba5c78250e130dde80fd`. Repository Git ownership and
Package B write pause were released to the lead. No operation remains active.
Independent whole-deliverable review, publication and longer checks remain
lead-owned after Package B is complete. This is not whole-branch readiness.

Owner: implementer0. Session identity verified by `dev-session current`, matching
`DEV_SESSION_SLUG`, `DEV_SESSION_WORKSPACE` and trusted thread binding. Repository
worktree: `worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin`; branch
`2026-10-24-vpsadmin-haveapi-upgrade`; initial base
`b82eeca50cd4dd7bd76728685c7de8aad66e7ba5`. Initial plan/state commit: `b6001eb8`.

## Scope and design

Follow Package A of [design.md](../design.md), plus the lead's accepted addition
of `haveapi-go-client` and `haveapi-rust-client` runtime adapter gems to the API.
Package B owns API documentation registration, specs and developer docs, with
no dependency-file overlap. No project source outside the assigned dependency
files is changed here. All updates form one logical dependency stream.

## Setup and procedure deviations

The lead's initial worktree creation failed its post-checkout Overcommit trust
check after Git had already created the exact branch and clean physical
worktree. Verified both identities and original base before proceeding.
Read `.overcommit.yml` and all four custom hooks. In the root Nix shell,
`bundle exec overcommit --sign` and `bundle exec overcommit --install` passed;
configuration verification remains enabled and all custom signatures exist.
See [hooks-setup.log](hooks-setup.log). The first transient watcher's shell wrapper
failed quoting before Nix ran; a fresh watcher then ran a parent-written script.

Ordinary `dev-session worktree add` registration retry first encountered another
same-session command, then succeeded without recreation or hooks bypass.
The registered repository retains its original exact initial base.

The local HaveAPI update skill references absent `tools/bundix_all.sh`.
Even `--skip-bundix` fails root detection because it requires that absent file.
The lead accepted direct edits of its four intended declarations and scoped
`rake vpsadmin:gems:api vpsadmin:gems:client vpsadmin:gems:download_mounter`
regeneration. The unrelated update skill is deliberately outside this package.

The first scoped regeneration used `bundle exec rake`, which leaked its root
Bundler environment into bundix's isolated Ruby wrapper. The task had copied the
API Gemfile and removed its lock before failing with root `GemNotFound`; no
resolver or Composer step completed. Reconciled these effects and retried with
the documented plain `rake` in the root Nix shell. The task owns normal lock
replacement; no manual lock reconstruction or hook bypass is involved. See
[generation.log](generation.log) and [generation-retry.log](generation-retry.log).

## Artifact provenance

Registry metadata is retained alongside this receipt. Ruby release SHA256:

| Gem | Version | SHA256 |
| --- | --- | --- |
| haveapi | 0.30.1 | `309b94465461b0ac1bd2019e63f601e287a027dfcb668ceb54b9f6799ab5b00f` |
| haveapi-client | 0.30.1 | `4759bb0003649a8ebcf5f88c05a33b3491db296a984a9b8d3408a205bc8e5cf1` |
| haveapi-go-client | 0.30.1 | `ffa292555fe3d203df7dbb1ee548c56600b69d443cf93ff03eef34fb4f652b92` |
| haveapi-rust-client | 0.30.1 | `226b1831bbcf8ed5bfc5ef58e12d3764b63df51304e610cbc95b6d6fb1fa18ca` |

The npm registry tarball
`https://registry.npmjs.org/haveapi-client/-/haveapi-client-0.30.1.tgz`
was SHA512-checked before extraction against registry integrity
`sha512-n4RMhSbaJZLRm9390wz+M1759h06sEOfh3XVG3t/wGrE0mr97uf+ozERXdJfGXGqxdxelkk765vidheYwUJBWw==`.
Tarball SHA256: `7760acdc16631c6eafe70586e76aa8508307bb16fc41a834fbb5e2bb0b150044`.
Both vendored files are byte-identical to its `dist/haveapi-client.js`, SHA256
`1448ad6f6ef8801f088410d7cf3be32cd00de613efb7be031445a9f0bc348593`.
That file also exactly matches checked-in `clients/js/dist/haveapi-client.js`
at HaveAPI `v0.30.1`, commit `1c3c98f0d77e0b23c8da1a8937f25c5799864a3b`.
Registry attestation statements identify that tag, commit and release workflow
run `40114719358`, attempt 1; statements are saved in
[npm-attestations.json](npm-attestations.json) and
[npm-provenance.json](npm-provenance.json). This is statement inspection and
artifact-integrity verification, not a claim of cryptographic attestation
signature verification. The registry metadata has no `gitHead`.

## Compatibility and recovery

Baseline packaged Ruby HaveAPI resolution is 0.29.12. Its Ruby client runtime
release diff to 0.30.1 only changes the version constant. Server runtime changes
are documentation rendering/profile registration and related assets. Ruby
protocol remains 2.0; API 7.0 is unchanged. Added Go/Rust adapter gems supply
profiles consumed by Package B. They are regular API runtime dependencies,
not developer-only dependencies.

The legacy PHP UI continues to construct `HaveAPI.Client`, load a saved API
description and authenticate by callback using token or OAuth2. Its callback
interface is preserved; no legacy caller is changed to the async API.
`console_router/views/console.erb` still loads its own distribution. Callback
checks use the released upstream compatibility suite against each exact local
bundle with Promise and AbortController deliberately absent.

No database migrations, persistent-state formats or node/OS configuration are
changed. Rollback restores source requirements, generated lock/gemset and PHP
integrity metadata, and both bundles as one set. No coordinated node update is
required. Deployment, integration, production KB publication and old-session
mutation are outside this package. Broader browser and packaged-services behavior
remain subject to the lead's post-review integration checks.

## Verification so far

- Root Nix setup, normal Overcommit signing/installation: passed (56 seconds).
- Existing-branch worktree registration: passed after transient contention.
- JavaScript syntax and upstream callback compatibility: 12/12 cases passed
  against each local distribution (24 total); [js-callback.log](js-callback.log).
  Covers UMD/global/AMD exports, OAuth2/token/basic authentication, resource and
  action invocation, response/list helpers, validation and ActionState callbacks.
- Scoped Ruby metadata and targeted PHP checks passed; see detailed results
  below. API load check passed after the accepted libffi shell fix.

## Documentation placement

Dependency declarations and generated metadata are authoritative for supported
versions. This mechanical package needs no separate lasting feature guide;
Package B owns discoverable API documentation/profile behavior and its docs.
This receipt retains temporary artifact, setup, resolver and review evidence.

## Resolver result and focused PHP checks

Scoped rake generation completed on the retry. Version comparison against the
exact initial base found no unrelated upgrades. API changes are HaveAPI and
HaveAPI client 0.29.12 to 0.30.1, new Go/Rust adapters 0.30.1, and required Rust
adapter dependencies fiddle 1.1.8 and tomlrb 2.0.5. Client and download-mounter
change only HaveAPI client 0.29.12 to 0.30.1. All 121 API, 29 client and 33
download-mounter lock entries match generated gemset version sets; each generated
HaveAPI hash matches its RubyGems SHA256. See
[ruby-resolution-changes.json](ruby-resolution-changes.json) and
[ruby-metadata-consistency.json](ruby-metadata-consistency.json).

Composer changed only haveapi/client 0.29.6 to 0.30.1, source commit
`195f1a4db7699dc4187463dab0f0e029df375e6c`. `composer2nix` initially required a
package name because composer.json intentionally has none. Retried with existing
name `vpsadmin-webui`, temporary composition output and `--no-copy-composer-env`
to preserve the repository's maintained default/environment. Only the HaveAPI
archive URL, source name and integrity hash changed in php-packages.nix.
PHP client load and Composer validation passed (existing missing-license warning).
The 13 selected regression cases passed 355 assertions, exit 0. A repeated check
with deprecation details traced the single warning to unchanged
`webui/lib/pagination.lib.php:151` (`$action` implicitly nullable), outside this
upgrade. See [php-checks.log](php-checks.log) and
[php-deprecations.log](php-deprecations.log).

## API shell diagnosis

The initial API setup run (handle 41101) exited 1; all effects are reconciled and
no run remains active. It installed many local gems, then failed building
fiddle 1.1.8 because the declared API development shell lacks libffi headers.
This is a required new dependency of the released Rust adapter. Pinned nixpkgs
`/nix/store/5b2ic4sxjc2lzgxk4hninyw22r5gv5qr-source` already defines default
fiddle gemConfig with libffi for packaged builds. Root devShell has libffi;
API devShell needs lasting support. The lead assigned the architect a bounded
brief before the source fix/retry.

This setup was launched by the parent by mistake before assigning its fresh
watcher. Its handle could not transfer, so the lead accepted minimal parent
monitoring of this exact run; no duplicate was launched and no effects were
abandoned. Later uncertain operations must resolve a fresh watcher first.

## Native dependency correction and final quick checks

The architect's native dependency addendum and lead accepted a bounded permanent
fix: add libffi/pkg-config to the API devShell only, plus libffi-dev/pkg-config
to the existing apt lists in both API topic jobs and the conditional migration
job. No action refs, matrices, conditions, root shell, package overlays or lock
inputs changed. Official action release metadata was checked and matches the
existing major refs; [workflow-action-upstream.json](workflow-action-upstream.json).

The API watcher initially received an unusable opaque task, then received the
follow-up brief and ran the exact command once; no parent duplicate was launched.
The corrected .#api shell setup passed in 35 seconds, exit 0. It installed Fiddle
1.1.8, `pkg-config --modversion libffi` printed 3.8.0, real Fiddle and Go/Rust
documentation adapter requires succeeded, all four HaveAPI runtime gems were
0.30.1, and API Gemfile RuboCop passed. See
[api-setup-fixed.log](api-setup-fixed.log). API devShell derivation:
`/nix/store/j3x5dlqj8cgrmwffbbh23mw8c2d88g88-vpsadmin-api.drv`.

Actual packaged API environment evaluation confirms Fiddle already receives
libffi 3.8.0 through pinned nixpkgs; no custom package workaround is needed.
See [packaged-api-evaluation.json](packaged-api-evaluation.json). This is
**evaluation**, not a completed packaged build or packaged runtime test.
Packaged runtime verification remains for the lead's post-review services-up
check.

Nixfmt, four source declaration RuboCop checks, workflow YAML parsing and
`git diff --check` passed; [quick-checks.log](quick-checks.log). Actionlint
workflow syntax passes with shellcheck disabled. Full actionlint reported the
same pre-existing SC2016 at migration workflow line 105 on the exact baseline:
its embedded Ruby code deliberately uses literal single quotes. See
[workflow-syntax.log](workflow-syntax.log), [workflow-lint.log](workflow-lint.log)
and [workflow-baseline-lint.log](workflow-baseline-lint.log). No workflow
syntax/matrix finding was introduced by the apt dependency additions.

Package B acknowledged a write pause before the normal hook commit. Its five
edited/untracked files were hashed before commit so ordinary Overcommit
stash/restore behavior can be checked without consuming any of B's changes.
Only the exact Package A paths are staged.

## Final commit, complete package inventory and handoff

Exact range:
`b82eeca50cd4dd7bd76728685c7de8aad66e7ba5..ff44d95ebe9794341185ba5c78250e130dde80fd`.
One logical update commit: `deps: adopt HaveAPI 0.30.1 across server and clients`.
20 changed dependency/native-prerequisite files. Complete review artifacts:
[final.diff](final.diff), [final-history.txt](final-history.txt),
[final-files.txt](final-files.txt), plus this receipt and linked verification logs.
No obsolete intermediate dependency pins or follow-up commits remain.

All normal pre-commit hooks passed: MigrationSpecs, Nixfmt, VpsadminWebuiI18n,
RuboCop, VpsadminApiI18n. Commit-msg checks passed with advisory warnings on two
body lines exceeding 72 columns; all lines satisfy required 80-column limit.
See [commit.log](commit.log). The five B-owned edited/untracked files matched
[b-before-commit.json](b-before-commit.json) after Overcommit restored changes.
Index is empty and no B file entered the A commit. The disposable PHP test cache
created by the focused checks was removed; local dependency directories remain
available for Package B's runtime checks. No watcher or parent command remains
active, and no uncertain Git/setup effect remains.

Migration inventory: **no migrations**. This package changes no migration file,
schema, seeds, persisted state or data conversion. No feature migration has been
merged, released, deployed or externally consumed. Nothing was pushed, merged or
deployed by this package. Native package evaluation is recorded separately from
built or deployed runtime evidence.

The lead may let B resume edits and Git operations, preserving the A commit.
B must finish actual documentation profile registration/rendering/specs/docs
before whole-deliverable independent final review. Longer checks remain as
planned: packaged services-up (including actual packaged Ruby adapter loads),
relevant browser/auth/console coverage, API full/core and affected package CI as
selected by the lead after review. These are outstanding, not passed evidence.
No deployment, integration, KB publication or lifecycle action was performed.

Session portal:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/>.
