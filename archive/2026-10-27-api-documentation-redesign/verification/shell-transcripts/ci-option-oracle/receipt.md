# CI option-name expectation correction

Commit `c79645e0d43885c26cdc4129cbac96fdd5a13b07`, tree
`802bfb1c1f2398f58858f393c8214f0ad9352855`, direct parent
`aee093cd3387c261570067e58b7f1e16029e3619`.

Exactly one line in `servers/ruby/spec/client_examples/shell_spec.rb:187`
now derives the expected option using `malicious_option.tr('_', '-')`.
Production already normalizes complete option names. The retained original CI
failure from release 41033397096/job 123988272695 shows `/work/_temp/` in the
stale expected option and `/work/-temp/` in the actual option. Applying the
existing normalization matches that exact raw difference. The hostile value,
marker path, shell execution and absent-marker assertion remain unchanged.
See [original excerpt](original-ci-excerpt.txt) and [exact patch](correction.diff).

Complete owning shell spec: **13/0**, actual failing CI seed **55311**,
0.78989s + 1.14s load. One-file RuboCop and `git diff --check` passed. Normal
mandatory HaveapiI18n/RuboCop/message hooks passed; message width had a non-failing
72-column warning, with every line within the required 80-column limit.
Existing declared Ruby 3.4.11, candidate-local frozen server/root bundles and
already-equal copied guide were reused; no setup or documentation generation.

[result.json](result.json) proves checked/staged/committed/index/current identity,
clean source/index, exactly +1/-1 in one file, unchanged production and all
other local refs. [Shell](shell.json), [lint](lint.json) and
[commit](commit.json) retain commands/results; adjacent logs retain output.

**SOURCE/Git/CHECK RELEASED.** All owned handles completed, with no active or
uncertain effects. No publication, network, CI retry or broader checks.
Main owns direct narrow-fix inspection under mandatory-change-review step 9,
then any publication/integration/CI disposition. No default, release,
deployment or lifecycle action was performed.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/)
