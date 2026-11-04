# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: admin/ip_assignment_vps_first.spec.ts >> @pr-smoke @pr-smoke-mobile a missing asynchronous receipt blocks replay across reload
- Location: e2e/specs/admin/ip_assignment_vps_first.spec.ts:152:1

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: getByTestId('admin.ip.owner.uncertain')
Expected: visible
Error: element(s) not found

Call log:
  - Expect "toBeVisible" with timeout 15000ms
  - waiting for getByTestId('admin.ip.owner.uncertain')

```

```yaml
- text: Loading…
```

# Test source

```ts
  59  | 
  60  | for (const language of ['cs', 'en'] as const) {
  61  |   test(`@pr-smoke @pr-smoke-mobile ${language} assign icon opens VPS first without an ownership write`, async ({ page, isMobile }, info) => {
  62  |     const state = await fixture(page, language);
  63  |     await page.goto('/admin/networking/ip-addresses');
  64  |     const icon = page.getByTestId(`admin.ip_addresses.${isMobile ? 'card' : 'row'}.100.action.route`);
  65  |     if (isMobile) await icon.tap(); else await icon.click();
  66  |     const dialog = page.getByTestId('admin.ip.route.dialog');
  67  |     await expect(dialog).toBeVisible();
  68  |     await expect(page.getByTestId('admin.ip.route.vps')).toBeFocused();
  69  |     await expect(dialog.getByTestId('admin.ip.owner.user')).toHaveCount(0);
  70  |     await expect(dialog.getByTestId('admin.ip.owner.environment')).toHaveCount(0);
  71  |     await choose(page);
  72  |     await expect(page.getByTestId('admin.ip.route.interface')).toHaveValue('501');
  73  |     await expect(page.getByTestId('admin.ip.route.target')).toContainText('synthetic-member');
  74  |     await expect(page.getByTestId('admin.ip.route.target')).toContainText('Production');
  75  |     await expectNoDocumentHorizontalOverflow(page);
  76  |     await dialog.screenshot({ path: info.outputPath(`vps-first-${language}.png`) });
  77  |     await page.getByTestId('admin.ip.route.submit').click();
  78  |     await expect(dialog).toBeHidden();
  79  |     expect(state.ownerWrites).toBe(0);
  80  |     expect(state.assignments).toEqual([{ path: 'assign', payload: { ip_address: { network_interface: 501 } } }]);
  81  |     await page.reload();
  82  |     await expect(page.getByTestId('admin.ip_address.page')).toBeVisible();
  83  |     await expect(dialog).toBeHidden();
  84  |   });
  85  | }
  86  | 
  87  | test('@pr-smoke @pr-smoke-mobile changing VPS clears the old interface and retains the combined host action', async ({ page }) => {
  88  |   const state = await fixture(page);
  89  |   await open(page); await choose(page);
  90  |   await expect(page.getByTestId('admin.ip.route.interface')).toHaveValue('501');
  91  |   await choose(page, '124');
  92  |   await expect(page.getByTestId('admin.ip.route.interface')).toHaveValue('');
  93  |   await expect(page.getByTestId('admin.ip.route.submit')).toBeDisabled();
  94  |   await page.getByTestId('admin.ip.route.interface').selectOption('503');
  95  |   await page.getByTestId('admin.ip.route.dialog').getByRole('checkbox').check();
  96  |   await page.getByTestId('admin.ip.route.submit').click();
  97  |   await expect(page.getByTestId('admin.ip.route.dialog')).toBeHidden();
  98  |   expect(state.assignments).toEqual([{ path: 'assign_with_host_address', payload: { ip_address: { network_interface: 503 } } }]);
  99  | });
  100 | 
  101 | for (const change of ['owner', 'interface'] as const) {
  102 |   test(`@pr-smoke @pr-smoke-mobile fresh ${change} change blocks assignment before any write`, async ({ page }) => {
  103 |     const state = await fixture(page);
  104 |     await open(page); await choose(page);
  105 |     await expect(page.getByTestId('admin.ip.route.submit')).toBeEnabled();
  106 |     if (change === 'owner') state.staleTarget = true;
  107 |     else state.missingInterface = true;
  108 |     await page.getByTestId('admin.ip.route.submit').click();
  109 |     await expect(page.getByTestId('admin.ip.route.error')).toContainText('changed');
  110 |     expect(state.assignments).toEqual([]);
  111 |     expect(state.ownerWrites).toBe(0);
  112 |   });
  113 | }
  114 | 
  115 | test('@pr-smoke @pr-smoke-mobile a foreign-owned address cannot implicitly change owner during assignment', async ({ page }) => {
  116 |   const state = await fixture(page); state.owner = { id: 9, login: 'other-member' };
  117 |   await open(page); await choose(page);
  118 |   await expect(page.getByTestId('admin.ip.route.dialog')).toContainText('another member');
  119 |   await expect(page.getByTestId('admin.ip.route.submit')).toBeDisabled();
  120 |   expect(state.assignments).toEqual([]);
  121 |   expect(state.ownerWrites).toBe(0);
  122 | });
  123 | 
  124 | test('@pr-smoke @pr-smoke-mobile failed preflight reads are retryable without marking a submitted mutation uncertain', async ({ page }) => {
  125 |   const state = await fixture(page);
  126 |   await open(page); await choose(page);
  127 |   await expect(page.getByTestId('admin.ip.route.submit')).toBeEnabled();
  128 |   state.preflightUnavailable = true;
  129 |   await page.getByTestId('admin.ip.route.submit').click();
  130 |   await expect(page.getByTestId('admin.ip.route.error')).toContainText('Preflight unavailable');
  131 |   await expect(page.getByTestId('admin.ip.route.submit')).toBeEnabled();
  132 |   await expect(page.getByTestId('admin.ip.owner.uncertain')).toHaveCount(0);
  133 |   expect(state.assignments).toHaveLength(0);
  134 |   state.preflightUnavailable = false;
  135 |   await page.getByTestId('admin.ip.route.submit').click();
  136 |   await expect(page.getByTestId('admin.ip.route.dialog')).toBeHidden();
  137 |   expect(state.assignments).toHaveLength(1);
  138 | });
  139 | 
  140 | test('@pr-smoke @pr-smoke-mobile an API rejection keeps VPS context and permits deliberate retry', async ({ page }) => {
  141 |   const state = await fixture(page); state.reject = true;
  142 |   await open(page); await choose(page);
  143 |   await page.getByTestId('admin.ip.route.submit').click();
  144 |   await expect(page.getByTestId('admin.ip.route.error')).toContainText('Address changed');
  145 |   await expect(page.getByTestId('admin.ip.route.interface')).toHaveValue('501');
  146 |   state.reject = false;
  147 |   await page.getByTestId('admin.ip.route.submit').click();
  148 |   await expect(page.getByTestId('admin.ip.route.dialog')).toBeHidden();
  149 |   expect(state.assignments).toHaveLength(2);
  150 | });
  151 | 
  152 | test('@pr-smoke @pr-smoke-mobile a missing asynchronous receipt blocks replay across reload', async ({ page }) => {
  153 |   const state = await fixture(page); state.receipt = false;
  154 |   await open(page); await choose(page);
  155 |   await page.getByTestId('admin.ip.route.submit').click();
  156 |   await expect(page.getByTestId('admin.ip.route.error')).toBeVisible();
  157 |   await expect(page.getByTestId('admin.ip.route.submit')).toBeDisabled();
  158 |   await page.reload();
> 159 |   await expect(page.getByTestId('admin.ip.owner.uncertain')).toBeVisible();
      |                                                              ^ Error: expect(locator).toBeVisible() failed
  160 |   await expect(page.getByTestId('admin.ip.owner.save')).toBeDisabled();
  161 |   await expect(page.getByTestId('admin.ip.route.assign.open')).toBeDisabled();
  162 |   expect(state.assignments).toHaveLength(1);
  163 | });
  164 | 
  165 | for (const mismatch of [false, true]) {
  166 |   test(`@pr-smoke @pr-smoke-mobile synchronous owner response ${mismatch ? 'with a mismatch remains uncertain' : 'is confirmed by a fresh read'}`, async ({ page }) => {
  167 |     const state = await fixture(page); state.mismatch = mismatch;
  168 |     await page.goto('/admin/networking/ip-addresses/100');
  169 |     await page.getByTestId('admin.ip.owner.user').fill('7');
  170 |     await page.getByTestId('admin.ip.owner.environment').selectOption('1');
  171 |     await page.getByTestId('admin.ip.owner.save').click();
  172 |     if (mismatch) {
  173 |       await expect(page.getByTestId('admin.ip.owner.uncertain')).toBeVisible();
  174 |       await expect(page.getByTestId('admin.ip.owner.error')).toBeVisible();
  175 |       await expect(page.getByTestId('admin.ip.owner.save')).toBeDisabled();
  176 |     } else {
  177 |       await expect(page.getByTestId('admin.ip.action.user')).toHaveAttribute('href', '/admin/users/7');
  178 |       await expect(page.getByTestId('admin.ip.owner.current')).toContainText('#7');
  179 |       await expect(page.getByTestId('admin.ip.owner.current')).toContainText('#1');
  180 |       await expect(page.getByTestId('admin.ip.owner.error')).toHaveCount(0);
  181 |       await expect(page.getByTestId('admin.ip.owner.uncertain')).toHaveCount(0);
  182 |     }
  183 |     expect(state.ownerWrites).toBe(1);
  184 |   });
  185 | }
  186 | 
```