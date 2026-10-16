# Keep the Reservations menu count current

## Goal and scope

Update the session's Reservations menu count without opening its panel. The
existing poll stops on other sections and the count lives in panel rendering.
Implement in dev-workspace; maintain matching deployment pins in dedicated
workspace and vpsfree-cz-configuration feature worktrees.

## Design and acceptance

The lead owns this bounded design and implementation. Poll immediately and every
five seconds while the document is visible, independently of the active section.
Compute the distinct held-machine count from the complete reservationHolders
summary, matched by slug and observation identity. Update the menu separately
from detailed panel rendering. Cache successful results and render them when the
panel opens. Preserve the last successful count on failure, mark its tooltip and
accessible label unavailable, and accept zero only from a successful response.
Abort and fence late reads on hidden documents/page exit. Keep title indicators
and notification behavior outside this fix.

## Compatibility, deployment and recovery

No persisted format, database, API, CLI, client, protocol or Nix option changes.
Old and new browser bundles use the existing coordination response. Rollback can
read all state; application selection follows supported forward recovery rather
than selecting an older package. No coordinated node update or reboot is needed.

User authorizes implementation and aitherdev deployment through
vpsfree-cz-configuration. Publish the exact runtime feature revision; select it
in the workspace nested runtime override and configuration's dev-workspace /
devWorkspace confctl channel. Preserve extension and unrelated inputs. Check
both locks with bin/check-dev-workspace-deployment. Build outside claims, then
use the coordinator's vpsfree:aitherdev reservation for system dry activation /
switch followed by application user-profile activation. Retain ownership during
review and feedback. Do not integrate feature branches without separate user
direction. Preserve exact attempts and recovery evidence on interruption.

## Documentation and verification

Readers are portal maintainers and operators. Update the owning coordination
guide's refresh contract; keep the individual deployment evidence in this
initiative. Main-agent user-facing-writing review applies before committing.

Quick checks: focused Node coordination regression suite and JS syntax, relevant
Go web tests and deployment contract checker in declared Nix environments.
Regression cases: initial count with Codex selected; held counts 1 -> 2 -> 0
while closed; failed read/recovery; duplicate, queued and released machines;
exact session identity; hidden/page-exit abort and late-response fencing; cached
details on opening. Complete committed independent review before longer package
and configuration builds. Monitor long checks with a fresh policy watcher.
After deployment, compare menu count against read-only coordination API while
Codex stays selected and verify served assets and system/profile identities.
