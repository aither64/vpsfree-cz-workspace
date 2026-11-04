# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/snapshot_delete_availability.spec.ts >> @pr-smoke @pr-smoke-mobile cs member cannot delete VPS snapshots from detail or Backup Center
- Location: e2e/specs/app/snapshot_delete_availability.spec.ts:87:5

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: locator('[data-testid="dataset.snapshots.row.200.rollback"]:visible, [data-testid="dataset.snapshots.card.200.rollback"]:visible')
Expected: visible
Error: element(s) not found

Call log:
  - Expect "toBeVisible" with timeout 15000ms
  - waiting for locator('[data-testid="dataset.snapshots.row.200.rollback"]:visible, [data-testid="dataset.snapshots.card.200.rollback"]:visible')

```

# Test source

```ts
  1   | import { expect, test, type Page } from '@playwright/test';
  2   | import { bootstrapVpsAdminWindow, installHaveApiMock, setUiSettingsLocalStorage } from '../../fixtures';
  3   | 
  4   | function action(page: Page, name: string, id = 200) {
  5   |   return page.locator(
  6   |     `[data-testid="dataset.snapshots.row.${id}.${name}"]:visible, [data-testid="dataset.snapshots.card.${id}.${name}"]:visible`
  7   |   );
  8   | }
  9   | 
  10  | async function setup(
  11  |   page: Page,
  12  |   options: { language?: 'cs' | 'en'; admin?: boolean; vps?: boolean; backups?: boolean; references?: boolean } = {}
  13  | ) {
  14  |   await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  15  |   await setUiSettingsLocalStorage(page, { language: options.language ?? 'en', theme: 'dark' });
  16  |   const state = {
  17  |     backups: options.backups ?? false,
  18  |     probeError: false,
  19  |     wrongTarget: false,
  20  |     rejection: '',
  21  |     deleted: false,
  22  |   };
  23  |   const deletes: string[] = [];
  24  |   const probes: string[] = [];
  25  |   const dataset = {
  26  |     id: 10,
  27  |     name: 'sample-storage',
  28  |     full_name: 'sample-storage',
  29  |     user: { id: 2, login: 'sample-member' },
  30  |     object_state: 'active',
  31  |     vps: options.vps ? { id: 300, hostname: 'sample.example' } : null,
  32  |   };
  33  |   await installHaveApiMock(page, {
  34  |     user: { id: 2, login: 'sample-member', level: options.admin ? 100 : 1 },
  35  |     handlers: {
  36  |       'GET datasets/10': () => ({ dataset }),
  37  |       'GET datasets/11': () => ({ dataset: { ...dataset, id: 11, name: 'other-storage' } }),
  38  |       'GET transaction_chains': () => ({ transaction_chains: [] }),
  39  |       'GET datasets': ({ searchParams }) => {
  40  |         const role = searchParams.get('dataset[role]');
  41  |         if (role === 'backup' || role === 'primary') {
  42  |           probes.push(role);
  43  |           expect(searchParams.get('dataset[dataset]')).toBe('10');
  44  |           expect(searchParams.get('dataset[to_depth]')).toBe('0');
  45  |           expect(searchParams.get('dataset[limit]')).toBe('1');
  46  |           expect(searchParams.has('dataset[subtree]')).toBe(false);
  47  |           if (state.probeError) return { status: false, message: 'Read unavailable' };
  48  |           if (state.wrongTarget) return { datasets: [{ ...dataset, id: 999 }] };
  49  |           return { datasets: role === 'primary' ? (options.vps ? [] : [dataset]) : state.backups ? [dataset] : [] };
  50  |         }
  51  |         return { datasets: [dataset] };
  52  |       },
  53  |       'GET datasets/10/snapshots': () => ({
  54  |         snapshots: state.deleted
  55  |           ? []
  56  |           : [
  57  |               { id: 200, name: 'Before update', created_at: '2026-10-26T12:00:00Z' },
  58  |               ...(options.references
  59  |                 ? [
  60  |                     { id: 201, name: 'Mounted snapshot', mount: { id: 30 } },
  61  |                     { id: 202, name: 'Exported snapshot', export: { id: 31 } },
  62  |                   ]
  63  |                 : []),
  64  |             ],
  65  |       }),
  66  |       'GET datasets/11/snapshots': () => ({ snapshots: [{ id: 201, name: 'Other snapshot' }] }),
  67  |       'GET snapshot_downloads': () => ({ snapshot_downloads: [] }),
  68  |       'DELETE datasets/10/snapshots/200': ({ request }) => {
  69  |         deletes.push(request.pathname);
  70  |         if (state.rejection) {
  71  |           state.backups = state.rejection.includes('with backups');
  72  |           return { status: false, message: state.rejection };
  73  |         }
  74  |         state.deleted = true;
  75  |         return { snapshot: {}, _meta: { action_state_id: 801 } };
  76  |       },
  77  |       'GET action_states/801': () => ({
  78  |         action_state: { id: 801, finished: true, status: true, current: 1, total: 1 },
  79  |       }),
  80  |     },
  81  |   });
  82  |   return { state, deletes, probes };
  83  | }
  84  | 
  85  | for (const language of ['cs', 'en'] as const)
  86  |   for (const admin of [false, true]) {
  87  |     test(`@pr-smoke @pr-smoke-mobile ${language} ${admin ? 'admin' : 'member'} cannot delete VPS snapshots from detail or Backup Center`, async ({
  88  |       page,
  89  |     }, info) => {
  90  |       const { deletes, probes } = await setup(page, { language, admin, vps: true });
  91  |       const base = admin ? '/admin' : '/app';
  92  |       for (const path of [`${base}/datasets/10/snapshots`, `/app/backups?tab=snapshots&dataset=10`]) {
  93  |         await page.goto(path);
> 94  |         await expect(action(page, 'rollback')).toBeVisible();
      |                                                ^ Error: expect(locator).toBeVisible() failed
  95  |         await expect(page.getByTestId('dataset.snapshots.deletion.notice')).toContainText(
  96  |           language === 'cs' ? 'Snapshoty VPS' : 'VPS snapshots'
  97  |         );
  98  |         await expect(action(page, 'delete')).toHaveCount(0);
  99  |         await expect(action(page, 'download')).toBeVisible();
  100 |         await expect(action(page, 'export')).toBeVisible();
  101 |         expect(deletes).toEqual([]);
  102 |         expect(probes).toEqual([]);
  103 |       }
  104 |       if (language === 'cs' && admin)
  105 |         await page.screenshot({ path: info.outputPath('vps-snapshots.png'), fullPage: true, scale: 'css' });
  106 |       expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
  107 |     });
  108 |     test(`@pr-smoke @pr-smoke-mobile ${language} ${admin ? 'admin' : 'member'} can delete an unreferenced NAS snapshot after review`, async ({
  109 |       page,
  110 |     }, info) => {
  111 |       const { deletes, probes } = await setup(page, { language, admin, references: true });
  112 |       await page.goto(`${admin ? '/admin' : '/app'}/nas/10/snapshots`);
  113 |       await expect(action(page, 'delete')).toBeEnabled();
  114 |       await expect(action(page, 'delete', 201)).toHaveCount(0);
  115 |       await expect(action(page, 'delete', 202)).toHaveCount(0);
  116 |       await action(page, 'delete').click();
  117 |       await expect(page.getByTestId('dataset.snapshots.delete_confirm')).toContainText('Before update');
  118 |       expect(deletes).toEqual([]);
  119 |       await page.getByTestId('dataset.snapshots.delete_confirm.cancel').click();
  120 |       expect(deletes).toEqual([]);
  121 |       await action(page, 'delete').click();
  122 |       if (language === 'cs' && admin)
  123 |         await page.screenshot({ path: info.outputPath('nas-delete-review.png'), scale: 'css' });
  124 |       const checksBeforeDelete = probes.filter((role) => role === 'backup').length;
  125 |       await page.getByTestId('dataset.snapshots.delete_confirm.confirm').click();
  126 |       await expect(page.getByTestId('dataset.snapshots.delete_confirm')).toBeHidden();
  127 |       expect(deletes).toHaveLength(1);
  128 |       expect(deletes[0]).toMatch(/\/datasets\/10\/snapshots\/200$/);
  129 |       expect(probes.filter((role) => role === 'backup').length).toBeGreaterThan(checksBeforeDelete);
  130 |     });
  131 |   }
  132 | 
  133 | test('@pr-smoke @pr-smoke-mobile NAS backups and failed or unscoped reads never offer Delete; retry restores availability', async ({
  134 |   page,
  135 | }) => {
  136 |   const { state, deletes } = await setup(page, { backups: true });
  137 |   await page.goto('/app/nas/10/snapshots');
  138 |   await expect(page.getByTestId('dataset.snapshots.deletion.notice')).toContainText('backup copies');
  139 |   await expect(action(page, 'delete')).toHaveCount(0);
  140 |   state.backups = false;
  141 |   state.probeError = true;
  142 |   await page.reload();
  143 |   await expect(page.getByTestId('dataset.snapshots.deletion.retry')).toBeVisible();
  144 |   await expect(action(page, 'delete')).toHaveCount(0);
  145 |   state.probeError = false;
  146 |   state.wrongTarget = true;
  147 |   await page.getByTestId('dataset.snapshots.deletion.retry').click();
  148 |   await expect(page.getByTestId('dataset.snapshots.deletion.retry')).toBeVisible();
  149 |   await expect(action(page, 'delete')).toHaveCount(0);
  150 |   state.wrongTarget = false;
  151 |   await page.getByTestId('dataset.snapshots.deletion.retry').click();
  152 |   await expect(action(page, 'delete')).toBeEnabled();
  153 |   expect(deletes).toEqual([]);
  154 | });
  155 | 
  156 | test('@pr-smoke @pr-smoke-mobile rechecks backup membership immediately before deletion', async ({ page }) => {
  157 |   const { state, deletes } = await setup(page);
  158 |   await page.goto('/app/nas/10/snapshots');
  159 |   await action(page, 'delete').click();
  160 |   state.backups = true;
  161 |   await page.getByTestId('dataset.snapshots.delete_confirm.confirm').click();
  162 |   await expect(page.getByTestId('dataset.snapshots.delete_confirm')).toContainText('backup copies');
  163 |   expect(deletes).toEqual([]);
  164 |   await page.getByTestId('dataset.snapshots.delete_confirm.cancel').click();
  165 |   await expect(action(page, 'delete')).toHaveCount(0);
  166 | });
  167 | 
  168 | for (const language of ['cs', 'en'] as const)
  169 |   for (const message of [
  170 |     'cannot destroy snapshot with backups',
  171 |     'this snapshot cannot be destroyed as others are depending on it',
  172 |   ]) {
  173 |     test(`@pr-smoke @pr-smoke-mobile ${language} explains the final API rejection: ${message}`, async ({
  174 |       page,
  175 |     }, info) => {
  176 |       const { state, deletes } = await setup(page, { language });
  177 |       await page.goto('/app/nas/10/snapshots');
  178 |       await action(page, 'delete').click();
  179 |       state.rejection = message;
  180 |       await page.getByTestId('dataset.snapshots.delete_confirm.confirm').click();
  181 |       const dialog = page.getByTestId('dataset.snapshots.delete_confirm');
  182 |       await expect(dialog).toContainText(language === 'cs' ? 'nelze' : 'cannot be deleted');
  183 |       await expect(dialog).not.toContainText('HaveApiError');
  184 |       await expect(dialog).not.toContainText(message);
  185 |       expect(deletes).toHaveLength(1);
  186 |       if (language === 'cs' && message.includes('with backups'))
  187 |         await page.screenshot({ path: info.outputPath('rejection.png'), scale: 'css' });
  188 |       await page.getByTestId('dataset.snapshots.delete_confirm.cancel').click();
  189 |       await expect(action(page, 'delete')).toHaveCount(0);
  190 |     });
  191 |   }
  192 | 
```