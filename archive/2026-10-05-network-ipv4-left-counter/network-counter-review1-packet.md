# Network inventory and availability final review packet

Final assignment packet: intended changes are committed and exact-head hosted
quick verification passed under the user override of local suites.
Overall risk HIGH: complete V branch includes authorization/admission, locking
and a database migration; the refinement adds an admin-only public contract.
Lanes: GENERAL, architecture/repetition, scope/proportionality, risk/compatibility.
Reviewer selection: retained ready read-only review-purpose reviewer0,
gpt-6.1-sol/xhigh, no override/fallback or nested reviewer.

## Requested outcome and boundary

Accepted design.md:2086–2273 records the October 8 refinement. Both interfaces
show authoritative Available to users and Owned, not assigned. The former counts
registered allocation rows with no owner/interface/reservation and returns zero
for disabled pools; the latter includes owned interface-null rows in reserved or
disabled pools. Prefix rows count once. Assigned still includes VPS and export
interfaces; editor uses separate existing Owned total. New counters are admin-only,
including Network associations. Old count semantics, permission scopes, admission,
cluster counter and schema are retained.

Legacy network rows use four vertical groups. Routed-IP lists have no Enabled
column, explicit false networks use grey rows and address tooltips; details and
assigned-service/removal paths remain available. React network layout stays;
desktop/mobile admin Networking flags show disabled only on explicit false.
Optional missing count data renders unknown/dash, never arithmetic guesses;
numeric zero is retained. Product copy is root-approved EN/CS.

No allocation-policy expansion, RFC1918 classification change, new fetch/filter,
shared visibility/default scope, new count HTTP capability, new CI selector,
debt waiver, production deployment, default integration or KB publication.
User expressly forbids LOCAL CI. Normal required hooks and source-only catalog /
inventory generators were allowed. Hosted exact-head verification replaces local
suites in the review gate. Manual preview is not final-head deployment proof yet.

## Whole branches, histories and splits

Exact clean bases/heads, complete lists, trees and checksums are in
network-counter-review1-inventory.json. Each project has a full-index binary
network-counter-review1-<project>.diff and complete .history.

V: 81f1f1aabdd18a042d276aa4be3ca32173ff14d0 ->
cc8e9e7e421a258a46279304c910f88e2ad33147; four logical commits: API admission/schema,
legacy availability/inventory, separately accepted Index policy, additive counters.
PHP refinement is folded into its owner; original API and Index patches retain
patch equality. The counter has its own additive contract purpose.
W: 5d853740a43ddd3ab2b73a976a48367065038f9b ->
a9d0b5e9402faafef937894f50463da3c27e8935; one owning availability/inventory commit.
Rebase preserves main mobile/language work and proxy-addr2.0.8, with both
REQ050/REQ051 retained. A narrow exact adopted-count expectation35 is folded in,
with errors[], deferred216 and all gates unchanged. No duplicate dependency fix.
C: 7e744b49ef90ba39d13b0f82a10a1f4c161c75f3 ->
525c02fea0334222020c492c29bd9d8e06d29de9; two canonical generated streams V/W.
K original: 873758fd6aec0c03f50a94600e0ceab97946f255 ->
819c4824eddbad89a3b1f797219becd8d33fcc48; one exact five-record V pin.
No merges/fixups/repeated pin streams remain. Require independent whole-branch
history and supported compatibility-path conclusions; do not only review counters.

## Provenance, actual consumers and documentation

network-counter-migration-provenance1.json records the sole feature migration
20261006120000_add_network_enabled immediately after20260914190000, and exact
schema/migration blobs unchanged from reviewed V5d. It adds final NOT NULL/default
true directly via reversible change. No counter migration; W/C/K no migrations.
Known external development consumption includes disposable API/VM databases and
the user's running manual preview at priorV5d. Production merge/release/deployment
consumption remains unverified. Retained refs are not production evidence.

Network owns new row readers/resource output. Consumers: real PHP HaveAPI
ResourceInstance/XTemplate and React optional network adapter, network page and
two admin IP responsive renderers. Legacy association access/export continuity and
new-assignment selectors keep existing semantics. Inspect actual permission and
association consumers from the full branch, not only supplied test fixtures.

C locked target metadata is Vcc/Wa9; W follows vpsadminServices. Strict comparison
with fresh default7e retains all unrelated nodes/edges/follows, including new
current-default devWorkspace and OS staging sources. K five exact records agree
on Vcc; pages/fingerprints/PNGs/scenarios unchanged. RuntimeK68/D51/E06 are separate
unchanged published deliverables; original K does not silently activate them.

Owning docs: V docs/ip-locking.md; W docs/design/{API_CONTRACTS,WORKFLOWS,
REQUIREMENTS,EVIDENCE_MATRIX}.md and docs/work-log/2026-10-06-network-availability.md (October 8 checkpoint). Source proposal and final copy JSON
explain optional old-API behavior, units, export assignment and admission separation.
Locked W terminology source revision a65a4dfeb92a59df4a80a737a20bcbf8558793ff.
Operational tracking is in state/plan; feature docs do not certify pending rollout.

## Evidence and remaining gates

Quick gate PASSED. V push API37751585267 succeeded across26 topic jobs and the
coverage aggregate. Affected full/core network236 and ip-ownership117 have zero
failures/pending/outside errors and identical scoped ID/status sets. All4 new
counter cases pass in both modes. Foundation1432 has52 core /3 full pending;
plugin-dependent core omissions and three existing snapshot/migration known
limitations are recorded in network-counter-hosted-api-result1.json.
The same-head PR duplicate37751591968 last remains in_progress; it is not needed
as a second proof and is not cancelled.
V PHP37751585268/91996, i18n85330/92018, RuboCop85374/92014,
migration85294/92056 succeeded (all IDs prefix377515). Native snapshots are
network-counter-hosted-v1-<ID>.json. Full hosted PHP log
network-counter-hosted-php37751585268.log reports107 tests/602 assertions and one
deprecation; its latest log does not name that deprecation. No suppression added.
W CI37752175357 succeeded (quality, script/unit/BFF, production build, Chromium
script lane). Focused rendered/adapter suites24 cases appear in its native log;
compiler import closure is35adopted/216deferred with no errors. W smoke37752175398
completed success across chromium/mobile-chrome/mobile-webkit. Native logs and
JSONs network-counter-hosted-final1-<ID>.*; exact hosted screenshots in
network-counter-hosted-final1-w-browser/. Parent visual interpretation follows.
Original K819 Check37752912755 succeeded: reported60 concepts/120 variants/
120existingPNGs, four fixture groups all green; configured --allow-missing does
not prove bitmap freshness. Native full hosted log retained. No local CI/test/build is substituted. All normal hooks
passed in declared Nix environments; no bypass or re-sign. V first ambient push
failed due Overcommit0.71 vs declared0.73; exact same push in its shell succeeded.
Source generators returned zero with intended catalogs, W inventory byte-identical.

Hosted V API includes full/core network/ip-ownership and foundation, ordinary
complete topic coverage. PHP suite includes ten actual-client methods and three
new grouping/escaping/capacity cases. W normal quality/unit/script/build + tagged
EN/CS desktop/mobile smoke covers counts/disabled-only flags. Prepared counts in
network-counter-source-proposal1.md are not executed counts. Require native result
and artifact interpretation rather than old successful receipts.

Residual limits retained: original W shared-OPTIONS timeout Advisory is accepted
and unresolved; current changes do not claim to fix it. No actual production
writer inventory/count attribution/network retirement verification. Schema first,
all allocation writers upgraded before disabling, then compatible controls; old
writer rollback loses admission enforcement. UI rollback preserves it. No node
update required by feature. Current preview API/React are earlier heads; supported
services refresh follows source review. Synthetic screenshots do not prove live API.
Only two KB PNGs (CS/EN networking/ip-address-list) are selected for future genuine
regeneration/export/strict validation/visual review; existing images are not fresh.
No long local API/VM/config12 build/portable capture tests will run under user override.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/)
