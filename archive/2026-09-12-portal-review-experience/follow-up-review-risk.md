# Follow-up risk and compatibility review

Lane: risk and compatibility
Risk: High
Reviewer: `gpt-5.6-sol`, `xhigh`
Review date: 2026-09-12

Reviewed the complete committed series and final trees at:

- `codex-web` `83770217d63f2c206689d2c569e1c81950544504..de83e9c72dec6cb5ff8ec13d5b0b21ed60148117`
- `dev-workspace` `d3bfd0f5a7c419c9df0ed53aa5f1acb77f8e10c2..ebc0e4a71b01e81d0d90a29b0ca7385a61b1bdd1`
- `vpsfree-dev-workspace` `a30de6c62d2bcd1ff41ee48018c595140c6d4042..534d0f2c5530bbbbf36d8254d282a9945cef9bfc`
- workspace `5dbe312b1edf6a4454c4e86ec06f68baa3b5f4b4..77ca31a5e3e5e4f44c907b34b0f30bd99aec6980`

The review used the documented trust boundary: the local workspace operator is
trusted to administer the host, while browser clients, request parameters and
repository content remain untrusted. I inspected the local `AGENTS.md` files,
commit sequence, native Git argument construction, persisted descriptor and
saved-pair formats, session/repository scope binding, request and subprocess
admission, immutable caches, browser URL restoration, worker/CSP packaging,
focused tests, and the exact downstream Nix pins.

## Findings

### Advisory — Durable review descriptors have no aggregate retention bound

- File: `portal/internal/web/repository_comparisons.go:160`
- Commit: `b924a157043b7c3535cccde514d63fad52cbffdb`

`saveReview` creates one permanent file for every distinct scoped comparison
pair. The 8 KiB per-record limit and content-derived identifier prevent repeated
requests for the same pair from multiplying files, but neither this service nor
the session archive, revive or delete paths retire descriptors. A branch that is
reviewed after many head changes therefore grows private portal state forever;
deleted or replaced sessions invalidate their links through the scope check but
leave their records behind. Remote clients cannot create new pairs without a
corresponding local branch change, so this is not an immediate denial-of-service
path across the documented boundary. It is a long-term availability and stale
metadata retention risk. Add a documented retention policy or an ownership-aware
garbage collector that preserves active/archive/recovery semantics.

No Blocking or Important findings were found.

## Security and data-safety assessment

- Every repository request is resolved through the requested session and a
  registered or freshly verified discovered repository. Snapshot handles bind
  the session slug, repository ID and scope; durable descriptors additionally
  bind tracking-directory device/inode identity, thread ID and repository
  registration. Archive rename preserves that identity, while replacement or
  registration changes fail closed.
- Durable URLs carry opaque identifiers and full object IDs, but do not grant
  authority by themselves. Descriptor canonicalization and hashing prevent a
  modified record from selecting another pair. A requested commit must be
  reachable from the frozen head and absent from the frozen base. A requested
  file must match an ID issued by the reconstructed exact diff.
- Git receives only verified canonical repository directories and validated
  full object IDs. No browser path, mutable ref or command fragment becomes a
  Git argument. Replacement objects, lazy fetch, global/system configuration,
  external diffs and text conversions are disabled. Output, time, file-count,
  blob-size, line-count, request, subprocess and batch concurrency are bounded;
  cancellation includes admission and coalesced work stops after its last
  waiter leaves.
- Cache entries contain immutable Git-derived values rather than authorization
  decisions. Callers must pass session/repository/scope checks before reaching
  shared entries, so cross-session cache reuse does not widen access.
- Commit messages, paths and source are rendered as text or CodeMirror documents.
  Syntax highlighting returns validated palette indices and ranges from a
  same-origin bounded worker; it does not return repository-controlled markup or
  CSS. The packaged build has no runtime imports or WASM engine, and CodeMirror
  receives the response-specific CSP style nonce.
- Accepted message receipts remain hidden only after the transcript contains
  both the exact client message ID and the SHA-256 digest of the same
  `TrimSpace`-normalized UTF-8 message. Observation and server acknowledgement
  remain separate, and queued-message deletion behavior is unchanged.

## Compatibility and deployment assessment

- Existing single GET endpoints and the comparison POST contract remain
  available. New batch/restore GET endpoints and response fields are additive.
  The old comparison GET behavior remains `405` when no durable review ID is
  present.
- Schema-1 review descriptors live below private portal state, separate from
  session manifests, lifecycle journals, creation receipts and saved comparison
  records. An old package ignores them and continues to read canonical state.
  While rolled back, the old UI cannot open the new durable URLs; roll-forward
  recovers them if their Git objects and scoped session identity still exist.
- The browser/backend/provider unit is coherent: conversation JS/CSS use cache
  version 4, `dev-workspace` pins the same `codex-web` revision in Go and Nix,
  the packaged editor and worker are copied into the portal output, and the
  organization and workspace flakes pin the exact runtime and provider heads.
  The atomic user-profile package avoids a mixed old/new asset deployment.
- The recorded rollout order, provider then runtime then organization then
  workspace profile, is sufficient. No database, canonical manifest, journal,
  Codex protocol, cluster generation, system configuration or public-origin
  migration is introduced. Rollback does not need to interpret or mutate the
  additive descriptor files.

## Residual risks and verification gaps

- Long Nix package/VM checks, a live backend-to-browser acceptance run and the
  follow-up profile deployment remain intentionally deferred until review
  reconciliation.
- A real idle-workspace old/new profile rollback has not yet been exercised for
  this follow-up. Structural and focused tests cover the additive-state boundary,
  but they do not replace that deployment check.
- Durable links intentionally do not fetch or retain Git objects. Garbage
  collection, repository removal or object loss can make a link unavailable;
  the implementation fails explicitly rather than changing revisions.
- Descriptor tests cover process restart and atomic file replacement. They do
  not simulate abrupt host power loss during first-time nested-directory
  creation, so crash persistence of the newly acknowledged link remains an
  operational gap.
- The Chromium component acceptance uses bounded mocked API data. The focused Go
  tests separately cover real Git parsing, restoration, unusual filenames,
  cancellation and scope changes; the deferred live run should exercise those
  layers together.
