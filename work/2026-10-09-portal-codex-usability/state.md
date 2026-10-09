---
lifecycle: active
---

# 2026-10-09-portal-codex-usability

## Status

Ready, awaiting merge approval. Implementation, independent review, browser and
package checks, and aitherdev host/profile deployment have passed. Live assets
match the final sources; credits and all three banked resets are visible. No
reset was redeemed. The existing Codex process stayed running.

This initiative was created by this conversation with
`dev-session start portal-codex-usability --no-codex --no-attach --json`.
It has no retained team; the lead owns design and application edits.

- [x] Planning and read-only investigation
- [x] Implementation and project documentation
- [x] Quick checks and committed branch inventory
- [x] Independent review
- [x] Full verification and publication
- [x] Aitherdev host and user-profile deployment
- [ ] Integration (awaiting explicit direction)

## Next actions

Ready for use after refreshing the browser. Integration requires explicit
direction for the four repositories and their master branches; no integration
has been authorized. Preserve the active initiative and retained branches.
See [review.md](review.md) and [rollout.md](rollout.md).

## Documentation

Provider reference and portal README/guide updated. See [design.md](design.md) and [review-packet.md](review-packet.md).

## Repositories

All feature branches are `2026-10-09-portal-codex-usability`, published over SSH
and retained. No default-branch integration authorized.

| Project | Base | Current head |
| --- | --- | --- |
| codex-web | 3d07cf60 | 860d515d0aa5d2f7ad68893db41f0969c78e00a7 |
| dev-workspace | c51ba3c0 | 675504f638d21578e87a94f460cc9cbf9e0df395 |
| workspace | 747e9a87 (registered 4ac9ef3e) | 5448392af308b64cd28af4c0c665d68cf81e18a7 |
| vpsfree-cz-configuration | ae670dc0 | 081ac7cc6098f79b004f7ff349e71c85257b518f |

Canonical worktrees are `worktrees/2026-10-09-portal-codex-usability/<project>`.
Corrections and repeated dependency updates are folded into owning commits.
No obsolete approach or migrations. See [review.md](review.md),
[review-remediation-packet.md](review-remediation-packet.md) and [rollout.md](rollout.md).

## Verification

- Quick: 59 provider Node tests and five mocked reset-controller tests pass.
  Focused Go account/client/cache and shipped browser API contracts pass.
- Protocol: selected native Codex 0.160.0 experimental schemas pass the full
  corpus; optional account/reset RPC supported.
- Review: all four Important findings fixed; same independent reviewer passes
  the focused lock design. Eight coherent commits and no migrations.
- Browser: all seven cases pass across full and focused runs. Chromium and
  Firefox cover presentation/restoration; native two-page reset locks, shared
  storage, same-key recovery, text paste and binary/mixed attachments pass.
- Provider package: Nix flake checks and exact-head CI37943560998 pass.
- Runtime CI: exact final head675504f6 passes run37945562244 (fast job;
  unchanged host VM job is skipped on feature branches).
- Runtime/workspace package and host build pass in 1,757 seconds. Full log
  /tmp/portal-usability-package-checks.log. Host generation
  2026-10-09--17-06-31; kernels fetched from cache, no local kernel build.
- Composition: check passes at runtime675504f6; extension source preserved.
- Deployment: exact host generation 2026-10-09--17-06-31 dry-activated and
  switched, then the composed workspace user profile switched successfully.
  Live portal/provider assets match the final sources. Read-only account checks
  report credits, three available resets and three expiration/detail rows.
  Codex MainPID 1204139 and native version 0.160.0 were preserved. Public TLS
  with the configured local CA returns the expected unauthenticated HTTP401.
  No live reset use. Exact deployed store paths are in [rollout.md](rollout.md).

Detailed review and failed-check diagnosis: [review.md](review.md).
Prepared transition and exact sources: [rollout.md](rollout.md).
Complete cleaned branch series: [final-inventory.md](final-inventory.md).

## Cleanup

Preserve unrelated shared workspace changes. Retain branches and this session.
All four source worktrees are clean and their published feature refs match the
recorded final heads. Shared master contains four pre-existing unpublished
coordination commits beneath this initiative's initial plan; leave their
publication to their owners. This handoff adds one consolidated local tracking
checkpoint. No feature content is integrated by that checkpoint.

## Browser verification correction

First long batch: provider Nix checks pass; settings, lifecycle, history paging
and repository browser cases pass. Three fixtures failed: question warning
still used the old ten-second grace; archival metadata assertions targeted the
old values container despite metadata already living under Technical details
in the base revision; asynchronous reset confirmations raced listener handling.
Fixtures now use current timing/selectors and await dialog handling. The
focused reruns pass; the final presentation fix opens the existing Workspace menu. Complete log /tmp/portal-usability-full-verification.log.

CI cancellation of superseded run 37943731262 was refused with GitHub API403
because the token lacks cancellation permission; no other runs were targeted.
Read-only native account check confirms credits and all three banked resets.
No live reset redemption was performed.
