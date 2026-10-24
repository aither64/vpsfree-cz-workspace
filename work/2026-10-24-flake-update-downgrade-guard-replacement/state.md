---
lifecycle: active
---

# 2026-10-24-flake-update-downgrade-guard-replacement

## Status

Implementation authorized by user: "great, implement it". Investigation and
design completed by architect0 and assessed by lead. See [design.md](design.md)
for exact workflow inventory,
proposed interfaces, implementation packages and verification plan.
Session identity matches `dev-session current`, both environment markers and
the trusted thread binding. Retained architect0 is ready with workspace-write
access. No application changes, commits, tests, review or deployment yet.

## Phase checklist

- [x] Verify session identity, roster and scope.
- [x] Inventory workflows and confctl; architect0 owns `design.md`.
- [x] Assess proposal and present solution to user.
- [ ] Implement shared confctl guard (packages A+B).
- [ ] Adopt in all seven workflows and bootstrap confctl pins (packages C+D).
- [ ] Complete quick checks and committed whole-branch inventories.
- [ ] Independent final review, then longer verification.
- [ ] Publish verified feature heads; await separate integration approval.

## Backlog

| Owner | Expected result | Acceptance | Dependencies/checks |
| --- | --- | --- | --- |
| architect0 | Workflow inventory and shared guard design | Exact repository/path evidence; safe outcomes and rollout plan | Read canonical refs and confctl; write design.md |
| lead | User-facing recommendation and tracking | Explain preservation of advanced pins, failure behavior and limits | Assess architect report and official Git/Nix docs |

## Next actions

Implementation is the next phase after this requested solution proposal.
Live roster rechecked; both implementation members ready with workspace_write.
Assign packages A/B (shared guard), then C/D (consumer workflows/tool bootstrap).
Refresh remote inventory before edits.
No branch is declared ready and no integration/deployment is authorized.

## Documentation

Using dev-session-documentation and dev-session-handoff skills. Proposal evidence
will remain session-local; no reusable project docs changed in this phase.

## Repositories

## Commands run

- `dev-session current`: exact expected slug.
- `dev-session team list <slug> --as-is`: retained Full-team members ready.
- Assigned architect0 read-only investigation plus session design write.
- Read official Git merge-base and Nix metadata documentation for ancestry and
  timestamp semantics.

## Results

Architect early findings: seven publishing workflows across haveapi,
terraform-provider-vpsadmin, vpsadminos, vpsf-status, both configuration
repositories and vpsfree-irc-bot. These publish direct commits, not PRs.
vpsadmin's daily update changes a build-environment override without staging the
lockfile and needs separate classification. Inventory uses local canonical refs,
without fetching; it does not establish current remote freshness.

Confctl updates lockfiles in place; existing `--downgrade` selects changelog
direction and does not prevent downgrades. Proposed shared explicit guard would
validate the complete candidate lock graph before installation and commit.

Material graph finding: vpsf-status and vpsfree-irc-bot use multi-component
`follows` paths, while current updater scripts hard-code `.nodes.nixpkgs` and
confctl's reader only considers the first follows component. A shared guard must
resolve semantic paths from `lock.root`. Configuration repositories pin old
confctl revisions, so rollout needs explicit tool bootstrap/pin changes.

Lead accepted strict all-or-nothing candidate validation. Final design refines
the early skip suggestion: known non-forward candidates preserve the existing
lock and return a distinct nonzero policy-rejection status, stopping existing
jobs before their common push. Unknown evidence also fails without mutation.
A future explicit wrapper could map only known rejections to a visible skip.
Direct
pushes must be ordinary non-force pushes from a fresh target baseline, with
concurrent advancement requiring regeneration/revalidation. Guarantee is commit
ancestry preservation, not semantic prevention of future upstream reverts.

Acceptance: lead read the completed proposal and inspected confctl's root CLI
at the recorded commit to confirm ordinary-flake update interface fit. Architect
reports document integrity checks passed. No application tests were run. This is
planning/investigation only; mandatory final deliverable review is not triggered.
No source/workflow implementation, independent final review, integration or
deployment occurred. All seven coverage claims are limited to inspected local
canonical snapshots; remote freshness and live schedules remain unverified.

## Open questions

## Cleanup

Leave the session open. No owned machine, repository claim or temporary worktree.
