---
lifecycle: active
---

# 2026-11-01-typescript-client-migration

## Status

- Implementation authorized; generator-first design and execution plan being
  finalized. End state is full SDK use and removal of the custom request layer.
- Verified `dev-session current` and both environment markers match this session.
- Architect `architect0` (retained Astra/xhigh, workspace_write, ready) owns
  investigation and `design.md`; lead owns records and acceptance.
- Live roster revision 61 verified: implementer0–implementer7 all ready,
  workspace_write, Sol/xhigh; reviewer0 retained Astra/xhigh, read_only. No team
  reconfiguration by lead.

## Phase checklist

- [x] Verify identity, scope and retained team.
- [x] Fetch affected default refs and assign investigation.
- [x] Compare client semantics and migration boundaries.
- [x] Inspect acceptance evidence and deliver recommendation.
- [x] Finalize generator/SDK/WebUI implementation contracts and package plan.
- [ ] Generator and schema/SDK foundation.
- [ ] WebUI policy integration and representative pilot.
- [ ] Parallel domain migration and custom-layer removal.
- [ ] Quick checks and committed independent final review.
- [ ] Longer integration/browser/package checks and feature readiness.
- [ ] Explicitly approved integration/publication/deployment, if requested later.

## Next actions

- Finish G source-unit checks and commit/review generator; regenerate S exact
  candidate, then release W and representative domain pilot slices.
- Session remains open. No integration, deployment or lifecycle action requested.

## Documentation

- [Plan](plan.md); [assessment, proposal and source evidence](design.md).
- Product documentation updates belong with their eventual implementation.

## Repositories

- `vpsadmin-webui` origin/main: `f2765d3fd778927f4cda3563f66615bfcf72b7cf`.
- `vpsadmin-typescript-client` origin/main:
  `e5786f69b7c223c3bb5b1de99b7f97186eec368a`.
- `haveapi` origin/master: `209a7ac0c2fe6cd1b78735f50b5e60d979309543`.
- `vpsadmin` origin/master: `610a96f8ce523afbcd3e4374a70047dbe3264b0d`.
- All four refs freshly fetched for implementation planning; owned worktree
  registration complete under `worktrees/2026-11-01-typescript-client-migration/`.
  HaveAPI/SDK/API branches use dated slug; WebUI uses
  `dev/typescript-client-migration`. See portal registrations for exact bases.

## Implementation backlog and current evidence

| Owner | Package | Dependency/status | Acceptance |
| --- | --- | --- | --- |
| architect0 | Generator/SDK/WebUI design and contract reconciliation | Brief delivered in design.md; source-contract questions being resolved | Clean generator-owned interface, preserved application policy |
| implementer0 | HaveAPI TypeScript generator | Active; focused 17 source examples and lint pass, broad unit queued | Descriptions, local validation error, typed metadata, coherent namespace override; committed quick checks |
| implementer1 | Full schema capture + SDK0.3.0 regeneration/package | Active; capture passed twice, waits exact G head | Full provenance, deterministic generated tree, immutable candidate archive |
| implementer2 | WebUI shared policy/pilot/integration/retirement | Read-only prep done; npm setup queued; waits G/S | One policy executor; no custom endpoint layer at completion |
| implementer3 | VPS/storage | Read-only mapping complete, holds for foundation/pilot | SDK calls/typed inputs, honest output models, receipts and read-back |
| implementer4 | Networking/DNS | Read-only mapping complete, holds for foundation/pilot | SDK descriptions/operations, nullable and secret handling preserved |
| implementer5 | Users/settings | Read-only mapping complete, holds for foundation/pilot | Scopes, settings, token/secret guards, types preserved |
| implementer6 | Infrastructure/operations | Read-only mapping complete, holds for foundation/pilot | Node capabilities, advisory revision contracts, paging and uncertainty |
| implementer7 | Finance/content | Read-only mapping complete, holds for foundation/pilot | Public models, compensation, reconciliation and role scope |

- Exact 64-file partition and checks in [implementation brief](design.md).
- G/W shared namespace contract reconciled by architect; SDK generated
  `createClient({execute,metaNamespace?})` owns coherent input/object metadata
  mapping and declared output row metadata projection, preserving raw envelope.
- G preparation passed (~68s): source bundles/npm, reviewed hook install/sign,
  JS build; no kernel build. Log `generator-prepare.log`.
- S preparation passed (~91s); two fresh full-fixture captures passed (~81s),
  14 exporter examples, 0 failures, 519 actions/151 resources each; exact schema
  and provenance bytes match. Logs under artifacts/package-s. Schema owner
  reconciles MariaDB cleanup and old/new input graph.
- S independently verified schema matches previous bytes, all plugin/profile
  coverage retained, refreshed provenance/tool lock, two exact captures, no
  MariaDB process or owned temporary database remains. Compact evidence in
  artifacts/package-s/schema-capture.md. API input checkout remains clean.
- W npm dependency preparation passed (~27s); S lock/install preparation passed
  (~5s), with HaveAPI0.32/TS6+TS5.9 alias verified. No audit-fix expansion.
- G first broader source-unit batch failed a stale exact import formatting
  assertion, fixed narrowly (focused case passes). Existing release fixture
  needs ignored Rust lock/bundle; minimal preparation + rerun active. No
  source-contract failure demonstrated; actual-runtime tests remain post-review.
- Source-backed domain corrections and ownership settled in
  [contract dispositions](contract-dispositions.md): ineffective search and
  unsupported nulls are not widened into SDK, advisory writes bind observed
  revisions, canonical namespaces replace legacy guesses. Domain source hold
  remains until stable generated artifact/shared pilot.
- No long integration tests, registry publication, default-branch integration
  or deployment yet. Long preparation/input generation uses fresh Luna/low
  utilities, one batch at a time. Domain source edits wait stable G/S/W pilot.

## Commands run

- `dev-session current`, filtered `team list`, `team assign`, `url`.
- Fetched explicit origin default-branch refspecs for all three projects.
- Read required workspace procedures and skills; inspected shared Git status
  without changing unrelated records/index entries. Workspace master is ahead
  of origin/master, with no remote-only commits.

## Results

- Confirmed generated SDK is a facade over HaveAPI, not a transport replacement.
  WebUI already calls raw `AsyncClient.request`, without dynamic resource setup.
- SDK 0.2.0 pins HaveAPI 0.30.2; WebUI pins 0.32.0. Proposed direction is to
  verify/upgrade SDK support, retaining the WebUI's newer runtime.
- Generated operations construct typed method/path/namespace/input specs and
  validate inputs; output payloads are asserted, not runtime-validated.
- Preserve policy at the `RequestSpec -> RequestResult` boundary: live auth,
  language, BFF recovery, error classification and ambiguous writes. Existing
  `CallOpts` omits outputNamespace/headers/timeout and is not a sufficient
  generated-executor interface.
- `architect0` delegated a read-only scale/special-case inventory to retained
  `implementer0`; no application edits are assigned.
- Inventory accepted from `implementer0`: 64 production TypeScript API files,
  53 with 368 lexical `haveApiCall` sites; 260 handwritten interface/type
  declarations across 60 files (DTOs, options and helpers, not endpoint count).
  Method: exact-commit `git ls-tree`/`git show`, production `src/**/*.ts(x)`,
  excluding tests/specs and `src/test`. Text counts, not AST analysis.
- Existing live OPTIONS probes gate fields/requiredness/permissions; retain them.
  Keep keyset URL history, bounded collection completeness, action-state proof,
  anonymous scope and full-envelope consumers. Download adapters return JSON
  links, not binary transport.
- SDK local input validation throws `TypeError`; existing mutation policy
  classifies `TypeError` as ambiguous. A later pilot needs a proven pre-dispatch
  validation distinction without reclassifying uncertain transport failures.
- Lead spot-checked exact source: `src/lib/api/haveapiRequestClient.ts`,
  `haveapi.ts`, `vps.ts`, SDK `src/index.ts`, generated runtime and VPS
  Index/Update operations. Generated VPS `id`/`hostname` are optional nullable,
  unlike current required UI fields, and association fields are partial unknown
  references. Normalize validated output to explicit view models; avoid broad
  casts that erase the benefit. Retain HTTP/meta/envelope receipts.
- Accepted architect's final report and `design.md`: phased executor/adapter
  migration, runtime version alignment, output normalization, retained permission
  and recovery policy, controlled schema regeneration/release pipeline.
- Checks: source inspection only, no builds/tests/API calls. SDK runtime/browser/
  TypeScript compatibility, exact endpoint coverage and bundle effects remain
  pilot validation. No independent change review triggered: this is routine
  investigation/findings, with no application or product-documentation changes.

## Open questions

## Cleanup

- No deployment, resource claims, runners or lifecycle actions.
