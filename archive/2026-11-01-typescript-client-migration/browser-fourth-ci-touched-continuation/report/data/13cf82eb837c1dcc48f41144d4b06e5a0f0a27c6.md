# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/vps_lifecycle_tab_actions.spec.ts >> @pr-smoke VPS lifecycle tab >> posts legacy rescue boot payload
- Location: e2e/specs/app/vps_lifecycle_tab_actions.spec.ts:239:3

# Error details

```
Test timeout of 90000ms exceeded.
```

```
Error: page.waitForRequest: Test timeout of 90000ms exceeded.
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
            - link "View commit be42b595a2a1" [ref=e194] [cursor=pointer]:
              - /url: https://github.com/vpsfreecz/vpsadmin-webui/commit/be42b595a2a1746c55842cbfc0a6786d015fead6
              - text: be42b595a2a1
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
              - generic [ref=e216]: admin
              - generic [ref=e217]: admin
        - main [ref=e218]:
          - generic [ref=e221]:
            - generic [ref=e223]:
              - generic [ref=e224]:
                - generic [ref=e225]:
                  - generic [ref=e226]:
                    - link "VPS" [ref=e227] [cursor=pointer]:
                      - /url: /admin/vps
                    - text: ·
                    - generic [ref=e228]: "#123"
                  - heading "vps123.example" [level=1] [ref=e230]
                  - generic [ref=e231]:
                    - generic [ref=e232]: Stopped
                    - generic [ref=e233]: Active
                    - generic "The action was started. Please wait until it finishes." [ref=e234]: Working…
                - generic [ref=e236]:
                  - button "Start" [disabled] [ref=e237]
                  - link "Snapshot" [ref=e238] [cursor=pointer]:
                    - /url: /admin/datasets/901/snapshots?action=create
                    - img [ref=e239]
                    - text: Snapshot
                  - combobox "VPS actions" [ref=e242]:
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
              - generic [ref=e243]:
                - generic [ref=e245]:
                  - generic [ref=e246]:
                    - text: Owner
                    - 'link "owner #7" [ref=e247] [cursor=pointer]':
                      - /url: /admin/users/7
                      - text: owner
                      - generic [ref=e248]: "#7"
                  - generic [ref=e249]: Distribution Debian latest
                  - generic [ref=e250]: Node node1.example
                  - generic [ref=e251]: Location Praha-2
                - generic [ref=e254]:
                  - generic [ref=e255]: "SSH:"
                  - generic [ref=e256]: No address available
              - generic [ref=e258]:
                - generic [ref=e259]:
                  - generic [ref=e260]:
                    - term [ref=e261]:
                      - img [ref=e262]
                      - text: Uptime
                    - definition [ref=e265]: —
                  - generic [ref=e266]:
                    - term [ref=e267]:
                      - img [ref=e268]
                      - text: Load average (1 / 5 / 15 min)
                    - definition [ref=e270]: —
                  - generic [ref=e271]:
                    - term [ref=e272]:
                      - img [ref=e273]
                      - text: Processes
                    - definition [ref=e277]: —
                  - generic [ref=e278]:
                    - term [ref=e279]:
                      - img [ref=e280]
                      - text: CPU usage
                    - definition [ref=e283]: —
                - generic [ref=e284]:
                  - link "Overview" [ref=e285] [cursor=pointer]:
                    - /url: /admin/vps/123
                  - link "Access" [ref=e286] [cursor=pointer]:
                    - /url: /admin/vps/123/access
                  - link "Network" [ref=e287] [cursor=pointer]:
                    - /url: /admin/vps/123/network
                  - link "Storage" [ref=e288] [cursor=pointer]:
                    - /url: /admin/vps/123/storage
                  - link "Maintenance" [ref=e289] [cursor=pointer]:
                    - /url: /admin/vps/123/maintenance
                  - link "History" [ref=e290] [cursor=pointer]:
                    - /url: /admin/vps/123/history
                  - link "Console" [ref=e291] [cursor=pointer]:
                    - /url: /admin/vps/123/console
            - generic [ref=e292]:
              - generic [ref=e293]: The previous operation has an uncertain outcome
              - generic [ref=e295]:
                - generic [ref=e296]: The server may have accepted the operation. Check Tasks and the affected object before acknowledging the result; repeating it blindly could duplicate or repeat a destructive action.
                - generic [ref=e297]:
                  - button "Open tasks" [ref=e298]
                  - button "I verified the outcome — unlock" [disabled] [ref=e299]
            - generic [ref=e300]:
              - generic [ref=e301]:
                - generic [ref=e302]:
                  - generic [ref=e303]:
                    - generic [ref=e304]: Boot from template
                    - generic [ref=e305]: Starts the VPS in rescue mode from a clean OS template.
                  - link "Back to actions" [ref=e307] [cursor=pointer]:
                    - /url: /admin/vps/123/lifecycle
                - generic [ref=e309]: "Current VPS #123, node #1, owner #7, expiration 8/1/2026, 2:00:00 AM."
              - generic [ref=e311]:
                - generic [ref=e312]:
                  - generic [ref=e313]: Temporary rescue system
                  - generic [ref=e315]: The VPS keeps the same configuration, but starts from a clean template. Changes made in the rescue system are discarded after the next start/restart.
                - generic [ref=e316]:
                  - generic [ref=e317]: Working…
                  - generic [ref=e319]:
                    - paragraph [ref=e320]: The action was started. Please wait until it finishes.
                    - button "Open tasks" [ref=e321]
                - generic [ref=e322]:
                  - generic [ref=e323]:
                    - generic [ref=e324]: OS template
                    - combobox "OS template Equivalent to the legacy Boot VPS from template form." [ref=e326]:
                      - option "Choose OS template…"
                      - option "Debian latest"
                      - option "AlmaLinux 9" [selected]
                    - generic [ref=e327]: Equivalent to the legacy Boot VPS from template form.
                  - generic [ref=e328]:
                    - generic [ref=e329]: Root dataset mountpoint
                    - textbox "Root dataset mountpoint When mounting is enabled, the original root filesystem is available at this path." [ref=e331]: /mnt/rescue-root
                    - generic [ref=e332]: When mounting is enabled, the original root filesystem is available at this path.
                - generic [ref=e333] [cursor=pointer]:
                  - checkbox "Mount original root dataset Disable when the rescue system should boot without mounting the original root dataset." [checked] [ref=e334]
                  - generic [ref=e335]:
                    - generic [ref=e336]: Mount original root dataset
                    - generic [ref=e337]: Disable when the rescue system should boot without mounting the original root dataset.
                - generic [ref=e338]:
                  - generic [ref=e339]:
                    - generic [ref=e340]: Target
                    - generic [ref=e341]: vps123.example (#123)
                  - generic [ref=e342]:
                    - generic [ref=e343]: Rescue template
                    - generic [ref=e344]: AlmaLinux 9
                  - generic [ref=e345]:
                    - generic [ref=e346]: Original root dataset
                    - generic [ref=e347]: The original root dataset will be mounted at /mnt/rescue-root.
                - generic [ref=e348]:
                  - generic [ref=e349]: Confirm the change in the next step
                  - generic [ref=e351]: Review the target VPS and values above. Then confirm the action in the normal dialog.
                - generic [ref=e352]:
                  - generic [ref=e353]: Boot from template failed
                  - generic [ref=e355]: Missing response namespace
                - button "Boot rescue system" [disabled] [ref=e357]
  - dialog "Boot rescue system" [ref=e360]:
    - generic [ref=e362]: Boot rescue system
    - generic [ref=e364]:
      - paragraph [ref=e365]: The VPS keeps the same configuration, but starts from a clean template. Changes made in the rescue system are discarded after the next start/restart.
      - generic [ref=e369]: Missing response namespace
    - generic [ref=e371]:
      - button "Cancel" [ref=e372]
      - button "Boot rescue system" [disabled] [ref=e373]
```

# Test source

```ts
  152 |     await expect(page.getByTestId('vps.config.admin_override')).not.toBeChecked();
  153 |   });
  154 | 
  155 |   test('does not expose resource override to a member', async ({ page }) => {
  156 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  157 |     await installLifecycleMock(page, { user: { id: 7, login: 'owner', level: 1 } });
  158 |     await page.goto('/app/vps/123/config');
  159 |     await page.getByRole('spinbutton', { name: /^Memory/ }).fill('4096');
  160 |     await expect(page.getByTestId('vps.config.admin_override')).toHaveCount(0);
  161 |     await page.getByTestId('vps.config.header.save').click();
  162 |     const dialog = page.getByTestId('vps.config.confirm');
  163 |     await expect(dialog).toBeVisible();
  164 |     await expect(dialog.getByTestId('vps.config.confirm.admin_override')).toHaveCount(0);
  165 |     const request = page.waitForRequest(r => r.method() === 'PUT' && r.url().includes('/vpses/123'));
  166 |     await dialog.getByTestId('vps.config.confirm.confirm').click();
  167 |     expect((await request).postDataJSON()).toEqual({ vps: { memory: 4096 } });
  168 |   });
  169 | 
  170 |   test('@pr-smoke-mobile keeps rejected VPS configuration saves inside the review dialog and allows retry', async ({ page }) => {
  171 |     let updateCalls = 0;
  172 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  173 |     await installLifecycleMock(page, {
  174 |       updateVps: () => {
  175 |         updateCalls += 1;
  176 |         if (updateCalls === 1) {
  177 |           return {
  178 |             status: 409,
  179 |             contentType: 'application/json',
  180 |             body: JSON.stringify({
  181 |               status: false,
  182 |               message: 'VPS configuration changed on the server. Review and retry.',
  183 |               response: null,
  184 |             }),
  185 |           };
  186 |         }
  187 |         return { vps, _meta: { action_state_id: 506 } };
  188 |       },
  189 |     });
  190 | 
  191 |     await page.goto('/admin/vps/123/config');
  192 |     await page.getByRole('textbox', { name: /^Hostname / }).fill('retry-config.example');
  193 |     await page.getByTestId('vps.config.header.save').click();
  194 | 
  195 |     const dialog = page.getByTestId('vps.config.confirm');
  196 |     await expect(dialog).toBeVisible();
  197 |     await dialog.getByTestId('vps.config.confirm.confirm').click();
  198 |     await expect.poll(() => updateCalls).toBe(1);
  199 |     await expect(dialog.getByTestId('vps.config.confirm.error')).toContainText(
  200 |       'VPS configuration changed on the server. Review and retry.',
  201 |     );
  202 |     await expect(dialog).toBeVisible();
  203 | 
  204 |     await dialog.getByTestId('vps.config.confirm.cancel').click();
  205 |     await expect(dialog).toBeHidden();
  206 |     await page.getByTestId('vps.config.header.save').click();
  207 |     await expect(dialog).toBeVisible();
  208 |     await expect(dialog.getByTestId('vps.config.confirm.error')).toHaveCount(0);
  209 | 
  210 |     await dialog.getByTestId('vps.config.confirm.confirm').click();
  211 |     await expect.poll(() => updateCalls).toBe(2);
  212 |     await expect(dialog).toBeHidden();
  213 |   });
  214 | 
  215 |   test('resets configuration review and lifetime editor when the VPS route changes', async ({ page }) => {
  216 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  217 |     await installLifecycleMock(page);
  218 |     const navigate = (path: string) => page.evaluate((nextPath) => {
  219 |       window.history.pushState({}, '', nextPath);
  220 |       window.dispatchEvent(new PopStateEvent('popstate'));
  221 |     }, path);
  222 | 
  223 |     await page.goto('/admin/vps/123/config');
  224 |     await page.getByRole('textbox', { name: /^Hostname / }).fill('draft-for-vps-a.example');
  225 |     await page.getByTestId('vps.config.header.save').click();
  226 |     await expect(page.getByText('Review and apply VPS configuration changes?')).toBeVisible();
  227 |     await navigate('/admin/vps/321/config');
  228 |     await expect(page.getByText('Review and apply VPS configuration changes?')).toHaveCount(0);
  229 |     await expect(page.getByRole('textbox', { name: /^Hostname / })).toHaveValue('vps123-playground');
  230 | 
  231 |     await navigate('/admin/vps/123/lifecycle/lifetime');
  232 |     await page.getByTestId('lifetimes.admin.edit').click();
  233 |     await expect(page.getByTestId('lifetimes.admin.modal')).toBeVisible();
  234 |     await page.getByTestId('lifetimes.admin.reason').fill('draft reason for VPS A');
  235 |     await navigate('/admin/vps/321/lifecycle/lifetime');
  236 |     await expect(page.getByTestId('lifetimes.admin.modal')).toHaveCount(0);
  237 |   });
  238 | 
  239 |   test('posts legacy rescue boot payload', async ({ page }) => {
  240 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  241 |     await installLifecycleMock(page);
  242 | 
  243 |     await page.goto('/admin/vps/123/lifecycle/boot');
  244 | 
  245 |     await expect(page.getByTestId('vps.lifecycle.page')).toBeVisible();
  246 |     await expect(page.getByTestId('vps.lifecycle.boot')).toBeVisible();
  247 | 
  248 |     await page.getByTestId('vps.lifecycle.boot.os_template').selectOption('7');
  249 |     await page.getByTestId('vps.lifecycle.boot.mountpoint').fill('/mnt/rescue-root');
  250 |     await expect(page.getByTestId('vps.lifecycle.boot.confirm').locator('input')).toHaveCount(0);
  251 | 
> 252 |     const reqPromise = page.waitForRequest(
      |                             ^ Error: page.waitForRequest: Test timeout of 90000ms exceeded.
  253 |       (r) => r.method() === 'POST' && r.url().includes('/api/v7.0/vpses/123/boot')
  254 |     );
  255 | 
  256 |     await page.getByTestId('vps.lifecycle.boot.submit').click();
  257 |     await page.getByTestId('vps.lifecycle.boot.submit.confirm_dialog.confirm').click();
  258 | 
  259 |     const req = await reqPromise;
  260 |     expect(req.postDataJSON()).toEqual({
  261 |       vps: {
  262 |         os_template: 7,
  263 |         mount_root_dataset: '/mnt/rescue-root',
  264 |       },
  265 |     });
  266 |   });
  267 | 
  268 |   test('@workflow-matrix admin sees lifecycle controls reserved for admin mode', async ({ page }) => {
  269 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  270 |     await installLifecycleMock(page);
  271 | 
  272 |     await page.goto('/admin/vps/123/lifecycle');
  273 | 
  274 |     await expect(page.getByTestId('vps.lifecycle.action_index')).toBeVisible();
  275 |     await expect(page.getByTestId('vps.lifecycle.daily_actions')).toBeVisible();
  276 |     await expect(page.getByTestId('vps.lifecycle.admin_actions')).toBeVisible();
  277 |     await expect(page.getByTestId('vps.lifecycle.action_link.start')).toBeVisible();
  278 |     await expect(page.getByTestId('vps.lifecycle.action_link.stop')).toBeVisible();
  279 |     await expect(page.getByTestId('vps.lifecycle.action_link.restart')).toBeVisible();
  280 |     await expect(page.getByTestId('vps.lifecycle.action_link.clone')).toBeVisible();
  281 |     await expect(page.getByTestId('vps.lifecycle.action_link.swap')).toBeVisible();
  282 |     await expect(page.getByTestId('vps.lifecycle.action_link.delete')).toBeVisible();
  283 |     await expect(page.getByTestId('vps.lifecycle.action_link.lifetime')).toBeVisible();
  284 |     await expect(page.getByTestId('vps.lifecycle.action_link.replace')).toBeVisible();
  285 |     await expect(page.getByTestId('vps.lifecycle.action_link.migrate')).toBeVisible();
  286 |     await page.getByTestId('vps.lifecycle.action_link.migrate').click();
  287 |     await expect(page).toHaveURL(/\/admin\/vps\/123\/lifecycle\/migrate$/);
  288 |     await expect(page.getByTestId('vps.lifecycle.migrate')).toBeVisible();
  289 |   });
  290 | 
  291 |   test('@workflow-matrix focused lifecycle start action posts start endpoint', async ({ page }) => {
  292 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  293 |     await installLifecycleMock(page);
  294 | 
  295 |     await page.goto('/admin/vps/123/lifecycle/start');
  296 | 
  297 |     await expect(page.getByTestId('vps.lifecycle.start')).toBeVisible();
  298 |     await expect(page.getByTestId('vps.lifecycle.start.current_state')).toContainText('Stopped');
  299 |     await page.getByTestId('vps.lifecycle.start.confirm').check();
  300 | 
  301 |     const reqPromise = page.waitForRequest(
  302 |       (r) => r.method() === 'POST' && r.url().includes('/api/v7.0/vpses/123/start')
  303 |     );
  304 | 
  305 |     await page.getByTestId('vps.lifecycle.start.submit').click();
  306 | 
  307 |     const req = await reqPromise;
  308 |     expect(req.postDataJSON()).toEqual({});
  309 | 
  310 |     await expect(page.getByTestId('modal.action_progress')).toBeVisible();
  311 |     await page.getByTestId('modal.action_progress.open_tasks').click();
  312 |     await expect(page.getByTestId('tasks.drawer')).toHaveAttribute('aria-modal', 'false');
  313 |     await expect(
  314 |       page.getByTestId('tasks.row.503').getByRole('button', { name: 'Start', exact: true }),
  315 |     ).toBeVisible();
  316 |     await expect(page.getByTestId('vps.lifecycle.page')).toBeVisible();
  317 |   });
  318 | 
  319 |   test('@pr-smoke @pr-smoke-mobile refreshes delayed runtime state after a lifecycle power action', async ({ page }) => {
  320 |     let vpsReads = 0;
  321 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  322 |     await installHaveApiMock(page, {
  323 |       user: { id: 1, login: 'admin', level: 99 },
  324 |       handlers: {
  325 |         'GET vpses/123': () => {
  326 |           vpsReads += 1;
  327 |           return { vps: { ...vps, is_running: vpsReads >= 3 } };
  328 |         },
  329 |         'GET ip_addresses': () => ({ ip_addresses: [] }),
  330 |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  331 |         'POST vpses/123/start': () => ({ vps: {}, _meta: { action_state_id: 516 } }),
  332 |         'GET action_states/516': () => runningActionState(516, 'Start VPS'),
  333 |       },
  334 |     });
  335 | 
  336 |     await page.goto('/admin/vps/123/lifecycle/start');
  337 |     await expect(page.getByTestId('vps.header').getByText('Stopped', { exact: true })).toBeVisible();
  338 |     await page.getByTestId('vps.lifecycle.start.confirm').check();
  339 |     await page.getByTestId('vps.lifecycle.start.submit').click();
  340 | 
  341 |     await expect(page.getByTestId('vps.header').getByText('Running', { exact: true })).toBeVisible({ timeout: 15_000 });
  342 |     expect(vpsReads).toBeGreaterThanOrEqual(3);
  343 |   });
  344 | 
  345 |   test('@workflow-matrix focused lifecycle stop action can send force flag', async ({ page }) => {
  346 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  347 |     await installHaveApiMock(page, {
  348 |       user: { id: 1, login: 'admin', level: 99 },
  349 |       handlers: {
  350 |         'GET vpses/123': () => ({ vps: { ...vps, is_running: true } }),
  351 |         'GET ip_addresses': () => ({ ip_addresses: [] }),
  352 |         'GET transaction_chains': () => ({ transaction_chains: [] }),
```