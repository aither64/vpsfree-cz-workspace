# Portal character highlighting rollout

## Status

Deployed and verified on aitherdev as user-profile generation 46. HTTP, asset,
service and live Chromium acceptance all passed. No operator action remains for
the requested fix. All three reviewed heads are now merged and pushed to their
respective `master` branches; both default-branch CI runs passed. All owned
worktrees and transient captures have been removed, retaining branches and useful
evidence. The session remains open.

## Package chain

- Runtime: `5d853b6b0c2608549a1f0e940c680ccb40a14bec`.
- Extension: `b75cc8a6270219ca2fc25c1e292ce030fc33e45d`.
- Workspace: `80b93a8c6b120ce178b4a6479901fde12156e3d5`.
- Branch in each: `2026-09-15-portal-diff-highlighting`.
- Previous observed profile: generation 45,
  `/nix/store/kimxny34bbmdybfpj7v6mlz6z88zsk5k-dev-workspace-0.2.0`.
  Recheck immediately before activation in case another deployment occurs.

## Deployment procedure

After mandatory review and package checks, build the consuming workspace package
from its exact committed feature worktree. Confirm feature refs/pins and save
package identity and previous profile/runtime process identities. Activate with:

```sh
workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-15-portal-diff-highlighting/workspace
```

The stable helper owns package compatibility checks and user-service activation.
No system configuration change or confctl deployment is needed. Preserve the
existing Codex runtime, extension catalog and all session state. Do not bypass a
refusal by stopping or mutating another session.

## Acceptance

- Active profile must equal the built site package; user services remain active.
- The served review-editor.js must match the reviewed/rebuilt bundle and be
  served without a stale cache directive.
- Open the user's saved comparison in Chromium, checking both unified and split
  layouts. The removed line 106 and added line 112 must have continuous character
  emphasis over their content. Merge adjacent DOM segments when measuring, since
  Shiki foreground token spans can split one background decoration.
- Verify source text and totals (+206/-75 for the reported file), syntax worker
  readiness, line navigation, browser errors and asset failures. Save concise
  results and useful screenshots as session artifacts.
- Inspect runtime and extension feature CI before reporting completion.

## Recovery

The visual repair changes no persistent format, source/range API, cluster
contract, authority or Codex version. The preceding profile remains available
through ordinary `workspace-host rollback`; it restores old visual behavior
without data migration. Use rollback only if activation/acceptance exposes a
failure. Do not roll back a concurrent later deployment. No live rollback test
is needed for this browser-only fix.

## Results

All four mandatory lanes completed with no Blocking or Important findings.
General Advisory G1 (stale status wording) was corrected. Runtime and extension
feature CI passed; extension CI includes full flake checks and devcluster-check.
The local consuming package and clean workspace deployment-contract check passed.

The documented switch command completed successfully and selected
`profile-46-link`, retaining `profile-45-link`. Deployed package:
`/nix/store/rl1kpyjg28kvvsyiykqkwl9fl34mmi1g-dev-workspace-0.2.0`.
It matches the reviewed/built source chain exactly. Codex protocol 0.154.0 was
verified by activation. Portal/router restarted normally; Codex PID 1090021 and
tmux PID 435397 were retained. All four services are active. The NixOS system
path is unchanged. No rollback was necessary.

Authenticated HTTPS verified with the site's CA returns 200 for health/session
and the editor asset, whose SHA-256 matches the built reviewed bundle:
`26acff84839bdaf5b7274326551e50be8b9d995b8a11cc03c27e29e408d96401`.
The asset is served `no-store`; unauthenticated access remains 401. Evidence:
[post-deployment.json](post-deployment.json).

Candidate Chromium checks passed with a local editor override before activation.
Live checks against the actually deployed asset passed with no local override.
Both layouts preserve +206/-75 counts, syntax coloring and selected line links.
The checked old/new lines each have one continuous character-highlight span, with
no page errors or failed assets. See [browser-results.json](browser-results.json),
[unified screenshot](fixed-unified.png) and [split screenshot](fixed-split.png).
Browser requests other than GET/HEAD were blocked, including the
page's background queue reconciliation, so the source session is not modified.

All three reviewed heads were fast-forwarded and pushed to `master` on
2026-09-15 after the user requested integration. No source head changed and no
additional deployment was needed. Runtime target-checkout build and all 13
editor tests passed; extension target-checkout flake evaluation passed.
Default-branch CI results and cleanup are recorded in [state.md](state.md).

The deployment command and `verify-deployment.py` are retained as execution
evidence: their exact source-worktree paths require recreating clean checkouts
at the recorded revisions after worktree cleanup. Browser verification also
requires Nix Node, Playwright and the portal-owner group described in the notes.
The session and retained branches remain available for follow-up.
