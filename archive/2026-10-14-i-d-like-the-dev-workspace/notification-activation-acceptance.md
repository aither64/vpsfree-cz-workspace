# Notification activation correction: deployed acceptance

Status: requested new/refreshed-tab worker update behavior implemented, reviewed,
verified and deployed. Actual physical Firefox/macOS notification appearance
and click acceptance remain unconfirmed.

Runtime469757183ba9491d642b56e91658dc64e390647b, workspace
bce984296ec29faa0cf756f632a26e30d77b6fba and configuration
40172e5fbef65c60e89b5977bae023e724572e9e are published/deployed, unmerged.

The worker installs with skipWaiting and claims documents on activation. New or
refreshed controls update the existing registration and confirm their current
controller. Other tabs can remain open; no automatic reload, subscription reset
or old-notification compatibility workflow is introduced. Updated copy no longer
asks closing portal tabs. Client includes usev3; shared store remainsv2.

38Node contracts,2focusedGo,changedsyntax/diffPASS. Retained independent source
review had one Advisory; narrow fix folded into owning seventh and lead directly
verified under step9. Final composition/fullhistory/consolidation/no-migrations
review passed. Complete seven source commits and one final pin each retained.
BothFirefox/Chromium actual lifecycle regressionPASS31s retained old controlled
tab/draft over oldactive+waiting->actualsuccessor. Chromium syntheticTest only;
Firefox lifecycle/currentcontroller capability only. FullflakePASS14m33s/allchecks,
recovery462.54s. CI38760306881 fastPASS5m43s, hostskipped; localVM checks passed.

Initial machine preparation failed because pressureGC removed its unrooted
helper; exact journal proves cause. Failed evidence retained. Corrected exact
catalog helper rooted; genuine machinev2PASS100s/profilePASS5m44s. No source
change, hook bypass, GCpolicy change or blind activation replay. Roots preserved.

Approved ordered machine81c0f179 and profile7ec26475 both succeeded/applied.
Independent SSH read confirms exact systemmvn0jq6s and application29jmlbai;
read-only authenticated HTTPS verifies exact committed worker/clientSHA256 and
currentpage clientv3. See notification-activation-acceptance.json and
worker-update-served-proof.json. No browser/provider mutation in final smoke.
No owned operation remains running. Reservation1956d2a0 stays deployed_review.

Next user step: refresh Browser notifications on Firefox/macOS, leaving other
portal tabs open, then send a Test if checking physical appearance. This change
removes the activation barrier; it does not explain the prior Linux Firefox
UnknownError display rejection or prove the macOS symptom repaired. Prior
provider/processgroup/fixture causes remain unknown. All oldevidence preserved.

Session stays active/open, allfeatureheads unmerged. No merge, reservation
release or lifecycle approval/action. Current product469 is now a supported
consumption boundary; preserve subscriptions/privatekeys/outbox/receipts/journals
and recover forward through compatible packages.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/
