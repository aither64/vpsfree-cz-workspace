# History review consolidation

## Goal and authorized scope

The user requested stronger instructions after four successive devWorkspace pin
updates entered configuration master despite an existing consolidation rule.
Implement the proposed review clarifications. User explicitly says to wait for
approval before merging. Prior portal merge approval does not cover this work.

Affected projects: workspace (Git/readiness procedure) and vpsfree-dev-workspace
(canonical mandatory-change-review skill and general lane). Generic runtime,
provider and production configuration are outside this change.

## Lead design and verification brief

This is a bounded instruction edit owned by the lead, with no retained team.
Update the workspace Git procedure and its AGENTS entry-point summary, plus the
canonical review skill and general-review reference. Keep one authoritative
home for detailed reviewer rules; workspace orchestration points to that skill.

Require one final dependency/channel-input update per logical update stream.
Distinguish preserving supported deployed behavior and migrations from preserving
intermediate Git pin commits. Deployment and branch publication alone cannot
justify redundant pins. Keep rollout SHA provenance in rollout records; preserve
necessary exact source refs where a supported consumer requires them. Do not
rewrite merged history.

Inventory repeated update streams in the review packet; require reviewers to
independently conclude which updates were superseded/consolidated or why an
exception is necessary. Exemption for purely mechanical content does not remove
whole-branch history duties. Unsupported redundant pins are Important findings.
Before any approved merge, the lead checks the current full series against the
reviewed final series and confirms the repeated-update conclusion, using existing
narrow-fix and patch-equivalent-rebase rules without automatic redundant reviews.

## Compatibility, deployment and recovery

No API, state, schema, migration, Nix input or executable changes. Existing
migration lineage, supported deployed behavior, saved rosters, archive ownership
and explicit merge approval remain required. Instruction files are compatible
with the current skill packaging; feature revisions do not replace the installed
Nix skill bundle. Deployment or downstream pins are outside this instruction
change. Recovery before merge is a normal feature-branch edit; afterward use
ordinary authorized follow-up changes, never rewrite published master.

## Checks and acceptance

Review full diffs for factual/authority consistency, whitespace and local Markdown
links. Evaluate the four-pin failure scenario and a legitimate supported-state
exception against the written rules. No new implementation-mirroring tests or
long application/VM builds are needed for prose-only changes. Commit all intended
changes, then run mandatory independent final review and reconcile findings.
Publish only feature branches and capture useful comparisons. Do not merge until
the user approves the exact repository/target set. No CI waits after merge.

Maintainers and reviewers read the changed procedures in their existing locations;
tracking keeps task provenance and review evidence. No new standalone project
explanation is needed.
