# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/vps_network_tab_actions.spec.ts >> @pr-smoke VPS network tab >> adds a private IPv4 address from the normal user VPS detail
- Location: e2e/specs/app/vps_network_tab_actions.spec.ts:523:3

# Error details

```
Error: locator.click: Test ended.
Call log:
  - waiting for getByTestId('vps.network.ip_addresses.add')

```

# Test source

```ts
  458 |         },
  459 |         'PUT ip_addresses/1': () => {
  460 |           throw new Error('owner update should be blocked by busy gate');
  461 |         },
  462 |         'POST host_ip_addresses/50/free': () => {
  463 |           throw new Error('host address free should be blocked by busy gate');
  464 |         },
  465 |       },
  466 |     });
  467 | 
  468 |     await page.goto('/admin/vps/123/network');
  469 |     await expect(page.getByTestId('vps.network.page')).toBeVisible();
  470 |     await openAdminNetworkSettings(page);
  471 | 
  472 |     const disable = page.getByTestId('vps.network.disable');
  473 |     await expect(disable).toHaveAttribute('aria-disabled', 'true');
  474 |     await expect(disable).toHaveAttribute('title', 'Operation in progress');
  475 | 
  476 |     await expect(page.getByTestId('vps.network.ip_addresses.item.1.owner')).toHaveAttribute('aria-disabled', 'true');
  477 |     await expect(page.getByTestId('vps.network.ip_addresses.item.1.free_route')).toHaveAttribute('aria-disabled', 'true');
  478 |     await expect(page.getByTestId('vps.network.ip_addresses.unassigned.2.assign')).toHaveAttribute('aria-disabled', 'true');
  479 |     await expect(page.getByTestId('vps.network.host_addresses.row.50.ptr')).toHaveAttribute('aria-disabled', 'true');
  480 |     await expect(page.getByTestId('vps.network.host_addresses.row.50.free')).toHaveAttribute('aria-disabled', 'true');
  481 |     await expect(page.getByTestId('vps.network.host_addresses.row.51.assign')).toHaveAttribute('aria-disabled', 'true');
  482 |     await expect(page.getByTestId('vps.network.host_addresses.row.51.delete')).toHaveAttribute('aria-disabled', 'true');
  483 |   });
  484 | 
  485 |   test('keeps ownership and VPS toggles admin-only while exposing user route management', async ({ page }) => {
  486 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  487 | 
  488 |     await installHaveApiMock(page, {
  489 |       user: { id: 2, login: 'user', level: 1 },
  490 |       handlers: {
  491 |         'GET vpses/123': () => ({ vps }),
  492 |         'GET ip_addresses': () => ({ ip_addresses: ips }),
  493 |         'GET host_ip_addresses': () => ({
  494 |           host_ip_addresses: [
  495 |             {
  496 |               id: 50,
  497 |               addr: '198.51.100.10',
  498 |               assigned: true,
  499 |               reverse_record_value: 'old.example.test.',
  500 |               user_created: true,
  501 |               ip_address: { id: 1, addr: '198.51.100.10' },
  502 |             },
  503 |           ],
  504 |         }),
  505 |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  506 |         'GET network_interfaces': () => ({ network_interfaces: netifs }),
  507 |         'GET network_interface_accountings': () => ({ network_interface_accountings: acct }),
  508 |       },
  509 |     });
  510 | 
  511 |     await page.goto('/app/vps/123/network');
  512 |     await expect(page.getByTestId('vps.network.page')).toBeVisible();
  513 |     await expect(page.getByTestId('vps.network.host_addresses')).toBeVisible();
  514 |     await expect(page.getByTestId('vps.network.host_addresses.row.50.ptr')).toBeVisible();
  515 |     await expect(page.getByTestId('vps.network.ip_addresses.add')).toBeVisible();
  516 |     await expect(page.getByTestId('vps.network.ip_addresses.item.1.owner')).toHaveCount(0);
  517 |     await expect(page.getByTestId('vps.network.ip_addresses.item.1.free_route')).toBeVisible();
  518 |     await expect(page.getByTestId('vps.network.ip_addresses.unassigned.2.assign')).toBeVisible();
  519 |     await expect(page.getByTestId('vps.network.admin_settings')).toHaveCount(0);
  520 |     await expect(page.getByTestId('vps.network.disable')).toHaveCount(0);
  521 |   });
  522 | 
  523 |   test('adds a private IPv4 address from the normal user VPS detail', async ({ page }) => {
  524 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  525 | 
  526 |     const freePrivate = {
  527 |       id: 77,
  528 |       addr: '10.20.30.40',
  529 |       prefix: 32,
  530 |       network_interface: null,
  531 |       user: null,
  532 |       network: { id: 9, role: 'private_access', purpose: 'vps', ip_version: 4 },
  533 |     };
  534 | 
  535 |     await installHaveApiMock(page, {
  536 |       user: { id: 2, login: 'user', level: 1 },
  537 |       handlers: {
  538 |         'GET vpses/123': () => ({ vps: { ...vps, user: { id: 2, login: 'user' } } }),
  539 |         'GET ip_addresses': (ctx) => {
  540 |           if (ctx.searchParams.get('ip_address[role]') === 'private_access') {
  541 |             return { ip_addresses: [freePrivate] };
  542 |           }
  543 |           return { ip_addresses: ips };
  544 |         },
  545 |         'GET host_ip_addresses': () => ({ host_ip_addresses: [] }),
  546 |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  547 |         'GET network_interfaces': () => ({ network_interfaces: netifs }),
  548 |         'GET network_interface_accountings': () => ({ network_interface_accountings: acct }),
  549 |         'POST ip_addresses/77/assign': () => ({
  550 |           ip_address: { ...freePrivate, network_interface: { id: 1 } },
  551 |           _meta: { action_state_id: 1277 },
  552 |         }),
  553 |         'GET action_states/1277': () => ({ action_state: { id: 1277, finished: true, status: true, current: 1, total: 1 } }),
  554 |       },
  555 |     });
  556 | 
  557 |     await page.goto('/app/vps/123/network');
> 558 |     await page.getByTestId('vps.network.ip_addresses.add').click();
      |                                                            ^ Error: locator.click: Test ended.
  559 |     await expect(page.getByTestId('vps.network.ip_addresses.add_modal')).toBeVisible();
  560 |     await page.getByTestId('network.user.assign.kind').selectOption('ipv4_private');
  561 |     await page.getByTestId('network.user.assign.continue').click();
  562 |     await expect(page.getByTestId('network.user.assign.address')).toContainText('10.20.30.40/32');
  563 | 
  564 |     const request = page.waitForRequest(
  565 |       (req) => req.method() === 'POST' && req.url().includes('/api/v7.0/ip_addresses/77/assign')
  566 |     );
  567 |     await page.getByTestId('network.user.assign.submit').click();
  568 |     expect((await request).postDataJSON()).toEqual({
  569 |       ip_address: { network_interface: 1 },
  570 |     });
  571 |   });
  572 | 
  573 |   test('@pr-smoke-mobile creates a route and its default host address in one workflow', async ({ page }) => {
  574 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  575 | 
  576 |     const freeIp = {
  577 |       id: 201,
  578 |       addr: '198.51.100.201',
  579 |       prefix: 32,
  580 |       network_interface: null,
  581 |       user: { id: 2, login: 'user' },
  582 |       network: {
  583 |         id: 21,
  584 |         role: 'public_access',
  585 |         purpose: 'vps',
  586 |         ip_version: 4,
  587 |         primary_location: { id: 10, label: 'Prague' },
  588 |       },
  589 |     };
  590 |     let currentIps: IpAddressFixture[] = [freeIp];
  591 |     let hostAddresses: Array<Record<string, unknown>> = [];
  592 |     let assignPayload: unknown;
  593 | 
  594 |     await installHaveApiMock(page, {
  595 |       user: { id: 2, login: 'user', level: 1 },
  596 |       handlers: {
  597 |         'GET vpses/123': () => ({ vps: { ...vps, user: { id: 2, login: 'user' } } }),
  598 |         'GET ip_addresses': () => ({ ip_addresses: currentIps }),
  599 |         'GET host_ip_addresses': () => ({ host_ip_addresses: hostAddresses }),
  600 |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  601 |         'GET network_interfaces': () => ({ network_interfaces: netifs }),
  602 |         'GET network_interface_accountings': () => ({ network_interface_accountings: acct }),
  603 |         'POST ip_addresses/201/assign_with_host_address': (ctx) => {
  604 |           assignPayload = ctx.request.postDataJSON?.();
  605 |           currentIps = [{ ...freeIp, network_interface: { id: 1, name: 'eth0' }, routed: true }];
  606 |           hostAddresses = [{
  607 |             id: 301,
  608 |             addr: '198.51.100.201',
  609 |             assigned: true,
  610 |             user_created: false,
  611 |             ip_address: { id: 201, addr: '198.51.100.201', network_interface: { id: 1 } },
  612 |           }];
  613 |           return { ip_address: currentIps[0], _meta: { action_state_id: 2201 } };
  614 |         },
  615 |         'GET action_states/2201': () => ({
  616 |           action_state: { id: 2201, finished: true, status: true, current: 1, total: 1 },
  617 |         }),
  618 |       },
  619 |     });
  620 | 
  621 |     await page.goto('/app/vps/123/network');
  622 |     await page.getByTestId('vps.network.ip_addresses.unassigned.201.assign').click();
  623 |     await page.getByTestId('network.user.assign.continue').click();
  624 |     await page.getByTestId('network.user.assign.mode').selectOption('route_host');
  625 |     await page.getByTestId('network.user.assign.submit').click();
  626 | 
  627 |     await expect(page.getByTestId('vps.network.ip_addresses.add_modal')).toBeHidden();
  628 |     await expect.poll(() => assignPayload).toEqual({
  629 |       ip_address: { network_interface: 1 },
  630 |     });
  631 |     await expect(page.getByTestId('vps.network.ip_addresses.item.201')).toBeVisible();
  632 |     await expect(page.getByTestId('vps.network.host_addresses.row.301')).toContainText('198.51.100.201');
  633 |   });
  634 | 
  635 |   test('routes through an eligible host address and reads the selected hop back', async ({ page }) => {
  636 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  637 | 
  638 |     const freeIp = {
  639 |       id: 202,
  640 |       addr: '198.51.100.202',
  641 |       prefix: 32,
  642 |       network_interface: null,
  643 |       user: { id: 2, login: 'user' },
  644 |       network: {
  645 |         id: 22,
  646 |         role: 'public_access',
  647 |         purpose: 'vps',
  648 |         ip_version: 4,
  649 |         primary_location: { id: 10, label: 'Prague' },
  650 |       },
  651 |     };
  652 |     const routeVia = {
  653 |       id: 350,
  654 |       addr: '198.51.100.10',
  655 |       assigned: true,
  656 |       user_created: true,
  657 |       ip_address: { id: 1, addr: '198.51.100.10', network_interface: { id: 1, name: 'eth0' } },
  658 |     };
```