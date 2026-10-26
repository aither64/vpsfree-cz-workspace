# CI-fix independent final review — original committed range

Reviewer0 reported FINAL independent review of HaveAPI base `cb43ae2367b12e22e602d69312bfd1f7331b4995` through original head `ea0932808c3bbcf70801d1728848e52507eb6193`. Later remediation edits were excluded using original committed objects. This report remains attributed to that range.

Identity: dev-session/current and both environment variables matched the bound session/workspace. Live roster revision37: reviewer0, review/read_only, retained thread `01a177c4-1e16-7f80-ae14-84e10687bcb9`, gpt-6.1-sol/xhigh. No override, fallback, nested reviewer or substantive authorship. Full packet/design/plan/state, mandatory review skill and all four references, relevant workspace/repository guidance read. High risk, all four lanes covered.

## Findings and lead disposition

No Blocking findings.

1. **Important — risk/compatibility and architecture.** `servers/ruby/benchmarks/performance_compare.rb:370-378` (`validate_blobs!`, especially373) runs git hash-object in ambient cwd/environment. `validate_tree!` correctly sanitizes GIT_* and global/system config in disposable explicit-SHA1 Git. Ambient SHA256 repositories or GIT_DIR cause unchanged retained SHA1 blobs to mismatch, and invalid inherited GIT_DIR rejects valid evidence. This violates portable isolated replay. Requested correction: same sanitized explicit-SHA1 context for blobs, with hostile-environment complete replay and retained tamper rejection. Lead accepted and assigned implementer1. Open on original head; focused lead inspection/checks may accept narrow requested remediation without automatic full rereview.
2. **Advisory — risk/compatibility.** Preparation clears RUBYGEMS_GEMDEPS, while new execution environment at performance_compare.rb:289-292, workflow:105-108 and doc/performance.md:50-54 omit it. Startup autoactivation can evaluate ambient Gemfile/activate Bundler before worker check. Exact graph should refuse extra activation: fail-closed launch robustness gap, not proof of silently accepted wrong hosted graph. Lead chose to fix narrowly in subprocess and public launch boundaries; assigned owner1 with focused assertion/shell checks.

## Whole-history and lane conclusions

Complete ordered commits: `65a9082ed68cd2546b9a12c69bd9b0ac0b9859b8` Ruff parity; `8b9afd3d4b7658ff7bbc47b0972d2c24d1b5c895` frozen environment; `ea0932808c3bbcf70801d1728848e52507eb6193` runner/provenance. All final diff/commit scopes/messages inspected. Three independently reviewable purposes; preparation tool and runner consumer reasonably separate. No obsolete designs, fixups or superseded unmerged approaches. No repeated dependency/channel/generated-input streams: Ruff changes once, frozen historical input introduced once, root contributor flake.lock unchanged. Original/effective graphs are separate provenance, not successive pins. No DB/schema migrations. Optional preparation inside schema2 is an intentional additive evidence migration; old absent-receipt replay preserved, partial/new malformed mode rejects. No obsolete transitional migrations; database merge/release/deployment/external-use provenance inapplicable. Fixes unmerged/unreleased/undeployed at reviewed range.

General: Ruff exact requirement is derived from TOML and compared with Nix metadata/executable; existing updater check precedes commit and runtime guard remains. Source/event selection, relevance, reference/budgets, outcome distinctions and15/45min limits retained. Coverage addresses legacy/new replay, tampering and deterministic gates.

Architecture: receipt.rb owns retained validation, prepare.rb live runtime/filesystem checks; runner/replay share validation. Contributor flakes remain source proof and effective runtime locks separately bound. Fixed immutable lock parsing is bounded, not a generic resolver. Finding1 is the isolation exception.

Scope: most historical environment lines are required exact locks/graphs/distribution provenance, with current consumers. No speculative framework, app change, recalibration, retry loop or budget relaxation. Dedicated fixture locks preserve ordinary library lock policy.

Risk/compatibility: live preparation rechecks actual copied inputs/runtime/specs/native/platform/checksums/Nix. Replay validates retained/current authority without vanished paths or activating historical stores. Loaded-source union binds Git OIDs and worker SHA256; no retained source execution. Legacy replay prior path remains. No service ordering/state rollback implications; reverting restores known CI refusals.

## Independent inspection and limits

Reviewer read-only byte inspections matched all17snapshot inputs/manifest hashes, all9reference-sourced files against b85ec364 blobs, all8artifact inputs against artifact12597024214, and all6historical evidence files. Canonical manifest ee21cae3..., effective-shell f64181e4..., Ruby-distribution66388f0b... and complete budget57b8d472... matched authority constants. Actual shell45llkcmppxpnmwyi8x3wgmvg38grzdxf/1521requisites/11Ruby requisites recorded distinctly from historical contributor shell. No claim recovered report is original raw calibration measurement.

No tests/builds/timings/live CI were run by reviewer; no files/refs changed. Owner quick-check evidence inspected, not independently executed. Full87 naturally activated graph/timing remains unverified: no-request smoke86 plus installed lazy io-console cannot prove campaign identity. ONE post-remediation hosted quick campaign and release build still required; no green/readiness claim yet. Important finding must be resolved before long verification. Review supplied no integration approval; user subsequently separately authorized merge when finished. Session stays open.

[Packet](review-ci-fixes.md) · [State/remediation results](state.md) · [Portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-client-readme-improvements/)

## Narrow review fixes accepted; publication released

Lead inspected final five-file delta and authoritative artifacts/review-remediation/affected.exit=0 plus affected.log:2examples0failures44.47s. Original watcher output recovered via stored exec handle96905; wrapper undefined exit_code serialization caused missing capture, not test failure; no second launch/retry. Existing sanitized explicit-SHA1 with_git now owns both blob/tree invocation. Complete replay works in ambient SHA256 cwd/GIT_DIR, nonexistent GIT_DIR and hostile hash/config; altered blobs still reject. RUBYGEMS_GEMDEPS cleared in subprocess and public workflow/doc/envREADME commands. Syntax/RuboCop/doc6fences/workflow checks passed; no prose changes, budget/reference/schema/legacy path unchanged.

Both original review findings resolved by narrow requested changes; mandatory review steps9-10 permit focused lead acceptance without automatic full rereview. Original independent report remains exact cb43ae23..ea093280. Implementer3 released to fold into owning environment/runner commits, retain exact range-diff and clean3commit inventory, then publish feature and launch one fresh pinned watcher for exacthead actual hosted quick/release CI (initial15min observation). No duplicate local campaign, automaticweekly/retry, merge claim or lifecycle action. CI-fix merge approval recorded separately; integration waits for hosted acceptance.

Final consolidation: corrected head08355a22df0fd957dc413708f67d7e4302ce09d3 from samebasecb43ae2367b12e22e602d69312bfd1f7331b4995, ordered65a9082ed68cd2546b9a12c69bd9b0ac0b9859b8/881e2ea4aa1bcd07002f9e2b4174c8d85971c72a/08355a22df0fd957dc413708f67d7e4302ce09d3. Lead inspected complete range-diff at artifacts/review-remediation/final-range-diff.txt: only accepted5file fixes, no changed calibration/source inputs; original independent report preserved and narrow requested remediations accepted under steps9-10. Clean history/index, hooks pass,46files8027+/71-. Hostedverification pending; userapprovedmerge after completion.
