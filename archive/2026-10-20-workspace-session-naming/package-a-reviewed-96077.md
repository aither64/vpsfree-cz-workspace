# Package A: codex-web native retry handling

Published head: `96077b6257bd7dac05930312a29eaf00fc900b3c`.
Base: `ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5`.
Branch: `2026-10-20-workspace-session-naming`.
Worktree: `worktrees/2026-10-20-workspace-session-naming/codex-web`.

One focused commit changes `codex/ephemeral.go`, its focused and native tests,
`test/codex_protocol_contract.py` and `docs/reference.md`. No migrations,
superseded approaches, intermediate dependency pins or deployed feature lineage.
The complete exact base-to-head diff is saved as `package-a-final.diff`.
The exact head is confirmed on the SSH remote. Worktree clean. No default-branch
integration or deployment performed. Independent final review and native execution
remain pending; implementer0 owns follow-up fixes.

The prior published head `b81f80586bb933d235447581e22e2a2937ad9388` was
pre-review and undeployed. A late-error regression and fix were folded into the
owning functional commit at the lead's direction, producing intermediate
`ee119a01d1d5ec3e036d1fb5b45791a45e5d9bee`. Contradictory or malformed error
evidence after completion invalidates retry proof before unsubscribe acknowledgement.
The final `96077b62` folds only a native fixture advice correction and its focused
regression into that same commit; production implementation is unchanged from
`ee119a01`. Both rewrites used exact old-head force-with-lease on the owned feature.

The helper treats exact owned `willRetry: true` as progress. The additive
`CanRetryEphemeralTurn` accessor preserves error categories and allows wrapping;
positive proof requires a structured transient classification, exact failed or
interrupted completion and successful unsubscribe/close cleanup, or a typed
temporary dial failure before any thread was issued. Unknown or permanent errors,
lost start replies, uncertain ownership, cancellation and incomplete cleanup do
not authorize a fresh attempt. Native isolation and output restrictions remain.

## Quick evidence

- `nix develop --command go test -mod=readonly ./codex -run '^TestEphemeral' -count=1 -timeout=45s`: passed, 3.316 seconds.
- After the folded late-error fix, that same focused suite passed in 3.202 seconds.
- Final fixture correction: `nix develop --command go test -mod=readonly -tags=codex_integration ./codex -run '^TestEphemeral(Integration(OverloadAdvice|HTTPFallbackResponder)|NativeRetryProgress|TerminalRetryProof)$' -count=1 -timeout=45s` passed in 0.658 seconds. Its actual-handler regression verifies nested advice for progress, absent advice for terminal failure and success after the two advised overloads, without a listener or native inference.
- Exact installed Codex 0.163.0 generated experimental JSON schemas into
  `/tmp/2026-10-20-workspace-session-naming-implementer0-schema`.
  ErrorNotification matches its native-source schema byte for byte.
- `nix develop --command python3 test/codex_protocol_contract.py /tmp/2026-10-20-workspace-session-naming-implementer0-schema codex/client.go`: compatible.
- `nix develop --command go test -mod=readonly -tags=codex_integration ./codex -run '^TestEphemeral(Native|Terminal|Error|Malformed|PreTurn|IntegrationHTTPFallbackResponder)' -count=1 -timeout=45s`: passed, 0.883 seconds. This compiles the native fixture and runs focused fake/protocol cases; it does not run native integration.
- `gofmt -l` on the four affected Go files and `git diff --check`: empty.
- No declared hook framework, configured hooksPath or active repository hooks.
  Commit ran via Nix Git and a temporary message file without bypass.
- Lead accepted the reference prose unchanged before commit.

## Prepared post-review native verification

Not executed. The lead must assign a fresh verification watcher after final
review. Run from the package worktree, ownership fixture first; proceed only if
it passes. These are synthetic private-namespace tests, not live provider proof.

```sh
export CODEX_EPHEMERAL_TEST_BINARY=/nix/store/wz4w670930cksh1ivz13y0gn3c23cjzl-codex-package-0.163.0/libexec/codex/bin/codex
export CODEX_EPHEMERAL_TEST_SHA256=5e538cfe7c25daf382afe195c08b2ffd24415b0cdd7f5456ec0cf1d277c3d1a5
export CODEX_EPHEMERAL_TEST_SOURCE=/nix/store/9is267xl3palxb615kk86qlli9nggkf9-source/codex-rs
export CODEX_EPHEMERAL_TEST_IP=/nix/store/3n7aiwyh3vhx8iqpy6i7jabfr10h4akp-iproute2-7.0.0/bin/ip
export CODEX_EPHEMERAL_TEST_NFT=/nix/store/a7sf90yc74dha1bcj2wx6hh3w10qf19z-nftables-1.1.6/bin/nft
export CODEX_EPHEMERAL_TEST_SQLITE=/nix/store/039a76ld66lja5991ryh4xps79fq379q-sqlite-3.53.1-bin/bin/sqlite3
export CODEX_EPHEMERAL_TEST_MODEL=gpt-6-luna
export CODEX_EPHEMERAL_TEST_CATALOG=/nix/store/rbfxh0rsz47zp9q74dpmcngsy1abdblq-source/codex/ephemeral_luna_models.json
nix develop --command go test -mod=readonly -tags=codex_integration ./codex -run '^TestEphemeralNamespaceOwnershipIntegration$' -count=1 -timeout=180s
nix develop --command go test -mod=readonly -tags=codex_integration ./codex -run '^TestEphemeralProtocolIntegration$' -count=1 -timeout=180s
```

The immutable catalog comes from this exact committed source's Nix path;
its required SHA-256 is
`049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1`.
The native fixture adds labelled `native-retry`/`native-terminal` cases using
architect-confirmed SSE `response.failed` with `error.code=server_is_overloaded`.
Its test proxy changes only the disposable thread's built-in OpenAI retry caps:
stream retries 2 with two overloads then success, or 0 for terminal failure.
Each progress overload includes `response.error.headers={"retry-after":"1"}`;
terminal overloads omit advice. The pinned native overload path requires that
structured integer-second server advice before retrying, regardless of its
configured retry ceiling. An HTTP-only response header would not satisfy it.
Assertions require actual owned native error/completion events, one turn and no
early interrupt; terminal proof must make the real accessor true. Production
policy, provider capabilities, model/catalog and isolation controls are unchanged.

The B packaged creation fixture separately covers a fresh utility call after
that exact terminal proof and exhausted recovery before session reservation.
Actual selected-provider availability still needs the approved controlled live
verification; synthetic tests cannot establish it.

## Provisional CI failure and corrected fixture

B268 CI run `39810261469` failed the newly added native-positive case, with
`duration_ms=512 outcome=utility_error category=server`, before session reservation.
The fixture injected overloads without nested retry advice. The architect traced
the exact pinned overload parser and retry policy: absent advice makes this
overload terminal before considering `stream_max_retries`. Upstream
`codex-api/src/sse/responses_error_tests.rs:118–139` proves the nested JSON header
shape, and `http-client/src/retry_after.rs:24–38` parses integer seconds.

The missing advice was confirmed in both A/B fixture payloads; adding it only to
the native-progress case corrects the test setup. Two terminal overloads consuming
the two fresh utility calls is consistent with the short failure, but the actual
native RPC frames and POST counts were not retained in that CI artifact, so that
execution sequence is inferred. The failure did not demonstrate a production
parser or ownership defect. Corrected native and packaged execution still require
the lead's final-review and watcher gate; no successful rerun is claimed here.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/>.
