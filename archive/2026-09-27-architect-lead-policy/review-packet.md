# Final branch review packet

This packet records the pre-deployment, pre-integration review input. See
[`state.md`](state.md) for subsequent verification, approval, and merge results.

Initiative: `2026-09-27-architect-lead-policy`.
Plan: [`plan.md`](plan.md). Accepted architect brief:
[`design.md`](design.md). Current execution state: [`state.md`](state.md).

## Requested outcome

Make new development teams architect-led: architect Astra/xhigh writes the
design and verification brief for substantive work, Sol implementers edit
application files, and the Sol lead orchestrates and gives an end-of-turn
progress checklist. Adapt the storage-redesign final-branch review rules.
Keep AGENTS.md and catalog initial prompts aligned. Preserve the current
generic runtime and retained-member settings. Deploy the reviewed package
through the user profile; do not merge feature content without separate
approval.

## Complete series and final diffs

| Repository | Base | Final head | Complete feature commits |
| --- | --- | --- | --- |
| Workspace | `9d1d9b754aed9453b4ce3f3130effbb30a3baade` | `680e2c52fc5067e3668d6ce3d5ce3f8c2a9cedf2` | `7f55c820864fc57899e3b610b8b1ade3ee8ab1fa` policy, catalog, docs, tests; `680e2c52fc5067e3668d6ce3d5ce3f8c2a9cedf2` extension pin and lock |
| Extension | `47d9d93cc2373f010a3e6963f76b1cb57bbc1240` | `bd961682cecb0b3b2bf729a53d2e08bda3d48eb2` | `bd961682cecb0b3b2bf729a53d2e08bda3d48eb2` review skill, references, tests |

Inspect the full final diffs and series at these exact paths:

```sh
git -C worktrees/2026-09-27-architect-lead-policy/workspace log --reverse --format=fuller 9d1d9b75..680e2c52
git -C worktrees/2026-09-27-architect-lead-policy/workspace diff 9d1d9b75..680e2c52
git -C worktrees/2026-09-27-architect-lead-policy/vpsfree-dev-workspace log --reverse --format=fuller 47d9d93..bd961682
git -C worktrees/2026-09-27-architect-lead-policy/vpsfree-dev-workspace diff 47d9d93..bd961682
```

The workspace was rebased onto the shared tracking-only `master` head;
`git range-diff 3daa226b..2e377c85 9d1d9b75..680e2c52` reports both
commits patch-equivalent. The extension is a direct child of its deployed
pin. No superseded approach or fixup commit was found in this initiative's
feature series; independently verify that conclusion. The prior
storage-redesign commits are source material, not part of these branches.

## Split, provenance, and boundaries

The workspace policy/catalog/tests/docs form one behavioral rule change. Its
Nix input and lock update is a separate dependency-selection commit. The
extension skill/references/tests form one reviewer-workflow change. This split
keeps the provider rule and consumer pin independently reviewable. The
workspace's selected extension changes from `47d9d93` to `bd961682`;
the extension's generic runtime remains `3b570f0a8b75d809a2753177590158e9dc4639f1`.
Do not apply storage-redesign pin commit `3f539b0f6f` as-is: it would select
the obsolete `dcb2762192` revision and discard newer runtime fixes.

There are **no migrations**, database or disk-format changes, public API,
CLI, protocol, node, or system-option changes in either branch. There is no
branch migration to consolidate and no migration merge, release, deployment,
or external-use provenance to establish. Catalog instructions and model
settings are frozen into new rosters; existing retained members and creation
retries preserve their saved values. Existing sessions are not migrated.
The generic portal's built-in label for `lead_designed` may remain outdated;
the preset key is retained for compatibility, while new instances get an
architect. Solo is intended for discussion/investigation, not source edits.

The user authorized user-profile deployment and conditional aitherdev
configuration deployment, but no configuration change is planned. The user
did not authorize merging these feature branches to default branches.
Older-package rollback is not a supported goal for newly created Astra
members; any package recovery should use the current forward-only switch
procedure. No cluster or configuration repository was changed.

## Documentation and quick verification

Workspace `AGENTS.md` owns the orchestration contract; routed
`docs/agent-instructions/{git,sessions,verification}.md` own procedural
details, and `docs/agent-teams.md` describes site role defaults and retained
settings. The extension mandatory-review skill owns reviewer procedure.
`design.md` and `state.md` are initiative-specific, not permanent feature
documentation. The existing READMEs were checked; no new entry point is
needed because the workspace AGENTS and site team document already link the
relevant rules.

Implementer-reported quick checks: workspace Ruby policy tests passed (6
tests, 84 assertions); Nix catalog evaluation, focused jq assertions, and
the agent-team-policy derivation evaluation passed. Extension Ruby skill
policy tests passed (4 tests, 50 assertions). Both worktrees are clean;
`git diff --check` passed. The workspace lock diff changes only extension
revision/hash/timestamp; the generic runtime pin remains unchanged. Longer
package checks, feature-branch CI, profile switch, and live smoke test have
not yet been accepted as complete.

## Review assignment

Overall risk: **High**, because the change selects a user-profile package and
changes cross-repository agent policy, including deployment and older-package
recovery expectations. Review lanes: general, architecture/repetition,
scope/proportionality, and risk/compatibility. This conversation has no
verified same-session retained roster, so use the installed default
development catalog's standalone `reviewer` fallback:
`gpt-6-sol/xhigh`, review purpose, read-only. One independent reviewer covers
all four lanes. Request explicit conclusions on the complete history,
obsolete branch-only behavior, and the empty migration inventory.
