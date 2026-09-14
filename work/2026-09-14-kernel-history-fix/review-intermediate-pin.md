# General exact-pin review of intermediate heads

Reviewed the high-risk exact-pin checkpoint with the mandatory general lane at
gpt-5.6-sol xhigh. During the review, the full supervisor integration gate
exposed a test-only ordering dependency in the synthetic scenario. The
following revisions are therefore reviewed intermediate heads rather than the
final rollout candidates:

- vpsAdmin `791ab3aa89e2f613979da6090b89785c78245db5` through
  `feaa152436cf66e980c4e53f86a541bb10daae16`;
- vpsfree-cz-configuration `249bed1ee28e69a907edd09ea97a1144dbcdefeb`
  through `fc7c37b236ba40b8d4769e66e4d86ec78e4128b8`;
- vpsfree-kb-contracts `919577d0c770e47b623c591f8bf0cce4e8d30666`
  through `09e09f0d8274702d6280e36e06c399766fd4afb4`;
- the prepared `rollout.md` in this initiative.

## Findings

No Blocking, Important, or Advisory findings in the assigned exact-pin scope.

The exact revision chain is consistent. The vpsAdmin feature head is pushed
and matches its upstream feature branch. Configuration changes only the
`vpsadminServices` lock entry from the shared base to the exact reviewed vpsAdmin
head; its locked revision, timestamp, and NAR hash match the vpsAdmin input in
the KB lock. The KB commit records the same full revision in `captures.json`,
`contract/navigation.yml`, `contract/pages.yml`, `flake.nix`, and both locked
and original fields in `flake.lock`. Its diff changes no transitive vpsAdminOS
or nixpkgs lock entry. Neither downstream reviewed tree contains the superseded
`2a312616...` or `b851ea971...` feature pin. This proves consistency among the
reviewed intermediate heads; it does not make them the final rollout set.

Commit history is consolidated and reviewable. vpsAdmin contains the intended
recorder/provider commit `7b4aec6bb9b948ab3d1bdf90a886b99a4ebd4ff5`
followed by the repair/integration/operator-documentation commit
`feaa152436cf66e980c4e53f86a541bb10daae16`. Configuration and KB each contain
one consolidated generated or pin commit directly on their fetched `origin/master`
base; the earlier pin commits are absent from the local reviewed series. The
generated configuration commit message is preserved. All three reviewed diffs
pass `git diff --check`.

At this intermediate checkpoint, the rollout preflight asserts configuration
HEAD `fc7c37b236ba40b8d4769e66e4d86ec78e4128b8` and the exact
`vpsadminServices` pin `feaa152436cf66e980c4e53f86a541bb10daae16`.
Its migration ID `20260914120000` and public Rake command
`vpsadmin:node:repair_kernel_history_bounds` exist at that vpsAdmin head. The
prepared shell blocks pass `bash -n`. The previously reviewed mask checks,
two-host activation ordering, separate paused preview approval, exact preview
comparison, and rollback limits remain present. Its two exact assertions must
be refreshed together after the standalone synthetic evidence correction
produces a new vpsAdmin head and regenerated configuration pin.

At inspection time, the vpsAdmin and KB worktrees were clean. The configuration
worktree had no tracked or staged changes and only the disclosed untracked
`.bin/` and `.bundle/` caches.

## Residual gates

- Replace the cross-example synthetic fixture dependency with complete
  standalone synthetic evidence and rerun the full
  `supervisor/runtime-ingestion` scenario successfully. Product behavior, pin
  format, and rollout ordering are unchanged by the planned test-only repair.
- Fold that repair into the owning unmerged vpsAdmin commit, then mechanically
  regenerate the one configuration pin commit and the one KB pin commit to the
  new exact vpsAdmin head. Refresh both exact rollout assertions together and
  repeat this bounded consistency check for the resulting heads.
- Do not push the currently reviewed configuration or KB heads. They are each
  one commit ahead and one superseded pin commit behind their remote feature
  branch, and now point to an intermediate vpsAdmin revision. Push only the
  regenerated consolidated heads with the expected lease protection, then
  validate the exact remote heads and run/monitor the KB workflows at the new
  KB head.
- The running 11-consumer configuration build and direct build-plan evidence
  are scoped to intermediate pin `feaa152436cf66e980c4e53f86a541bb10daae16`.
  Rerun the pin assertions and all 11 consumer builds successfully for the
  regenerated configuration head.
- vpsAdmin CI run `34833489308` and API Specs run `34833489304` are also scoped
  to the intermediate head. Monitor the workflow runs triggered by the
  corrected pushed head; completed intermediate results may remain supporting
  evidence only where the relevant tree is unchanged.
- `verification.md` still describes superseded intermediate heads and the
  earlier 11-consumer build. It is not yet a rollout approval artifact. Update
  it with the completed final-head results before satisfying `rollout.md`'s
  explicit stop condition.
- Production rollout and the separate node 400 repair remain unexecuted and
  require their stated approvals after all gates above pass.
