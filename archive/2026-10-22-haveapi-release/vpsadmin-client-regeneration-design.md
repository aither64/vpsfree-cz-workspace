# vpsAdmin Rust client regeneration with the fixed HaveAPI generator

Architect0 execution brief, 2026-10-23. User authorized “okay, regenerate the
client”; this covers the saved-schema refresh on a development branch. It does
not authorize a schema fetch, crate version change, release, token/account setup,
default integration, deployment or lifecycle action. No HaveAPI registry release
is needed. Lead owns assignments, final review and verification launch.

## Exact baseline and input contract

Fresh SSH `refs/heads/main` on `git@github.com:vpsfreecz/vpsadmin-rust-client.git`
is `945af6a97717a7a6373507bbc9592d5cd53727c2`, tree
`c993cef64194e86bac41c073409d345846eecf8a`. Canonical-object reads, not another
session's worktree, supplied AGENTS, README, development/release guidance,
helpers, provenance, manifests and workflows. Implementer0 reports a new clean
registered worktree at
`worktrees/2026-10-22-haveapi-release/vpsadmin-rust-client`, branch
`2026-10-22-haveapi-release-regenerate-vpsadmin-client`, from that exact base.
Preparation receipt: `vpsadmin-client-preparation-20261023T182018Z`. No repository
hook framework is declared. Implementer0 retains sole Git/index ownership.

| Input | Retained value / change |
| --- | --- |
| Actual Cargo package/import | `vpsadmin-client` / `vpsadmin_client`; version **0.1.0 unchanged** |
| API/schema | API 7.0, protocol 2.0, profile `public-live-api-7.0`; no network capture |
| Snapshot SHA-256 | `70f89335e15263fd7177f29a00fab04b5ff1923c6922dfd318b07c3ae922fb8d` |
| Inventory file SHA-256 | `563b3472fe0ab03f9c8b0ecc4a5623a883efe43103060e3c6484c13bdbd474a1` |
| Coverage | 152 resources, 524 actions, 8720 parameters; existing public-only/plugin-unknown limits unchanged |
| Old generator SHA | `68cc80b012b7a6b9bcdf35c008c338cbc3f4c000` (0.29.0) |
| Fixed generator SHA | **`090a188cb4ef3477324718627f4ae3415d1c0975`** (0.30.0), tree `e9473d5453e014ff2b0da36d4bb21f0eab2eb7e2` |
| Public generator ref | Fresh SSH `2026-10-22-haveapi-release-followups` resolves to that SHA; pin SHA in provenance, not floating branch |
| New generator source digest | `ee40aeee00e25aac87d007c241b29b519c7c22ccf3c027c1372e867809312892` |
| New generator Ruby lock digest | `7f51e5ea00157f4d215355acec5d95c2a8bcbb7d4600c5b34f5e1a338acbc1e4` |
| Runtime digest, unchanged | `9c50b8167a8b82118ba42372633e3b004276ba49fbdfed75d4979a913feea739` |
| Downstream toolchain pin | nixpkgs `fe13242281a67641c0102cdb1087f0ebe586c7df`, NAR `sha256-zp8ToDMnqZcu4o4IH9pdwXFXGp7yLm/M0dEnNWnyd7I=`; retain flake.lock |
| Formatter / language | Exact **rustfmt 1.9.0**, edition 2024, MSRV 1.95; retain generator.toml and rustfmt.toml |
| Rust dependencies | Existing Cargo.toml/Cargo.lock unchanged; reqwest/Serde/url remain ordinary registry dependencies |

Digests above were reproduced read-only from canonical Git blobs using the
generator's path-NUL-bytes-NUL hashing rule. They are expected inputs, not a
regeneration success receipt. Lead reports HaveAPI 090a final review accepted
with no findings and eight local/seven CI checks passed. Preserve that source,
all follow-up/official artifacts and refs; do not amend it for this consumer.

## Source delta and expected output

Compared old 68cc to fixed 090a: generator.rb, IR, Naming, snapshot acquisition,
CLI and all eight runtime source files have no changes. The only Rust-rendering
template changes add a rationale comment and scoped `#[allow(non_snake_case)]`
at nested resource module declarations and corresponding Client accessors.
No route, method spelling, public type, field, validation, wire shape, auth or
transport change is expected.

The source digest also includes new `lib/haveapi/rust_client/documentation.rb`;
the offline generator loader does not load that adapter. The generator version
became 0.30.0 and the Ruby lock now records matching local HaveAPI gems plus the
explicit runtime `fiddle (~> 1.1, >= 1.1.8)` locked at 1.1.8. These are real
provenance differences beyond the generated lint attributes, not new crate
runtime dependencies. Preserve their exact hashes rather than labeling the
whole source pin patch-identical.

Expected generated file set: **50 modified files**, no added/deleted generated
paths: 48 `src/generated/resources/<name-with-__>/mod.rs`, the common
`src/generated/resources/mod.rs`, and `.haveapi-generated.json`. The manifest
still accounts for 686 output files. The 49 Rust files gain 96 scoped attributes
and 96 explanatory comments in total. After removing only those exact new
comment/attribute lines, all generated Rust should equal baseline byte-for-byte,
subject only to the exact common-module ordering clarification below.
All action files, generated API constants, ordinary resource modules and eight
runtime files must remain byte-equal without normalization. A different result
requires diagnosis through lead; never hand-correct generated output.

### Observed common-module ordering clarification, 2026-10-23

Lead accepted this exact exception on 2026-10-23.
The frozen generated candidate has one additional formatting difference in
`src/generated/resources/mod.rs`: `pub mod authentication__token__token;`
moves from baseline physical line 4 (third declaration) to the final declaration,
physical line 153 after removing the exact new comments/attributes. The file
contains the same **152 unique module declarations**. The other 151 declarations
retain their order; removing this one unique declaration from both normalized
files leaves byte-identical content. Do not sort either file or waive any other
reordering. Each declaration must occur exactly once and the named declaration
must occupy those exact positions. Preserve the module's scoped lint allowance.

The unchanged `clients/rust/lib/haveapi/rust_client/ir.rb` walks ordinary
resources before authentication resources. The owning `template/resources.rs.erb`
still emits that IR order; its only change is the comment/attribute pair for
names containing `__`. The unchanged generator requires rustfmt **1.9.0** and
invokes it with edition 2024 and `skip_children=true`; the downstream formatter
configuration specifies only edition 2024. The new output retains the template's
auth-last position. This is consistent with a comment/attribute boundary changing
formatter reorder groups; that internal mechanism has not been independently
proven. No formatter-internal source audit or extra formatter run was performed
by architect. Owner3's successful generation and
read-only regeneration check establish reproducibility with the pinned inputs.

This file consists of ordinary out-of-line module declarations, without
`macro_use` or execution/registration statements. The named auth module likewise
does not introduce textual macro scope. Moving its declaration changes source
location/order, not module identity, visibility, public paths, method/type names,
route dispatch or runtime initialization. No product fix or generated hand edit
is warranted. The candidate manifest SHA-256 independently reported by owner1 is
`07b37518b47fc0037abe2a38aa2eac8446b717c67274d53501e2c8924b13308f`.

Owner1 independently confirms the sole normalized difference, 50 changed
generated paths, 49 Rust files, 96 exact added attributes/comments, 686 valid
manifest hashes and unchanged schema/inventory/config/Cargo/runtime inputs.
Its final [surface crosscheck](vpsadmin-client-regeneration-surface-check.md)
and [full JSON evidence](vpsadmin-client-regeneration-surface-check.json) report
PASS with zero unexpected findings and preserve the original strict mismatch.
The frozen 53 changed files have path-NUL-bytes-NUL SHA-256
`3063e0b310f21e58b681c435422ab831058fb3e2e0732083f7517ad59b2827b0`.
Retain these receipts and the exact constrained comparison in the final review
packet; this evidence supports, rather than replaces, committed final review.
All other normalization and exact-byte rules remain unchanged. Existing
default/blocking, Rust1.95, docs, package and naming-lint gates remain sufficient;
this does not authorize an extra compiler campaign or a new source test fixture.

## Ownership and implementation packages

**Implementer0 — setup and sole Git.** Registration is reported complete. Preserve
the exact base and clean boundaries; serialize staging/commits/push and capture
comparison after final head. Do not change another worktree or source ref. Push
only this feature branch over canonical SSH after readiness gates. No merge to
main, release ref, workflow dispatch or cleanup is implied.

**Implementer3 — sole downstream source writer.** Own `schema/provenance.json`,
`flake.nix`, the narrowly related `docs/development.md` paragraph, and regeneration
of `src/generated/**`. Add **libffi only** to the existing downstream Nix shell:
its Ruby3.3/compiler/pkg-config already exist, but the new Fiddle native gem needs
libffi headers/libraries (demonstrated by the owning HaveAPI fix). Keep nixpkgs,
Rust/formatter, Ruby selection and Cargo inputs unchanged. If fresh setup reveals
another concrete incompatibility, report it rather than update toolchains/locks
or borrow an ambient bundle. No compiler execution is needed during this design.

Use the clean session-owned HaveAPI follow-up checkout at exact 090a as a
read-only generator source. CI already reads `schema/provenance.json`'s exact
revision and checks out that SHA; no new stable-ref creation or workflow edit is
needed. Set `HAVEAPI_SOURCE` to that verified root; reject a dirty/mismatched
generator before use. Do not let bundle setup modify HaveAPI's tracked lock or
local configuration. Use a dedicated Ruby3.3 bundle under the downstream ignored
`target/` directory with `BUNDLE_FROZEN=true`, `BUNDLE_PATH` and `BUNDLE_USER_HOME`
explicitly set there; do not reuse HaveAPI's Ruby3.4 native extension installation.
This setup is a bounded prerequisite once granted, not a long Cargo campaign.
No gem publication or `cargo login` occurs.

Regenerate only through `tools/regenerate`, then `tools/regenerate --check` in
the downstream pinned shell with the exact rustfmt 1.9.0. Keep `schema/api-7.0.json`,
`schema/inventory.json`, capture timestamps/profile/diagnostics/coverage,
generator.toml, Cargo files and handwritten Rust/examples/tests unchanged.
Update provenance's generator revision/version/source digest/Ruby-lock digest
to actual fixed-source/generated-manifest values; retain runtime digest and all
capture/toolchain facts when their inputs remain unchanged. Do not fabricate a
new capture or refresh provenance timestamps merely because generation ran.
Document the explicit native dependency, frozen bundle and formatter distinction
in the existing development guide; do not add a new release or CHANGELOG heading.
Existing tools need no functional changes for this bounded refresh.

**Implementer1 — independent read-only surface/input crosscheck.** After the
generated tree is available, compare exact base to candidate: schema/inventory
byte hashes, 686 manifest entries/all file hashes, the expected 50-path delta,
96 scoped attributes/comments, normalized Rust equality with only the explicit
common-module exception above, exact eight-runtime-file
equality, public names/routes/types and unchanged package/config/lock identity.
Independently reproduce new source and Ruby-lock digests from exact 090a. Save a
session evidence receipt only; no source/pin/generated file writes. This bounded
crosscheck supports final review and does not replace it. No additional API,
registry, CI polling, compilation or live acceptance campaign is needed here.

## Quick checks and commit purposes

Inside downstream pinned Nix shell, after isolated frozen Ruby setup:

```sh
bash -n tools/regenerate
tools/regenerate
tools/regenerate --check
tools/check-provenance
cargo fmt --all -- --check
```

The first regenerate is the authorized generated-source operation; the second
must be read-only, deterministic and leave no tracked diff. Also run the owning
read-only input/surface/hash checks and inspect package manifest requirements.
Do not compile or run local servers during quick checks. Retain command, tool,
source and result evidence; shell entry/dependency setup can be monitored through
the normal utility policy when uncertain, without broadening its scope.

Commit split is required by the downstream AGENTS:

1. Authored generator pin/provenance, native shell prerequisite and bounded
   development documentation. One final pin, not intermediate repeated updates.
2. Generator-produced Rust/ownership manifest only. No handwritten generated
   correction or package metadata mixed into this commit.

The paired commits are one deliverable; temporary provenance/generated mismatch
between them is not a release or readiness checkpoint. Final HEAD must satisfy
all checks. Implementer0 commits only owned paths; no hooks bypass is needed
because the repository declares no framework. Preserve the HaveAPI review range
as input evidence; never change its final commit message or history.

## Final review, longer checks and publication boundary

After both commits and quick checks, lead commissions independent final review
of the complete main-base-to-final-head branch, source/input graph and all
generated outputs. Mechanical generated content can avoid a separate standalone
review, but does **not** exempt this complete deliverable: the exact pin,
provenance, native build configuration and substantive development instructions
need review and the generated changes remain in its whole-branch inventory.
Suggested lanes: general, architecture/configuration, proportionality and
cross-project compatibility; no database/schema migration. Earlier HaveAPI review
does not certify the downstream regeneration.

Only after review, a fresh policy watcher runs the exact committed downstream
head in its own pinned environment, recording clean-source/head, source input
hashes and tool identities:

```sh
tools/check-provenance
tools/regenerate --check
cargo test --locked --all-targets
cargo test --locked --all-targets --features blocking
cargo doc --locked --all-features --no-deps
cargo rustc --locked --lib --all-features -- -D non_snake_case
cargo package --list --locked
cargo package --locked
```

For the separate Rust1.95 pass, retain the downstream formatter for generation
and explicitly select the known non-bootstrap Cargo/rustc pair from
[api-doc-msrv-readiness.md](api-doc-msrv-readiness.md):

```text
Cargo /nix/store/rai05nypxnmj22l65nwsk5xjsaq8s4vc-cargo-1.95.0/bin/cargo
rustc /nix/store/m4hrdkg9ypcw8y1banfc26q3f27kfqvb-rustc-wrapper-1.95.0/bin/rustc
```

In the downstream shell, use that Cargo executable with `RUSTC` set to that
compiler for the default and blocking `cargo test --locked --all-targets`
passes and `cargo rustc --locked --lib --all-features -- -D non_snake_case`.
Unset inherited compiler wrappers/flags for both toolchains; record exact
identities. Do not substitute the HaveAPI development formatter 1.10.0 for the
downstream required 1.9.0. Both async/blocking modes, public examples, docs,
package contents and scoped naming lint must pass. No live production requests,
tokens or new vpsAdmin DB/listener campaign: the runtime/schema are byte-equal,
and ignored real_vpsadmin mutation tests remain unselected for this task.

Retain the new `.crate` archive, manifest/list, full command/exit evidence and
generation input/output digests under a new downstream receipt, clearly distinct
from official HaveAPI artifacts. Check packed source contains the generated
runtime and no HaveAPI path/Git runtime dependency. A packaging failure due to
environment/runtime resolution is diagnosed, never bypassed with allow-dirty or
unlocked dependency updates. Feature push triggers ordinary existing CI; observe
its exact head without dispatching release.yml. Passing CI/package checks is not
publication approval.

## Compatibility and recovery

No public Rust names/types, generated routes, API version, Cargo version/MSRV,
runtime wire/auth behavior, persisted state, database or deployment changes.
Old/new generated clients coexist against API7.0. The attributes only document
intentional naming exceptions. Fiddle/libffi are generation tools and are not
crate runtime dependencies. Rollback selects prior source/pin/generated tree;
no state conversion or server coordination is needed. Keep both exact revisions
and the unchanged saved schema as evidence. No crate publication, new HaveAPI
release or integration is authorized by “regenerate the client.”

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
