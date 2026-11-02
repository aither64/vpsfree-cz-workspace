# Independent final review — automated mx2 verification and internal DNS

Reviewer0 delivered the complete report via report_to_lead; lead records it here
because the retained reviewer is read-only. This report covers the exact reviewed
range below. Later narrow remediation/acceptance belongs in separate state and
implementation receipts, preserving this review's original identities.

## Findings and lead decisions

**Important R1, general/risk:** denied relay is not tested over IPv6. At reviewed
head f3789413, tests/mx2.py:159-173 calls every negative case with default IPv4
source/target. The IPv6 transaction at213-216 only proves delivery. Literal
address checks at145-147 can miss an inadvertently trusted IPv6 subnet. Such a
regression could pass IPv4 denials and positive IPv6 delivery. Parameterize
existing DNS-resolvable unrelated/subdomain denial cases over existing IPv4 and
IPv6 pairs; retain RCPT5xx and empty-queue assertions. No policy/fixture redesign.
Lead accepts and delegates this exact fix; must reconcile before long tests.

**Advisory R2, general:** temporary-primary-error case246-253 only proves a
deferred item. DNS/connect failure could satisfy it, then recovery pass without
observing intended primary4xx. Add queue-ID/recipient-bound evidence of
`450 4.2.0 fixture temporary rejection` before removing the response-map entry.
Lead accepts this focused assertion as worthwhile, no conformance-suite growth.

No Blocking finding. No source correctness, network isolation, DNS scope or
history defect found beyond R1's Important coverage gap. Source head is not yet
cleared for long tests until remediation. Reviewer explicitly says focused
checks/direct lead inspection under skillstep9 suffice for these narrow fixes;
no automatic full final-review rerun is needed. Broader behavior or fixture
changes would require affected-lane review.

## Reviewer identity, risk and reviewed range

Retained reviewer0, thread `01a19caf-15c8-74a2-baf1-6594cf30d117`, saved
`gpt-6.1-sol` / `xhigh` / read_only. Independently verified current/env/binding
for this exact slug/workspace. No override, fallback, nested reviewer or authorship.
Read mandatory skill/all four lane references, applicable workspace/repository
instructions, full source and context. High risk: authorization, firewall,
durable accepted mail, DNS/host behavior and future rollback. General,
architecture/repetition, scope/proportionality and risk/compatibility lanes.

Entire base `c040c14cdbacc07998700b524996a89306188d7f` to head
`f3789413a53bcd12e2352940a0ec3e88009c5d9f`, tree
`0cfad62780eee89d51e17d0b9deba2d1a5738d9a`. Reviewer confirmed merge-base,
clean worktree/full-range whitespace, remote feature and unchanged master.
No build, VM, production access, Git mutation or file write by reviewer.

## Scope and architecture conclusion

New user scope is agent-executed verification with minimal input plus explicitly
approved internal mail-zone source correction to public DNS. Three conventional
VM roles, one50line shared policy, small stdlib SMTP helper, focused driver and
operation guide fit that scope. Full branch13paths/715adds4deletes includes the
original host import. No new framework/registry/compatibility subsystem,
dependency refresh or CI campaign. Postfix/DNS/VM operations use owning tools.
Recorded design/baseline/DNS/implementation milestones explain growth; incomplete
active-time coverage does not support a total-efficiency claim. No optional
subsystem needs removal. Inbound certificate infrastructure, primary policy
exploration, recipient synchronization and actual hosting remain outside phase.

The production host and fixture import the same configs/mx2.nix. Relay/firewall
fixes, exact domains, pinned-default parent-domain exclusion, separate relay
restrictions, modern settings.main and primary-observed size are coherent.
Transport/trust/DNSBL/milter/state paths/stateVersion preserved. No fleet-wide
vpsAdminOS or API/client coordination implied.

## Independent fidelity and isolation conclusions

Reviewer read full Nix/Python/helper and independently compared receipt main.cf,
transport and Postgrey texts to exact nix derivation show values. Only hostname
and seven stated retry/policy settings differ; transport derivation/text equal.
Postgrey units equal after300s-to2s normalization. Enabled firewall permits TCP25
for both families, production keeps unrelated shared-profile allowances. Paths,
restrictions, TLS defaults and missing-milter action shared, no weakened fixture.

Isolation adequate on inspection: restrictNetwork on every guest, no default
gateway/forwarded ports, private VLAN/address set, no-resolv/no-poll/nonforwarding
local catch-all DNS. Pinned QEMU implementation inspected: restrict=on. Production
names resolve only locally and no production IP is bound. Runtime assertions
check routes/resolver/upstreamA/AAAA, negativeDNS and positiveDNSBL. Runtime
isolation still requires the actual test; reviewer did not start it.

Negative unrelated/subdomain names resolve locally, separating relay denial from
NXDOMAIN. Unknown-domain case proves rejection, not independently that a specific
reject_unknown_recipient_domain rule caused it, because relay authorization acts
first. No extra subsystem requested for that nuance.

Coverage otherwise substantive: fresh Postgrey rejection/retry and persisted
state through service/guest restart, policy-service failure, deterministic DNSBL,
missing-milter DATA acceptance, three-domain envelope/Message-ID/subject/body,
IPv6 positive path, accepted queue ID/content across Postfix/same-disk reboot,
recovery/delivery/drain, primary deferral,5xxDSN, selfsigned TLS in Received and
plaintext fallback, EHLO/SIZE. Reboot ultimately verifies content/envelope,
not metadata only; no queue deletion. Wait/runtime bounds explicit. R1 is material
missing security coverage. Fixture does not claim Debian/container equivalence.

## DNS consumer conclusion

Only authorized mail RRsets/SOA change: apex/lists MX pair, missing primaryA/AAAA,
currentmx1/mx2AAAA, serial2026093000-to2026110200. Unrelated split-DNS/mail alias/
existingIPv4/public-zone source preserved. User-designated public evidence retains
time15:44:32UTC/TTLs/querylimits. No internalorg zone added; recursive behavior.
Reviewer inspected zone diff, owning DNS substitution/module and actual imports.
Exactly four consumers: cz.vpsfree/containers/brq/int.ns1,
cz.vpsfree/containers/prg/int.ns1, cz.vpsfree/containers/prg/int.mon1,
cz.vpsfree/containers/prg/int.mon2. BIND/parser/canonical evidence covers allfour.
Source correct in explicit authority; changes future internal mail selection/
IPv6 resolution, including preserved alias. Target builds still required; no
live deployment/propagation. Future source rollback must use higher SOA serial.

## Explicit complete-history and migration conclusions

Reviewed full three-commit series:

1. `36ae652962d0217dd5b22965cd44fd711790d77a`: final host/shared mail policy.
2. `91595bef8847063d76246b292293a687362af420`: independent DNS source correction.
3. `f3789413a53bcd12e2352940a0ec3e88009c5d9f`: tests/docs/flake/README glue.

No obsolete unmerged history, hostfixup or unused transitional path. Corrected
host folded into owning commit; meaningful DNS and tests/docs separate.
Reviewer confirmed pre-consolidation13e0ad185a7254ca3814167d28832d6276b107e0 tree
identical and old655851/new91595 DNS stablepatchID
87bf97c34572a6e79d3635773555be5e77ca9fd1. Full range-diff/provenance inspected.
**No database/schema migrations**, no transitional lineage; persistent paths/
stateVersion retained, no CentOS state conversion. **No repeated dependency/
channel/input/generated update streams**; lock/inputs unchanged. Old cachepatch
already upstream and correctly absent. Exact40411source/e4c1ac0cimport refs kept.
Reviewed import is nonancestor substantive predecessor, not literally merged/
deployed. Historical consumption unknown; no new feature deployment claimed.

## Documentation, inputs and remaining gates

Reviewer checked plan/state/design/packets, primary/DNS/implementation receipts,
range comparisons and old provenance. Opsguide linked fromREADME, explains
reusable command, actual overrides, behavior and recovery/production limits;
run evidence correctly stays in session. No rewrite/expansion requested.

Quick Nix/Python/format/hooks/derivation evaluation recorded passed. Reviewed
identities (evaluation only): testdrv5r61m584nlyrp5gyzq3yjnrc2lxnd2b4 ->
w9x7y16ynljlkpy7j07kjwb1gdm1q7ww-vm-test-run-mx2; productiondrv
qisgvyzw6xhld9p6g89ar5pmv5xiinv2 ->
y7q64g66v8i5hqm7wys1zr0i09aidl2f-nixos-system-mx2-26.05.20261026.718f670.
Full paths and graph in verification-implementation.md. Lockblob
ec3d5aea9a7e55e69778e3ae4136cf2b3bb84e86, SHA256
505f6c89e18972827beecc29a0c7c85e1df2576ed4074205501167a3dd6f326a.
PinnedStable718f670e845328e9c2cecdd832835712b2cbd065,
vpsAdminOSb45b27b4330a08d85f413999e4bf66ba4503eee1,
confctl7bee58a52372b95c2198ce3f2a719807a3c2c66b; complete graph/sourcepaths bound.
None proves realization/runtime. Old import build cannot certify successor.

Next: owner implements R1/R2, focused checks/commit-fold; lead verifies narrowdiff,
updates head/receipts/comparison/publication, then freshwatcher VMcheck+mx2+four
DNSsystem builds. Isolated pass does not clear real recipient/trust/primary
acceptance, inbound certificate, milter scanning/backscatter policy, container/
network/placement, DNS propagation, source identity or cutover/accepted queue
rollback. No deployment/integration/lifecycle approval.
