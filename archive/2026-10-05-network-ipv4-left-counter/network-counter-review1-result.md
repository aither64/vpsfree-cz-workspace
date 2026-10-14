# Completed inventory whole-branch review

Reviewer0's final report was received on 2026-10-08. This is the lead's
curated account of that report and its dispositions; later working tooltip
changes are excluded. No local CI was run by the reviewer or lead.

## Identity and exact snapshots

Retained reviewer0: read_only, review purpose, gpt-6.1-sol/xhigh,
thread 01a10c52-55c7-7490-8cd9-75efda7f00d9. Exact bound session and live
roster were independently verified. Risk HIGH; GENERAL, architecture/repetition,
scope/proportionality and risk/compatibility were all inspected directly.
No nested reviewer, writes, requests, tests, builds or lifecycle operations.

| Project | Exact merge base | Reviewed head |
| --- | --- | --- |
| V | 81f1f1aabdd18a042d276aa4be3ca32173ff14d0 | cc8e9e7e421a258a46279304c910f88e2ad33147 |
| W | 5d853740a43ddd3ab2b73a976a48367065038f9b | a9d0b5e9402faafef937894f50463da3c27e8935 |
| C | 7e744b49ef90ba39d13b0f82a10a1f4c161c75f3 | 525c02fea0334222020c492c29bd9d8e06d29de9 |
| Original K | 873758fd6aec0c03f50a94600e0ceab97946f255 | 819c4824eddbad89a3b1f797219becd8d33fcc48 |

Actual objects, trees, complete histories, paths and binary diff checksums
match the review packet/inventory. Separate K-runtime/D/E were not recertified.

## Findings and disposition

0 Blocking, 1 Important, 1 Advisory.

- Important / GENERAL: absolute count descriptions in NetworksPage:120 are
  clipped by TableCard's overflow viewport. The reviewer independently viewed
  the hosted EN desktop image. The desktop disabled-IP warning has the same
  source boundary; final-row readable geometry also needs verification.
  Root disposition: implement the accepted shared InventoryDescription owner,
  preserve copy/values/actions, require final-head hosted geometry and manual
  EN/CS desktop/mobile inspection. Pending working bytes are not certified.
- Advisory / GENERAL/risk: Network#ensure_enabled! raises IpAddressInvalid,
  but public IpAddress.Create, Network.AddAddresses and VPS.Update do not
  translate it. HaveAPI 0.29.8 returns generic server_error/500. Rejection
  remains atomic. Root accepts this feedback limitation under skill step 8,
  with source evidence and future HTTP-coverage scope recorded in
  [finding dispositions](network-counter-findings.md).

The earlier accepted shared-OPTIONS timeout Advisory remains: capability
lookup can outlive the caller's twelve-second timer. It affects loading and
progression, not admission enforcement.

## Lane conclusions

Network owns enabled policy and row readers; IpAddress owns the correlated
reservation scope. New statistics count allocation rows, including an IPv6
prefix as one, and remain admin-only even in included Network output. Disabled
available stock is zero; owned-unassigned includes reserved/disabled stock.
Existing count readers and write inputs remain unchanged. PHP's real-client
attributes extraction preserves zero/missing state and safe numeric markup.
React preserves unknown counts, the editor's owned total and false-only flags.

Sorted parent network acquisition, captured candidates and current rechecks
preserve transaction/admission boundaries, including export endpoints during
VPS ownership transfer. Tenant visibility remains the outer Index restriction;
Show and association access remain unchanged. Continuity retains existing
assignments without a new public policy bypass. No new authorization registry,
reservation definition, node protocol, RFC1918 classification or HTTP count
shape was introduced. The original absolute-tooltip repetition is finding 1.

The full branch is proportionate to availability, the separately accepted
Index policy and this inventory refinement. Structural debt changes only the
reviewed UserNetworkPage hash/allowance (691 to 683); historical baseline,
sourceRevision, removal criterion and other 35 entries remain unchanged.
E2E adoption adds precisely the selected availability spec (34 to 35), with
216 deferred and no weakened gate. Dependency files retain current main,
including proxy-addr 2.0.8. Generated adapter inventory is unchanged.

## Complete history and migration conclusion

V's four commits are coherent: API/schema/admission 5b6700dc; legacy UI
bee928bb; separate Index policy da3ae4fe; read-only counters cc8e9e7e.
Original API/Index patches remain equal. W has one owning a9d0b5e commit.
C has canonical V d281a0cd and W 525c02fe streams. K has one five-record
819c4824 pin. No merges, leftover fixups, obsolete unmerged approaches,
repeated pin iterations or unused transitional compatibility paths remain.

V has one feature migration, 20261006120000_add_network_enabled, directly
after 20260914190000_add_node_kernel_evidence_checkpoints. It adds the final
reversible NOT NULL/default-true boolean without stale-schema guards. Migration
and schema bytes remain unchanged versus V5d. The counter needs no migration.
W/C/K: no migrations. Known consumption includes disposable API/VM tests and
the earlier manual development preview. Production merge/release/deployment
or other consumption is not established; external absence is not inferred.

C changes only V/W locked revision/hash/time; every unrelated current-base
node, edge and follows remains exact, including devWorkspace and OS staging.
W follows V in C. K's five revision records and metadata agree on Vcc.
Pages, fingerprints, fixtures, scenarios and PNGs remain unchanged.

## Evidence and limits

Native V API37751585267 has all26 topics plus aggregate success. Full/core
network236 and ip-ownership117 agree on IDs/statuses with zero failures,
pending or outside errors; all four counter cases pass in both modes.
Foundation1432 has zero failures/outside errors, three known full pending
and 52 core pending (49 documented plugin exclusions). Effective lock hashes
agree in the inspected modes. Exact-head PHP/locales/lint/migration checks pass.
Root additionally records PHP107/602 and one unnamed deprecation; it is not
suppressed or independently attributed by the current log.

W CI37752175357 passes the required quick/suites/build; affected unit cases
are 12 network-page, 8 IP-inventory, 4 adapter. Smoke37752175398 passes all
three projects. One unrelated mobile-chrome route-focus retry remains in the
native log. Passing visibility assertions do not prove readable geometry.
K Check37752912755 passes contracts/fixture suites and existing 60-concept,
120-variant, 120-PNG inventory; allow-missing and unchanged bytes do not prove
freshness. Earlier receipts keep their original revisions.

Both CS/EN networking/ip-address-list PNGs remain pending genuine capture,
allowlisted export, strict validation and independent visual/artifact review.
Synthetic browser/template evidence is not live API/guest/deployment proof.
No production writer/revision inventory, retirement, default integration,
KB production write or preview refresh is certified. Rollout remains schema
first, every allocation writer before disable, then compatible UI/discovery.
UI rollback preserves enforcement; old writer/schema rollback needs operator
resolution while disabled pools exist. No coordinated node update is required.

The Important finding prevents readiness until correction or explicit decision.
The shared portal component is new behavior beyond the originally inspected
absolute hints: final committed affected GENERAL/architecture/scope review will
follow hosted quick evidence, retaining the unchanged whole-branch conclusions.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/
