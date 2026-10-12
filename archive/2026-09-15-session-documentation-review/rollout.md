# Documentation workflow rollout

## Status

Deployment is complete. Live verification and all feature/default-branch CI
checks passed. No operator action remains.

The application is installed in the user profile on aitherdev. No NixOS host
module or configuration change was needed. The user authorized deployment and
integration of the runtime, extension and workspace feature branches.

## Revisions and prerequisite checks

The exact reviewed dependency chain is recorded in [review-packet.md](review-packet.md).
All required reviews, package checks and feature-head CI passed before deployment.
The final heads remained unchanged, and all comparisons were captured before
integration. Results below record the executed deployment.

The preceding user profile, rechecked immediately before deployment, resolves to `/nix/store/243g1pcykrjq7alpvk9f1n81yfxcfimd-dev-workspace-0.2.0`.
Profile link before deployment: `profile-44-link`. The stable command preserved
that predecessor and selected `profile-45-link`.

## Executed application update

The following command completed successfully from the consuming workspace
initiative worktree on 2026-09-15:

```sh
workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-15-session-documentation-review/workspace
```

Use the installed stable command. Respect its existing unfinished-operation and
compatibility refusals. Resolve only this initiative's work; never abandon,
interrupt, or reset another session to make deployment proceed. The package
retains the current Codex version when appropriate and reconciles user services
through the normal activation path.

## Verification procedure

- Compare the selected package with the built consumer package.
- Check that dev-session-documentation is a managed link to the selected catalog
  and that the review/handoff skills still resolve to the selected extension.
- Check implicit skill discovery using a fresh directory/session context and
  the installed App Server's skill catalog. A catalog check does not imply all
  existing conversations have reloaded instructions already in their context.
- Check the user services and existing initiative portal page through the normal
  local endpoint. Confirm that registered Markdown artifacts still render.
- Record the exact deployed revisions, generation, results and remaining work.

## Rollback

The stable `workspace-host rollback` command selects the retained preceding
package generation and reconciles its managed skills. A generation predating
this feature removes the new managed skill link while preserving authored docs.
Session Markdown and manifest formats remain readable by the preceding runtime;
finish any in-progress creation or fork using its originating generation before
a package transition. Rollback of the application does not revert committed
workspace policy: if rolling back this capability, temporarily suspend its new
skill reference in workspace instructions through a normal reviewed change or
restore the feature package. Do not delete documentation to roll back tooling.

Skill-link installation and rollback are tested with isolated package fixtures;
a live rollback is only needed to recover an actual deployment failure.

## Executed results

- Runtime `9a1b16464e45d722110b448a79315a0f3ce134aa`, extension
  `c6afe2905506fba0b8e372e0436b570f5597f8bd`, and workspace
  `7353127dc22275f24f1f92e5782fb34840dd0e49` were integrated into their
  remote master branches by fast-forward. No reviewed head changed.
- All three local flake checks and the consuming package build passed before
  the switch; feature CI passed for the runtime and extension.
- Profile generation 45 resolves to
  `/nix/store/kimxny34bbmdybfpj7v6mlz6z88zsk5k-dev-workspace-0.2.0`, exactly
  matching the built consumer package. All six managed skill links resolve
  to its schema-1 catalog, including the new generic documentation skill.
- The switch verified compatibility with Codex 0.154.0. Codex App Server and
  tmux retained their process identities; router and portal restarted through
  activation and all four services report active. No pending reconciliation
  or deployment refusal was reported.
- A new WebSocket client used the installed Codex-generated schemas to call
  `skills/list` with `forceReload: true`, first at the runtime worktree and
  then at a fresh empty temporary directory. Both returned the documentation,
  review and handoff skills enabled, with zero discovery errors. This verifies
  discovery in a fresh context without creating a new conversation or model
  turn; it does not guarantee future authoring quality or refresh instructions
  already present in existing conversations.
- The live initiative page returned successfully through its portal socket and
  rendered the assessment, rollout and all four review artifact entries.
- No live rollback was necessary. The predecessor remains available; isolated
  link rollback and the host activation/rollback VM checks passed.

Final default-branch CI passed on both providers; see [verification.md](verification.md).
The three clean feature worktrees were removed after integration and deployment,
retaining branches, comparisons and the open session. The source path in the
executed command is therefore historical; the deployment uses the retained
immutable package in the user profile.
