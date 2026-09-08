# Prometheus annotation labels come from the query result

Initiative: `work/2026-09-07-vpsfstatus-index-stale-2/`.

The new promtool rule fixtures initially expected `$labels` inside alert
annotations to include static rule labels such as `severity` and `frequency`.
Promtool 3.12.0 showed that the annotation template receives the query result's
labels, while the emitted alert includes the additional rule labels.

Keep `severity` and `frequency` in `exp_labels`, but exclude them from an
expected `LABELS: {{ $labels }}` string unless the query itself supplied them.
The `absent_over_time(...{job="vpsf-status"}[5m])` branch produces just the
`job` query label. After correcting the expected annotation strings, all six
production-rule scenarios passed via
`nix build .#checks.x86_64-linux.vpsf-status-prometheus-rules --no-link -L`.
