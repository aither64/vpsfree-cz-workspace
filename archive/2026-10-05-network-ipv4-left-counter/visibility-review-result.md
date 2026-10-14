# Independent visibility review result (2026-10-07)

Reviewer0 completed all four lanes at retained gpt-6.1-sol/xhigh, review purpose,
read_only, thread 01a10c52-55c7-7490-8cd9-75efda7f00d9. Identity/live roster matched
this session; no overrides, nested delegation, writes or verification execution.
Risk is high. Exact assigned bases/heads and complete histories are in
visibility-review-packet.md and visibility-final-inventory.json; these artifacts
remain the original reviewed snapshots, not certification of later fixes.

Result: zero Blocking, one Important, one Advisory.

## Findings

Important, General, V d7d7fb668: network_write_spec.rb:130-141 still expects a
member Index(enabled:false) request to return the disabled network. New
Network::Index#query:67-68 correctly intersects enabled:true, so the result must
be empty. Quick4's five files omit this original regression. Fix the example
name/list assertion, retain member forbidden-write and disabled Show checks,
and verify the whole file in core/full modes. Reviewer inspected the exact
committed blob and excluded the pending uncommitted correction.

Advisory, General, W e4c49bcd: useProgressiveSuggestedIpQueries.ts:60-67 awaits a
shared capability query outside its 12-second signal; ipAddresses.ts:96-99
supplies no signal. A stalled OPTIONS can delay all suggestions/progression.
Bound the shared request or each waiter without losing deduplication/error
feedback and add stalled-request coverage if fixing. This is loading feedback,
not admission enforcement. Root confirmed the source path and accepted it as a
recorded availability limitation, leaving W unchanged in this backend follow-up.
See visibility-review-findings.md for the disposition and narrow fix evidence.

## Lane and history conclusions

No additional concrete architecture, proportionality or risk/compatibility issue.
The later accepted list policy warrants a separate V commit. Network owns
admission locks/enabled policy; IpAddress owns captured identity/current-row
checks/unreserved scope. Captured source/destination unions avoid late pool
expansion after IP locks. The two different list restrictions belong to their
resource owners; no new generic permission registry or default_scope is needed.

The non-admin availability OR stays inside existing user_visible_scope. It does
not grant foreign assigned IPs or promote export-only association access into
Index. Explicit filters narrow it; count/pagination use the restricted query.
Show/shared scopes and existing owned/assigned continuity are preserved. The
original export-owner admission gap is already corrected. Counter classification
is solely public_access role, enabled IPv4 and unowned/unassigned/unreserved;
location joins cannot duplicate it. No RFC1918 logic or new public metadata.

All3/1/2/1 commits are coherent. No obsolete unmerged fixups, abandoned paths or
transitional migrations remain. The stale old-policy assertion is a final-tree
issue to fix, not a reason to erase the accepted separate policy commit.
V has one migration 20261006120000 after 20260914190000, direct reversible
NOT NULL/default-true bool, core schema version/column only, no stale guards.
Follow-up blobs unchanged; retained defaults/tags do not establish release
inclusion. Declared use is disposable tests, production provenance unverified.
W/C/K have no migrations.

C preserves every unrelated fresh-base node, including devWorkspace. Only the
two selected application locked rev/narHash/time fields change; W->Services
follows stays intact, and generated channel history remains canonical. K's five
records/effective fresh shell source agree with V; fingerprints/pages/PNGs are
unchanged. W's 683-line debt allowance is a 691→683 downward ratchet with matching
hash, historical sourceRevision, 37 exceptions and ≤500 removal condition retained;
no baseline/model/allowance growth. Retained W is not current-main certification.

## Evidence and remaining limits

Reviewer parsed native JSON: prior core 226 with exactly 3 failed IDs, corrected
core 3 pass, full 226 matching IDs all pass, no pending/outside errors. Lint/pin/KB receipts
are 0, but omit the stale write test until focused correction verification.
Older-head receipts retain their stated SQL/admission/spec/browser/route/export/
config evidence; they do not certify new queries or new C generations.

Remaining exact checks: migration-with-data, remote descendant restore, legacy
admin-cluster and 12 current C consumers, with real capacity and payload/checksum/
IP assertions. Do not substitute selectors or await CI. W still omits advanced
main's dependency/mobile/language work and needs reconciliation before current
release/deployment readiness. CS/EN member IP-list images require a supported
owned capture runtime; static contracts are not bitmap proof. No helper or
lifecycle bypass is authorized.

Production revisions, writers, consumption, counter attribution and retirement
list remain external. Schema first, all writers before first disable, compatible
controls afterward; old writer rollback loses policy, UI rollback preserves it,
no coordinated node update. Review supplies no integration/deployment/retirement
or lifecycle permission. Root owns the step 9 narrow fix checks/publication and
final readiness limits. No reviewer rerun is required merely to confirm this
assertion-only requested fix.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/
