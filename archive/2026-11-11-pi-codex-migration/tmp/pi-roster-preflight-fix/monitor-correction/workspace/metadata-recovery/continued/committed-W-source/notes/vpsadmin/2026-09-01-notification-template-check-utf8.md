# Notification template checks must choose UTF-8 explicitly

Related initiative: `work/2026-08-31-vpsadmin-notifications/`.

Running the notification-template checker in a Nix sandbox exposed an
`Encoding::CompatibilityError` even though the same files passed in an
interactive shell. The sandbox's Ruby process defaulted to US-ASCII, so syntax
and metadata reads inherited the wrong external encoding.

Read Ruby metadata and ERB template files with an explicit UTF-8 encoding.
After applying that rule throughout the parser, the checker passed both in a
locale-free environment and as a Nix derivation.
