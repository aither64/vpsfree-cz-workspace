# Final generated-client synchronization candidates

Owner implementer1. API owner0 and React owner2 retain their source/Git scopes.
Lead owns independent reviewer assignment and publication coordination.

Requested outcome: assess all3 clients against final committed/published API
7919441ccb8e9587ad0afc84674b074ca9c5a880, preserve exact raw inputs and pinned
per-client generation/runtime/config/toolchain, update all affected generated
outputs and add meaningful omission/null/false/response/wire coverage.
No version bump, tag, registry release, default integration or deployment.

## Shared source and compatibility evidence

Raw schema f919dcebf8ce5453dce6b0eb09e718f72664b5137443bb8e2064ff6452470ca7;
raw provenance d9f839fac6bf45c5d92d7a7a83cc49a5328a5c136bd7e11539b5c955a5208bdd;
exporter lock2e9a124eff7b80d6fd57cd0f03cb2809847c67cc7f1af6364911c3622d7242a0.
All three copies retain raw bytes. API profile EN/full6plugins/API7.0/protocol2.0.
Independent repeated export belongs to owner0 and matches exactly; see
nov13-api-export-receipt.json. Schema comparison against previous client input:
103 added parameter records, zero removed or modified existing records; no
resource/action additions/removals. Total152resources/526actions includes
1authenticationresource/5actions; application151resources/521actions;8863params.

All generators retain HaveAPI1ef9b204ba45bb261d3334be5c555cc1856b713b/0.32.2,
shared-schema identityd704e6c155f9f2ec82bdf627857bdc23aa08a1d2133806df1f8ed5beb2d8c439.
No provider edit/upgrade. TS retains published runtime0.32.0 and all tooling/
formatter/locks; Rust retains copied runtime9c50b8167a8b82118ba42372633e3b004276ba49fbdfed75d4979a913feea739,
generator lock/config/Ruby3.3.10/rustfmt1.9.0. Go retains source-file digest
inventory, generator lock/Ruby3.4.11/Go1.26.10 and sole bounded OAuth endpoint
projection, raw+derived digests. Go projection actually used declared shell
Python3.13.17; corrected the execution provenance to that path, no dependency
or shell-source change. Exporter tooling Ruby3.4.9/Bundler4.0.24 differs from
retained generators as expected; no normalization of its lock.

Initial reads omit selector despite backend default. Selected writes retain
selector/null resets/false without unrelated input. Generated optional output
remains subject to permissions/API capability. Datetimes are strings. TS retains absent/null output; Rust maps both to None. Retained Go scalar
output maps both to zero
values (documented, no provider scope expansion). Primitive strings remain
server registry/status validation, per architect Nov14 clarification. No new
enum provider or rawtransport/cast shim. Update metadata absence does not
invent pending/completed transactions. Rollback restores schema/provenance and
outputs together; cannot undo previously submitted writes.

## vpsadmin-typescript-client

Worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/vpsadmin-typescript-client`. Base `2da950a98fa13468b36d03b13fb5e81cca206e0e`; final head `6a6ca3613ce947a1393597d5ddcbc78294f6b12d`, tree `301df127050d80620a32798c588530c5f351efe3`. Clean source.

```
77e22636c17cb639fa2837239e3d7bf79e1359c6 Refresh generated VPS incident operations from the final API schema
6a5227c156aeef89447abb1f2e68988cecb735f4 Verify incident selectors and settings through the packaged runtime
6a6ca3613ce947a1393597d5ddcbc78294f6b12d Retain the reviewed SDK archive for development HTTPS consumers
```

```
development-artifacts/incident-escalation-sdk.json |   29 +
 development-artifacts/incident-escalation-sdk.tgz  |  Bin 0 -> 341450 bytes
 docs/development.md                                |    9 +
 schema/provenance.json                             |   76 +-
 schema/schema.json                                 | 1298 +++++++++++++++++---
 schema/tooling.Gemfile.lock                        |  105 +-
 src/generated/.haveapi-generated.json              |   16 +-
 src/generated/api.ts                               |    2 +-
 src/generated/resources/vps/actions/clone.ts       |   19 +
 src/generated/resources/vps/actions/create.ts      |   19 +
 src/generated/resources/vps/actions/index.ts       |   62 +
 src/generated/resources/vps/actions/replace.ts     |   19 +
 src/generated/resources/vps/actions/show.ts        |   33 +-
 src/generated/resources/vps/actions/update.ts      |   32 +
 test/consumer/runtime.mjs                          |   72 +-
 test/consumer/types.ts                             |   26 +
 tools/generator.json                               |    6 +-
 17 files changed, 1586 insertions(+), 237 deletions(-)
```

Full diff: `git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/vpsadmin-typescript-client diff 2da950a98fa13468b36d03b13fb5e81cca206e0e..6a6ca3613ce947a1393597d5ddcbc78294f6b12d`.

## vpsadmin-go-client

Worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/vpsadmin-go-client`. Base `af9a819ca35f6de5556092679b4df7cb72e7aa89`; final head `a2ab4ead896ae1f4d1fe70ad364040dae76f0f7c`, tree `981d147cb650f9555bfa72d75cd3da2b8a5d966b`. Clean source.

```
356417d8abce2ed2e3a46f1e22f51b6cdd206b5e Refresh generated incident fields from the final API schema
a2ab4ead896ae1f4d1fe70ad364040dae76f0f7c Check incident settings through the generated Go transport
```

```
README.md                             |   12 +-
 client/incident_policy_test.go        |  120 +++
 client/resource_vps_action_clone.go   |   19 +
 client/resource_vps_action_create.go  |   19 +
 client/resource_vps_action_index.go   |   89 ++-
 client/resource_vps_action_replace.go |   19 +
 client/resource_vps_action_show.go    |  123 ++++
 client/resource_vps_action_update.go  |  166 ++++-
 schema/api-7.0.json                   | 1298 +++++++++++++++++++++++++++++----
 schema/generator.json                 |   19 +-
 schema/provenance.json                |   76 +-
 schema/source-api-7.0.json            | 1298 +++++++++++++++++++++++++++++----
 schema/tooling.Gemfile.lock           |  105 +--
 13 files changed, 2946 insertions(+), 417 deletions(-)
```

Full diff: `git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/vpsadmin-go-client diff af9a819ca35f6de5556092679b4df7cb72e7aa89..a2ab4ead896ae1f4d1fe70ad364040dae76f0f7c`.

## vpsadmin-rust-client

Worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/vpsadmin-rust-client`. Base `823a4f8450fce4947310fc81bcdebdca91d9ffae`; final head `9157c271b6a5446aaf5e3809a82b5b486441e4fb`, tree `63856abcecf4cd3d3110961b3e9b1dca3c1860cd`. Clean source.

```
d0f4c3d038151a72714915bccf7afccccb31854d Refresh generated incident types from the final API export
9157c271b6a5446aaf5e3809a82b5b486441e4fb Cover incident input and response protocol behavior
```

```
docs/development.md                    |    9 +
 schema/api-7.0.json                    | 1298 ++++++++++++++++++++++++++++----
 schema/inventory.json                  |  680 ++++++++++++++++-
 schema/provenance.json                 |    8 +-
 schema/source-provenance.json          |   76 +-
 schema/tooling.Gemfile.lock            |  105 ++-
 src/generated/.haveapi-generated.json  |   16 +-
 src/generated/mod.rs                   |    2 +-
 src/generated/resources/vps/clone.rs   |   38 +
 src/generated/resources/vps/create.rs  |   38 +
 src/generated/resources/vps/index.rs   |   89 +++
 src/generated/resources/vps/replace.rs |   38 +
 src/generated/resources/vps/show.rs    |   62 +-
 src/generated/resources/vps/update.rs  |   76 ++
 tests/incident_policy.rs               |  228 ++++++
 15 files changed, 2494 insertions(+), 269 deletions(-)
```

Full diff: `git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/vpsadmin-rust-client diff 823a4f8450fce4947310fc81bcdebdca91d9ffae..9157c271b6a5446aaf5e3809a82b5b486441e4fb`.

## Whole series, generated streams and migration lineage

Each client has one final generated schema/output update stream and one
separate handwritten test/docs commit; no superseded intermediate generator
input, provider update, unused compatibility path or migration. No client
migration exists or was merged/released/deployed/externally consumed. Raw
export provenance inventories backend migrations only; owner0 owns their
schema lineage and review. No package manifests/versions/dependency graphs
were changed.

TS has one additional delivery-only support commit at lead's explicit request:
exact independently reviewed npm archive + compact provenance, outside npm
files whitelist. PackedSOURCE remains6a5227c, archive bytes unchanged. Standard
React Nix fetch rejects relative file archives, so immutable HTTPS transport
is required for the accepted temporary dependency. This is not a repeated
schema/pin stream. Lead owns mechanical certificate/review reuse over6a..6a6.

Generated whole-tree comparisons include removals: TS677->677, Go684->684,
Rust688->688; each has0added/0removed owned files. Changes are the six affected
VPS action modules plus schema hash/ownership records where applicable. Full
input snapshots are additive103parameterrecords with no existing changes.
Handwritten files and module/package metadata preserved.

## Verification and finite gaps

- TS build/typecheck/consumer types/npm15tests/package pass0;
  `/tmp/incident-client-ts-quick.log`. Deterministic pinned regeneration
  --check0: `/tmp/incident-client-ts-regeneration.log`. Exact341450B archive
  SHAfee3800140869c1f721c5a07eda3e438d1a347690dc89aa5f8379a9efc1663bf passed
  existing-archive package consumer: `/tmp/incident-client-ts-exact-pack.log`.
  ActualHaveAPI0.32.0 request+HTTP loopback assertions; strict installed consumer.
- Go full fresh output byte comparison684files0; generation exit0 in
  `/tmp/incident-client-go-generation.log`; go test ./... and4schema tests0
  `/tmp/incident-client-go-quick-fixed.log`. Initial tests expected false text
  instead of existing numeric0 query and omitted existing empty_meta; corrected
  test expectations, no production defect (`...go-quick.log` retained).
- Rust format/shellsyntax/check-provenance/7provenance tests0,
  `/tmp/incident-client-rust-quick.log`;10regeneration refusal tests0,
  `/tmp/incident-client-rust-refusals-fixed.log`; deterministic regen--check0,
  `/tmp/incident-client-rust-regeneration.log`. Initial refusal command lacked
  HAVEAPI_SOURCE then prepared bundle env; fixed invocation once within guide
  with raw failure logs retained. Generator/runtime source unchanged.
- Rust focused committed protocol tests passed3/3,0filtered, exit0 in
  `/tmp/incident-client-rust-focused-corrected.log`. Fresh catalogLuna/low
  first compiled2m43s but a trailing dot filtered all3 tests; that result is
  compilation-only (`...rust-focused.log`). Corrected unfiltered inline run
  finished0.35s. Existing two generated dead-code warnings remain. Target
  allocation now997516KiB (generator tools+compiled client/dependencies).
  Broader default/blocking/doc/package/minimum-compiler gates remain separate;
  no real-server/browser/guest checks.
- TS feature6a6ca361 published with exact SSH/HTTPS receipt; Go/Rust unpushed.
  TS2da..6a independent final review CLEAR per
  lead; exact6a..artifacthead mechanical certificate accepted. Go/Rust final
  independent review is ready for lead assignment; finite quick checks pass.

## Documentation routing and review scope

Incident selectors/capability/nullability/response behavior -> SDK contributors,
reference -> TS/Rust docs/development.md, Go README existing regeneration home;
backed by focused real serializer/transport tests. Generation/compatibility/
rollback contributor process -> existing client guides and authoritative
vpsAdmin docs/api-schema-export.md, checked/retained. Individual source/check/
archive/publication records -> this session packet and linked handoff receipt;
no rollout log in product docs. No KB/UI image or prose change in this package.

Overall high risk at public/cross-project contract boundary. Suggested all4
lanes general/architecture/scope/risk and explicit whole-branch generated-stream/
migration conclusion; lead selects retained reviewer0 Sol/xhigh unchanged.
No default integration or publication permission inferred from review. TS
release on registry remains a separate prerequisite before React merge.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/


## Accepted review and G1 narrow closure

Lead reports reviewer0 Go/Rust all4lanes/HIGH source CLEAR, no Blocking or
Important; whole history/no migrations/docs/provenance satisfactory. G1 accepted
and fixed with one Go1.16-compatible map-key lookup, folded into handwritten
commit. Generated commit356417d8 unchanged; final Goheada2ab4ead896ae1f4d1fe70ad364040dae76f0f7c,
old f367 retained. Exact diff/tree/series/focusedcheck evidence in
[go-g1-closure.json](go-g1-closure.json). Rust9157 source unchanged.


## Final publication and automatic hosted verification

All three final featureheads now published with exact SSH default/head/lease
and capture proofs; defaults unchanged. See go-/rust-/typescript-publication-
receipt.json. TS artifact delivery head6a6ca361 retains packedsource6a5227c;
HTTPS200exactapprovedarchive verified. Go a2ab4ead includes only accepted G1
map lookup narrow fix; Rust9157 unchanged. Lead owns step9 closure and durable
observation after one initial CI inventory. Exact current gates/run IDs/job IDs/
attempts and snapshots: ci-handoff.json. TS passed; Rust async/regeneration passed,
blocking/docs/package/min1.95 pending at handoff. No duplicate local broad suite,
CI watcher, live API or other runtime operation.
