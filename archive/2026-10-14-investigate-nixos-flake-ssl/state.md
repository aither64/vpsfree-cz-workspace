---
lifecycle: archived
---

# 2026-10-14-investigate-nixos-flake-ssl

## Status

- Phase: findings ready; identity verified against the thread binding and both
  environment markers. Source tracing and bounded local checks completed.
  No implementation, independent review, or deployment performed.
- The vpsAdminOS module's static nameservers trigger upstream NixOS domain
  generation. Wildcard AAAA/search fallback reproduces the bad `getent hosts`
  result; current dual-stack curl and Nix still succeed. The original Nix-only
  connection path needs evidence from the affected VPS.
- Follow-up: vpsAdminOS does not assign a guest domain; the first reporter
  explicitly configured one. Confctl can default networking.domain from
  machine.host.fullDomain. These findings do not establish a vpsAdminOS defect.

## Phase checklist

- [x] Verify session identity and inspect retained roster.
- [x] Read the discussion and identify reported DNS substitution.
- [x] Trace vpsAdminOS and upstream NixOS resolver configuration.
- [x] Verify DNS/search behavior and explain the limits of Nix/curl inference.
- [x] Record evidence and report conclusions and remaining uncertainty.
- [x] Distinguish implicit domain assignment from upstream resolver generation;
  verify confctl's conditional domain default.

## Next actions

- No further local work is required for the requested explanation. If exact
  original Nix failure attribution is needed, obtain effective resolver/NSS
  configuration, address-family behavior, and Nix/curl versions and connection
  evidence from the affected VPS.

## Documentation

- [Findings and source/check evidence](findings.md).
- No code or owning-project documentation change was necessary.
- Initial plan/state/manifest committed on shared master as `959fbf5a`.
- Portal artifact registration refused with "session creation is unfinished;
  retry dev-session start" despite the retained tracking manifest reporting
  creation ready. Findings remain linked from this state. No lifecycle retry or
  session reinitialization was performed; that is outside this investigation.

## Repositories

- `repos/vpsadminos.git`, read-only `origin/staging` reference; no feature branch
  or worktree registered. Initial reference:
  `1150e37b1cc997b1728f2fda806a3433ef55b798`.
- `repos/confctl.git`, read-only local `origin/master` reference
  `cc40679d267165aecfa569128438bb55fe910268`; no branch/worktree changes.

## Commands run

- Discussion JSON read and converted to text; canonical vpsAdminOS staging
  fetched and relevant module/osctld source inspected.
- Public DNS A/AAAA queries; process-local `LOCALDOMAIN` comparisons using
  getent, Python getaddrinfo, curl, and bounded Nix prefetch.
- Source evidence links and exact inspected project revisions in findings.

## Results

- The discussion's third post reports `api.github.com.panpanika.eu` as an IPv6
  result. Public DNS currently returns that AAAA and the same answer for a
  fresh label, consistent with wildcard DNS. `api.github.com` currently has
  an A record and NOERROR/no-answer for AAAA.
- The compatibility module sets nameservers and disables host resolv.conf
  inheritance; searches found no domain/search override. Upstream source
  tracing confirmed that NixOS supplies the domain when static
  nameservers and networking.domain are both configured.
- Current local Nix and dual-stack curl succeed under the same domain override;
  the original Nix TLS failure itself was not reproduced. Investigation-only
  deliverables do not trigger mandatory independent final review.

## Open questions

- Original VPS Nix/curl backend/version, resolver options, sudo environment,
  and actual connection address are unavailable in the discussion.

## Cleanup

- Session remains open. No lifecycle, production, or application mutations.
