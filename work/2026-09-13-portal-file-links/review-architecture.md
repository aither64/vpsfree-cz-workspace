# Architecture and repetition review

Reviewed the complete committed ranges from the review packet, including the
provider implementation at `6735370851447ec62f6fbce25175c21db97c4686` and
the three exact dependency-pin commits. I also inspected each repository's
local `AGENTS.md`, the existing repository-review and artifact boundaries, the
shared editor, tests, packaging, and the current consumers of `mkPackage` and
`nixosModules.host`.

## Findings

### Important — The source viewer applies the repository path contract to curated artifacts

Commit `6735370851447ec62f6fbce25175c21db97c4686` applies
`repository.ValidSourcePath` before distinguishing a worktree path from a
tracking artifact, and applies it again to the `artifact` query
(`portal/internal/web/source_files.go:53-55`, `portal/internal/web/source_files.go:106-110`).
That validator owns repository-specific rules, including rejection of a `.git`
component, backslashes, control characters, non-canonical spelling, and paths
longer than 4096 bytes (`portal/internal/repository/source.go:24-34`). The
authoritative artifact registry has a different existing contract: manifest
validation accepts any confined relative path and `OpenArtifact` authorizes the
cleaned path against that catalog (`portal/internal/session/manifest.go:198-215`,
`portal/internal/session/manifest.go:672-696`).

This creates two independent artifact path policies. For example, a declared
artifact at `reports/.git/notes.md` is valid, remains selectable and readable
through the existing artifact preview/download path, but its absolute Markdown
link is not rewritten and a direct source-viewer query is rejected. Future
changes to either validator can create more silent mismatches. That violates the
stated interface that built-in and explicitly registered artifacts are the
viewer capability boundary.

Make the session/artifact owner expose one artifact path normalization and
validation contract, and use that contract in link rewriting, query parsing,
manifest validation, and opening. Apply `ValidSourcePath` only to the
repository-relative path. If the intended public contract is instead to narrow
artifact names, enforce that restriction when manifests are loaded and record
the compatibility effect, so artifacts cannot be accepted by one interface and
rejected by another.

### Advisory — Source provenance is a scattered string contract with a misleading default

The four public provenance values are introduced as literals in the repository
reader and web artifact branch (`portal/internal/repository/source.go:40-49`,
`portal/internal/web/source_files.go:152-155`), documented separately, and
interpreted in the browser with every unknown value treated as a current session
artifact (`portal/internal/web/static/source-file.js:13-19`). A future source
kind or a spelling mistake can therefore produce a plausible but incorrect
provenance label, which is especially confusing when the label is meant to tell
the reviewer whether bytes are live or tied to an archived commit.

Use named backend constants (or a typed enum) and handle all four values
explicitly in the browser. Unknown values should report unavailable/unknown
provenance rather than silently claiming a current artifact. Keep a browser/API
contract test that enumerates the complete set.

## Residual validation

The provider owns the capability and the consumer updates preserve the existing
generic -> organization -> user package and generic host-module dependency
directions. The editor extension is backward compatible for its existing
repository-review consumer and reuses the established preview classifier. No
additional architecture or repetition findings were found. Manual browser
checks remain useful for the editor's scroll/highlight behavior, but they do not
change the findings above.
