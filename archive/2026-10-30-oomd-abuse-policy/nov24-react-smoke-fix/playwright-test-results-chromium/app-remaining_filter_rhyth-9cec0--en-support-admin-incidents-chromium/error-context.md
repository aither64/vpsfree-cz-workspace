# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/remaining_filter_rhythm.spec.ts >> @pr-smoke @pr-smoke-mobile remaining filters en support /admin/incidents
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
          - 'button "Account: support" [ref=e21]':
            - generic [ref=e22]: support
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
          - link "View commit 477685239cc8" [ref=e201] [cursor=pointer]:
            - /url: https://github.com/vpsfreecz/vpsadmin-webui/commit/477685239cc8f288955b8fcb7f2fd6d262111808
            - text: 477685239cc8
    - main [ref=e204]:
      - generic [ref=e207]:
        - generic [ref=e210]:
          - heading "Incident reports" [level=1] [ref=e212]
          - paragraph [ref=e213]: Incident reports related to VPS.
        - generic [ref=e214]:
          - generic [ref=e215]:
            - generic [ref=e216]:
              - combobox "Open an incident by ID or filter incident reports" [ref=e217]
              - button "Help" [ref=e219]:
                - img [ref=e220]
            - status [ref=e223]
          - button "Advanced filters" [ref=e224]:
            - img [ref=e225]
          - generic [ref=e226]:
            - combobox "Policy" [disabled] [ref=e227]:
              - option "All policies" [selected]
            - generic [ref=e230]: Incidents unavailable
          - button "Copy link" [ref=e231]
        - generic [ref=e234]: No incident reports
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