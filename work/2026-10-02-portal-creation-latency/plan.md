# Portal session creation latency investigation

Analyze the reported roughly 105-second creation delay in the dev-workspace
portal and explain the difference from an ordinary Codex CLI launch. Scope is
read-only diagnosis of the deployed generic dev-workspace runtime, its
codex-web dependency, creation receipts, and timing metadata. Do not change
application code, restart shared services, send model prompts, or mutate other
sessions.

Identify the actual request duration, reconstruct the critical path from
persisted timestamps and deployed source, and rank concrete optimizations.
Separate measured intervals from code-based hypotheses and record evidence
limits. Likely readers are the operator and a subsequent implementation team;
put the investigation in this session's analysis.md and summary in state.md.

Compatibility: this investigation changes no schemas, persisted conversation
formats, API contracts, package generations, or deployment configuration.
Any proposed optimization must preserve exact-once initial prompt handling,
creation recovery, trusted thread identity, retained team policy, and mixed
package/rollback behavior. No integration or deployment is authorized here.

Verification uses existing creation metadata, local source inspection, and
bounded read-only observations. Avoid creating extra model-backed sessions for
benchmarking. No builds or integration tests are needed for analysis alone.
