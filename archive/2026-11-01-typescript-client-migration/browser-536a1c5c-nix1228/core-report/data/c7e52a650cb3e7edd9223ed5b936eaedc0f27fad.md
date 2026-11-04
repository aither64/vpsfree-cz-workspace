# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: app/profile_keys_sessions.spec.ts >> @smoke profile: ssh keys + sessions flows
- Location: e2e/specs/app/profile_keys_sessions.spec.ts:5:1

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator:  getByTestId('profile.keys.table').getByTestId('profile.keys.row.1')
Expected: visible
Received: hidden
Timeout:  15000ms

Call log:
  - Expect "toBeVisible" with timeout 15000ms
  - waiting for getByTestId('profile.keys.table').getByTestId('profile.keys.row.1')
    23 × locator resolved to <tr data-testid="profile.keys.row.1" class="border-b border-border/60 last:border-b-0">…</tr>
       - unexpected value "hidden"

```

```yaml
- link "Skip to main content":
  - /url: "#main-content"
- banner:
  - button "Open navigation"
  - button "Search"
  - button "Open tasks"
  - button "Open account menu"
- main:
  - heading "Account" [level=1]
  - paragraph: Public keys used for access and automation.
  - link "Overview":
    - /url: /app/profile
  - link "Resources":
    - /url: /app/profile/resources
  - link "Security":
    - /url: /app/profile/security
  - link "Two-step verification":
    - /url: /app/profile/mfa
  - link "Sessions":
    - /url: /app/profile/sessions
  - link "SSH keys":
    - /url: /app/profile/keys
  - link "Metrics tokens":
    - /url: /app/profile/metrics
  - link "Mail":
    - /url: /app/profile/mail
  - link "User data templates":
    - /url: /app/profile/user-data
  - link "User namespaces":
    - /url: /app/profile/user-namespaces
  - text: SSH keys Public keys used for access and automation.
  - button "Add key"
  - text: "Laptop #1 Auto-add SHA256:AAAA"
  - button "Edit"
  - button "Delete"
```

# Test source

```ts
  4   | 
  5   | test('@smoke profile: ssh keys + sessions flows', async ({ page }) => {
  6   |   const user = { id: 1, login: 'e2e', level: 1 };
  7   | 
  8   |   await bootstrapVpsAdminWindow(page, { sessionToken: 'TEST' });
  9   | 
  10  |   let keys = [
  11  |     {
  12  |       id: 1,
  13  |       label: 'Laptop',
  14  |       fingerprint: 'SHA256:AAAA',
  15  |       auto_add: true,
  16  |       created_at: '2026-02-01T12:00:00Z',
  17  |     },
  18  |   ];
  19  | 
  20  |   let sessions = [
  21  |     {
  22  |       id: 1,
  23  |       label: 'Firefox',
  24  |       auth_type: 'oauth2',
  25  |       created_at: '2026-02-01T12:00:00Z',
  26  |       last_request_at: '2026-02-02T08:00:00Z',
  27  |       closed_at: null as string | null,
  28  |       api_ip_addr: '203.0.113.10',
  29  |       api_ip_ptr: 'user.example.test',
  30  |       client_ip_addr: '203.0.113.10',
  31  |       client_ip_ptr: 'client.example.test',
  32  |       user_agent: 'Mozilla/5.0 (X11; Linux x86_64)',
  33  |       client_version: 'vpsadmin-webui 9a5fccf4',
  34  |       token_fragment: 'abc…',
  35  |       token_lifetime: 'renewable_auto',
  36  |       token_interval: 900,
  37  |       request_count: 111,
  38  |       scope: 'all',
  39  |     },
  40  |     {
  41  |       id: 2,
  42  |       label: 'Old token',
  43  |       auth_type: 'token',
  44  |       created_at: '2026-01-01T12:00:00Z',
  45  |       last_request_at: '2026-01-02T08:00:00Z',
  46  |       closed_at: '2026-01-02T08:30:00Z',
  47  |       api_ip_addr: '198.51.100.20',
  48  |       client_ip_addr: '198.51.100.21',
  49  |       user_agent: 'curl/8',
  50  |       client_version: 'vpsfreectl 1.0',
  51  |       token_fragment: 'deadbeef',
  52  |       token_lifetime: 'fixed',
  53  |       token_interval: 3600,
  54  |       request_count: 8,
  55  |       scope: 'dns',
  56  |     },
  57  |   ];
  58  | 
  59  |   await installHaveApiMock(page, {
  60  |     user,
  61  |     handlers: {
  62  |       'GET users/1/public_keys': () => ({ public_keys: keys }),
  63  |       'POST users/1/public_keys': () => {
  64  |         const created = {
  65  |           id: 2,
  66  |           label: 'Office',
  67  |           fingerprint: 'SHA256:BBBB',
  68  |           auto_add: false,
  69  |           created_at: '2026-02-02T08:00:00Z',
  70  |         };
  71  |         keys = [keys[0]!, created];
  72  |         return { public_key: created };
  73  |       },
  74  |       'PUT users/1/public_keys/2': () => {
  75  |         keys = keys.map((k) => (k.id === 2 ? { ...k, label: 'Office (renamed)', auto_add: true } : k));
  76  |         return { public_key: keys.find((k) => k.id === 2) };
  77  |       },
  78  |       'DELETE users/1/public_keys/2': () => {
  79  |         keys = keys.filter((k) => k.id !== 2);
  80  |         return { ok: true };
  81  |       },
  82  | 
  83  |       'GET user_sessions': (ctx) => {
  84  |         const authType = ctx.searchParams.get('user_session[auth_type]');
  85  |         const rows = authType ? sessions.filter((s) => s.auth_type === authType) : sessions;
  86  |         return { user_sessions: rows };
  87  |       },
  88  |       'GET user_sessions/2': () => ({ user_session: sessions.find((s) => s.id === 2) }),
  89  |       'PUT user_sessions/1': () => {
  90  |         sessions = sessions.map((s) => (s.id === 1 ? { ...s, label: 'Firefox (renamed)' } : s));
  91  |         return { user_session: sessions.find((s) => s.id === 1) };
  92  |       },
  93  |       'POST user_sessions/1': () => {
  94  |         sessions = sessions.map((s) => (s.id === 1 ? { ...s, closed_at: '2026-02-02T08:30:00Z' } : s));
  95  |         return { user_session: sessions.find((s) => s.id === 1) };
  96  |       },
  97  |     },
  98  |   });
  99  | 
  100 |   await page.goto('/app/profile/keys');
  101 |   const keysTable = page.getByTestId('profile.keys.table');
  102 | 
  103 |   // Create key
> 104 |   await expect(keysTable.getByTestId('profile.keys.row.1')).toBeVisible();
      |                                                             ^ Error: expect(locator).toBeVisible() failed
  105 |   await page.getByTestId('profile.keys.add').click();
  106 |   await expect(page.getByTestId('profile.keys.modal')).toBeVisible();
  107 |   await page.getByTestId('profile.keys.modal.label').fill('Office');
  108 |   await page.getByTestId('profile.keys.modal.key').fill('ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA TEST');
  109 |   // Disable auto-add
  110 |   await page.getByTestId('profile.keys.modal.auto_add').click();
  111 | 
  112 |   const createReqP = page.waitForRequest((r) => r.method() === 'POST' && r.url().includes('/users/1/public_keys'));
  113 |   await page.getByTestId('profile.keys.modal.save').click();
  114 |   const createReq = await createReqP;
  115 |   const createBody = createReq.postDataJSON();
  116 |   expect(createBody.public_key.label).toBe('Office');
  117 |   expect(createBody.public_key.key).toContain('ssh-ed25519');
  118 |   expect(createBody.public_key.auto_add).toBe(false);
  119 | 
  120 |   await expect(keysTable.getByTestId('profile.keys.row.2')).toBeVisible();
  121 | 
  122 |   // Edit key (rename + enable auto-add)
  123 |   await keysTable.getByTestId('profile.keys.row.2.edit').click();
  124 |   await expect(page.getByTestId('profile.keys.modal')).toBeVisible();
  125 |   await page.getByTestId('profile.keys.modal.label').fill('Office (renamed)');
  126 |   await page.getByTestId('profile.keys.modal.auto_add').click();
  127 | 
  128 |   const updateReqP = page.waitForRequest((r) => r.method() === 'PUT' && r.url().includes('/users/1/public_keys/2'));
  129 |   await page.getByTestId('profile.keys.modal.save').click();
  130 |   const updateReq = await updateReqP;
  131 |   const updateBody = updateReq.postDataJSON();
  132 |   expect(updateBody.public_key.label).toBe('Office (renamed)');
  133 |   expect(updateBody.public_key.auto_add).toBe(true);
  134 |   // key field is optional on update when unchanged
  135 |   expect(updateBody.public_key.key).toBeUndefined();
  136 | 
  137 |   // Delete key
  138 |   await keysTable.getByTestId('profile.keys.row.2.delete').click();
  139 |   await expect(page.getByTestId('profile.keys.delete_dialog')).toBeVisible();
  140 | 
  141 |   const deleteReqP = page.waitForRequest((r) => r.method() === 'DELETE' && r.url().includes('/users/1/public_keys/2'));
  142 |   await page.getByTestId('profile.keys.delete_dialog.confirm').click();
  143 |   await deleteReqP;
  144 | 
  145 |   // Navigate to Sessions tab
  146 |   await page.goto('/app/profile/sessions');
  147 |   const sessionsTable = page.getByTestId('profile.sessions.table');
  148 | 
  149 |   // Session rename
  150 |   await expect(sessionsTable.getByTestId('profile.sessions.row.1')).toBeVisible();
  151 |   await expect(sessionsTable.getByText('Request count').first()).toBeVisible();
  152 |   await expect(sessionsTable.getByText('111').first()).toBeVisible();
  153 |   await expect(sessionsTable.getByText('vpsadmin-webui 9a5fccf4')).toBeVisible();
  154 |   await expect(sessionsTable.getByTestId('profile.sessions.row.1.transactions')).toBeVisible();
  155 | 
  156 |   const authFilterReqP = page.waitForRequest((r) => {
  157 |     const url = new URL(r.url());
  158 |     return r.method() === 'GET'
  159 |       && url.pathname === '/api/v7.0/user_sessions'
  160 |       && url.searchParams.get('user_session[auth_type]') === 'token';
  161 |   });
  162 |   await page.getByTestId('profile.sessions.auth_type').selectOption('token');
  163 |   await authFilterReqP;
  164 |   await expect(sessionsTable.getByTestId('profile.sessions.row.2')).toBeVisible();
  165 |   await expect(sessionsTable.getByTestId('profile.sessions.row.1')).toBeHidden();
  166 | 
  167 |   const exactIdReqP = page.waitForRequest((r) => r.method() === 'GET' && r.url().includes('/user_sessions/2'));
  168 |   await page.getByTestId('profile.sessions.exact_id').fill('2');
  169 |   await exactIdReqP;
  170 |   await expect(sessionsTable.getByTestId('profile.sessions.row.2')).toBeVisible();
  171 | 
  172 |   await page.getByTestId('profile.sessions.exact_id').fill('');
  173 |   await page.getByTestId('profile.sessions.auth_type').selectOption('all');
  174 |   await expect(sessionsTable.getByTestId('profile.sessions.row.1')).toBeVisible();
  175 | 
  176 |   await sessionsTable.getByTestId('profile.sessions.row.1.rename').click();
  177 |   await expect(page.getByTestId('profile.sessions.rename_modal')).toBeVisible();
  178 |   await page.getByTestId('profile.sessions.rename_modal.label').fill('Firefox (renamed)');
  179 | 
  180 |   const renameReqP = page.waitForRequest((r) => r.method() === 'PUT' && r.url().includes('/user_sessions/1'));
  181 |   await page.getByTestId('profile.sessions.rename_modal.save').click();
  182 |   const renameReq = await renameReqP;
  183 |   const renameBody = renameReq.postDataJSON();
  184 |   expect(renameBody.user_session.label).toBe('Firefox (renamed)');
  185 | 
  186 |   // Close session
  187 |   await sessionsTable.getByTestId('profile.sessions.row.1.close').click();
  188 |   await expect(page.getByTestId('profile.sessions.close_dialog')).toBeVisible();
  189 |   await expect(page.getByTestId('profile.sessions.close_dialog.confirm')).toBeEnabled();
  190 |   const closeReqP = page.waitForRequest((r) => r.method() === 'POST' && r.url().includes('/user_sessions/1'));
  191 |   await page.getByTestId('profile.sessions.close_dialog.confirm').click();
  192 |   await closeReqP;
  193 | });
  194 | 
```