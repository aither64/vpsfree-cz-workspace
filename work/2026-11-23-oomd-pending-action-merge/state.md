---
lifecycle: active
---

# Oomd pending action integration

- [x] Packaged and independently reviewed the two-commit series on staging
  e9d55bada43c888ae91139d549d156a0831817de. The sampler commit is
  4e5f74a29b3ecd2c6251e3317430574f3c68b9ce and the controller commit is
  b86287c105b749827cd63632ac35936533910f63. No migrations or dependency pins.
- [x] Passed 399 local examples. Both added regression cases failed on staging.
  In KVM a peer restarted on partial sample 9 during an inventory stall, then
  its new init stopped on sample 14 while the first restart still held its lock.
  The existing watchdog suite passed seven of nine examples. Its host-row
  assertion also fails on staging. Both affected examples passed with the
  isolated fixture correction, including real RTNL distress.
- [x] User authorized the vpsAdminOS staging merge in this conversation with
  “so merge your changes, i'll think about the follow-up”.
- [x] Published branch `2026-11-23-oomd-pending-action-merge` and captured its
  staging comparison. Fast-forwarded remote `staging` to
  `b86287c105b749827cd63632ac35936533910f63`. Verified the remote head and
  released the merge claim. Production deployment is outside this delivery.

## GitHub checks on staging

The following links identify the runs triggered by the staging push.

- [CI (ci)](https://github.com/vpsfreecz/vpsadminos/actions/runs/45252903685) — queued as of the merge handoff.
- [RSpec](https://github.com/vpsfreecz/vpsadminos/actions/runs/45252903796) — in progress as of the merge handoff.
- [RuboCop](https://github.com/vpsfreecz/vpsadminos/actions/runs/45252903731) — success as of the merge handoff.

## Evidence

The registered repository is available in the portal. The Files tab includes
`verification.tar.gz` with the focused guest output, staging controls and
watchdog follow-up. The initiative was created in shell-only mode. The existing
chat transcript is separate. The interactive Top proposal was deferred.
