# Read central logs and monitoring metrics

Run these commands as `aither` on aitherdev. They require the deployed
`log-reader` account and dedicated monitoring access. The logger uses the existing
aitherdev SSH machine identity. Monitoring uses the private curl config at
`/home/aither/.config/vpsfree-observability/prometheus.curlrc`.
If either prerequisite is missing, ask the maintainer to complete access setup.

For account setup, historical permissions, credentials, revocation and recovery,
use the configuration runbooks:

- [Log reader access](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/959e1d54cabc7ac5530dac6179acacb077a57754/docs/operations/log-reader-access.md)
- [Prometheus query access](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/959e1d54cabc7ac5530dac6179acacb077a57754/docs/operations/prometheus-query-access.md)

## Read logger logs

Use the full hostname `log.int.prg.vpsfree.cz` and the `log-reader` account.
Read a bounded part of one current node log:

```sh
ssh -T log-reader@log.int.prg.vpsfree.cz \
  'tail -n 100 /var/log/remote/cz.vpsfree/nodes/prg/node1/log'
```

Replace the location and node with the host under investigation. Date-suffixed
archives use `log-YYYYMMDD`; replace `YYYYMMDD` with the rotation date. Search
only the last 500 lines of one archive:

```sh
ssh -T log-reader@log.int.prg.vpsfree.cz \
  'tail -n 500 /var/log/remote/cz.vpsfree/nodes/prg/node1/log-YYYYMMDD | grep -F -- "search text"'
```

Read the logger's local messages or the combined node runit/svlogd stream:

```sh
ssh -T log-reader@log.int.prg.vpsfree.cz 'tail -n 100 /var/log/messages'
ssh -T log-reader@log.int.prg.vpsfree.cz 'tail -n 100 /var/log/remote/localhost/log'
```

The combined stream identifies nodes in the messages. Local messages
archives are `/var/log/messages-YYYYMMDD`; select one date and use the same
bounded `tail` approach. Keep searches to the relevant host, file and time range.
Logs are readable without redaction, so avoid copying unrelated contents into
reports.

The account cannot directly modify protected logs. It is an ordinary unprivileged
shell that can write its home and `/tmp`, run programs and connect outbound.
SSH forwarding and PTYs are disabled. Other processes using the same account
share its access.

## Fetch monitoring metrics

Each address queries its own monitor:

- `https://mon1.prg.vpsfree.cz/codex/api/v1`
- `https://mon2.prg.vpsfree.cz/codex/api/v1`

Use the dedicated curl config for authentication. It must be owned by `aither`,
mode `0600`, in its private directory at mode `0700`. Its contents are private;
do not print them or put the credential in a URL, command argument, environment
variable or report. Other processes and sessions running as `aither`, and root,
can read this file.

Query the last ten minutes on mon1 with a 60s step:

```sh
range_end=$(date -u +%s)
range_start=$((range_end - 600))
curl -q --config /home/aither/.config/vpsfree-observability/prometheus.curlrc \
  --get --data-urlencode 'query=up' \
  --data-urlencode "start=$range_start" --data-urlencode "end=$range_end" \
  --data-urlencode 'step=60s' --data-urlencode 'timeout=20s' \
  https://mon1.prg.vpsfree.cz/codex/api/v1/query_range
```

Send a form query to mon2:

```sh
curl -q --config /home/aither/.config/vpsfree-observability/prometheus.curlrc \
  --data-urlencode 'query=sum(up)' --data-urlencode 'timeout=20s' \
  https://mon2.prg.vpsfree.cz/codex/api/v1/query
```

Keep `-q` first so curl skips its default config. Use fixed HTTPS addresses,
normal certificate verification and the explicit private config. Do not add
redirect following, verbose/trace output or `--insecure`. Choose the smallest
useful time range and query; `timeout=20s` does not impose a hard proxy CPU budget.

The credential permits the query and selected discovery/diagnostic routes in
the runbook, without metric redaction or tenant isolation. It does not grant
administrative API or human UI access. Both monitors share a budget of 2
requests/s and 4 active requests; excess requests return 429. Reduce request
frequency rather than retrying in a burst. For authentication failures or
missing log access, ask the maintainer to check the linked setup and recovery
instructions.
