# Supply the runtime contract for local migration tests

Running `ruby test/migration_test.rb` from a checkout can fail during helper
loading with `generic workspace runtime contract is missing`. The packaged
flake checks supply the contract; an ambient shell or a Ruby-only Nix shell
does not.

From the extension checkout, derive the contract from its pinned runtime:

```sh
export DEV_WORKSPACE_RUNTIME_CONTRACT="$(nix eval --raw --impure --expr \
  '(builtins.getFlake (toString ./.)).inputs.dev-workspace.lib.runtimeContract')"
nix shell --inputs-from . nixpkgs#ruby -c ruby test/migration_test.rb \
  -n test_user_migration_rewrites_runtime_and_reverses_exactly
```

The focused forward/reverse test passed with 1 run and 15 assertions. No helper
change or compatibility workaround was required. Full packaged checks continue
to own their environment setup.

Related initiative: `work/2026-09-17-documentation-boundaries/`.
