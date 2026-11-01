# Documentation version policy: final review packet

User/lead brief: add a durable general rule avoiding unnecessary software and
client versions in prose, installation snippets and links, unless their purpose
or established update flow justifies them. Prefer maintained requirements;
preserve machine-significant API/protocol identifiers and necessary
compatibility, reproducibility, upgrade and recovery constraints.

Session: `2026-10-24-vpsadmin-haveapi-upgrade`. Lead owns existing
[plan](../plan.md), [state](../state.md) and combined review coordination.
This packet changes neither plan/state nor shared reusable documentation.

Repository: `git@github.com:aither64/vpsfree-cz-workspace.git`.
Owned worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/workspace`.
Branch: `2026-10-24-vpsadmin-haveapi-upgrade-doc-version-policy`.
Exact base: `41b34dbfe490ddb221b6752aeacd05ea59b72c66`.
Exact head: `0c2c9f18fc18bbb8e2ba7bf65bb9ffea66fbb7c6`.
Exact tree: `627491e225aa71f2a31d141c65d19bbd67ed2a84`.
Fresh fetched origin/master: `398dc7bab89ee51bcc77d23a5acc52c7e02878c1`.
The current shared master/base includes the original tracking checkpoint and
E3's committed KB deliverable. Lead authorized the final tracking-base refresh;
`git rebase 41b34dbfe490ddb221b6752aeacd05ea59b72c66` completed successfully. Own worktree is clean.
No same-session workspace worktree existed; ordinary `dev-session worktree add`
created and registered this one from original base
`56db4fb2f1d25077f99e712abc713dbd6c4d056a`; the refresh below changes only
its final comparison base/head.

The complete range contains exactly one functional instruction commit:
`0c2c9f18fc18bbb8e2ba7bf65bb9ffea66fbb7c6` — Document when software versions belong in documentation.
[Complete series](commit-series.txt), [complete final diff](final.diff), and
[quick check results](quick-checks.txt) are retained next to this packet.
Two files, 15 added lines. No superseded approaches, fixup commits, repeated
pin/channel/input/generated streams, interim versions or retained shims.
Consolidation: one coherent final rule plus its discoverability link.
**NO MIGRATIONS**: no schema/data/state changes, migration versions, or
merge/release/deployment/external-consumption migration lineage exists.

`docs/agent-instructions/documentation.md#versions-in-documentation` is the
single authoritative rule, already routed by root AGENTS for documentation
work. `docs/agent-instructions/knowledge-base.md` adds only its short pointer,
so KB authors discover the same policy without a duplicate rule. No existing
version literal, command, pin, API path, protocol identifier or historical
acceptance/rollout evidence was deleted or rewritten. No product/SDK/provider,
source/dependency/runtime/cluster/KB-stage/default/PR changes are included.
No dependency or configuration inputs changed; no binary compatibility or
rollout/recovery procedure changed. The instruction is reversible by reverting
this one commit. Publication and integration both remain pending.

Quick verification passed before commit and on the final committed range:
`git diff --check`, exact changed-path/one-commit/clean-tree checks, and
in-memory resolution of all local Markdown targets/anchors in both affected
files. No new persistent checker or test framework was added. No hook framework
is declared and no active hooks were present; normal configured identity and
`git commit -F <temporary-message-file>` were used without bypass.

Risk: low, localized documentation-only instruction. Suggested lane: general,
including complete history/consolidation and explicit NO MIGRATIONS assessment;
lead selects any additional combined KB lanes and verifies the retained review
member/settings. Read the mandatory-change-review skill and general reference.
No reviewer is assigned by this packet and no independent-review pass is claimed.
This is STOP-for-review, before publication or any integration. Lead will inspect
wording and coordinate final combined review; source/package checks are not needed
for this instruction-only diff. No new watcher or runtime action was started.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/

## Final tracking-base refresh

Original range: `56db4fb2f1d25077f99e712abc713dbd6c4d056a..e7963d2d8e8428e91bd83e3df6f0467abdfd04f9`.
Final range: `41b34dbfe490ddb221b6752aeacd05ea59b72c66..0c2c9f18fc18bbb8e2ba7bf65bb9ffea66fbb7c6`.
Only intervening base commit `41b34dbfe490ddb221b6752aeacd05ea59b72c66` adds the lead-confirmed KB deliverable
under this session's work/ records (16 paths); no rule-file baseline changed.
Fresh normal SSH fetch observed origin/master unchanged at398dc7b.
Complete old/new binary Git diffs are byte-identical, SHA256
`f9140df69b7214bc01e1e9907d31bb4162be5fc45e80432549890965306ff8ee`.
[Original diff](original-range.diff) and [range-diff](old-new-range-diff.txt)
preserve exact old/new lineage; range-diff reports `=` for the sole commit.
Original author/name/email/date and full commit message are preserved.
Final diff check, two-file scope, all local link/anchor checks, one-commit/direct
parent and clean worktree assertions PASS. No conflicts, new source wording,
additional quick/full suite, default integration or publication.
NO MIGRATIONS/repeated-update-streams/obsolete-history conclusions unchanged.
