---
lifecycle: abandoned
---

# 2026-09-13-partial-ip-replace

## Repositories

- `vpsadmin`: canonical bare repository `repos/vpsadmin.git`; read-only inspection
  of fetched `origin/master`. No feature branch or worktree needed for source review.
- Inspected revision: `6923c7bfcb628f6acacb4e6fc62806084afc8213`.

## Status

- Verified current session matches `DEV_SESSION_SLUG`.
- Investigation finished: partial transfer/replacement is unsupported.
- Public IPv4 + IPv6 replacement works with replace=true and transfer=false.
- Private IPv4 preservation + IPv6 replacement has no supported flag combination.
- Detailed evidence and conceptual follow-up design are in `investigation.md`.

## Commands run

- `dev-session current`: `2026-09-13-partial-ip-replace`, matching the environment.
- Inspected workspace rules and the handoff skill; preserved other sessions' changes.
- `git fetch origin master` in the bare vpsAdmin repository fetched current source.
- `git show` / `git grep` traced API inputs, operation mapping, migration branch
  selection, allocator, resource recharging, WebUI, and existing migration specs.
- Initial coordination commit: `7e92a43` (plan, state, and portal manifest), after
  fetching workspace origin and confirming local master was ahead, not divergent.
- Attempted to open the immutable raw GitHub source through the web reader for
  links; it returned a cache miss. Evidence comes from the successful SSH fetch
  and local Git object reads, not the web reader.
- `dev-session url 2026-09-13-partial-ip-replace --as-is` returned the portal URL.

## Results

- Transfer is all-or-error and takes precedence over replacement.
- Replace changes every attached allocation, including shared private IPv4.
- Both flags disabled remove attached IPs for cross-location migration.
- No tests executed; this was a read-only source investigation. Existing migration
  tests inspected do not exercise the requested partial scenario.
- Mandatory change review is not applicable: no project implementation,
  configuration, product documentation, deployment, or security changes.

## Open questions

- None blocking the investigation. Any follow-up implementation needs a decision
  on exposing a compatible mixed IP policy; no implementation was requested.
- Live production revision and network records were not inspected.

## Cleanup

- Leave session open. No lifecycle action requested.
- No project worktrees, feature branches, clusters, or transient captures created.
- Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-13-partial-ip-replace/
