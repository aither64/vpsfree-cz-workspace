# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/vps_network_tab_actions.spec.ts >> @pr-smoke VPS network tab >> assigns routes and manages interface addresses and PTR
- Location: e2e/specs/app/vps_network_tab_actions.spec.ts:247:3

# Error details

```
Error: expect(locator).toHaveValue(expected) failed

Locator: getByTestId('vps.network.host_addresses.assign.interface')
Expected: "1"
Error: Not an input element

Call log:
  - Expect "toHaveValue" with timeout 15000ms
  - waiting for getByTestId('vps.network.host_addresses.assign.interface')

```

# Page snapshot

```yaml
- generic [ref=e1]:
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
            - link "View commit dbe60e2fd335" [ref=e194] [cursor=pointer]:
              - /url: https://github.com/vpsfreecz/vpsadmin-webui/commit/dbe60e2fd335efc4261f6af3a7878643221b66a7
              - text: dbe60e2fd335
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
                    - generic [ref=e232]: Running
                    - generic [ref=e233]: Active
                - generic [ref=e235]:
                  - link "Access" [ref=e236] [cursor=pointer]:
                    - /url: /admin/vps/123/access
                  - button "Restart" [ref=e237]:
                    - img [ref=e238]
                    - text: Restart
                  - button "Shutdown" [ref=e241]:
                    - img [ref=e242]
                    - text: Shutdown
                  - combobox "VPS actions" [ref=e244]:
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
                    - option "OOM reports"
                    - option "Incident reports"
                    - option "Outages"
                    - option "Configure OOM reports"
                    - option "Report incident"
                    - option "User namespaces"
                    - option "Update VPS lifecycle"
                    - option "Replace VPS"
                    - option "Migrate VPS"
              - generic [ref=e245]:
                - generic [ref=e247]:
                  - generic [ref=e248]: Distribution debian
                  - generic [ref=e249]: Node node1.example
                  - generic [ref=e250]: Location Prague
                - generic [ref=e253]:
                  - generic [ref=e254]: "SSH:"
                  - generic [ref=e255]:
                    - code [ref=e256]: ssh root@198.51.100.10
                    - button "Copy" [ref=e257]
              - generic [ref=e259]:
                - generic [ref=e260]:
                  - generic [ref=e261]:
                    - term [ref=e262]:
                      - img [ref=e263]
                      - text: Uptime
                    - definition [ref=e266]: 3h 25m
                  - generic [ref=e267]:
                    - term [ref=e268]:
                      - img [ref=e269]
                      - text: Load average (1 / 5 / 15 min)
                    - definition [ref=e271]: 0.12 / — / —
                  - generic [ref=e272]:
                    - term [ref=e273]:
                      - img [ref=e274]
                      - text: Processes
                    - definition [ref=e278]: —
                  - generic [ref=e279]:
                    - term [ref=e280]:
                      - img [ref=e281]
                      - text: CPU usage
                    - definition [ref=e284]: —
                - generic [ref=e285]:
                  - link "Overview" [ref=e286] [cursor=pointer]:
                    - /url: /admin/vps/123
                  - link "Access" [ref=e287] [cursor=pointer]:
                    - /url: /admin/vps/123/access
                  - link "Network" [ref=e288] [cursor=pointer]:
                    - /url: /admin/vps/123/network
                  - link "Storage" [ref=e289] [cursor=pointer]:
                    - /url: /admin/vps/123/storage
                  - link "Maintenance" [ref=e290] [cursor=pointer]:
                    - /url: /admin/vps/123/maintenance
                  - link "History" [ref=e291] [cursor=pointer]:
                    - /url: /admin/vps/123/history
                  - link "Console" [ref=e292] [cursor=pointer]:
                    - /url: /admin/vps/123/console
            - generic [ref=e293]:
              - generic [ref=e294]:
                - generic [ref=e295]:
                  - generic [ref=e296]:
                    - generic [ref=e297]: Network overview
                    - generic [ref=e298]: Network connection state, interfaces and traffic for the current month.
                  - generic [ref=e300]:
                    - button "Refresh" [ref=e301]
                    - generic [ref=e302]: Network enabled
                - generic [ref=e304]:
                  - generic [ref=e305]:
                    - generic [ref=e306]: VPS network
                    - generic [ref=e307]: Enabled
                    - generic [ref=e308]: Network access is enabled for this VPS.
                  - generic [ref=e309]:
                    - generic [ref=e310]: Interfaces
                    - generic [ref=e311]: 0/1 enabled
                    - generic [ref=e312]: 1 disabled interfaces.
                  - generic [ref=e313]:
                    - generic [ref=e314]: Ingress
                    - generic [ref=e315]: 1.0 KiB
                    - generic [ref=e316]: Current month
                  - generic [ref=e317]:
                    - generic [ref=e318]: Egress
                    - generic [ref=e319]: 2.0 KiB
                    - generic [ref=e320]: Current month
              - generic [ref=e321]:
                - generic [ref=e322]:
                  - generic [ref=e323]:
                    - generic [ref=e324]: Interfaces
                    - generic [ref=e325]: Edit interface settings. Disabling network affects connectivity.
                  - button "Refresh" [ref=e327]
                - table [ref=e330]:
                  - rowgroup [ref=e331]:
                    - row "Name Type MAC address IP addresses Enabled Max TX Max RX" [ref=e332]:
                      - columnheader [ref=e333]
                      - columnheader "Name" [ref=e334]
                      - columnheader "Type" [ref=e335]
                      - columnheader "MAC address" [ref=e336]
                      - columnheader "IP addresses" [ref=e337]
                      - columnheader "Enabled" [ref=e338]
                      - columnheader "Max TX" [ref=e339]
                      - columnheader "Max RX" [ref=e340]
                      - columnheader [ref=e341]
                  - rowgroup [ref=e342]:
                    - row "eth0 virtio — 2 Disabled 100 Mbps 200 Mbps Edit" [ref=e343]:
                      - cell [ref=e344]
                      - cell "eth0" [ref=e346]
                      - cell "virtio" [ref=e347]
                      - cell "—" [ref=e348]
                      - cell "2" [ref=e349]
                      - cell "Disabled" [ref=e350]:
                        - generic [ref=e351]: Disabled
                      - cell "100 Mbps" [ref=e352]
                      - cell "200 Mbps" [ref=e353]
                      - cell "Edit" [ref=e354]:
                        - button "Edit" [ref=e355]
              - generic [ref=e356]:
                - generic [ref=e358]:
                  - generic [ref=e359]:
                    - heading "IP addresses" [level=2] [ref=e360]
                    - paragraph [ref=e361]: First add a route to the VPS, then choose an address from it for the network interface. Edit PTR directly on the address.
                  - generic [ref=e362]:
                    - generic [ref=e363]: "1"
                    - generic [ref=e364]: Assign route
                    - generic [ref=e365]: →
                    - generic [ref=e366]: "2"
                    - generic [ref=e367]: Add address
                - generic [ref=e368]:
                  - generic [ref=e369]:
                    - generic [ref=e370]:
                      - generic [ref=e372]:
                        - generic [ref=e373]: "1"
                        - generic [ref=e374]: Routes to VPS
                      - generic [ref=e375]: A route makes the selected address range available to this VPS.
                    - generic [ref=e377]:
                      - button "Refresh" [ref=e378]
                      - button "Add route" [ref=e379]
                  - generic [ref=e380]:
                    - generic [ref=e381]: Select an interface and address type, then a concrete free route. Add the address itself to the interface in step 2 below.
                    - generic [ref=e382]:
                      - generic [ref=e384]:
                        - generic [ref=e385]:
                          - generic [ref=e386]:
                            - generic [ref=e387]: 198.51.100.10
                            - generic [ref=e388]: Public IPv4
                            - generic [ref=e389]: Active
                          - generic [ref=e390]:
                            - generic [ref=e391]: "Interface: eth0"
                            - generic [ref=e392]: "Location: Prague"
                            - generic [ref=e393]: "Owner: old-owner"
                        - generic [ref=e394]:
                          - link "IP detail" [ref=e395] [cursor=pointer]:
                            - /url: /admin/networking/ip-addresses/1
                          - button "Owner" [ref=e396]
                          - button "Add host addresses" [ref=e397]
                          - button "Free route" [ref=e398]
                      - generic [ref=e400]:
                        - generic [ref=e401]:
                          - generic [ref=e402]:
                            - generic [ref=e403]: 198.51.100.20
                            - generic [ref=e404]: Public IPv4
                            - generic [ref=e405]: Active
                          - generic [ref=e406]:
                            - generic [ref=e407]: "Interface: eth0"
                            - generic [ref=e408]: "Location: Prague"
                            - generic [ref=e409]: "Owner: old-owner"
                        - generic [ref=e410]:
                          - link "IP detail" [ref=e411] [cursor=pointer]:
                            - /url: /admin/networking/ip-addresses/2
                          - button "Owner" [ref=e412]
                          - button "Add host addresses" [ref=e413]
                          - button "Free route" [ref=e414]
                - generic [ref=e415]:
                  - generic [ref=e416]:
                    - generic [ref=e417]:
                      - generic [ref=e419]:
                        - generic [ref=e420]: "2"
                        - generic [ref=e421]: Interface addresses & PTR
                      - generic [ref=e422]: Addresses used directly by the VPS and their reverse DNS.
                    - button "Refresh" [ref=e424]
                  - generic [ref=e425]:
                    - generic [ref=e426]: After adding a route, choose an available address for the interface. You can add or edit PTR directly on it at any time.
                    - generic [ref=e429]:
                      - generic [ref=e430]:
                        - generic [ref=e431]:
                          - generic [ref=e432]: 198.51.100.10
                          - generic [ref=e433]: On interface
                        - generic [ref=e434]:
                          - generic [ref=e435]: "Route: 198.51.100.10"
                          - generic [ref=e436]: "PTR: old.example.test."
                      - generic [ref=e437]:
                        - button "Edit PTR" [ref=e438]
                        - button "Remove from interface" [ref=e439]
                    - generic [ref=e440]:
                      - generic [ref=e441]: Available addresses from assigned routes
                      - generic [ref=e442]: Choose the address to add to the VPS network interface.
                      - generic [ref=e444]:
                        - generic [ref=e445]:
                          - generic [ref=e446]: 198.51.100.11
                          - generic [ref=e447]: "Route: 198.51.100.10"
                          - generic [ref=e448]: "PTR: —"
                        - generic [ref=e449]:
                          - button "Add PTR" [ref=e450]
                          - button "Add to interface" [ref=e451]
                          - button "Delete" [ref=e452]
                - group [ref=e454]:
                  - generic "Network administration Less common administrator actions for the VPS network connection. Show" [ref=e455] [cursor=pointer]:
                    - generic [ref=e456]:
                      - generic [ref=e457]: Network administration
                      - generic [ref=e458]: Less common administrator actions for the VPS network connection.
                    - generic [ref=e459]: Show
  - dialog "Add address 198.51.100.11 to interface" [ref=e462]:
    - generic [ref=e464]: Add address 198.51.100.11 to interface
    - generic [ref=e466]:
      - generic [ref=e467]:
        - generic [ref=e468]: Target VPS
        - generic [ref=e469]:
          - generic [ref=e470]: vps123.example
          - generic [ref=e471]: "#123"
      - generic [ref=e472]:
        - generic [ref=e473]: Network interface
        - text: eth0
      - generic [ref=e474]: 198.51.100.11 will be assigned to eth0.
    - generic [ref=e476]:
      - button "Cancel" [active] [ref=e477]
      - button "Add to interface" [ref=e478]
```

# Test source

```ts
  236 |     const req = await reqPromise;
  237 |     expect(req.postDataJSON()).toEqual({
  238 |       vps: {
  239 |         enable_network: false,
  240 |         change_reason: 'Testing',
  241 |       },
  242 |     });
  243 | 
  244 |     await expect(page.getByTestId('vps.network.disable_confirm')).toBeHidden();
  245 |   });
  246 | 
  247 |   test('assigns routes and manages interface addresses and PTR', async ({ page }) => {
  248 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  249 | 
  250 |     let currentIps: IpAddressFixture[] = [...ips];
  251 |     let hostAddresses = [
  252 |       {
  253 |         id: 50,
  254 |         addr: '198.51.100.10',
  255 |         assigned: true,
  256 |         reverse_record_value: 'old.example.test.',
  257 |         user_created: true,
  258 |         ip_address: { id: 1, addr: '198.51.100.10', network_interface: { id: 1 } },
  259 |       },
  260 |       {
  261 |         id: 51,
  262 |         addr: '198.51.100.11',
  263 |         assigned: false,
  264 |         user_created: true,
  265 |         ip_address: { id: 1, addr: '198.51.100.10', network_interface: { id: 1 } },
  266 |       },
  267 |     ];
  268 | 
  269 |     await installHaveApiMock(page, {
  270 |       user: { id: 1, login: 'admin', level: 90 },
  271 |       handlers: {
  272 |         'GET vpses/123': () => ({ vps }),
  273 |         'GET ip_addresses': () => ({ ip_addresses: currentIps }),
  274 |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  275 |         'GET network_interfaces': () => ({ network_interfaces: netifs }),
  276 |         'GET network_interface_accountings': () => ({ network_interface_accountings: acct }),
  277 |         'GET host_ip_addresses': () => ({ host_ip_addresses: hostAddresses }),
  278 |         'GET environments': () => ({ environments: [{ id: 3, label: 'env-test' }] }),
  279 |         'POST ip_addresses/2/assign': () => {
  280 |           currentIps = currentIps.map((ip) => (ip.id === 2 ? { ...ip, network_interface: { id: 1 }, routed: true } : ip));
  281 |           return { ip_address: currentIps.find((ip) => ip.id === 2), _meta: { action_state_id: 1202 } };
  282 |         },
  283 |         'POST ip_addresses/1/free': () => {
  284 |           currentIps = currentIps.map((ip) => (ip.id === 1 ? { ...ip, network_interface: null, routed: false } : ip));
  285 |           return { ip_address: currentIps.find((ip) => ip.id === 1), _meta: { action_state_id: 1203 } };
  286 |         },
  287 |         'PUT ip_addresses/1': () => {
  288 |           currentIps = currentIps.map((ip) => (ip.id === 1 ? { ...ip, user: { id: 77, login: 'new-owner' } } : ip));
  289 |           return { ip_address: currentIps.find((ip) => ip.id === 1), _meta: { action_state_id: 1204 } };
  290 |         },
  291 |         'POST host_ip_addresses/51/assign': () => {
  292 |           hostAddresses = hostAddresses.map((h) => (h.id === 51 ? { ...h, assigned: true } : h));
  293 |           return { host_ip_address: hostAddresses.find((h) => h.id === 51), _meta: { action_state_id: 1205 } };
  294 |         },
  295 |         'POST host_ip_addresses/50/free': () => {
  296 |           hostAddresses = hostAddresses.map((h) => (h.id === 50 ? { ...h, assigned: false } : h));
  297 |           return { host_ip_address: hostAddresses.find((h) => h.id === 50), _meta: { action_state_id: 1206 } };
  298 |         },
  299 |         'PUT host_ip_addresses/50': () => {
  300 |           hostAddresses = hostAddresses.map((h) =>
  301 |             h.id === 50 ? { ...h, reverse_record_value: 'new.example.test.' } : h
  302 |           );
  303 |           return { host_ip_address: hostAddresses[0], _meta: { action_state_id: 1207 } };
  304 |         },
  305 |         'GET action_states/1202': () => ({ action_state: { id: 1202, finished: true, status: true, current: 1, total: 1 } }),
  306 |         'GET action_states/1203': () => ({ action_state: { id: 1203, finished: true, status: true, current: 1, total: 1 } }),
  307 |         'GET action_states/1204': () => ({ action_state: { id: 1204, finished: true, status: true, current: 1, total: 1 } }),
  308 |         'GET action_states/1205': () => ({ action_state: { id: 1205, finished: true, status: true, current: 1, total: 1 } }),
  309 |         'GET action_states/1206': () => ({ action_state: { id: 1206, finished: true, status: true, current: 1, total: 1 } }),
  310 |         'GET action_states/1207': () => ({ action_state: { id: 1207, finished: true, status: true, current: 1, total: 1 } }),
  311 |       },
  312 |     });
  313 | 
  314 |     await page.goto('/admin/vps/123/network');
  315 |     await expect(page.getByTestId('vps.network.page')).toBeVisible();
  316 |     await page.getByTestId('vps.network.ip_addresses.unassigned.2.assign').click();
  317 |     await expect(page.getByTestId('vps.network.ip_addresses.add_modal')).toBeVisible();
  318 |     await expect(page.getByTestId('network.user.assign.interface')).toHaveValue('1');
  319 |     await expect(page.getByTestId('network.user.assign.kind')).toHaveValue('ipv4_public');
  320 |     await page.getByTestId('network.user.assign.continue').click();
  321 |     await expect(page.getByTestId('network.user.assign.address')).toHaveValue('2');
  322 |     await expect(page.getByTestId('network.user.assign.mode')).toHaveValue('route');
  323 | 
  324 |     const assignReq = page.waitForRequest(
  325 |       (r) => r.method() === 'POST' && r.url().includes('/api/v7.0/ip_addresses/2/assign')
  326 |     );
  327 |     await page.getByTestId('network.user.assign.submit').click();
  328 |     expect((await assignReq).postDataJSON()).toEqual({
  329 |       ip_address: {
  330 |         network_interface: 1,
  331 |       },
  332 |     });
  333 |     await expect(page.getByTestId('vps.network.ip_addresses.add_modal')).toBeHidden();
  334 | 
  335 |     await page.getByTestId('vps.network.host_addresses.row.51.assign').click();
> 336 |     await expect(page.getByTestId('vps.network.host_addresses.assign.interface')).toHaveValue('1');
      |                                                                                   ^ Error: expect(locator).toHaveValue(expected) failed
  337 | 
  338 |     const assignHostReq = page.waitForRequest(
  339 |       (r) => r.method() === 'POST' && r.url().includes('/api/v7.0/host_ip_addresses/51/assign')
  340 |     );
  341 |     await page.getByTestId('vps.network.host_addresses.assign.submit').click();
  342 |     expect((await assignHostReq).postDataJSON()).toEqual({
  343 |       host_ip_address: {
  344 |         network_interface: 1,
  345 |       },
  346 |     });
  347 |     await expect(page.getByTestId('vps.network.host_addresses.assign')).toBeHidden();
  348 | 
  349 |     await page.getByTestId('vps.network.host_addresses.row.50.ptr').click();
  350 |     await page.getByTestId('vps.network.host_addresses.ptr.value').fill('new.example.test.');
  351 | 
  352 |     const ptrReq = page.waitForRequest(
  353 |       (r) => r.method() === 'PUT' && r.url().includes('/api/v7.0/host_ip_addresses/50')
  354 |     );
  355 |     await page.getByTestId('vps.network.host_addresses.ptr.submit').click();
  356 |     expect((await ptrReq).postDataJSON()).toEqual({
  357 |       host_ip_address: {
  358 |         reverse_record_value: 'new.example.test.',
  359 |       },
  360 |     });
  361 | 
  362 |     await page.getByTestId('vps.network.host_addresses.row.50.free').click();
  363 |     await expect(page.getByTestId('vps.network.host_addresses.free_confirm')).toBeVisible();
  364 |     const freeHostReq = page.waitForRequest(
  365 |       (r) => r.method() === 'POST' && r.url().includes('/api/v7.0/host_ip_addresses/50/free')
  366 |     );
  367 |     await page.getByTestId('vps.network.host_addresses.free_confirm.confirm').click();
  368 |     expect((await freeHostReq).postData()).toBe('{}');
  369 | 
  370 |     await page.getByTestId('vps.network.ip_addresses.item.1.owner').click();
  371 |     await page.getByTestId('vps.network.ip_addresses.owner.user').fill('77');
  372 |     await page.getByTestId('vps.network.ip_addresses.owner.environment').selectOption('3');
  373 |     const ownerReq = page.waitForRequest(
  374 |       (r) => r.method() === 'PUT' && r.url().includes('/api/v7.0/ip_addresses/1')
  375 |     );
  376 |     await page.getByTestId('vps.network.ip_addresses.owner.submit').click();
  377 |     expect((await ownerReq).postDataJSON()).toEqual({
  378 |       ip_address: {
  379 |         user: 77,
  380 |         environment: 3,
  381 |       },
  382 |     });
  383 | 
  384 |     await page.getByTestId('vps.network.ip_addresses.item.1.free_route').click();
  385 |     await expect(page.getByTestId('vps.network.ip_addresses.free_route_confirm')).toBeVisible();
  386 |     const freeRouteReq = page.waitForRequest(
  387 |       (r) => r.method() === 'POST' && r.url().includes('/api/v7.0/ip_addresses/1/free')
  388 |     );
  389 |     await page.getByTestId('vps.network.ip_addresses.free_route_confirm.confirm').click();
  390 |     expect((await freeRouteReq).postData()).toBe('{}');
  391 |   });
  392 | 
  393 |   test('busy VPS transaction gates networking mutations with an explanation', async ({ page }) => {
  394 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  395 | 
  396 |     await installHaveApiMock(page, {
  397 |       user: { id: 1, login: 'admin', level: 90 },
  398 |       handlers: {
  399 |         'GET vpses/123': () => ({ vps }),
  400 |         'GET ip_addresses': () => ({ ip_addresses: ips }),
  401 |         'GET network_interfaces': () => ({ network_interfaces: netifs }),
  402 |         'GET network_interface_accountings': () => ({ network_interface_accountings: acct }),
  403 |         'GET host_ip_addresses': () => ({
  404 |           host_ip_addresses: [
  405 |             {
  406 |               id: 50,
  407 |               addr: '198.51.100.10',
  408 |               assigned: true,
  409 |               reverse_record_value: 'old.example.test.',
  410 |               user_created: true,
  411 |               ip_address: { id: 1, addr: '198.51.100.10' },
  412 |             },
  413 |             {
  414 |               id: 51,
  415 |               addr: '198.51.100.11',
  416 |               assigned: false,
  417 |               user_created: true,
  418 |               ip_address: { id: 1, addr: '198.51.100.10' },
  419 |             },
  420 |           ],
  421 |         }),
  422 |         'GET environments': () => ({ environments: [{ id: 3, label: 'env-test' }] }),
  423 |         'GET transaction_chains': (ctx) => {
  424 |           const cls = ctx.searchParams.get('transaction_chain[class_name]');
  425 |           const rowId = ctx.searchParams.get('transaction_chain[row_id]');
  426 | 
  427 |           if (cls === 'Vps' && rowId === '123') {
  428 |             return {
  429 |               transaction_chains: [
  430 |                 {
  431 |                   id: 919,
  432 |                   state: 'running',
  433 |                   name: 'Vps#123 network operation',
  434 |                   progress: 0,
  435 |                   size: 1,
  436 |                 },
```