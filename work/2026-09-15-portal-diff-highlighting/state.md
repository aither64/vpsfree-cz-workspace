---
lifecycle: active
---

# Portal character highlighting fix

## Current status

The fix is deployed on aitherdev and all three reviewed heads are merged and
pushed to `master`. The live editor matches the reviewed build; Chromium
acceptance passed for the reported saved comparison in unified and split layouts.
All 13 editor tests, package checks, mandatory review and feature CI passed.
Both default-branch CI runs passed. All three feature worktrees and the two
temporary integration worktrees have been removed; feature branches are retained.
No source changes or further deployment were needed during integration. The session remains open for follow-up.

Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-15-portal-diff-highlighting/

## Repositories and integration

All retained local and remote feature branches are
`2026-09-15-portal-diff-highlighting`. The reviewed heads below were merged by
fast-forward into each remote `master` without rebasing or changing their content.

| Name | Reviewed base | Final merged feature head |
| --- | --- | --- |
| dev-workspace | `9a1b16464e45d722110b448a79315a0f3ce134aa` | `5d853b6b0c2608549a1f0e940c680ccb40a14bec` |
| vpsfree-dev-workspace | `c6afe2905506fba0b8e372e0436b570f5597f8bd` | `b75cc8a6270219ca2fc25c1e292ce030fc33e45d` |
| workspace | `259c0c3fe7d4f3d454f8b27172cb7a8f99ca79be` | `80b93a8c6b120ce178b4a6479901fde12156e3d5` |

The workspace feature was rebased onto shared master before review. Runtime code
and both consuming pins are separate commits. No npm, Codex, cluster input,
system configuration or state contract changed. No hook framework is declared
in these repositories; none was bypassed.

All three comparisons were recaptured before integration. Independent projects
were merged, checked and pushed from fresh detached target worktrees under
`worktrees/2026-09-15-portal-diff-highlighting/merge/<name>`. The workspace feature
was integrated from the shared master checkout, preserving the unrelated staged
diff byte for byte. Explicit fetches proved that the exact local and remote
feature heads are ancestors of their respective remote masters. See
[integration-results.json](integration-results.json).

## Investigation and repair

See [diagnosis.md](diagnosis.md). The immutable portal payload exactly matches
both Git objects and all 31 independent Git change blocks (+206/-75). The old
model reproduced the deployed bundle and the same fragments in 100 repeats;
removing scan/time limits in three checked blocks did not change the result.
Commit `1741603` lost CodeMirror presentation cleanup while preserving exact Git
line ranges. The fix restores existing `presentableDiff` for cosmetic marks.

The four new regressions failed on the old implementation and pass with the fix.
They cover complete identifiers and unrelated multiline replacements in both
layouts. Existing source identities, bounds, unusual/Unicode contents, Git
counts and line links remain covered. Presentation cleanup is still heuristic;
no new similarity or line-pairing policy was introduced.

## Verification

- Confirmed `dev-session current` equals `DEV_SESSION_SLUG`.
- Locked npm dependencies installed using Nix Node/npm. `npm run build && npm
  test`: 13/13 pass, including the fresh runtime integration checkout.
- `git diff --check` and all three `nix flake check --no-build` evaluations passed.
  Extension integration-checkout flake evaluation also passed.
- Consuming site package built successfully. Nix UI tests: 13/13; all Go packages
  pass. Ruby suites: 311 runs/3276 assertions/12 skips; 8/33/0 skips; 77/475/3 skips.
  No failures/errors. Existing Nix configuration disables real tmux tests.
- Clean workspace deployment-contract check: 3 runs, 14 assertions, pass.
- Runtime feature CI [34973505619](https://github.com/aither64/dev-workspace/actions/runs/34973505619) passed.
- Extension feature CI [34973600703](https://github.com/vpsfreecz/dev-workspace/actions/runs/34973600703) passed, including flake checks and devcluster-check.
- Runtime master CI [34976917688](https://github.com/aither64/dev-workspace/actions/runs/34976917688) passed both fast checks and the host activation/renewal/rollback VM test.
- Extension master CI [34976949502](https://github.com/vpsfreecz/dev-workspace/actions/runs/34976949502) passed full flake checks and devcluster-check.
- Workspace has no GitHub workflow; its unchanged reviewed head passed the local
  flake and deployment-contract checks above.

## Mandatory review

[review-packet.md](review-packet.md) records the conservative High classification
for cross-project deployment pins. Four standalone gpt-6-astra/xhigh lanes:
[general](review-general.md), [architecture](review-architecture.md),
[scope](review-scope.md) and [risk](review-risk.md). No Blocking or Important
findings. General Advisory G1 identified stale investigation status wording,
which was reconciled in state and diagnosis without changing implementation.
No review rerun was needed; all integrated heads are the exact reviewed heads.

## Deployment and documentation

[rollout.md](rollout.md) records the executed user-profile activation, package
chain, acceptance and recovery limits. Generation 46 contains
`/nix/store/rl1kpyjg28kvvsyiykqkwl9fl34mmi1g-dev-workspace-0.2.0`; predecessor 45
is retained. Codex 0.154.0 and the original Codex/tmux PIDs were preserved, all
four services stayed active and the NixOS system was unchanged. No rollback was
needed. The user allowed configuration deployment; this application belongs to
the user profile and needed no `vpsfree-cz-configuration` change.

Authenticated HTTPS with the site's CA verified the served editor SHA-256:
`26acff84839bdaf5b7274326551e50be8b9d995b8a11cc03c27e29e408d96401`.
It matches the reviewed build, is served no-store and retains unauthenticated
401 responses. See [post-deployment.json](post-deployment.json).

Candidate and live Chromium acceptance passed both layouts: continuous highlight
spans on checked old/new lines, +206/-75 counts, syntax readiness and old-L106
selection, with no page errors or failed assets. Live acceptance used the deployed
asset without an override. Background queue reconciliation POSTs were blocked;
no source-session records or worktrees were changed. See
[browser-results.json](browser-results.json), [unified](fixed-unified.png) and
[split](fixed-split.png) screenshots. No credentials were copied or printed.

The runtime's adjacent model comment records the presentation-cleanup invariant.
Runtime portal docs, extension README and workspace deployment policy were
checked; no public interface or operator-procedure change warrants larger docs.
Retained verification scripts record the executed checks; recreating their exact
worktree/tool prerequisites is described in rollout.md. Five reusable notes cover
presentation cleanup, UI build order, browser group access, blocked background
reconciliation and absolute tracking paths under `notes/dev-workspace/` and
`notes/cross-project/`, dated 2026-09-15.

## Cleanup and tracking

Initial plan/state commit: `259c0c3`. The user's explicit integration/cleanup
request is recorded in one consolidated tracking checkpoint containing only this
initiative's records and its five notes. Unrelated shared changes are preserved.

Owned temporary input payloads, old/candidate bundles, candidate screenshots,
Nix result links, Playwright link and reproducible build/deployment logs were
removed after retaining their useful results here and in rollout.md. The user's
original attachment remains untouched outside version control. Fixed screenshots,
review reports, exact deployment/merge evidence and feature branches are retained.

All three registered feature worktrees were removed through `dev-session worktree
remove`; their exact final heads remain in portal.yml. Both detached integration
worktrees were removed with non-force `git worktree remove`, then their empty
parent directories were removed. Canonical local master refs were fast-forwarded
to their remote masters. The temporary nested merge directory caused harmless
portal-discovery warnings while it existed; the warning ended after its removal.

The portal still serves this session and its retained artifacts. With worktrees
removed, repository cards report missing local checkouts; recreating a checkout
on the retained branch restores interactive browsing. Saved comparisons remain
in portal storage. No session archive, delete, stop or other lifecycle action was
requested or performed. The session stays active/open. No operator action remains.
