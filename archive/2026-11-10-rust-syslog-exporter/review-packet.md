# Final review record — Rust syslog exporter

## Current accepted source

| Repository / target | Complete final range |
| --- | --- |
| syslog-exporter / master | `7c5a8e74e44a704cceb99cd05716af6800d78efd..891db6b82ccd37e985507c654050143e165041a7` |
| vpsfree-cz-configuration / master | `e91c8d21055b7110182fd4c531389947f180e359..dda57166bd8bb6d85a74decdd05a8810933bdecc` |

Both published feature branches are `2026-11-10-rust-syslog-exporter`, each with
one coherent replacement commit and no migrations. Worktrees are beneath
`worktrees/2026-11-10-rust-syslog-exporter/`. Both exact final heads are now integrated into their remote master targets. Configebe/provider6ec were deployed to
log.int via exactgsw onNov11 after explicit approval; D3 live validation passed.
User later approved both master integrations and the confirmed compatibility
corrections while requiring essential-service continuity. The corrected sources above are now deployed as79kk/gv3/profile145; prior3hk/gsw
remains retained as the immediate fallback. Exact current build and verification outcomes belong in
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

## R3 correction and final consumer binding

[R3 affected final review](r3-final-review.md) found no findings in complete
`7c5..891db6b8`, affected `6ec..891db6b8`, across all four lanes. It independently
assessed strict raw UTF8 headers, body-only borrowed/replacement decoding,
ASCII/strip/colon semantics, one fixed diagnostic, focused regressions, docs and
whole single-commit history/no migrations. The report's historical src-tree typo
is preserved and corrected by the reviewer's addendum. Local25tests/fmt/Clippy,
active hooks and exact891 CI43116296064 passed. Deployed6ec is preserved by a
protected ref; this successor is substantive, not tree-equivalent to deployed3hk.

C4 is mechanical consumer content atop a patch-equivalent rebase: native temporary
index reconstruction applies exact3c..ebe binary patch to freshe91, then substitutes
only provider891 and sourcehash. The entire expected tree equals finaldda57166
`f56d93d060cc9e0e44917a32452d8a9c3bccbab9`; recipeblob/parent/single-commit and fresh
SSH feature/default refs independently match. Schema1
`c2-artifacts/c4-lead-expected-tree.json` binds original C2 review, intervening
mechanical proofs, deployed range and R3 provider review. No additional full
consumer content review is required; unchanged module/docs/check/lock behavior
and no-migration conclusions retain their original independent basis.

Final package/normal-host builds are now authorized with actual25 release checks;
old3hk runtime/performance evidence does not certify the successor. V3 uses only
final Nix output for focused parity, small matched ordinary/OOM and65s two-consumer
checks. Exact results remain in owner evidence; actual corrected deployment and
remote integrated lineage are still prerequisites to release held machine6fda.
This review checkpoint preceded activation/integration. Both final heads were
subsequently actually deployed/verified and FF integrated, with exact remote
lineage and released claims in deployment/ receipts.

## Measured-message successor and deployed consumer

User explicitly requested the measured comparison in the exporter commit body.
M amended only that message: faf→6ec, complete tree5d3e unchanged. Independent
native reconstruction and schema1 logs/m-lead-reconstruction.json bind the I2
review/ranges/no migrations. Local amended-head19tests/fmt/Clippy and activehooks
pass. NewCI43096574664 is queued externally, not a claimed green run; identical
source prior CI and accepted actual3hk release remain applicable.

C3 amended only the pinned exporter revision froma839→ebe; sourcehash/Cargo inputs
are unchanged. Independent native reconstruction exactly matches the complete
38d58a87 tree. c2-artifacts/c3-lead-pin-reconstruction.json binds original C2
review, intermediate proof, M proof and no migrations. Typed derivation proof
records changed .drv IDs through fixed-source rev/revCustom/urls; all content,
builder, profile and output identities remain equal. No redundant whole review
or Rust recompile was required. New normal hostlr1→gsw build passed162.683s;
current head remains based on reviewed3c despite fresh unrelated mastere91.

User explicitly approved log.int deployment while keeping both branches unmerged.
Normal copy/dry/switch completed0, only exporter restarted, initial runtime/profile/
proc-exe/hash verified. [Rollout](rollout.md) owns exact deployed heads/paths,
claim, recovery and operation evidence. Integration was unapproved at that
checkpoint and has since been explicitly authorized by the user.
These operational records add no substantive implementation requiring another
review. No migration or new supported intermediate state was introduced.

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
without approval however. prepare it all, but stop before deploy”. Later approval explicitly permits deployment/dry activation of log.int while
withholding integration. No default-branch integration or lifecycle authorization exists.
Reviews and local builds do not grant any of those permissions.

FIFO has no durable acknowledgement/replay; faster processing cannot recover
upstream loss or restart gaps. Retained labels have no total memory cap. Final
release scraping and bounded transport/lifecycle measurements were accepted for
their actual observed stages, without claiming production losslessness, isolated
causal<=10%scrape-capacity effect or production peak. See [V evidence](verification.md). [Rollout preparation](rollout.md) owns exact candidate
and rollback identities and the future approval boundary.

## Follow-up F: development flake (ready, awaiting merge approval)

Complete new range891db6b8..99ffea73005685fc9f198dda3402fe24660ee944 is one normal
follow-up commit, tree3dd3e3330c1b2fcaf9585d77c6a2fb04314c9c1c. It changes only
README, flake.nix/flake.lock and removal of shell.nix. Merged/deployed891 history
remains intact; no runtime, dependency, consumer or production change occurs.
Direct small-edit brief kept nixpkgs718f and all six existing tools, without
extra flake helpers/package outputs or a CI redesign.

[RF final review](flake-final-review.md), same independent reviewer0
Sol/xhigh/read_only, assessed all four affected lanes and found no findings.
The new documented development-command/input contract makes compatibility
review applicable; production/state behavior is unchanged. Both Linux shells
evaluated; local x86_64 nix develop tools and mandatory active hook passed
fmt/Clippy/all25 tests, current-head CI43180133253 succeeded. Initial watcher
raw-retention limits are preserved; complete hook/final-eval/CI evidence is
authoritative. Aarch64 execution is not claimed. No migrations/obsolete history
or redundant pin stream. README placement/hook fidelity passed review.

This follow-up is published on the retained feature branch and separately awaits
integration direction. No repository/machine claim or deployment is needed for
preparation. F source/lock/code/command evidence lives in exporter-review.md and
logs/f-*; owned target cleanup completed after the accepted no-rerun boundary
(391,110,656allocated bytes removed, no universal protected-process visibility
claim). All known commands are joined; no implementation/check work remains.

## B: Dependabot automatic merge (local committed review)

User replaced the unpublished custom-updater proposal with Dependabot PRs that
merge automatically after sufficient verification, without routine manual review.
Superseded A has no source implementation/history to retain. Complete source
range891db6b82ccd37e985507c654050143e165041a7..5e3a5f38f7d396e957d20afcb6448704a21b4c9d
contains useful F99ff and one coherent B commit; affected99ff..5e3, treef86bdb46,
16paths866+/22- across the complete range. No migrations, repeated pin stream,
runtime/manifest/Cargo.lock/toolchain/flake.lock/consumer/deployment change.
B adds one owning Nix release definition and the tests/gates for this concrete
maintenance consumer; F remains a development-shell commit, not obsolete history.

RB assigned retained independent reviewer0 Sol/xhigh/read_only, HIGH risk from
future automatic default writes and credential boundaries, all four lanes.
All intended changes are locally committed and quick/active hook passes; source
publication and long Nix/audit/replay intentionally wait for review. See owning
[exporter packet](exporter-review.md), logs/b-source-provenance.json and complete/
affected patches, plus preserved inherited-Git hook/index failure/recovery proof.
No final-head CI success is claimed yet; remote feature remains99ff/master891.

Documentation routing: README remains entry point; docs/maintenance.md owns
enduring lock-only scope, verification, native merge trust, required ruleset
bootstrap and revert procedure; docs/verification.md distinguishes coarse CI
regression from controlled capacity evidence. Session records own exact source,
checks, settings receipts and one activation. Lead prose pass preserved commands,
values, hidden-bypass visibility limit and failure semantics. Cross-project
consumer config remains on891 and is not automatically deployed by this workflow.

Required server aggregate is Rust required from GitHub Actions15368, strict and
linear in same active named repository ruleset; initial admin bypass_actors=[]
receipt is separate from runtime Metadata-read inspection. Missing/redacted hidden
bypass list is not runtime proof of emptiness; visible nonempty refuses. No
admin-only legacy API, new PAT, bypass, PR approval or custom publisher machinery.
Initial bootstrap integration/settings remains approval-bound and unexecuted.

RB accepted; [original report](dependabot-final-review.md) has no Blocking or
Important findings. Advisory RB-A1's exact trigger/doc reduction is bound from
reviewed5e3 to finalf382/tree096 by lead independent native reconstruction,
logs/b-lead-narrow-fix.json, with final active hook/focused checks. WholeF+B
history/no migrations unchanged. Exactf382 hosted fullCI43200250554 then passed
all4selectedjobs, fresh audit/sandbox release and12matched+65s pairedHTTP gates.
Both initial locks/outputs identical: this validates the harness, not a real
update/live auto-merge. Individual release test logs were not streamed; successful
fresh doCheck release contract and direct quick25 evidence are distinguished.
I0 final effects/owned target cleanup accepted; see logs/b-final-validation-effects.json.
Initial bootstrap settings/default integration still awaits separate approval.

## C: simple weekly/manual custom updater (RC locally committed review)

Latest user rejects B complexity and requests the existing-repository pattern:
update dependencies, test, then commit/push as github-actions bot, weekly and
manually. C design.md:1114 +trusted-installer correction is sufficient (SHAa2f10be2).
Complete891..0b3131ffa6a2855cfa15c42de778d4bf794b4510/treef5d1659f retains usefulF99ff
and replaces B with one coherent C commit. UnmergedBrefs/reports remain historical,
not literally integrated. No migrations, repeated lock/input stream or production
adoption; Cargo.lock/toolchain/flake.lock/runtime/developerhook remain unchanged.

RC savedreviewer0 Sol/xhigh/read_only, HIGH/all4lanes; completebranch11paths392+/16-,
affectedC9paths339+/10-. One102line weekly/manual updater, one-job read-only RustCI,
18line owning checkedNix package, small sharedrelease option,132line actual-shell/
realGit fixture, shortdocs. No authorizer/publisher/artifact/Dependabot/ruleset/
performance campaign. OriginalBtests/review don't certify C privilege boundary.

Quickcommitted8+25/fmt/Clippy/hooks passed, exactstagingrecovery and inputproof in
owner exporter-review.md C1/logs/c-source-provenance.json and full logs/patches.
Publication intentionally held before long Nixchecks. Trusted pinned checkout/
installer may consume builtin token and configure hostNix, excluded from candidate
sandbox; all updatedcode/hookchecks inside ordinarysandbox true. Finalpush only
explicit shelltoken env. No bypass/newcredential. Direct normal push requires
frozen testedlock/base andfreshremote; nochange/failure/dryrun/stale/race cannot
silentlyapply untested source. No repo setting change required.

README remains entry; docs/maintenance.md owns concise schedule/manual/check/
trusted-setup/commit/stale/recovery, docs/verification.md restoresF +sandbox notes.
Exact executions/history remain session records. Lead directprose/CLI/message pass
accepted. Actualsandboxed release/feature CI follows RC; actual updater dryrun
orchestration follows separate initial approved integration, not certified yet.

RC complete: [original final report](custom-updater-final-review.md), one Important
RC-I1 (fallback can disable sandbox despite sandbox=true), no other findings.
Exact Nix2.35.6 source establishes conditional risk; no actual hosted leak is
claimed. Lead accepts required fallback=false config/assertion/hook/fixture fix,
I0 amends under narrow-fix rule; main maintenance prose updated. Original0b313
review stays fixed, successor binding awaits direct inspection/focused hook proof.
No long validation or publication before that closure.

RC-I1 closed on a455 by lead exact four-path inspection/focused9+25 hook proof,
logs/c-lead-narrow-fix.json; no new scope/review restart. First actual Nix CI
43214738861/a455 then failed entry126 before checks because /usr/bin/env is absent
in sandbox. Exact one-word package invocation correction accepted on final
b9b9cfea4331ff28bd883f1ed7415af6f27cd5f7/treea1d826ec, all other blobs/modes/message/F
parent and strict flags unchanged. Syntax/phase+active9+25 hook14.95s and newhelper
absolute-interpreter check support logs/c-lead-entry-fix.json. Failed run retained,
no green release claim; next changed-head feature Rust validation released.

C final b9b9cfea/source treea1d826ec accepted: RC0b313 +exact RC-I1 and Bash entry
fix bindings retained, source C on usefulF/merged891. Actual43216044595 hosted
checked release passed stricttrue/false,9real-shell fixtures+25Rust/fmt/Clippy;
full raw log and compact c-hosted-validation.json distinguish this from failed
43214738861/a455. All effects ended and owned debug target removed, no required
root/source/history changes. C integration prep/selected guide complete; initial
master approval and actual updater dry_run remain unexecuted. No live audit/
update/bot-authenticated push is claimed by feature Rust CI.
