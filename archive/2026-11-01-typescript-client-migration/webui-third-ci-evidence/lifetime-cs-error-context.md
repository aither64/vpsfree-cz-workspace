# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/vps_expiration_reactivation.spec.ts >> @pr-smoke @pr-smoke-mobile expired VPS can be renewed, reactivated and started (cs)
- Location: e2e/specs/app/vps_expiration_reactivation.spec.ts:5:3

# Error details

```
Error: expect(locator).toBeHidden() failed

Locator:  getByTestId('lifetimes.admin.modal')
Expected: hidden
Received: visible
Timeout:  15000ms

Call log:
  - Expect "toBeHidden" with timeout 15000ms
  - waiting for getByTestId('lifetimes.admin.modal')
    33 × locator resolved to <div role="dialog" tabindex="-1" aria-modal="true" data-overlay="modal" aria-labelledby="_r_k_" data-overlay-surface="overlay" data-testid="lifetimes.admin.modal" class="relative z-10 flex w-full flex-col overflow-hidden bg-overlay-surface shadow-panel ring-1 ring-border max-h-modal rounded-lg max-w-3xl">…</div>
       - unexpected value "visible"

```

```yaml
- 'dialog "Upravit životní cyklus: expired-playground-test"':
  - text: "Upravit životní cyklus: expired-playground-test Upraví stav účtu a datum expirace. Odesílají se jen tato pole. Stav"
  - combobox
  - text: Objekt je aktivní a použitelný. Vyprší
  - textbox "RRRR-MM-DD HH:MM:SS": 2026-11-21 09:25:00
  - button "Vymazat"
  - text: Další připomenutí
  - textbox "RRRR-MM-DD HH:MM:SS": 2026-11-01 09:25:00
  - button "Vymazat"
  - text: Důvod
  - textbox
  - text: Zobrazí se v logu stavů. Doporučeno pro dohledatelnost.
  - alert
  - button "Zrušit"
  - button "Uložit"
```

# Test source

```ts
  1   | import { expect, test } from '@playwright/test';
  2   | import { bootstrapVpsAdminWindow, installHaveApiMock, setUiSettingsLocalStorage } from '../../fixtures';
  3   | 
  4   | for (const language of ['cs', 'en'] as const) {
  5   |   test(`@pr-smoke @pr-smoke-mobile expired VPS can be renewed, reactivated and started (${language})`, async ({
  6   |     page,
  7   |     hasTouch,
  8   |   }, testInfo) => {
  9   |     await bootstrapVpsAdminWindow(page);
  10  |     await setUiSettingsLocalStorage(page, { language });
  11  |     const vps = {
  12  |       id: 123,
  13  |       hostname: 'expired-playground-test',
  14  |       object_state: 'suspended',
  15  |       is_running: false,
  16  |       expiration_date: '2026-10-01T00:00:00.000Z',
  17  |       remind_after_date: null as string | null,
  18  |       user: { id: 1, login: 'test' },
  19  |       node: { id: 1, location: { id: 1, label: 'Playground' } },
  20  |     };
  21  |     const writes: Record<string, unknown>[] = [];
  22  |     let starts = 0;
  23  |     await installHaveApiMock(page, {
  24  |       user: { id: 1, login: 'test', level: 99 },
  25  |       handlers: {
  26  |         'GET vpses/123': () => ({ vps }),
  27  |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  28  |         'GET ip_addresses': () => ({ ip_addresses: [] }),
  29  |         'PUT vpses/123': ({ params }) => {
  30  |           const data = params['vps'] as Record<string, unknown>;
  31  |           writes.push(data);
  32  |           // Mirror the real HaveAPI schema: only expiration_date is nullable.
  33  |           if (data['remind_after_date'] === null)
  34  |             return {
  35  |               status: false,
  36  |               message: 'Input parameters are invalid',
  37  |               errors: { remind_after_date: ['cannot be null'] },
  38  |               response: null,
  39  |             };
  40  |           const stateChanging = data['object_state'] && data['object_state'] !== vps.object_state;
  41  |           Object.assign(vps, data);
  42  |           if ('expiration_date' in data && !('remind_after_date' in data)) vps.remind_after_date = null;
  43  |           return { vps, _meta: stateChanging ? { action_state_id: 701 } : {} };
  44  |         },
  45  |         'GET action_states/701': () => ({
  46  |           action_state: { id: 701, status: true, finished: true, current: 1, total: 1 },
  47  |         }),
  48  |         'POST vpses/123/start': () => {
  49  |           expect(vps.object_state).toBe('active');
  50  |           starts++;
  51  |           vps.is_running = true;
  52  |           return { _meta: { action_state_id: 702 } };
  53  |         },
  54  |         'GET action_states/702': () => ({
  55  |           action_state: { id: 702, status: true, finished: true, current: 1, total: 1 },
  56  |         }),
  57  |       },
  58  |     });
  59  |     const open = async () => {
  60  |       await page.goto('/admin/vps/123/lifecycle/lifetime');
  61  |       await page.getByTestId('lifetimes.admin.edit').click();
  62  |     };
  63  |     const save = async () => {
  64  |       const button = page
  65  |         .getByTestId('lifetimes.admin.modal')
  66  |         .getByRole('button', { name: language === 'cs' ? 'Uložit' : 'Save', exact: true });
  67  |       if (hasTouch) await button.tap();
  68  |       else await button.click();
> 69  |       await expect(page.getByTestId('lifetimes.admin.modal')).toBeHidden();
      |                                                               ^ Error: expect(locator).toBeHidden() failed
  70  |     };
  71  |     await open();
  72  |     await page.getByTestId('lifetimes.admin.state').selectOption('active');
  73  |     await page.getByTestId('lifetimes.admin.expiration').fill('2026-11-21 09:25:00');
  74  |     await save();
  75  |     expect(writes[0]).toEqual({
  76  |       object_state: 'active',
  77  |       expiration_date: new Date('2026-11-21T09:25:00').toISOString(),
  78  |     });
  79  |     await page.reload();
  80  |     await expect(page.getByTestId('vps.lifecycle.lifetime')).toContainText(language === 'cs' ? 'Aktivní' : 'Active');
  81  |     await page.screenshot({ path: testInfo.outputPath(`reactivated-${language}.png`), scale: 'css' });
  82  |     await page.goto('/admin/vps/123/lifecycle/start');
  83  |     await page.getByTestId('vps.lifecycle.start.confirm').check();
  84  |     await page.getByTestId('vps.lifecycle.start.submit').click();
  85  |     await expect.poll(() => starts).toBe(1);
  86  |     await open();
  87  |     await page.getByTestId('lifetimes.admin.remind_after').fill('2026-11-01 09:25:00');
  88  |     await save();
  89  |     await open();
  90  |     await page.getByTestId('lifetimes.admin.remind_after.clear').click();
  91  |     await save();
  92  |     expect(writes.at(-1)).toEqual({ expiration_date: vps.expiration_date });
  93  |     expect(vps.remind_after_date).toBeNull();
  94  |     await open();
  95  |     await page.getByTestId('lifetimes.admin.expiration.clear').click();
  96  |     await save();
  97  |     expect(writes.at(-1)).toEqual({ expiration_date: null });
  98  |   });
  99  | }
  100 | 
```