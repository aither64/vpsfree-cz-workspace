# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/admin_incident_policies.spec.ts >> admin policy Overview/History cs mobile=true
- Location: e2e/specs/app/admin_incident_policies.spec.ts:43:5

# Error details

```
Error: expect(received).toBeTruthy()

Received: undefined
```

# Page snapshot

```yaml
- generic [ref=e2]:
  - link "Přeskočit na hlavní obsah" [ref=e3] [cursor=pointer]:
    - /url: "#main-content"
  - generic [ref=e6]:
    - banner [ref=e7]:
      - button "Otevřít navigaci" [ref=e8]:
        - img [ref=e9]
        - generic [ref=e10]: Navigace
    - main [ref=e11]:
      - generic [ref=e13]:
        - generic [ref=e15]:
          - heading "Přehled" [level=1] [ref=e17]
          - paragraph [ref=e18]: Všechny VPS s aktuálně započítanými incidenty podle pravidel, včetně VPS pod limity.
        - generic [ref=e19]:
          - link "Přehled" [ref=e20] [cursor=pointer]:
            - /url: /admin/incidents/overview?offset=25&as_of=2026-11-24T10%3A00%3A01.000Z
          - link "Hlášení" [ref=e21] [cursor=pointer]:
            - /url: /admin/incidents
          - link "Historie" [ref=e22] [cursor=pointer]:
            - /url: /admin/incidents/history
        - generic [ref=e25]: Rozhodný čas určuje období pro počítání. Nastavení, vlastník a výsledky akcí odpovídají poslednímu načtení. Obnovením se nastaví nový rozhodný čas. Zbývající počet udává, kolik incidentů chybí do limitu. Počet může klesnout, když starší incidenty vypadnou ze sledovaného období. Tento údaj ani konec ochranné lhůty nezaručují, že další incident vyvolá akci.
        - generic [ref=e26]:
          - generic [ref=e27]:
            - generic [ref=e28]:
              - generic [ref=e29]: Klíč pravidla
              - textbox "Klíč pravidla" [ref=e30]
            - generic [ref=e31]:
              - generic [ref=e32]: ID VPS
              - textbox "ID VPS" [ref=e33]
            - generic [ref=e34]:
              - generic [ref=e35]: ID vlastníka
              - textbox "ID vlastníka" [ref=e36]
            - generic [ref=e37]:
              - generic [ref=e38]: ID nodu
              - textbox "ID nodu" [ref=e39]
          - generic [ref=e40]:
            - generic [ref=e41]:
              - generic [ref=e42]: Dosažení limitu
              - combobox "Dosažení limitu" [ref=e43]:
                - option "Vše" [selected]
                - option "Pod limity"
                - option "Blízko limitu"
                - option "Limit pro upozornění dosažen"
                - option "Limit pro vypnutí dosažen"
                - option "Neplatná konfigurace"
            - generic [ref=e44]:
              - generic [ref=e45]: Výsledný režim
              - combobox "Výsledný režim" [ref=e46]:
                - option "Vše" [selected]
                - option "Pouze sledování"
                - option "Pouze upozornění"
                - option "Upozornění a automatické vypnutí"
            - generic [ref=e47]:
              - generic [ref=e48]: Automatické vypnutí povoleno
              - combobox "Automatické vypnutí povoleno" [ref=e49]:
                - option "Vše" [selected]
                - option "Ano"
                - option "Ne"
            - generic [ref=e50]:
              - generic [ref=e51]: Řadit podle
              - combobox "Řadit podle" [ref=e52]:
                - option "Priorita" [selected]
                - option "ID VPS"
                - option "Login vlastníka"
                - option "Klíč pravidla"
                - option "Počet incidentů za 7 dní"
                - option "Počet incidentů za 30 dní"
                - option "Počet incidentů do limitu pro upozornění"
                - option "Počet incidentů do limitu pro vypnutí"
                - option "Poslední započítaný incident"
            - generic [ref=e53]:
              - generic [ref=e54]: Směr
              - combobox "Směr" [ref=e55]:
                - option "Sestupně" [selected]
                - option "Vzestupně"
          - generic [ref=e56]:
            - button "Použít filtry" [ref=e57]
            - button "Obnovit" [ref=e58]
        - generic [ref=e59]:
          - generic [ref=e60]: "Rozhodný čas počítání: 11/24/2026, 11:00:01 AM"
          - generic [ref=e61]: "Aktuální údaje načteny: 11/24/2026, 11:01:00 AM"
        - generic [ref=e64]:
          - generic [ref=e65]:
            - generic [ref=e67]:
              - link "#45 synthetic-25.example.test" [ref=e68] [cursor=pointer]:
                - /url: /admin/vps/45
              - link "demo-owner (#4)" [ref=e70] [cursor=pointer]:
                - /url: /admin/users/4
              - generic [ref=e71]: node.example.test (#5)
            - link "SYNTHETIC policy 26 policy-25" [ref=e73] [cursor=pointer]:
              - /url: /admin/vps/45/incidents#incident-policy-policy-25
              - text: SYNTHETIC policy 26
              - generic [ref=e74]: policy-25
          - generic [ref=e75]:
            - generic [ref=e76]:
              - generic [ref=e77]: Limit pro upozornění
              - generic [ref=e79]:
                - generic [ref=e80]: 2 / 3 incidentů za 7 dní
                - generic [ref=e81]: "Do limitu zbývá incidentů: 1"
            - generic [ref=e82]:
              - generic [ref=e83]: Limit pro vypnutí
              - generic [ref=e85]:
                - generic [ref=e86]: 4 / 10 incidentů za 30 dní
                - generic [ref=e87]: "Do limitu zbývá incidentů: 6"
            - generic [ref=e88]:
              - generic [ref=e89]: Dosažení limitu
              - generic [ref=e90]:
                - text: Pod limity
                - generic [ref=e91]: "Poslední započítaný incident: 11/24/2026, 11:00:00 AM"
            - generic [ref=e92]:
              - generic [ref=e93]: Režim a omezení
              - generic [ref=e95]:
                - generic [ref=e96]: "Výsledný režim: Upozornění a automatické vypnutí"
                - generic [ref=e97]: "Globální režim: Upozornění a automatické vypnutí"
                - generic [ref=e98]: "Upozornění e-mailem povoleno: Ano"
                - generic [ref=e99]: "Automatické vypnutí povoleno: Ne"
            - generic [ref=e100]:
              - generic [ref=e101]: Poslední zaznamenaný výsledek
              - generic [ref=e103]: Bez zaznamenané akce
        - generic [ref=e104]:
          - generic [ref=e105]: Řádky 26–26 z 26
          - button "Předchozí" [ref=e106]
          - button "Další" [disabled] [ref=e107]
          - generic [ref=e108]:
            - text: Řádků na stránce
            - combobox "Řádků na stránce" [ref=e109]:
              - option "25" [selected]
              - option "50"
              - option "100"
```

# Test source

```ts
  1   | import { expect, test, type Page } from '@playwright/test';
  2   | import { installAdminIncidentFixture } from '../../fixtures/adminIncidentPolicies';
  3   | import { expectNoDocumentHorizontalOverflow } from '../../helpers/horizontalOverflow';
  4   | 
  5   | interface SyntheticDiagnostics {
  6   |   consoleErrors: string[];
  7   |   pageErrors: string[];
  8   |   failedRequests: string[];
  9   |   blockedExternal: string[];
  10  | }
  11  | const observed = new WeakMap<Page, SyntheticDiagnostics>();
  12  | test.beforeEach(async ({ page }) => {
  13  |   const diagnostics: SyntheticDiagnostics = {
  14  |     consoleErrors: [],
  15  |     pageErrors: [],
  16  |     failedRequests: [],
  17  |     blockedExternal: [],
  18  |   };
  19  |   observed.set(page, diagnostics);
  20  |   page.on('console', (message) => {
  21  |     if (message.type() === 'error') diagnostics.consoleErrors.push(message.text());
  22  |   });
  23  |   page.on('pageerror', (error) => diagnostics.pageErrors.push(error.message));
  24  |   page.on('requestfailed', (request) =>
  25  |     diagnostics.failedRequests.push(`${request.method()} ${request.url()} ${request.failure()?.errorText}`)
  26  |   );
  27  |   await page.route('**/*', (route) => {
  28  |     const url = new URL(route.request().url());
  29  |     if (['127.0.0.1', 'localhost'].includes(url.hostname)) return route.fallback();
  30  |     diagnostics.blockedExternal.push(route.request().url());
  31  |     return route.abort('blockedbyclient');
  32  |   });
  33  | });
  34  | test.afterEach(async ({ page }, testInfo) => {
  35  |   await testInfo.attach('synthetic-diagnostics', {
  36  |     body: Buffer.from(JSON.stringify({ synthetic: true, ...observed.get(page) })),
  37  |     contentType: 'application/json',
  38  |   });
  39  | });
  40  | 
  41  | for (const language of ['en', 'cs'] as const) {
  42  |   for (const mobile of [false, true]) {
  43  |     test(`admin policy Overview/History ${language} mobile=${mobile}`, async ({ page }, testInfo) => {
  44  |       await page.setViewportSize(mobile ? { width: 390, height: 844 } : { width: 1280, height: 1000 });
  45  |       const fixture = await installAdminIncidentFixture(page, language);
  46  |       await page.goto('/admin/incidents/overview');
  47  |       await expect(page.getByTestId('incidents.admin.overview')).toBeVisible();
  48  |       await expect(page.getByTestId('incidents.admin.paging')).toBeVisible();
  49  |       await expect.poll(() => new URL(page.url()).searchParams.has('as_of')).toBe(true);
  50  |       expect(fixture.overviewQueries).toHaveLength(1);
  51  |       await page.screenshot({
  52  |         path: testInfo.outputPath(`initial-overview-${language}-${mobile ? 'mobile' : 'desktop'}.png`),
  53  |         fullPage: false,
  54  |       });
  55  |       await page.getByTestId('incidents.admin.paging').getByRole('button').last().click();
  56  |       await expect.poll(() => Number(fixture.overviewQueries.at(-1)?.['offset'])).toBe(25);
  57  |       const cutoff = fixture.overviewQueries.at(-1)?.['as_of'];
> 58  |       expect(cutoff).toBeTruthy();
      |                      ^ Error: expect(received).toBeTruthy()
  59  |       await page.goBack();
  60  |       await expect.poll(() => Number(new URL(page.url()).searchParams.get('offset') ?? 0)).toBe(0);
  61  |       expect(new URL(page.url()).searchParams.get('as_of')).toBe(cutoff);
  62  |       await page.locator('input[name="vps"]').fill('12');
  63  |       await page
  64  |         .locator('form')
  65  |         .filter({ has: page.locator('input[name="vps"]') })
  66  |         .locator('button[type="submit"]')
  67  |         .click();
  68  |       await expect.poll(() => Number(fixture.overviewQueries.at(-1)?.['vps'])).toBe(12);
  69  |       expect(Number(fixture.overviewQueries.at(-1)?.['offset'])).toBe(0);
  70  |       expect(fixture.overviewQueries.at(-1)?.['as_of']).toBe(cutoff);
  71  |       await expect(
  72  |         page.locator('a[href="/admin/vps/12/incidents#incident-policy-policy-0"]').filter({ visible: true })
  73  |       ).toBeVisible();
  74  |       await expectNoDocumentHorizontalOverflow(page);
  75  |       await page.screenshot({
  76  |         path: testInfo.outputPath(`filtered-overview-${language}-${mobile ? 'mobile' : 'desktop'}.png`),
  77  |         fullPage: true,
  78  |       });
  79  |       const reads = fixture.overviewQueries.length;
  80  |       await page
  81  |         .locator('form')
  82  |         .filter({ has: page.locator('input[name="vps"]') })
  83  |         .locator('button[type="button"]')
  84  |         .click();
  85  |       await expect.poll(() => fixture.overviewQueries.length).toBe(reads + 1);
  86  |       expect(fixture.overviewQueries.at(-1)?.['as_of']).toBeUndefined();
  87  |       await expect.poll(() => new URL(page.url()).searchParams.get('as_of')).not.toBe(cutoff);
  88  |       await page.getByTestId('incidents.admin.tabs').locator('a[href="/admin/incidents/history"]').click();
  89  |       await expect(page.getByTestId('incidents.admin.history')).toBeVisible();
  90  |       await expect.poll(() => fixture.historyQueries.length).toBeGreaterThan(0);
  91  |       await expect(
  92  |         page.getByTestId(mobile ? 'incidents.admin.history.mobile' : 'incidents.admin.history.rows')
  93  |       ).toBeVisible();
  94  |       expect(fixture.historyQueries.at(-1)).not.toHaveProperty('sort');
  95  |       await expect(page.locator('select').filter({ has: page.locator('option[value="evaluated_at"]') })).toHaveCount(0);
  96  |       await expectNoDocumentHorizontalOverflow(page);
  97  |       await page.screenshot({
  98  |         path: testInfo.outputPath(`initial-history-${language}-${mobile ? 'mobile' : 'desktop'}.png`),
  99  |         fullPage: true,
  100 |       });
  101 |       await page
  102 |         .locator('select')
  103 |         .filter({ has: page.locator('option[value="outstanding"]') })
  104 |         .selectOption('outstanding');
  105 |       await expect.poll(() => fixture.historyQueries.at(-1)?.['scope']).toBe('outstanding');
  106 |       await expect(page.locator('input[name="from"]')).toBeDisabled();
  107 |       await expect(page.locator('input[name="to"]')).toBeDisabled();
  108 |       await page.getByTestId('incidents.admin.tabs').locator('a[href="/admin/incidents"]').click();
  109 |       await expect(page.getByTestId('incidents.list.header')).toBeVisible();
  110 |       expect(new URL(page.url()).pathname).toBe('/admin/incidents');
  111 |     });
  112 |   }
  113 | }
  114 | 
  115 | for (const level of [1, 21]) {
  116 |   test(`new admin policy routes deny role level ${level} without endpoint reads`, async ({ page }) => {
  117 |     const fixture = await installAdminIncidentFixture(page, 'en', level);
  118 |     await page.goto('/admin/incidents/overview');
  119 |     await expect(page.getByTestId('forbidden.page')).toBeVisible();
  120 |     expect(fixture.overviewQueries).toHaveLength(0);
  121 |     expect(fixture.historyQueries).toHaveLength(0);
  122 |   });
  123 | }
  124 | test('missing new capabilities keep Reports reachable without endpoint reads', async ({ page }) => {
  125 |   const fixture = await installAdminIncidentFixture(page, 'en', 90, false);
  126 |   await page.goto('/admin/incidents/overview');
  127 |   await expect(page.getByTestId('incidents.admin.overview')).toBeVisible();
  128 |   await expect(page.getByTestId('incidents.admin.paging')).toHaveCount(0);
  129 |   expect(fixture.overviewQueries).toHaveLength(0);
  130 |   await page.getByTestId('incidents.admin.tabs').locator('a[href="/admin/incidents"]').click();
  131 |   await expect(page.getByTestId('incidents.list.header')).toBeVisible();
  132 | });
  133 | 
```