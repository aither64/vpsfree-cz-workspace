# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/user_requests_smoke.spec.ts >> user requests: independent ID spaces paginate the complete merged history without skips
- Location: e2e/specs/app/user_requests_smoke.spec.ts:326:1

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: getByTestId('app.requests.row.change.2')
Expected: visible
Timeout: 15000ms
Error: element(s) not found

Call log:
  - Expect "toBeVisible" with timeout 15000ms
  - waiting for getByTestId('app.requests.row.change.2')

```

```yaml
- heading "Can’t load your session" [level=1]
- paragraph: vpsAdmin could not verify your login state. This is usually a network issue or a temporary backend error.
- paragraph: "ApiOutputError: Invalid users#current response"
- button "Reload"
- link "Try signing in":
  - /url: http://127.0.0.1:5187/oauth/login?next=%2Fapp%2Frequests
- link "Go to status":
  - /url: /
```

# Test source

```ts
  289 |     user: { id: 10, login: 'alice', level: 1 },
  290 |     handlers: {
  291 |       'GET user_request/registrations': () => ({ registrations: [] }),
  292 |       'GET user_request/changes': () => ({
  293 |         changes: [{
  294 |           id: 66,
  295 |           user: { id: 99, login: 'mallory' },
  296 |           state: 'awaiting',
  297 |           change_reason: 'FOREIGN SECRET REASON',
  298 |           address: 'FOREIGN SECRET ADDRESS',
  299 |         }],
  300 |       }),
  301 |       'GET user_request/changes/66': () => ({
  302 |         change: {
  303 |           id: 66,
  304 |           state: 'awaiting',
  305 |           change_reason: 'OWNERLESS SECRET REASON',
  306 |           address: 'OWNERLESS SECRET ADDRESS',
  307 |         },
  308 |       }),
  309 |     },
  310 |   });
  311 | 
  312 |   await page.goto('/app/requests');
  313 |   await expect(page.getByRole('heading', { name: 'Moje žádosti' })).toBeVisible();
  314 |   await expect(page.getByTestId('app.requests.error')).toBeVisible();
  315 |   await expect(page.getByText('FOREIGN SECRET REASON')).toHaveCount(0);
  316 |   await expect(page.getByText('FOREIGN SECRET ADDRESS')).toHaveCount(0);
  317 |   await expect(page.getByText('mallory')).toHaveCount(0);
  318 | 
  319 |   await page.goto('/app/requests/change/66');
  320 |   await expect(page.getByTestId('app.requests.detail.error')).toBeVisible();
  321 |   await expect(page.getByText('OWNERLESS SECRET REASON')).toHaveCount(0);
  322 |   await expect(page.getByText('OWNERLESS SECRET ADDRESS')).toHaveCount(0);
  323 |   await expect(page.getByText('Tuto žádost nelze otevřít')).toBeVisible();
  324 | });
  325 | 
  326 | test('user requests: independent ID spaces paginate the complete merged history without skips', async ({ page, isMobile }) => {
  327 |   const indexUrls: URL[] = [];
  328 |   await setUiSettingsLocalStorage(page, { language: 'en' });
  329 |   await bootstrapVpsAdminWindow(page);
  330 |   await installHaveApiMock(page, {
  331 |     user: { id: '10', login: 'alice', level: 1 } as any,
  332 |     handlers: {
  333 |       'GET user_request/registrations': ({ url }) => {
  334 |         const requestUrl = new URL(url);
  335 |         indexUrls.push(requestUrl);
  336 |         const fromId = Number(requestUrl.searchParams.get('registration[from_id]')) || null;
  337 |         const limit = Number(requestUrl.searchParams.get('registration[limit]')) || 25;
  338 |         const all = Array.from({ length: 30 }, (_, index) => {
  339 |           const id = 130 - index;
  340 |           return {
  341 |             id,
  342 |             user: { id: 10 },
  343 |             state: 'awaiting',
  344 |             login: `registration-${id}`,
  345 |             created_at: new Date(Date.UTC(2026, 7, 1, 0, id - 100)).toISOString(),
  346 |           };
  347 |         });
  348 |         return {
  349 |           registrations: all
  350 |             .filter((request) => fromId === null || request.id < fromId)
  351 |             .slice(0, limit),
  352 |           _meta: { total_count: all.length },
  353 |         };
  354 |       },
  355 |       'GET user_request/changes': ({ url }) => {
  356 |         const requestUrl = new URL(url);
  357 |         indexUrls.push(requestUrl);
  358 |         const fromId = Number(requestUrl.searchParams.get('change[from_id]')) || null;
  359 |         const limit = Number(requestUrl.searchParams.get('change[limit]')) || 25;
  360 |         const all = [
  361 |           {
  362 |             id: 2,
  363 |             user: { id: '10' },
  364 |             state: 'awaiting',
  365 |             change_reason: 'newest change',
  366 |             created_at: '2026-08-01T00:31:00.000Z',
  367 |           },
  368 |           {
  369 |             id: 1,
  370 |             user: { id: '10' },
  371 |             state: 'awaiting',
  372 |             change_reason: 'oldest change',
  373 |             created_at: '2026-08-01T00:00:00.000Z',
  374 |           },
  375 |         ];
  376 |         return {
  377 |           changes: all
  378 |             .filter((request) => fromId === null || request.id < fromId)
  379 |             .slice(0, limit),
  380 |           _meta: { total_count: all.length },
  381 |         };
  382 |       },
  383 |     },
  384 |   });
  385 | 
  386 |   await page.goto('/app/requests');
  387 |   const rowPrefix = isMobile ? 'app.requests.mobile.row' : 'app.requests.row';
  388 |   const paginationPrefix = isMobile ? 'app.requests.pagination.mobile' : 'app.requests.pagination.desktop';
> 389 |   await expect(page.getByTestId(`${rowPrefix}.change.2`)).toBeVisible();
      |                                                           ^ Error: expect(locator).toBeVisible() failed
  390 |   await expect(page.getByTestId(`${rowPrefix}.registration.130`)).toBeVisible();
  391 |   await expect(page.getByTestId(`${rowPrefix}.registration.107`)).toBeVisible();
  392 |   await expect(page.getByTestId(`${rowPrefix}.registration.106`)).toHaveCount(0);
  393 |   await expect(page.getByTestId(paginationPrefix)).toContainText('Page 1');
  394 |   await expect(page.getByTestId(`${paginationPrefix}.page.2`)).toBeVisible();
  395 | 
  396 |   await page.getByTestId(`${paginationPrefix}.next`).click();
  397 |   await expect(page).toHaveURL(/page=2/);
  398 |   await expect(page).toHaveURL(/registration_from_id=107/);
  399 |   await expect(page).toHaveURL(/change_from_id=2/);
  400 |   await expect(page.getByTestId(`${rowPrefix}.registration.106`)).toBeVisible();
  401 |   await expect(page.getByTestId(`${rowPrefix}.registration.101`)).toBeVisible();
  402 |   await expect(page.getByTestId(`${rowPrefix}.change.1`)).toBeVisible();
  403 |   await expect(page.getByTestId(`${rowPrefix}.change.2`)).toHaveCount(0);
  404 |   await expect(page.getByTestId(`${paginationPrefix}.prev`)).toBeEnabled();
  405 | 
  406 |   expect(indexUrls).toHaveLength(4);
  407 |   const registrationUrls = indexUrls.filter((url) => url.pathname.endsWith('/user_request/registrations'));
  408 |   const changeUrls = indexUrls.filter((url) => url.pathname.endsWith('/user_request/changes'));
  409 |   expect(registrationUrls).toHaveLength(2);
  410 |   expect(changeUrls).toHaveLength(2);
  411 |   expect(registrationUrls[0]?.searchParams.has('registration[from_id]')).toBe(false);
  412 |   expect(changeUrls[0]?.searchParams.has('change[from_id]')).toBe(false);
  413 |   expect(registrationUrls[1]?.searchParams.get('registration[from_id]')).toBe('107');
  414 |   expect(changeUrls[1]?.searchParams.get('change[from_id]')).toBe('2');
  415 |   expect(indexUrls.every((url) => url.searchParams.get('_meta[count]') === 'true')).toBe(true);
  416 | });
  417 | 
```