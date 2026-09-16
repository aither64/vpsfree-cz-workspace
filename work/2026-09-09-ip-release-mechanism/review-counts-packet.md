# Follow-up review packet: mail grammar, member navigation and campaign counts

Initiative: 2026-09-09-ip-release-mechanism. Worktrees are under
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism/.
Tracking plan/state live under the corresponding work/ directory.

Review the committed follow-up against these previously reviewed heads:
vpsAdmin 46acba869d319726126e8d9337e9d53fcea7aa6d;
overlay 715c063396fa49277852b98d36347c8bec5160d3;
KB d76608007bf20710c16058ad7f1fe6b9d81fd4c9.
Final heads and quick results are recorded below before launch.

User-approved behavior:
- Requested/reminder subjects and text/HTML use singular vs plural based on
  allocations in the actual message. EN core and EN/CS overlay. Keep approved
  tone, location parentheses, support footer, HTML button, opt-out conditional,
  public IPv4 scarcity conditional. No response requested, no manual-release
  explanation, no forced-mode support/exemption instruction, no update notice.
- Page select-all checkbox belongs in its first header, no visible text,
  localized title/aria-label. Keep indeterminate state, restoration, narrow
  column and 500-row pages. Preview-wide all/none buttons remain separate.
- Member sidebar contains Networking and IP release requests. No redundant
  current-request link or Notice history. History is admin-only in UI and API;
  retain its exact admin name and audit data. Members see all their own
  requests, including closed requests; no other users or campaign metadata.
- Admin campaign Index/Show add total_ip_count, to_release_ip_count,
  kept_ip_count. Count snapshot rows, never allocation sizes. Use the existing
  protection evaluator, bounded iteration, once per response, no DB writes or
  new locks. Total includes all rows. To release includes eligible open rows
  and releases in progress even if closed. Kept includes assigned/host-routed,
  exported, admin-exempt, and policy-honored user reasons. Released, changed,
  closed unresolved rows count only toward Total. Explain non-partition with
  tooltips. Display same summary in admin list (one IPs column) and detail.
- No changes to locking, ownership, accounting, cleanup or release mutations.

Commit shape: preserve six pre-existing resource/IP-locking prerequisite
commits. Fold campaign API/model/mail/spec/docs changes into owning campaign
commit and PHP/CSS/gettext/browser tests into owning WebUI commit. Retain the
independent default-IP-fixture collision correction. Overlay stays in its
existing template feature commit. KB commit pins exact pushed vpsAdmin head.
Upstream advanced only API package gem metadata; rebase includes that update.
Assess the follow-up and commit boundaries without relitigating unchanged,
previously reviewed prerequisite design. Serious discovered regressions still
belong in findings.

Owners and consumers: vpsAdmin Ruby API owns status and authorization; its
pinned HaveAPI PHP client consumes discovered Index/Show counts. The API mail
builder supplies the actual eligible address array to core and site-overlay
ERB variants. Overlay metadata/interface is unchanged. vpsfree-kb-contracts pins
exact vpsAdmin for navigation/documentation tests; no new screenshot capture or
production KB publication is requested.

Risk: high because member authorization and public API output change. All
four lanes, gpt-6-astra/xhigh. No schema/state migration, counter persistence,
new framework or generic client/locking change. API must deploy before WebUI;
refresh discovery. Existing stored campaigns/notices/reasons remain readable.
Notice-history removal is intentional in this unmerged feature contract.
Dev API startup reruns seed overrides; snapshot existing data, update API, then
restore seed-managed settings/owners and reconcile overlay, verifying campaign
records and quota/PTR invariants. Never reset the review cluster for this change.

Documentation: vpsAdmin docs/ip-release.md owns current behavior, API fields,
count interpretation, member privacy and deployment ordering. docs/README.md
already links it. Tracking contains current rollout and durable seed-order
lesson. KB exact-pin checks assess managed page/navigation impact; user forbids
screenshot work. Leave the cluster and session open; no merge or lifecycle action.

Reviewer instructions: read applicable AGENTS.md, the mandatory-change-review
skill and your lane reference. Work read-only. Perform your assigned review
without nested reviewers. Report Blocking, Important, Advisory findings with
file/line and concrete scenario, or say no findings and note residual gaps.

## Final committed inputs and quick verification

- vpsAdmin base15ae9175c382a3661079c3b7f9446749b230ac74,
  headbb1dc50688cd5b46774371e637c29e5e33b42cd2. Campaign commit801abfb0c,
  WebUI432da0faf, fixture correctionbb1dc5068. Six prerequisites compare
  identically in range-diff; only hashes changed with rebase.
- Overlay base6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333,
  headf275bf35abc0dc501881b5af78b1e19fb98aec68.
- KB base8789cc1f5aeb3b19cbff13f741d6dd9960f14567,
  head32b01694eecfd9417447a60aa674b02f7f10db7a.

The KB update adds an explicit vpsadmin.inputs.vpsadminos URL retaining the
previous locked6bdf458 runtime. Plain nix flake update vpsadmin had reverted
that nested input to the API repository's older8e44 revision. The override
preserves the previously tested OS/nixpkgs; it does not upgrade the platform.

Quick checks:65 campaign API/model examples,64 passed with one invalid new
IPv6 fixture corrected to configure split_prefix:80. The corrected example
and English rendering matrix then passed in a focused2-example run. The API
checks include admin-only history, member-only all-own (including closed)
requests,501-row Index/Show counts and member output whitelists. The model
checks cover current policy toggles, assignment/host routing/export use,
exemptions, ownership/deletion changes, closure, cleanup pending and failed.
EN/CS overlay runtime matrix:88 examples,0 failures; both initial/reminder,
policy modes,1/2/5 allocations, public/privateIPv4,IPv6 and mixed messages.
Two synthetic HTML preview examples also passed. Core actual reminder-shrink
test verifies singular subject and bodies when six snapshots leave one
eligible allocation.

WebUI PHPUnit:96 tests,398 assertions passed. PHP syntax and configured
PHP-CS-Fixer check passed; Ruby lint passed. API/Czech normalization and
all commit hooks passed. Overlay checker73 templates/363 files and flake
check passed. KB full bin/check passed; existing60 concepts/120 variants
validated without capture generation. Browser full flow awaits this review.

Logs: /tmp/ip-release-counts-spec.log,
/tmp/ip-release-followup-mail-spec.log,
/tmp/ip-release-followup-overlay-render.log,
/tmp/ip-release-followup-phpunit.log, /tmp/ip-release-followup-kb-check.log.
