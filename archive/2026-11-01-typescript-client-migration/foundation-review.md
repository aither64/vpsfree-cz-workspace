# Foundation final-review packet

Current phase: complete generator and SDK foundation, before real HTTP/archive
integration. This is final review of those completed phase deliverables, not
review of the unfinished WebUI or a claim of whole-initiative readiness.

User scope: full vpsadmin-typescript-client adoption in WebUI, clean separation
of concerns, SDK improvements through its generator, autonomous isolated-worktree
implementation, periodic rebase for concurrent WebUI changes. No integration,
registry publication, tags or deployment. Initial assessment/design alone did
not trigger review. Foundation implements reusable facilities required to remove
custom WebUI calls and live OPTIONS endpoint definitions.

Read work/2026-11-01-typescript-client-migration/{plan,state,design,assessment,
contract-dispositions}.md and package source reports. The implementation remains
bounded to generator-owned facilities, exact full schema/provenance and consumer
checks; no backend behavior changes. WebUI source is still unchanged.

## Repositories and lineage

- HaveAPI worktree `worktrees/2026-11-01-typescript-client-migration/haveapi`,
  branch `2026-11-01-typescript-client-migration`, base
  `209a7ac0c2fe6cd1b78735f50b5e60d979309543`, final
  `7cffd0b6b6959abf5b5af810ba81004b8defc13c`.
- SDK worktree `worktrees/2026-11-01-typescript-client-migration/vpsadmin-typescript-client`,
  same dated branch, base `e5786f69b7c223c3bb5b1de99b7f97186eec368a`.
  Final SDK head `383e8556208f330472961077cce4dcb546231c8a`; complete S source
  report in artifacts/package-s/review-packet.md.
- vpsAdmin clean exporter input `610a96f8ce523afbcd3e4374a70047dbe3264b0d`,
  schema capture old source `bcfa95eb136c50d25024f53a6b1af557d1173d56`.
  No API source changes, migrations or operations against deployed APIs.
- WebUI consumer currently `f2765d3fd778927f4cda3563f66615bfcf72b7cf`,
  branch `dev/typescript-client-migration`; current phase has no WebUI diff.
  Representative actual consumers/policy in src/lib/api/haveapi.ts,
  haveapiRequestClient.ts, nodes.ts, networks.ts, vps.ts; assessment documents
  their concrete requirements. W owner will integrate only verified archive.

HaveAPI complete series is one functional commit, 26 files +475/-62, no
superseded approaches or repeated update streams. Runtime support0.30.2→0.32.0
pin/spec/docs changes belong to one support contract. Intermediate message-only
amendments18b8d966/e5b7d31 have identical trees, are absent from final series and
are not pinned. No published/merged history rewritten. SDK one consolidated
schema/generator/runtime/version0.3 stream expected, exact series in assignment.
No migrations, persistent-state format changes, merged/released/deployed or
external-use migration lineage. No feature content pushed/merged/deployed yet.

SDK saved schema remains byte-identical (SHA256
476f0086726a443a6ef8ad9a9d499bd3feff6eb6c5b0b652dcc999192d638794),
519 actions/151 resources/8720 parameters/six plugins. Two fresh captures have
identical schema/provenance/export lock. New provenance binds API610a96f,
fixture/tool inputs, plugin digests and exact gem graph; compact evidence in
artifacts/package-s/schema-capture.md. No permission-filtered live schema.
Generator sourceSHA89ae36c11883979150bd6963a078052a270e5d0d27f7e7853a667997c027193f.
Published HaveAPI0.32 runtimeSHA256
9285eab56e435ee86a501a24808e15496d44521881a032090003a1108511f016.

## Intended public contract / acceptance

- Ordinary invocation and RequestExecutor preserved, one send.
- Generated root/action describe via captured help/path/method/mount, aliases and
  encoded IDs; conservative extensible wire descriptions, no payload validator.
- ClientInputError identifies only proven pre-dispatch generated validation;
  ordinary executor errors unchanged, no secret payloads in errors.
- ActionResult types global metadata with unknown extensions/raw receipt.
- Client metadata namespace override coherent through input/global/object/list
  metadata; narrow declared list projection preserves raw envelope/Custom/nested
  values. No application auth/retry/cache/pagination in SDK.
- Current exact HaveAPI0.32 runtime support and TS5.9/6 consumers.
- Generated source only through exact pinned generator, deterministic manifests;
  no handwritten SDK shim for missing generator features.

Check scope/proportionality and actual public consumers, compatibility/collision
rules, empty/custom outputs, description namespace semantics, malformed metadata,
namespace projection, local-error versus transport distinction and source/package
provenance. Do not treat owner/architect acceptance as independent review.

## Checks and pending integration

G: focused17 plus related emitter/formatter/negative TS/request spies; full
make test-typescript73/0 and release TypeScript fixture24/0;
RuboCop28 files/no offenses; syntax checks; all normal hooks pass. Source final
clean. Initial stale formatted import expectation fixed narrowly; environment
ignored Rust lock prepared for existing unit fixture, no source expansion.
Logs generator-unit-rerun.log and generator-prepare.log.

S: corrected offline regeneration +--check, build, TS6 source/consumer, TS5.9
Bundler consumer, client+release13/0, source refusal1/0. Log
artifacts/package-s/regenerate-quick-retry.log. First watcher launched wrong cwd
and stopped before generation; corrected exact SDK flake/cd, no code workaround.
Export source checks14/0 and double capture passed; MariaDB cleanup verified.

After review/remediation: real published-runtime generator wire/docs harness,
immutable SDK archive checker including actual HTTP loopback consumer and both
compilers. No such long integration run yet. These are separate acceptance
checks, no green fixture claim for a deployed API. SDK remains unpublished.

Docs checked/updated: HaveAPI clients/typescript README/docs +development/release
guidance; SDK README/development/changelog. Main lead applied writing guidance.
Exact reproducibility versions retained because they define support/input graph.
No rollout or deployment instructions are executed by writing these docs.

Overall risk HIGH: reusable public generated cross-project contracts and
metadata/description serialization. All lanes apply: general, architecture,
scope/proportionality, risk/compatibility. Retained reviewer0 saved Astra/xhigh,
read_only, eligible/independent; verify fresh roster before assignment. Read
mandatory-change-review SKILL and all four lane references, review directly
without nested reviewers. Require explicit full-series/history/update-stream
and migration conclusions. Findings Blocking/Important need owner remediation
before long integrations; narrow fixes follow skill rerun rules.
