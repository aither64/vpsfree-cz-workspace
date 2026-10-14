---
lifecycle: active
---

# 2026-10-14-investigate-nixos-flake-ssl

## Status

- Phase: investigation; identity verified against the thread binding and both
  environment markers. No implementation, review, or deployment performed.

## Phase checklist

- [x] Verify session identity and inspect retained roster.
- [x] Read the discussion and identify reported DNS substitution.
- [ ] Trace vpsAdminOS and upstream NixOS resolver configuration.
- [ ] Verify DNS/search behavior and explain Nix/curl differences.
- [ ] Record evidence and report conclusions and remaining uncertainty.

## Next actions

- Check upstream NixOS resolvconf generation and the resolver used by Nix.

## Documentation

## Repositories

- `repos/vpsadminos.git`, read-only `origin/staging` reference; no feature branch
  or worktree registered. Initial reference:
  `1150e37b1cc997b1728f2fda806a3433ef55b798`.

## Commands run

## Results

- The discussion's third post reports `api.github.com.panpanika.eu` as an IPv6
  result. Public DNS currently returns that AAAA and the same answer for a
  fresh label, consistent with wildcard DNS. `api.github.com` currently has
  an A record and NOERROR/no-answer for AAAA.
- The compatibility module sets nameservers and disables host resolv.conf
  inheritance; searches found no domain/search override. Continue upstream
  tracing before attributing the application failure.

## Open questions

## Cleanup

- Session remains open. No lifecycle, production, or application mutations.
