# Generated-client synchronization proposal

Phase 1 is complete: Go 0.2.0, Rust 0.2.0 and TypeScript 0.4.0 were integrated,
tagged and verified publicly available. See [Go](go-release.md),
[Rust](rust-release.md) and [publication evidence](release-observation.md).
The lead delivered the final release handoff. Phase 2 now implements only the
procedural documentation below; the WebUI WIP merge remains user-owned.
Architect0 owns this brief; repository owners are listed in the Phase 2 table.
The lead coordinates integration under the user's current condition: remaining
changes may merge **when the TypeScript/WebUI migration session finishes**.
That condition is not presently satisfied by this design or an earlier peer
completion message; the user reports that migration work is still broken/active.
The original investigation evidence is in [Go](go-evidence.md),
[Rust](rust-evidence.md) and [TypeScript](typescript-evidence.md) evidence;
implementer3 supplied the WebUI dependency check to the lead.

## Original investigation findings

SSH default refs inspected during the original investigation through canonical
bare repositories; refresh them before future execution:

| Repository | Default | Exact head |
| --- | --- | --- |
| vpsadmin | master | `942c6eaed41331f823d8e0f670ed239e2b308440` |
| haveapi | master | `f29c1e4675bc1f79641faa619b8c68ecec923c71` |
| vpsadmin-go-client | master | `134a9e69f9aa6ddec5c94b53744865c6f81ecdd0` |
| vpsadmin-rust-client | main | `3ec8c045dcefcca85b60ffccd38259cda29eeb60` |
| vpsadmin-typescript-client | main | `d354491537f8b654b4d2c33a705cad84474f95d6` |
| vpsadmin-webui | main | `1c8478bceb3943645ec06ccde895ee4b0985873f` |

**All three generated clients needed regeneration at those inspected heads.** API commit
`8225229aa0e3306f8b1723c5583969a33c64571c`, already in the inspected default,
adds `SecurityAdvisory#Retract` and `#Delete` at
`api/lib/vpsadmin/api/resources/security_advisory.rb:415,440`. All three clients
lack those actions and the new optional `expected_state` input on advisory
Update and CVE/node-status Create/Update/Delete. TypeScript also rejects unknown
input keys before dispatch, so a type assertion does not supply this guard.

Go records an October 30 public API capture and HaveAPI 0.32.0, without a saved
schema or exact source receipt. Rust retains that day's public live schema;
plugin completeness and API source SHA are unknown. TypeScript already uses a
full-fixture export from API `5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5`.
Rust/TypeScript pin generator source
`1ef9b204ba45bb261d3334be5c555cc1856b713b` and have saved-input consistency
checks; these do not establish freshness against current API source. Versions
identify different components: exporter gems are 0.32.2, TypeScript runtime is
0.32.0, and the inspected HaveAPI master still declares Go generator 0.32.0.
Use exact revisions and input hashes, not version-number inference.

## Phase 1: completed refresh and releases

The following input/design notes retain the execution contract and its rationale;
the verified release receipts above supersede candidate-status wording.

First refresh, check, independently review and update the Go, Rust and TypeScript
clients, then release updated versions using each repository's release
conventions. Verify current default heads, tags and published package versions
before choosing versions or preparing releases. TypeScript defaults to a new
minor version unless the user explicitly specifies otherwise: the recorded
package version is 0.3.0, making 0.4.0 a candidate, not a verified next release.
Choose final Go/Rust versions under their own conventions; execution candidates
and their limits are recorded below.

### Stable execution inputs and file boundaries

Refreshed SSH HEAD/fetch checks confirm API master
`942c6eaed41331f823d8e0f670ed239e2b308440` and HaveAPI master
`f29c1e4675bc1f79641faa619b8c68ecec923c71`. Use the existing proven generator
revision **`1ef9b204ba45bb261d3334be5c555cc1856b713b`** for all clients.
Across `clients/{go,rust,typescript,ruby}` and `VERSION`, its diff against the
fresh HaveAPI master contains only eight version/gemspec declarations, with no
generator/runtime/shared-schema implementation changes. At this chosen revision
the Go version file declares 0.32.2; the originally inspected master declares
0.32.0. Neither value substitutes for the exact source identity. The API exporter
separately pins its installed HaveAPI gem to 0.32.2.
The chosen generator commit is **not an ancestor** of HaveAPI master
(`merge-base --is-ancestor` returned 1). Retain this honest source-dependency
lineage. Source retention/completion handling remains an explicit lead-owned
obligation; no fake merge, unregistration or ref repointing establishes completion.

Implementer3 owns the session's `vpsadmin` and `haveapi` source worktrees under
`worktrees/2026-11-03-vpsadmin-client-sync/`, at the exact API and generator
revisions above. Keep tracked source unchanged. Shared export paths, relative to
this tracking directory, are `source-inputs/api-7.0/schema.json`,
`provenance.json` and `tooling.Gemfile.lock`; a second independent fresh-database
export goes to `source-inputs/api-7.0-repeat/`. The export is now accepted for
client generation; [source-inputs.md](source-inputs.md) retains the full receipt.
Architect0 independently recomputed these hashes and confirmed the repeat matches
all three files byte for byte:

| Shared artifact | Accepted SHA256 |
| --- | --- |
| `schema.json` | `d6ec617653913c56e92398a6032aa350118597a0e3f45c599bc92b6071ea0a26` |
| `provenance.json` | `c85815abd315f53a5ef05f324abe377760293786a13a25b7a127ec804c50e0c1` |
| `tooling.Gemfile.lock` | `62a0e7f65e0755296ea50e3f5efa590f51e8615571a078cf45243f6ca8555f1c` |

The receipt reports 14 passing database-free examples and both fresh-database
exports passing. Inventory is 151 resources, 521 actions and 8,760 parameters;
the required advisory actions and state guards passed the owner's assertions.
This accepts source input, not regenerated clients, releases or deployment.

The shared contract is format 1, API 7.0, protocol 2.0, mount `/`, English,
profile `vpsadmin-full-fixture`, synthetic source URL
`https://schema.invalid/v7.0/`, and bundled plugins monitoring, newslog,
outage_reports, payments, requests and webui. Preserve identical raw schema bytes
across all three clients; Go uses only the explicit transport projection below
for generation. Require Retract/Delete and `expected_state` on all seven
previously identified mutation inputs. Go/Rust must explicitly migrate from
public-capture provenance; do not describe the source fixture as a live capture.

| Owner | Client-owned inputs and implementation boundary |
| --- | --- |
| implementer0, Go | Retain raw `schema/source-api-7.0.json`, derive effective `schema/api-7.0.json` using the approved projection below, and retain raw `schema/provenance.json`, exporter `schema/tooling.Gemfile.lock`, and minimal generator receipt/lock at `schema/generator.json` and `schema/generator.Gemfile.lock`. Generate a fresh module with module `github.com/vpsfreecz/vpsadmin-go-client`, package `client`; reconcile generated files/removals while preserving handwritten files and `go.mod`. No new CI subsystem. |
| implementer1, Rust | Replace `schema/api-7.0.json`; retain raw exporter receipt as `schema/source-provenance.json` and exporter lock as `schema/tooling.Gemfile.lock`. Update existing `schema/provenance.json`/inventory/checker for mounted-source acquisition while preserving generator/runtime evidence and `schema/generator.Gemfile.lock`. Own `src/generated`, existing checks and release metadata. |
| implementer2, TypeScript | Update existing `schema/schema.json`, raw `schema/provenance.json`, exporter lock and `tools/generator.json` hashes; own `src/generated`, bounded consumer checks and release metadata. Retain generator revision and `haveapi-client` runtime 0.32.0. Calculate final tooling hashes after version/package-lock changes. |

Owners may compute generator/shared/runtime identity digests with existing
helpers once the source checkout is ready. Keep each client's pinned toolchain:
Rust's Ruby 3.3.10, Bundler and rustfmt graph is distinct from exporter tooling.
Coordinate ignored component dependency files under `clients/go` and
`clients/rust` with implementer3; use isolated bundle paths and never overwrite
shared root Bundler configuration or another component's bundle. TypeScript uses
its existing source helper and pinned client toolchain. No generator source edits
are planned; report any actual blocker before changing the shared source contract.

Fresh owner checks found current Go/Rust releases 0.1.0 and TypeScript 0.3.0.
Recommend Go/Rust **0.2.0**, subject to their complete generated diff and release
conventions; TypeScript **0.4.0** follows the user's minor default and is absent
from the checked registry/tags. These are release candidates, not published
versions. Owners must assess all removals/type changes and compatibility from
the actual output; representative investigation alone cannot settle that verdict.

### Go OAuth fixture compatibility exception

Lead accepted this bounded revision after implementer0 identified a concrete
regression. The exporter seeds `core.api_url` as `http://api.test`, so raw OAuth
metadata uses `http://api.test/_auth/oauth2/revoke`. The Go generator embeds that
absolute URL, and its preserved origin validator would reject it against a
production client origin. The existing shipped client instead uses
`https://auth.vpsfree.cz/_auth/oauth2/revoke`; Rust/TypeScript do not require this
projection.

Implementer0 owns a small deterministic `tools/prepare-schema` helper, its
focused tests, provenance/docs and normal generated output. Preserve the raw
export and source receipt verbatim. Derive the effective generation schema by
changing **only** `description.authentication.oauth2.revoke_url` from the exact
fixture URL above to the existing HTTPS production URL. Fail on unexpected format,
API/protocol version, fixture profile or old URL. Record the exact field path,
old/new values and raw/effective SHA256 hashes in the generator receipt. No
generic transformation framework, manual generated-source edits, generator
changes or trust-policy relaxations are authorized by this exception.

Focused acceptance: raw bytes stay unchanged; parsed schemas differ only at the
one declared field; repeat preparation is deterministic; unexpected input is
rejected. Verify emitted Go retains the intended endpoint, untrusted cross-origin
revocation fails before dispatch, and explicit existing `AllowOAuth2Origin`
permits the correct HTTPS endpoint through a local HTTP transport stub. Preserve
the existing authentication-clear-on-success behavior. Include this projection
and the retained production endpoint in independent review's compatibility/risk
scope. This preserves current Go deployment behavior; it does not certify a live
production endpoint or make a generic multi-deployment OAuth discovery claim.

The user confirms that generated TypeScript-client adoption in WebUI is work in
progress and will merge it once the updated releases are available. That WIP
merge remains user-owned; this plan does not inspect or modify it. Phase 1
finishes with verified available releases and their exact source/artifact
identities, before introducing the rules in Phase 2. Integration and publication
retain their respective authorization requirements.

Reuse `tools/export-api-schema`: it exports API 7.0 from clean committed source,
all six bundled plugins and a disposable MariaDB fixture, with schema/input
provenance and pinned exporter dependencies. It needs no deployed API or cluster.
Use the same reviewed full-fixture contract for all three clients; moving Go and
Rust from public capture is an explicit profile/provenance change. Pin the
chosen generator source separately. HaveAPI provides
`clients/{go,rust,typescript}/bin/haveapi-<language>-client generate --schema ...`.
Rust/TypeScript already wrap generation with `tools/regenerate` and `--check`.
Go needs fresh-directory generation and a generated-file-set comparison,
including removed files: its generator has neither `--check` nor stale-file
deletion. Preserve handwritten files and package metadata.

## Phase 2: institute future synchronization rules

After the client releases, make synchronization part of **API-task completion**:
every API change must assess Go, Rust and TypeScript; changes affecting exported
contracts or generator output require updated clients, while behavior-only
changes may record a source-tied no-generated-change result. Complete the task
only after all changed client heads are integrated into their defaults, or each
unchanged client has documented no-op evidence. Future ordinary synchronization
alone requires no version bump, tag or publication; the conditional TypeScript
release requirement below applies when WebUI needs new support.

Put the authoritative procedure in vpsAdmin's existing
`docs/api-schema-export.md`, routed from its `AGENTS.md`; link client contributor
guides and this site's workspace verification routing to it. Workspace project/routing
guidance should include Rust and TypeScript alongside Go. Initially this is an
explicit contributor/agent rule with task evidence, not a claimed CI guarantee.

### User-corrected repository boundary

The user rejected vpsAdmin-specific guidance in generic HaveAPI documentation as
a separation violation. Owner1 is removing the sole unmerged HaveAPI guidance
commit; there is no replacement change in HaveAPI. Keep downstream policy in
vpsAdmin and site coordination, without imposing it on the generic framework.

No additional site-extension feature is necessary. The existing candidate
workspace `docs/agent-instructions/verification.md#delivery-and-scope-checkpoints`
already routes "vpsAdmin API work and HaveAPI generator changes affecting
vpsAdmin clients" to the canonical procedure. That procedure records the chosen
generator, copied runtime and shared inputs, compares complete output, and
requires source-tied no-change evidence. It therefore supplies the needed
assessment path for generator/shared-schema/runtime changes affecting these
clients without another copy of the rule. Shared code changes that do not affect
these clients do not create a site-policy obligation in HaveAPI.

Decision: retain the existing vpsAdmin procedure and workspace routing; add no
files or feature work in `vpsfree-dev-workspace` (`git@github.com:vpsfreecz/dev-workspace.git`).
The extension is a permissible site-specific home if a concrete uncovered need
emerges later, but moving or duplicating sufficient routing now adds no benefit.
This reassessment edits only this design. Lead/owner1 reconcile the authorized
HaveAPI removal and existing final-review records; no new tests, builds,
deployment or integration authorization arise from this decision.

Prepare and check client candidates against the final API feature commit before
integration. With explicit approval for each repository/target, integrate
clients first where forward compatibility permits; otherwise integrate API then
clients in the same bounded approved batch. Do not require each repository's
source SHA to be on the other's default before either can merge. Cross-repository
updates are not atomic; failures leave the task incomplete with an owned next
action. A rebase or intervening contract change requires refreshed input proof.

### WebUI release gate and TypeScript version default

The user's added requirement is a separate pre-merge gate: a WebUI change using
new API support through `vpsadmin-typescript-client` must consume a **published
release containing that support** before merging WebUI main. Feature-branch,
Git or local dependencies are allowed during development; final manifest and lock
must resolve the released npm artifact, without temporary overrides. Record the
needed generated members, release version and resolved integrity. Integration and
publication still require their respective explicit authorization.
Default a TypeScript-client release to the next minor version; an explicit user
version override takes precedence. Verify the current release state at execution
time rather than treating today's candidate version as fixed.

The original investigation found no generated-client dependency on the then-inspected
WebUI main; it pinned transport `haveapi-client` 0.32.0. That observation does not
describe the user's separate WIP or establish today's adoption state. Add the rule to its `AGENTS.md`
maintainer/review boundaries and existing client design guide. Its
`scripts/check-package-source.mjs` already checks HaveAPI registry provenance;
extending it for the generated package is a small optional follow-up, not an
existing gate. Publication does not prove the API is deployed: deploy compatible
API support before enabling new calls, or capability-gate them during rollout.

### Phase 2 execution packages and acceptance

The canonical heading is `## Generated client synchronization` in vpsAdmin's
`docs/api-schema-export.md`, giving anchor `#generated-client-synchronization`.
External consumers use
`https://github.com/vpsfreecz/vpsadmin/blob/master/docs/api-schema-export.md#generated-client-synchronization`.
The canonical procedure owns the complete workflow; consumers add short scoped
requirements and links, not copies. All packages are documentation/instructions
only, with no runtime, test, script, workflow, configuration or version changes.

| Owner | Exact document boundary | Acceptance |
| --- | --- | --- |
| implementer3 | vpsAdmin `docs/api-schema-export.md` new canonical section and introduction; `AGENTS.md` Required procedures row | Assess all three clients for API work; update their defaults or retain source-tied no-output-change evidence before task completion. Explain raw/profile/generator provenance, owned transformations, client checks versus source freshness, release-free ordinary sync, conditional TS release/WebUI gate, minor default/override and bounded approved integration ordering. Preserve export safety instructions. |
| implementer0 | Go `README.md#development-and-regeneration`, `AGENTS.md#agent-specific-instructions`; workspace `docs/agent-instructions/projects.md` and `docs/agent-instructions/verification.md#delivery-and-scope-checkpoints` in a dedicated workspace feature worktree | Link Go regeneration/completion to the canonical procedure without changing commands. Add missing Rust/TS project entries and one workspace routing paragraph. No shared-master feature edits; separate logical commit in each repository. |
| implementer1 | Rust `docs/development.md#saved-schema` and, only as needed, `#compatibility-and-release-checks`; remove the rejected unmerged HaveAPI guidance under the lead's assignment | Rust links to the canonical procedure. No vpsAdmin-specific documentation or routing remains in HaveAPI from this initiative. No replacement extension feature or generator/source/version changes. |
| implementer2 | TypeScript `docs/development.md#schema-and-regeneration`, `docs/releasing.md` short version-selection paragraph; WebUI `AGENTS.md#deployment-and-review-boundaries`, `docs/design/HAVEAPI_CLIENT.md` scoped generated-client subsection and required dated `docs/work-log/` entry/index pointer | Distinguish transport from generated SDK. Dev feature/Git/local dependencies are allowed; dependent WebUI merge requires the published matching TS release and final registry manifest/lock/provenance, no temporary override. Default TS releases to next minor unless the user specifies otherwise. No WIP, application or dependency edits. |

Packages can draft independently against the fixed canonical anchor. Owner3
settles the canonical text before final consumer-link reconciliation. Authors
send prose drafts to the lead for the required main writing pass before commits.
Make one coherent documentation commit per repository; keep already released
history immutable. Do not mix separate repositories or unrelated changes, record
future hashes, or create an intermediate state inconsistent with its own inputs.

Quick acceptance: inspect the scoped diff, local links/anchors and repository
instructions; run whitespace and declared hooks. WebUI runs its required
`npm run audit:design-docs` for the design-guide edit. Check the canonical external
anchor against the candidate source before publication rather than accepting a
temporarily missing default-branch URL. Verify five scenarios in prose review:
schema change updates all clients; behavioral-only work records a justified no-op;
source sync alone does not force publication; dependent WebUI merge requires an
actually published artifact; TS defaults to minor with explicit override allowed.
Preserve explicit named-target integration approval and separate deployed-API
capability readiness. Run mandatory independent final documentation/history
review after all intended commits and quick checks; no long test/build batch for
these prose changes. Integration remains conditional on the user's migration
completion requirement above and requires the lead's fresh scope/state check.

### Superseded HaveAPI documentation transition and retained source

The earlier documentation transition was performed and recorded in
[phase2-rust-haveapi.md](phase2-rust-haveapi.md), but its HaveAPI guidance scope is
now withdrawn by the user. Preserve that historical evidence and the owner's
removal receipt; it is not an instruction to recreate or integrate the change.
The original `initial_base_sha` remains
`1ef9b204ba45bb261d3334be5c555cc1856b713b`. Its public `v0.32.2` source tag and
immutable detached checkout at
`worktrees/2026-11-03-vpsadmin-client-sync/haveapi-generator-0.32.2` preserve the
released clients' generator dependency. Do not alter original source/release
receipts or describe that nonancestor dependency as merged into HaveAPI master.
Lead/owner1 own reconciliation of the actual final registered head after the
authorized removal under the existing completion rules. This reassessment
authorizes no branch mutation, unregistration, lifecycle action or cleanup.

## Retained Phase 1 checks and compatibility

Quick checks: input identities, schema/action inventory, diff ownership and
existing formatter/provenance checks. Longer checks: isolated export plus repeat
for determinism, regeneration and language/consumer suites in their Nix shells;
use the required watcher for uncertain/long runs. Generator changes need their
own focused tests. Client-local reproducibility alone never proves API freshness.

No persisted state, database migration or coordinated node update is introduced.
Generated methods do not grant authorization; older servers may lack new methods
or parameters. Assess removals/type changes and generator/runtime pairing before
integration. Roll back schema, provenance, generator pin and generated tree
together; retain published artifacts and restore a compatible WebUI dependency.
The original investigation established representative source-contract drift;
later generation, review and release evidence belongs to the linked receipts.
Neither source generation nor publication alone proves production compatibility.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-vpsadmin-client-sync/)
