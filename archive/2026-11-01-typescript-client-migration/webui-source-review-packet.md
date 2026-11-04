# Final WebUI generated-client review

All intended changes are committed and quick checks pass. Independent final
review requested before long tests/build/browser/isolated API execution.

## User scope and acceptance

The user requested full adoption of vpsadmin-typescript-client, replacing custom
endpoint/request logic, with clear ownership boundaries. Autonomous implementation
and periodic rebasing are authorized. SDK improvements must originate in
HaveAPI's generator; generated output must not be edited by hand.

The user chose "Keep the SDK unpublished for now", then explicitly requested
temporary support for unpublished candidates to refine implementation without
releasing arbitrary versions. The final support uses an exact tracked archive,
ordinary relative npm file dependency and bounded existing Nix fetch hooks.
No SDK/default merge, release tag, npm publication or deployment is authorized.

Acceptance: every ordinary vpsAdmin operation and capability description uses
generated actions; HaveAPI retains serialization/decoding; WebUI retains auth,
language, public isolation, validated read recovery, no write replay and uncertain
write semantics. Domain guards preserve full receipts and honest nullable/partial
data. No fabricated IDs/flags/counts, backend behavior expansion or generic schema
framework. Temporary dependency must install reproducibly from source and be
removable later without a new distribution service.

## Exact review range and complete series

Workspace /home/aither/workspace/ai/vpsfree.cz, session
2026-11-01-typescript-client-migration. Worktree:
worktrees/2026-11-01-typescript-client-migration/vpsadmin-webui.
Branch dev/typescript-client-migration, unpublished, clean index/worktree.
Base 63d484fc070dbee633d32624de545e834d483701.
Head aef727cff377c8368268bf61c881d173efe88ef5.
Tree 204193162e635fe95466cf1c182a5f86bab046f6.
Final diff: 424 files, 13,312 insertions and 9,173 deletions; archive 337,414 bytes.

Complete base-to-head series:

1. 831c2a6b638d372fab0b9eb5daf6d26a9f8d59e4 — shared generated bindings/policy.
2. e2e8092935c903a56a768c57f2c4d90bf15a02da — infrastructure workflows.
3. df5f7c4fde3769c8867b07688964304ea26f380c — users/settings.
4. 1bf0abd6a794aadf326450e336b46d62ab35c858 — finance/content.
5. 859050daec72059d6ef340176abac2b4d21dbc48 — network/DNS.
6. ac8d1ba6b681662ef70e06b15f57a7a89553eca9 — VPS/storage.
7. 99fe652316f376f44fa831fe0fb29dffb5d7bf7d — isolated API contract test glue.
8. aef727cff377c8368268bf61c881d173efe88ef5 — temporary unpublished SDK input.

The policy/domain split aids review. Existing cross-domain imports make the
migration one combined verification boundary; intermediate commits are not claimed
to compile independently. No temporary wrappers were invented solely for history.

## History, migrations and update streams

Original complete tip343e was consolidated to636e, folding five fixups into their
owners. Exact complete trees matched9350af2f and each logical aggregate patch was
verified; original author identities/dates retained. Receipts:
webui-history-consolidation.json and its range-diff.

Main advanced fromf2765 to63d (89paths). Original owners resolved shared docs,
network/IP ownership and VPS conflicts, preserving upstream OAuth security,
owner-only synchronous update/readback, extracted dialogs/locks/Tasks behavior
and migration invariants. Final a9e treec7bb8128 was independently reconstructed
from a three-way projection plus exactly nine owner-approved blobs. This was a
substantive refresh, not whole-patch equivalence. Infra/users/finance/runner patch
IDs remained equal. Receipts: webui-upstream-refresh-final.json,
webui-rebase-resolutions.json and range-diff.

After temporary support, one upstream pagination receipt fixture fix was folded
into network. Finald0b2→aef complete trees both20419316, all eight aggregate patches
and authors preserved, all eleven support blobs identical. Receipts:
webui-final-fold-receipt.json and range-diff. Retained feature refs preserve old
complete tips; no merged history rewritten.

No database/schema migrations, changed persisted formats or backend configuration.
The API migrations adapter is frontend VPS-migration workflow, not a DB migration.
No feature commit was merged, released or deployed; no supported intermediate
state requires preservation. Single SDK pin stream exists only in final support
commit: archive/provenance/manifest/npm lock/frontend cache hash. Earlier shared
package.json edit only registers nested test files. No superseded pins remain.
Independently conclude whether obsolete history, repeated streams or migration
lineage problems remain; do not accept these assertions without inspection.

## Provider and artifact provenance

HaveAPI foundation eea3ae5e82c3db23d5f5bc9f1a5e7784117c4e1b on
391b0190241cf195a69b06f7297d3e4eebec5a83 was independently reviewed by this same
retained reviewer before runtime integration. Important selectorless help issue
and advisory descriptor bloat were fixed and directly checked. Original review
and remedies are in foundation-review-result.md. Mechanical refresh from reviewed
172c preserves generator/shared input graphs; artifacts/generator-refresh.json.

SDK99ee06654ef956a09b52749f4cd02d1435362087 on
e5786f69b7c223c3bb5b1de99b7f97186eec368a is entirely generator-produced.
Exact archive SHA256:
f3bb42d0392fb738f5c70fe1415cc8742ab943a31c2ed2a85af5ccbd385d831f.
Schema SHA256:
476f0086726a443a6ef8ad9a9d499bd3feff6eb6c5b0b652dcc999192d638794.
HaveAPI runtime0.32.0 SHA256:
9285eab56e435ee86a501a24808e15496d44521881a032090003a1108511f016.
API input610a96f8ce523afbcd3e4374a70047dbe3264b0d remains clean; six-plugin
full-fixture schema export unchanged.

The tracked archive is mechanical content from the reviewed SDK foundation.
Relative to accepted b650, only generator commit provenance changes; all1352
built runtime/declaration files and source/build/dependency graphs match.
artifacts/package-s/validation.md binds inventories, digests and reused checks.
Review new consumption/configuration fully; avoid duplicating an exhaustive
review of unchanged generated archive content.

## Temporary dependency mechanism

vendor/vpsadmin-typescript-client-0.3.0-99ee06654ef9.tgz is byte-identical to the
retained candidate, with compact packages/vpsadmin-typescript-client-provenance.json.
npm generated canonical package-lock.json from current upstream graph; all
existing package records are unchanged except the root SDK spec/new SDK record.
No sibling checkout, absolute local dependency or SDK registry request is needed.

Existing fetchNpmDeps cannot resolve relative file tarballs. Its local preBuild
validates source/provenance, saves canonical lock and omits only the SDK package
entry from temporary remote prefetch input. postBuild restores byte-identical
canonical lock in cache; the ordinary npm hook retains lock comparison and
offline npm ci reads/caches the source archive with makeCacheWritable.
No second committed lock, new fetch system, SDK prepare hook or source build.

Actual frontend cache hash:
sha256-utOpabPprstf97qzc/yre2O/EW36u6SsfS0o2Aas36k=.
Verified cache:
 /nix/store/6ri6jdfd2py0n3b2v0xwspxdsc1bwppl-vpsadmin-webui-frontend-1.0.0-npm-deps.
Canonical lock cmp passed. Existing sourcefilter retains vendor; installed public
allowlist excludes it. Full installed-package proof still awaits post-review run.
Update procedure uses new revision-qualified archive/integrity and regenerated
lock/hash, removes prior archive from current tree. Registry return removes
temporary hooks/provenance after an actually authorized publication.

## Source and documentation boundaries

HaveAPI owns transport encoding/decoding; generated SDK owns operation contracts,
namespaces, descriptions and pre-dispatch input checks. WebUI's RequestSpec policy
owns dynamic auth/language, BFF read recovery and public credential isolation.
Receipt-preserving output guards validate consumed fields; malformed post-write
output stays uncertain. Generic haveapi.ts wrapper/imports/callers are removed.

Source-backed visible corrections include unsupported filters/search, static host
assignment, mount create/edit fields, clone descendants, missing historical disk
series, earliest bounded StateLog, nullable settings/accounts, public correction
template eligibility and frozen advisory revision/serialized child readback.
contract-dispositions.md records exact backend evidence. ui-copy.md contains
lead-approved en/cs text; locked terminologya65a4dfe was used. No API widening.

Owning docs changed: docs/design/API_CONTRACTS.md, ARCHITECTURE.md,
CONFIGURATION.md, DOMAIN_COVERAGE.md, HAVEAPI_CLIENT.md,
IMPLEMENTATION_INVENTORY.md, PACKAGING.md, REQUIREMENTS.md and
docs/work-log/2026-11-01-typescript-client-migration.md. Read technical contracts,
update/rollback guidance and limits against actual code. Canonical KB workflow
was read; existing bindings cover legacy PHP, so no blind React pin refresh or
KB write was made. No screenshots or browser pass claimed yet.

## Quick evidence and remaining verification

Full refreshed ci:quick passes across preserved audit run and narrow typed tail:
toolchain, docs/inventory, lint/format, catalogs8376/language, structural budgets
without baseline/allowance growth, CSP/pages/architecture/strings/mutations;
application/tooling/E2E typechecks (100checked/182deferred), BFF6/6.
Logs w-unpublished-sdk-final-quick.log and w-final-typed-tail.log.
Six incomplete upstream test receipts were fixed by i4, five focused tests pass;
no provider/type weakening. Failed invocation/coverage logs retained in state.

Temporary support: source checker10/10; clean npm ci410packages18.2s; ESM import;
four SDK/policy/output suites38tests10.2s; real FOD/cache-lock comparison pass.
w-unpublished-sdk-prep-result.md, recovered complete log and final-quick result.
Post-upstream refresh: VPS/network11/11, IP72/72. Original owner-focused results
are recorded without summing overlapping batches. Source equality binds final
history fold; no unchanged checks repeated.

The committed scripts/integration/vpsadmin-sdk-contract.{mjs,rb,test.mjs} reuse
API Safety/Bootstrap/TestDb/SpecSeed/Puma, exact SDK and genuine HaveAPI transport.
Pure safety4/4 and JS/Ruby syntax pass. NO DB/server/matrix execution yet.
Proposed matrix is loopback, mounted,23calls(max30), separate identities/private
credential IPC, DB-only mutations and native server/TestDb shutdown. It covers
auth/current-user, capabilities/template roles, bounded user count/predicate and
isolated settings persistence/errors. It does not prove OAuth/BFF/browser,
VPS worker completion or deployed behavior. Review this glue before running it.

After review: existing full script/BFF/unit tests and production build; Nix
frontend+BFF/provenance/source/package-content checks; ordinary affected browser
workflows and real cs/en desktop/mobile captures; bounded isolated API matrix.
These are planned, not passed. No machine/deployment/session lifecycle action.

## Independent assignment and finding handling

Risk HIGH: authentication, tenant/public isolation, authorization-sensitive choices,
ambiguous/destructive writes and generated public contracts. All four lanes:
general; architecture/repetition; scope/proportionality; risk/compatibility.
Eligible retained reviewer0: read_only, saved Astra/xhigh, independent. No overrides.

Read mandatory-change-review/SKILL.md and all four references; inspect directly,
no nested agents. Start by comparing user scope with handwritten growth and
necessary contracts. Report concrete severities, lane, file/line and failure
scenario, plus explicit complete-history/update-stream/migration conclusions.
Return findings to lead; do not edit source. Blocking stops long tests; Important
requires fix or recorded decision. Original owners handle fixes; narrow direct
remedies are inspected/checked without unnecessary full review reruns.
