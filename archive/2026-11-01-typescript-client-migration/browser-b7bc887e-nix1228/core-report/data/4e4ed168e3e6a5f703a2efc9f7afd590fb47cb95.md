# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/vps_storage_tab_mounts.spec.ts >> @smoke VPS storage tab mounts >> deletes mount via confirm dialog
- Location: e2e/specs/app/vps_storage_tab_mounts.spec.ts:326:3

# Error details

```
Error: expect(locator).toBeHidden() failed

Locator:  getByTestId('vps.storage.mounts.delete_confirm')
Expected: hidden
Received: visible
Timeout:  15000ms

Call log:
  - Expect "toBeHidden" with timeout 15000ms
  - waiting for getByTestId('vps.storage.mounts.delete_confirm')
    33 × locator resolved to <div role="dialog" tabindex="-1" aria-modal="true" data-overlay="modal" aria-labelledby="_r_i_" data-overlay-surface="overlay" data-testid="vps.storage.mounts.delete_confirm" class="relative z-10 flex w-full flex-col overflow-hidden bg-overlay-surface shadow-panel ring-1 ring-border max-h-modal rounded-lg max-w-sm">…</div>
       - unexpected value "visible"

```

```yaml
- dialog "Delete mount":
  - text: Delete mount
  - paragraph: This will remove the mount configuration from the VPS.
  - text: Failed to delete mount Missing response namespace
  - button "Cancel"
  - button "Delete" [disabled]
```

# Test source

```ts
  271 |     await expect(page.getByTestId('vps.storage.root_dataset.metadata')).toContainText('15 GiB');
  272 |     await expect(page.getByTestId('vps.storage.root_dataset.metadata')).toContainText('20 GiB');
  273 |     await expect(page.getByTestId('vps.storage.no_backup_cta_note')).toHaveCount(0);
  274 |     await expect(page.getByTestId('vps.storage.root_dataset.details')).toBeVisible();
  275 |     await expect(page.getByTestId('vps.storage.root_dataset.system_context')).toHaveCount(0);
  276 |     await expect(page.getByTestId('vps.storage.root_dataset.open')).toHaveAttribute('href', '/app/datasets/10');
  277 |     await expect(page.getByTestId('vps.storage.root_dataset.create_subdataset')).toHaveAttribute(
  278 |       'href',
  279 |       '/app/datasets/10?create=subdataset'
  280 |     );
  281 |     await expect(page.getByTestId('vps.storage.root_dataset.snapshots')).toHaveAttribute('href', '/app/datasets/10/snapshots');
  282 |     await expect(page.getByTestId('vps.storage.root_dataset.downloads')).toHaveAttribute('href', '/app/datasets/10/downloads');
  283 |     await expect(page.getByTestId('vps.storage.root_dataset.create_snapshot')).toHaveCount(0);
  284 |     await expect(page.getByTestId('vps.storage.root_dataset.restore')).toHaveCount(0);
  285 |     await expect(page.getByTestId('vps.storage.root_dataset.backup')).toHaveCount(0);
  286 |     await expect(mountItem(page, 1)).toBeVisible();
  287 |     await expect(mountItemControl(page, 1, 'dataset')).toHaveAttribute('href', '/app/datasets/9');
  288 |     await expect(mountItem(page, 1)).toContainText('mounted');
  289 |     await expect(mountItem(page, 1)).toContainText('2026');
  290 |     await expect(page.getByText('Master enabled')).toHaveCount(0);
  291 |     await expect.poll(() => page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
  292 | 
  293 |     await page.getByTestId('vps.storage.mounts.add').click();
  294 |     await expect(page.getByTestId('vps.storage.mounts.create')).toBeVisible();
  295 |     await expect(page.getByTestId('vps.storage.mounts.create.master_enabled')).toHaveCount(0);
  296 | 
  297 |     await page.getByTestId('vps.storage.mounts.create.dataset').fill('tank/data');
  298 |     await page.getByTestId('vps.storage.mounts.create.find_dataset').click();
  299 | 
  300 |     await page.getByTestId('vps.storage.mounts.create.mountpoint').fill('/mnt/data');
  301 | 
  302 |     const reqPromise = page.waitForRequest(
  303 |       (r) => r.method() === 'POST' && r.url().includes('/api/v7.0/vpses/123/mounts')
  304 |     );
  305 | 
  306 |     await page.getByTestId('vps.storage.mounts.create.submit').click();
  307 | 
  308 |     const req = await reqPromise;
  309 |     expect(req.postDataJSON()).toEqual({
  310 |       mount: {
  311 |         dataset: 10,
  312 |         mountpoint: '/mnt/data',
  313 |         mode: 'rw',
  314 |         on_start_fail: 'ignore',
  315 |         enabled: true,
  316 |       },
  317 |     });
  318 | 
  319 |     await expect(page.getByTestId('vps.storage.mounts.create')).toBeHidden();
  320 |     await expect(page.getByTestId('modal.action_progress')).toBeHidden();
  321 |     await page.getByTestId('tasks.open-button').click();
  322 |     await expect(page.getByTestId('tasks.row.703')).toBeVisible();
  323 |     await expect(mountItem(page, 2)).toBeVisible();
  324 |   });
  325 | 
  326 |   test('deletes mount via confirm dialog', async ({ page }) => {
  327 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  328 | 
  329 |     let mounts = [
  330 |       {
  331 |         id: 1,
  332 |         mountpoint: '/mnt/old',
  333 |         mode: 'ro',
  334 |         enabled: true,
  335 |         on_start_fail: 'ignore',
  336 |         dataset: { id: 9, name: 'tank/old' },
  337 |         created_at: '2026-01-31T00:00:00Z',
  338 |       },
  339 |     ];
  340 | 
  341 |     await installHaveApiMock(page, {
  342 |       user: { id: 1, login: 'user', level: 1 },
  343 |       handlers: {
  344 |         'GET vpses/123': () => ({ vps }),
  345 |         'GET ip_addresses': () => ({ ip_addresses: [] }),
  346 |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  347 |         'GET vpses/123/mounts': () => ({ mounts }),
  348 |         'DELETE vpses/123/mounts/1': () => {
  349 |           mounts = mounts.filter((m) => m.id !== 1);
  350 |           return { _meta: { action_state_id: 704 } };
  351 |         },
  352 |       },
  353 |     });
  354 | 
  355 |     await page.goto('/app/vps/123/storage');
  356 | 
  357 |     await expect(mountItem(page, 1)).toBeVisible();
  358 | 
  359 |     await mountItemControl(page, 1, 'delete').click();
  360 |     await expect(page.getByTestId('vps.storage.mounts.delete_confirm')).toBeVisible();
  361 |     await expect(page.getByTestId('vps.storage.mounts.delete_confirm.confirm')).toBeEnabled();
  362 | 
  363 |     const reqPromise = page.waitForRequest(
  364 |       (r) => r.method() === 'DELETE' && r.url().includes('/api/v7.0/vpses/123/mounts/1')
  365 |     );
  366 | 
  367 |     await page.getByTestId('vps.storage.mounts.delete_confirm.confirm').click();
  368 | 
  369 |     await reqPromise;
  370 | 
> 371 |     await expect(page.getByTestId('vps.storage.mounts.delete_confirm')).toBeHidden();
      |                                                                         ^ Error: expect(locator).toBeHidden() failed
  372 |   });
  373 | 
  374 |   test('shows admin-only mount controls to admins', async ({ page }) => {
  375 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  376 | 
  377 |     await installHaveApiMock(page, {
  378 |       user: { id: 1, login: 'admin', level: 99 },
  379 |       handlers: {
  380 |         'GET vpses/123': () => ({ vps }),
  381 |         'GET datasets/10': () => ({ dataset }),
  382 |         'GET ip_addresses': () => ({ ip_addresses: [] }),
  383 |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  384 |         'GET vpses/123/mounts': () => ({
  385 |           mounts: [
  386 |             {
  387 |               id: 1,
  388 |               mountpoint: '/mnt/old',
  389 |                     mode: 'ro',
  390 |               enabled: true,
  391 |               master_enabled: false,
  392 |               on_start_fail: 'ignore',
  393 |                     current_state: 'mounted',
  394 |               dataset: { id: 9, name: 'tank/old' },
  395 |               created_at: '2026-01-31T00:00:00Z',
  396 |             },
  397 |           ],
  398 |         }),
  399 |       },
  400 |     });
  401 | 
  402 |     await page.goto('/admin/vps/123/storage');
  403 | 
  404 |     await expect(page.getByTestId('vps.storage.root_dataset.open')).toHaveAttribute('href', '/admin/datasets/10');
  405 |     await expect(page.getByTestId('vps.storage.root_dataset.system_context')).toContainText('3 snapshots');
  406 |     await expect(page.getByTestId('vps.storage.mounts.table')).toContainText('Master');
  407 |     await expect(mountItem(page, 1)).toContainText('No');
  408 | 
  409 |     await page.getByTestId('vps.storage.mounts.add').click();
  410 |     await expect(page.getByTestId('vps.storage.mounts.create.master_enabled')).toHaveCount(0);
  411 |   });
  412 | 
  413 |   test('keeps mounts visible and explains missing root dataset references', async ({ page }) => {
  414 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  415 | 
  416 |     const vpsWithoutDataset = {
  417 |       ...vps,
  418 |       dataset: null,
  419 |     };
  420 | 
  421 |     await installHaveApiMock(page, {
  422 |       user: { id: 1, login: 'user', level: 1 },
  423 |       handlers: {
  424 |         'GET vpses/123': () => ({ vps: vpsWithoutDataset }),
  425 |         'GET ip_addresses': () => ({ ip_addresses: [] }),
  426 |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  427 |         'GET vpses/123/mounts': () => ({
  428 |           mounts: [
  429 |             {
  430 |               id: 1,
  431 |               mountpoint: '/mnt/old',
  432 |                     mode: 'ro',
  433 |               enabled: true,
  434 |               on_start_fail: 'ignore',
  435 |                     current_state: 'mounted',
  436 |               dataset: { id: 9, name: 'tank/old' },
  437 |               created_at: '2026-01-31T00:00:00Z',
  438 |             },
  439 |           ],
  440 |         }),
  441 |       },
  442 |     });
  443 | 
  444 |     await page.goto('/app/vps/123/storage');
  445 | 
  446 |     await expect(page.getByTestId('vps.storage.root_dataset.empty')).toBeVisible();
  447 |     await expect(page.getByTestId('vps.storage.root_dataset.empty')).toContainText('No root dataset reference');
  448 |     await expect(page.getByTestId('vps.storage.root_dataset.open')).toHaveCount(0);
  449 |     await expect(mountItem(page, 1)).toBeVisible();
  450 |     await expect(mountItemControl(page, 1, 'dataset')).toHaveAttribute('href', '/app/datasets/9');
  451 |   });
  452 | });
  453 | 
```