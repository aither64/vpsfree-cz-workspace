# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/security_advisories_admin.spec.ts >> @smoke Security advisory admin management >> creates a localized draft together with normalized CVE references
- Location: e2e/specs/app/security_advisories_admin.spec.ts:11:3

# Error details

```
Error: expect(page).toHaveURL(expected) failed

Expected pattern: /\/admin\/security-advisories\/77$/
Received string:  "http://127.0.0.1:5187/admin/security-advisories"
Timeout: 15000ms

Call log:
  - Expect "toHaveURL" with timeout 15000ms
    32 × unexpected value "http://127.0.0.1:5187/admin/security-advisories"

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
  - link "View commit 96d9c996f355":
    - /url: https://github.com/vpsfreecz/vpsadmin-webui/commit/96d9c996f3556a8e5d4322e79c11b0657564d33d
    - text: 96d9c996f355
- banner:
  - search:
    - combobox "Quickly search objects"
    - text: Ctrl K · /
  - text: Admin view
  - button "Open tasks": Tasks
  - button "Open account menu": security-admin admin
- main:
  - heading "Security advisories" [level=1]
  - paragraph: Create, publish, and maintain security advisories, related CVEs, affected nodes, updates, and outages.
  - button "Refresh"
  - button "New advisory" [disabled]
  - text: Search advisories
  - textbox "Search advisories Page 1 of 1":
    - /placeholder: Search by name, summary, ID, or exact CVE…
  - text: Page 1 of 1
  - combobox:
    - option "All states" [selected]
    - option "Draft"
    - option "Published"
    - option "Retracted"
  - combobox:
    - option "Newest first" [selected]
    - option "Oldest first"
  - text: No security advisories Create a draft to start documenting a vulnerability and its remediation.
  - button "Prev" [disabled]
  - button "Page 1 (current)": "1"
  - button "Next" [disabled]
  - text: Page 1 of 1 Rows
  - combobox:
    - option "25" [selected]
    - option "50"
    - option "100"
  - text: "CVE changes need review Draft created; review the CVE changes. #77 Requested CVEs: CVE-2026-12345, CVE-2026-23456 Accepted changes: — Changes to review: CVE-2026-12345, CVE-2026-23456 AdvisoryDraftConflictError: Advisory draft changed Some changes may already have been applied. Review the current advisory before submitting more changes."
  - link "Review advisory":
    - /url: /admin/security-advisories/77
- dialog "Create security advisory":
  - text: "Create security advisory CVE changes need review Draft created; review the CVE changes. #77 Requested CVEs: CVE-2026-12345, CVE-2026-23456 Accepted changes: — Changes to review: CVE-2026-12345, CVE-2026-23456 AdvisoryDraftConflictError: Advisory draft changed Some changes may already have been applied. Review the current advisory before submitting more changes."
  - link "Review advisory":
    - /url: /admin/security-advisories/77
  - text: "Error AdvisoryDraftConflictError: Advisory draft changed CVEs"
  - textbox "CVEs Enter one or more CVE identifiers separated by commas or whitespace.":
    - /placeholder: CVE-2026-12345, CVE-2026-23456
    - text: cve-2026-12345; CVE-2026-23456
  - text: Enter one or more CVE identifiers separated by commas or whitespace. Vulnerability name
  - textbox "Vulnerability name Optional well-known public name. It may be shown on public advisory pages.":
    - /placeholder: For example, Dirty Pipe
    - text: Linux kernel advisory
  - text: Optional well-known public name. It may be shown on public advisory pages. Publication date
  - textbox "Publication date Leave empty while preparing a draft, or set the intended publication time.": 2026-07-27T12:30
  - text: Leave empty while preparing a draft, or set the intended publication time.
  - tablist "Advisory translations":
    - tab "English ✓"
    - tab "Čeština ✓" [selected]
  - tabpanel:
    - text: Summary
    - textbox "Summary A short public title is required in every supported language.": Zranitelnost kernelu
    - text: A short public title is required in every supported language. Description
    - textbox "Description": Týká se podporovaných výpočetních nodů.
    - text: Response and recommendations
    - textbox "Response and recommendations": Nasaď opravený kernel a restartuj.
  - button "Cancel"
  - button "Create draft" [disabled]
```

# Test source

```ts
  1   | import { expect, test } from '@playwright/test';
  2   | 
  3   | import { bootstrapVpsAdminWindow, failEnvelope, installHaveApiMock } from '../../fixtures';
  4   | 
  5   | const languages = [
  6   |   { id: 1, code: 'en', label: 'English' },
  7   |   { id: 2, code: 'cs', label: 'Čeština' },
  8   | ];
  9   | 
  10  | test.describe('@smoke Security advisory admin management', () => {
  11  |   test('creates a localized draft together with normalized CVE references', async ({ page }) => {
  12  |     let advisoryPayload: any;
  13  |     const cvePayloads: any[] = [];
  14  |     let createdAdvisory: Record<string, unknown> | null = null;
  15  |     const createdCves: Array<Record<string, unknown>> = [];
  16  | 
  17  |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  18  |     await installHaveApiMock(page, {
  19  |       user: { id: 1, login: 'security-admin', level: 90 },
  20  |       handlers: {
  21  |         'GET languages': () => ({ languages }),
  22  |         'GET security_advisories': () => ({ security_advisories: [] }),
  23  |         'POST security_advisories': ({ reqJson }) => {
  24  |           advisoryPayload = reqJson;
  25  |           createdAdvisory = {
  26  |             id: 77,
  27  |             state: 'draft',
  28  |             created_at: '2026-07-27T10:00:00.000Z',
  29  |             ...(advisoryPayload?.security_advisory ?? {}),
  30  |           };
  31  |           return { security_advisory: createdAdvisory };
  32  |         },
  33  |         'POST security_advisory_cves': ({ reqJson }) => {
  34  |           cvePayloads.push(reqJson);
  35  |           const cve = {
  36  |             id: 900 + cvePayloads.length,
  37  |             security_advisory_id: 77,
  38  |             ...(reqJson as any)?.security_advisory_cve,
  39  |           };
  40  |           createdCves.push(cve);
  41  |           return { security_advisory_cve: cve };
  42  |         },
  43  | 
  44  |         // The successful create navigates straight to the detail. Keep that
  45  |         // route deterministic as well so the assertion cannot race a failed
  46  |         // background query.
  47  |         'GET security_advisories/77': () => ({ security_advisory: createdAdvisory }),
  48  |         'GET security_advisory_cves': () => ({ security_advisory_cves: createdCves }),
  49  |         'GET nodes': () => ({ nodes: [] }),
  50  |         'GET security_advisories/77/node_statuses': () => ({ node_statuses: [] }),
  51  |         'GET security_advisory_updates': () => ({ security_advisory_updates: [] }),
  52  |         'GET outage_security_advisories': () => ({ outage_security_advisories: [] }),
  53  |       },
  54  |     });
  55  | 
  56  |     await page.goto('/admin/security-advisories');
  57  |     await expect(page.getByTestId('admin.security_advisories.page')).toBeVisible();
  58  |     await page.getByTestId('admin.security_advisories.create').click();
  59  |     await expect(page.getByTestId('admin.security_advisories.editor')).toBeVisible();
  60  | 
  61  |     await page
  62  |       .getByTestId('admin.security_advisories.editor.cves')
  63  |       .fill('cve-2026-12345; CVE-2026-23456');
  64  |     await page.getByTestId('admin.security_advisories.editor.name').fill('Linux kernel advisory');
  65  |     await page.getByTestId('admin.security_advisories.editor.published_at').fill('2026-07-27T12:30');
  66  | 
  67  |     await page.getByTestId('admin.security_advisories.editor.en.summary').fill('Kernel vulnerability');
  68  |     await page
  69  |       .getByTestId('admin.security_advisories.editor.en.description')
  70  |       .fill('Affects supported compute nodes.');
  71  |     await page
  72  |       .getByTestId('admin.security_advisories.editor.en.response')
  73  |       .fill('Apply the fixed kernel and reboot.');
  74  | 
  75  |     await page.getByTestId('admin.security_advisories.editor.language.cs').click();
  76  |     await page.getByTestId('admin.security_advisories.editor.cs.summary').fill('Zranitelnost kernelu');
  77  |     await page
  78  |       .getByTestId('admin.security_advisories.editor.cs.description')
  79  |       .fill('Týká se podporovaných výpočetních nodů.');
  80  |     await page
  81  |       .getByTestId('admin.security_advisories.editor.cs.response')
  82  |       .fill('Nasaď opravený kernel a restartuj.');
  83  | 
  84  |     await page.getByTestId('admin.security_advisories.editor.save').click();
  85  | 
> 86  |     await expect(page).toHaveURL(/\/admin\/security-advisories\/77$/);
      |                        ^ Error: expect(page).toHaveURL(expected) failed
  87  |     await expect.poll(() => cvePayloads.length).toBe(2);
  88  |     expect(advisoryPayload).toEqual({
  89  |       security_advisory: expect.objectContaining({
  90  |         name: 'Linux kernel advisory',
  91  |         published_at: expect.any(String),
  92  |         en_summary: 'Kernel vulnerability',
  93  |         en_description: 'Affects supported compute nodes.',
  94  |         en_response: 'Apply the fixed kernel and reboot.',
  95  |         cs_summary: 'Zranitelnost kernelu',
  96  |         cs_description: 'Týká se podporovaných výpočetních nodů.',
  97  |         cs_response: 'Nasaď opravený kernel a restartuj.',
  98  |       }),
  99  |     });
  100 |     expect(cvePayloads).toEqual([
  101 |       { security_advisory_cve: { security_advisory: 77, cve_id: 'CVE-2026-12345' } },
  102 |       { security_advisory_cve: { security_advisory: 77, cve_id: 'CVE-2026-23456' } },
  103 |     ]);
  104 |   });
  105 | 
  106 |   test('gates publishing, manages node assessments, retracts through an update and links an outage', async ({
  107 |     page,
  108 |   }) => {
  109 |     const mutations: Array<{ method: string; path: string; body: any }> = [];
  110 |     let advisory = {
  111 |       id: 77,
  112 |       state: 'draft',
  113 |       name: 'Linux kernel advisory',
  114 |       published_at: null as string | null,
  115 |       created_at: '2026-07-27T10:00:00.000Z',
  116 |       en_summary: 'Kernel vulnerability',
  117 |       en_description: 'Affects supported compute nodes.',
  118 |       en_response: 'Apply the fixed kernel and reboot.',
  119 |       cs_summary: 'Zranitelnost kernelu',
  120 |       cs_description: 'Týká se podporovaných výpočetních nodů.',
  121 |       cs_response: 'Nasaď opravený kernel a restartuj.',
  122 |       affected_node_count: 2,
  123 |       affected_user_count: 4,
  124 |       affected_vps_count: 8,
  125 |     };
  126 |     const cves = [
  127 |       { id: 901, security_advisory_id: 77, cve_id: 'CVE-2026-12345' },
  128 |     ];
  129 |     const nodes = [
  130 |       { id: 10, active: true, type: 'node', domain_name: 'node10.prg' },
  131 |       { id: 20, active: true, type: 'storage', domain_name: 'storage20.prg' },
  132 |       { id: 30, active: false, type: 'node', domain_name: 'retired30.prg' },
  133 |     ];
  134 |     let statuses = [
  135 |       {
  136 |         id: 501,
  137 |         security_advisory_id: 77,
  138 |         node_id: 10,
  139 |         node: nodes[0],
  140 |         state: 'unknown',
  141 |         vulnerable_until: null,
  142 |         mitigated_since: null,
  143 |         note: null,
  144 |       },
  145 |       {
  146 |         id: 502,
  147 |         security_advisory_id: 77,
  148 |         node_id: 20,
  149 |         node: nodes[1],
  150 |         state: 'not_affected',
  151 |         vulnerable_until: null,
  152 |         mitigated_since: null,
  153 |         note: 'Storage is not affected',
  154 |       },
  155 |     ];
  156 |     let updates: Array<Record<string, unknown>> = [];
  157 |     let outageLinks: Array<Record<string, unknown>> = [];
  158 | 
  159 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  160 |     await installHaveApiMock(page, {
  161 |       user: { id: 1, login: 'security-admin', level: 90 },
  162 |       handlers: {
  163 |         'GET languages': () => ({ languages }),
  164 |         'GET security_advisories/77': () => ({ security_advisory: advisory }),
  165 |         'GET security_advisory_cves': () => ({ security_advisory_cves: cves }),
  166 |         'GET nodes': () => ({ nodes }),
  167 |         'GET security_advisories/77/node_statuses': () => ({ node_statuses: statuses }),
  168 |         'GET security_advisory_updates': () => ({ security_advisory_updates: updates }),
  169 |         'GET outage_security_advisories': () => ({ outage_security_advisories: outageLinks }),
  170 | 
  171 |         'PUT security_advisories/77/node_statuses/501': ({ reqJson }) => {
  172 |           const attrs = (reqJson as any)?.node_status ?? {};
  173 |           statuses = statuses.map((status) =>
  174 |             status.id === 501 ? { ...status, ...attrs, node_id: 10, node: nodes[0] } : status,
  175 |           );
  176 |           return { node_status: statuses.find((status) => status.id === 501) };
  177 |         },
  178 |         'PUT security_advisories/77/node_statuses/502': ({ reqJson }) => {
  179 |           const attrs = (reqJson as any)?.node_status ?? {};
  180 |           statuses = statuses.map((status) =>
  181 |             status.id === 502 ? { ...status, ...attrs, node_id: 20, node: nodes[1] } : status,
  182 |           );
  183 |           return { node_status: statuses.find((status) => status.id === 502) };
  184 |         },
  185 |         'POST security_advisories/77/publish': ({ reqJson }) => {
  186 |           const attrs = (reqJson as any)?.security_advisory ?? {};
```