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
          - link "View commit 55a813b44edb*" [ref=e194] [cursor=pointer]:
            - /url: https://github.com/vpsfreecz/vpsadmin-webui/commit/55a813b44edb915c7ed5ce68366d6d797a551606
            - text: 55a813b44edb*
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
              - text: Incident status
              - combobox "Incident status" [ref=e247]:
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
              - 'row "Running memory.example.test ID 123 Running Active VPS memory-pressure incidents: 9 / 10 in 30 days · Exempt from automatic stops Owner: #7 Location: — Node: — — · Load — — Console Restart VPS Shutdown VPS Details Delete VPS" [ref=e273]':
                - cell "Running" [ref=e274] [cursor=pointer]:
                  - img "Running" [ref=e275]
                - cell "memory.example.test ID 123" [ref=e276] [cursor=pointer]:
                  - generic [ref=e277]:
                    - link "memory.example.test" [ref=e278]:
                      - /url: /admin/vps/123
                    - generic [ref=e279]: ID 123
                - 'cell "Running Active VPS memory-pressure incidents: 9 / 10 in 30 days · Exempt from automatic stops" [ref=e280] [cursor=pointer]':
                  - generic [ref=e281]:
                    - generic [ref=e282]: Running
                    - generic [ref=e283]: Active
                    - 'link "VPS memory-pressure incidents: 9 / 10 in 30 days · Exempt from automatic stops" [ref=e284]':
                      - /url: /admin/vps/123#incident-escalation
                      - generic [ref=e285]: "VPS memory-pressure incidents: 9 / 10 in 30 days · Exempt from automatic stops"
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