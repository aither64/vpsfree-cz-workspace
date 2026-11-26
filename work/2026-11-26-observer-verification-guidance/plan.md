# 2026-11-26-observer-verification-guidance

## Goal

I'd like to update observer prompt/instructions. I notice that the lead gets stuck in verification loops, building infra for verification, running costly tests and discovering issues one by one. This all takes a long time. The observer could get the lead back on track. Instruct it to reassess the design, use faster verification and not address issues one by one.

## Affected repositories

- Coordination workspace: observer role instructions in `config/agent-teams.nix`
  and aligned guidance in `docs/agent-teams.md` (architect confirms boundary).
- Generic runtime is reference only unless a concrete prompt compatibility need
  is established; no runtime feature or deployment is planned.

## Approach

- Architect owns a bounded guidance/compatibility brief in `design.md`.
- One implementer owns the instruction/doc edit, quick checks, commit,
  publication and review evidence in the session's workspace feature worktree.
- Retained independent reviewer reviews the complete committed branch.
- Keep this a prompt improvement: no verification framework or new runtime gate.

## Decisions

- Observer should challenge repeated expensive verification and infrastructure
  growth, recommend reassessing design and verification strategy, and encourage
  bounded diagnosis and related fixes as a batch before another expensive run.
- Preserve required acceptance, independent review and observer advisory authority.
- Integration and deployment are separate from this requested source update.

## Compatibility and deployment

- No persisted format, schema, protocol or supported runtime behavior changes.
- Record stock observer refresh implications from the existing runtime contract;
  do not change retained role settings or select a package in this task.
- Feature integration requires explicit repository/target approval.

## Documentation

- Readers: observer/lead maintainers. Lasting guidance belongs beside the role
  catalog in `docs/agent-teams.md`; execution evidence stays in session records.

## Testing plan

- Use existing quick Nix syntax/catalog and whitespace checks appropriate to a
  prose-only Nix string change; architect/implementer determine exact commands.
- No costly build, deployment, integration suite or new harness without a
  concrete uncovered risk. Final independent review remains required.
