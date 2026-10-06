# 2026-07-05-vpsfbot-outage-reports

## Goal
Investigate why vpsfree-irc-bot announced outage 1426 but did not notice
outages 1427 and 1428, which were reportedly created shortly afterwards, then
implement and deploy a clean fix.

## Affected repositories
- vpsfree-irc-bot
  - code fix and regression coverage
- vpsfree-cz-configuration
  - production package pin update after the bot fix is verified and merged

## Approach
- Inspect outage polling, API filtering, and persisted state handling.
- Compare the expected API/outage data for IDs 1426, 1427, and 1428 when
  reachable.
- Reconstruct the most likely sequence that left only outage 1426 in
  `/var/vpsfbot/libera/irc.libera.chat/outages.yml`.
- Treat `state == announced` outage updates as new outage announcements when
  the outage is not already present in the bot's state. This uses the
  announcement update stream as the source of truth for staged outages becoming
  visible, while keeping the existing direct outage polling path for outages
  that are created already announced.
- Add integration coverage that creates two staged outages, announces the first
  one so the polling cursor advances, then announces the second one and expects
  the bot to report it too.
- After quick local verification, run the mandatory standalone review before
  the heavier integration workflow.
- Push the feature branch to trigger GitHub workflows, investigate failures,
  merge to the default branch with a fast-forward-only merge after verification,
  then update and merge the production package pin.

## Compatibility and deployment
- The existing YAML state file remains unchanged. Stored outage records keep
  the same keys and value shapes.
- The fix only changes how the bot reacts to outage update events. It does not
  change vpsAdmin API contracts, database schemas, IRC protocol output format,
  or service configuration.
- Mixed-version operation is not a concern for a single IRC bot process. A
  rollback can read state written by the new version because the persisted
  format is unchanged.
- Deployment ordering is simple: merge and package the bot revision, update the
  `vpsfree-cz-configuration` package pin, then deploy the bot host.

## Testing plan
- Run `bundle exec rspec`.
- Run `bundle exec rubocop`.
- Run the mandatory standalone change review after the committed quick-check
  pass.
- Push the bot feature branch and monitor GitHub Actions, including the
  integration workflow that runs the `vpsadmin-events` test.
- Build the production bot configuration after updating the package pin in
  `vpsfree-cz-configuration`.
