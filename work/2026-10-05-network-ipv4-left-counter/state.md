---
lifecycle: active
---

# Network availability and IPv4-left counter

## Status

Phase: implemented and independently reviewed; verification handoff (2026-10-06).
Backend, both UIs and configuration/KB contract pins are committed and published.
All four independent review findings were corrected and verified. Final heads:
V be136b6c00f03b85b7a12cc57550b4a1394a94a7,
W e4c49bcdc91b33b7f644a2f125231cb413cf4bf4,
C dd10d88073da3aed6c4512e938abe4374422aab1,
K 291566b2c0bd43389802f607852fd9a4f8241752. All five worktrees, including the
separate dependency maintenance branch, are clean.

Passed evidence includes the 26-job API CI matrix, core/full SQL admission and
Create tests, React desktop/mobile synthetic browser tests and production build,
route/host-address and export-lifecycle VM scenarios, and all 12 affected-host
configuration builds. [Final verification](fixture-final-verification.md) records
exact revisions, receipts and limits. Migration, restore and legacy browser tests
still need matching exact-selector CI evidence or sufficient real VM capacity;
existing integration CI 37485699588 remains in progress at the latest snapshot.
Two member IP-list KB images still need a supported owned capture environment.

The network WebUI CI audit fails on proxy-addr 2.0.7 already present in main.
The separate maintenance branch a7361bb2912485b61a5a0b1472d51158ac08ec96 is
ready, awaiting merge approval, in [WebUI PR #20](https://github.com/vpsfreecz/vpsadmin-webui/pull/20).
Its audits, tests, clean package/provenance checks and CI passed; its smoke
workflow remains in progress. Network feature/configuration heads do not bundle
that patch. Proper integration of this prerequisite remains necessary before
network WebUI CI can clear its dependency audit.

Draft implementation PRs: [backend/legacy #45](https://github.com/vpsfreecz/vpsadmin/pull/45),
[React UI #19](https://github.com/vpsfreecz/vpsadmin-webui/pull/19),
[configuration #3](https://github.com/vpsfreecz/vpsfree-cz-configuration/pull/3).
The network branches retain the verification gaps above. No production deployment,
network retirement or default-branch integration is authorized. The initiative
remains active; no verification process launched here remains running.

Session identity verified against `dev-session current` from the bound directory
and trusted thread binding; both shell markers are absent. Retained Full-team
roster is unchanged: architect0 owns design, implementer0 owns source/configuration
edits, and reviewer0 completed the independent committed-deliverable review.

## Phase checklist

- [x] Verify session identity and retained roster.
- [x] Establish proposal-only scope and affected repositories.
- [x] Trace counters and allocation semantics; produce architect proposal.
- [x] Consolidate findings and suggested solution for user.
- [x] Reconcile architect brief and establish owned feature worktrees.
- [x] Implement backend, both UIs and configuration channel pins.
- [x] Quick checks, hooks and committed whole-branch source inventory.
- [x] Independent final source review of committed original branches.
- [x] Correct and verify four accepted review findings; reconcile final heads/pins.
- [x] Affected-host builds (all 12); route and export runtime verification.
- [ ] Remaining migration/restore/legacy evidence and KB images (external prerequisites).
- [x] Separate BFF dependency maintenance commit, package verification and PR.
- [x] Handoff committed branches with passed evidence and explicit remaining limits.
- [ ] Default integration and production activation (not authorized).

## Repositories and evidence

Owned worktrees now exist under worktrees/2026-10-05-network-ipv4-left-counter/:
- vpsadmin: branch 2026-10-05-network-ipv4-left-counter,
  base c4d9b50f4e74417ed37b5fe410cca3ec1addc24e.
- vpsadmin-webui: branch dev/network-enabled (repository branch exception),
  base 02ac0c7de1a588dbb14a18e652fe3f7e9b45cc51; default main corrected in manifest.
- vpsadmin-webui-proxy-addr: isolated maintenance branch dev/proxy-addr-patch,
  same exact main base; registered separately, with default main.
- vpsfree-cz-configuration: branch 2026-10-05-network-ipv4-left-counter,
  base cde8451718d75929c931db63626b48f7de92fc4f.
V/config git worktree creation completed but post-checkout hooks failed (unsigned
Overcommit config in V; missing bundle in config). Helper recorded the worktrees;
setup was repaired within Nix by the dedicated setup watcher. No hooks bypassed.
- vpsfree-kb-contracts: branch 2026-10-05-network-ipv4-left-counter,
  base 873758fd6aec0c03f50a94600e0ceab97946f255.
Initial proposal used older source revisions; current implementation bases above
are authoritative. Architect rechecked relevant source behavior at these bases
and recorded exact paths in design.md. Both index pages consume the same
Cluster::PublicStats.ipv4_left. The old count had no enabled state or reservation
exclusion. The accepted new count still describes global allocation-row inventory;
location, autopick/userpick and purpose policies can limit actual VPS selection.
No IP cooldown column/predicate was found.

## Results and limits

Committed source, passing scoped quick checks and independent source review are
available. Production data and deployed revision have not been inspected. Remaining
VM and visual checks are listed above; configuration builds passed.
Public/private exclusion currently relies on network role, not numeric CIDRs.
Initial plan/state committed as `374d6611` on workspace master; unrelated
changes preserved and no declared workspace hook framework found.
All setup commands passed; current verification is detailed in the review packet.

Initial reviewed heads: V6b3628af665049dc095ba985ef0fbe8a22286863,
W811742f50cce2b7724784d0a674c8d4d5dcb6273,
Cdea15f88c38341ecfd3e5030c700d1fee3d854a7,
Kef72876da07dae61449502e2d03856d1d3b133e4. V/W exact feature refs are published;
C/K feature publication follows verification. Original reviewed snapshots and
review findings remain preserved; all application remediations are now committed.
See [complete inventory](branch-inventory.md) and [review packet](review-packet.md).

## Accepted solution and next action

See [accepted architect design](design.md) for revision/path evidence, operation matrix,
concurrency/continuity boundaries, compatibility, rollout, acceptance criteria,
and a read-only per-network diagnostic query (prepared, not executed).

- Add Network.enabled NOT NULL default true; admin-only updates in both UIs.
- Enforce disabled state for new automatic/explicit allocations, detached-owned
  reuse, ownership transfers and owned registration. Retain visibility, existing
  service, release/rollback and trusted same-allocation continuity operations.
- Shared PublicStats count: unowned, unassigned, enabled public IPv4 inventory,
  unreserved; public/private classification uses Network.role only. Preserve allocation-row count;
  do not infer retirement from location/purpose/maintenance settings.
- Upgrade every allocator/writer before disabling pools. Older writer rollback
  ignores policy and is unsafe while disabled networks exist.

Next action: inspect completed CI 37485699588 for selection and successful results
of the three exact remaining scenarios, or supply a supported runner with adequate
capacity. No supported lower-memory route exists at the unchanged V head: these
scenarios require 24 GiB effective memory/shared memory, normally at least 32 GiB
detected free with the runner's default 8 GiB reserves. Regenerate the two KB
images only after a supported capture runtime is supplied. Merge approval for the
separate maintenance PR is distinct from network verification and production
rollout. Production attribution and an explicit retirement list remain operator
inputs for a separately authorized rollout.

## Documentation and cleanup

Plan and [accepted design](design.md) are session-owned planning records. Project
behavior and supported upgrade/rollback guidance are implementation deliverables. Keep this session open. No cleanup.

Stable session portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/

## 2026-10-06 chronological checkpoints

Earlier checkpoints below describe their then-current state; the status and final
verification record above are authoritative for the handoff.

Identity reverified with current from the bound session directory. Both shell
markers are absent; trusted thread binding exactly matches. A root-directory
current lookup initially returned no session; no mutation was made until resolved.
Retained roster unchanged; architect0 assigned brief reconciliation. Canonical
source fetches started; separate frontend origin lacks a fetch refspec, so main
is fetched explicitly into origin/main rather than changing shared settings.
Initial implementation planning refresh will be committed before source work.

Architect reconciled design accepted; implementer0 assigned all application and
channel-pin changes with verified workspace-write access. Network-first shared
SQL admission lock order accepted to avoid registration/IP lock inversion.
Vps::Update chown_vps is included as a new-ownership path. Neither broadening
requires a new user decision: both enforce accepted new-use semantics.
Pinned catalog 3343a06... matches installed package catalog; verification watcher
policy gpt-6-luna/low and native utility configuration dw_ae5d947... verified.

Migration lock-order implementation clarification accepted: preload scoped
destination candidate networks together with source networks before source IP
reload/reservation; shared locks in ID order and final current eligibility
rechecks remain required. No new public continuity bypass.
Setup watcher: V root signature/install, API bootstrap, PHP Composer, W npm,
locked guide resolution, and C bundle/hooks all passed; no operation remains running.

KB impact source inspection: see [kb-impact.md](kb-impact.md). No existing
admin-network or public-counter screenshot/navigation concept found. Required
final-source contract pin/check remains pending in an owned contract worktree.
W open PR inventory was empty via gh on 2026-10-06; no duplicate current PR.

Setup watcher passed V API (117 gems), V PHP Composer (45 installs) and W npm
(407 packages). W npm install reports 3 audit vulnerabilities (2 moderate, 1 high);
no dependency change made. Root hooks remain active. These are setup evidence,
not feature correctness checks. W locked terminology source resolved to
/nix/store/030czw9xwvihmw4l24p97d5r2xxd71vi-source, revision
a65a4dfeb92a59df4a80a737a20bcbf8558793ff; both guide files read by lead.

Parent applied the user-facing-writing skill to EN/CS errors, metadata and UI
help, and supplied exact final strings to implementer0 before regeneration and
commits. New drafts remain subject to parent wording reconciliation. Detailed
setup evidence is in setup-*.log with corresponding zero .exit files.

Migration/swap batch clarification accepted from architect0: retain the scoped
network map for the whole preparation; replacement selection cannot acquire
fresh pools after source IP locks. Swap prelocks both source sets together and
shares that map with both child setups. Disabled source continuity remains valid.
See design.md's dated batch-boundary section. Implementation refinement pending.

Fresh quick_checks_1 Luna/low watcher owns the sequential generator/focused-check
batch supplied by implementer0. Schema generation uses the core-only isolated
network_enabled_schema test DB; parent verified no configured DATABASE_URL or
api/config/database.yml. No long integration/configuration builds started.

Quick1 core schema/API locale generator exited 0. Schema delta is only the
new migration version and enabled column. Core-only locale regeneration also
pruned unrelated plugin translations; source owner will restore baseline
catalogs, reapply intended text and regenerate in all-plugin mode. This result
is not accepted as a final catalog. Quick1 command2 failed exit127 because
watcher omitted .#webui; exact shell corrected for fresh quick_checks_2, which
owns PHP generation and the remaining focused read-only checks. No retry of
a feature failure or hook bypass.

Quick2 PHP locale generation passed (8s). Focused API batch ran 109 examples in
553s, with 108 passing and one counter fixture failure: undefined network_v6
at cluster_spec.rb:198. Counter assertion was not reached. Source owner assigned
fixture correction; logs quick2-api-focused-rspec.log/.exit (1). Migration and W
unit/type checks were not run because watcher stopped at first failure. No
operation remains running. Catalog restoration/regeneration can now proceed.

Architect confirmed automatic allocation batch lifetime from fire2/use_chain
source. Create/clone and multi-address allocation retain IP SQL locks across
child calls; they must capture their scoped candidate union before the first IP
lock. Implementer assigned explicit held-map propagation across requested
families/interfaces, preserving partial clone allocation and disabled-source
continuity. No framework/global lock registry or separate family commits.

Catalogs restored to exact V baseline with only intended additions (11 lines
each before regeneration). Corrected counter fixture uses SpecSeed.network_v6.
Fresh quick_checks_3 owns full-plugin locale generation/health, PHP regeneration,
the failed counter case only, migration spec, W adapter/selector/DOM unit checks
and typecheck. Avoid repeating the already-passing108 examples for a fixture
fix; later substantive source changes still need affected checks. Final PHP
actions use distinct Enable this network / Disable this network msgids to keep
existing VPS action translations intact.

Longer scenario source is drafted, not executed: network_admission MariaDB
interleavings, disabled route/host continuity and detached-use denial, data-safe
migration, legacy confirmed POST/member denial, and React bilingual desktop/mobile
fixtures with screenshot output. Restore/export continuity coverage and automatic
batch closure are being finalized before final committed review.

Quick3 all-plugin API locale generation/health and PHP locales both passed.
Watcher misclassified the explicitly assigned Vroot for PHP as wrong and stopped;
parent inspected log command/CWD and confirmed both were correct, accepting
evidence without rerun. API locale diff is scoped (+10 lines each, no deletion).

Quick4 fixed wrapper completed96s: counter1example and migration2examples passed;
React4files/38tests passed. Typecheck failed with two missing envelope fields in
NetworksPage.test.tsx mocks. Source owner assigned genuine response-shape fix;
no type weakening. All logs quick4-*.log/.exit, no running operation.

Automatic batch source closure is now drafted with actual Create multi-family
and Clone multi-interface behavior cases plus retained-set exhaustion/identity
cases. Scoped backend checks still pending. Restore and export VM scenarios now
cover disabled existing service; helper-default zero IPv4 corrected by explicitly
attaching an existing test IP before disable. Known data/checksum assertions retained.

Parent final short reruns passed: PHP locales-update + locales-health (exit0),
W typecheck plus NetworksPage4DOM tests (exit0). Approved new action translations
compiled; old VPS action translations preserved. W UserNetworkPage action extracted
into UserNetworkAddressActions to preserve its existing structural budget, without
exemptions.

Fresh quick_checks_5 launched reviewed frozen run-implementer-quick5.sh with explicit
per-tool shell routing. It owns scoped Ruby/PHP/Nix checks, affected backend batch
and continuity specs, W inventory generation and ci:quick gates. Logs quick5-*.
Commit preparation follows successful checks; final review still unassigned.

Quick5 stopped at Ruby lint: syntax passed, but explicit file arguments included
the generated schema despite the declared exclusion. Quick6 uses force-exclusion;
the schema remains unchanged. Implementer fixed the real source/test offenses
under existing lint rules and added legacy selector/stale-form regression cases.
Fresh quick_checks_6 owns the reviewed frozen wrapper, including final PHP locale
generation/health, PHP regressions, Nix source formatting, seven backend batch and
continuity spec files, React inventory generation and ci:quick. No concurrency,
browser, VM or configuration builds are launched in this batch. Proposed commit
splits/messages and exact-pin wrappers are prepared for lead inspection.

Quick6 stopped after39s at PHPformatter exit8. Ruby34files clean and CI-selector
16tests/55assertions passed; final PHPcatalog generation/health passed. The first
PHPfile needs only separate lines for table_td arguments; implementer assigned
that fix and a remaining-check wrapper. No operation remains running. Prepared
commit path inventories cover every current V/W change, except React generated
inventory which is intentionally produced by the pending docs:inventory step.

Quick7 PHPformatter and all six syntax checks passed. PHPUnit ran99tests with
98passing; the new CSRF dispatch test's template stub lacks title(), so it
failed before reaching csrf_check. Source owner assigned an explicit stub and
focused class rerun. Global Composer shellsetup output did not change repository
composer.json or composer.lock. Nix/backend/React remaining steps were not run;
no operation remains running. Commit helper inspection confirms explicit owned
path staging, branch/base guards and mandatory active hooks; its evidence gates
must be reconciled with the succeeding focused run before launch.

Quick8 completed150s: PHPformatter/syntax/Csrf4tests, Nix source format, API
sevenfiles72examples/0failures/2pending and React inventory passed. The pending
cases are existing remote clone snapshot retention and multi-interface migration
contracts. React ci:quick passed earlier lint/format/localization/docs/CSP gates,
then stopped on the touched UserNetworkPage inherited exception's changed hash.
No operation remains running.

Lead reread the exact structural policy/model rather than forcing unrelated
page restructuring. Current page683lines is down from accepted691; the model
requires allowance equal current metric. Lead reviewed the limited rowActions
extraction, disabled detached-action guard and desktop/mobile disabled badges,
accepting SHA256046865da62cc7c0cbf14db481e918e507edf6cf73ecab81daf0fced586b170f4
with the existing allowance lowered to683, removal condition<=500 retained and
baseline unchanged. Implementer will update only this reviewed ledger entry and
truthful note/rationale; no new exception, cap growth or audit-model change.
Independent final review will receive this explicit disposition. Further W
checks and per-repository commit gates are being prepared; Vsource is frozen.

V commit attempts stopped before creating any commit: first an untracked PHPUnit
history cache, retained beneath tracking; then a stored Overcommit configuration
signature mismatch. Lead/implementer verified config and custom hooks byte-equal
to c4d9b50f. Lead re-signed through the declared Nix root shell (exit0) and
unstaged only the attempted APIpaths after verifying their owned set. No hooks
bypassed, source edits or unrelated index changes. Exact cause of signature
change remains unknown. Fresh quick9_and_v_commits owns Wfocused tests/quality,
then both Vcommits with mandatory hooks; source remains frozen.

Quick9 and Vcommit batch passed in180s: five Reactfiles42tests, full ci:quick
including all type checks, both Vcommits with mandatory hooks. VAPI commit
819d66b0ec15fa874492437139fb80dc8e175a39; legacy UI/final Vhead
6b3628af665049dc095ba985ef0fbe8a22286863. Per-step logs/exits and SHA artifacts
are authoritative; watcher reported outer exit0 but did not preserve its requested
aggregate wrapper files. No operation remains running. Wworklog/draftPR is
receiving exact final quick evidence before commit; application source is frozen.

## Independent review reconciliation (2026-10-06)

Reviewer0 reviews exact committed V6b3628af/W811742f5/Cdea15f88/Kef72876d,
using saved gpt-6.1-sol/xhigh and all four lanes at high risk. Review completed on the original committed snapshot; see [review result](review-result.md). No Blocking findings.
Two source-backed Important findings and two Advisory findings have been accepted and assigned to
implementer0 as uncommitted narrow corrections pending the full report:

- General: new legacy browser test asserts Enabled/Disabled text while
  boolean_icon renders only an image. Align assertions with the specific
  availability cell's rendered icon; do not change unrelated boolean rendering.
- Risk/compatibility: VPS chown transfers dataset/subdataset export ownership
  but its initial admission batch includes only VPS IPs. Export endpoint IPs
  must enter the same sorted network/IP/host lock batch before any IP row lock.
  Disabled endpoints must reject new ownership before mutations. Existing
  same-owner export service remains valid. This closes an accepted-policy gap.

Architect0 performed a separate read-only verification-tooling investigation.
K/bin/devcluster does support screenshots topology dynamically; its help is
stale. However its startup broad-kills slug-matched processes, later deletes
a workspace-independent socket directory, and has no transition-lock/generation
validation or atomic recorded workspace socket identity. Lifecycle procedure
lines93-110 require those properties. Fresh-slug/absence preflight does not
provide them. Installed catalog has only vpsadmin/vpsadminos providers; the K
capture adapter requires K-local state and offers no supported binding to them.
Do not start K's helper, fabricate provider/state records, or install/activate
a package to bypass this prerequisite. A supported owned capture environment or
a separately scoped runtime compatibility fix is needed for the two PNGs.
No cluster or capture operation was launched. Other verification will proceed
after review remediation; this limitation prevents claiming full visual readiness.

Final independent review received: all four lanes, original complete histories
and migration lineage explicitly accepted. Reviewer found no obsolete history
and accepted the structural debt downward ratchet. Added Advisory corrections:
server-side enabled filtering before first50 suggestion limit, and visible
network-write capability error/retry with stale-capability denial. All four
findings are assigned to the same source owner. Root will inspect focused fixes
and use skill step9 unless actual changes expand reviewed behavior. No long
verification has started.

GitHub read-only snapshot: Vhead6b3628af migration, RuboCop, PHPunit,
libnodectld and i18n workflows passed; CI37469395891 and API topics37469395795
were still in progress. Wfeature branch had no workflow runs. These old-head
results are preliminary and will not substitute for final revised-head checks.

Narrow drafts inspected directly: endpoint admission shares one sorted original
batch, browser assertions target the specific availability icon, React query
uses existing OPTIONS metadata before the suggestion limit and preserves stale
guards/old-API omission, editor error/retry gates cached writes. Root applied
final owning V/W English docs with writing skill. Fresh remediation_quick_1
Luna/low watcher now owns the frozen five-step syntax/lint/API update/React
unit/full-ci:quick packet. No long integration/browser/config check yet.

Remediation quick1 stopped at Ruby lint in10s: both syntax checks passed, three
argument/hash alignment offenses in update_spec.rb274/277. No later step ran.
Source owner assigned exact formatting correction and immutable quick2 packet.
No runtime failure or still-running operation; log/exit evidence retained.

Remediation quick2 passed all five steps in3m15s: Ruby syntax/lint, legacy Node
syntax, VPS update14examples/0failures, six Reactfiles51tests and full ci:quick
(including docs/all type domains). Frozen source/helper checksums unchanged.
No operation remains running. All four review corrections now have direct
inspection/focused verification under skill step9, with no contract expansion.
Final source evidence prose, normal-hook consolidation and regenerated final
C/K pins precede long checks. Original reviewed diffs/histories preserved as
review-original-*; final records will name rewritten exact heads.

Normal-hook API/legacy/W fixup commits and autosquash completed. Final corrected
V30603a832d2848207bd7319c79c6b0388bc8646a has API718c031f7c2d212fd36e9ee7fe135b06be2df64c
and legacy30603a83; Wb3b756a7b45864459bd39481a0d5245886777660 is one commit.
Original authors/messages retained; exact final tree equality checked before/
after rebase and V migrations/schema unchanged. Complete two/one series and
remediation range-diffs saved. Corrected publication and regenerated C/K pins
remain next; old remote refs/pins still name original reviewed source heads.

Corrected V/W feature heads published with explicit old-head force-with-lease;
remote heads verified. Superseded same-branch CI37469395891 cancellation requested;
current heads/other branches untouched. Repin watcher stopped before C/K mutation
in2s: explicit Wfetch rejected non-fast-forward local origin/dev/network-enabled
(still811742f5). Parent verified remoteWb3b756a7 and all four worktrees clean with
C/K oldheads unchanged, then synced ONLY that remote-tracking ref with an explicit
+refspec. Wbareorigin lacks fetch refspec, so force-push had not refreshed it.
No default/source feature ref was changed by this sync. Original packet can
resume unchanged now. Watcher failed to retain requested aggregate files;
reported command/exit1 and parent exact ref/status evidence are recorded here.

## Final corrected commit gate

- vpsadmin: `30603a832d2848207bd7319c79c6b0388bc8646a`.
- vpsadmin-webui: `b3b756a7b45864459bd39481a0d5245886777660`.
- vpsfree-cz-configuration: `a6243f09265398368e07695dd531e4a0e312350b`.
- vpsfree-kb-contracts: `8c396b88ff10bf71c47e2364e7ea1ee34f20d184`.

V/W published; C/K not yet published. Normal hooks and focused checks pass.
Complete corrected inventory and diffs are linked in branch-inventory.md; original review evidence is preserved. Narrow remediations required direct verification, with no design expansion or new bypass. Generated pin review confirms only intended nodes and exact source revisions.

Post-review batch1 stopped at SQL: 5 examples, 1 failure. Four admission-ordering cases passed; parallel admission fixture omitted required TransactionChain.type and failed before locks. implementer0 assigned narrow fixture/isolation diagnosis and correction. No continuing process. Browser/build verification may proceed independently with unchanged W. Original failed CI evidence downloaded to review-original-ci-api-failed.log; no blind rerun.

React browser attempt1 failed before page execution because cached generic-Linux Chromium cannot launch on NixOS (stub-ld, exit127); four desktop cases all failed to launch. No mobile/build execution. W head b3b756a7 was correctly checked by wrapper; watcher cited root workspace HEAD in error, which is not tested repository identity. Root diagnosed environment from raw log and chose existing E2E_CHROMIUM_EXECUTABLE_PATH with Chromium from W locked nixpkgs input, no browser-policy relaxation or source edit.

Pinned Chromium from W nixpkgs runs the browser successfully (154.0.8037.57). Desktop2 has two passing older-API/inventory cases and two fixture failures: incomplete single-key OPTIONS response is unwrapped as a namespace and loses input metadata, hiding the availability control. implementer0 assigned realistic action-description fixture correction. No product copy or API adapter change is authorized by this finding. Mobile/build remain unrun. Current API foundation CI core/full failure logs retained; missing typed/runtime chain fixture and committed-fixture collisions are being repaired narrowly before re-verification.

Fixture repair quick2 passed all four steps in167s: scoped syntax/lint, core18examples0failures at36954, full18examples0failures at9346, and full Wci:quick. Per-example cleanup detects surviving reservations/inventory/quota changes after joining all workers. Modern/old API browser fixture metadata matches HaveAPI action description shape. Production code/schema/adapter/copy remain unchanged. Root directly inspected narrow test repairs under review step9. Normal-hook fixups are being consolidated into original logical commits before browser/VM continuation. Original leak mechanism remains unproven; clean focused reproductions now pass at both failed seeds.

Root commit wrapper first stopped before staging because mixed absolute-source/relative-helper manifest entries were checked from the V cwd. Root corrected only its own wrapper to check that manifest from tracking; source/helper bytes and Git HEAD were unchanged. Normal-hook retry is in progress.

## Final fixture/browser verification and source consolidation

Core and all-plugin concurrency/Create checks passed 18 examples each at the
original failing CI seeds 36954 and 9346. The cleanup mechanism's historical
leak remains unproven; scoped teardown checks now expose leaked reservations,
IP/host rows, seed changes and quota changes rather than allowing cross-example
contamination. The fix uses the standard typed transaction-chain helper.

React desktop and mobile each passed all four scoped synthetic browser cases at
e00336ccf06fe701116c63623a5d8bf93b201dbb. The production build passed. The utility
report accidentally appended a fifth character to this SHA; root verified the
actual exact head, wrapper guard and log receipts. No operation remains running.
Root inspected all four EN/CS editor captures. Final evidence prose passed the
68-document/71-requirement audit, then was committed and consolidated into one
W feature commit e4c49bcdc91b33b7f644a2f125231cb413cf4bf4. App/e2e/scripts/package
and flake bytes are identical to the tested e003 head. V remains two logical
commits at be136b6c00f03b85b7a12cc57550b4a1394a94a7; schema/migrations unchanged
from the reviewed corrected source. Both trees are clean. Final publication/pin
refresh is being prepared; no merge/deployment or lifecycle operation occurred.

Final pins committed: C dd10d88073da3aed6c4512e938abe4374422aab1 (two canonical
confctl commits); K 291566b2c0bd43389802f607852fd9a4f8241752 (one exact-pin commit).
Root inspected full lock/source diffs and static KB checks passed. V/W feature
refs are published with explicit leases and owned tracking refs synchronized.
Only superseded V CI run 37476572943 was canceled. No current-head CI cancellation.
All worktrees clean; final inventory refreshed. Runtime/build gate remains clear
under completed independent review plus direct narrow fixture verification.

Draft review PRs created after duplicate checks: [vpsadmin #45](https://github.com/vpsfreecz/vpsadmin/pull/45)
and [vpsadmin-webui #19](https://github.com/vpsfreecz/vpsadmin-webui/pull/19).
Descriptions link the stable portal, actual checks and remaining proof limits.
Current-head API/libnodectld/PHP/i18n/RuboCop/migration/CI jobs and W CI/browser
jobs are queued or running; several quick V workflows passed. Exact snapshots
are fixture-final-ci-{v,w}-status.json. No current-head CI wait/cancellation has
been performed. A fresh watcher owns the serial VM/legacy/configuration batch;
initial metadata evaluation has shown no unexpected kernel compilation.

C/K feature refs published at dd10d88073da3aed6c4512e938abe4374422aab1 /
291566b2c0bd43389802f607852fd9a4f8241752 after fresh default ancestry checks,
with normal Git/Nix environments and no force/default push. All four final
feature heads are now published; worktrees remain clean.

Configuration draft PR: [#3](https://github.com/vpsfreecz/vpsfree-cz-configuration/pull/3).
VM routes selector inventory passed and the single selected test began. Runner
warned about 16GiB requested shm versus a14.3GiB scheduling limit. Root checked
actual resources read-only: /dev/shm available23,935,971,328 bytes and RAM
available43,697,700,864 bytes at that snapshot. Both exceed the request; root
allowed the one owned test to continue without concurrent tests or scheduler
limit changes. Unrelated shared-memory users/processes remain untouched. This
is headroom evidence at one snapshot, not a completed runtime result.

VM route run stopped before feature assertions: OsVm::Shell UNIXServer rejected
a141-byte socket path (108-byte maximum), after253.18s test time / about10m
batch including metadata. Inventory passed; later VM/legacy/build modes did
not run. No owned processes remain and no local kernel compile appeared.
Parent traced test-runner Executor#test_sock_dir to state_dir/socks and OsVm
Machine#socket_path to hash-prefixed machine socket filenames. Verification
runner now uses mktemp-created private0700 short /tmp/n6-* state roots for each
owned isolated test, with exact session/revision/selector/UID/path receipts in
tracking. Failed logs remain; no production source or persistent development
cluster state changed. Same-head passed route inventory is reused.

Separate dependency preparation used the monitor skill's visible parent fallback
while the single utility slot remained occupied by the VM batch. Targeted npm
generation, exact installed-leaf check, both production audits and independent
prefetches passed. BFF and root production audits report zero vulnerabilities.
The BFF lock delta is proxy-addr 2.0.8 metadata plus npm key ordering only; the
frontend lock/hash and product runtime source are unchanged. New canonical BFF
hash is sha256-m6CayVcO1z+Xuy+XlAEqVLoRFRACSNjdcn4pae1T+Dc=. Source owner is
applying that hash and drafting scoped packaging/work-log records before checks.

Maintenance quick stage passed via the same visible parent-monitor fallback:
all existing BFF suites, package/proxy-response script fixtures, focused
bootstrap/OAuth units, complete ci:quick and Nix format checks. Exact generated
lock/hash/source guards passed before and after checks. Package builds and clean
provenance verification remain pending for the separate committed candidate.

W CI run37486610216 failed only its BFF dependency audit; required quick/unit
gates were skipped, while Chromium script regression and production build
passed. Failed log/job metadata downloaded before any retry. Unchanged base
and feature BFF lock both contain proxy-addr2.0.7. Upstream critical advisory
GHSA-jqcg-44mw-7w3h was verified; patched2.0.8 is a separate dependency
prerequisite. Root is preparing an isolated reviewable fix, preserving current
network feature heads/pins/runtime guard. No claim of deployed exploitability
is made. Current V broad API matrix and integration CI are still running.

Final-head CI snapshot: 25 of 26 API matrix jobs passed, including both core
and full foundation jobs that failed before the fixture repair. Full platform
infrastructure and integration CI remain running. W smoke browser workflow
37486610147 passed at e4c49bcdc91b33b7f644a2f125231cb413cf4bf4. The separate
dependency audit failure remains unresolved in the network branch; no unchanged
CI rerun was launched. Local route scenario has reached test VPS creation.

Short-state VM route scenario passed: the route/host-address example succeeded
in 301.92 seconds and the script finished in 657.24 seconds. The watcher still
owns cleanup and the serial batch; wrapper exit and later mode results remain
pending. No unexpected kernel compilation or resource exhaustion was reported.

Complete final-head API matrix 37485699478 subsequently passed: all 26 jobs
successful at be136b6c00f03b85b7a12cc57550b4a1394a94a7. This is broad CI evidence
in addition to the focused SQL runs. Integration CI remains separate and running.
Local route runner completed cleanup and returned exit 0; export inventory also
passed before the export scenario entered its private short state directory.

Export lifecycle VM scenario passed: its example succeeded in 123.21 seconds,
script in 433.99 seconds. Owned VM cleanup is still running; the serial batch
will continue to migration and restore data checks after the mode exits.
Export cleanup subsequently completed and the mode returned exit 0. Migration
selector preparation is now running under the same owned watcher.

Migration resource prerequisite: the runner confirmed 24 GiB of shared memory
for three 8 GiB VMs, exceeding the 22.3 GiB actual free snapshot. The parent
authorized cancellation of only the owned batch before VM startup. Watcher
interrupted it during test JSON build; no matching owned runner remains. Route
and export exits are 0; migration inventory is 0, migration exit is 1 from
interruption, not a feature assertion. Restore and legacy modes were not run.
Their metadata also declares three VMs; no capacity override or foreign cleanup
is authorized. All logs and /tmp/n6-taK4ggY9 state remain preserved.

Separate maintenance commit a7361bb2912485b61a5a0b1472d51158ac08ec96 is clean,
one focused four-file commit from main base 02ac0c7. Normal Git/hook inspection
and final docs audit passed. The complete diff contains only generated leaf
dependency/hash and matching documentation metadata; there are no migrations,
obsolete fixes, runtime/trust/API edits or network features. Mandatory review
is exempt under its mechanical dependency-only criterion. Fresh Luna/low watcher
proxy_addr_clean_packages owns the exact five Nix builds/checks and clean paired
metadata proof. The network feature heads and C/K pins remain unchanged.

Maintenance package verification completed exit 0: BFF/frontend and provenance,
source-content/package-content checks passed at a7361bb2912485b61a5a0b1472d51158ac08ec96.
Actual paired metadata matches that full revision with dirty=false; installed
proxy-addr is 2.0.8. The feature was published after fresh main ancestry/SSH
checks, and [separate draft PR #20](https://github.com/vpsfreecz/vpsadmin-webui/pull/20)
was created after duplicate checks. Ready for maintenance review; no merge or
deployment authorized. The network PR still requires proper integration of the
dependency prerequisite; no patch was bundled or cherry-picked into it.
Maintenance CI 37494845158 passed at the exact published a7361bb2 head.
Its broader smoke workflow remains separate evidence; no unchanged CI rerun
or merge was launched.

Architect0 is investigating only a supported isolated test-resource profile;
no VM/flake edits, override, lifecycle or package activation is authorized by
that read-only task. Configuration-only batch started via visible parent fallback
while the package utility slot was occupied; fresh config_final_observation5
now observes its independent logs/exit artifacts. Parent retains tool session
37524 for final status/cancellation. int.api1 build passed; other hosts pending.

Architect read-only resource investigation found no existing supported lower
memory route for unchanged V: --test-config requires missing tested-flake
testFramework exports and is script framework data, not a VM-sizing interface.
Neither bootMemory nor extraModules is connected through the current caller.
No adapter or source/config override was introduced. Required remaining proof is
exact-selector successful evidence from existing CI 37485699588, or a supported
environment with adequate real capacity (24 GiB effective, normally 32 GiB
detected free with the default 8 GiB reserves). Current CI metadata still says
in_progress at the exact final head. Interrupted migration is not a failed
feature assertion; restore/legacy have not run locally.

Configuration verification finished: all 12 actual channel consumers returned
exit 0 at C dd10d88073da3aed6c4512e938abe4374422aab1, pinning V be136b6c and W
e4c49bcd. The root-owned run returned exit 0; fresh watcher
config_final_observation5 observed completion independently. No unexpected kernel
compilation was found in inspected logs. Full logs were retained for the final
two hosts; confctl removed earlier full logs before copying, but all per-host
console summaries and exit receipts remain. Built generations were not deployed.
All five worktrees were rechecked clean after verification.
