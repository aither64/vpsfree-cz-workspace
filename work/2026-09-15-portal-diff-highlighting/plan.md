# Portal changed-character highlighting fix

## Goal and authorization

The user accepted the investigation and requested implementation and deployment
to aitherdev, then explicitly requested default-branch integration and cleanup.
Restore readable character highlights in the reported comparison,
while retaining Git-authoritative lines, counts, source text and line links.
See [diagnosis.md](diagnosis.md) for the reproduced regression.

## Affected repositories

- `aither64/dev-workspace`: use existing `presentableDiff` in the review model,
  add regression assertions, and document why visual cleanup is necessary.
- `vpsfreecz/dev-workspace` (`vpsfree-dev-workspace` locally): pin the runtime fix.
- Shared coordination repository, feature worktree `workspace`: pin the extension
  to produce the deployed site package with existing site configuration.
- `vpsfree-cz-configuration` is evidence only. The user permits its use for
  deployment, but application deployment belongs to the user profile and needs
  no host change or system-config pin.

## Approach and decisions

1. Reuse this slug and create isolated feature worktrees for the three packages.
2. Add semantic regression coverage that fails on raw character splitting:
   identifier replacements and unrelated multiline rewrites in both layouts.
3. Use the already locked CodeMirror `presentableDiff`; retain Git boundaries,
   bounded diff config and current rendering. A short code comment owns rationale.
4. Commit the fix, update the two downstream pins in separate commits, run quick
   checks and the mandatory adaptive review before package/integration checks.
5. Push feature branches, inspect CI, build the exact consuming workspace package,
   and activate with `workspace-host switch --source <workspace-worktree>`.
6. Verify the served bundle and the original comparison in a real browser; record
   deployment revision, package, predecessor and recovery instructions.
7. Merge the unchanged reviewed heads into all three `master` branches, inspect
   default-branch CI, and clean owned worktrees and transient files.

A new line-pairing algorithm or similarity policy is outside this bounded repair.
The existing presentation cleanup is still heuristic and may retain common
punctuation/indentation in rewritten blocks. Assess the actual repaired view.
Integrate the reviewed heads by fast-forward, retain feature branches and saved
comparisons, and remove the initiative’s clean worktrees and transient captures.
Keep the session open for follow-up; no lifecycle action.

## Compatibility and deployment

No API, protocol, schema, migration, manifest, journal, cluster contract, Codex
version, NixOS module or persistent-state changes. Old and new browser bundles
consume the same source/range payload. Reloading a page loads the fixed bundle.
There is no mixed-version ordering requirement beyond publishing runtime then
extension then the site package. Existing stable profile activation owns service
reconciliation and retains the previous generation for `workspace-host rollback`.
The application rollback reverts visual behavior without state conversion.
Do not change or interrupt unrelated sessions to bypass an activation refusal.

## Documentation

Runtime's adjacent model comment will explain why raw diffs are unsuitable for
visible highlights. Existing README covers source rendering and exact Git ranges;
no new operator procedure is needed there. This session owns diagnosis, review,
verification and exact deployment record. Reconcile the existing investigation
notes to distinguish historical findings from the implemented fix.

## Verification

Run new regression tests before and after the fix, build review UI then run its
full tests, verify exact-source projection invariants and line counts, check
pin changes and flake evaluation. After required review, run package checks and
consumer build, inspect CI, verify the deployed asset and original saved review
in unified and split layouts. Avoid redundant unrelated integration suites.
