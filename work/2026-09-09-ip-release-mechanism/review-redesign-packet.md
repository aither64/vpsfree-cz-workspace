# Review: campaign WebUI structure and bulk exemptions

Initiative: 2026-09-09-ip-release-mechanism. Coordination root:
/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-ip-release-mechanism
Read plan.md's accepted WebUI redesign section and state.md current summary.

## Outcome and acceptance

Respect established WebUI structure: real rendered sidebar with Cluster/list/new
and contextual actions; table_add_category headers; perex only errors/action
confirmations; normal summaries and separate edit/notify/release/close forms.
One campaign-wide IP table across users, checkbox selection including select-all,
bulk set/remove admin exemptions, distinct user reasons/admin exemptions and
attribution by stored actor ID/login/time visible only to admins. Keep the exact
label Notice history, explain it, and list notices across recipients for admins.
Clarify that close starts no release, retains ownership/history and blocks new
operations while existing release chains continue. Preserve creation selection
on validation errors and request email links. Manual release/date/policy behavior
is unchanged. User approves resetting the review cluster, wants no screenshot
deliverables, and has not authorized merge or session lifecycle cleanup.

## Committed repositories

vpsAdmin worktree:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism/vpsadmin
Base: 564cc80ea5d4420d0f2441c996fb0df2f82bb39c
Head: 43530927dc814780e8b641fd5e5ce846bd9f4b79

The eight-commit separation was already reviewed on its previous base:
1 relative cluster-resource provider; 2 charge provenance; 3 network identity;
4 shared IP helpers; 5 composite relative accounting; 6 cleanup before disown;
7 campaign API; 8 campaign WebUI and browser integration.
This revision folds the redesign into commits 7/8. Tests/translations/docs belong
with the API or WebUI behavior they exercise. No generic Lockable or
TransactionChain locking API change. First six runtime trees are unchanged.

Previous implementation reference:
d778e1b590a0cead8e7c39b8551bade88a28a2f8
For the focused new delta use git diff from that reference over api/, webui/,
tests/ and docs/ip-release.md. The intervening upstream commits only replaced
old ikiwiki documentation. Both new documentation links were carried from the
deleted docs/index.mdwn to docs/README.md in their owning commits. A comparison
with pre-rebase 90f0b2e04 showed zero differences in api/, webui/ or tests/.
Review the series and existing shared-provider decisions as context; prioritize
new changes and concrete regressions, rather than redesigning accepted behavior.

Notification overlay worktree:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism/vpsfree-notification-templates
Base: 6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333
Head: 715c063396fa49277852b98d36347c8bec5160d3
Unchanged in this redesign. Approved EN/CS HTML/plain copy is retained.

KB contract revision will be appended below after its quick check/commit.

## Interfaces and consumers

Campaign API is the owner. New admin-only Campaign.Address.Index and
Campaign.Notice.Index feed admin WebUI tables. Campaign.Exempt accepts selected
request-address IDs plus a common reason (null removes), validates the whole
selection, uses existing campaign/ordered SQL row locks and commits atomically.
Existing Request.Address.Exempt delegates to the same model operation. Member
request lists and Keep remain owner-scoped. Shared parameter definitions keep
both list surfaces equivalent; privileged actor/owner/debug fields are removed
from member output. Existing kept_by_id/exempted_by_id persist attribution after
actor deletion; no additional migration. Both reasons remain independent.

HaveAPI dynamic clients discover additive endpoints/fields. New UI needs new API
and refreshed discovery; old request endpoints stay compatible. New modules are
nested in the existing campaign resource; this adds no top-level API resource
or shared-framework extension. New batch metadata operations do not change quota,
IP cleanup, node protocol, release-time snapshot checks, or force policy.

Canonical behavior/deployment docs: vpsAdmin docs/ip-release.md; locking context:
docs/ip-locking.md. Both are linked in docs/README.md. Existing deployment/rollback
constraints of the earlier ownership work remain in those pages.

## Quick verification

- API/model campaign specs: 52 examples/0 failures, seed 55547.
- Concurrency: 13 examples/0 failures, seed 5672. Includes bulk exemptions
  serializing with release, and rejecting after concurrent release/closure.
- WebUI PHPUnit: 93 tests/388 assertions passing.
- PHP syntax and JS syntax pass; touched RuboCop, Nixfmt and PHP CS Fixer pass.
- API locale regeneration/check and WebUI gettext generation/health pass.
- Normal commit hooks passed. No local long integration has started yet.
- Browser test now begins at Cluster, follows sidebar to creation, checks failed
  form redisplay, semantic headers, select-all across two owners, removal,
  attributed re-exemption, member isolation, email login, keep/assign, reminders,
  early release, repeat release, Notice history and closure. Still needs runtime.

## Risk and review instructions

High risk due to authorization/tenant boundaries and exemption edits affecting
release decisions. All four lanes apply: general, architecture/repetition,
scope/proportionality, risk/compatibility. Use gpt-6-astra/xhigh, fresh context.
Follow /home/aither/.codex/skills/mandatory-change-review/SKILL.md and assigned
lane reference. Review directly; do not spawn subagents. Read-only: no edits,
commits, cluster mutations or long integration runs. Return concrete findings
with severity, code/commit references, rationale and residual coverage gaps.

## Final KB head and check

Worktree:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism/vpsfree-kb-contracts
Base: 8789cc1f5aeb3b19cbff13f741d6dd9960f14567
Head: 2dfe4c7c3ba8e1e9675647eb100cf39e7a42ec3c
Only exact vpsAdmin pin metadata changes, consolidated in one commit. Runtime
vpsAdminOS remains 6bdf458fd9105379860234ff33d352e55844f08f. Full bin/check passed,
including semantic controls/pages/fixtures and inventory validation. No existing
page, control or image drift; no screenshots were generated. Campaign pages are
outside existing capture crops. KB/overlay content needs no redesign edits.
