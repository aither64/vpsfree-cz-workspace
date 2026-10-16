# Cycle assertion remediation

Read compatibility-pure.log in full. It reports upstream filesystems.nix selecting
.result from a cyclic topology, a hard missing-attribute error not caught by
tryEval. The correction touches only tests/nixos-container-persistence-eval.nix.

The test now imports utils.fsBefore from each actual pinned release source and
uses that release library's toposort on effective boot.specialFileSystems. It
requires no result, a reported nonempty cycle, and both expected state/log
mountpoints in that cycle. It does not force generation of the impossible
activation script. The unused failure helper is removed. All positive generated
script, global order, backend, dry, root, declaration, standalone, equivalence
and shell assertions are preserved.

Known static checks passed: nix-instantiate --parse, prepared nixfmt --check,
and git diff --check. Hash comparison confirms the other 13 owned technical
paths stayed byte-identical to the prior frozen receipt. No Nix evaluation/build
or runtime was launched. Only the changed test is restaged; the rest of the
lead's existing index is preserved. Product HEAD remains 84d2fbe0607aa768b10a5acf5f6e952e423493c5.

The normal affected verification is:

    nix build .#checks.x86_64-linux.nixos-container-persistence --no-link

The parent owns its fresh watcher and subsequent checks. Source is frozen again.

Current test sha256: 4457cc607bbb5781d42308a139c219e0784b3bb336a29e4ea1690f461c005287
