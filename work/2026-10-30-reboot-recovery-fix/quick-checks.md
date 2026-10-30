# Quick verification

At codex-web d3a29bee90ef00a08816920408c596152339a637 (same source before commit),
from runtime worktree:

    nix develop --command bash -c 'cd ../codex-web && go test -mod=readonly ./codex -run TestListThreadsStateDBOnly -count=1'

Passed in 0.030s. Initial Go-only nix shell lacked gcc; full runtime Nix shell
provides the compiler. No source workaround.

At runtime f05f50eed6dbfa2794502653176f0bbbbf20f1fa (same source before commit):

    nix develop --command bash -c 'cd portal && go test -mod=readonly ./internal/workspacecodex -run "TestRetainedDiscoveryAfterRestart|TestArchiveDiscovery|TestThreadlessObservation" -count=1'

Passed in 0.066s. A Python try/finally temporarily removed only the
ModelProviders empty-slice line from discovery.go and ran:

    go test -mod=readonly ./internal/workspacecodex -run TestRetainedDiscoveryAfterRestartIncludesPreviousProviders -count=1

Failed as expected: `a retained active conversation is absent from archive
discovery; pages=0 loaded reads=1`. Restoring the line made the same command pass
in 0.044s. The working file was restored before commit; no test-only changes remain.

Both project branches passed git diff --check. Configuration f9a69961 hooks
passed Nixfmt and commit-msg checks (generated message width warning allowed).
Workspace 1deb88301 passed git diff --check and:

    bin/check-dev-workspace-deployment --workspace-root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-reboot-recovery-fix/workspace --configuration-root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-reboot-recovery-fix/vpsfree-cz-configuration

Result: deployment contract passed at f05f50eed6dbfa2794502653176f0bbbbf20f1fa.
Library CI 41137125628 passed on exact d3a29bee90ef00a08816920408c596152339a637.

Vendor calculation command was `nix build --no-link --print-build-logs
.#packages.x86_64-linux.dev-workspace.goModules`; expected hash mismatch output
is retained in vendor-hash.log. Final vendor hash is
sha256-B4Ohm0GVtPb6weaOcRG4uCF1IyCrxCP3bDzCmUz9cxQ=.
