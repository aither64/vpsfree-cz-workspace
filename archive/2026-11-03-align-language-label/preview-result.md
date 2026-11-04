# Running API documentation preview

Current preview: <http://172.16.106.40:4567/v1.0/?doc_lang=en>.
Open the gear beside the API name to inspect Language above Theme. Czech:
<http://172.16.106.40:4567/v1.0/?doc_lang=cs>.

The preview remains running under this session's managed service registry.
No stop or cleanup is scheduled. No application source, configuration,
integration or release changed.

## Current service on port 4567

The user identified port 4567 as reachable in another preview, and the lead
explicitly assigned a second managed service there. Rechecked with
`ss -ltn '( sport = :4567 )'`: no listener before launch. Verified current/env
identity and exact source head `b606b4b3c32bf05779c05babeaa1c31a33dee6fa`.
No peer session records or worktrees were accessed.

- Service label: `HaveAPI language label preview port 4567`.
- Service ID: `e60a076c-4d7d-4b97-ad97-46b03edf019e`.
- Unit: `workspace-session-e60a076c-4d7d-4b97-ad97-46b03edf019e.service`.
- Registry: `1871982c-e773-4559-ad8c-639324006c43`.
- CWD: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-align-language-label/haveapi/servers/ruby`.
- Command: `/run/current-system/sw/bin/nix develop .#server-ruby -c bundle exec ruby test_support/client_test_server.rb --bind 0.0.0.0 --port 4567`.
- Launch: public `dev-session service run` under this verified session.
- Logs: `journalctl --user -u workspace-session-e60a076c-4d7d-4b97-ad97-46b03edf019e.service`.

Verification on 2026-11-04: `GET /__health` returned HTTP 200 and `ok`;
`GET /v1.0/?doc_lang=en` returned HTTP 200 with the native Language label;
its linked CSS returned HTTP 200 and exactly matched the worktree bytes,
including the corrected selector/margin. SHA-256:
`5d9a9bf0ccd821921c81552c5048e6b5f28477e6f4486e93d7feae16d4059542`.
No environment workaround, source edit, firewall/proxy/configuration change,
test campaign or service stop was needed. The original port-18761 service is
untouched and remains running. The prior access investigation below describes
that blocked port; it does not apply to the newly selected port 4567.

## Original service on port 18761

- Verified session: `2026-11-03-align-language-label`; environment and trusted
  thread binding match `/home/aither/workspace/ai/vpsfree.cz`.
- Source revision: `b606b4b3c32bf05779c05babeaa1c31a33dee6fa`, clean worktree.
- Service label: `HaveAPI language label preview`.
- Service ID: `1fd4affd-9359-4f0e-b32a-cbbfc2ef5b92`.
- Registry ID: `1871982c-e773-4559-ad8c-639324006c43`.
- Unit: `workspace-session-1fd4affd-9359-4f0e-b32a-cbbfc2ef5b92.service`.
- Invocation: `92634d8e1bdd4ca2b9cfa2a24ef83c15`.
- Bind: `0.0.0.0:18761`; port was unused before launch.
- CWD: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-align-language-label/haveapi/servers/ruby`.
- Command: `/run/current-system/sw/bin/nix develop .#server-ruby -c bundle exec ruby test_support/client_test_server.rb --bind 0.0.0.0 --port 18761`.
- Created with public `dev-session service run` and the service ID above.
- Logs: `journalctl --user -u workspace-session-1fd4affd-9359-4f0e-b32a-cbbfc2ef5b92.service`.
- Runtime status: managed registry `running`; systemd `active/running`.

This is the existing `HaveAPI::ClientTestAPI` fixture, using in-memory sample
projects/tasks and fixture users. It loads the actual server library and public
assets from this worktree. It uses no production data or credentials.

## Verification

On 2026-11-04, the existing prepared Nix shell fetched missing cached inputs,
constructed small shell/PHP wrappers, and started the fixture in approximately
23 seconds. No long build or additional test campaign was needed.

- `GET /__health`: HTTP 200, body `ok`.
- `GET /v1.0/?doc_lang=en`: HTTP 200; Language label retains
  `for="docs-language"` and the native select retains that ID. Language appears
  before Theme.
- `GET /v1.0/?doc_lang=cs`: HTTP 200 with the localized `Jazyk` label.
- The page links to `/css/documentation.css?v=5d9a9bf0ccd821921c81552c5048e6b5f28477e6f4486e93d7feae16d4059542`.
  That asset returns HTTP 200 and exactly equals the worktree CSS, including
  `.docs-sidebar [data-documentation-language] label` and `margin: 0 0 .4rem`.
- Served/source CSS SHA-256:
  `5d9a9bf0ccd821921c81552c5048e6b5f28477e6f4486e93d7feae16d4059542`.

The URL was verified from the development host using its bridge address.
Remote browser network reachability has not been independently tested.
`aitherdev.int.vpsfree.cz` resolves locally through `/etc/hosts`, but its Host
header is rejected by Sinatra's development HostAuthorization with HTTP 403
(`Host not permitted`). The IP URL is verified and avoids a source change or
stopping/restarting any service. Lead has been notified of the hostname limit.

## Firewall/exposure follow-up

The existing API service remains running with its original ID and command.
No new proxy service, firewall change, system configuration edit, package
deployment, service stop or lifecycle action was performed.

Read-only findings:

- Active Nginx configuration:
  `/nix/store/j1jvhxfsdzybjfb3qj57i4la4lxmi7ii-nginx.conf`.
  HTTPS on `172.16.106.40:443` accepts workspace hostnames under
  `*.workspace.aitherdev.int.vpsfree.cz` and proxies all requests to
  `/run/dev-workspaces/router.sock`, behind the existing Basic authentication.
  There is no dynamic per-port preview location or user-writable include.
- Installed package observed through `workspace-host status`:
  `/nix/store/myjy32qh6bd4avgym1awx180y29nvwz9-dev-workspace-0.2.0`.
  Public `dev-session --help` exposes service run/list/stop, but no forwarding
  operation. Installed `workspace-portal router -h` accepts only registry,
  runtime directory and Unix socket. Its `serve -h` has no preview proxy option.
- The installed `run_router` launcher and canonical runtime
  `portal/cmd/workspace-portal/router.go` show workspace hostname lookup and a
  fixed `<runtime>/<workspace>/portal.sock` destination. Canonical
  `docs/workspace-portal.md` workspace-configuration guidance describes portal
  hostname/alias registration, not arbitrary backend registration. No peer
  session records or worktrees were read.

A second local managed proxy would still lack an ingress route through the
existing HTTPS listener. Creating such a route would require an explicitly
approved host configuration change, outside this assignment.

Shortest zero-host-change alternative, requiring the user's existing SSH access:

```sh
ssh -N -L 18761:127.0.0.1:18761 aither@aitherdev.int.vpsfree.cz
```

Then open <http://localhost:18761/v1.0/?doc_lang=en>. This command must run on
the user's computer; no SSH connection or tunnel was launched on the host.
Use the user's existing SSH alias/account if it differs. Host-local requests
with `Host: localhost:18761` returned HTTP 200 for both documentation and the
HTML-linked stylesheet, with the exact corrected CSS digest recorded above.
Actual user-side tunnel reachability has not yet been verified.

For browser-only access without an SSH tunnel, the lead must obtain separate
direction for a narrowly scoped temporary HTTPS ingress route or a restricted
firewall allowance. Neither is implemented or authorized by this investigation.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-align-language-label/)
