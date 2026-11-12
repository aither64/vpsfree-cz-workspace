# TypeScript 0.3.0 final review packet

Status: committed deliverable and assigned quick checks complete; ready for lead
to assign independent final review. Integration/publication gates remain.

## Requested result and bounds

Consume released HaveAPI 0.32.2, regenerate the full-fixture API 7.0 SDK and
publish the next minor only because actual generated TypeScript code changes.
Package owner implementer3 follows architect-owned design.md package D/common/
release rules. Lead owns review assignment, approved main integration and external
release sequencing. No machine deployment, server mutation or lifecycle work.

Repository: git@github.com:vpsfreecz/vpsadmin-typescript-client.git, target main.
Worktree: worktrees/2026-11-02-haveapi-vpsadmin-release/vpsadmin-typescript-client.
Branch: 2026-11-02-haveapi-vpsadmin-release.
Base: e5786f69b7c223c3bb5b1de99b7f97186eec368a.
Head: d354491537f8b654b4d2c33a705cad84474f95d6.
Complete series: one commit d354491537f8b654b4d2c33a705cad84474f95d6,
Regenerate the TypeScript SDK for HaveAPI 0.32.2 as version 0.3.0.
Final diff: 687 files,29934 insertions/11443 deletions.
Use git diff e5786f69b7c223c3bb5b1de99b7f97186eec368a..d354491537f8b654b4d2c33a705cad84474f95d6.

Session records: plan.md, state.md, design.md, typescript-package.md and
vpsadmin-schema-export-receipt.json under this tracking directory.

## Source/input contract and compatibility

HaveAPI annotated tag v0.32.2 object7f8f656ca7655bafaf2cf5e7095573806085a442,
peeled source1ef9b204ba45bb261d3334be5c555cc1856b713b. Separate clean source-only
clone haveapi-ts-tools is not an unmerged HaveAPI feature branch. Generation
loads both exact Ruby schema and TypeScript generator source, preserving existing
refusals and writer ownership. No generated source is handpatched.

The two independent vpsAdmin full-fixture exports from clean committed reviewed
A head5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5 are byte-identical for schema,
provenance and tooling lock. API7.0/protocol2.0, all six plugins,151 application
resources/519actions/8720parameters and separate1auth resource/5actions remain.
Canonical schema hash476f0086726a443a6ef8ad9a9d499bd3feff6eb6c5b0b652dcc999192d638794
is unchanged from prior SDK. Updated provenance and lock faithfully bind the new
source and all five0.32.2 gem identities. Exporter dependency graph changes are
recorded inputs, not a changed client npm toolchain.

Npm peer/dev dependencies both pin exactly haveapi-client0.32.0, as required by
the released generator runtime contract. Older SDK/runtime pairs remain pin-able.
Pinned Node24.21.0/npm11.19.0/Ruby3.4.11/TS6.0.3/Prettier3.9.10 retained.
New SDK metadata typing, describe helpers/options and local ClientInputError are
public-contract changes accepted in the conditional0.x minor. No server auth or
permissions are inferred from snapshot/static presence. Transport errors preserve
identity and do not establish whether a write was sent. Description types remain
conservative/extensible wire data. Existing handwritten adapter is unchanged.
No database migrations, persisted-state or node protocol changes. Explicit
migration inventory: no migrations. Snapshot provenance retains unchanged
upstream fixture/plugin migration inventories; SDK does not execute them.

D integration/publication requires A master integration and exact exported SHA
== integrated final A feature head, with fresh remote ancestry evidence. Any A
rebase/head change requires both fresh exports and D input/provenance reconciliation
even when schema bytes remain equal. No integration/publication is claimed here.

## Changes and scope

Generated manifest grows674→675 owned files by adding descriptions.ts; no old
owned file or exported declaration removed. Root/action OPTIONS describe uses
saved help routes and encoded placeholders; receipts type declared global meta
while retaining unknown extension keys; one metadata namespace override maps
declared metadata; generated pre-dispatch checks throw ClientInputError.

Focused SDK consumer tests add positive/negative describe option/type checks,
typed metadata and unknown extension use, pre-dispatch TypeError subtype
identity vs unchanged executor TypeError, namespace projection/raw-envelope
preservation, and actual published AsyncClient loopback wire calls. Existing
request shape, omission/null/false/zero/error/adapter and source-refusal checks are
reused. Package checker asserts exact peer/runtime version and uses the retained
archive in a strict ESM/types consumer. Upstream exhaustive generator suites are
not duplicated. No unrelated workflow, generator wrapper or app source edits.

CHANGELOG/README/development guidance use main-agent final prose; describes
features and exact runtime pairing. No operational guide change needed: existing
docs/releasing.md immutable artifact/OIDC/retry workflow remains authoritative.

## Intended commit shape and history duties

One final coupled SDK update: recorded generator inputs, owned generated source,
exact runtime dependencies, consumer checks, user-facing compatibility guidance
and final0.3.0 package identity. The generator's reproducibility identity binds
package-lock.json including package version, making this one final input stream.
No intermediate pin commits, abandoned approaches, fixups or duplicate update
streams will be retained. This preserves a coherent reproducible/revertible SDK
and avoids obsolete package-lock/generator-digest updates.

Final reviewer must assess the complete base-to-head series and final diff,
explicitly conclude obsolete-history/repeated-stream disposition and no migrations.
The generated/dependency content exemption does not remove these history duties.

Risk classification high: generated public request/description/metadata contracts
and cross-project runtime pairing. Applicable lanes: general, architecture and
repetition, scope/proportionality, risk/compatibility. Retained reviewer0 Sol/xhigh
is lead-selected; lead verifies live saved identity/settings before assignment.

## Validation

Exact-source generate + deterministic --check passed40s (typescript-generation-result.md).
Manifest inventory and exported-declaration comparison found only descriptions.ts
added and no removals. Fresh Git/npm queries still show latest release0.2.0,
no0.3.0; actual code changes justify selected0.3.0.

Initial batch: install/build/source+strict consumer typechecks passed; unit test
12/13, because new loopback assertion omitted the schema's network query namespace.
Corrected assertion to observed canonical network[enabled]/network[limit]. No code
change required. Final required check batch and commit receipt pending below.


Final local verification passed under fresh Luna/low watcher in77s, exit0:
- exact-source deterministic `./tools/regenerate --haveapi-source ../haveapi-ts-tools --check`;
- shared-source selection/dirty/untracked refusal test1/1;
- `npm test` (build plus13/13 tests);
- `npm run test:package` (packed ESM, strict types and actual runtime consumer);
- `npm run typecheck` and `npm run typecheck:consumer`.
See [final checks](typescript-final-checks-result.md) and its full log.
Clean npm install and standalone build also passed in initial batch before the
corrected loopback assertion. `git diff --check`/staged check passed. No hook
framework is declared; canonical hooks contain only samples; no hook bypass.

All intended source changes are committed and worktree is clean. No superseded
unmerged approaches, follow-up commits, repeated dependency/input streams or
migrations remain. Snapshot and fixture/plugin migration inventories are
unchanged recorded upstream evidence. No integration, tag push or publication
has been performed. No process/watcher remains active. Broad long CI is not
awaited under the user's constraint.

Feature publication receipt: SSH push succeeded and fresh remote query confirms
feature d354491537f8b654b4d2c33a705cad84474f95d6, target main still
 e5786f69b7c223c3bb5b1de99b7f97186eec368a. Complete diff is676 generated paths
(675 owned TS sources plus ownership manifest),29697generated insertions and
11398deletions, plus11 input/package/prose/test/checker paths. No rebase required.
