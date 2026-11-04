# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/authenticated_home_smoke.spec.ts >> @smoke authenticated dashboard skips HaveAPI description bootstrap in standalone mode
- Location: e2e/specs/app/authenticated_home_smoke.spec.ts:48:1

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: getByTestId('app.dashboard.page')
Expected: visible
Timeout: 15000ms
Error: element(s) not found

Call log:
  - Expect "toBeVisible" with timeout 15000ms
  - waiting for getByTestId('app.dashboard.page')

```

```yaml
- heading "Can’t load your session" [level=1]
- paragraph: vpsAdmin could not verify your login state. This is usually a network issue or a temporary backend error.
- paragraph: Invalid API description configuration
- button "Reload"
- link "Try signing in":
  - /url: http://127.0.0.1:5187/oauth/login?next=%2Fapp
- link "Go to status":
  - /url: /
```

# Test source

```ts
  1  | import { expect, test, type Request } from '@playwright/test';
  2  | 
  3  | import { bootstrapVpsAdminWindow, installHaveApiMock } from '../../fixtures';
  4  | 
  5  | test('@workflow-matrix @pr-smoke @pr-smoke-mobile @smoke @smoke-mobile authenticated user lands on dashboard and can open VPS list', async ({ page }) => {
  6  |   const vpsRequests: Request[] = [];
  7  |   page.on('request', request => {
  8  |     if (new URL(request.url()).pathname.endsWith('/vpses')) vpsRequests.push(request);
  9  |   });
  10 |   await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST_USER_SESSION' });
  11 | 
  12 |   await installHaveApiMock(page, {
  13 |     user: { id: 10, login: 'alice', level: 1 },
  14 |     handlers: {
  15 |       'GET vpses': () => ({
  16 |         vpses: [
  17 |           { id: 101, hostname: 'alpha', is_running: true, object_state: 'active' },
  18 |           { id: 102, hostname: 'beta', is_running: false, object_state: 'active' },
  19 |         ],
  20 |         _meta: { total_count: 2 },
  21 |       }),
  22 |       'GET datasets': () => ({ datasets: [{ id: 1 }], _meta: { total_count: 1 } }),
  23 |       'GET dns_zones': () => ({ dns_zones: [{ id: 1 }], _meta: { total_count: 1 } }),
  24 |       'GET transaction_chains': () => ({ transaction_chains: [], _meta: { total_count: 0 } }),
  25 |     },
  26 |   });
  27 | 
  28 |   await page.goto('/app');
  29 | 
  30 |   await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();
  31 |   await expect(page.getByText('Signed in as alice')).toBeVisible();
  32 |   await expect(page.getByTestId('app.dashboard.kpi.vps')).toContainText('VPS');
  33 |   await expect(page.getByTestId('app.dashboard.kpi.vps')).toContainText('2');
  34 |   await expect(page.getByText('Running:')).toHaveCount(0);
  35 | 
  36 |   await page.getByTestId('app.dashboard.kpi.vps').getByRole('link', { name: 'Open' }).click();
  37 | 
  38 |   await expect(page).toHaveURL(/\/app\/vps$/);
  39 |   await expect(page.getByRole('heading', { name: 'VPS' })).toBeVisible();
  40 |   await expect(page.getByRole('link', { name: /alpha/i })).toBeVisible();
  41 |   expect(vpsRequests.length).toBeGreaterThan(0);
  42 |   for (const request of vpsRequests) {
  43 |     expect(request.resourceType()).toBe('xhr');
  44 |     expect(request.headers()['x-haveapi-auth-token']).toBe('TEST_USER_SESSION');
  45 |   }
  46 | });
  47 | 
  48 | test('@smoke authenticated dashboard skips HaveAPI description bootstrap in standalone mode', async ({ page }) => {
  49 |   const descriptionRequests: string[] = [];
  50 | 
  51 |   page.on('request', (request) => {
  52 |     const url = new URL(request.url());
  53 |     if (
  54 |       ['GET', 'OPTIONS'].includes(request.method()) &&
  55 |       ['/api', '/api/', '/api/v7.0', '/api/v7.0/'].includes(url.pathname)
  56 |     ) {
  57 |       descriptionRequests.push(url.pathname);
  58 |     }
  59 |   });
  60 | 
  61 |   await bootstrapVpsAdminWindow(page, {
  62 |     sessionToken: 'TEST_USER_SESSION',
  63 |     description: false,
  64 |     webuiNext: {
  65 |       haveApi: {
  66 |         authHeader: 'X-HaveAPI-Auth-Token',
  67 |         metaNamespace: '_meta',
  68 |       },
  69 |     },
  70 |   });
  71 | 
  72 |   await installHaveApiMock(page, {
  73 |     user: { id: 10, login: 'alice', level: 1 },
  74 |     handlers: {
  75 |       'GET vpses': () => ({ vpses: [], _meta: { total_count: 0 } }),
  76 |       'GET datasets': () => ({ datasets: [], _meta: { total_count: 0 } }),
  77 |       'GET dns_zones': () => ({ dns_zones: [], _meta: { total_count: 0 } }),
  78 |       'GET transaction_chains': () => ({ transaction_chains: [], _meta: { total_count: 0 } }),
  79 |     },
  80 |   });
  81 | 
  82 |   await page.goto('/app');
  83 | 
> 84 |   await expect(page.getByTestId('app.dashboard.page')).toBeVisible();
     |                                                        ^ Error: expect(locator).toBeVisible() failed
  85 |   expect(descriptionRequests).toEqual([]);
  86 | });
  87 | 
```