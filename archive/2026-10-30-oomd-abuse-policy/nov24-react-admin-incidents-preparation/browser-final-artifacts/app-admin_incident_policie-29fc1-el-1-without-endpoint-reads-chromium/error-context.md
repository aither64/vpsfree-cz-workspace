# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/admin_incident_policies.spec.ts >> new admin policy routes deny role level 1 without endpoint reads
- Location: e2e/specs/app/admin_incident_policies.spec.ts:135:3

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: getByTestId('forbidden.page')
Expected: visible
Timeout: 15000ms
Error: element(s) not found

Call log:
  - Expect "toBeVisible" with timeout 15000ms
  - waiting for getByTestId('forbidden.page')

```

```yaml
- heading "Admin access required" [level=1]
- paragraph: You’re signed in as synthetic-admin, but this account does not have permission to use the admin view.
- link "Go to My view":
  - /url: /app
- link "Go to status":
  - /url: /
```

# Test source

```ts
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
  51  |       if (!mobile) {
  52  |         const widths = await page.getByTestId('incidents.admin.overview.rows').evaluate((table) => ({
  53  |           content: table.parentElement!.clientWidth,
  54  |           scroll: table.parentElement!.scrollWidth,
  55  |           right: table.querySelector('th:last-child')!.getBoundingClientRect().right,
  56  |         }));
  57  |         expect(widths.scroll).toBeLessThanOrEqual(widths.content + 1);
  58  |         expect(widths.right).toBeLessThanOrEqual(1280);
  59  |       }
  60  |       await page.screenshot({
  61  |         path: testInfo.outputPath(`initial-overview-${language}-${mobile ? 'mobile' : 'desktop'}.png`),
  62  |         fullPage: false,
  63  |       });
  64  |       await page.getByTestId('incidents.admin.paging').getByRole('button').last().click();
  65  |       await expect.poll(() => Number(fixture.overviewQueries.at(-1)?.['offset'])).toBe(25);
  66  |       const cutoff = fixture.overviewQueries.at(-1)?.['as_of'];
  67  |       expect(cutoff).toBeTruthy();
  68  |       await page.goBack();
  69  |       await expect.poll(() => Number(new URL(page.url()).searchParams.get('offset') ?? 0)).toBe(0);
  70  |       expect(new URL(page.url()).searchParams.get('as_of')).toBe(cutoff);
  71  |       await page.locator('input[name="vps"]').fill('12');
  72  |       await page
  73  |         .locator('form')
  74  |         .filter({ has: page.locator('input[name="vps"]') })
  75  |         .locator('button[type="submit"]')
  76  |         .click();
  77  |       await expect.poll(() => Number(fixture.overviewQueries.at(-1)?.['vps'])).toBe(12);
  78  |       expect(Number(fixture.overviewQueries.at(-1)?.['offset'])).toBe(0);
  79  |       expect(fixture.overviewQueries.at(-1)?.['as_of']).toBe(cutoff);
  80  |       await expect(
  81  |         page.locator('a[href="/admin/vps/12/incidents#incident-policy-policy-0"]').filter({ visible: true })
  82  |       ).toBeVisible();
  83  |       await expectNoDocumentHorizontalOverflow(page);
  84  |       await page.screenshot({
  85  |         path: testInfo.outputPath(`filtered-overview-${language}-${mobile ? 'mobile' : 'desktop'}.png`),
  86  |         fullPage: true,
  87  |       });
  88  |       const reads = fixture.overviewQueries.length;
  89  |       await page
  90  |         .locator('form')
  91  |         .filter({ has: page.locator('input[name="vps"]') })
  92  |         .locator('button[type="button"]')
  93  |         .click();
  94  |       await expect.poll(() => fixture.overviewQueries.length).toBe(reads + 1);
  95  |       expect(fixture.overviewQueries.at(-1)?.['as_of']).toBeUndefined();
  96  |       await expect.poll(() => new URL(page.url()).searchParams.get('as_of')).not.toBe(cutoff);
  97  |       await page.getByTestId('incidents.admin.tabs').locator('a[href="/admin/incidents/history"]').click();
  98  |       await expect(page.getByTestId('incidents.admin.history')).toBeVisible();
  99  |       await expect.poll(() => fixture.historyQueries.length).toBeGreaterThan(0);
  100 |       await expect(
  101 |         page.getByTestId(mobile ? 'incidents.admin.history.mobile' : 'incidents.admin.history.rows')
  102 |       ).toBeVisible();
  103 | 
  104 |       if (!mobile) {
  105 |         const widths = await page.getByTestId('incidents.admin.history.rows').evaluate((table) => ({
  106 |           content: table.parentElement!.clientWidth,
  107 |           scroll: table.parentElement!.scrollWidth,
  108 |           right: table.querySelector('th:last-child')!.getBoundingClientRect().right,
  109 |         }));
  110 |         expect(widths.scroll).toBeLessThanOrEqual(widths.content + 1);
  111 |         expect(widths.right).toBeLessThanOrEqual(1280);
  112 |       }
  113 |       expect(fixture.historyQueries.at(-1)).not.toHaveProperty('sort');
  114 |       await expect(page.locator('select').filter({ has: page.locator('option[value="evaluated_at"]') })).toHaveCount(0);
  115 |       await expectNoDocumentHorizontalOverflow(page);
  116 |       await page.screenshot({
  117 |         path: testInfo.outputPath(`initial-history-${language}-${mobile ? 'mobile' : 'desktop'}.png`),
  118 |         fullPage: true,
  119 |       });
  120 |       await page
  121 |         .locator('select')
  122 |         .filter({ has: page.locator('option[value="outstanding"]') })
  123 |         .selectOption('outstanding');
  124 |       await expect.poll(() => fixture.historyQueries.at(-1)?.['scope']).toBe('outstanding');
  125 |       await expect(page.locator('input[name="from"]')).toBeDisabled();
  126 |       await expect(page.locator('input[name="to"]')).toBeDisabled();
  127 |       await page.getByTestId('incidents.admin.tabs').locator('a[href="/admin/incidents"]').click();
  128 |       await expect(page.getByTestId('incidents.list.header')).toBeVisible();
  129 |       expect(new URL(page.url()).pathname).toBe('/admin/incidents');
  130 |     });
  131 |   }
  132 | }
  133 | 
  134 | for (const level of [1, 21]) {
  135 |   test(`new admin policy routes deny role level ${level} without endpoint reads`, async ({ page }) => {
  136 |     const fixture = await installAdminIncidentFixture(page, 'en', level);
  137 |     await page.goto('/admin/incidents/overview');
> 138 |     await expect(page.getByTestId('forbidden.page')).toBeVisible();
      |                                                      ^ Error: expect(locator).toBeVisible() failed
  139 |     expect(fixture.overviewQueries).toHaveLength(0);
  140 |     expect(fixture.historyQueries).toHaveLength(0);
  141 |   });
  142 | }
  143 | test('missing new capabilities keep Reports reachable without endpoint reads', async ({ page }) => {
  144 |   const fixture = await installAdminIncidentFixture(page, 'en', 90, false);
  145 |   await page.goto('/admin/incidents/overview');
  146 |   await expect(page.getByTestId('incidents.admin.overview')).toBeVisible();
  147 |   await expect(page.getByTestId('incidents.admin.paging')).toHaveCount(0);
  148 |   expect(fixture.overviewQueries).toHaveLength(0);
  149 |   await page.getByTestId('incidents.admin.tabs').locator('a[href="/admin/incidents"]').click();
  150 |   await expect(page.getByTestId('incidents.list.header')).toBeVisible();
  151 | });
  152 | 
```