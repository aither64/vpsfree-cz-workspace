# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/admin_incident_policies.spec.ts >> admin policy Overview/History cs mobile=false
- Location: e2e/specs/app/admin_incident_policies.spec.ts:70:5

# Error details

```
Error: expect(locator).toContainText(expected) failed

Locator: getByTestId('incidents.admin.history.rows').locator('details').first()
Expected substring: "#95"
Received string:    "Podrobnostipolicy-0 · #4 original-ownerZjištěno: 11/20/2026, 10:59:00 AMZaznamenáno · ShodaVýsledný režim: Upozornění a automatické vypnutíVypnutí povoleno při vyhodnocení: AnoUložené rozhodnutí: VypnutíVypnutí: DokončenoTransakční řetězec č. 100Společná akce vypnutí VPS č. 95Akce vytvořena: 11/20/2026, 11:00:00 AMAkce naposledy změněna: 11/20/2026, 11:01:00 AMPotvrzené vypnutí: 11/24/2026, 10:00:00 AME-mail s oznámením: SelhaloOznámení č. 71"
Timeout: 15000ms

Call log:
  - Expect "toContainText" with timeout 15000ms
  - waiting for getByTestId('incidents.admin.history.rows').locator('details').first()
    33 × locator resolved to <details open="" class="mt-2" data-testid="incidents.admin.rowDetails">…</details>
       - unexpected value "Podrobnostipolicy-0 · #4 original-ownerZjištěno: 11/20/2026, 10:59:00 AMZaznamenáno · ShodaVýsledný režim: Upozornění a automatické vypnutíVypnutí povoleno při vyhodnocení: AnoUložené rozhodnutí: VypnutíVypnutí: DokončenoTransakční řetězec č. 100Společná akce vypnutí VPS č. 95Akce vytvořena: 11/20/2026, 11:00:00 AMAkce naposledy změněna: 11/20/2026, 11:01:00 AMPotvrzené vypnutí: 11/24/2026, 10:00:00 AME-mail s oznámením: SelhaloOznámení č. 71"

```

```yaml
- group:
  - text: "Podrobnosti policy-0 · #4 original-owner Zjištěno: 11/20/2026, 10:59:00 AM Zaznamenáno · Shoda Výsledný režim: Upozornění a automatické vypnutí Vypnutí povoleno při vyhodnocení: Ano Uložené rozhodnutí: Vypnutí Vypnutí: Dokončeno"
  - link "Transakční řetězec č. 100":
    - /url: /admin/transactions/100
  - text: "Společná akce vypnutí VPS č. 95 Akce vytvořena: 11/20/2026, 11:00:00 AM Akce naposledy změněna: 11/20/2026, 11:01:00 AM Potvrzené vypnutí: 11/24/2026, 10:00:00 AM E-mail s oznámením: Selhalo"
  - link "Oznámení č. 71":
    - /url: /admin/incidents/71
```

# Test source

```ts
  56  |   // Record actual current geometry; no font-size reduction is allowed.
  57  |   expect(widths.firstRowHeight).toBeLessThan(145);
  58  |   expect(widths.fontSize).toBe('14px');
  59  |   return widths;
  60  | }
  61  | async function keyboardToggle(details: ReturnType<Page['locator']>, opened: boolean) {
  62  |   const summary = details.locator(':scope > summary');
  63  |   await summary.focus();
  64  |   await summary.press('Enter');
  65  |   await expect.poll(() => details.evaluate((element) => (element as HTMLDetailsElement).open)).toBe(opened);
  66  | }
  67  | 
  68  | for (const language of ['en', 'cs'] as const) {
  69  |   for (const mobile of [false, true]) {
  70  |     test(`admin policy Overview/History ${language} mobile=${mobile}`, async ({ page }, testInfo) => {
  71  |       await page.setViewportSize(mobile ? { width: 390, height: 844 } : { width: 1280, height: 1000 });
  72  |       const fixture = await installAdminIncidentFixture(page, language);
  73  |       await page.goto('/admin/incidents/overview');
  74  |       const overview = page.getByTestId(mobile ? 'incidents.admin.overview.mobile' : 'incidents.admin.overview.rows');
  75  |       await expect(overview).toBeVisible();
  76  |       await expect(page.getByTestId('incidents.admin.paging')).toBeVisible();
  77  |       await expect.poll(() => new URL(page.url()).searchParams.has('as_of')).toBe(true);
  78  |       expect(fixture.overviewQueries).toHaveLength(1);
  79  |       const more = page.getByTestId('incidents.admin.moreFilters');
  80  |       await expect.poll(() => more.evaluate((element) => (element as HTMLDetailsElement).open)).toBe(false);
  81  |       await expect(page.locator('input[name="vps"]')).toBeEnabled();
  82  |       await expect(page.locator('input[name="vps"]')).not.toBeVisible();
  83  |       const rowDetails = overview.locator('details').first();
  84  |       await expect.poll(() => rowDetails.evaluate((element) => (element as HTMLDetailsElement).open)).toBe(false);
  85  |       const overviewGeometry = await geometry(page, 'overview', mobile);
  86  |       await page.evaluate(() => window.scrollTo(0, 0));
  87  |       await page.screenshot({
  88  |         path: testInfo.outputPath(`initial-overview-${language}-${mobile ? 'mobile' : 'desktop'}.png`),
  89  |         fullPage: false,
  90  |       });
  91  |       await keyboardToggle(rowDetails, true);
  92  |       await expect(rowDetails).toContainText('node.example.test');
  93  |       expect(fixture.overviewQueries).toHaveLength(1);
  94  |       await rowDetails.scrollIntoViewIfNeeded();
  95  |       await page.screenshot({
  96  |         path: testInfo.outputPath(`opened-overview-${language}-${mobile ? 'mobile' : 'desktop'}.png`),
  97  |         fullPage: false,
  98  |       });
  99  |       await keyboardToggle(rowDetails, false);
  100 |       await page.getByTestId('incidents.admin.paging').getByRole('button').last().click();
  101 |       await expect.poll(() => Number(fixture.overviewQueries.at(-1)?.['offset'])).toBe(25);
  102 |       const cutoff = fixture.overviewQueries.at(-1)?.['as_of'];
  103 |       expect(cutoff).toBeTruthy();
  104 |       await page.goBack();
  105 |       await expect.poll(() => Number(new URL(page.url()).searchParams.get('offset') ?? 0)).toBe(0);
  106 |       expect(new URL(page.url()).searchParams.get('as_of')).toBe(cutoff);
  107 |       await keyboardToggle(more, true);
  108 |       await page.locator('input[name="vps"]').fill('12');
  109 |       await page
  110 |         .locator('form')
  111 |         .filter({ has: page.locator('input[name="vps"]') })
  112 |         .locator('button[type="submit"]')
  113 |         .click();
  114 |       await expect.poll(() => Number(fixture.overviewQueries.at(-1)?.['vps'])).toBe(12);
  115 |       expect(Number(fixture.overviewQueries.at(-1)?.['offset'])).toBe(0);
  116 |       expect(fixture.overviewQueries.at(-1)?.['as_of']).toBe(cutoff);
  117 |       await expect.poll(() => more.evaluate((element) => (element as HTMLDetailsElement).open)).toBe(true);
  118 |       await keyboardToggle(more, false);
  119 |       await expect(page.locator('input[name="vps"]')).toBeEnabled();
  120 |       await expect(page.locator('input[name="vps"]')).toHaveValue('12');
  121 |       await page
  122 |         .locator('form')
  123 |         .filter({ has: page.locator('input[name="vps"]') })
  124 |         .locator('button[type="submit"]')
  125 |         .click();
  126 |       expect(new URL(page.url()).searchParams.get('vps')).toBe('12');
  127 |       const reads = fixture.overviewQueries.length;
  128 |       await page
  129 |         .locator('form')
  130 |         .filter({ has: page.locator('input[name="vps"]') })
  131 |         .locator('button[type="button"]')
  132 |         .click();
  133 |       await expect.poll(() => fixture.overviewQueries.length).toBe(reads + 1);
  134 |       expect(fixture.overviewQueries.at(-1)?.['as_of']).toBeUndefined();
  135 |       expect(Number(fixture.overviewQueries.at(-1)?.['vps'])).toBe(12);
  136 |       await expect.poll(() => new URL(page.url()).searchParams.get('as_of')).not.toBe(cutoff);
  137 |       // A fresh document with nondefault URL fields must open More filters too.
  138 |       await page.reload();
  139 |       await expect.poll(() => more.evaluate((element) => (element as HTMLDetailsElement).open)).toBe(true);
  140 |       await expect(page.locator('input[name="vps"]')).toHaveValue('12');
  141 |       await page.getByTestId('incidents.admin.tabs').locator('a[href="/admin/incidents/history"]').click();
  142 |       const history = page.getByTestId(mobile ? 'incidents.admin.history.mobile' : 'incidents.admin.history.rows');
  143 |       await expect(history).toBeVisible();
  144 |       await expect.poll(() => fixture.historyQueries.length).toBeGreaterThan(0);
  145 |       await expect.poll(() => more.evaluate((element) => (element as HTMLDetailsElement).open)).toBe(false);
  146 |       const historyDetails = history.locator('details').first();
  147 |       await expect.poll(() => historyDetails.evaluate((element) => (element as HTMLDetailsElement).open)).toBe(false);
  148 |       const historyGeometry = await geometry(page, 'history', mobile);
  149 |       await page.evaluate(() => window.scrollTo(0, 0));
  150 |       await page.screenshot({
  151 |         path: testInfo.outputPath(`initial-history-${language}-${mobile ? 'mobile' : 'desktop'}.png`),
  152 |         fullPage: false,
  153 |       });
  154 |       const historyReads = fixture.historyQueries.length;
  155 |       await keyboardToggle(historyDetails, true);
> 156 |       await expect(historyDetails).toContainText('#95');
      |                                    ^ Error: expect(locator).toContainText(expected) failed
  157 |       expect(fixture.historyQueries).toHaveLength(historyReads);
  158 |       await historyDetails.scrollIntoViewIfNeeded();
  159 |       await page.screenshot({
  160 |         path: testInfo.outputPath(`opened-history-${language}-${mobile ? 'mobile' : 'desktop'}.png`),
  161 |         fullPage: false,
  162 |       });
  163 |       await keyboardToggle(historyDetails, false);
  164 |       expect(fixture.historyQueries.at(-1)).not.toHaveProperty('sort');
  165 |       await expect(page.locator('select').filter({ has: page.locator('option[value="evaluated_at"]') })).toHaveCount(0);
  166 |       await page
  167 |         .locator('select')
  168 |         .filter({ has: page.locator('option[value="outstanding"]') })
  169 |         .selectOption('outstanding');
  170 |       await expect.poll(() => fixture.historyQueries.at(-1)?.['scope']).toBe('outstanding');
  171 |       await expect(page.locator('input[name="from"]')).toBeDisabled();
  172 |       await expect(page.locator('input[name="to"]')).toBeDisabled();
  173 |       await page.getByTestId('incidents.admin.tabs').locator('a[href="/admin/incidents"]').click();
  174 |       await expect(page.getByTestId('incidents.list.header')).toBeVisible();
  175 |       expect(new URL(page.url()).pathname).toBe('/admin/incidents');
  176 |       await expect(page.getByTestId('nav.sidebar.incidents')).toHaveAttribute('href', '/admin/incidents/overview');
  177 |       await testInfo.attach('compact-geometry', {
  178 |         body: Buffer.from(JSON.stringify({ language, mobile, overview: overviewGeometry, history: historyGeometry })),
  179 |         contentType: 'application/json',
  180 |       });
  181 |     });
  182 |   }
  183 | }
  184 | 
  185 | for (const level of [1, 21]) {
  186 |   test(`new admin policy routes deny role level ${level} without endpoint reads`, async ({ page }) => {
  187 |     const fixture = await installAdminIncidentFixture(page, 'en', level);
  188 |     await page.goto('/admin/incidents/overview');
  189 |     if (level === 1)
  190 |       await expect(page.getByRole('heading', { name: 'Admin access required', exact: true })).toBeVisible();
  191 |     else await expect(page.getByTestId('forbidden.page')).toBeVisible();
  192 |     expect(fixture.overviewQueries).toHaveLength(0);
  193 |     expect(fixture.historyQueries).toHaveLength(0);
  194 |   });
  195 | }
  196 | test('missing new capabilities keep Reports reachable without endpoint reads', async ({ page }) => {
  197 |   const fixture = await installAdminIncidentFixture(page, 'en', 90, false);
  198 |   await page.goto('/admin/incidents/overview');
  199 |   await expect(page.getByTestId('incidents.admin.overview')).toBeVisible();
  200 |   await expect(page.getByTestId('incidents.admin.paging')).toHaveCount(0);
  201 |   expect(fixture.overviewQueries).toHaveLength(0);
  202 |   await page.getByTestId('incidents.admin.tabs').locator('a[href="/admin/incidents"]').click();
  203 |   await expect(page.getByTestId('incidents.list.header')).toBeVisible();
  204 | });
  205 | 
```