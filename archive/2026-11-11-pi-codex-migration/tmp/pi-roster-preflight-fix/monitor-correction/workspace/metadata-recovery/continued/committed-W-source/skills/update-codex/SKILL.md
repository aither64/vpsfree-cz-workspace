---
name: update-codex
description: Update Codex across this development workspace, its dev-workspace/codex-web dependencies and aitherdev, using repository-owned update skills and coordinated system/application deployment.
---

# Update workspace Codex

Read AGENTS.md and its applicable procedure routes. Verify or create the owning
session before mutation, use isolated worktrees, record the plan/design and keep
the shared checkout on master. Resolve the live roster before substantive work.
This skill does not grant deployment, merge or lifecycle permissions.

## Run the repository-owned processes

Resolve the latest stable OpenAI Codex release unless the caller selected an
exact version. Freeze the version and an exact llm-agents revision containing it.
Record current and selected versions plus the exact native/source identities.

Read skills/update-aitherdev-codex/SKILL.md from this initiative's
vpsfree-cz-configuration checkout. Its canonical repository is
git@github.com:vpsfreecz/vpsfree-cz-configuration.git. That skill points to the
runtime's update-dev-workspace-codex skill, which points to codex-web's
update-codex-web skill. Read each repository's instructions before edits.

Pass the same selected version and explicit dependency roots through the chain.
Run dependency changes before consumer pins, publish exact feature revisions,
and retain returned check evidence. Each layer owns its repository changes;
the workspace owns combined review and deployment ordering. Do not duplicate
lower-level procedures here or repeatedly rerun already-proven checks.

## Compose the workspace package

Use a workspace feature worktree for the direct nested runtime URL
inputs.vpsfree-dev-workspace.inputs.dev-workspace.url. Preserve the extension
revision and sibling inputs. After selecting the published runtime, generate
the lock with the scoped update:

```sh
nix flake update vpsfree-dev-workspace/dev-workspace
bin/check-dev-workspace-deployment --workspace-root WORKSPACE_ROOT \
  --configuration-root CONFIGURATION_ROOT
```

Inspect semantic input paths: configuration's devWorkspace and the workspace's
nested runtime must match. Also verify the system and packaged llm-agents Codex
versions and the runtime's codex-web source/Go pin agree. Do not add the
application to system configuration or incidentally deduplicate the lock graph.

## Review, verify and roll out

Complete all intended changes, quick checks and commits before mandatory final
review. Include all branches' complete histories, final diffs, pin consolidation
and migration provenance, including an explicit no-migrations conclusion when
applicable. Then run applicable longer exact-binary/native, naming, packaged
and state-compatibility checks through fresh verification watchers. Validate each
new skill and check that its dependency references resolve from selected sources.

Build the exact final system and application outputs. When deployment is
authorized, reserve aitherdev through the selected coordinator and submit system
activation before dependent user-profile activation. Read the installed
coordination guides and preserve the reservation through acceptance/review.
Changed native invocation needs idle sessions: wait without interrupting other
sessions or bypassing transition refusals.

Verify system/profile/native daemon identities, naming, providers, terminal and
browser operation, saved-thread continuity and service health. Record actual
rollout results separately from reusable project guides. Preserve journals,
retained generations, roots and conversations. Recover application selection
forward through the original attempt; reconcile uncertain system effects.

Publish branches and update session state/artifacts and its stable portal URL.
Without explicit integration direction keep the initiative active, awaiting
merge approval; deployment does not release its integration obligations. Do not
archive, delete, stop sessions or prune retained packages as a finishing step.
