# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/snapshot_export_shortcut.spec.ts >> @pr-smoke @pr-smoke-mobile snapshot NFS export preserves its source (member)
- Location: e2e/specs/app/snapshot_export_shortcut.spec.ts:7:3

# Error details

```
Error: locator.click: Test ended.
Call log:
  - waiting for getByTestId('dataset.snapshots.row.133.export')

```

# Test source

```ts
  1  | import { expect, test } from '@playwright/test';
  2  | 
  3  | import { bootstrapVpsAdminWindow, installHaveApiMock, setUiSettingsLocalStorage } from '../../fixtures';
  4  | import { expectNoDocumentHorizontalOverflow } from '../../helpers/horizontalOverflow';
  5  | 
  6  | for (const mode of ['member', 'admin'] as const) {
  7  |   test(`@pr-smoke @pr-smoke-mobile snapshot NFS export preserves its source (${mode})`, async ({ page, hasTouch }, testInfo) => {
  8  |     await bootstrapVpsAdminWindow(page);
  9  |     const cs = mode === 'member';
  10 |     await setUiSettingsLocalStorage(page, { language: cs ? 'cs' : 'en', theme: 'dark' });
  11 |     const dataset = {
  12 |       id: 10, name: 'backup-test', full_name: 'tank/backup-test', object_state: 'active',
  13 |       user: { id: 1, login: 'backup-test' }, snapshots_count: 3,
  14 |     };
  15 |     const snapshots = [131, 132, 133].map((id) => ({
  16 |       id, name: `backup-${id}`, label: `Backup ${id}`, created_at: '2026-10-17T09:00:00Z',
  17 |       ...(id === 133 ? { export: { id: 70 } } : {}),
  18 |     }));
  19 |     const writes: Record<string, unknown>[] = [];
  20 |     let pickerLoaded = false;
  21 |     await installHaveApiMock(page, {
  22 |       user: { id: 1, login: 'backup-test', level: cs ? 1 : 99 },
  23 |       handlers: {
  24 |         'GET datasets/10': () => ({ dataset: dataset }),
  25 |         'GET datasets': () => ({ datasets: [dataset], _meta: { total_count: 1 } }),
  26 |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  27 |         'GET exports/70': () => ({ export: { id: 70, dataset, snapshot: snapshots[2], user: dataset.user, enabled: true } }),
  28 |         'GET exports/71': () => ({ export: { id: 71, dataset, snapshot: snapshots[1], user: dataset.user, enabled: true } }),
  29 |         'GET exports/70/hosts': () => ({ hosts: [] }),
  30 |         'GET exports/71/hosts': () => ({ hosts: [] }),
  31 |         'GET datasets/10/snapshots': ({ searchParams }) => {
  32 |           // The selected row is outside the export picker's first 100 results.
  33 |           if (searchParams.get('snapshot[limit]') === '100') {
  34 |             pickerLoaded = true;
  35 |             return { snapshots: [{ id: 1, name: 'unrelated-backup' }] };
  36 |           }
  37 |           return { snapshots, _meta: { total_count: 3 } };
  38 |         },
  39 |         'POST exports': ({ params }) => {
  40 |           writes.push(params);
  41 |           return { export: { id: 71, snapshot: { id: 132 }, dataset } };
  42 |         },
  43 |       },
  44 |     });
  45 |     const base = cs ? '/app' : '/admin';
  46 |     const path = cs ? '/app/backups?tab=snapshots&dataset=10' : '/admin/datasets/10/snapshots';
  47 |     await page.goto(path);
  48 |     const layout = hasTouch ? 'card' : 'row';
  49 |     const action = (id: number) => page.getByTestId(`dataset.snapshots.${layout}.${id}.export`);
  50 |     await expect(action(131)).toBeVisible();
  51 |     await expect(page.getByTestId(`dataset.snapshots.${layout}.131`).getByText('#131', { exact: true })).toHaveCount(1);
  52 |     await expect(action(133)).toHaveAttribute('href', `${base}/exports/70`);
  53 |     await expectNoDocumentHorizontalOverflow(page);
  54 |     await page.screenshot({ path: testInfo.outputPath(`snapshot-actions-${mode}.png`), fullPage: true });
> 55 |     const activate = async (id: number) => hasTouch ? action(id).tap() : action(id).click();
     |                                                                                     ^ Error: locator.click: Test ended.
  56 |     await activate(131);
  57 |     const dialog = page.getByTestId('dataset.exports.create');
  58 |     await expect(dialog).toBeVisible();
  59 |     await expect.poll(() => pickerLoaded).toBe(true);
  60 |     await expect(dialog.getByRole('combobox', { name: cs ? 'Typ zdroje' : 'Source type', exact: true })).toHaveValue('snapshot');
  61 |     await expect(dialog.getByRole('combobox', { name: 'Snapshot', exact: true })).toHaveValue('131');
  62 |     await expect(dialog.getByRole('combobox', { name: 'Snapshot', exact: true })).toBeEnabled();
  63 |     await expect(dialog).toContainText('tank/backup-test');
  64 |     expect(writes).toEqual([]);
  65 |     await expectNoDocumentHorizontalOverflow(page);
  66 |     await page.screenshot({ path: testInfo.outputPath(`snapshot-export-${mode}.png`), fullPage: false });
  67 |     await dialog.getByRole('button', { name: cs ? 'Zrušit' : 'Cancel', exact: true }).click();
  68 |     await expect(dialog).not.toBeVisible();
  69 |     await activate(132);
  70 |     await expect(dialog.getByRole('combobox', { name: 'Snapshot', exact: true })).toHaveValue('132');
  71 |     await expect(page.getByTestId('exports.create.submit')).toBeEnabled();
  72 |     if (hasTouch) await page.getByTestId('exports.create.submit').tap();
  73 |     else await page.getByTestId('exports.create.submit').click();
  74 |     await expect.poll(() => writes.length).toBe(1);
  75 |     expect(writes[0]).toMatchObject({ export: { snapshot: 132 } });
  76 |     expect((writes[0]?.['export'] as Record<string, unknown>)['dataset']).toBeUndefined();
  77 |     await expect(page).toHaveURL(new RegExp(`${base}/exports/71$`));
  78 |     await expect(page.getByTestId('exports.detail.page')).toBeVisible();
  79 |     await page.goto(path);
  80 |     await activate(133);
  81 |     await expect(page).toHaveURL(new RegExp(`${base}/exports/70$`));
  82 |     await expect(page.getByTestId('exports.detail.page')).toBeVisible();
  83 |     expect(writes).toHaveLength(1);
  84 |   });
  85 | }
  86 | 
```