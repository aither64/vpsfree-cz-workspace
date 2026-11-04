# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/vps_network_tab_actions.spec.ts >> @pr-smoke VPS network tab >> edits interface and sends PUT
- Location: e2e/specs/app/vps_network_tab_actions.spec.ts:82:3

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: getByTestId('vps.network.page')
Expected: visible
Timeout: 15000ms
Error: element(s) not found

Call log:
  - Expect "toBeVisible" with timeout 15000ms
  - waiting for getByTestId('vps.network.page')

```

```yaml
- link "Skip to main content":
  - /url: "#main-content"
- complementary:
  - text: VA vpsAdmin next UI
  - navigation:
    - link "Dashboard":
      - /url: /admin
    - region "Services":
      - text: Services
      - link "VPS":
        - /url: /admin/vps
      - link "Datasets":
        - /url: /admin/datasets
      - link "NAS":
        - /url: /admin/nas
      - link "Exports":
        - /url: /admin/exports
      - link "DNS":
        - /url: /admin/dns
      - link "Networking":
        - /url: /admin/networking/ip-addresses
    - region "Operations":
      - text: Operations
      - link "Transactions":
        - /url: /admin/transactions
      - link "Monitoring":
        - /url: /admin/monitoring
      - link "Incidents":
        - /url: /admin/incidents
      - link "Out-of-memory":
        - /url: /admin/oom-reports
      - link "Audit":
        - /url: /admin/audit
    - region "Users and finance":
      - text: Users and finance
      - link "Users":
        - /url: /admin/users
      - link "User namespaces":
        - /url: /admin/user-namespaces/namespaces
      - link "Requests":
        - /url: /admin/requests
      - link "Finance":
        - /url: /admin/payments/incoming
    - region "Infrastructure":
      - text: Infrastructure
      - link "Cluster":
        - /url: /admin/cluster/summary
      - link "Nodes":
        - /url: /admin/nodes
      - link "Migration plans":
        - /url: /admin/migration-plans
      - link "Admin":
        - /url: /admin/admin-info
    - region "Content":
      - text: Content
      - link "Mailer":
        - /url: /admin/mailer/templates
      - link "News and help":
        - /url: /admin/content/news
  - link "Account":
    - /url: /admin/profile
  - navigation "Service status":
    - link "Outages":
      - /url: /admin/outages
    - link "Security advisories":
      - /url: /admin/security-advisories
  - link "About":
    - /url: /about
  - link "View commit ad5327eba649":
    - /url: https://github.com/vpsfreecz/vpsadmin-webui/commit/ad5327eba64919d58cede22186958ff0e0ad0b77
    - text: ad5327eba649
- banner:
  - search:
    - combobox "Quickly search objects"
    - text: Ctrl K · /
  - text: Admin view
  - button "Open tasks": Tasks
  - button "Open account menu": admin admin
- main:
  - text: Failed to load VPS Please try again.
  - button "Retry"
  - link "Back":
    - /url: /admin/vps
  - link "Status":
    - /url: /
  - button "Copy details"
  - group: Details
```

# Test source

```ts
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
  20  |   node: { id: 1, domain_name: 'node1.example', location: { id: 10, label: 'Prague' } },
  21  |   os_template: { label: 'debian' },
  22  |   dns_resolver: 'inherit',
  23  | };
  24  | 
  25  | const netifs = [
  26  |   {
  27  |     id: 1,
  28  |     name: 'eth0',
  29  |     type: 'virtio',
  30  |     enable: false,
  31  |     max_tx: 100 * 1024 * 1024,
  32  |     max_rx: 200 * 1024 * 1024,
  33  |   },
  34  | ];
  35  | 
  36  | const ips = [
  37  |   {
  38  |     id: 1,
  39  |     addr: '198.51.100.10',
  40  |     network_interface: { id: 1 },
  41  |     network: {
  42  |       role: 'public_access',
  43  |       purpose: 'vps',
  44  |       ip_version: 4,
  45  |       location: { id: 10, label: 'Prague' },
  46  |       primary_location: { id: 10, label: 'Prague' },
  47  |     },
  48  |     user: { id: 20, login: 'old-owner' },
  49  |     routed: true,
  50  |   },
  51  |   {
  52  |     id: 2,
  53  |     addr: '198.51.100.20',
  54  |     network_interface: null,
  55  |     network: {
  56  |       role: 'public_access',
  57  |       purpose: 'vps',
  58  |       ip_version: 4,
  59  |       location: { id: 10, label: 'Prague' },
  60  |       primary_location: { id: 10, label: 'Prague' },
  61  |     },
  62  |     user: { id: 20, login: 'old-owner' },
  63  |   },
  64  | ];
  65  | 
  66  | const acct = [{ id: 1, bytes_in: 1024, bytes_out: 2048 }];
  67  | 
  68  | 
  69  | async function openAdminNetworkSettings(page: Page) {
  70  |   await page.getByTestId('vps.network.admin_settings.toggle').click();
  71  | }
  72  | 
  73  | function interfaceEditButton(page: Page) {
  74  |   return page.getByTestId(
  75  |     (page.viewportSize()?.width ?? 0) < 768
  76  |       ? 'vps.network.interfaces.card.1.edit'
  77  |       : 'vps.network.interfaces.row.1.edit'
  78  |   );
  79  | }
  80  | 
  81  | test.describe('@pr-smoke VPS network tab', () => {
  82  |   test('edits interface and sends PUT', async ({ page }) => {
  83  |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  84  | 
  85  |     await installHaveApiMock(page, {
  86  |       user: { id: 1, login: 'admin', level: 90 },
  87  |       handlers: {
  88  |         'GET vpses/123': () => ({ vps }),
  89  |         'GET ip_addresses': () => ({ ip_addresses: ips }),
  90  |         'GET host_ip_addresses': () => ({ host_ip_addresses: [] }),
  91  |         'GET environments': () => ({ environments: [] }),
  92  |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  93  |         'GET network_interfaces': () => ({ network_interfaces: netifs }),
  94  |         'GET network_interface_accountings': () => ({ network_interface_accountings: acct }),
  95  |         'PUT network_interfaces/1': () => ({
  96  |           network_interface: { ...netifs[0] },
  97  |           _meta: { action_state_id: 1201 },
  98  |         }),
  99  |         'GET action_states/1201': () => ({ action_state: { id: 1201, finished: true, status: true, current: 1, total: 1 } }),
  100 |       },
  101 |     });
  102 | 
  103 |     await page.goto('/admin/vps/123/network');
  104 | 
> 105 |     await expect(page.getByTestId('vps.network.page')).toBeVisible();
      |                                                        ^ Error: expect(locator).toBeVisible() failed
  106 |     if ((page.viewportSize()?.width ?? 0) < 768) {
  107 |       await expect(page.getByTestId('vps.network.interfaces.card.1')).toBeVisible();
  108 |       await expect(page.getByTestId('vps.network.interfaces.card.1.dot')).toBeVisible();
  109 |     } else {
  110 |       await expect(page.getByTestId('vps.network.interfaces.table')).toBeVisible();
  111 |       await expect(page.getByTestId('vps.network.interfaces.row.1')).toHaveAttribute('data-row-variant', 'warn');
  112 |       await expect(page.getByTestId('vps.network.interfaces.row.1.dot')).toBeVisible();
  113 |     }
  114 | 
  115 |     await interfaceEditButton(page).click();
  116 |     await expect(page.getByTestId('vps.network.edit')).toBeVisible();
  117 | 
  118 |     await page.getByTestId('vps.network.edit.name').fill('eth0-renamed');
  119 |     await page.getByTestId('vps.network.edit.max_tx').fill('500');
  120 |     await page.getByTestId('vps.network.edit.max_rx').fill('600');
  121 | 
  122 |     const reqPromise = page.waitForRequest(
  123 |       (r) => r.method() === 'PUT' && r.url().includes('/api/v7.0/network_interfaces/1')
  124 |     );
  125 | 
  126 |     await page.getByTestId('vps.network.edit.save').click();
  127 | 
  128 |     const req = await reqPromise;
  129 |     expect(req.postDataJSON()).toEqual({
  130 |       network_interface: {
  131 |         name: 'eth0-renamed',
  132 |         enable: false,
  133 |         max_tx: 500 * 1024 * 1024,
  134 |         max_rx: 600 * 1024 * 1024,
  135 |       },
  136 |     });
  137 | 
  138 |     await expect(page.getByTestId('vps.network.edit')).toBeHidden();
  139 |   });
  140 | 
  141 |   test('keeps an in-flight interface edit bound to its original VPS after route rerender', async ({ page }) => {
  142 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  143 | 
  144 |     let releaseUpdate!: () => void;
  145 |     const updateGate = new Promise<void>((resolve) => {
  146 |       releaseUpdate = resolve;
  147 |     });
  148 | 
  149 |     await installHaveApiMock(page, {
  150 |       user: { id: 1, login: 'admin', level: 90 },
  151 |       handlers: {
  152 |         'GET vpses/123': () => ({ vps }),
  153 |         'GET vpses/456': () => ({ vps: { ...vps, id: 456, hostname: 'vps456.example' } }),
  154 |         'GET ip_addresses': () => ({ ip_addresses: ips }),
  155 |         'GET host_ip_addresses': () => ({ host_ip_addresses: [] }),
  156 |         'GET environments': () => ({ environments: [] }),
  157 |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  158 |         'GET network_interfaces': () => ({ network_interfaces: netifs }),
  159 |         'GET network_interface_accountings': () => ({ network_interface_accountings: acct }),
  160 |         'PUT network_interfaces/1': async () => {
  161 |           await updateGate;
  162 |           return { network_interface: { ...netifs[0] }, _meta: { action_state_id: 1250 } };
  163 |         },
  164 |         'GET action_states/1250': () => ({ action_state: { id: 1250, finished: true, status: true, current: 1, total: 1 } }),
  165 |       },
  166 |     });
  167 | 
  168 |     await page.goto('/admin/vps/123/network');
  169 |     await interfaceEditButton(page).click();
  170 |     await page.getByTestId('vps.network.edit.name').fill('vps123-interface');
  171 | 
  172 |     const originalRequest = page.waitForRequest(
  173 |       (request) => request.method() === 'PUT' && request.url().includes('/api/v7.0/network_interfaces/1')
  174 |     );
  175 |     await page.getByTestId('vps.network.edit.save').click();
  176 |     expect((await originalRequest).postDataJSON()).toMatchObject({ network_interface: { name: 'vps123-interface' } });
  177 | 
  178 |     await page.evaluate(() => {
  179 |       window.history.pushState({}, '', '/admin/vps/456/network');
  180 |       window.dispatchEvent(new PopStateEvent('popstate'));
  181 |     });
  182 |     await expect(page.getByText('vps456.example')).toBeVisible();
  183 |     await expect(page.getByTestId('vps.network.edit')).toHaveCount(0);
  184 |     await interfaceEditButton(page).click();
  185 |     await page.getByTestId('vps.network.edit.name').fill('vps456-unsaved');
  186 |     releaseUpdate();
  187 | 
  188 |     await expect(page.getByTestId('vps.network.edit')).toBeVisible();
  189 |     await expect(page.getByTestId('vps.network.edit.name')).toHaveValue('vps456-unsaved');
  190 |   });
  191 | 
  192 |   test('disables VPS networking with a change reason', async ({ page }) => {
  193 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  194 | 
  195 |     let enabled = true;
  196 | 
  197 |     await installHaveApiMock(page, {
  198 |       user: { id: 1, login: 'admin', level: 90 },
  199 |       handlers: {
  200 |         'GET vpses/123': () => ({ vps: { ...vps, enable_network: enabled } }),
  201 |         'GET ip_addresses': () => ({ ip_addresses: ips }),
  202 |         'GET host_ip_addresses': () => ({ host_ip_addresses: [] }),
  203 |         'GET environments': () => ({ environments: [] }),
  204 |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  205 |         'GET network_interfaces': () => ({ network_interfaces: netifs }),
```