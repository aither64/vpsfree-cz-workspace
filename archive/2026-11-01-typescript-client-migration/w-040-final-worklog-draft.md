## Released client and current-main advisory integration (2026-11-03)

The migration now selects published `vpsadmin-typescript-client@0.4.0` with its
canonical registry URL and SHA-512 integrity. The verified 338234-byte archive
has SHA-256 `3a6f2a2a6f4eaeb31f490035b312e9b5403cf21589d649dc1fd31d60b64e1906`;
all 1364 installed files match it. The public source is `c53cb4dabb0b3aac8d05834478872d2cfa698fa7`,
generated with `1ef9b204` / Ruby `0.32.2` from API capture `942c6eae`.
The npm runtime peer remains exactly `haveapi-client@0.32.0`. Inspected npm-reported
provenance binds the release source/tag and archive; independent Sigstore
signature verification was not performed.

This release adds advisory Retract and Delete actions and `expected_state` on
seven existing guarded actions. Earlier `0.3.0` program-byte equality does not
extend to these additions. Delete accepts the generated empty
`security_advisory` output frame. State choices, reviewed revisions and live
capability checks remain application policy: every draft synchronization checks
all six CVE and node-status mutation actions before writing. Missing actions,
guard parameters or allowed state choices deny writes without omitting guards
or replaying accepted work. Guarded operations require backend `8225229a` or
independently equivalent live capabilities. The running preview's older API
remains unchanged and cannot certify this contract.

The feature was semantically rebased onto main `1c8478bc`, preserving upstream
correction, announcement, lifecycle and localization behavior. The migration
also covers new, nonconflicting main callers. Authenticated generated root and
object descriptions replace manual advisory endpoint descriptors; receipt
metadata uses the existing shared helper. Parent/child snapshots, exact child
identity, revision advancement, partial accepted progress and refusal after
uncertain read-back remain enforced. A missing or replaced child visibly
refuses deletion before confirmation. The superseded draft-only hook is removed;
its recovery tests exercise the active correction flow. The exact old `4ed519b6`
source and its original history remain retained for recovery; this semantic
successor does not relabel that deployed source as an ancestor.

The dependency/lock/hash stream uses one released selection with ordinary npm
fetching and frontend hash
`sha256-3H/bRfGSY5Mra3MkhjcgBSiP/NciqX0Q58K+zem/i9k=`. Unrelated root lock
records, BFF dependencies/hash and flake/API/localization pins are unchanged.
Strict coverage is 143 checked and 140 deferred, including the main contract
helper and complete advisory-outage spec. The original baseline, sourceRevision,
compiler options and all 140 surviving deferral records are preserved.

Application strict passed on the final source without diagnostics in 59.822
seconds. Tooling strict, the combined E2E strict gate and six source-checker tests
retain their successful unchanged-input executions. Failed advisory fixture and
snapshot checks were investigated, corrected and passed in affected Vitest
continuations. Scoped lint/format, documentation inventory/links, both catalogs,
structural budgets, API-barrel imports, Nix syntax and whitespace checks passed.
These are local source and synthetic-fixture checks, not a real backend or browser
certification of the new guarded operations. Independent final review, full CI,
exact-final-head Nix packaging and conditional integration remain pending.
No database or persisted-format migration, default-branch integration,
production deployment or preview update is claimed.
