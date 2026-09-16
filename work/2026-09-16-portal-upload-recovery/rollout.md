# Portal upload recovery rollout

## Prepared scope

User authorized deployment to aitherdev using vpsfree-cz-configuration. Build and
deploy from feature worktrees; application remains in the user-profile package.
Initial deployment left defaults unmerged. The later user-requested integration
and cleanup are recorded in integration.md. No archive was requested. Exact
deployment heads: revisions.json.

## Previous installed generations

- Application: /nix/store/rl1kpyjg28kvvsyiykqkwl9fl34mmi1g-dev-workspace-0.2.0
- System: /nix/store/rpi2qkdsi5s2x7g0lslljca62a5q3359-nixos-system-aitherdev-26.05.20260911.21a67dc

No upload path or catalog migration is planned. Keep these generations available.
A rollback preserves uploaded contents; older assets restore the known removal
bug and older admission rules. Reload pages after a generation change.

## Ordered operations after review

1. Reconcile all review findings and pass focused regression checks.
2. Run actual portal browser fixture against both forms, current/old assets,
   reload recovery and special filenames; retain only synthetic data/evidence.
3. Run provider flake checks; build the workspace package with packaged checks.
4. Build cz.vpsfree/machines/aitherdev through confctl, then dry-activate.
5. Switch the application with stable `workspace-host switch --source` pointing
   to the initiative workspace worktree. Deploy the prepared system generation
   through confctl. Never add the application package to the system configuration.
6. Confirm portal/router/Codex health, exact installed revisions, matching host
   configuration, and authenticated live synthetic uploads/download/removal.
7. Record CI outcomes and cleanup transient fixture processes/outputs. Retain
   feature worktrees/branches and session for follow-up.

## Execution results

Completed 2026-09-16. All mandatory reviews and focused remediations completed
before acceptance. Provider flake check, packaged runtime suites, 16 Firefox
checks and current-head CI passed.

Executed from the configuration feature worktree:

```sh
nix develop --command confctl build --yes cz.vpsfree/machines/aitherdev
nix develop --command confctl deploy --yes --generation 2026-09-16--08-59-31 cz.vpsfree/machines/aitherdev dry-activate
```

Switched the user profile from the shared workspace root using the stable command:

```sh
workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-16-portal-upload-recovery/workspace
```

Then activated the already built system:

```sh
nix develop --command confctl deploy --yes --generation 2026-09-16--08-59-31 cz.vpsfree/machines/aitherdev switch
```

- Application profile **47**:
  `/nix/store/ql5prmqfml0y62z2xj4yx45sdv7ijgrz-dev-workspace-0.2.0`.
- System profile **148**:
  `/nix/store/4j48v2vg75ph5hm0lakzgha2fljbrx46-nixos-system-aitherdev-26.05.20260914.c3eea5b`.
- Host input metadata confirms devWorkspace **eb658d49**. This configuration
  baseline also advances nixpkgs from 21a67dc4 to c3eea5b2; home-manager and
  llm-agents revisions are unchanged. Kernel outputs came from cache; there was
  no kernel source compilation or reboot.
- Both confctl health checks passed. Portal, router, nginx and Codex are active.
  Codex 0.154.0 retained MainPID **1090021** across the update.
- Authenticated HTTPS health, initiative page and updated versioned browser assets
  passed. Live synthetic names with quotes, backslashes, Unicode, SQL/HTML-like
  text and path-like text round-tripped through JSON and MIME. Exact downloaded
  bytes, checksums, idempotent creation and removal passed; control characters
  were rejected with the specific error. All synthetic files were deleted.
- Application profile **46** and system profile **147** still point to the
  previous paths above. `workspace-host rollback` restores the preceding
  application/Codex pair. System profile 147 remains the known prior generation
  for ordinary operator rollback. No rollback was needed or performed.
- At deployment, feature refs were pushed and unmerged. The later merge request
  is recorded in integration-revisions.json and integration.md. See
  revisions.json, ci-results.json and live-smoke.log for deployment evidence.

## Integration verification

The configuration pin rebased without changing its patch onto scheduled upstream
updates. The resulting aitherdev generation `2026-09-16--15-30-55` built as
`/nix/store/67qww05a1kp0q5kd391v0mm2w4prh00r-nixos-system-aitherdev-26.05.20260915.b67c7a6`.
It was a build check for merging, not another deployment. The running application
and system remain the verified profiles 47 and 148 above.
