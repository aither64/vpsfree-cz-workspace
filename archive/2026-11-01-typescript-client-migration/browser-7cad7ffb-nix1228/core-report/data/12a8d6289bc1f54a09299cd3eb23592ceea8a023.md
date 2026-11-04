# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: admin/host_ip_addresses_responsive_actions.spec.ts >> @pr-smoke @pr-smoke-mobile rejected host IP deletion stays in context and supports retry
- Location: e2e/specs/admin/host_ip_addresses_responsive_actions.spec.ts:130:1

# Error details

```
Error: expect(locator).toBeHidden() failed

Locator:  getByTestId('admin.host_ip_addresses.delete_confirm')
Expected: hidden
Received: visible
Timeout:  15000ms

Call log:
  - Expect "toBeHidden" with timeout 15000ms
  - waiting for getByTestId('admin.host_ip_addresses.delete_confirm')
    33 × locator resolved to <div role="dialog" tabindex="-1" aria-modal="true" data-overlay="modal" aria-labelledby="_r_a_" data-overlay-surface="overlay" data-testid="admin.host_ip_addresses.delete_confirm" class="relative z-10 flex w-full flex-col overflow-hidden bg-overlay-surface shadow-panel ring-1 ring-border max-h-modal rounded-lg max-w-sm">…</div>
       - unexpected value "visible"

```

```yaml
- dialog "Delete host IP address?":
  - text: Delete host IP address?
  - paragraph: "Delete host address {198.51.100.20} from vpsAdmin."
  - text: Error Missing response namespace
  - button "Cancel"
  - button "Delete"
```

# Test source

```ts
  72  |     clientWidth: element.clientWidth,
  73  |     scrollLeft: element.scrollLeft,
  74  |     scrollWidth: element.scrollWidth,
  75  |   }));
  76  |   expect(metrics.scrollLeft).toBe(0);
  77  |   expect(metrics.scrollWidth).toBeLessThanOrEqual(metrics.clientWidth + 1);
  78  |   const tableDisplay = await tableCard.locator('table').evaluate((element) => getComputedStyle(element).display);
  79  |   expect(tableDisplay).toBe(mobile ? 'block' : 'table');
  80  | 
  81  |   const actions = [
  82  |     { control: page.getByTestId('admin.host_ip_addresses.row.501.ptr'), label: 'PTR' },
  83  |     { control: page.getByTestId('admin.host_ip_addresses.row.501.free'), label: 'Remove' },
  84  |     { control: page.getByTestId('admin.host_ip_addresses.row.502.ptr'), label: 'PTR' },
  85  |     { control: page.getByTestId('admin.host_ip_addresses.row.502.assign'), label: 'Assign' },
  86  |     { control: page.getByTestId('admin.host_ip_addresses.row.502.delete'), label: 'Delete' },
  87  |   ];
  88  | 
  89  |   if (mobile) {
  90  |     for (const label of ['Host IP', 'Route IP', 'Interface', 'VPS', 'User', 'PTR', 'Flags', 'Actions']) {
  91  |       await expect(assignedRow.getByText(label, { exact: true })).toBeVisible();
  92  |     }
  93  | 
  94  |     const viewportWidth = await page.evaluate(() => document.documentElement.clientWidth);
  95  |     for (const { control, label } of actions) {
  96  |       await expect(control).toHaveCount(1);
  97  |       await expect(control).toBeVisible();
  98  |       const generatedLabel = await control.evaluate((element) => getComputedStyle(element, '::after').content);
  99  |       expect(generatedLabel).toContain(label);
  100 |       const box = await control.boundingBox();
  101 |       expect(box).not.toBeNull();
  102 |       expect(box?.height ?? 0).toBeGreaterThanOrEqual(44);
  103 |       expect(box?.x ?? -1).toBeGreaterThanOrEqual(0);
  104 |       expect((box?.x ?? 0) + (box?.width ?? 0)).toBeLessThanOrEqual(viewportWidth);
  105 |     }
  106 |   } else {
  107 |     await expect(tableCard.getByRole('columnheader', { name: 'Host IP' })).toBeVisible();
  108 |     for (const { control } of actions) await expect(control).toHaveText('');
  109 |   }
  110 | 
  111 |   await page.getByTestId('admin.host_ip_addresses.row.501.ptr').click();
  112 |   const ptrDialog = page.getByRole('dialog', { name: 'Set reverse record' });
  113 |   await expect(ptrDialog).toBeVisible();
  114 |   expect(detailRequests).toBe(1);
  115 |   await ptrDialog.getByRole('button', { name: 'Cancel' }).click();
  116 | 
  117 |   await page.getByTestId('admin.host_ip_addresses.row.502.assign').click();
  118 |   const assignDialog = page.getByRole('dialog', { name: 'Assign host IP address' });
  119 |   await expect(assignDialog).toBeVisible();
  120 |   await assignDialog.getByRole('button', { name: 'Cancel' }).click();
  121 | 
  122 |   await page.getByTestId('admin.host_ip_addresses.row.502.delete').click();
  123 |   const deleteDialog = page.getByRole('dialog', { name: 'Delete host IP address?' });
  124 |   await expect(deleteDialog).toBeVisible();
  125 |   await deleteDialog.getByRole('button', { name: 'Cancel' }).click();
  126 | 
  127 |   expect(mutationRequests).toEqual([]);
  128 | });
  129 | 
  130 | test('@pr-smoke @pr-smoke-mobile rejected host IP deletion stays in context and supports retry', async ({ page }) => {
  131 |   await setUiSettingsLocalStorage(page, { language: 'en' });
  132 |   await bootstrapVpsAdminWindow(page, { sessionToken: 'HOST_IP_DELETE_RETRY' });
  133 | 
  134 |   let deleteAttempts = 0;
  135 | 
  136 |   await installHaveApiMock(page, {
  137 |     user: { id: 1, login: 'admin', level: 90 },
  138 |     handlers: {
  139 |       'GET host_ip_addresses': () => ({
  140 |         host_ip_addresses: [{
  141 |           id: 502,
  142 |           addr: '198.51.100.20',
  143 |           assigned: false,
  144 |           user_created: true,
  145 |           ip_address: { id: 302, ip_addr: '198.51.100.20' },
  146 |         }],
  147 |         _meta: { total_count: 1 },
  148 |       }),
  149 |       'DELETE host_ip_addresses/502': () => {
  150 |         deleteAttempts += 1;
  151 |         if (deleteAttempts === 1) {
  152 |           return {
  153 |             status: 409,
  154 |             contentType: 'application/json',
  155 |             body: JSON.stringify({ status: false, message: 'Host address is still assigned', response: null }),
  156 |           };
  157 |         }
  158 |         return { _meta: { action_state_id: 703 } };
  159 |       },
  160 |     },
  161 |   });
  162 | 
  163 |   await page.goto('/admin/networking/host-ip-addresses');
  164 |   await page.getByTestId('admin.host_ip_addresses.row.502.delete').click();
  165 | 
  166 |   const dialog = page.getByTestId('admin.host_ip_addresses.delete_confirm');
  167 |   await dialog.getByTestId('admin.host_ip_addresses.delete_confirm.confirm').click();
  168 |   await expect(page.getByTestId('admin.host_ip_addresses.delete_confirm.error')).toContainText('Host address is still assigned');
  169 |   await expect(dialog).toContainText('198.51.100.20');
  170 | 
  171 |   await dialog.getByTestId('admin.host_ip_addresses.delete_confirm.confirm').click();
> 172 |   await expect(dialog).toBeHidden();
      |                        ^ Error: expect(locator).toBeHidden() failed
  173 |   expect(deleteAttempts).toBe(2);
  174 | });
  175 | 
```