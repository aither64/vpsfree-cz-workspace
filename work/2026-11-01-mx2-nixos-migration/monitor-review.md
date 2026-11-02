# Targeted final review — mx2 exporter metadata

Reviewer0 report delivered read-only via lead; lead records the accepted report
and evidence qualifications here. No findings in affected general,
architecture/repetition or risk/compatibility lanes. Existing scope conclusion
unchanged. One existing-interface declaration is the smallest correct repair.
Proceed to required new-system builds; no deployment/integration permission.

## Identity and exact scope

Retained reviewer0, thread01a19caf-15c8-74a2-baf1-6594cf30d117,
savedgpt-6.1-sol/xhigh/read_only; same-session current/env/binding independently
verified, no override/fallback/nestedreview/authorship. Mandatory step10 applies
because real monitor consumer behavior was not covered by prior test-only fixes.
Skill/affected references/local source read. No build, production access, source/
file/Git mutation by reviewer.

Basec040c14cdbacc07998700b524996a89306188d7f; prior runtime8d4e03d53699d80f46030b0ee6eb213151b8ae30;
new1e3afc478fb72b54a25a0147910463f060fee88f,
tree77d73449040aba400215ca81843c3d6a2173593c. Complete old/new source delta solely
services.node-exporter={} at cluster/cz.vpsfree/containers/mx2/module.nix29.
Worktree/whole-range whitespace/merge-base pass. Reviewer remote check still
showed8d during review; final publication remains owner/lead verification.

## Producer/consumer correctness

modules/cluster/default.nix expands declared services using authoritative
modules/services/definitions.nix73 defaultport9100. Neighboring NixOS containers
use the same empty declaration. Shared modules/system/monitoring.nix already
enables exporter and source-restricted firewall; built8d unit is enabled with
0.0.0.0:9100. New metadata enables no daemon/firewall/peer/persistence change.
No parallel registry, generic consumer fallback, shared monitor edit or inputs.

Both monitors use all-machine selection in modules/clusterconf/monitor/default.nix.
Its infra branch148-157 requires services.node-exporter.port. Owner proved
baseline missing[] vs8donlymx2; reviewer independently evaluated current missing[].
Both complete monitor and allfive system evaluations pass. Fix belongs to new
producer, not weaker consumer validation. Metadata is enabled/non-monitor,
monitoring.target=null, exporter.address37.205.11.114/port9100/monitor=null.

Important evidence distinction: monitorTarget63-65 uses host FQDN when targetnull.
Actual scrape endpoint mx2.vpsfree.cz:9100, not literal37.205.11.114:9100;
that address is service metadata and expected resolution. Corrected receipts
preserve this. Future deployed resolver/reachability and metric/monitor health
checks still required; unavailable candidate can produce normal alerts.
No API/schema/queue/rolling-version or fleet-wide update incompatibility.

## Verification identity and artifact qualification

Batch6 full three-VM mail suite passed exit0/227.03s (script202.93s) at8d;
mx2/bothDNSserver builds passed. mon1 failed missingmetadata, mon2notrun.
No batch6 operation remains. Reviewer inspected actual successlog/status.

New-head check independently evaluates EXACT priorpassed
/nix/store/8pan3ddqairw3js87iaysvjqwzalxgls-vm-test-run-mx2.drv,
expected /nix/store/jgq1lk68xjj40j2h4wnw403pc3nylni4-vm-test-run-mx2.
Complete lockhash505f6c89e18972827beecc29a0c7c85e1df2576ed4074205501167a3dd6f326a
and blobec3d5aea9a7e55e69778e3ae4136cf2b3bb84e86 unchanged; mail/test/fixture
files unchanged. Canonical complete derivationJSON SHA256
d1e739bbeefe29f257dbb3a5e27558bb2183fe48314d324fa59a7ee661191255.
Reuse binds successfulrun+immutablederivation/fullinputs, not source-tree equality;
no VM rerun needed for metadata-only successor.

Immediately postrun root path-info verified8pan deriver, output NAR
sha256-pQpattmS9VmO3ZIQUFn66az8GSmB4IvYhTTCFn6SUmo=, registration1793638801.
Later reviewer/owner/root filesystem+path-info find it absent/null. No explicit
remote store selected, removalcause unknown, no session-owned storedeletion.
Correct fact is realization/NAR verified then, artifact currently unavailable.
Retain passlog/status/derivation/input proof; do not claim current availability,
re-run unnecessarily or investigate broad GC. This does not invalidate passreuse.
Root repeat path-info returned exit0 withnull+stderr, so availability follows
mapping/filesystem, not CLIexit alone. Allfive new systemderivations need builds;
old systems cannot certify successor.

## Complete history and final gates

Full current series:

1. 9c6e36135192f65baed975e3b127160f068e0b0d host/shared policy/exporter metadata.
2. a5848319ae19d1bcd348ab3837683dec71c90e01 independent internal DNS source.
3. 1e3afc478fb72b54a25a0147910463f060fee88f tests/docs.

Full diff13paths/733adds4deletes. Reviewer inspected fullseries/range-diff:
only hostmetadata+commitbody changes; DNS/tests patch-equivalent. No obsolete
hostfixup/abandoned/transitional/redundant intermediate history remains.
Original40411/reviewede4/runtime8d refs retained; no nonancestor literalmerge/
deployment claim, historical source consumptionunknown and no featuredeployment.
**No database/schema migrations or repeated dependency/channel/input/generated
update streams.** Persistedpaths/stateVersion unchanged, no CentOS conversion,
already-upstream cachepatch absent. Prior fullreview and directtestfix conclusions
remain valid for unchanged content.

After actualpublication/comparison proof, run native exactfive-system pattern:
cz.vpsfree/containers/{mx2,brq/int.ns1,prg/int.ns1,prg/int.mon1,prg/int.mon2}.
Inventoryexactfive/semanticFNM_EXTGLOB verified; no toolchange. Freshutility or
already documented parentfallback, retain finalsource/graph/drv/output/results.
Currenteval is not buildsuccess. No defaultintegration/deployment/primarymail/
DNSreload/sessionlifecycle permission. Realcontainer/recipient/TLS/resolver/
cutover/queue-safe recovery limitations remain.
