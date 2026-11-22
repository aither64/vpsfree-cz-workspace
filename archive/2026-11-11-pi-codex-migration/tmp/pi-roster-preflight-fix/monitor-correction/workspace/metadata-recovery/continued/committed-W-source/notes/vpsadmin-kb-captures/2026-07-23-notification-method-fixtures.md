# Notification method fixtures need provider configuration

Related initiative: `work/2026-06-15-vpsadmin-events`

When the capture seed tried to create Telegram and SMS notification targets,
`vpsadmin-database-setup.service` failed with `Validation failed: Action is not
available`. Skipping the per-user delivery-method validation is insufficient:
the target model also checks whether the method is configured globally.

For the `screenshots` topology, configure Telegram in webhook mode with
automatic registration disabled and configure an SMS gateway with an
`example.test` URL. Store only inert documentation credentials in Nix store
files. Also enable the corresponding per-user delivery methods in the capture
seed. This lets target and receiver forms represent paired/verified methods
without contacting Telegram or an SMS provider.

The normal API notification configuration is materialized by the API pre-start
hook. Database seed files run before that hook, so the target model otherwise
still sees both actions as unavailable. Give
`vpsadmin-database-setup.service` and the follow-up capture seed service a
minimal `VPSADMIN_NOTIFICATIONS_CONFIG` which marks Telegram and SMS configured.
Keep normal model validation enabled; do not use `save(validate: false)`.

Enabling a per-user delivery method and adding broad role routes can make
additional receivers eligible. The screenshot seed runs from both the database
setup and its follow-up seed service, so route-state fixtures must remain
correct on an idempotent second run. Put a non-continuing route used to
demonstrate an inactive time interval before later broad additive routes;
moving only the broad-route creation after the assertion works on the first
run, but not after those routes already exist.

After a database-seed failure, stop and reset the disposable devcluster before
restarting it. Reusing the partially migrated and seeded database can hide
whether the fixture is cleanly reproducible.
