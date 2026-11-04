# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: admin/security_advisory_nodes_mobile_actions.spec.ts >> @pr-smoke @pr-smoke-mobile security advisory node actions stay directly usable on mobile
- Location: e2e/specs/admin/security_advisory_nodes_mobile_actions.spec.ts:27:1

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: getByTestId('admin.security_advisories.nodes.editor')
Expected: visible
Timeout: 15000ms
Error: element(s) not found

Call log:
  - Expect "toBeVisible" with timeout 15000ms
  - waiting for getByTestId('admin.security_advisories.nodes.editor')

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
  - button "Open account menu": security-admin admin
- main:
  - heading "Linux kernel advisory" [level=1]
  - paragraph: "Security advisory #77"
  - text: Draft
  - link "CVE-2026-12345":
    - /url: https://www.cve.org/CVERecord?id=CVE-2026-12345
  - link "Back to list":
    - /url: /admin/security-advisories
  - button "Edit"
  - button "Recalculate affected VPS"
  - button "Publish"
  - navigation "Security advisory sections":
    - button "Overview"
    - button "Nodes"
    - button "Affected users and VPS"
    - button "Updates"
    - button "Outages"
  - text: Node status Record whether each active compute or storage node is affected and when it was mitigated.
  - button "Set all nodes"
  - table:
    - rowgroup:
      - row "Node Type State Vulnerable until Mitigated since Note Actions":
        - columnheader "Node"
        - columnheader "Type"
        - columnheader "State"
        - columnheader "Vulnerable until"
        - columnheader "Mitigated since"
        - columnheader "Note"
        - columnheader "Actions"
    - rowgroup:
      - 'row "very-long-security-node-name-without-shortcuts.example.test #10 Compute node Mitigated 9/16/2026, 11:00:00 AM 9/16/2026, 12:00:00 PM — Edit Remove status"':
        - 'cell "very-long-security-node-name-without-shortcuts.example.test #10"'
        - cell "Compute node"
        - cell "Mitigated"
        - cell "9/16/2026, 11:00:00 AM"
        - cell "9/16/2026, 12:00:00 PM"
        - cell "—"
        - cell "Edit Remove status":
          - button "Edit"
          - button "Remove status"
```

# Test source

```ts
  23  |   type: 'node',
  24  |   domain_name: 'very-long-security-node-name-without-shortcuts.example.test',
  25  | };
  26  | 
  27  | test('@pr-smoke @pr-smoke-mobile security advisory node actions stay directly usable on mobile', async ({
  28  |   page,
  29  | }, testInfo) => {
  30  |   const mobile = testInfo.project.name === 'mobile-chrome';
  31  |   const mutations: Array<{ method: string; path: string }> = [];
  32  | 
  33  |   if (mobile) await page.setViewportSize({ width: 320, height: 740 });
  34  | 
  35  |   await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  36  |   await installHaveApiMock(page, {
  37  |     user: { id: 1, login: 'security-admin', level: 90 },
  38  |     handlers: {
  39  |       'GET languages': () => ({ languages: [{ id: 1, code: 'en', label: 'English' }] }),
  40  |       'GET security_advisories/77': () => ({ security_advisory: advisory }),
  41  |       'GET security_advisory_cves': () => ({
  42  |         security_advisory_cves: [{ id: 901, security_advisory_id: 77, cve_id: 'CVE-2026-12345' }],
  43  |       }),
  44  |       'GET nodes': () => ({ nodes: [node] }),
  45  |       'GET security_advisories/77/node_statuses': () => ({
  46  |         node_statuses: [
  47  |           {
  48  |             id: 501,
  49  |             security_advisory_id: 77,
  50  |             node_id: node.id,
  51  |             node,
  52  |             state: 'mitigated',
  53  |             vulnerable_until: '2026-09-16T09:00:00.000Z',
  54  |             mitigated_since: '2026-09-16T10:00:00.000Z',
  55  |             note: 'A-very-long-assessment-note-that-must-wrap-within-the-mobile-card-without-hiding-actions',
  56  |           },
  57  |         ],
  58  |       }),
  59  |       'GET security_advisory_updates': () => ({ security_advisory_updates: [] }),
  60  |       'GET outage_security_advisories': () => ({ outage_security_advisories: [] }),
  61  |     },
  62  |   });
  63  | 
  64  |   page.on('request', (request) => {
  65  |     const url = new URL(request.url());
  66  |     if (!url.pathname.includes('/security_advisories/77/node_statuses')) return;
  67  |     if (request.method() === 'GET') return;
  68  |     mutations.push({ method: request.method(), path: url.pathname });
  69  |   });
  70  | 
  71  |   await page.goto('/admin/security-advisories/77?tab=nodes');
  72  | 
  73  |   const panel = page.getByTestId('admin.security_advisories.nodes.panel');
  74  |   const tableCard = page.getByTestId('admin.security_advisories.nodes.table');
  75  |   const row = page.getByTestId(`admin.security_advisories.nodes.row.${node.id}`);
  76  |   const bulk = page.getByTestId('admin.security_advisories.nodes.bulk.open');
  77  |   const edit = page.getByTestId(`admin.security_advisories.nodes.row.${node.id}.edit`);
  78  |   const remove = page.getByTestId(`admin.security_advisories.nodes.row.${node.id}.delete`);
  79  | 
  80  |   await expect(panel).toBeVisible();
  81  |   await expect(row).toBeVisible();
  82  |   await expect(tableCard.getByRole('table')).toBeVisible();
  83  |   await row.scrollIntoViewIfNeeded();
  84  |   await expectNoDocumentHorizontalOverflow(page);
  85  | 
  86  |   const layout = await tableCard.evaluate((card) => {
  87  |     const scroller = card.firstElementChild as HTMLElement;
  88  |     const table = scroller.querySelector('table') as HTMLTableElement;
  89  |     return {
  90  |       clientWidth: scroller.clientWidth,
  91  |       scrollWidth: scroller.scrollWidth,
  92  |       scrollLeft: scroller.scrollLeft,
  93  |       tableDisplay: getComputedStyle(table).display,
  94  |       tableMinWidth: Number.parseFloat(getComputedStyle(table).minWidth) || 0,
  95  |     };
  96  |   });
  97  | 
  98  |   if (mobile) {
  99  |     expect(layout.scrollWidth).toBeLessThanOrEqual(layout.clientWidth + 1);
  100 |     expect(layout.scrollLeft).toBe(0);
  101 |     expect(layout.tableDisplay).toBe('block');
  102 |     await expect(row.getByText('Node', { exact: true })).toBeVisible();
  103 |     await expect(row.getByText('Actions', { exact: true })).toBeVisible();
  104 |     await expect(edit).toBeInViewport();
  105 |     await expect(remove).toBeInViewport();
  106 |     expect((await bulk.boundingBox())?.height).toBeGreaterThanOrEqual(44);
  107 |     expect((await edit.boundingBox())?.height).toBeGreaterThanOrEqual(44);
  108 |     expect((await remove.boundingBox())?.height).toBeGreaterThanOrEqual(44);
  109 |   } else {
  110 |     expect(layout.tableDisplay).toBe('table');
  111 |     expect(layout.tableMinWidth).toBeGreaterThanOrEqual(840);
  112 |     await expect(tableCard.getByRole('columnheader', { name: 'Node' })).toBeVisible();
  113 |     expect((await bulk.boundingBox())?.height).toBe(36);
  114 |     expect((await edit.boundingBox())?.height).toBe(32);
  115 |     expect((await remove.boundingBox())?.height).toBe(32);
  116 |   }
  117 | 
  118 |   const proofScreenshot = process.env.E2E_SECURITY_NODE_ACTIONS_PROOF_SCREENSHOT?.trim();
  119 |   if (proofScreenshot) await page.screenshot({ path: proofScreenshot, fullPage: true });
  120 | 
  121 |   await edit.click();
  122 |   const editor = page.getByTestId('admin.security_advisories.nodes.editor');
> 123 |   await expect(editor).toBeVisible();
      |                        ^ Error: expect(locator).toBeVisible() failed
  124 |   await editor.getByRole('button', { name: 'Cancel' }).click();
  125 |   await expect(editor).toHaveCount(0);
  126 | 
  127 |   await remove.click();
  128 |   await expect(page.getByTestId('admin.security_advisories.nodes.delete')).toBeVisible();
  129 |   await page.getByTestId('admin.security_advisories.nodes.delete.cancel').click();
  130 |   await expect(page.getByTestId('admin.security_advisories.nodes.delete')).toHaveCount(0);
  131 |   expect(mutations).toEqual([]);
  132 | });
  133 | 
```