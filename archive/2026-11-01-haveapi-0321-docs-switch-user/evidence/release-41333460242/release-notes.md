# Sun Nov 01 2026 - version 0.32.1

## Ruby server

- Add `switch_user_revoke_params` for provider-specific revoke parameters when
  switching documentation accounts. Providers can close shared SSO while
  ordinary Sign out keeps its existing behavior.

## Development tooling

- Skip quick performance comparisons for new branches created at a commit
  already contained in the default branch.
