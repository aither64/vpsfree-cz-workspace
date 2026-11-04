# Package S final source review packet

Latest provenance-only final source is `99ee06654ef956a09b52749f4cd02d1435362087`,
pinning rebased identical generator source `eea3ae5e`. See the current
[validation/equivalence record](validation.md); the accepted source-review and
narrow remediation ranges below remain retained evidence.

Current accepted source is `b650f21fa83c314b3c21aaf62f0d9dda2b08befd`,
one consolidated commit from the same `e5786f69` base. The packet below records
the initially reviewed `383e855` range; this paragraph and
[validation.md](validation.md) record the directly verified narrow follow-up.
The final generator pin is `172c752ef65792de177279956917259d2c3f9b37`,
source SHA256
`ea539499207e09c7e1835733115aeca73db3175963b817c95a621baf45da330b`.
Review found no Blocking issues, Important R1 (explicit action help must select
its exact method) and Advisory A1 (replace full internal output descriptors with
relevant name arrays). Lead accepted the exact narrow remedies. All 519 public
action import/type/interface/factory bodies remained identical after removing
descriptor blocks; no schema/input/public contract changed. Affected quick checks
were repeated successfully. Final diff: 689 files, 30,083 added and 11,449 removed
lines; final manifest SHA256
`c3f8bca08ab66ef954a38aa9650edf073c196af961882ac21a8e8c1a6a9bdffb`.
Old candidate/receipt remain preserved in `candidate-383e855/`.

SDK repository: `vpsadmin-typescript-client`, target `origin/main`, feature
branch `2026-11-01-typescript-client-migration`, assigned worktree under this
initiative. Base `e5786f69b7c223c3bb5b1de99b7f97186eec368a`; final source head
`383e8556208f330472961077cce4dcb546231c8a`. Worktree is clean.

The complete base-to-head series is one commit:

`383e8556208f330472961077cce4dcb546231c8a Generate version 0.3.0 with live descriptions and typed metadata`

The final diff is 689 files, 61,177 added and 11,449 removed lines. Most of the
diff is generated action descriptors/callables and exports across all 519
actions. There are 675 manifest-owned generated files; no generated file was
edited by hand. The ownership manifest SHA256 is
`485eced4d25a57c3f2c7c0bee97e0b120c9cb09c9ab9733894903caa0ee0d098`.
All manifest file hashes and recorded tooling hashes were independently checked
after the successful regeneration batch.

The requested outcome is a fully generated SDK foundation for WebUI migration:
live root/action descriptions, generated pre-dispatch input errors, typed global
metadata, configured wire metadata namespaces, and HaveAPI JS 0.32.0 support.
The unchanged executor seam owns transport/authentication/protocol decoding;
SDK code adds no authentication cache, retry, pagination or completion behavior.
The immutable extracted archive will be checked after this review. No registry
publication, tag, deployment or default-branch integration is authorized here.

## Exact inputs and compatibility

- Generator source: HaveAPI
  `7cffd0b6b6959abf5b5af810ba81004b8defc13c`, clean committed source; generator
  source SHA256
  `89ae36c11883979150bd6963a078052a270e5d0d27f7e7853a667997c027193f`.
- Shared Ruby schema source remains version 0.32.0, SHA256
  `e12f7989a028bb529f4a78a510af8e09411bbeb5eec9c782feb1fbf20862533c`.
- API source `610a96f8ce523afbcd3e4374a70047dbe3264b0d`; see
  [schema-capture.md](schema-capture.md) for full source/export lineage,
  reproducibility and native MariaDB cleanup. The API worktree remains clean
  with no source changes. Schema bytes match the old SDK exactly.
- Schema SHA256
  `476f0086726a443a6ef8ad9a9d499bd3feff6eb6c5b0b652dcc999192d638794`;
  provenance SHA256
  `b20bd20c83e6316c02befdf02e5f4a66c89348337f549bf357113bd488efdb0b`;
  exporter lock SHA256
  `56541da8b42745ab4f392b5d4183f330b3e9d5cd44559d05373c152946ba1053`.
- 151 application resources, 519 actions, 8,720 parameters; all six bundled
  plugins. One authentication resource/five actions remain separately retained,
  validated and excluded from generation because the runtime owns those routes.
- npm-lock SHA256
  `0bc0a5291fcd4126c0b8bf77505970fe56627db566c5b0de3f234d718793db6a`;
  exact HaveAPI JS peer/dev 0.32.0. Installed runtime bundle SHA256
  `9285eab56e435ee86a501a24808e15496d44521881a032090003a1108511f016`,
  matching generator-owner verification evidence.
- Existing pinned SDK tools remain Node 24.21.0/npm 11.19.0/Ruby 3.4.11/
  TypeScript 6.0.3/Prettier 3.9.10. A locked TypeScript 5.9.3 npm alias checks
  WebUI Bundler declarations without changing the WebUI toolchain.

SDK version is the unpublished 0.3.0 candidate. Root/action invocation syntax
and `RequestExecutor` remain compatible; exact runtime dependency changes from
0.30.2 to 0.32.0 intentionally. `ClientInputError` extends `TypeError`; the
new fields classify generated local failure only, while executor errors retain
identity. Output fields and metadata retain optional/null behavior, and unknown
metadata extensions remain possible. Namespace override projects only declared
immediate object-list metadata in returned `data`; the raw envelope and nested
association/Custom values remain untouched. Live descriptions are not permission
grants and types do not validate payloads. Rollback restores matching package,
generator, schema/provenance and manifest.

## History and delivery boundaries

There are no migrations in this branch, no API schema changes, and no persisted
state format changes. No migrations were merged, released, deployed or externally
consumed by this work. There are no superseded approaches or repeated dependency
update commits: version, runtime peer/npm lock, generator pin, refreshed capture
and generated output form one consolidated 0.3.0 update. No intermediate SDK head
requires retention for a deployed or supported state boundary.

No hook framework or repository-local AGENTS.md is declared by the SDK; canonical
Git hooks contain only samples. Commit used the pinned Nix environment and normal
Git path without bypasses. Workspace initial plan/state commit exists before this
project commit. No feature push has run yet; exact generator pin fetchability and
fresh remote default checks remain delivery preparation.

Changed technical docs: README describes descriptions, metadata, input-error
semantics and namespace support; development guide covers exact tools,
reproducible schema/generator provenance, and dual compiler/archive checks;
release guide preserves the retained-archive publication contract; changelog
records 0.3.0. Lead main writing review accepted the documentation facts, and
the package owner applied the writing skill. These docs describe candidate
revision behavior; published npm remains the earlier release until separately
authorized publication.

## Quick checks and remaining verification

Successful exact batch in `regenerate-quick-retry.log`:

```sh
./tools/regenerate --haveapi-source ../haveapi
./tools/regenerate --haveapi-source ../haveapi --check
npm run build
npm run typecheck
npm run typecheck:consumer
npm run typecheck:consumer:webui
node --test test/client.test.mjs test/release.test.mjs
HAVEAPI_SOURCE="$PWD/../haveapi" node --test test/regeneration/sources.test.mjs
```

All passed: source and strict consumer checks with TS6, TS5.9 Bundler consumer,
13 client/release tests, one source-refusal regression. Generation and `--check`
agree. The first watcher invocation failed 127 from the wrong directory before
generation; it had no output effects. The corrected script uses an absolute
working directory. No running operation remains.

After independent G+S review, build/pack one immutable candidate and record its
commit and SHA256/npm SHA512 receipt using existing release tooling. Validate that
exact archive through `tools/check-package.mjs --archive`: package completeness,
dual strict compiler consumers, executor spies, and real installed HaveAPI 0.32.0
against the new owned loopback HTTP fixture. Then give WebUI the same retained
archive for pilot verification. No actual HTTP/package integration ran before
review. The broader isolated API member/admin contract and WebUI integration
remain coordinated by the lead.

Review should cover general, architecture, scope/proportionality and
risk/compatibility lanes with the retained independent reviewer. The public
cross-project contract and runtime dependency justify high risk classification.
The lead owns assignment and whole-foundation G+S review recording.
