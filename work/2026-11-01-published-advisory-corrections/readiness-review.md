# Affected readiness-helper review packet

The published advisory implementation is unchanged. The required legacy browser
gate found a healthy API rejected by an obsolete HTML-title readiness check.
The lead accepted a bounded observation-only correction. It is committed and
quick-checked; strict KB and legacy retry remain gated on this affected review.

## Exact source and history

API base `097226b22edf8b59f80b5dfaa55265e9d0cac633`, final head
`0111e97768982701a30634c2277c1c364230067a`. Complete series:

1. A `9415cf2855a3f9caef6ab68dc7df8405ed9f3ef8` — guarded advisory corrections
   and lifecycle actions, including the accepted endpoint inventory and readiness
   observation corrections.
2. B `0111e97768982701a30634c2277c1c364230067a` — legacy advisory management.

Previously accepted range ended at `4cf556e56b522722db18ebf1f1bb5859523e8b4c`.
Its complete successor delta is only
`tests/runner/extensions/vpsadmin_services.rb`, +13/-2. A fold/replay took 69.33s
with normal root Nix hooks. B's binary patch is byte-identical. Final tree
`6b7fb42661283d0fed026c2c138fa477a7f1f34c` matches an alternate-index
reconstruction of `4cf` plus this exact helper patch. Fresh target stayed
`097226b`; feature lease-push and remote SSH proof succeeded, worktree/index clean.
The old head remains under the session-owned `-pre-readiness` ref, alongside
the earlier reviewed/runtime-verified refs. No default history was rewritten.

The final KB successor is one consolidated five-pin commit on unchanged base
`ce2c8cd9358c3636e5d39343e595df813a0b197f`, final head
`fd9267bf43009a567e4b958aaec296bf0a60a8ee`. It selects API
`0111e97768982701a30634c2277c1c364230067a`.
JSON/YAML/Nix and full graph checks pass: other nodes/follows, explicit OS
`6bdf458fd9105379860234ff33d352e55844f08f`, capture/page provenance, assets and
content are preserved. No repeated obsolete pin/fixup stream remains.

NO MIGRATIONS, persisted-state change, API contract, schema, mail, authorization,
production/deployment/default-integration or lifecycle action is introduced by
this successor. Original final/refresh reviews remain in `final-review.md`,
`refresh-review.md` and `review-reconciliation.md`.

## Failure and contract evidence

On exact `4cf`, `./test-runner.sh test 'webui#security-advisories'` exited 1 after
1365.02s. Native run `/tmp/os-test-runner/os-test-webui-fd1a3b33` records one
unexpectedly failed script: readiness timeout at extension line 209 before any
Playwright scenario. No Playwright count is claimed. The watcher's unrelated
1460-RSpec-example statement is discarded.

The service shell log has 245 curl probes. After initial startup, HTTP 200
returned valid HaveAPI 0.32.1 documentation with `<h1>API versions</h1>`, while
the helper required literal `API description`. Puma journal shows both workers
booted and listening at 20:55:12Z. Full native logs are retained. Services and
node1 both record `qemu_exit` status 0 and `destroy`; node2 records no start and
was destroyed. No process references the exact owned run directory. This
failure was diagnosed before retry; deadlines were not increased.

The actual installed HaveAPI `server.rb` root OPTIONS branch supports
`describe=versions`, returning `versions` and `default`, wrapped by the existing
formatter's successful `status`/`response` envelope. The repository already uses
the same curl request and version membership assertion in
`tests/suite/services-up.nix:137`. The extension already requires `json` at line
3 and rescues `JSON::ParserError` in its other parsing context.

## Bounded behavior change

Only `wait_for_vpsadmin_api` changes. It uses the same host and unauthenticated
observation, existing deadline/remaining-budget/curl failure behavior and caller
interface. It requests OPTIONS JSON `?describe=versions`, accepting a Hash
envelope with `status == true`, a Hash response, versions Array and a nonempty
String default contained in that Array. Non-JSON, malformed and error responses
continue through the existing sleep/deadline/error path. There is no generalized
validator, new helper abstraction, timeout increase or authenticated mutation.

## Quick evidence and reuse limits

Root Nix syntax, scoped RuboCop (one file, no offenses) and diff checks pass.
Normal amendment hooks pass, including root RuboCop and both i18n health checks.
A temporary focused direct-method check loads the actual extension with native
runner/osvm dependencies and its existing public hook registration. It verifies
valid readiness, 14 malformed/error/default/version shapes continuing to the next
valid response, and retained timeout class/message and curl exception propagation.
No permanent test framework was added; no existing readiness-unit owner exists.

Evidence lives in
`/tmp/2026-11-01-published-advisory-corrections-acceptance/readiness/`:
`quick.log`, `readiness.patch`, `readiness-range-diff.txt`,
`readiness-final-delta.patch`, `readiness-fold-status.json`, `fold.log`,
`api-flake-metadata.json`, `api-shell-derivation.json`, and
`api-verification-reuse.json`. Direct-method check source is the parent
acceptance directory's `readiness-quick.rb`.

The API subtree is identical to `4cf`. The complete tracked source graph apart
from the already accepted inventory and this helper is identical to actual
runtime-tested `c8ef`; actual final API shell derivation JSON is byte-identical
to that run's derivation, and the full locked graph is equal. The prior effective
full/core environment comparisons remain bound to their actual observation tree
(`c8ef` plus the two-line inventory patch, later committed as `4cf`). Original
full88/core79 successes, client298 and modern successes are retained for their
actual tested SHAs; no unchanged long suite was repeated. The changed readiness
behavior still requires the affected review and real legacy retry.

Strict KB passed on `41097` selecting `4cf` after the separately diagnosed,
unchanged startup fixture race and exact orphan recovery; first failure is
retained in `api-acceptance.md`. The refreshed final pin still needs a fresh strict
check. The lead will release it and legacy after this affected committed review.

Session remains open:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/>
