# 2026-10-14-investigate-nixos-flake-ssl

## Goal

Investigate the issue in https://discourse.vpsfree.cz/t/nixos-flake-update-ssl-connect-error/370/2

Is it something caused by a container configuration in vpsAdminOS? (They're talking about VPS (containers) on vpsAdminOS). Looking at my /etc/resolv.conf, I also have domain set on multiple machines and yet I haven't had an issue with it.

## Affected repositories

- Read-only investigation of `vpsadminos` container compatibility modules and
  osctld DNS configuration through its canonical bare repository.
- Upstream NixOS, glibc, Nix and curl resolver behavior as needed.
- No application/configuration implementation or production changes planned.

## Approach

1. Read all posts in the linked Discourse topic.
2. Trace the origin of `domain`/`search` in container `/etc/resolv.conf`.
3. Check public A/AAAA and wildcard DNS answers for the reported names.
4. Compare IPv6-only `getent hosts` with application address resolution and
   establish why Nix can differ from curl.
5. Explain platform responsibility, conditions that trigger the problem, and
   bounded diagnostic/mitigation options with evidence and uncertainty.

## Decisions

- Lead owns the investigation. Same-session retained roster inspected; findings
  and tracking alone do not trigger independent final review.
- Do not modify live resolver files or another session's worktrees.
- Prefer bounded read-only network requests and isolated resolver checks.

## Compatibility and deployment

Investigation changes no state formats, APIs, schemas, protocols, Nix options,
running nodes or containers. No deployment, mixed-version update, or rollback
is required. Any proposed container resolver change must preserve intentional
short-name resolution and be presented as a recommendation.

## Documentation

Readers: the requesting operator and future investigators. Preserve the
evidence and limitations in session findings, and current progress in state.
Update owning-project documentation only if implementation becomes necessary.

## Testing plan

Quick checks: public DNS A/AAAA queries, read container and upstream resolver
source, and isolated process-local search-domain comparisons. No full build or
integration suite is needed for this investigation. If verification expands to
a long or uncertain build/test, use the required fresh utility watcher.
