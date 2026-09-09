---
lifecycle: active
---

# IP release mechanism

## Current status

Implementation and all mandatory review corrections are committed and pushed.
The full local browser flow and all hosted CI checks passed. Broader WebUI,
networking and DNS integration is running on the shared runner; the managed KB
runtime check is queued. No production writes, merge, or deployment occurred.

Current vpsadmin head: 1e2d2d7c9bec10d7eb06feaa2c172d10d9fb7a15.
Its three commits separate existing ownership/accounting safety, campaign API,
and WebUI. The final amendment changed only two browser fixture/spec files;
API, WebUI product code and node code remain identical to 42ccae0c. All hooks
passed. Earlier tree-preserving history rewrites are recorded below.
Notification overlay remains 420c98c51ed3db015a366a5564e2128fc83a91b4,
with successful current-head CI. KB contract
9d79ff9d04d9df852898042aecf69b5e4c74567f is pushed and pins 1e2d2d7c9 exactly, preserving its existing vpsAdminOS runtime pin. Full local
contract checks and current-head Check CI passed.

Initial coordination plan/state were committed in 767669d. Ongoing records below
are chronological evidence; this status and the final handoff section take
precedence over older pending-task entries. This is the consolidated
implementation handoff checkpoint for 2026-09-10.

## Verification summary

- All four mandatory review lanes completed at gpt-5.6-sol/xhigh. Blocking and
  Important findings were fixed; narrow corrections received focused checks.
  The chronological review sections and immutable packets preserve the audit.
- Actual API + NodeCtld confirmation checks passed success, failure and rollback
  (3 examples), including cleanup, ownership/quota retention and manual retry.
- Independent SQL connection tests passed for ownership/assignment, quota updates,
  policy/reason/exemption races and network-registration ordering. Capacity tests
  exercise 100 allocations, repeat release, IPv6 prefixes and legacy provenance.
- Existing writer/API coverage passed 110 examples; direct IpAddress API coverage
  passed 47; final Network invariant corrections passed 35. The broader deferred
  API/model run passed 120 with one existing pending migration contract.
- PHP regression suite passed 91 tests/368 assertions; current-head PHP and i18n
  CI passed. Migration CI, RuboCop and libnodectld CI passed on the identical
  component trees before the final browser-fixture-only amendment.
- Notification overlay checks passed, including 8 real reconciliation/rendering
  combinations across CS/EN, initial/update notices and both retention policies.
  Overlay current-head CI passed; no mail was sent to real recipients.
- Full KB checks passed 60 tests/194 assertions, navigation/page bindings and all
  120 screenshot files. No existing reader-visible documentation/capture drift.
  Exact API pin 1e2d2d7c9 is committed and pushed in contract 9d79ff9.
- Browser v3 passed all five tests. All 26 API topic jobs and their coverage
  check passed on the final head. Broader shared-runner integration is running;
  the managed KB runtime check is queued.

## Repositories

- vpsadmin: branch 2026-09-09-ip-release-mechanism at
  worktrees/2026-09-09-ip-release-mechanism/vpsadmin; base 19971f039.
- vpsfree-notification-templates: same branch/worktree group; base 9e1ddbd.
- vpsfree-kb-contracts: same branch/worktree group; base81d6d7d.
  Exact-pin checks passed at 1e2d2d7c9; contract head 9d79ff9 is pushed.
- Shared workspace remains master; unrelated tracking changes preserved.

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
- Initial and explicit update mail only; no automatic campaign actions.

## Next steps

Review the pushed implementation. Follow the two shared-runner jobs below
before merging or deploying; investigate any failure before accepting a rerun. Production merge/deployment remains
outside this implementation request; the documented writer rollout and legacy
quota reconciliation are prerequisites for later operational use.

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
