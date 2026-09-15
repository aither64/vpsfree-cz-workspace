# Commit separation and IP release review packet

Status: all intended runtime changes committed; quick checks passed.
Ready for four-lane review before long integration tests.

Initiative: 2026-09-09-ip-release-mechanism. Plan and state are alongside this
file. Worktrees are under ../../worktrees/2026-09-09-ip-release-mechanism/ for
vpsadmin, vpsfree-notification-templates and vpsfree-kb-contracts.

The user accepted the eight-commit split in plan.md and explicitly requested
an audit of generic resource regressions and complete IP assignment locking,
including shared helpers. The original campaign behavior and approved final
email text must survive the rewrite. After validation, a single/bridge review
cluster with prepared unassigned IPs and an unsent campaign is authorized.
No merge, production deployment, lifecycle closure or cleanup is authorized.

High risk: quota accounting, assignment authorization, database schema and
manual address release with asynchronous DNS cleanup. All four review lanes
apply; each reviewer must use gpt-6-astra/xhigh with fresh context and perform
its own lane directly, without subagents.

Boundaries: absolute reallocate_resource! keeps its existing public contract;
new relative adjust_resource! shares its validation/allocation implementation.
No second quota implementation, generic Lockable change, transaction-engine
protocol change, automatic release/retry, delivery-checking logic, inferred
legacy provenance backfill, or multi-interface migration support. Clone and
VPS clearing/deletion do support multiple interfaces and must aggregate deltas.

Resource reservations last through chain completion/rollback; SQL locks provide
current preparation-time reads only. Public writers reload and authorize current
state. Explicit reserved-object paths preserve pending included-chain assignment
state and verify a real reservation. Allocation shares its picker criteria for
selection and current revalidation. Consumers include network registration,
manual routes/hosts/PTR, DNS/export grants, VPS create/clone/migrate/swap/replace/
chown/delete and resource teardown. Non-IP provider consumers remain absolute:
VPS CPU/memory/swap, dataset quota/refquota and automatic disk expansion.

Campaigns: fixed selections, editable deadline and opt-out policy, independent
admin exemptions, initial notices/reminders, admin-triggered release anytime.
No policy-update email. Deleted/reassigned/assigned IPs are protected; owner and
quota remain until successful host/PTR/grant cleanup. HTML/text EN/CS notices
include location parentheses and IPv4 scarcity only where relevant. Neutral
closing; forced mode has no exemption-advice paragraph. See doc/ip-release.md
for rollout/drain, schema/rollback and verified legacy accounting requirements.

The templates repository owns the vpsFree.cz overlay and vpsAdmin owns core mail
events/built-in English fallbacks. KB contracts pin the exact vpsAdmin feature
revision; they own capture/navigation evidence, not the application runtime.
The node protocol and vpsAdminOS input are unchanged by this initiative.


## Quick verification evidence

- Provider: 82 model/concurrency examples; 35 absolute-contract examples also
  pass against the upstream provider; 110 provider/real VPS/dataset consumers.
- Provenance and registration: 74 model/API cases; 8 registration/concurrency
  cases and 3 targeted Network API cases.
- Shared writers: 114 initial cases (two corrected fixtures, one existing
  unsupported-migration pending), final focused current-owner runs 10/0 and
  28/0; SQL-session cases cover host/export/DNS grant races.
- Relative callers: 44 cases (four corrected new fixtures, two existing
  pending contracts); Clear/SoftDelete/Destroy composite deductions and the
  two-interface clone addition now pass. Opposite ownership transfers and
  stale-snapshot additions pass.
- Cleanup: 21 model/concurrency cases and WebUI 2 tests/10 assertions pass.
- Campaigns: 48 model cases, with one imported relative-call test corrected
  and passing in isolation; 9 API authorization/behavior cases pass, seed
  42032; migration 2/0 seed 533; overlay 24/0 seed 57865.
- Root commit hooks passed for every committed prerequisite and campaign API.
  Schema remains core-only and adds four tables to the refreshed schema.

Logs are /tmp/ip-release-*.log; state.md gives the specific commands and
intermediate failures. Long node/browser integration starts after this review.
Prior full feature CI is evidence for the preserved campaign behavior, not a
substitute for validating this new accounting/helper implementation.


## Exact reviewed repositories

Root: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism

| Repository | Base | Head |
| --- | --- | --- |
| vpsadmin | c38839d5be62e9d40d055b23a84844e2037ba4db | 201c263919049792315598efd4fea5d1a5cfe950 |
| vpsfree-notification-templates | 6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333 | 715c063396fa49277852b98d36347c8bec5160d3 |
| vpsfree-kb-contracts | 8789cc1f5aeb3b19cbff13f741d6dd9960f14567 | same (no feature delta yet) |

The first two worktrees use 2026-09-09-ip-release-mechanism-split construction
branches; canonical feature refs retain the original published heads until the
new series is verified. KB is clean on the canonical feature branch at current
upstream. Its obsolete old feature pin was dropped during rebase. After this
runtime review, push the reviewed vpsAdmin head, update the KB's exact dependency
pin through the prescribed Nix workflow, and run its contract. That dependency
refresh cannot be fetched before publication; any newly required documentation
or capture logic will receive its own applicable review before its integration.
No existing KB source/capture change is presumed necessary; reassess drift.

All worktrees are clean. WebUI quick checks: PHP 3 tests/12 assertions, JS syntax,
16 CI selector tests/55 assertions; 413 API specs covered exactly once across
13 topics (migration specs intentionally have a separate workflow). Every
commit hook passed. Representative selector listing is still evaluating test
metadata; it has not started a VM or a long integration scenario.

The runtime series is:
- ffffa52f2 api: add explicit relative cluster resource adjustments
- f3cef8d15 api: record the charge environment of owned IP allocations
- 316e92c0e api: serialize network registration with resource identity changes
- a9dd51bb1 api: share IP reservations and revalidate assignment writers
- fc1640374 api: combine relative IP accounting changes before confirmation
- 77ee3ca3a api: retain IP ownership until address cleanup succeeds
- 40ca8c082 api: add administrator-managed IP release campaigns
- 201c26391 webui: manage IP release campaigns and user retention


Reviews must examine the final implementation and the commit boundaries. Tests,
migrations, localizations and protocol notes stay with the behavior they verify.
The cleanup commit includes the existing WebUI caller because asynchronous
completion changes its disown-and-remove sequencing. Campaign UI is separate.
Do not edit code or Git state, launch nested agents, or run shared Nix/Bundler
setup concurrently with other reviewers; inspect existing evidence and ask the
coordinator if an additional executable check is needed.
