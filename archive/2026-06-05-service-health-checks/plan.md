# Service health checks

## Goal

Extend machine health checks in `vpsfree-cz-configuration` so important
services are tested beyond "the machine is up" and, where useful, beyond "the
systemd unit is active". HTTP services should fetch a local or proxied URL and
match a stable response string. Netboot servers should also assert that the
HTTP side of netboot is running.

## Affected repositories

- `vpsfree-cz-configuration`
  - Branch: `2026-06-05-service-health-checks`
  - Worktree:
    `worktrees/2026-06-05-service-health-checks/vpsfree-cz-configuration`
  - Base: `origin/master` at
    `6f2934dac1bfb77693a55e6a5e545707c57ed120`
- `confctl`
  - Branch: `2026-06-05-service-health-checks`
  - Worktree: `worktrees/2026-06-05-service-health-checks/confctl`
  - Base: `origin/master` at
    `af164b442100b92b8d93c0d67b315eff982e0180`

No changes are expected in `vpsadmin` or monitoring exporters. The existing
machine health check schema already supports systemd property checks and
commands with output matching.

## Review decisions

- First implementation is limited to vpsAdmin/confctl machine health checks.
  Prometheus blackbox body matching is deferred.
- First pass includes core services plus low-risk extra checks for Grafana,
  rubygems, paste, and utils.
- Proxy coverage checks both the main website and KB through local HTTPS nginx
  routing.
- `confctl` should preserve literal argv over SSH; shell syntax must be
  explicit through `sh -c`.
- `confctl health-check` should skip non-runnable carried machines such as
  `cz.vpsfree/machines/nixos-live`.

## Current configuration notes

- Reusable health checks live under `health-checks/`.
- `health-checks/vpsadmin/api.nix`, `webui.nix`, and `rabbitmq.nix` already use
  command output checks, so extending HTTP checks with `curl` and
  `standardOutput.include` follows local style.
- `health-checks/monitoring.nix` currently checks only
  `prometheus.service`.
- `health-checks/alerts.nix` currently checks only `alertmanager.service` and
  `sachet.service`.
- `int.munin` already fetches `http://localhost` and matches `Munin` and
  `</html>`.
- `int.web`, `int.kb`, `int.utils`, and `prg/int.grafana` currently have no
  machine health checks.
- `int.rubygems`, `int.paste`, `int.vpsfbot`, and `discourse` have unit-state
  checks but no content checks.
- `prg/proxy` currently checks only `nginx.service`.
- Netboot/carrier machines `build`, `prg/apu`, and `brq/apu` check
  `netboot-atftpd.service`; they do not check `nginx.service`.
- Prometheus blackbox HTTP probes in `modules/clusterconf/monitor/http.nix`
  cover several public URLs, but currently validate only HTTP status. They do
  not check response content and do not cover every public vhost.

## Implemented phase 1

Extend machine health checks:

- Add a small local pattern for HTTP command checks:
  `curl --fail --silent --show-error --max-time 10`, with `Host` headers or
  `--resolve` where needed, and `standardOutput.include` for stable strings.
- Extend `health-checks/monitoring.nix`:
  - keep `prometheus.service`;
  - add a local Prometheus readiness or health endpoint check;
  - match the documented ready/healthy response text, verified during
    implementation.
- Extend `health-checks/alerts.nix`:
  - keep `alertmanager.service` and `sachet.service`;
  - add a local Alertmanager ready/healthy or UI check;
  - keep Sachet at unit-state only unless a stable unauthenticated health
    endpoint is found.
- Add checks to `cluster/cz.vpsfree/containers/int.web/module.nix`:
  - `nginx.service` active;
  - PHP-FPM pool unit active after verifying the evaluated unit name;
  - local HTTP checks for `vpsfree.cz` and `vpsfree.org`, matching stable page
    strings.
- Add checks to `cluster/cz.vpsfree/containers/int.kb/module.nix`:
  - `nginx.service` active;
  - Dokuwiki PHP-FPM pool unit(s) active after verifying evaluated unit names;
  - local HTTP checks for `kb.vpsfree.cz` and `kb.vpsfree.org`, matching
    `Znalostní báze` and `Knowledge base` or another stable rendered string.
- Extend `cluster/cz.vpsfree/containers/prg/proxy/module.nix`:
  - keep `nginx.service`;
  - add at least one end-to-end HTTPS check through local nginx using
    `curl --resolve vpsfree.cz:443:127.0.0.1 https://vpsfree.cz/...`;
  - match content from a public page. This tests TLS/vhost routing, the proxy,
    and an upstream service.
- Extend netboot machine checks in:
  - `cluster/cz.vpsfree/machines/build/module.nix`;
  - `cluster/cz.vpsfree/machines/prg/apu/module.nix`;
  - `cluster/cz.vpsfree/machines/brq/apu/module.nix`.
  Add `nginx.service` active. Consider a second pass with a deterministic HTTP
  fetch from the generated netboot tree if a stable URL is identified.
- Add focused checks for other service containers where the endpoint is stable:
  - `prg/int.grafana`: `grafana.service` and `/api/health`;
  - `int.rubygems`: `geminabox.service` plus local root or API check;
  - `int.paste`: existing Bepasty service plus local root content check;
  - `int.utils`: `nginx.service`, Adminer PHP-FPM unit after verification, and
    `/adminer/adminer.php` content check;
  - `discourse`: deferred to avoid adding a potentially heavier or flakier
    application-level check in the first pass.

Fix `confctl` runtime behavior required by these checks:

- Remote command execution shell-quotes the command argv into one SSH remote
  command string, preserving arguments containing spaces.
- Health-check selection uses runnable machines and avoids carried machines or
  machines without a direct target.
- Internal call sites that intentionally use shell syntax invoke `sh -c`
  explicitly.
- The config branch pins fixed `confctl` revision `7e8b7c9b` and uses explicit
  Host headers for local vhost curl checks.
- The rubygems check matches `Gem in a Box`.

## Implemented phase 2

Extend Prometheus blackbox HTTP probes with response-body validation:

- Add optional `bodyMatches` regex lists to
  `modules/clusterconf/monitor/http.nix`.
- Render `bodyMatches` into generated blackbox exporter modules using
  `fail_if_body_not_matches_regexp`.
- Add body checks for existing public probes: vpsFree registration pages,
  vpsAdmin API, console asset, web UI, and `status.vpsf.cz`.
- Add unauthenticated public probes for KB CZ/EN, rubygems, paste, Discourse,
  Munin, and public Grafana.
- Add warning-level alerts for the new public-service blackbox jobs and update
  existing HTTP probe annotations so content mismatch is described as an
  unexpected HTTP response, not only as a service being down.
- Keep basic-auth, dev, webhook-only, and legacy/external proxy vhosts out of
  scope for this pass.

## Compatibility and deployment

- The primary changes are metadata consumed by vpsAdmin/confctl health checks
  and Prometheus blackbox monitoring.
  No persistent state, database schema, API contract, generated client, or
  protocol format changes are expected.
- Rollout can be incremental per machine. Old deployed systems ignore the
  source changes until rebuilt/deployed; new health checks can begin reporting
  failures immediately after the configuration is deployed.
- Rollback is simple: deploy the previous configuration. No state written by
  new checks needs to be read by old code.
- Main operational risk is false positives from brittle response strings,
  redirects, local-only firewall behavior, or checks that are too slow. Prefer
  stable health endpoints or page titles and short timeouts, and avoid
  authenticated public endpoints in the first pass.
- No coordinated vpsAdminOS node update is required.
- The `confctl` argv change intentionally makes `confctl ssh` and health-check
  commands literal argv interfaces. Operators who need remote shell features
  should use `sh -c '...'`.

## Validation plan

- Format changed Nix files with `nixfmt`.
- For `confctl`, run `bundle exec rspec`, `bundle exec rubocop`,
  `overcommit --run`, and `./test-runner.sh test deploy/flakes`.
- Build a focused set of affected machines:
  - `confctl build "cz.vpsfree/containers/prg/int.mon{1,2}"`
  - `confctl build "cz.vpsfree/containers/prg/int.alerts{1,2}"`
  - `confctl build "cz.vpsfree/containers/int.{web,kb,utils,rubygems,paste}"`
  - `confctl build "cz.vpsfree/containers/prg/{proxy,int.grafana}"`
  - `confctl build "cz.vpsfree/machines/{build,prg/apu,brq/apu}"`
- If blackbox content checks are included, build both monitor nodes:
  `confctl build "cz.vpsfree/containers/prg/int.mon{1,2}"`.
- Before committing, enter the repo dev shell with `nix develop` so Overcommit
  has the required Ruby gems, then run the installed hooks through a normal
  commit workflow.

## Open follow-up

- Full netboot machine build validation requires a local or deploy-time
  environment where `/srv/iso-images/systemrescue-11.01-amd64.iso` exists.
- Live health-check validation requires an environment with accepted SSH host
  keys/access to the production targets.
