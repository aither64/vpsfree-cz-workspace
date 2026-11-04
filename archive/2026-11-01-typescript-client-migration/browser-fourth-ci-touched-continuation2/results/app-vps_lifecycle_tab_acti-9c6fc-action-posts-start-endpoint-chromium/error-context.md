# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/vps_lifecycle_tab_actions.spec.ts >> @pr-smoke VPS lifecycle tab >> @workflow-matrix focused lifecycle start action posts start endpoint
- Location: e2e/specs/app/vps_lifecycle_tab_actions.spec.ts:293:3

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
          - link "View commit a27a076877f2" [ref=e194] [cursor=pointer]:
            - /url: https://github.com/vpsfreecz/vpsadmin-webui/commit/a27a076877f2227dbd5d23f82765740937a62a2e
            - text: a27a076877f2
    - status [ref=e195]:
      - generic [ref=e196]:
        - generic [ref=e197]:
          - generic [ref=e198]: Starting VPS…
          - paragraph [ref=e199]: You can keep this window open or continue in background.
        - button "Close" [ref=e200]:
          - img [ref=e201]
      - generic [ref=e204]:
        - generic [ref=e205]: "Start · vps123.example · #503"
        - generic [ref=e207]:
          - generic [ref=e208]: 1/2
          - generic [ref=e209]: 50%
        - generic [ref=e212]:
          - button "Open tasks" [ref=e213]
          - button "Continue in background" [ref=e214]
    - generic [ref=e216]:
      - banner [ref=e217]:
        - generic [ref=e218]:
          - search [ref=e219]:
            - img [ref=e220]
            - combobox "Quickly search objects" [ref=e223]
            - generic "Open quick search" [ref=e224]: Ctrl K · /
          - generic "All accessible objects are shown" [ref=e225]:
            - generic [ref=e226]: Admin view
          - button "Open tasks" [ref=e227]:
            - img [ref=e228]
            - generic [ref=e230]: Tasks
          - button "Open account menu" [ref=e232]:
            - img [ref=e233]
            - generic [ref=e236]: admin
            - generic [ref=e237]: admin
      - main [ref=e238]:
        - generic [ref=e241]:
          - generic [ref=e243]:
            - generic [ref=e244]:
              - generic [ref=e245]:
                - generic [ref=e246]:
                  - link "VPS" [ref=e247] [cursor=pointer]:
                    - /url: /admin/vps
                  - text: ·
                  - generic [ref=e248]: "#123"
                - heading "vps123.example" [level=1] [ref=e250]
                - generic [ref=e251]:
                  - generic [ref=e252]: Stopped
                  - generic [ref=e253]: Active
                  - generic "The action was started. Please wait until it finishes." [ref=e254]: Working…
              - generic [ref=e256]:
                - button "Start" [disabled] [ref=e257]
                - link "Snapshot" [ref=e258] [cursor=pointer]:
                  - /url: /admin/datasets/901/snapshots?action=create
                  - img [ref=e259]
                  - text: Snapshot
                - combobox "VPS actions" [ref=e262]:
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
                  - option "OOM reports"
                  - option "Incident reports"
                  - option "Outages"
                  - option "Configure OOM reports"
                  - option "Report incident"
                  - option "User data"
                  - option "User namespaces"
                  - option "Update VPS lifecycle"
                  - option "Replace VPS"
                  - option "Migrate VPS"
            - generic [ref=e263]:
              - generic [ref=e265]:
                - generic [ref=e266]:
                  - text: Owner
                  - 'link "owner #7" [ref=e267] [cursor=pointer]':
                    - /url: /admin/users/7
                    - text: owner
                    - generic [ref=e268]: "#7"
                - generic [ref=e269]: Distribution Debian latest
                - generic [ref=e270]: Node node1.example
                - generic [ref=e271]: Location Praha-2
              - generic [ref=e274]:
                - generic [ref=e275]: "SSH:"
                - generic [ref=e276]: No address available
            - generic [ref=e278]:
              - generic [ref=e279]:
                - generic [ref=e280]:
                  - term [ref=e281]:
                    - img [ref=e282]
                    - text: Uptime
                  - definition [ref=e285]: —
                - generic [ref=e286]:
                  - term [ref=e287]:
                    - img [ref=e288]
                    - text: Load average (1 / 5 / 15 min)
                  - definition [ref=e290]: —
                - generic [ref=e291]:
                  - term [ref=e292]:
                    - img [ref=e293]
                    - text: Processes
                  - definition [ref=e297]: —
                - generic [ref=e298]:
                  - term [ref=e299]:
                    - img [ref=e300]
                    - text: CPU usage
                  - definition [ref=e303]: —
              - generic [ref=e304]:
                - link "Overview" [ref=e305] [cursor=pointer]:
                  - /url: /admin/vps/123
                - link "Access" [ref=e306] [cursor=pointer]:
                  - /url: /admin/vps/123/access
                - link "Network" [ref=e307] [cursor=pointer]:
                  - /url: /admin/vps/123/network
                - link "Storage" [ref=e308] [cursor=pointer]:
                  - /url: /admin/vps/123/storage
                - link "Maintenance" [ref=e309] [cursor=pointer]:
                  - /url: /admin/vps/123/maintenance
                - link "History" [ref=e310] [cursor=pointer]:
                  - /url: /admin/vps/123/history
                - link "Console" [ref=e311] [cursor=pointer]:
                  - /url: /admin/vps/123/console
          - generic [ref=e312]:
            - generic [ref=e313]:
              - generic [ref=e314]:
                - generic [ref=e315]:
                  - generic [ref=e316]: Start
                  - generic [ref=e317]: Start a stopped VPS through the same task queue as the detail header control.
                - link "Back to actions" [ref=e319] [cursor=pointer]:
                  - /url: /admin/vps/123/lifecycle
              - generic [ref=e321]: "Current VPS #123, node #1, owner #7, expiration 8/1/2026, 2:00:00 AM."
            - generic [ref=e323]:
              - generic [ref=e324]:
                - generic [ref=e325]: Start check
                - generic [ref=e327]: Starting a VPS makes it boot on its assigned node. The action is blocked while another VPS task is active.
              - generic [ref=e328]:
                - generic [ref=e329]:
                  - generic [ref=e330]: Power state
                  - generic [ref=e331]: Stopped
                - generic [ref=e332]:
                  - generic [ref=e333]: Lifecycle state
                  - generic [ref=e334]: active
                - generic [ref=e335]:
                  - generic [ref=e336]: Task queue
                  - generic [ref=e337]: Busy
              - generic [ref=e338]:
                - generic [ref=e339]: Working…
                - generic [ref=e341]:
                  - paragraph [ref=e342]: The action was started. Please wait until it finishes.
                  - button "Open tasks" [ref=e343]
              - generic [ref=e345] [cursor=pointer]:
                - checkbox "I want to start this VPS." [ref=e346]
                - generic [ref=e348]: I want to start this VPS.
              - button "Start" [disabled] [ref=e350]
```

# Test source

```ts
  210 |     await expect(dialog.getByTestId('vps.config.confirm.error')).toHaveCount(0);
  211 | 
  212 |     await dialog.getByTestId('vps.config.confirm.confirm').click();
  213 |     await expect.poll(() => updateCalls).toBe(2);
  214 |     await expect(dialog).toBeHidden();
  215 |   });
  216 | 
  217 |   test('resets configuration review and lifetime editor when the VPS route changes', async ({ page }) => {
  218 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  219 |     await installLifecycleMock(page);
  220 |     const navigate = (path: string) => page.evaluate((nextPath) => {
  221 |       window.history.pushState({}, '', nextPath);
  222 |       window.dispatchEvent(new PopStateEvent('popstate'));
  223 |     }, path);
  224 | 
  225 |     await page.goto('/admin/vps/123/config');
  226 |     await page.getByRole('textbox', { name: /^Hostname / }).fill('draft-for-vps-a.example');
  227 |     await page.getByTestId('vps.config.header.save').click();
  228 |     await expect(page.getByText('Review and apply VPS configuration changes?')).toBeVisible();
  229 |     await navigate('/admin/vps/321/config');
  230 |     await expect(page.getByText('Review and apply VPS configuration changes?')).toHaveCount(0);
  231 |     await expect(page.getByRole('textbox', { name: /^Hostname / })).toHaveValue('vps123-playground');
  232 | 
  233 |     await navigate('/admin/vps/123/lifecycle/lifetime');
  234 |     await page.getByTestId('lifetimes.admin.edit').click();
  235 |     await expect(page.getByTestId('lifetimes.admin.modal')).toBeVisible();
  236 |     await page.getByTestId('lifetimes.admin.reason').fill('draft reason for VPS A');
  237 |     await navigate('/admin/vps/321/lifecycle/lifetime');
  238 |     await expect(page.getByTestId('lifetimes.admin.modal')).toHaveCount(0);
  239 |   });
  240 | 
  241 |   test('posts legacy rescue boot payload', async ({ page }) => {
  242 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  243 |     await installLifecycleMock(page);
  244 | 
  245 |     await page.goto('/admin/vps/123/lifecycle/boot');
  246 | 
  247 |     await expect(page.getByTestId('vps.lifecycle.page')).toBeVisible();
  248 |     await expect(page.getByTestId('vps.lifecycle.boot')).toBeVisible();
  249 | 
  250 |     await page.getByTestId('vps.lifecycle.boot.os_template').selectOption('7');
  251 |     await page.getByTestId('vps.lifecycle.boot.mountpoint').fill('/mnt/rescue-root');
  252 |     await expect(page.getByTestId('vps.lifecycle.boot.confirm').locator('input')).toHaveCount(0);
  253 | 
  254 |     const reqPromise = page.waitForRequest(
  255 |       (r) => r.method() === 'POST' && r.url().includes('/api/v7.0/vpses/123/boot')
  256 |     );
  257 | 
  258 |     await page.getByTestId('vps.lifecycle.boot.submit').click();
  259 |     await page.getByTestId('vps.lifecycle.boot.submit.confirm_dialog.confirm').click();
  260 | 
  261 |     const req = await reqPromise;
  262 |     expect(req.postDataJSON()).toEqual({
  263 |       vps: {
  264 |         os_template: 7,
  265 |         mount_root_dataset: '/mnt/rescue-root',
  266 |       },
  267 |     });
  268 |   });
  269 | 
  270 |   test('@workflow-matrix admin sees lifecycle controls reserved for admin mode', async ({ page }) => {
  271 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  272 |     await installLifecycleMock(page);
  273 | 
  274 |     await page.goto('/admin/vps/123/lifecycle');
  275 | 
  276 |     await expect(page.getByTestId('vps.lifecycle.action_index')).toBeVisible();
  277 |     await expect(page.getByTestId('vps.lifecycle.daily_actions')).toBeVisible();
  278 |     await expect(page.getByTestId('vps.lifecycle.admin_actions')).toBeVisible();
  279 |     await expect(page.getByTestId('vps.lifecycle.action_link.start')).toBeVisible();
  280 |     await expect(page.getByTestId('vps.lifecycle.action_link.stop')).toBeVisible();
  281 |     await expect(page.getByTestId('vps.lifecycle.action_link.restart')).toBeVisible();
  282 |     await expect(page.getByTestId('vps.lifecycle.action_link.clone')).toBeVisible();
  283 |     await expect(page.getByTestId('vps.lifecycle.action_link.swap')).toBeVisible();
  284 |     await expect(page.getByTestId('vps.lifecycle.action_link.delete')).toBeVisible();
  285 |     await expect(page.getByTestId('vps.lifecycle.action_link.lifetime')).toBeVisible();
  286 |     await expect(page.getByTestId('vps.lifecycle.action_link.replace')).toBeVisible();
  287 |     await expect(page.getByTestId('vps.lifecycle.action_link.migrate')).toBeVisible();
  288 |     await page.getByTestId('vps.lifecycle.action_link.migrate').click();
  289 |     await expect(page).toHaveURL(/\/admin\/vps\/123\/lifecycle\/migrate$/);
  290 |     await expect(page.getByTestId('vps.lifecycle.migrate')).toBeVisible();
  291 |   });
  292 | 
  293 |   test('@workflow-matrix focused lifecycle start action posts start endpoint', async ({ page }) => {
  294 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  295 |     await installLifecycleMock(page);
  296 | 
  297 |     await page.goto('/admin/vps/123/lifecycle/start');
  298 | 
  299 |     await expect(page.getByTestId('vps.lifecycle.start')).toBeVisible();
  300 |     await expect(page.getByTestId('vps.lifecycle.start.current_state')).toContainText('Stopped');
  301 |     await page.getByTestId('vps.lifecycle.start.confirm').check();
  302 | 
  303 |     const reqPromise = page.waitForRequest(
  304 |       (r) => r.method() === 'POST' && r.url().includes('/api/v7.0/vpses/123/start')
  305 |     );
  306 | 
  307 |     await page.getByTestId('vps.lifecycle.start.submit').click();
  308 | 
  309 |     const req = await reqPromise;
> 310 |     expect(req.postDataJSON()).toEqual({});
      |                                ^ Error: expect(received).toEqual(expected) // deep equality
  311 | 
  312 |     await expect(page.getByTestId('modal.action_progress')).toBeVisible();
  313 |     await page.getByTestId('modal.action_progress.open_tasks').click();
  314 |     await expect(page.getByTestId('tasks.drawer')).toHaveAttribute('aria-modal', 'false');
  315 |     await expect(
  316 |       page.getByTestId('tasks.row.503').getByRole('button', { name: 'Start', exact: true }),
  317 |     ).toBeVisible();
  318 |     await expect(page.getByTestId('vps.lifecycle.page')).toBeVisible();
  319 |   });
  320 | 
  321 |   test('@pr-smoke @pr-smoke-mobile refreshes delayed runtime state after a lifecycle power action', async ({ page }) => {
  322 |     let vpsReads = 0;
  323 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  324 |     await installHaveApiMock(page, {
  325 |       user: { id: 1, login: 'admin', level: 99 },
  326 |       handlers: {
  327 |         'GET vpses/123': () => {
  328 |           vpsReads += 1;
  329 |           return { vps: { ...vps, is_running: vpsReads >= 3 } };
  330 |         },
  331 |         'GET ip_addresses': () => ({ ip_addresses: [] }),
  332 |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  333 |         'POST vpses/123/start': () => ({ vps: {}, _meta: { action_state_id: 516 } }),
  334 |         'GET action_states/516': () => runningActionState(516, 'Start VPS'),
  335 |       },
  336 |     });
  337 | 
  338 |     await page.goto('/admin/vps/123/lifecycle/start');
  339 |     await expect(page.getByTestId('vps.header').getByText('Stopped', { exact: true })).toBeVisible();
  340 |     await page.getByTestId('vps.lifecycle.start.confirm').check();
  341 |     await page.getByTestId('vps.lifecycle.start.submit').click();
  342 | 
  343 |     await expect(page.getByTestId('vps.header').getByText('Running', { exact: true })).toBeVisible({ timeout: 15_000 });
  344 |     expect(vpsReads).toBeGreaterThanOrEqual(3);
  345 |   });
  346 | 
  347 |   test('@workflow-matrix focused lifecycle stop action can send force flag', async ({ page }) => {
  348 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  349 |     await installHaveApiMock(page, {
  350 |       user: { id: 1, login: 'admin', level: 99 },
  351 |       handlers: {
  352 |         'GET vpses/123': () => ({ vps: { ...vps, is_running: true } }),
  353 |         'GET ip_addresses': () => ({ ip_addresses: [] }),
  354 |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  355 |         'POST vpses/123/stop': () => ({ vps: {}, _meta: { action_state_id: 514 } }),
  356 |         'POST vpses/123/restart': () => ({ vps: {}, _meta: { action_state_id: 515 } }),
  357 |         'GET action_states/514': () => runningActionState(514, 'Stop VPS'),
  358 |       },
  359 |     });
  360 | 
  361 |     await page.goto('/admin/vps/123/lifecycle/stop');
  362 |     await expect(page.getByTestId('vps.lifecycle.stop')).toBeVisible();
  363 |     await page.getByTestId('vps.lifecycle.stop.force').check();
  364 |     await page.getByTestId('vps.lifecycle.stop.confirm').check();
  365 | 
  366 |     const stopReqPromise = page.waitForRequest(
  367 |       (r) => r.method() === 'POST' && r.url().includes('/api/v7.0/vpses/123/stop')
  368 |     );
  369 | 
  370 |     await page.getByTestId('vps.lifecycle.stop.submit').click();
  371 |     const stopReq = await stopReqPromise;
  372 |     expect(stopReq.postDataJSON()).toEqual({ vps: { force: true } });
  373 | 
  374 |     await expect(page.getByTestId('modal.action_progress')).toBeVisible();
  375 |     await page.getByTestId('modal.action_progress.open_tasks').click();
  376 |     await expect(page.getByTestId('tasks.drawer')).toHaveAttribute('aria-modal', 'false');
  377 |     await expect(
  378 |       page.getByTestId('tasks.row.514').getByRole('button', { name: 'Poweroff', exact: true }),
  379 |     ).toBeVisible();
  380 |     await expect(page.getByTestId('vps.lifecycle.page')).toBeVisible();
  381 |   });
  382 | 
  383 |   test('@workflow-matrix focused lifecycle restart action can send force flag', async ({ page }) => {
  384 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  385 |     await installHaveApiMock(page, {
  386 |       user: { id: 1, login: 'admin', level: 99 },
  387 |       handlers: {
  388 |         'GET vpses/123': () => ({ vps: { ...vps, is_running: true } }),
  389 |         'GET ip_addresses': () => ({ ip_addresses: [] }),
  390 |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  391 |         'POST vpses/123/restart': () => ({ vps: {}, _meta: { action_state_id: 515 } }),
  392 |         'GET action_states/515': () => runningActionState(515, 'Restart VPS'),
  393 |       },
  394 |     });
  395 | 
  396 |     await page.goto('/admin/vps/123/lifecycle/restart');
  397 |     await expect(page.getByTestId('vps.lifecycle.restart')).toBeVisible();
  398 |     await page.getByTestId('vps.lifecycle.restart.force').check();
  399 |     await page.getByTestId('vps.lifecycle.restart.confirm').check();
  400 | 
  401 |     const restartReqPromise = page.waitForRequest(
  402 |       (r) => r.method() === 'POST' && r.url().includes('/api/v7.0/vpses/123/restart')
  403 |     );
  404 | 
  405 |     await page.getByTestId('vps.lifecycle.restart.submit').click();
  406 |     const restartReq = await restartReqPromise;
  407 |     expect(restartReq.postDataJSON()).toEqual({ vps: { force: true } });
  408 | 
  409 |     await expect(page.getByTestId('modal.action_progress')).toBeVisible();
  410 |     await page.getByTestId('modal.action_progress.open_tasks').click();
```