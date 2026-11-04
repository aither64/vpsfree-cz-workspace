# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/vps_storage_tab_mounts.spec.ts >> @smoke VPS storage tab mounts >> creates a user subdataset from the VPS storage entrypoint
- Location: e2e/specs/app/vps_storage_tab_mounts.spec.ts:148:3

# Error details

```
Test timeout of 90000ms exceeded.
```

```
Error: locator.click: Test timeout of 90000ms exceeded.
Call log:
  - waiting for getByTestId('vps.storage.root_dataset.create_subdataset')

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
          - link "View commit 4b69fe0b87f5" [ref=e116] [cursor=pointer]:
            - /url: https://github.com/vpsfreecz/vpsadmin-webui/commit/4b69fe0b87f56402703550d17ba9f1a9ac4f083a
            - text: 4b69fe0b87f5
    - generic [ref=e118]:
      - banner [ref=e119]:
        - generic [ref=e120]:
          - search [ref=e121]:
            - img [ref=e122]
            - combobox "Quickly search objects" [ref=e125]
            - generic "Open quick search" [ref=e126]: Ctrl K · /
          - button "Open tasks" [ref=e127]:
            - img [ref=e128]
            - generic [ref=e130]: Tasks
          - button "Open account menu" [ref=e132]:
            - img [ref=e133]
            - generic [ref=e136]: user
            - generic [ref=e137]: user
      - main [ref=e138]:
        - generic [ref=e141]:
          - generic [ref=e143]:
            - generic [ref=e144]:
              - generic [ref=e145]:
                - generic [ref=e146]:
                  - link "VPS" [ref=e147] [cursor=pointer]:
                    - /url: /app/vps
                  - text: ·
                  - generic [ref=e148]: "#123"
                - heading "vps123.example" [level=1] [ref=e150]
                - generic [ref=e151]:
                  - generic [ref=e152]: Running
                  - generic [ref=e153]: Active
              - generic [ref=e155]:
                - link "Access" [ref=e156] [cursor=pointer]:
                  - /url: /app/vps/123/access
                - link "Snapshot" [ref=e157] [cursor=pointer]:
                  - /url: /app/datasets/10/snapshots?action=create
                  - img [ref=e158]
                  - text: Snapshot
                - button "Restart" [ref=e161]:
                  - img [ref=e162]
                  - text: Restart
                - button "Shutdown" [ref=e165]:
                  - img [ref=e166]
                  - text: Shutdown
                - combobox "VPS actions" [ref=e168]:
                  - option "More…" [selected]
                  - option "DNS servers"
                  - option "Root password"
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
            - generic [ref=e169]:
              - generic [ref=e171]:
                - generic [ref=e172]: Distribution debian
                - generic [ref=e173]: Node node1.example
                - generic [ref=e174]: Location —
              - generic [ref=e177]:
                - generic [ref=e178]: "SSH:"
                - generic [ref=e179]: No address available
            - generic [ref=e181]:
              - generic [ref=e182]:
                - generic [ref=e183]:
                  - term [ref=e184]:
                    - img [ref=e185]
                    - text: Uptime
                  - definition [ref=e188]: 3h 25m
                - generic [ref=e189]:
                  - term [ref=e190]:
                    - img [ref=e191]
                    - text: Load average (1 / 5 / 15 min)
                  - definition [ref=e193]: 0.12 / — / —
                - generic [ref=e194]:
                  - term [ref=e195]:
                    - img [ref=e196]
                    - text: Processes
                  - definition [ref=e200]: —
                - generic [ref=e201]:
                  - term [ref=e202]:
                    - img [ref=e203]
                    - text: CPU usage
                  - definition [ref=e206]: —
              - generic [ref=e207]:
                - link "Overview" [ref=e208] [cursor=pointer]:
                  - /url: /app/vps/123
                - link "Access" [ref=e209] [cursor=pointer]:
                  - /url: /app/vps/123/access
                - link "Network" [ref=e210] [cursor=pointer]:
                  - /url: /app/vps/123/network
                - link "Storage" [ref=e211] [cursor=pointer]:
                  - /url: /app/vps/123/storage
                - link "Maintenance" [ref=e212] [cursor=pointer]:
                  - /url: /app/vps/123/maintenance
                - link "History" [ref=e213] [cursor=pointer]:
                  - /url: /app/vps/123/history
                - link "Console" [ref=e214] [cursor=pointer]:
                  - /url: /app/vps/123/console
          - generic [ref=e215]:
            - generic [ref=e216]:
              - generic [ref=e217]:
                - generic [ref=e218]:
                  - generic [ref=e219]: Storage
                  - generic [ref=e220]: Root dataset, capacity and manual mounts for this VPS.
                - button "Add mount" [ref=e222]
              - generic [ref=e224]:
                - generic [ref=e227]:
                  - generic [ref=e229]:
                    - generic [ref=e231]: Capacity
                    - generic [ref=e232]: — used of Unlimited
                  - generic [ref=e234]: —
                - generic [ref=e237]:
                  - generic [ref=e239]:
                    - generic [ref=e241]: Manual mounts
                    - generic [ref=e242]: 0 enabled · 0 disabled
                  - generic [ref=e244]: "0"
                - generic [ref=e247]:
                  - generic [ref=e249]:
                    - generic [ref=e251]: Mount access
                    - generic [ref=e252]: No failed mount state reported.
                  - generic [ref=e254]: 0 RW · 0 RO
            - generic [ref=e255]:
              - generic [ref=e257]:
                - generic [ref=e258]: Root dataset
                - generic [ref=e259]: Capacity and dataset context for tank/data.
              - generic [ref=e260]:
                - generic [ref=e262]:
                  - generic [ref=e263]: Failed to load root dataset metadata.
                  - generic [ref=e265]: Missing response namespace
                - generic [ref=e266]:
                  - generic [ref=e267]:
                    - generic [ref=e268]: Used
                    - generic [ref=e269]: —
                  - generic [ref=e270]:
                    - generic [ref=e271]: Available
                    - generic [ref=e272]: —
                  - generic [ref=e273]:
                    - generic [ref=e274]: Space limit
                    - generic [ref=e275]: —
                  - generic [ref=e276]:
                    - generic [ref=e277]: Capacity used
                    - generic [ref=e278]: —
                - generic [ref=e279]:
                  - link "Open dataset" [ref=e280] [cursor=pointer]:
                    - /url: /app/datasets/10
                  - link "Snapshots" [ref=e281] [cursor=pointer]:
                    - /url: /app/datasets/10/snapshots
                  - link "Exports/downloads" [ref=e282] [cursor=pointer]:
                    - /url: /app/datasets/10/downloads
                - generic [ref=e283]: Subdatasets are created from the root dataset detail; if the button is not shown, this action is not available for this dataset.
                - group [ref=e284]:
                  - generic "Technical dataset details" [ref=e285] [cursor=pointer]
            - generic [ref=e286]:
              - generic [ref=e287]:
                - generic [ref=e288]:
                  - generic [ref=e289]: Mounts
                  - generic [ref=e290]: Datasets mounted into the VPS filesystem.
                - button "Refresh" [ref=e292]
              - generic [ref=e294]: No mounts configured.
```

# Test source

```ts
  79  |               current: 0,
  80  |               total: 1,
  81  |             },
  82  |           }),
  83  |         },
  84  |       });
  85  | 
  86  |       await page.goto('/admin/vps/123/storage?resize=ssd');
  87  |       await expect(page).toHaveURL(/\/admin\/vps\/123\/storage$/);
  88  |       const modal = page.getByTestId('vps.storage.resize.modal');
  89  |       await expect(modal).toBeVisible();
  90  |       await expect(modal).toContainText('No VPS restart');
  91  |       await expect(modal).toContainText('Current size: 20 GiB');
  92  |       await expect(modal.getByTestId('vps.storage.resize.submit')).toBeDisabled();
  93  | 
  94  |       await modal.getByTestId('vps.storage.resize.size').fill('4');
  95  |       await expect(modal).toContainText('cannot be smaller than the currently used space');
  96  |       await expect(modal.getByTestId('vps.storage.resize.submit')).toBeDisabled();
  97  | 
  98  |       await modal.getByTestId('vps.storage.resize.size').fill('32');
  99  |       await expect(modal.getByTestId('vps.storage.resize.admin_override')).not.toBeChecked();
  100 |       if (override) await modal.getByTestId('vps.storage.resize.admin_override').check();
  101 |       const requestPromise = page.waitForRequest(
  102 |         (request) => request.method() === 'PUT' && request.url().includes('/api/v7.0/datasets/10')
  103 |       );
  104 |       await modal.getByTestId('vps.storage.resize.submit').click();
  105 | 
  106 |       expect((await requestPromise).postDataJSON()).toEqual({ dataset: { refquota: 32 * 1024, ...(override ? { admin_override: true } : {}) } });
  107 |       expect(vpsUpdateCount).toBe(0);
  108 |       await expect(modal).toBeHidden();
  109 |       await expect(page.getByTestId('vps.storage.root_dataset.resize')).toBeVisible();
  110 | 
  111 |       await page.goto('/app/vps/123/config');
  112 |       await expect(page.getByTestId('vps.resources.disk')).toHaveCount(0);
  113 |       await page.goto('/app/vps/123/storage');
  114 |       await expect(page.getByTestId('vps.storage.root_dataset.resize')).toHaveCount(0);
  115 |     });
  116 | 
  117 |   }
  118 | 
  119 |   test('resets a mount deletion confirm when the VPS route changes', async ({ page }) => {
  120 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  121 |     const mounts = [{
  122 |       id: 1, mountpoint: '/mnt/old', mode: 'ro', enabled: true,
  123 |       on_start_fail: 'ignore', dataset: { id: 9, name: 'tank/old' },
  124 |     }];
  125 |     await installHaveApiMock(page, {
  126 |       user: { id: 1, login: 'user', level: 1 },
  127 |       handlers: {
  128 |         'GET vpses/123': () => ({ vps }),
  129 |         'GET vpses/456': () => ({ vps: { ...vps, id: 456, hostname: 'vps456.example', dataset: null } }),
  130 |         'GET ip_addresses': () => ({ ip_addresses: [] }),
  131 |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  132 |         'GET vpses/123/mounts': () => ({ mounts }),
  133 |         'GET vpses/456/mounts': () => ({ mounts: [] }),
  134 |       },
  135 |     });
  136 | 
  137 |     await page.goto('/app/vps/123/storage');
  138 |     await mountItemControl(page, 1, 'delete').click();
  139 |     await expect(page.getByTestId('vps.storage.mounts.delete_confirm')).toBeVisible();
  140 |     await page.evaluate(() => {
  141 |       window.history.pushState({}, '', '/app/vps/456/storage');
  142 |       window.dispatchEvent(new PopStateEvent('popstate'));
  143 |     });
  144 |     await expect(page.getByTestId('vps.storage.mounts.delete_confirm')).toHaveCount(0);
  145 |     await expect(page.getByTestId('vps.storage.page')).toBeVisible();
  146 |   });
  147 | 
  148 |   test('creates a user subdataset from the VPS storage entrypoint', async ({ page }) => {
  149 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  150 | 
  151 |     const childDataset = {
  152 |       ...dataset,
  153 |       id: 11,
  154 |       name: 'storage-child',
  155 |       full_name: 'tank/data/storage-child',
  156 |       parent: { id: 10 },
  157 |       used: 0,
  158 |       referenced: 0,
  159 |       snapshots_count: 0,
  160 |       mount_count: 0,
  161 |       export_count: 0,
  162 |     };
  163 | 
  164 |     await installHaveApiMock(page, {
  165 |       user: { id: 1, login: 'user', level: 1 },
  166 |       handlers: {
  167 |         'GET vpses/123': () => ({ vps }),
  168 |         'GET datasets/10': () => dataset,
  169 |         'GET datasets/11': () => childDataset,
  170 |         'GET ip_addresses': () => ({ ip_addresses: [] }),
  171 |         'GET transaction_chains': () => ({ transaction_chains: [], _meta: { total_count: 0 } }),
  172 |         'GET vpses/123/mounts': () => ({ mounts: [] }),
  173 |         'POST datasets': () => ({ dataset: childDataset }),
  174 |       },
  175 |     });
  176 | 
  177 |     await page.goto('/app/vps/123/storage');
  178 | 
> 179 |     await page.getByTestId('vps.storage.root_dataset.create_subdataset').click();
      |                                                                          ^ Error: locator.click: Test timeout of 90000ms exceeded.
  180 | 
  181 |     const createModal = page.getByTestId('dataset.manage.create.modal');
  182 |     await expect(createModal).toBeVisible();
  183 |     await expect(page).toHaveURL(/\/app\/datasets\/10$/);
  184 |     await createModal.getByTestId('dataset.manage.create.name').fill('storage-child');
  185 | 
  186 |     const createRequest = page.waitForRequest(
  187 |       (request) => request.method() === 'POST' && request.url().includes('/api/v7.0/datasets')
  188 |     );
  189 |     await createModal.getByTestId('dataset.manage.create.submit').click();
  190 | 
  191 |     expect((await createRequest).postDataJSON()).toEqual({
  192 |       dataset: {
  193 |         name: 'storage-child',
  194 |         dataset: 10,
  195 |         automount: true,
  196 |       },
  197 |     });
  198 |     await expect(page).toHaveURL(/\/app\/datasets\/11$/);
  199 |     await expect(page.getByTestId('dataset.header')).toContainText('tank/data/storage-child');
  200 |   });
  201 | 
  202 |   test('@workflow-matrix creates mount by finding dataset and posting', async ({ page }) => {
  203 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  204 | 
  205 |     let mounts = [
  206 |       {
  207 |         id: 1,
  208 |         mountpoint: '/mnt/old',
  209 |         mode: 'ro',
  210 |         enabled: true,
  211 |         on_start_fail: 'ignore',
  212 |         current_state: 'mounted',
  213 |         expiration_date: '2026-02-28T00:00:00Z',
  214 |         dataset: { id: 9, name: 'tank/old' },
  215 |         created_at: '2026-01-31T00:00:00Z',
  216 |       },
  217 |     ];
  218 | 
  219 |     await installHaveApiMock(page, {
  220 |       user: { id: 1, login: 'user', level: 1 },
  221 |       handlers: {
  222 |         'GET vpses/123': () => ({ vps }),
  223 |         'GET datasets/10': () => ({ dataset }),
  224 |         'GET ip_addresses': () => ({ ip_addresses: [] }),
  225 |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  226 |         'GET vpses/123/mounts': () => ({ mounts }),
  227 |         'GET datasets/find_by_name': () => ({ dataset }),
  228 |         'POST vpses/123/mounts': () => {
  229 |           const created = {
  230 |             id: 2,
  231 |             mountpoint: '/mnt/data',
  232 |                 mode: 'rw',
  233 |             enabled: true,
  234 |             on_start_fail: 'ignore',
  235 |                 current_state: 'mounted',
  236 |             expiration_date: '2026-02-28T00:00:00Z',
  237 |             dataset: { ...dataset },
  238 |             created_at: '2026-01-31T01:00:00Z',
  239 |           };
  240 |           mounts = [...mounts, created];
  241 |           return { mount: created, _meta: { action_state_id: 703 } };
  242 |         },
  243 |         'GET action_states/703': () => ({
  244 |           action_state: {
  245 |             id: 703,
  246 |             label: 'Create mount',
  247 |             status: true,
  248 |             finished: false,
  249 |             current: 1,
  250 |             total: 2,
  251 |           },
  252 |         }),
  253 |       },
  254 |     });
  255 | 
  256 |     await page.goto('/app/vps/123/storage');
  257 | 
  258 |     await expect(page.getByTestId('vps.storage.page')).toBeVisible();
  259 |     await expect(page.getByTestId('vps.storage.root_dataset')).toBeVisible();
  260 |     await expect(page.getByTestId('vps.storage.root_dataset.metadata')).toContainText('5.0 GiB');
  261 |     await expect(page.getByTestId('vps.storage.root_dataset.metadata')).toContainText('15 GiB');
  262 |     await expect(page.getByTestId('vps.storage.root_dataset.metadata')).toContainText('20 GiB');
  263 |     await expect(page.getByTestId('vps.storage.no_backup_cta_note')).toHaveCount(0);
  264 |     await expect(page.getByTestId('vps.storage.root_dataset.details')).toBeVisible();
  265 |     await expect(page.getByTestId('vps.storage.root_dataset.system_context')).toHaveCount(0);
  266 |     await expect(page.getByTestId('vps.storage.root_dataset.open')).toHaveAttribute('href', '/app/datasets/10');
  267 |     await expect(page.getByTestId('vps.storage.root_dataset.create_subdataset')).toHaveAttribute(
  268 |       'href',
  269 |       '/app/datasets/10?create=subdataset'
  270 |     );
  271 |     await expect(page.getByTestId('vps.storage.root_dataset.snapshots')).toHaveAttribute('href', '/app/datasets/10/snapshots');
  272 |     await expect(page.getByTestId('vps.storage.root_dataset.downloads')).toHaveAttribute('href', '/app/datasets/10/downloads');
  273 |     await expect(page.getByTestId('vps.storage.root_dataset.create_snapshot')).toHaveCount(0);
  274 |     await expect(page.getByTestId('vps.storage.root_dataset.restore')).toHaveCount(0);
  275 |     await expect(page.getByTestId('vps.storage.root_dataset.backup')).toHaveCount(0);
  276 |     await expect(mountItem(page, 1)).toBeVisible();
  277 |     await expect(mountItemControl(page, 1, 'dataset')).toHaveAttribute('href', '/app/datasets/9');
  278 |     await expect(mountItem(page, 1)).toContainText('mounted');
  279 |     await expect(mountItem(page, 1)).toContainText('2026');
```