# Forward-only follow-up

Architect0 bounded read-only D3 report accepted 2026-11-18. Both final daily
workflows protect the one-time pin, by rejecting an update rather than silently
skipping the stale input. No source changes, update/workflow execution or tests.

## Exact consumers and implementation

- A head 828c390c7e1857f11522933977afd852634b85f8, daily-update.yml lines59–60:
  grouped {nixos-stable,production,staging} nixpkgs with --forward-only;
  set -euo pipefail lines51/54.
- B head 72c18d811086dac8e16ec8c7ee6bf8e32ce62123, daily-update.yml line58:
  --forward-only nixos-stable, set -euo pipefail lines50/53.
- Both use confctl ff5e017780a35fb97b549db2a51b570193867c3b and keep original
  nixos-26.05, selecting one-time4077fb98f09d5bd847f848ae4f214a4c5b9f0a9d.

Pinned confctl lib/confctl/inputs/git_compare.rb:11–22 delegates GitRepoMirror;
lib/confctl/git_repo_mirror.rb:71–86/:172–177 uses git merge-base --is-ancestor,
not timestamps. Old ancestor of candidate allows forward; reverse rejects
behind; neither rejects divergence. Full-history/cache failures remain errors.
ForwardGuard (:24–55/:60–104) validates full reachable input graph.

Outcomes: unchanged identity 0/no-op; accepted descendant 0/install/commit;
behind/diverged or same-SHA changed lock attrs 3/rejected; invalid evidence,
unsupported source, Nix or ancestry failures1/error. See update_result.rb:5–13,
docs/flake-inputs.md:249–269, forward_guard_spec.rb equality/forward/nested
rollback/newer-timestamp rollback/equal-SHA metadata cases.

GuardedUpdate (:29–70) prepares separate reference/candidate, validates and
snapshot-checks before atomic accepted installation. Rejection/error leaves
real lock/index/HEAD unchanged. Tests cover unchanged state and atomic rejection
of mixed batches. Hook failure after accepted install may leave a validated
candidate installed while failing job; distinct from guard rejection.

## This pin and workflow effect

At 2026-11-18T17:57:17Z, one public GitHub compare4077fb98...nixos-26.05 returned
behind, ahead_by0, behind_by106, merge-base f68407657ad294471eb4b2e65d193df26edf729f.
Against that candidate the guard rejects3 and keeps the pin.

A rejects the entire first grouped update, including otherwise-forward production
or staging, and set-e prevents later update/push steps. B similarly stops before
os-staging/push. Cache-save cleanup steps may run. Earlier successful invocations
are not undone, but later publish does not execute after failure.

When nixos-26.05 equals4077fb98 with unchanged attrs it succeeds as no-op; a
candidate descendant updates normally if entire graph passes. Original branch
tracking already preserved, so no manual restoration required. Equivalent
cherry-picks without ancestry remain rejected. Descendant commits reverting a
fix are not detected: ancestry protection is not semantic package validation.

No app changes/check execution or review needed for this investigation.

## Recommended semantics and clean solution (D4)

User asked for a solution and whether ordinary behind-channel status should fail.
Recommendation: guarded update succeeds as no-update for unchanged/equal or
behind-only candidates; descendants advance. Divergence, source/removal/equal-SHA
metadata policy violations remain rejection3; unavailable or invalid evidence,
Nix and validation failures remain errors1. No workflow `|| true` or new flag.
Existing strict check-update still rejects a supplied rollback artifact.

Implement in confctl GuardedUpdate, retaining one process lock/snapshot/install/
commit transaction. Generate Nix candidates sequentially per selected terminal
input using existing update_inputs follows resolution/deduplication. Start with
original temporary reference; each accepted whole candidate becomes next temp
reference. Discard behind-only attempt as skipped, retaining old input and its
coherent graph. Any other policy rejection/error aborts before installation.
Validate final accumulated graph against original, recheck snapshot, install once,
commit accepted changes once. All-skipped leaves exact lock/index/HEAD unchanged,
no commit, success0 with skip summary. Stable deterministic selection order.

Skip boundary is entire selected input attempt including nested changes; never
splice nodes from rejected candidate. Complete-graph checks preserve shared follows
and prevent downgrade through another root. Re-resolve selections against accepted
intermediate graph; incompatible target redirection/removal is error, not skip.
Independent forward inputs continue even if stable channel is behind. No maximal
subset solver or retry loop; interdependent updates can be conservatively skipped.

Use structured guard rejection kinds, not parsed issue strings. Preserve strict
guard validator and explicit set/unguarded update behavior. Document intentional
exit3→success compatibility change for behind-only UPDATE; strict check-update
remains available for callers validating a proposed final lock. Configuration
workflows need only consume new confctl revision, no text workaround.

Focused tests: all-behind/no-byte-or-commit-change; grouped behind stable plus
forward production/staging one commit; nested parent skip/shared follows aliases;
equal/descendant catch-up; mixed behind plus real failure atomic; later Nix failure
and concurrent snapshot/post-install hook contracts; strict check-update rollback
rejection. No implementation, commits, tests or workflows executed for D4.
