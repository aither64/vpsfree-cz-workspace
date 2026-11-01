# Final review context

Outcome: stop retained checkout/build/raw tracking copies from accumulating,
without collecting live work or losing committed Git heads.

User decisions: new archives discard ALL staged, unstaged, untracked and ignored
checkout contents; keep committed heads/branches. Tracking retains Markdown and
portal.yml only; no external artifact store. Unused preparations/orphans expire
after 24 hours. Aitherdev deployment and explicit maintenance are authorized.
Default-branch integration is NOT authorized. Historical archive deletion is
prepared on the workspace feature branch only; it must not touch shared master.

High risk: destructive archive behavior, private persisted formats, interrupted
conversion, compatibility gates, concurrent collection and host deployment.
All four lanes apply: general, architecture/repetition, scope/proportionality,
risk/compatibility. Trusted local operator boundary is in runtime AGENTS.md;
ordinary mistakes, concurrency, wrong identity and remote clients remain in scope.

No database migrations. Private archive inventory formats 1/2 are existing
supported predecessors. New inventory/record format 3 represents committed-only
recovery. Optional explicit compaction converts completed private inventories to
3; no conversion or deployment has occurred. Old readers are retained solely for
existing predecessor archives and interrupted operations. New record/inventory
capability gates require archiveRecoveryPolicy 3; a policy-2 initiator may need
the documented candidate forward-switch entry. Conversion publishes schema 3
before rewriting individual records so policy 2 rejects interrupted conversion.
Software rollback cannot restore discarded uncommitted files/raw artifacts.

Three owning components: generic dev-workspace owns archive recovery, summary
projection, sparse workspace checkouts and coordinator GC; workspace consumes the
runtime through its direct nested input and supplies site maintenance policy;
configuration consumes the same exact runtime through confctl channel dev-workspace,
role devWorkspace for the host contract. The vpsfree extension revision is fixed at
767dfd587e346168e1443e65ccdb67ce748f3fe3. Codex remains 0.163.0.

Commit split: runtime archive lifecycle+legacy readers+summary filtering; sparse
additional checkout initialization; coordinator TTL/explicit expiry/size reporting
and independent integration-scratch GC. Supporting tests/docs stay with each
behavior. Workspace historical deletions are a separate mechanical commit, then
policy/maintenance/docs, then one generated input update. Configuration operations
docs and one generated confctl pin are separate commits. Earlier unmerged fixups
and repeated pins are consolidated; none of those iterations was deployed.

Review deletion inventory through archive-deletion-summary.json and
archive-deletion-manifest.txt. Do not generate a full archive deletion diff:
66,320 raw entries represent 4,369,293,668 logical bytes. Programmatic verification
found no removed Markdown or portal.yml entry; 3,073 summary entries (24,729,629
bytes) survive. The deletion manifest includes 358 symlinks and one embedded
Git-link artifact, without traversing external trees.

Docs: runtime docs/{dev-sessions,session-archive-recovery,coordination-operations}.md;
workspace docs/operations/workspace-storage-retention.md and agent lifecycle
procedure; configuration docs/operations/aitherdev-disk-retention.md. These explain
supported behavior and reusable maintenance; exact rollout evidence belongs here.

Quick evidence already retained: quick-runtime.log (5 archive cases, 103 assertions;
5 GC cases, 28 assertions; 2 capability cases, 4 assertions), quick-workspace.log
(2 maintenance cases, 10 assertions), quick-sparse-reuse-fixed.log and
quick-sparse-roundtrip.log. Legacy and interruption fixtures are checked in the
final unit batch. Initial full-CI fixture errors and their causes are recorded
in state.md with full failed logs; do not treat a retry alone as proof.

Non-goals: default branch integration, deleting active session work, generic
backup storage, changing automatic archive eligibility, changing Codex versions,
manual Nix store deletion, collecting unrelated QEMU campaigns or caches.

Remaining after review: packaged/composed checks, exact-head native CI, scoped
host build/dry activation; publish consumer branches; machine claim, system then
application selection; verify portal/naming/conversation continuity; recovery-only
compaction and expire-unused GC previews/apply; ordinary Nix GC and measured
attribution. Machine claim remains held until both verification and integrated
lineage satisfy installed policy, since merge approval is separate.
