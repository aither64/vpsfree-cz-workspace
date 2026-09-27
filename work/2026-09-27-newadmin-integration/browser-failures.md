# Initial browser failure inventory

Revision `fd290b5ec1b22900e704e8cb990c5ba050af2394`. Command: `npm run e2e:pr`.
Desktop Chromium stage: 378 tests, default 32 workers, 349 passed and 29 failed.
The chained mobile stage did not run. This inventory records failures, not 29
independently confirmed application bugs. See [verification](verification.md)
for investigation and focused follow-up results.

## 1. e2e/specs/admin/cluster_dns_resolvers_smoke.spec.ts:36:3 › @smoke @pr-smoke @pr-smoke-mobile Admin cluster DNS resolvers › lists with the real API contract and removes stale unsupported filters

expect(locator).toBeVisible() failed

Locator: `getByTestId('admin.cluster.dns_resolvers.page')`

## 2. e2e/specs/admin/cluster_dns_tools_smoke.spec.ts:5:1 › @smoke @pr-smoke admin cluster dns tools pages render

expect(locator).toBeVisible() failed

Locator: `getByTestId('admin.cluster.dns_servers.page')`

## 3. e2e/specs/admin/cluster_environments_responsive_actions.spec.ts:10:1 › @pr-smoke @pr-smoke-mobile @smoke-mobile environment actions stay reachable without horizontal scrolling

expect(locator).toBeVisible() failed

Locator: `getByTestId('admin.cluster.environments.row.4')`

## 4. e2e/specs/admin/cluster_networks_filter_contract.spec.ts:5:1 › @pr-smoke @pr-smoke-mobile admin cluster networks use only exact Network.Index filters

expect(locator).toBeVisible() failed

Locator: `getByTestId('admin.cluster.networks.page')`

## 5. e2e/specs/admin/cluster_resource_maintenance.spec.ts:17:1 › @pr-smoke environment and location maintenance lock and unlock with exact payloads and readback

expect(locator).toBeVisible() failed

Locator: `getByTestId('admin.cluster.environments.row.4.maintenance.lock')`

## 6. e2e/specs/admin/cluster_resource_packages_filter_contract.spec.ts:10:3 › Admin resource package filter contract › @pr-smoke @pr-smoke-mobile uses nullable user scope and never sends unsupported filters

expect(locator).toBeVisible() failed

Locator: `getByTestId('admin.cluster.resource_packages.row.21')`

## 7. e2e/specs/admin/dns_tsig_keys_responsive_actions.spec.ts:6:1 › @pr-smoke @pr-smoke-mobile @smoke-mobile admin TSIG key delete stays reachable without horizontal scrolling

expect(locator).toBeVisible() failed

Locator: `getByTestId('admin.cluster.dns_tsig.row.1')`

## 8. e2e/specs/admin/help_boxes_responsive_actions.spec.ts:6:1 › @pr-smoke @pr-smoke-mobile @smoke-mobile admin help-box actions stay reachable on mobile

expect(locator).toBeVisible() failed

Locator: `getByTestId('admin.help_boxes.table').locator('tbody tr').filter({ has: getByTestId('admin.help_boxes.preview.42') })`

## 9. e2e/specs/admin/host_ip_addresses_responsive_actions.spec.ts:5:1 › @pr-smoke @pr-smoke-mobile host IP actions stay reachable without horizontal scrolling

expect(locator).toBeVisible() failed

Locator: `getByTestId('admin.host_ip_addresses.row.501')`

## 10. e2e/specs/admin/ip_address_assignment_exact_filter.spec.ts:20:1 › @pr-smoke @pr-smoke-mobile IP address assignment action opens an exact filtered audit

expect(locator).toBeVisible() failed

Locator: `getByTestId('admin.ip_addresses.row.125.action.assignments')`

## 11. e2e/specs/admin/mail_template_recipient_mobile_actions.spec.ts:47:1 › @pr-smoke @pr-smoke-mobile keeps mail-template recipient actions reachable in narrow content

expect(locator).toBeVisible() failed

Locator: `getByTestId('admin.mailer.templates.detail.recipients.table')`

## 12. e2e/specs/admin/network_detail_responsive_actions.spec.ts:5:1 › @pr-smoke @pr-smoke-mobile network location actions stay reachable without table scrolling

expect(locator).toBeVisible() failed

Locator: `getByTestId('admin.cluster.network_detail.ln.1001')`

## 13. e2e/specs/admin/node_heatmaps.spec.ts:13:5 › @pr-smoke @pr-smoke-mobile heatmaps use legacy configuration and eligibility in cs at /

expect(locator).toBeVisible() failed

Locator: `locator('[data-testid="nodes.heatmap.open.node1.prg.example"]:visible')`

## 14. e2e/specs/admin/node_pool_maintenance.spec.ts:59:1 › @pr-smoke @pr-smoke-mobile admin locks and unlocks a real pool, while inherited maintenance stays read-only

expect(locator).toBeVisible() failed

Locator: `getByTestId('admin.node.storage.pool.11.maintenance.lock')`

## 15. e2e/specs/admin/nodes_filter_contract.spec.ts:41:1 › @pr-smoke @pr-smoke-mobile admin nodes only send filters supported by Node.Index

expect(locator).toBeVisible() failed

Locator: `getByTestId('admin.nodes.page')`

## 16. e2e/specs/admin/orphaned_change_request_owner.spec.ts:55:1 › @workflow-matrix @pr-smoke @pr-smoke-mobile @smoke @smoke-mobile orphaned change requests are historical-only while ownerless registrations stay actionable

expect(locator).toBeVisible() failed

Locator: `locator('[data-testid="admin.requests.row.change.2041"]:visible, [data-testid="admin.requests.mobile.row.change.2041"]:visible')`

## 17. e2e/specs/admin/os_templates_responsive_actions.spec.ts:6:1 › @pr-smoke @pr-smoke-mobile @smoke-mobile admin OS-template actions stay reachable on mobile

expect(locator).toBeVisible() failed

Locator: `getByTestId('admin.cluster.os_templates.table').locator('tbody tr').filter({ has: getByTestId('admin.cluster.os_templates.row.11.edit') })`

## 18. e2e/specs/admin/request_detail_error_recovery.spec.ts:16:1 › @workflow-matrix @pr-smoke @pr-smoke-mobile @smoke admin request detail: retry recovers in place without a mutation or page reload

expect(locator).toBeVisible() failed

Locator: `getByTestId('admin.requests.detail.error')`

## 19. e2e/specs/admin/requests_operations_smoke.spec.ts:210:3 › @workflow-matrix @pr-smoke @pr-smoke-mobile admin requests: address copy and risk emphasis work across breakpoints in en

expect(locator).toHaveAttribute(expected) failed

Locator: `getByTestId('admin.requests.detail.metadata').locator('details')`

## 20. e2e/specs/admin/resource_package_detail_mobile_actions.spec.ts:5:1 › @pr-smoke @pr-smoke-mobile resource package detail actions stay reachable without horizontal scrolling

expect(locator).toBeVisible() failed

Locator: `getByTestId('admin.cluster.resource_package_detail.assign.row.41')`

## 21. e2e/specs/admin/security_advisory_nodes_mobile_actions.spec.ts:27:1 › @pr-smoke @pr-smoke-mobile security advisory node actions stay directly usable on mobile

expect(locator).toBeVisible() failed

Locator: `getByTestId('admin.security_advisories.nodes.panel')`

## 22. e2e/specs/admin/vps_map_mode.spec.ts:24:1 › @pr-smoke @pr-smoke-mobile admin reviews and submits a restart-dependent VPS map-mode change

expect(locator).toBeVisible() failed

Locator: `getByTestId('vps.config.map_mode')`

## 23. e2e/specs/app/admin_network_live_noc.spec.ts:5:1 › @pr-smoke @pr-smoke-mobile admin live network center uses bounded API filters and stops polling

expect(locator).toContainText(expected) failed

Locator: `getByTestId('admin.network_live.filter.vps.opt.5')`

## 24. e2e/specs/app/dns_zone_logs_keyset_pagination.spec.ts:94:3 › DNS zone logs filters and keyset pagination › @pr-smoke @pr-smoke-mobile renders real change badges and keeps pagination inside the viewport

expect(page).toHaveURL(expected) failed

## 25. e2e/specs/app/dns_zones_keyset_pagination.spec.ts:68:3 › DNS zones keyset pagination › @pr-smoke @pr-smoke-mobile @smoke @smoke-mobile navigates to next and previous pages via from_id

expect(page).not.toHaveURL(expected) failed

## 26. e2e/specs/app/incidents_smart_filter.spec.ts:164:3 › Incident reports - exact Smart Filter contract › admin normalizes stale q before the first GET, rejects full text, and retains exact filters across pages @pr-smoke @pr-smoke-mobile

expect(received).toBe(expected) // Object.is equality

## 27. e2e/specs/app/known_devices_keyset_pagination.spec.ts:237:3 › @smoke known-device keyset pagination › @pr-smoke @pr-smoke-mobile admin exact terminal page drops a stale forward edge after forgetting its last device

expect(locator).toBeVisible() failed

Locator: `getByTestId('admin.user.mfa.known_devices.table').getByTestId('admin.user.mfa.known_devices.row.1')`

## 28. e2e/specs/app/user_namespace_filter_contract.spec.ts:271:3 › User namespace index contracts › @pr-smoke @pr-smoke-mobile namespace pagination follows ascending exclusive cursors without overlap or terminal loops

expect(locator).toBeVisible() failed

Locator: `getByTestId('profile.userns.namespaces.row.1')`

## 29. e2e/specs/app/user_namespace_filter_contract.spec.ts:450:3 › User namespace index contracts › @pr-smoke @pr-smoke-mobile an empty map cursor page can return safely through Prev

expect(page).toHaveURL(expected) failed
