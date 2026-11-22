# nixpkgs RuboCop wrapper can have an inconsistent Prism closure

## Symptom

Running `nix shell nixpkgs#rubyPackages.rubocop -c rubocop ...` fetched RuboCop
1.80.2 but failed before linting because `rubocop-ast` required Prism `~> 1.7`
while the closure provided Prism 1.6.0.

## Workaround

For a vpsAdmin-related maintenance task, use the RuboCop bundle in the
vpsAdmin API development shell:

```sh
nix develop .#api --command bundle exec rubocop ...
```

This successfully linted the task. Remember that this shell changes its
working directory to `api`, so adjust paths accordingly.

Related initiative: `archive/2026-09-07-fix-ip-charged-environments/`.
