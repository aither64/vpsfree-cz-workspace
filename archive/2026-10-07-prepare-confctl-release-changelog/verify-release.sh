#!/usr/bin/env bash
set -euo pipefail

records=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-07-prepare-confctl-release-changelog
source_tree=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-07-prepare-confctl-release-changelog/confctl
expected_head=1b56616eff41e760327f3a0dbed8875e4aa9dbec

cd "$source_tree"
test "$(git rev-parse HEAD)" = "$expected_head"
test -z "$(git status --porcelain=v1)"
export CONFCTL_TEST_NIXPKGS
CONFCTL_TEST_NIXPKGS=$(nix eval --raw --impure --expr '(builtins.getFlake (toString ./.)).inputs.nixpkgs.outPath')
export NIX_PATH="nixpkgs=$CONFCTL_TEST_NIXPKGS"
spec_work=$(mktemp -d "$records/rspec-ruby34.XXXXXX")
(
  export BUNDLE_GEMFILE="$source_tree/Gemfile"
  cd "$spec_work"
  bundle exec rspec -I "$source_tree/spec" --require "$source_tree/spec/spec_helper.rb" "$source_tree/spec"
)
bundle exec rubocop --parallel --force-exclusion
git ls-files -z '*.nix' | xargs -0 nixfmt --check
nix shell --inputs-from . nixpkgs#ruby_3_3 -c bash "$records/verify-ruby33.sh"

# The gemspec falls back to directory globbing in Git worktrees. Build a clean
# export so only committed source and generated documentation enter the gem.
release_tree=$(mktemp -d "$records/release-source.XXXXXX")
git archive "$expected_head" | tar -xf - -C "$release_tree"
git ls-files -z > "$records/release-source-files.list"
export BUNDLE_GEMFILE="$release_tree/Gemfile"
export RUBYLIB="$release_tree/lib"
cd "$release_tree"
bundle exec rake md2man:man build

gem_file="$release_tree/pkg/confctl-3.0.0.gem"
bundle exec ruby "$records/inspect-package.rb" "$gem_file" "$records/release-source-files.list" "$records" "$expected_head"
mkdir -p "$source_tree/pkg"
cp "$gem_file" "$source_tree/pkg/confctl-3.0.0.gem"
sha256sum "$source_tree/pkg/confctl-3.0.0.gem" > "$records/gem.sha256"
cd "$source_tree"
test -z "$(git status --porcelain=v1)"
bash "$records/verify-nix-package.sh"
printf 'Verified release head: %s\n' "$expected_head"
