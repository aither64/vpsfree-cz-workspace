# Run dev-session outside HaveAPI's Nix shell

In the HaveAPI patch-release initiative
`work/2026-11-01-haveapi-0321-docs-switch-user/`, invoking `dev-session worktree add`
inside `nix develop` failed before registration mutation. The runtime's pinned
Ruby 3.4.9 inherited HaveAPI GEM_HOME, then tried to load a native json extension
built by Ruby 3.4.11 against GLIBC_2.44.

Run dev-session in the ordinary workspace shell so it retains its own Ruby/gem
environment. Both master and stable worktree registrations then exited zero.
Keep HaveAPI release commands and Overcommit operations inside its declared Nix
shell. When signing another checkout, `overcommit --sign -- TARGET` disambiguates
the target path from the optional hook argument; inspect configuration and hooks
before signing.

Overcommit also reads `.overcommit.yml` from the command's current directory for
pre-push. A push invoked with `git --git-dir=repos/haveapi.git` from the workspace
root failed before remote mutation because that file was absent there. The normal
push from the prepared HaveAPI Nix worktree passed with hooks enabled. Run project
pushes from their worktree even when refs live in a canonical bare clone.
