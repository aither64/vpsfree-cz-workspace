# Notification grouping queue permissions on existing clusters

Related initiative: `work/2026-06-15-vpsadmin-events`

## Symptom

`vpsadmin-notification-grouper` repeatedly failed with RabbitMQ
`ACCESS_REFUSED` while declaring `vpsadmin.notifications.grouping`, although
the updated initialization tool included the new queue in its permission
regular expression.

## Cause

`vpsadmin-rabbitmq-setup` is intentionally one-shot and records
`/var/lib/vpsadmin-rabbitmq/rabbitmq-initialized`. Updating
`tools/rabbitmqcfg.rb` therefore fixes new clusters but does not change the
notification user's permissions on an already initialized broker.

## Fix and verification

Reconcile the user's permissions from deployment configuration after
`rabbitmq.service` and `vpsadmin-rabbitmq-setup.service`. Deploy RabbitMQ nodes
before starting the new groupers on API hosts.

In the development cluster, applying the updated permission command and
restarting the grouper produced an active service and a durable quorum queue
named `vpsadmin.notifications.grouping`.
