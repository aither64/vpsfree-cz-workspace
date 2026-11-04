No Blocking, Important or Advisory findings in the completed released-client transition review.

Reviewer, scope and decision

- reviewer0, retained gpt-6-astra/xhigh/read_only, ready review-purpose member in live roster revision61, thread01a19801-c630-7971-b7b9-cc178b6ced88. dev-session current confirms2026-11-01-typescript-client-migration in /home/aither/workspace/ai/vpsfree.cz. Both DEV_SESSION identity variables are absent. No override, fallback or nested reviewer.
- Exact affected range: b5c12bcd8afa67103ae05bd3fc993ad4fe14f256..4ed519b69c422ea6b4fd0bd7bf490a20fcd6983e.
- Final tree: ea57e42fa2ebdd3b85895ce114eeb067c379b593. HEAD/tree, clean worktree/index and all11 changed/deleted receipt entries independently match.
- Complete branch: 63d484fc070dbee633d32624de545e834d483701..4ed519b69c422ea6b4fd0bd7bf490a20fcd6983e,37 commits,511 changed paths,+15248/-10183. Affected delta is11 paths,+210/-370, including deletion of the337414-byte candidate archive.
- Overall migration risk remains HIGH. All four affected lanes completed directly: general/history, architecture/repetition, scope/proportionality, risk/compatibility. Read current mandatory-change-review and all four references, current WebUI instructions, applicable workspace guidance, packet/addendum and relevant plan/state/design.
- Unaffected foundation/source/packaging/readiness and prior complete-history conclusions are retained within their original scopes. No exhaustive reaudit of the complete511-path migration was necessary.

The exact candidate is suitable to proceed to the parent-owned final packaging checks. This is not a package-build, preview-activation, CI or current-main integration acceptance.

General correctness and release evidence

package.json:85 and package-lock.json:6994 select exact vpsadmin-typescript-client0.3.0, its canonical registry URL and the actual release SRI. Independently parsed the old/new locks: only the root client selector and client package record change; all484 other package records are identical. The HaveAPI0.32.0 peer/runtime and XMLHttpRequest lock remain unchanged.

I inspected the retained published archive directly in memory and compared it with the old archive read from the immutableb5c Git object, rather than relying on the shared0.3.0 version:
- Release archive:337128bytes, SHA25657236647f4065a0ffeaabb0f5f6c64370a5ca4e7e530876b0d562c69651ce610.
- Computed SRI matches the new lock: sha512-jZKO+c9azQqwXYLMp+yCl54pqhjyGDVr6rxOzq2rjusEBQ8Xm5dCdc8a2iHV5buUq8hc6835tmF5wjlP8/HJ/A==.
- Both archives have the same1360 regular member paths, with no duplicate, escaping or nonregular entries.
- All1352 dist JavaScript/declaration files are byte-identical. The API7/protocol2 schema is identical, as are all675 generated ownership hashes.
- Exactly six entries differ: README.md, package.json, schema/provenance.json, schema/tooling.Gemfile.lock, src/generated/.haveapi-generated.json and tools/generator.json.
- Package-manifest differences are development compiler scripts/dependencies. Public exports, module type, runtime dependencies/peer and shipped entrypoints are unchanged; no new install-time behavior is introduced.
- Independently compared the current installed client: all1360 regular files and their path set match the release archive, with no installed client symlinks.

These comparisons support retaining prior generated-program/interface conclusions, including operation descriptions, namespace handling and pre-dispatch errors. They do not equate different source revisions.

Inspected the retained registry metadata, public tag response, source package/generator records and decoded npm-reported attestations. The canonical release/tag binds client sourced354491537f8b654b4d2c33a705cad84474f95d6 to release run41538988296; its subject digest matches the archive. Archived public-source package/generator records match the shipped records. Release generator1ef9b204ba45bb261d3334be5c555cc1856b713b, generator/Ruby version0.32.2 and API capture5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5 remain distinct from oldeea3/API610 and the separately mergedf29c. The consumer peer is still haveapi-client0.32.0. I performed no network query or cryptographic Sigstore verification; the documentation states that limit accurately.

Architecture, removal and preserved safeguards

packages/frontend.nix:10–25 returns to ordinary buildNpmPackage dependency fetching with the exact prefetched root hash sha256-e/oJZ1x+TRpjIw1DhoTLCJiQ2ifm4VednmrI201+ayQ=. The custom npmDeps lock projection, cache-map delegate/hook override and writable-cache setting are removed together. No dangling executable reference to the deleted adapter remains.

The source checker still runs in prePatch, before frontend installation/build. Its required application/audit source checks, recursive private/generated-path and symlink refusal, HaveAPI manifest/lock/provenance checks and exact locked XHR protection remain. Source-filter, public-output allowlist, BFF packaging and shared provenance implementation are unchanged. Only the removed unpublished-client/archive mechanism loses its specific validation and tests.

scripts/check-package-source.test.mjs retains six applicable cases, including missing-source rejection, generated/private/symlink rejection, external-symlink rejection, HaveAPI substitution refusal and missing transitive-integrity refusal. The removed cases exercised the now-absent local archive/cache-map mechanism. No production negative assertion, role guard or uncertain-write test changed.

This restores ownership to npm's locked artifact-integrity handling and the ordinary Nix dependency fetcher. A replacement registry validation framework or optional archive mode is unnecessary for this boundary. Provider/generated behavior remains upstream; WebUI retains its existing request policy and domain guards.

Scope and documentation

The11-path change is proportionate to the user's newly authorized released-client adoption. The manifest/lock/hash update, removal of incompatible temporary file-cache support and matching documentation form one coherent, independently reviewable transition. It reduces maintenance surface and adds no application feature, fallback, runner, role policy or preview mechanism.

docs/design/HAVEAPI_CLIENT.md:59 and PACKAGING.md:10 now describe the selected registry dependency, ordinary installation/hash workflow, program-versus-source equivalence and rollback of a matching source/manifest/lock/hash set. The standard optional npm build/pack/no-save override, exact generator-HEAD guard, peer/entrypoint checks, warning about other temporary dependencies and npm ci restoration remain. There is no new link mode or Nix override mode.

REQ-068 alone is reconciled. The dated work-log append at docs/work-log/2026-11-01-typescript-client-migration.md:688 records actual installation/quicks and pending review/build/preview. The old provenance link at:205 now targets the immutableb5c source; historical claims remain historical. Retained old anchor IDs preserve existing links. Current instructions no longer depend on the removed candidate archive/provenance file.

No product-visible behavior/copy, localization or KB/media changes occur. Documentation accurately distinguishes published source provenance from old program-byte equivalence and does not anticipate deployment.

Risk and compatibility

Actual application, BFF, public files, browser fixtures, shared policy/guards, strict-coverage inputs, flake/API/localization pins and HaveAPI provenance are unchanged. Together with exact distributed-code/declaration equality and the unchanged peer, this supports a compatible distribution transition without a new API, role, secret-handling, receipt or no-replay behavior.

The required-source/private-path/symlink security protections are preserved. Installation still uses the exact package-lock integrity; the release is not selected through a mutable dist-tag or floating version range. The removed local-archive path no longer participates in the final source or dependency cache.

The released-client selection prerequisite is now evidenced. That does not establish final packaging, actual serving bytes, live API authorization, OAuth behavior or production readiness. Newer recorded generator/API provenance alone does not mean the runtime or backend was repinned.

Complete-history and repeated-input-stream conclusions

Independently enumerated all37 actual commits and compared them with the packet and prior36-commit series. The complete36-commit published prefix throughb5c is literally preserved, in order. 4ed519 is its ordinary single-parent child. The commit message explains selection, removal, compatibility and documentation; there is no fixup chain or bundled unrelated behavior.

There is now ONE generated-client input stream with TWO deliberate stages, not an absence of repeated updates:
1. 167f8531267a9eea3b11ed5fbdf85adda1f3c703 supplied the explicitly authorized unpublished99ee artifact and the packaging support needed by the pre-release migration.
2. 4ed519b69c422ea6b4fd0bd7bf490a20fcd6983e adopts the subsequently published0.3.0 artifact, with its own digest/source provenance, and removes that temporary packaging support.

I accept this as a concrete external release and user-scope boundary, not a redundant debugging pin sequence. The old stage represents the deliberately supported unpublished input while release adoption was held; the new release did not supply that input at the earlier milestone. Replacing the earlier selection retroactively would conflate those supported inputs/provenance and rewrite the protected published series. Retention is not justified merely by prior CI, deployment or branch publication. Repository instructions also forbid rewriting those published objects without exact authorization, which is absent.

The archive stage is superseded in the final tree and intentionally retained only in the protected history and original evidence. No obsolete archive implementation, alternate input mode, redundant intermediate candidate pin or unexplained transitional path remains active. No additional consolidation is required for this bounded successor. The other package.json-touching8b648c84 changes a test command, not a separate dependency stream.

Migration conclusion

No database, schema or persisted-format migrations occur in this transition or the retained complete branch inventory. The migration-named source files are VPS migration-plan API consumers, not DB migrations. No transitional schema step, compatibility guard, conversion, new externally consumed state format or rollback-state boundary is introduced. API source/provenance differences in the released artifact are not WebUI schema migrations.

Quick evidence and verification limits

- Independently matched all committed/deleted entries against w-registry-transition-commit-receipt.json and matched quick receipt input hashes to the final Git blobs. The other2569 tracked entries are unaffected.
- Release-proof receipt SHA256a68b00e09dc99a6f138b4776c13b52329a0ca8dbb58b5eeb10d7f15a56ecc8f0 matches. Installed/archive comparisons were independently inspected as above.
- The retained dependency batch exited0 in93.806s and its log reports the exact hash now in frontend.nix. This is dependency preparation, not a successful frontend/BFF build. The first watcher refusal had no native install execution and remains separate historical evidence.
- w-registry-transition-quick.json SHA25679872c5896f2f469b1bff820a757c051d72bcae49ea29bc1df67f2ba129e8548 and its matching log record six checker tests and100 policy/wire tests passing, application/tooling strict and E2E strict141/141 with zero diagnostics, lint/format/Nix syntax passing. Total83.942s. These ran before commit on byte-bound inputs now committed unchanged.
- The final docs receipt/log records successful formatting,257 routes/73 API modules/177 documents/76 requirements and whitespace checks. The first deleted-link audit failure and misleading aggregate shell exit are honestly retained; the actual docs-only correction/recheck resolved it. No source-test success is inferred from the earlier aggregate shell exit.
- Native npm output retains12 moderate advisories, the existing bundled-WASI cache warnings and its esbuild install-script warning. No unrelated dependency repair was introduced. Final packaging is the next acceptance boundary.
- I ran no checks/tests/builds or installations. Exact4ed519 frontend/BFF/provenance/source/package realization and input-graph/installed-metadata evidence remain pending. Oldb5c Nix success is not a new-head pass.
- Repeating the entire browser matrix or isolated API database campaign solely for this byte-identical program transition is not warranted by the inspected delta. Prior actual executions retain their original inputs; the affected installed-policy/type checks and pending package/preview verification cover the changed distribution boundary. Any new failure requires its own evidence-based disposition.
- Session preview is user-authorized but not started or certified by this review. Parent owns the standard session preview and its actual final package/source/serving verification. Selection labels or planned commands alone do not prove activation. Historical API2 cleanup uncertainty and other prior evidence limits remain unchanged.

Fresh-main boundary

Read the packet addendum and publication-preparation receipt SHA256f7fac644068808e482427e51aa64f5587850ec615ac31fe8bca2231529021746. Independently inspected the available Git object: authoritative main1c8478bceb3943645ec06ccde895ee4b0985873f is a child of recorded63d and changes50 paths. Its intersection with this11-path registry delta is only docs/design/REQUIREMENTS.md. This does not establish non-conflict or compatibility for the full migration.

The reviewed candidate remains exact4ed519 on the original63d base, with no source substitution or rebase. I make no readiness-to-merge-current-main claim. Fresh upstream reconciliation and appropriate review/checks remain an integration dependency; the newermain work is not silently included in the requested session preview. No default integration grant exists.

No finding blocks the parent-owned final package checks for this exact candidate. Parent owns acceptance and subsequent preview release. Review remained read-only: no source/file/index/Git mutations, checks, builds, installs, downloads, probes, browser/API/DB/cluster/CI execution, publication, merge, production deployment or lifecycle action. Session remains open.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/
