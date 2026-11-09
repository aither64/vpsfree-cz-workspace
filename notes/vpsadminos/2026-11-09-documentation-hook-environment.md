# Narrow hook tools for documentation-only vpsAdminOS changes

The default vpsAdminOS development shell includes MkDocs, Ruby bundle setup and
other development tools. For a documentation-only commit, realizing that shell
can prepare unrelated Python/Tkinter and bundix dependencies before reaching
hook setup. The shell is still appropriate when its full toolset is needed.

A smaller repository-pinned environment worked for the documentation cleanup:

```sh
nix shell --inputs-from . nixpkgs#overcommit nixpkgs#nixfmt nixpkgs#ruby
```

Inspect `.overcommit.yml` and custom hooks before legitimately signing changed
configuration. Keep the installed hooks enabled. The packaged Overcommit wrapper
uses a private gem environment; Ruby processes spawned by Git hooks need its
matching `GEM_HOME` and `GEM_PATH` (or a correctly configured pinned bundle).

For the inspected nixpkgs `c56a87d8e41ce69bd2af57eb35dcc117a9dfca33`, the successful
gem root was
`/nix/store/2pz9r5iwiqqspbkmk8klbcl6ak3pjykz-overcommit-0.68.0/lib/ruby/gems/3.4.0`.
Both variables used that value during the ordinary commit. Precommit and commit
message hooks passed. Resolve the root again for a different package/pin.

A checkout hook failure can occur after Git has created a complete worktree.
Reconcile the exact owned path, branch, HEAD and status before retrying setup;
finish public registration through the ordinary worktree command. Do not delete
the checkout or bypass hooks merely because its creation command returned failure.

The canceled full-shell client was joined and verified gone before the narrow
setup. No kernel build, source workaround or hook bypass was needed. The final
documentation-render check remains separate from commit-hook preparation.

Evidence: `work/2026-11-08-documentation-governance-review/state.md` and package P2
completion report; committed source head `6154dbcd5eaea4a505168f2a7f4fdc25aed4c96d`.

[Session evidence](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-08-documentation-governance-review/)
remains discoverable if its records later move through authorized archival.
