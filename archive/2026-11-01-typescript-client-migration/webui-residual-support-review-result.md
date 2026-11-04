No Blocking, Important or Advisory findings in the completed residual-support affected review.

Reviewer and exact scope

- reviewer0, retained gpt-6-astra / xhigh / read_only, review-purpose member, ready in live same-session roster revision61; thread 01a19801-c630-7971-b7b9-cc178b6ced88. dev-session current from the bound session directory confirms 2026-11-01-typescript-client-migration; DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE are both absent. Workspace is /home/aither/workspace/ai/vpsfree.cz. No override, fallback or nested reviewer.
- Final affected range: 24ae8a8f681ed8d4df7e147d5179116113869628..b5c12bcd8afa67103ae05bd3fc993ad4fe14f256.
- Exact final tree: 5c5446624525afdf1fa1fcddeffb37fd051cb4ad. HEAD/tree match, worktree and index are clean.
- Complete branch: 63d484fc070dbee633d32624de545e834d483701..b5c12bcd8afa67103ae05bd3fc993ad4fe14f256, 36 commits, 513 changed paths, +15371/-10146. The affected delta is exactly four paths, +36/-8.
- Overall migration risk remains HIGH. All four affected lanes were performed directly: general/history, architecture/repetition, scope/proportionality, risk/compatibility. Read the current mandatory-change-review skill and all four references, repository AGENTS, applicable workspace guidance, complete packet and relevant state/design. Retained unaffected foundation/source/packaging/readiness/history conclusions; this is not a new exhaustive audit of 513 files.

General: correction and original evidence

The change at e2e/specs/app/vps_support_permissions.spec.ts:29 in b5c12bcd replaces only dns_resolver:'inherit' with null. Independently compared the entire old/new leaf: this literal replacement accounts for every changed byte. Original leaf SHA256 is 1d54f0d7d24590f6bdbe168fd2df8b23288156370ba43afa4c22e9eab41f32cb; final is d7691cb300b11ff874356815839d38d085bae491ee38784ae4cc901c126baa1a.

Read the selected retry-0 trace/context directly from the retained local ZIP, with nested members read in memory. Verified trace SHA256 c8ef7bfd9418662b7e9f06e778578e838db3e3c97e382a9df4c2acc9afdbff17, context 258a0ef448be782a6644c4c2810b1d54a4d95ee7e7398f4e6fc2c249c14f8bbf, and the embedded original source hash. GET /api/v7.0/vpses/123 returned HTTP200 with response.vps and dns_resolver:"inherit". The context shows Failed to load VPS, and the first overview assertion at line102 timed out. Recorded API requests are GETs; this trace proves no later tab outcome.

The selected99ee archive's package/dist/generated/resources/vps/actions/show.d.ts declares dns_resolver as Partial<Record<"id" | "label", unknown>> | null. Existing src/lib/api/vps.ts:66–71 and :117–118 reject a primitive relation but accept null; fetchVps at :221–227 retains output validation. VpsLayout renders its error state on that rejection. The corrected fixture conforms to the selected contract without weakening the production guard or changing support permissions. The form model already represents an absent resolver as the inherited/default choice.

Risk: role and assertion preservation

I inspected the complete scenario and the relevant reader, role and tab consumers, beyond confirming a one-line diff:

- Support identity21/level21 and foreign owner77 remain unchanged. The route remains /admin/vps/123. Existing role mapping resolves level21 to support, and VpsLayout permits mutation in admin mode only for admins.
- The overview must actually render, display the owner and stopped status, and omit lifecycle mutation/admin-only actions. An error page cannot satisfy these positive assertions.
- Configuration retains the permission message and disabled fieldset. Lifecycle retains action absence and direct-migration denial, including nodeRequests===0.
- Access retains hidden password/key mutation controls and the visible host-key section. Network retains actual interface/IP/host rows with edit/assign/PTR/free controls absent. Storage retains the mount row with create/edit/delete controls absent. Features and maintenance retain rendered data and absent editing/save controls.
- The final empty request list at :210 and its exact settings-PUT exception at :42 remain unchanged. The fixture supplies the API description at initialization; the inspected read-only tab paths use the existing reads and local capabilities. I found no reachable discovery request that would justify changing that assertion.
- No role upgrade, assertion removal, error swallowing, timing/lock bypass, mutation receipt weakening or test selection change was introduced.

This remains synthetic UI permission evidence. It does not independently certify backend authorization or establish that all later steps now pass; the original failed run never reached them.

Strict adoption and documentation

scripts/fixtures/e2e-type-coverage.json:141 and tsconfig.e2e.json:144 add the entire support leaf. Independently parsed old/new metadata: adopted140->141 and deferred142->141, with only that leaf's deferred record removed. All141 surviving deferral records and their ordering remain unchanged. Compiler options, extends, include, ambient/support inputs and checker are unchanged.

The baseline SHA256 is still 7bdc6a363a2706be14533e05712bda641aa709ce2413a4bd68ebe427ecec3317, and sourceRevision remains abab859d94a3f364d2bb719fa09f00749fd69ef9. No hash-only refresh, type allowance or local typing workaround was added.

The 33-line append at docs/work-log/2026-11-01-typescript-client-migration.md:655 accurately distinguishes original24ae CI, the first failure boundary, this correction, quick checks, and review/browser work still pending when committed. It does not claim a new-head browser or Nix pass. This is adequate documentation for a fixture-only correction; no product/KB/visible-copy change requires further documentation here.

Architecture and proportionality

Ownership remains correct: the generated client declares the API relation, the application validates its consumed shape, and the leaf fixture supplies a conforming value. No downstream provider reimplementation, shared fixture normalization, new helper, fallback, framework or production abstraction was added.

The one-literal repair, required whole-file strict adoption and factual work-log append are proportionate to the observed failure. They do not expand the user-authorized migration. The large complete diff is retained migration work, not new handwritten scope in this batch. The single new commit has one coherent purpose and a message explaining the resulting behavior and rationale.

Complete history, equivalence and repeated-input-stream conclusions

Independently enumerated the actual complete36-commit series and compared it with the packet and the35 commits through24ae. All35 are literally identical ordered commit objects; b5c12bcd is an ordinary single-parent child of24ae. No published history was rewritten by this delta.

Also reconciled the earlier fourth-CI review at b1b with the retained narrow-remediation receipts and actual b1b..451d diff: two explicit template Show handlers and two Start-body expectations aligned to {vps:{}}. Those corrections are folded into the owning unpublished lifecycle/power commit before the published24ae prefix; the final diff has no other hidden changes. The intervening24ae commit is a factual work-log append. Prior mapping/fold/direct-remediation conclusions remain applicable with their original ranges and evidence; b1b is not mislabeled as the current published ancestor.

The new commit repairs an inherited leaf that remained unchanged through the earlier migration and was exposed by the later published-head CI. It is not an obsolete alternative, replacement implementation or redundant fixup chain. With the retained complete-history conclusions and the inspected successor proof, no obsolete unapplied approach or additional consolidation is identified.

Independently inspected package/lock/flake/vendor history across the complete range. There remains one generated-client dependency/archive/provenance/Nix input stream at167f8531267a9eea3b11ed5fbdf85adda1f3c703. The other package.json change at8b648c84 changes the test command. b5c12bcd changes no input selection. Monotonic strict membership adoption is coverage expansion, not repeated generated dependency updates. No redundant pin stream requires consolidation.

Selected client99ee06654ef956a09b52749f4cd02d1435362087, generator eea3ae5e82c3db23d5f5bc9f1a5e7784117c4e1b and HaveAPI runtime0.32.0 remain. I inspected the archive declarations and generator metadata, and verified archive SHA256 f3bb42d0392fb738f5c70fe1415cc8742ab943a31c2ed2a85af5ccbd385d831f. Package/lock/flake inputs are identical to24ae. Separate HaveAPI/master integration atf29c is not silently adopted by this WebUI.

Migration and compatibility conclusion

No database, schema or persisted-format migrations exist in this affected delta or the retained complete branch migration inventory. The migration-named source paths are VPS migration-plan API consumers, not DB migrations. No transitional migration, schema-existence workaround or new release/deployment/consumed-state boundary is introduced. Existing API migration provenance remains historical contract input.

The affected change is compatible with the selected archive and current reader; it changes no application/API behavior, wire protocol, public interface, dependency, deployment ordering or rollback requirement.

Verification evidence and residual limits

- Inspected w-residual-support-strict.json (SHA256 4b77d5338d09e6ba9bf023f753633c7cb908610002e8662ce543570ae22f3a0e), its log and the commit receipt (f0729baef78cbe30d51c5093a9480123291617459dbd920342c1c4e6c61b3edc). The existing combined strict gate exited0 in11.998605s,141 checked/141 deferred, zero diagnostics, one attempt. It ran on working inputs based at24ae; I matched their hashes to the committedb5c bytes. This is byte-bound quick evidence, not a falsely relabeled literalb5c execution.
- Scoped ESLint exited0 in2.14233s; formatting/docs/whitespace results are retained owner evidence. I ran no checks.
- The subsequently available fifth-ci-support-preflight.json records one exact Chromium identity, matching the original failed ID/title and line32, no errors/duplicates/omissions, and empty actual_results. This is enumeration only.
- No native browser pass onb5c is established. The parent-owned whole-scenario Chromium gate remains necessary, including the later positive and negative tab assertions. Source inspection cannot replace that execution.
- Original24ae core CI and smoke totals retain their exact original scope. Prior136 local acceptance remains114 actual451d passes plus22 proven unchanged historical passes; it is not a new137 aggregate or a b5c pass.
- Literal24ae Nix/input-graph evidence does not establish literalb5c packaging provenance. Exact-final-head packaging/CI and broader readiness remain separate.
- Earlier isolated API evidence, historical API2 cleanup uncertainty, and limits concerning real authorization, OAuth, workers and deployment remain unchanged. No absence-of-effects or lifecycle claim is added by this review.
- A compatible actually published client is still required before merge under the user's separate release decision. This report supplies no registry selection/publication, WebUI/client default integration, deployment or session lifecycle authorization.

No finding blocks the parent's bounded native Chromium gate for this exact candidate. Parent owns acceptance, direct remediation if needed, and launch. Review remained read-only: no source/file/index/Git mutation, tests/builds/install, downloads, browser/CI/API/DB/server execution, publication, merge, deployment or lifecycle action. Session remains open.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/
