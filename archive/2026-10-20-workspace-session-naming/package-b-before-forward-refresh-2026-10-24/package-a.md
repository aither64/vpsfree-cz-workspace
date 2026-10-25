# Package A: codex-web native retry handling

Published head: `4300c40b6406161afc74c124c40155f28a557032`.
Base: `ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5`.
Branch: `2026-10-20-workspace-session-naming`.
Worktree: `worktrees/2026-10-20-workspace-session-naming/codex-web`.

One focused commit changes `codex/ephemeral.go`, its focused and native tests,
`test/codex_protocol_contract.py` and `docs/reference.md`. No migrations,
superseded approaches, intermediate dependency pins or deployed feature lineage.
The complete exact base-to-head diff is saved as `package-a-final.diff`.
The exact head is confirmed on the SSH remote. Worktree clean. No default-branch
integration or deployment performed. Independent final review is complete. The Important replay finding was fixed
and accepted by lead focused inspection under mandatory-review steps 9–10.
Lead-owned native verification passed on the corrected final A head;
implementer0 owns follow-up fixes.

The prior published head `b81f80586bb933d235447581e22e2a2937ad9388` was
pre-review and undeployed. A late-error regression and fix were folded into the
owning functional commit at the lead's direction, producing intermediate
`ee119a01d1d5ec3e036d1fb5b45791a45e5d9bee`. Contradictory or malformed error
evidence after completion invalidates retry proof before unsubscribe acknowledgement.
The reviewed `96077b62` folded only a native fixture advice correction and its focused
regression into that same commit; production implementation is unchanged from
`ee119a01`. Those rewrites used exact old-head force-with-lease on the owned feature.

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

## Accepted independent-review correction

The intermediate owning commit `f722adab914fa34da9d7c66bca63f9515e1ebf6f` folded
the reviewer's Important buffered post-completion-error fix. A shared lock-required
validator invalidates proof before the error short circuit in both delivery and
replay. Six paired regressions cover permanent false, progress true and terminal
false errors after exact failed completion. Late delivery is synchronized to
unsubscribe rather than relying on response scheduling. Every case requires a
false direct/wrapped accessor, empty output, no private diagnostic leakage, one
start/unsubscribe and zero interrupts. Existing returned error categories remain.

The reviewed source fails all three buffered cases with `retry=true` when
overlaid beneath the corrected regressions; exact output is
`package-a-review-red.log`. Final full focused ephemeral tests passed in 3.209s;
protocol coverage passed; tagged regression/local responder checks passed in
0.129s. Lead independently ran the new regression (PASS 0.127s) and accepted the
exact `package-a-review-correction.diff`; no new design or reviewer rerun.
`package-a-review-checks.md` records commands and limits. Old review evidence is
preserved in `package-a-reviewed-96077*`; all old candidates remain undeployed
provenance. One owning commit remains above the unchanged fresh upstream base.

SSH publication used the explicit exact `96077b6` lease and remote proof. The
immutable Nix source is `/nix/store/x4m4qa56gzm1345m1msxlfhd33krapwl-source`,
narHash `sha256-7GUx9sFhXZP4yd492B7XVG1XeHAYztGkqh+VZsWlbWs=`.
Source is frozen after publication. CI `39818940510` was in progress when checked,
not awaited. Reviewed `96077b6` CI `39814333581` completed successfully; no
superseded queued/running CI required cancellation.

## Diagnosed native fixture correction after first execution

Lead's native watcher at `f722adab` passed namespace ownership but failed only
the two new overload cases at thread/start, before any provider call. Captured
phase evidence shows invalid-request -32600 with no thread/turn/provider IDs;
raw native error text was sanitized. Pinned config validation rejects the
reserved built-in provider ID openai, exactly the entry inserted only by these
fixture modes. Architect independently confirmed this source-backed cause.

The final `4300c40b6406161afc74c124c40155f28a557032` folds ONLY deletion of
that 13-line test override block relative to f722. Production code is identical.
`package-a-native-fixture-correction.diff` is the exact delta. Focused tagged
regression/advice/responder/progress/terminal checks passed in0.725s. Full failed
execution, bounded phase extraction and diagnosis are preserved as
`verification-native-f722-failed.*`, `package-a-native-f722-*` and
`package-a-failed-f722*`. No native rerun was launched by implementer0.

Final SSH publication used explicit f722 lease and exact remote proof. Source
is frozen. Current CI39820073331 was in progress when checked, not awaited;
f722 CI39818940510 completed successfully, no superseded active run to cancel.
Lead owns focused delta inspection and the fresh diagnosed native watcher.

## Corrected native verification result

Lead's fresh watcher on exact final `4300c40b6406161afc74c124c40155f28a557032`
passed namespace ownership (0.159s) and the full protocol fixture (18.911s),
exit0 in25.2s. Evidence is `verification-native-4300.log` and
`verification-native-4300-result.json`. These files explicitly identify recovery
from retained execution-tool output because no live redirected log was present;
no raw phase transcript or extra event counts are invented. Lead inspected the
exact13-deletion fixture delta and accepted the diagnosed rerun as resolving
that fixture failure. This is synthetic native proof, not deployed readiness or
actual selected-provider availability. No native test was run by implementer0.

## Prepared post-review native verification

Not executed by implementer0. The lead assigns a fresh verification watcher
after final review and accepted remediation. Run from the package worktree, ownership fixture first; proceed only if
it passes. These are synthetic private-namespace tests, not live provider proof.

```sh
export CODEX_EPHEMERAL_TEST_BINARY=/nix/store/wz4w670930cksh1ivz13y0gn3c23cjzl-codex-package-0.163.0/libexec/codex/bin/codex
export CODEX_EPHEMERAL_TEST_SHA256=5e538cfe7c25daf382afe195c08b2ffd24415b0cdd7f5456ec0cf1d277c3d1a5
export CODEX_EPHEMERAL_TEST_SOURCE=/nix/store/9is267xl3palxb615kk86qlli9nggkf9-source/codex-rs
export CODEX_EPHEMERAL_TEST_IP=/nix/store/3n7aiwyh3vhx8iqpy6i7jabfr10h4akp-iproute2-7.0.0/bin/ip
export CODEX_EPHEMERAL_TEST_NFT=/nix/store/a7sf90yc74dha1bcj2wx6hh3w10qf19z-nftables-1.1.6/bin/nft
export CODEX_EPHEMERAL_TEST_SQLITE=/nix/store/039a76ld66lja5991ryh4xps79fq379q-sqlite-3.53.1-bin/bin/sqlite3
export CODEX_EPHEMERAL_TEST_MODEL=gpt-6-luna
export CODEX_EPHEMERAL_TEST_CATALOG=/nix/store/x4m4qa56gzm1345m1msxlfhd33krapwl-source/codex/ephemeral_luna_models.json
nix develop --command go test -mod=readonly -tags=codex_integration ./codex -run '^TestEphemeralNamespaceOwnershipIntegration$' -count=1 -timeout=180s
nix develop --command go test -mod=readonly -tags=codex_integration ./codex -run '^TestEphemeralProtocolIntegration$' -count=1 -timeout=180s
```

The immutable catalog comes from this exact committed source's Nix path;
its required SHA-256 is
`049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1`.
The native fixture adds labelled `native-retry`/`native-terminal` cases using
architect-confirmed SSE `response.failed` with `error.code=server_is_overloaded`.
It preserves the built-in OpenAI retry defaults and capabilities. Native stream
ceiling5 permits the two advised overloads then success; advice-free terminal
overload returns before considering the ceiling. HTTP200 does not trigger HTTP
request retries. No reserved-provider configuration override is injected.
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
