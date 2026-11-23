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
- [ ] Publish the reviewed feature, capture comparison, integrate and confirm
  the remote staging head. Check CI after releasing the repository claim.

The tracking session was created with the CLI after the previous portal
preparation compatibility error cleared. The registered feature worktree belongs
under worktrees/2026-11-23-oomd-pending-action-merge/vpsadminos. The published
operational documentation accompanies the code in docs/os/oomd.md. Full local
verification evidence is available in the portal file verification.tar.gz.
