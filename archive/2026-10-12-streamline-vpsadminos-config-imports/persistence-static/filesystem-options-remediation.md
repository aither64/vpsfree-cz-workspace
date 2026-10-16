# Non-bind fixture options remediation

Read compatibility-pure-rerun1.log in full. The filesystem shell fixture
explicitly set options=[]; the upstream option type requires a nonempty list.
Only tests/nixos-container-persistence-eval.nix changes: the filesystem fixture
now uses [ "defaults" ]; the declared bind fixture retains [ "bind" ].
This preserves bind identity versus other-filesystem presence handling and
shell filtering. Raw files, guide, other tests and every assertion are unchanged.
The other 13 owned technical paths match their prior frozen hashes.

Prepared nixfmt --check, nix-instantiate --parse and git diff --check passed.
Only the changed owned test is restaged, preserving all other index content.
Source is frozen again. No Nix eval/build/runtime, commit or ref operation.
Parent owns rerun2 of the normal pure build:

    nix build .#checks.x86_64-linux.nixos-container-persistence --no-link
