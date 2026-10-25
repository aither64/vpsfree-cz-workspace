# Sat Oct 24 2026 - version 0.30.1
## Ruby server
- Simplify Go and Rust documentation profiles: configure the SDK import path or
  crate name, with optional SDK versions. The generator version defaults to the
  server version.
- Build example naming models from the complete mounted API declaration while
  keeping displayed actions, fields and samples filtered for the current user.
  Retain saved-schema profiles for older or restricted SDKs.

## Go client generator
- Show `go get IMPORT@latest` when no SDK module version is configured, leaving
  version resolution to Go when the user installs the SDK.
- Match resource association field identities across live Ruby descriptions and
  saved JSON descriptions.

## Rust client generator
- Allow documentation examples without a crate version or packaging TOML, and
  support an explicit HTTPS Git source with a full commit revision.
- Declare the Fiddle dependency needed by the generator and limit generated
  naming-lint allowances to the affected resource members.

## JavaScript and TypeScript clients
- Update TypeScript and Rollup build dependencies while preserving ES5 output
  and the public declarations.
- Fix build helper resolution and internal import cycles.
- Replace the obsolete JSDoc wrapper and template tools with direct JSDoc,
  preserve the documented Action anchor, and update its Markdown dependencies.

## Release tooling
- Confirm published package metadata and checksums with bounded reads, including
  delayed registry visibility. Preserve uploaded artifact identities during
  partial-publication recovery.
