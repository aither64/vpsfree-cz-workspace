# vpsAdmin Devcluster Seed Reapply

Related initiative: `work/2026-05-30-dev-vpsadmin-clusters`

Symptom:

- The web UI login action returned HTTP 500 before showing the OAuth2 login
  form.
- The webui container nginx journal reported
  `HaveAPI\Client\Exception\ProtocolError: Invalid OAuth2 authorize_url`.

Cause:

- vpsAdmin `databaseSetup.seedFiles` are only applied when the database is first
  initialized.
- The existing dev database still had older `core.auth_url` and OAuth2 client
  values from the earlier `-tmp` domain model, while the web UI config trusted
  only the newer primary auth origin.
- Restarting PHP/webui alone could not fix it because the OAuth2 URLs are served
  by the API from persistent database state and cached in the API process.

Fix/workaround:

- Rerun the dev seed file against the existing database and restart
  `vpsadmin-api`.
- The devcluster config now provides `vpsadmin-devcluster-seed.service` on the
  services VM. It runs after `vpsadmin-database-setup.service` and before
  `vpsadmin-api.service`.
- `devcluster update <slug> services` restarts `vpsadmin-api` after switching;
  the API unit dependency reruns the dev seed service first.

Verification:

- `curl -k -X OPTIONS https://api.aitherdev.int.vpsfree.cz/v7.0/` showed OAuth2
  URLs on `https://auth.aitherdev.int.vpsfree.cz`.
- `curl -k -D - -X POST
  'https://webui.aitherdev.int.vpsfree.cz/?page=login&action=login'` returned
  HTTP 302 to the auth server instead of HTTP 500.

Follow-up symptom:

- After credentials were submitted, the web UI callback rendered
  `vpsAdmin was unable to obtain access token from the authorization server`.
- The callback handler catches the token-exchange exception, so nginx/PHP logs
  only show HTTP 200 for the callback page.

Follow-up cause:

- The webui container did not trust the devcluster CA.
- Server-side token exchange from the web UI to
  `https://auth.aitherdev.int.vpsfree.cz/_auth/oauth2/token` failed TLS
  verification before reaching the API.

Follow-up fix:

- Add the devcluster CA to `security.pki.certificateFiles` on the services VM
  and in the webui container.
- Verify from inside the webui container that `curl
  https://auth.aitherdev.int.vpsfree.cz/_auth/oauth2/authorize` no longer fails
  with `unable to get local issuer certificate`.
- A complete OAuth2 login should then show `POST /_auth/oauth2/token` returning
  HTTP 200 in HAProxy logs and finish at `?page=cluster`.
