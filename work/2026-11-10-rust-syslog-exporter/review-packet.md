# Final review record — Rust syslog exporter

## Current accepted source

| Repository / target | Complete final range |
| --- | --- |
| syslog-exporter / master | `7c5a8e74e44a704cceb99cd05716af6800d78efd..faf06c1185ad2f6d39286d2e33896a6455b7bea6` |
| vpsfree-cz-configuration / master | `3c088a4b71881b3649441ce3c4e92c71757708e6..a839ccf7e7ff07ac616ad7994af33f07975bd1b5` |

Both published feature branches are `2026-11-10-rust-syslog-exporter`, each with
one coherent replacement commit and no migrations. Worktrees are beneath
`worktrees/2026-11-10-rust-syslog-exporter/`. Neither branch has been integrated
or deployed. Exact current build and verification outcomes belong in
[state](state.md), [C2 evidence](c2-evidence.md) and [V evidence](verification.md).

## Independent review and accepted changes

All reviews used retained independent reviewer0, `gpt-6.1-sol`, xhigh,
read_only, native thread `01a1c742-93c5-7c50-b59e-f792fafd9624`.
Overall risk is high because FIFO delivery, metrics, service failure and rollback
cross repository boundaries.

1. [Original exporter final review](exporter-final-review.md), full range
   `7c5a8e74..9a5b3d1`, covered general, architecture, scope and risk lanes.
   Important I1 identified unbounded driver pacing sleep; Advisory A1 identified
   missing assertions for the captured HTTP fixture. Both were fixed in
   `8ef8241c60f3b99976191b92f0467c945e36b1c8` and directly verified by the lead
   under the review skill's narrow-fix rule. The runtime source tree was unchanged;
   deadline/reaping and fallback/gzip regressions passed, with 14 quick tests and
   exact-head CI42910934231. The original report remains verbatim.
2. [Original consumer final review](c2-final-review.md), full range
   `3c088a4b..75b0af03`, covered all four lanes with no findings. It assessed the
   complete single-commit history, source pin/package/service, scoped Ruby removal,
   module test and operations guide. Subsequent package/host builds passed, but
   those artifacts are historical after the HTTP correction.
3. [I2 affected final review](i2-final-review.md), complete current provider range
   `7c5a8e74..faf06c1`, compared `8ef8241c..faf06c1`. General, architecture and risk
   lanes found no findings; prior scope conclusions remain applicable. It assessed
   the final single-commit history, no migrations, HTTP concurrency/cancellation
   tests, documentation and unchanged-scope evidence. Only `src/http.rs` and two
   existing HTTP documentation files changed. All other 31 tracked paths,
   dependencies, profiles, driver and fixtures are identical.
4. The final consumer refresh `75b0af03..a839ccf7` is mechanical: only the provider
   revision and source hash changed. Under the independent I2 report's explicit
   consumer boundary and the review skill's mechanical-refresh rule, the lead
   independently reconstructed the entire final Git tree from the original
   consumer tree plus those substitutions. Tree equality, reviewer/ranges,
   source reconstruction and no-migration inventory are bound in schema-1
   `c2-artifacts/lead-i2-pin-reconstruction.json`. Original review is retained;
   no substantive consumer behavior changed and no redundant whole review ran.

Full owner packets: [exporter](exporter-review.md),
[original consumer](c2-review-packet.md), [mechanical refresh](c2-i2-pin-review.md).
Superseded source identities are provenance, not literal ancestors of the amended
final commits. No obsolete approaches, fixup commits, repeated pin streams,
transitional migrations or externally consumed intermediate state remain.

## Why I2 was necessary

The old release produced 7 HTTP503 responses among 40 paired requests during
correct ingestion. Two configured independent Prometheus monitors scrape the
logger every 60 seconds, so isolated successful scrapes could not establish
compatibility. Architect D2 in [design.md](design.md) settled the bounded fix:
max two metrics handlers, one encoder, one asynchronous waiter for at most one
second, with permits retained by cancelled blocking work and released before body
writes. No cache, worker pool, new dependency or transport change was introduced.
Five deterministic tests use the actual production state and a gated collector.
Current quick checks pass all 19 tests, rustfmt and Clippy; exact-head
CI42921690945 attempt1 succeeded. Final release network evidence subsequently passed42paired/periodic requests
during1.04Mrecords; source review alone did not close the observed scrape gap.

## Scope, contracts and documentation

The user's requested result is complete Ruby replacement with equivalent rsyslog
metrics, measured flood performance, Rust tooling/CI, and integration preparation
for the single logger. Maintained dependencies and Cargo.lock are used; crates.io
publication, durable transport, fleet changes, speculative cardinality policy and
unrelated Ruby removal are outside scope. Exporter owns CLI/JSON/FIFO/parser/metric
semantics; configuration owns package selection, unit, account and monitoring.

| Topic / reader / class | Authoritative home | Fidelity evidence |
| --- | --- | --- |
| Input, metrics, expiry and failure / maintainers / reference | Exporter README → docs/reference.md; tests/fixtures/README.md | Actual pinned Ruby/rsyslog fixtures, source and independent reviews |
| Build, hooks, CI and measurement / developers / how-to | Exporter README → docs/verification.md | Shared check commands, committed finite driver and review |
| Package/service, cutover and recovery / operators / reusable operations | Configuration docs/operations/README.md → syslog-exporter.md | Package/module, retained old closure and independent consumer review |
| Exact heads, measurements, approval and recovery retention / this initiative / execution | Session state, rollout and linked evidence | Actual local builds, receipts and explicit authorization boundary |

The lead applied the required writing/fidelity pass before project commits.
Project documentation stands without private session access; rollout outcomes stay
in session records. All reviews explicitly accepted placement and preservation
of supported failure, upgrade and recovery guidance.

## Authorization and remaining limits

The user said “otherwise you can implement it” and “you are not to deploy log.int
without approval however. prepare it all, but stop before deploy”. There is no
deployment, dry-activation, default-branch integration or lifecycle authorization.
Reviews and local builds do not grant any of those permissions.

FIFO has no durable acknowledgement/replay; faster processing cannot recover
upstream loss or restart gaps. Retained labels have no total memory cap. Final
release scraping and bounded transport/lifecycle measurements were accepted for
their actual observed stages, without claiming production losslessness, isolated
causal<=10%scrape-capacity effect or production peak. See [V evidence](verification.md). [Rollout preparation](rollout.md) owns exact candidate
and rollback identities and the future approval boundary.
