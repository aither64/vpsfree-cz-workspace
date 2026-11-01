# OAuth sign-in for vpsAdmin API documentation

The API's HTML documentation can use a dedicated OAuth client to show the
API descriptions available to the signed-in user. Its cookie does not
authenticate ordinary API, JSON or OPTIONS requests. Without the optional
private configuration below, documentation remains anonymous.

This procedure covers `int.api1`, `int.api2` and their TLS edge on `proxy.prg`.
Register the client and prepare its private files before deployment. Deploy the
proxy protections before enabling sign-in on either API host.

## Register the client before deployment

Use the existing administrator OAuth2Client Create/Update interface, exposed at
`POST /v7.0/oauth2_clients` and `PUT /v7.0/oauth2_clients/ID`. Client registration
uses the existing API and does not depend on deploying the documentation
feature. Inspect an existing dedicated client before reusing it.

Create one confidential client with these settings:

| Field | Value |
| --- | --- |
| `name` | A recognizable name for API documentation |
| `client_id` | A newly generated dedicated identifier |
| `client_secret` | A newly generated secret retained privately |
| `redirect_uri` | `https://api.vpsfree.cz/_documentation/oauth/callback` |
| `is_default` | `false` |
| `access_token_lifetime` | `fixed` |
| `access_token_seconds` | `3600` |
| `issue_refresh_token` | `false` |
| `allow_single_sign_on` | `false` |

The nonempty secret makes this a confidential client; there is no separate
client-type setting. Ordinary Show does not return the secret, so retain it
when registering the client. Keep the existing default client and PHP/React
credentials unchanged. Use the normal API, not database writes. Scope `all`
belongs to the documentation configuration, not the client-create fields.

Check the API's OAuth provider metadata. Its origin comes from
`core.auth_url`, falling back to `core.api_url`; authorize, token and revoke
paths use `/_auth/oauth2/` without an API-version prefix. Browser and API
workers must trust the provider's HTTPS certificate. Do not substitute the
documentation callback origin for the provider origin.

## Prepare the private API files

Check the effective `vpsadmin.api.stateDirectory`, `user` and `group` in the
reviewed configuration. The normal directory on both API hosts is
`/var/lib/vpsadmin/api/config`, owned by `vpsadmin-api:vpsadmin-api` at mode
`0750`. Prepare these protected regular files there:

| File | Contents |
| --- | --- |
| `documentation-oauth.json` | The dedicated client ID, secret and exact callback below |
| `documentation-session.key` | At least 64 bytes of cryptographically random secret material |

```json
{
  "client_id": "DEDICATED_CLIENT_ID",
  "client_secret": "DEDICATED_CLIENT_SECRET",
  "redirect_uri": "https://api.vpsfree.cz/_documentation/oauth/callback",
  "switch_user": false
}
```

Generate the session key once using the normal procedure for private secrets.
Use identical JSON and the same stable key on both hosts and across all
workers. Inspect existing ownership, file types and contents privately before
replacement; retain an existing valid key rather than rotating it on upgrade.
Install both files atomically with owner `vpsadmin-api:vpsadmin-api` and mode
`0600`. Do not expose values through command arguments, logs, Git or the Nix
store. Do not place these files in the authored `configs/vpsadmin/api` tree or
the supervisor's persistent configuration directory.

The API setup preserves these regular files and links its runtime
`/run/vpsadmin/api/config` to the persistent directory. The authored `api.rb`
hook is a store symlink, so it resolves private files through
`VpsAdmin::API.root/config`, not through the hook's source directory. The
supervisor shares the authored hook but receives no documentation credentials.
ExceptionMailer remains enabled. Missing OAuth JSON leaves documentation
anonymous. If the JSON exists but is malformed, has invalid fields or refers to
a missing or invalid key, startup fails with an error that omits secret values.

The hook requests scope `all` and limits the documentation session to 3600
seconds. Keep `switch_user` false until a fresh authorization for this client
offers editable account credentials. Disabling SSO is necessary but
does not alone prove that behavior. No `prompt` or `select_account` parameter
is required or added. Keep enough API concurrency for token and revoke calls.

## Prepare and activate the matching configuration

From this configuration repository's `nix develop` shell, pin the exact
published, reviewed vpsAdmin revision through its existing channel:

```shell
confctl inputs channel set --commit vpsadmin vpsadmin APPROVED_CONSUMER_REVISION
```

The channel maps to `vpsadminServices`. Inspect the generated lock and changelog,
including the WebUI and notification-template inputs that follow this source.
Keep their own pins and the staging/production node channels unchanged. Retain
the preceding configuration, channel and system-generation identities for
rollback. Build and review the proxy and both API configurations before an
operator activates them.

Activate the proxy routing and logging protections before enabling documentation
OAuth on either API host. The production and maintenance API/auth routes go
directly to the existing HAProxy Unix backend, bypassing Varnish request/response
logging. These routes do not use the API metrics endpoint's 60-second Varnish
cache. TLS, ACME, DDNS aliases, maintenance responses, private API binds
and unrelated PHP/React/console routes remain in place.

Verify generated nginx configuration for trusted edge forwarding, access logs
without query strings, headers or bodies, and disabled sensitive error logging
on both HTTPS and HTTP redirects, including maintenance responses. Verify API
HAProxy request logging is disabled. These protections must apply before values
reach the application's callback checks; rejected requests can contain secrets
too. Errors rejected before nginx selects a virtual host are outside these
per-host logging controls.

Then activate the matching API package and hook on both hosts with the prepared
private files. Rolling instances can temporarily show different documentation;
verify the final source, hook, private-file readability and shared key on both
before accepting the rollout. A missing-file anonymous fallback is not proof
that credentialed sign-in was enabled correctly.

## Acceptance and rollback

After deployment, verify the installed package and configuration on both API
hosts, anonymous documentation and logs that omit secrets. Exercise real HTTPS
sign-in, callback, sign-out/revoke and expiry/relogin with a controlled account.
Check account entry and Switch user only if enabled. Development fixtures do
not certify the production provider, CA trust, routing or credentials. Preserve
only results and safe identifiers, never callback queries, cookies or tokens.

For software rollback, restore the preceding API bundle and authored hook
together: an older server cannot load documentation options it does not support.
Retain the client and private files/key for recovery. Keep direct protected
proxy routing while documentation OAuth is enabled. Removing the JSON from
the API runtime configuration makes documentation anonymous but does not revoke
already-issued tokens; revocation is a separate normal operator action.
This configuration introduces no database migration or coordinated node upgrade.
