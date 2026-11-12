# Production observability

Required workspace procedure, selected by the routing table in `AGENTS.md`.
Its rules retain workspace scope and precedence. Paths and commands are relative
to the coordination workspace unless the text specifies another repository.

Before investigating production metrics, read the configuration repository's
[Prometheus query access guide](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/master/docs/operations/prometheus-query-access.md).
Its source is `docs/operations/prometheus-query-access.md` in the canonical
`repos/vpsfree-cz-configuration.git` repository. It owns endpoint, credential,
retention, API limits and recovery guidance. Check this documented route before
guessing endpoints, trying raw Prometheus ports or looking for SSH access.

On aitherdev, use the existing private curl config at
`/home/aither/.config/vpsfree-observability/prometheus.curlrc` (mode `0600`).
The dedicated API base is `https://mon1.prg.vpsfree.cz/codex/api/v1`; the guide
also documents mon2 and the monitors' different retention limits. A small
read-only access check is:

```sh
curl -q --config /home/aither/.config/vpsfree-observability/prometheus.curlrc \
  https://mon1.prg.vpsfree.cz/codex/api/v1/status/buildinfo
```

Keep `-q` as curl's first option to suppress the default curlrc. Never print the
private config or put credentials in arguments, environment variables, URLs,
logs or chat. Keep certificate verification enabled; do not add redirect
following or verbose/trace output. For PromQL, follow the guide's query examples,
use `timeout=20s`, and bound time ranges and response sizes.

If the config is missing/unreadable or the request fails, report the access
blocker and consult the guide. Credential provisioning, rotation and deployment
are separate operations; do not alter credentials or production configuration
as part of ordinary metrics discovery.
