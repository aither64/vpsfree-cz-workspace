# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/remaining_filter_rhythm.spec.ts >> @pr-smoke @pr-smoke-mobile remaining filters en member /app/incidents
- Location: e2e/specs/app/remaining_filter_rhythm.spec.ts:314:5

# Error details

```
Error: expect(received).toBeGreaterThanOrEqual(expected)

Expected: >= 160
Received:    156.765625
```

# Page snapshot

```yaml
- generic [ref=e2]:
  - link "Skip to main content" [ref=e3]:
    - /url: "#main-content"
  - generic [ref=e6]:
    - banner [ref=e7]:
      - button "Open navigation" [ref=e8]:
        - img [ref=e9]
        - generic [ref=e10]: Navigation
    - main [ref=e11]:
      - generic [ref=e14]:
        - generic [ref=e17]:
          - heading "Incident reports" [level=1] [ref=e19]
          - paragraph [ref=e20]: Incident reports related to VPS.
        - generic [ref=e21]:
          - generic [ref=e22]:
            - generic [ref=e23]:
              - combobox "Open an incident by ID or filter incident reports" [ref=e24]
              - button "Help" [ref=e26]:
                - img [ref=e27]
            - status [ref=e30]
          - button "Advanced filters" [ref=e31]:
            - img [ref=e32]
          - generic [ref=e33]:
            - combobox "Policy" [disabled] [ref=e34]:
              - option "All policies" [selected]
            - generic [ref=e37]: Incidents unavailable
          - button "Copy link" [ref=e38]
        - generic [ref=e41]: No incident reports
```

# Test source

```ts
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
  372 |         expect(Math.round(field.height)).toBe(reference);
> 373 |         if (!baseline && item.referenceHeight === 44) expect(field.width).toBeGreaterThanOrEqual(160);
      |                                                                           ^ Error: expect(received).toBeGreaterThanOrEqual(expected)
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