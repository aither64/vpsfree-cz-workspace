# Compact campaign-list columns review

User request: administrator campaign list must show separate Total, Release,
and Keep columns with short labels. Accepted Czech labels are Celkem, Uvolnit,
Ponechat. Numeric cells are right-aligned, including zero. Existing explanatory
tooltips move to headers. Empty list spans seven columns. Campaign details,
member lists, API counts and release behavior are unchanged.

Initiative: 2026-09-09-ip-release-mechanism. Tracking plan.md/state.md here.
Worktrees: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism/
- vpsadmin: prior58a9b71eae255fb2c5547b8be4c41d968ab4dc22,
  headb76affa12f6f8664ce01d329183dc66cb35ab8a7. API commitdc483b57a and
  first six prerequisites unchanged. WebUI owning commit0d532b15a; ninth
  independent fixture patch unchanged by range-diff. Base15ae9175c.
- vpsfree-kb-contracts: prior2e5cb3b078ff99805fbc42075ed45a05b576a8f2,
  headc4c4ba469becafde34ea058c4333106725b41678. Exact vpsAdmin pin only; explicit nested
  vpsAdminOS6bdf458 and nixpkgs remain unchanged.
- Notification overlay f275bf35a is unchanged and outside this delta.

Review the committed delta against the prior heads and preserved commit split;
the earlier campaign implementation was already reviewed and tested. Low risk:
a reversible local presentation change, no API/state/security/ownership/locking
change and no changed deployment contract. General and architecture lanes at
gpt-6-astra/xhigh. Scope/risk not triggered: no new abstraction or cross-project
capability; KB update is the required mechanical exact pin.

The list deliberately repeats three existing tooltip strings to keep this
small renderer change local; there is no duplicated eligibility/count logic.
No generic XTemplate or table CSS change, no API restart, no seed/fixture reset,
no email changes or screenshot work. The development WebUI uses a live bind
mount, so only PHP workers may need reloading for gettext. Existing data stays.

Quick checks: PHP syntax/style, gettext health and PHPUnit96 tests/398 assertions
passed. Updated browser source and live-check script pass Node syntax checks.
All commit hooks passed. KB full bin/check passed (60 concepts/120 variants,
existing PNG validation only). Existing Playwright campaign test now checks
three headers, tooltips, corresponding numbers and right alignment; a focused
live check will cover both locales, empty rows, pagination, unchanged details
and the two-column member list. No new unit test for this small display change.
Logs: /tmp/ip-release-columns-{quick,style,commit,kb-check}.log.

Owning docs/ip-release.md now names the three list columns. No managed KB page
or capture documents this admin list; the full contract has no drift. Guide,
commit map and state will be refreshed after deployment.

Read repository AGENTS.md, the mandatory-change-review skill and your lane
reference. Review read-only; do not delegate or launch nested reviewers. Report
Blocking/Important/Advisory findings with location and scenario, or no findings
and residual gaps. Perform your review independently.
