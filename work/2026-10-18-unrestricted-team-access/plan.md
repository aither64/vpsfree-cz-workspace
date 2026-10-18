# 2026-10-18-unrestricted-team-access

## Goal

Give all existing and new team members and verification utilities the lead's
unrestricted filesystem, network and Nix execution access. Preserve assigned
roles in instructions. Prove direct same-session peer messaging works.

## Affected repositories

- codex-web: trusted explicit full-access thread policy and approvals.
- dev-workspace: schema-6 package execution policy, retained-member execution,
  catalog/CLI/browser integration, verification utilities and documentation.
- workspace: site policy, composed runtime pin, instructions and checks.
- vpsfree-cz-configuration: matching dev-workspace channel pin and aitherdev.

## Approach

Extend codex-web policy validation and request serialization; add schema 6 with
package-level execution_access: full_access. Apply selected package policy above
historical roster access on every safe new turn. Retain historical role access,
models, efforts, identities, prompts and retry receipts. Display effective access
separately. Cover CLI assignments, browser sends, queues, forks and native utility
launches. Document the existing peer CLI and keep report_to_lead focused on lead
reports. Commit and quick-check the complete change before independent final
review, then run packaged/live verification, deploy, verify and integrate.

## Decisions

The user selected unrestricted access for every role, reviewers and watchers
included, and application to both existing and new teams. Role-only editing
restrictions remain instructions. The user authorized aitherdev deployment via
vpsfree-cz-configuration and explicitly selected all four repositories for merge
into master after successful deployed verification. No merge before that gate.
No Codex version upgrade or unrelated service change is intended.

## Compatibility and deployment

Read schemas 4/5 without changing their semantics. Schema 6 is a new immutable
catalog contract; old packages cannot read it. Retained roster/creation/ledger
formats do not change. Never rewrite uncertain submissions or re-send a message
whose outcome is unknown. Existing active turns complete with their original
permissions; subsequent turns receive selected execution policy. Preserve the
forward-only profile transition and existing recovery/journal gates. There are
no database migrations, daemon message changes or vpsAdminOS fleet updates.

Publish exact reviewed revisions, compose workspace/client/runtime pins and set
the configuration's existing dev-workspace/devWorkspace channel through confctl.
Check matching final locks. Build outside claims; reserve vpsfree:aitherdev for
coordinated system activation followed by user-profile activation. Verify actual
member and utility execution plus peer messages. Only then fast-forward merge
codex-web, dev-workspace, workspace and configuration master branches in dependency
order. Keep the reservation until final deployed inputs are integrated and
acceptance is recorded; retain feature refs and the active session.

## Documentation

Readers: workspace developers, team leads and deployment operators. Keep the
generic contract in dev-workspace's portal/session docs and monitor skill; public
policy support in codex-web; site choices in workspace team docs/instructions;
machine-specific operations in configuration. Keep individual rollout evidence
under this session. Apply the writing skill directly to user-visible copy.

## Testing plan

Focused Go policy/catalog/runtime/browser tests, Ruby command/transition tests,
Nix catalog checks and workspace instruction/deployment contracts. Inspect whole
branch history and no-migration provenance during mandatory independent review.
Then packaged suites and native live tests using fresh Luna/low watchers. From
real member/utility contexts verify Nix daemon access, declared shell entry,
network and owned out-of-worktree temp writes. Verify architect/implementer peer
messages, replies, busy delivery, stable-ID retry and resume. Run the same
acceptance after deployment before any approved integration.
