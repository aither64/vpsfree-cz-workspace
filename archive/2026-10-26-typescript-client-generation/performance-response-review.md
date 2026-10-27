# Final performance-policy review — cross-revision response changes

No Blocking, Important or Advisory findings. No implementation changes requested. The planned retained-sample replay can proceed after review reconciliation; it remains acceptance work, not an outcome established by this report.

## Identity, scope and method

Reviewer0 independently performed the review directly with saved gpt-6.1-sol/xhigh/read_only settings, no overrides, fallback or nested agents. `dev-session current` returned `2026-10-26-typescript-client-generation`; both DEV_SESSION identity variables were absent, consistent with the trusted developer binding to `/home/aither/workspace/ai/vpsfree.cz`. The live same-session roster confirmed reviewer0 ready, purpose review, thread `01a177e7-c4ad-7893-b980-0807c3ec58b3`.

Read the complete performance-response packet, TOP accepted simplified design, current state and applicable workspace/repository procedures, mandatory-change-review and general/architecture/scope references. Reviewed the actual committed comparator, CLI/error attribution, CI report consumer, focused regression changes and documentation. No test, build, compiler, replay, benchmark/API request, network, source/record write or Git mutation was performed. Static Git/file inspection and in-memory hash/inventory comparison only.

Exact reviewed new range: `18b45aeddd0c28c8ddf6c5ea81f9611d6e3a7875..4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c`, tree `1cab0cbb36d28270c16d3e115813b689186f95b8`. Independently confirmed exact HEAD, clean index/worktree and one new commit with parent18b45aed. The prior five merged commits are supported historical baseline and are neither rewritten nor re-reviewed here.

## General lane

The implementation matches the user's selected policy: response content differing between revisions is diagnostic and does not itself fail, skip or discount performance comparison. The existing reference, wall/CPU limits, noise/adequacy/agreement rules, allocation limits and ceilings remain unchanged.

`compare_case` establishes output distributions by the actual SHA from the verified observation after checking that the sample belongs to the expected source. Both columns of each baseline/self pair therefore use the baseline SHA. Canonical identity and occurrence totals remain stable within each revision. Raw serialization variation, including JSON map order, remains tolerated as before. The former cross-revision equality gate is removed without weakening the retained raw/canonical body proofs, operation counts, status/counter checks or provenance validation.

Response diagnostics use only baseline/candidate pairs. Bytes per request are weighted by each output's occurrence count; self-pairs do not bias the size comparison. Raw and canonical changes are separate distribution diagnostics, and signed byte/percentage deltas do not enter timing or allocation classification. Validated positive body sizes and occurrence totals provide the denominator. Reports retain summaries rather than response bodies.

The CLI retains format2 and the original measurement harness identity. It records policy, the loaded comparator file digest and the exact consumed sample-byte digest. Loaded-input error reports preserve measurement source/profile/harness/budget identities when available; invalid or unavailable input does not acquire the current fixture/harness identity. New run output hashes the exact saved samples bytes before comparison.

The actual CI Campaign consumer validates runner exit/status/source identity before writing the step summary, then returns the ordinary exit code. Summary handling covers pass, regression, inconclusive and error; nonerror rows expose wall/CPU/allocation outcomes alongside response diagnostics. Existing workflow aggregation remains unchanged, including the distinction between inconclusive process success and a measured pass.

Focused new tests exercise changed valid JSON/HTML classified normally, the same changed responses with wall, CPU or allocation regressions still failing, canonical variation within a revision including the second self-pair column, weighted arithmetic without self-pair bias, map-order/raw variation, exact comparator/input attribution and original harness attribution on loaded-input errors. Existing malformed counts, raw/canonical/hash disagreement, counters and provenance refusals remain. I inspected these assertions and the reported quick-check scope without executing them.

Documentation accurately describes the new comparison policy, unchanged performance limits, retained normalization, replay limitations and additive report identities. It does not describe historical failures as passes or claim replay independently reproduces all live functional checks.

## Architecture and repetition lane

The comparator remains the single owner of response-distribution validation and performance classification. The small output-count helper is reused for canonical stability and raw/canonical diagnostics; byte reporting stays beside those comparisons. The CLI owns consumed-byte/report attribution, and the existing CI driver consumes the report without duplicating classification policy. No second validator, response registry or approval mechanism is introduced.

Representative consumers are the CLI run/compare entry points, Campaign/unchanged workflow and the existing focused specs. Their format2 interface remains compatible through additive fields, including retention of the legacy distinct_responses field with per-source counts added. The actual-source attribution avoids confusing a self-pair's candidate-named column with a candidate revision. Component boundaries and error behavior are clear and proportionate to this change.

## Scope and proportionality lane

The eight-path implementation is the bounded policy/reporting correction requested by the user. It does not restore the rejected semantic-validator/helper, format3, fixture inventory, normalization/allowlist, acknowledgement or per-byte-discount proposals. The changed tests target owned classification, attribution and consumer behavior rather than creating a new benchmark campaign or validation framework.

No additional hardening project or fixture expansion is required by this review. Existing functional and evidence constraints remain within their previously supported boundary; output differences are diagnostics while timing/allocation limits remain enforced.

## Independent input and history conclusions

The exact new series contains one coherent, independently revertible commit: `4d36efcf servers/ruby: compare performance across changed responses`. Comparator policy, report attribution/summary, tests and owning docs support the same behavior. No unrelated functional change is bundled.

Independently compared complete tracked inventories: only the specified eight paths differ; all848 other mode/blob/path entries are identical to18b45aed. This includes clients/VERSION, fixtures, performance budgets/reference inputs, benchmark Gemfile/lock/shell, workflow, Makefile and flakes. No downstream generator repin is needed or present.

Committed comparator SHA256 is `163e7bbec7725d784e72677456238ada5264adec8c2c8dda9caa83ccd7fd5267`; unchanged budget SHA256 is `57b8d4725e76c4552e6cb2eb54982cd8d406bd2415eb99e51cb43049bae3a050`. These match the packet's prepared replay identities.

No obsolete unmerged approach, redundant fixup, abandoned format/schema iteration or transitional mechanism remains in the new range. Prior five merged commits are preserved supported history, not obsolete feature iterations. No repeated dependency, channel, generated-metadata or input-pin update stream exists in this new range. There is no release/consumer/state boundary offered to justify redundant updates, and none are retained.

No migrations. This commit introduces no database schema/seed, persisted runtime format, application wire/API or deployment state change. There are no new/transitional migration versions or merged/released/deployed/externally consumed feature-migration predecessors. Migration lineage is sound and empty.

## Residual acceptance and authority

The retained115773806-byte sample replay has not run in this review. It must use the matching immutable budget and reviewed comparator in a new output directory, binding the original source pair and measurement harness plus the new comparison policy/input identity. Missing/invalid samples or an actual regression remain visible failures; no pass is inferred here. Replay reclassifies existing measurements and must not be called a new measurement or retroactively green the original failed40529570313 run/report. No new baseline, budget, reference, fixture or ancestor workaround is accepted.

Future source publication/exact-head CI and any default integration remain the lead's separate work. Earlier integration approval does not cover this material new policy. This report provides no source-push, default-merge, release, deployment, registry or session lifecycle authorization.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-typescript-client-generation/
