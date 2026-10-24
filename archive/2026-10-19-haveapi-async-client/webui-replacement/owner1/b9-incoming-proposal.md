# Read-only incoming-main adaptation proposal

Candidate WebUI8772bab21cd8739bf4672cdf4976aea2a6e59de3, original base7860521f30826c3886c89c35e8ab6f4e082e0a4b, captured mainb9f47f06e0877eb4a160053c413c4b87dd4a3d55. No fetch, ref/index mutation, rebase, consumer edit or test was performed. Candidate remains clean. This is a proposal only; the obsolete pilot history finding is unresolved and publication does not justify retaining it.

## Six overlapping paths

- WORK_LOG.md: preserve all incoming contributor/node/IP/dashboard/verification/swap/snapshot entries and append the new replacement/historical evidence entries without replacing incoming text.
- docs/design/API_CONTRACTS.md: preserve incoming Admin node overview and maintenance (REQ-028) section; add the production-client contract independently.
- docs/design/REQUIREMENTS.md: preserve incoming acceptance changes (resource swap, node maintenance, verification labels, snapshot export and news navigation); apply only the four client-policy link updates to REQ-007/011/012/059.
- src/lib/api/nodes.test.ts: preserve both new incoming imports, the overview/maintenance test and every existing node case; adapt the added HTTP fixture to the existing controlled XHR seam.
- tsconfig.e2e.json: retain every incoming strict root and add feature public/overview once.
- scripts/fixtures/e2e-type-coverage.json: retain every incoming adoption/deferred removal and add feature public/overview adoption. Do not alter the immutable initial baseline or hashes, gate implementation or compiler flags.

The earlier three-path overlap referred only to the original pilot diff. The completed replacement includes the other three paths; a future reconciliation must handle all six.

## Node source and fixture seam

Main adds five optional Node metric fields, fetchNodeOverview(signal) GET /nodes/overview_list without pagination, and fetchNodeMaintenanceCapability(id) OPTIONS /nodes/:id/set_maintenance?method=POST. Preserve src/lib/api/nodes.ts from main: it is not modified by this feature, and both helpers already call haveApiCall and will naturally use AsyncClient. Keep incoming NodesModel/inventory/maintenance/metric/action components and fixtures unchanged.

Minimal test adaptation of the incoming appended test:

1. Replace vi.stubGlobal('fetch', mockFetchOk(...)) with installHaveApiXhr(mockFetchOk(...)). The feature's existing lastFetchCall already reads apiWire.respond.
2. Preserve exact overview result, pathname and empty search assertions and the capability OPTIONS method + method=POST query assertions.
3. Replace the obsolete RequestInit.signal identity assertion with a real cancellation assertion: abort the supplied controller after the successful overview, call fetchNodeOverview with that same aborted signal, assert AbortError and unchanged apiWire.requests length. Keep the existing feature in-flight XHR abort regression; no fabricated signal property or fetch delegation.

No package/source-policy change is needed. Existing library action-path resolution supports the capability query already used by other passing node capability tests. Incoming nodes_overview_maintenance.spec.ts uses the shared API route fixture; it needs no standalone pilot/bootstrap setup. Its important roles, denied capability, no-replay and exact read-back assertions must remain intact.

## Strict E2E union

Main:67 adopted/198 deferred; feature:61/202. Union is expected68 adopted/197 deferred, subject to the actual compiler/import-closure gate. Seven incoming additions are admin_dashboard, ip_addresses_filters_pagination, ip_addresses_suggested_request_budget, nodes_overview_maintenance, ip_addresses_environment_filter, profile_mfa_recovery and snapshot_export_shortcut. Feature adds public/overview. Preserve exact incoming deferred records for all remaining paths; remove overview's existing deferred entry only.

## Proposed quick and later checks

After an explicitly authorized reconciliation/history candidate exists, run focused nodes.test.ts plus the existing actual-package/core API tests; run upstream NodesModel.test.ts, then app/tooling/E2E strict types and design inventory/audit/diffcheck. Re-running the known39-file API batch is a small quick gate after changed baseline/fixture. Regenerate inventory rather than reusing old counts. No checks have been run for this proposal.

The already-approved nine ordinary browser specs remain the source-adoption selection. The incoming nodes_overview_maintenance browser spec is a useful affected-node check if the lead includes it after final review; this proposal does not expand the current browser authorization. All long app/Nix/browser work remains held until final review/history strategy and explicit release. No minified-browser, merged/default/runtime or lifecycle claim is made.
