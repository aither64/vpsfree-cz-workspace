
## Released generated client adoption (2026-11-03)

The root now selects published `vpsadmin-typescript-client@0.3.0` from the npm
registry with its exact URL and SHA-512 integrity. The release archive has
SHA-256 `57236647f4065a0ffeaabb0f5f6c64370a5ca4e7e530876b0d562c69651ce610`.
All 1360 files installed by ordinary `npm ci` match the verified release archive,
including all 1352 distributed JavaScript and declaration files that are
byte-identical to the tested `99ee0665` candidate. Public exports, the API schema
and 675 generated ownership hashes are unchanged. The public `createClient`
entrypoint loads and resolves its exact `haveapi-client@0.32.0` peer.

The released source is `d354491537f8b654b4d2c33a705cad84474f95d6`, generated with
HaveAPI `1ef9b204ba45bb261d3334be5c555cc1856b713b` and API capture
`5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5`. Generator/Ruby version `0.32.2`
is distinct from the npm runtime peer. Inspected npm-reported provenance binds
the source/tag and archive digest to release run 41538988296; independent
Sigstore signature verification was not performed. Program-byte equality does
not equate these newer source/provenance identities to the earlier candidate or
relabel earlier browser and isolated-API executions.

The committed candidate archive, compact provenance and archive-only source
checks/Nix cache adapter are removed. The frontend uses ordinary
`buildNpmPackage` dependency fetching with the prefetched hash
`sha256-e/oJZ1x+TRpjIw1DhoTLCJiQ2ifm4VednmrI201+ayQ=`. The lock changes only the
root client selector and client package record; all 484 unrelated records,
HaveAPI/XHR provenance, BFF dependencies/hash and flake/API/localization pins are
unchanged. The original strict baseline, sourceRevision, compiler options and
141 checked / 141 deferred membership are unchanged. The standard optional
local build/pack/no-save override and `npm ci` restoration remain documented.

The dependency install/prefetch batch passed in 93.806 seconds. Affected checks
passed against the installed registry release: 6 source-checker tests, 100
policy/wire tests in 6 files, application/tooling strict checks and the combined
E2E strict gate with 141 checked and 141 deferred. Scoped ESLint/format and Nix
syntax checks passed; this quick batch took 83.942 seconds. npm reported 12
moderate advisories, and prefetch retained the six known bundled WASI dependency
warnings; no unrelated dependency repair was attempted. No production code,
persisted format or database migration changes are introduced.

Independent affected review, exact-final-head Nix packaging and the requested
session preview remain pending at this commit. No repeated full browser matrix
or isolated-API run is claimed for this distribution-only transition. Subsequent
review/build/preview results belong in session and PR evidence. This adopts an
existing registry release; it does not publish a client, integrate a default
branch or deploy production services.
