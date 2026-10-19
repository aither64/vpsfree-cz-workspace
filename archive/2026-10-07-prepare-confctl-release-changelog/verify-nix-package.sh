#!/usr/bin/env bash
set -euo pipefail
records=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-07-prepare-confctl-release-changelog
package_attr=packages.x86_64-linux.confctl
nix build ".#$package_attr" --no-link --print-out-paths > "$records/nix-package-path.txt"
nix_package=$(cat "$records/nix-package-path.txt")
nix_deps=$(nix eval --raw ".#$package_attr.deps.outPath")
nix_ruby=$(nix eval --raw ".#$package_attr.ruby.outPath")
nix_gem_path=$(nix eval --raw ".#$package_attr.ruby.gemPath")
nix_source=$(nix eval --raw ".#$package_attr.src")
test "$(nix eval --raw ".#$package_attr.deps.gems.confctl.version")" = 3.0.0
test -f "$nix_source/confctl.gemspec"
env -u RUBYOPT -u RUBYLIB -u BUNDLE_GEMFILE -u BUNDLE_BIN_PATH -u BUNDLE_PATH \
  GEM_HOME="$nix_deps/$nix_gem_path" GEM_PATH="$nix_deps/$nix_gem_path" RUBYLIB="$nix_source/lib" \
  "$nix_ruby/bin/ruby" -e 'require "confctl"; source = File.realpath(ARGV.fetch(0)); abort "Incorrect Nix source root" unless File.realpath(ConfCtl.root) == source; loaded = $LOADED_FEATURES.find { |f| f.end_with?("/confctl.rb") }; abort "Incorrect Nix loaded source" unless loaded && File.realpath(loaded) == File.join(source, "lib/confctl.rb"); spec = Gem::Specification.load(File.join(source, "confctl.gemspec")); abort "Incorrect Nix gem version" unless spec && spec.version.to_s == "3.0.0" && ConfCtl::VERSION == "3.0.0"; puts "Nix path-gem: #{spec.full_name}"; puts "Nix loaded source: #{source}"' "$nix_source" \
  > "$records/nix-package-metadata.txt"
env -u RUBYOPT -u BUNDLE_GEMFILE -u BUNDLE_BIN_PATH -u BUNDLE_PATH \
  "$nix_package/bin/confctl" --help > "$records/nix-package-help.txt"
rg -q 'inputs' "$records/nix-package-help.txt"
rg -q 'swpins' "$records/nix-package-help.txt"
cat "$records/nix-package-metadata.txt"
printf 'Verified Nix package: %s\n' "$nix_package"
