# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/vps_power_stop_confirm.spec.ts >> @workflow-matrix @pr-smoke @smoke VPS detail power actions >> starts a stopped VPS and tracks the returned action state
- Location: e2e/specs/app/vps_power_stop_confirm.spec.ts:85:3

# Error details

```
Error: expect(received).toEqual(expected) // deep equality

- Expected  - 1
+ Received  + 3

- Object {}
+ Object {
+   "vps": Object {},
+ }
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
          - generic [ref=e15]:
            - link "Dashboard" [ref=e16] [cursor=pointer]:
              - /url: /app
              - img [ref=e18]
              - generic [ref=e23]: Dashboard
            - link "VPS" [ref=e24] [cursor=pointer]:
              - /url: /app/vps
              - img [ref=e26]
              - generic [ref=e29]: VPS
            - link "NAS" [ref=e30] [cursor=pointer]:
              - /url: /app/nas
              - img [ref=e32]
              - generic [ref=e34]: NAS
            - link "Backups" [ref=e35] [cursor=pointer]:
              - /url: /app/backups
              - img [ref=e37]
              - generic [ref=e43]: Backups
            - link "Exports" [ref=e44] [cursor=pointer]:
              - /url: /app/exports
              - img [ref=e46]
              - generic [ref=e49]: Exports
            - link "DNS" [ref=e50] [cursor=pointer]:
              - /url: /app/dns
              - img [ref=e52]
              - generic [ref=e55]: DNS
            - link "Networking" [ref=e56] [cursor=pointer]:
              - /url: /app/networking
              - img [ref=e58]
              - generic [ref=e63]: Networking
            - link "Transactions" [ref=e64] [cursor=pointer]:
              - /url: /app/transactions
              - img [ref=e66]
              - generic [ref=e69]: Transactions
            - link "Monitoring" [ref=e70] [cursor=pointer]:
              - /url: /app/monitoring
              - img [ref=e72]
              - generic [ref=e74]: Monitoring
            - link "Incidents" [ref=e75] [cursor=pointer]:
              - /url: /app/incidents
              - img [ref=e77]
              - generic [ref=e79]: Incidents
            - link "Out-of-memory" [ref=e80] [cursor=pointer]:
              - /url: /app/oom-reports
              - img [ref=e82]
              - generic [ref=e84]: Out-of-memory
            - link "Payments" [ref=e85] [cursor=pointer]:
              - /url: /app/payments
              - img [ref=e87]
              - generic [ref=e89]: Payments
            - link "My requests" [ref=e90] [cursor=pointer]:
              - /url: /app/requests
              - img [ref=e92]
              - generic [ref=e95]: My requests
            - link "Account" [ref=e96] [cursor=pointer]:
              - /url: /app/profile
              - img [ref=e98]
              - generic [ref=e101]: Account
        - navigation "Service status" [ref=e102]:
          - link "Outages" [ref=e103] [cursor=pointer]:
            - /url: /outages
            - img [ref=e105]
            - generic [ref=e107]: Outages
          - link "Security advisories" [ref=e108] [cursor=pointer]:
            - /url: /security-advisories
            - img [ref=e110]
            - generic [ref=e112]: Security advisories
        - generic [ref=e114]:
          - link "About" [ref=e115] [cursor=pointer]:
            - /url: /about
          - link "View commit b1b37ccf5dc5" [ref=e116] [cursor=pointer]:
            - /url: https://github.com/vpsfreecz/vpsadmin-webui/commit/b1b37ccf5dc5d000baed3d77d49fab6f5b84b663
            - text: b1b37ccf5dc5
    - status [ref=e117]:
      - generic [ref=e118]:
        - generic [ref=e119]:
          - generic [ref=e120]: Starting VPS…
          - paragraph [ref=e121]: You can keep this window open or continue in background.
        - button "Close" [ref=e122]:
          - img [ref=e123]
      - generic [ref=e126]:
        - generic [ref=e127]: "Start · vps123.example · #776"
        - generic [ref=e129]:
          - generic [ref=e130]: 1/2
          - generic [ref=e131]: 50%
        - generic [ref=e134]:
          - button "Open tasks" [ref=e135]
          - button "Continue in background" [ref=e136]
    - generic [ref=e138]:
      - banner [ref=e139]:
        - generic [ref=e140]:
          - search [ref=e141]:
            - img [ref=e142]
            - combobox "Quickly search objects" [ref=e145]
            - generic "Open quick search" [ref=e146]: Ctrl K · /
          - button "Open tasks" [ref=e147]:
            - img [ref=e148]
            - generic [ref=e150]: Tasks
          - button "Open account menu" [ref=e152]:
            - img [ref=e153]
            - generic [ref=e156]: user
            - generic [ref=e157]: user
      - main [ref=e158]:
        - generic [ref=e161]:
          - generic [ref=e163]:
            - generic [ref=e164]:
              - generic [ref=e165]:
                - generic [ref=e166]:
                  - link "VPS" [ref=e167] [cursor=pointer]:
                    - /url: /app/vps
                  - text: ·
                  - generic [ref=e168]: "#123"
                - heading "vps123.example" [level=1] [ref=e170]
                - generic [ref=e171]:
                  - generic [ref=e172]: Stopped
                  - generic [ref=e173]: Active
                  - generic "The action was started. Please wait until it finishes." [ref=e174]: Working…
              - generic [ref=e176]:
                - button "Start" [disabled] [active] [ref=e177]
                - combobox "VPS actions" [ref=e178]:
                  - option "More…" [selected]
                  - option "DNS servers"
                  - option "Root password" [disabled]
                  - option "Open tasks"
                  - option "Access"
                  - option "Config"
                  - option "Network"
                  - option "Storage"
                  - option "Features"
                  - option "Maintenance"
                  - option "History"
                  - option "Transaction log"
                  - option "Reinstall VPS"
                  - option "Clone VPS"
                  - option "Swap VPS"
                  - option "Update VPS template info"
                  - option "Boot VPS from template"
                  - option "Delete VPS"
            - generic [ref=e179]:
              - generic [ref=e181]:
                - generic [ref=e182]: Distribution debian
                - generic [ref=e183]: Node node1.example
                - generic [ref=e184]: Location dc1
              - generic [ref=e186]:
                - generic [ref=e187]:
                  - generic [ref=e188]: "SSH:"
                  - generic [ref=e189]:
                    - code [ref=e190]: ssh root@198.51.100.10
                    - button "Copy" [ref=e191]
                - generic [ref=e192]:
                  - text: "Tracking: Start · vps123.example ·"
                  - button "Open tasks" [ref=e193]
                  - text: "· #776"
            - generic [ref=e195]:
              - generic [ref=e196]:
                - generic [ref=e197]:
                  - term [ref=e198]:
                    - img [ref=e199]
                    - text: Uptime
                  - definition [ref=e202]: —
                - generic [ref=e203]:
                  - term [ref=e204]:
                    - img [ref=e205]
                    - text: Load average (1 / 5 / 15 min)
                  - definition [ref=e207]: —
                - generic [ref=e208]:
                  - term [ref=e209]:
                    - img [ref=e210]
                    - text: Processes
                  - definition [ref=e214]: —
                - generic [ref=e215]:
                  - term [ref=e216]:
                    - img [ref=e217]
                    - text: CPU usage
                  - definition [ref=e220]: —
              - generic [ref=e221]:
                - link "Overview" [ref=e222] [cursor=pointer]:
                  - /url: /app/vps/123
                - link "Access" [ref=e223] [cursor=pointer]:
                  - /url: /app/vps/123/access
                - link "Network" [ref=e224] [cursor=pointer]:
                  - /url: /app/vps/123/network
                - link "Storage" [ref=e225] [cursor=pointer]:
                  - /url: /app/vps/123/storage
                - link "Maintenance" [ref=e226] [cursor=pointer]:
                  - /url: /app/vps/123/maintenance
                - link "History" [ref=e227] [cursor=pointer]:
                  - /url: /app/vps/123/history
                - link "Console" [ref=e228] [cursor=pointer]:
                  - /url: /app/vps/123/console
          - generic [ref=e229]:
            - status [ref=e230]:
              - generic [ref=e233]:
                - generic [ref=e234]: Operation in progress
                - generic [ref=e235]: Some actions are temporarily unavailable until the current task finishes.
              - generic [ref=e236]:
                - generic [ref=e237]: Stopped
                - generic [ref=e238]: Operation in progress
            - generic [ref=e239]:
              - generic [ref=e240]:
                - generic [ref=e241]:
                  - generic [ref=e243]:
                    - img [ref=e244]
                    - generic [ref=e247]: Resources
                  - generic [ref=e248]: Provisioned capacity and current VPS utilization.
                - link "Edit resources" [ref=e250] [cursor=pointer]:
                  - /url: /app/vps/123/config?section=resources
              - generic [ref=e251]:
                - generic [ref=e252]:
                  - generic [ref=e253]: CPU
                  - generic [ref=e254]: 2 CPU
                - generic [ref=e255]:
                  - generic [ref=e256]:
                    - generic [ref=e257]:
                      - generic [ref=e258]: Memory
                      - generic [ref=e259]: 768 MiB / 2.0 GiB
                    - img "Memory" [ref=e260]
                  - generic [ref=e264]:
                    - generic [ref=e265]:
                      - generic [ref=e266]: Disk
                      - generic [ref=e267]: 5.0 GiB / 20 GiB
                    - img "Disk" [ref=e268]
            - generic [ref=e272]:
              - generic [ref=e273]:
                - generic [ref=e274]:
                  - generic [ref=e276]:
                    - img [ref=e277]
                    - generic [ref=e280]: Access
                  - generic [ref=e281]: SSH, console and essential runtime information.
                - link "Manage access" [ref=e283] [cursor=pointer]:
                  - /url: /app/vps/123/access
              - generic [ref=e284]:
                - generic [ref=e285]:
                  - generic [ref=e286]: SSH
                  - generic [ref=e287]:
                    - code [ref=e288]: ssh root@198.51.100.10
                    - button "Copy" [ref=e289]
                - generic [ref=e290]:
                  - generic [ref=e291]:
                    - generic [ref=e292]: Uptime
                    - generic [ref=e293]: 3h 25m
                  - generic [ref=e294]:
                    - generic [ref=e295]: Load
                    - generic [ref=e296]: 0.12 / — / —
                - generic [ref=e297]: Console is unavailable for the current VPS placement.
            - generic [ref=e298]:
              - generic [ref=e299]:
                - generic [ref=e300]:
                  - generic [ref=e302]:
                    - img [ref=e303]
                    - generic [ref=e308]: Network
                  - generic [ref=e309]: Assigned public, private and IPv6 addresses.
                - link "Manage network" [ref=e311] [cursor=pointer]:
                  - /url: /app/vps/123/network
              - list [ref=e313]:
                - listitem [ref=e314]:
                  - generic [ref=e315]:
                    - generic [ref=e316]: 198.51.100.10
                    - generic [ref=e318]: Public IPv4
                  - button "Copy" [ref=e319]
            - generic [ref=e320]:
              - generic [ref=e321]:
                - generic [ref=e322]:
                  - generic [ref=e324]:
                    - img [ref=e325]
                    - generic [ref=e327]: Storage
                  - generic [ref=e328]: Root dataset, capacity utilization and mounted datasets.
                - link "Open storage" [ref=e330] [cursor=pointer]:
                  - /url: /app/vps/123/storage
              - generic [ref=e331]:
                - generic [ref=e332]:
                  - generic [ref=e333]: Dataset
                  - generic [ref=e334]: The root dataset is unavailable.
                - generic [ref=e335]:
                  - generic [ref=e336]:
                    - generic [ref=e337]: Usage
                    - generic [ref=e338]: 5.0 GiB / 20 GiB
                  - img "Usage" [ref=e339]
            - generic [ref=e344]:
              - generic [ref=e345]:
                - generic [ref=e346]: Usage charts
                - generic [ref=e347]: Load, memory and disk history is available on demand.
              - button "Show charts" [ref=e350]
            - generic [ref=e351]:
              - generic [ref=e353]:
                - generic [ref=e354]: Diagnostics
                - generic [ref=e355]: Quick links to incident reports and OOM kills for this VPS.
              - generic [ref=e356]:
                - generic [ref=e357]:
                  - link "OOM reports" [ref=e358] [cursor=pointer]:
                    - /url: /app/oom-reports?vps=123
                  - link "OOM rules" [ref=e359] [cursor=pointer]:
                    - /url: /app/oom-reports/rules/123
                  - link "Incidents" [ref=e360] [cursor=pointer]:
                    - /url: /app/incidents?vps=123
                - generic [ref=e361]: Links open in the current mode and are pre-filtered to this VPS.
```

# Test source

```ts
  1   | import { expect, test, type Page } from '@playwright/test';
  2   | 
  3   | import { bootstrapVpsAdminWindow, failEnvelope, installHaveApiMock } from '../../fixtures';
  4   | 
  5   | const vps = {
  6   |   id: 123,
  7   |   hostname: 'vps123.example',
  8   |   object_state: 'active',
  9   |   is_running: true,
  10  |   enable_network: true,
  11  |   cpus: 2,
  12  |   memory: 2048,
  13  |   swap: 0,
  14  |   diskspace: 20480,
  15  |   used_memory: 768,
  16  |   used_swap: 0,
  17  |   used_diskspace: 5120,
  18  |   uptime: 12345,
  19  |   loadavg1: 0.12,
  20  |   node: { id: 1, domain_name: 'node1.example', location: { label: 'dc1' } },
  21  |   user: { id: 42, login: 'user' },
  22  |   os_template: { label: 'debian' },
  23  |   dns_resolver: null,
  24  | };
  25  | 
  26  | function runningActionState(id: number, label: string) {
  27  |   return {
  28  |     action_state: {
  29  |       id,
  30  |       label,
  31  |       status: true,
  32  |       finished: false,
  33  |       current: 1,
  34  |       total: 2,
  35  |       created_at: '2026-07-15T12:00:00Z',
  36  |       updated_at: '2026-07-15T12:00:01Z',
  37  |     },
  38  |   };
  39  | }
  40  | 
  41  | async function installPowerMock(
  42  |   page: Page,
  43  |   options: { action: 'start' | 'stop' | 'restart'; actionStateId: number; isRunning: boolean; admin?: boolean }
  44  | ) {
  45  |   const label = `${options.action.charAt(0).toUpperCase()}${options.action.slice(1)} VPS`;
  46  | 
  47  |   await installHaveApiMock(page, {
  48  |     user: { id: 42, login: 'user', level: options.admin ? 99 : 1 },
  49  |     handlers: {
  50  |       'GET vpses': () => ({ vpses: [vps], _meta: { total_count: 1 } }),
  51  |       'GET vpses/123': () => ({ vps: { ...vps, is_running: options.isRunning } }),
  52  |       'GET ip_addresses': () => ({
  53  |         ip_addresses: [
  54  |           {
  55  |             id: 1,
  56  |             addr: '198.51.100.10',
  57  |             vps: { id: 123 },
  58  |             network: { role: 'public', purpose: 'public' },
  59  |           },
  60  |         ],
  61  |       }),
  62  |       'GET vpses/123/statuses': () => ({ statuses: [] }),
  63  |       'GET transaction_chains': () => ({ transaction_chains: [] }),
  64  |       [`POST vpses/123/${options.action}`]: () => ({
  65  |         vps: {},
  66  |         _meta: { action_state_id: options.actionStateId },
  67  |       }),
  68  |       [`GET action_states/${options.actionStateId}`]: () =>
  69  |         runningActionState(options.actionStateId, label),
  70  |     },
  71  |   });
  72  | }
  73  | 
  74  | async function expectTrackedTask(page: Page, actionStateId: number, label: string) {
  75  |   await expect(page.getByTestId('modal.action_progress')).toBeVisible();
  76  |   await page.getByTestId('modal.action_progress.open_tasks').click();
  77  |   await expect(page.getByTestId('tasks.drawer')).toHaveAttribute('aria-modal', 'false');
  78  |   await expect(
  79  |     page.getByTestId(`tasks.row.${actionStateId}`).getByRole('button', { name: label, exact: true }),
  80  |   ).toBeVisible();
  81  |   await expect(page.getByTestId('vps.header')).toBeVisible();
  82  | }
  83  | 
  84  | test.describe('@workflow-matrix @pr-smoke @smoke VPS detail power actions', () => {
  85  |   test('starts a stopped VPS and tracks the returned action state', async ({ page }) => {
  86  |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  87  |     await installPowerMock(page, { action: 'start', actionStateId: 776, isRunning: false });
  88  | 
  89  |     await page.goto('/app/vps/123');
  90  | 
  91  |     const reqPromise = page.waitForRequest(
  92  |       (request) => request.method() === 'POST' && request.url().includes('/api/v7.0/vpses/123/start')
  93  |     );
  94  |     await page.getByTestId('vps.action.start').click();
  95  | 
  96  |     const request = await reqPromise;
> 97  |     expect(request.postDataJSON()).toEqual({});
      |                                    ^ Error: expect(received).toEqual(expected) // deep equality
  98  |     await expectTrackedTask(page, 776, 'Start');
  99  |   });
  100 | 
  101 |   test('stops a running VPS with force and tracks the returned action state', async ({ page }) => {
  102 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  103 |     await installPowerMock(page, { action: 'stop', actionStateId: 777, isRunning: true });
  104 | 
  105 |     await page.goto('/app/vps/123');
  106 | 
  107 |     await expect(page.getByTestId('vps.action.stop.header')).toBeEnabled();
  108 |     await page.getByTestId('vps.action.stop.header').click();
  109 | 
  110 |     await expect(page.getByTestId('vps.action.stop_confirm')).toBeVisible();
  111 |     await expect(page.getByTestId('vps.action.stop_confirm.target')).toContainText('vps123.example');
  112 |     await expect(page.getByTestId('vps.action.stop_confirm.target')).toContainText('#123');
  113 |     await page.getByTestId('vps.action.stop_confirm.force').click();
  114 | 
  115 |     const reqPromise = page.waitForRequest(
  116 |       (request) => request.method() === 'POST' && request.url().includes('/api/v7.0/vpses/123/stop')
  117 |     );
  118 |     await page.getByTestId('vps.action.stop_confirm.confirm').click();
  119 | 
  120 |     const request = await reqPromise;
  121 |     expect(request.postDataJSON()).toEqual({ vps: { force: true } });
  122 |     await expect(page.getByTestId('vps.action.stop_confirm')).toBeHidden();
  123 |     await expectTrackedTask(page, 777, 'Poweroff');
  124 |   });
  125 | 
  126 |   test('keeps the stop confirmation and force choice available after an immediate rejection', async ({ page }) => {
  127 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  128 |     let attempts = 0;
  129 |     await installHaveApiMock(page, {
  130 |       user: { id: 42, login: 'user', level: 1 },
  131 |       handlers: {
  132 |         'GET vpses/123': () => ({ vps }),
  133 |         'GET ip_addresses': () => ({ ip_addresses: [] }),
  134 |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  135 |         'POST vpses/123/stop': () => {
  136 |           attempts += 1;
  137 |           return attempts === 1
  138 |             ? failEnvelope('Stop rejected by API')
  139 |             : { vps: {}, _meta: { action_state_id: 781 } };
  140 |         },
  141 |         'GET action_states/781': () => runningActionState(781, 'Stop VPS'),
  142 |       },
  143 |     });
  144 | 
  145 |     await page.goto('/app/vps/123');
  146 |     await page.getByTestId('vps.action.stop.header').click();
  147 |     await page.getByTestId('vps.action.stop_confirm.force').click();
  148 |     await page.getByTestId('vps.action.stop_confirm.confirm').click();
  149 | 
  150 |     await expect(page.getByTestId('vps.action.stop_confirm')).toBeVisible();
  151 |     await expect(page.getByTestId('vps.action.stop_confirm.force')).toBeChecked();
  152 |     await expect(page.getByTestId('vps.action.stop_confirm.error')).toContainText('Stop rejected by API');
  153 | 
  154 |     await page.getByTestId('vps.action.stop_confirm.confirm').click();
  155 |     await expect(page.getByTestId('vps.action.stop_confirm')).toBeHidden();
  156 |     await expectTrackedTask(page, 781, 'Poweroff');
  157 |   });
  158 | 
  159 |   test('restarts a running VPS with force and tracks the returned action state', async ({ page }) => {
  160 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  161 |     await installPowerMock(page, { action: 'restart', actionStateId: 778, isRunning: true });
  162 | 
  163 |     await page.goto('/app/vps/123');
  164 |     await page.getByTestId('vps.action.restart.header').click();
  165 | 
  166 |     await expect(page.getByTestId('vps.action.restart_confirm')).toBeVisible();
  167 |     await expect(page.getByTestId('vps.action.restart_confirm.target')).toContainText('vps123.example');
  168 |     await expect(page.getByTestId('vps.action.restart_confirm.target')).toContainText('#123');
  169 |     await page.getByTestId('vps.action.restart_confirm.force').click();
  170 | 
  171 |     const reqPromise = page.waitForRequest(
  172 |       (request) => request.method() === 'POST' && request.url().includes('/api/v7.0/vpses/123/restart')
  173 |     );
  174 |     await page.getByTestId('vps.action.restart_confirm.confirm').click();
  175 | 
  176 |     const request = await reqPromise;
  177 |     expect(request.postDataJSON()).toEqual({ vps: { force: true } });
  178 |     await expectTrackedTask(page, 778, 'Restart');
  179 |   });
  180 | 
  181 |   test('keeps a tracked VPS task bound to the member context that started it', async ({ page }) => {
  182 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  183 |     await installPowerMock(page, { action: 'restart', actionStateId: 780, isRunning: true, admin: true });
  184 | 
  185 |     await page.goto('/admin/vps/123?user=42');
  186 |     await page.getByTestId('vps.action.restart.header').click();
  187 |     await page.getByTestId('vps.action.restart_confirm.confirm').click();
  188 |     await expect(page.getByTestId('modal.action_progress')).toBeVisible();
  189 |     await page.goto('/admin/vps?user=84');
  190 |     await page.getByTestId('tasks.open-button').click();
  191 | 
  192 |     await expect(page.getByTestId('tasks.row.target.780')).toHaveAttribute('href', '/admin/vps/123?user=42');
  193 |     await page.getByTestId('tasks.row.target.780').click();
  194 |     await expect(page).toHaveURL(/\/admin\/vps\/123\?user=42$/);
  195 |   });
  196 | 
  197 |   test('names the VPS before generating a root password from the detail actions', async ({ page }) => {
```