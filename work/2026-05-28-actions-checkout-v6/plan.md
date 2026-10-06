# actions/checkout v6

## Goal

Update vpsfree-irc-bot workflows to use actions/checkout@v6.

## Affected repositories

- vpsfree-irc-bot only.

## Compatibility

This is a CI-only workflow action version bump. Runtime bot behavior and
vpsfree-cz-configuration are unaffected.

## Testing

- Run actionlint on workflows.
- Push to master and confirm the RSpec workflow passes.
