# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: admin/network_availability.spec.ts >> @pr-smoke @pr-smoke-mobile suggestion timeout preserves shared discovery, retry and manual filtering (en)
- Location: e2e/specs/admin/network_availability.spec.ts:182:3

# Error details

```
Error: expect(received).toBe(expected) // Object.is equality

Expected: 1
Received: 0

Call Log:
- Timeout 15000ms exceeded while waiting on the predicate
```

# Page snapshot

```yaml
- generic [ref=e6]: Loading…
```

# Test source

```ts
  150 |     const modalLayer = await editor.evaluate((node) => {
  151 |       for (let parent = node.parentElement; parent; parent = parent.parentElement) {
  152 |         if (getComputedStyle(parent).position === 'fixed') return Number(getComputedStyle(parent).zIndex);
  153 |       }
  154 |       throw new Error('Editor has no fixed modal layer');
  155 |     });
  156 |     expect(await editorTooltip.evaluate((node) => Number(getComputedStyle(node).zIndex))).toBeGreaterThan(modalLayer);
  157 |     await page.screenshot({ path: testInfo.outputPath(`network-editor-counts-${language}.png`), fullPage: true });
  158 |     await expect(toggle).toBeVisible();
  159 |     await expect(toggle).toBeChecked();
  160 |     expect(capabilityMethods).toEqual(['PUT']);
  161 |     await expect(editor).toContainText(language === 'en' ? 'Existing service continues' : 'Stávající provoz pokračuje');
  162 |     await toggle.uncheck();
  163 |     // Captures show the implemented UI with synthetic API fixtures.
  164 |     await page.screenshot({ path: testInfo.outputPath(`network-availability-${language}.png`), fullPage: true });
  165 |     await page.getByTestId('admin.cluster.networks.editor.save').click();
  166 |     await expect(editor).toContainText('Allocation policy rejected');
  167 |     await expect(toggle).not.toBeChecked();
  168 |     await page.getByTestId('admin.cluster.networks.editor.save').click();
  169 |     await expect(editor).toBeHidden();
  170 |     await expect(page.locator('#network-editor-owned')).toHaveCount(0);
  171 |     await expect(page.getByTestId('admin.cluster.networks.row.101.enabled')).toHaveText(language === 'en' ? 'Disabled' : 'Zakázáno');
  172 |     await page.getByTestId('admin.cluster.networks.row.101.edit').click();
  173 |     await toggle.check();
  174 |     await page.getByTestId('admin.cluster.networks.editor.save').click();
  175 |     await expect(editor).toBeHidden();
  176 |     await expect(page.getByTestId('admin.cluster.networks.row.101.enabled')).toHaveText(language === 'en' ? 'Enabled' : 'Povoleno');
  177 |     expect(writes).toEqual([false, false, true]);
  178 |   });
  179 | }
  180 | 
  181 | for (const language of ['en', 'cs'] as const) {
  182 |   test(`@pr-smoke @pr-smoke-mobile suggestion timeout preserves shared discovery, retry and manual filtering (${language})`, async ({ page }, testInfo) => {
  183 |     const now = new Date('2026-10-09T12:00:00Z');
  184 |     await page.clock.install({ time: now });
  185 |     await page.clock.pauseAt(now);
  186 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  187 |     await setUiSettingsLocalStorage(page, { language });
  188 |     let releaseMetadata!: () => void;
  189 |     let releasePriority!: () => void;
  190 |     const metadataGate = new Promise<void>((resolve) => { releaseMetadata = resolve; });
  191 |     const priorityGate = new Promise<void>((resolve) => { releasePriority = resolve; });
  192 |     let capabilityCalls = 0;
  193 |     const suggestions: Array<{ location: number; role: string | null; version: string | null }> = [];
  194 |     const locations = [
  195 |       { id: 10, label: 'Praha', environment: { id: 1, label: 'Production' } },
  196 |       { id: 20, label: 'Brno', environment: { id: 1, label: 'Production' } },
  197 |       { id: 30, label: 'Playground', environment: { id: 2, label: 'Playground' } },
  198 |     ];
  199 |     const address = (id: number, location: number) => ({
  200 |       id, addr: `192.0.2.${location + 1}`, prefix: 32, user: null, network_interface: null,
  201 |       network: { id: 100 + location, address: '192.0.2.0', prefix: 24, enabled: true,
  202 |         ip_version: 4, role: 'public_access', purpose: 'vps',
  203 |         primary_location: locations.find((item) => item.id === location) },
  204 |     });
  205 |     let manualCalls = 0;
  206 |     let priorityFinished = false;
  207 |     await installHaveApiMock(page, {
  208 |       user: { id: 1, login: 'admin', level: 100 },
  209 |       handlers: {
  210 |         'GET locations': () => ({ locations }),
  211 |         'OPTIONS ip_addresses': async (ctx) => {
  212 |           expect(ctx.method).toBe('OPTIONS');
  213 |           expect(ctx.searchParams.get('method')).toBe('GET');
  214 |           capabilityCalls += 1;
  215 |           await metadataGate;
  216 |           return {
  217 |             method: 'GET', scope: 'ip_address#index',
  218 |             input: { namespace: 'ip_address', layout: 'object', parameters: { network_enabled: { type: 'Boolean' } } },
  219 |             output: { namespace: 'ip_addresses', layout: 'array', parameters: {} },
  220 |           };
  221 |         },
  222 |         'GET ip_addresses': async (ctx) => {
  223 |           const param = (name: string) => ctx.searchParams.get(`ip_address[${name}]`);
  224 |           if (param('addr')) {
  225 |             expect(param('addr')).toBe('192.0.2.99');
  226 |             manualCalls += 1;
  227 |             return { ip_addresses: [{ ...address(999, 10), addr: '192.0.2.99' }] };
  228 |           }
  229 |           expect(param('network_enabled')).toBe('true');
  230 |           expect(param('limit')).toBe('50');
  231 |           expect(param('assigned_to_interface')).toBe('false');
  232 |           const location = Number(param('location'));
  233 |           const role = param('role');
  234 |           const version = param('version');
  235 |           suggestions.push({ location, role, version });
  236 |           if (location === 10 && role === 'public_access') {
  237 |             await priorityGate;
  238 |             priorityFinished = true;
  239 |           }
  240 |           return { ip_addresses: role === 'public_access' && version === '4' ? [address(location * 10 + 1, location)] : [] };
  241 |         },
  242 |       },
  243 |     });
  244 |     const visible = (id: number) => page.locator(`[data-testid="admin.ip_addresses.row.${id}"]:visible, [data-testid="admin.ip_addresses.card.${id}"]:visible`);
  245 |     const rows = page.locator('tr[data-testid^="admin.ip_addresses.row."]:visible, div[data-testid^="admin.ip_addresses.card."]:visible');
  246 |     const partial = page.getByTestId('admin.ip_addresses.suggested.partial_error');
  247 |     const progress = page.getByTestId('admin.ip_addresses.suggested.loading');
  248 |     try {
  249 |       await page.goto('/admin/ip-addresses');
> 250 |       await expect.poll(() => capabilityCalls).toBe(1);
      |                                                ^ Error: expect(received).toBe(expected) // Object.is equality
  251 |       await expect(page.getByTestId('admin.ip_addresses.loading')).toBeVisible();
  252 |       expect(suggestions).toEqual([]);
  253 |       await page.clock.runFor(12_001);
  254 |       expect(suggestions).toEqual([]); // Timed-out Prague/Brno callers cannot start GET later.
  255 |       releaseMetadata();
  256 |       await expect.poll(async () => { await page.clock.runFor(50); return suggestions.length; }).toBe(3);
  257 |       expect(suggestions.every((request) => request.location === 30)).toBe(true);
  258 |       await expect.poll(async () => { await page.clock.runFor(50); return visible(301).isVisible(); }).toBe(true);
  259 |       await expect(visible(301)).toContainText('192.0.2.31');
  260 |       await expect(partial).toBeVisible();
  261 |       await expect.poll(async () => { await page.clock.runFor(50); return progress.isVisible(); }).toBe(false);
  262 |       await expect(progress).toBeHidden();
  263 |       expect(capabilityCalls).toBe(1);
  264 |       await page.screenshot({ path: testInfo.outputPath(`ip-suggestions-timeout-${language}.png`), fullPage: true });
  265 | 
  266 |       await page.getByTestId('admin.ip_addresses.suggested.retry').click();
  267 |       await expect.poll(async () => { await page.clock.runFor(50); return suggestions.length; }).toBe(9);
  268 |       await expect.poll(async () => { await page.clock.runFor(50); return visible(201).isVisible(); }).toBe(true);
  269 |       await expect(visible(201)).toContainText('192.0.2.21');
  270 |       await expect(progress).toBeVisible();
  271 |       expect(capabilityCalls).toBe(1); // Retry uses the late successful shared metadata.
  272 |       const search = page.getByTestId('admin.ip_addresses.smart_filter.input');
  273 |       await search.fill('addr:192.0.2.99');
  274 |       await search.press('Enter');
  275 |       await expect.poll(async () => { await page.clock.runFor(50); return manualCalls; }).toBe(1);
  276 |       await expect.poll(async () => { await page.clock.runFor(50); return visible(999).isVisible(); }).toBe(true);
  277 |       await expect(visible(999)).toContainText('192.0.2.99');
  278 |       const lateResponse = page.waitForResponse((response) => {
  279 |         const url = new URL(response.url());
  280 |         return response.request().method() === 'GET' && url.pathname.endsWith('/ip_addresses')
  281 |           && url.searchParams.get('ip_address[location]') === '10'
  282 |           && url.searchParams.get('ip_address[role]') === 'public_access';
  283 |       });
  284 |       releasePriority();
  285 |       await lateResponse;
  286 |       await expect.poll(async () => { await page.clock.runFor(50); return priorityFinished; }).toBe(true);
  287 |       await expect(rows).toHaveCount(1);
  288 |       await expect(visible(999)).toBeVisible();
  289 |       await expect(visible(101)).toHaveCount(0);
  290 |       await expect(page).toHaveURL(/addr=192\.0\.2\.99/);
  291 |       await page.screenshot({ path: testInfo.outputPath(`ip-suggestions-manual-${language}.png`), fullPage: true });
  292 | 
  293 |       await page.getByTestId('admin.ip_addresses.chip.addr').getByRole('button').click();
  294 |       await expect.poll(async () => { await page.clock.runFor(50); return visible(101).isVisible(); }).toBe(true);
  295 |       for (const id of [101, 201, 301]) await expect(visible(id)).toBeVisible();
  296 |       await expect(rows).toHaveCount(3);
  297 |       await expect(partial).toBeHidden();
  298 |       await expect.poll(async () => { await page.clock.runFor(50); return progress.isVisible(); }).toBe(false);
  299 |       await expect(progress).toBeHidden();
  300 |       expect(capabilityCalls).toBe(1);
  301 |       expect(suggestions).toHaveLength(9);
  302 |       await page.screenshot({ path: testInfo.outputPath(`ip-suggestions-recovered-${language}.png`), fullPage: true });
  303 |     } finally {
  304 |       releaseMetadata();
  305 |       releasePriority();
  306 |     }
  307 |   });
  308 | }
  309 | 
  310 | test('@pr-smoke @pr-smoke-mobile older APIs keep unknown state and omit unsupported availability fields', async ({ page }) => {
  311 |   await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  312 |   await setUiSettingsLocalStorage(page, { language: 'en' });
  313 |   let saved = false;
  314 |   const capabilityMethods: string[] = [];
  315 |   const network = { id: 101, address: '192.0.2.0', prefix: 24, ip_version: 4, role: 'public_access',
  316 |     purpose: 'vps', managed: true, split_access: 'no_access', split_prefix: 32,
  317 |     size: 256, used: 9, taken: 7, owned: 5 };
  318 |   await installHaveApiMock(page, {
  319 |     user: { id: 1, login: 'admin', level: 100 },
  320 |     handlers: {
  321 |       'GET locations': () => ({ locations: [] }),
  322 |       'GET networks': () => ({ networks: [network] }),
  323 |       'OPTIONS networks/101': (ctx) => {
  324 |         expect(ctx.method).toBe('OPTIONS');
  325 |         expect(ctx.searchParams.get('method')).toBe('PUT');
  326 |         capabilityMethods.push(ctx.searchParams.get('method') ?? '');
  327 |         return {
  328 |           method: 'PUT', scope: 'network#update',
  329 |           input: { namespace: 'network', layout: 'object', parameters: { managed: { type: 'Boolean' } } },
  330 |           output: { namespace: 'network', layout: 'object', parameters: {} },
  331 |         };
  332 |       },
  333 |       'PUT networks/101': (ctx) => {
  334 |         expect((ctx.reqJson as { network: object }).network).not.toHaveProperty('enabled');
  335 |         saved = true;
  336 |         return { network };
  337 |       },
  338 |     },
  339 |   });
  340 |   await page.goto('/admin/cluster/networks');
  341 |   await expect(page.getByTestId('admin.cluster.networks.row.101.enabled')).not.toHaveText('Disabled');
  342 |   await expect(page.getByTestId('admin.cluster.networks.row.101.available_to_users')).toHaveText('—');
  343 |   await expect(page.getByTestId('admin.cluster.networks.row.101.owned_unassigned')).toHaveText('—');
  344 |   await page.getByTestId('admin.cluster.networks.row.101.edit').click();
  345 |   await expect(page.getByTestId('admin.cluster.networks.editor.label')).toBeVisible();
  346 |   await expect.poll(() => capabilityMethods).toEqual(['PUT']);
  347 |   await expect(page.getByTestId('admin.cluster.networks.editor.enabled')).toHaveCount(0);
  348 |   await page.getByTestId('admin.cluster.networks.editor.save').click();
  349 |   await expect(page.getByTestId('admin.cluster.networks.editor')).toBeHidden();
  350 |   expect(saved).toBe(true);
```