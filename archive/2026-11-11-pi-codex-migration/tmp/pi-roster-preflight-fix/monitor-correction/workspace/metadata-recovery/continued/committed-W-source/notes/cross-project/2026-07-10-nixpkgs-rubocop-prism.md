# nixpkgs RuboCop can miss its Prism dependency

Initiative: `work/2026-07-10-kb-czech-fixes`

Running `nix shell nixpkgs#rubocop -c rubocop ...` with the 2026-07-10
workspace nixpkgs failed before linting. RubyGems reported that `rubocop-ast`
required `prism ~> 1.7`, but Prism was not available on the generated gem load
path. Adding `nixpkgs#rubyPackages.prism` to the shell did not change the load
path used by the RuboCop executable.

Use the target repository's own development shell and hook-managed RuboCop
when it declares one. Do not assume the standalone `nixpkgs#rubocop` executable
is self-contained. A RuboCop setup borrowed from another repository may also
be unsuitable when its `TargetRubyVersion` differs; in this case it targeted
Ruby 2.7 and rejected Ruby 3 keyword shorthand already used by the workspace.

For this initiative, Ruby 3.4 syntax checks, unit tests, explicit line-length
inspection, and `git diff --check` were used as fallback validation because the
coordination repository has no Ruby hook framework.
