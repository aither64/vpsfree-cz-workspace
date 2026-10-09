# Nix lock updates need Git in a clean environment

A targeted `nix flake update kb-runtime` in a Git worktree reported a new lock
entry, then failed with `executing "git": No such file or directory`. The parent
had supplied Nix and the system bin directory in PATH; Git was available only
through the user's selected store package.

The lock was partly updated, while Git's index remained empty. Preserve the
failed log and inspect the tree/index before continuing. Include the exact
existing Git bin directory alongside Nix in the clean PATH, then repeat only
the mechanical input generator with a new receipt. That corrected command
completed with exit0. Do not treat the initially written lock as a successful
native generation result or restore unrelated files.

Session: work/2026-10-05-network-ipv4-left-counter/state.md.
