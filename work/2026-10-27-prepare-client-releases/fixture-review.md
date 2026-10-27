# Affected final review: HaveAPI maintenance fixtures

No Blocking, Important or Advisory findings. The affected source-review gate passes at `c9124da141adc258fbbaf67d4ec19ee3f8580849`. Required broader validation and release recovery remain pending.

## Scope and identity

Reviewed the committed fixture fix under mandatory-change-review, with general, architecture/repetition, scope/proportionality and risk/compatibility references read in full. Reused the original completed review for unchanged release metadata and SDK content; did not repeat that analysis.

Session current and both environment markers matched `2026-10-27-prepare-client-releases` and `/home/aither/workspace/ai/vpsfree.cz`. Live roster confirmed retained reviewer0, thread `01a17e59-3823-76f0-9764-5525072525a2`, review purpose, ready, `gpt-6.1-sol/xhigh/read_only`, unchanged settings and no fallback. Reviewed packet, applicable guidance, bounded design, preparation receipt, failure evidence, complete final history and affected source/context. No checks, builds, writes, Git mutations or nested agents were performed. Report returned for the lead to save.

## History and proportionality

Base: `4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c`, also the merge base against the retained origin/master ref.

Complete two-commit series:
1. `3bbb98e76e286d64707c368fe1c2cc4d03f35eed` — release: prepare HaveAPI 0.31.0.
2. `c9124da141adc258fbbaf67d4ec19ee3f8580849` — servers/ruby: isolate maintenance lineage test versions.

Final cumulative diff is 19 files, +141/-35. The new commit changes only `servers/ruby/spec/performance/release_lineage_spec.rb`, +47/-18. Every production, benchmark, budget, reference, workflow, version and changelog byte remains unchanged from the original review.

This is a proportionate correction to the demonstrated release-validation failure and the user's recurrence-prevention request. A focused test commit was delivered within roughly seven minutes of the tagged failure recorded in the saved log. It adds one local helper and one later-minor regression, with no new framework or expanded production contract.

The metadata and correction to a pre-existing test are independently reviewable purposes; their separate commits are appropriate. The original tagged source remains preserved rather than reconstructed. Explicit whole-history conclusion: **no obsolete unmerged approaches, superseded fixes or unused compatibility paths remain**. **No repeated dependency/channel/input/generated update streams** exist in the complete series. **No migrations** or transitional migration lineage exist; there are no migration versions requiring merge/release/deployment/external-use preservation. No 0.31.1 version stream was introduced.

## Correctness and architecture

The saved tagged failure shows both direct worker normalization and fixture construction sending live 0.31.0 into the intentional 0.30-only guard. This supports the diagnosed test-fixture defect.

- At spec lines 77–95, `contents` reads the template's VERSION directly before synchronizing the synthetic VERSION, local constants and internal constraints. Validation remains on the completed synthetic fixture. `with_maintenance_source` owns its temporary directory through block-scoped `Dir.mktmpdir`.
- At lines 205–218, the recurrence test first materializes a synchronized 0.32.0 template, then scopes only the example's root helper to it. Producing and capturing 0.30.2 from that template succeeds; synchronized 0.32.0 and 0.31.0 inputs still fail with the explicit 0.30 contract error. Reintroducing the old pre-substitution validation would fail this regression. Production methods and global file reads are not stubbed.
- At lines 230–273, ordinary non-release input validation still uses the actual checkout before component-version stubs. The real release worker consumes the owned 0.30.2 source and retained lock/benchmark harness. RSpec scopes the three component-version stubs to the example and restores them afterwards. The 0.30.99 input still exercises the actual loaded-version mismatch refusal.
- At lines 379–400, the actual Worker#measure and HTML normalizer receive matching owned source/body versions and retain raw-body and canonical-digest assertions.
- Real served-HTML adaptation, replay CLI execution and raw/normalized/graph/authentication/panel tampering checks remain intact.

The helper is local test glue with two real consumers. Repeated file-materialization loops are small explicit examples with distinct versions and no meaningful duplicated policy requiring another abstraction. The production Release.version/normalize/html and Worker.inputs behavior remain unchanged and consistent with `doc/performance.md`'s reviewed 0.30 maintenance boundary. No public interface, security boundary, persisted state or deployment compatibility changes are introduced.

The commit message and existing design/preparation records explain the defect and correction; no additional product documentation is needed for this internal fixture repair.

## Verification evidence and remaining limits

The preparation receipt records final pinned-Nix `make doc`, 18 lineage examples passing with seed 63695 in 8.55 seconds, targeted RuboCop clean and required hooks passing. The retained `haveapi-fixture-focus.log/status` are explicitly the earlier 17-example watcher run, not the final inline 18-example run. I inspected that distinction and did not launch verification.

The checkout has no tracked changes, is one commit ahead of origin/haveapi-0.31, and retains the pre-existing untracked `utils/release/__pycache__/` untouched.

At inspection, `refs/tags/v0.31.0` still names annotated object `73eb7726a245804b8aa3abdff9181772f827d2d9`, peeling to `3bbb98e76e286d64707c368fe1c2cc4d03f35eed`; the session recovery ref preserves that exact old tag object. This is local readback, not fresh remote proof.

Proceed with the required deterministic/full validation of the fixed head. Source review does not establish release success. The user's latest exact failed-tag recovery direction and old-object lease remain the lead's operational boundary; no other tag or default-branch integration is authorized by this review. PHP preparation still requires a successful actual tagged artifact, its own review and explicit PHP master/tag/ordering approval. Preserve failed-run/tag identities and reconcile uncertainty before mutation.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-prepare-client-releases/
