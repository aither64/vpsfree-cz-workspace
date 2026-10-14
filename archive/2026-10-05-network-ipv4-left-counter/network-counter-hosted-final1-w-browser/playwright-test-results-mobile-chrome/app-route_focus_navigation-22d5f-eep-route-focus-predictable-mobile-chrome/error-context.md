# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/route_focus_navigation.spec.ts >> @pr-smoke @pr-smoke-mobile @smoke @smoke-mobile keyboard users can skip chrome and keep route focus predictable
- Location: e2e/specs/app/route_focus_navigation.spec.ts:34:1

# Error details

```
Error: expect(page).toHaveURL(expected) failed

Expected pattern: /\/app\/vps$/
Received string:  "http://127.0.0.1:5173/app"
Timeout: 15000ms

Call log:
  - Expect "toHaveURL" with timeout 15000ms
    34 × unexpected value "http://127.0.0.1:5173/app"

```

```yaml
- link "Skip to main content":
  - /url: "#main-content"
- banner:
  - button "Open navigation"
  - button "Search"
  - text: Mine
  - button "Open tasks"
  - button "Open account menu"
- main:
  - heading "Dashboard" [level=1]
  - paragraph: A focused daily overview of your resources, outages, security advisories, and service health.
  - text: "Signed in as alice (role: admin) Status data is incomplete Some operational sources could not be loaded. The cards below show what is available."
  - region "Dashboard preferences":
    - text: Dashboard preferencesCompact · 0 hidden · 0 collapsed
    - button "Customize"
  - text: VPS 1 In your current scope
  - link "Open":
    - /url: /app/vps
  - text: DNS 0 In your current scope
  - link "Open":
    - /url: /app/dns
  - text: Event log and news Latest announcements, trimmed to the essentials
  - button "Collapse"
  - link "All news":
    - /url: /news
  - text: Failed to load news Outages and maintenance 0 active · 0 planned
  - button "Collapse"
  - link "Open outages":
    - /url: /outages
  - text: Failed to load outages Security advisories Recent published advisories and CVEs.
  - button "Collapse"
  - link "View advisories":
    - /url: /security-advisories
  - text: Failed to load security advisories Cluster status 0 nodes · 0 need attention
  - button "Collapse"
  - text: Failed to load node status
```

# Test source

```ts
  1   | import { expect, test, type Page } from '@playwright/test';
  2   | 
  3   | import { bootstrapVpsAdminWindow, installHaveApiMock } from '../../fixtures';
  4   | 
  5   | type ScrollTrackingWindow = Window & { __routeFocusScrollToCalls: number };
  6   | 
  7   | async function installScrollTracker(page: Page) {
  8   |   await page.evaluate(() => {
  9   |     const trackedWindow = window as ScrollTrackingWindow;
  10  |     const originalScrollTo = window.scrollTo.bind(window);
  11  |     trackedWindow.__routeFocusScrollToCalls = 0;
  12  |     window.scrollTo = ((first?: number | ScrollToOptions, second?: number) => {
  13  |       trackedWindow.__routeFocusScrollToCalls += 1;
  14  |       if (typeof first === 'number') originalScrollTo(first, second ?? 0);
  15  |       else originalScrollTo(first);
  16  |     }) as typeof window.scrollTo;
  17  |   });
  18  | }
  19  | 
  20  | async function resetScrollTracker(page: Page) {
  21  |   await page.evaluate(() => {
  22  |     (window as ScrollTrackingWindow).__routeFocusScrollToCalls = 0;
  23  |   });
  24  | }
  25  | 
  26  | async function scrollToCallCount(page: Page) {
  27  |   return page.evaluate(() => (window as ScrollTrackingWindow).__routeFocusScrollToCalls);
  28  | }
  29  | 
  30  | async function settleAnimationFrames(page: Page) {
  31  |   await page.evaluate(() => new Promise<void>((resolve) => requestAnimationFrame(() => requestAnimationFrame(() => resolve()))));
  32  | }
  33  | 
  34  | test('@pr-smoke @pr-smoke-mobile @smoke @smoke-mobile keyboard users can skip chrome and keep route focus predictable', async ({ page, browserName }, testInfo) => {
  35  |   await bootstrapVpsAdminWindow(page, { sessionToken: 'KEYBOARD_USER_SESSION' });
  36  |   await installHaveApiMock(page, {
  37  |     user: { id: 10, login: 'alice', level: 100 },
  38  |     handlers: {
  39  |       'GET vpses': () => ({
  40  |         vpses: [{ id: 101, hostname: 'alpha', is_running: true, object_state: 'active' }],
  41  |         _meta: { total_count: 1 },
  42  |       }),
  43  |       'GET datasets': () => ({ datasets: [], _meta: { total_count: 0 } }),
  44  |       'GET dns_zones': () => ({ dns_zones: [], _meta: { total_count: 0 } }),
  45  |     },
  46  |   });
  47  | 
  48  |   await page.goto('/app');
  49  |   await installScrollTracker(page);
  50  |   await page.addStyleTag({ content: '#main-content { min-height: 2500px; }' });
  51  |   const main = page.getByTestId('shell.main');
  52  |   const skipLink = page.getByTestId('shell.skip-link');
  53  |   await expect(page.getByTestId('app.dashboard.page')).toBeVisible();
  54  |   await expect(main).not.toBeFocused();
  55  | 
  56  |   // WebKit on macOS uses Option+Tab to include links in keyboard traversal.
  57  |   await page.keyboard.press(browserName === 'webkit' ? 'Alt+Tab' : 'Tab');
  58  |   await expect(skipLink).toBeFocused();
  59  |   await expect(skipLink).toBeVisible();
  60  |   await expect(skipLink).not.toHaveCSS('box-shadow', 'none');
  61  |   await page.keyboard.press('Enter');
  62  |   await expect(main).toBeFocused();
  63  |   await expect(main).toHaveCSS('outline-style', 'none');
  64  |   await page.evaluate(() => window.history.replaceState(window.history.state, '', '/app'));
  65  |   await expect(page).toHaveURL(/\/app$/);
  66  | 
  67  |   await page.evaluate(async () => {
  68  |     window.scrollTo({ top: document.body.scrollHeight, behavior: 'auto' });
  69  |     await new Promise<void>((resolve) => requestAnimationFrame(() => requestAnimationFrame(() => resolve())));
  70  |   });
  71  |   await expect.poll(() => page.evaluate(() => window.scrollY)).toBeGreaterThan(200);
  72  |   await resetScrollTracker(page);
  73  | 
  74  |   if (testInfo.project.name === 'mobile-chrome') {
  75  |     const menuButton = page.getByTestId('shell.mobile-nav-button');
  76  |     await menuButton.focus();
  77  |     await page.keyboard.press('Enter');
  78  |     await expect(page.getByTestId('nav.drawer')).toBeVisible();
  79  |     await page.keyboard.press('Escape');
  80  |     await expect(page.getByTestId('nav.drawer')).toBeHidden();
  81  |     await expect(menuButton).toBeFocused();
  82  | 
  83  |     await page.keyboard.press('Enter');
  84  |     await expect(page.getByTestId('nav.drawer')).toBeVisible();
  85  |     const vpsLink = page.getByTestId('nav.drawer.vps');
  86  |     await vpsLink.focus();
  87  |     await expect.poll(() => page.evaluate(() => window.scrollY)).toBeGreaterThan(200);
  88  |     await page.keyboard.press('Enter');
  89  |     await expect(page.getByTestId('nav.drawer')).toBeHidden();
  90  |   } else {
  91  |     const vpsLink = page.getByTestId('nav.sidebar.vps');
  92  |     await vpsLink.focus();
  93  |     await expect.poll(() => page.evaluate(() => window.scrollY)).toBeGreaterThan(200);
  94  |     await page.keyboard.press('Enter');
  95  |   }
  96  | 
> 97  |   await expect(page).toHaveURL(/\/app\/vps$/);
      |                      ^ Error: expect(page).toHaveURL(expected) failed
  98  |   await expect(page.getByTestId('vps.list')).toBeVisible();
  99  |   await expect(main).toBeFocused();
  100 |   await expect(main).toHaveCSS('outline-style', 'none');
  101 |   await expect.poll(() => page.evaluate(() => window.scrollY)).toBe(0);
  102 |   await settleAnimationFrames(page);
  103 |   expect(await scrollToCallCount(page)).toBe(1);
  104 | 
  105 |   if (testInfo.project.name === 'mobile-chrome') {
  106 |     const menuButton = page.getByTestId('shell.mobile-nav-button');
  107 |     await menuButton.focus();
  108 |     await page.keyboard.press('Enter');
  109 |     await expect(page.getByTestId('nav.drawer')).toBeVisible();
  110 | 
  111 |     await resetScrollTracker(page);
  112 |     await page.goBack();
  113 |     await expect(page).toHaveURL(/\/app$/);
  114 |     await expect(page.getByTestId('nav.drawer')).toBeHidden();
  115 |     await expect(main).toBeFocused();
  116 |     await expect(main).toHaveCSS('outline-style', 'none');
  117 |     await settleAnimationFrames(page);
  118 |     expect(await scrollToCallCount(page)).toBe(0);
  119 | 
  120 |     await page.goForward();
  121 |     await expect(page).toHaveURL(/\/app\/vps(?:\?.*)?$/);
  122 |     await expect(main).toBeFocused();
  123 |     await expect(main).toHaveCSS('outline-style', 'none');
  124 |     await settleAnimationFrames(page);
  125 |     expect(await scrollToCallCount(page)).toBe(0);
  126 |   }
  127 | 
  128 |   const smartFilter = page.getByTestId('vps.smart_filter.input');
  129 |   await resetScrollTracker(page);
  130 |   await smartFilter.fill('alpha');
  131 |   await smartFilter.press('Enter');
  132 |   await expect(page).toHaveURL(/\/app\/vps\?.*q=alpha/);
  133 |   await expect(smartFilter).toBeFocused();
  134 |   await expect(smartFilter).not.toHaveCSS('box-shadow', 'none');
  135 |   await settleAnimationFrames(page);
  136 |   expect(await scrollToCallCount(page)).toBe(0);
  137 | 
  138 |   await page.evaluate(async () => {
  139 |     window.scrollTo({ top: document.body.scrollHeight, behavior: 'auto' });
  140 |     await new Promise<void>((resolve) => requestAnimationFrame(() => requestAnimationFrame(() => resolve())));
  141 |   });
  142 |   await expect.poll(() => page.evaluate(() => window.scrollY)).toBeGreaterThan(200);
  143 |   await resetScrollTracker(page);
  144 |   await page.getByTestId('shell.user-menu-button').click();
  145 |   await expect.poll(() => page.evaluate(() => window.scrollY)).toBeGreaterThan(200);
  146 |   const beforeScopeSwitchY = await page.evaluate(() => window.scrollY);
  147 |   await page.getByTestId('shell.user-menu.scope.all').click();
  148 | 
  149 |   await expect(page).toHaveURL(/\/admin\/vps\?.*q=alpha/);
  150 |   await expect(page.getByTestId('vps.list')).toBeVisible();
  151 |   await expect(page.getByTestId('shell.main')).toBeFocused();
  152 |   await expect.poll(() => page.evaluate(() => window.scrollY)).toBe(0);
  153 |   await settleAnimationFrames(page);
  154 |   expect(await scrollToCallCount(page)).toBe(1);
  155 | 
  156 |   await resetScrollTracker(page);
  157 |   await page.goBack();
  158 |   await expect(page).toHaveURL(/\/app\/vps\?.*q=alpha/);
  159 |   await expect(page.getByTestId('vps.list')).toBeVisible();
  160 |   await expect(page.getByTestId('shell.main')).toBeFocused();
  161 |   await settleAnimationFrames(page);
  162 |   expect(await scrollToCallCount(page)).toBe(0);
  163 |   await expect.poll(() => page.evaluate((expected) => Math.abs(window.scrollY - expected), beforeScopeSwitchY)).toBeLessThanOrEqual(2);
  164 | });
  165 | 
```