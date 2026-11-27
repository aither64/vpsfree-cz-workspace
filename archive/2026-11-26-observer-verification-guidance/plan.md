# 2026-11-26-observer-verification-guidance

## Goal

I'd like to update observer prompt/instructions. I notice that the lead gets stuck in verification loops, building infra for verification, running costly tests and discovering issues one by one. This all takes a long time. The observer could get the lead back on track. Instruct it to reassess the design, use faster verification and not address issues one by one.

## Affected repositories

- Coordination workspace: observer role instructions in `config/agent-teams.nix`
  and aligned guidance in `docs/agent-teams.md` (confirmed by accepted brief).
- Generic runtime is reference only unless a concrete prompt compatibility need
  is established; no runtime feature or deployment is planned.

## Approach

- Architect owns a bounded guidance/compatibility brief in `design.md`.
- One implementer owns the instruction/doc edit, quick checks, commit,
  publication and review evidence in the session's workspace feature worktree.
- Retained independent reviewer reviews the complete committed branch.
- Keep this a prompt improvement: no verification framework or new runtime gate.
- Complete implementation and review evidence: [design.md](design.md),
  [review-packet.md](review-packet.md), [final-review.md](final-review.md).

## Decisions

- Observer should challenge repeated expensive verification and infrastructure
  growth, recommend reassessing design and verification strategy, and encourage
  bounded diagnosis and related fixes as a batch before another expensive run.
- Preserve required acceptance, independent review and observer advisory authority.
- Integration and deployment are separate from this requested source update.

## Compatibility and deployment

- Source-only update; no runtime/schema/API/settings changes. Existing retained
  observers do not automatically receive latest site-catalog instructions.
- Deployment and live reconfiguration are separate; neither was performed.
- User approved workspace/master integration with “merge it”. Exact reviewed
  feature head `844ac4dbf768ebced1d27d208f4d5ebaf8b82deb` was fast-forward
  merged and verified on origin/master; merge ownership released. Deployment
  remains separate and was not requested.

- No persisted format, schema, protocol or supported runtime behavior changes.
- Record stock observer refresh implications from the existing runtime contract;
  do not change retained role settings or select a package in this task.
- Feature integration requires explicit repository/target approval.

## Documentation

- Maintainer/observer reference remains in the existing `docs/agent-teams.md`;
  catalog prompt stays authoritative. Exact execution evidence stays in session
  records rather than maintained reference.

- Readers: observer/lead maintainers. Lasting guidance belongs beside the role
  catalog in `docs/agent-teams.md`; execution evidence stays in session records.

## Testing plan

- Pure catalog evaluation/comparison and whitespace checks passed; no builds
  or new tests/harness. Prompt 4087/4096 UTF-8 bytes.
- Existing instruction suite: nine tests pass, one unrelated AGENTS.md size
  failure reproduced at exact baseline. Full suite is not green.
- General-lane final review by retained reviewer0 (Sol/xhigh) found no issues
  and accepted the proven baseline limitation for this bounded change.

- Use existing quick Nix syntax/catalog and whitespace checks appropriate to a
  prose-only Nix string change; architect/implementer determine exact commands.
- No costly build, deployment, integration suite or new harness without a
  concrete uncovered risk. Final independent review remains required.

## Deployment extension

User authorized deployment and specified vpsfree-cz-configuration mediation.
Use its own registered worktree and operational procedure. Architect extends
brief; implementer owns concrete preparation/build/check evidence, lead owns
activation/claims/release. Source prompt remains reviewed/integrated. Resolve
runtime/module identity matching before build/activation; do not infer a pin
bump or system rebuild from the repository's involvement alone. Any actual
configuration feature change retains its own commit/review/integration rules.

## Nov27 refresh boundary

Queued machine ownership was granted after profile/system changed. The old
candidate was not activated and unused ownership was released. Current profile
still has the old prompt and a matching-runtime refresh is needed. Installed
bridge contract requires authoritative prior cleanup/retirement proof before
ordinary update; bounded public-contract and existing-receipt reads did not
establish it. Stop on that external evidence dependency. See current design and
state for the conditional two-file source refresh and its ordinary review,
integration, build and fresh ownership gates. No broader recovery work is added.


## Final delivery decision

The observer default is installed by an intervening deployment in selected6j7.
Exact reviewed prompt/catalog, health/continuity and a no-build derivation match
to integrated root0d24 establish delivery. Earlier conditional source alignment
and rebuild plans are superseded; no new source/code review/build/activation or
merge approval is needed. Historical original deployment SHA is not invented.
Unused machine ownership was released before refresh; no resources are held.
Existing saved session observers retain their instructions, while new selections
use the deployed default. Session remains open with no lifecycle action.
