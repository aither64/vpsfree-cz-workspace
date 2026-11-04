# Immutable frontend and BFF packages

Requirement: [REQ-068](REQUIREMENTS.md). The flake exposes separate
`packages.x86_64-linux.frontend` and `packages.x86_64-linux.bff` outputs. The
frontend package is the public static root. The BFF package contains its own
production Node runtime graph and executable. These packages do not enable a
service or deploy a host; the reusable [NixOS service module](NIXOS_SERVICE.md)
is disabled by default and site configuration remains separate.

## Reproduce the dependencies

Enter `nix develop` for the locked Node and npm. The root and BFF are independent
npm projects. The root uses the tracked generated client candidate described
below; `npm ci` installs it from the repository-relative archive without a registry
request for that client or a source build. Compute the BFF's cache separately:

```sh
prefetch-npm-deps bff/package-lock.json
```

The frontend cache hash belongs to [frontend.nix](../../packages/frontend.nix);
the separate BFF hash belongs to [bff.nix](../../packages/bff.nix). The frontend
includes the exact registry HaveAPI dependency and locked XMLHttpRequest transport; see its
[source and artifact contract](HAVEAPI_CLIENT.md). The root prefetch reported six bundled optional
dependencies nested under `@tailwindcss/oxide-wasm32-wasi` without separate
resolved URLs. Their WASI-only
placement and bundled metadata explain the warning, but only an actual x86_64
package build can establish whether the cached dependency set is sufficient.
Do not edit a lock or reuse the other project's hash to work around a fetch
failure.

<a id="temporary-unpublished-sdk-input"></a>

### Temporary unpublished generated client input

The generated client remains unpublished. The root manifest uses
`file:vendor/vpsadmin-typescript-client-0.3.0-99ee06654ef9.tgz`, an unchanged copy
of the verified candidate. [Its compact provenance](../../packages/vpsadmin-typescript-client-provenance.json)
records the complete client revision, archive size/digests, generator/schema
identity and runtime peer. Version and revision in this filename identify the reproducible
input; an unpublished package version may be reused for a later candidate only
with a new revision-qualified filename and updated integrity.

The source checker verifies that the archive is a regular file and that its size
and hashes match the provenance record. It also checks the manifest and npm lock
against that record. Existing generated client archive verification owns content,
ESM/type and HaveAPI consumer checks. WebUI does not unpack or rebuild the archive
to validate it. The source filter retains `vendor/`; the installed public root
contains only the reviewed compiled frontend output.

The pinned remote npm prefetcher cannot resolve a relative `file:` tarball. The
frontend's existing `fetchNpmDeps` validates source/provenance, saves the canonical
lock and removes only the generated client package record from a temporary
prefetch lock. Its post-build hook restores the byte-identical canonical lock in the cache.
The normal npm hook compares that lock and runs offline `npm ci`; the archive
comes from the retained source. `makeCacheWritable` lets npm cache that local
archive. The BFF fetcher and lock remain independent.

The frontend selects the normal npm hook through `pkgs.npmHooks.override`, with
a small adapter for its `prefetch-npm-deps` dependency. It delegates all arguments
and failures to the pinned upstream tool. After a successful `--map-cache`, the
existing source checker adds the local client's original resolved key and
recomputed, verified SHA-512 integrity to the transient map. Remote entries stay
intact; conflicting client entries or invalid source bytes fail without rewriting
the map or lock. This describes verified local source bytes, not a remote cache download.
The unchanged upstream `--fixup-lockfile` and ordinary offline npm install then
retain the canonical generated client integrity. The BFF uses its original hook.

For a candidate update:

1. Change reusable client behavior through the HaveAPI generator, regenerate with
   the client's sole tool, then use its existing build/pack/archive-check workflow.
2. Copy the verified archive unchanged under its new revision-qualified name.
   Update the compact provenance and generate the root manifest/lock with pinned
   npm (`npm install --package-lock-only --ignore-scripts --save-exact file:vendor/<candidate>.tgz`).
   Preserve unrelated dependency records and remove the superseded archive from
   the current source tree. Never replace different bytes under one identity.
3. Stage the new archive and provenance before building a Git-backed flake. Temporarily set
   `npmDepsHash = pkgs.lib.fakeHash` in `packages/frontend.nix`, then run only the
   dependency-cache derivation:

   ```sh
   nix build --no-link --print-out-paths .#frontend.npmDeps
   ```

   The expected hash mismatch prints `got: sha256-...`. Set `npmDepsHash` to that
   value and repeat the same command to verify the cache. Its `package-lock.json`
   must compare byte-for-byte with the committed lock. Plain root
   `prefetch-npm-deps package-lock.json` cannot perform this local-archive step.
4. Check a clean npm install, ESM/type resolution, source-checker negatives and
   affected policy tests. Commit the source/metadata and complete independent
   review before full frontend/Nix package and browser/API verification.

Rollback restores a matching WebUI source/archive/lock/cache-hash set. A compatible
released client is a pre-merge prerequisite; no registry version has been selected
and publication remains separately authorized. When that release is available,
replace the file dependency with its exact version/integrity, remove the temporary
archive/provenance checks, Nix prefetch hooks and frontend cache-map adapter, and
regenerate the ordinary registry lock and cache hash. Run the affected package
checks. No future registry artifact is assumed.

The [optional local-client workflow](HAVEAPI_CLIENT.md#optional-local-generated-client-development)
uses a no-save npm archive override and remains available after that transition.
It does not change committed packaging inputs or add an optional Nix mode. The
current `file:` dependency still needs the adapter described above.

## Source, contents and provenance

Both packages use one cleaned flake source. It retains the linked design
handbook, generated inventory, source and scripts needed by the archive-safe
design audit. It excludes generated and private paths, including `.git`,
`node_modules`, build outputs, audit artifacts and `.env*`. A symlink in the
retained source stays visible to `check-package-source.mjs`, which rejects it
before the frontend install/build phase; filtering must not conceal an external
reference. Fixed-output dependency fetching is a separate build prerequisite.
The frontend also runs the design audit on the actual Gitless derivation source
before building.

The frontend build selects `VITE_RUNTIME_MODE=bff`. Its installed public root
contains only `index.html`, `favicon.png`, schema-1 `build-info.json` and
compiled `assets/`. Vite's copied `config.local.js.example` is deliberately
excluded. The BFF installs only its reviewed own runtime modules,
`package.json`, production `node_modules`, a pinned slim-Node executable wrapper
and separate metadata under `share/vpsadmin-webui-bff/build-info.json`. It
includes the credential reader code but no credential file or secret value. It
does not run npm or build source at service start. The package-content check
rejects extra public files, source maps, missing runtime imports/dependencies
and mismatched metadata. A real closure check is still needed before claiming
that no shell or full Node toolchain is present at runtime.

One flake provenance value is passed to both derivations. A clean Git-backed
flake revision produces a full 40-character commit and `dirty: false`. A
recognized dirty revision keeps that commit with `dirty: true`. A source without
a trustworthy revision records `unknown`, `dirty: true` and
`source: unavailable`. The frontend build receives both `VITE_BUILD_SHA` and
`VITE_BUILD_DIRTY`, so loss of `.git` cannot turn dirty or unknown source into a
clean release. Both metadata files retain the schema-1 fields `schemaVersion`,
`commit`, `shortCommit`, `dirty` and `source`; clean release acceptance requires
matching full commits and false dirty flags.

## Verification and deployment boundary

```sh
nix build .#frontend .#bff
nix build .#checks.x86_64-linux.provenance
nix build .#checks.x86_64-linux.source-contents
nix build .#checks.x86_64-linux.package-contents
```

The source check rejects missing audit inputs, generated/private files and
symlinks. The package check builds both outputs and checks their installed
contents together. Local Node fixtures and Nix syntax checks cover the checker
and provenance logic without claiming a successful Nix build. Verify the
package results on the exact candidate before enabling the NixOS module.
Roll back the frontend and BFF as a matching pair; retain the session
store and signing secret so an application rollback does not destroy sessions.
The existing `/config.json`, `/config.js`, `/session.json` and OAuth contracts
remain the runtime interface.
