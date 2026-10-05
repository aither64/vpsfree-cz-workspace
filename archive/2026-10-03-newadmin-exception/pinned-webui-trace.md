# Exact pinned WebUI source trace

Configuration's unchanged WebUI lock is
`f123a7fb825437034a764a8a5654032a481a8476`. An SSH fetch from the canonical
`git@github.com:vpsfreecz/vpsadmin-webui.git` resolved this object after the
reviewer reported it unavailable locally. No WebUI worktree or source was changed.

Lead inspected this exact revision:

- `bff/server.js:154-183`: `ensureFreshToken` refreshes an expired/nearly expired
  access token using the retained refresh token and saves the new OAuth token
  snapshot. It does not involve the SSO association.
- `bff/server.js:256-275`: `/session.json` calls that function before returning
  the current access token to the same-origin browser.
- `src/app/runtimeBootstrap.ts:235-251`: bootstrap fetches `/session.json`,
  installs its access token and remembers the BFF session.
- `src/app/auth.tsx:124-130` and `src/lib/api/users.ts:19-24`: current-user
  authentication invokes `GET /users/current`.
- `src/lib/api/haveapi.ts:382-390`: the OAuth access token is sent using the
  API-described authentication header. Lines 474-480 and
  `src/lib/auth/bffSession.ts` support one bounded recovery after an explicit
  HTTP authentication rejection by fetching `/session.json` again.

This confirms the refresh -> access-authentication path in the configuration's
actual pinned consumer source, replacing the earlier reference-only inspection
of `aa2f60b8`. It does not prove which WebUI/BFF revision was running when the
email occurred, or reproduce a browser request against production. The API fix
changes no consumer contract and requires no WebUI source or pin change.
