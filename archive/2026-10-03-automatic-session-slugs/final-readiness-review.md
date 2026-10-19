Team assignment from reviewer0 to lead:

Independent retained reviewer0 — FINAL whole-branch source and pin review
Session: 2026-10-03-automatic-session-slugs
Reviewer: saved review purpose / gpt-6.1-sol / xhigh / read_only. No override, fallback, implementation authorship or nested reviewers.
Overall High risk; general, architecture/repetition, scope/proportionality and risk/compatibility reviewed directly.

Findings, ordered by severity:
Blocking: none.
Important: R1 below.
Advisory: none.

R1 — Attachment prevalidation can publish ownership before the durable intent.
Lanes: general / risk and compatibility; shared validation/mutation ownership also affects architecture.
Repository/file: dev-workspace portal/internal/uploads/store.go:870–876, with transaction:217–223, compact:289–293 and prepareSubmission:992–1001; caller portal/internal/web/preparation.go:366–373.
Introduced in owning uploads commit802b3db0757ddc1e79aacc879842c6d2787a4be7; present at final66012154e45b1a5d79f32ffd5d505c535da2f99e.

ValidatePreparation passes the LIVE catalog to preparePreparation, which calls prepareSubmission and inserts the pending preparation submission plus updated file records. Returning changed=false does not roll these mutations back. transaction separately saves the entire mutated catalog whenever its prior compact call returned true. A concrete trigger is a ready upload still carrying its chunk checksums: Complete changes the state to ready, and the next transaction's compact clears those checksums. An expired/deleted unrelated record is another ordinary trigger.

Therefore a successful validation can already publish scope/initial/preparation:<requestId> with state=pending BEFORE savePreparationForDispatchLocked writes the accepting intent. If that subsequent intent write fails before rename (for example, write/fsync failure), there is no durable preparation record or predetermined receipt binding, while preparationMutation refuses further file mutations and the collector retains the pending files. Reconciliation scans preparations, so it cannot repair this orphan by itself; a surviving identical client can retry, but that is not the promised intent-before-claim recovery invariant. This can retain and lock an unaccepted upload indefinitely. The same unwanted publication can occur in the prevalidation transaction's own uncertain-save path. This is a source-proven control-flow defect; I did not execute a reproduction.

Smallest correction: make prevalidation nonmutating with respect to the catalog that transaction may save. Retain shared ready-file/ownership/wire validation, but separate insertion/update from that validation or evaluate the existing mutating helper on a properly isolated disposable catalog copy. Do not change the intentional transaction compaction or weaken pending retention. ClaimPreparation remains the sole owner of installing a pending claim after the durable intent.
Required regression: arrange compaction during ValidatePreparation (ready checksum metadata and/or an unrelated compactable record), prove no preparation submission/file-update side effect is published, then inject an intent-write failure before publication and prove no orphan claim/locked scope remains. Preserve the existing successful claim, replay, uncertain durability and continuous-retention checks. Existing preparation upload tests exercise ClaimPreparation but do not cover this mutating prevalidation plus compaction path.

Conclusion: the FINAL complete-branch source review is complete, but the source gate is conditional on R1 being corrected or explicitly discussed and recorded under the mandatory skill before new longer package/managed checks. No additional source, pin, commit-split, scope or migration finding was established. A previous incremental no-findings report does not close this newly identified whole-branch issue.

Reviewed exact ranges:
- codex-web4c170393a96ed0a6ac2e43488d073f6fcab36132 →32775fa7fdd9bc9b41aef74b7f195e5c3bc0f8d5.
- dev-workspace924c0ec28c41dd8b56aaf17f2212b302ca614899 →66012154e45b1a5d79f32ffd5d505c535da2f99e.
- vpsfree-dev-workspace8f8d8ecf5031c40d3e4a4ee2e9425721fc035800 →62841ca622cd5c2d9920671cd9cb4b50fb39e28d.
- workspacea51fa51e2e2503ce658003f75b77a5be1ff6c042 →32ca68c30f83661ae5de00cedd282061c084ed70; functional incoming base5c855f52412b2cf38bc0b998c370557dff76c07e.

Inspection and evidence:
Verified session identity against the trusted binding; both DEV_SESSION identity variables are absent. Read mandatory-change-review SKILL and all four references fully, workspace AGENTS and applicable projects/sessions/git/lifecycle/documentation/verification/deployment/knowledge-base/commits routes, affected repository instructions and documentation placement guidance. Read current plan/state, final-readiness-review-packet, complete branch inventory, final/incoming comparisons, retained related reports and native observation. Independently inspected actual committed objects/parents/messages, final code and consumers. No tests/builds/native/model/browser/VM, Git commands, source/record/ref/pin changes, deployment, approval, lifecycle operation or delegation was performed.

All complete final/incoming artifact hunks were checked against actual old and new committed blobs, including the large workspace tracking comparison: provider10 files, runtime46 final/43 incoming, extension25 final/2 incoming, workspace80 final/2 incoming. All postimages and changed-path inventories match the exact ranges; current tracked application-worktree bytes match their committed heads. Unchanged production/fixture/documentation conclusions carry forward after actual tree comparison, rather than treating prior report prose as sufficient proof.

General / public and runtime contracts:
Provider codex/ephemeral.go:73,317,356,419,686 and runtime portal/internal/web/session_namer.go:34,44 / session_name.go:111 / preparation.go:313,452,556 / preparation_store.go:316,384.
The provider owns the fixed supported Direct gpt-5.5/low profile, bounded private generation/thread/turn dispatch, exact immutable original catalog plus startup sessionFlags preflight, nonempty provider-owned instruction-file constant, static safe errors and cancellation/cleanup inside the original deadline. Runtime directly consumes that API/constant; model input is at most8192 raw UTF-8 bytes with no attachment metadata, whole naming budget10s including queue and two concurrent slots. Custom naming and deterministic fallback remain distinct outcomes. The portal owns one child lifetime and closes preparation workers before child teardown; no ordinary-socket fallback or respawn was added.

The fresh final inspection retained exact request/body/input-digest replay, captured settings, predetermined receipt/epoch checks, immutable reserved names, current-generation mutation checks, bounded compact mappings and browser recovery/separate-tab behavior. R1 is the specific exception to the intended durable upload acceptance ordering. It does not invalidate the separately reviewed model-action or native logging boundary.

Architecture / scope:
The provider owns reusable isolated-turn protocol/policy; runtime owns naming, child lifetime, preparation and browser behavior; extension adds site tools/providers through runtime mkPackage; workspace supplies site/team/cluster settings. Final generated updates stay in dependency units. There is no downstream reimplementation of the provider constant or speculative new configuration lease, native patch, model metadata rewrite, SQL framework, process manager or compromised-local-operator defense. The tagged PID/schema/diagnostic seams remain confined to demonstrated verification needs. No independent repetition/proportionality finding beyond R1's validation/mutation boundary.

Accepted logging and documentation:
Provider docs/reference.md:506,631,644,669; runtime docs/session-preparations.md:117,178,216,257 and docs/codex-package.md:115,148; workspace-portal links the owning preparation contract.
Lasting API, caller/file lifetime, original model/catalog, shutdown, replay/upload/older-reader and failure semantics are in owning project documentation. Prepared rollout, exact heads, historical attempts and diagnostic evidence stay in initiative records. The user's “ok, so use the local diagnostic logs” choice is resolved. Existing native plaintext input/identities may persist locally; ten-day startup pruning is not an erasure guarantee. Operational outcome/duration logs and normal preparation/history are distinct contracts. No new consent, external logger or assertion waiver is required by this review.

Final consumer/pin proof:
Runtime660 compared with reviewed952 changes ONLY flake.nix/lock, portal/go.mod/sum and nix/workspace-portal.nix vendorHash. Provider327 is unchanged. Extension628 compared with2e changes only flake.nix/lock; workspace's functional final diff from5c is likewise only those two files.
Runtime ordinary Go module selects v0.0.0-20261004060753-32775fa7fdd9, consistent with the provider's actual commit time/revision and flake pin. Old provider sums are removed; there is no committed replace/GOWORK workaround. x/net/html's existing v0.42.0 is merely classified direct for the managed-tag import.
Actual lock node sets are equal. Changed nodes are exactly runtime:{codex-web}, extension:{codex-web,dev-workspace}, workspace:{codex-web,dev-workspace,vpsfree-dev-workspace}. All other native/llm-agents/nixpkgs/cluster/team/site inputs remain unchanged.
Independently reconstructed canonical NAR SHA256 from the committed provider/runtime/extension trees; each equals its final lock narHash. The prepared vendor tree's canonical NAR SHA256 equals declared sha256-KlckfIvbzTtFvu31Fd5T/GYM/V7Es8Ks7yv/HZwEhOU=. Its17 public provider Go files and restriction policy match provider327 byte-for-byte. This checks source/hash consistency; it is NOT an executed fixed-output build.
Runtime flake/nix packaging passes the exact provider input/version to its pin contract and installs its non-test public resources plus policy. It installs the full original catalog read-only and checks its digest. Extension forwards runtime mkPackage, and workspace selects that extension with existing settings. Actual final closure/resource/native identities and managed lifetime still require package/VM proof.
If R1 is fixed and runtime history rewritten, update dependent exact hashes/vendor inputs as applicable, preserve protected ancestry, and refresh final comparisons/check evidence. The current supplied pin chain itself has no unresolved mechanical refresh.

Explicit FINAL complete-history / obsolete-history conclusion:
The complete series is coherent and its splits are independently reviewable:
- Provider: one final owning helper/test/docs commit32775fa7.
- Runtime: preserved consumed4ef298b3; uploads802b3db0; preparatione6837343; owned naming child/tests/docsb92129d3; ONE generated Go/flake/vendor stream117eaa78; browser recovery4753d90d; focused inherited test-event correction2eabff02; managed-service verification66012154.
- Extension: retained5b2e9a4b/101d3126/f50c92bf/399c3302 policy/maintenance/storage/verification ancestry, then ONE final dependency stream62841ca6.
- Workspace: tracking-only5c855f5, then ONE functional pin commit32ca68c3.

No obsolete incoming Luna/V8 utility, empty-instruction-file shim, superseded follow-up/fixup series or unapplied intermediate compatibility implementation remains in the final complete source histories. Earlier approach diffs in the explicitly historical tracking artifacts and retained backup refs are provenance, not extra incoming implementation commits. Provider native fixture corrections and runtime atomic evidence/docs are folded into their proper owning units.

I independently verified exact consumed runtime4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4 and extension399c33023a568a8d7a21e4e4df52829628720a28 as unchanged ancestors. Runtime schema1/policy3 contract bytes match the consumed runtime exactly; extension's entire functional subtree after399 is unchanged apart from dependency pins. Their published/deployed but unmerged lineage and supported maintenance/storage/bootstrap behavior are preserved, not rewritten.

Workspace remote-default history includes5c855f5 already on shared local master. Its78 changed paths are ONLY this initiative's records and six notes; no functional application/flake/config mutation is in that checkpoint. The final feature descends from it; functional incoming contains only flake.nix/lock. Recorded725=b382 rebase is patch-equivalent. No unrelated tracking deletion or default-branch feature integration is introduced. Final comparison capture remains required before any future authorized integration.

Explicit migration conclusion:
NO NEW MIGRATIONS in any reviewed incoming branch. Native SQLite0002 is external pinned DDL inspection, not a conversion shipped by this feature. Additive preparation version1 files do not replace existing creation receipt, upload catalog, manifest, namespace, lifecycle journal, host or cluster schemas. No transitional migration or schema-existence shim for an obsolete branch state remains. Consumed schema1/policy3 and supported predecessors are preserved; migration lineage is sound.
Older packages ignore preparation records and retain schema1 pending uploads, but cannot continue preparation UI/reservations and may create a competing destination; newer recovery must refuse that conflict. Recovery is a compatible forward update, not selection of an earlier user profile. Format compatibility does not excuse R1's pre-intent ownership publication.

Executed evidence and remaining gates:
1. Independently parsed retained full-runtime JSONL:948 pass events,0fail,2skip; wrapper/runtime exit files0. This was runtime952 with the explicit temporary source modfile, not final closure proof. Parsed final NORMAL-module focused JSONL:27 pass events,0fail/skip, terminal cmd PASS1.971s and web PASS1.332s. I do not invent an uncaptured parent process exit code. Managed-tag run was compile-only.
2. Retained real native log has ownership-control PASS0.13s and full TestEphemeralProtocolIntegration PASS17.89s, no failed-test headers. The safe metadata has39 fixed deny2→2 phases and two ownership cycles with2 direct waits/2 adopted reaps/ECHILD/init alive. Provider source327 is unchanged at this review. This is valid exact-source native proof under the accepted local-log exception, not an assembled final package/managed-service or live-provider proof.
3. R1 needs focused regression/source reconciliation. Full final fixed-output build must confirm the declared vendorHash, package/resource/catalog/binary contracts and normal CI. At assignment, provider CI37182636158 at327 succeeded; runtime37182904607 at660 and extension37182947726 at628 were running. I did not poll, await or claim their completion. No workspace workflow result is supplied.
4. Execute the prepared actual managed-service VM against the exact final candidate, proving startup/loss, HTTP failure, TERM/KILL/cgroup cleanup, held-worker cancellation and ordinary continuity. Compile/source review does not pass that gate.
5. Native fixture covers HTTP/SSE fallback. Successful WebSocket frames, continuation caches, reconnects and hostile WebSocket delivery remain untested. The unchanged-serving-transport positive MODEL result within10s, custom and durable replay/recovery canaries remain separate required live gates. Fallback is not MODEL proof.
6. Authorized user-profile deployment/profile switch remains future parent work, after applicable reconciliation and candidate proof. No system configuration change, default-branch merge approval or session archive/delete/stop is supplied. Final comparison capture remains pending.

The review completes the whole-branch assessment with R1 open. It does not declare readiness for use or deployment, waive unexecuted package/CI/VM/live gates, or authorize integration/lifecycle action. Parent records this report and owns remediation, exact downstream updates and verification. Reviewer0 is returning idle and available; session stays open.
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-automatic-session-slugs/
