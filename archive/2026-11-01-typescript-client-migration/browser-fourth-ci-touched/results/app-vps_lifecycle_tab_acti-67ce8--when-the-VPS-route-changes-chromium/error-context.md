# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/vps_lifecycle_tab_actions.spec.ts >> @pr-smoke VPS lifecycle tab >> resets configuration review and lifetime editor when the VPS route changes
- Location: e2e/specs/app/vps_lifecycle_tab_actions.spec.ts:215:3

# Error details

```
Error: locator.fill: Test ended.
Call log:
  - waiting for getByRole('textbox', { name: /^Hostname / })

```

# Test source

```ts
  124 | test.describe('@pr-smoke VPS lifecycle tab', () => {
  125 |   test('retries a resource allocation failure only after an admin explicitly enables override', async ({ page }) => {
  126 |     let updateCalls = 0;
  127 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  128 |     await installLifecycleMock(page, {
  129 |       updateVps: () => ++updateCalls === 1
  130 |         ? failEnvelope('Resource allocation error: no Memory left')
  131 |         : { vps, _meta: { action_state_id: 506 } },
  132 |     });
  133 |     await page.goto('/admin/vps/123/config');
  134 |     await expect(page.getByTestId('vps.config.admin_override')).toBeVisible();
  135 |     await expect(page.getByTestId('vps.config.admin_override')).not.toBeChecked();
  136 |     await page.getByRole('spinbutton', { name: /^Memory/ }).fill('8192');
  137 |     await page.getByTestId('vps.config.header.save').click();
  138 |     const dialog = page.getByTestId('vps.config.confirm');
  139 |     const first = page.waitForRequest(r => r.method() === 'PUT' && r.url().includes('/vpses/123'));
  140 |     await dialog.getByTestId('vps.config.confirm.confirm').click();
  141 |     expect((await first).postDataJSON()).toEqual({ vps: { memory: 8192 } });
  142 |     await expect(dialog.getByTestId('vps.config.confirm.error')).toContainText('no Memory left');
  143 |     await expect(dialog.getByTestId('vps.config.confirm.admin_override')).not.toBeChecked();
  144 |     await dialog.getByTestId('vps.config.confirm.admin_override').check();
  145 |     await expect(dialog.getByTestId('vps.config.confirm.error')).toHaveCount(0);
  146 |     expect(updateCalls).toBe(1);
  147 |     await page.screenshot({ path: test.info().outputPath('resource-review.png') });
  148 |     const retry = page.waitForRequest(r => r.method() === 'PUT' && r.url().includes('/vpses/123'));
  149 |     await dialog.getByTestId('vps.config.confirm.confirm').click();
  150 |     expect((await retry).postDataJSON()).toEqual({ vps: { memory: 8192, admin_override: true } });
  151 |     await expect(dialog).toBeHidden();
  152 |     await expect(page.getByTestId('vps.config.admin_override')).not.toBeChecked();
  153 |   });
  154 | 
  155 |   test('does not expose resource override to a member', async ({ page }) => {
  156 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  157 |     await installLifecycleMock(page, { user: { id: 7, login: 'owner', level: 1 } });
  158 |     await page.goto('/app/vps/123/config');
  159 |     await page.getByRole('spinbutton', { name: /^Memory/ }).fill('4096');
  160 |     await expect(page.getByTestId('vps.config.admin_override')).toHaveCount(0);
  161 |     await page.getByTestId('vps.config.header.save').click();
  162 |     const dialog = page.getByTestId('vps.config.confirm');
  163 |     await expect(dialog).toBeVisible();
  164 |     await expect(dialog.getByTestId('vps.config.confirm.admin_override')).toHaveCount(0);
  165 |     const request = page.waitForRequest(r => r.method() === 'PUT' && r.url().includes('/vpses/123'));
  166 |     await dialog.getByTestId('vps.config.confirm.confirm').click();
  167 |     expect((await request).postDataJSON()).toEqual({ vps: { memory: 4096 } });
  168 |   });
  169 | 
  170 |   test('@pr-smoke-mobile keeps rejected VPS configuration saves inside the review dialog and allows retry', async ({ page }) => {
  171 |     let updateCalls = 0;
  172 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  173 |     await installLifecycleMock(page, {
  174 |       updateVps: () => {
  175 |         updateCalls += 1;
  176 |         if (updateCalls === 1) {
  177 |           return {
  178 |             status: 409,
  179 |             contentType: 'application/json',
  180 |             body: JSON.stringify({
  181 |               status: false,
  182 |               message: 'VPS configuration changed on the server. Review and retry.',
  183 |               response: null,
  184 |             }),
  185 |           };
  186 |         }
  187 |         return { vps, _meta: { action_state_id: 506 } };
  188 |       },
  189 |     });
  190 | 
  191 |     await page.goto('/admin/vps/123/config');
  192 |     await page.getByRole('textbox', { name: /^Hostname / }).fill('retry-config.example');
  193 |     await page.getByTestId('vps.config.header.save').click();
  194 | 
  195 |     const dialog = page.getByTestId('vps.config.confirm');
  196 |     await expect(dialog).toBeVisible();
  197 |     await dialog.getByTestId('vps.config.confirm.confirm').click();
  198 |     await expect.poll(() => updateCalls).toBe(1);
  199 |     await expect(dialog.getByTestId('vps.config.confirm.error')).toContainText(
  200 |       'VPS configuration changed on the server. Review and retry.',
  201 |     );
  202 |     await expect(dialog).toBeVisible();
  203 | 
  204 |     await dialog.getByTestId('vps.config.confirm.cancel').click();
  205 |     await expect(dialog).toBeHidden();
  206 |     await page.getByTestId('vps.config.header.save').click();
  207 |     await expect(dialog).toBeVisible();
  208 |     await expect(dialog.getByTestId('vps.config.confirm.error')).toHaveCount(0);
  209 | 
  210 |     await dialog.getByTestId('vps.config.confirm.confirm').click();
  211 |     await expect.poll(() => updateCalls).toBe(2);
  212 |     await expect(dialog).toBeHidden();
  213 |   });
  214 | 
  215 |   test('resets configuration review and lifetime editor when the VPS route changes', async ({ page }) => {
  216 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  217 |     await installLifecycleMock(page);
  218 |     const navigate = (path: string) => page.evaluate((nextPath) => {
  219 |       window.history.pushState({}, '', nextPath);
  220 |       window.dispatchEvent(new PopStateEvent('popstate'));
  221 |     }, path);
  222 | 
  223 |     await page.goto('/admin/vps/123/config');
> 224 |     await page.getByRole('textbox', { name: /^Hostname / }).fill('draft-for-vps-a.example');
      |                                                             ^ Error: locator.fill: Test ended.
  225 |     await page.getByTestId('vps.config.header.save').click();
  226 |     await expect(page.getByText('Review and apply VPS configuration changes?')).toBeVisible();
  227 |     await navigate('/admin/vps/321/config');
  228 |     await expect(page.getByText('Review and apply VPS configuration changes?')).toHaveCount(0);
  229 |     await expect(page.getByRole('textbox', { name: /^Hostname / })).toHaveValue('vps123-playground');
  230 | 
  231 |     await navigate('/admin/vps/123/lifecycle/lifetime');
  232 |     await page.getByTestId('lifetimes.admin.edit').click();
  233 |     await expect(page.getByTestId('lifetimes.admin.modal')).toBeVisible();
  234 |     await page.getByTestId('lifetimes.admin.reason').fill('draft reason for VPS A');
  235 |     await navigate('/admin/vps/321/lifecycle/lifetime');
  236 |     await expect(page.getByTestId('lifetimes.admin.modal')).toHaveCount(0);
  237 |   });
  238 | 
  239 |   test('posts legacy rescue boot payload', async ({ page }) => {
  240 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  241 |     await installLifecycleMock(page);
  242 | 
  243 |     await page.goto('/admin/vps/123/lifecycle/boot');
  244 | 
  245 |     await expect(page.getByTestId('vps.lifecycle.page')).toBeVisible();
  246 |     await expect(page.getByTestId('vps.lifecycle.boot')).toBeVisible();
  247 | 
  248 |     await page.getByTestId('vps.lifecycle.boot.os_template').selectOption('7');
  249 |     await page.getByTestId('vps.lifecycle.boot.mountpoint').fill('/mnt/rescue-root');
  250 |     await expect(page.getByTestId('vps.lifecycle.boot.confirm').locator('input')).toHaveCount(0);
  251 | 
  252 |     const reqPromise = page.waitForRequest(
  253 |       (r) => r.method() === 'POST' && r.url().includes('/api/v7.0/vpses/123/boot')
  254 |     );
  255 | 
  256 |     await page.getByTestId('vps.lifecycle.boot.submit').click();
  257 |     await page.getByTestId('vps.lifecycle.boot.submit.confirm_dialog.confirm').click();
  258 | 
  259 |     const req = await reqPromise;
  260 |     expect(req.postDataJSON()).toEqual({
  261 |       vps: {
  262 |         os_template: 7,
  263 |         mount_root_dataset: '/mnt/rescue-root',
  264 |       },
  265 |     });
  266 |   });
  267 | 
  268 |   test('@workflow-matrix admin sees lifecycle controls reserved for admin mode', async ({ page }) => {
  269 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  270 |     await installLifecycleMock(page);
  271 | 
  272 |     await page.goto('/admin/vps/123/lifecycle');
  273 | 
  274 |     await expect(page.getByTestId('vps.lifecycle.action_index')).toBeVisible();
  275 |     await expect(page.getByTestId('vps.lifecycle.daily_actions')).toBeVisible();
  276 |     await expect(page.getByTestId('vps.lifecycle.admin_actions')).toBeVisible();
  277 |     await expect(page.getByTestId('vps.lifecycle.action_link.start')).toBeVisible();
  278 |     await expect(page.getByTestId('vps.lifecycle.action_link.stop')).toBeVisible();
  279 |     await expect(page.getByTestId('vps.lifecycle.action_link.restart')).toBeVisible();
  280 |     await expect(page.getByTestId('vps.lifecycle.action_link.clone')).toBeVisible();
  281 |     await expect(page.getByTestId('vps.lifecycle.action_link.swap')).toBeVisible();
  282 |     await expect(page.getByTestId('vps.lifecycle.action_link.delete')).toBeVisible();
  283 |     await expect(page.getByTestId('vps.lifecycle.action_link.lifetime')).toBeVisible();
  284 |     await expect(page.getByTestId('vps.lifecycle.action_link.replace')).toBeVisible();
  285 |     await expect(page.getByTestId('vps.lifecycle.action_link.migrate')).toBeVisible();
  286 |     await page.getByTestId('vps.lifecycle.action_link.migrate').click();
  287 |     await expect(page).toHaveURL(/\/admin\/vps\/123\/lifecycle\/migrate$/);
  288 |     await expect(page.getByTestId('vps.lifecycle.migrate')).toBeVisible();
  289 |   });
  290 | 
  291 |   test('@workflow-matrix focused lifecycle start action posts start endpoint', async ({ page }) => {
  292 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  293 |     await installLifecycleMock(page);
  294 | 
  295 |     await page.goto('/admin/vps/123/lifecycle/start');
  296 | 
  297 |     await expect(page.getByTestId('vps.lifecycle.start')).toBeVisible();
  298 |     await expect(page.getByTestId('vps.lifecycle.start.current_state')).toContainText('Stopped');
  299 |     await page.getByTestId('vps.lifecycle.start.confirm').check();
  300 | 
  301 |     const reqPromise = page.waitForRequest(
  302 |       (r) => r.method() === 'POST' && r.url().includes('/api/v7.0/vpses/123/start')
  303 |     );
  304 | 
  305 |     await page.getByTestId('vps.lifecycle.start.submit').click();
  306 | 
  307 |     const req = await reqPromise;
  308 |     expect(req.postDataJSON()).toEqual({});
  309 | 
  310 |     await expect(page.getByTestId('modal.action_progress')).toBeVisible();
  311 |     await page.getByTestId('modal.action_progress.open_tasks').click();
  312 |     await expect(page.getByTestId('tasks.drawer')).toHaveAttribute('aria-modal', 'false');
  313 |     await expect(
  314 |       page.getByTestId('tasks.row.503').getByRole('button', { name: 'Start', exact: true }),
  315 |     ).toBeVisible();
  316 |     await expect(page.getByTestId('vps.lifecycle.page')).toBeVisible();
  317 |   });
  318 | 
  319 |   test('@pr-smoke @pr-smoke-mobile refreshes delayed runtime state after a lifecycle power action', async ({ page }) => {
  320 |     let vpsReads = 0;
  321 |     await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  322 |     await installHaveApiMock(page, {
  323 |       user: { id: 1, login: 'admin', level: 99 },
  324 |       handlers: {
```