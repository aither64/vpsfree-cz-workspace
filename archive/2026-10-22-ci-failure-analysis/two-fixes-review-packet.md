# Final review: source-fetch backoff and aging observation

Session: 2026-10-22-ci-failure-analysis. Plan/state/design in this directory.
Repository: worktrees/2026-10-22-ci-failure-analysis/vpsadminos.
Base: cb4dcaaa397cad1f18c8f3c067b95bb8036072dd (already integrated staging).
Final head:96facc49755c17e18f1e57473d8534fac4669f8d.
Tree:b477bbda5e5a7967054f8ca725813f1d569b0f44. Clean index/worktree.
Complete series, oldest first:
1.4729f76656415233d29cd8f513f48f282f6aad54 tests/kernel: wait for complete aging progress
2.96facc49755c17e18f1e57473d8534fac4669f8d linux: back off transient kernel source fetch failures
Final diff three files,+72/-0. Native diff --check clean.

User requested fixing the two investigated failures. Accept finite, longer
transient source download retries with unchanged pinned archive identity, and
correct aging observation with the existing bounded all-counter wait. Preserve
strict assertions and the previously merged helper fixture. No new framework,
producer/kernel fix, input repin, VM/assertion/compiler retry or weaker counter.

Risk Medium: bounded compatible changes to fetch policy and test observation.
Review lanes: general, architecture/repetition, scope/proportionality. No security,
persisted-state, public API, host behavior or deployment boundary changes.
Reviewer0 is independent, ready, review-purpose, read_only, saved
GPT-6.1-sol/xhigh; no overrides or fallback. Read mandatory-change-review skill
and all three lane references, repository AGENTS and patch-series policy.

Complete intended split: aging call/comment + meaningful existing helper specs
in one owner; Linux fetch options + owning comment in a separate owner. Both
introduce final behavior directly, no superseded unmerged implementations or
fixup commits. Merged parent history stays intact. No migrations, schemas,
versions, rollback format changes, release/deployment or external-consumption
migration lineage. No repeated dependency/channel/input/kernel revision/gem or
generated artifact streams; URL/revision/hash/lock unchanged. Two independent
behaviors justify two commits.

Source fetch uses the existing fetchurl curlOptsList extension. Exact retained
failed drv/builder and installed same-version curl manual were read by architect;
design.md records those identities and option-order proof. Initial+3 transient
retries normally30s apart, connect30s, transfer600s, retry initiation1800s.
Retry-After and partial resumes can extend overall time: no whole-fetch deadline
or measured fit claim. Archive fixed-output integrity remains unchanged. No
native archive download/evaluation/build was run. All other kernel file bytes
compare unchanged (receipt below).

Aging keeps sleep60, then existing qualification_wait_for_progress(population),
then reread/strict assertion. At most60 extra observation seconds per iteration;
age target/overall bounds unchanged. Tests use actual AWK predicate and extracted
aging block: newer fork with unchanged wakeups pending, later all-counter advance
accepted, timeout propagates before reread. All task/CPU/health/network/NFS/TUN
assertions preserved. Actual failed VM eventual progress is unknown.

Quick evidence:
- repair/aging-progress-spec-2.log:38/0, seed3735,4.82s+0.68517load.
- repair/aging-progress-style-2.log: syntax2OK, RuboCop2files/no offenses.
- repair/aging-progress-commit.log: ordinary hooks pass, unsuppressed72-column
  preference warning, all message lines<=80.
- repair/ci-followup-prebuild-1/kernel-fetch-checks.txt: cached nixfmt and
  nix-instantiate --parse pass; exact static identity/scope check. No eval.
- repair/ci-followup-prebuild-1/kernel-fetch-commit-hooks.log: ordinary hooks
  pass, width preference warnings retained; all message lines<=80.

Owning documentation is adjacent comments and existing helper explanation;
no separate product page is useful for these small internal timing changes.
No shared runner/framework contract changed: existing helper is reused inside
one scenario; no cross-project consumer/API changes. Rollback restores previous
fetch and observation timing only; no coordinated node update.

Review full committed base-to-head diff and history, explicitly conclude on
obsolete history, migration lineage and repeated update streams. Report concrete
findings and residual native-fetch/VM gaps. No tests, Nix/eval/build, network,
fetch, mutation, cleanup or nested reviewers. No integration approval implied.
