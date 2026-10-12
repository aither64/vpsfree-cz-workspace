# Release and consumer handoff

HaveAPI master includes the repair at ed88e2a. The supported release branch is
784e113, tagged v0.29.9. All three Ruby packages are published. The downloaded
server gem matches the verified build and serves all three repaired documents.

Completed checks: 20 focused and 365 full server examples, seven exact release
CI workflows, independent whole-branch reviews, 31 packaged service examples,
and successful builds for both API hosts. Local generation:
2026-10-12--12-29-00, configuration revision ad9830a5. No deployment occurred.

## Remaining gates

- npm returns 401. Refresh authentication from the HaveAPI release worktree
  with `nix develop -c npm login`. Resume only `npm publish` in the prepared
  `tmp/haveapi-client-js` staging directory; Ruby gems must not be repushed.
- Exact-head vpsAdmin API specs have passed; full integration CI remains queued,
  owned by the fresh consumer_ci utility watcher. Four other workflows passed.
- Obtain explicit master integration approval for vpsAdmin 7d911899,
  configuration ad9830a5 and PHP mirror 7fa4e35 after CI. PHP tag v0.29.9 follows
  its merge. These branches are published, independently reviewed and locally
  verified. Entire multi-component release remains incomplete until publication
  and PHP synchronization gates finish.
- The user handles deployment. Previous configuration service pin:
  b4ef8535a629ee8c9cd753afecdb05e0895d0eea. No migrations or state conversion;
  API instances may roll independently and nodes need no coordinated update.

[Release review](release-review.md), [consumer review](consumer-review.md),
[CI checkpoint](consumer-ci-checkpoint.json), [current state](state.md).
Session remains active and open; branches and owned auxiliary worktrees retained.
