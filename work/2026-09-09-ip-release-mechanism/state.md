---
lifecycle: active
---

## Current follow-up (2026-09-16)

The mail grammar, header selection, member navigation/history and administrator
counts follow-up is implemented, pushed and deployed. The session and bridge
review cluster remain open. Existing campaign data was preserved.

Published branch heads:

- vpsAdmin: `58a9b71eae255fb2c5547b8be4c41d968ab4dc22`
- Notification overlay: `f275bf35abc0dc501881b5af78b1e19fb98aec68`
- KB contract: `2e5cb3b078ff99805fbc42075ed45a05b576a8f2`

The vpsAdmin series is based on `15ae9175c`. All six prerequisite patches and
the independent ninth fixture correction are unchanged by range-diff. Follow-ups
are folded into campaign API `dc483b57a`, WebUI `a8fa57999` and the overlay.
No schema, ownership, locking or daemon changes were added in this follow-up.
All branches remain unmerged. See commit-map.md for the review boundaries.

Four mandatory review lanes completed with fresh gpt-6-astra/xhigh reviewers.
General/architecture used collaboration agents; risk/scope used fresh read-only
ephemeral processes after the retained-thread limit was reached. Risk found
that expanded campaign responses bypass Show#exec and returned null counters.
Lazy initialization in the three getters fixes this; focused HTTP and once-only
model checks, lint and final network CI passed. Direct Index/Show still refresh.
This was direct remediation, so no new review round was required. Architecture's
query-cost advisory is recorded: 501 rows took 3.030s/2025 SQL notifications for
Index and 2.893s/2022 for Show. Retain the shared protection evaluator; larger
histories need measurement before optimization. Review packet and reconciled
results are review-counts-{packet,results}.md.

Verification:

- Final isolated `webui#networking-dns`: all five Playwright tests passed in
  8.6 minutes; full runner and teardown passed in 1514.48s, at 16:49 CEST.
  Covers creation, header selection, counts/policy, member privacy/navigation,
  notices/reminders, retention/assignment, release and closure. No screenshots
  or local kernel build. Log /tmp/ip-release-counts-browser-final.log.
- Live fresh-session checks passed for administrator and both members: matching
  list/detail counts, narrow header-only checkbox, indeterminate state, preview
  controls, own request lists, localized sidebar, hidden admin fields and denied
  history routes. No campaign changes. Log /tmp/ip-release-counts-live-browser.log.
  Existing live requests are all open; closed-request coverage is in API and the
  isolated browser test.
- API/model checks cover authorization, count states, 501 rows and shrinking
  reminders. Final full/core network and engine topic jobs passed. Overlay
  runtime matrix: 88 passing cases for EN/CS, initial/reminder, both policies,
  1/2/5 addresses and public/private IPv4, IPv6 and mixed lists. Core English
  rendering matrix and two synthetic HTML previews passed. WebUI PHPUnit:
  96 tests, 398 assertions. PHP/Ruby style, normalization and all hooks passed.
- Overlay checker (73 templates/363 files), flake check and hosted Check passed.
  KB full local bin/check and hosted Check35108117525 passed against the exact
  API pin. Explicit nested OS input preserves the prior OS/nixpkgs revision.
  No managed page content changes or screenshot generation were needed.
- API Specs35107887309 passed: all 26 topics and coverage are successful.
  All other current-head vpsAdmin workflows passed. KB Managed runtime35108117644 passed. Every final-head workflow is green.
  Superseded runs were cancelled only for older heads on this branch.

Deployment: services switched successfully to
/nix/store/ws24j6dzxskh4gv8hm2cfr7wwvr38wbl-nixos-system-vpsadmin-services-26.05pre-git.
Final API start and development signing-key unlock preceded seed-setting/owner
restoration and overlay reconciliation. All 3 campaigns, 5 requests, 12 address
rows and 7 notices match the private pre-update snapshot exactly. All three IP
resource quotas match allocations; retained/released PTR 21/30 and both running
VPSes passed. Campaign 3 has 4 total, 3 eligible, 1 kept at the verification timestamp;
its existing notices and reason are preserved. No campaign reset or additional
release was performed. Logs: /tmp/ip-release-counts-{services-update,api-start,restore}.log.
Current links and inventory are in review-guide.md and review-inventory.json.
Credentials remain in private storage; existing sessions should sign out/in once
to refresh API discovery.

All requested implementation, review, verification and development deployment
work is complete. The user can review the live interface; no failed or pending
check remains for these branch heads.
No merge, archive, deletion, shutdown or other session lifecycle action is
requested. The user explicitly selected this initiative despite the absent
DEV_SESSION_SLUG; the same worktrees and tracking have been retained.

Reusable lessons: notes/vpsadmin/2026-09-16-haveapi-expanded-association-output.md
and notes/vpsfree-kb-contracts/2026-09-16-preserve-nested-platform-input.md. Earlier
seed ordering and hook-signature lessons remain applicable. The September 16 consolidated
tracking checkpoint records this follow-up and the previous evening's completed
refinement. Unrelated shared-workspace changes are preserved.

# IP release mechanism

## Previous deployed checkpoint (2026-09-15)

The selection/member-view refinement is implemented and deployed to the
single/bridge development cluster. Runtime revision: vpsAdmin be21bc8b9
(API ad203b205). Published branch head 46acba869 adds a separate test-only fix
for an unrelated CI fixture collision. The eight feature commits and first six
prerequisites retain their exact hashes. All required reviews passed.

The reported pagination error is resolved in live browser checks. The running
API had been immutable a75 while WebUI used current files through its bind
mount. The updated API accepts 500-address pages. The administrator campaign
list retains ordinary 25-campaign pagination. Fresh login refreshes cached API
discovery in an existing WebUI session.

Services system: /nix/store/a2sycrs0pxll9j5s7w3jfp45mxmv05bw-nixos-system-vpsadmin-services-26.05pre-git.
Only disposable campaign tables were rebuilt from the final unmerged migration.
A private backup and complete row comparison verified preservation of all
campaigns, requests, notices, address snapshots and reasons. Campaigns 1 and 2
retain the user's interactions. Campaign 3 is unsent with four allocations
(public IPv4, IPv6 and private IPv4 across two members), due 22 September at
17:38 UTC. Final accounting, retained/released PTR and both running VPS checks
pass. No full cluster reset or local kernel build was needed.

Published heads: vpsAdmin 46acba869d319726126e8d9337e9d53fcea7aa6d,
KB d76608007bf20710c16058ad7f1fe6b9d81fd4c9, notification overlay
715c063396fa49277852b98d36347c8bec5160d3. All required reviews and verification
passed. All project worktrees are clean; feature branches remain unmerged.

- Live browser checks: administrator and both members; campaign list,
  500-address details, sidebar actions, multi-select/private/user filtering,
  selection controls, narrow checkbox column and member isolation.
- Final isolated browser regression: all five tests passed; full runner and
  teardown passed in 1518.56 seconds. No local kernel build or screenshots.
- Local API engine: 1,166 examples, zero failures, three expected pending,
  original failing CI seed 55211. Targeted API/PHP/migration/lint checks passed.
- Final API Specs workflow 35002860902: all 26 topic jobs and coverage passed.
  RuboCop, i18n and selected CI passed. The earlier engine failure was reproduced
  and fixed in the separate ninth test-only commit.
- KB static contract Check 35003281480 and Managed runtime 35003281177 passed
  on d7660800; local full bin/check passed too.

The review cluster and session remain open. Campaign 3, the account links and
suggested steps are in review-guide.md; credentials remain in private storage.
Existing sessions may need one sign-out/sign-in to refresh API discovery.
Next action belongs to the user: review the interface and flow. No merge,
archive, deletion or session lifecycle closure is authorized. No additional
tracking-only commit was made after today's existing consolidated checkpoint;
current notes remain in the coordination working tree under the same initiative.

## Previous validation checkpoint

The WebUI redesign is implemented and deployed in the accepted eight-commit
series. Current vpsAdmin head is a75bb80d5d4ce76e95c766199bc35e798fab956e,
pushed with an explicit lease on 564cc80ea5d4420d0f2441c996fb0df2f82bb39c.
KB pin 7222baa580476ce7f9c5c02deabece2744d92f9b is pushed; full contract passes.
All mandatory reviews and targeted checks passed. The final isolated browser
scenario passed (all five Playwright tests, including teardown, 1403.61 s).
All 26 hosted API Specs jobs passed on the final revision. The hosted integration
and KB managed-runtime workflows are still running.

Live browser verification passed for test-admin and both members: sidebar
navigation, creation preview, column headers, cross-owner bulk setting/removal,
restored selection, actor attribution, edit/release/close confirmation forms,
Notice history, and member isolation. Fixture verification confirms campaign 1
is unsent with five eligible allocations, two owners, no trial reasons or
exemptions, and exact IPv4/IPv6 accounting. Both member VPSes are running.
Actual DNS queries return review-ip.example.test. for .20 and no PTR for the
previously released .27. No further fixture mutation is planned.

Evidence: review-bulk-remove-results.md, /tmp/ip-release-remove-live-browser.log,
/tmp/ip-release-redesign-final-fixtures.log. Guide/inventory reflect the latest
fixture deadline: 22 September 2026, 14:44 UTC. Private access files are unchanged
and mode 0600. Session and review cluster remain open.

The user explicitly authorized resetting this initiative's dev cluster and
confirmed no fixture changes. They do not want screenshot deliverables; provide
live review links, a guide and private account details. Notice history keeps its
label. No merge or session lifecycle closure is authorized.

Published final-head workflows: API Specs 34982706137; CI 34982706278;
WebUI PHPUnit 34982706277; i18n 34982707003; RuboCop 34982706298;
migrations 34982706162; libnodectld 34982706251. All quick hosted workflows
passed, including all API Specs jobs; integrations are running. Previous workflow failures were
investigated from logs/artifacts and addressed (endpoint inventory and preview
submit timing). Superseded active runs were cancelled after each explicit-lease
push. Use gh api with exact head_sha filters for current runs.

## Previous status before WebUI redesign

The accepted eight-commit separation and locking hardening are implemented.
The single/bridge review cluster is running with two working member VPSes,
private access details and an unsent campaign. The final API, overlay and KB
heads are published. The user then reported a server error on the campaign list
page. A one-line HaveAPI invocation fix and admin/member list browser coverage
are being verified and folded into the WebUI commit; prior validation below
refers to the preceding head.
The session remains active;
no merge or lifecycle closure is authorized.

Current feature branch: `2026-09-09-ip-release-mechanism` in all three worktrees.

- vpsAdmin: `aa9ac1e3af0acde65e15fd2c9758d1613689fed0`, pushed with an explicit
  lease, eight commits on `ff5d5e5914bf5746e649f3a986659e4193717044`.
- Notification overlay: `715c063396fa49277852b98d36347c8bec5160d3`, pushed,
  one commit on `6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333`.
- KB contracts: `243b15895e7a0f7b13eb63b96c348df309e2e2e5`, pushed with an
  explicit lease, exact aa9ac1e3a pin on
  `8789cc1f5aeb3b19cbff13f741d6dd9960f14567`; OS runtime 6bdf458 retained.

The prerequisites are separate: relative resource provider, charge provenance,
network identity, shared IP reservation/current-read helpers, composite relative
IP accounting, cleanup before disownership; then campaign API and WebUI.
No generic Lockable or TransactionChain locking interface changed. Both SQL
row locks and existing vpsAdmin resource reservations are used, for different
lifetimes, as explained in `docs/ip-locking.md` and locking-refactor-audit.md.

Original API/overlay `-before-split` refs and construction `-split` refs remain.
Four mandatory astra/xhigh review lanes completed; four Important findings were
fixed and verified. See review-split-results.md. Live inspection then found stale
XTemplate form wrappers; a bounded fix was folded into the WebUI commit and
reviewed by all four fresh astra/xhigh lanes with no findings. See
review-form-results.md. The final rebase only incorporated upstream's docs/
rename and PHPUnit update; range-diff verified unchanged implementation.

Validation completed:

- All eight local network/DNS/browser integration scenarios passed (4279.21 s),
  including live PTR-before-release and assignment paths. Log:
  `/tmp/ip-release-split-integration.log`. No local kernel build.
- Actual API/NodeCtld confirmations: 12/0 (seed 63630), covering successful
  cleanup, failure, rollback and retry. Generic provider and non-IP consumers
  passed the focused checks in review-split-results.md.
- All 26 hosted API Specs jobs passed at 4d53fa157 (34960278822); API code is
  byte-identical at final aa9ac1e3a. Lint, i18n, migrations, libnodectld,
  WebUI PHPUnit and overlay Check also passed there.
- Final form syntax and capacity contract pass, including upstream PHPUnit
  13.3.4 (1 test, 2 assertions).
- Full KB contract passed on 4d53fa157 with no page or screenshot drift;
  final exact pin check also passed (same counts, no drift).
- Real OAuth logins work for test-admin, test-user1 (CS), test-user2 (EN).
  Live campaign/member form checks pass; screenshots are in review-screenshots/.
- Separate live smoke campaign 2 sent an initial notice and two reminders,
  delivered to Mailpit with plain/HTML parts, correct location/IPv4 context and
  approved closing. Early release removed IPv4 .27 and its PTR. A changed policy
  released retained IPv6, while an admin exemption remained. Quota equals owned
  allocation totals. Main campaign 1 and its eight unassigned addresses remain
  untouched. Final smoke log: `/tmp/ip-release-smoke-final.log`.
- Actual DNS queries confirm review PTR .20 remains and smoke PTR .27 is absent.
- A delivered HTML button was clicked in a fresh browser. The guest page
  requested sign-in; using its login control completed real OAuth and returned
  test-user2 to the correct request.

The updated isolated browser scenario `webui#networking-dns` passed, including
VM teardown (1242.72 seconds total; example 435.37 seconds), at 14:44 CEST. Its
immutable Playwright suite, campaign form, API models and API library match
the final source byte for byte. Log:
`/tmp/ip-release-form-integration.log`.

Pending hosted validation: final-head API Specs 34968848791 (24/26 jobs green
as of 14:51 CEST; both platform jobs still running), CI 34968848861 and
KB managed runtime 34969414263 (both queued). Previous successful platform
jobs took 31–35 minutes; the current durations are within that range.
Final KB Check 34969414240 passed. Old
in-progress CI 34960278529 was cancelled after the explicit-lease push because
its head was superseded. Superseded KB runtime 34960640899 was also cancelled
after the final pin push.

The services update to aa9ac1e3a completed successfully. The development seed
reapplied nil owners to its two declared assigned IPs while preserving their
quota; their recorded owners were restored under the shared IP lock. Review
policy, languages, IP free-chain definitions and overlay were reapplied.
Post-update checks pass: both VPSes running, all eight custom review addresses
unassigned, campaign 1 unsent, both members' exact ownership accounting and
separate smoke outcomes preserved. No further fixture mutation is planned
after access was handed to the user at approximately 14:38 CEST.

See review-guide.md and review-inventory.json for the campaign, addresses and
suggested manual flow. Private credentials are outside tracking under
`/home/aither/.local/state/ip-release-review/2026-09-09-ip-release-mechanism/`
(mode 0600 in a 0700 directory), never portal artifacts. Keep the cluster running
and the session open after handoff.

Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-09-ip-release-mechanism/

## Earlier progress notes

Validation checkpoint: current-head CI is green for RuboCop, i18n, API
migrations, libnodectld specs and WebUI PHPUnit; overlay Check and KB Check
are green. API topic jobs and full CI/KB managed runtime are still running or
queued. The first local network scenario (export enable/disable/hosts) passed
including teardown, in 928.7 seconds. Initial VM/API startup was slow but
completed; KVM acceleration was confirmed and no local kernel build occurred.
Fixture setup is prepared in review-fixtures.rb and syntax-checked, not executed.


Node confirmation engine verification passed all 12 IPv4/IPv6 success, failure,
rollback and retry cases (seed 63630). The first harness launch loaded the wrong
bundle because the component shell hook overwrote pre-set BUNDLE_* variables;
post-hook exports fixed it, as recorded in the existing durable note.
KB contract passed: 45 controls/36 paths/35 capture concepts/3 selectors,
94 bindings/9 exceptions, 4 pages/8 variants/12 tests/21 executable samples,
60 test cases/194 assertions, and 60 concepts/120 PNGs. Exact pin commit
dfebd25c2c782cffc893adf83f57306b0216b42d is pushed. A plain input update
initially reverted the inherited OS pin; a Nix override-input update restored
6bdf458, leaving only the intended vpsAdmin node changed in flake.lock.


The reviewed series is now published on the canonical feature branches:

- vpsAdmin: `4d53fa1573bf5d0ba8de5d896153e4ca21dcfb5a` (eight commits on
  `c38839d5b`). Final prerequisite heads: ffffa52f2, f3cef8d15, 316e92c0e,
  b7e625f87, 4b419cc24, e5a7202ef; campaign API 5188056bd, WebUI 4d53fa157.
- Notification overlay: `715c063396fa49277852b98d36347c8bec5160d3` (one commit
  on `6ebfb6f`). Original API/overlay heads remain in local `-before-split`
  refs, and construction `-split` refs are retained.
- KB exact pin update to the new API head is in progress on base `8789cc1`.

All four Important review findings are resolved and tested; details are in
review-split-results.md. Direct fixes were folded into their owning commits.
Two expected conflicts in the IP Free spec were resolved while folding;
final Git tree 5a8cd4a4bb531e082e732a9bf3e65083f0b65aa9 is byte-identical to the
verified pre-fold tree. All commit hooks passed. A fresh upstream fetch found
no further movement. Pushes used explicit leases for the original feature heads.

Current-head CI started (API Specs 34960278822, CI 34960278529); superseded
original-head in-progress CI 34943116818 was cancelled after the rewrite push.
Long local integration started with network/*, dns/zone-transfer-config,
tasks/dns-reverse-record-check and webui#networking-dns, jobs=2, state directory
/tmp/ip-release-split-integration-state, log /tmp/ip-release-split-integration.log.
Actual API/NodeCtld confirmation/rollback check is running separately in the
combined temporary Gemfile environment. Review cluster remains stopped until
validation completes.


All four mandatory review lanes completed on the split series; see
[review-split-results.md](review-split-results.md). Four Important findings are
being fixed directly: legacy teardown, current assignment policy, compatible
automatic charge selection and teardown dependency ordering. Scope passed.
The first 14 focused regressions passed; expanded/final checks are in progress.
No long integration or cluster startup has begun yet.

Implementation of the accepted commit-separation/hardening/review-cluster plan
has started. The previous status below describes the preserved input heads.
Initial project worktrees are clean at vpsAdmin 395bf80b7, overlay 51c8f2c3 and
KB 87bc0fbc. The user explicitly selected this existing initiative; process
DEV_SESSION_SLUG remains unset and dev-session current finds none, so no new
session or lifecycle operation is performed. Cluster startup is now explicitly
authorized after validation. See plan.md's accepted follow-up for scope.

Construction branch: 2026-09-09-ip-release-mechanism-split in the existing
vpsAdmin worktree. Refreshed/rebased onto current origin/master
c38839d5be62e9d40d055b23a84844e2037ba4db. The six prerequisite heads are now
ffffa52f2 (provider), f3cef8d15 (provenance), 316e92c0e (network identity),
a9dd51bb1 (IP helpers), fc1640374 (relative IP accounting), 77ee3ca3a (cleanup).
All commit hooks passed. Canonical feature remains preserved at original
395bf80b76b2e715fbad25f7c637c5763dc35ad5 until the complete series is verified.

Campaign API step is committed as 40ca8c082, with final approved mail/spec changes
folded in and release using the shared IP helper. The schema merge retained the
new upstream version and only adds the four campaign tables. The 48-example
model run had one imported test still calling reallocate_resource!(delta:);
updated it to adjust_resource! and the focused example passed (see /tmp/ip-release-campaign-focused.log). Migration checks run in a
separate process and pass 2/0 seed 533. API authorization passed 9/0 seed 42032; all 24 overlay render
cases passed, seed 57865. Full-plugin locale regeneration preserves upstream keys.
Accidental generated-schema lint formatting was restored from the resolved
index; only the intended new tables remain. See the new verification note.

WebUI step is committed as 201c263919049792315598efd4fea5d1a5cfe950, with the original browser correction folded in. The
translation merge removed an obsolete duplicate Disabled entry and regenerated
PO/POT/MO from current sources. Three relevant PHP tests pass (12 assertions);
a CLI flag deprecation was diagnostic-only (--do-not-cache-result is renamed
--do-not-record-test-run-history in PHPUnit 13). Browser JS syntax passed using
Nix-provided nodejs. CI selection: 16 tests/55 assertions pass; all 413 ordinary
API spec files map to exactly one of 13 topics. Migration specs are correctly
excluded from that matrix and covered by their separate workflow. Representative
network/DNS selector enumeration passed, including network lifecycle/route/host,
export, DNS/PTR and webui#networking-dns cases; only runner Ruby packages built.
All WebUI commit hooks passed. All three project worktrees are clean.
Four-lane high-risk mandatory review is being launched against the exact
heads in review-split-packet.md, gpt-6-astra/xhigh with fresh context. No long
integration test started yet.

Overlay construction head remains 715c063 on upstream 6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333.
KB fetched/rebased onto 8789cc1 (current upstream). Its only old feature commit
was an obsolete pin that conflicted with all five newer upstream pin files;
it was dropped during rebase. Current KB branch is clean at upstream and will
receive a new exact feature pin after the reviewed vpsAdmin head is pushed.
This also removes the old explicit OS pin override; preserve the current
upstream runtime dependency when updating the feature pin.

Fourth rebuilt vpsAdmin commit: b5781fdce (shared IP/host reservations and
writer checks), root hooks passed. Current-owner checks use shared SQL reads
for the effective VPS owner; staged export grants have an explicit reserved
path. Separate-connection host/export/DNS grant ownership cases pass. Final
focused sets: 10/0 seed 14321 and 28/0 seed 4487; original broad writer check
114 examples included two corrected fixture errors and one existing pending.
No generic Lockable or transaction-engine lock contract was changed.

Fifth rebuilt commit: c4c7cac65 (relative IP callers and composite totals).
Concurrent ownership/allocation checks passed in the 44-example run, with two
existing pending contracts. Corrected new fixture joins and created the clone
fixture's missing usage row; focused Clear/SoftDelete/Destroy checks passed
(seed 3606), and two-interface clone passed (seed 6221). Root hooks passed
after correcting one final test hash alignment. No runtime fix was needed
for those fixture/style failures.

Sixth step: cleanup now precedes final disownership and quota deduction; Free
uses the common cleanup chain. Host deletion waits for transfer cleanup even
without a PTR. 21 relevant model/concurrency checks passed (seed 3078), touched
Ruby lint passed, and the WebUI completion test passed (2 tests/10 assertions).
Czech cleanup translations regenerated; commit hooks are running.

Third rebuilt vpsAdmin commit: f9f73b771 (network registration/resource
identity), root hooks passed. It reloads current cached network metadata and
releases only its successfully acquired resource reservation. The original
IP hardening is separated from accounting, cleanup and campaign behavior.

Second rebuilt vpsAdmin commit: de251e883 (charge provenance). Focused model
and full Network/IpAddress API resource checks passed: 74 examples, zero
failures (seed 22571); touched RuboCop and root commit hooks passed. An initial
command used a nonexistent ip_address_write_spec.rb path and aborted before
running examples; corrected to the actual ip_address_spec.rb.

Network registration step: eight model/concurrency examples passed (seed
59864), plus three targeted API cases (seed 62742) and touched RuboCop. In
addition to the original role/family barrier, it reloads cached network metadata
before selecting a batch and only releases its successfully acquired resource
lock. Original-head integration CI 34943116818 remains in progress at the last
read-only check; no failure result to investigate or rerun was reported.

First rebuilt vpsAdmin commit: f6bf88c21 (generic relative accounting), with
root commit hooks passed. Overlay reconstructed on its refreshed upstream as
construction branch 2026-09-09-ip-release-mechanism-split, commit 715c063
(single consolidated template change); original canonical overlay branch/head
51c8f2c3 remains retained. Overlay flake check passed. Its final member-facing
wording was reviewed directly and remains unchanged from the approved versions.
Read-only devcluster status reports this initiative stopped; no startup or
lifecycle mutation has been performed yet.

Accounting step verification: 82 provider/concurrency examples passed (seed
64009); 35 absolute-contract examples also passed against the original upstream
provider (seed 54415); 110 provider and real VPS/dataset consumer examples passed
(seed 43556). New coverage includes refquota rejection/override, automatic
expansion beyond the allowance, first-use races, stale usage and stale budget
snapshots. The first run failed because new numeric-budget fixtures omitted the
required value and confirmation expectations used strings instead of symbols;
those fixture errors were fixed. Source behavior was not changed to satisfy them.
API topic coverage already includes these new files through the engine glob.
Post-checkout reported an Overcommit signature error after successfully switching;
reviewed unchanged hook configuration and signed it in the root Nix shell.

The IP release mechanism is implemented on retained feature branches. The
September 15 follow-up replaces the presumptive email closing with “Děkujeme
za tvůj čas.” / “Thank you for your time.” across built-in and overlay EN/CS
text/HTML notices and reminders. Forced-release notices still omit exemption
advice; shared VPS-assignment guidance and opt-out policy gating are unchanged.

The failed API Specs workflow 34491288836 was a test assertion false positive:
192.0.2.20 matched eligible 192.0.2.200/32. Explicit overlapping fixtures
reproduce both affected initial/reminder tests; CIDR assertions fix them.
The complete core-engine suite passed the original CI seed 24922: 912 examples,
zero failures, 50 existing pending. All 24 overlay render cases, overlay flake
check, touched spec RuboCop and commit hooks passed. Prior complete integration
CI 34491288911 passed on 7483c4d25. See ci-investigation.md for all findings.

Current local and pushed vpsAdmin head: 395bf80b76b2e715fbad25f7c637c5763dc35ad5,
including spec fix 36a6869fe93b2699eafa2f75a8ae1ecf7be38d15. Current local and pushed
overlay head: 51c8f2c3f94b094ca93e1bddb719e0b23a9e04ab. Both worktrees are
clean and pushed. V8 general and architecture reviews passed without findings.
Current-head core-engine CI (the previously failed job), RuboCop, i18n and
notification overlay checks passed. The remaining API matrix and integration
run are still in progress, with no reported failures. KB contract
87bc0fbcb267292a30867d7a5f90eee92552fc10 remains clean and pushed, pinning
871fa3dae for the unchanged WebUI contract. No new KB pin or capture is needed.

locking-notes.md explains existing prerequisite commit 664e1e184: both vpsAdmin
resource locks and short SQL row locks, their race coverage, contention costs,
and the additional accounting/validation behavior bundled there. No locking
implementation was changed in this follow-up. Refreshed upstream master has
advanced substantially; reconcile with it before future integration.

No production writes, merge, deployment or session lifecycle operation occurred.
The session remains active and open. Historical sections below retain previous
heads/results; this status takes precedence over them.

## Verification summary

- September 15 copy/spec correction: 912 core-engine examples, zero failures,
  50 existing pending; 24 localized rendering examples, zero failures; flake,
  touched RuboCop and hooks passed. V8 general/architecture review passed.
- Previous forced-mode copy: 25 notification/render examples passed, overlay
  flake and hooks passed, v7 general review had no findings. Hosted integration
  34491288911, RuboCop 34491288966, i18n 34491288907 and overlay Check
  34491267241 passed; API 34491288836 failed only the assertion fixed above.
- Email-copy follow-up: 38 campaign examples and 24 localized render/routing
  combinations passed; overlay flake check, touched RuboCop and hooks passed.
  General v6 review found no issues. Copy-head CI is running: vpsAdmin
  integration 34484865348, API topics 34484865323, RuboCop 34484865318,
  i18n 34484865320. Overlay Check 34484854385 passed.
- Four v5 review lanes completed at gpt-5.6-sol/xhigh. Reminder template metadata
  and the directly owned browser fixture's charge environment were corrected.
  Earlier ownership/accounting changes retain their v1-v4 review evidence.
- Final focused API resources: 9 passing; models/concurrency: 48 passing;
  migration tests: 2 passing in a separate process. Earlier broader writer,
  authorization and quota regression results are recorded below.
- Actual API + NodeCtld confirmation harness: 12 passing combinations covering
  success/failure/rollback, IPv4/IPv6 and default/user-created host addresses.
- Overlay: 24 passing render/routing combinations across CS/EN, initial/reminder,
  both policies and IPv4/IPv6/mixed lists, plus HTML escaping and absolute URLs.
  Flake check and current-head hosted Check 34466827250 passed.
- PHP: 91 tests/368 assertions; touched Ruby, JS, Nix and localization checks
  passed. Hosted migration, RuboCop, PHP, i18n and libnodectld checks passed.
- Hosted API matrix 34466834918 passed all 26 core/full topics and coverage.
  Product component trees are unchanged by the two later test-only commits.
- Hosted integration 34469920231 passed all four task scenarios on 871fa3dae,
  including real authoritative PTR removal and ownership finalization.
- Local webui#vps-user-core passed all four browser tests. The focused
  webui#networking-dns rerun passed all five tests, including the actual HTML
  email button/login, no GET mutation, retention, assignment, policy override,
  eligible-only reminder, manual/repeat release and notice history.
- Hosted integration 34474145934 passed all 12 selected network/DNS tests on
  feccc0073. No stale in-flight branch run needed cancellation.
- Full KB bin/check passed: 60 tests/194 assertions, navigation/page bindings
  and 120 screenshots. No existing documentation/capture drift. Current-head
  Check 34470210306 and managed runtime 34470210256 both passed. The
  preceding runtime 34467150396 also passed on the identical product trees.

## Repositories

All three use branch 2026-09-09-ip-release-mechanism and worktrees beneath
worktrees/2026-09-09-ip-release-mechanism/:

- vpsadmin: base 19971f039771500d5d0304610f91fe6f4af5fed3.
- vpsfree-notification-templates: base 9e1ddbd973703cf48a43f0e5afc2bfb392a8b676.
- vpsfree-kb-contracts: base 81d6d7dfe530884aff3e1d2634e02e4b12fe28e8.
- Shared workspace remains master; unrelated working-tree changes are preserved.

## Setup and observations

- Verified dev-session current matches VPSFREE_DEV_SESSION_SLUG.
- Read current workspace/repository rules and review/handoff/writing skills.
- vpsadmin worktree add completed checkout and portal registration but returned
  failure from an unsigned Overcommit configuration. Reviewed .overcommit.yml;
  installing/signing via root nix develop. Reused existing Overcommit notes.
- Implemented additive campaign/request/address schema, scoped HaveAPI resources,
  explicit notices, manual release chains, user reasons and admin exemptions.
- Added WebUI campaign preview/create/edit/release and owner retention forms,
  Czech catalogs, built-in and localized overlay initial/update mail templates.
- Hardened the affected IP allocation/assignment writers to lock and reload before
  ownership changes. Added relative quota updates using a current locked read to
  avoid lost changes under MySQL REPEATABLE READ.
- vpsadmin committed API717397727 and WebUIdbc18632c; all hooks passed.
- Notification templates committed as 420c98c; its flake check passed.

## Verification so far

- Focused API/model specs: 15 examples, 0 failures.
- Models, independent-connection concurrency, existing Ip::Update and AddRoute:
  21 examples, 0 failures before the final relative-quota and assignment tests;
  expanded final suite passed: 23 examples, 0 failures.
- Migration suite independently: 2 examples, 0 failures.
- API locale regeneration/health passed. WebUI gettext health and CI selector
  tests passed; finishing formatting checks and regenerated artifacts.
- Overlay nix flake check passed with all new templates staged.
- Added a Playwright scenario covering initial/update notices, login return,
  escaped user reasons, assignment, forced policy, exemption and repeated release.
  Long integration tests have not started; mandatory review must run first.
- Migration specs cannot share an RSpec process with ordinary model/API specs:
  migration_helper switches the global connection and resets its separate DB.
  Rerunning separately resolved the test invocation failure.
- API locale tasks run from the API shell/cwd, not the root Rakefile.
- No project branch pushed, merged or deployed yet.

## Accepted behavior

- Whole-campaign admin release, any time; advisory deadline, no mail gates.
- Campaign-wide editable policy; current policy overrides/restores user reasons.
- Separate admin exemptions; user reasons accepted until release or close.
- Initial notices and repeatable explicit reminders; no update mail or automatic campaign actions.

## Next steps

The requested final wording is implemented, reviewed, tested and pushed. New
hosted checks on the exact heads are running/queued; inspect results before
integration and investigate any failure. All feature branches and this session
remain open. Merge/deployment remain outside this request; the documented
writer rollout and legacy quota reconciliation are prerequisites for later
operational use. Refresh against current upstream before integration.

## Portal / cleanup

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-09-ip-release-mechanism/

Feature worktrees remain for review and follow-up. Do not archive/stop without
explicit user direction.


## Mandatory review

High risk (schema, tenant scoping, destructive ownership and quota changes).
Review packet: review-packet.md. Launching general, architecture/repetition,
scope/proportionality and risk/compatibility lanes, each fresh gpt-5.6-sol xhigh.
Reviewed heads dbc18632c and420c98c; no integration tests started yet.

- PHP regression suite: 88 tests, 356 assertions, all passed.
- API topic coverage: all 392 ordinary specs mapped exactly once (per-topic
  glob results are deduplicated, matching CI).
- Preliminary KB contract check against feature source passes: 44 controls,
  35 paths, 35 concepts, 3 selectors. See kb-impact.md; exact pin still pending.
- Reused notes/vpsadmin/2026-07-25-migration-spec-database-isolation.md for the
  mixed-suite invocation issue. Added a note for split-commit gettext hooks.
- Local narrow WebUI follow-ups pending: correct perex browser selectors,
  avoid touching an admin resource when users submit a reason, label each
  admin address table with its owner. These will be folded into the WebUI commit.

## Initial review findings and remediation

All four lanes reviewed immutable vpsadmin dbc18632c and overlay420c98c,
using fresh gpt-5.6-sol/xhigh agents. Scope reported no findings. General,
architecture and risk found overlapping issues:

- Blocking: host/PTR/route-via/DNS-transfer writers did not all share the parent
  IP lock, and DNS transfer grants survived release. Adding shared host/parent
  locking, fresh actor checks, current dependency reads and transfer cleanup
  before ownership removal. Include existing child workflows in quick tests.
- Blocking: member Keep constructed an admin-only campaign resource. Fixed by
  constructing campaign clients only for campaign mutations.
- Important: notification history was overwritten. Replaced mutable request
  pointers with append-only notice records and a scoped paginated API/WebUI view.
- Important: unbounded preview could hit PHP max_input_vars and silently omit
  selected IPs. API campaigns capped at 100, preview/list pagination added and
  selection completeness checked before create/keep.
- Important: exemption description polluted generic reason metadata and new
  labels were identifier-derived. Moved exemption instructions to the action
  description; labels/descriptions now live in resource declarations.
- Important/general: browser perex selectors and owner labels fixed.
- Advisory: IPv6 allocation-unit regression added; relative/absolute quota API
  now rejects ambiguous or missing mode. Status string centralization deferred:
  the current finite values agree and the API is additive; no general state
  framework is warranted for this feature.

These remediations are uncommitted and still undergoing focused checks. New
notice/schema and shared locking behavior require architecture/risk reruns;
scope should assess the added bound/helper contract as well. Do not start long
integration tests or push until required findings are resolved.

Quick invocation correction: requested separate PTR chain specs do not exist;
reran with the existing HostIpAddress API and host/DNS chain coverage. No product
failure was inferred from the initial RSpec loading error. PHP CS Fixer uses the
root .php-cs-fixer.dist.php, not a WebUI-local file.

## Remediation verification

- Expanded model/chain/concurrency run passed 41 examples, including the new
  IPv6 prefix and DNS transfer cases. Their first failures were invalid fixtures:
  the IPv6 network split_prefix was still /128 and cleanup had no available node.
  Tests now use matching /80 allocation metadata and queued DNS cleanup, checking
  grant removal from the active set and the resource lock while cleanup runs.
- Existing HostIpAddress API coverage passed in the 91-example expanded run.
  Candidate pagination required the action's IpAddress model and the standard
  HaveAPI request namespace. The corrected boundary case passes; HaveAPI semantic
  errors use HTTP200 with status=false, and the test now checks that contract.
- Follow-up found deferred quota confirmations could overwrite synchronous
  release accounting. Converted IP quota writers (registration, VPS create,
  clone, chown, migration and route deletion) to relative reads; deferred edits
  hold the existing UserClusterResource chain lock, and synchronous relative
  updates respect that lock. A pending-quota regression prevents premature
  release. This is part of the required all-writers deployment boundary.
- Expanded final accounting/model/VPS/route and candidate API run: 71 examples,
  0 failures, 2 pre-existing pending contracts (clone keep_snapshots and migration
  with multiple interfaces). No pending contract was introduced here.
- Final WebUI PHP regression suite passes 88 tests/356 assertions. Node syntax
  check passed through nix shell nixpkgs#nodejs. RuboCop, PHP formatter and gettext
  health pass. New browser coverage also rejects incomplete selection submission.
- Folding review remediations into the original API and WebUI commits, then
  preparing affected review reruns. No integration tests/pushes have started.

Final pre-rerun vpsAdmin heads: API1d6ebc974, WebUI3f5e700bf; clean.
All hooks passed. Final migration run2/0. Ambient git rebase again encountered
an Overcommit signature mismatch; running it inside root nix develop succeeded
without bypassing hooks (the known shell/framework-version issue).
Review reruns apply to all four lanes because new notice/pagination UI and
expanded writer/accounting contracts affect general, architecture, risk and
scope. Fresh agents use gpt-5.6-sol/xhigh and review-packet-v2.md.


## Second review and ongoing rollback remediation

Fresh scope/architecture/risk v2 reviewed immutable 3f5e700bf/420c98c.
General v2 has not been launched; implementation changed before a slot freed.
All findings below are being addressed in the working tree; no integration or
push has started. Current committed heads remain API1d6ebc974/WebUI3f5e700bf.

- Blocking missing Network#add_ips relative quota writer: converted; independent
  connection old-snapshot regression passed.
- Blocking migration/swap source IP/host locks and stale replacement selection:
  Migrate::Base setup locks/reloads all source parents/hosts (covers both nested
  swap migrations); replacement selection now has a helper that locks/reloads
  and validates availability. Independent-connection stale-selection regression
  passed, as did migrate/swap simulated-detach lock regressions.
- Blocking chown vs DNS transfer creation: chown now locks parent/host children
  before accounting/cleanup. Regression rejects new transfer during queued chown.
- Blocking standalone transfer deletion rollback: Destroy now locks/reloads
  parent/host before zone and transfer. Free/DelRoute/chown use shared cleanup.
- DestroyUser likewise locks discovered parents/hosts before zone, current-reads
  membership under zone lock, and rejects a newly added unlocked host for a
  manual retry. No automatic retry mechanism introduced.
- Important opposite-direction quota transfers: source/destination config rows
  now prelocked in ID order in Ip::Update, VPS chown and both migration helpers.
- Architecture's claimed same-config quota lock inversion was retracted after
  inspection: both relative modes first lock the same config row.
- Important commit separation accepted: split existing writer safety/accounting
  prerequisite from additive campaign API; then WebUI. Not yet rewritten.
- Advisory member notice history retained: useful owner-scoped record of the
  notice received when policy changes; no extra mutation surface. Bounded query
  fan-out accepted for first version. Status constants advisory remains accepted.

Quick v2 run passed 30 examples/0 failures/1 pre-existing migration pending.
Expanded v2 run passed 66 examples/0 failures/1 existing pending, including the
new Network and stale migration replacement independent-connection tests.
Logs /tmp/ip-release-v2-writers.log and /tmp/ip-release-v2-final.log.

Risk's final Blocking finding requires a design correction: asynchronous cleanup
can restore old DNS/PTR/host rows on rollback and release locks on ordinary
failure. Synchronously removing ownership first could expose restored grants
on a redistributed IP. In progress: Ip::Update defers ownership and quota to a
final successful edit-after confirmation whenever cleanup appends transactions.
It returns that Confirmable to the release chain, which puts its release stamp
and active-claim removal on the same confirmation. Empty cleanup stays immediate.
Pending release is shown as releasing; reasons/exemptions cannot change an
already initiated attempt. Failed cleanup keeps ownership/quota and requires a
new manual admin action. Policy edits govern future attempts; close does not
cancel already initiated cleanup. Need actual node-confirmation success/failure/
rollback checks and updated model/API/UI tests and prose before committing.
This is a new design and requires fresh affected review lanes after quick checks.

Browser fixture follow-up (uncommitted): networking-dns script temporarily enables
local test mail and seeds accurate public IPv4 accounting for directly inserted
owned fixtures before Playwright. Mailpit already enabled globally in tests;
preference restored afterward. No delivery check added to the product.


Deferred finalization and new allocation provenance are now implemented, still
uncommitted. Ip::Update returns the final Confirmable for asynchronous disown;
Release adds its item edits to it. Detect appended cleanup via last_id change,
not nested chain.empty? (included chains do not own the outer size counter).
Ownership/quota/claim remain until success; current chain status governs pending
and failed item display. Policy edits/close cannot cancel initiated work.

- Actual API + NodeCtld::Confirmations + Command#close_chain checks passed 3/0:
  execute success, execute failure, rollback; all include PTR, DNS transfer and
  user-created host cleanup, preserved accounting on failure, manual retry,
  quota once and actor/owner/chain audit. Artifact confirmation-check.rb. Log:
  /tmp/ip-release-confirmations.log. Temporary composite bundle under
  /tmp/ip-release-confirmation-env/Gemfile, BUNDLE_PATH=<worktree>/api/.gems,
  VPSADMIN_CHECK_ROOT=<vpsadmin worktree>; run from api in .#libnodectld shell.
- A harness failure first needed the libnodectld native RUBYLIB shell, then
  restoration of raw MySQL query_options after NodeCtld. See new durable note
  notes/vpsadmin/2026-09-09-api-node-confirmations.md.
- Final capacity/concurrency run passed 23 examples/0 failures, including a
  100-allocation managed-network campaign released twice, legacy null charge
  provenance retained/reported, both standalone and bulk DNS deletion locks,
  independent network accounting and migration stale selection, and opposite
  ownership transfers through real SQL lock barriers.
- New IpAddress.register and Network#add_ips persist their actual charge
  environment. The deployment doc contains a legacy audit SQL and requires
  explicit accounting reconciliation before setting missing provenance. No
  current-location inference or silent data backfill. Other campaign items
  continue when a legacy item fails. API/model tests use natural registered
  charge data instead of repairing it in the campaign fixture helper.
- Audit authority is the campaign item (original owner/allocation and confirmed
  release actor/time), its attributed chain, and PaperTrail pending-attempt
  history. Deferred final SQL confirmations do not generate PaperTrail callbacks;
  release timestamp identifies the admin attempt, chain log records completion.
- Final gettext health and selector suite passed (16 tests, 55 assertions).
- Expanded deferred API/model tests still running; final PHP tests running.
  Need commit/split, fresh review lanes, browser integration and pushed CI.

## Final series and v3 review checkpoint

Deferred finalization, provenance and the browser fixture correction are now
committed. Split the existing writer prerequisite from the campaign API; final
series is efe60cf3493e5ca784776bfd24ce4d497ef77c06,
9fd2d741b7da8df57b7ffc078b4932a147d4c7bf,
5a028e0f9529befc0e849a186b0d10a1a2fd149a. All hooks passed and the
final tree matches the pre-split c8f47bbc7 tree exactly. Fetched origins; vpsadmin
base remains current at 19971f039. No branches pushed.

Expanded deferred API/model suite finished: 120 examples, 0 failures, 1 existing
pending migration example (/tmp/ip-release-deferred-checks.log). Final PHP suite
passed 88 tests / 356 assertions (/tmp/ip-release-final-phpunit-v3.log). Final
workflow topic checker maps all 393 ordinary API specs exactly once. Capacity
and actual node confirmation results remain as recorded above.

New durable notes record cross-version RuboCop directive compatibility and Git
rebase exec clean-index requirements. Neither required bypassing hooks.

Fresh v3 general, risk and architecture agents launched against immutable
review-packet-v3.md; scope follows when capacity frees. All four lanes are
required for the expanded writer boundary and deferred finalization contract.
Model gpt-5.6-sol, effort xhigh, risk high. No long integration until findings
are reconciled. Running bounded existing VPS create/clone regressions meanwhile.

Existing VPS create, clone and os-to-os clone follow-up: 18 examples, 0 failures,
1 existing pending keep_snapshots expectation; /tmp/ip-release-create-clone-v3.log.
This confirms new registration charge provenance through the existing consumers.

## V3 review remediation in progress (uncommitted)

General v3 finished against 5a028e0f/420c98c; architecture/risk still finishing.
Scope has not run against the final series yet. Consolidated accepted findings:

- Blocking (all three): owned Network.AddAddresses without environment creates
  uncharged NULL provenance. Require user/environment together before creation,
  validate availability, reject owned IpAddress.register without provenance.
- Blocking (general/risk): Ip::Free selected by topology and trusted stale owner.
  It now selects charged_environment_id, reloads/rechecks owner and charge under
  IP lock, and defers owner removal until after host/DNS cleanup.
- Blocking (general/risk): public route/host assignment/removal trusted pre-lock
  authorization. NetworkInterface now passes actor into entry chains, reloads
  interface/VPS owner, repeats shared route validators under lock, and checks
  host actor/assignment/routed dependencies. Internal included chains retain
  their explicit operational semantics. Focused tests still needed for all cases.
- Blocking (all three): free owned IPs can be NFS ExportHost clients. Campaign
  retains them with exported status. ExportHost#lock_ip! serializes every
  create/edit/delete/destroy path, including direct VPS chown grant creation.
  It rechecks stale owner/assignment; included chains already owning the IP lock
  preserve intended pending in-memory assignments. No grant is revoked by a
  campaign. Need all-writer/rollback and concurrency regression coverage.
- Blocking (general/risk): existing WebUI disown then Free raced asynchronous
  cleanup. Added route_unassign_address using native ActionState.Poll(timeout=15);
  Free runs only on success. Pending/failure retains route, links chain and
  requires explicit resubmit. PHP regression passed 2 tests/10 assertions.
- Blocking (risk): AddRoute/Allocate guessed legacy NULL provenance. Shared
  IpAddress#ensure_charge_environment! now guards Update/AddRoute/Allocate and
  migration replacement. Need automatic Allocate regression.
- Important (risk): older failed-attempt rescue can overwrite a newer queued
  attempt. Rescue now also skips release_in_progress?; regression pending.
- Important (architecture): cap copies may drift. API references MAX_ADDRESSES;
  WebUI now owns IP_RELEASE_MAX_ADDRESSES with cross-language invariant test.
  Explicit fixed 100 cap remains; changing it requires coordinated UI/docs/tests.
- Important (architecture): mutable Network role/IP version changes quota
  semantics. Reject those changes while any allocations exist, serialize the
  empty-network check with registration via SQL network row lock. No conversion
  framework. New compatibility restriction requires docs/tests and focused review.

Quick initial remediation chains: 23 examples, 0 failures. Expanded run: 74
examples, 5 failures, all from new concurrency fixture setup/cleanup: the main
RSpec REPEATABLE READ snapshot could not see independently committed IPs; then
its fixture locks blocked cleanup and polluted subsequent examples. Moved the
three new race scenarios into separate-connection rollback transactions, matching
existing concurrency test structure. Rerun underway at
/tmp/ip-release-v3-concurrency-fixed.log (tool session 58644).
Expanded prior log: /tmp/ip-release-v3-remediation-regressions.log.
Root RuboCop correction underway (/tmp/ip-release-v3-rubocop.log, session48951).
Current uncommitted changes still need tests, formatter/localization, prose/docs,
focused fixup commits/autosquash, remaining mandatory scope/review as appropriate,
then browser integration and pushes/CI/KB exact pin. No long integration started.

Browser test runner preparation: /tmp/ip-release-browser-test.sh uses unique
/tmp/ip-release-integration-state and writes /tmp/ip-release-browser-integration.log
and .exit. Script not run. Ambient tmux uses a different socket/session than
dev-session; use a dedicated `tmux -L ip-release-test` server for the test, with
remain-on-exit, and leave other sessions untouched.

## V3 focused verification results

- Forty concurrency/provenance/retry examples passed. All four stale public
  route/host actor cases and the Network API suite passed (29 examples total).
- PHP and gettext health passed: 91 tests / 368 assertions.
- Effective notification overlay reconciliation and actual API Notify rendering
  passed all 8 combinations (CS/EN, initial/update, opt-out on/off). Durable
  harness overlay-check.rb; /tmp/ip-release-overlay-runtime.log. It queued only
  in disposable test databases and delivered no mail. This addresses the
  architecture review's Important provider/overlay validation finding without
  introducing another dependency pin or checker framework.
- Accepted Advisory: the seven-day default is a fixed coordinated API/UI
  contract, documented alongside the 100-address cap; no configuration layer.
- Expanded existing export, public IP and network-interface regressions underway.
  Initial invocation used nonexistent *_write_spec.rb names; rerun uses the
  repository's ip_address_assignment_spec.rb and host_ip_address_spec.rb.
- PHP formatter config is at repository root (.php-cs-fixer.dist.php). Corrected
  the invocation; no tooling/hook bypass.

## V4 remaining review checkpoint

Review packet review-packet-v4.md names the immutable final three-commit series.
Scope reviews the full implementation; architecture/risk review the new Network
role/IP-version restriction and registration serialization. Other V3 fixes were
verified directly under the skill's narrow-remediation rule. All reviewers use
gpt-5.6-sol / xhigh / fresh context, high overall risk.
The existing compound WebUI caller and its translated pending/failure copy now
ship in the first ownership prerequisite commit, before campaign functionality.
Each rewritten commit passed all hooks. Rewriting preserved the final tree
exactly. All origins fetched; the three upstream bases remain unchanged.

Expanded existing export/IP/interface regression suite passed: 110 examples,
0 failures (/tmp/ip-release-v3-existing-writers.log). The final topic checker
passed all 394 ordinary API specs exactly once; it mirrors CI's within-topic
sort/unique behavior before checking cross-topic duplicates.

Verified imported action versions in the changed API-topic workflow using each
upstream GitHub repository's releases/latest API: actions/checkout v7.0.1,
actions/upload-artifact v7.0.1, actions/download-artifact v8.0.1 and
ruby/setup-ruby v1.321.0. Existing v7/v7/v8/v1 major refs remain current; no
unrelated action pin change is needed.

V4 scope review finished against 4d8e9947d/420c98c with no Blocking, Important
or Advisory findings. It found the three-commit split coherent and the expanded
writer/accounting boundary proportional to demonstrated failures. Residuals are
browser/CI/KB verification and the documented writer drain/legacy reconciliation.
Focused architecture and risk reviews of network quota semantics remain active.
A final direct IpAddress API run covers its actual Assign/AssignWithHostAddress,
Free and Update endpoints; the previous broad suite included the separate
assignment-history resource as well as HostIpAddress.

## V4 findings and narrow corrections

Architecture and risk reviews both finished. Consolidated Important findings:
- Empty networks permitted an IP-version change inconsistent with their address.
  Added family/address validation, invalid partial-update and coherent conversion
  followed by registration tests, plus populated-family rejection coverage.
- Old API writers/rollback bypass the model invariant. Deployment now pauses
  role/family changes and new registrations through Network.Create,
  Network.AddAddresses and IpAddress.Create while writers are mixed/old work
  drains. The semantic update freeze remains after rollback.
- Existing populated networks can have historically changed quota type even
  with a non-null charge environment. Added explicit history/accounting audit
  and reconciliation prerequisites before release or ownership transfer.
- The SQL serialization guarantee lacked direct concurrency tests. Added actual
  separate-connection registration-first and update-first cases covering direct
  registration and managed additions, with quota-resource assertions.
No new framework, conversion behavior, or public API is introduced by these
validation/test/documentation corrections; focused checks will verify them
directly, without another confirmation-only review cycle.
Final direct IpAddress API suite passed 47 examples, 0 failures, including
Assign, AssignWithHostAddress, Free and Update.
New focused network checks running in /tmp/ip-release-v4-network-fixes.log.

V4 focused corrections passed 35 examples, 0 failures, including both actual
network SQL lock orderings, the coherent IPv6 conversion followed by addition,
and invalid/occupied conversion rejection. Root RuboCop passed after two layout
corrections. All review findings are now reconciled; committing narrow fixes
into their owning commits, then proceeding to browser integration and pushes.

Notification overlay branch pushed at 420c98c51ed3db015a366a5564e2128fc83a91b4.
Current-head CI passed: https://github.com/vpsfreecz/vpsfree-notification-templates/actions/runs/34407990032
Both V4 correction commits passed all hooks and are being folded into the
ownership prerequisite and campaign documentation commits.

## Integration and branch publication

Final vpsadmin series is a825b6179, 5b44f055a, 14942a9e6. The final tree exactly
matches pre-autosquash 238943226; both correction commits passed all hooks.
Fetched origin immediately before pushing; origin/master remains 19971f039.
Both vpsadmin and notification branches are now pushed.
Started webui#networking-dns through the dedicated tmux -L ip-release-test
server/session browser, using /tmp/ip-release-browser-test.sh and isolated
/tmp/ip-release-integration-state. Log /tmp/ip-release-browser-integration.log;
exit file /tmp/ip-release-browser-integration.exit. Do not touch other tmux servers.
Exact KB pins are being updated to 14942a9e6753b202b0f1d8a289938e3376c77fea.

KB exact-pin check found no navigation drift (44 controls / 35 paths / 35
concepts / 3 selectors; 92 bindings / 9 exceptions) but rejected an incidental
vpsAdminOS downgrade to 8e44a512. Investigation: both old 1acc1955 and new
14942a9e vpsAdmin commits embed 8e44a512, whereas the KB lock/contract already
used 6bdf458f. `nix flake update vpsadmin` reset this nested choice. Added an
explicit exact nested input override preserving the existing 6bdf458f runtime;
its nixpkgs and runtime action revisions remain unchanged. Re-running bin/check.
This is a dependency-only pin declaration, with no new runtime behavior; the
mandatory review skill's mechanical metadata exemption applies to the KB change.
A durable repository note records the failure and fix.

Full exact-pin KB bin/check passed: documentation 44/35/35/3; annotations
92 bindings/9 exceptions; page contract 4 pages/8 variants/12 tests/21 executable
samples; 60 regression tests/194 assertions; inventory 60 concepts/120 variants
and PNGs. kb-impact.md records the final no-drift assessment. No page/screenshot
regeneration or production wiki mutation is needed. No hook framework is
declared by the KB repository; its full check and git diff --check passed before
the first commit. Five current-head vpsadmin workflows passed so far (migration,
RuboCop, WebUI PHPUnit, i18n and libnodectld); API topics and integration remain.

## CI failure investigation and correction

API topic run 34408267506 failed engine core/full (894 examples, three failures
each) and full endpoint coverage. Downloaded completed job logs through the
REST jobs/{id}/logs endpoint while the workflow was still active:
102656365915, 102656366165 and 102656365920. Logs are in
/tmp/ip-release-ci-{core-engine,full-engine,full-coverage}.log.

Engine failures are stale operation specs after actor forwarding: two Update
calls must pass an explicit attributes hash before the actor keyword, and the
Destroy expectation must include the actor. Actual production callers already
pass this shape and their API checks passed. Updated the tests to assert explicit
actor forwarding. Full coverage lacked the 14 new release scopes in the existing
covered_endpoints.yml inventory. Added them and extended the API spec to exercise
admin index/show/notify/exempt/close and positive owner request details.
Focused verification running in /tmp/ip-release-ci-remediation-specs.log. These
are test/inventory corrections; production behavior is unchanged. No rerun was
accepted in place of investigation. Local browser integration continues at
14942a9e, whose runtime source remains identical.
KB branch pushed at 4a1b48f with the exact 14942a9e pin and preserved runtime.
It will need one final pin refresh after the test correction commit.

CI correction verification passed: 18 examples, 0 failures; root RuboCop clean.
The new admin API test confirms notice creation, exemption persistence and Close
without release. Folding test changes into their owning prerequisite/API commits.
KB Check CI passed at 4a1b48f (run34408729342); managed-page runtime is queued.

## First browser integration result

At 14942a9e, four existing networking/DNS Playwright tests passed; the new
campaign test failed before exemption selection. Error-context and shell logs
showed an Invalid request: transaction_chain#show had unresolved path arguments.
The HaveAPI PHP client's ResourceInstance::__get resolves resource attributes
even when null; its documented `<association>_id` properties read IDs without
resolution. The address renderer used `release_chain` as a boolean before a
release attempt existed. Switched nullable transaction and IP links to native
release_chain_id/ip_address_id. Extended the browser test to require all three
address rows immediately after creation, before notices. No client shim or new
API behavior was added. PHP/gettext recheck and browser rerun follow.
Evidence: services-shell.log lines2107-2384 and embedded error-context.md under
/tmp/ip-release-integration-state/os-test-webui-fd1a3b33. VM services reported no
failed services; no local Linux kernel build occurred. The driver shut down VMs
after capturing diagnostics. Preserve this state as evidence; use a new state
directory for the rerun.

Nullable-resource view fix passed all 91 PHP tests / 368 assertions and gettext
health. The original browser run ended with exit1 after 898.6 seconds; its VMs
were shut down. Preparing a fresh v2 state directory and retaining v1 evidence.
The browser fix is a narrow consumer correction using the existing HaveAPI
association-ID contract; no additional review lane is needed under the direct
remediation rule.

## Final browser and CI rerun

The final narrow corrections are folded into the functional series:
664e1e184 (ownership), 3302bcd9f (campaign API), 42ccae0c0 (WebUI).
Origin/master remains 19971f039 after fetch. Pushed with an exact force lease;
the stale queued CI run34408267475 at14942a9e was canceled. Current-head jobs
are preserved. API topic run34410737903 and integration run34410737744 now
track42ccae0c. Initial ambient push encountered the known Overcommit-version
signature mismatch; root nix develop push passed without re-signing or bypass.
Reuse notes/vpsadmin/2026-09-09-push-overcommit-version.md for this behavior.

Browser v2 started on42ccae0c using the private tmux server/session
`tmux -L ip-release-test`, `browser-v2`. Isolated state:
/tmp/ip-release-integration-state-v2. Log/exit:
/tmp/ip-release-browser-integration-v2.{log,exit}. Original failed evidence is
retained separately. The KB flake refresh changes only the vpsAdmin lock entry,
not the documented runtime or its dependencies.

Final KB head a1093d1020482c1a11aeb8acf5356ece31fa2993 pins42ccae0c.
Full local bin/check passed again: 44 controls/35 paths/35 concepts/3 selectors,
92 bindings/9 exceptions, 4 pages/8 variants/12 tests/21 samples, 60 regression
tests/194 assertions, and all120 PNGs. No existing documentation/capture drift.
Only the vpsAdmin lock entry changed during this refresh. Pushed with lease and
canceled old-head managed runtime run34408729344. Current-head KB runs:
Check34410947763, managed page runtime34410947637. No production wiki operation.

Final hosted checks are passing: migrations, RuboCop, PHPunit, gettext/i18n,
libnodectld and KB Check. Both API engine variants passed the corrected actor
specifications. The API matrix and local browser flow continue. The self-hosted
vpsadmin integration and KB managed runtime jobs remain queued. The preceding
master integration ran17:40-22:10 UTC; the superseded KB job started22:10 and
finished cancellation22:12. Runner inventory is unavailable to the configured
GitHub token (403); no permissions or runner configuration were changed.

Shared-runner queue is explained by read-only GitHub evidence: the canceled
old KB job used gh-runner3.int.vpsadminos.org. Another initiative's vpsAdminOS
CI run34398423999 started its test-suite job102653711116 at22:12:42 UTC, after
our old KB cancellation. That job is still running. Its scope/runners are left
untouched. The local browser run is independent and continues on our isolated
state directory; this is an external CI-capacity wait, not a feature failure.

## Browser v2 fixture failure and correction

At42ccae0c the browser passes campaign creation, all address rows, initial notice,
admin exemption, login return and escaped retention reason. Assignment then fails
because the new VPS fixture was database-only. Node log explicitly reports
RouteAdd cannot call add_route on a missing interface, and rollback cannot call
remove_route. Chain14/transaction13 failed at22:25:19 UTC; owner/assignment stayed
unchanged. The four existing form-oriented networking/DNS tests passed.
This was not an API rejection or reason-policy defect.

The networking script now reuses prepare_webui_storage_runtime for this one
stopped VPS, then recreates its empty database-only interface using the existing
VethRouted::Create chain. That initializes both nodectld config and osctld state.
The fixture JSON records the returned interface ID, and preparation waits for
successful confirmation. Browser assignment asserts its notification and uses
the existing transaction-settled helper before reading request protection.
No product/runtime behavior or new fixture framework is introduced. The narrow
fixture correction is verified directly; all completed review lanes remain valid.
Nix syntax passed; the root dev shell has no Node, so the JS check uses the
existing nix shell nixpkgs#nodejs workflow. Final hooks and browser v3 follow.

V2 ran915.55 seconds and stopped its VMs. Its default cleanup removes VM disks,
so traces printed only inside the guest are not persistent after shutdown;
embedded error contexts, node logs and SQL diagnostics supplied the root cause.

The fixture correction passed Nix/JS syntax and all commit hooks. Vpsadmin head
1e2d2d7c9 is pushed; origin/master remains19971f039. API and PHP product trees
are unchanged from42ccae0c (only the two browser fixture/spec files changed).
Browser v3 is running via private tmux browser-v3 and isolated
/tmp/ip-release-integration-state-v3; log/exit suffix integration-v3.
After pushing, canceled stale queued integration34410737744 and the old API
matrix34410737903 (24 topic jobs had passed; two platform jobs were still running).
Dispatched the existing API workflow on the new head for a complete current-head
result. No unrelated or current-head workflow was canceled. Current integration
is34412825378; WebUI PHPUnit34412825369 and i18n34412825351 started on1e2d2d7c9.
The existing KB pin remainsa1093d1/42ccae0c until the browser correction is verified.

## Final browser success and exact contract pin

Browser v3 passed all 5 Playwright tests on 1e2d2d7c9 in 6.1 minutes, including the
complete campaign flow: fixed selection, notices, exemption, login return,
escaped reason, actual assignment to a stopped VPS, forced policy, repeated
manual release and owner notice history. The test example passed in 382.35s;
script time 837.4s excludes machine-build/startup and final cleanup overhead.
The new interface setup chain was successfully confirmed before browser start.
No product code changed after the nullable resource-link correction. All feature
worktrees are clean. The runner exited 0 after 1105.73s and shut down its VMs.
Retained logs are separate from the failed runs. Removed the private test tmux server after all
three panes had exited; the managed development session remains active.

Final KB full check passed against 1e2d2d7c9, with no existing navigation/page/
screenshot drift (same 60 tests/194 assertions and 120 PNG inventory). Contract
head 9d79ff9d04d9df852898042aecf69b5e4c74567f is pushed. Only the API revision
changed in this final lock refresh; existing runtime and other dependencies are
preserved. Canceled superseded KB runtime34410947637 after the push. Current
KB runs: Check34414445971 and managed runtime34414445897. No wiki writes.

## Handoff — 2026-09-10

Implementation, mandatory reviews, targeted integration and hosted CI are
complete. The shared-runner jobs remain pending, so final broad integration
validation is not yet claimed. No merge, production deployment, or archival was
requested. All three feature worktrees remain attached and clean on branch
2026-09-09-ip-release-mechanism. The development session remains active.

Final heads:
- vpsadmin: 1e2d2d7c9bec10d7eb06feaa2c172d10d9fb7a15
- vpsfree-notification-templates: 420c98c51ed3db015a366a5564e2128fc83a91b4
- vpsfree-kb-contracts: 9d79ff9d04d9df852898042aecf69b5e4c74567f

Successful hosted checks:
- [API matrix: all 26 topics and topic coverage](https://github.com/vpsfreecz/vpsadmin/actions/runs/34412890207)
- [WebUI PHPUnit](https://github.com/vpsfreecz/vpsadmin/actions/runs/34412825369)
- [i18n health](https://github.com/vpsfreecz/vpsadmin/actions/runs/34412825351)
- [Migration specs](https://github.com/vpsfreecz/vpsadmin/actions/runs/34410737717)
- [RuboCop](https://github.com/vpsfreecz/vpsadmin/actions/runs/34410737831)
- [libnodectld specs](https://github.com/vpsfreecz/vpsadmin/actions/runs/34410737875)
- [Notification overlay](https://github.com/vpsfreecz/vpsfree-notification-templates/actions/runs/34407990032)
- [KB contract Check](https://github.com/vpsfreecz/vpsfree-kb-contracts/actions/runs/34414445971)

Migration, RuboCop and libnodectld results apply to component trees identical to
the final head; its last amendment changed only two browser fixture/spec files.
All final commit hooks passed. The local browser runner exited 0 with all five
Playwright tests passing; its VMs and private test tmux server are stopped.

Outstanding shared-runner checks:
- [vpsAdmin integration](https://github.com/vpsfreecz/vpsadmin/actions/runs/34412825378):
  running. The selector chooses CI-tagged WebUI, networking and DNS suites.
- [Managed KB page runtime](https://github.com/vpsfreecz/vpsfree-kb-contracts/actions/runs/34414445897):
  queued at handoff.

Before operational use, follow vpsadmin/doc/ip-release.md: apply the additive
migration, update all affected API writers and drain old transactions, preserve
the network role/family freeze during rollout/rollback, and audit/reconcile
legacy charge-environment and quota-resource history. No node protocol or
vpsAdminOS fleet upgrade is introduced by this feature.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-09-ip-release-mechanism/

## Follow-up implementation — 2026-09-10

User approved revised plan: empathetic bilingual text/HTML notices with locations
and conditional public IPv4 scarcity; admin reminders only for still-eligible
addresses of previously notified users; permanent exclusions for deleted owners
and changed allocations; PTR/ownership regression coverage. Reusing the exact
initiative/worktrees explicitly selected by the ongoing conversation. This shell
has no VPSFREE_DEV_SESSION_SLUG and dev-session current reports none; read-only
list confirms this exact initiative is managed with its three registered repos.
No session lifecycle mutation is needed or authorized. Existing initial tracking
commit remains in place; ongoing follow-up records are uncommitted.

Follow-up quick verification in progress. First pass: 53 examples, 5 failures
(all 9 API examples passed). Four failures were fixture setup: IPv6 helper
defaults to IPv4 text and an allocation-drift fixture hit model validation.
Corrected explicit IPv6 addresses and direct persisted-drift setup. Second pass:
47 model/concurrency examples, 2 failures, both PTR fixtures lacked a live node
for the existing deferred database confirmation. Corrected these to assert the
staged PTR destroy and retained default host; actual completion is covered by
the expanded API/NodeCtld harness and the new live DNS integration example.
The newly added owner-change race and user lifecycle locking checks passed.
Notification overlay flake check passed. Core-only schema regenerated; retained
only the changed table because this dumper reordered unrelated existing tables.

Final focused checks: 48 model/concurrency examples passed; migration checks
passed 2/2 independently. PHP regression passed 91 tests/368 assertions.
Overlay rendering passed 24 combinations (CS/EN, initial/reminder, both policies,
IPv4/IPv6/mixed), plus 2 default-host PTR staging examples. RuboCop passed all
11 touched Ruby implementation/spec files. Gettext health and CI selection
passed (16 tests/55 assertions); JS syntax passed. The DNS runtime example adds
the dns tag so IP-release changes select it. A Ruby empty single-quoted string
inside Nix's indented string needed double quotes; corrected before nixfmt and
selector validation. No kernel build occurred.

Overlay history consolidated to fd58bc0 (unpushed). API and WebUI corrections
are being folded into their existing unpublished functional commits.

Expanded API/NodeCtld confirmation checks passed 12/12: execute success, execute
failure, rollback; IPv4 and IPv6; default and user-created host addresses. PTR
records are removed only on completion, restored on rollback/failure, and the
user lifecycle lock is released with the chain. Exact once quota accounting and
manual retries pass. Final overlay render rerun with absolute test URLs passed
24/24. Bilingual HTML previews are saved under email-previews/.

API fixup 91f84d2f7 and WebUI fixup 5dbade8c4 passed all commit hooks. Consolidating
these into the original API/UI commits before mandatory review; pre-rewrite tree
is 22d953df92b6d358c7d9c368cb76045258db59cf. No branch has been merged/deployed.

Final follow-up heads before review: vpsadmin d21a376be6e708b289d4b32f2a0d1760ac3ae295
(API 74172b64d, original ownership prerequisite 664e1e184); overlay
fd58bc05cceb883d41f98c568069dc30a0d6a3eb. Rebase preserved the verified tree and
all hooks passed. Both feature worktrees are clean. Upstream bases are unchanged
after fetch. Starting mandatory high-risk review in all four lanes using fresh
gpt-5.6-sol/xhigh agents; packet v5 describes the bounded follow-up and earlier
review baseline. No long integration has started for this follow-up.

Earlier hosted results resolved during follow-up review: KB managed runtime
34414445897 passed on 9d79ff9. vpsAdmin integration 34412825378 failed with
116 passing tests and two failures. Downloaded its failed logs and artifact
vpsadmin-test-logs-34412825378 before considering another run. The network
shaper/rename example passed its assertions, then the runner timed out waiting
for `poweroff -f` during VM teardown. WebUI vps-user-core selected the directly
inserted owned fixture 203.0.113.137, which lacks charged_environment; the new
ownership safeguard correctly rejects it (the resource maps this exception to
the generic wrong-location message). The other networking fixtures already set
this field. A narrow fixture correction and a focused vps-user-core run are
needed in addition to the planned browser and live DNS checks. Artifact/log
copies are temporary under /tmp, not part of the durable portal.

Architecture v5 finished (gpt-5.6-sol/xhigh); scope lane launched when its slot
freed. Architecture and general independently found the same stale overlay
metadata ID: reminder directory still declared ip_release_updated. Reconciled
severity: Blocking, because this silently drops the registered admin recipient
role and can use the primary address instead. Extended overlay harness to assert
template_id, descriptor roles, and a configured role destination. Reproduced two
failing reminder examples at the exact stale-ID assertion, then corrected the
ID. Full 24-case render/routing matrix and overlay flake check are running.

Architecture advisory: active/suspended owner eligibility is repeated in preview,
locked creation, and request status. Current values agree and the checks cover
these paths. Accepted for this bounded feature without adding a new abstraction;
future lifecycle-policy changes must update the three checks together. Repeated
notification lookups are bounded by the existing 100-address cap; performance
measurement is a residual gap, not a delivery gate. No reviewer rerun is needed
for the direct metadata correction. A packet wording error about historical
login snapshots was corrected: the accepted contract preserves original user ID
and allocation snapshots, with nullable current login and a deleted-ID fallback.
General withdrew that finding after checking plan.md.

Risk v5 finished (gpt-5.6-sol/xhigh): same Blocking metadata finding, no others.
The fixed overlay passed all 24 render/routing combinations and flake checks.
Residuals recorded: live DNS test covers IPv4 default-host cleanup, with IPv6
and user-created variants covered through the actual NodeCtld confirmation
harness; notices use eligibility at preparation time and can become stale before
asynchronous delivery, while destructive release rechecks locked current state.
This matches the explicitly accepted absence of delivery gates. General also
records the proven missing-charge browser fixture as Important; corrected with
the known seed environment and folded into the WebUI commit.

General v5 completed: same metadata and fixture findings, no additional issues.
Direct fixes are committed with clean worktrees: vpsadmin
473b5c62aae74734a1b57d7780b75c906400a8d4; notification overlay
0c80160f92a5ae81b33cc1dc2441b00e10c9eeb9. The API implementation commit remains
74172b64d. Fixture Nix formatting and commit hooks passed. Scope review remains
pending; no long integration or follow-up push yet.

Scope v5 completed (gpt-5.6-sol/xhigh): same resolved Blocking metadata issue,
no additional findings. All four mandatory lanes are complete with no unresolved
Blocking/Important findings. Narrow remediations are verified without rerunning
reviewers; no new design or contract was introduced. Starting long integration
on clean corrected heads, then exact KB repin and hosted CI follow-up.

Fetched all three upstreams: bases unchanged. Pushed vpsadmin 473b5c62a and
overlay 0c80160 using explicit leases for the previous feature heads. No
superseded queued/running branch workflows remained to cancel. Hosted checks
started on the new exact heads (vpsAdmin CI 34466834808, API 34466834918;
overlay Check 34466827250). Local combined integration command:
`./test-runner.sh test --state-dir /tmp/ip-release-followup-integration-state
--fresh --jobs 2 --status-interval 60
'{webui#{networking-dns,vps-user-core},tasks/dns-reverse-record-check}'`.

Updated the KB exact API revision in its four manifests, then ran
`nix flake update vpsadmin`. Diff confirms only the API node changed in the
lockfile; the existing vpsAdminOS 6bdf458f runtime pin is preserved. Full
`nix develop -c bin/check` is running. This is mechanical revision metadata,
so no additional review lane is required if the documentation contract stays
green.

KB full check passed: 44 controls/35 paths/35 capture concepts/3 selectors;
92 annotation bindings/9 exceptions; 4 managed pages/8 variants/12 tests/
21 executable samples; 60 regression tests/194 assertions; 60 concepts/120 PNGs.
No documentation or screenshot drift. Updated kb-impact.md. KB commit
614442a9f06422646d12086353d95572f099e354 is pushed; hosted Check 34467150390
and Managed page runtime 34467150396 are on this exact head. No stale in-flight
KB workflow required cancellation. The local integration selector confirmed all
three intended scripts. Resource limits correctly serialize DNS (10 GiB shared
memory) and WebUI (24 GiB), with 25.9 GiB available after the runner reserve.
Build logs show cached kernels plus normal initrd/module-pruning derivations;
no Linux kernel compilation occurred.

Hosted final-head migration, RuboCop, WebUI PHPUnit, i18n health and libnodectld
specs have passed. API topic matrix, integration and KB runtime are in progress.

Local DNS integration: original drift-check example passed; the added release
example failed before release at its first dig query, with localhost:53 connection
refused. The fixture BIND configuration deliberately listens only on
dnsNode.ipAddr (192.168.10.31), not loopback. The new test now uses the existing
dns_query_short helper and the configured fixture address for both assertions.
This is a direct test-endpoint correction, not a release or DNS behavior change;
focused Nix formatting/commit checks suffice before rerunning the scenario, with
no additional review lane. Original test logs are retained under the private
integration state. The browser scripts continue against the unchanged product
tree; DNS will be rerun after they release the required shared memory.

The DNS-only test correction is committed as
871fa3dae787678ceea7f36ba5cbec139c93e5ee, currently unpushed. All hooks passed
(commit text-width advisory only; lines satisfy the repository's 80-column
requirement). The product component trees are identical to pushed 473b5c62a.
Keeping this direct runtime-test correction as a separate functional test commit
preserves its failure rationale. Waiting for the existing API matrix to finish
before the follow-up push, then cancel any remaining superseded workflows as
required and refresh the exact KB pin once more. Current API matrix: 24 topics
passed including both core/full network and mail; only core/full platform remain
in the RSpec step. Their preceding successful run took 30–35 minutes, so the
current duration is not yet abnormal. KB Check passed on 614442a; its runtime
suite is still running (previous successful runtime was about 41 minutes).

Hosted API run 34466834918 completed successfully: all 26 core/full topics and
the topic-coverage check passed. KB managed runtime 34467150396 also passed on
614442a (API 473b5c62a). These product trees are unchanged by the DNS-only test
correction 871fa3dae. Pushing that correction now and canceling only remaining
queued/running workflows for superseded heads of this exact feature branch.

Pushed vpsadmin 871fa3dae with a fast-forward update. Canceled superseded
integration run 34466834808 after verifying its head was 473b5c62a; no other
stale jobs remained. New integration run 34469920231 uses 871fa3dae. Final KB
repin and full bin/check passed with the same contract/regression counts;
vpsAdminOS runtime remains 6bdf458f. KB head is
87bc0fbcb267292a30867d7a5f90eee92552fc10, being pushed with an explicit lease
for previous head 614442a. Its previous hosted Check/runtime were both complete
and successful, so no stale KB run needs cancellation. No new product behavior
has changed since the reviewed implementation and matching hosted API results.

Hosted follow-up integration 34469920231 passed on exact head 871fa3dae:
all four task scripts passed. Downloaded the completed job log and verified
the new live-DNS release example explicitly succeeded in 36.12 seconds;
the full DNS scenario passed in 304.53 seconds. This confirms PTR answers
disappear and owner/record state is finalized correctly using the configured
server endpoint. No identical local DNS rerun is necessary. The combined local
run retains the already diagnosed pre-fix DNS failure, while its two browser
scripts continue against the identical API/WebUI component trees.

Final KB push 87bc0fb succeeded. Its hosted Check 34470210306 passed; managed
runtime 34470210256 is a repeat after a mechanical pin to the test-only API
commit. The same product component trees already passed managed runtime on
614442a. No production deployment, wiki write, branch merge or lifecycle action
has been performed.

Local webui#vps-user-core passed all four Playwright tests after the charge-
environment fixture correction. Browser execution took 1944.17 seconds; the
full script including setup took 2303.26 seconds. This completes the regression
for the earlier hosted failure and exercises the remaining VPS form/reinstall
steps that had previously been skipped. The runner has moved on to
webui#networking-dns, including the real HTML email button/login and reminders.

The networking browser script passed its four existing tests, then the IP
release scenario failed while reading the initial queued email, before clicking
the button. The new test incorrectly assumed runVpsadminctl always returned a
response wrapper; the CLI returned the unwrapped payload. Existing transaction
browser helpers already normalize `response.response || response`. Added that
same normalization to a small local showApiResource helper for the four request/
mail reads. JS syntax and diff checks pass; this narrow test-harness correction
does not change production code or require another review lane. Rerun only
webui#networking-dns; VPS core and live DNS are already verified. The original
combined runner has exited with its two diagnosed failures and retained logs.

Browser-harness correction committed as
feccc00735c1d6323732ca39ef2aced8691d0432 (currently unpushed); hooks passed.
Started `./test-runner.sh test --state-dir
/tmp/ip-release-followup-browser-v2-state --fresh --status-interval 60
'webui#networking-dns'`, logging to /tmp/ip-release-followup-browser-v2.log.
No need to rerun the already passing 32-minute VPS form scenario.

Documentation pin decision for this last test-only correction: retain the KB
input at exact product revision 871fa3dae. feccc0073 changes only the vpsAdmin
networking Playwright spec; API, WebUI, libnodectld, and shared test-runner/
machine/configuration trees are byte-identical (verified with git diff). KB owns
its own browser/page scenarios and does not consume this spec. No visible WebUI
change or documentation contract change occurs, so another mechanical pin and
repeat KB runtime cycle would add no validation. The existing 87bc0fb contract
head already pins and verifies the final product tree.

Final KB managed runtime 34470210256 completed successfully on exact contract
head 87bc0fbcb. All KB validation is complete. A fresh upstream fetch found
vpsAdmin master advanced from 19971f039 to c975544fe with an automated package
dependency update only. This implementation remains on its reviewed/tested base;
no integration is being performed. Refresh/rebase against the then-current
default branch before a later merge, as required by workspace rules. Notification
and KB upstream bases are unchanged.

Final focused networking browser rerun passed all five Playwright tests in
6.9 minutes (426.93-second example, 820.98-second script including setup).
This explicitly verifies the actual queued HTML email button through login,
no mutation from GET, reason submission, VPS assignment, exemption, a forced
policy reminder containing only the remaining eligible IP, manual release
before the advisory date, repeat release and user notice history. Final
vpsAdmin head feccc00735c1d6323732ca39ef2aced8691d0432 is pushed by fast-forward;
all three project worktrees are clean. Its new hosted CI 34474145934 is running.
No superseded queued/in-progress runs remained. The final test-only push does
not change the already verified product component trees or the KB pin decision.
Portal URL confirmed and email preview/review artifacts are registered.

Focused browser runner exited 0 after normal VM teardown: one script/test
successful, total 1055.68 seconds. No runner or session lifecycle command was
used to terminate it. Final tracking diff whitespace check passed.

## Follow-up: remove policy-history sentence and investigate CI

User requested removal of the previous-reasons sentence from emails and
investigation of failed vpsAdmin CI. Removed it from all built-in EN and overlay
EN/CS requested/reminder text/HTML variants; updated existing forced-policy
render assertions to the retained admin-exemption instructions. Current branch
CI 34474145934 is now successful. Latest failed CI is the earlier feature run
34412825378 (1e2d2d7c9); inspecting both failing scenarios and retained artifacts
before deciding on further runtime validation.

Rechecked the old CI artifacts: the shaper example and script passed before
OsVm::Machine#stop blocked in the poweroff command channel for about 15 minutes.
No guest kernel panic/backtrace was captured, so the underlying guest/channel
hang remains unknown; no speculative product/runner fix is warranted. Current
CI 34474145934 passed all 12 selected network/DNS tests, including this same
shaper scenario and its teardown in 320.98 seconds. The missing-charge fixture
was already corrected and the full four-test VPS browser regression passed.
Detailed evidence is in ci-investigation.md and registered on the portal.

Email copy follow-up committed: vpsadmin
37e08d8be10c2f38138f5511403c94523126d033; overlay
ff5cc7c474cab76dbdebabcd706b5d43c8d5319a. Quick checks passed: 38 campaign
examples, 24 localized render/routing combinations, overlay flake check, touched
RuboCop and all commit hooks. The delta is low-risk prose deletion; the existing
assertions changed only their expected literals. General-only review v6 is
required at gpt-5.6-sol/xhigh; no runtime/test logic, abstraction or contract
change triggers another lane. Existing v1-v5 reviews remain authoritative for
the unchanged implementation. No long integration rerun started for this copy
edit; the failed scenarios were investigated from existing completed artifacts.

General review v6 completed at gpt-5.6-sol/xhigh on exact heads 37e08d8be and
ff5cc7c4: no Blocking, Important or Advisory findings. Reviewer verified all
12 variants, retained instructions, quick-check evidence and CI artifacts.
Residuals accepted: absence of deleted prose is checked directly rather than
adding brittle permanent copy assertions; underlying old guest shutdown hang
remains unexplained; new hosted checks begin after pushing the copy-only heads.
No additional review lanes or long local integration tests are warranted for
this literal deletion. Pushing the two commits by fast-forward now.

Pushed vpsadmin 37e08d8be and overlay ff5cc7c4 with fast-forward updates; both
worktrees are clean. Current-head workflows: vpsAdmin CI 34484865348, API topic
matrix 34484865323, RuboCop 34484865318, i18n 34484865320; overlay Check
34484854385. No superseded queued/running workflow remained to cancel. Upstream
vpsAdmin master remains the unrelated dependency-only c975544fe; retain the
reviewed base for this bounded follow-up and refresh before later integration.
New CI runs are additional validation of the copy-only commit; all targeted
checks and the failed-scenario investigation are complete. No new local long
integration run was necessary. Session remains active and open.

Current-head overlay Check 34484854385 completed successfully on ff5cc7c4.
Current-head vpsAdmin RuboCop 34484865318 also passed; API topics remain
queued and integration/i18n are in progress at handoff.

## Follow-up: direct support instructions

User requested replacing the abstract administrator-exemption sentence with
direct instructions to reply to the email, which reaches support and allows
support to grant an exemption. Updated all 12 built-in/overlay EN/CS text/HTML
variants and existing render expectations. Applied the previously read workspace
writing/humanizer guidance directly; no new behavior or public contract. Will
fold this wording into the latest unmerged prose-only commit per repository.
Before this edit, API topic CI 34484865323, RuboCop and i18n passed on 37e08d8be;
integration 34484865348 is still running. No new failure is reported.

The user immediately corrected the support wording: forced-release mode should
omit the exemption paragraph entirely. Removed the else branch from all 12
email variants; the common assignment instructions remain and reason-form
instructions appear only with opt-outs enabled. No support wording was committed
or pushed. Updated the existing forced-policy render assertion to check that
the user reason form is not offered. Verification now targets this final copy.

Final forced-mode paragraph removal passed 25 examples (one existing campaign
notification test plus the 24 localized rendering/routing combinations), overlay
flake checks, diff whitespace checks and every commit hook. Source searches
confirm the absence of exemption/policy-history/proposed support instructions
in all 12 variants. Latest prose-only commits amended to vpsAdmin
7483c4d2535b994a10ea3a82856052bd78c4913c and overlay
00519f79fa9a5073eb83f41bae3857bc66229e17. General-only v7 review is low risk,
gpt-5.6-sol/xhigh, scoped to the delta from reviewed 37e08d8be/ff5cc7c4.
No new runtime behavior or compatibility contract changes.

V7 general review completed at gpt-5.6-sol/xhigh on exact heads 7483c4d25 and
00519f79: no Blocking, Important or Advisory findings. The reviewer verified
all 12 else-branch deletions, unchanged assignment guidance, allow_keep gating,
ERB structure, focused amended commits and passing verification. Accepted
residual: direct searches cover the removed prose on these heads; no brittle
permanent assertion naming deleted wording is added for this copy-only edit.

Pushed final heads 7483c4d25 and 00519f79 using explicit leases for the prior
37e08d8be/ff5cc7c4 feature heads after a fresh upstream fetch. Both worktrees are
clean. Requested cancellation of only the still-running old-head integration
34484865348; all other superseded checks had completed successfully. Current
workflows: vpsAdmin CI 34491288911, API topics 34491288836, RuboCop 34491288966,
i18n 34491288907; overlay Check 34491267241. No new production or session
lifecycle action was performed.

Current-head overlay Check 34491267241 passed on 00519f79. The old-head CI
cancellation request has been accepted but is still in progress as of handoff;
no current-head workflow was canceled.

## 2026-09-15: closing wording, API specs and locking explanation

User requested a neutral email closing, investigation of failed API specs, and
an explanation/justification of locking prerequisite commit 664e1e184. Reusing
the explicitly selected existing initiative; dev-session current finds no
process session and DEV_SESSION_SLUG is unset, so no lifecycle/start operation
is performed. Project worktrees began clean at 7483c4d25/00519f79.

Current complete integration CI 34491288911 passed. API workflow 34491288836
failed only core-engine job 102918382409: 912 examples, one failure, 50 pending,
seed 24922. The failure is the initial-notice negative substring assertion for
192.0.2.20. The fixture helper derives addresses from max(id), while rolled-back
inserts advance auto-increment IDs, so the next IP can be 192.0.2.200. Reproducing
with explicit overlapping address strings before changing the assertions.
No blind rerun or change to locking behavior is planned.

Explicit overlapping addresses reproduced two failures with the original
initial-notice and reminder assertions. The assertions now include the IP
prefix, preserving deterministic regression fixtures. Full core-engine rerun
with the failed CI seed passed: VPSADMIN_PLUGINS=none nix develop .#api -c
bundle exec rspec spec/models --seed 24922; 912 examples, zero failures, 50
existing pending examples, 4m51.6s. Overlay nix flake check passed. The neutral
closing is “Děkujeme za tvůj čas.” / “Thank you for your time.” in all 12
built-in/overlay EN/CS text/HTML notice/reminder variants. Render matrix pending.

Added locking-notes.md with verified call-site distinctions, lifetimes, race
examples, contention costs and bundled accounting/validation behavior. No
locking implementation change is included in this follow-up. A new durable
note records the substring-assertion trap and deterministic reproduction.

Fetched upstream before preparing pushes. vpsAdmin master is now f7a17d6e5
(authentication/recovery/daily-report/DDNS work and dependency updates); overlay
master is 6ebfb6f (recovery and daily-report templates). Retain the established
reviewed base for this bounded copy/spec correction; integration will require
a refreshed base and assessment of the newer authentication/lifecycle paths.
No merge or deployment is authorized or performed here.

The 24-case localized render matrix passed; safe HTML previews regenerated.
Touched spec RuboCop, whitespace checks and every commit hook passed. Committed
test fix 36a6869fe93b2699eafa2f75a8ae1ecf7be38d15 and built-in copy
395bf80b76b2e715fbad25f7c637c5763dc35ad5 separately; overlay copy is
51c8f2c3f94b094ca93e1bddb719e0b23a9e04ab. Both worktrees are clean, not yet
pushed. V8 review is low risk, general + architecture for the handwritten
test changes. The current mandatory-change-review skill specifies gpt-6-astra
with xhigh effort, which supersedes the model recorded for earlier reviews.

V8 architecture review completed at gpt-6-astra/xhigh with no findings. It
verified the deterministic CIDR regression fixtures, all 12 literal template
edits, existing provider/overlay boundary, and the accuracy of locking-notes.md
against the cited code. Accepted residuals: new prose is checked in source and
previews without brittle permanent wording assertions; no compatibility claim
for newer upstream code or reopened full-feature audit. General review pending.

V8 general review completed at gpt-6-astra/xhigh with no findings. Reviewer
independently ran the two changed examples with seed 24922 (two passing),
verified separate commit purposes, all literal closing edits, full-suite and
render logs, and the factual locking explanation. Both required lanes passed;
no remediation or rerun is needed. Fetched both upstreams again before push.

Pushed exact reviewed heads by fast-forward over SSH: vpsAdmin 395bf80b7,
overlay 51c8f2c3. Both local heads match the remote feature refs and both
worktrees are clean. No superseded queued/in-progress workflow remains on this
branch; no cancellation was needed. New hosted checks: API Specs 34943116908,
RuboCop 34943116885, integration CI 34943116818, i18n 34943116902; overlay
Check 34943088429. API is queued; the other checks have started. No new local
long integration tests were needed for this copy/spec-only correction.

Current-head overlay Check 34943088429 and vpsAdmin RuboCop 34943116885 passed.
API Specs has started both core and full engine jobs; nine jobs have completed
without a failure so far. Waiting for the previously failed engine job before
reporting the hosted regression result. Integration and i18n remain running.

Final September 15 regression status: the previously failed API core-engine job
passed on pushed head 395bf80b7 in workflow 34943116908. i18n 34943116902,
RuboCop 34943116885 and overlay Check 34943088429 also passed. The API matrix
has ten completed jobs with no failures; full-engine and remaining topics are
still running, as is integration 34943116818. This is not a claim that the
whole new workflow has completed. The exact original-seed core suite also
passed locally (912/0/50 pending), and both v8 review lanes passed.

Handoff includes the neutral email previews, CI root-cause evidence and
locking-notes.md. The broader locking prerequisite is unchanged. Its shared
IP/host reservation has a concrete race/rollback rationale; quota/provenance
and network validation remain explicitly identified as additional behavior to
present separately before integration. Follow-up integration must reconcile
new upstream changes and finish outstanding CI; no merge, deployment, real
email, archival, cleanup scheduling or session lifecycle action was performed.
Stable portal confirmed with dev-session url:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-09-ip-release-mechanism/


Split review launch: general and architecture lanes are active at the exact
packet heads, gpt-6-astra/xhigh/fresh context. A third concurrent spawn was
refused by the tool thread limit despite the nominal four-slot catalog. Risk
and scope remain required and will run as slots become available; none is
skipped. Read-only devcluster status still reports stopped and there is no
config at the legacy workspace-local path. No startup or lifecycle change yet.

## WebUI redesign implementation checkpoint (2026-09-15)

Implemented campaign-scoped address/notices and atomic bulk exemptions, shared
single/batch validation, raw historical actor IDs with admin-only visibility,
rendered sidebars, standard headers, unified admin address table and separate
action forms. Retain Notice history. Added two-owner browser fixtures and
navigation-driven coverage. Existing mail templates are unchanged.

Quick verification: API/model specs 52/0 seed 55547; concurrency 13/0 seed 5672;
WebUI PHPUnit 93 tests/388 assertions; PHP and JS syntax passed. Touched Ruby
formatting passed. Locale regeneration/check passed after translating the new
CS entries. No long integration has started before required review.

Tool corrections: component Nix shells already change directory; do not `cd api`
again. PHP CS Fixer lives in the root shell, node is available through
`nix shell nixpkgs#nodejs`. Existing workspace notes cover these shell details.
`git commit --fixup TARGET -F FILE` is rejected by Git; use a literal `fixup!`
subject in the required message file and autosquash later. This failed before
any commit. Upstream added two documentation commits, requiring the feature's
index links to move from deleted docs/index.mdwn to docs/README.md on rebase.

Review started on vpsAdmin 43530927d and KB 2dfe4c7. General and architecture use
fresh collaboration agents, gpt-6-astra/xhigh. Launching the risk reviewer through
collaboration hit the retained agent-thread limit (an older completed reviewer
still occupies a thread). To preserve fresh context, risk uses a standalone
`codex exec --ephemeral --sandbox read-only`, same gpt-6-astra/xhigh model/effort,
packet and no-subagents instruction. Its log/result are temporary; findings will
be consolidated here. Scope lane will run when capacity is available. No review
lane is omitted and no long local integration has started.

Redesign review remediation: general and architecture both found three omitted
covered endpoint scopes. The hosted full coverage job 104407949077 in run
34977231855 confirms exactly that failure in its downloaded log. Added the three
already-tested scopes; plugin-enabled inventory passes 1/0 seed 8975. General's
advisory Select all restoration issue is also fixed and browser assertions added.
Narrow remediations are folded into API 2f2fefeb5 and WebUI 5e15045a6. Risk review
has no findings; scope review is finishing against the original committed heads.
GitHub log retrieval required --allow-escape-sequences; local saved output was
stripped of ANSI control sequences before inspection.

All four redesign review lanes completed. Scope and risk found no issues;
general/architecture findings are fixed as recorded in review-redesign-results.md.
Browser integration webui#networking-dns started on 5e15045a6 after reconciliation.
The existing single/bridge cluster is receiving a services update; a full reset
is unnecessary because the redesign adds no migration. Prepared restoration
checks seed-managed ownership/quota, reapplies the overlay and extends the unsent
review campaign to both members. The main campaign will remain unsent.

Live browser checks verified navigation, creation preview, restored selection,
whole-campaign bulk setting and actor attribution, but removal failed locally in
the PHP client: required nullable input was rejected before HTTP. Confirmed in
haveapi/client 0.29.6 and upstream 0.29.8. Implementing an explicit remove flag
on the new bulk API, preserving nonblank reasons for setting and model atomicity.
The main campaign temporarily has the test exemptions on all five rows; clear
them after the corrected live check and verify the unsent fixture before handoff.

The first redesigned integration attempt completed with four browser tests
passing and the campaign test stopping at the preview step (1051.12 s total,
including teardown). The submitForm helper snapshots controls with Locator.all()
without waiting after navigation; the failure capture already shows the Preview
addresses button. The live browser reached this form successfully. Replaced the
three new creation submits with scoped getByRole(...).click() calls, which wait
for the control. The next integration attempt will also cover explicit removal.
Failure evidence: /tmp/ip-release-redesign-browser.log and the runner's recorded
services-shell.log. No screenshots were added to review deliverables.

The explicit-removal correction passed all 12 campaign API request examples
(seed 58936, 7m08s), plus the focused missing/null/blank-reason case with the
final null assertion (1/0, seed 9059, 58s). Ruby lint and PHP/JS syntax passed.
Hosted CI 34978785877 failed only webui#networking-dns; downloaded artifact
10402055358 confirms the same No submit button matched Preview addresses error.
The other eleven selected integration scripts passed. A separate live DOM
check confirms the named filter form contains the button after waiting; the
scoped waiting locator finds exactly one matching control.

Removal correction a75bb80d5 is pushed with an explicit lease; base remains
564cc80ea. General/architecture/risk reruns found no issues, including isolated
PHP client and stale-discovery checks. See review-bulk-remove-results.md.
Superseded 5e15045 API Specs run 34978785866 was cancelled after the push;
24 jobs had passed and the two long platform jobs were still running.
Browser rerun and services update started after reconciliation; KB repin/check
is in progress. Main fixture cleanup is still pending the new live API.

Final services deployment: /nix/store/gmqgr5szpvbspn7wy5yv7s9vm41pzki5-nixos-system-vpsadmin-services-26.05pre-git.
The development API signing key was unlocked through the configured admin CLI.
After seed reconciliation, the corrected live UI set and removed all five trial
exemptions; read-only checks verified fixture eligibility, quota and PTR.
Both node containers report running. No reset was needed; account secrets stayed
private and were not rotated. Use pinned Nix shells for browser tools: a store
path reported by a finished review process was unavailable later (exit 127);
reentering the repository-pinned Node shell worked.

Final local integration: webui#networking-dns passed at 17:01 CEST on a75bb80d5.
All five Playwright tests passed. Example 549.19 s; full script 1112.28 s;
total including build and teardown 1403.61 s. Log:
/tmp/ip-release-redesign-browser-final.log. This covers the complete revised
flow through real email login, member reasons, VPS assignment, policy change,
reminder, early release, repeated release, bulk exemptions and closure.
No local kernel build was needed. No screenshots are included in deliverables.

Refinement quick verification: PHP 95 tests/396 assertions, CI selection 16/55,
migration 2/0 seed 5735, focused API 4/0 seed 64991 (explicit limit500 and 501
addresses) pass. The earlier 71-example run had one test expectation failure on
HaveAPI's standard _meta; the corrected assertion checks both the member field
whitelist and allowed metadata keys. Final focus passes. Ruby lint and locale
health pass; the correct API task is vpsadmin:i18n:health (not :check).

Commit isolation note: Overcommit hides unstaged tracked UI changes but leaves
new untracked PHP files visible to gettext scanning. The first API-only commit
attempt therefore correctly detected a changed POT source reference from the
new selection helper. Temporarily moved that untracked helper outside webui,
committed the API against the baseline UI with all hooks, restored the helper,
then staged it with the matching UI catalog/commit. No hook was bypassed.

Refinement vpsAdmin head 9840cdf08b9dbdb825bac0da04aa74281d3c4e2a is published
with an explicit lease, API commit 3fb0ab7f5, exactly eight commits on 564cc80ea.
Final tree is identical to the verified pre-fold tree; first six are unchanged.
The initial ambient-shell push hit Overcommit's configuration-signature guard;
verified .overcommit.yml and custom hooks have no diff, signed in the repository
Nix shell and pushed successfully. An early KB fetch therefore saw HTTP404;
rerunning after ls-remote proved the new head is published. Superseded a75
integration run 34982706278 was cancelled during this push transition.

All four refinement reviews completed on 9840cdf08 / KB e098f688. General and
risk found Blocking (scope Important) PHP GET transport incompatibility: pinned
client 0.29.6 stringifies custom array filters as "Array". Reproduced with the
actual client and an in-memory sender. Remediation keeps the contract local:
comma-separated String query parameters, converted from UI multi-selections;
model normalization also supports internal arrays. Added real-client transport
coverage for defaults and multi-value filters. Architecture's Advisory notice
whitelist is also fixed: own Notice history explicitly exposes id/event/subject/
created_at. API notice response key assertions added. General/architecture/risk
will review the committed transport correction because its new query contract
was not covered by the completed review. Scope is unchanged; no generic client
patch or new framework. Multi-page selection bookkeeping passes at 1101 rows;
actual multi-page browser settings preservation remains a recorded test gap.

General/architecture used fresh collaboration reviewers. Retained thread limit
blocked the risk spawn; risk and scope ran fresh ephemeral, read-only Codex CLI
reviewers, gpt-6-astra/xhigh, with the same packet and no nested review. No lane
was omitted and no local long integration or deployment began before review.

All three committed filter-transport reruns pass on be21bc8b9 / KB bce530f8,
with no findings. Reviewers independently exercised the pinned client and
normalizer. Long integration and deployment can proceed for the feature.

Final-head API Specs engine job 104488002326 in run35000486221 failed with
one failure among1165 examples (three expected pending), seed55211. Downloaded
and inspected the original log. Failing case: IncidentReport task, locked
incident continuation. Fixture setup raises duplicate IP before task execution.
Shared create_ip_address! derives 192.0.2.(maximum(id)%200+20); rolled-back
examples retain auto-increment sequence advancement, so two subsequent fixture
rows can get the same default address. This is unrelated to production campaign
logic but must be repaired for reliable CI. Add a separate test-only commit
rather than mixing the fixture fix into the eight feature commits; first six
and all production locking remain unchanged. Reproduce the collision explicitly,
skip occupied defaults while preserving explicit addr behavior, run incident
and representative helper consumers, then review the bounded fix.

Fixture repair46acba869 and KB exact pin d7660800 are published. General and
architecture review both found no issues (review-fixture-results.md). Full KB
check passes. Full engine specs with original failing seed55211 and isolated
webui#networking-dns started after reconciliation. Current hosted API Specs is
35002860902; CI35002860988. Superseded be21 integration35000486438 cancelled.

Live fresh-session browser checks passed for the admin and both members: default
campaign list, existing/fresh campaign details at500, sidebar availability,
blank narrow checkbox column, placeholder, all multi-select fields, private
user-filtered preview, all/none selection and member response isolation.
Log: /tmp/ip-release-refinement-live.log. No screenshots.

Development seed ordering: vpsadmin-api.service depends on a nonpersistent
oneshot vpsadmin-devcluster-seed.service, so starting API after schema conversion
reapplies seed overrides, clearing the seed-managed assigned IP owners. The
post-start accounting check caught exactly one missing assigned owner for each
member; private accounting was correct. Restore fixture settings/owners only
after the final API start, then verify quota/PTR/state without restarting API.
This affects disposable seed data, not production accounting.

Final post-start fixture check passed: all three resource totals match owned
allocations for both members, retained/released PTR states are correct, campaign3
is unsent with four eligible rows and no trial reasons/exemptions, both VPSes
report running. Log /tmp/ip-release-refinement-restore-final.log. Shared seed
ordering lesson is notes/vpsadmin/2026-09-15-devcluster-api-restart-seed.md.
KB previous runtime35000880043 cancelled after publishing d7660800; current
Check35003281480 and Managed runtime35003281177 are running.

Final-head hosted engine jobs104495517779 (full) and104495517995 (core) both
passed, confirming the fixture repair in both configurations. RuboCop, i18n
and selected CI passed; the test-only push selects no runtime integration, so
local final webui#networking-dns is the runtime validation. Other API topics
and KB managed runtime remain in progress.

Full local API engine rerun passed on46acba869 with the original CI seed55211:
1166 examples, zero failures, three expected pending; 8m25s plus14.46s loading.
Log /tmp/ip-release-fixture-engine.log. Expected pending cases remain the
existing dataset clone/rotation cases; no new failure.

Hosted KB Check35003281480 passed on d7660800. API Specs has16 completed
successful topic jobs and10 still running; no failures. Final browser setup
is creating its isolated fixtures. Live review remains available.

Final isolated browser run on46acba869: all five Playwright tests passed in
8.7 minutes at20:09 CEST. Includes the full refined campaign flow through
creation, bulk exemptions, notices, member retention, assignment, reminders,
policy change, manual release and closure. Runner teardown remains in progress.
Log /tmp/ip-release-refinement-browser-final.log and
/tmp/os-test-runner/os-test-webui-fd1a3b33/services-shell.log. No screenshots
were generated by the passing run.

Final isolated test-runner completed successfully at20:13 CEST, including
teardown: one script, all five browser tests, 1518.56s total. Example538.13s,
script1074.28s. No local kernel build and no failure screenshots. All project
worktrees are clean. The live review cluster remains running and unchanged.

API Specs has24 successful topic jobs; only full/core platform jobs remain.
Both network topics and both engine topics passed. KB managed runtime remains
running; its contract Check passed. No known failure is outstanding.

API Specs35002860902 is completed successfully: all26 topic jobs plus topic
coverage passed on46acba869. The original reported CI failure is resolved.
KB runtime35003281177 remains in progress on d7660800; previous successful
comparable runs took43 and67 minutes. No new failure has appeared.

Final hosted KB runtime35003281177 completed successfully on d7660800. All
current-head workflows are green; all known failures have been investigated
and resolved. The session and review cluster remain open for user testing.
