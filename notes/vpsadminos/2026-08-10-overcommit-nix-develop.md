# Run vpsAdminOS Overcommit inside the Nix development shell

## Symptom

An ordinary `git commit` can invoke the installed Overcommit hook but fail its
Nixfmt check with `nixfmt: command not found` in the ambient shell.

## Cause and workaround

The hook is active, but its formatter dependency is supplied by the repository
development shell. Run the commit itself through `nix develop --command git
commit -F MESSAGE_FILE`; do not bypass the hook. The same environment can be
used for a preliminary `nix develop --command overcommit --run`.

## Verification

The hook completed successfully inside `nix develop` for initiative
`work/2026-08-09-test-vm-kernel-oops`.
