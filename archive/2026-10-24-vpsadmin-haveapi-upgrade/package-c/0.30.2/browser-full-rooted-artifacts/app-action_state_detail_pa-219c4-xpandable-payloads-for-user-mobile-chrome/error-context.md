# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/action_state_detail_page.spec.ts >> @workflow-matrix @smoke Action state detail page >> shows related transactions and expandable payloads for user
- Location: e2e/specs/app/action_state_detail_page.spec.ts:60:5

# Error details

```
Test timeout of 90000ms exceeded.
```

```
Error: locator.click: Test timeout of 90000ms exceeded.
Call log:
  - waiting for getByTestId('action_state.detail.tx.toggle.7001')
    - locator resolved to <button type="button" aria-label="Expand" title="Details (input/output)" data-testid="action_state.detail.tx.toggle.7001" class="inline-flex items-center justify-center gap-2 rounded-md font-medium transition-colors focus:outline-none focus:ring-2 focus:ring-focus/35 focus:ring-offset-2 focus:ring-offset-bg disabled:cursor-not-allowed disabled:opacity-50 [@media(any-pointer:coarse)]:min-h-11 [@media(any-pointer:coarse)]:min-w-11 bg-transparent text-fg hover:bg-surface-2 h-8 px-3 text-sm h-8 w-8 px-0">…</button>
  - attempting click action
    - waiting for element to be visible, enabled and stable
    - element is visible, enabled and stable
    - scrolling into view if needed
    - done scrolling
    - <div class="h-2 rounded-full bg-fg/60"></div> from <div class="min-w-0 rounded-lg border border-border bg-surface shadow-card">…</div> subtree intercepts pointer events
  - retrying click action
    - waiting for element to be visible, enabled and stable
    - element is visible, enabled and stable
    - scrolling into view if needed
    - done scrolling
    - <div class="space-y-6">…</div> intercepts pointer events
  - retrying click action
    - waiting 20ms
    - waiting for element to be visible, enabled and stable
    - element is visible, enabled and stable
    - scrolling into view if needed
    - done scrolling
    - <div class="h-2 rounded-full bg-fg/60"></div> from <div class="min-w-0 rounded-lg border border-border bg-surface shadow-card">…</div> subtree intercepts pointer events
  2 × retrying click action
      - waiting 100ms
      - waiting for element to be visible, enabled and stable
      - element is visible, enabled and stable
      - scrolling into view if needed
      - done scrolling
      - <div class="p-4">…</div> from <div class="min-w-0 rounded-lg border border-border bg-surface shadow-card">…</div> subtree intercepts pointer events
  38 × retrying click action
       - waiting 500ms
       - waiting for element to be visible, enabled and stable
       - element is visible, enabled and stable
       - scrolling into view if needed
       - done scrolling
       - <div class="space-y-6">…</div> intercepts pointer events
     - retrying click action
       - waiting 500ms
       - waiting for element to be visible, enabled and stable
       - element is visible, enabled and stable
       - scrolling into view if needed
       - done scrolling
       - <div class="h-2 rounded-full bg-fg/60"></div> from <div class="min-w-0 rounded-lg border border-border bg-surface shadow-card">…</div> subtree intercepts pointer events
     - retrying click action
       - waiting 500ms
       - waiting for element to be visible, enabled and stable
       - element is visible, enabled and stable
       - scrolling into view if needed
       - done scrolling
       - <div class="p-4">…</div> from <div class="min-w-0 rounded-lg border border-border bg-surface shadow-card">…</div> subtree intercepts pointer events
     - retrying click action
       - waiting 500ms
       - waiting for element to be visible, enabled and stable
       - element is visible, enabled and stable
       - scrolling into view if needed
       - done scrolling
       - <div class="p-4">…</div> from <div class="min-w-0 rounded-lg border border-border bg-surface shadow-card">…</div> subtree intercepts pointer events
  - retrying click action
    - waiting 500ms
    - waiting for element to be visible, enabled and stable
    - element is visible, enabled and stable
    - scrolling into view if needed
    - done scrolling
    - <div class="space-y-6">…</div> intercepts pointer events
  - retrying click action
    - waiting 500ms
    - waiting for element to be visible, enabled and stable
    - element is visible, enabled and stable
    - scrolling into view if needed
    - done scrolling
    - <div class="h-2 rounded-full bg-fg/60"></div> from <div class="min-w-0 rounded-lg border border-border bg-surface shadow-card">…</div> subtree intercepts pointer events
  - retrying click action
    - waiting 500ms

```

# Page snapshot

```yaml
- generic [ref=e2]:
  - link "Skip to main content" [ref=e3] [cursor=pointer]:
    - /url: "#main-content"
  - generic [ref=e6]:
    - banner [ref=e7]:
      - generic [ref=e8]:
        - button "Open navigation" [ref=e9]:
          - img [ref=e10]
        - button "Search" [ref=e11]:
          - img [ref=e12]
        - button "Open tasks" [ref=e15]:
          - img [ref=e16]
        - button "Open account menu" [ref=e19]:
          - img [ref=e20]
    - main [ref=e23]:
      - generic [ref=e26]:
        - generic [ref=e29]:
          - generic [ref=e30]:
            - generic [ref=e31]:
              - link "Action progress" [ref=e32] [cursor=pointer]:
                - /url: /app/action-states
              - text: "/ #123"
            - heading "Create VPS" [level=1] [ref=e34]
            - generic [ref=e36]:
              - generic [ref=e37]: Done
              - generic [ref=e38]: VPS
              - generic [ref=e39]: Normal
              - generic [ref=e40]: User action
            - generic [ref=e41]:
              - text: created 1/26/2026, 1:00:00 AM · updated 1/26/2026, 1:10:00 AM
              - generic [ref=e42]: · Auto-refreshing…
          - generic [ref=e44]:
            - button "Refresh" [ref=e45]
            - button "Pin" [ref=e46]:
              - img [ref=e47]
            - button "Track" [ref=e49]
            - button "Open tasks" [ref=e50]
        - generic [ref=e51]:
          - generic [ref=e53]:
            - generic [ref=e54]: Details
            - generic [ref=e55]:
              - text: "Transaction chain:"
              - link "Create chain" [ref=e56] [cursor=pointer]:
                - /url: /app/transactions/456
          - generic [ref=e57]:
            - generic [ref=e58]:
              - generic [ref=e59]:
                - generic [ref=e60]: State
                - generic [ref=e62]: Done
              - generic [ref=e63]:
                - generic [ref=e64]: Operation
                - generic [ref=e65]: Create VPS
              - generic [ref=e66]:
                - generic [ref=e67]: Type
                - generic [ref=e68]: VPS
              - generic [ref=e69]:
                - generic [ref=e70]: Progress
                - generic [ref=e71]: 2/2 · 100%
              - generic [ref=e72]:
                - generic [ref=e73]: Current step
                - generic [ref=e74]: —
            - generic [ref=e75]:
              - generic [ref=e76]:
                - generic [ref=e77]: "ID:"
                - generic [ref=e78]: "#123"
              - generic [ref=e79]:
                - generic [ref=e80]: "Operation:"
                - text: Create VPS
              - generic [ref=e81]:
                - generic [ref=e82]: "Type:"
                - text: VPS
              - generic [ref=e83]:
                - generic [ref=e84]: "Activity:"
                - text: User action
              - generic [ref=e85]:
                - generic [ref=e86]: "Can cancel:"
                - text: "No"
              - generic [ref=e87]:
                - generic [ref=e88]: "Created:"
                - text: 1/26/2026, 1:00:00 AM
              - generic [ref=e89]:
                - generic [ref=e90]: "Updated:"
                - text: 1/26/2026, 1:10:00 AM
              - generic [ref=e91]:
                - generic [ref=e92]: "Progress:"
                - text: 2/2
            - generic [ref=e96]: 100%
        - generic [ref=e97]:
          - generic [ref=e99]:
            - generic [ref=e100]: Backend details
            - generic [ref=e101]: Raw action-state fields useful for debugging errors and backend output.
          - generic [ref=e103]: "{ \"id\": 123, \"label\": \"Create VPS\", \"state\": \"done\", \"created_at\": \"2026-01-26T00:00:00.000Z\", \"updated_at\": \"2026-01-26T00:10:00.000Z\", \"current\": 2, \"total\": 2, \"finished\": true, \"status\": true, \"transaction_chain\": { \"id\": 456, \"label\": \"Create chain\" } }"
        - generic [ref=e104]:
          - generic [ref=e105]:
            - generic [ref=e106]:
              - generic [ref=e107]: Chained transactions
              - generic [ref=e108]: "Transaction chain #456"
            - generic [ref=e110]:
              - button "Expand all" [ref=e111]
              - button "Collapse all" [ref=e112]
              - link "Open chain" [ref=e113] [cursor=pointer]:
                - /url: /app/transactions/456
              - link "View all" [ref=e114] [cursor=pointer]:
                - /url: /app/transactions/items?transaction_chain=456
          - table [ref=e117]:
            - rowgroup [ref=e118]:
              - row "ID State Name Node VPS Created Started Finished Success Details (input/output)" [ref=e119]:
                - columnheader "ID" [ref=e120]
                - columnheader "State" [ref=e121]
                - columnheader "Name" [ref=e122]
                - columnheader "Node" [ref=e123]
                - columnheader "VPS" [ref=e124]
                - columnheader "Created" [ref=e125]
                - columnheader "Started" [ref=e126]
                - columnheader "Finished" [ref=e127]
                - columnheader "Success" [ref=e128]
                - columnheader "Details (input/output)" [ref=e129]:
                  - generic [ref=e130]: Details (input/output)
            - rowgroup [ref=e131]:
              - row "#7001 Done Normal Create dataset VPS · type 3001 node2 vps12 1/26/2026, 1:01:00 AM 1/26/2026, 1:01:01 AM 1/26/2026, 1:01:05 AM 1 Expand" [ref=e132]:
                - cell "#7001" [ref=e133]:
                  - link "#7001" [ref=e134] [cursor=pointer]:
                    - /url: /app/transactions/items/7001
                - cell "Done Normal" [ref=e135]:
                  - generic [ref=e136]:
                    - generic [ref=e137]: Done
                    - generic [ref=e138]: Normal
                - cell "Create dataset VPS · type 3001" [ref=e139]:
                  - generic [ref=e140]: Create dataset
                  - generic [ref=e141]: VPS · type 3001
                - cell "node2" [ref=e142]
                - cell "vps12" [ref=e143]:
                  - link "vps12" [ref=e144] [cursor=pointer]:
                    - /url: /app/vps/12
                - cell "1/26/2026, 1:01:00 AM" [ref=e145]
                - cell "1/26/2026, 1:01:01 AM" [ref=e146]
                - cell "1/26/2026, 1:01:05 AM" [ref=e147]
                - cell "1" [ref=e148]
                - cell "Expand" [ref=e149]:
                  - button "Expand" [ref=e150]:
                    - img [ref=e151]
```

# Test source

```ts
  29  |       handlers: {
  30  |         'GET action_states/123': () => ({ action_state: makeAction(123) }),
  31  |         'POST action_states/123/cancel': () => {
  32  |           cancelCalled = true;
  33  |           return {};
  34  |         },
  35  |       },
  36  |     });
  37  | 
  38  |     await page.goto('/app/action-states/123');
  39  | 
  40  |     await expect(page.getByTestId('action_state.detail')).toBeVisible();
  41  |     await expect(page.getByTestId('action_state.detail.header')).toBeVisible();
  42  | 
  43  |     // Primary controls
  44  |     await expect(page.getByTestId('action_state.detail.refresh')).toBeVisible();
  45  |     await expect(page.getByTestId('action_state.detail.open_tasks')).toBeVisible();
  46  | 
  47  |     // Cancel flow
  48  |     await page.getByTestId('action_state.detail.cancel').click();
  49  |     await expect(page.getByTestId('tasks.cancel_dialog')).toBeVisible();
  50  | 
  51  |     await page.getByTestId('tasks.cancel_dialog.confirm').click();
  52  | 
  53  |     await expect.poll(() => cancelCalled).toBe(true);
  54  |   });
  55  | 
  56  |   for (const roleCase of [
  57  |     { name: 'user', basePath: '/app', user: { id: 1, login: 'user', level: 1 } },
  58  |     { name: 'admin', basePath: '/admin', user: { id: 1, login: 'admin', level: 99 } },
  59  |   ]) {
  60  |     test(`shows related transactions and expandable payloads for ${roleCase.name}`, async ({ page }) => {
  61  |       await bootstrapVpsAdminWindow(page, {
  62  |         sessionToken: 'TEST_TOKEN',
  63  |       });
  64  | 
  65  |       const handlers = {
  66  |         'GET action_states/123': () => ({
  67  |           action_state: {
  68  |             id: 123,
  69  |             label: 'Create VPS',
  70  |             state: 'done',
  71  |             created_at: '2026-01-26T00:00:00.000Z',
  72  |             updated_at: '2026-01-26T00:10:00.000Z',
  73  |             current: 2,
  74  |             total: 2,
  75  |             finished: true,
  76  |             status: true,
  77  |             transaction_chain: { id: 456, label: 'Create chain' },
  78  |           },
  79  |         }),
  80  |         'GET transaction_chains/456': () => ({
  81  |           transaction_chain: {
  82  |             id: 456,
  83  |             label: 'Create chain',
  84  |             state: 'done',
  85  |             progress: 2,
  86  |             size: 2,
  87  |           },
  88  |         }),
  89  |         'GET transactions': ({ searchParams }: { searchParams: URLSearchParams }) => {
  90  |           if (searchParams.get('transaction[transaction_chain]') !== '456') return { transactions: [] };
  91  |           return {
  92  |             transactions: [
  93  |               {
  94  |                 id: 7001,
  95  |                 name: 'Create dataset',
  96  |                 done: 'done',
  97  |                 success: 1,
  98  |                 type: 3001,
  99  |                 priority: 0,
  100 |                 created_at: '2026-01-26T00:01:00.000Z',
  101 |                 started_at: '2026-01-26T00:01:01.000Z',
  102 |                 finished_at: '2026-01-26T00:01:05.000Z',
  103 |                 node: { id: 2, label: 'node2' },
  104 |                 vps: { id: 12, label: 'vps12' },
  105 |                 user: { id: 9, login: 'worker' },
  106 |                 transaction_chain: { id: 456 },
  107 |                 input: { dataset: 'tank/ct/vps12' },
  108 |                 output: { ok: true },
  109 |                 result: { mounted: true },
  110 |               },
  111 |             ],
  112 |           };
  113 |         },
  114 |       };
  115 | 
  116 |       await installHaveApiMock(page, {
  117 |         user: roleCase.user,
  118 |         handlers,
  119 |       });
  120 | 
  121 |       await page.goto(`${roleCase.basePath}/action-states/123`);
  122 | 
  123 |       await expect(page.getByTestId('action_state.detail.transactions')).toBeVisible();
  124 |       await expect(page.getByTestId('action_state.detail.transactions.view_all')).toHaveAttribute(
  125 |         'href',
  126 |         `${roleCase.basePath}/transactions/items?transaction_chain=456`
  127 |       );
  128 | 
> 129 |       await page.getByTestId('action_state.detail.tx.toggle.7001').click();
      |                                                                    ^ Error: locator.click: Test timeout of 90000ms exceeded.
  130 |       await expect(page.getByTestId('action_state.detail.tx.expanded.7001')).toBeVisible();
  131 |       await expect(page.getByTestId('action_state.detail.tx.expanded.7001')).toContainText('tank/ct/vps12');
  132 |       await expect(page.getByTestId('action_state.detail.tx.expanded.7001')).toContainText('worker');
  133 |       await expect(page.getByTestId('action_state.detail.tx.expanded.7001')).toContainText('mounted');
  134 |     });
  135 |   }
  136 | 
  137 |   test('deep reload keeps action-state detail and chained transactions visible', async ({ page }) => {
  138 |     await bootstrapVpsAdminWindow(page, {
  139 |       sessionToken: 'TEST_TOKEN',
  140 |     });
  141 | 
  142 |     await installHaveApiMock(page, {
  143 |       user: { id: 1, login: 'test', level: 1 },
  144 |       handlers: {
  145 |         'GET action_states/123': () => ({
  146 |           action_state: {
  147 |             id: 123,
  148 |             label: 'Create VPS',
  149 |             state: 'done',
  150 |             current: 1,
  151 |             total: 1,
  152 |             finished: true,
  153 |             status: true,
  154 |             transaction_chain: { id: 456, label: 'Create chain' },
  155 |           },
  156 |         }),
  157 |         'GET transaction_chains/456': () => ({
  158 |           transaction_chain: { id: 456, label: 'Create chain', state: 'done', progress: 1, size: 1 },
  159 |         }),
  160 |         'GET transactions': ({ searchParams }: { searchParams: URLSearchParams }) => {
  161 |           if (searchParams.get('transaction[transaction_chain]') !== '456') return { transactions: [] };
  162 |           return {
  163 |             transactions: [
  164 |               {
  165 |                 id: 7001,
  166 |                 name: 'Create dataset',
  167 |                 done: 'done',
  168 |                 success: 1,
  169 |                 transaction_chain: { id: 456 },
  170 |                 input: { dataset: 'tank/ct/vps12' },
  171 |               },
  172 |             ],
  173 |           };
  174 |         },
  175 |       },
  176 |     });
  177 | 
  178 |     await page.goto('/app/action-states/123');
  179 |     await expect(page.getByTestId('action_state.detail.transactions')).toBeVisible();
  180 | 
  181 |     await page.reload();
  182 | 
  183 |     await expect(page).toHaveURL(/\/app\/action-states\/123$/);
  184 |     await expect(page.getByTestId('action_state.detail')).toBeVisible();
  185 |     await expect(page.getByTestId('action_state.detail.transactions.table')).toContainText('Create dataset');
  186 |   });
  187 | });
  188 | 
```