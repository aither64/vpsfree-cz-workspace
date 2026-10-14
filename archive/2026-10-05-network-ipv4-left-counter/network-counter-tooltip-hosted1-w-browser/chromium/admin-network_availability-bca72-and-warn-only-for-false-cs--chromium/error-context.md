# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: admin/network_availability.spec.ts >> @pr-smoke @pr-smoke-mobile admin IP flags preserve disabled assignments and warn only for false (cs)
- Location: e2e/specs/admin/network_availability.spec.ts:247:3

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator:  locator('#admin-ip-row-128-network-disabled')
Expected: visible
Received: hidden
Timeout:  15000ms

Call log:
  - Expect "toBeVisible" with timeout 15000ms
  - waiting for locator('#admin-ip-row-128-network-disabled')
    33 × locator resolved to <div hidden="" role="tooltip" id="admin-ip-row-128-network-disabled" class="pointer-events-none fixed z-[60] overflow-y-auto whitespace-normal rounded-md border border-border bg-surface p-2 text-left text-xs font-normal text-fg shadow-lg">Síť je zakázaná pro nové přidělování a přiřazován…</div>
       - unexpected value "hidden"

```

```yaml
- link "Přeskočit na hlavní obsah":
  - /url: "#main-content"
- complementary:
  - text: VA vpsAdmin next UI
  - navigation:
    - link "Přehled":
      - /url: /admin
    - region "Služby":
      - text: Služby
      - link "VPS":
        - /url: /admin/vps
      - link "Datasety":
        - /url: /admin/datasets
      - link "NAS":
        - /url: /admin/nas
      - link "Exporty":
        - /url: /admin/exports
      - link "DNS":
        - /url: /admin/dns
      - link "Síť":
        - /url: /admin/networking/ip-addresses
    - region "Provoz":
      - text: Provoz
      - link "Transakce":
        - /url: /admin/transactions
      - link "Dohled":
        - /url: /admin/monitoring
      - link "Incidenty":
        - /url: /admin/incidents
      - link "OOM":
        - /url: /admin/oom-reports
      - link "Bezpečnostní upozornění":
        - /url: /admin/security-advisories
      - link "Audit":
        - /url: /admin/audit
    - region "Uživatelé a finance":
      - text: Uživatelé a finance
      - link "Uživatelé":
        - /url: /admin/users
      - link "Uživatelské jmenné prostory":
        - /url: /admin/user-namespaces/namespaces
      - link "Žádosti":
        - /url: /admin/requests
      - link "Finance":
        - /url: /admin/payments/incoming
    - region "Infrastruktura":
      - text: Infrastruktura
      - link "Cluster":
        - /url: /admin/cluster/summary
      - link "Nody":
        - /url: /admin/nodes
      - link "Migrační plány":
        - /url: /admin/migration-plans
      - link "Administrace":
        - /url: /admin/admin-info
    - region "Obsah":
      - text: Obsah
      - link "Pošta":
        - /url: /admin/mailer/templates
      - link "Obsah":
        - /url: /admin/content/news
  - link "Účet":
    - /url: /admin/profile
- banner:
  - search:
    - combobox "Rychle hledat objekty"
    - text: Ctrl K · /
  - text: Administrátorský pohled
  - button "Otevřít úlohy": Úlohy
  - button "Otevřít menu účtu": admin admin
- main:
  - heading "IP adresy" [level=1]
  - paragraph: Procházej, vyhledávej a filtruj alokace IP adres (admin).
  - text: "Tip: stiskni ? ve filtračním poli pro nápovědu. Filtry se aplikují na serveru."
  - combobox "Hledat IP adresu nebo přesný login uživatele…"
  - button "Nápověda"
  - status
  - text: vps:#1
  - button "Odebrat"
  - button "Pokročilé filtry": Pokročilé
  - button "Kopírovat odkaz"
  - button "Vymazat filtry"
  - text: Prostředí / lokace
  - combobox "Prostředí / lokace":
    - option "Všechna prostředí" [selected]
  - text: Síť / subnet
  - textbox "Síť / subnet":
    - /placeholder: Vyber existující subnet…
  - text: Verze IP
  - combobox "Verze IP":
    - option "Libovolná verze" [selected]
    - option "IPv4"
    - option "IPv6"
  - text: Obsazenost
  - button "Libovolné"
  - button "Přiřazené"
  - button "Volné adresy"
  - text: Rychlé filtry
  - button "IPv4"
  - button "IPv6"
  - button "Po rozhraní"
  - table:
    - rowgroup:
      - row "Stav IP Síť Prostředí VPS Uživatel Rozhraní Příznaky Vytvořeno Akce":
        - columnheader "Stav"
        - columnheader "IP"
        - columnheader "Síť"
        - columnheader "Prostředí"
        - columnheader "VPS"
        - columnheader "Uživatel"
        - columnheader "Rozhraní"
        - columnheader "Příznaky"
        - columnheader "Vytvořeno"
        - columnheader "Akce"
    - rowgroup:
      - 'row "Přiřazené 192.0.2.126/32 #126 192.0.2.0/24 — — — #76 Přiřazené směrovaná — Akce"':
        - cell "Přiřazené":
          - img "Přiřazené"
        - 'cell "192.0.2.126/32 #126"':
          - link "192.0.2.126/32":
            - /url: /admin/ip-addresses/126
          - text: "#126"
        - cell "192.0.2.0/24"
        - cell "—"
        - cell "—"
        - cell "—"
        - cell "#76"
        - cell "Přiřazené směrovaná"
        - cell "—"
        - cell "Akce":
          - group "Akce":
            - link "Incidenty":
              - /url: /admin/incidents?ip_addr=192.0.2.126
            - link "Přiřazení":
              - /url: /admin/networking/ip-address-assignments?ip_addr=192.0.2.126
            - link "Odebrat routu":
              - /url: /admin/ip-addresses/126#route
            - link "Vlastnictví":
              - /url: /admin/ip-addresses/126#owner
            - link "Host IP adresy":
              - /url: /admin/ip-addresses/126#hosts
      - 'row "Přiřazené 192.0.2.127/32 #127 192.0.2.0/24 — — — #77 Přiřazené směrovaná — Akce"':
        - cell "Přiřazené":
          - img "Přiřazené"
        - 'cell "192.0.2.127/32 #127"':
          - link "192.0.2.127/32":
            - /url: /admin/ip-addresses/127
          - text: "#127"
        - cell "192.0.2.0/24"
        - cell "—"
        - cell "—"
        - cell "—"
        - cell "#77"
        - cell "Přiřazené směrovaná"
        - cell "—"
        - cell "Akce":
          - group "Akce":
            - link "Incidenty":
              - /url: /admin/incidents?ip_addr=192.0.2.127
            - link "Přiřazení":
              - /url: /admin/networking/ip-address-assignments?ip_addr=192.0.2.127
            - link "Odebrat routu":
              - /url: /admin/ip-addresses/127#route
            - link "Vlastnictví":
              - /url: /admin/ip-addresses/127#owner
            - link "Host IP adresy":
              - /url: /admin/ip-addresses/127#hosts
      - 'row "Přiřazené 192.0.2.128/32 #128 192.0.2.0/24 — — — #78 Přiřazené směrovaná Síť zakázána — Akce"':
        - cell "Přiřazené":
          - img "Přiřazené"
        - 'cell "192.0.2.128/32 #128"':
          - link "192.0.2.128/32":
            - /url: /admin/ip-addresses/128
          - text: "#128"
        - cell "192.0.2.0/24"
        - cell "—"
        - cell "—"
        - cell "—"
        - cell "#78"
        - cell "Přiřazené směrovaná Síť zakázána"
        - cell "—"
        - cell "Akce":
          - group "Akce":
            - link "Incidenty":
              - /url: /admin/incidents?ip_addr=192.0.2.128
            - link "Přiřazení":
              - /url: /admin/networking/ip-address-assignments?ip_addr=192.0.2.128
            - link "Odebrat routu":
              - /url: /admin/ip-addresses/128#route
            - link "Vlastnictví":
              - /url: /admin/ip-addresses/128#owner
            - link "Host IP adresy":
              - /url: /admin/ip-addresses/128#hosts
  - button "Předchozí"
  - button "Přejít na stranu 1": "1"
  - button "Strana 2 (aktuální)": "2"
  - button "Další" [disabled]
  - text: Strana 2 Přejít na
  - spinbutton "Přejít na"
  - button "Přejít" [disabled]
  - text: Řádků
  - combobox:
    - option "25" [selected]
    - option "50"
    - option "100"
```

# Test source

```ts
  1   | import { expect, test, type Locator, type Page } from '@playwright/test';
  2   | 
  3   | import { bootstrapVpsAdminWindow, installHaveApiMock, setUiSettingsLocalStorage } from '../../fixtures';
  4   | 
  5   | async function expectUnclippedDescription(page: Page, trigger: Locator, description: string) {
  6   |   const id = await trigger.getAttribute('aria-describedby');
  7   |   if (!id) throw new Error('Inventory trigger has no description ID');
  8   |   const tooltip = page.locator(`#${id}`);
  9   |   await expect(trigger).toHaveAttribute('title', description);
  10  |   await expect(trigger).toHaveAccessibleDescription(description);
  11  |   await expect(tooltip).toHaveCount(1);
  12  |   await expect(tooltip).toHaveAttribute('role', 'tooltip');
> 13  |   await expect(tooltip).toBeVisible();
      |                         ^ Error: expect(locator).toBeVisible() failed
  14  |   await expect(tooltip).toHaveText(description);
  15  |   const geometry = await tooltip.evaluate((node, triggerId) => {
  16  |     const box = node.getBoundingClientRect();
  17  |     const anchor = document.querySelector(`[aria-describedby="${triggerId}"]`)?.getBoundingClientRect();
  18  |     if (!anchor) throw new Error('Inventory description has no trigger');
  19  |     const range = document.createRange();
  20  |     range.selectNodeContents(node);
  21  |     const textBoxes = Array.from(range.getClientRects()).filter((rect) => rect.width > 0 && rect.height > 0);
  22  |     const clippingAncestors: string[] = [];
  23  |     for (let parent = node.parentElement; parent; parent = parent.parentElement) {
  24  |       const style = getComputedStyle(parent);
  25  |       const bounds = parent.getBoundingClientRect();
  26  |       const left = bounds.left + parent.clientLeft;
  27  |       const top = bounds.top + parent.clientTop;
  28  |       if ((['hidden', 'clip', 'auto', 'scroll'].includes(style.overflowX)
  29  |           && (box.left < left - 1 || box.right > left + parent.clientWidth + 1))
  30  |         || (['hidden', 'clip', 'auto', 'scroll'].includes(style.overflowY)
  31  |           && (box.top < top - 1 || box.bottom > top + parent.clientHeight + 1))) {
  32  |         clippingAncestors.push(parent.tagName);
  33  |       }
  34  |     }
  35  |     return {
  36  |       bodyPortal: node.parentElement === document.body,
  37  |       position: getComputedStyle(node).position,
  38  |       clippingAncestors,
  39  |       insideViewport: box.left >= 0 && box.top >= 0 && box.right <= window.innerWidth && box.bottom <= window.innerHeight,
  40  |       fullText: textBoxes.length > 0 && textBoxes.every((text) => text.left >= box.left && text.right <= box.right && text.top >= box.top && text.bottom <= box.bottom),
  41  |       selfClipped: node.scrollWidth > node.clientWidth + 1 || node.scrollHeight > node.clientHeight + 1,
  42  |       anchor: { top: anchor.top, bottom: anchor.bottom },
  43  |       popup: { top: box.top, bottom: box.bottom, height: box.height },
  44  |       viewport: { width: window.innerWidth, height: window.innerHeight },
  45  |     };
  46  |   }, id);
  47  |   expect(geometry).toMatchObject({ bodyPortal: true, position: 'fixed', clippingAncestors: [], insideViewport: true, fullText: true, selfClipped: false });
  48  |   return { tooltip, geometry };
  49  | }
  50  | 
  51  | for (const language of ['en', 'cs'] as const) {
  52  |   test(`@pr-smoke @pr-smoke-mobile network availability retains service context and rejected drafts (${language})`, async ({ page }, testInfo) => {
  53  |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  54  |     await setUiSettingsLocalStorage(page, { language });
  55  |     let enabled = true;
  56  |     let rejectNext = true;
  57  |     const writes: boolean[] = [];
  58  |     const capabilityMethods: string[] = [];
  59  |     const network = () => ({
  60  |       id: 101, label: 'Retained service', address: '192.0.2.0', prefix: 24,
  61  |       ip_version: 4, role: 'public_access', purpose: 'vps', managed: true,
  62  |       enabled, split_access: 'no_access', split_prefix: 32, assigned: 3, owned: 5, used: 9, size: 256, taken: 7,
  63  |       available_to_users: 0, owned_unassigned: 2,
  64  |     });
  65  |     await installHaveApiMock(page, {
  66  |       user: { id: 1, login: 'admin', level: 100 },
  67  |       handlers: {
  68  |         'GET locations': () => ({ locations: [] }),
  69  |         'GET networks': () => ({ networks: [network()] }),
  70  |         'OPTIONS networks/101': (ctx) => {
  71  |           expect(ctx.method).toBe('OPTIONS');
  72  |           expect(ctx.searchParams.get('method')).toBe('PUT');
  73  |           capabilityMethods.push(ctx.searchParams.get('method') ?? '');
  74  |           return {
  75  |             method: 'PUT', scope: 'network#update',
  76  |             input: { namespace: 'network', layout: 'object', parameters: { enabled: { type: 'Boolean' } } },
  77  |             output: { namespace: 'network', layout: 'object', parameters: {} },
  78  |           };
  79  |         },
  80  |         'PUT networks/101': (ctx) => {
  81  |           const input = ctx.reqJson as { network: { enabled: boolean } };
  82  |           expect(typeof input.network.enabled).toBe('boolean');
  83  |           writes.push(input.network.enabled);
  84  |           if (rejectNext) {
  85  |             rejectNext = false;
  86  |             return { status: false, message: 'Allocation policy rejected', response: null };
  87  |           }
  88  |           enabled = input.network.enabled;
  89  |           return { network: network() };
  90  |         },
  91  |       },
  92  |     });
  93  |     await page.goto('/admin/cluster/networks');
  94  |     const row = page.getByTestId('admin.cluster.networks.row.101');
  95  |     await expect(row.getByTestId('admin.cluster.networks.row.101.available_to_users')).toHaveText('0');
  96  |     await expect(row.getByTestId('admin.cluster.networks.row.101.owned_unassigned')).toHaveText('2');
  97  |     await expect(row.getByTestId('admin.cluster.networks.row.101.assigned')).toHaveText('3');
  98  |     await expect(row.getByTestId('admin.cluster.networks.row.101.used')).toHaveText('9');
  99  |     const countDescription = language === 'en'
  100 |       ? "Registered addresses or prefixes with no owner or interface assignment, and not reserved by an operation. Disabled networks contribute zero. Use on a particular VPS also depends on location, network purpose and user limits."
  101 |       : "Evidované adresy nebo prefixy bez vlastníka a bez přiřazení k rozhraní, které nejsou rezervované probíhající operací. V zakázané síti je tento počet nulový. Použití na konkrétním VPS závisí také na lokaci, účelu sítě a limitech uživatele.";
  102 |     const countLabel = page.locator('[aria-describedby="network-count-available"]');
  103 |     const countTooltip = page.locator('#network-count-available');
  104 |     const viewport = page.viewportSize();
  105 |     if (!viewport) throw new Error('Browser project requires a viewport');
  106 |     const tableScroll = page.getByTestId('admin.cluster.networks.table').locator('.overflow-x-auto');
  107 |     expect(await tableScroll.evaluate((node) => node.scrollWidth > node.clientWidth)).toBe(true);
  108 |     await tableScroll.evaluate((node) => { node.scrollLeft = node.scrollWidth; });
  109 |     await expect.poll(() => tableScroll.evaluate((node) => node.scrollLeft)).toBeGreaterThan(0);
  110 |     await countLabel.scrollIntoViewIfNeeded();
  111 |     await countLabel.focus();
  112 |     await expect(countLabel).toBeFocused();
  113 |     await expectUnclippedDescription(page, countLabel, countDescription);
```