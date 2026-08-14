# Optional notification modules in feature-revision dev clusters

The top-level vpsAdmin development cluster can evaluate a feature revision that
predates the optional notifications module. In that case, guarding only the
module import is insufficient: option declarations for the notification
dispatcher, Telegram receiver/webhook, SMS gateway and webhook test service
also fail evaluation because their option namespaces do not exist.

Keep all notification-dependent declarations behind the same
`builtins.pathExists` check used for the module import. This lets a dev cluster
boot older or rewritten feature revisions without weakening the configuration
used by revisions that include the module.

This was encountered while deploying initiative
`work/2026-08-12-dns-secondary-zone-transfer-failure` and verified by starting
the single-node topology over its bridge network.
