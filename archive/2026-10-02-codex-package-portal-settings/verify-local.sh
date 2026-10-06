#!/usr/bin/env bash
# Session-owned verification only; never selects a live profile or live state.
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-02-codex-package-portal-settings
group=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-codex-package-portal-settings
generic="$group/dev-workspace"
consumer="$group/workspace"
test "$(git -C "$generic" rev-parse HEAD)" = 40838aa28c8433e42a4a3fbed4586a3df0146de9
test "$(git -C "$consumer" rev-parse HEAD)" = c5d8bed5fcd3bc01ce18831ea680aac7edfd68ee
test -z "$(git -C "$generic" status --porcelain --untracked-files=no)"
test -z "$(git -C "$consumer" status --porcelain --untracked-files=no)"

cd "$consumer"
nix build --accept-flake-config --print-build-logs --out-link "$tracking/candidate-workspace-package" .#default
nix flake check --accept-flake-config --print-build-logs
candidate=$(readlink -f "$tracking/candidate-workspace-package")
assembled=$(readlink -f "$candidate/libexec/codex")
nix-store --query --references "$assembled"
nix-store --query --requisites "$assembled"
"$assembled/bin/codex" --version

cd "$generic"
nix build --accept-flake-config --impure --print-build-logs --out-link "$tracking/review-assets" --expr \
  'let flake = builtins.getFlake "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-codex-package-portal-settings/dev-workspace"; pkgs = import flake.inputs.nixpkgs { system = "x86_64-linux"; }; in pkgs.callPackage /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-codex-package-portal-settings/dev-workspace/nix/review-ui.nix {}'
driver=$(nix build --out-link "$tracking/playwright-tools" --print-out-paths --inputs-from . nixpkgs#playwright-test)
browsers=$(nix build --out-link "$tracking/playwright-browsers" --print-out-paths --inputs-from . nixpkgs#playwright-driver.browsers)
fixture=$(mktemp -d /tmp/codex-package-browser.XXXXXX)
git archive HEAD | tar -x -C "$fixture"
# Standard build-generated assets go only into this disposable checkout.
cp "$tracking/review-assets"/review-* "$fixture/portal/internal/web/static/"
cd "$fixture/portal"
nix shell --inputs-from "$generic" nixpkgs#go nixpkgs#stdenv.cc^out nixpkgs#nodejs -c \
  env NODE_PATH="$driver/lib/node_modules" PLAYWRIGHT_BROWSERS_PATH="$browsers" PORTAL_BROWSER_TEST=1 \
  go test ./internal/web -run '^TestQuestionBrowser/team_settings_browser_test.cjs$' -count=1 -timeout=5m -v

private_contract=$(mktemp -d /tmp/codex-package-contract.XXXXXX)
env CODEX_HOME="$private_contract" CODEX_SQLITE_HOME="$private_contract" OPENAI_API_KEY= CODEX_API_KEY= \
  "$candidate/bin/workspace-host" check-codex --codex "$assembled/bin/codex"

cd "$generic/portal"
nix shell --inputs-from "$generic" nixpkgs#go nixpkgs#stdenv.cc^out nixpkgs#python3 -c \
  go build -o "$tracking/compat-probe" "$tracking/compat_probe.go"
nix shell --inputs-from "$generic" nixpkgs#python3 -c "$tracking/compat-probe" \
  /nix/store/4mxlhqv9angcqgjw4c067nfpjlxv3d4h-codex-0.159.2/bin/codex "$assembled/bin/codex"
nix shell --inputs-from "$generic" nixpkgs#python3 -c python3 "$tracking/daemon_probe.py" "$assembled/bin/codex"
