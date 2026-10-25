# HaveAPI 0.30.0 preparation handoff

Ready, awaiting merge approval. Implementation, independent review, local
acceptance and all ten final-head CI workflows passed. The feature branch is
published; master integration and release publication remain separate steps.
The session remains active and open.

## Source and delivered behavior

Repository `vpsfreecz/haveapi`, branch `2026-10-22-haveapi-release`:

- Base and unchanged remote master: `a32b15e379f44fc6dae4b15ef4ec17a142e5f465`.
- Final head: `b64fb25bea8d8222fb3263b99956c0b61438a859`.
- Final tree: `05384a632290653cb4560c7451b3897acd5956c8`.
- 22 logical commits; last message exactly `Version 0.30.0`, with no body.
- SSH push and fresh remote verification confirmed the exact feature head;
  tracked source/index are clean. Known caches and prior evidence are preserved.

The branch prepares shared release tooling, including the Rust generator gem,
and runnable JavaScript/TypeScript callback and async plus Python sync/async
documentation examples. Saved generated-SDK profiles enable Go and Rust
async/blocking panels; missing profiles hide those panels. Filesystem panels
and their overview link are removed; the separate filesystem project remains.
Existing Ruby/PHP/CLI/curl/HTTP examples remain supported.

Mounted descriptor routes resolve from the API origin while raw/discovery joins
retain their existing semantics. Required Python login values come from explicit
environment input. Actual server schemas, runtime validation and continuation
ownership remain intact. The final Go fixes correct fixture build and wire
expectations without changing the generator or SDK runtime.

## Accepted evidence

| Check | Actual execution identity and result |
| --- | --- |
| Final artifacts and Go | `b64fb25b`: manifest verification, extracted Rust generator/runtime packaged smoke and all 16 rendered Go programs compiled/executed; exit 0, 24.24 seconds |
| Installed dynamic examples | `3fb91caf`: npm plus Python wheel/sdist, six variants, 36 programs and 42 logs per distribution, including both no-token challenges; passed |
| Rust documentation | `48543f8c`: root/mounted routes, async/blocking, development 1.99/MSRV 1.95, 26 programs per mount; exit 0, 915.38 seconds |
| Final CI | All ten exact `b64fb25b` runs completed/success, confirmed `2026-10-22T19:57:51Z` |

Earlier dynamic and Rust results retain their actual tested heads. Independent
review reconstructed the unchanged tracked inputs and locks, including all 310
original Rust inputs and both flake inputs. These results are accepted through
that evidence and are not described as literal final-head reruns.

[Final review](go-query-final-review.md) reports no Blocking, Important or
Advisory findings. Same retained reviewer0, thread
`01a16406-faaa-7cd0-bde3-c20802c18a72`, saved/actual
`gpt-6.1-sol` / `xhigh` / `read_only`, no overrides, fallback or nested agents.
General, architecture/repetition and scope/proportionality lanes passed;
earlier risk/compatibility conclusions are retained through unchanged inputs.
The complete branch series, final diff and repeated streams were assessed:
no obsolete history, redundant updates or migrations. The final execution and
CI results close the verification gaps recorded by that review.

Evidence:

- [Final readiness receipt](final-release-readiness.json).
- [Source/history receipt](go-query-final-receipt.md),
  [input equivalence](go-query-final-input-equivalence.json) and
  [Rust input equivalence](go-query-final-rust-input-equivalence.json).
- [Final local result](go-query-verification-result.json),
  [complete log](go-query-verification.log),
  [wheel result](go-final-acceptance-results/dynamic-wheel/result.json),
  [sdist result](go-final-acceptance-results/dynamic-sdist/result.json) and
  [Rust result](rust-documentation-verification-result.json).
- [Final CI snapshot](go-query-ci-status.json),
  [release build](https://github.com/vpsfreecz/haveapi/actions/runs/39843638181),
  [Rust CI](https://github.com/vpsfreecz/haveapi/actions/runs/39843638091) and
  [feature push](go-query-push-ci.md).

All 12 final files remain in the HaveAPI worktree's `dist/`, including
`release-manifest.json`. Every byte count and SHA-256 matched the
[final inventory](final-artifacts-b64fb25b-sha256.json) at handoff. Prior artifact
sets, successful executions and failures remain preserved with their original
source identities. No runner, fixture, Git or hook operation remains pending.

## Remaining user decisions and setup

Integration into HaveAPI `master` requires explicit direction and fresh target
preparation. Official `haveapi-0.30` branch/tag creation and publication also
require explicit authorization. Nothing has been merged, tagged, published or
deployed during this handoff.

Before publication, confirm account-side trusted publishers using GitHub tuple
`vpsfreecz / haveapi / release.yml / release`:

- RubyGems: existing `haveapi`, `haveapi-client`, `haveapi-go-client`; pending
  publisher for the new `haveapi-rust-client` gem.
- PyPI: pending publisher for the new `haveapi-client` project.
- npm: `haveapi-client`, direct `npm publish` allowed; a new publisher entry
  needs its first successful publication within two days.

These account entries remain unverified. The protected release environment and
reviewer were confirmed; enablement variable, PHP deploy-key/secret and Packagist
webhook reads had access gaps. See [release checklist](release-checklist.md),
[registry audit](registry-readiness.md) and [GitHub audit](github-release-readiness.md).
HaveAPI's Rust generator is a Ruby gem with an embedded private runtime; it
requires no HaveAPI crates.io package or token.

The separate `vpsfreecz/vpsadmin-rust-client` crate `vpsadmin-client` has its own
first-publication token bootstrap and later trusted publisher tuple
`vpsfreecz / vpsadmin-rust-client / release.yml / release`. Its credential was
not read or used; its publication remains outside this preparation. See
[separate crate readiness](vpsadmin-rust-client-readiness.md).

No application documentation changed after final review. This handoff and the
updated state/checklist reconcile evidence only. The previous state is preserved
in [state-before-final-release-handoff.md](state-before-final-release-handoff.md).

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
