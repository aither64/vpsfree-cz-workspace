# HaveAPI 0.30.0 metadata preparation

Implementer0 completed the bounded lead brief on 2026-10-22. Changes remain
unstaged and uncommitted pending the lead's final source/prose and Git turn.

## Checkout and hook reconciliation

- Exact session and both environment markers matched
  `2026-10-22-haveapi-release` in `/home/aither/workspace/ai/vpsfree.cz`.
- HaveAPI worktree and branch match the registered portal entry, based at
  `a32b15e379f44fc6dae4b15ef4ec17a142e5f465`; initial index was empty and only
  the lead's `CHANGELOG.md` was dirty. No unfinished setup command or lock
  remained. No registration retry was necessary.
- Existing common-directory Overcommit hooks were executable. Read the current
  configuration and both custom hooks, signed the configuration, then ran
  `bundle exec overcommit --sign pre_commit`; custom signatures were unchanged.
- Root dependencies were installed by a fresh catalog-matching
  `gpt-6-luna`/low verification watcher. The selected catalog digest is
  `840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa`, with
  full-access/never execution policy. The operation exited 0 in 34 seconds;
  [complete log](implementer0-hook-deps.log). No owned command remains running.

## Generated metadata inventory

Ran from the top-level HaveAPI worktree:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c make version VERSION=0.30.0
```

This changed 17 tracked files:

- `VERSION`
- `servers/ruby/lib/haveapi/version.rb`
- `servers/ruby/haveapi.gemspec`
- `clients/ruby/lib/haveapi/client/version.rb`
- `clients/go/lib/haveapi/go_client/version.rb`
- `clients/go/haveapi-go-client.gemspec`
- `clients/rust/lib/haveapi/rust_client/version.rb`
- `clients/rust/haveapi-rust-client.gemspec`
- `clients/js/package.json`
- `clients/js/package-lock.json`
- `clients/js/src/haveapi/client.ts`
- `clients/js/dist/haveapi-client.js`
- `clients/php/composer.json`
- `clients/php/src/Client.php`
- `clients/python/pyproject.toml`
- `clients/python/uv.lock`
- `examples/servers/ruby/activerecord_auth/Gemfile`

The JavaScript bundle and npm lockfile are tracked despite matching ignore
patterns; preserve these intended version changes. The Python lockfile changes
only the local project's version, and npm changes only its two root versions.

With the lead's added scope, ran Bundler 4.0.23 `bundle lock --local` using
`BUNDLE_GEMFILE=clients/rust/Gemfile` in the top-level Nix shell. This adds the
18th tracked metadata path, `clients/rust/Gemfile.lock`: five local-version
replacements, preserving all registry versions/checksums. The lead accepted
this exact diff.

## Focused checks

All passed in the declared top-level Nix environment:

- `git diff --check`.
- Existing `make release-check`: reports `Release metadata valid: 0.30.0`.
  This helper currently omits Rust; its success is metadata evidence for the
  existing implementation, not validation of the planned Rust release path.
- Ruby syntax checks for four version files, three changed gemspecs and the
  example Gemfile; PHP syntax for `clients/php/src/Client.php`; Node syntax
  for the tracked browser bundle.
- `uv lock --check` for the Python client, resolving the existing 27 packages.
- Explicit parsed comparison of all 18 version metadata paths, including Rust
  version, gem dependency and both lockfile local package entries/checksum
  placeholders. An initial ad hoc regex matched `PROTOCOL_VERSION`; adding a
  word boundary corrected the checker, and all metadata then passed.
- `bundle exec overcommit --diff HEAD`: HaveapiI18n, PhpCsFixer, PythonChecks
  and RuboCop all passed, with signatures enforced.

No full component suites, release build, registry write, release branch, tag,
default integration, or commit was performed. No API, persistent state, protocol
or deployment behavior changes in this metadata package. Existing release
documentation already describes the version command; no project documentation
edit was needed for this bounded mechanical preparation.

## Remaining work

Hold for the architect brief and lead's Git turn. The later substantive package
must add permanent Rust version/dependency/lock agreement checks; the ad hoc
metadata check above does not replace those tests. Lead owns changelog fact
acceptance and final prose. Keep all metadata together in one later version
commit, with release helper/workflow fixes in separate commits.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
