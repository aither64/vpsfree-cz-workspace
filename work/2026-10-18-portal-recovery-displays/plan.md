# 2026-10-18-portal-recovery-displays

## Goal

Implement portal uncertain-message Retry original/Dismiss controls, shared index warning grace, and timestamp metadata-loading grace; review and verify, deploy aitherdev, then merge dev-workspace, workspace and vpsfree-cz-configuration branches into master as explicitly authorized in the initiating conversation.

## Affected repositories

- dev-workspace: portal browser behavior, additive index loading flag, regression tests and portal documentation.
- workspace: matching nested application runtime pin.
- vpsfree-cz-configuration: matching dev-workspace channel pin for aitherdev's host contract.

## Approach

Add Retry original and Dismiss to unresolved ordinary-message receipts. Retry
the saved text, attachments and ID; preserve revised composer drafts. Persist
dismissal without deleting retry identity or claiming cancellation/delivery.
Continue transcript-based acknowledgement and preserve existing plan recovery.

Route server snapshot warnings through the shared 30-second visible warning
grace, with an additive loading flag for the existing 750 ms cold-cache delay.
Keep the six-second server refresh deadline.

Retain exact entry times during metadata refresh. Withhold new estimated times
while metadataPending is true until the shared 30-second visible grace elapses.
Show estimates with ~ once enrichment settles or grace expires; upgrade to exact
times immediately. Keep footer times and date grouping consistent.

## Decisions

- User selected explicit retry/dismissal, rather than hiding old warnings after a newer send.
- User selected delaying temporary timestamp estimates while retaining confirmed times.
- User explicitly selected merging dev-workspace, workspace and vpsfree-cz-configuration into master after deployment and verification succeed. This is standing integration direction for this initiative.
- This is an external conversation with a newly created shell-only initiative and no retained roster. Lead owns design and implementation; independent final review uses the installed default review policy. Long verification uses the site's Luna/low utility policy.

## Compatibility and deployment

Preserve submission IDs, server ledgers, queue behavior, session/journal schemas,
Codex version and protocol. Browser dismissal is optional additive metadata;
old browsers may redisplay warnings but preserve retries. The index loading flag
is additive; timestamp retention stays in page memory. Servers lacking
metadataPending retain existing marked estimates. No database migrations, API
client generation, CLI/Terraform changes or node-wide upgrade is needed.

Publish exact source revisions; update configuration through its dev-workspace
channel and the workspace's existing nested runtime selection. Verify the
deployment contract and complete review/checks before coordinated aitherdev
system activation followed by user-profile activation. Retain the machine
reservation through UI verification and authorized integration. Package recovery
is forward-only through the admitted candidate or a reviewed successor.

## Documentation

Portal users and future maintainers need receipt semantics, warning timing and
timestamp precision documented in dev-workspace/docs/workspace-portal.md.
Keep individual deployment evidence and exact SHAs in this initiative's rollout
record; reuse the existing configuration operations guide.

## Testing plan

Quick: JS syntax, focused Node contracts and focused Go index-response tests
from the repository Nix environment. Commit all intended changes and inventory
the complete branch series, pin streams and no-migration conclusion before
mandatory independent final review. After review: browser integration coverage
for message retry/dismissal, snapshot warning clocks and timestamp transitions;
packaged checks, CI, deployment contract and exact aitherdev build. Long checks
are launched/monitored by a fresh verification watcher. Verify deployed portal,
runtime identities and session continuity before merges.
