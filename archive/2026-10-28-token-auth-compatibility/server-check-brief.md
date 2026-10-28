Post-review server adapter/profile verification. Exact clean source head
2f5156262baaf137800c17a9321e617c2b5df1d5 in
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-token-auth-compatibility/haveapi.
Use dev-session-monitor; session identity verified by parent. Catalog watcher
Luna/low and native full-access utility. Run only:

HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -euo pipefail -c 'cd servers/ruby && bundle exec rspec spec/client_examples/go_spec.rb spec/client_examples/profiles_spec.rb spec/client_examples/profile_mount_spec.rb'

Capture complete stdout/stderr in session server-adapter-check.log with exact
exit status. Expected under 1 minute; if exceeds 5 minutes report running status
and retain ownership, no automatic cancellation. No source edits, diagnosis,
retry, deploy or acceptance. Return revision/command/elapsed/exit and bounded
failures. This batch follows independent review, avoids duplicate full suites
already in exact-head CI. No kernel build expected; stop/escalate unexpected
kernel build. No nested agents.
