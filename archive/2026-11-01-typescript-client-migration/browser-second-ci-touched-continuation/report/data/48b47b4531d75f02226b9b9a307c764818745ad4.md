# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/security_advisories_admin.spec.ts >> @smoke Security advisory admin management >> gates publishing, manages node assessments, retracts through an update and links an outage
- Location: e2e/specs/app/security_advisories_admin.spec.ts:125:3

# Error details

```
Test timeout of 90000ms exceeded.
```

```
Error: locator.selectOption: Test timeout of 90000ms exceeded.
Call log:
  - waiting for getByTestId('admin.security_advisories.nodes.editor.state')

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
          - link "View commit 129bf840dda8" [ref=e194] [cursor=pointer]:
            - /url: https://github.com/vpsfreecz/vpsadmin-webui/commit/129bf840dda84a71c006b875a8afb6301cf53a89
            - text: 129bf840dda8
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
              - generic [ref=e226]:
                - generic [ref=e227]: Draft
                - link "CVE-2026-12345" [ref=e228] [cursor=pointer]:
                  - /url: https://www.cve.org/CVERecord?id=CVE-2026-12345
                  - generic [ref=e229]: CVE-2026-12345
            - generic [ref=e230]:
              - link "Back to list" [ref=e231] [cursor=pointer]:
                - /url: /admin/security-advisories
              - button "Edit" [ref=e232]:
                - img [ref=e233]
                - text: Edit
              - button "Recalculate affected VPS" [ref=e235]:
                - img [ref=e236]
                - text: Recalculate affected VPS
              - button "Publish" [disabled] [ref=e239]:
                - img [ref=e240]
                - text: Publish
          - navigation "Security advisory sections" [ref=e243]:
            - button "Overview" [ref=e244]
            - button "Nodes" [ref=e245]
            - button "Affected users and VPS" [ref=e246]
            - button "Updates" [ref=e247]
            - button "Outages" [ref=e248]
          - generic [ref=e249]:
            - generic [ref=e250]:
              - generic [ref=e251]:
                - generic [ref=e252]: Node status
                - generic [ref=e253]: Record whether each active compute or storage node is affected and when it was mitigated.
              - button "Set all nodes" [ref=e255]:
                - img [ref=e256]
                - text: Set all nodes
            - table [ref=e262]:
              - rowgroup [ref=e263]:
                - row "Node Type State Vulnerable until Mitigated since Note Actions" [ref=e264]:
                  - columnheader "Node" [ref=e265]
                  - columnheader "Type" [ref=e266]
                  - columnheader "State" [ref=e267]
                  - columnheader "Vulnerable until" [ref=e268]
                  - columnheader "Mitigated since" [ref=e269]
                  - columnheader "Note" [ref=e270]
                  - columnheader "Actions" [ref=e271]
              - rowgroup [ref=e272]:
                - 'row "node10.prg #10 Compute node Unknown — — — Edit Remove status" [ref=e273]':
                  - 'cell "node10.prg #10" [ref=e274]':
                    - generic [ref=e275]:
                      - generic [ref=e276]: node10.prg
                      - generic [ref=e277]: "#10"
                  - cell "Compute node" [ref=e278]
                  - cell "Unknown" [ref=e279]:
                    - generic [ref=e281]: Unknown
                  - cell "—" [ref=e282]
                  - cell "—" [ref=e283]
                  - cell "—" [ref=e284]
                  - cell "Edit Remove status" [ref=e285]:
                    - generic [ref=e286]:
                      - button "Edit" [active] [ref=e287]:
                        - img [ref=e288]
                        - text: Edit
                      - button "Remove status" [ref=e291]:
                        - img [ref=e292]
                        - text: Remove status
                - 'row "storage20.prg #20 Storage node Not affected — — — Edit Remove status" [ref=e295]':
                  - 'cell "storage20.prg #20" [ref=e296]':
                    - generic [ref=e297]:
                      - generic [ref=e298]: storage20.prg
                      - generic [ref=e299]: "#20"
                  - cell "Storage node" [ref=e300]
                  - cell "Not affected" [ref=e301]:
                    - generic [ref=e303]: Not affected
                  - cell "—" [ref=e304]
                  - cell "—" [ref=e305]
                  - cell "—" [ref=e306]
                  - cell "Edit Remove status" [ref=e307]:
                    - generic [ref=e308]:
                      - button "Edit" [ref=e309]:
                        - img [ref=e310]
                        - text: Edit
                      - button "Remove status" [ref=e313]:
                        - img [ref=e314]
                        - text: Remove status
```

# Test source

```ts
  162 |         note: null,
  163 |       },
  164 |       {
  165 |         id: 502,
  166 |         security_advisory_id: 77,
  167 |         node_id: 20,
  168 |         node: nodes[1],
  169 |         state: 'not_affected',
  170 |         vulnerable_until: null,
  171 |         mitigated_since: null,
  172 |         note: 'Storage is not affected',
  173 |       },
  174 |     ];
  175 |     let updates: Array<Record<string, unknown>> = [];
  176 |     let outageLinks: Array<Record<string, unknown>> = [];
  177 | 
  178 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  179 |     await installHaveApiMock(page, {
  180 |       user: { id: 1, login: 'security-admin', level: 90 },
  181 |       handlers: {
  182 |         'GET languages': () => ({ languages }),
  183 |         'GET security_advisories/77': () => ({ security_advisory: advisory }),
  184 |         'GET security_advisory_cves': () => ({ security_advisory_cves: cves }),
  185 |         'GET nodes': () => ({ nodes }),
  186 |         'GET security_advisories/77/node_statuses': () => ({ node_statuses: statuses }),
  187 |         'GET security_advisory_updates': () => ({ security_advisory_updates: updates }),
  188 |         'GET outage_security_advisories': () => ({ outage_security_advisories: outageLinks }),
  189 | 
  190 |         'PUT security_advisories/77/node_statuses/501': ({ reqJson }) => {
  191 |           const attrs = (reqJson as any)?.node_status ?? {};
  192 |           statuses = statuses.map((status) =>
  193 |             status.id === 501 ? { ...status, ...attrs, node_id: 10, node: nodes[0] } : status,
  194 |           );
  195 |           return { node_status: statuses.find((status) => status.id === 501) };
  196 |         },
  197 |         'PUT security_advisories/77/node_statuses/502': ({ reqJson }) => {
  198 |           const attrs = (reqJson as any)?.node_status ?? {};
  199 |           statuses = statuses.map((status) =>
  200 |             status.id === 502 ? { ...status, ...attrs, node_id: 20, node: nodes[1] } : status,
  201 |           );
  202 |           return { node_status: statuses.find((status) => status.id === 502) };
  203 |         },
  204 |         'POST security_advisories/77/publish': ({ reqJson }) => {
  205 |           const attrs = (reqJson as any)?.security_advisory ?? {};
  206 |           advisory = { ...advisory, ...attrs, state: 'published' };
  207 |           return { security_advisory: advisory };
  208 |         },
  209 |         'POST security_advisory_updates': ({ reqJson }) => {
  210 |           const attrs = (reqJson as any)?.security_advisory_update ?? {};
  211 |           const update = {
  212 |             id: 701,
  213 |             created_at: '2026-07-27T13:00:00.000Z',
  214 |             reporter_name: 'security-admin',
  215 |             ...attrs,
  216 |           };
  217 |           updates = [update, ...updates];
  218 |           if (attrs.state === 'retracted') advisory = { ...advisory, state: 'retracted' };
  219 |           return { security_advisory_update: update };
  220 |         },
  221 |         'POST outage_security_advisories': ({ reqJson }) => {
  222 |           const attrs = (reqJson as any)?.outage_security_advisory ?? {};
  223 |           const link = {
  224 |             id: 801,
  225 |             security_advisory_id: 77,
  226 |             outage_id: attrs.outage,
  227 |             outage: {
  228 |               id: attrs.outage,
  229 |               begins_at: '2026-07-27T14:00:00.000Z',
  230 |               en_summary: 'Emergency kernel maintenance',
  231 |               cs_summary: 'Nouzová údržba kernelu',
  232 |             },
  233 |           };
  234 |           outageLinks = [link];
  235 |           return { outage_security_advisory: link };
  236 |         },
  237 |       },
  238 |     });
  239 | 
  240 |     page.on('request', (request) => {
  241 |       const url = new URL(request.url());
  242 |       if (!url.pathname.startsWith('/api/v7.0/')) return;
  243 |       if (!['POST', 'PUT', 'DELETE'].includes(request.method())) return;
  244 |       mutations.push({ method: request.method(), path: url.pathname, body: request.postDataJSON() });
  245 |     });
  246 | 
  247 |     await page.goto('/admin/security-advisories/77');
  248 |     await expect(page.getByTestId('admin.security_advisory.detail')).toBeVisible();
  249 |     await expect(page.getByTestId('admin.security_advisory.readiness')).toBeVisible();
  250 |     await expect(page.getByTestId('admin.security_advisory.publish')).toBeDisabled();
  251 |     await expect(page.getByTestId('admin.security_advisory.edit')).toBeVisible();
  252 |     await expect(page.getByTestId('admin.security_advisory.post_update')).toHaveCount(0);
  253 |     await page.getByTestId('admin.security_advisory.tab.updates').click();
  254 |     await expect(page.getByTestId('admin.security_advisory.updates.post_update')).toHaveCount(0);
  255 |     await expect(page.getByText('Publish this draft before posting follow-up updates.')).toBeVisible();
  256 | 
  257 |     // Resolve an individual assessment first, including the date validation
  258 |     // required for a mitigated node.
  259 |     await page.getByTestId('admin.security_advisory.tab.nodes').click();
  260 |     await expect(page.getByTestId('admin.security_advisories.nodes.row.10')).toBeVisible();
  261 |     await page.getByTestId('admin.security_advisories.nodes.row.10.edit').click();
> 262 |     await page.getByTestId('admin.security_advisories.nodes.editor.state').selectOption('mitigated');
      |                                                                            ^ Error: locator.selectOption: Test timeout of 90000ms exceeded.
  263 |     await page
  264 |       .getByTestId('admin.security_advisories.nodes.editor.vulnerable_until')
  265 |       .fill('2026-07-27T11:00');
  266 |     await page
  267 |       .getByTestId('admin.security_advisories.nodes.editor.mitigated_since')
  268 |       .fill('2026-07-27T12:00');
  269 |     await page.getByTestId('admin.security_advisories.nodes.editor.note').fill('Fixed kernel installed');
  270 |     await page.getByTestId('admin.security_advisories.nodes.editor.save').click();
  271 |     await expect(page.getByTestId('admin.security_advisories.nodes.editor')).toHaveCount(0);
  272 |     await expect
  273 |       .poll(() =>
  274 |         mutations.some(
  275 |           (mutation) =>
  276 |             mutation.method === 'PUT' &&
  277 |             mutation.path === '/api/v7.0/security_advisories/77/node_statuses/501' &&
  278 |             mutation.body?.node_status?.state === 'mitigated',
  279 |         ),
  280 |       )
  281 |       .toBeTruthy();
  282 | 
  283 |     // Bulk assessment applies the same explicit result to every active compute
  284 |     // and storage node, but skips the inactive node.
  285 |     await page.getByTestId('admin.security_advisories.nodes.bulk.open').click();
  286 |     await page.getByTestId('admin.security_advisories.nodes.bulk.state').selectOption('not_affected');
  287 |     await page.getByTestId('admin.security_advisories.nodes.bulk.apply').click();
  288 |     await expect(page.getByTestId('admin.security_advisories.nodes.bulk.confirm')).toBeVisible();
  289 |     await page.getByTestId('admin.security_advisories.nodes.bulk.confirm.confirm').click();
  290 |     await expect(page.getByTestId('admin.security_advisories.nodes.bulk')).toHaveCount(0);
  291 |     await expect.poll(() => statuses.map((status) => status.state)).toEqual(['not_affected', 'not_affected']);
  292 |     expect(mutations.some((mutation) => mutation.path.endsWith('/node_statuses/502'))).toBeTruthy();
  293 |     expect(mutations.some((mutation) => mutation.path.endsWith('/node_statuses/503'))).toBeFalsy();
  294 | 
  295 |     // Readiness now has a CVE and a resolved status for every relevant node.
  296 |     await page.getByTestId('admin.security_advisory.tab.overview').click();
  297 |     await expect(page.getByTestId('admin.security_advisory.publish')).toBeEnabled();
  298 |     await page.getByTestId('admin.security_advisory.publish').click();
  299 |     await expect(page.getByTestId('admin.security_advisory.publish_dialog')).toBeVisible();
  300 |     await page.getByTestId('admin.security_advisory.publish_dialog.send_mail').check();
  301 |     await page.getByTestId('admin.security_advisory.publish_dialog.confirm').click();
  302 |     await expect(page.getByTestId('admin.security_advisory.publish_dialog')).toHaveCount(0);
  303 |     await expect(page.getByTestId('admin.security_advisory.post_update')).toBeVisible();
  304 |     await expect(page.getByTestId('admin.security_advisory.edit')).toHaveCount(0);
  305 |     expect(
  306 |       mutations.find(
  307 |         (mutation) =>
  308 |           mutation.method === 'POST' &&
  309 |           mutation.path === '/api/v7.0/security_advisories/77/publish',
  310 |       )?.body,
  311 |     ).toEqual({
  312 |       security_advisory: expect.objectContaining({ send_mail: true, published_at: expect.any(String) }),
  313 |     });
  314 | 
  315 |     // Retraction is represented by a localized advisory update and requires a
  316 |     // second explicit confirmation before the API mutation is sent.
  317 |     await page.getByTestId('admin.security_advisory.post_update').click();
  318 |     await page.getByTestId('admin.security_advisories.update.editor.state').selectOption('retracted');
  319 |     await page
  320 |       .getByTestId('admin.security_advisories.update.editor.en.summary')
  321 |       .fill('Advisory retracted');
  322 |     await page
  323 |       .getByTestId('admin.security_advisories.update.editor.en.message')
  324 |       .fill('The report was based on incorrect package metadata.');
  325 |     await page.getByTestId('admin.security_advisories.update.editor.language.cs').click();
  326 |     await page
  327 |       .getByTestId('admin.security_advisories.update.editor.cs.summary')
  328 |       .fill('Upozornění staženo');
  329 |     await page
  330 |       .getByTestId('admin.security_advisories.update.editor.cs.message')
  331 |       .fill('Hlašení vycházelo z chybných metadat balíčku.');
  332 |     await page.getByTestId('admin.security_advisories.update.editor.save').click();
  333 |     await expect(page.getByTestId('admin.security_advisory.update.confirm')).toBeVisible();
  334 |     await page.getByTestId('admin.security_advisory.update.confirm.confirm').click();
  335 |     await expect(page.getByTestId('admin.security_advisories.update.editor')).toHaveCount(0);
  336 |     await expect.poll(() => advisory.state).toBe('retracted');
  337 |     await expect(page.getByTestId('admin.security_advisory.post_update')).toHaveCount(0);
  338 |     await page.getByTestId('admin.security_advisory.tab.updates').click();
  339 |     await expect(page.getByTestId('admin.security_advisory.updates.post_update')).toHaveCount(0);
  340 |     await expect(page.getByText(/This advisory is retracted/)).toBeVisible();
  341 |     const postedUpdate = page.getByTestId('admin.security_advisory.update.701');
  342 |     await expect(postedUpdate).toBeVisible();
  343 |     await expect(page.getByTestId('admin.security_advisory.update.701.edit')).toBeVisible();
  344 |     await expect(page.getByTestId('admin.security_advisory.update.701.delete')).toBeVisible();
  345 |     expect(
  346 |       mutations.find(
  347 |         (mutation) =>
  348 |           mutation.method === 'POST' &&
  349 |           mutation.path === '/api/v7.0/security_advisory_updates',
  350 |       )?.body,
  351 |     ).toEqual({
  352 |       security_advisory_update: expect.objectContaining({
  353 |         security_advisory: 77,
  354 |         state: 'retracted',
  355 |         send_mail: false,
  356 |         en_summary: 'Advisory retracted',
  357 |         cs_summary: 'Upozornění staženo',
  358 |       }),
  359 |     });
  360 | 
  361 |     // Link a related outage from the dedicated tab and verify the nested API
  362 |     // payload as well as the refreshed row.
```