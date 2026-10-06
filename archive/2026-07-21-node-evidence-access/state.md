---
lifecycle: abandoned
---
# 2026-07-21-node-evidence-access

## Repositories

- `vpsadmin`
  - branch: `2026-07-21-node-evidence-access`
  - worktree: `worktrees/2026-07-21-node-evidence-access/vpsadmin`
  - review base: `origin/master` at `88f03da44`
- `security-advisories`
  - branch: `2026-07-21-node-evidence-access`
  - worktree:
    `worktrees/2026-07-21-node-evidence-access/security-advisories`
  - initially created from the repository default branch at `55e26c3`, then
    fast-forwarded to the current advisory review branch at `06ddc840`

## Status

- Active initiative verified through both `bin/dev-session current` and the
  matching `VPSFREE_DEV_SESSION_SLUG` environment variable.
- Isolated worktrees are prepared and source-clean.
- Review plan and compatibility boundaries are recorded.
- Source, authorization, reporter, WebUI and reference-consumer review is
  complete.
- Field-by-field findings and the recommended projection design are recorded
  in `work/2026-07-21-node-evidence-access/review.md`.
- Focused current-behavior verification passed. No product behavior has been
  changed.

## Commands run

- `bin/dev-session current`
- `git status --short --branch` in the shared workspace
- read the `vpsadmin-security-audit` skill
- fetched `vpsadmin` and `security-advisories` over their existing SSH remotes
- inspected recent vpsAdmin Node-evidence history and prior initiative notes
- `bin/dev-session worktree add 2026-07-21-node-evidence-access vpsadmin
  --as-is`
- `bin/dev-session worktree add 2026-07-21-node-evidence-access
  security-advisories --as-is`
- read both repository-local `AGENTS.md` files
- fast-forwarded the initiative's `security-advisories` branch to
  `origin/2026-07-20-security-advisory-review` at `06ddc840`
- inspected all Node kernel evidence API resources, their shared scope and
  projection helpers, models, API specs, and authorization rules
- inspected WebUI Node routing, rendering helpers, regression coverage, and
  Playwright coverage for member/admin evidence behavior
- inspected the libnodectld security-evidence reporter, its exact software
  components, boot data, and 34 tracked sysctls
- inspected the public vpsAdminOS and vpsFree.cz configuration sources for
  actual kernel-parameter and sysctl value classes; no production data was
  queried
- inspected the security-advisories collector, API permissions, and evidence
  contract
- verified current GitHub visibility of vpsAdmin, vpsAdminOS, the Linux tree,
  and vpsfree-cz-configuration as public
- `nix develop .#api -c bundle exec rspec
  spec/api/resources/node_kernel_history_spec.rb
  spec/api/resources/node_kernel_evidence_spec.rb`
- `git diff --check` in the shared workspace
- `git status --short --branch` in both initiative worktrees

## Results

- The shared workspace checkout already contained unrelated modified and
  untracked files; none were changed by this initiative apart from its own
  `work/2026-07-21-node-evidence-access/` tracking files.
- Current vpsAdmin `origin/master` includes the recent kernel history, boot
  evidence reconciliation, generalized system-configuration evidence, and
  software revision-link changes.
- The security-advisories post-checkout hook could not load its locked RuboCop
  gems in the ambient shell. `bin/dev-session` recovered and registered a
  clean worktree. Any hook or test command must run inside `nix develop`.
- Current access is intentionally split: authenticated users receive a
  sanitized active-host kernel history, while every lossless top-level evidence
  resource remains administrator-only. No bypass was identified.
- The focused API verification passed: 20 examples, 0 failures. It covered
  ordinary-user sanitized history, anonymous denial, inactive/service-host
  exclusion, ordinary-user denial of typed evidence, and admin resource shapes.
- The existing top-level evidence resources must not simply have their
  authorization widened. Several support fleet-wide/inactive history and all
  expose internal associations or evidence metadata. New active-Node-scoped
  public projections are recommended instead.
- Recommended for authenticated members: current booted/activated software
  identities and sanitized deployment history, current evidence freshness and
  generic completeness, and explicit allowlists of member-observable boot
  parameters and sysctls.
- Recommended to remain administrator-only: raw command lines and unrestricted
  parameters, full sysctl inventory/history, kernel configuration/options,
  loaded modules, Nix closure paths, boot/evidence IDs and revisions, raw
  collection errors and gaps, and livepatch/eBPF implementation details.
- Exact software revisions are a reasonable transparency boundary because all
  referenced source repositories are public and the WebUI already generates
  only configured HTTPS commit links.
- Both project worktrees remain source-clean. Shared-workspace unrelated
  changes remain untouched, and this initiative's documentation passes
  `git diff --check`.

## Open questions

- User review of the recommended field boundary is pending.
- Before implementation, agree on the exact public boot-parameter and sysctl
  allowlists. The review proposes initial categories and names, but recommends
  a final product/security decision because these lists become a durable public
  contract.
- The review recommends all authenticated members can inspect all active
  Node/storage hosts, consistent with existing public Node status and member
  kernel/system history. Confirm this whole-fleet scope before implementation.

## Cleanup

- Keep both review worktrees until the user has reviewed the findings.
- No feature branches should be deleted during cleanup.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
