# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/payments_page.spec.ts >> @pr-smoke @pr-smoke-mobile user payments copy sanitized localized text with a touch-safe mobile target
- Location: e2e/specs/app/payments_page.spec.ts:236:1

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: getByTestId('payments.my.instructions.text').getByRole('heading', { name: 'Platba v CZK' })
Expected: visible
Error: element(s) not found

Call log:
  - Expect "toBeVisible" with timeout 15000ms
  - waiting for getByTestId('payments.my.instructions.text').getByRole('heading', { name: 'Platba v CZK' })

```

# Test source

```ts
  199 |             <tr><td>Message (<a href="#">more info</a>):</td><td>/VS/53</td></tr>
  200 |             <tr><td>Sum:</td><td>300 CZK per month</td></tr>
  201 |             <tr><td>Bank account overview:</td><td><a href="https://example.test">https://example.test</a></td></tr>
  202 |           </table>
  203 |         `,
  204 |       },
  205 |     };
  206 |   });
  207 | 
  208 |   haveApiMock.addHandler('GET user_payments', () => {
  209 |     return {
  210 |       status: true,
  211 |       response: {
  212 |         user_payments: [],
  213 |       },
  214 |     };
  215 |   });
  216 | 
  217 |   await page.goto(withAppUrl('/app/payments'));
  218 | 
  219 |   const instructions = page.getByTestId('payments.my.instructions.text');
  220 |   await expect(instructions.getByRole('heading', { name: 'Obecné informace' })).toBeVisible();
  221 |   await expect(instructions.getByRole('heading', { name: 'Platba v CZK' })).toBeVisible();
  222 |   await expect(instructions.getByText('Bankovní účet pro CZK (CZ):')).toBeVisible();
  223 |   await expect(instructions.getByText('Variabilní symbol:')).toBeVisible();
  224 |   await expect(instructions.getByText('300 CZK měsíčně')).toBeVisible();
  225 |   await expect(instructions).not.toContainText('Payment in CZK');
  226 |   await expect(instructions).not.toContainText('Variable symbol:');
  227 | 
  228 |   const qr = instructions.locator('img').first();
  229 |   await expect(qr).toBeVisible();
  230 |   await expect.poll(() => qr.evaluate((image: HTMLImageElement) => image.complete && image.naturalWidth > 0)).toBe(true);
  231 |   const qrBox = await qr.boundingBox();
  232 |   expect(qrBox?.width).toBeLessThanOrEqual(160);
  233 |   expect(qrBox?.height).toBeLessThanOrEqual(160);
  234 | });
  235 | 
  236 | test('@pr-smoke @pr-smoke-mobile user payments copy sanitized localized text with a touch-safe mobile target', async ({ page, isMobile }) => {
  237 |   test.setTimeout(90_000);
  238 |   await page.setViewportSize(isMobile ? { width: 390, height: 844 } : { width: 1440, height: 1000 });
  239 | 
  240 |   await page.addInitScript(({ storageKey }) => {
  241 |     window.localStorage.setItem(
  242 |       storageKey,
  243 |       JSON.stringify({
  244 |         sidebarCollapsed: false,
  245 |         theme: 'system',
  246 |         language: 'cs',
  247 |         tips: { sidebarTimeZone: 'visible' },
  248 |       })
  249 |     );
  250 |   }, { storageKey: UI_SETTINGS_STORAGE_KEY });
  251 |   await bootstrapVpsAdminWindow(page);
  252 |   await page.addInitScript(() => {
  253 |     const writes: string[] = [];
  254 |     Object.assign(window, { __paymentInstructionsClipboardWrites: writes });
  255 |     Object.defineProperty(navigator, 'clipboard', {
  256 |       configurable: true,
  257 |       value: {
  258 |         writeText: async (text: string) => {
  259 |           writes.push(text);
  260 |         },
  261 |       },
  262 |     });
  263 |   });
  264 | 
  265 |   const haveApiMock = await installHaveApiMock(page);
  266 |   const mutationRequests: Array<{ method: string; url: string }> = [];
  267 |   page.on('request', (request) => {
  268 |     if (['POST', 'PUT', 'PATCH', 'DELETE'].includes(request.method())) {
  269 |       mutationRequests.push({ method: request.method(), url: request.url() });
  270 |     }
  271 |   });
  272 |   haveApiMock.addHandler('GET users/current', () => ({
  273 |     user: {
  274 |       id: 53,
  275 |       login: 'kerry',
  276 |       level: 1,
  277 |       monthly_payment: 300,
  278 |       paid_until: '2099-01-01T00:00:00Z',
  279 |     },
  280 |   }));
  281 |   haveApiMock.addHandler('GET users/53/get_payment_instructions', () => ({
  282 |     user: {
  283 |       instructions: `
  284 |       <h3 onclick="bad()">Payment in CZK</h3>
  285 |       <p>Payments can be made either in CZK or EUR, see below for bank account numbers.</p>
  286 |       <table>
  287 |         <tr><td>Variable symbol:</td><td><strong>53</strong></td></tr>
  288 |         <tr><td>Sum:</td><td>300 CZK per month</td></tr>
  289 |       </table>
  290 |       <script>window.PWNED = true</script>
  291 |     `,
  292 |     },
  293 |   }));
  294 |   haveApiMock.addHandler('GET user_payments', () => ({ user_payments: [] }));
  295 | 
  296 |   await page.goto(withAppUrl('/app/payments'));
  297 | 
  298 |   const instructions = page.getByTestId('payments.my.instructions.text');
> 299 |   await expect(instructions.getByRole('heading', { name: 'Platba v CZK' })).toBeVisible();
      |                                                                             ^ Error: expect(locator).toBeVisible() failed
  300 |   await expect(instructions).not.toContainText('PWNED');
  301 |   expect(await page.evaluate(() => (window as Window & { PWNED?: boolean }).PWNED)).toBeUndefined();
  302 | 
  303 |   const copy = page.getByTestId('payments.my.instructions.copy');
  304 |   await expect(copy).toBeVisible();
  305 |   const copyBox = await copy.boundingBox();
  306 |   expect(copyBox).not.toBeNull();
  307 |   if (isMobile) {
  308 |     expect(copyBox!.height).toBeGreaterThanOrEqual(44);
  309 |     expect(copyBox!.width).toBeGreaterThanOrEqual(44);
  310 |   } else {
  311 |     expect(copyBox!.height).toBeGreaterThanOrEqual(30);
  312 |     expect(copyBox!.height).toBeLessThanOrEqual(40);
  313 |   }
  314 |   await copy.click();
  315 | 
  316 |   const clipboardWrites = await page.evaluate(() => (
  317 |     window as Window & { __paymentInstructionsClipboardWrites?: string[] }
  318 |   ).__paymentInstructionsClipboardWrites ?? []);
  319 |   expect(clipboardWrites).toEqual([[
  320 |     'Platba v CZK',
  321 |     'Platbu můžeš provést v CZK nebo EUR. Čísla účtů najdeš níže.',
  322 |     'Variabilní symbol: 53',
  323 |     'Částka: 300 CZK měsíčně',
  324 |   ].join('\n')]);
  325 |   expect(clipboardWrites[0]).not.toContain('<');
  326 |   expect(clipboardWrites[0]).not.toContain('PWNED');
  327 |   expect(clipboardWrites[0]).not.toContain('Payment in CZK');
  328 |   // The app shell may persist UI settings while the route opens. Any other
  329 |   // same-origin or external write would make this read-only scenario fail.
  330 |   const appOrigin = new URL(page.url()).origin;
  331 |   expect(mutationRequests.filter(({ method, url }) => {
  332 |     const target = new URL(url);
  333 |     return !(
  334 |       method === 'PUT'
  335 |       && target.origin === appOrigin
  336 |       && target.pathname === '/api/v7.0/webui_user_settings/ui/settings'
  337 |       && target.search === ''
  338 |       && target.hash === ''
  339 |     );
  340 |   })).toEqual([]);
  341 | });
  342 | 
```