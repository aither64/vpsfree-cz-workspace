# Independent final review — original committed heads

Reviewer0 report received through report_to_lead; persisted by lead because the
reviewer is read-only. Source review remains independent. No Blocking findings,
one Important finding and one Advisory finding.

## Important: transient silent-bootstrap failure permanently disables polling

General/risk lanes. Bot commit `2756ee653fb844a611a9f2083ca8890a1f70f72d`,
`lib/vpsfree-irc-bot/security_advisories.rb:37-48` and `:85-96`, with unchanged
`api.rb:13-22,37`. Initialization flag is set only after all initialization
requests succeed. Api#api_setup marks API setup successful before invoking
post_api_setup outside its retry rescue; its setup timer has one shot. A
transient bootstrap advisory-list/CVE failure leaves the new guard false and
every subsequent poll exits, with no flush deadline. This affects all modes,
including previously working default individual mode, and exceeds accepted
best-effort loss of individual announcements.

Reviewer reproduced with repository-selected Ruby 3.3.10 and installed bundle:
fail bootstrap list once, then restore it. API setup remained true, initialized
nil; three subsequent check/flush ticks skipped, total advisory queries stayed
at one. Request: local silent bootstrap retry and failure/recovery regression.

The proposed owner fix from the existing check under the same mutex, preserving
original startup cursor/store and returning silently on recovery, meets review
step 9 narrow-fix policy. Keep deadline/initialized assignment after successful
bootstrap; verify repeated/list/CVE failures, all modes and full first interval.
No shared Api redesign needed. Lead may directly inspect/test, amend the owning
commit, refresh/consolidate the configuration pin and recheck histories. No
automatic full review rerun required within this boundary. The original report
does not claim the pending fix has passed.

## Advisory: document quoted YAML off mode

General/documentation lane. README:36, sample:21-22, loader cli.rb:76. Psych
parses plain `mode: off` as false; strict string validation rejects it. Selected
Ruby reproduction confirmed quoted `'off'` produces the accepted string. Add
a short README/sample note showing quoted off. Preserve strict validation; no
parsing compatibility layer needed.

## Scope and reviewer identity

Retained reviewer0, saved gpt-6.1-sol/xhigh/read_only,
thread `01a1559f-acad-7f31-bb08-3650095a8a44`; no fallback/overrides. Exact
session current matched trusted thread binding; both identity env markers absent.
Read mandatory skill/all four lane references, applicable procedures, packet,
plan/state/design, actual histories/diffs, bot/spec/integration context and site
module/package consumer. Direct review only; no source edits, commits, long
tests/builds, deployment or lifecycle actions.

General/architecture/scope/risk inspection otherwise found the solution coherent
and proportional: plugin owns modes, ID sets and monotonic scheduling; site owns
policy/pin through existing arbitrary-settings module. Poll/flush share a mutex,
arrivals never move deadlines, delayed/failed/muted sends start a full new
interval and discard pending counts, empty boundaries silent, new wins across
polls, off consumes without queue. Existing individual reporting/API request
shapes retained. No new authorization, secret, schema or public API boundary.
Separate summary batch path justified by all-queries-success commit boundary.

## Independent whole-branch/history conclusions

Bot base/merge-base `e9c60b0b95d3cc0dad6f012d8127c2bc078cfa7d` to
`2756ee653fb844a611a9f2083ca8890a1f70f72d`: complete series is sole feature
commit. Five files, +669/-23; code with supporting unit/integration tests and
README/sample is one supported feature. No obsolete unmerged approaches or
follow-up/fixup history. **No migrations**, transitional steps or migration
merge/release/deployment/external-use provenance. No dependency/repeated pin
streams in bot branch.

Configuration base/merge-base `91639dec2c78721b3d8765de10dc65e0c66d59db` to
`aa933ecf78325326c1ccc097944f2ce53b8423f8`: complete ordered series is policy
`fcdb2e7c58ed1d9f665b800d691f060c08312b8d`, then package
`aa933ecf78325326c1ccc097944f2ce53b8423f8`. Exactly two files +4/-2.
Functional site policy and mechanical pin split are reviewable and follow
repository rules; no deployed interim state. No obsolete history. **No
migrations** or transitional/provenance obligations. One source-pin stream,
exactly one final update selecting bot 2756ee6 and
`sha256-hQl4jf4oLNgU5XlBV10W6v+/bNTPzV2hUouMo6ulMmQ=`. No redundant
pins to consolidate. Fix-driven repin must remain consolidated in that same
final package commit.

Original heads matched retained origin feature refs and were clean when
inspected. Reviewer performed no independent upstream fetch.

## Verification and compatibility limits

Reviewer independently reran all 34 advisory specs (0.20s), inspected full
146-example/RuboCop/format/hook evidence, checked both branch whitespace and
scoped config evaluation summary/3600/#vpsfree/generated JSON/ExecStart/source.
Harness-only regex context correction disclosed. Source hash prefetched by
owner, not rebuilt by reviewer. Long VM integration, full container build and
CI outcomes remain outside review evidence. Private overrides intentionally
uninspected and may override site settings.

YAML snapshot format unchanged, rollback readable; old bot ignores mode and
restores individual volume. Pending loss on restart/mute/send failure and
non-atomic API polling remain accepted, not requests for durable delivery.
Package/settings must take effect together if separately deployed.

## Disposition

Original-head final review complete. Resolve Important and record Advisory
disposition before long verification/readiness. No integration/deployment
approval implied. Lead accepts both findings: owned bootstrap fix plus quoted
YAML documentation correction, verified directly under narrow-fix policy.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-security-advisory-notifications/)

## Lead remediation inspection

Lead inspected `bot-review-remediation.diff` directly: only local bootstrap
context/retry/readiness handling, four focused failure/recovery cases and YAML
quoted-off documentation. Recovery uses the existing poll/mutex, original store
and startup watermark, no shared Api or public-contract change. Owner reports
38 focused/150 full examples pass, RuboCop two/63 files clean, Nixfmt/diff clean.
Selected Ruby/Psych verifies bare off becomes false, all quoted modes remain
strings and the sample parses summary/3600. Lead authored/inspected the exact
quoted-off note using required writing guidance. Both findings accepted as fixed
within reviewer-confirmed narrow boundary; original feature commit amendment and
single dependent pin refresh authorized. Final heads/verification recorded in state.

## Lead final history reconciliation after narrow fixes

Corrected bot sole feature head is 49a8ff8086b7b325f9f1a8f4825619f8e03245ce
above unchanged e9c60b0. Lead inspected exact reviewed-to-final diff: only
requested startup recovery/tests and YAML quoting. Consolidated into the owning
commit; no obsolete unmerged history or migration/dependency stream introduced.

Configuration repin amended its sole package commit, selecting that bot and
hash sha256-eDDFH9gQPDibgzeD0f/z3jpVZxKuCGMAKFgyAZowIsQ=. Origin advanced
with unrelated WebUI-only flake.lock pin a2ad6da408715de811cc6d8ea7b29ac55ea341ec.
Owner cleanly rebased without conflicts. Lead independently inspected full
range-diff 91639dec..76cf08d1 to a2ad6da4..e30cd339: both commits patch-equivalent
('='). Complete final series policy 0238ad1b90f95d6179b45130979be02a5f47718c,
pin/head e30cd3399c5f57fd792afa4147d293307227d9b4. Final base-to-head diff
still exactly two files, summary/3600 and one final source rev/hash. No repeated
pin, obsolete approach, migration or new contract added. Evidence:
config-rebase-range-diff.txt, refreshed config-series.txt/config-final.diff.
Original independent history conclusions remain applicable under narrow-fix and
patch-equivalent rebase policy; final quick/evaluation results recorded in state.

## Lead narrow fixture correction after runtime evidence

Local and exact-head CI failed at the new fixture's NAMES join before advisory
creation. Exact ngIRCd27 socket reproduction proves summarybot (10 characters)
is rejected432 at default limit9 while digbot is welcomed001. Lead inspected
committed 49a8ff8-to-a5d1dfe diff: only tests/suite/vpsadmin-events.nix changes,
consistent short nick, service readiness and bounded failure-journal diagnostics.
Framework confirms succeeds returns [status, output]. No app code, server limit,
timing, contract or design changes. Full150/0, RuboCop63, Nix parse/format and
extracted Ruby syntax pass. This direct correction remains within reviewed
fixture boundary; no new affected-lane design requiring a review rerun.

Corrected sole bot feature head a5d1dfe565526c3532183d756c592a26e7270675 above
e9c60b0; no obsolete history, migrations or dependencies. Full failure logs/CI
artifact and exact committed diff/reproduction retained. Targeted runtime retry
is required before acceptance/merge; config repin remains one logical package
commit. See long-verification-failure.md and bot-integration-diagnosis.md.

## Lead direct fixture assertion correction

Second runtime at a5d1dfe proves exact combined digest and >=60-second first-delay
checks passed; final overly broad count included four unrelated existing URL
marker replies. Lead inspected single fixture +6/-4 diff: digest category count
narrowed to existing “ in vpsAdmin: ” messages with exact payload check retained,
individual-advisory suppression asserted over all bot output, explicit RSpec
expectation exception plus bounded IRC/journal diagnostics. No app, timing,
plugin, server limit or public contract change. Full150/0, RuboCop63 and Nix/Ruby
static checks pass. Direct narrow repair within reviewed fixture behavior; no
new behavior requiring affected-lane rerun. Source histories to be consolidated
and final runtime success still required before merge. See bot-digest-assertion.diff
and preserved failure/reproduction evidence; no blind acceptance of a rerun.

## Lead direct existing-status readiness correction

Final263ddbc run passed all7 other examples including hourly digest, but unchanged
firstexample received explicit Cluster API-not-ready response. Setup only waits
independent OutageReports API; fixed sleep never guaranteed Cluster readiness.
Lead inspected firstexample-only fixture repair: total120s deadline, response
wait at most15s/remaining, reissue !status only after explicit known not-ready
reply, break only on original concrete nodes-online assertion. Silent/unmatched
errors still fail. No app/API/helper/framework/advisory behavior change. Full150,
RuboCop63, Nix parse/format, extracted Ruby syntax and whitespace pass. Scope is
existing test readiness rather than new behavior/abstraction; direct narrow
verification accepted. No unsupported per-example runner selector used; original
network setup exception detail remains unknown. Preserve bot-status-readiness.diff,
diagnosis and failed263ddbc evidence. Consolidate owning commit/pin, rerun final
runtime and build before conditional merges. No deployment.
