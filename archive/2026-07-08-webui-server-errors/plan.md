# 2026-07-08-webui-server-errors

## Goal

Notify operators when vpsAdmin WebUI produces server-side errors. Today the
fatal PHP errors and backtraces are visible in the webui hosts'
`nginx.service` journal, but there is no alerting signal.

## Affected repositories

- `vpsfree-cz-configuration`
  - Prometheus scrape jobs and alert rules live under
    `modules/clusterconf/monitor`.
  - `int.log` rsyslog and syslog-exporter deployment live in
    `cluster/cz.vpsfree/containers/prg/int.log/config.nix`.
  - The production WebUI hosts are `webui1.int.vpsfree.cz` and
    `webui2.int.vpsfree.cz`.
- `syslog-exporter`
  - Already converts central syslog events to Prometheus metrics.
  - Needed if we want content-specific detection of existing nginx/PHP log
    messages.
- `ssh-exporter`
  - Similar small Ruby exporter with no existing spec harness. It should get
    the same baseline RSpec/CI support before adding more syslog-exporter
    behavior.
- `vpsadmin`
  - PHP WebUI warnings/notices from `webui1-nginx-journal.txt` are fixed here.
  - The WebUI package is deployed through `vpsadminServices` in
    `vpsfree-cz-configuration`, but no configuration pin update is planned
    until the code branch is pushed/merged.

## Approach

Current findings:

- The vpsAdmin WebUI PHP-FPM pool sends PHP errors to stderr and nginx reports
  FastCGI stderr in `nginx.service`. The uploaded sample confirms the relevant
  errors are visible in the nginx journal, not the php-fpm service journal.
- NixOS machines forward syslog to `int.log` via rsyslog. `int.log` writes logs
  to disk and mirrors them to `syslog-exporter` through a named pipe.
- Prometheus already scrapes `syslog-exporter` as job `log` every 60 seconds.
- `syslog-exporter` currently has a generic
  `syslog_message_count{program,alias,fqdn}` counter and several custom alert
  flares for kernel/osctld/nodectld/lxc/ZFS events.
- Existing vpsAdmin alerts check service state and blackbox HTTP success, but
  they do not catch intermittent user-triggered HTTP 500/server errors.
- Uploaded sample:
  `/home/aither/workspace/ai/vpsfree.cz/webui1-nginx-journal.txt`.
  It contains many nginx error-level lines that are not alert-worthy:
  PHP warnings, missing `robots.txt`, scanner probes, and handled validation
  exceptions. It also contains fatal PHP errors such as
  `PHP message: PHP Fatal error:  Uncaught Error: ...` and
  `PHP message: PHP Fatal error:  Uncaught TypeError: ...`.
- Some handled application errors, e.g.
  `HaveAPI\Client\Exception\ValidationError`, include a stack trace in nginx
  output but are not fatal PHP errors. The collector must not alert just
  because a line contains `Stack trace`.

## Selected solution

Before implementing WebUI fatal-error monitoring, add generic RSpec support,
baseline coverage, and GitHub Actions RSpec workflows to both `syslog-exporter`
and `ssh-exporter`. Commit those prerequisite changes first.

## Spec support prerequisite

Add to both exporters:

- `rspec` as a development dependency in `Gemfile`;
- `.rspec`;
- `spec/spec_helper.rb`;
- focused specs for current behavior;
- `.github/workflows/rspec.yml` running `bundle exec rspec` on push and pull
  request, plus `workflow_dispatch`.

Suggested `syslog-exporter` coverage:

- `SyslogExporter::Config`
  - loads `syslog_pipe`, default `pipe_size`, host alias/FQDN/OS fields;
  - honors explicit `pipe_size`.
- `SyslogExporter::Parser`
  - parses RFC5424-style lines forwarded by rsyslog;
  - extracts `program` and `pid`;
  - returns `KernelMessage` for kernel program names;
  - parses the `localhost`/`svlogd -tt` format documented in the parser;
  - drops the first possibly incomplete line in `each_message`;
  - warns and skips malformed lines.
- `SyslogExporter::KernelMessage`
  - extracts syslog namespace tags used by kernel metrics.
- Collector behavior
  - `MessageCount` increments with `program` and host labels;
  - `LxcStart` detects generic failed starts and netns-limit failures and
    extracts container IDs;
  - `Nodectld`, `Osctld`, `Zfs`, and `Kernel` match their documented log
    signatures and ignore unrelated messages;
  - flare renewal/settling resets gauges.
- `SyslogExporter::Processor`
  - routes messages to collectors by configured host name or FQDN. This can be
    covered with light test doubles, without opening the pipe.

Suggested `ssh-exporter` coverage:

- `SshExporter::Config`
  - loads host alias/FQDN/user/private key fields;
  - defaults `interval` to 60 and `timeout` to 30;
  - honors explicit `interval` and `timeout`;
  - raises clearly when required host fields are absent.
- `SshExporter::Collector`
  - registers all expected Prometheus gauges with `alias` and `fqdn` labels;
  - on a successful SSH check, sets `ssh_host_up`, `ssh_host_last_check`,
    `ssh_host_check_seconds`, and load-average gauges from `/proc/loadavg`;
  - on a failed SSH check, sets `ssh_host_up` to 0 and leaves load-average
    gauges unchanged;
  - builds the SSH command from the host config, including timeout, user,
    private key, and FQDN.
- `SshExporter::Rackup`
  - optionally smoke-test that the Rack app builds with a temporary config and
    a stubbed collector.

Workflow shape:

- Keep workflows small and similar in both repos.
- Use current upstream versions of imported GitHub Actions after verification.
- Run on Ubuntu with Ruby 3.1 or newer, matching gemspecs.
- Cache gems through the Ruby setup action if used.

## WebUI fatal-error monitoring

Proceed with solution 1: extend `syslog-exporter` with a vpsAdmin WebUI
fatal-error collector and add Prometheus alerts in `vpsfree-cz-configuration`.

Implementation shape:

- Add a `SyslogExporter::Collectors::VpsadminWebui` collector.
- Scope it to production WebUI hosts by host identity:
  `webui1.int.vpsfree.cz` and `webui2.int.vpsfree.cz` (aliases
  `webui1.int` and `webui2.int`).
- Scope matching to nginx-originated messages. The sample format is
  `program=nginx` and message contains `FastCGI sent in stderr`.
- Count only fatal PHP errors, initially matching:
  - `PHP message: PHP Fatal error:`
  - `PHP message: PHP Parse error:`
  - `PHP message: PHP Recoverable fatal error:`
  - fatal resource-limit messages if present, e.g. `Allowed memory size` or
    `Maximum execution time`, only when logged as PHP fatal errors.
- Do not count:
  - `PHP Warning`, `PHP Notice`, `PHP Deprecated`, or `PHP Strict Standards`;
  - nginx static-file/probe errors such as missing `robots.txt` or WordPress
    scanner paths;
  - handled HaveAPI validation/action errors, even when the log line includes
    `Stack trace`;
  - stack trace continuation lines following a fatal error. Only the first line
    containing the fatal signature should increment the metric.
- Expose both:
  - a counter, e.g. `syslog_vpsadmin_webui_fatal_error_count`, labelled by
    existing host labels and a bounded `error_type` label such as
    `fatal`, `parse`, or `recoverable_fatal`;
  - a short-lived flare gauge, e.g. `syslog_vpsadmin_webui_fatal_error == 1`,
    to match existing syslog alert patterns.
- Add alert rules under `modules/clusterconf/monitor/rules/syslog.nix` or
  `modules/clusterconf/monitor/rules/vpsadmin.nix`:
  - warning on any flare;
  - optionally critical on repeated events, e.g. an increase over a short
    window once real event volume is known.
- Release/bump `syslog-exporter` in `vpsfree-cz-configuration` and build
  `int.log` plus a monitor.

## WebUI PHP warning cleanup

The follow-up WebUI cleanup targets warning signatures extracted from
`webui1-nginx-journal.txt`. Most lines come from first-render filter forms that
read optional `$_GET` keys directly. Smaller clusters come from first-render
POST defaults, optional template variables, and missing helper guard clauses.

Implementation shape:

- In `vpsadmin/webui`, replace direct optional `$_GET`/`$_POST` reads with
  existing helpers such as `get_val()`, `post_val()`, `api_get()`, or null
  coalescing where appropriate.
- Preserve current form behavior: absent filters remain empty/default, present
  filters keep their selected values, and failed POST submissions still
  redisplay submitted values.
- Guard optional template fragments such as `AJAX_SCRIPT` with an empty string
  default before appending JavaScript.
- Make shared helper code tolerate missing API parameter metadata where callers
  may ask for optional forms.
- Add focused PHPUnit regression coverage for helper behavior or high-volume
  warning paths where it can be tested without browser VM startup.
- Do not change API contracts, database schemas, or deployment configuration in
  this code-only cleanup.

## Compatibility and deployment

- No persisted state, database schema, API contract, generated client, or
  protocol changes are needed for any option or for the WebUI warning cleanup.
- The selected solution changes only the central `syslog-exporter` package and
  alert rules.
  Mixed-version behavior is safe: before `int.log` receives the new exporter,
  new alert expressions are absent/no-op. Rollback removes the new metrics and
  alerts stop firing.
- The WebUI cleanup only changes missing optional request values from PHP
  warnings to the same empty/default form state. Mixed-version operation is
  safe; old and new WebUI instances can run side by side during rollout.
- The parser is intentionally conservative. It may miss non-PHP infrastructure
  5xx failures, but it should avoid warning noise and handled validation errors.
- None of these require coordinated vpsAdminOS node updates.

## Testing plan

- For `syslog-exporter` changes:
  - Add unit-level coverage or a small parser/collector regression test.
  - Feed representative syslog lines based on
    `webui1-nginx-journal.txt` for:
    - nginx FastCGI `PHP Fatal error` lines;
    - fatal lines preceded by PHP warnings in the same nginx message;
    - PHP warning-only lines;
    - handled `HaveAPI\Client\Exception\ValidationError` stack traces;
    - unrelated nginx file-not-found/scanner messages.
  - Verify the metric names and labels with a local Rack/Puma run if practical.
- For `vpsfree-cz-configuration` changes:
  - Run `nixfmt` on touched Nix files.
  - Enter `nix develop` and run a targeted `confctl build` for
    `cz.vpsfree/containers/prg/int.log` and one monitor, e.g.
    `cz.vpsfree/containers/prg/int.mon1`.
- After intended code changes and quick verification, run the workspace
  mandatory change review skill before long integration tests.
- For `vpsadmin` WebUI cleanup:
  - Run focused PHPUnit regression tests under `webui`.
  - Run `composer test --working-dir=webui` if dependencies are available.
  - Run PHP CS Fixer/Overcommit before commit.
  - Use browser integration tests only if the fix changes visible user
    workflows beyond default form state.
