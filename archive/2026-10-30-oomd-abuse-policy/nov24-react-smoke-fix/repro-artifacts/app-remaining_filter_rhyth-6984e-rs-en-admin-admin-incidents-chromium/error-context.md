# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/remaining_filter_rhythm.spec.ts >> @pr-smoke @pr-smoke-mobile remaining filters en admin /admin/incidents
- Location: e2e/specs/app/remaining_filter_rhythm.spec.ts:314:5

# Error details

```
Error: expect(received).toBe(expected) // Object.is equality

Expected: 44
Received: 36
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
          - 'button "Account: admin" [ref=e21]':
            - generic [ref=e22]: admin
            - generic [ref=e23]: All
            - generic [ref=e24]: Admin
            - img [ref=e25]
        - navigation [ref=e27]:
          - link "Dashboard" [ref=e30] [cursor=pointer]:
            - /url: /admin
            - img [ref=e32]
            - generic [ref=e37]: Dashboard
          - region "Services" [ref=e38]:
            - generic [ref=e39]: Services
            - generic [ref=e40]:
              - link "VPS" [ref=e41] [cursor=pointer]:
                - /url: /admin/vps
                - img [ref=e43]
                - generic [ref=e46]: VPS
              - link "Datasets" [ref=e47] [cursor=pointer]:
                - /url: /admin/datasets
                - img [ref=e49]
                - generic [ref=e53]: Datasets
              - link "NAS" [ref=e54] [cursor=pointer]:
                - /url: /admin/nas
                - img [ref=e56]
                - generic [ref=e58]: NAS
              - link "Exports" [ref=e59] [cursor=pointer]:
                - /url: /admin/exports
                - img [ref=e61]
                - generic [ref=e64]: Exports
              - link "DNS" [ref=e65] [cursor=pointer]:
                - /url: /admin/dns
                - img [ref=e67]
                - generic [ref=e70]: DNS
              - link "Networking" [ref=e71] [cursor=pointer]:
                - /url: /admin/networking/ip-addresses
                - img [ref=e73]
                - generic [ref=e78]: Networking
          - region "Operations" [ref=e79]:
            - generic [ref=e80]: Operations
            - generic [ref=e81]:
              - link "Transactions" [ref=e82] [cursor=pointer]:
                - /url: /admin/transactions
                - img [ref=e84]
                - generic [ref=e87]: Transactions
              - link "Monitoring" [ref=e88] [cursor=pointer]:
                - /url: /admin/monitoring
                - img [ref=e90]
                - generic [ref=e92]: Monitoring
              - link "Incidents" [ref=e93] [cursor=pointer]:
                - /url: /admin/incidents/overview
                - img [ref=e95]
                - generic [ref=e97]: Incidents
              - link "Out-of-memory" [ref=e98] [cursor=pointer]:
                - /url: /admin/oom-reports
                - img [ref=e100]
                - generic [ref=e102]: Out-of-memory
              - link "Audit" [ref=e103] [cursor=pointer]:
                - /url: /admin/audit
                - img [ref=e105]
                - generic [ref=e108]: Audit
          - region "Users and finance" [ref=e109]:
            - generic [ref=e110]: Users and finance
            - generic [ref=e111]:
              - link "Users" [ref=e112] [cursor=pointer]:
                - /url: /admin/users
                - img [ref=e114]
                - generic [ref=e119]: Users
              - link "User namespaces" [ref=e120] [cursor=pointer]:
                - /url: /admin/user-namespaces/namespaces
                - img [ref=e122]
                - generic [ref=e126]: User namespaces
              - link "Requests" [ref=e127] [cursor=pointer]:
                - /url: /admin/requests
                - img [ref=e129]
                - generic [ref=e132]: Requests
              - link "Finance" [ref=e133] [cursor=pointer]:
                - /url: /admin/payments/incoming
                - img [ref=e135]
                - generic [ref=e137]: Finance
          - region "Infrastructure" [ref=e138]:
            - generic [ref=e139]: Infrastructure
            - generic [ref=e140]:
              - link "Cluster" [ref=e141] [cursor=pointer]:
                - /url: /admin/cluster/summary
                - img [ref=e143]
                - generic [ref=e153]: Cluster
              - link "Nodes" [ref=e154] [cursor=pointer]:
                - /url: /admin/nodes
                - img [ref=e156]
                - generic [ref=e159]: Nodes
              - link "Migration plans" [ref=e160] [cursor=pointer]:
                - /url: /admin/migration-plans
                - img [ref=e162]
                - generic [ref=e166]: Migration plans
              - link "Admin" [ref=e167] [cursor=pointer]:
                - /url: /admin/admin-info
                - img [ref=e169]
                - generic [ref=e171]: Admin
          - region "Content" [ref=e172]:
            - generic [ref=e173]: Content
            - generic [ref=e174]:
              - link "Mailer" [ref=e175] [cursor=pointer]:
                - /url: /admin/mailer/templates
                - img [ref=e177]
                - generic [ref=e180]: Mailer
              - link "News and help" [ref=e181] [cursor=pointer]:
                - /url: /admin/content/news
                - img [ref=e183]
                - generic [ref=e186]: News and help
          - generic [ref=e188]:
            - link "Outages" [ref=e189] [cursor=pointer]:
              - /url: /admin/outages
              - img [ref=e191]
              - generic [ref=e193]: Outages
            - link "Security advisories" [ref=e194] [cursor=pointer]:
              - /url: /admin/security-advisories
              - img [ref=e196]
              - generic [ref=e198]: Security advisories
        - generic [ref=e200]:
          - img [ref=e201]
          - generic [ref=e203]: vpsAdmin
        - generic [ref=e205]:
          - link "About" [ref=e206] [cursor=pointer]:
            - /url: /about
          - link "View commit 6c6792a62d5b" [ref=e207] [cursor=pointer]:
            - /url: https://github.com/vpsfreecz/vpsadmin-webui/commit/6c6792a62d5bb1193b1ce96c0d6ff9167341de49
            - text: 6c6792a62d5b
    - main [ref=e210]:
      - generic [ref=e213]:
        - generic [ref=e214]:
          - generic [ref=e215]:
            - generic [ref=e216]:
              - heading "Incident reports" [level=1] [ref=e218]
              - paragraph [ref=e219]: Incident reports related to VPS.
            - link "New report" [ref=e221] [cursor=pointer]:
              - /url: /admin/incidents/new?returnTo=%2Fadmin%2Fincidents%3Fpage%3D1%26limit%3D50
          - generic [ref=e222]:
            - link "Overview" [ref=e223] [cursor=pointer]:
              - /url: /admin/incidents/overview
            - link "Reports" [ref=e224] [cursor=pointer]:
              - /url: /admin/incidents?page=1&limit=50
            - link "History" [ref=e225] [cursor=pointer]:
              - /url: /admin/incidents/history
        - generic [ref=e226]:
          - generic [ref=e227]:
            - generic [ref=e228]:
              - combobox "Open an incident by ID or filter incident reports" [ref=e229]
              - button "Help" [ref=e231]:
                - img [ref=e232]
            - status [ref=e235]
          - button "Advanced filters" [ref=e236]:
            - img [ref=e237]
          - generic [ref=e238]:
            - combobox "Policy" [disabled] [ref=e239]:
              - option "All policies" [selected]
            - generic [ref=e242]: Incidents unavailable
          - button "Copy link" [ref=e243]
        - generic [ref=e246]: No incident reports
```

# Test source

```ts
  272 |   'monitored_events',
  273 |   'network_interface_accountings',
  274 |   'network_interface_monitors',
  275 |   'network_interfaces',
  276 |   'networks',
  277 |   'news_logs',
  278 |   'node_kernel_evidences',
  279 |   'nodes',
  280 |   'object_histories',
  281 |   'oom_report_rules',
  282 |   'oom_reports',
  283 |   'os_families',
  284 |   'os_templates',
  285 |   'outage_security_advisories',
  286 |   'outage_updates',
  287 |   'outages',
  288 |   'pools',
  289 |   'security_advisories',
  290 |   'security_advisory_cves',
  291 |   'security_advisory_updates',
  292 |   'snapshot_downloads',
  293 |   'system_configs',
  294 |   'transaction_chains',
  295 |   'transactions',
  296 |   'user_cluster_resource_packages',
  297 |   'user_namespace_maps',
  298 |   'user_namespaces',
  299 |   'user_outages',
  300 |   'user_payments',
  301 |   'user_security_advisories',
  302 |   'user_sessions',
  303 |   'users',
  304 |   'vps_outages',
  305 |   'vps_security_advisories',
  306 |   'vps_user_data',
  307 |   'vpses',
  308 | ];
  309 | for (const [language, theme] of [
  310 |   ['cs', 'dark'],
  311 |   ['en', 'light'],
  312 | ] as const) {
  313 |   for (const item of cases)
  314 |     test(`@pr-smoke @pr-smoke-mobile remaining filters ${language} ${item.mode} ${item.route}`, async ({
  315 |       page,
  316 |     }, info) => {
  317 |       const mobile = info.project.name.startsWith('mobile');
  318 |       const baseline = process.env['CAPTURE_SIDE']?.startsWith('baseline') ?? false;
  319 |       await page.setViewportSize(mobile ? { width: 390, height: 844 } : { width: 1440, height: 1000 });
  320 |       await bootstrapVpsAdminWindow(page);
  321 |       await setUiSettingsLocalStorage(page, { language, theme });
  322 |       const errors: string[] = [],
  323 |         writes: string[] = [];
  324 |       page.on('pageerror', (e) => errors.push(String(e)));
  325 |       page.on('request', (r) => {
  326 |         if (['POST', 'PUT', 'PATCH', 'DELETE'].includes(r.method()))
  327 |           writes.push(r.method() + ' ' + new URL(r.url()).pathname);
  328 |       });
  329 |       const handlers: Record<string, HaveApiHandler> = Object.fromEntries(
  330 |         endpoints.map((name) => ['GET ' + name, () => ({ [name]: [] })])
  331 |       );
  332 |       handlers['GET users/42'] = () => ({
  333 |         user: {
  334 |           id: 42,
  335 |           login: 'audit-member',
  336 |           level: 1,
  337 |           full_name: 'Kontrolní účet s dlouhým českým jménem',
  338 |           object_state: 'active',
  339 |         },
  340 |       });
  341 |       await installHaveApiMock(page, {
  342 |         user: { id: 90, login: item.mode, level: item.mode === 'member' ? 1 : item.mode === 'support' ? 30 : 100 },
  343 |         handlers,
  344 |       });
  345 |       await page.goto(item.route + '?q=' + encodeURIComponent('Ověření rozměrů s dlouhým českým názvem a diakritikou'));
  346 |       const bar = item.barTestId
  347 |         ? page.getByTestId(item.barTestId)
  348 |         : page
  349 |             .locator('div.flex.w-full.flex-wrap.items-end.gap-2')
  350 |             .filter({ has: page.locator('input,select') })
  351 |             .first();
  352 |       await expect(bar).toBeVisible();
  353 |       const geometry = await bar.evaluate((root) =>
  354 |         Array.from(root.querySelectorAll('input,select,button,a'))
  355 |           .filter((el) => !!(el as HTMLElement).offsetParent)
  356 |           .map((el) => ({
  357 |             tag: el.tagName,
  358 |             id: el.getAttribute('data-testid'),
  359 |             height: el.getBoundingClientRect().height,
  360 |             width: el.getBoundingClientRect().width,
  361 |             type: el.getAttribute('type'),
  362 |             secondaryChip: !!el.closest('span.inline-flex.text-xs'),
  363 |           }))
  364 |       );
  365 |       const fields = geometry.filter(
  366 |         (c) => ['INPUT', 'SELECT'].includes(c.tag) && !['checkbox', 'radio', 'hidden'].includes(c.type ?? '')
  367 |       );
  368 |       const controls = geometry.filter((c) => ['BUTTON', 'A'].includes(c.tag) && c.height > 20 && !c.secondaryChip);
  369 |       expect(controls.length).toBeGreaterThan(0);
  370 |       const reference = mobile ? 44 : item.referenceHeight;
  371 |       for (const field of fields) {
> 372 |         expect(Math.round(field.height)).toBe(reference);
      |                                          ^ Error: expect(received).toBe(expected) // Object.is equality
  373 |         if (!baseline && item.referenceHeight === 44) expect(field.width).toBeGreaterThanOrEqual(160);
  374 |       }
  375 |       const nativeHelp = /\/(Environments|Locations)Page\.tsx$/.test(item.file);
  376 |       if (baseline && !mobile) expect(controls.some((c) => Math.round(c.height) !== reference)).toBe(true);
  377 |       else if (baseline && nativeHelp) {
  378 |         expect(controls.filter((c) => Math.round(c.height) === 32)).toHaveLength(1);
  379 |         for (const control of controls) expect([32, 44]).toContain(Math.round(control.height));
  380 |       } else
  381 |         for (const control of controls) {
  382 |           expect(Math.round(control.height), control.id ?? control.tag).toBe(reference);
  383 |           expect(control.width).toBeGreaterThanOrEqual(reference);
  384 |         }
  385 |       const overflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth);
  386 |       expect(overflow).toBe(false);
  387 |       await bar.screenshot({ path: info.outputPath('filter.png'), scale: 'css' });
  388 |       await writeFile(
  389 |         info.outputPath('geometry.json'),
  390 |         JSON.stringify({ ...item, language, theme, project: info.project.name, baseline, geometry }, null, 2)
  391 |       );
  392 |       if (item.helpId || nativeHelp) {
  393 |         const help = item.helpId
  394 |           ? page.getByTestId(item.helpId)
  395 |           : bar.locator('input').first().locator('..').getByRole('button');
  396 |         await help.focus();
  397 |         await page.keyboard.press('Enter');
  398 |         await expect(page.getByRole('dialog')).toBeVisible();
  399 |         await page.keyboard.press('Escape');
  400 |         await expect(help).toBeFocused();
  401 |       }
  402 |       if (mobile) {
  403 |         await page.setViewportSize({ width: 320, height: 750 });
  404 |         await page.evaluate(
  405 |           () => new Promise((resolve) => requestAnimationFrame(() => requestAnimationFrame(resolve)))
  406 |         );
  407 |         const narrow = await page.evaluate(() => ({
  408 |           width: innerWidth,
  409 |           document: document.documentElement.scrollWidth,
  410 |           body: document.body.scrollWidth,
  411 |         }));
  412 |         await writeFile(info.outputPath('narrow.json'), JSON.stringify({ ...item, language, narrow }, null, 2));
  413 |         if (['/admin/cluster/system-config', '/admin/users/42/history'].includes(item.route))
  414 |           await page.screenshot({ path: info.outputPath('narrow.png'), scale: 'css' });
  415 |         if (!baseline) expect(Math.max(narrow.document, narrow.body)).toBeLessThanOrEqual(narrow.width);
  416 |       }
  417 |       expect(errors).toEqual([]);
  418 |       expect(
  419 |         writes.filter((w) => !/^PUT \/api\/v7\.0\/webui_user_settings\/(ui|ui_setting)\/settings$/.test(w))
  420 |       ).toEqual([]);
  421 |     });
  422 | }
  423 | 
```