# Database package Rake task scope

Related initiative: `work/2026-06-15-vpsadmin-events/`

## Symptom

Running the generic task below from the stripped vpsAdmin database package
fails with `NameError: uninitialized constant Rails`:

```shell
bundle exec rake db:version
```

The failure can look like a database or package problem even when the database
is reachable and the migration tasks are usable.

## Cause

The database package's Rake environment is intentionally limited. Its setup
enhances the deployment migration tasks, while generic Active Record tasks can
still expect the full Rails application constant and environment.

## Working deployment checks

Use the tasks supported by the production database package:

```shell
bundle exec rake db:migrate
bundle exec rake vpsadmin:plugins:migrate
bundle exec rake db:migrate:status
```

`db:migrate:status` was verified against the running event-system development
cluster and reported all event migrations as applied. Do not use the failure of
`db:version` alone as evidence that database credentials or connectivity are
broken.
