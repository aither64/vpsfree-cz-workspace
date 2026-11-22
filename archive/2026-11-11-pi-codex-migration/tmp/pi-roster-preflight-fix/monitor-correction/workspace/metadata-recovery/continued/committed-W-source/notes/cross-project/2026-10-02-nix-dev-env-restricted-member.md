# Pinned Nix tools in a member shell without daemon access

In session `work/2026-10-02-vpsfbot-github-notifications`, the retained
workspace-write implementer could edit application files, but `nix develop -c
bundle exec overcommit --help` failed with `Operation not permitted` on the Nix
daemon socket. Saved source access did not imply access to that socket.

The lead first had a fresh policy watcher prepare each repository's exact Nix
environment with `nix develop -c bundle check`. After those commands passed,
the lead exported each environment from its corresponding same-session
worktree with `nix print-dev-env` to a task-specific mode-0600 temporary script.
The member sourced the matching script from that repository's worktree to use
its pinned Ruby/tool paths and local dependencies without daemon access.

The exported script runs shellHook itself; do not evaluate shellHook again.
Do not substitute ambient tools, reuse another session's environment/worktree,
disable hooks or escalate the member's sandbox. Inspect the export for
unexpected environment changes, keep it private, and do not commit it.
Daemon-dependent builds/prefetch operations remain lead/watcher tasks.

Lead smoke checks reported Ruby 3.3.10 for the bot and Ruby 3.4.9 for site
configuration, with both dependency checks satisfied. This resolves the tool
execution boundary; it does not replace the repository's required hooks or
verification. See the initiative state for later hook/spec/build results.

The initial worktree additions had already created branches/worktrees and
registered them before their post-checkout hooks failed. Inspect exact ownership
and status before recovery; do not remove/recreate a worktree or bypass hooks
merely because the wrapper returned failure. Session mutations also hold a
shared lock: wait for one to finish before starting the next.

For a longer task, pass `--profile` with a task-specific temporary profile path
when exporting the environment. An earlier unrooted Ruby/tool path disappeared
in this session and had to be substituted again. Preserve the profile while
members use the exported paths; the export alone does not retain the closure.

Use a shell that surfaces startup failure. Here the bot's locked Bundler4.0.12
was installed in `.gems/ruby/3.3.0`, but shellHook exposed only root `.gems`.
The newer root Bundler tried to fetch the locked version from a member shell
without network access. Installing the already-cached locked gem into the root
same-session gem directory with the exact pinned Ruby `gem install --local
--no-document` fixed the lookup without changing lockfiles or dependency
versions. Do not infer this nested-path failure from every Bundler warning;
inspect actual specifications/cache paths first.

Use the same repository environment for Git operations that invoke hooks.
The bot's first push from the outer shell failed Overcommit configuration
signature verification despite successful repository-local commit hooks.
Sourcing the exact exported bot environment and retrying the push passed,
without re-signing, bypassing hooks or editing source. An outer-shell signature
failure alone does not prove that the reviewed hook configuration changed.
