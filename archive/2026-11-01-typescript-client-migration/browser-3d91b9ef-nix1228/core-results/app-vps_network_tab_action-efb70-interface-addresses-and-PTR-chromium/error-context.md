# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/vps_network_tab_actions.spec.ts >> @pr-smoke VPS network tab >> assigns routes and manages interface addresses and PTR
- Location: e2e/specs/app/vps_network_tab_actions.spec.ts:247:3

# Error details

```
Error: expect(received).toEqual(expected) // deep equality

- Expected  - 1
+ Received  + 3

- Object {}
+ Object {
+   "host_ip_address": Object {},
+ }
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
            - link "View commit 3d91b9ef3727" [ref=e194] [cursor=pointer]:
              - /url: https://github.com/vpsfreecz/vpsadmin-webui/commit/3d91b9ef3727cc2370d48c1dcab3f7e84efb8184
              - text: 3d91b9ef3727
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
                    - generic [ref=e427]:
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
                      - generic [ref=e441]:
                        - generic [ref=e442]:
                          - generic [ref=e443]:
                            - generic [ref=e444]: 198.51.100.11
                            - generic [ref=e445]: On interface
                          - generic [ref=e446]:
                            - generic [ref=e447]: "Route: 198.51.100.10"
                            - generic [ref=e448]: "PTR: —"
                        - generic [ref=e449]:
                          - button "Add PTR" [ref=e450]
                          - button "Remove from interface" [ref=e451]
                - group [ref=e453]:
                  - generic "Network administration Less common administrator actions for the VPS network connection. Show" [ref=e454] [cursor=pointer]:
                    - generic [ref=e455]:
                      - generic [ref=e456]: Network administration
                      - generic [ref=e457]: Less common administrator actions for the VPS network connection.
                    - generic [ref=e458]: Show
  - generic:
    - status [ref=e459]:
      - generic [ref=e460]:
        - generic [ref=e461]:
          - generic [ref=e462]: "Done: Assign host address"
          - generic [ref=e463]: "vps123.example · #1205"
        - button "Close" [ref=e464]:
          - generic [ref=e465]: ×
      - button "Open tasks" [ref=e467]
    - status [ref=e468]:
      - generic [ref=e469]:
        - generic [ref=e471]: IP address was added to the interface.
        - button "Close" [ref=e472]:
          - generic [ref=e473]: ×
    - status [ref=e474]:
      - generic [ref=e475]:
        - generic [ref=e476]:
          - generic [ref=e477]: "Done: Assign IP route"
          - generic [ref=e478]: "vps123.example · #1202"
        - button "Close" [ref=e479]:
          - generic [ref=e480]: ×
      - button "Open tasks" [ref=e482]
    - status [ref=e483]:
      - generic [ref=e484]:
        - generic [ref=e485]:
          - generic [ref=e486]: Route added
          - generic [ref=e487]: 198.51.100.20 is being added to VPS vps123.example.
        - button "Close" [ref=e488]:
          - generic [ref=e489]: ×
```

# Test source

```ts
  253 |       {
  254 |         id: 50,
  255 |         addr: '198.51.100.10',
  256 |         assigned: true,
  257 |         reverse_record_value: 'old.example.test.',
  258 |         user_created: true,
  259 |         ip_address: { id: 1, addr: '198.51.100.10', network_interface: { id: 1 } },
  260 |       },
  261 |       {
  262 |         id: 51,
  263 |         addr: '198.51.100.11',
  264 |         assigned: false,
  265 |         user_created: true,
  266 |         ip_address: { id: 1, addr: '198.51.100.10', network_interface: { id: 1 } },
  267 |       },
  268 |     ];
  269 | 
  270 |     await installHaveApiMock(page, {
  271 |       user: { id: 1, login: 'admin', level: 90 },
  272 |       handlers: {
  273 |         'GET vpses/123': () => ({ vps }),
  274 |         'GET ip_addresses': () => ({ ip_addresses: currentIps }),
  275 |         'GET transaction_chains': () => ({ transaction_chains: [] }),
  276 |         'GET network_interfaces': () => ({ network_interfaces: netifs }),
  277 |         'GET network_interface_accountings': () => ({ network_interface_accountings: acct }),
  278 |         'GET host_ip_addresses': () => ({ host_ip_addresses: hostAddresses }),
  279 |         'GET host_ip_addresses/51': () => {
  280 |           hostAssignmentRequests.push('read');
  281 |           return { host_ip_address: hostAddresses.find((h) => h.id === 51) };
  282 |         },
  283 |         'GET environments': () => ({ environments: [{ id: 3, label: 'env-test' }] }),
  284 |         'POST ip_addresses/2/assign': () => {
  285 |           currentIps = currentIps.map((ip) => (ip.id === 2 ? { ...ip, network_interface: { id: 1 }, routed: true } : ip));
  286 |           return { ip_address: currentIps.find((ip) => ip.id === 2), _meta: { action_state_id: 1202 } };
  287 |         },
  288 |         'POST ip_addresses/1/free': () => {
  289 |           currentIps = currentIps.map((ip) => (ip.id === 1 ? { ...ip, network_interface: null, routed: false } : ip));
  290 |           return { ip_address: currentIps.find((ip) => ip.id === 1), _meta: { action_state_id: 1203 } };
  291 |         },
  292 |         'PUT ip_addresses/1': () => {
  293 |           currentIps = currentIps.map((ip) => (ip.id === 1 ? { ...ip, user: { id: 77, login: 'new-owner' } } : ip));
  294 |           return { ip_address: currentIps.find((ip) => ip.id === 1), _meta: { action_state_id: 1204 } };
  295 |         },
  296 |         'POST host_ip_addresses/51/assign': () => {
  297 |           hostAssignmentRequests.push('assign');
  298 |           hostAddresses = hostAddresses.map((h) => (h.id === 51 ? { ...h, assigned: true } : h));
  299 |           return { host_ip_address: hostAddresses.find((h) => h.id === 51), _meta: { action_state_id: 1205 } };
  300 |         },
  301 |         'POST host_ip_addresses/50/free': () => {
  302 |           hostAddresses = hostAddresses.map((h) => (h.id === 50 ? { ...h, assigned: false } : h));
  303 |           return { host_ip_address: hostAddresses.find((h) => h.id === 50), _meta: { action_state_id: 1206 } };
  304 |         },
  305 |         'PUT host_ip_addresses/50': () => {
  306 |           hostAddresses = hostAddresses.map((h) =>
  307 |             h.id === 50 ? { ...h, reverse_record_value: 'new.example.test.' } : h
  308 |           );
  309 |           return { host_ip_address: hostAddresses[0], _meta: { action_state_id: 1207 } };
  310 |         },
  311 |         'GET action_states/1202': () => ({ action_state: { id: 1202, finished: true, status: true, current: 1, total: 1 } }),
  312 |         'GET action_states/1203': () => ({ action_state: { id: 1203, finished: true, status: true, current: 1, total: 1 } }),
  313 |         'GET action_states/1204': () => ({ action_state: { id: 1204, finished: true, status: true, current: 1, total: 1 } }),
  314 |         'GET action_states/1205': () => ({ action_state: { id: 1205, finished: true, status: true, current: 1, total: 1 } }),
  315 |         'GET action_states/1206': () => ({ action_state: { id: 1206, finished: true, status: true, current: 1, total: 1 } }),
  316 |         'GET action_states/1207': () => ({ action_state: { id: 1207, finished: true, status: true, current: 1, total: 1 } }),
  317 |       },
  318 |     });
  319 | 
  320 |     await page.goto('/admin/vps/123/network');
  321 |     await expect(page.getByTestId('vps.network.page')).toBeVisible();
  322 |     await page.getByTestId('vps.network.ip_addresses.unassigned.2.assign').click();
  323 |     await expect(page.getByTestId('vps.network.ip_addresses.add_modal')).toBeVisible();
  324 |     await expect(page.getByTestId('network.user.assign.interface')).toHaveValue('1');
  325 |     await expect(page.getByTestId('network.user.assign.kind')).toHaveValue('ipv4_public');
  326 |     await page.getByTestId('network.user.assign.continue').click();
  327 |     await expect(page.getByTestId('network.user.assign.address')).toHaveValue('2');
  328 |     await expect(page.getByTestId('network.user.assign.mode')).toHaveValue('route');
  329 | 
  330 |     const assignReq = page.waitForRequest(
  331 |       (r) => r.method() === 'POST' && r.url().includes('/api/v7.0/ip_addresses/2/assign')
  332 |     );
  333 |     await page.getByTestId('network.user.assign.submit').click();
  334 |     expect((await assignReq).postDataJSON()).toEqual({
  335 |       ip_address: {
  336 |         network_interface: 1,
  337 |       },
  338 |     });
  339 |     await expect(page.getByTestId('vps.network.ip_addresses.add_modal')).toBeHidden();
  340 | 
  341 |     await page.getByTestId('vps.network.host_addresses.row.51.assign').click();
  342 |     const hostAssignDialog = page.getByTestId('vps.network.host_addresses.assign');
  343 |     await expect(hostAssignDialog).toContainText('198.51.100.11');
  344 |     await expect(hostAssignDialog.getByTestId('vps.network.host_addresses.assign.target')).toContainText('vps123.example');
  345 |     await expect(hostAssignDialog.getByTestId('vps.network.host_addresses.assign.target')).toContainText('#123');
  346 |     await expect(hostAssignDialog.getByTestId('vps.network.host_addresses.assign.interface')).toContainText('eth0');
  347 |     await expect(hostAssignDialog.getByRole('combobox')).toHaveCount(0);
  348 | 
  349 |     const assignHostReq = page.waitForRequest(
  350 |       (r) => r.method() === 'POST' && r.url().includes('/api/v7.0/host_ip_addresses/51/assign')
  351 |     );
  352 |     await page.getByTestId('vps.network.host_addresses.assign.submit').click();
> 353 |     expect((await assignHostReq).postDataJSON()).toEqual({});
      |                                                  ^ Error: expect(received).toEqual(expected) // deep equality
  354 |     await expect(hostAssignDialog).toBeHidden();
  355 |     expect(hostAssignmentRequests).toEqual(['read', 'assign']);
  356 | 
  357 |     await page.getByTestId('vps.network.host_addresses.row.50.ptr').click();
  358 |     await page.getByTestId('vps.network.host_addresses.ptr.value').fill('new.example.test.');
  359 | 
  360 |     const ptrReq = page.waitForRequest(
  361 |       (r) => r.method() === 'PUT' && r.url().includes('/api/v7.0/host_ip_addresses/50')
  362 |     );
  363 |     await page.getByTestId('vps.network.host_addresses.ptr.submit').click();
  364 |     expect((await ptrReq).postDataJSON()).toEqual({
  365 |       host_ip_address: {
  366 |         reverse_record_value: 'new.example.test.',
  367 |       },
  368 |     });
  369 | 
  370 |     await page.getByTestId('vps.network.host_addresses.row.50.free').click();
  371 |     await expect(page.getByTestId('vps.network.host_addresses.free_confirm')).toBeVisible();
  372 |     const freeHostReq = page.waitForRequest(
  373 |       (r) => r.method() === 'POST' && r.url().includes('/api/v7.0/host_ip_addresses/50/free')
  374 |     );
  375 |     await page.getByTestId('vps.network.host_addresses.free_confirm.confirm').click();
  376 |     expect((await freeHostReq).postData()).toBe('{}');
  377 | 
  378 |     await page.getByTestId('vps.network.ip_addresses.item.1.owner').click();
  379 |     await page.getByTestId('vps.network.ip_addresses.owner.user').fill('77');
  380 |     await page.getByTestId('vps.network.ip_addresses.owner.environment').selectOption('3');
  381 |     const ownerReq = page.waitForRequest(
  382 |       (r) => r.method() === 'PUT' && r.url().includes('/api/v7.0/ip_addresses/1')
  383 |     );
  384 |     await page.getByTestId('vps.network.ip_addresses.owner.submit').click();
  385 |     expect((await ownerReq).postDataJSON()).toEqual({
  386 |       ip_address: {
  387 |         user: 77,
  388 |         environment: 3,
  389 |       },
  390 |     });
  391 | 
  392 |     await page.getByTestId('vps.network.ip_addresses.item.1.free_route').click();
  393 |     await expect(page.getByTestId('vps.network.ip_addresses.free_route_confirm')).toBeVisible();
  394 |     const freeRouteReq = page.waitForRequest(
  395 |       (r) => r.method() === 'POST' && r.url().includes('/api/v7.0/ip_addresses/1/free')
  396 |     );
  397 |     await page.getByTestId('vps.network.ip_addresses.free_route_confirm.confirm').click();
  398 |     expect((await freeRouteReq).postData()).toBe('{}');
  399 |   });
  400 | 
  401 |   test('busy VPS transaction gates networking mutations with an explanation', async ({ page }) => {
  402 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  403 | 
  404 |     await installHaveApiMock(page, {
  405 |       user: { id: 1, login: 'admin', level: 90 },
  406 |       handlers: {
  407 |         'GET vpses/123': () => ({ vps }),
  408 |         'GET ip_addresses': () => ({ ip_addresses: ips }),
  409 |         'GET network_interfaces': () => ({ network_interfaces: netifs }),
  410 |         'GET network_interface_accountings': () => ({ network_interface_accountings: acct }),
  411 |         'GET host_ip_addresses': () => ({
  412 |           host_ip_addresses: [
  413 |             {
  414 |               id: 50,
  415 |               addr: '198.51.100.10',
  416 |               assigned: true,
  417 |               reverse_record_value: 'old.example.test.',
  418 |               user_created: true,
  419 |               ip_address: { id: 1, addr: '198.51.100.10' },
  420 |             },
  421 |             {
  422 |               id: 51,
  423 |               addr: '198.51.100.11',
  424 |               assigned: false,
  425 |               user_created: true,
  426 |               ip_address: { id: 1, addr: '198.51.100.10' },
  427 |             },
  428 |           ],
  429 |         }),
  430 |         'GET environments': () => ({ environments: [{ id: 3, label: 'env-test' }] }),
  431 |         'GET transaction_chains': (ctx) => {
  432 |           const cls = ctx.searchParams.get('transaction_chain[class_name]');
  433 |           const rowId = ctx.searchParams.get('transaction_chain[row_id]');
  434 | 
  435 |           if (cls === 'Vps' && rowId === '123') {
  436 |             return {
  437 |               transaction_chains: [
  438 |                 {
  439 |                   id: 919,
  440 |                   state: 'running',
  441 |                   name: 'Vps#123 network operation',
  442 |                   progress: 0,
  443 |                   size: 1,
  444 |                 },
  445 |               ],
  446 |             };
  447 |           }
  448 | 
  449 |           return { transaction_chains: [] };
  450 |         },
  451 |         'PUT ip_addresses/1': () => {
  452 |           throw new Error('owner update should be blocked by busy gate');
  453 |         },
```