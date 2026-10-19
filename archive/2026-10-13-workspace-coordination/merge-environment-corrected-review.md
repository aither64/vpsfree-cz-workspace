**Important — General / risk: the source checkout hook can still be skipped on retry.** In [retain_commit](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-13-workspace-coordination/dev-workspace/libexec/workspace-coordination-execution.rb:199), `fresh` depends only on directory existence, and the prepared checkout runs only when `fresh` is true.

If shell initialization fails after `read-tree` materializes the source, the directory remains clean. A retry successfully initializes dependencies but skips the source’s `post-checkout` hook. The same happens after that hook itself fails. Creating the separate target checkout does not validate the retained feature source.

Complete the prepared source checkout on retry as well; directory existence cannot prove hook completion. Add a focused regression covering failed initialization followed by a successful retry, with the source hook required to run.

Reviewed runtime head: `22e221618171e453cc04450e73efba6a477abc3e`.

- **General:** First-attempt ordering is corrected, and the new real-Git regression covers it. The Important finding remains open for retries.
- **Architecture/proportionality:** The bounded initialization block fits existing ownership; no broader recovery mechanism is needed.
- **Risk/compatibility:** No new schema or worker contract change. Existing generation, transport and environment-restoration conclusions remain valid.
- **History:** Correction is folded into the single logical commit after `a10af6c4`. Unchanged history and pin-stream conclusions stand. **No migrations.**

The worktree is clean; syntax and diff checks pass. Reported quick checks are **4 tests/20 assertions**, but omit the retry path above.

**Acceptance: partial; not yet accepted as fully resolving the Important finding.** Prior exact push-recovery acceptance remains unchanged; do not repeat the completed recovery. No agents, mutations or long checks were performed.