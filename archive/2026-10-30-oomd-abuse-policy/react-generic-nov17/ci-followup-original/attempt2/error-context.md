# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/vps_support_permissions.spec.ts >> @pr-smoke support account stays read-only inside the admin VPS shell
- Location: e2e/specs/app/vps_support_permissions.spec.ts:32:1

# Error details

```
Error: expect(received).toEqual(expected) // deep equality

- Expected  -  1
+ Received  + 11

- Array []
+ Array [
+   "OPTIONS /api/v7.0/",
+   "OPTIONS /api/v7.0/",
+   "OPTIONS /api/v7.0/",
+   "OPTIONS /api/v7.0/",
+   "OPTIONS /api/v7.0/",
+   "OPTIONS /api/v7.0/",
+   "OPTIONS /api/v7.0/",
+   "OPTIONS /api/v7.0/",
+   "OPTIONS /api/v7.0/",
+ ]
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
          - search [ref=e10]:
            - img [ref=e11]
            - combobox "Quickly search objects" [ref=e14]
          - button "Open tasks" [ref=e16]:
            - img [ref=e17]
            - generic [ref=e19]: Tasks
          - 'button "Account: support-agent" [ref=e21]':
            - generic [ref=e22]: support-agent
            - generic [ref=e23]: Support
            - img [ref=e24]
        - navigation [ref=e26]:
          - link "Dashboard" [ref=e29] [cursor=pointer]:
            - /url: /admin
            - img [ref=e31]
            - generic [ref=e36]: Dashboard
          - region "Services" [ref=e37]:
            - generic [ref=e38]: Services
            - generic [ref=e39]:
              - link "VPS" [ref=e40] [cursor=pointer]:
                - /url: /admin/vps
                - img [ref=e42]
                - generic [ref=e45]: VPS
              - link "Datasets" [ref=e46] [cursor=pointer]:
                - /url: /admin/datasets
                - img [ref=e48]
                - generic [ref=e52]: Datasets
              - link "NAS" [ref=e53] [cursor=pointer]:
                - /url: /admin/nas
                - img [ref=e55]
                - generic [ref=e57]: NAS
              - link "Exports" [ref=e58] [cursor=pointer]:
                - /url: /admin/exports
                - img [ref=e60]
                - generic [ref=e63]: Exports
              - link "DNS" [ref=e64] [cursor=pointer]:
                - /url: /admin/dns
                - img [ref=e66]
                - generic [ref=e69]: DNS
              - link "Networking" [ref=e70] [cursor=pointer]:
                - /url: /admin/networking/ip-addresses
                - img [ref=e72]
                - generic [ref=e77]: Networking
          - region "Operations" [ref=e78]:
            - generic [ref=e79]: Operations
            - generic [ref=e80]:
              - link "Transactions" [ref=e81] [cursor=pointer]:
                - /url: /admin/transactions
                - img [ref=e83]
                - generic [ref=e86]: Transactions
              - link "Monitoring" [ref=e87] [cursor=pointer]:
                - /url: /admin/monitoring
                - img [ref=e89]
                - generic [ref=e91]: Monitoring
              - link "Incidents" [ref=e92] [cursor=pointer]:
                - /url: /admin/incidents
                - img [ref=e94]
                - generic [ref=e96]: Incidents
              - link "Out-of-memory" [ref=e97] [cursor=pointer]:
                - /url: /admin/oom-reports
                - img [ref=e99]
                - generic [ref=e101]: Out-of-memory
              - link "Audit" [ref=e102] [cursor=pointer]:
                - /url: /admin/audit
                - img [ref=e104]
                - generic [ref=e107]: Audit
          - region "Users and finance" [ref=e108]:
            - generic [ref=e109]: Users and finance
            - generic [ref=e110]:
              - link "Users" [ref=e111] [cursor=pointer]:
                - /url: /admin/users
                - img [ref=e113]
                - generic [ref=e118]: Users
              - link "User namespaces" [ref=e119] [cursor=pointer]:
                - /url: /admin/user-namespaces/namespaces
                - img [ref=e121]
                - generic [ref=e125]: User namespaces
              - link "Requests" [ref=e126] [cursor=pointer]:
                - /url: /admin/requests
                - img [ref=e128]
                - generic [ref=e131]: Requests
          - region "Infrastructure" [ref=e132]:
            - generic [ref=e133]: Infrastructure
            - generic [ref=e134]:
              - link "Cluster" [ref=e135] [cursor=pointer]:
                - /url: /admin/cluster/summary
                - img [ref=e137]
                - generic [ref=e147]: Cluster
              - link "Nodes" [ref=e148] [cursor=pointer]:
                - /url: /admin/nodes
                - img [ref=e150]
                - generic [ref=e153]: Nodes
              - link "Migration plans" [ref=e154] [cursor=pointer]:
                - /url: /admin/migration-plans
                - img [ref=e156]
                - generic [ref=e160]: Migration plans
              - link "Admin" [ref=e161] [cursor=pointer]:
                - /url: /admin/admin-info
                - img [ref=e163]
                - generic [ref=e165]: Admin
          - region "Content" [ref=e166]:
            - generic [ref=e167]: Content
            - generic [ref=e168]:
              - link "Mailer" [ref=e169] [cursor=pointer]:
                - /url: /admin/mailer/templates
                - img [ref=e171]
                - generic [ref=e174]: Mailer
              - link "News and help" [ref=e175] [cursor=pointer]:
                - /url: /admin/content/news
                - img [ref=e177]
                - generic [ref=e180]: News and help
          - generic [ref=e182]:
            - link "Outages" [ref=e183] [cursor=pointer]:
              - /url: /admin/outages
              - img [ref=e185]
              - generic [ref=e187]: Outages
            - link "Security advisories" [ref=e188] [cursor=pointer]:
              - /url: /admin/status/security-advisories
              - img [ref=e190]
              - generic [ref=e192]: Security advisories
        - generic [ref=e194]:
          - img [ref=e195]
          - generic [ref=e197]: vpsAdmin
        - generic [ref=e199]:
          - link "About" [ref=e200] [cursor=pointer]:
            - /url: /about
          - link "View commit 3b8a3aeafe28" [ref=e201] [cursor=pointer]:
            - /url: https://github.com/vpsfreecz/vpsadmin-webui/commit/3b8a3aeafe287e43af65e7272f6c9e8349d70a55
            - text: 3b8a3aeafe28
    - main [ref=e204]:
      - generic [ref=e207]:
        - generic [ref=e209]:
          - generic [ref=e210]:
            - generic [ref=e212]:
              - heading "support-vps.example" [level=1] [ref=e214]
              - generic [ref=e216]:
                - generic [ref=e217]:
                  - link "VPS" [ref=e218] [cursor=pointer]:
                    - /url: /admin/vps
                  - generic [ref=e219]: ·
                  - generic [ref=e220]: "#123"
                - generic [ref=e221]: Stopped
                - generic [ref=e222]: Active
            - generic [ref=e224]:
              - link "Access" [ref=e225] [cursor=pointer]:
                - /url: /admin/vps/123/access
              - combobox "VPS actions" [ref=e227]:
                - option "More…" [selected]
                - option "DNS servers"
                - option "Access"
                - option "Config"
                - option "Network"
                - option "Storage"
                - option "Features"
                - option "Maintenance"
                - option "History"
                - option "Transaction log"
                - option "OOM reports"
                - option "Incident reports"
                - option "Outages"
          - generic [ref=e228]:
            - generic [ref=e230]:
              - generic [ref=e231]:
                - text: Owner
                - 'link "foreign-owner #77" [ref=e232] [cursor=pointer]':
                  - /url: /admin/users/77
                  - text: foreign-owner
                  - generic [ref=e233]: "#77"
              - generic [ref=e234]: Distribution Debian latest
              - generic [ref=e235]: Node node1.example
              - generic [ref=e236]: Location Praha-2
            - generic [ref=e239]:
              - generic [ref=e240]: "SSH:"
              - generic [ref=e241]:
                - code [ref=e242]: ssh root@192.0.2.10
                - button "Copy" [ref=e243]
          - generic [ref=e245]:
            - generic [ref=e246]:
              - generic [ref=e247]:
                - term [ref=e248]:
                  - img [ref=e249]
                  - text: Uptime
                - definition [ref=e252]: —
              - generic [ref=e253]:
                - term [ref=e254]:
                  - img [ref=e255]
                  - text: Load average (1 / 5 / 15 min)
                - definition [ref=e257]: —
              - generic [ref=e258]:
                - term [ref=e259]:
                  - img [ref=e260]
                  - text: Processes
                - definition [ref=e264]: —
              - generic [ref=e265]:
                - term [ref=e266]:
                  - img [ref=e267]
                  - text: CPU usage
                - definition [ref=e270]: —
            - generic [ref=e271]:
              - link "Overview" [ref=e272] [cursor=pointer]:
                - /url: /admin/vps/123
              - link "Access" [ref=e273] [cursor=pointer]:
                - /url: /admin/vps/123/access
              - link "Network" [ref=e274] [cursor=pointer]:
                - /url: /admin/vps/123/network
              - link "Storage" [ref=e275] [cursor=pointer]:
                - /url: /admin/vps/123/storage
              - link "Maintenance" [ref=e276] [cursor=pointer]:
                - /url: /admin/vps/123/maintenance
              - link "History" [ref=e277] [cursor=pointer]:
                - /url: /admin/vps/123/history
              - link "Console" [ref=e278] [cursor=pointer]:
                - /url: /admin/vps/123/console
        - generic [ref=e279]:
          - generic [ref=e280]:
            - generic [ref=e282]:
              - generic [ref=e283]: VPS modifications by the admin team
              - generic [ref=e284]: Choose whether vpsFree.cz administrators may update the base system configuration inside this VPS.
            - generic [ref=e286]:
              - generic [ref=e287]:
                - paragraph [ref=e288]: New software features or bug fixes may require changes to base system configuration files normally delivered in OS templates. If you allow these changes, the admin team can make them for you. The team does not access or modify your applications or data and will notify you by email about changes.
                - generic [ref=e290]: The current preference is unavailable. Refresh before changing it.
                - group "VPS modifications by the admin team" [ref=e291]:
                  - generic [ref=e292]: VPS modifications by the admin team
                  - generic [ref=e293] [cursor=pointer]:
                    - radio "Allow modifications by the vpsFree.cz admin team (recommended)" [disabled] [ref=e294]
                    - generic [ref=e295]: Allow modifications by the vpsFree.cz admin team (recommended)
                  - generic [ref=e296] [cursor=pointer]:
                    - radio "Do not allow modifications by the vpsFree.cz admin team" [disabled] [ref=e297]
                    - generic [ref=e298]: Do not allow modifications by the vpsFree.cz admin team
              - button "Refresh" [ref=e300]
          - generic [ref=e301]:
            - generic [ref=e303]:
              - generic [ref=e304]: Maintenance window
              - generic [ref=e305]: Configure a weekly maintenance schedule for this VPS.
            - generic [ref=e306]:
              - generic [ref=e307]:
                - generic [ref=e308]: Not allowed
                - generic [ref=e311]: You do not have permission to perform this action.
              - generic [ref=e312]:
                - generic [ref=e314]: No unsaved changes.
                - table [ref=e316]:
                  - rowgroup [ref=e317]:
                    - row "Day Open Opens Closes Summary" [ref=e318]:
                      - columnheader "Day" [ref=e319]
                      - columnheader "Open" [ref=e320]
                      - columnheader "Opens" [ref=e321]
                      - columnheader "Closes" [ref=e322]
                      - columnheader "Summary" [ref=e323]
                  - rowgroup [ref=e324]:
                    - row "Monday Open 01:00 02:00 01:00–02:00" [ref=e325]:
                      - cell "Monday" [ref=e326]
                      - cell "Open" [ref=e327]
                      - cell "01:00" [ref=e328]
                      - cell "02:00" [ref=e329]
                      - cell "01:00–02:00" [ref=e330]
                    - row "Tuesday Closed — — Closed" [ref=e331]:
                      - cell "Tuesday" [ref=e332]
                      - cell "Closed" [ref=e333]
                      - cell "—" [ref=e334]
                      - cell "—" [ref=e335]
                      - cell "Closed" [ref=e336]
                    - row "Wednesday Closed — — Closed" [ref=e337]:
                      - cell "Wednesday" [ref=e338]
                      - cell "Closed" [ref=e339]
                      - cell "—" [ref=e340]
                      - cell "—" [ref=e341]
                      - cell "Closed" [ref=e342]
                    - row "Thursday Closed — — Closed" [ref=e343]:
                      - cell "Thursday" [ref=e344]
                      - cell "Closed" [ref=e345]
                      - cell "—" [ref=e346]
                      - cell "—" [ref=e347]
                      - cell "Closed" [ref=e348]
                    - row "Friday Closed — — Closed" [ref=e349]:
                      - cell "Friday" [ref=e350]
                      - cell "Closed" [ref=e351]
                      - cell "—" [ref=e352]
                      - cell "—" [ref=e353]
                      - cell "Closed" [ref=e354]
                    - row "Saturday Closed — — Closed" [ref=e355]:
                      - cell "Saturday" [ref=e356]
                      - cell "Closed" [ref=e357]
                      - cell "—" [ref=e358]
                      - cell "—" [ref=e359]
                      - cell "Closed" [ref=e360]
                    - row "Sunday Closed — — Closed" [ref=e361]:
                      - cell "Sunday" [ref=e362]
                      - cell "Closed" [ref=e363]
                      - cell "—" [ref=e364]
                      - cell "—" [ref=e365]
                      - cell "Closed" [ref=e366]
```

# Test source

```ts
  115 |   await expect(page.getByTestId('vps.actions.menu').locator('option[value$="/config"]')).toHaveCount(1);
  116 |   await expect(page.getByTestId('vps.actions.menu').locator('option[value="/admin/vps/123/lifecycle"]')).toHaveCount(0);
  117 |   await expect(page.getByTestId('vps.actions.menu').locator('option[value="/admin/oom-reports?vps=123"]')).toHaveCount(1);
  118 |   await expect(page.getByTestId('vps.actions.menu').locator('option[value="/admin/incidents?vps=123"]')).toHaveCount(1);
  119 |   await expect(page.getByTestId('vps.actions.menu').locator('option[value="/admin/oom-reports/rules/123"]')).toHaveCount(0);
  120 |   await expect(page.getByTestId('vps.actions.menu').locator('option[value="/admin/incidents/new?vps=123"]')).toHaveCount(0);
  121 |   await expect(page.getByTestId('vps.actions.menu').locator('option[value="/admin/users/77/user-data"]')).toHaveCount(0);
  122 | 
  123 |   await page.goto('/admin/vps/123/config');
  124 | 
  125 |   await expect(page.getByText('Boot preferences')).toBeVisible();
  126 |   await expect(page.getByText('Start menu timeout', { exact: true })).toHaveCount(0);
  127 |   await expect(page.getByText('Owner', { exact: true })).toHaveCount(0);
  128 |   await expect(page.getByText('CPU limit', { exact: true })).toHaveCount(0);
  129 |   await expect(page.getByText('Autostart priority', { exact: true })).toHaveCount(0);
  130 |   await expect(page.getByText('Change reason', { exact: true })).toHaveCount(0);
  131 |   await expect(page.getByText('Admin lock type', { exact: true })).toHaveCount(0);
  132 |   await expect(page.getByTestId('vps.config.admin_override')).toHaveCount(0);
  133 |   await expect(page.getByText('You do not have permission to perform this action.')).toBeVisible();
  134 |   const configFieldsets = page.locator('main fieldset:disabled');
  135 |   expect(await configFieldsets.count()).toBeGreaterThan(0);
  136 |   for (const fieldset of await configFieldsets.all()) await expect(fieldset).toBeVisible();
  137 |   const configInputs = page.locator('main fieldset input, main fieldset select, main fieldset textarea');
  138 |   expect(await configInputs.count()).toBeGreaterThan(0);
  139 |   for (const input of await configInputs.all()) await expect(input).toBeDisabled();
  140 | 
  141 |   await page.goto('/admin/vps/123/lifecycle');
  142 | 
  143 |   await expect(page.getByText('You do not have permission to perform this action.')).toBeVisible();
  144 |   await expect(page.getByTestId('vps.lifecycle.daily_actions')).toHaveCount(0);
  145 |   await expect(page.getByTestId('vps.lifecycle.action_link.clone')).toHaveCount(0);
  146 |   await expect(page.getByTestId('vps.lifecycle.action_link.swap')).toHaveCount(0);
  147 |   await expect(page.getByTestId('vps.lifecycle.action_link.delete')).toHaveCount(0);
  148 |   await expect(page.getByTestId('vps.lifecycle.admin_actions')).toHaveCount(0);
  149 |   await expect(page.getByTestId('vps.lifecycle.action_link.lifetime')).toHaveCount(0);
  150 |   await expect(page.getByTestId('vps.lifecycle.action_link.replace')).toHaveCount(0);
  151 |   await expect(page.getByTestId('vps.lifecycle.action_link.migrate')).toHaveCount(0);
  152 | 
  153 |   await page.goto('/admin/vps/123/lifecycle/migrate');
  154 | 
  155 |   await expect(page.getByTestId('vps.lifecycle.page')).toBeVisible();
  156 |   await expect(page.getByTestId('vps.lifecycle.migrate')).toHaveCount(0);
  157 |   expect(nodeRequests).toBe(0);
  158 | 
  159 |   await page.goto('/admin/vps/123/access');
  160 | 
  161 |   await expect(page.getByTestId('vps.access.read_only')).toBeVisible();
  162 |   await expect(page.getByTestId('vps.access.password_type')).toHaveCount(0);
  163 |   await expect(page.getByTestId('vps.access.password.generate')).toHaveCount(0);
  164 |   await expect(page.getByTestId('vps.access.ssh.key')).toHaveCount(0);
  165 |   await expect(page.getByTestId('vps.access.ssh.deploy')).toHaveCount(0);
  166 |   await expect(page.getByTestId('vps.access.host_keys')).toBeVisible();
  167 | 
  168 |   await page.goto('/admin/vps/123/network');
  169 | 
  170 |   await expect(page.getByTestId('vps.network.read_only')).toBeVisible();
  171 |   const interfaceTestId = mobileLayout
  172 |     ? 'vps.network.interfaces.card.31'
  173 |     : 'vps.network.interfaces.row.31';
  174 |   await expect(page.getByTestId(interfaceTestId)).toBeVisible();
  175 |   await expect(page.getByTestId(`${interfaceTestId}.edit`)).toHaveCount(0);
  176 |   await expect(page.getByTestId('vps.network.ip_addresses.item.41')).toBeVisible();
  177 |   await expect(page.getByTestId('vps.network.ip_addresses.add')).toHaveCount(0);
  178 |   await expect(page.getByTestId('vps.network.ip_addresses.item.41.free_route')).toHaveCount(0);
  179 |   await expect(page.getByTestId('vps.network.host_addresses.row.51')).toBeVisible();
  180 |   await expect(page.getByTestId('vps.network.host_addresses.row.51.ptr')).toHaveCount(0);
  181 |   await expect(page.getByTestId('vps.network.host_addresses.row.51.free')).toHaveCount(0);
  182 |   await expect(page.getByTestId('vps.network.admin_settings')).toHaveCount(0);
  183 | 
  184 |   await page.goto('/admin/vps/123/storage');
  185 | 
  186 |   await expect(page.getByTestId('vps.storage.read_only')).toBeVisible();
  187 |   await expect(page.getByTestId('vps.storage.mounts.add')).toHaveCount(0);
  188 |   const mountTestId = mobileLayout
  189 |     ? 'vps.storage.mounts.card.61'
  190 |     : 'vps.storage.mounts.row.61';
  191 |   await expect(page.getByTestId(mountTestId)).toBeVisible();
  192 |   await expect(page.getByTestId(`${mountTestId}.edit`)).toHaveCount(0);
  193 |   await expect(page.getByTestId(`${mountTestId}.delete`)).toHaveCount(0);
  194 |   await expect(page.getByTestId('vps.storage.root_dataset.create_subdataset')).toHaveCount(0);
  195 | 
  196 |   await page.goto('/admin/vps/123/features');
  197 | 
  198 |   await expect(page.getByTestId('vps.features.read_only')).toBeVisible();
  199 |   await expect(page.getByTestId('vps.features.item.71')).toBeVisible();
  200 |   await expect(page.getByTestId('vps.features.item.71').locator('input')).toHaveCount(0);
  201 |   await expect(page.getByTestId('vps.features.reset')).toHaveCount(0);
  202 |   await expect(page.getByTestId('vps.features.save')).toHaveCount(0);
  203 | 
  204 |   await page.goto('/admin/vps/123/maintenance');
  205 | 
  206 |   await expect(page.getByTestId('vps.maintenance.read_only')).toBeVisible();
  207 |   await expect(page.getByTestId('vps.maintenance.day.1')).toBeVisible();
  208 |   await expect(page.getByTestId('vps.maintenance.day.1.open')).toHaveCount(0);
  209 |   await expect(page.getByTestId('vps.maintenance.day.1.opens.h')).toHaveCount(0);
  210 |   await expect(page.getByTestId('vps.maintenance.reset')).toHaveCount(0);
  211 |   await expect(page.getByTestId('vps.maintenance.save')).toHaveCount(0);
  212 |   await expect(page.getByTestId('vps.maintenance.allow_anytime')).toHaveCount(0);
  213 |   await expect(page.getByTestId('vps.maintenance.disallow_all')).toHaveCount(0);
  214 | 
> 215 |   expect(mutatingApiRequests).toEqual([]);
      |                               ^ Error: expect(received).toEqual(expected) // deep equality
  216 | });
  217 | 
```