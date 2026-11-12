# Rust client package

## Preparation status

Package C is complete. Lead reports reviewed integration and fresh SSH proof of
Rust `main` at exact `3ec8c045dcefcca85b60ffccd38259cda29eeb60`, with repository
claim released. Regeneration changed metadata
only: all 686 generated API/runtime source files are byte-identical. No minor
crate release, version bump, tag or publication is needed; crate remains 0.1.0.
Lead released generation independently of package A after the architect confirmed
the retained public-schema/source inputs are independent. Package A is integrated
at exact `5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5` after all 34 services-up
checks passed. Package E remains prepared and gated on TypeScript 0.3.0 completion.

Final feature head: `3ec8c045dcefcca85b60ffccd38259cda29eeb60`.
Review base: `1ab58627a225589fefc983829de5c4cfee770b3b`.

Session identity was verified with `dev-session current` and both environment
markers: `2026-11-02-haveapi-vpsadmin-release` in
`/home/aither/workspace/ai/vpsfree.cz`.

## Repository and worktree

- Repository: `vpsfreecz/vpsadmin-rust-client`; default branch: `main`.
- SSH remote: `git@github.com:vpsfreecz/vpsadmin-rust-client.git`.
- Feature branch: `2026-11-02-haveapi-vpsadmin-release`.
- Worktree: `worktrees/2026-11-02-haveapi-vpsadmin-release/vpsadmin-rust-client`.
- Genuine registration/creation base:
  `80be1c1a90b7009f8ddecf6a7fe042b506de8b42`.
- Reconciled fresh remote/review base before implementation:
  `1ab58627a225589fefc983829de5c4cfee770b3b`.
- Created and registered with `dev-session worktree add ... --base origin/main`;
  `portal.yml` retains the genuine initial base. The helper selected a stale
  `origin/main`; explicit `git fetch origin refs/heads/main:refs/remotes/origin/main`
  followed by a clean feature fast-forward reconciled the actual target.
  Worktree was clean at the reconciled review base before implementation; the
  final committed range is inventoried below.

The target already includes `1559e448e2b7c7f4311030aa8c0b2dce6a6e424d`
and `1ab58627a225589fefc983829de5c4cfee770b3b`: retained
`schema/generator.Gemfile.lock`, source/lock/shared-schema/runtime refusals,
isolated frozen CI, development instructions and refusal tests. No duplicate
tooling adaptation is needed.

Read workspace AGENTS and the Git, sessions, lifecycle, commits, verification
and documentation procedures, plus dev-session-documentation and
dev-session-handoff skills. Read repository AGENTS, README, development guide,
flake and lock, generator configuration, regeneration wrapper, package manifest,
provenance, changelog and CI/publication workflows.

## Hooks and environment

Repository AGENTS explicitly declares no commit hook framework. No effective
`core.hooksPath`, declared framework files or active executable Git hooks were
found. No hooks were installed or bypassed.

The retained Nix input is nixpkgs
`fe13242281a67641c0102cdb1087f0ebe586c7df`. The shell declares Ruby 3.3,
Cargo/Rust/rustfmt, libffi and other generation/build tools. Generation requires
the exact `rustfmt 1.9.0` and edition 2024. Preserve the existing Rust 1.95 MSRV.

A bounded tool-version preparation probe used:

```sh
nix develop --offline --no-update-lock-file --max-jobs 0 --option builders '' \
  --command bash -c 'ruby --version; rustfmt --version; rustc --version; cargo --version; bundle --version; pkg-config --modversion libffi'
```

It exited 1 because the complete shell closure is not present locally and local
builds were disabled. No tool versions were verified, and no build ran. An
auxiliary offline `nix path-info` probe was interrupted; both commands have
finished. This is an environment preparation gap, not a failing client check.
The subsequent fresh Luna/low watcher completed ordinary Nix shell preparation
in approximately 23 seconds, using substitutions and only a trivial
`nix-shell-env` build. Verified Ruby 3.3.10, rustfmt 1.9.0, rustc 1.98.1,
Cargo 1.98.0, shell Bundler 4.0.9 and libffi 3.8.0. Bundler 4.0.23 is installed
separately for the frozen generator graph. See `rust-shell-setup-result.md` and
the untracked `rust-shell-setup.log`. No process remains from that probe.

Watcher policy: retained/installed catalog
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`,
utility `verification_watcher`, gpt-6-luna/low, fresh context and full-access
execution; native identity `dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`.

## Released tooling inputs

Lead released publication run `41529223599`, attempt 1, SUCCESS. Independently
downloaded public release asset:
https://github.com/vpsfreecz/haveapi/releases/download/v0.32.2/release-manifest.json

GitHub's asset SHA-256 and downloaded bytes match:
`7c53624cc059434279e6eba6f8a9ec151a57897f41e96f0b1d261e1b58fa728b`.
Manifest identifies source `1ef9b204ba45bb261d3334be5c555cc1856b713b`,
tag `v0.32.2`, version `0.32.2` and the same run. Its exact
`dependency_locks["clients/rust/Gemfile.lock"]` text has SHA-256
`061f5e4e0f3cb48d529a7914eb087cabda9889d4200a1af9d0d70af7908b5459`.
Saved untracked manifest and extracted lock under this session; restored only
that lock to the owned tooling checkout. No fresh dependency resolution is
intended. The released graph uses Bundler 4.0.23.

Original tooling checkout: `worktrees/2026-11-02-haveapi-vpsadmin-release/haveapi-rust-tools`,
branch `2026-11-02-haveapi-vpsadmin-release-rust-tools`, head and initial base both
`1ef9b204ba45bb261d3334be5c555cc1856b713b`. It has no feature commits or source
edits; the restored component lock is ignored upstream. Creation met an inherited
Overcommit configuration-signature refusal after checkout was already created.
Registration retry recognized that valid existing checkout; no hook bypass,
signature change or commit occurred.

The tooling checkout was incorrectly registered as a HaveAPI feature target by
implementer2. Lead corrected that manifest entry, but the scanner re-added it
when package E was registered. Lead then assigned the durable repair below.
This is a read-only exact-tag source input, not a HaveAPI feature deliverable.

## Durable source-input repair

Current source checkout:
`worktrees/2026-11-02-haveapi-vpsadmin-release/haveapi-rust-source`.
Created an independent local clone without hardlinks, set canonical SSH origin
`git@github.com:vpsfreecz/haveapi.git`, detached at exact
`1ef9b204ba45bb261d3334be5c555cc1856b713b`, and restored the released ignored lock.
Its clean tracked tree is `fda4d5c159746ffa91887ead63197e7b788e0a64` and lock
SHA-256 remains `061f5e4e0f3cb48d529a7914eb087cabda9889d4200a1af9d0d70af7908b5459`.
Existing isolated frozen bundle check passes with this clone, and both loaded
HaveAPI component paths identify it. No gems or dependency locks were re-resolved.

Removed only the original canonical worktree through ordinary
`git --git-dir=repos/haveapi.git worktree remove .../haveapi-rust-tools`.
Retained original branch
`2026-11-02-haveapi-vpsadmin-release-rust-tools` at exact `1ef9b204`.
The independent source clone is outside canonical worktree discovery, so that
false feature obligation can no longer be recreated from the original checkout.
Lead owns the final manifest-entry correction.

One safety error was found and reconciled: a process-reference assertion found an
idle shell, but the removal sequence lacked fail-fast shell settings, so it
continued after the assertion failed. The shell was proven to be this session's
idle tmux pane `%470`, PID 1694410, with no children. After verifying exact
session/pid/no children, changed its cwd through its existing tmux pane to the
new clone. Readlink/tmux and a repeated command/cwd/fd scan prove no old-source
references remain. No install/generation command was running, no shell/session
was stopped, and source/lock/branch receipts remain intact. Subsequent mutation
sequences use `set -euo pipefail` or checked subprocess calls. No unfinished or
uncertain command effects remain.

Read-only loaded-source receipt from the current clone:

- Ruby 3.3.10; Bundler 4.0.23; generator version 0.32.2.
- Generator source SHA-256:
  `7f941d42626a967296ae1c8e897ef7c9b249858f564e98a3d41824fbf10d15a1`.
- Shared schema: `haveapi-client` 0.32.2,
  `d704e6c155f9f2ec82bdf627857bdc23aa08a1d2133806df1f8ed5beb2d8c439`.
- Maintained runtime SHA-256:
  `9c50b8167a8b82118ba42372633e3b004276ba49fbdfed75d4979a913feea739`.

## Retained execution constraints

- Use exact released HaveAPI source
  `1ef9b204ba45bb261d3334be5c555cc1856b713b` when released by the lead.
- Use an independent generator checkout. Do not mutate a shared HaveAPI
  checkout, its lockfile or Bundler configuration.
- Keep Ruby 3.3 and rustfmt 1.9.0. The lead accepted a narrow frozen generator-lock
  reproducibility adaptation; its final implementation and scope await design.
- Never edit `src/generated/**` manually. Keep generated refreshes separate
  from handwritten changes.
- Current crate is 0.1.0; API target is 7.0. Preserve saved public schema and
  inventory. Generator/runtime source comparison against recorded 0.32.0
  `0e7166a0f8f15827bfac051666a53bf449e999ec` shows only documentation renderer,
  version and gemspec changes; maintained runtime/emitter are unchanged.
  Actual generation must establish whether any Rust code changes. Metadata-only
  changes do not trigger a minor release.
- No integration, repository claims, machine reservations, deployment, long CI
  wait or session lifecycle action is assigned.

Frozen bundle setup passed in approximately 40 seconds via a fresh standalone
Luna/low watcher (`--sandbox danger-full-access --ask-for-approval never`) running
`nix develop --no-update-lock-file --command bash .../rust-bundle-setup.sh`.
The exact released lock installed unchanged under Ruby 3.3.10/Bundler 4.0.23,
`bundle check` passed, and the loaded `haveapi-rust-client`/`haveapi-client`
paths identify the owned exact-source checkout. No operation remains running.
See `rust-bundle-setup-result.md` and untracked `rust-bundle-setup.log`.
An earlier native watcher returned status observations instead of executing the
command; it made no source edits or checks. The corrected one-operation standalone
handoff supplied the setup result above.

Fresh remote tag and crates.io checks report only version 0.1.0. No release
version has been selected; a metadata-only result will keep 0.1.0.

## Final C deliverable and review packet

Complete series from fresh actual `origin/main` review base
`1ab58627a225589fefc983829de5c4cfee770b3b`:

1. `3ec8c045dcefcca85b60ffccd38259cda29eeb60`
   `generated: record released HaveAPI 0.32.2 inputs`.

One focused update stream, one commit. No superseded local attempts, follow-up
fixes, unused compatibility paths or repeated generator/input pin commits remain.
The earlier 0.32.0 tooling commits are already upstream at the genuine new review
base; they are not new feature commits. The original creation base stays recorded
for historical accuracy. No migrations exist: none were authored, merged,
released, deployed or externally consumed by this branch.

Final diff: four files, 18 insertions and 18 deletions:

- `schema/generator.Gemfile.lock`: exact released component graph, including
  0.32.2 path component versions and the publisher-selected `domain_name`
  0.7.20261031 patch. This is the immutable release input, not local resolution.
- `schema/provenance.json`: released exact source, generator/shared-schema
  identities and released lock digest. Capture/schema/toolchain remain unchanged.
- `src/generated/.haveapi-generated.json`: generator-generated ownership metadata
  only; its complete 686-file hash map and runtime digest remain identical.
- `CHANGELOG.md`: main-agent-approved Unreleased wording records the refreshed
  provenance and unchanged generated code. Lead performed the user-facing writing
  pass before commit.

`schema/api-7.0.json`, `schema/inventory.json`, `generator.toml`, Cargo manifest
and lock, Nix inputs, all generated `.rs` and handwritten runtime-facing source
are byte-identical to review base. No schema recapture, new runtime dependency,
tooling framework, workflow or source-generation implementation change.

Requested outcome/acceptance: consume exact released HaveAPI tooling, preserve
public API 7.0/protocol 2.0 and Rust pins, prove reproducible generation and make a
minor crate release only if generated Rust code changes. The measured no-code
result satisfies the conditional no-release outcome. Existing README and
`docs/development.md` remain accurate; no durable behavior/workflow explanation
needs changing beyond the concise changelog. Operational provenance belongs here.

Quick verification passed in the pinned Nix shell before commit:

- `bash -n tools/regenerate`.
- `cargo fmt --all -- --check`.
- `tools/check-provenance` (same canonical schema digest
  `70f89335e15263fd7177f29a00fab04b5ff1923c6922dfd318b07c3ae922fb8d`).
- `tools/regenerate`, then read-only `tools/regenerate --check` with the fresh
  independent exact-source checkout and retained frozen lock.
- `python3 -B tools/test-regenerate.py`: all 10 refusal tests passed, 8.185 seconds.
- Exact retained/released/installed lock byte equality and source/runtime identity
  checks; loaded components point at the new independent source clone.
- Every generated owned file's actual SHA-256 equals its retained manifest hash;
  complete pre/post generated file hash maps are equal (686 files).
- Saved snapshot/inventory, package/config and Nix inputs byte equality;
  `git diff --check` including final changelog.

Actual tools remain Ruby 3.3.10, Bundler 4.0.23, rustfmt 1.9.0,
rustc 1.98.1, Cargo 1.98.0, edition 2024, MSRV 1.95. No hook framework is
declared in this crate, as verified before commit.

Lead explicitly accepted bounded verification for the metadata-only result:
no long compile/doc/package/MSRV matrix is required because emitted Rust, runtime,
package manifest/lock, schema and toolchain are unchanged. No live-server test or
server mutation is required. This does not claim new compilation/MSRV evidence.
The existing frozen/refusal behavior is reused without handwritten adaptation.

Risk is low: mechanical provenance/lock metadata and a factual changelog update,
with no runtime/API/persisted-state/compatibility or deployment behavior change.
Standalone substantive content review may use the mechanical-content exemption;
the lead still assigns independent complete-series/history/migration review under
mandatory-change-review (retained reviewer0 Sol/xhigh). Review outcome is pending.

Feature branch was pushed over SSH; fresh remote head proof equals
`3ec8c045dcefcca85b60ffccd38259cda29eeb60`. CI run
`41534639867` is queued on that exact head; no broad CI wait is requested.
Saved comparison capture binds exact
`1ab58627a225589fefc983829de5c4cfee770b3b` →
`3ec8c045dcefcca85b60ffccd38259cda29eeb60`. No PR, default-branch merge,
tag, crate publication, resource claim, deployment or lifecycle operation.
Broad CI is not awaited. Lead owns the fresh target check/integration after A;
implementer2 retains review-fix ownership and package E execution after its gates.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-haveapi-vpsadmin-release/
