# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/security_advisory_update_mutations.spec.ts >> @pr-smoke edits and deletes an advisory update with confirmation and refreshed readback
- Location: e2e/specs/app/security_advisory_update_mutations.spec.ts:61:1

# Error details

```
Error: expect(received).toEqual(expected) // deep equality

- Expected  - 1
+ Received  + 3

  Array [
-   Object {},
+   Object {
+     "security_advisory_update": Object {},
+   },
  ]
```

# Page snapshot

```yaml
- generic [active] [ref=e1]:
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
            - link "View commit 6fabda0b80e0" [ref=e194] [cursor=pointer]:
              - /url: https://github.com/vpsfreecz/vpsadmin-webui/commit/6fabda0b80e04fde4490f22ed079c83ae899f0e1
              - text: 6fabda0b80e0
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
              - generic [ref=e216]: security-admin
              - generic [ref=e217]: admin
        - main [ref=e218]:
          - generic [ref=e220]:
            - generic [ref=e221]:
              - generic [ref=e222]:
                - heading "Linux kernel advisory" [level=1] [ref=e223]
                - paragraph [ref=e224]: "Security advisory #77"
                - generic [ref=e227]: Published
              - generic [ref=e228]:
                - link "Back to list" [ref=e229] [cursor=pointer]:
                  - /url: /admin/security-advisories
                - button "Recalculate affected VPS" [ref=e230]:
                  - img [ref=e231]
                  - text: Recalculate affected VPS
                - button "Post update" [ref=e234]:
                  - img [ref=e235]
                  - text: Post update
            - navigation "Security advisory sections" [ref=e236]:
              - button "Overview" [ref=e237]
              - button "Nodes" [ref=e238]
              - button "Affected users and VPS" [ref=e239]
              - button "Updates1" [ref=e240]
              - button "Outages" [ref=e241]
            - generic [ref=e242]:
              - button "Post update" [ref=e244]:
                - img [ref=e245]
                - text: Post update
              - generic [ref=e246]:
                - generic [ref=e247]:
                  - generic [ref=e248]:
                    - generic [ref=e249]: Edited update
                    - generic [ref=e250]: 8/31/2026, 3:00:00 PM · security-admin
                  - generic [ref=e252]:
                    - button "Edit" [ref=e253]
                    - button "Delete" [ref=e254]
                - paragraph [ref=e256]: Edited English message.
  - dialog "Delete advisory update?" [ref=e259]:
    - generic [ref=e261]: Delete advisory update?
    - generic [ref=e263]:
      - paragraph [ref=e264]: This removes the update from the advisory history. Deleting a retraction update does not restore the parent advisory state.
      - generic [ref=e266]:
        - generic [ref=e267]: Error
        - generic [ref=e269]: Missing response namespace
    - alert [ref=e272]:
      - generic [ref=e273]:
        - generic [ref=e274]:
          - generic [ref=e275]: Error
          - generic [ref=e276]: Missing response namespace
        - button "Close" [ref=e277]:
          - generic [ref=e278]: ×
    - generic [ref=e280]:
      - button "Cancel" [ref=e281]
      - button "Delete" [ref=e282]
```

# Test source

```ts
  17  |   name: 'Linux kernel advisory',
  18  |   published_at: '2026-08-31T12:00:00.000Z',
  19  |   created_at: '2026-08-31T10:00:00.000Z',
  20  |   en_summary: 'Kernel vulnerability',
  21  |   en_description: 'Affects supported compute nodes.',
  22  |   en_response: 'Apply the fixed kernel.',
  23  |   cs_summary: 'Zranitelnost kernelu',
  24  |   cs_description: 'Týká se podporovaných nodů.',
  25  |   cs_response: 'Nasaď opravený kernel.',
  26  | };
  27  | 
  28  | function initialUpdate() {
  29  |   return {
  30  |     id: 701,
  31  |     security_advisory_id: 77,
  32  |     created_at: '2026-08-31T13:00:00.000Z',
  33  |     reporter_name: 'security-admin',
  34  |     en_summary: 'Original update',
  35  |     en_message: 'Original English message.',
  36  |     cs_summary: 'Původní aktualizace',
  37  |     cs_message: 'Původní česká zpráva.',
  38  |   };
  39  | }
  40  | 
  41  | async function installAdvisoryDetailMock(
  42  |   page: Page,
  43  |   handlers: Record<string, (ctx: any) => unknown>,
  44  | ) {
  45  |   await setUiSettingsLocalStorage(page, { language: 'en' });
  46  |   await bootstrapVpsAdminWindow(page, { sessionToken: 'SECURITY_UPDATE_MUTATIONS' });
  47  |   await installHaveApiMock(page, {
  48  |     user: { id: 1, login: 'security-admin', level: 100 },
  49  |     handlers: {
  50  |       'GET languages': () => ({ languages }),
  51  |       'GET security_advisories/77': () => ({ security_advisory: advisory }),
  52  |       'GET security_advisory_cves': () => ({ security_advisory_cves: [] }),
  53  |       'GET nodes': () => ({ nodes: [] }),
  54  |       'GET security_advisories/77/node_statuses': () => ({ node_statuses: [] }),
  55  |       'GET outage_security_advisories': () => ({ outage_security_advisories: [] }),
  56  |       ...handlers,
  57  |     },
  58  |   });
  59  | }
  60  | 
  61  | test('@pr-smoke edits and deletes an advisory update with confirmation and refreshed readback', async ({ page }) => {
  62  |   let updates = [initialUpdate()];
  63  |   const putPayloads: unknown[] = [];
  64  |   const deletePayloads: unknown[] = [];
  65  |   let deleteCalls = 0;
  66  | 
  67  |   await installAdvisoryDetailMock(page, {
  68  |     'GET security_advisory_updates': () => ({ security_advisory_updates: updates }),
  69  |     'PUT security_advisory_updates/701': ({ reqJson }) => {
  70  |       putPayloads.push(reqJson);
  71  |       updates = updates.map((update) => ({
  72  |         ...update,
  73  |         ...((reqJson as any)?.security_advisory_update ?? {}),
  74  |       }));
  75  |       return { security_advisory_update: updates[0] };
  76  |     },
  77  |     'DELETE security_advisory_updates/701': ({ reqJson }) => {
  78  |       deleteCalls += 1;
  79  |       deletePayloads.push(reqJson);
  80  |       updates = [];
  81  |       return null;
  82  |     },
  83  |   });
  84  | 
  85  |   await page.goto('/admin/security-advisories/77?tab=updates');
  86  |   const updateCard = page.getByTestId('admin.security_advisory.update.701');
  87  |   await expect(updateCard).toContainText('Original update');
  88  | 
  89  |   await page.getByTestId('admin.security_advisory.update.701.edit').click();
  90  |   await expect(page.getByTestId('admin.security_advisories.update.editor')).toBeVisible();
  91  |   await page.getByTestId('admin.security_advisories.update.editor.en.summary').fill('Edited update');
  92  |   await page.getByTestId('admin.security_advisories.update.editor.en.message').fill('Edited English message.');
  93  |   await page.getByTestId('admin.security_advisories.update.editor.language.cs').click();
  94  |   await page.getByTestId('admin.security_advisories.update.editor.cs.summary').fill('Upravená aktualizace');
  95  |   await page.getByTestId('admin.security_advisories.update.editor.cs.message').fill('Upravená česká zpráva.');
  96  |   await page.getByTestId('admin.security_advisories.update.editor.save').click();
  97  | 
  98  |   await expect.poll(() => putPayloads).toEqual([{
  99  |     security_advisory_update: {
  100 |       en_summary: 'Edited update',
  101 |       en_message: 'Edited English message.',
  102 |       cs_summary: 'Upravená aktualizace',
  103 |       cs_message: 'Upravená česká zpráva.',
  104 |     },
  105 |   }]);
  106 |   await expect(page.getByTestId('admin.security_advisories.update.editor')).toHaveCount(0);
  107 |   await expect(updateCard).toContainText('Edited update');
  108 |   await expect(updateCard).toContainText('Edited English message.');
  109 | 
  110 |   await page.getByTestId('admin.security_advisory.update.701.delete').click();
  111 |   await expect(page.getByTestId('admin.security_advisory.update.delete_confirm')).toBeVisible();
  112 |   expect(deleteCalls).toBe(0);
  113 |   expect(deletePayloads).toEqual([]);
  114 | 
  115 |   await page.getByTestId('admin.security_advisory.update.delete_confirm.confirm').click();
  116 |   await expect.poll(() => deleteCalls).toBe(1);
> 117 |   expect(deletePayloads).toEqual([{}]);
      |                          ^ Error: expect(received).toEqual(expected) // deep equality
  118 |   await expect(page.getByTestId('admin.security_advisory.update.delete_confirm')).toHaveCount(0);
  119 |   await expect(updateCard).toHaveCount(0);
  120 | });
  121 | 
  122 | test('@pr-smoke @pr-smoke-mobile advisory update PUT and DELETE 403 errors preserve the editor, confirmation and data', async ({ page }) => {
  123 |   const update = initialUpdate();
  124 |   let updates = [update];
  125 |   let putCalls = 0;
  126 |   let deleteCalls = 0;
  127 | 
  128 |   await installAdvisoryDetailMock(page, {
  129 |     'GET security_advisory_updates': () => ({ security_advisory_updates: updates }),
  130 |     'PUT security_advisory_updates/701': () => {
  131 |       putCalls += 1;
  132 |       return {
  133 |         status: 403,
  134 |         contentType: 'application/json',
  135 |         body: JSON.stringify({ status: false, message: 'update denied', response: null }),
  136 |       };
  137 |     },
  138 |     'DELETE security_advisory_updates/701': () => {
  139 |       deleteCalls += 1;
  140 |       if (deleteCalls > 1) {
  141 |         updates = [];
  142 |         return null;
  143 |       }
  144 |       return {
  145 |         status: 403,
  146 |         contentType: 'application/json',
  147 |         body: JSON.stringify({ status: false, message: 'delete denied', response: null }),
  148 |       };
  149 |     },
  150 |   });
  151 | 
  152 |   await page.goto('/admin/security-advisories/77?tab=updates');
  153 |   const updateCard = page.getByTestId('admin.security_advisory.update.701');
  154 |   await expect(updateCard).toContainText('Original update');
  155 | 
  156 |   await page.getByTestId('admin.security_advisory.update.701.edit').click();
  157 |   await page.getByTestId('admin.security_advisories.update.editor.en.summary').fill('Unsaved edit');
  158 |   await page.getByTestId('admin.security_advisories.update.editor.save').click();
  159 | 
  160 |   await expect.poll(() => putCalls).toBe(1);
  161 |   const editor = page.getByTestId('admin.security_advisories.update.editor');
  162 |   await expect(editor).toBeVisible();
  163 |   await expect(editor).toContainText('update denied');
  164 |   await expect(page.getByTestId('admin.security_advisories.update.editor.en.summary')).toHaveValue('Unsaved edit');
  165 |   await expect(updateCard).toContainText('Original update');
  166 |   await editor.getByRole('button', { name: 'Cancel', exact: true }).click();
  167 | 
  168 |   await page.getByTestId('admin.security_advisory.update.701.delete').click();
  169 |   const deleteDialog = page.getByTestId('admin.security_advisory.update.delete_confirm');
  170 |   await expect(deleteDialog).toBeVisible();
  171 |   expect(deleteCalls).toBe(0);
  172 |   await page.getByTestId('admin.security_advisory.update.delete_confirm.confirm').click();
  173 | 
  174 |   await expect.poll(() => deleteCalls).toBe(1);
  175 |   await expect(deleteDialog).toBeVisible();
  176 |   await expect(page.getByTestId('admin.security_advisory.update.delete_confirm.error')).toContainText('delete denied');
  177 |   await expect(updateCard).toContainText('Original update');
  178 |   await expect(deleteDialog.getByTestId('toast.modal_viewport')).toContainText('delete denied');
  179 | 
  180 |   await page.getByTestId('admin.security_advisory.update.delete_confirm.confirm').click();
  181 |   await expect.poll(() => deleteCalls).toBe(2);
  182 |   await expect(deleteDialog).toBeHidden();
  183 |   await expect(updateCard).toHaveCount(0);
  184 | });
  185 | 
```