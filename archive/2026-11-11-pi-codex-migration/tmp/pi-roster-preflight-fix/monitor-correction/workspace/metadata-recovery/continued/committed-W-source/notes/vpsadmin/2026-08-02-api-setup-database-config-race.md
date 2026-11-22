# vpsAdmin API setup can expose a passwordless database configuration

## Symptom

An integration helper using `VpsadminServices#api_ruby_json` can fail
sporadically with:

```text
Access denied for user 'api'@'127.0.0.1' (using password: NO)
```

The same helper can succeed seconds earlier, and direct MariaDB probes with
the test password continue to work.

## Cause

`nixos/modules/vpsadmin/api-app.nix` generates `database.yml` with
`password: #dbpass#`. Its setup script first copies this template into the
shared live configuration and then substitutes the password with `sed`.

API rake services invoke that setup from `preStart`. The setup lock serializes
writers, but readers such as the integration test's standalone Ruby process do
not take the lock. A reader can therefore load `database.yml` between the copy
and substitution. YAML treats `#dbpass#` as a comment and supplies a null
password.

## Evidence

In vpsAdmin event-branch CI run `30719120204`, the failing helper began at
01:40:37 and `vpsadmin-api-monitoring-check.service` began at 01:40:38. The
helper failed at 01:40:41 with `using password: NO`; earlier helper calls and
credentialed SQL probes in the same VM succeeded.

## Fix direction

Build the complete credential-substituted file privately and atomically rename
it into place while retaining the existing writer lock. Do the same for other
live configuration files assembled through copy-then-edit if concurrent
readers can observe them.

Related initiative: `work/2026-06-15-vpsadmin-events/`.
