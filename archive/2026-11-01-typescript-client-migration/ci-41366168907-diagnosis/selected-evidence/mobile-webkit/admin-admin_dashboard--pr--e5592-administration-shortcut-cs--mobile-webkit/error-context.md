# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: admin/admin_dashboard.spec.ts >> @pr-smoke @pr-smoke-mobile news administration shortcut (cs)
- Location: e2e/specs/admin/admin_dashboard.spec.ts:78:3

# Error details

```
Error: expect(locator).toContainText(expected) failed

Locator: getByTestId('app.dashboard.news.card')
Expected substring: "Vyzkoušej nové"
Received string:    "Event log a novinkyNejnovější oznámení, zkrácené na podstatné věciSbalitVšechny novinkySpravovat novinkyNepodařilo se načíst novinky"
Timeout: 15000ms

Call log:
  - Expect "toContainText" with timeout 15000ms
  - waiting for getByTestId('app.dashboard.news.card')
    6 × locator resolved to <div data-testid="app.dashboard.news.card" class="min-w-0 rounded-lg border border-border bg-surface shadow-card">…</div>
      - unexpected value "Event log a novinkyNejnovější oznámení, zkrácené na podstatné věciSbalitVšechny novinkySpravovat novinkyNačítám novinky…"
    27 × locator resolved to <div data-testid="app.dashboard.news.card" class="min-w-0 rounded-lg border border-border bg-surface shadow-card">…</div>
       - unexpected value "Event log a novinkyNejnovější oznámení, zkrácené na podstatné věciSbalitVšechny novinkySpravovat novinkyNepodařilo se načíst novinky"

```

```yaml
- text: Event log a novinky Nejnovější oznámení, zkrácené na podstatné věci
- button "Sbalit"
- link "Všechny novinky":
  - /url: /news
- link "Spravovat novinky":
  - /url: /admin/content/news
- text: Nepodařilo se načíst novinky
```

# Test source

```ts
  1   | import { expect, test, type Page } from '@playwright/test';
  2   | 
  3   | import { bootstrapVpsAdminWindow, installHaveApiMock, setUiSettingsLocalStorage } from '../../fixtures';
  4   | 
  5   | test.use({ locale: 'cs-CZ' });
  6   | 
  7   | test.describe('Admin dashboard', () => {
  8   |   test('@smoke keeps the overview concise and groups navigation', async ({ page }) => {
  9   |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  10  |     await setUiSettingsLocalStorage(page, { language: 'en' });
  11  | 
  12  |     await installHaveApiMock(page, {
  13  |       user: { id: 1, login: 'administrator', level: 90 },
  14  |       handlers: {
  15  |         'GET cluster_full_stats': () => ({
  16  |           cluster_full_stats: [{ vps_count: 0, dataset_count: 0, dns_zone_count: 0 }],
  17  |         }),
  18  |         'GET datasets': () => ({ datasets: [], _meta: { total_count: 0 } }),
  19  |         'GET dns_zones': () => ({ dns_zones: [], _meta: { total_count: 0 } }),
  20  |         'GET nodes/public_status': () => ({ nodes: [] }),
  21  |         'GET outages': () => ({ outages: [] }),
  22  |         'GET news_logs': () => ({ news_logs: [] }),
  23  |         'GET security_advisories': () => ({ security_advisories: [], _meta: { total_count: 0 } }),
  24  |       },
  25  |     });
  26  | 
  27  |     await page.goto('/admin');
  28  | 
  29  |     await expect(page.getByTestId('app.dashboard.page')).toBeVisible();
  30  |     await expect(page.getByTestId('admin.attention.queue')).toHaveCount(0);
  31  | 
  32  |     if ((page.viewportSize()?.width ?? 0) < 768) {
  33  |       await page.getByRole('button', { name: 'Open navigation', exact: true }).click();
  34  |       await expect(page.getByTestId('nav.drawer.group.services')).toBeVisible();
  35  |       await expect(page.getByTestId('nav.drawer.group.operations')).toBeVisible();
  36  |       await expect(page.getByTestId('nav.drawer.group.users-finance')).toBeVisible();
  37  |       await expect(page.getByTestId('nav.drawer.account')).toBeVisible();
  38  |       await page.getByTestId('nav.drawer.close').click();
  39  |     } else {
  40  |       await expect(page.getByTestId('nav.sidebar.group.services')).toBeVisible();
  41  |       await expect(page.getByTestId('nav.sidebar.group.operations')).toBeVisible();
  42  |       await expect(page.getByTestId('nav.sidebar.group.users-finance')).toBeVisible();
  43  |       await expect(page.getByTestId('nav.sidebar.account')).toBeVisible();
  44  |     }
  45  |   });
  46  | });
  47  | 
  48  | async function newsDashboard(page: Page, language: 'cs' | 'en', level: number, path: string) {
  49  |   await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  50  |   await setUiSettingsLocalStorage(page, { language, theme: 'dark' });
  51  |   await installHaveApiMock(page, {
  52  |     user: { id: 1, login: 'news-test', level },
  53  |     handlers: {
  54  |       'GET cluster_full_stats': () => ({ cluster_full_stats: [{ vps_count: 0 }] }),
  55  |       'GET vpses': () => ({ vpses: [], _meta: { total_count: 0 } }),
  56  |       'GET datasets': () => ({ datasets: [], _meta: { total_count: 0 } }),
  57  |       'GET dns_zones': () => ({ dns_zones: [], _meta: { total_count: 0 } }),
  58  |       'GET nodes/public_status': () => ({ nodes: [] }),
  59  |       'GET outages': () => ({ outages: [] }),
  60  |       'GET news_logs': () => ({
  61  |         news_logs: [
  62  |           {
  63  |             id: 42,
  64  |             published_at: '2026-10-19T09:00:00Z',
  65  |             cs_message: 'Vyzkoušej nové webové rozhraní vpsAdminu.',
  66  |             en_message: 'Try the new vpsAdmin web interface.',
  67  |           },
  68  |         ],
  69  |       }),
  70  |       'GET security_advisories': () => ({ security_advisories: [] }),
  71  |     },
  72  |   });
  73  |   await page.goto(path);
  74  |   await expect(page.getByTestId('app.dashboard.news.card')).toBeVisible();
  75  | }
  76  | 
  77  | for (const language of ['cs', 'en'] as const) {
  78  |   test(`@pr-smoke @pr-smoke-mobile news administration shortcut (${language})`, async ({
  79  |     page,
  80  |     isMobile,
  81  |   }, testInfo) => {
  82  |     await newsDashboard(page, language, 90, '/admin');
  83  |     const card = page.getByTestId('app.dashboard.news.card');
  84  |     const manage = card.getByRole('link', {
  85  |       name: language === 'cs' ? 'Spravovat novinky' : 'Manage news',
  86  |       exact: true,
  87  |     });
  88  |     await expect(manage).toHaveAttribute('href', '/admin/content/news');
  89  |     const all = card.getByRole('link', { name: language === 'cs' ? 'Všechny novinky' : 'All news', exact: true });
  90  |     await expect(all).toHaveAttribute('href', '/news');
> 91  |     await expect(card).toContainText(language === 'cs' ? 'Vyzkoušej nové' : 'Try the new');
      |                        ^ Error: expect(locator).toContainText(expected) failed
  92  |     if (language === 'cs' && process.env['E2E_CAPTURE_SCREENSHOTS'] === '1') {
  93  |       await card.screenshot({ path: `docs/design/images/news-manage-${testInfo.project.name}.png`, scale: 'css' });
  94  |     }
  95  |     if (isMobile) await page.setViewportSize({ width: 320, height: 900 });
  96  |     expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
  97  |     await page.getByTestId('app.dashboard.widget.news.collapse').click();
  98  |     await expect(manage).toBeVisible();
  99  |     if (isMobile) await manage.tap();
  100 |     else await manage.click();
  101 |     await expect(page).toHaveURL(/\/admin\/content\/news$/);
  102 |     await expect(page.getByTestId('admin.newslog.create')).toBeVisible();
  103 |     await page.getByTestId('admin.newslog.create').click();
  104 |     await expect(page.getByTestId('admin.newslog.editor.cs_message')).toBeVisible();
  105 |     await expect(page.getByTestId('admin.newslog.editor.en_message')).toBeVisible();
  106 |     await page.keyboard.press('Escape');
  107 |     await page.goto('/admin');
  108 |     await page
  109 |       .getByTestId('app.dashboard.news.card')
  110 |       .getByRole('link', { name: language === 'cs' ? 'Všechny novinky' : 'All news', exact: true })
  111 |       .click();
  112 |     await expect(page.getByTestId('public.news.page')).toBeVisible();
  113 |   });
  114 | }
  115 | 
  116 | for (const scenario of [
  117 |   { label: 'member', level: 1, path: '/app' },
  118 |   { label: 'administrator in My view', level: 90, path: '/app' },
  119 |   { label: 'support', level: 21, path: '/admin' },
  120 | ]) {
  121 |   test(`news administration shortcut is hidden for ${scenario.label}`, async ({ page }) => {
  122 |     await newsDashboard(page, 'en', scenario.level, scenario.path);
  123 |     await expect(page.getByTestId('app.dashboard.news.manage')).toHaveCount(0);
  124 |     await expect(
  125 |       page.getByTestId('app.dashboard.news.card').getByRole('link', { name: 'All news', exact: true })
  126 |     ).toHaveAttribute('href', '/news');
  127 |   });
  128 | }
  129 | 
```