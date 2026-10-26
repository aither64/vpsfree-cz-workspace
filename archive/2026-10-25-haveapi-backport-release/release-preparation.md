# HaveAPI 0.30.2 release preparation

Prepared by implementer1 on 2026-10-25, with read-only checks completed by
15:12 UTC. This is preparation evidence, not a publication receipt or final
review. No application files, Git refs, registry state or GitHub settings were
changed. No builds, tests or publishing commands were run.

## Source and procedure

`dev-session current`, both `DEV_SESSION_*` identity values and the trusted
thread binding agree on `2026-10-25-haveapi-backport-release` in
`/home/aither/workspace/ai/vpsfree.cz`.

The canonical bare repository was inspected without fetching or modifying it.
Read-only GitHub API requests independently confirmed its current source tips:

| Ref | Commit | Shared VERSION |
| --- | --- | --- |
| `master` | `38ecca75edaf797d048fb36c6a50ea7e05eb50a9` | `0.30.0` |
| `haveapi-0.30` | `1c3c98f0d77e0b23c8da1a8937f25c5799864a3b` | `0.30.1` |

`haveapi-0.30` is the newest numbered release branch. The remote `v0.30.2` tag
and GitHub Release both return HTTP 404. The existing `v0.30.1` Release is public,
published at `2026-10-24T17:22:00Z`, with 11 assets.

HaveAPI's AGENTS.md and release procedure are identical at these source tips.
The relevant sources read were README.md, AGENTS.md,
[releases.md](https://github.com/vpsfreecz/haveapi/blob/1c3c98f0d77e0b23c8da1a8937f25c5799864a3b/doc/agent-instructions/releases.md),
both branches' development procedures, Makefile, flake.nix, flake.lock,
.github/workflows/release.yml, package manifests/version files and the Rust
packaging guide. Patch releases backport with `git cherry-pick -x`; source and
release metadata commits stay separate. Preserve the intended 0.30.2 version
when backporting from master's older development version.

## Packages and public versions

Every maintained package uses the shared version and is released together.
Each endpoint below returned HTTP 200, listed 0.30.1, and did not list 0.30.2.
The four Ruby VERSION constants and the JS/PHP/Python package manifests on
`haveapi-0.30` also agree on 0.30.1.

| Registry | Package | Current latest | Metadata checked |
| --- | --- | --- | --- |
| RubyGems | `haveapi` | 0.30.1 | `https://rubygems.org/api/v1/versions/haveapi.json` |
| RubyGems | `haveapi-client` | 0.30.1 | `https://rubygems.org/api/v1/versions/haveapi-client.json` |
| RubyGems | `haveapi-go-client` | 0.30.1 | `https://rubygems.org/api/v1/versions/haveapi-go-client.json` |
| RubyGems | `haveapi-rust-client` | 0.30.1 | `https://rubygems.org/api/v1/versions/haveapi-rust-client.json` |
| npm | `haveapi-client` | 0.30.1 | `https://registry.npmjs.org/haveapi-client` |
| PyPI | `haveapi-client` | 0.30.1 | `https://pypi.org/pypi/haveapi-client/json` |
| Packagist | `haveapi/client` | 0.30.1 | `https://repo.packagist.org/p2/haveapi/client.json` |

The npm package contains the callback/async JS clients and TypeScript
declarations. Its browser bundle is also a Release asset. PHP is synchronized
through `vpsfreecz/haveapi-client-php`; its remote master is
`195f1a4db7699dc4187463dab0f0e029df375e6c`, the exact peeled `v0.30.1` commit,
with subject `Release 0.30.1`. This is a read-only baseline observation; the
publishing helper must still perform its full mirror preflight later.
Elixir components are excluded. Rust's embedded runtime is not separately
published to crates.io and needs no crates.io publishing credential.

## Tools and authentication capability

The ambient shell has Git 2.54.0, Nix 2.34.9, Make 4.4.1, Ruby 3.4.9,
RubyGems 3.7.2, Bundler 4.0.14, Python 3.13.15, PHP 8.4.27, gh 2.102.0 and
SSH. Node, npm, uv, Composer, Cargo and rustc are absent from ambient PATH.
This is not a release-shell failure: the required top-level Nix shell declares
Node 24/npm, Ruby 3.4, Python 3.11, PHP 8.3/Composer, uv, Rust/Cargo, gh and
the other release tools. At the inspected release tip its nixpkgs input is
`02c087f3fe673c9e317f206a627cb6b910336dbe`.

The Nix shell was not entered or realized in this bounded investigation;
dependency preparation and exact shell/tool availability remain to be checked
through the monitor workflow if long or uncertain. Ambient Python/PHP versions
are not evidence for the declared release environment.

Only presence/capability results were emitted; no credentials or environment
dumps were printed:

- `gh auth status --hostname github.com` succeeds. Authenticated GET requests
  work, and the current account reports HaveAPI push permission.
- GitHub's `release` environment exists, requires one reviewer, allows `v*`
  tags, and has `prevent_self_review=false`. `HAVEAPI_RELEASE_ENABLED` is
  exactly `true`; release.yml is active. The environment secret named
  `HAVEAPI_PHP_DEPLOY_KEY` exists. Its contents were not retrieved.
- No nonempty GitHub, RubyGems, npm, PyPI or PHP deploy-key token variables
  checked were present in this shell. The GitHub CLI credential file and an
  npm credential setting exist locally; registry credential validity and scope
  were not tested. No RubyGems or PyPI credential file was found.
- RubyGems, npm and PyPI publication use job-scoped OIDC, so local registry
  tokens are not a workflow prerequisite. Current trusted-publisher settings
  cannot be proven from these local/public checks. The exact existing release
  workflow succeeded for `v0.30.1` in
  [run 40114719358](https://github.com/vpsfreecz/haveapi/actions/runs/40114719358),
  providing recent evidence of an operational publishing path. The current
  master build-only release workflow also succeeded in
  [run 40204639555](https://github.com/vpsfreecz/haveapi/actions/runs/40204639555).

No preparation blocker was found. Publication still depends on the final
source, review/check gates, authorization, environment approval and working
OIDC/deploy-key configuration when the approved run executes.

## Required release sequence, not executed

1. Finish the architect-owned backport design and approved implementation on
   the session feature branch based on `haveapi-0.30`. Preserve `-x` backport
   provenance and keep release metadata in its own commit. Do not create a
   new minor branch or bring release content onto master as part of this task.
2. Prepare local inputs before versioning: run
   `nix develop .#client-rust -c true`; enter the top-level `nix develop` shell
   and run `make release-deps`. This prepares Bundler, npm, Composer and uv
   dependencies and ignored library locks. Retain these locks for locked
   checks; do not commit library lockfiles. Release commands run in this shell.
3. Run `make version VERSION=0.30.2`; update CHANGELOG.md with the existing
   `# <date> - version 0.30.2` format and changed components only. Run
   `make release-check`, commit intended changes with active Overcommit hooks,
   and complete the workspace's independent final review before longer checks.
4. Complete the assigned verification through a fresh monitor for long or
   uncertain commands. The documented full local sequence includes
   `make release-test`, `make release`, `make test`,
   `ruby utils/release/cli.rb smoke-npm dist`,
   `ruby utils/release/rust_smoke.rb dist`,
   `ruby utils/release/cli.rb verify dist`, and
   `(cd clients/python && uv run --locked python utils/package_smoke.py)`.
   `make release` requires a clean tracked checkout and empty dist directory;
   it generates server documentation and packages without uploading. The build
   already runs the packaged Rust smoke check. Repeating it is useful only
   when the verification brief requires an independent retained-artifact check.
5. After the lead resolves exact target integration and publication
   authorization, update the supported release branch through the applicable
   coordinated Git procedure and push an annotated `v0.30.2` tag over SSH.
   Recheck remote heads and version absence immediately before release. Never
   move existing tags. Do not begin another tagged release while this one runs.
6. The tag workflow verifies branch membership, VERSION and protected release
   setup, prepares dependencies, runs i18n health/release/component tests,
   builds packages and retains `release-<run-id>` for 90 days. Inspect its tests,
   candidate summary, manifest and artifacts before approving `release` under
   **Review deployments → Approve and deploy**. That gate authorizes registry
   uploads and PHP mirror master/tag synchronization. No package is rebuilt
   after approval. `make publish` deliberately refuses local publication.
7. The approved job verifies retained artifacts and draft Release assets,
   preflights existing package hashes and the PHP mirror, uploads missing
   retained Python files, then publishes the Ruby client before dependent gems,
   npm and PHP. It makes the GitHub Release public only after all destinations
   succeed. Verify publication receipts, exact artifact hashes, all seven
   package versions and asynchronous Packagist indexing.
8. On partial failure, preserve the tag, original Actions artifacts and draft
   Release. Inspect successful uploads and verify their public hashes before
   retrying. Reruns reuse retained files and skip only exact matches; never
   rebuild accepted versions, use `skip-existing`, retag or overwrite a version.
   A source correction requires a new patch release and publication authorization.

The lead owns subsequent tracking and authorization decisions. Link this file
from state.md when accepting the package. This investigation alone does not
trigger mandatory final change review. The session remains open.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-haveapi-backport-release/
