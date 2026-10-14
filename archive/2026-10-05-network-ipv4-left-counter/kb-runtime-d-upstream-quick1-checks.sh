#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/dev-workspace
prefix=kb-runtime-d-upstream-quick1
verify() {
  test "$(git -C "$repo" rev-parse HEAD)" = c582ee757cd5b55c69db7b030ffd25eae8e5635b
  test "$(git -C "$repo" branch --show-current)" = 2026-10-05-network-ipv4-left-counter
  sha256sum --check "$tracking/$prefix-source.sha256"
  diff -u "$tracking/$prefix-source.diff" <(git -C "$repo" diff --binary)
  diff -u "$tracking/$prefix-source.index" <(git -C "$repo" diff --cached --binary)
  diff -u "$tracking/$prefix-source.status" <(git -C "$repo" status --porcelain=v1 --untracked-files=all)
}
run() {
  local name=$1
  shift
  set +e
  (cd "$repo"; "$@") >"$tracking/$prefix-$name.log" 2>&1
  local result=$?
  set -e
  printf '%s\n' "$result" >"$tracking/$prefix-$name.exit"
  cat "$tracking/$prefix-$name.log"
  return "$result"
}
verify
export TMPDIR=/tmp
unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_PATH BUNDLE_BIN BUNDLE_WITH BUNDLE_WITHOUT
export GEM_HOME="$(ruby --disable-gems -rrubygems -e 'print Gem.default_dir')"
export GEM_PATH="$GEM_HOME"
run toolchain bash -ec '
  test "$(readlink -f "$(command -v gofmt)")" = /nix/store/3yh8g6m3balbhzxsx77jlyyx443bxqii-go-1.26.6/share/go/bin/gofmt
  go version
  go env GOROOT GOMODCACHE
  ruby -rjson -rrbconfig -rrubygems -rminitest -rtimeout -e '\''
    features = $LOADED_FEATURES.grep(%r{/(?:minitest(?:/|\.rb)|timeout\.rb)})
    specs = %w[minitest timeout].to_h { |name| [name, Gem.loaded_specs.fetch(name).full_gem_path] }
    raise "non-Nix Ruby or gems" unless RbConfig.ruby.start_with?("/nix/store/") &&
      specs.values.all? { |path| path.start_with?("/nix/store/") } &&
      features.all? { |path| path.start_with?("/nix/store/") }
    raise "ambient RubyGems path" unless Gem.path.all? { |path| path.start_with?("/nix/store/") }
    puts JSON.pretty_generate(ruby: RUBY_DESCRIPTION, executable: RbConfig.ruby,
      minitest: Minitest::VERSION, timeout: Timeout::VERSION,
      gem_paths: Gem.path, gem_specs: specs, loaded_features: features)
  '\''
'
run formatting-syntax bash -ec '
  test -z "$(gofmt -l portal/internal/web/operation_state.go portal/internal/web/operation_state_test.go)"
  git diff --check -- portal/internal/web/operation_state.go portal/internal/web/operation_state_test.go
  ruby -c libexec/workspace-host
  ruby -c test/workspace_host_test.rb
  ruby -c test/workspace_host/commands_and_locks_test.rb
'
run focused go -C portal test -mod=readonly ./internal/web -json -count=1 -timeout=5m -run '^(TestLifecycleFreshOwnerReconciliation.*|Test(Archive|Delete)JournalRetryRefusesASameKindReplacementWhileWaitingForTheLock|TestLifecycleRetryCompareAndSwapRejectsAReplacementReceipt|TestLifecycleReconciliationCannotOverwriteRetryOrResurrectDismissedReceipt|TestLifecycleTargetAttemptRejectsLateResultWithTheSameReceipt|TestLifecycleSnapshotGETDoesNotWaitForGenerationOrReceiptMutex|TestDisplayGenerationContentionKeepsReceiptUnchanged)$'
run web go -C portal test -mod=readonly ./internal/web -json -count=1 -timeout=5m
run dispatch ruby test/workspace_host_test.rb --name '/capture_lease|non_streaming_provider_dispatch/'
verify
