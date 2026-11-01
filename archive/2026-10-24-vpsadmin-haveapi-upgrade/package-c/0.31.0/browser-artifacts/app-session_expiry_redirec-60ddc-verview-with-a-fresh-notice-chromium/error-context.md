# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/session_expiry_redirect.spec.ts >> @smoke expired session redirects to public overview with a fresh notice
- Location: e2e/specs/app/session_expiry_redirect.spec.ts:5:1

# Error details

```
Error: expect(page).toHaveURL(expected) failed

Expected pattern: /\/$/
Received string:  "http://127.0.0.1:52847/?session=expired"
Timeout: 15000ms

Call log:
  - Expect "toHaveURL" with timeout 15000ms
    26 × unexpected value "http://127.0.0.1:52847/app/vps"
    - waiting for" http://127.0.0.1:52847/?session=expired" navigation to finish...
    - navigated to "http://127.0.0.1:52847/?session=expired"
    - unexpected value "http://127.0.0.1:52847/?session=expired"

```

# Test source

```ts
  1  | import { expect, test } from '../../fixtures/playwright';
  2  | import { bootstrapVpsAdminWindow } from '../../fixtures/bootstrap';
  3  | import { installHaveApiMock, jsonFulfill } from '../../fixtures/haveapi';
  4  | 
  5  | test('@smoke expired session redirects to public overview with a fresh notice', async ({ page }) => {
  6  |   await bootstrapVpsAdminWindow(page, { sessionToken: 'EXPIRED_SESSION' });
  7  |   await installHaveApiMock(page, {
  8  |     handlers: {
  9  |       'GET users/current': () =>
  10 |         jsonFulfill({ status: false, message: 'Session expired', response: null }, 401),
  11 |       'GET cluster/public_stats': () => ({ public_stats: { user_count: 10, vps_count: 20, ipv4_left: 30 } }),
  12 |       'GET nodes/public_status': () => ({ nodes: [] }),
  13 |       'GET outages': () => ({ outages: [] }),
  14 |       'GET news_logs': () => ({ news_logs: [] }),
  15 |       'GET help_boxes': () => ({ help_boxes: [] }),
  16 |     },
  17 |   });
  18 | 
  19 |   await page.goto('/app/vps');
  20 | 
> 21 |   await expect(page).toHaveURL(/\/$/);
     |                      ^ Error: expect(page).toHaveURL(expected) failed
  22 |   await expect(page.getByTestId('public.overview.page')).toBeVisible({ timeout: 30_000 });
  23 |   await expect(page.getByTestId('auth.session-expired.notice')).toBeVisible();
  24 | });
  25 | 
```