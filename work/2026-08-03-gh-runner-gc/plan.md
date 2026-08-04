# 2026-08-03-gh-runner-gc

## Goal

Investigate why the vpsadminos.org GitHub runners run out of Nix store space,
then implement the two confirmed CI churn fixes: keep mutable workflow scratch
outside path-flake source trees and reuse NixOS raw disk images whenever the
evaluated machine configuration is identical.

## Affected repositories

- `vpsadminos-org-configuration`: primary location of the runner GC timer and
  GitHub job hooks. No worktree or code change was requested for this
  investigation.
- `vpsadminos`: implement content-based NixOS test image reuse, add an
  evaluation-only regression check, and move its CI log into prepared state.
- `vpsadmin`: move selector and test log scratch outside the checkout and pin
  the vpsAdminOS feature revision for integration validation.

## Approach

1. Inspect the runner configuration, its recent GC coordination changes, and
   the exact Nix version selected by the current nixpkgs input.
2. Verify Nix's temporary-root locking and stale-file cleanup behavior against
   the matching upstream Nix source.
3. Classify the non-temporary roots reported by the runner and identify roots
   that the existing plain `nix-collect-garbage` invocation can never remove.
4. Separate one-time recovery from a durable boundary-cleanup design.
5. Trace the vpsAdmin integration test's NixOS image derivations, repository
   source snapshots, output links, and observed GitHub Actions cadence.
6. Implement the confirmed fixes in independent branches based on
   `vpsadminos/staging` and `vpsadmin/master`; do not modify the existing
   `vpsadmin-events` branches or worktrees.
7. Review, validate, and push both branches. At the user's direction, use a
   successful reviewed-head vpsAdminOS workflow as the long integration gate
   and use a partial vpsAdmin run to compare source/image churn without waiting
   several hours for that suite to finish.

## Compatibility and deployment

- Temporary roots must remain protected while a Nix client or daemon operation
  owns their lock. Deleting files from `/nix/var/nix/temproots` manually is not
  a supported cleanup mechanism.
- Keep the job start/completion exclusion protocol introduced in August 2026;
  concurrent GC previously correlated with missing live build paths.
- Deleting old system generations reduces rollback history. Prefer an explicit
  age retention such as 14 days over `--delete-old` unless operators decide
  that only the current generation is needed.
- `/run/booted-system` and `/run/current-system` continue to protect the booted
  and activated configurations even if their old profile generation links are
  pruned. A mixed booted/current state is therefore retained until reboot.
- Removing `result` symlinks after all workflow steps releases local GC roots
  but does not remove outputs already copied to the binary cache. It must happen
  only in the completed-job hook and only under the runner/GC boundary protocol.
- Reusing NixOS base images must remain content-addressed by the complete NixOS
  machine configuration. Removing a test label from the derivation name is safe
  only because different machine inputs still produce different derivations.
- Moving CI logs and selector scratch files outside the checked-out flake must
  preserve failed-log upload and result evaluation behavior.
- Apply the configuration uniformly to all three runners. No API, persistent
  data format, or cross-component deployment ordering change is involved.

## Testing plan

If the recommendation is implemented:

1. Extend the existing shell test to prove completed-job cleanup releases only
   Nix output links and that GC cannot race the next job-start hook.
2. Test generation retention with disposable profiles and verify that the
   current generation is retained.
3. Evaluate the NixOS configurations for all three runner hosts.
4. Deploy to one runner first; verify hook logs, retained roots, reclaimed
   space, and a complete vpsAdminOS CI build before rolling out to the others.
5. For the vpsAdmin churn fix, compare two tests with identical services
   machine configuration and prove that they resolve to the same base image,
   while tests with different configurations remain isolated.
6. During a representative vpsAdmin CI sample, verify that test evaluations use
   one stable `vpsadmin-source` output and compare image/copy churn with the
   pre-fix artifact. Record peak `/nix/store` growth separately when runner
   shell access is available.
7. Run repository hooks and the mandatory fresh-context change review before
   the long GitHub integration run.
