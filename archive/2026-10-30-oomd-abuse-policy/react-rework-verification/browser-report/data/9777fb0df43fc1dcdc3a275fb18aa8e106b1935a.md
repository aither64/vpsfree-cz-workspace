# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/vps_incident_summary.spec.ts >> @pr-smoke @pr-smoke-mobile admin incident overview filters the existing VPS list on the server
- Location: e2e/specs/app/vps_incident_summary.spec.ts:64:1

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
            - text: Incident status
            - combobox "Incident status" [ref=e53]:
              - option "All"
              - option "Below the incident limits"
              - option "Approaching an incident limit" [selected]
              - option "Warning limit reached"
              - option "Automatic stop limit reached"
          - generic [ref=e54]:
            - text: Automatic stop exemption
            - combobox "Automatic stop exemption" [ref=e55]:
              - option "All" [selected]
              - option "Exempt from automatic stops"
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
              - 'link "VPS memory-pressure incidents: 9 / 10 in 30 days · Exempt from automatic stops" [ref=e69] [cursor=pointer]':
                - /url: /admin/vps/123#incident-escalation
                - generic [ref=e70]: "VPS memory-pressure incidents: 9 / 10 in 30 days · Exempt from automatic stops"
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
  16 |         incident_policy: 'oomd', incident_policy_label: language === 'en' ? 'VPS memory-pressure incidents' : 'Incidenty přetížení paměti VPS',
  17 |         incident_count_7d: 5, incident_count_30d: 10, incident_warning_limit: warning ?? 5, incident_stop_limit: stop ?? 10,
  18 |         ...(admin ? { incident_warning_limit_override: warning, incident_stop_limit_override: stop } : {}),
  19 |         incident_enforcement_enabled: enabled, incident_stop_enforced: enabled, incident_mode: 'enforce',
  20 |         incident_status: 'stop_threshold', incident_action_state: 'none',
  21 |         incident_last_stop_at: '2026-10-29T12:00:00Z', incident_next_stop_allowed_at: '2026-10-30T12:00:00Z',
  22 |       });
  23 |       await installHaveApiMock(page, {
  24 |         user: { id: 7, login: 'synthetic-member', level: admin ? 90 : 1 },
  25 |         handlers: {
  26 |           'GET vpses/123': () => ({ vps: vps() }),
  27 |           'GET transaction_chains': () => ({ transaction_chains: [] }),
  28 |           'PUT vpses/123': ctx => {
  29 |             writes.push(ctx.json);
  30 |             const body = ctx.json as { vps?: Record<string, unknown> };
  31 |             const payload = body.vps ?? {};
  32 |             warning = typeof payload['incident_warning_limit_override'] === 'number' ? payload['incident_warning_limit_override'] : null;
  33 |             stop = typeof payload['incident_stop_limit_override'] === 'number' ? payload['incident_stop_limit_override'] : null;
  34 |             enabled = payload['incident_enforcement_enabled'] === true;
  35 |             return { vps: vps(), _meta: {} };
  36 |           },
  37 |         },
  38 |       });
  39 |       const prefix = admin ? '/admin' : '/app';
  40 |       await page.goto(`${prefix}/vps/123`);
  41 |       const card = page.getByTestId('vps.incident');
  42 |       await expect(card).toContainText('5 / 5');
  43 |       await expect(card).toContainText('10 / 10');
  44 |       await expect(card).toContainText(language === 'en' ? 'No stop is scheduled' : 'není naplánované vypnutí');
  45 |       await expect(card.getByRole('link').first()).toHaveAttribute('href', `${prefix}/incidents?vps=123&codename=oomd`);
  46 |       await expect(page.getByTestId('vps.incident.settings')).toHaveCount(admin ? 1 : 0);
  47 |       await card.scrollIntoViewIfNeeded();
  48 |       await page.screenshot({ path: testInfo.outputPath('memory-summary.png'), fullPage: true, scale: 'css' });
  49 |       if (admin) {
  50 |         await card.getByRole('button', { name: language === 'en' ? 'Use default limits' : 'Použít výchozí limity' }).click();
  51 |         await card.getByRole('checkbox').check();
  52 |         expect(writes).toHaveLength(0);
  53 |         await card.getByRole('button', { name: language === 'en' ? 'Save incident settings' : 'Uložit nastavení incidentů', exact: true }).click();
  54 |         await page.getByTestId('vps.incident.confirm.confirm').click();
  55 |         await expect(page.getByTestId('vps.incident.confirm')).toHaveCount(0);
  56 |         expect(writes).toEqual([{ vps: { incident_policy: 'oomd', incident_warning_limit_override: null, incident_stop_limit_override: null, incident_enforcement_enabled: false } }]);
  57 |         await expect(card).toContainText(language === 'en' ? 'Exempt from automatic stops' : 'Výjimka z automatického vypnutí');
  58 |       }
  59 |       expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
  60 |     });
  61 |   }
  62 | }
  63 | 
  64 | test('@pr-smoke @pr-smoke-mobile admin incident overview filters the existing VPS list on the server', async ({ page }, testInfo) => {
  65 |   await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  66 |   await setUiSettingsLocalStorage(page, { language: 'en' });
  67 |   const queries: Record<string, unknown>[] = [];
  68 |   await installHaveApiMock(page, {
  69 |     user: { id: 7, login: 'synthetic-admin', level: 90 },
  70 |     handlers: {
  71 |       'GET vpses': ctx => {
  72 |         queries.push(ctx.params);
  73 |         return { vpses: [{ id: 123, hostname: 'memory.example.test', object_state: 'active', is_running: true,
  74 |           user: { id: 7 }, incident_policy: 'oomd', incident_policy_label: 'VPS memory-pressure incidents', incident_count_7d: 4, incident_count_30d: 9, incident_warning_limit: 5,
  75 |           incident_stop_limit: 10, incident_status: 'near_limit', incident_enforcement_enabled: false }] };
  76 |       },
  77 |       'GET transaction_chains': () => ({ transaction_chains: [] }),
  78 |     },
  79 |   });
  80 |   await page.goto('/admin/vps');
  81 |   await expect(page.getByTestId('vps.incident.filters')).toBeVisible();
  82 |   await page.getByLabel('Incident status').selectOption('near_limit');
  83 |   await page.getByLabel('Automatic stop exemption', { exact: true }).selectOption('false');
> 84 |   await expect.poll(() => queries.some(query => query['vps[incident_policy]'] === 'oomd' && query['vps[incident_status]'] === 'near_limit' && String(query['vps[incident_enforcement_enabled]']) === 'false')).toBe(true);
     |                                                                                                                                                                                                                ^ Error: expect(received).toBe(expected) // Object.is equality
  85 |   await expect(page).toHaveURL(/incident_status=near_limit/);
  86 |   await page.screenshot({ path: testInfo.outputPath('memory-overview.png'), fullPage: true, scale: 'css' });
  87 | });
  88 | 
  89 | test('@pr-smoke @pr-smoke-mobile an older API keeps the normal VPS overview', async ({ page }) => {
  90 |   await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  91 |   await installHaveApiMock(page, { user: { id: 7, login: 'synthetic-member', level: 1 }, handlers: {
  92 |     'GET vpses/123': () => ({ vps: { id: 123, hostname: 'older.example.test', object_state: 'active', user: { id: 7 }, node: { id: 1 } } }),
  93 |     'GET transaction_chains': () => ({ transaction_chains: [] }),
  94 |   } });
  95 |   await page.goto('/app/vps/123');
  96 |   await expect(page.getByTestId('vps.overview.control_center')).toBeVisible();
  97 |   await expect(page.getByTestId('vps.incident')).toHaveCount(0);
  98 | });
  99 | 
```