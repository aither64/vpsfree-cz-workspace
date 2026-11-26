storage: add administrator backup cleanup

Administrators can disable backups and remove primary snapshots from the existing
dataset plans page, including datasets with no remaining plan. Preservation is
on by default, scope and opt-out loss are explicit, and one generated API call
uses the existing task and unknown-outcome handling. Ordinary plan removal now
explains that primary and backup snapshots remain. VPS storage links to the
existing plans route in its app/admin context.

REQ-011, REQ-024 and REQ-048. Focused tests: 64 passed; complete quick checks
passed on the canonical dependency tree with the verified SDK overlay. The final
metadata-refreshed candidate passed 30 consumer/wire tests. Browser source and
capture steps are included; execution/screenshots follow independent review.

Integration is blocked until an authorized published SDK supplies the new action
and the manifest, lock and provenance select that registry artifact. The current
local 0.6.0 candidate is development only. No merge or deployment has occurred.
