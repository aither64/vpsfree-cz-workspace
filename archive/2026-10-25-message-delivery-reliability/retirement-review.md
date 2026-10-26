# Findings

**No Blocking, Important or Advisory findings** in the lifecycle CLI ownership
fix. The correction selects the existing shared store; it adds no new storage
contract, compatibility mechanism or lifecycle operation.

Final packaged creation/deletion and lifecycle acceptance remain required.
The cancelled CI run contains a real failure and is not a successful check.

# Reviewed behavior

Retained independent reviewer `01a172a0-e739-7563-85b4-f3c8fc7f0ef2`, assigned
`gpt-6.1-sol/xhigh`, read-only. All four affected lanes were assessed directly:
general, architecture/repetition, scope/proportionality, risk/compatibility.
Risk remains high because lifecycle helpers consume persistent delivery state.
No nested agents, source edits, long tests, builds, CI retries or live-state
mutations were used. This report is the only write.

I read the complete [retirement packet](retirement-review-packet.md), its
resolution/evidence context and the committed delta. I reused the mandatory
review skill, all four lane references, repository AGENTS and applicable
workspace procedures already read in this context. The current delta changes
none of that guidance. [Original review](review.md),
[reboot review](reboot-review.md) and [baseline review](baseline-review.md)
retain their reports, identities, exact ranges and unchanged assessments.

The production correction is at
[libexec/dev-session:6932](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-message-delivery-reliability/dev-workspace/libexec/dev-session:6932)
and
[libexec/dev-session:9216](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-message-delivery-reliability/dev-workspace/libexec/dev-session:9216),
in storage-integration commit `d6f3f214d3adc0ad4c0e9eb14ad092ce55213c76`.
Both `thread retire` and `thread require-idle` now receive the runner's canonical
workspace and expanded, selected `@workspace_state_root`. These are trusted
runner-owned values, independent of an omitted Go flag or a different ambient
environment.

`threadCommand` passes its state-root flag explicitly to `newCodexClient`; an
empty value therefore overrides the constructor's ambient fallback. With the
correct root, that constructor selects the same socket-path-hash SQLite and
predecessor paths used by the portal. Workspace forwarding also preserves retry
ownership checks. The generic standalone fallback is unchanged.

Retirement consumes durable operation/receipt state, including
`ClearConversationAttempts`; idle checks consume submission and automatic-retry
state. Correct owner propagation therefore fixes the diagnosed fence-decoding
failure without loosening thread/cwd proofs, force policy, retirement ordering,
or scoped receipt cleanup. No new locks or changed lock order are introduced.

I inspected the caller audit against the Ruby commands and Go entry points.
Create/fork, observation, teams, provider/coordinator paths, explicit archive and
frozen-settings checks already select their state root. The remaining simple
set-name, materialization, initial-message and archive-state proof calls do not
consume the ordinary receipt store. I found no further analogous omission in
that inspected scope. Forwarding the existing owner flags at these two callers
is proportionate; no shared abstraction or fallback redesign is needed.

The baseline plan-wait finding was addressed by the prescribed scope reduction:
the shared source verifier defaults to nonblocking and only the fork caller opts
into waiting before destination/provider admission. The delta and documentation
reflect that boundary. This is context, not a redundant confirmation review or
test rerun of that narrow reduction.

# Exact history, pins and migration conclusions

All four worktrees were clean and matched the supplied final heads. I inspected
the complete recorded commit lists, current final changes and the runtime
range comparison with `101a1850`, reusing the unchanged baseline comparisons.

| Repository | Base | Reviewed final head | Complete ordered series |
| --- | --- | --- | --- |
| codex-web | `872c7ad3962f9fa9b17358244e27f3e3fac59fc5` | `8b60554bc10c2a6bcbf9732a8b77ad959c317036` | `66ab8c0`, `a9086b0`, `8b60554` |
| dev-workspace | `10bb047513c82d1310e8fcaa797e8772f948dd8a` | `9634151b9836311c331a58880fbb4c46133fd98f` | `c33f5191`, `f29686a5`, `ec53874b`, `902f7554`, `d6f3f214`, `64164336`, `9634151b` |
| vpsfree-cz-configuration | `d12a77374b18e15fe7600f95307114e2e1882828` | `45683e38d3dc8e3ced20eae553f879e46ec84348` | `f5d55557`, `45683e38` |
| workspace | `cb89659dfe30af6ce3d8f789c8f5eed60e8451be` | `72e15700b241d75bcbc1eb8abf04542f70d9792f` | `9368c8fe9`, `9ab0a185c`, `72e15700b` |

**Whole-history conclusion:** no obsolete unmerged approach, fixup commit or
transitional migration remains. Ownership fixes and their focused regression
assertions are folded into their owning storage-integration commit. The
browser commit is patch-equivalent to the baseline-reviewed version; fork
waiting remains its separate logical commit with narrowed plan scope. The
previously verified deployed runtime baseline and exact workspace cherry-picks
are unchanged, including archive recovery policy 3.

**Repeated-update conclusion:** no redundant pin stream remains. Library
dependencies are owned by `66ab8c0`, runtime library selection by unchanged
`902f7554`, configuration runtime selection by `45683e38`, and nested workspace
runtime selection by `72e15700b`. Superseded own pins are absent from the final
series. Relative to the baseline-reviewed heads, runtime locks and Go library
selection are unchanged; configuration changes only its devWorkspace node and
the workspace only its nested dev-workspace node. Both select `9634151b` with
the same locked hash. Library stays `8b60554`; native Codex 0.163.0, extension
`767dfd5` and sibling selections are preserved.

**Migration conclusion:** lineage remains sound under the recorded provenance.
The sole delivery migration remains library `a9086b0`: schema-3 JSON to SQLite
`user_version=1`, then schema-4 predecessor fences and the import/ready journal,
with the reviewed orphan-backup guard. The library is unchanged. The packet
reports no merge, release, live deployment or external consumption of any
delivery migration revision; disposable checks alone have used it.
There are **no new database migrations** in runtime, configuration or workspace,
and none in this ownership fix. Inherited deployed archive format/policy 3 and
its predecessor recovery readers remain intact. Its provenance and exact
preservation were established in the baseline review and are not reclassified
as an unused transition.

# Verification and remaining risks

Independent checks in this turn were inspection, caller/range comparisons,
semantic lock comparison and full-range `git diff --check` for all four
repositories; whitespace checks passed. No tests were run by this reviewer.

I inspected the relevant excerpt of the full cancelled-run log for CI
`40189655484`. It contains the ordinary-deletion failure
`clear retired conversation attempts: decode queue attempt ledger: json: unknown field "storage"`
before cancellation. The old empty flag, socket-adjacent fence and retirement
cleanup path support the packet's diagnosis. An empty `--log-failed` result for
an overall cancelled run does not erase this evidence or justify a blind retry.

The packet reports the strengthened Ruby/Go deletion bridge passing after
failing before the fix, preserving tombstone/team ordering. Root retirement in
that bridge remains synthetic: it proves exact owner arguments and ordering,
not successful native retirement against the migrated SQLite store. The idle
fixture similarly proves owner propagation and late-active-turn refusal. Its
aggregate-fixture invocation passed; the earlier direct-subfile fixture-loading
failure is not product validation. Focused fork/source checks, Ruby syntax and
composed-lock validation are supplied passing results, not checks rerun here.

Before activation, complete the final packaged/native and applicable
creation/deletion/archive/lifecycle checks against these exact inputs, including
ordinary retirement after migration and preserved refusal of active/unresolved
work. Earlier successful builds and native/VM checks remain bound to their
recorded inputs. The ownership fix changes neither the forward-only recovery
requirement nor the need to exclude predecessor application writers.

Owning documentation remains codex-web `docs/submission-storage.md` and runtime
`docs/dev-sessions.md`/`docs/workspace-portal.md`. No new feature section is
needed merely to forward existing owner flags. [Rollout](rollout.md) remains
prepared evidence. No claim, activation, live migration or original-attempt
repair was performed or verified here. Current acceptance and pre-transmission
evidence are still required before the separately prepared exact-row recovery;
absent history alone permits no replay.

No default-branch integration is authorized. The previous baseline report's
target-refresh/equivalence gate remains applicable before merge readiness.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-message-delivery-reliability/
