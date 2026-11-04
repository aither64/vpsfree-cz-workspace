# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: admin/requests_operations_smoke.spec.ts >> @workflow-matrix @smoke admin requests: correction uses the canonical detail and registration bulk approval is blocked
- Location: e2e/specs/admin/requests_operations_smoke.spec.ts:717:1

# Error details

```
Test timeout of 90000ms exceeded.
```

```
Error: locator.uncheck: Test timeout of 90000ms exceeded.
Call log:
  - waiting for getByTestId('admin.requests.review.continue')
    - locator resolved to <input checked type="checkbox" class="h-4 w-4 rounded border-border" data-testid="admin.requests.review.continue"/>
  - attempting click action
    - waiting for element to be visible, enabled and stable
    - element is visible, enabled and stable
    - scrolling into view if needed
    - done scrolling
    - <div>…</div> from <div class="fixed inset-0 z-50 flex items-center justify-center p-0 sm:p-4">…</div> subtree intercepts pointer events
  - retrying click action
    - waiting for element to be visible, enabled and stable
    - element is visible, enabled and stable
    - scrolling into view if needed
    - done scrolling
    - <div aria-hidden="true" data-overlay-backdrop="true" class="absolute inset-0 bg-backdrop/45"></div> from <div class="fixed inset-0 z-50 flex items-center justify-center p-0 sm:p-4">…</div> subtree intercepts pointer events
  - retrying click action
    - waiting 20ms
    2 × waiting for element to be visible, enabled and stable
      - element is visible, enabled and stable
      - scrolling into view if needed
      - done scrolling
      - <div>…</div> from <div class="fixed inset-0 z-50 flex items-center justify-center p-0 sm:p-4">…</div> subtree intercepts pointer events
    - retrying click action
      - waiting 100ms
    40 × waiting for element to be visible, enabled and stable
       - element is visible, enabled and stable
       - scrolling into view if needed
       - done scrolling
       - <div>…</div> from <div class="fixed inset-0 z-50 flex items-center justify-center p-0 sm:p-4">…</div> subtree intercepts pointer events
     - retrying click action
       - waiting 500ms
       - waiting for element to be visible, enabled and stable
       - element is visible, enabled and stable
       - scrolling into view if needed
       - done scrolling
       - <div aria-hidden="true" data-overlay-backdrop="true" class="absolute inset-0 bg-backdrop/45"></div> from <div class="fixed inset-0 z-50 flex items-center justify-center p-0 sm:p-4">…</div> subtree intercepts pointer events
     - retrying click action
       - waiting 500ms
       - waiting for element to be visible, enabled and stable
       - element is visible, enabled and stable
       - scrolling into view if needed
       - done scrolling
       - <div>…</div> from <div class="fixed inset-0 z-50 flex items-center justify-center p-0 sm:p-4">…</div> subtree intercepts pointer events
     - retrying click action
       - waiting 500ms
       - waiting for element to be visible, enabled and stable
       - element is visible, enabled and stable
       - scrolling into view if needed
       - done scrolling
       - <div>…</div> from <div class="fixed inset-0 z-50 flex items-center justify-center p-0 sm:p-4">…</div> subtree intercepts pointer events
     - retrying click action
       - waiting 500ms

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
            - link "View commit c1ad3e253ee7" [ref=e194] [cursor=pointer]:
              - /url: https://github.com/vpsfreecz/vpsadmin-webui/commit/c1ad3e253ee7953fde8c5734cfa8a4d971854614
              - text: c1ad3e253ee7
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
            - generic [ref=e222]:
              - generic [ref=e223]:
                - 'heading "Registration #401" [level=1] [ref=e224]'
                - paragraph [ref=e225]:
                  - generic [ref=e226]:
                    - generic [ref=e228]: Awaiting admin
                    - generic "Fraud score 100" [ref=e229]: High risk 100
              - link "Back" [ref=e231] [cursor=pointer]:
                - /url: /admin/requests?limit=50&page=1
            - generic [ref=e232]:
              - generic [ref=e234]:
                - generic [ref=e236]:
                  - generic [ref=e237]: Applicant details
                  - generic [ref=e238]: Complete data submitted with the registration request.
                - generic [ref=e240]:
                  - generic [ref=e241]:
                    - generic [ref=e242]:
                      - generic [ref=e243]:
                        - term [ref=e244]: Login
                        - definition [ref=e245]: alice
                      - generic [ref=e246]:
                        - term [ref=e247]: Full name
                        - definition [ref=e248]: Alice Example
                      - generic [ref=e249]:
                        - term [ref=e250]: Organisation
                        - definition [ref=e251]: Example Foundation
                      - generic [ref=e252]:
                        - term [ref=e253]: Organisation ID
                        - definition [ref=e254]: CZ12345678
                      - generic [ref=e255]:
                        - term [ref=e256]: Email
                        - definition [ref=e257]: alice@example.test
                      - generic [ref=e258]:
                        - term [ref=e259]: Year of birth
                        - definition [ref=e260]: "1990"
                      - generic [ref=e261]:
                        - term [ref=e262]: How
                        - definition [ref=e263]: Community recommendation
                      - generic [ref=e264]:
                        - term [ref=e265]: Note
                        - definition [ref=e266]: Runs public mirrors
                      - generic [ref=e267]:
                        - term [ref=e268]: OS template
                        - definition [ref=e269]: Debian 13
                      - generic [ref=e270]:
                        - term [ref=e271]: Location
                        - definition [ref=e272]: Prague
                      - generic [ref=e273]:
                        - term [ref=e274]: Currency
                        - definition [ref=e275]: CZK
                      - generic [ref=e276]:
                        - term [ref=e277]: Language
                        - definition [ref=e278]: Čeština
                      - generic [ref=e279]:
                        - term [ref=e280]: Time zone
                        - definition [ref=e281]: Europe/Prague
                    - generic [ref=e283]:
                      - term [ref=e284]: Address
                      - definition [ref=e285]:
                        - generic [ref=e286]:
                          - iframe [ref=e287]:
                            - generic [ref=f1e2]:
                              - generic:
                                - region "Map" [ref=f1e3]
                                - button "Map marker" [ref=f1e4]:
                                  - img [ref=f1e5]
                              - generic:
                                - generic [ref=f1e8]:
                                  - button "Zoom In" [ref=f1e9] [cursor=pointer]
                                  - button "Zoom Out" [ref=f1e11] [cursor=pointer]
                                - group [ref=f1e13]:
                                  - generic [ref=f1e14]:
                                    - text: ©
                                    - link "OpenStreetMap contributors" [ref=f1e15] [cursor=pointer]:
                                      - /url: /copyright
                                    - text: ♥️
                                    - link "Make a Donation" [ref=f1e16] [cursor=pointer]:
                                      - /url: https://supporting.openstreetmap.org
                                    - text: .
                                    - link "Website and API terms" [ref=f1e17] [cursor=pointer]:
                                      - /url: https://wiki.osmfoundation.org/wiki/Terms_of_Use
                          - generic [ref=e288]:
                            - generic [ref=e289]:
                              - img [ref=e291]
                              - generic [ref=e294]: Stodolní 138/44, 14400 Ostrava, Česko
                            - generic [ref=e295]:
                              - 'button "Copy applicant address: Stodolní 138/44, 14400 Ostrava, Česko" [ref=e296]': Copy address
                              - 'link "Open address in OpenStreetMap: Stodolní 138/44, 14400 Ostrava, Česko" [ref=e297] [cursor=pointer]':
                                - /url: https://www.openstreetmap.org/search?query=Stodoln%C3%AD+138%2F44%2C+14400+Ostrava%2C+%C4%8Cesko
                                - text: Open in OpenStreetMap
                                - img [ref=e298]
                  - group [ref=e304]:
                    - generic "Technical metadataIP addresses, timestamps, and operational links" [ref=e305] [cursor=pointer]:
                      - img [ref=e306]
                      - generic [ref=e308]: Technical metadataIP addresses, timestamps, and operational links
                    - generic [ref=e309]:
                      - generic [ref=e310]:
                        - generic [ref=e311]:
                          - term [ref=e312]: User
                          - definition [ref=e313]:
                            - link "alice" [ref=e314] [cursor=pointer]:
                              - /url: /admin/users/42
                        - generic [ref=e315]:
                          - term [ref=e316]: Admin
                          - definition [ref=e317]: admin
                        - generic [ref=e318]:
                          - term [ref=e319]: Created
                          - definition [ref=e320]: 3/1/2026, 11:00:00 AM
                        - generic [ref=e321]:
                          - term [ref=e322]: Updated
                          - definition [ref=e323]: 3/1/2026, 12:00:00 PM
                        - generic [ref=e324]:
                          - term [ref=e325]: API IP
                          - definition [ref=e326]: 203.0.113.10
                        - generic [ref=e327]:
                          - term [ref=e328]: Client IP
                          - definition [ref=e329]: 198.51.100.20
                      - generic [ref=e330]:
                        - generic [ref=e331]: Operational links
                        - generic [ref=e332]:
                          - 'link "Action state #77" [ref=e333] [cursor=pointer]':
                            - /url: /admin/action-states/77
                          - link "Open chain" [ref=e334] [cursor=pointer]:
                            - /url: /admin/transactions/88
                          - link "Open transaction" [ref=e335] [cursor=pointer]:
                            - /url: /admin/transactions/items/99
                  - region "Risk checks" [ref=e337]:
                    - generic [ref=e338]:
                      - heading "Risk checks" [level=2] [ref=e339]
                      - paragraph [ref=e340]: Status and key signals first; expand a check for its complete response.
                    - generic [ref=e341]:
                      - generic [ref=e342]:
                        - img [ref=e344]
                        - generic [ref=e346]:
                          - generic [ref=e347]: High-risk registration
                          - generic [ref=e348]: Do not approve before verifying the highlighted IP or email signals.
                      - generic [ref=e349]: "Highest score: 100"
                    - generic [ref=e350]:
                      - generic [ref=e351]:
                        - generic [ref=e353]:
                          - generic [ref=e354]: IP address check
                          - generic [ref=e356]:
                            - generic [ref=e357]: "Fraud score: 87"
                            - generic [ref=e358]: Check completed
                        - generic [ref=e359]:
                          - generic [ref=e360]:
                            - generic [ref=e361]:
                              - term [ref=e362]: Proxy
                              - definition [ref=e363]: "Yes"
                            - generic [ref=e364]:
                              - term [ref=e365]: VPN
                              - definition [ref=e366]: "Yes"
                            - generic [ref=e367]:
                              - term [ref=e368]: Tor
                              - definition [ref=e369]: "No"
                            - generic [ref=e370]:
                              - term [ref=e371]: Recent abuse
                              - definition [ref=e372]: "Yes"
                          - group [ref=e373]:
                            - generic "Show all signals" [ref=e374] [cursor=pointer]
                      - generic [ref=e375]:
                        - generic [ref=e377]:
                          - generic [ref=e378]: Email check
                          - generic [ref=e380]:
                            - generic [ref=e381]: "Fraud score: 100"
                            - generic [ref=e382]: Check failed
                        - generic [ref=e383]:
                          - generic [ref=e384]: Provider timeout
                          - generic [ref=e385]:
                            - generic [ref=e386]:
                              - term [ref=e387]: Valid
                              - definition [ref=e388]: "No"
                            - generic [ref=e389]:
                              - term [ref=e390]: Disposable
                              - definition [ref=e391]: "Yes"
                            - generic [ref=e392]:
                              - term [ref=e393]: Deliverability
                              - definition [ref=e394]: low
                            - generic [ref=e395]:
                              - term [ref=e396]: Recent abuse
                              - definition [ref=e397]: "Yes"
                          - group [ref=e398]:
                            - generic "Show all signals" [ref=e399] [cursor=pointer]
              - complementary [ref=e400]:
                - generic [ref=e401]:
                  - generic [ref=e403]:
                    - generic [ref=e404]: Decision
                    - generic [ref=e405]: Choose one specific action for this request.
                  - generic [ref=e406]:
                    - generic [ref=e407]:
                      - generic [ref=e410]: Awaiting admin
                      - generic [ref=e412] [cursor=pointer]:
                        - checkbox "Automatically open the next request after each decision" [checked] [ref=e413]
                        - generic [ref=e414]: Automatically open the next request after each decision
                    - generic [ref=e415]:
                      - button "Approve" [ref=e416]
                      - button "Deny and notify" [ref=e417]
                      - button "Close without reply" [ref=e418]
                      - button "Request correction" [ref=e419]
  - dialog "Request additional information" [ref=e422]:
    - generic [ref=e424]: Request additional information
    - generic [ref=e425]:
      - generic [ref=e426]: The applicant receives a link to correct the registration data together with your reason.
      - generic [ref=e428]:
        - generic [ref=e429]:
          - generic [ref=e430]: Preset reason
          - combobox "Preset reason" [ref=e431]:
            - option "Custom text / choose a preset" [selected]
            - option "Incomplete address"
            - option "Address cannot be verified"
            - option "Missing or incomplete name"
        - paragraph [ref=e432]: "Message language: Czech. You can edit the text or write your own. It will be sent as shown below; custom text is not translated automatically."
        - generic [ref=e433]:
          - generic [ref=e434]: Reason (required)
          - textbox "Reason (required)" [active] [ref=e435]: Please fix the address
      - group [ref=e436]:
        - generic "Optional overrides" [ref=e437] [cursor=pointer]
        - option "Select…"
        - option "Debian 13" [disabled] [selected]
        - option "Select…"
        - option "Prague" [selected]
        - option "Select…"
        - option "Čeština" [selected]
      - generic [ref=e438]:
        - generic [ref=e439]:
          - generic [ref=e440]: Review before resolving
          - generic [ref=e441]:
            - generic [ref=e442]: Registration
            - generic [ref=e443]: Awaiting admin
        - generic [ref=e444]:
          - generic [ref=e445]:
            - generic [ref=e446]: Target
            - generic [ref=e447]: "#401 · alice"
          - generic [ref=e448]:
            - generic [ref=e449]: Impact
            - generic [ref=e450]: Return the request to the applicant with your reason.
          - generic [ref=e451]:
            - generic [ref=e452]: Submit gates
            - list [ref=e453]:
              - listitem [ref=e454]: Reason required before submit.
          - generic [ref=e455]:
            - generic [ref=e456]: Optional overrides
            - list [ref=e457]:
              - listitem [ref=e458]: "Override login: alice"
              - listitem [ref=e459]: "Override full name: Alice Example"
              - listitem [ref=e460]: "Override organisation: Example Foundation"
              - listitem [ref=e461]: "Override organisation ID: CZ12345678"
              - listitem [ref=e462]: "Override email: alice@example.test"
              - listitem [ref=e463]: "Override address: Stodolní 138/44, 14400 Ostrava, Česko"
              - listitem [ref=e464]: "Override year of birth: 1990"
              - listitem [ref=e465]: "Override registration source: Community recommendation"
              - listitem [ref=e466]: "Override note: Runs public mirrors"
              - listitem [ref=e467]: "Override OS template: 5"
              - listitem [ref=e468]: "Override location: 7"
              - listitem [ref=e469]: "Override currency: czk"
              - listitem [ref=e470]: "Override language: 2"
              - listitem [ref=e471]: "Override time zone: Europe/Prague"
          - generic [ref=e472]:
            - generic [ref=e473]: Response / reason stored with this request
            - generic [ref=e474]: Please fix the address
        - generic [ref=e475]: The action is queued; if the backend returns an action state, it is tracked in the Tasks panel.
    - generic [ref=e478]:
      - button "Cancel" [ref=e479]
      - button "Send correction request" [ref=e480]
```

# Test source

```ts
  650 |   const mapCard = page.getByTestId('admin.requests.detail.registration.address.map');
  651 |   const retry = mapCard.getByTestId('admin.requests.detail.registration.address.map.retry');
  652 | 
  653 |   await expect(retry).toBeVisible();
  654 |   await expect.poll(osm.requestCount).toBe(1);
  655 |   await retry.click();
  656 |   await expect(mapCard.getByTestId('admin.requests.detail.registration.address.map.preview')).toBeVisible();
  657 |   await expect.poll(osm.requestCount).toBe(2);
  658 | });
  659 | 
  660 | test('@workflow-matrix @pr-smoke @smoke admin requests: automatic address map distinguishes an unknown address', async ({
  661 |   page,
  662 | }, testInfo) => {
  663 |   await bootstrapVpsAdminWindow(page);
  664 |   const osm = await installOsmMapMock(page, { empty: true });
  665 | 
  666 |   await installHaveApiMock(page, {
  667 |     user: { id: 1, login: 'admin', level: 100 },
  668 |     handlers: {
  669 |       'GET user_request/registrations/127': () => ({ registration: registration(127) }),
  670 |     },
  671 |   });
  672 | 
  673 |   await page.goto('/admin/requests/registration/127');
  674 |   const mapCard = page.getByTestId('admin.requests.detail.registration.address.map');
  675 | 
  676 |   await expect(mapCard.getByText('The address was not found in OpenStreetMap.')).toBeVisible();
  677 |   await expect(mapCard.getByTestId('admin.requests.detail.registration.address.map.retry')).toHaveCount(0);
  678 |   await expect(mapCard.getByTestId('admin.requests.detail.registration.address.map.preview')).toHaveCount(0);
  679 |   await expect.poll(osm.requestCount).toBe(1);
  680 |   await page.evaluate(() => window.scrollTo(0, 0));
  681 |   await page.screenshot({ path: testInfo.outputPath('request-unknown-address.png'), fullPage: true });
  682 | });
  683 | 
  684 | test('@workflow-matrix @pr-smoke @pr-smoke-mobile @smoke @smoke-mobile admin requests: rejected action error is visible', async ({
  685 |   page,
  686 | }) => {
  687 |   await bootstrapVpsAdminWindow(page);
  688 |   await installOsmMapMock(page);
  689 | 
  690 |   await installHaveApiMock(page, {
  691 |     user: { id: 1, login: 'admin', level: 100 },
  692 |     handlers: {
  693 |       'GET user_request/registrations': () => ({ registrations: [registration(124)] }),
  694 |       'GET user_request/changes': () => ({ changes: [] }),
  695 |       'GET user_request/registrations/124': () => ({ registration: registration(124) }),
  696 |       'GET nodes': () => ({ nodes: [] }),
  697 |       'GET locations': () => ({ locations: [{ id: 7, label: 'Prague' }] }),
  698 |       'GET os_templates': () => ({
  699 |         os_templates: [{ id: 5, label: 'Debian 13', cgroup_version: 'cgroup_v2', enabled: true, supported: true }],
  700 |       }),
  701 |       'POST user_request/registrations/124/resolve': () => failEnvelope('Cannot approve this request'),
  702 |     },
  703 |   });
  704 | 
  705 |   await page.goto('/admin/requests/registration/124');
  706 |   await expect(page.getByTestId('admin.requests.resolve.action.approve')).toBeVisible();
  707 |   await page.getByTestId('admin.requests.resolve.action.approve').click();
  708 |   await expect(page.getByTestId('admin.requests.resolve.modal')).toBeVisible();
  709 |   await page.getByTestId('admin.requests.resolve.submit').click();
  710 |   const error = page.getByTestId('admin.requests.resolve.modal').getByRole('alert');
  711 |   await expect(error).toBeVisible();
  712 |   await expect(error).toContainText('Cannot approve this request');
  713 |   await expect(page.getByTestId('admin.requests.resolve.cancel')).toBeEnabled();
  714 |   await expect(page).toHaveURL('/admin/requests/registration/124');
  715 | });
  716 | 
  717 | test('@workflow-matrix @smoke admin requests: correction uses the canonical detail and registration bulk approval is blocked', async ({
  718 |   page,
  719 | }) => {
  720 |   await bootstrapVpsAdminWindow(page);
  721 | 
  722 |   const resolveBodies: unknown[] = [];
  723 | 
  724 |   await installHaveApiMock(page, {
  725 |     user: { id: 1, login: 'admin', level: 100 },
  726 |     handlers: {
  727 |       'GET user_request/registrations': () => ({ registrations: [registration(401), registration(400)] }),
  728 |       'GET user_request/changes': () => ({ changes: [] }),
  729 |       'GET user_request/registrations/401': () => ({ registration: registration(401) }),
  730 |       'POST user_request/registrations/401/resolve': ({ reqJson }) => {
  731 |         resolveBodies.push(reqJson);
  732 |         return { registration: { ...registration(401), state: 'pending_correction' } };
  733 |       },
  734 |       'POST user_request/registrations/400/resolve': ({ reqJson }) => {
  735 |         resolveBodies.push(reqJson);
  736 |         return { registration: { ...registration(400), state: 'approved' } };
  737 |       },
  738 |     },
  739 |   });
  740 | 
  741 |   await page.goto('/admin/requests');
  742 |   await expect(page.getByTestId('admin.requests.table')).toBeVisible();
  743 | 
  744 |   await page.getByTestId('admin.requests.row.registration.401').getByRole('link', { name: '#401' }).press('Enter');
  745 |   await expect(page).toHaveURL(/\/admin\/requests\/registration\/401\?returnTo=/);
  746 |   await page.getByTestId('admin.requests.resolve.action.request_correction').click();
  747 |   await expect(page.getByTestId('admin.requests.resolve.override.login')).toHaveValue('alice');
  748 |   await expect(page.getByTestId('admin.requests.resolve.override.full_name')).toHaveValue('Alice Example');
  749 |   await page.getByTestId('admin.requests.resolve.reason').fill('Please fix the address');
> 750 |   await page.getByTestId('admin.requests.review.continue').uncheck();
      |                                                            ^ Error: locator.uncheck: Test timeout of 90000ms exceeded.
  751 |   await page.getByTestId('admin.requests.resolve.submit').click();
  752 |   await expect.poll(() => resolveBodies.length).toBe(1);
  753 |   expect(resolveBodies[0]).toEqual({
  754 |     registration: {
  755 |       action: 'request_correction',
  756 |       reason: 'Please fix the address',
  757 |       login: 'alice',
  758 |       full_name: 'Alice Example',
  759 |       org_name: 'Example Foundation',
  760 |       org_id: 'CZ12345678',
  761 |       email: 'alice@example.test',
  762 |       address: 'Stodolní 138/44, 14400 Ostrava, Česko',
  763 |       year_of_birth: 1990,
  764 |       how: 'Community recommendation',
  765 |       note: 'Runs public mirrors',
  766 |       os_template: 5,
  767 |       location: 7,
  768 |       currency: 'czk',
  769 |       language: 2,
  770 |       time_zone: 'Europe/Prague',
  771 |     },
  772 |   });
  773 | 
  774 |   await expect(page.getByTestId('admin.requests.table')).toBeVisible();
  775 |   await expect(page.getByTestId('admin.requests.bulk')).toHaveCount(0);
  776 |   await page.getByTestId('admin.requests.bulk.selection_mode').click();
  777 |   await page.getByTestId('admin.requests.bulk.select.registration.400').check();
  778 |   await expect(page.getByTestId('admin.requests.bulk')).toBeVisible();
  779 |   await expect(page.getByTestId('admin.requests.bulk.registration_approve_blocked')).toBeVisible();
  780 |   await expect(page.getByTestId('admin.requests.bulk.action').locator('option[value="approve"]')).toHaveCount(0);
  781 |   await expect.poll(() => resolveBodies.length).toBe(1);
  782 | });
  783 | 
  784 | test('@workflow-matrix @smoke admin requests: bulk writes require confirmation and failed rows stay selected', async ({
  785 |   page,
  786 | }) => {
  787 |   await bootstrapVpsAdminWindow(page);
  788 | 
  789 |   const resolveBodies: unknown[] = [];
  790 |   let failedCalls = 0;
  791 |   const changes = [402, 401].map((id) => ({
  792 |     id,
  793 |     state: 'awaiting',
  794 |     label: `Change #${id}`,
  795 |     user: { id, login: `user${id}` },
  796 |     change_reason: 'Update profile',
  797 |     created_at: '2026-03-01T09:00:00Z',
  798 |   }));
  799 | 
  800 |   await installHaveApiMock(page, {
  801 |     user: { id: 1, login: 'admin', level: 100 },
  802 |     handlers: {
  803 |       'GET user_request/registrations': () => ({ registrations: [] }),
  804 |       'GET user_request/changes': () => ({ changes }),
  805 |       'GET user_request/changes/402': () => ({ change: changes[0] }),
  806 |       'GET user_request/changes/401': () => ({ change: changes[1] }),
  807 |       'POST user_request/changes/402/resolve': ({ reqJson }) => {
  808 |         resolveBodies.push(reqJson);
  809 |         return { change: { ...changes[0], state: 'ignored' } };
  810 |       },
  811 |       'POST user_request/changes/401/resolve': () => {
  812 |         failedCalls += 1;
  813 |         return failEnvelope('Temporary failure');
  814 |       },
  815 |     },
  816 |   });
  817 | 
  818 |   await page.goto('/admin/requests');
  819 |   await page.getByTestId('admin.requests.bulk.selection_mode').click();
  820 |   await page.getByTestId('admin.requests.bulk.select.change.402').check();
  821 |   await expect(page.getByTestId('admin.requests.bulk.select_all')).toHaveAttribute('aria-checked', 'mixed');
  822 |   await expect(page.getByTestId('admin.requests.bulk.select_all')).toHaveJSProperty('indeterminate', true);
  823 |   await page.getByTestId('admin.requests.bulk.select.change.401').check();
  824 |   await page.getByTestId('admin.requests.bulk.action').selectOption('deny');
  825 |   await expect(page.getByTestId('admin.requests.bulk.apply')).toBeDisabled();
  826 |   await page.getByTestId('admin.requests.bulk.reason').fill('Duplicate request');
  827 |   await page.getByTestId('admin.requests.bulk.apply').click();
  828 | 
  829 |   await expect(page.getByTestId('admin.requests.bulk.confirm')).toBeVisible();
  830 |   await expect(page.getByTestId('admin.requests.bulk.confirm.targets')).toContainText('#402');
  831 |   await expect(page.getByTestId('admin.requests.bulk.confirm.targets')).toContainText('#401');
  832 |   await expect(page.getByTestId('admin.requests.bulk.confirm.reason')).toContainText('Duplicate request');
  833 |   expect(resolveBodies).toEqual([]);
  834 |   expect(failedCalls).toBe(0);
  835 |   await page.getByTestId('admin.requests.bulk.confirm.confirm').click();
  836 | 
  837 |   await expect.poll(() => resolveBodies.length).toBe(1);
  838 |   await expect.poll(() => failedCalls).toBe(1);
  839 |   expect(resolveBodies[0]).toEqual({ change: { action: 'deny', reason: 'Duplicate request' } });
  840 |   await expect(page.getByTestId('admin.requests.bulk.select.change.401')).toBeChecked();
  841 |   await expect(page.getByTestId('admin.requests.bulk.select.change.402')).not.toBeChecked();
  842 | });
  843 | 
  844 | test('@workflow-matrix @smoke admin requests: visible state and type segments keep the list simple', async ({
  845 |   page,
  846 | }) => {
  847 |   await bootstrapVpsAdminWindow(page);
  848 | 
  849 |   await installHaveApiMock(page, {
  850 |     user: { id: 1, login: 'admin', level: 100 },
```