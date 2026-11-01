# Pointer-only documentation version guidance: final general review

Requested outcome: user's authoritative version-omission policy belongs in
`vpsfreecz/dev-workspace`; replace the workspace's duplicate rule with one short
canonical pointer while retaining KB discoverability. No duplicate vpsAdmin rule.
Lead's direct brief authorizes this bounded documentation-only adaptation.

Session `2026-10-24-vpsadmin-haveapi-upgrade`; existing plan/state/design remain
lead/architect-owned. Repository `git@github.com:aither64/vpsfree-cz-workspace.git`.
Own registered worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/workspace`.
Branch `2026-10-24-vpsadmin-haveapi-upgrade-doc-version-policy`.

Final base `1c7f990d9ccd61c510c22da18f4771cdaaef640b`, head `eeec0c40d66a6db374dc0e6e60151666d1a9ec49`,
tree `63866b2bc084ae18f48614227c01ef44e9cde2ce`.
Fresh remote origin/master `4beddf77a8f9af1d926c5b48bd6ee4c84f439e85`;
current shared master/base is11 tracking commits ahead and remote is its ancestor.
Original reviewed/published range `41b34dbfe490ddb221b6752aeacd05ea59b72c66..0c2c9f18fc18bbb8e2ba7bf65bb9ffea66fbb7c6`
(tree `627491e225aa71f2a31d141c65d19bbd67ed2a84`).
Original publication/review receipts in the parent directory are unchanged.
Before rewriting, preserved local recovery ref `refs/heads/2026-10-24-vpsadmin-haveapi-upgrade-doc-version-policy-published-0c2` at exact
oldhead; original remote feature ref was independently read at oldhead and has
not been pushed or changed. [Recovery facts](recovery.json) retain these identities.

The final range has ONE coherent commit, `Link documentation version guidance
to the writing skill`, two files/eight added lines against the refreshed base.
[Complete series](commit-series.txt), [complete final diff](final.diff),
[old range](old-range.diff), [old/new range-diff](old-new-range-diff.txt),
and [old/new documentation comparison](old-new-final-tree-docs.diff).
This is an intentional scope reduction from duplicate authoritative prose to
one maintained pointer, not a claim of patch equivalence to the old prose.
Original authorship/date retained; final message describes the current result.
No fixups, superseded intermediate pin streams, compatibility shims, repeated
updates or obsolete approaches remain in the final one-commit history.
**NO MIGRATIONS**: no schema/state/data changes or migration versions, so no
merged/released/deployed/externally-consumed migration lineage.

Only `docs/agent-instructions/documentation.md` and `knowledge-base.md` differ.
The former's Versions in documentation anchor now points to the stable canonical
source [writing workflow](https://github.com/vpsfreecz/dev-workspace/blob/master/skills/vpsfree-user-facing-writing/SKILL.md#workflow),
and the latter retains the same local discoverability link. Canonical published
source `d4355518d945ef2e7d5fc2fdb45d6eab8226fa4c` was inspected: its Workflow
contains the accepted version guidance. No external-link GET was necessary.
The pointer applies to general documentation work, examples/install snippets and
links; the detailed policy stays solely in the extension. No source/config pins,
A0/runtime/provider files or E3 KB content were changed.

**Integration ordering:** extension policy d435 must integrate into
`vpsfreecz/dev-workspace` before this pointer-only workspace change is integrated.
The stable master URL is deliberately maintained, not commit/version-specific.
Neither integration is authorized here. Configuration package f0175c86 remains
untouched and waiting separately for the final published A0 consumer.

[Quick checks](quick-checks.txt): whitespace, exact scope/clean/history, all local
links/anchors, and canonical published source anchor/path PASS. Normal existing
Git hooks/identity procedures followed; no declared/active hook or bypass.
No framework, tests, builds, CI campaign, lifecycle or default push was started.
Risk low; GENERAL final lane requested, including whole-history/consolidation
and explicit NO MIGRATIONS. Lead verifies/assigns retained reviewer settings;
this packet does not claim independent review completed.

Publication is a separate later released step. Because this exact same feature
branch was rewritten, ordinary non-force publication to its existing remote
ref cannot fast-forward. The normal safe same-ref operation is canonical SSH
with the exact old-head `--force-with-lease` and one refspec, recorded without
execution in [publication plan](publication-plan.json); fresh clean/default/ownref
checks and remote readback remain required. No additional user gate is invented
by this packet, and no force/default push is performed now. Original recovery
ref/receipts remain retained. Stop for final GENERAL review.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
