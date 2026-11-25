# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/admin_incident_policies.spec.ts >> admin policy Overview/History en mobile=false
- Location: e2e/specs/app/admin_incident_policies.spec.ts:43:5

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: getByText('SYNTHETIC policy 1', { exact: true }).filter({ visible: true })
Expected: visible
Timeout: 15000ms
Error: element(s) not found

Call log:
  - Expect "toBeVisible" with timeout 15000ms
  - waiting for getByText('SYNTHETIC policy 1', { exact: true }).filter({ visible: true })

```

```yaml
- link "Skip to main content":
  - /url: "#main-content"
- complementary:
  - search:
    - combobox "Quickly search objects"
  - button "Open tasks": Tasks
  - 'button "Account: synthetic-admin"': synthetic-admin All Admin
  - navigation:
    - link "Dashboard":
      - /url: /admin
    - region "Services":
      - text: Services
      - link "VPS":
        - /url: /admin/vps
      - link "Datasets":
        - /url: /admin/datasets
      - link "NAS":
        - /url: /admin/nas
      - link "Exports":
        - /url: /admin/exports
      - link "DNS":
        - /url: /admin/dns
      - link "Networking":
        - /url: /admin/networking/ip-addresses
    - region "Operations":
      - text: Operations
      - link "Transactions":
        - /url: /admin/transactions
      - link "Monitoring":
        - /url: /admin/monitoring
      - link "Incidents":
        - /url: /admin/incidents/overview
      - link "Out-of-memory":
        - /url: /admin/oom-reports
      - link "Audit":
        - /url: /admin/audit
    - region "Users and finance":
      - text: Users and finance
      - link "Users":
        - /url: /admin/users
      - link "User namespaces":
        - /url: /admin/user-namespaces/namespaces
      - link "Requests":
        - /url: /admin/requests
      - link "Finance":
        - /url: /admin/payments/incoming
    - region "Infrastructure":
      - text: Infrastructure
      - link "Cluster":
        - /url: /admin/cluster/summary
      - link "Nodes":
        - /url: /admin/nodes
      - link "Migration plans":
        - /url: /admin/migration-plans
      - link "Admin":
        - /url: /admin/admin-info
    - region "Content":
      - text: Content
      - link "Mailer":
        - /url: /admin/mailer/templates
      - link "News and help":
        - /url: /admin/content/news
    - link "Outages":
      - /url: /admin/outages
    - link "Security advisories":
      - /url: /admin/security-advisories
  - text: vpsAdmin
  - link "About":
    - /url: /about
  - link "View commit c27d70dbd4e9*":
    - /url: https://github.com/vpsfreecz/vpsadmin-webui/commit/c27d70dbd4e96540de4d58027bfa6fce09a4df15
    - text: c27d70dbd4e9*
- main:
  - heading "Overview" [level=1]
  - paragraph: All VPSes with current policy matches, including those below the thresholds.
  - link "Overview":
    - /url: /admin/incidents/overview?as_of=2026-11-24T10%3A00%3A00.000Z&vps=12
  - link "Reports":
    - /url: /admin/incidents
  - link "History":
    - /url: /admin/incidents/history
  - text: The cutoff sets the counting windows. Settings, ownership and action outcomes reflect the latest read. Refresh sets a new cutoff. Reports remaining is the number needed to reach a threshold. Counts can fall as older reports leave the window. Neither this number nor the end of a cooldown guarantees an action on the next report. Policy key
  - textbox "Policy key"
  - text: VPS ID
  - textbox "VPS ID": "12"
  - text: Owner ID
  - textbox "Owner ID"
  - text: Node ID
  - textbox "Node ID"
  - text: Threshold status
  - combobox "Threshold status":
    - option "All" [selected]
    - option "Below thresholds"
    - option "Near a threshold"
    - option "Warning threshold reached"
    - option "Shutdown threshold reached"
    - option "Invalid configuration"
  - text: Effective mode
  - combobox "Effective mode":
    - option "All" [selected]
    - option "Observation only"
    - option "Warnings only"
    - option "Warnings and automatic shutdown"
  - text: Automatic shutdown allowed
  - combobox "Automatic shutdown allowed":
    - option "All" [selected]
    - option "Yes"
    - option "No"
  - text: Order by
  - combobox "Order by":
    - option "Priority" [selected]
    - option "VPS ID"
    - option "Owner login"
    - option "Policy key"
    - option "7-day incident count"
    - option "30-day incident count"
    - option "Reports until warning threshold"
    - option "Reports until shutdown threshold"
    - option "Last counted incident"
  - text: Direction
  - combobox "Direction":
    - option "Descending" [selected]
    - option "Ascending"
  - button "Apply filters"
  - button "Refresh"
  - text: "Counting cutoff: 11/24/2026, 11:00:00 AM Current facts read at: 11/24/2026, 11:01:00 AM"
  - table:
    - rowgroup:
      - row "VPS / owner Policy Warning threshold Shutdown threshold Threshold status Mode and restrictions Latest recorded outcome":
        - columnheader "VPS / owner"
        - columnheader "Policy"
        - columnheader "Warning threshold"
        - columnheader "Shutdown threshold"
        - columnheader "Threshold status"
        - columnheader "Mode and restrictions"
        - columnheader "Latest recorded outcome"
    - rowgroup:
      - 'row "#12 synthetic-0.example.test demo-owner (#4) node.example.test (#5) SYNTHETIC policy 1 policy-0 2 / 3 incidents in 7 days Reports remaining to threshold: 1 4 / 10 incidents in 30 days Reports remaining to threshold: 6 Below thresholds Last counted incident: 11/24/2026, 11:00:00 AM Effective mode: Warnings and automatic shutdown Global mode: Warnings and automatic shutdown Warning emails allowed: Yes Automatic shutdown allowed: No No recorded action"':
        - cell "#12 synthetic-0.example.test demo-owner (#4) node.example.test (#5)":
          - link "#12 synthetic-0.example.test":
            - /url: /admin/vps/12
          - link "demo-owner (#4)":
            - /url: /admin/users/4
          - text: node.example.test (#5)
        - cell "SYNTHETIC policy 1 policy-0":
          - link "SYNTHETIC policy 1 policy-0":
            - /url: /admin/vps/12/incidents#incident-policy-policy-0
        - 'cell "2 / 3 incidents in 7 days Reports remaining to threshold: 1"'
        - 'cell "4 / 10 incidents in 30 days Reports remaining to threshold: 6"'
        - 'cell "Below thresholds Last counted incident: 11/24/2026, 11:00:00 AM"'
        - 'cell "Effective mode: Warnings and automatic shutdown Global mode: Warnings and automatic shutdown Warning emails allowed: Yes Automatic shutdown allowed: No"'
        - cell "No recorded action"
      - 'row "#12 synthetic-1.example.test demo-owner (#4) node.example.test (#5) SYNTHETIC policy 2 policy-1 3 / 3 incidents in 7 days Threshold reached 4 / 10 incidents in 30 days Reports remaining to threshold: 6 Warning threshold reached Last counted incident: 11/24/2026, 11:00:00 AM Effective mode: Warnings and automatic shutdown Global mode: Warnings and automatic shutdown Warning emails allowed: Yes Automatic shutdown allowed: No No recorded action"':
        - cell "#12 synthetic-1.example.test demo-owner (#4) node.example.test (#5)":
          - link "#12 synthetic-1.example.test":
            - /url: /admin/vps/12
          - link "demo-owner (#4)":
            - /url: /admin/users/4
          - text: node.example.test (#5)
        - cell "SYNTHETIC policy 2 policy-1":
          - link "SYNTHETIC policy 2 policy-1":
            - /url: /admin/vps/12/incidents#incident-policy-policy-1
        - cell "3 / 3 incidents in 7 days Threshold reached"
        - 'cell "4 / 10 incidents in 30 days Reports remaining to threshold: 6"'
        - 'cell "Warning threshold reached Last counted incident: 11/24/2026, 11:00:00 AM"'
        - 'cell "Effective mode: Warnings and automatic shutdown Global mode: Warnings and automatic shutdown Warning emails allowed: Yes Automatic shutdown allowed: No"'
        - cell "No recorded action"
  - text: Rows 1–2 of 2
  - button "Prev" [disabled]
  - button "Next" [disabled]
  - text: Rows per page
  - combobox "Rows per page":
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
  58  |       expect(cutoff).toBeTruthy();
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
> 71  |       await expect(page.getByText('SYNTHETIC policy 1', { exact: true }).filter({ visible: true })).toBeVisible();
      |                                                                                                     ^ Error: expect(locator).toBeVisible() failed
  72  |       await expectNoDocumentHorizontalOverflow(page);
  73  |       await page.screenshot({
  74  |         path: testInfo.outputPath(`filtered-overview-${language}-${mobile ? 'mobile' : 'desktop'}.png`),
  75  |         fullPage: true,
  76  |       });
  77  |       const reads = fixture.overviewQueries.length;
  78  |       await page
  79  |         .locator('form')
  80  |         .filter({ has: page.locator('input[name="vps"]') })
  81  |         .locator('button[type="button"]')
  82  |         .click();
  83  |       await expect.poll(() => fixture.overviewQueries.length).toBe(reads + 1);
  84  |       expect(fixture.overviewQueries.at(-1)?.['as_of']).toBeUndefined();
  85  |       await expect.poll(() => new URL(page.url()).searchParams.get('as_of')).not.toBe(cutoff);
  86  |       await page.getByTestId('incidents.admin.tabs').locator('a[href="/admin/incidents/history"]').click();
  87  |       await expect(page.getByTestId('incidents.admin.history')).toBeVisible();
  88  |       await expect.poll(() => fixture.historyQueries.length).toBeGreaterThan(0);
  89  |       await expect(
  90  |         page.getByTestId(mobile ? 'incidents.admin.history.mobile' : 'incidents.admin.history.rows')
  91  |       ).toBeVisible();
  92  |       expect(fixture.historyQueries.at(-1)).not.toHaveProperty('sort');
  93  |       await expect(page.locator('select').filter({ has: page.locator('option[value="evaluated_at"]') })).toHaveCount(0);
  94  |       await expectNoDocumentHorizontalOverflow(page);
  95  |       await page.screenshot({
  96  |         path: testInfo.outputPath(`initial-history-${language}-${mobile ? 'mobile' : 'desktop'}.png`),
  97  |         fullPage: true,
  98  |       });
  99  |       await page
  100 |         .locator('select')
  101 |         .filter({ has: page.locator('option[value="outstanding"]') })
  102 |         .selectOption('outstanding');
  103 |       await expect.poll(() => fixture.historyQueries.at(-1)?.['scope']).toBe('outstanding');
  104 |       await expect(page.locator('input[name="from"]')).toBeDisabled();
  105 |       await expect(page.locator('input[name="to"]')).toBeDisabled();
  106 |       await page.getByTestId('incidents.admin.tabs').locator('a[href="/admin/incidents"]').click();
  107 |       await expect(page.getByTestId('incidents.list.header')).toBeVisible();
  108 |       expect(new URL(page.url()).pathname).toBe('/admin/incidents');
  109 |     });
  110 |   }
  111 | }
  112 | 
  113 | for (const level of [1, 21]) {
  114 |   test(`new admin policy routes deny role level ${level} without endpoint reads`, async ({ page }) => {
  115 |     const fixture = await installAdminIncidentFixture(page, 'en', level);
  116 |     await page.goto('/admin/incidents/overview');
  117 |     await expect(page.getByTestId('forbidden.page')).toBeVisible();
  118 |     expect(fixture.overviewQueries).toHaveLength(0);
  119 |     expect(fixture.historyQueries).toHaveLength(0);
  120 |   });
  121 | }
  122 | test('missing new capabilities keep Reports reachable without endpoint reads', async ({ page }) => {
  123 |   const fixture = await installAdminIncidentFixture(page, 'en', 90, false);
  124 |   await page.goto('/admin/incidents/overview');
  125 |   await expect(page.getByTestId('incidents.admin.overview')).toBeVisible();
  126 |   await expect(page.getByTestId('incidents.admin.paging')).toHaveCount(0);
  127 |   expect(fixture.overviewQueries).toHaveLength(0);
  128 |   await page.getByTestId('incidents.admin.tabs').locator('a[href="/admin/incidents"]').click();
  129 |   await expect(page.getByTestId('incidents.list.header')).toBeVisible();
  130 | });
  131 | 
```