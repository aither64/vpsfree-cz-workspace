# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: admin/ip_assignment_vps_first.spec.ts >> @pr-smoke @pr-smoke-mobile a foreign-owned address cannot implicitly change owner during assignment
- Location: e2e/specs/admin/ip_assignment_vps_first.spec.ts:115:1

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: getByTestId('admin.ip.route.dialog')
Expected: visible
Error: element(s) not found

Call log:
  - Expect "toBeVisible" with timeout 15000ms
  - waiting for getByTestId('admin.ip.route.dialog')

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
  - link "View commit dc95fbca818d":
    - /url: https://github.com/vpsfreecz/vpsadmin-webui/commit/dc95fbca818d3de38b5b65be6ff633d8529ed58c
    - text: dc95fbca818d
- banner:
  - search:
    - combobox "Quickly search objects"
    - text: Ctrl K · /
  - text: Admin view
  - button "Open tasks": Tasks
  - button "Open account menu": synthetic-admin admin
- main:
  - heading "Networking" [level=1]
  - paragraph: Advanced IP, assignment, and traffic tooling.
  - link "IP addresses":
    - /url: /admin/networking/ip-addresses
  - link "Host IPs":
    - /url: /admin/networking/host-ip-addresses
  - link "Assignments":
    - /url: /admin/networking/ip-address-assignments
  - link "Live":
    - /url: /admin/networking/live
  - link "Top users":
    - /url: /admin/networking/traffic-users
  - text: Loading…
```

# Test source

```ts
  1   | import { expect, test, type Page } from '@playwright/test';
  2   | import { bootstrapVpsAdminWindow, installHaveApiMock, setUiSettingsLocalStorage } from '../../fixtures';
  3   | import { expectNoDocumentHorizontalOverflow } from '../../helpers/horizontalOverflow';
  4   | 
  5   | type Owner = { id: number; login?: string } | null;
  6   | async function fixture(page: Page, language: 'cs' | 'en' = 'en') {
  7   |   await bootstrapVpsAdminWindow(page);
  8   |   await setUiSettingsLocalStorage(page, { language, theme: 'dark' });
  9   |   const state = {
  10  |     owner: null as Owner, environment: null as { id: number } | null,
  11  |     ownerWrites: 0, assignments: [] as Array<{ path: string; payload: unknown }>,
  12  |     mismatch: false, staleTarget: false, missingInterface: false, preflightUnavailable: false, receipt: true, reject: false,
  13  |   };
  14  |   const ip = () => ({ id: 100, addr: '192.0.2.100', prefix: 32, user: state.owner,
  15  |     charged_environment: state.environment, network_interface: null,
  16  |     network: { id: 3, enabled: true, ip_version: 4, role: 'public_access',
  17  |       primary_location: { id: 3, label: 'Praha', environment: { id: 1, label: 'Production' } } } });
  18  |   const vps = (id: number) => ({ id, hostname: `fixture-${id}.example.test`,
  19  |     user: { id: state.staleTarget ? 8 : 7, login: 'synthetic-member' },
  20  |     node: { id: 1, location: { id: 3, environment: { id: 1, label: 'Production' } } } });
  21  |   const assign = (path: string, payload: unknown) => {
  22  |     state.assignments.push({ path, payload });
  23  |     if (state.reject) return { status: 409, contentType: 'application/json', body: JSON.stringify({ status: false, message: 'Address changed', response: null }) };
  24  |     return { ip_address: ip(), _meta: state.receipt ? { action_state_id: 701 } : {} };
  25  |   };
  26  |   await installHaveApiMock(page, { user: { id: 1, login: 'synthetic-admin', level: 99 }, handlers: {
  27  |     'GET locations': () => ({ locations: [{ id: 3, label: 'Praha', environment: { id: 1, label: 'Production' } }] }),
  28  |     'GET ip_addresses': () => ({ ip_addresses: [ip()] }),
  29  |     'GET ip_addresses/100': () => ({ ip_address: ip() }),
  30  |     'GET environments': () => ({ environments: [{ id: 1, label: 'Production' }] }),
  31  |     'GET host_ip_addresses': () => ({ host_ip_addresses: [] }),
  32  |     'GET vpses/123': () => ({ vps: vps(123) }),
  33  |     'GET vpses/124': () => ({ vps: vps(124) }),
  34  |     'GET network_interfaces': ({ searchParams }) => {
  35  |       if (state.preflightUnavailable) return { status: 503, contentType: 'application/json', body: JSON.stringify({ status: false, message: 'Preflight unavailable', response: null }) };
  36  |       return { network_interfaces: state.missingInterface ? [] :
  37  |         searchParams.get('network_interface[vps]') === '123'
  38  |           ? [{ id: 501, name: 'eth0', vps: { id: 123 } }]
  39  |           : [502, 503].map((id) => ({ id, name: `eth${id - 502}`, vps: { id: 124 } })) };
  40  |     },
  41  |     'POST ip_addresses/100/assign': ({ reqJson }) => assign('assign', reqJson),
  42  |     'POST ip_addresses/100/assign_with_host_address': ({ reqJson }) => assign('assign_with_host_address', reqJson),
  43  |     'PUT ip_addresses/100': () => {
  44  |       state.ownerWrites += 1;
  45  |       if (!state.mismatch) { state.owner = { id: 7 }; state.environment = { id: 1 }; }
  46  |       return { ip_address: { id: 100 }, _meta: {} };
  47  |     },
  48  |   } });
  49  |   return state;
  50  | }
  51  | async function open(page: Page) {
  52  |   await page.goto('/admin/networking/ip-addresses/100?action=assign#route');
> 53  |   await expect(page.getByTestId('admin.ip.route.dialog')).toBeVisible();
      |                                                           ^ Error: expect(locator).toBeVisible() failed
  54  | }
  55  | async function choose(page: Page, id = '123') {
  56  |   await page.getByTestId('admin.ip.route.vps').fill(id);
  57  |   await expect(page.getByTestId('admin.ip.route.target')).toContainText(`fixture-${id}`);
  58  | }
  59  | 
  60  | for (const language of ['cs', 'en'] as const) {
  61  |   test(`@pr-smoke @pr-smoke-mobile ${language} assign icon opens VPS first without an ownership write`, async ({ page, isMobile }, info) => {
  62  |     const state = await fixture(page, language);
  63  |     await page.goto('/admin/networking/ip-addresses');
  64  |     const icon = page.getByTestId(`admin.ip_addresses.${isMobile ? 'card' : 'row'}.100.action.route`);
  65  |     if (isMobile) await icon.tap(); else await icon.click();
  66  |     const dialog = page.getByTestId('admin.ip.route.dialog');
  67  |     await expect(dialog).toBeVisible();
  68  |     await expect(page.getByTestId('admin.ip.route.vps')).toBeFocused();
  69  |     await expect(dialog.getByTestId('admin.ip.owner.user')).toHaveCount(0);
  70  |     await expect(dialog.getByTestId('admin.ip.owner.environment')).toHaveCount(0);
  71  |     await choose(page);
  72  |     await expect(page.getByTestId('admin.ip.route.interface')).toHaveValue('501');
  73  |     await expect(page.getByTestId('admin.ip.route.target')).toContainText('synthetic-member');
  74  |     await expect(page.getByTestId('admin.ip.route.target')).toContainText('Production');
  75  |     await expectNoDocumentHorizontalOverflow(page);
  76  |     await dialog.screenshot({ path: info.outputPath(`vps-first-${language}.png`) });
  77  |     await page.getByTestId('admin.ip.route.submit').click();
  78  |     await expect(dialog).toBeHidden();
  79  |     expect(state.ownerWrites).toBe(0);
  80  |     expect(state.assignments).toEqual([{ path: 'assign', payload: { ip_address: { network_interface: 501 } } }]);
  81  |     await page.reload();
  82  |     await expect(page.getByTestId('admin.ip_address.page')).toBeVisible();
  83  |     await expect(dialog).toBeHidden();
  84  |   });
  85  | }
  86  | 
  87  | test('@pr-smoke @pr-smoke-mobile changing VPS clears the old interface and retains the combined host action', async ({ page }) => {
  88  |   const state = await fixture(page);
  89  |   await open(page); await choose(page);
  90  |   await expect(page.getByTestId('admin.ip.route.interface')).toHaveValue('501');
  91  |   await choose(page, '124');
  92  |   await expect(page.getByTestId('admin.ip.route.interface')).toHaveValue('');
  93  |   await expect(page.getByTestId('admin.ip.route.submit')).toBeDisabled();
  94  |   await page.getByTestId('admin.ip.route.interface').selectOption('503');
  95  |   await page.getByTestId('admin.ip.route.dialog').getByRole('checkbox').check();
  96  |   await page.getByTestId('admin.ip.route.submit').click();
  97  |   await expect(page.getByTestId('admin.ip.route.dialog')).toBeHidden();
  98  |   expect(state.assignments).toEqual([{ path: 'assign_with_host_address', payload: { ip_address: { network_interface: 503 } } }]);
  99  | });
  100 | 
  101 | for (const change of ['owner', 'interface'] as const) {
  102 |   test(`@pr-smoke @pr-smoke-mobile fresh ${change} change blocks assignment before any write`, async ({ page }) => {
  103 |     const state = await fixture(page);
  104 |     await open(page); await choose(page);
  105 |     await expect(page.getByTestId('admin.ip.route.submit')).toBeEnabled();
  106 |     if (change === 'owner') state.staleTarget = true;
  107 |     else state.missingInterface = true;
  108 |     await page.getByTestId('admin.ip.route.submit').click();
  109 |     await expect(page.getByTestId('admin.ip.route.error')).toContainText('changed');
  110 |     expect(state.assignments).toEqual([]);
  111 |     expect(state.ownerWrites).toBe(0);
  112 |   });
  113 | }
  114 | 
  115 | test('@pr-smoke @pr-smoke-mobile a foreign-owned address cannot implicitly change owner during assignment', async ({ page }) => {
  116 |   const state = await fixture(page); state.owner = { id: 9, login: 'other-member' };
  117 |   await open(page); await choose(page);
  118 |   await expect(page.getByTestId('admin.ip.route.dialog')).toContainText('another member');
  119 |   await expect(page.getByTestId('admin.ip.route.submit')).toBeDisabled();
  120 |   expect(state.assignments).toEqual([]);
  121 |   expect(state.ownerWrites).toBe(0);
  122 | });
  123 | 
  124 | test('@pr-smoke @pr-smoke-mobile failed preflight reads are retryable without marking a submitted mutation uncertain', async ({ page }) => {
  125 |   const state = await fixture(page);
  126 |   await open(page); await choose(page);
  127 |   await expect(page.getByTestId('admin.ip.route.submit')).toBeEnabled();
  128 |   state.preflightUnavailable = true;
  129 |   await page.getByTestId('admin.ip.route.submit').click();
  130 |   await expect(page.getByTestId('admin.ip.route.error')).toContainText('Preflight unavailable');
  131 |   await expect(page.getByTestId('admin.ip.route.submit')).toBeEnabled();
  132 |   await expect(page.getByTestId('admin.ip.owner.uncertain')).toHaveCount(0);
  133 |   expect(state.assignments).toHaveLength(0);
  134 |   state.preflightUnavailable = false;
  135 |   await page.getByTestId('admin.ip.route.submit').click();
  136 |   await expect(page.getByTestId('admin.ip.route.dialog')).toBeHidden();
  137 |   expect(state.assignments).toHaveLength(1);
  138 | });
  139 | 
  140 | test('@pr-smoke @pr-smoke-mobile an API rejection keeps VPS context and permits deliberate retry', async ({ page }) => {
  141 |   const state = await fixture(page); state.reject = true;
  142 |   await open(page); await choose(page);
  143 |   await page.getByTestId('admin.ip.route.submit').click();
  144 |   await expect(page.getByTestId('admin.ip.route.error')).toContainText('Address changed');
  145 |   await expect(page.getByTestId('admin.ip.route.interface')).toHaveValue('501');
  146 |   state.reject = false;
  147 |   await page.getByTestId('admin.ip.route.submit').click();
  148 |   await expect(page.getByTestId('admin.ip.route.dialog')).toBeHidden();
  149 |   expect(state.assignments).toHaveLength(2);
  150 | });
  151 | 
  152 | test('@pr-smoke @pr-smoke-mobile a missing asynchronous receipt blocks replay across reload', async ({ page }) => {
  153 |   const state = await fixture(page); state.receipt = false;
```