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
  - generic [ref=e4]:
    - complementary [ref=e5]:
      - generic [ref=e6]:
        - generic [ref=e8]:
          - generic [ref=e9]: VA
          - generic [ref=e10]:
            - generic [ref=e11]: vpsAdmin
            - generic [ref=e12]: next UI
        - navigation [ref=e13]:
          - link "Dashboard" [ref=e16] [cursor=pointer]:
            - /url: /admin
            - img [ref=e18]
            - generic [ref=e23]: Dashboard
          - region "Services" [ref=e24]:
            - generic [ref=e25]: Services
            - generic [ref=e26]:
              - link "VPS" [ref=e27] [cursor=pointer]:
                - /url: /admin/vps
                - img [ref=e29]
                - generic [ref=e32]: VPS
              - link "Datasets" [ref=e33] [cursor=pointer]:
                - /url: /admin/datasets
                - img [ref=e35]
                - generic [ref=e39]: Datasets
              - link "NAS" [ref=e40] [cursor=pointer]:
                - /url: /admin/nas
                - img [ref=e42]
                - generic [ref=e44]: NAS
              - link "Exports" [ref=e45] [cursor=pointer]:
                - /url: /admin/exports
                - img [ref=e47]
                - generic [ref=e50]: Exports
              - link "DNS" [ref=e51] [cursor=pointer]:
                - /url: /admin/dns
                - img [ref=e53]
                - generic [ref=e56]: DNS
              - link "Networking" [ref=e57] [cursor=pointer]:
                - /url: /admin/networking/ip-addresses
                - img [ref=e59]
                - generic [ref=e64]: Networking
          - region "Operations" [ref=e65]:
            - generic [ref=e66]: Operations
            - generic [ref=e67]:
              - link "Transactions" [ref=e68] [cursor=pointer]:
                - /url: /admin/transactions
                - img [ref=e70]
                - generic [ref=e73]: Transactions
              - link "Monitoring" [ref=e74] [cursor=pointer]:
                - /url: /admin/monitoring
                - img [ref=e76]
                - generic [ref=e78]: Monitoring
              - link "Incidents" [ref=e79] [cursor=pointer]:
                - /url: /admin/incidents
                - img [ref=e81]
                - generic [ref=e83]: Incidents
              - link "Out-of-memory" [ref=e84] [cursor=pointer]:
                - /url: /admin/oom-reports
                - img [ref=e86]
                - generic [ref=e88]: Out-of-memory
              - link "Audit" [ref=e89] [cursor=pointer]:
                - /url: /admin/audit
                - img [ref=e91]
                - generic [ref=e94]: Audit
          - region "Users and finance" [ref=e95]:
            - generic [ref=e96]: Users and finance
            - generic [ref=e97]:
              - link "Users" [ref=e98] [cursor=pointer]:
                - /url: /admin/users
                - img [ref=e100]
                - generic [ref=e105]: Users
              - link "User namespaces" [ref=e106] [cursor=pointer]:
                - /url: /admin/user-namespaces/namespaces
                - img [ref=e108]
                - generic [ref=e112]: User namespaces
              - link "Requests" [ref=e113] [cursor=pointer]:
                - /url: /admin/requests
                - img [ref=e115]
                - generic [ref=e118]: Requests
              - link "Finance" [ref=e119] [cursor=pointer]:
                - /url: /admin/payments/incoming
                - img [ref=e121]
                - generic [ref=e123]: Finance
          - region "Infrastructure" [ref=e124]:
            - generic [ref=e125]: Infrastructure
            - generic [ref=e126]:
              - link "Cluster" [ref=e127] [cursor=pointer]:
                - /url: /admin/cluster/summary
                - img [ref=e129]
                - generic [ref=e139]: Cluster
              - link "Nodes" [ref=e140] [cursor=pointer]:
                - /url: /admin/nodes
                - img [ref=e142]
                - generic [ref=e145]: Nodes
              - link "Migration plans" [ref=e146] [cursor=pointer]:
                - /url: /admin/migration-plans
                - img [ref=e148]
                - generic [ref=e152]: Migration plans
              - link "Admin" [ref=e153] [cursor=pointer]:
                - /url: /admin/admin-info
                - img [ref=e155]
                - generic [ref=e157]: Admin
          - region "Content" [ref=e158]:
            - generic [ref=e159]: Content
            - generic [ref=e160]:
              - link "Mailer" [ref=e161] [cursor=pointer]:
                - /url: /admin/mailer/templates
                - img [ref=e163]
                - generic [ref=e166]: Mailer
              - link "News and help" [ref=e167] [cursor=pointer]:
                - /url: /admin/content/news
                - img [ref=e169]
                - generic [ref=e172]: News and help
        - link "Account" [ref=e174] [cursor=pointer]:
          - /url: /admin/profile
          - img [ref=e176]
          - generic [ref=e179]: Account
        - navigation "Service status" [ref=e180]:
          - link "Outages" [ref=e181] [cursor=pointer]:
            - /url: /admin/outages
            - img [ref=e183]
            - generic [ref=e185]: Outages
          - link "Security advisories" [ref=e186] [cursor=pointer]:
            - /url: /admin/security-advisories
            - img [ref=e188]
            - generic [ref=e190]: Security advisories
        - generic [ref=e192]:
          - link "About" [ref=e193] [cursor=pointer]:
            - /url: /about
          - link "View commit 5d2628083118" [ref=e194] [cursor=pointer]:
            - /url: https://github.com/vpsfreecz/vpsadmin-webui/commit/5d262808311831334086584d5914552426788fbf
            - text: 5d2628083118
    - generic [ref=e196]:
      - banner [ref=e197]:
        - generic [ref=e198]:
          - search [ref=e199]:
            - img [ref=e200]
            - combobox "Quickly search objects" [ref=e203]
            - generic "Open quick search" [ref=e204]: Ctrl K · /
          - generic "All accessible objects are shown" [ref=e205]:
            - generic [ref=e206]: Admin view
          - button "Open tasks" [ref=e207]:
            - img [ref=e208]
            - generic [ref=e210]: Tasks
          - button "Open account menu" [ref=e212]:
            - img [ref=e213]
            - generic [ref=e216]: synthetic-admin
            - generic [ref=e217]: admin
      - main [ref=e218]:
        - generic [ref=e221]:
          - generic [ref=e222]:
            - generic [ref=e223]:
              - heading "VPS" [level=1] [ref=e224]
              - paragraph [ref=e225]: Your virtual private servers. Open a VPS to access its console and full control center.
            - link "Create VPS" [ref=e227] [cursor=pointer]:
              - /url: /admin/vps/new
              - img [ref=e228]
              - text: Create VPS
          - generic [ref=e229]:
            - generic [ref=e231]:
              - generic [ref=e232]:
                - combobox "Filter… (hostname, ID, key:value, ?)" [ref=e233]
                - button "Help" [ref=e235]:
                  - img [ref=e236]
              - status [ref=e239]
            - button "Advanced filters" [ref=e240]:
              - img [ref=e241]
              - generic [ref=e242]: Advanced
            - button "Copy link" [ref=e243]
            - button "Clear filters" [ref=e244]
          - generic [ref=e245]:
            - generic [ref=e246]:
              - text: Memory pressure incident status
              - combobox "Memory pressure incident status" [ref=e247]:
                - option "All" [selected]
                - option "Below the incident limits"
                - option "Approaching an incident limit"
                - option "Warning limit reached"
                - option "Automatic stop limit reached"
            - generic [ref=e248]:
              - text: Automatic stop exemption
              - combobox "Automatic stop exemption" [ref=e249]:
                - option "All"
                - option "Exempt from automatic stops" [selected]
                - option "No stop exemption"
          - table [ref=e253]:
            - rowgroup [ref=e262]:
              - row "State VPS State Owner / location Resources Activity Actions" [ref=e263]:
                - columnheader "State" [ref=e264]:
                  - generic [ref=e265]: State
                - columnheader "VPS" [ref=e266]
                - columnheader "State" [ref=e267]
                - columnheader "Owner / location" [ref=e268]
                - columnheader "Resources" [ref=e269]
                - columnheader "Activity" [ref=e270]
                - columnheader "Actions" [ref=e271]
            - rowgroup [ref=e272]:
              - 'row "Running memory.example.test ID 123 Running Active OOM: 9 / 10 in 30 days · Exempt from automatic stops Owner: #7 Location: — Node: — — · Load — — Console Restart VPS Shutdown VPS Details Delete VPS" [ref=e273]':
                - cell "Running" [ref=e274] [cursor=pointer]:
                  - img "Running" [ref=e275]
                - cell "memory.example.test ID 123" [ref=e276] [cursor=pointer]:
                  - generic [ref=e277]:
                    - link "memory.example.test" [ref=e278]:
                      - /url: /admin/vps/123
                    - generic [ref=e279]: ID 123
                - 'cell "Running Active OOM: 9 / 10 in 30 days · Exempt from automatic stops" [ref=e280] [cursor=pointer]':
                  - generic [ref=e281]:
                    - generic [ref=e282]: Running
                    - generic [ref=e283]: Active
                    - 'link "OOM: 9 / 10 in 30 days · Exempt from automatic stops" [ref=e284]':
                      - /url: /admin/vps/123#oom
                      - generic [ref=e285]: "OOM: 9 / 10 in 30 days · Exempt from automatic stops"
                - 'cell "Owner: #7 Location: — Node: —" [ref=e286] [cursor=pointer]':
                  - generic [ref=e287]:
                    - generic [ref=e288]:
                      - generic [ref=e289]: "Owner:"
                      - text: "#7"
                    - generic [ref=e290]:
                      - generic [ref=e291]: "Location:"
                      - text: —
                    - generic [ref=e292]:
                      - generic [ref=e293]: "Node:"
                      - text: —
                - cell "— · Load —" [ref=e294] [cursor=pointer]:
                  - generic [ref=e296]: — · Load —
                - cell "—" [ref=e297] [cursor=pointer]:
                  - generic [ref=e299]: —
                - cell "Console Restart VPS Shutdown VPS Details Delete VPS" [ref=e300] [cursor=pointer]:
                  - generic [ref=e301]:
                    - link "Console" [ref=e302]:
                      - /url: /admin/vps/123/console
                      - img [ref=e303]
                      - generic [ref=e305]: Console
                    - button "Restart VPS" [ref=e306]:
                      - img [ref=e307]
                      - generic [ref=e310]: Restart
                    - button "Shutdown VPS" [ref=e311]:
                      - img [ref=e312]
                      - generic [ref=e314]: Shutdown
                    - link "Details" [ref=e315]:
                      - /url: /admin/vps/123
                      - img [ref=e316]
                      - generic [ref=e320]: Details
                    - button "Delete VPS" [ref=e321]:
                      - img [ref=e322]
                      - generic [ref=e325]: Delete VPS
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