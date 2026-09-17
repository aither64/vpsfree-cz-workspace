# Documentation policy rollout

## Status

Deployment completed on 2026-09-17. The installed package and fresh skill
discovery select the reviewed files. Both default-branch CI runs and worktree
cleanup are complete. No operator action remains for this deployment. The user
authorized deployment and default-branch integration.
Reusable authoring rules remain in their owning repositories.

## Package and prerequisites

The [review packet](review-packet.md) identifies the exact provider/consumer
revisions. Mandatory review, full local flake checks, consumer build and provider
feature CI passed before deployment. Final comparisons were captured before
fast-forward integration; reviewed heads did not change.

All three remote master branches contain the exact final feature heads:
runtime 5bcb83120cf25974ecd2dad7b7e737473169b173,
extension f2fdbcebc115b7fd07ab6e0c91ebea189a57f341 and
workspace fd626e56f6440834c2ce50f32fd7f218a458f020.

The workspace application is deployed through its user profile. No NixOS host
configuration or cluster change is currently required. The skill name, catalog
format, templates and persisted state remain unchanged.

## Executed update

The installed stable command completed successfully:

```sh
workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-17-documentation-boundaries/workspace
```

Immediately before switching, profile-48-link selected
/nix/store/bspd81hp98awq942lnr7p93k38i8d8di-dev-workspace-0.2.0.
Activation selected profile-49-link and
/nix/store/mk716d08x840l2wdlc1mbaqpnhabn30f-dev-workspace-0.2.0, exactly matching
the built consumer. The predecessor remains available. The compatibility check
accepted Codex 0.154.0. No transition refusal or recovery action occurred.

The clean source worktree in the executed command was subsequently removed.
The installed immutable package remains in the user profile. Feature branches,
captured comparisons and this initiative's session remain available.

## Verification

- All six managed skill links match the selected package catalog. The edited
  documentation/review/handoff entrypoints and general-review reference are
  byte-identical to their reviewed sources.
- Fresh App Server clients called skills/list with forceReload from the project
  directory and a fresh empty directory. Both returned the three skills enabled,
  pointing to the new immutable source paths, with zero discovery errors.
- Codex, tmux, portal and router are active. Codex PID 1090021 and tmux PID 435397
  were retained; portal/router restarted normally during activation.
- This initiative's portal page and Markdown preview endpoint serve the IP
  release handoff. No source-session conversation or cluster action was sent.
- Existing conversations can retain older instructions in context. Catalog
  discovery verifies new selection, not automatic rewriting of loaded context.

## Recovery

The preceding generation is retained. Recovery, if needed, uses the stable
workspace-host rollback workflow and must be recorded here. A profile
rollback restores older skill text; it does not revert the committed workspace
policy or authored documentation. No database or session-format migration needs
reversal. No live rollback was needed; the isolated host activation/rollback VM
test and packaged profile/skill-link checks passed before deployment.
