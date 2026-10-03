# Declared Nix environments and hooks in restricted member shells

In session `work/2026-10-03-newadmin-exception`, an implementation member with
writable assigned source paths could not connect to the Nix daemon, and its
socket-backed API localization hook later failed with `EPERM`. These are runtime
access limits; writable source paths alone do not imply socket access.

For tooling already prepared by the lead in the repository's declared Nix shell,
the lead generated an exact cached environment with `nix print-dev-env --offline`.
Sourcing that script once provided the cached tools and ran `shellHook`; evaluating
the hook again was unnecessary. The API shell automatically enters `api/`, so
`nix develop .#api -c bundle exec rspec ...` must not include another `cd api`.

The member retained all application edits, lint and hook preparation. Lead then
executed the member-prepared unchanged commit with all mandatory hooks enabled
in the socket-capable declared root shell. The API localization hook passed.
The same approach supported the member-prepared channel generator, without
hand-editing locks or bypassing hooks.

An ambient-shell push was independently refused by Overcommit's signature
check. Reviewing/signing the unchanged configuration and publishing from the
same declared root shell succeeded. Keep hook verification and Git operations
in the intended environment; a successful commit in one shell does not prove
another shell has matching Overcommit signatures.
