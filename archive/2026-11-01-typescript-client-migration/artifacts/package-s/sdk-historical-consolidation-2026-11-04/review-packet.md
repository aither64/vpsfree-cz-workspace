# Client historical consolidation — independent history review packet

Requested reviewer: retained reviewer0, saved Astra/xhigh/read_only. Parent owns assignment; no reviewer was started by implementer1. Requested lanes: GENERAL plus RISK/SCOPE for history, successor coverage and compatibility. Read the current mandatory-change-review skill and relevant lane references. This packet supplies evidence for independent assessment, not a claim of final acceptance. The operation has no new authored content; the lineage includes cross-project API contracts, so retain the high-risk compatibility context while keeping review bounded to the final historical disposition.

## Request and authorized boundary

The user selected released client 0.4.0 for the completed WebUI/configuration migration and requested final accounting. Lead authorized only local historical client branch consolidation to already-integrated public source. SDK/default integration and publication were neither required nor performed. Parent owns session completion/state. The session stays open.

Repository: `git@github.com:vpsfreecz/vpsadmin-typescript-client.git`.
Registered own worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/vpsadmin-typescript-client`.
Registered branch: `2026-11-01-typescript-client-migration`.
Original registration base remains `e5786f69b7c223c3bb5b1de99b7f97186eec368a`.

Accept only a supported public successor conclusion. Do not call old e166 literally merged, old/new complete trees equal, or the two ranges patch-equivalent. Do not replay obsolete candidate inputs, infer a new release, or add source/tests/builds/review campaigns merely to make history look alike.

## Exact ranges and commit inventory

Original reviewed range `e5786f69b7c223c3bb5b1de99b7f97186eec368a..e16663a9e7ed1bbd7e25337b824283f635f47395` has two commits:

1. `99ee06654ef956a09b52749f4cd02d1435362087` — Generate version 0.3.0 with live descriptions and typed metadata. Full fixture generation, shared executor/live descriptions, typed extensible global metadata, pre-dispatch ClientInputError, configurable metadata namespace, receipt preservation, recorded provenance and strict consumer verification.
2. `e16663a9e7ed1bbd7e25337b824283f635f47395` — docs: use generated client wording for live descriptions. One README sentence and wrapping only.

Selected already-public range `e5786f69b7c223c3bb5b1de99b7f97186eec368a..c53cb4dabb0b3aac8d05834478872d2cfa698fa7` has four commits:

1. `d354491537f8b654b4d2c33a705cad84474f95d6` — Regenerate the TypeScript SDK for HaveAPI 0.32.2 as version 0.3.0.
2. `ec08ec18c4d9ba9f4f311cfb9e5af12fd4f01c97` — Refresh generated advisory operations from the current API schema.
3. `2071a164eab6a7681c5ba35542768c8a5e16251b` — Cover guarded advisory mutations through the published runtime.
4. `c53cb4dabb0b3aac8d05834478872d2cfa698fa7` — Prepare version 0.4.0 for the added advisory operations.

Selected tree is `c85e30b1fc1ae27bba9c08884e11fa78bbb15f7b`; old e166 tree is `2cafe84faeecb0e4ff52291ec874d236dc4880b1`. Final owned change range is **c53..c53, zero commits and zero diff**. The old-to-public tree delta is 27 paths, +1179/-376. Raw author/committer/parent history, full per-commit binary diffs, cumulative binary diffs, range-diff and stable patch IDs are retained in this directory. [History disposition](history-disposition.json) maps old candidate commits to their supported successor purposes without asserting patch equivalence.

## Source and artifact coverage

[Actual Git source evidence](source-coverage.json): e166 versus first public 0.3 source d354 differs under `src` only in `.haveapi-generated.json`; all **675** owned generated source hashes are equal. Selected public c53 still has byte-identical `src/generated/runtime.ts`, `descriptions.ts`, handwritten root adapter, sole regenerate command/source loader and release workflow compared with e166. Exact blobs are recorded.

The retained [0.3 proof](../published-client-proof-2026-11-03/release-proof-receipt.json), SHA256 `a68b00e09dc99a6f138b4776c13b52329a0ca8dbb58b5eeb10d7f15a56ecc8f0`, independently bound canonical published d354 artifact to all **1352** identical compiled JS/declarations from historical99ee. This includes descriptions, metadata projection/namespace, input errors, unchanged executor identity, receipts and no-replay behavior.

The retained [0.4 proof](../published-client-proof-0.4.0-2026-11-03/release-proof-receipt.json), SHA256 `cf45d568e9c2560915b9c4dbe95359e9313cb1aae2122d5bfa1b2badee6a9952`, binds canonical338234-byte tarball SHA256 `3a6f2a2a6f4eaeb31f490035b312e9b5403cf21589d649dc1fd31d60b64e1906` to annotated public tag object `296d286401ec2b456919c406f9fd90461529119d` and source c53. npm-reported provenance was inspected; cryptographic Sigstore signature verification was not performed.

0.4 adds exactly two advisory actions (Retract/Delete) and seven optional non-null expected_state inputs on advisory Update, CVE C/U/D and nested node-status C/U/D. No existing schema field was removed or modified. Existing required revisions/help/namespaces/receipts/error/no-replay behavior remains. Common dist counts are1333 identical,19 changed,4 added,none removed. Exact HaveAPI JS peer/dev remains0.32.0. Public generator is `1ef9b204ba45bb261d3334be5c555cc1856b713b`/0.32.2, distinct from historicaleea3; API capture is `942c6eaed41331f823d8e0f670ed239e2b308440`, schema SHA256 `d6ec617653913c56e92398a6032aa350118597a0e3f45c599bc92b6071ea0a26`, six plugins,151resources/521application actions plus authentication1resource/5actions.

The released README replaced the old paragraph editorially but retains generated-client terminology, permission-filtered descriptions, input-error/uncertain-write and no-replay meaning. Public source also replaces some consumer tests/docs, removes the development-only TypeScript5.9 alias/extra npm script and standalone haveapi.mjs fixture, and records updated provenance. Its runtime consumer contains actual mounted HaveAPI0.32 description/metadata/read/write and guarded-advisory tests. It is not a literal test/doc superset. Previously executed old foundation and current W/release acceptance results keep their exact scope; no tests were rerun or relabelled by this operation. Old installed ignored outputs are still historical.

## Preservation and performed operation

Fresh canonical SSH observations before and after show main remains c53 and published feature remains e166. Original e166 remains remotely reachable; local expected-absent preservation ref `refs/heads/2026-11-01-typescript-client-migration-historical-e16663a9` was atomically created at e166, retaining99ee ancestry. All other refs remain unchanged. Old artifacts/reports were not edited. The selected feature was moved by ordinary **zero-commit** `git rebase --no-update-refs --onto c53 e166 2026-11-01-typescript-client-migration`, exit0. No reset/clean/stash, hook bypass, new commit, remote push or default mutation occurred.

The repository has no AGENTS or declared hook framework; core.hooksPath and rebase.updateRefs were unset, hooks contain sample files only. Normal Git2.54.0 and configured contributor Jakub Skokan were retained. Explicit --no-update-refs protects all other branches. Final tracked files/index/blob/modes equal public c53, index/worktree are clean, no operation/lock markers remain. All1743 ignored entries (60878305 regular-file bytes) have unchanged names/modes/content/symlink targets. Historical build/node_modules inputs were preserved without asserting they are newly built0.4.

Ordinary comparison capture succeeded with explicit e578..c53; portal.yml bytes and original initial_base_sha stayed unchanged. [Receipt](receipt.json) records all commands, identities, remote observations, preservation and hashes. No compile/test/runtime/build/evaluation/install/regeneration/check campaign ran. Exact committed/live source equality and ancestry are the bounded quick evidence.

## History, migrations and independent question

There is one superseded unpublished generated-client input stream in the old selected series,99ee plus its README follow-up. The user-selected public0.4 successor is already released/integrated and preserves the intended generated behavior while adding the required advisory contracts. It replaces that candidate stream without altering main or rewriting public release history. Historical exact artifact/provenance refs remain available for recovery and old receipts remain truthful. There are **no SDK DB or persisted-state migrations** in either complete series; schema/export provenance lists are capture evidence, not new migrations or execution. No application/cluster/configuration state changed here.

Independently assess whether this successor/preservation disposition correctly closes the old candidate source obligation, with no unique necessary client deliverable omitted and no unsupported literal-integration/equivalence claim. Review the complete old/new histories, intentional tooling/docs differences and accepted release scope. Do not infer this report is your conclusion; report findings or residual gaps to parent. Parent owns final acceptance and session state.

Previous source review context: [foundation final review](../../../foundation-review-result.md), including lead-accepted narrow R1/A1 remedy; [terminology final review](../../../local-client-terminology-review-result.md), explicitly e578..e166 and no migrations. Old release/source/run receipts and current lead adoption acceptance remain in the same session. The canonical0.4 proof is static artifact/source evidence; broader current W acceptance is parent-owned and not rerun by this package.

SDK source/Git/index turn is explicitly returned with no running/uncertain operation. [Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/) remains open.
