# TypeScript generated-client candidate

Complete committed candidate, pending lead-assigned independent final review.
No push, version bump, release, publication, merge or deployment performed.

- Repository/worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/vpsadmin-typescript-client`
- Branch: `2026-10-30-oomd-abuse-policy`; default `main`
- Base: `2da950a98fa13468b36d03b13fb5e81cca206e0e`
- Head: `6a5227c156aeef89447abb1f2e68988cecb735f4`; clean tracked source.
- API input: `7919441ccb8e9587ad0afc84674b074ca9c5a880`, schema `f919dcebf8ce5453dce6b0eb09e718f72664b5137443bb8e2064ff6452470ca7`.
- Exact pack/provenance: [handoff receipt](typescript-handoff.json).

## Acceptance and scope

Synchronize final full-fixture API input with retained HaveAPI1ef9b204 and
HaveAPI JS runtime0.32.0. Preserve optional read selectors despite backend
default, all selected summary members/types, nullable resets, false values and
old-API capability absence. Registry/status strings remain server validated
per architect clarification in design.md. No provider change or shim.

## Complete series and generated stream

```
77e22636c17cb639fa2837239e3d7bf79e1359c6 Refresh generated VPS incident operations from the final API schema
6a5227c156aeef89447abb1f2e68988cecb735f4 Verify incident selectors and settings through the packaged runtime
```

One final generated input stream (first commit), separate handwritten tests/docs
(second commit). No superseded candidate/pin stream, no migration, persisted
state, conversion, deployment or externally consumed migration. Raw API export
records upstream backend migrations as provenance only, not client migrations.
Full generated set remains677 files; additions0/removals0, six VPS action modules
and root schema hash/manifest change. Handwritten package files preserved.

```
docs/development.md                            |    9 +
 schema/provenance.json                         |   76 +-
 schema/schema.json                             | 1298 +++++++++++++++++++++---
 schema/tooling.Gemfile.lock                    |  105 +-
 src/generated/.haveapi-generated.json          |   16 +-
 src/generated/api.ts                           |    2 +-
 src/generated/resources/vps/actions/clone.ts   |   19 +
 src/generated/resources/vps/actions/create.ts  |   19 +
 src/generated/resources/vps/actions/index.ts   |   62 ++
 src/generated/resources/vps/actions/replace.ts |   19 +
 src/generated/resources/vps/actions/show.ts    |   33 +-
 src/generated/resources/vps/actions/update.ts  |   32 +
 test/consumer/runtime.mjs                      |   72 +-
 test/consumer/types.ts                         |   26 +
 tools/generator.json                           |    6 +-
 15 files changed, 1557 insertions(+), 237 deletions(-)
```

Full diff: `git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/vpsadmin-typescript-client diff 2da950a98fa13468b36d03b13fb5e81cca206e0e..6a5227c156aeef89447abb1f2e68988cecb735f4`.

## Quick evidence

Pinned Nix: build, typecheck, strict consumer typecheck, npm test15/15,
test:package passed0; log `/tmp/incident-client-ts-quick.log`.
Deterministic regeneration --check passed0 against exact final raw input,
log `/tmp/incident-client-ts-regeneration.log`.
Exact named handoff archive passed check-package --archive0,
log `/tmp/incident-client-ts-exact-pack.log`. Archive341450bytes, SHA256
`fee3800140869c1f721c5a07eda3e438d1a347690dc89aa5f8379a9efc1663bf`. Actual published runtime0.32.0 sends omitted initial
selectors, explicit selected writes/null/false and propagates server refusal.
No live API/guest/browser checks launched.

## Documentation and compatibility

Incident selector/type/capability/synchronous semantics -> SDK contributors,
reference -> `docs/development.md`, checked by real runtime + strict packed
consumer. API export/generation process -> contributors/how-to -> existing
vpsAdmin `docs/api-schema-export.md` and client guide, unchanged process/pins.
Exact candidate and check receipts -> session execution -> this packet and
handoff JSON, not project product docs.

Additive optional inputs/output preserve old callers. Callers omit incident
selectors on initial reads of older APIs and check returned capability fields
before new calls; backend permission/registry checks remain authoritative.
Datetime strings and nullable/absent output follow existing generator behavior.
Rollback restores input metadata and generated output together; cannot undo
writes already sent. Package version0.4.0 is unchanged development candidate,
not a registry claim. Published TS release remains required before React merge.

Risk: high at cross-project/public-contract boundary. Lead owns reviewer0 saved
Sol/xhigh assignment; applicable general, architecture, scope, risk lanes and
whole-series/generated-stream/migration conclusion. No independent review
claimed by implementer. Go/Rust package remains underway before full delivery.
