# Python uv tooling on NixOS

During `2026-10-19-dynamic-python-api-client`, a fresh Python client environment
failed on two generic Linux wheel executables even inside `nix develop`:
`uv_build`'s isolated build binary and the venv Ruff executable hit NixOS's
stub dynamic loader. Pure Python pytest ran successfully.

The repository's locked Nix uv was 0.13.0. A backend requirement
`uv_build>=0.13.2,<0.14` forced an isolated newer backend. Allowing
`uv_build>=0.13.0,<0.14` let uv use its native compatible backend, while ordinary
PEP 517 frontends could still select the newer compatible backend. Locked uv
sync then succeeded without a loader bypass.

For Ruff, the declared Python shell supplies a native executable and the dev
lock uses the same version (0.16.10 at this checkpoint). The small project
runner compares `ruff --version` with installed package metadata before
executing it; a mismatch fails. The same entrypoint is used by hooks, the common
check script and CI. Native Ruff and mypy 2.4.0 version checks, example
format/lint checks and the public vpsAdmin description parser test passed.

Use the owning project's current contributor instructions, not these historical
version numbers, for future setup. Do not assume that entering a Nix shell makes
arbitrary wheel binaries executable or bypass failed hooks.

Overcommit also snapshots tracked unstaged changes before checking a commit.
Signing a new working-tree `.overcommit.yml` while leaving the original config
in the index can therefore fail signature verification after snapshot setup.
In this run, setup itself failed before normal restoration, leaving the
automatic stash intact. The owner inventoried that exact same-session stash and
restored only its nine owned root paths to the worktree, preserving the index,
concurrent docs and untracked files. Staging the inspected/signed hook config
with the first tooling commit avoids the old/new signature mismatch. Retain
recovery evidence and never use a broad stash pop, reset or clean to recover a
shared worktree.
