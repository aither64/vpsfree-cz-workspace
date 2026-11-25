# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/vps_oom_summary.spec.ts >> @pr-smoke @pr-smoke-mobile admin incident overview filters the existing VPS list on the server
- Location: e2e/specs/app/vps_oom_summary.spec.ts:63:1

# Error details

```
Error: expect(received).toBe(expected) // Object.is equality

Expected: true
Received: false

Call Log:
- Timeout 15000ms exceeded while waiting on the predicate
```

# Page snapshot

```yaml
- generic [ref=e2]:
  - link "Skip to main content" [ref=e3] [cursor=pointer]:
    - /url: "#main-content"
  - generic [ref=e6]:
    - banner [ref=e7]:
      - generic [ref=e8]:
        - button "Open navigation" [ref=e9]:
          - img [ref=e10]
        - button "Search" [ref=e11]:
          - img [ref=e12]
        - generic "All accessible objects are shown" [ref=e15]:
          - generic [ref=e16]: All
        - button "Open tasks" [ref=e17]:
          - img [ref=e18]
        - button "Open account menu" [ref=e21]:
          - img [ref=e22]
    - main [ref=e25]:
      - generic [ref=e28]:
        - generic [ref=e29]:
          - generic [ref=e30]:
            - heading "VPS" [level=1] [ref=e31]
            - paragraph [ref=e32]: Your virtual private servers. Open a VPS to access its console and full control center.
          - link "Create VPS" [ref=e34] [cursor=pointer]:
            - /url: /admin/vps/new
            - img [ref=e35]
            - text: Create VPS
        - generic [ref=e36]:
          - generic [ref=e38]:
            - generic [ref=e39]:
              - combobox "Filter… (hostname, ID, key:value, ?)" [ref=e40]
              - button "Help" [ref=e42]:
                - img [ref=e43]
            - status [ref=e46]
          - button "Advanced filters" [ref=e47]:
            - img [ref=e48]
          - button "Copy link" [ref=e49]
          - button "Clear filters" [ref=e50]
        - generic [ref=e51]:
          - generic [ref=e52]:
            - text: Memory pressure incident status
            - combobox "Memory pressure incident status" [ref=e53]:
              - option "All" [selected]
              - option "Below the incident limits"
              - option "Approaching an incident limit"
              - option "Warning limit reached"
              - option "Automatic stop limit reached"
          - generic [ref=e54]:
            - text: Automatic stop exemption
            - combobox "Automatic stop exemption" [ref=e55]:
              - option "All"
              - option "Exempt from automatic stops" [selected]
              - option "No stop exemption"
        - generic [ref=e59]:
          - generic [ref=e60]:
            - generic [ref=e61]:
              - generic [ref=e62]:
                - img "Running" [ref=e63]
                - link "memory.example.test" [ref=e64] [cursor=pointer]:
                  - /url: /admin/vps/123
              - generic [ref=e65]: ID 123
            - generic [ref=e66]:
              - generic [ref=e67]: Running
              - generic [ref=e68]: Active
              - 'link "OOM: 9 / 10 in 30 days · Exempt from automatic stops" [ref=e69] [cursor=pointer]':
                - /url: /admin/vps/123#oom
                - generic [ref=e70]: "OOM: 9 / 10 in 30 days · Exempt from automatic stops"
          - generic [ref=e71]:
            - generic [ref=e72]:
              - generic [ref=e73]: Owner
              - generic [ref=e74]: "#7"
            - generic [ref=e75]:
              - generic [ref=e76]: Location
              - generic [ref=e77]: —
            - generic [ref=e78]:
              - generic [ref=e79]: Node
              - generic [ref=e80]: —
            - generic [ref=e81]:
              - generic [ref=e82]: Memory
              - generic [ref=e83]: —
            - generic [ref=e84]:
              - generic [ref=e85]: Diskspace
              - generic [ref=e86]: —
            - generic [ref=e87]:
              - generic [ref=e88]: Uptime
              - generic [ref=e89]: —
            - generic [ref=e90]:
              - generic [ref=e91]: Load —
              - generic [ref=e92]: —
          - generic [ref=e94]:
            - link "Console" [ref=e95] [cursor=pointer]:
              - /url: /admin/vps/123/console
              - img [ref=e96]
              - generic [ref=e98]: Console
            - button "Restart VPS" [ref=e99]:
              - img [ref=e100]
              - generic [ref=e103]: Restart
            - button "Shutdown VPS" [ref=e104]:
              - img [ref=e105]
              - generic [ref=e107]: Shutdown
            - link "Details" [ref=e108] [cursor=pointer]:
              - /url: /admin/vps/123
              - img [ref=e109]
              - generic [ref=e113]: Details
            - button "Delete VPS" [ref=e114]:
              - img [ref=e115]
              - generic [ref=e118]: Delete VPS
```

# Test source

```ts
  1  | import { expect, test } from '@playwright/test';
  2  | import { bootstrapVpsAdminWindow, installHaveApiMock, setUiSettingsLocalStorage } from '../../fixtures';
  3  | 
  4  | for (const language of ['en', 'cs'] as const) {
  5  |   for (const admin of [false, true]) {
  6  |     test(`@pr-smoke @pr-smoke-mobile memory incident summary ${language} admin=${admin}`, async ({ page }, testInfo) => {
  7  |       await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  8  |       await setUiSettingsLocalStorage(page, { language, theme: 'dark' });
  9  |       let warning: number | null = 5;
  10 |       let stop: number | null = 10;
  11 |       let enabled = true;
  12 |       const writes: unknown[] = [];
  13 |       const vps = () => ({
  14 |         id: 123, hostname: 'memory.example.test', object_state: 'active', is_running: true,
  15 |         user: { id: 7 }, node: { id: 1 }, memory: 2048,
  16 |         oom_incidents_7d: 5, oom_incidents_30d: 10, oom_warning_limit: warning ?? 5, oom_stop_limit: stop ?? 10,
  17 |         ...(admin ? { oom_warning_limit_override: warning, oom_stop_limit_override: stop } : {}),
  18 |         oom_enforcement_enabled: enabled, oom_stop_enforced: enabled, oom_mode: 'enforce',
  19 |         oom_status: 'stop_threshold', oom_action_state: 'none',
  20 |         oom_last_stop_at: '2026-10-29T12:00:00Z', oom_next_stop_allowed_at: '2026-10-30T12:00:00Z',
  21 |       });
  22 |       await installHaveApiMock(page, {
  23 |         user: { id: 7, login: 'synthetic-member', level: admin ? 90 : 1 },
  24 |         handlers: {
  25 |           'GET vpses/123': () => ({ vps: vps() }),
  26 |           'GET transaction_chains': () => ({ transaction_chains: [] }),
  27 |           'PUT vpses/123': ctx => {
  28 |             writes.push(ctx.json);
  29 |             const body = ctx.json as { vps?: Record<string, unknown> };
  30 |             const payload = body.vps ?? {};
  31 |             warning = typeof payload['oom_warning_limit_override'] === 'number' ? payload['oom_warning_limit_override'] : null;
  32 |             stop = typeof payload['oom_stop_limit_override'] === 'number' ? payload['oom_stop_limit_override'] : null;
  33 |             enabled = payload['oom_enforcement_enabled'] === true;
  34 |             return { vps: vps(), _meta: {} };
  35 |           },
  36 |         },
  37 |       });
  38 |       const prefix = admin ? '/admin' : '/app';
  39 |       await page.goto(`${prefix}/vps/123`);
  40 |       const card = page.getByTestId('vps.oom');
  41 |       await expect(card).toContainText('5 / 5');
  42 |       await expect(card).toContainText('10 / 10');
  43 |       await expect(card).toContainText(language === 'en' ? 'No stop is scheduled' : 'není naplánované vypnutí');
  44 |       await expect(card.getByRole('link').first()).toHaveAttribute('href', `${prefix}/incidents?vps=123&codename=oomd`);
  45 |       await expect(page.getByTestId('vps.oom.settings')).toHaveCount(admin ? 1 : 0);
  46 |       await card.scrollIntoViewIfNeeded();
  47 |       await page.screenshot({ path: testInfo.outputPath('memory-summary.png'), fullPage: true, scale: 'css' });
  48 |       if (admin) {
  49 |         await card.getByRole('button', { name: language === 'en' ? 'Use default limits' : 'Použít výchozí limity' }).click();
  50 |         await card.getByRole('checkbox').check();
  51 |         expect(writes).toHaveLength(0);
  52 |         await card.getByRole('button', { name: language === 'en' ? 'Save' : 'Uložit', exact: true }).click();
  53 |         await page.getByTestId('vps.oom.confirm.confirm').click();
  54 |         await expect(page.getByTestId('vps.oom.confirm')).toHaveCount(0);
  55 |         expect(writes).toEqual([{ vps: { oom_warning_limit_override: null, oom_stop_limit_override: null, oom_enforcement_enabled: false } }]);
  56 |         await expect(card).toContainText(language === 'en' ? 'Exempt from automatic stops' : 'Výjimka z automatického vypnutí');
  57 |       }
  58 |       expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
  59 |     });
  60 |   }
  61 | }
  62 | 
  63 | test('@pr-smoke @pr-smoke-mobile admin incident overview filters the existing VPS list on the server', async ({ page }, testInfo) => {
  64 |   await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  65 |   await setUiSettingsLocalStorage(page, { language: 'en' });
  66 |   const queries: Record<string, unknown>[] = [];
  67 |   await installHaveApiMock(page, {
  68 |     user: { id: 7, login: 'synthetic-admin', level: 90 },
  69 |     handlers: {
  70 |       'GET vpses': ctx => {
  71 |         queries.push(ctx.params);
  72 |         return { vpses: [{ id: 123, hostname: 'memory.example.test', object_state: 'active', is_running: true,
  73 |           user: { id: 7 }, oom_incidents_7d: 4, oom_incidents_30d: 9, oom_warning_limit: 5,
  74 |           oom_stop_limit: 10, oom_status: 'near_limit', oom_enforcement_enabled: false }] };
  75 |       },
  76 |       'GET transaction_chains': () => ({ transaction_chains: [] }),
  77 |     },
  78 |   });
  79 |   await page.goto('/admin/vps');
  80 |   await expect(page.getByTestId('vps.oom.filters')).toBeVisible();
  81 |   await page.getByLabel('Memory pressure incident status').selectOption('near_limit');
  82 |   await page.getByLabel('Automatic stop exemption', { exact: true }).selectOption('false');
> 83 |   await expect.poll(() => queries.some(query => query['vps[oom_status]'] === 'near_limit' && String(query['vps[oom_enforcement_enabled]']) === 'false')).toBe(true);
     |                                                                                                                                                          ^ Error: expect(received).toBe(expected) // Object.is equality
  84 |   await expect(page).toHaveURL(/oom_status=near_limit/);
  85 |   await page.screenshot({ path: testInfo.outputPath('memory-overview.png'), fullPage: true, scale: 'css' });
  86 | });
  87 | 
  88 | test('@pr-smoke @pr-smoke-mobile an older API keeps the normal VPS overview', async ({ page }) => {
  89 |   await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  90 |   await installHaveApiMock(page, { user: { id: 7, login: 'synthetic-member', level: 1 }, handlers: {
  91 |     'GET vpses/123': () => ({ vps: { id: 123, hostname: 'older.example.test', object_state: 'active', user: { id: 7 }, node: { id: 1 } } }),
  92 |     'GET transaction_chains': () => ({ transaction_chains: [] }),
  93 |   } });
  94 |   await page.goto('/app/vps/123');
  95 |   await expect(page.getByTestId('vps.overview.control_center')).toBeVisible();
  96 |   await expect(page.getByTestId('vps.oom')).toHaveCount(0);
  97 | });
  98 | 
```