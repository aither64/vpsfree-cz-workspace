# Final review packet: portal restart recovery

Initiative: 2026-10-09-portal-restart-recovery. Coordination workspace:
/home/aither/workspace/ai/vpsfree.cz. Read AGENTS.md and applicable procedure
routes, owning repository AGENTS.md, plan.md, design.md and state.md. Review
committed changes read-only. Use mandatory-change-review/SKILL.md and every
general, architecture, scope and risk reference; perform the review directly,
without nested agents. Selected fallback policy: installed lead_reviewed/reviewer,
gpt-6-astra/xhigh; native role TOML at
/home/aither/.local/state/dev-workspaces/profile/share/dev-workspace/agent-teams/lead_reviewed/reviewer-xhigh.toml.

User outcome: web portal sessions restore after host/runtime restart, with the
same root/history and saved context. Previously running sessions restore
automatically. Stopped/failed ones offer Resume/Retry. Every thread, queue and
active goal stays dormant until explicit user action. Send enqueues before
loading and preserves FIFO. Continue activates queued work or an active goal;
otherwise it submits one visible prompt with retry identity. Members stay held
until addressed/assigned. A portal-only restart preserves live work. Status
refresh preserves composer/draft. User authorized deployment of aitherdev using
configuration and explicitly forbade actually rebooting it. No merge, archive,
delete or other session mutation beyond owned implementation/fixtures is authorized.

Worktree prefix:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-09-portal-restart-recovery/

Complete feature series (inspect base..head log and complete diff yourself):

| Project | Base | Final head and sole feature commit |
| --- | --- | --- |
| codex-web | 7dab76305dc0084735095d6dbdaef607585d9bca | c9878454f07da244c103b8a79340b92b6d5bf052 |
| dev-workspace | 66262519d497073d9bb0dccc2252cdec4528f389 | 97ea4c56f4984c5d8e574735e09a205c6a648f59 |
| workspace | b73995877adf9e70ad36eef68df06e514c9f6faf | 4f4060ab3425c8eecc4614c261f28ee359b611e0 |
| vpsfree-cz-configuration | 1f3569902a4a6b02633019cd172eade5afe90005 | f715299ccd019a3f282dfbd969231223f3479e3b |

One provider primitive commit, one complete recovery runtime commit including
its inseparable provider pin/vendor closure, one workspace composition pin and
one generated confctl host-input pin. Tests/docs stay with the behavior they
explain. Intermediate development pin corrections were amended; no duplicate
update streams or abandoned approaches remain. No implementation has been
deployed yet. Explicitly conclude whole-branch history and repeated-update
consolidation, and migration lineage. No database migrations. New private v1
sidecar is introduced directly, without transitional versions. Existing v3
ledger is imported once from its deployed volatile location; no schema change.
No new schema version was merged, released, deployed or externally consumed.

Rerun all four affected lanes after the initial review in review.md. The fixes
introduce new provider contracts: AllowImplicitResume is a filesystem-only
permission callback for retained subscriptions; RequireSubmissionAttemptsKnown
proves queued or started delegated submissions while the existing strict
RequireSubmissionAttemptsResolved remains the retirement gate; TransportError
distinguishes connection failures from native refusals. The CLI propagates
temporary transport failure as exit 75. Prepared send options/context remain
durable until native queue/history proof, without fabricating acceptance.
Continue receipts retire after successful activation and restart per socket
epoch. Held clients forward the optional queue deletion completion interface.
RecoveryReady excludes unfinished creation from recovery controls/composer.

The native fixture now retains both normal and observer subscriptions across
the private App Server restart and checks no inference before explicit action.
A new session-recovery-boot Nix check registers an actual private workspace and
tests lingering/user units/socket startup across a disposable VM reboot. The
existing host CI lane includes it. Neither fixture reboots aitherdev or mutates
another initiative. Review these contracts and test boundaries independently;
focused remediation checks are evidence, not a substitute for review.

All remediations were folded into each sole feature commit. Configuration was
regenerated from its original base, so its generated change log describes the
single final runtime update 66262519 -> 97ea4c56. No old pin commit remains.

Owning components: codex-web owns cold goal reads, explicit native activation,
queued-send retry proof and ledger import. dev-workspace owns execution holds,
canonical session/runtime/lifecycle identity, recovery orchestration and UI.
Its portal imports the provider, pinned by both go.mod and flake.lock. Workspace
composes the existing vpsFree extension 0ff827df13e82dfab4b536ff29979280f264e8f5
with the new generic runtime. Configuration selects the same runtime host module
through its existing dev-workspace/devWorkspace channel. Application deployment
comes from the user profile. Discover any other actual consumers from source.

High risk: persisted permission/receipts, native queues/goals, host lifecycle and
package rollback. Local operator is trusted per repository AGENTS.md; assess
ordinary mistakes, concurrency, wrong scope, interruption and remote-client
authorization. Do not invent compromised-local-operator containment requirements.
Preserve origins, generation locks, exact retained identity and lifecycle locks.
No native Codex patch, thread recreation, automatic replay, speculative new team,
host reboot, or default-branch integration. Rollback to a predecessor ignoring
holds/receipts is deliberately refused after state exists; recover forward.

Documentation: codex-web/docs/reference.md; dev-workspace/docs/dev-sessions.md
and docs/workspace-portal.md; initiative design and compatibility in plan.md.
Operational deployment evidence will be recorded separately after execution.
Quick checks and limitations are in state.md. No long integration test had run
at the initial review; the corrected native fixture subsequently passed, and
packaged/browser/disposable VM verification is underway. Native package remains
0.160.0. Fixture corrections introduced exact project/marker identity and a
private zero unload delay, without changing application contracts.
Environment-only Go workspace file is an uncommitted local testing artifact.

Return findings by severity/lane with files/lines and commit references. Request
missing evidence rather than assuming acceptance. State residual test gaps and
explicit whole-branch history, update-stream and migration conclusions. Do not
edit code, deploy, merge, update tracking or run long integration checks.

Final heads include the requested narrow hot-send reconciliation and complete
transport propagation corrections after the second review. Main inspected and
verified those direct fixes under steps 9–10; no further design or public API was
introduced. Detailed findings/conclusions and fixture limits are in review.md.
The boot fixture's missing workspace directories were corrected after its first
run failed at registration. Main verified this setup-only change by source
inspection, Nix parse and formatting checks; it preserves the reviewed boundary.
Further setup corrections register the application closure in the VM store,
install a proper Nix profile generation, enable private QEMU reboots and wait
for socket readiness. Application code and contracts remain unchanged. Main
verified the pinned NixOS driver/module contracts before these direct fixes.
Workspace rebased patch-equivalently over shared tracking-only b7399587; its
complete origin/master series includes initial plan 87296b12, unrelated tracking
b7399587, and the sole final functional pin 4f4060ab. No abandoned pin streams or
transitional migrations were added.
