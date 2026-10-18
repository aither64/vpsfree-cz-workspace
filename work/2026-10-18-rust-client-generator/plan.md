# 2026-10-18-rust-client-generator

## Goal

I'd like to create haveapi client generator for rust. similar to how we have generator for golang, except in idiomatic rust. it would generate a client for given API version. as part of this work, we'd create vpsadmin-rust-client, similar to how we have vpsadmin-go-client. suggest a solution and create an implementation plan.

## Scope of this turn

Investigate the existing Go implementation, recommend an idiomatic Rust
equivalent, and prepare an implementation plan. Application implementation,
repository creation, package publication and integration are future work.

## Affected repositories

- `haveapi`: proposed Rust client runtime and metadata-driven generator.
- `vpsadmin-rust-client`: proposed new generated client repository/crate.
- `vpsadmin-go-client`: read-only reference for generation and releases.
- `vpsadmin`: read-only source of versioned API metadata and protocol behavior;
  include changes only if investigation establishes a necessary metadata gap.

## Approach

The retained architect (`architect0`, Astra/xhigh, workspace-write) owns source
investigation and `design.md`. The lead owns scope, acceptance, this plan,
state and the user-facing proposal. Implementers and reviewer are unassigned
for this planning-only request. Implementation packages will identify owners,
interfaces, dependencies, acceptance criteria and checks before coding starts.

Investigate generator inputs, requested-version selection, request and response
envelopes, authentication, pagination and asynchronous HaveAPI operations.
Choose Rust type mappings and public APIs from those contracts. Define a
reproducible generation and release workflow for a selected API version.

## Decisions

- Preserve the HaveAPI wire protocol and existing language clients.
- Prefer generated static Rust types/methods for one explicit API version.
- Reuse Ruby and HaveAPI's existing metadata client for generation initially;
  emit Rust rather than introducing a second metadata-discovery implementation.
- Share a hand-written Rust runtime across generated APIs instead of copying
  transport and authentication code into each generated client.
- Start async-only, using Tokio/reqwest, Serde models, and generated fluent
  action builders. Defer a blocking facade and browser OAuth2 orchestration.
- Support Basic, existing HaveAPI tokens and existing OAuth2 tokens, plus
  explicit generated token lifecycle/challenge actions. Keep vpsAdmin TOTP and
  password-reset steps explicit; avoid hidden refresh loops or mutation retries.
- Keep absent, explicit null and concrete input values distinct. Represent
  ordinary output fields as optional because permissions can remove fields.
  Preserve strict response-envelope validation. Use JSON values for `Custom`
  data and partial association results rather than assuming complete objects.
- Request and verify a specific API version; do not silently fall back to the
  server default. Only the API version selects the generated API contract;
  vpsAdmin application releases are irrelevant. Crate SemVer independently
  versions the Rust library. Use the requested API version (for example `7.0`)
  in generation inputs, constants and compatibility claims.
- Treat generation-time metadata as permission-dependent. A selected API version
  alone is not sufficient provenance: save the schema and its digest, and define
  what credentials/roles produced its supported surface without saving secrets.
- The accepted proposed architecture, file boundaries, evidence and verification
  brief are in [design.md](design.md). Material deviations return to the lead.

## Proposed execution sequence

These are future packages, not active implementation assignments. The architect
brief names exact file boundaries and proposed public runtime interfaces.

| Package | Proposed owner | Expected result and acceptance | Dependencies/checks |
| --- | --- | --- | --- |
| P0: contracts and fixtures | architect0 with future implementers | Frozen runtime/generator interface, API 7.0 capture profile, names and toolchain pins | Source-backed design; representative versioned schemas and explicit unsupported metadata diagnostics |
| P1: Rust runtime | implementer0 | Shared transport/auth/errors/metadata with omitted/null/value support | P0; owned `clients/rust/runtime/**`; focused quick unit/HTTP checks, formatting |
| P1: Rust generator | implementer1 | Explicit-version fetch plus deterministic offline generate/check | P0; owned Ruby/templates/specs under `clients/rust`; quick fixture specs and snapshots; parallel with runtime |
| P2: protocol integration fixtures | implementer1, runtime fixes by implementer0 | Generated fixture crates and HaveAPI test-server scenarios, no silently dropped types | Both P1 lanes; author tests here, execute long/uncertain compilation and integration after final review |
| P2: generated vpsAdmin crate | implementer0 | New repository, selected API 7.0 snapshot, typed generated source and compiling examples | P1 contracts and reviewed snapshot/profile; full described action inventory; longer compilation after review |
| P3: tooling, releases and docs | implementer1 in HaveAPI; implementer0 in new client | Pinned Nix environment, CI, reproducible regeneration and explicit release tasks | P2; quick checks first; longer package/MSRV checks after review |
| Final: review and verification | reviewer0, implementers, utility watcher | Reviewed committed deliverable, then longer integration/smoke checks and readiness evidence | All code/tests/docs committed and quick checks passing; complete branch/history/migration inventory; final review before long tests |

The lead coordinates overlapping edits and commits in HaveAPI, accepts package
reports, and keeps records. Each implementer owns follow-up fixes in its package.
Publication and default-branch integration follow the applicable authorization
gates; planning does not execute either operation.

## Compatibility and deployment

The intended work adds a new consumer. No database migration, persistent-state
conversion, daemon protocol change, configuration rollout or coordinated node
update is expected. The design must separate crate versions, generator/runtime
versions and API versions, define behavior with compatible server additions,
and preserve rollback by retaining older client releases and metadata inputs.
Do not require a server deployment unless a concrete metadata defect is found.
The investigation found no required server change for the initial client.
Preserve metadata-defined global authentication routes even when they live
outside the selected version's URL prefix. Permission-filtered metadata cannot
prove API-wide completeness: document the schema-export role/context, compare
expected actions, and make unsupported descriptions fail with useful diagnostics.

Older/newer servers must still offer the selected API version. Tolerate unknown
response fields and absent authorized outputs without weakening required input
validation. Richer schema typing and a general full-schema export are separate
future work if existing metadata cannot supply them.

## Documentation

Readers: implementers, HaveAPI maintainers and Rust client consumers. Planning
artifacts live here; lasting generator/runtime contracts belong in HaveAPI and
usage/regeneration/release instructions belong in the new client repository
during implementation. Register the finished design and plan in the portal.

## Testing plan

This turn checks source evidence, plan completeness, document links and scoped
tracking diffs. No application build or integration test is needed for planning.
The design must specify fixture tests, compile checks, HTTP protocol tests,
deterministic regeneration, full vpsAdmin schema generation and later live
smoke tests. Independent final review follows committed implementation and
quick checks, before long integration tests; routine planning is exempt.

## Investigation evidence

The architect inspected canonical bare repository HEADs, without borrowing
another initiative's checkout:

- HaveAPI `1e475d2e`: Ruby/ERB Go generator consumes OPTIONS metadata through
  the Ruby client; generated Go clients embed runtime code.
- vpsadmin-go-client `45a5170b`: reference API/client layout and generation;
  inspected tree has no release workflows and its instructions use live/default
  generation, so Rust needs an explicit reproducibility policy.
- vpsAdmin `b4ef8535`: API versions, authentication steps and output filtering.

Detailed source paths and official Rust references belong in the architect's
[design and verification brief](design.md). These are inspected local revisions,
not a claim to have fetched or tested the current upstream default branches.
