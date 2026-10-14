# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: admin/network_availability.spec.ts >> @pr-smoke @pr-smoke-mobile network availability retains service context and rejected drafts (cs)
- Location: e2e/specs/admin/network_availability.spec.ts:6:3

# Error details

```
Error: expect(locator).toContainText(expected) failed

Locator: getByTestId('admin.cluster.networks.editor')
Expected substring: "Stávající provoz pokračuje"
Received string:    "Upravit síťOpatrné úpravyZměna adresy/prefixu nebo split nastavení může ovlivnit konektivitu existujících VPS. Před uložením vše zkontroluj.192.0.2.0/24 (#101) · Přiřazeno: 3 · Vlastněno: 5PopisekVerze IPIPv4IPv6RoleVeřejnáPrivátníAdresaPrefixÚčelLibovolnýVPSExportPřístup ke splituBez přístupuRozdělit podle uživateleRozdělit podle vlastníkaPrefix splituPokud je split povolený, tento prefix se používá pro split podsítě.Spravováno vpsAdminemPokud je povoleno, vpsAdmin vede inventář IP adres v této síti.ZrušitUložit"
Timeout: 15000ms

Call log:
  - Expect "toContainText" with timeout 15000ms
  - waiting for getByTestId('admin.cluster.networks.editor')
    33 × locator resolved to <div role="dialog" tabindex="-1" aria-modal="true" data-overlay="modal" aria-labelledby="_r_f_" data-overlay-surface="overlay" data-testid="admin.cluster.networks.editor" class="relative z-10 flex w-full flex-col overflow-hidden bg-overlay-surface shadow-panel ring-1 ring-border max-h-modal rounded-lg max-w-xl">…</div>
       - unexpected value "Upravit síťOpatrné úpravyZměna adresy/prefixu nebo split nastavení může ovlivnit konektivitu existujících VPS. Před uložením vše zkontroluj.192.0.2.0/24 (#101) · Přiřazeno: 3 · Vlastněno: 5PopisekVerze IPIPv4IPv6RoleVeřejnáPrivátníAdresaPrefixÚčelLibovolnýVPSExportPřístup ke splituBez přístupuRozdělit podle uživateleRozdělit podle vlastníkaPrefix splituPokud je split povolený, tento prefix se používá pro split podsítě.Spravováno vpsAdminemPokud je povoleno, vpsAdmin vede inventář IP adres v této síti.ZrušitUložit"

```

```yaml
- dialog "Upravit síť":
  - text: "Upravit síť Opatrné úpravy Změna adresy/prefixu nebo split nastavení může ovlivnit konektivitu existujících VPS. Před uložením vše zkontroluj. 192.0.2.0/24 (#101) · Přiřazeno: 3 · Vlastněno: 5 Popisek"
  - textbox: Retained service
  - text: Verze IP
  - combobox:
    - option "IPv4" [selected]
    - option "IPv6"
  - text: Role
  - combobox:
    - option "Veřejná" [selected]
    - option "Privátní"
  - text: Adresa
  - textbox: 192.0.2.0
  - text: Prefix
  - textbox: "24"
  - text: Účel
  - combobox:
    - option "Libovolný"
    - option "VPS" [selected]
    - option "Export"
  - text: Přístup ke splitu
  - combobox:
    - option "Bez přístupu" [selected]
    - option "Rozdělit podle uživatele"
    - option "Rozdělit podle vlastníka"
  - text: Prefix splitu Pokud je split povolený, tento prefix se používá pro split podsítě.
  - textbox: "32"
  - checkbox "Spravováno vpsAdminem Pokud je povoleno, vpsAdmin vede inventář IP adres v této síti." [checked]
  - text: Spravováno vpsAdminem Pokud je povoleno, vpsAdmin vede inventář IP adres v této síti.
  - button "Zrušit"
  - button "Uložit"
```

# Test source

```ts
  1   | import { expect, test } from '@playwright/test';
  2   | 
  3   | import { bootstrapVpsAdminWindow, installHaveApiMock, setUiSettingsLocalStorage } from '../../fixtures';
  4   | 
  5   | for (const language of ['en', 'cs'] as const) {
  6   |   test(`@pr-smoke @pr-smoke-mobile network availability retains service context and rejected drafts (${language})`, async ({ page }, testInfo) => {
  7   |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  8   |     await setUiSettingsLocalStorage(page, { language });
  9   |     let enabled = true;
  10  |     let rejectNext = true;
  11  |     const writes: boolean[] = [];
  12  |     const network = () => ({
  13  |       id: 101, label: 'Retained service', address: '192.0.2.0', prefix: 24,
  14  |       ip_version: 4, role: 'public_access', purpose: 'vps', managed: true,
  15  |       enabled, split_access: 'no_access', split_prefix: 32, assigned: 3, owned: 5,
  16  |     });
  17  |     await installHaveApiMock(page, {
  18  |       user: { id: 1, login: 'admin', level: 100 },
  19  |       handlers: {
  20  |         'GET locations': () => ({ locations: [] }),
  21  |         'GET networks': () => ({ networks: [network()] }),
  22  |         'OPTIONS networks/101': () => ({ input: { parameters: { enabled: {} } } }),
  23  |         'PUT networks/101': (ctx) => {
  24  |           const input = ctx.reqJson as { network: { enabled: boolean } };
  25  |           expect(typeof input.network.enabled).toBe('boolean');
  26  |           writes.push(input.network.enabled);
  27  |           if (rejectNext) {
  28  |             rejectNext = false;
  29  |             return { status: false, message: 'Allocation policy rejected', response: null };
  30  |           }
  31  |           enabled = input.network.enabled;
  32  |           return { network: network() };
  33  |         },
  34  |       },
  35  |     });
  36  |     await page.goto('/admin/cluster/networks');
  37  |     await page.getByTestId('admin.cluster.networks.row.101.edit').click();
  38  |     const editor = page.getByTestId('admin.cluster.networks.editor');
  39  |     const toggle = page.getByTestId('admin.cluster.networks.editor.enabled').getByRole('checkbox');
  40  |     await expect(editor).toContainText('192.0.2.0/24 (#101)');
  41  |     await expect(editor).toContainText(language === 'en' ? 'Assigned: 3' : 'Přiřazeno: 3');
  42  |     await expect(editor).toContainText(language === 'en' ? 'Owned: 5' : 'Vlastněno: 5');
> 43  |     await expect(editor).toContainText(language === 'en' ? 'Existing service continues' : 'Stávající provoz pokračuje');
      |                          ^ Error: expect(locator).toContainText(expected) failed
  44  |     await toggle.uncheck();
  45  |     // Captures show the implemented UI with synthetic API fixtures.
  46  |     await page.screenshot({ path: testInfo.outputPath(`network-availability-${language}.png`), fullPage: true });
  47  |     await page.getByTestId('admin.cluster.networks.editor.save').click();
  48  |     await expect(editor).toContainText('Allocation policy rejected');
  49  |     await expect(toggle).not.toBeChecked();
  50  |     await page.getByTestId('admin.cluster.networks.editor.save').click();
  51  |     await expect(editor).toBeHidden();
  52  |     await expect(page.getByTestId('admin.cluster.networks.row.101.enabled')).toHaveText(language === 'en' ? 'Disabled' : 'Zakázáno');
  53  |     await page.getByTestId('admin.cluster.networks.row.101.edit').click();
  54  |     await toggle.check();
  55  |     await page.getByTestId('admin.cluster.networks.editor.save').click();
  56  |     await expect(editor).toBeHidden();
  57  |     await expect(page.getByTestId('admin.cluster.networks.row.101.enabled')).toHaveText(language === 'en' ? 'Enabled' : 'Povoleno');
  58  |     expect(writes).toEqual([false, false, true]);
  59  |   });
  60  | }
  61  | 
  62  | test('@pr-smoke @pr-smoke-mobile older APIs keep unknown state and omit unsupported availability fields', async ({ page }) => {
  63  |   await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  64  |   await setUiSettingsLocalStorage(page, { language: 'en' });
  65  |   let saved = false;
  66  |   const network = { id: 101, address: '192.0.2.0', prefix: 24, ip_version: 4, role: 'public_access',
  67  |     purpose: 'vps', managed: true, split_access: 'no_access', split_prefix: 32 };
  68  |   await installHaveApiMock(page, {
  69  |     user: { id: 1, login: 'admin', level: 100 },
  70  |     handlers: {
  71  |       'GET locations': () => ({ locations: [] }),
  72  |       'GET networks': () => ({ networks: [network] }),
  73  |       'OPTIONS networks/101': () => ({ input: { parameters: { managed: {} } } }),
  74  |       'PUT networks/101': (ctx) => {
  75  |         expect((ctx.reqJson as { network: object }).network).not.toHaveProperty('enabled');
  76  |         saved = true;
  77  |         return { network };
  78  |       },
  79  |     },
  80  |   });
  81  |   await page.goto('/admin/cluster/networks');
  82  |   await expect(page.getByTestId('admin.cluster.networks.row.101.enabled')).not.toHaveText('Disabled');
  83  |   await page.getByTestId('admin.cluster.networks.row.101.edit').click();
  84  |   await expect(page.getByTestId('admin.cluster.networks.editor.label')).toBeVisible();
  85  |   await expect(page.getByTestId('admin.cluster.networks.editor.enabled')).toHaveCount(0);
  86  |   await page.getByTestId('admin.cluster.networks.editor.save').click();
  87  |   await expect(page.getByTestId('admin.cluster.networks.editor')).toBeHidden();
  88  |   expect(saved).toBe(true);
  89  | });
  90  | 
  91  | test('@pr-smoke @pr-smoke-mobile disabled detached owned addresses stay visible without assignment', async ({ page }) => {
  92  |   await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  93  |   await setUiSettingsLocalStorage(page, { language: 'en' });
  94  |   const ip = { id: 102, addr: '192.0.2.10', prefix: 32, user: { id: 7 },
  95  |     network: { id: 11, enabled: false, ip_version: 4, role: 'public_access', purpose: 'vps' },
  96  |     network_interface: null };
  97  |   await installHaveApiMock(page, {
  98  |     user: { id: 7, login: 'member', level: 1 },
  99  |     handlers: {
  100 |       'GET vpses': () => ({ vpses: [] }),
  101 |       'GET ip_addresses': () => ({ ip_addresses: [ip] }),
  102 |       'GET ip_address_assignments': () => ({ ip_address_assignments: [] }),
  103 |       'GET user_cluster_resources': () => ({ user_cluster_resources: [] }),
  104 |     },
  105 |   });
  106 |   await page.goto('/app/networking');
  107 |   const visible = page.locator('[data-testid="network.user.ip.row.102"]:visible, [data-testid="network.user.ip.card.102"]:visible');
  108 |   await expect(visible).toContainText('192.0.2.10');
  109 |   await expect(visible).toContainText('Disabled');
  110 |   await expect(visible.getByTestId('network.user.ip.102.assign')).toBeDisabled();
  111 | });
  112 | 
```