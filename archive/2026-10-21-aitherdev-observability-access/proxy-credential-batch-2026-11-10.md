# Proxy credential batch, 2026-11-10

The installation and candidate-validation blocks were executed once after lead
release at 2026-11-10T15:47Z, both exit 0. Proxy switch and paced acceptance later
completed successfully under the lead's activation release; final post-check
was 2026-11-10T16:14:43Z. See the rollout receipt for exact results. Configuration source remains
`959e1d54cabc7ac5530dac6179acacb077a57754`; workspace guide remains `029a8866`.
Execution requires the lead's exact held typed proxy claim, verified mapping,
and explicit release of this batch. Lead owns service/profile activation.

Read-only refresh: `/var/lib/nginx-auth`, its dedicated password file, and the
aitherdev client directory/file are absent. `/var/lib` is root:root 0755 and
`/home/aither/.config` is aither:users 0755. Candidate binary and explicit config
are present remotely, root-owned, modes 0555 and 0444 respectively. Native
htpasswd/install/mktemp/mv/stat are available on the proxy.

Before mutation, all six status-only GET baselines returned 200:
`https://vpsfree.cz/`, `https://kb.vpsfree.cz/`, `https://kb.vpsfree.org/`,
`https://blog.vpsfree.cz/`, `https://blog.vpsfree.org/`, and
`https://newadmin.vpsfree.cz/healthz`. Bodies were discarded, no authentication
was supplied, and no credential was generated.

## Credential installation, after claim-bound release

Run as aither on aitherdev with tracing disabled. The first checks must still
find all dedicated paths absent; otherwise stop and report. The private client
file is installed first, so a subsequent remote failure retains the secret in
that file for authorized recovery. Do not automatically repeat a partially
successful batch. No existing credential is overwritten.

```bash
(
  set +x
  set -eu
  umask 077
  test "$(id -un)" = aither
  client_dir=/home/aither/.config/vpsfree-observability
  client_file=$client_dir/prometheus.curlrc
  for path in "$client_dir" "$client_file"; do
    test ! -e "$path"
    test ! -L "$path"
  done
  ssh -n -o BatchMode=yes -o StrictHostKeyChecking=yes root@proxy.prg.vpsfree.cz '
    set -e
    test ! -e /var/lib/nginx-auth
    test ! -L /var/lib/nginx-auth
    test ! -e /var/lib/nginx-auth/prometheus-codex.htpasswd
    test ! -L /var/lib/nginx-auth/prometheus-codex.htpasswd
  '
  mkdir -m 0700 "$client_dir"
  chgrp users "$client_dir"
  password_tmp=$(mktemp "$client_dir/.password.XXXXXX")
  client_tmp=$(mktemp "$client_dir/.curlrc.XXXXXX")
  trap 'rm -f -- "$password_tmp" "$client_tmp"' EXIT
  openssl rand -hex 32 > "$password_tmp"
  test "$(wc -c < "$password_tmp")" -eq 65
  {
    printf 'user = "codex-aitherdev:'
    tr -d '\n' < "$password_tmp"
    printf '"\nbasic\nfail\nsilent\nshow-error\nproto = "=https"\nproto-redir = "=https"\nconnect-timeout = 5\nmax-time = 45\n'
  } > "$client_tmp"
  chgrp users "$client_tmp"
  chmod 0600 "$client_tmp"
  mv -nT -- "$client_tmp" "$client_file"
  test ! -e "$client_tmp"
  ssh -o BatchMode=yes -o StrictHostKeyChecking=yes root@proxy.prg.vpsfree.cz '
    set -eu
    umask 077
    test ! -e /var/lib/nginx-auth
    test ! -L /var/lib/nginx-auth
    mkdir -m 0750 /var/lib/nginx-auth
    chown root:nginx /var/lib/nginx-auth
    server_tmp=$(mktemp /var/lib/nginx-auth/.prometheus-codex.XXXXXX)
    trap "rm -f -- \"$server_tmp\"" EXIT
    htpasswd -c -i -B -C 8 "$server_tmp" codex-aitherdev
    chown root:nginx "$server_tmp"
    chmod 0640 "$server_tmp"
    mv -nT -- "$server_tmp" /var/lib/nginx-auth/prometheus-codex.htpasswd
    test ! -e "$server_tmp"
    stat -c "%n %U:%G %a %F" /var/lib/nginx-auth /var/lib/nginx-auth/prometheus-codex.htpasswd
  ' < "$password_tmp"
  stat -c '%n %U:%G %a %F' "$client_dir" "$client_file"
)
```

The secret is 32 random bytes encoded as 64 hex characters. It is never assigned
to a shell/environment variable or printed: only private local files and SSH/
htpasswd stdin carry plaintext. The remote temporary file contains only the
bcrypt cost-8 record. Same-directory no-clobber renames make each final file
atomic. Human password files and SSH configuration are untouched.

## Candidate validation, under the same held claim

This validation may open/create normal nginx runtime files; it is authorized
only with the held claim and explicit batch release. It does not activate,
reload or restart any service. Emit the result only, without config/header dumps.

```bash
ssh -n -o BatchMode=yes -o StrictHostKeyChecking=yes root@proxy.prg.vpsfree.cz '
  if /nix/store/smpkfhyjj22b4zy1f0cprzfhr0nimllr-nginx-1.30.6/bin/nginx \
      -t -e stderr -c /nix/store/p8qz9fwjpfz2fwc1wbsigh86w1n4i27i-nginx.conf \
      >/dev/null 2>&1; then
    printf "candidate_nginx_validation=passed\n"
  else
    printf "candidate_nginx_validation=FAILED\n"
    exit 1
  fi
'
```

## Acceptance, only after the lead confirms activation

Use the private client config on both fixed mon1/mon2 HTTPS names. Pace requests
one second apart. GET instant and form POST use `count(up)` with `timeout=20s`;
GET range uses the same expression over ten minutes with a 60s step. Print only
JSON status, result type, series count and range sample count using jq. Require
successful vector/matrix responses, never print labels, samples or credentials.

Verify exact 401 for missing authentication, an intentionally invalid credential
from a disposable private curl config, and the real dedicated credential at each
human `/` route. Use `--no-fail --output /dev/null --write-out '%{http_code}'`
when overriding the real client's `fail` option for these denial checks; no
headers or verbose output. The wrong config contains only a known synthetic
invalid password and is removed afterwards. No load or mutation probes.

Repeat the six fixed public-site GETs above with bodies discarded and compare
their statuses to the saved 200 baseline. Retain only statuses/type/counts,
metadata, exact claim/config identities and phase outcomes in the rollout
receipt. Stop on any failure; do not retry or activate services independently.

```bash
(
  set +x
  set -euo pipefail
  umask 077
  client=/home/aither/.config/vpsfree-observability/prometheus.curlrc
  wrong=$(mktemp /home/aither/.config/vpsfree-observability/.invalid-test.XXXXXX)
  trap 'rm -f -- "$wrong"' EXIT
  printf '%s\n' 'user = "codex-aitherdev:invalid-acceptance-only"' basic > "$wrong"
  for host in mon1.prg.vpsfree.cz mon2.prg.vpsfree.cz; do
    printf '%s GET instant\n' "$host"
    curl -q --config "$client" --get --data-urlencode 'query=count(up)' \
      --data-urlencode 'timeout=20s' "https://$host/codex/api/v1/query" |
      jq -ce 'select(.status == "success" and .data.resultType == "vector" and (.data.result|length) > 0) | {status, type:.data.resultType, series:(.data.result|length)}'
    sleep 1
    range_end=$(date -u +%s)
    range_start=$((range_end - 600))
    printf '%s GET range\n' "$host"
    curl -q --config "$client" --get --data-urlencode 'query=count(up)' \
      --data-urlencode "start=$range_start" --data-urlencode "end=$range_end" \
      --data-urlencode 'step=60s' --data-urlencode 'timeout=20s' \
      "https://$host/codex/api/v1/query_range" |
      jq -ce 'select(.status == "success" and .data.resultType == "matrix" and (.data.result|length) > 0 and (([.data.result[].values|length]|add // 0) > 0)) | {status, type:.data.resultType, series:(.data.result|length), samples:([.data.result[].values|length]|add // 0)}'
    sleep 1
    printf '%s POST instant\n' "$host"
    curl -q --config "$client" --data-urlencode 'query=count(up)' \
      --data-urlencode 'timeout=20s' "https://$host/codex/api/v1/query" |
      jq -ce 'select(.status == "success" and .data.resultType == "vector" and (.data.result|length) > 0) | {status, type:.data.resultType, series:(.data.result|length)}'
    sleep 1
    code=$(curl -q --silent --show-error --proto '=https' --connect-timeout 5 \
      --max-time 10 --output /dev/null --write-out '%{http_code}' \
      "https://$host/codex/api/v1/query")
    printf '%s missing_auth=%s\n' "$host" "$code"
    test "$code" = 401
    sleep 1
    code=$(curl -q --config "$wrong" --silent --show-error --proto '=https' \
      --connect-timeout 5 --max-time 10 --output /dev/null \
      --write-out '%{http_code}' "https://$host/codex/api/v1/query")
    printf '%s wrong_auth=%s\n' "$host" "$code"
    test "$code" = 401
    sleep 1
    code=$(curl -q --config "$client" --no-fail --output /dev/null \
      --write-out '%{http_code}' "https://$host/")
    printf '%s dedicated_at_human_root=%s\n' "$host" "$code"
    test "$code" = 401
    sleep 1
  done
  for url in https://vpsfree.cz/ https://kb.vpsfree.cz/ https://kb.vpsfree.org/ \
      https://blog.vpsfree.cz/ https://blog.vpsfree.org/ \
      https://newadmin.vpsfree.cz/healthz; do
    code=$(curl -q --silent --show-error --proto '=https' --connect-timeout 5 \
      --max-time 10 --output /dev/null --write-out '%{http_code}' "$url")
    printf '%s HTTP=%s\n' "$url" "$code"
    test "$code" = 200
  done
)
```
