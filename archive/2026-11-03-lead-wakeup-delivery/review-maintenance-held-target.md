# Final affected review: held-target compatibility repair

## Findings and R1 disposition

No new Blocking, Important or Advisory findings in the completed affected repair.

The Important R1 from review-maintenance-cold-completion.md is resolved at 40c342f924561d6ed3f3632bdff8463ce8bb2d3d within this source/quick-check boundary. The cold-completion source now requires an explicit held-target behavior capability; policy1 reader compatibility no longer supplies that guarantee. Preparation, fresh validation, operation creation, actual recovery-target activation admission and target self-activation all preserve the requirement before the relevant effects.

This closes R1 for the current protocol. It does not retrofit new semantics onto old SourcePackage owners or certify native task/mail preservation, canonical positive cutover, full automation or live deployment.

## Identity, settings and exact reviewed scope

Retained independent reviewer0; purpose review, saved gpt-6.1-sol / xhigh / read_only, same-session roster ready. No override, fallback or nested agent.

Before session records, dev-session current from /home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-lead-wakeup-delivery printed exactly 2026-11-03-lead-wakeup-delivery. Both DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE match that slug and the trusted developer-bound workspace /home/aither/workspace/ai/vpsfree.cz.

Repository: git@github.com:aither64/dev-workspace.git.
Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-lead-wakeup-delivery/dev-workspace.

- Affected range: fb7820b3ddda043c4e5053201726e0fc02939d78..40c342f924561d6ed3f3632bdff8463ce8bb2d3d.
- Actual HEAD:40c342f924561d6ed3f3632bdff8463ce8bb2d3d.
- Actual tree:4b163546f23ade0468004c086c5a66059dfeba65.
- Direct parent:3145caa8fcf23b1e825eb54fe9176258f58c6b7f.
- Affected diff:12 paths,+322/-26.
- Complete owned range:3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7..40c342f924561d6ed3f3632bdff8463ce8bb2d3d; five commits,124 paths,+26244/-162.
- Merge base is exact3bb. Actual worktree/index is clean and checked code matches the committed code.

Overall risk HIGH: host activation, mixed-version capability admission and two persisted recovery consumers. I independently applied general, architecture/repetition, scope/proportionality and risk/compatibility. I read the current top packet, state, sufficient design2675+ and rescue clarification, repository instructions, mandatory skill and all four references; applicable unchanged procedures were reused where permitted.

The previous fb source review and earlier reports/closures are reused only where unchanged. No unrelated SDK, native producer or whole-runtime implementation audit was repeated.

## General lane: exact gate behavior

The additive runtime descriptor field is maintenanceHeldCompletionPolicy with supported integer value1. Existing maintenanceStateSchema, maintenancePolicy and maintenanceMcpPolicy remain1.

The actual gates inspected are:

- workspace-host:713 checks the exact candidate at the end of preparation when the established maintenance-transition predicate applies.
- workspace-maintenance.rb:110–114 extracts the previous start eligibility without changing its conditions; start_maintenance_switch:193–194 checks capability before operation construction/control, rooting or worker launch.
- workspace-host:742 rechecks the actual prepared target during fresh validation, including an existing maintenance worker. Its source-recovery preparation substitution is retained, so this is not a cached candidate boolean.
- maintenance_control.go:443–454 binds the prepared candidate to the operation candidate and requires capability before store creation or observer retention.
- maintenance_control.go:590–612 chooses the actual candidate or retained source target according to SourceRecovered, retains exact requested package/native/plans equality, and checks that actual package before writing activation intent.
- workspace-host:1210–1211 checks the executing target's capability for a nonterminal operation before install_links or service configuration. Existing held deferral and generic-restart refusal remain.

The Ruby predicate at workspace-maintenance.rb:100–107 uses the bounded strict descriptor reader and exact Integer1. The Go predicate at maintenance_control.go:155–194 bounds the descriptor to64KiB, requires an object/valid complete JSON through the existing decoder, rejects duplicate top-level descriptor keys, and accepts only exact integer1. Missing, null, string, floating, boolean,0 and unknown2 values refuse. There is no fallback from reader support, no-state startup, native version or the capability's absence.

Preparation may still build/inspect/probe its source as before. The pre-effect guarantee here concerns maintenance operation creation, pause/drain, worker/rooting, selection and activation effects; the implementation/docs do not falsely promise a side-effect-free build preparation.

The source-backed regression tests cover refusal and supported values at the real Ruby and Go boundaries, changed prepared target, both actual activation-target branches, ordinary startup-only behavior, held startup and retained recovery. The capable fixture now constructs its immutable creation tuple before Store.Create rather than mutating it afterward; the original failed log is preserved.

## Architecture and repetition lane

This is one finite behavior declaration in the existing descriptor, not a new registry, capability discovery service or native API. It belongs to target host activation behavior. Reader compatibility and source-native admission accounting remain separate responsibilities.

Ruby shares one held-target predicate across its existing boundaries and one extracted maintenance-switch eligibility predicate across preparation/start/fresh checks. Go owns its corresponding control boundary and uses one local bounded predicate for prepare/activation. The cross-language validation is intentional at two existing executors; the authoritative supported declaration remains the installed descriptor. The tests cover strict value semantics on both sides.

Legacy SourcePackage forwarding remains ahead of semantic dispatch in maintenance_control.go:60–76; the new gates are inside the resolved owner's worker implementation. Ruby worker dispatch to the retained SourcePackage likewise remains before worker claim and phase processing. Therefore a new selected target does not apply its new admission interpretation to an old source-owned operation. Missing owners still refuse.

The actual SourceRecovered branch checks its retained source package rather than CandidatePackage or the latest profile. Existing requested/prepared native/plans and operation identities remain mandatory.

The two descriptor equality projections have narrow ownership:

- Failed-creation recovery at workspace-host:1044–1051 retains raw executing_contract equality against RUNTIME_CONTRACT, then compares projections under the existing turnRetrySessionPolicy exception.
- Archive recovery at workspace-host:1111–1113 retains raw current-target equality and original lifecycle/flag checks.
- Both use maintenance_recovery_contract at workspace-maintenance.rb:489–495, which validates a present additive value as exact integer1 and omits only this one field. An absent field is accepted only in these unrelated recovery comparisons.

Searches found this projection only at the two intended consumers. It is not used for maintenance admission and never inserts a default1. Other historical descriptor and identity checks remain.

## Scope and proportionality lane

The user retained coupled wakeup delivery plus full automatic pause/resume while challenging the overall changeset size. R1 required a concrete cross-generation distinction: an older policy1 target can otherwise reopen writers before cold proof. The repair stays within that defect.

Production is four paths,+99/-9; six test paths and two owning docs support the contract, its necessary comparison fallout and refusal cleanup. The additive declaration avoids conflating a new host behavior with unchanged journal/MCP reader policy. It introduces no new journal marker, scheduler, compatibility framework or diagnostic subsystem.

The rescue adjustment is directly necessary for truthful target pre-effect refusal. workspace-host:1200 initializes an invocation-local effects_started=false; line1221 sets it immediately before install_links; rescue:1237 rethrows immediately if that invocation never entered activation effects. This preserves an existing autoarchive timer on capability refusal. Setting the flag before the call preserves the original cleanup when install_links fails after partial mutation. It does not authorize unrelated cleanup or generic rollback.

The full branch remains large and full automation is not yet accepted. Closing this bounded contract finding does not settle whole-feature minimality, choose the pending native-mail product behavior or authorize further native implementation. No optional framework or additional diagnostic mechanism is recommended.

## Risk, compatibility and recovery

The new capability promises held target startup/reconciliation and delayed restoration for the owning nonterminal maintenance operation. It is not completion proof, native pause support or authority to continue work.

Old/missing/unknown targets are refused by the new cold source at admission rather than relying on an incapable target to reject itself after selection. Target self-check supplies an independent boundary for capable executors. Existing source/token/registry/claim/startup and prepared target/native/plans checks are preserved.

Ordinary nonmaintenance switches and startup-only records without a real maintenance operation retain their existing behavior. The two unrelated recovery comparisons remain usable with older descriptors absent the additive field, while malformed/unknown present fields refuse. Current executing-target descriptor equality remains exact. This distinguishes compatible reader/state recovery from admission to a new behavioral protocol.

The focused Ruby refusal regression uses a real preexisting timer symlink and requires it remain intact with no install/service/cleanup command. The partial-install/configuration/timer failure cases preserve the original compensation and primary error. Thus early refusal does not mutate the retained timer, and partial effects still receive their previous cleanup.

No operation/journal/MCP/on-disk conversion is introduced. The runtime descriptor changes add one supported behavior field; schema1 reader policy is unchanged. Historical operations remain with their retained owner and original semantics, including limitations; no unsafe automatic conversion or retroactive repair is claimed.

The owning docs now state the exact capability/value, source and target checks, source-recovery choice and distinction from reader compatibility. The MCP guide links to the update guide rather than duplicating a version history. Existing entry links and native prerequisite explanations remain.

The native task/admission handoff, memory-only accepted child mail, unreported-cell limitation and lack of canonical positive cutover are unchanged. The pending native-mail product decision remains unresolved. No actual source/target activation, mixed-version package roundtrip, mailbox guarantee or whole automation success follows from these source/unit results.

## Whole-branch history, consolidation, repeated streams and migration lineage

Actual complete ancestry remains:

1. e18a1e8de4d599df830e6ac390c9ab306d23d891 — independent tracking-directory admission deadline fixture.
2. 58e87f9d3ccc1aac262b29f587a1d0553257a554 — coherent durable monitor capability.
3. f161ede8a6ea4cf540edcb7ece81ebb76f064a05 — adopted passive archive-hydration diagnostic.
4. 3145caa8fcf23b1e825eb54fe9176258f58c6b7f — final maintenance SDK and genuine historical test input.
5. 40c342f924561d6ed3f3632bdff8463ce8bb2d3d — current maintenance capability with explicit held-target admission.

I compared the actual series, full changed-path inventory, final message and affected diff with the packet. The first four commits are identical. The remediation is folded into its owning maintenance commit; there is no introduce/remove capability iteration or separate fixup ancestry. No obsolete branch history, transitional migration or abandoned close-completion production path remains within this whole-history review boundary.

The retained reviewed-fb ref resolves exactly to fb7820b3ddda043c4e5053201726e0fc02939d78. Old reviewed/failed heads and their results remain provenance, not successor acceptance or claims of literal merging of nonancestor revisions.

No repeated dependency/channel/pin/generated update stream remains. Production SDKc3 is selected once in3145, with Go/Nix/vendor consistency retained. The genuine original3bb/SDKd3 predecessor is a distinct historical test consumer, not an intermediate production update. Later flake/package edits install feature/check files, not a second selection. All five supplied immutable inputs match the prior head; native/SDK/model/catalog pins are unchanged.

No database migrations or seeds occur in the complete changed-path inventory. There is no remediation-specific durable format change or conversion. Private maintenance schema1 is introduced directly, with reader/recovery paths retained. Existing public/monitor/submission/claim/services/retry obligations retain their earlier reviewed formats. The new descriptor field is behavioral admission, not a migration or persisted proof.

Historical donor external consumption remains unproved; no global absence assertion or private-state inspection is used. Current W/C still pin historicalf161 and supply no final composition acceptance for this runtime. Later consumer pins, artifacts, source-native support, exact packaged/live acceptance and integration remain separate.

## Evidence and limits

Committed packet: /tmp/lead-wakeup-held-capability-B-b3xnqgib/committed-source.json, SHA256474ca77395eabd00747f8ecb2eca9a77d18535c1281fa865b8afc8268444163c.

I independently matched the packet hash, all12 baseline/final source pairs, five unchanged input hashes, all ten command-log hashes and final-remediation.patch SHA2563f859d00d715df75bfea0c5d7609a1dbfd37ce458101494fd07611ecd55ad118. That saved patch equals the actual ordinary Git diff exactly. Full-index index-line formatting is not a source difference.

I also compared source-ready inputs with the final committed files: Go/descriptor/comparison code remained unchanged after the passing checks. Final Ruby guard/refusal/partial-install changes received their focused follow-up. Final docs match the explicitly bound main prose. Current HEAD/tree/parent, retained reference, merge base and clean status were checked directly.

Read original logs only:

- Strict owner/admission/recovery Go0.798s; session contract0.011s.
- Broader command/control/startup scope3.504s.
- Correct live_switch_integration compile0.045s, NO TESTS RUN.
- Ruby broad maintenance/profile/held/startup20 runs/314 assertions.
- Recovery comparisons5 runs/100 assertions.
- Final pre-effect refusal/partial-install cleanup2 runs/108 assertions.
- Ruby syntax/static checks pass; declared Nix Go1.26.6, actual portal module, -mod=readonly and GOWORK=off.
- The original immutable-creation-tuple fixture failures remain, with corrected setup before Create. They are not hidden product failures or a reason to weaken the production digest guard.
- Dirty-tree/system-rename/ignored cache-busy warnings are retained in their original scope. No native acceptance is inferred from them or from compilation.

No tests, evaluations, builds, native/browser/VM execution, Git mutation/publication, CI, claims, profile/live action, lifecycle operation or peer/private-state inspection was performed by this reviewer. This review authorizes none of those actions.

Review complete; reviewer0 returns capacity explicitly, with no implied follow-up assignment. Main owns final disposition and subsequent execution gates. Session remains open.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/)
