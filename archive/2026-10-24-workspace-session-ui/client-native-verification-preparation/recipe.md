# Post-review client native verification preparation

**Preparation only. No tests, native/version/provider execution, build, Nix
setup/evaluation or live operation was performed.** DeepSeek preparation remains
frozen and was not rerun. Parent must complete combined final review before
launching this bounded package.

Client: `975746f40fe99c77689ede064197772e2cc25c18`.
Runtime: `b24164822fd33c330a6e5511e4d1580ab6590224`, selecting client
`v0.0.0-20261025170722-975746f40fe9` and llm-agents
`ea188d2f072e0ec8d5b71245e228803672801a22`.
[inputs.json](inputs.json) binds committed file/blob/mode/SHA256 identities,
native bytes, existing receipt hashes and retained prerequisite links.

Commands reuse committed client `docs/reference.md:986` (state fixture),
`:1242` (native contracts) and `:1276` (namespace prerequisites/selectors).
The additional strict provider-selection selector is the existing
`codex/ephemeral_provider_integration_test.go:20`; it uses synthetic providers.
No new fixture framework or full quick-suite rerun is proposed.

## Prerequisites and ownership

- Already realized/rooted prerequisite: `native0164-prerequisite/codex-0.164-prerequisite`
  points to `/nix/store/16f481b2zzvyvr2ycw51sm51b3f0508f-codex-0.164.0`;
  `codex-0.164-source` points to `/nix/store/10pdz4z8bfg35ysd7aqrhnzdkijpmmwb-source`.
  Existing watcher/derivation receipts and these symlink targets were inspected
  read-only; no roots were created or changed.
- Retained old native: `/nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0/bin/codex`;
  source: `/nix/store/9is267xl3palxb615kk86qlli9nggkf9-source/codex-rs`.
  Owner0 confirmed provenance. The saved recursive old graph identifies
  `nzagi1sc4hjfjcq411pvaishwjjbbxn7-codex-0.163.0.drv`, its source,
  daemon patch/postPatch and assembly output `jrsm...`. Preserve the retained
  generation/package; fresh old-native/source root protection remains a
  parent launch gate, not a new claim from this preparation.
- Parent still supplies verified absolute `ip`, `nft` and `sqlite3` executables
  in the declared Nix fixture environment. Owner0 has no previously verified
  tool-path receipt. Do not guess store paths or silently realize missing tools.
  The committed flake's Go/GCC/Python environment alone does not declare these
  three native-fixture tools. Namespace/firewall/mount capability is also
  unproven until the ownership control runs.
- Parent supplies an immutable client source path matching the runtime lock's
  client revision/NAR `sha256-+tqKIdYu5jHkE/jL9cY0DtxAAJMcOehZ5HJ95JdLB6s=`.
  Its Luna catalog must be canonical, read-only, 62680 bytes, SHA256
  `049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1`.
  The full catalog is 472072 bytes, SHA256
  `943ca7fe1d19ed019054158303f0dbbd80b3bef43b3aa425a71aa7cb3fb52c2b`.
- Final system/application assembled paths, retained roots, manifest/helpers/
  daemon-copy/closure evidence and actual launch identity remain parent-output
  gates. These raw-native results can be reused only after the final assembled
  native is byte-identical to reviewed `d2af...`; equal version text is insufficient.

A fresh parent-owned verification watcher gets this exact command packet,
canonical cwd, frozen revision/manifest and per-command log/exit destinations.
Use the installed session utility policy and fresh context; full-access launch
is `--sandbox danger-full-access --ask-for-approval never`. One watcher can own
this related serial batch. It executes/monitors only: no edits, diagnosis,
retries, acceptance, deployment or nested agents. Preserve each real exit and
elapsed time; report any still-running operation. Missing prerequisites or a
failed selected check returns to the parent. No host-network fallback, skipped
assertions, relaxed tool policy or invented quiet-run timeout is permitted.

## Exact future selectors and environment

Run from `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-workspace-session-ui/codex-web`
inside its declared Nix environment, retaining the complete Go/GCC stdenv as in
`../codex-web-naming/run-go-quick-naming-tmp-v2.sh`. Reuse its short-TMPDIR
lesson, not its already-used temporary directory or quick-suite commands.
Before launch, the parent checks the existing complete final tested-tree/input
manifest against this exact client HEAD, with no extra source files; changed
source/inputs require reconciliation and applicable review. No test listing or
compilation was launched for this preparation.

```sh
set -euo pipefail
test "$(git rev-parse HEAD)" = 975746f40fe99c77689ede064197772e2cc25c18
: "${IN_NIX_SHELL:?declared repository environment required}"
: "${CLIENT_IMMUTABLE_SOURCE:?verified exact client Nix source required}"
: "${NATIVE_FIXTURE_IP:?verified absolute ip executable required}"
: "${NATIVE_FIXTURE_NFT:?verified absolute nft executable required}"
: "${NATIVE_FIXTURE_SQLITE:?verified absolute sqlite3 executable required}"
native_tmp=$(mktemp -d /tmp/cn.XXXXXX)
export TMPDIR="$native_tmp"
printf 'owned TMPDIR=%s\n' "$native_tmp"
unset CODEX_WEB_TEST_BINARY CODEX_EPHEMERAL_TEST_NAMESPACE
unset CODEX_EPHEMERAL_TEST_OUTER_PID_NAMESPACE CODEX_EPHEMERAL_TEST_OWNERSHIP_HELPER
unset CODEX_EPHEMERAL_TEST_OWNERSHIP_ROOT CODEX_EPHEMERAL_TEST_OWNERSHIP_PID_NAMESPACE
export CODEX_EPHEMERAL_TEST_IP="$NATIVE_FIXTURE_IP"
export CODEX_EPHEMERAL_TEST_NFT="$NATIVE_FIXTURE_NFT"
export CODEX_EPHEMERAL_TEST_SQLITE="$NATIVE_FIXTURE_SQLITE"
old_native=/nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0/bin/codex
new_native=/nix/store/16f481b2zzvyvr2ycw51sm51b3f0508f-codex-0.164.0/libexec/codex/bin/codex
old_source=/nix/store/9is267xl3palxb615kk86qlli9nggkf9-source/codex-rs
new_source=/nix/store/10pdz4z8bfg35ysd7aqrhnzdkijpmmwb-source/codex-rs
old_sha=8d733334a9ce033fd57f0e3c08064d2b1ec549d7b7f29949ae44b24e87a7c15a
new_sha=d2af1cd0ea4187d413c237e80204e94ffcd5c7d8142840a662156b89750f54ae
luna_catalog="$CLIENT_IMMUTABLE_SOURCE/codex/ephemeral_luna_models.json"
printf '%s  %s\n' "$old_sha" "$old_native" "$new_sha" "$new_native" | sha256sum -c -
printf '%s  %s\n' \
  049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1 \
  "$luna_catalog" | sha256sum -c -

# No model/native prerequisite for the ownership control itself. Run first.
go test -mod=readonly -tags=codex_integration ./codex \
  -run '^TestEphemeralNamespaceOwnershipIntegration$' -count=1 -timeout=180s -v

# Prompted raw 0.164: full selected suite, Luna/low.
export CODEX_EPHEMERAL_TEST_BINARY="$new_native" CODEX_EPHEMERAL_TEST_SHA256="$new_sha"
export CODEX_EPHEMERAL_TEST_SOURCE="$new_source"
export CODEX_EPHEMERAL_TEST_MODEL=gpt-6-luna CODEX_EPHEMERAL_TEST_CATALOG="$luna_catalog"
go test -mod=readonly -tags=codex_integration ./codex \
  -run '^TestPromptedEphemeralProtocolIntegration$' -count=1 -timeout=180s -v

# Retained strict 0.163: full hostile-dispatch suite, GPT-5.5/low.
export CODEX_EPHEMERAL_TEST_BINARY="$old_native" CODEX_EPHEMERAL_TEST_SHA256="$old_sha"
export CODEX_EPHEMERAL_TEST_SOURCE="$old_source" CODEX_EPHEMERAL_TEST_MODEL=gpt-5.5
unset CODEX_EPHEMERAL_TEST_CATALOG
go test -mod=readonly -tags=codex_integration ./codex \
  -run '^TestEphemeralProtocolIntegration$' -count=1 -timeout=180s -v

# Same strict suite and old binary, canonical Luna/low profile.
export CODEX_EPHEMERAL_TEST_MODEL=gpt-6-luna CODEX_EPHEMERAL_TEST_CATALOG="$luna_catalog"
go test -mod=readonly -tags=codex_integration ./codex \
  -run '^TestEphemeralProtocolIntegration$' -count=1 -timeout=180s -v

# Affected retained strict provider-routing fixture: synthetic providers only.
CODEX_WEB_TEST_BINARY="$old_native" go test -mod=readonly ./codex \
  -run '^TestPinnedCodexEphemeralProviderSelection$' -count=1 -timeout=180s -v

# Two-binary saved-state sequence; provenance strings identify actual receipts.
CODEX_UPGRADE_OLD_BINARY="$old_native" CODEX_UPGRADE_OLD_SHA256="$old_sha" \
CODEX_UPGRADE_NEW_BINARY="$new_native" CODEX_UPGRADE_NEW_SHA256="$new_sha" \
CODEX_UPGRADE_CLIENT_REVISION=975746f40fe99c77689ede064197772e2cc25c18 \
CODEX_UPGRADE_OLD_PROVENANCE='/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/workspace-input-preparation/selected-profile-derivations.json#sha256=78a33d8c2642243cf1401e73a18bde8a48bf8cb66fd37bb00879b4a39ee4f577' \
CODEX_UPGRADE_NEW_PROVENANCE='/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/codex-web-naming/final-source-input-graph.json#sha256=8e0be88eeecf9aead1386ee84f2c8db04aaa6ba3ec757f47e74dca9a890b221b' \
go test -mod=readonly -tags=codex_integration ./codex \
  -run '^TestNativeStateUpgrade0163To0164$' -count=1 -timeout=180s -v
```

The protocol fixtures require matching versions/hashes and fail missing
prerequisites. Select entire suites, not just baseline subtests. Prompted
0.164 observes actual advertised schemas and shared-runner fixed requests,
native retry/terminal proof, output, questions and teardown; it makes no
empty-tools/absent-handler claim. Both strict0.163 profiles retain empty-tool
and hostile native-dispatch requirements. The separate provider-selection
fixture uses strict Luna and proves one selected synthetic provider hit with
zero default-provider hits; it is not raw0.164 or real-provider acceptance.

## Private state, process completion and retained evidence

The protocol fixture itself creates Linux user/network/mount/PID namespaces,
mounts private `/proc` and `/etc`, and restricts egress with nftables to its
synthetic provider. Its reexecuted test process is PID1. Ownership is checked
before every namespace-wide signal; both native process owners are waited,
adopted descendants are reaped through ECHILD, then same-home restart/persistence
checks proceed. The ownership control covers detached/orphaned descendants in
two cycles. Never forge its child markers or signal the host process domain.
The provider-routing fixture separately owns and waits its direct process in a
private home/cwd/socket with an explicit environment; it has no namespace-wide
signalling authority.

The state fixture (committed SHA256
`9eaff2784a5b9c420aed201bfb397c3c6bf3b28086ad181a21d172c5d9c1da32`)
uses the existing recovery harness, a private 0700 home/cwd/socket and allowlist
environment, synthetic loopback Responses and SQLite client receipts. It does
not claim the protocol fixture's namespace isolation. One version runs at a
time:0.163 seed -> stop/join ->0.164 cold reads without inference -> explicit
root resume/new turn/fork ->0.164 restart -> stop/join/offline snapshot ->0.163
old-reader cold reads last at the same original path. Held queues and receipts
remain intact and undispatched; cold phases require no provider hits.

Record the printed `/tmp/codex-native-upgrade-evidence-*` path before harness
cleanup. Retain `assertions.json`, `upgrade-result.json`, native log, exported
thread receipt JSON, complete `before-old-reader/{home,client-receipts}` with
sidecars/inventory/assertions, and after-old-reader inventories/copies. Upgrade
and old-reader outcomes remain separate. Old-reader success proves only those
cold reads, not old writes, concurrent writers or safe downgrade. Recovery is
forward-only; failures require parent disposition without automatic rollback.

Watcher logs/exit receipts bind exact client HEAD, command, binaries, source/
patch/catalog hashes, namespace observations, elapsed time and any unfinished
process. Preserve owned evidence and the short TMPDIR for parent reconciliation;
this packet authorizes no session or unrelated fixture cleanup.

Real-provider transport acceptance, the runtime's exact packaged naming-child
positive canary within its original 30-second deadline, managed-service
lifecycle/creation acceptance, DeepSeek and final assembly/actual-daemon checks
remain separate parent packages. None is replaced by these synthetic-provider
client fixtures, and none was launched here.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
