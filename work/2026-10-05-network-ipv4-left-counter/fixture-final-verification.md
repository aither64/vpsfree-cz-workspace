# Verification handoff (2026-10-06)

Implementation, independent review and all four finding corrections are complete.
The published network heads are V be136b6c00f03b85b7a12cc57550b4a1394a94a7,
W e4c49bcdc91b33b7f644a2f125231cb413cf4bf4,
C dd10d88073da3aed6c4512e938abe4374422aab1 and
K 291566b2c0bd43389802f607852fd9a4f8241752. All worktrees are clean.
[Whole-branch inventory](branch-inventory.md), [review packet](review-packet.md)
and [finding dispositions](review-result.md) preserve history and migration
conclusions. Nothing has been merged, deployed or disabled in production.

## Passed checks

- Final V API CI 37485699478 passed all 26 matrix jobs, including core and
  all-plugin foundation jobs. Snapshot: fixture-final-v-api-status4.json.
- The core and full SQL runs passed all 13 concurrency and five Create examples
  at seeds 36954 and 9346. They include disable-before/admit-before, registration
  and parallel same-pool admission. The standard typed TransactionChain fixture
  and complete scoped worker cleanup replaced the faulty manual fixture. The
  historical leak mechanism remains unproven. Evidence:
  fixture-repair-quick2-api-{core,full}.log and zero exit receipts.
- Allocation/batch/continuity checks passed 72 examples with two pre-existing
  pending contracts: remote clone snapshot retention and multi-interface
  migration. Ownership checks passed 14 examples, including all five new root/
  child export endpoint transfer and same-owner continuity cases. Migration
  forward/reverse, API resources, Ruby/PHP formatting and syntax, PHP regressions
  and API/PHP locale health checks also passed; details remain in the review packet.
- W focused unit/DOM verification passed 51 tests across six synthetic files,
  then full ci:quick including four type-check domains. Documentation audit
  passed 68 documents and 71 requirement IDs. Desktop and mobile each passed
  four scoped synthetic browser cases with pinned Nix Chromium. Realistic
  HaveAPI OPTIONS fixtures select PUT and include namespaces/layouts/Boolean
  metadata. Production build passed with a chunk-size warning. Four bilingual
  editor captures were inspected with no overflow observed at those sizes.
  Evidence: post-review3-react-{desktop,mobile,build}.log and zero exit receipts.
  Browser-tested W e00336ccf06fe701116c63623a5d8bf93b201dbb differs from final W
  only in dated evidence prose; app/e2e/scripts/package/flake bytes are identical.
  These synthetic tests do not certify a live API or deployment.
- Exact V VM scenarios network/network-interface-routes-and-host-ips and
  network/export-lifecycle passed, including disabled-pool existing route/host
  and export continuity, removal and re-enable behavior. Evidence:
  post-review4-vm-{routes,export}.log and zero exit receipts. Each used a private
  short /tmp/n6-* state directory after the original long socket path failed
  before feature assertions. Both owned runs completed cleanup.
- All 12 actual configuration channel consumers built successfully at exact C:
  int.api1, int.api2, int.db, int.rabbitmq1-3, int.redis1, int.vpsadmin-webui1,
  int.vpsadmin1, int.webui-dev, int.webui1 and int.webui2. Authoritative aggregate
  post-review-remaining5.exit and post-review4-config-build.exit are 0; every
  post-review-config-HOST.exit is 0. Root tool handle 37524 completed exit 0,
  independently observed by fresh watcher config_final_observation5. No unexpected
  kernel build appeared in inspected logs. Confctl removed earlier full logs
  before copies could be retained; all per-host console summaries remain, plus
  full copies for int.webui1 and int.webui2. Built generations were not activated.
- K static bin/check passed: 60 concepts, 120 variants, 66 Czech/61 English
  references and 120 PNG files. Its five revision records match exact V; existing
  screenshot files were not refreshed.

## Remaining proof and prerequisites

Local vps/migrate-with-data-check was interrupted before VM startup when metadata
requested 24 GiB shared memory against about 22.3 GiB actually free. Its exit 1
records authorized interruption, not a feature assertion failure.
storage/restore-after-reinstall-with-descendants-remote and webui#admin-cluster
were not launched locally. Preserve these exact selectors and their payload,
sentinel/checksum, dataset hierarchy, assigned-IP and disabled-state assertions.

Architect read-only inspection found no supported lower-memory route at unchanged
V. The runner's --test-config requires missing tested-flake testFramework exports
and passes framework data, not VM sizing. Current callers do not expose suiteArgs,
extraModules or bootMemory. No wrapper flake, JSON patch or memory adapter was
introduced. A fresh normal run requires at least 24 GiB effective memory/shared
memory; with default 8 GiB reserves that normally means at least 32 GiB detected
free at startup. Serial scheduling cannot reduce one scenario's three VMs.

Existing integration CI [37485699588](https://github.com/vpsfreecz/vpsadmin/actions/runs/37485699588)
remains in progress at exact V in fixture-final-v-integration-status6.json.
Completed CI can supply this proof only if its selected-test preview includes all
three selectors and logs/results show each executed successfully. A green whole
workflow alone is insufficient. No current-head rerun, cancellation or new CI
wait was launched.

The Czech and English networking/ip-address-list KB bitmaps still need refresh
for the Enabled column. The legacy K helper lacks atomic workspace ownership,
generation validation and workspace-scoped sockets; absence preflight does not
supply those guarantees. No supported capture binding to installed providers was
found. Raw helper startup, copied state and invented ownership records were not
used. Supply a supported owned capture environment or separately authorize the
bounded compatibility work before capture. See [KB impact](kb-impact.md).

Network W CI 37486610216 fails on the proxy-addr 2.0.7 audit finding already in
its main baseline. Its browser-script/production-build jobs and smoke workflow
37486610147 passed, but the audit prevented required quick/unit CI gates. The
separate [dependency PR #20](https://github.com/vpsfreecz/vpsadmin-webui/pull/20)
at a7361bb2912485b61a5a0b1472d51158ac08ec96 passed both production audits,
57 BFF tests, 14 script fixtures, 43 focused unit tests, full quality/type gates,
clean frontend/BFF packages and all three provenance/content checks. Actual
paired package metadata has that full revision and dirty=false; proxy-addr is
2.0.8. Its CI 37494845158 passed; smoke 37494845344 remains in progress in the
latest snapshot. See [maintenance review](proxy-addr-maintenance-review.md).
Network heads and pins do not bundle the patch; proper integration remains a
prerequisite for clearing the network WebUI dependency audit.

Production running revisions, writer inventory, count attribution and the
retirement list remain unverified. Rollout requires schema first, every writer
upgraded before the first disable, then compatible controls. Old API rollback
while pools remain disabled loses enforcement. No coordinated node upgrade is
required. Default integration, production deployment and retirement remain
separate user decisions; the initiative stays active.
