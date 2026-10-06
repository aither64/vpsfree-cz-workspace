# vpsAdmin integration test Mailpit

Goal: capture vpsAdmin integration-test email delivery through Mailpit so tests
can assert that queued mail reaches SMTP, not only that `mail_logs` rows exist.

Affected components:

- vpsadmin: integration test NixOS services configuration, test-runner helper,
  and existing alert/mail integration scenarios.

Approach:

- add Mailpit to the existing `vpsadmin-services` test machine inside the
  `mailer` container;
- keep Postfix enabled, but force test nodectld mail delivery to Mailpit on
  `127.0.0.1:1025`;
- expose the Mailpit API on `127.0.0.1:8025` inside the mailer container and
  use it through reusable test-runner helpers;
- retrofit the existing alert/mail tests to clear Mailpit before mail-producing
  actions and assert delivered message subject, recipient, and body fragments;
- keep existing database `mail_logs` assertions as separate persistence checks.

Compatibility:

- production deployments are unaffected; the change is test-only;
- no schema, API, generated client, or persistent production state changes;
- no mixed-version runtime concern outside integration test VMs;
- rollback removes Mailpit from test configuration and helper assertions.

Testing plan:

- run Ruby syntax checks for edited helpers;
- run `ruby tests/ci-selection-test.rb`;
- run `./test-runner.sh test services-up`;
- run the alert mail tests:
  `alerts/lifetime-and-daily-report`,
  `alerts/oom-report-notify-and-prune`,
  `alerts/incident-report-process`.
