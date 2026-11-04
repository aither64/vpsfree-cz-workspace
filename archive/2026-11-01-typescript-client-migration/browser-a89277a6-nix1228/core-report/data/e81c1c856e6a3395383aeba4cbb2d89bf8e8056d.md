# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/payments_page.spec.ts >> user payments page: shows status, instructions and history
- Location: e2e/specs/app/payments_page.spec.ts:9:1

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: getByTestId('payments.my.instructions.text').getByRole('heading', { name: 'Payment in CZK' })
Expected: visible
Timeout: 15000ms
Error: element(s) not found

Call log:
  - Expect "toBeVisible" with timeout 15000ms
  - waiting for getByTestId('payments.my.instructions.text').getByRole('heading', { name: 'Payment in CZK' })

```

```yaml
- link "Skip to main content":
  - /url: "#main-content"
- complementary:
  - text: VA vpsAdmin next UI
  - navigation:
    - link "Dashboard":
      - /url: /app
    - link "VPS":
      - /url: /app/vps
    - link "NAS":
      - /url: /app/nas
    - link "Backups":
      - /url: /app/backups
    - link "Exports":
      - /url: /app/exports
    - link "DNS":
      - /url: /app/dns
    - link "Networking":
      - /url: /app/networking
    - link "Transactions":
      - /url: /app/transactions
    - link "Monitoring":
      - /url: /app/monitoring
    - link "Incidents":
      - /url: /app/incidents
    - link "Out-of-memory":
      - /url: /app/oom-reports
    - link "Payments":
      - /url: /app/payments
    - link "My requests":
      - /url: /app/requests
    - link "Account":
      - /url: /app/profile
  - navigation "Service status":
    - link "Outages":
      - /url: /outages
    - link "Security advisories":
      - /url: /security-advisories
  - link "About":
    - /url: /about
  - link "View commit a89277a6a4bc":
    - /url: https://github.com/vpsfreecz/vpsadmin-webui/commit/a89277a6a4bcd7b5849d48f760c9728982c67aa9
    - text: a89277a6a4bc
- banner:
  - search:
    - combobox "Quickly search objects"
    - text: Ctrl K · /
  - button "Open tasks": Tasks
  - button "Open account menu": alice user
- main:
  - heading "Payments" [level=1]
  - paragraph: Your membership payments and payment instructions.
  - text: Paid until in 26359 days 1/1/2099, 1:00:00 AM Paid Monthly payment Default monthly payment amount. 200 Payment ID Use this identifier when paying (e.g. variable symbol). 1 Payment instructions Unable to load payment instructions Please try again.
  - button "Retry"
  - button "Back"
  - link "Status":
    - /url: /
  - button "Copy details"
  - group: Details
  - text: Payment history Accepted payments extending your account.
  - table:
    - rowgroup:
      - row "Created Amount Period":
        - columnheader "Created"
        - columnheader "Amount"
        - columnheader "Period"
    - rowgroup:
      - row "2/14/2026, 10:00:00 AM 200 2/1/2026 → 3/1/2026":
        - cell "2/14/2026, 10:00:00 AM"
        - cell "200"
        - cell "2/1/2026 → 3/1/2026"
      - row "2/14/2026, 10:00:00 AM 200 2/1/2026 → 3/1/2026":
        - cell "2/14/2026, 10:00:00 AM"
        - cell "200"
        - cell "2/1/2026 → 3/1/2026"
      - row "2/14/2026, 10:00:00 AM 200 2/1/2026 → 3/1/2026":
        - cell "2/14/2026, 10:00:00 AM"
        - cell "200"
        - cell "2/1/2026 → 3/1/2026"
      - row "2/14/2026, 10:00:00 AM 200 2/1/2026 → 3/1/2026":
        - cell "2/14/2026, 10:00:00 AM"
        - cell "200"
        - cell "2/1/2026 → 3/1/2026"
      - row "2/14/2026, 10:00:00 AM 200 2/1/2026 → 3/1/2026":
        - cell "2/14/2026, 10:00:00 AM"
        - cell "200"
        - cell "2/1/2026 → 3/1/2026"
      - row "2/14/2026, 10:00:00 AM 200 2/1/2026 → 3/1/2026":
        - cell "2/14/2026, 10:00:00 AM"
        - cell "200"
        - cell "2/1/2026 → 3/1/2026"
      - row "2/14/2026, 10:00:00 AM 200 2/1/2026 → 3/1/2026":
        - cell "2/14/2026, 10:00:00 AM"
        - cell "200"
        - cell "2/1/2026 → 3/1/2026"
      - row "2/14/2026, 10:00:00 AM 200 2/1/2026 → 3/1/2026":
        - cell "2/14/2026, 10:00:00 AM"
        - cell "200"
        - cell "2/1/2026 → 3/1/2026"
      - row "2/14/2026, 10:00:00 AM 200 2/1/2026 → 3/1/2026":
        - cell "2/14/2026, 10:00:00 AM"
        - cell "200"
        - cell "2/1/2026 → 3/1/2026"
      - row "2/14/2026, 10:00:00 AM 200 2/1/2026 → 3/1/2026":
        - cell "2/14/2026, 10:00:00 AM"
        - cell "200"
        - cell "2/1/2026 → 3/1/2026"
  - button "Prev" [disabled]
  - button "Page 1 (current)": "1"
  - button "Next" [disabled]
  - text: Page 1 Rows
  - combobox:
    - option "25"
    - option "50" [selected]
    - option "100"
```

# Test source

```ts
  1   | import { test, expect } from '@playwright/test';
  2   | 
  3   | import { bootstrapVpsAdminWindow } from '../../fixtures/bootstrap';
  4   | import { installHaveApiMock } from '../../fixtures/haveapi';
  5   | import { withAppUrl } from '../../fixtures/url';
  6   | 
  7   | const UI_SETTINGS_STORAGE_KEY = 'vpsadmin.uiSettings.v1';
  8   | 
  9   | test('user payments page: shows status, instructions and history', async ({ page }) => {
  10  |   test.setTimeout(90_000);
  11  | 
  12  |   await bootstrapVpsAdminWindow(page);
  13  |   const haveApiMock = await installHaveApiMock(page);
  14  | 
  15  |   haveApiMock.addHandler('GET users/current', () => {
  16  |     return {
  17  |       user: {
  18  |         id: 1,
  19  |         login: 'alice',
  20  |         level: 1,
  21  |         monthly_payment: 200,
  22  |         paid_until: '2099-01-01T00:00:00Z',
  23  |       },
  24  |     };
  25  |   });
  26  | 
  27  |   haveApiMock.addHandler('GET users/1/get_payment_instructions', () => {
  28  |     return {
  29  |       hash: {
  30  |         instructions: '<h3>Payment in CZK</h3><table><tr><td>IBAN:</td><td>CZ00TEST</td></tr><tr><td>VS:</td><td>1</td></tr></table>',
  31  |       },
  32  |     };
  33  |   });
  34  | 
  35  |   haveApiMock.addHandler('GET user_payments', ({ searchParams }) => {
  36  |     const limit = Number(searchParams.get('user_payment[limit]') ?? 50);
  37  |     const fromIdRaw = searchParams.get('user_payment[from_id]');
  38  |     const fromId = fromIdRaw ? Number(fromIdRaw) : null;
  39  | 
  40  |     const ids = Array.from({ length: 10 }, (_, i) => 300 - i)
  41  |       .filter((id) => (fromId ? id < fromId : true))
  42  |       .slice(0, limit);
  43  | 
  44  |     return {
  45  |       status: true,
  46  |       response: {
  47  |         user_payments: ids.map((id) => ({
  48  |           id,
  49  |           amount: 200,
  50  |           created_at: '2026-02-14T09:00:00Z',
  51  |           from_date: '2026-02-01T00:00:00Z',
  52  |           to_date: '2026-03-01T00:00:00Z',
  53  |         })),
  54  |       },
  55  |     };
  56  |   });
  57  | 
  58  |   await page.goto(withAppUrl('/app/payments'));
  59  | 
  60  |   await expect(page.getByTestId('payments.my.stat.paid_until')).toBeVisible({ timeout: 30_000 });
  61  |   await expect(page.getByTestId('payments.my.stat.paid_until').getByText('Paid', { exact: true })).toBeVisible();
  62  | 
  63  |   const instructions = page.getByTestId('payments.my.instructions.text');
> 64  |   await expect(instructions.getByRole('heading', { name: 'Payment in CZK' })).toBeVisible();
      |                                                                               ^ Error: expect(locator).toBeVisible() failed
  65  |   await expect(instructions.getByText('CZ00TEST')).toBeVisible();
  66  |   await expect(instructions).not.toContainText('<h3>');
  67  |   await expect(page.getByTestId('payments.my.instructions.copy')).toBeVisible();
  68  | 
  69  |   await expect(page.getByTestId('payments.my.history.table')).toBeVisible();
  70  |   await expect(page.getByTestId('payments.my.history.table').locator('tbody tr')).toHaveCount(10);
  71  | });
  72  | 
  73  | test('@pr-smoke @pr-smoke-mobile user payment history uses a hidden lookahead and stops on an exact terminal page', async ({ page }) => {
  74  |   await bootstrapVpsAdminWindow(page);
  75  |   const haveApiMock = await installHaveApiMock(page);
  76  |   const paymentRequests: Array<{ fromId: number | null; limit: number; userId: number | null }> = [];
  77  |   const allIds = Array.from({ length: 50 }, (_, index) => 400 - index);
  78  |   let revisitWithoutLookahead = false;
  79  | 
  80  |   haveApiMock.addHandler('GET users/current', () => ({
  81  |     user: {
  82  |       id: 1,
  83  |       login: 'alice',
  84  |       level: 1,
  85  |       monthly_payment: 200,
  86  |       paid_until: '2099-01-01T00:00:00Z',
  87  |     },
  88  |   }));
  89  |   haveApiMock.addHandler('GET users/1/get_payment_instructions', () => ({
  90  |     instructions: 'VS: 1',
  91  |   }));
  92  |   haveApiMock.addHandler('GET user_payments', ({ searchParams }) => {
  93  |     const limit = Number(searchParams.get('user_payment[limit]') ?? 50);
  94  |     const rawFromId = searchParams.get('user_payment[from_id]');
  95  |     const fromId = rawFromId ? Number(rawFromId) : null;
  96  |     const rawUserId = searchParams.get('user_payment[user]');
  97  |     const userId = rawUserId ? Number(rawUserId) : null;
  98  |     paymentRequests.push({ fromId, limit, userId });
  99  | 
  100 |     const responseLimit = fromId === null && revisitWithoutLookahead ? 25 : limit;
  101 |     const ids = allIds
  102 |       .filter((id) => (fromId === null ? true : id < fromId))
  103 |       .slice(0, responseLimit);
  104 | 
  105 |     return {
  106 |       user_payments: ids.map((id) => ({
  107 |         id,
  108 |         amount: id,
  109 |         created_at: '2026-02-14T09:00:00Z',
  110 |         from_date: '2026-02-01T00:00:00Z',
  111 |         to_date: '2026-03-01T00:00:00Z',
  112 |       })),
  113 |     };
  114 |   });
  115 | 
  116 |   await page.goto(withAppUrl('/app/payments?limit=25'));
  117 | 
  118 |   const tableRows = page.getByTestId('payments.my.history.table').locator('tbody tr');
  119 |   const next = page.getByTestId('payments.my.history.pagination.next');
  120 |   await expect(tableRows).toHaveCount(25);
  121 |   await expect(tableRows.first()).toContainText('400');
  122 |   await expect(tableRows.last()).toContainText('376');
  123 |   await expect(next).toBeEnabled();
  124 |   expect(paymentRequests[0]).toEqual({ fromId: null, limit: 26, userId: 1 });
  125 | 
  126 |   await next.click();
  127 | 
  128 |   await expect(page).toHaveURL(/(?:\?|&)from_id=376(?:&|$)/);
  129 |   await expect(tableRows).toHaveCount(25);
  130 |   await expect(tableRows.first()).toContainText('375');
  131 |   await expect(tableRows.last()).toContainText('351');
  132 |   await expect(next).toBeDisabled();
  133 |   const previous = page.getByTestId('payments.my.history.pagination.prev');
  134 |   await expect(previous).toBeEnabled();
  135 |   expect(paymentRequests.at(-1)).toEqual({ fromId: 376, limit: 26, userId: 1 });
  136 | 
  137 |   await previous.click();
  138 | 
  139 |   await expect(page).not.toHaveURL(/(?:\?|&)from_id=/);
  140 |   revisitWithoutLookahead = true;
  141 |   await page.reload();
  142 |   await expect(tableRows.first()).toContainText('400');
  143 |   await expect(tableRows.last()).toContainText('376');
  144 |   await expect(next).toBeEnabled();
  145 |   expect(paymentRequests.at(-1)).toEqual({ fromId: null, limit: 26, userId: 1 });
  146 | 
  147 |   await next.click();
  148 | 
  149 |   await expect(page).toHaveURL(/(?:\?|&)from_id=376(?:&|$)/);
  150 |   await expect(tableRows.first()).toContainText('375');
  151 |   await expect(tableRows.last()).toContainText('351');
  152 |   await expect(next).toBeDisabled();
  153 | });
  154 | 
  155 | test('user payments page: localizes and constrains legacy payment instruction HTML', async ({ page }) => {
  156 |   test.setTimeout(90_000);
  157 | 
  158 |   await bootstrapVpsAdminWindow(page);
  159 |   await page.addInitScript(({ storageKey }) => {
  160 |     window.localStorage.setItem(
  161 |       storageKey,
  162 |       JSON.stringify({
  163 |         sidebarCollapsed: false,
  164 |         theme: 'system',
```