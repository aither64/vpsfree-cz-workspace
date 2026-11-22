# confctl checks from a sandboxed team member

Related initiative: `work/2026-10-08-remove-software-pins-support/`.

A retained implementation member could write its assigned worktree, but
`nix develop -c ruby -c ...` failed before Ruby with EPERM on the Nix daemon
socket. Saved `workspace_write` access established source access; it did not
grant the shell access to the daemon. Session identity was valid after checking
`dev-session current` from the bound tracking directory.

The lead's fresh verification watcher successfully bootstrapped the declared
Nix shell and installed/signed Overcommit. The lead then resolved tool paths
with `nix print-dev-env --json`. The implementer used that shell's Ruby/nixfmt
binaries directly for syntax/format checks, without a daemon call or hook
bypass. For Bundler, preserve the worktree's GEM_HOME/GEM_PATH, BUNDLE_GEMFILE,
BUNDLE_PATH and BUNDLE_APP_CONFIG. Do not reuse unrelated-session gem directories.

Daemon-dependent evaluation and tests ran through parent-owned verification
watchers. Keep application edits with the implementer; do not change retained
access or sandbox settings merely to run these checks. Inspect every tool exit
before reporting a check as passed.

For watcher batches, a parent-written script with process-start redirection and
one exit-status artifact per command avoids ambiguous background launches and
transcript-derived logs. The first watcher batch here left RSpec incomplete;
its empty log was not accepted as verification evidence.

Overcommit temporarily stashes unstaged content before checking staged files.
Owned intent-to-add entries used to expose new files to Nix can make that stash
refuse. Removing only those index markers before staging the intended commit
preserves file content; no hooks or checks need to be bypassed. Here all final
commits passed the installed hooks. A member SSH fetch also failed on ownership
validation of a systemd-provided SSH proxy config inside the Nix store; the
parent's ordinary canonical fetch succeeded without changing SSH configuration.

Disposable non-Git flake snapshots also need explicit `path:` references,
including builtins.getFlake strings and external fixture installables/lock
commands. Bare absolute snapshot discovery hit the existing Nix2.34.8 failure
`git+file:///tmp` before evaluation. Reuse
`notes/cross-project/2026-10-06-explicit-path-for-exported-flakes.md`; correct
only verification references, preserve repository sources/locks and failed logs,
and rerun through a fresh watcher. Package/RSpec builds and help had already
passed, so they did not need to be repeated.

Actual CLI relative flake installables still require a configuration Git
repository in these disposable checks. Explicit path URLs fixed source/export
evaluation but did not alter CLI discovery. Initialize only each disposable
configuration Git repository and stage its source and lock, following the
existing spec/integration fixture helpers. Do not change ancestor repositories
or application installable semantics to repair a verification fixture.

The example contains five skeleton directories but its generated
cluster/cluster.nix enables only the two NixOS machines. Derive fixture machine
expectations from the declared module list, rather than counting skeleton
directories. Here the CLI/evaluation/lock checks succeeded and a parent-written
expected-name assertion alone failed; correcting and checking the completed
captures avoided repeating the successful Nix operations.

The carrier/netboot and deploy/flakes integration fixtures lock before Git
initialization. With the declared Nix version, their bare `nix flake lock`
commands discovered `git+file:///tmp` and failed before test assertions. The
same commands existed at v3. Using `nix flake lock "path:<fixture-dir>"` at
that boundary keeps later Git setup and update coverage intact. Preserve the
original failure evidence and retry only affected selectors after review.

Use `./test-runner.sh` for confctl integration checks. Calling the generic
component's Nix-store `bin/test-runner` directly lacked its Ruby load path and
failed with `LoadError: test-runner/cli`; the repository wrapper supplied the
declared environment. The runner accepts one path pattern. Its matching uses
Ruby `File::FNM_EXTGLOB`, so a quoted brace pattern selects a bounded batch;
preview its output with `ls` and assert the intended selectors before running.
