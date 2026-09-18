# Recovery review: risk and compatibility

No additional Blocking, Important, or Advisory findings in this lane.

This conclusion does not clear the original committed series for delivery by
itself. The coordinating review already identified the installed maintenance
loader guard, the synthetic software revision, and the batch-size discrepancy.
Their narrow remediations and verification remain required. The coordinator
clarified that the approved maintenance default is 1,000, to be owned by the
task instead of inherited from HistoryBackfill's actual 10,000 default.

## Reviewed scope

Standalone risk/compatibility review, performed directly without subagents using
the user's gpt-6-astra/xhigh override. Overall risk: high, because the change
adds persisted state and an operator command that modifies historical bounds.

- vpsadmin: `014fbc78422f3660b295add7a50f35cc7acdf0c8` through
  `268f7d09b9e3ca59d2b8f286e6666f72f9f7a9ff`, including both logical commits
  `cccf59c060be4c85a7a0809203e6fe24447e16a4` and `268f7d09…`.
- vpsfree-maintenance-tasks: `6eea682ede8d8e2634b2d41e5b11cf0f02231bc6`
  through `c77ff3742f623afd23c0be26c0f6ddbc026f1ba4`.
- Read the review packet, accepted follow-up plan, state, rollout, local
  AGENTS.md files, commit messages, relevant implementation, migrations,
  resource definitions, Nix service definitions, and regression coverage.

## Evidence and compatibility conclusions

- **Schema and rollback:** both migrations are additive and contain no
  predecessor-schema guards, defaults, backfill, or historical rewrite. The
  checkpoint node reference has the existing node key's unsigned integer type,
  a unique index, and a cascading foreign key. The cascade also handles node
  deletion by an older application that lacks the new association. Older code
  does not consume checkpoint JSON. Keeping the schema during application
  rollback is consistent with the implementation and operator documentation.
- **Atomic recovery and mixed writers:** `status.rb:36–51,116–135,202–219`
  keeps ordering, comparison, checkpoint capture, current replacement and
  checkpoint removal within the node lock and transaction. Capture precedes
  replacement; failed recovery rolls back deletion and history changes.
  Missing and stale reports retain the checkpoint. `snapshot_reader.rb:7–28`
  prefers comparable current evidence, then the newer of the checkpoint and
  retained node-report event. An older writer can lose newer unchanged
  observations, but its newer event cannot be replaced by an older checkpoint.
  The tests cover that conservative fallback and recovery across a new
  supervisor instance.
- **Public boundaries:** the checkpoint has a separate private model/table;
  there is no new evidence enum, resource, or API field. Existing event and
  evidence resources use explicit projections. The added resource regression
  checks unchanged public evidence/component rows and endpoint inventory.
  No node protocol, generated client, Terraform, or WebUI contract changes.
- **Confirmation semantics:** `record_kernel_evidence.rb:96–108,294–302`
  advances only proven, monotonic confirmation times and uses
  `update_columns`, preserving public revision inputs and immutable snapshots.
  The application fallback takes the newer proven bound. StableState requires
  complete, nontransitioning evidence, known matching boot identity, the same
  reported release and effective patch IDs. Existing removal/legacy reporter
  protections remain in place.
- **Repair integrity and concurrency:** `node_repair.rb:57–169` requires the
  immediate public predecessor, intact event snapshots belonging to the node,
  stable matching-boot evidence, compatible event classification, and strict
  lower < confirmation < upper ordering. Stored digests are checked against
  normalized contents for baseline, target and confirmation. Supporting proof
  is limited to event snapshots still referenced by that node's events;
  checkpoints and mutable snapshots cannot participate. Each proposed write
  recomputes the target, predecessor and supporting proof under the same node
  lock used by ingestion, compares the proposal/fingerprint, and updates only
  the lower bound with normal timestamping. Candidate membership is fixed
  before writes. Earlier repairs remain committed after a later failure, and
  reruns are idempotent without new proof.
- **Operator sequence:** the prepared procedure pauses and checks both
  supervisors through API1 activation, migrations and API2 activation. This
  matches the Nix modules' explicit migration requirement when autoSetup is
  false. It requires no coordinated node update or reboot. A preview is not an
  apply manifest; the paused-writer/repeated-preview procedure states that
  limitation explicitly.

## Remaining validation boundaries

- This was a code and evidence review; no production operations or new long
  integration runs were performed. Existing recorded quick results were
  inspected without claiming an independent rerun. The failed-recovery,
  checkpoint invisibility, migration, legacy-evidence, digest-drift and
  concurrent-change regressions address the principal risks.
- The corrected standalone launcher needs its installed Ruby `load` semantics
  test, and the corrected synthetic report needs the planned runtime-ingestion
  run. The old committed launcher/fixture defects are covered by the other
  review lanes, not waived here.
- The rollout still contains the previous delivery's exact revision assertions.
  Its explicitly planned final-pin update, downstream review and consumer
  builds must precede delivery. This report approves no stale configuration
  pin and authorizes no production rollout or repair.
- Checkpoints cannot reconstruct observations discarded before installation;
  repairs cannot tighten intervals without retained immutable proof. Keeping
  both schema additions on rollback resumes older recording behavior and its
  limitations, as documented.
