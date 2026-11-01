# Affected API dependency-baseline refresh review packet

Previous full independent expanded review is final-review.md, with prescribed
modern findings reconciled directly in review-reconciliation.md. This packet
requests ONLY the affected API risk/compatibility plus history/migration/pin
refresh after a genuinely new dependency baseline; no modern/client broad rerun.
All changed intended source/pin deliverables are committed, quick checks/hooks
pass, clean and remote-proven. No real API/KB suite has started on this range.

## Exact old/new ranges

Previously reviewed vpsadmin:
610a96f8ce523afbcd3e4374a70047dbe3264b0d..
218e3180896debd3006b9a0583e557286702761d, A866bccf1+B218e.
Old pin21c5213256c28f4a65fd582485e07234a02f5f55 overce2c8cd9 selects218e.

Fresh upstream adds exactly one commit:
097226b22edf8b59f80b5dfaa55265e9d0cac633,
api: adopt HaveAPI0.32.1 documentation switching.
Ten dependency/package/schema-export/docs paths, no feature owner/spec/locale
path overlap. Actual framework input changes, so not certified by source patch
equality alone. Compare relevant0.32.0→0.32.1 documentation/metadata/parameters,
authorization/preparation and consumer compatibility from actual sources/pins;
keep review bounded to concrete changed baseline, not a general framework audit.

New final vpsadmin range:
097226b22edf8b59f80b5dfaa55265e9d0cac633..
c8efabeb01ccca66b19425ee429e834d23cf3688.
Complete series:
- e200ab369bbc85ee7e5837091379a2899a261688 API correction/lifecycle commit.
- c8efabeb01ccca66b19425ee429e834d23cf3688 legacy UI commit.

Range-diff old complete series→new complete series shows ONLY one accepted new
spec fixture literal cve-2026-9998→CVE-2026-9998, preserving existing API uppercase
format validator. B binary patch exactly equal; no feature runtime/API/prose/
metadata behavior changed. Final tree135f6a75154f1e4387fc912db26a5c6ae1abed08
independently reconstructed from new base+reviewed patch+one fixture line.

New final KB range:
ce2c8cd9358c3636e5d39343e595df813a0b197f..
beeb258c72f84105b73b75fc4837e18b87e81cf2.
One coherent mechanical five-file pin update selects finalc8ef; no repeated pin
commit retained. All unrelated input nodes/root follows/explicit vpsadminos6bdf458f,
capture/page provenance/assets unchanged. All five pins agree.

Both own worktrees under worktrees/2026-11-01-published-advisory-corrections/.
Current targets unchanged at fresh097 andce2 remote proof. Old reviewed ranges,
refs, source/fixture patches, full range-diff, expected/final tree and B equality
are retained by fixture-rebase.md and its raw input receipts.

## Actual failure and quick evidence

Old218e API run41337574258 core platform-operations job124940972367 completed
236examples/2failures [1:4:6]/[1:4:7] only. The new lowercase CVE fixture was rejected
by the existing model-derived uppercase API input regex before normalization;
full log/native results/environment/file manifest downloaded. Fix changes only
that fixture to valid uppercase, no runtime validator change or blind rerun.
ci-snapshot-1902.md records exact evidence.

Actual new HaveAPI0.32.1 bundle prepared, metadata/i18n health,3filelint/syntax
pass78s on fresh baseline. Normal root A amend/B replay hooks pass; exact expected
final tree and patch equality verified. KB generation, pinned parse/full graph/
provenance/diff checks pass. No API/D long suite or strict full KB check yet.

New CI API41340446069,CI41340446005,i18n41340446172,RuboCop41340446028,
PHP41340446196; KBCheck41340595714/Managed41340595741, queued/running snapshot,
not accepted as pass. Superseded218e API/integration and21c5 runtime runs terminal
canceled only after exact new pushes; no current-head run canceled.

## Requested independent conclusion

Retain reviewer0 Sol/xhigh, read_only, no override/fallback, no nested reviewers.
Read mandatory skill and affected general/history and risk/compatibility lane
references. Inspect actual old/new source/input/range evidence and owning changed
baseline; explicit conclusions on compatible API/client/metadata behavior,
consolidated two-commit feature + single pin history, NO MIGRATIONS and no extra
public contract/design expansion. Add architecture lane only if changed dependency
reveals a concrete owning interface concern; no speculative broad hardening.
Return refresh-review.md report text for lead to persist. No source edits/tests/
fetch/deploy/default integration/production/lifecycle operations. Actual runtime
acceptance follows this review and cannot be replaced by quick/patch evidence.
