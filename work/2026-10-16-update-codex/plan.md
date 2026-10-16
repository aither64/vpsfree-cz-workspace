# 2026-10-16-update-codex

## Goal

Upgrade the packaged and system Codex to the latest stable release and provide
repository-owned update skills. User approved implementation and deployment of
aitherdev through vpsfree-cz-configuration. No default-branch integration is
authorized.

## Affected repositories

- codex-web: protocol/client support, exact model catalogs, update skill.
- dev-workspace: llm-agents selection, codex-web pin, naming prerequisite,
  package checks, update skill and generic package documentation.
- vpsfree-cz-configuration: confctl channels, aitherdev operations/update skill.
- workspace: nested runtime selection, top-level update skill and routing.

Use branch/worktree group 2026-10-16-update-codex. Keep the shared workspace on
master and edit workspace feature content only in its dedicated worktree.

## Approach and decisions

Current latest stable is Codex 0.163.0; resolve again at implementation start,
then freeze its exact llm-agents revision. Update dependency sources before
their consumers. Skills form workspace -> configuration -> dev-workspace ->
codex-web; each owns its repository procedure, links lower-level guidance, and
returns revisions/check evidence without duplicating orchestration. The user
explicitly selected the extra top-level workspace entry point.

Preserve model choices and utility isolation. Refresh source catalogs, derived
Luna metadata and bound hashes together. Retain the assembly helper because
the upstream package still links resources. Review upstream Nix-store daemon
startup semantics rather than assuming the old copy/updater contract remains.

## Compatibility and deployment

Keep terminal and portal on the same exact validated native executable. The
upgrade changes invocation and needs idle sessions before restart; do not
interrupt other work to bypass that gate. Existing packages keep their own
catalogs and state. Adapt wire requests only where the target schema/behavior
requires it. No application-owned state/schema or public API redesign is planned.

Probe old/new persisted thread and daemon behavior using disposable private
state. Establish downgrade compatibility before claiming system downgrade can
read new state. Application recovery is forward-only. Preserve retained system
generations, workspace Codex roots, operation journals, provider credentials and
all existing conversations. No coordinated fleet update or reboot is intended.

Use confctl channels for llm-agents and dev-workspace. Match configuration's
devWorkspace and the workspace's direct nested runtime input while preserving
extension and sibling inputs. Build and validate outside coordinator claims;
activate the system before the user-profile application under one aitherdev
reservation. Publish feature branches, leave them active and unmerged.

## Documentation

Readers are project maintainers and workspace operators. Put reusable procedures
in each skill and authoritative project documentation; link from AGENTS.md and
existing documentation entry points. Keep exact rollout revisions/results here.

## Testing plan

Quick: skill validation, focused Go/Ruby/browser checks, exact generated App
Server schemas and utility configuration policy against target source. Commit
all intended deliverables and run independent final review/history assessment
before long checks. Long: packaged Nix suites, namespace ownership and native
ephemeral integration for both profiles, managed naming service lifecycle,
terminal/browser startup, thread resume/fork, old/new disposable state and exact
aitherdev/workspace builds. Delegate long checks to fresh catalog-policy utility
watchers. After activation verify system/profile/daemon identities, naming,
providers, service health and retained conversations. Record failures and recovery.
