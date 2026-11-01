# HaveAPI preparation evidence

Owner: implementer1. Session identity and environment matched
`2026-11-01-haveapi-0321-docs-switch-user` in
`/home/aither/workspace/ai/vpsfree.cz`; saved access is `workspace_write`.

## Worktrees and hook preparation

- Master feature checkout: `worktrees/2026-11-01-haveapi-0321-docs-switch-user/haveapi`,
  branch `2026-11-01-haveapi-0321-docs-switch-user`, initial base
  `209a7ac0c2fe6cd1b78735f50b5e60d979309543`, integration target `master`.
- Stable feature checkout: `worktrees/2026-11-01-haveapi-0321-docs-switch-user/haveapi-stable`,
  branch `2026-11-01-haveapi-0321-docs-switch-user-stable`, initial base
  `0e7166a0f8f15827bfac051666a53bf449e999ec`, integration target `haveapi-0.32`.
- Both use canonical project `haveapi`, GitHub `vpsfreecz/haveapi` and SSH origin
  `git@github.com:vpsfreecz/haveapi.git`. Both ordinary registration retries
  exited zero. The installed command has no `--default-branch` option; stable
  registration's `default_branch` was corrected in this session's `portal.yml`
  with lead authorization. No historical base was invented or branch recreated.
- Reviewed `.overcommit.yml` and all three custom hooks. The master/stable hook
  sources match. Existing shared Overcommit hook entrypoints are installed.
  In the prepared root Nix environment, ran documented `overcommit --sign`
  separately for both checkouts and `overcommit --sign pre_commit`; no plugin
  signatures changed. Hooks were never bypassed.
- Git preparation ownership was explicitly released to the lead/implementer0
  after both registrations. Further shared Git/config/ref writes are serialized
  through the lead.

## Root environment

Fresh Luna/low watcher `/root/prepare_master_nix` ran
`nix develop --command bash -c 'ruby --version; bundle check && bundle exec overcommit --version && bundle exec overcommit --help'`
at master initial base. Passed, exit 0, 67 seconds. Ruby 3.4.11, Bundler 4.0.23,
Overcommit 0.74.0. Full disposable log:
`/tmp/2026-11-01-haveapi-0321-docs-switch-user-master-nix-prep.log`.
Root development bundle was prepared; this does not prepare server/client
component bundles or establish passing source tests.

Stable `nix develop -c make release-deps` passed, exit 0, about 170 seconds,
at stable initial base. Fresh Luna/low watcher `/root/prepare_stable_deps` owned
the run; no command remains running. Full disposable log:
`/tmp/2026-11-01-haveapi-0321-docs-switch-user-stable-release-deps.log`.
Exact flake/dependency lock texts and SHA-256 receipts are saved in
`evidence/stable-prepared-inputs.json` for local comparison during versioning.
The tracked checkout remains clean. No longer integration suite was launched
before final committed review.

## Environment-boundary lesson

Run `dev-session` in the normal workspace environment. Running it inside
HaveAPI's root Nix shell inherited `GEM_HOME` pointing at native gems built by
Ruby 3.4.11. The installed workspace command uses pinned Ruby 3.4.9; loading the
inherited json extension failed with a GLIBC_2.44 version error before session
mutation. The same ordinary registration command outside Nix succeeded.
Keep HaveAPI tool commands inside its required Nix shell. For signing another
checkout, `overcommit --sign -- TARGET` separates the target from `--sign`'s
optional hook argument; bare `--sign TARGET` treats TARGET as a hook name.

## Read-only registry observation

On 2026-11-01, exact 0.32.1 endpoints returned HTTP 404 for RubyGems `haveapi`,
`haveapi-client`, `haveapi-go-client`, `haveapi-rust-client`,
`haveapi-typescript-client`, npm `haveapi-client` and PyPI `haveapi-client`.
Packagist `haveapi/client` metadata returned HTTP 200 without version 0.32.1.
This is observation-time absence, not proof of registry ownership or release
readiness. Publication needs a fresh preflight and original artifact hashes.

## Proposed patch notes for lead inspection

```markdown
# Sun Nov 01 2026 - version 0.32.1

## Ruby server

- Add `switch_user_revoke_params` for provider-specific revoke parameters when
  switching documentation accounts. Providers can close shared SSO while
  ordinary Sign out keeps its existing behavior.

## Development tooling

- Skip quick performance comparisons for new branches created at a commit
  already contained in the default branch.
```

Source backports, version metadata and committed quick checks are complete.
Master final head is `cc06cb8c2a6305f13d3b80ebc0a461507055b14c` with VERSION
`0.32.0`; stable final head is `c54404c0818284135add1e77f43feb92e192116c`
with VERSION `0.32.1`. Both worktrees are clean. Stable OAuth/event-baseline
specs passed (152 examples, zero failures), release-check and branch-wide
Overcommit hooks passed, and external dependency records are unchanged. Git
ownership is released to the lead for independent final review. Feature pushes,
longer suites, integration and protected publication remain pending. The lead
owns protected actions. No production deployment or session lifecycle action was
performed or requested.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-haveapi-0321-docs-switch-user/

## Release-CI fixture remediation

Run `41329778485` failed before package build in two release specs: copied
0.32.1 metadata was implicitly or explicitly treated as master. The production
master patch-zero guard correctly rejected both. One test-file fix names the
cold-source branch explicitly and normalizes the detached CLI master fixture to
synchronized `999.0.0` metadata; binary files are excluded from normalization.
The existing positive CLI and nonzero-patch rejection assertions remain.
No production guard, package version, dependency or runtime behavior changed.

Old reviewed/published feature heads are retained in separate recovery refs
`2026-11-01-haveapi-0321-docs-switch-user-recovery-master-ci` at
`cc06cb8c2a6305f13d3b80ebc0a461507055b14c` and
`2026-11-01-haveapi-0321-docs-switch-user-recovery-stable-ci` at
`c54404c0818284135add1e77f43feb92e192116c`. No history was rewritten.
Master now ends at `391b0190241cf195a69b06f7297d3e4eebec5a83`; stable has
its `-x` backport `9efeadf91d894e01d1d4f4a3e3fc64c6309785c7`. Both are
clean. Full comparisons were recaptured against the original registered bases.

On each line, the cold-source example passed (one example), all master-version
policy examples passed (four examples), and changed-file RuboCop passed. Master
commit hooks and stable changed-range hooks passed; stable release-check still
validates 0.32.1 metadata/prepared inputs. Logs:
`/tmp/2026-11-01-haveapi-0321-docs-switch-user-master-fixtures-quick.log`,
`/tmp/2026-11-01-haveapi-0321-docs-switch-user-master-cold-fixture.log`,
`/tmp/2026-11-01-haveapi-0321-docs-switch-user-stable-fixtures-quick.log`.

Git ownership is released to the lead for the same independent reviewer's
affected-lane/history assessment. No new push, workflow rerun, long suite,
integration, tag or package publication was launched in this package.
