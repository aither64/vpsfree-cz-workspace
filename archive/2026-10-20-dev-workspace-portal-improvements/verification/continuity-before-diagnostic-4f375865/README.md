# Before-smoke diagnostic preparation

Original activation attempt4f375865 stopped phasebefore/not_confirmed with
ownedCommandMayStillRunfalse, selectedhzf/systemjwnd and no pending reconciliation.
Original before-smoke.log reports only the generic read_only_continuity_not_confirmed.
No switch-result or before continuity snapshot exists. This diagnosis did not
rerun the driver, contact the portal/SSH, inspect other sessions or mutate live state.

Static inspection has NOT established the failing assertion. The checked queue
endpoint does return an array, so that assumption is not a proven defect; no
product fix or weaker guard is justified from the generic failure. Existing read
and process checks can throw before assertions, hence fixed source-line telemetry
is needed before selecting a correction.

continuity-diagnostic.cjs is a NEW copy only. It adds fixed stages, fixed check
classes and numeric source lines; asset indices map through stage-map.json.
Assertion and subprocess errors retain only those fields. Bootstrap/cleanup are
also sanitized. Existing naming helper failure output may contribute ONLY a
hardcoded allowlisted reason; no raw child output or exception is emitted.
No raw argv, credentials, headers, bodies, transcripts or user/root/native IDs
are added to logs. candidate.json/naming-readiness.py are byte-identical copies.
Every original assertion/get call count and the exact GET allowlist/request-route
block are preserved. No timeout, validation, state contract or endpoint changed.

Pinned Node syntax/Bash syntax/Python compilation PASS. original-sha256.json
confirms original helpers, driver, failed attempt, real gates and old command
hash files remain immutable. No reproduction/GET/credential read occurred.
The first generator assertion found a duplicate source marker and wrote no files;
its unique marker was corrected before this copy was created.

ONE existing passive before-smoke reproduction argv (parent fresh execution
utility; workdir own session tracking):

    bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/continuity-before-diagnostic-4f375865/reproduce-before.sh

This uses the SAME pinned Node/PW/Chromium, same before phase/claims-independent
read checks, same own-session GET allowlist, JSdisabled/SWblocked and strict fixed
key rootSSH credential access only in memory. It writes only NEW diagnostic
receipts under /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/continuity-before-diagnostic-4f375865/attempts/before-reproduction-1 and refuses duplicate execution.
No activation driver/private helper/profile/host/config/portal writes are present.
The wrapper preserves the original180s bound and clears DEBUG/PWDEBUG/NODE_DEBUG.
Sequential15s local commands,40s GET deadlines and asset reads make total duration
uncertain/potentially>1min; therefore it was NOT run inline. Parent should launch
it once under the prescribed fresh utility and return only safe stage/check/line
or the sanitized pass. No automatic retry; no fresh activation authorized here.

Aea64/Bbc40/C40b0/config5a524 remain frozen. Package/CI/browser passes are unchanged.
After a concrete diagnostic result, correct only a proved helper assumption under
parent routing, preserving the original failure. Parent alone may authorize a
fresh ordinary activation after cause/correction proof. Machine755 is unchanged.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
