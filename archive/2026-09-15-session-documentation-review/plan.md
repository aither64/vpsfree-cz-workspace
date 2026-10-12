# Model-driven documentation for dev-workspace

## Goal

Implement the accepted plan: make the agent responsible for proportionate,
durable documentation during ordinary development. Ship the generic
`dev-session-documentation` skill to all dev-workspace installations, connect
vpsFree review and handoff, integrate the three affected repositories, and deploy
the application on aitherdev. Improve other projects as related work touches them.

The earlier assessment is in [assessment.md](assessment.md). The user chose a
generic runtime skill and deferred historical backfilling. The user explicitly
authorized implementation and aitherdev deployment, including host configuration
if necessary. Do not archive or stop the initiative.

## Affected repositories

- `dev-workspace`: generic skill, package catalog, session templates and recovery,
  tests, session guide and documentation entry points.
- `vpsfree-dev-workspace`: review/handoff guidance and generic runtime pin.
- `workspace`: policy, documentation destinations and consuming extension pin.
- `vpsfree-cz-configuration` only if a host change proves necessary. Application
  delivery uses the workspace user profile. Configuration integration requires
  separate authorization.

Use branch and worktree group `2026-09-15-session-documentation-review` throughout.
The shared workspace stays on master; reusable changes use its own worktree.

## Approach

1. Add a self-contained, implicitly discoverable generic skill. Let the model
   choose useful documentation without a fixed bundle, length, or new approval
   step. Capture decisions while context is available, distinguish evidence from
   inference, and keep durable knowledge in its owning project.
2. Include the skill in the existing package catalog; preserve extension entries
   and reject a name collision. Reuse activation and rollback reconciliation.
3. Add Decisions/Documentation prompts to plans, and Status-first state with
   Next actions/Documentation. Preserve required headings and lifecycle format.
   Account for exact-template comparisons in supported creation recovery.
4. Document the actual workflow and rationale in the generic session guide and
   link from README/repository instructions. Update vpsFree policy, review packet,
   general-review checks and handoff links. Keep existing review severity and
   tracking/archival cadence.
5. Quick-check and commit functional changes, pin runtime -> extension ->
   workspace, then run required adaptive review at xhigh before long checks.
6. Resolve findings, complete package checks and final-head CI, fetch/rebase and
   capture comparisons, integrate each repository by fast-forward and deploy.

## Compatibility and deployment

No database schema, project API/client, daemon protocol, container state, NixOS
option, or coordinated node update changes. Skill catalog and session manifest
schemas remain unchanged. Existing plans/states are not rewritten on restart or
revive. Recognize the immediately preceding templates only where supported
creation recovery needs them; reject malformed/edited drafts as before.

Adding the generic skill name reserves it against a conflicting extension entry.
Existing distinct extension skills remain installed. Profile rollback reconciles
managed skill links and retains authored Markdown. Preserve existing transition
checks for unfinished sessions and cluster state. Deploy with the stable
`workspace-host switch --source` command from the initiative workspace checkout,
retaining the previous generation. No host configuration change is expected.

## Documentation

The generic session guide explains document ownership, rationale capture,
current versus historical records, discovery, and deployment/rollback. The skill
contains actionable authoring guidance. vpsFree-specific destinations and existing
KB publication rules stay downstream. Record this rollout in a session artifact
and link the generic guide and applicable instructions from the final handoff.

## Testing plan

- Skill-creator validation; package catalog presence, extension coexistence and
  duplicate-name rejection; isolated skill install/upgrade/rollback tests.
- New creation/goal seeding, supported old/new interrupted creation, preserved
  retained tracking, fork retry, archive/revive and malformed partial drafts.
- Focused Ruby/Nix/whitespace checks and hooks before commits and mandatory review.
- Adaptive general, architecture, scope, and compatibility review as triggered,
  all at xhigh, followed by package checks and GitHub CI on final revisions.
- Guidance examples: small fix, consequential design, ordered migration, and
  uncertain historical rationale. Validate discovery in a fresh session context
  and live portal access after deployment without disturbing other sessions.

## Decisions

- Generic skill ships in dev-workspace, not the vpsFree extension.
- Existing project docs improve as touched; no historical backfill or portal
  search/UI feature in this initiative.
- Preserve ordinary authorization, lifecycle, commit cadence, and review rules.
- Integrate runtime, extension, and workspace through normal fast-forward paths;
  preserve branches and keep the session open after deployment.

## Follow-up: unify vpsAdmin documentation directory

The user requested that vpsAdmin use `docs/` as the other projects do. Rename
its tracked top-level `doc/` tree, update live repository references and any
build/CI path consumers, and preserve the existing document contents and layout
below that root. Record the reason in the commit and keep README/agent entry
points accurate. Do not rename unrelated package or generated `doc` paths.

Use this initiative's vpsAdmin branch and worktree. Check references and moved
file contents, run the relevant repository hooks and any affected path-selector
tests, then commit and run mandatory review. Fetch/rebase, capture the final
comparison and integrate by fast-forward after applicable CI passes. No runtime
deployment is needed for a documentation-tree rename.

Compatibility: repository-relative and unpinned browser links to `doc/` change
to `docs/`; update current in-repository consumers together. Commit-pinned
historical links remain valid. There is no state/database/API/protocol change
and no mixed-version service or coordinated-node requirement. If a build or
publication consumer is found, assess its ordering before proceeding.
