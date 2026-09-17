# Mandatory procedure routing for agent instructions

## Goal and accepted approach
Reduce always-loaded instructions in the coordination workspace and each active
project while preserving every requirement, exception, authority boundary and
standalone repository workflow. The user selected explicit mandatory procedure
loading, replacing the earlier inline-only option. No substantive policy change.

## Components and ownership
The workspace owns its coordination routing and procedures. Each independent
repository owns its local AGENTS.md and supporting procedures in its existing
docs/doc layout (docs when neither exists). Inventory all canonical clones,
deduplicate renamed aliases, and leave small cohesive files unchanged where
splitting would increase overhead. Generic mechanisms belong in dev-workspace;
this change should not need runtime mechanisms or site configuration changes.

## Implementation
Record source revisions and map every original nonblank line/requirement to its
retained or relocated text. Move full sections with minimal rewriting. Keep
critical prohibitions, authorization, precedence, secrets, ownership and model
policy inline. Route explicitly by action and indirect trigger before acting;
load all applicable procedures, revisit on scope expansion/delegation, resolve
relative paths against the owning file, and stop the affected action on missing
guidance. Existing skills remain authoritative at their current triggers.

## Compatibility and rollout
No APIs, schemas, persisted state, generated clients, protocols, module options
or model defaults change. Publish entrypoints and referenced procedures in the
same commits. Older revisions remain self-contained; mixed worktree revisions
read their own guidance. Existing sessions must reread changed instructions;
do not interrupt unrelated sessions. No host deployment or coordinated node
upgrade is needed. Retain source text and Git history for rollback. Configuration
master integration is not authorized. No CI wait, per standing user instruction.

## Verification and documentation
Readers are development agents and maintainers reviewing instruction coverage.
Maintain a per-repository coverage artifact, validate every routing target and
loaded-size budget, and report baseline/core/task-specific bytes without claiming
weekly savings. Target workspace core <16 KiB and leave headroom below the
installed 32 KiB discovery limit. Use committed Astra/xhigh mandatory review,
then harmless fresh-session scenarios proving actual prerequisite file reads,
standalone operation, indirect triggers, scope expansion and missing-file stop.
No semantic rule may be discarded to meet a size target. Procedures live with
their owner; source mapping and one-off verification remain in this initiative.
