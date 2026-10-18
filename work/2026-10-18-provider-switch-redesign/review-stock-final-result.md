**No Blocking or Important findings remain at the reviewed heads. One Advisory finding remains.**

1. **Advisory — the new-child inheritance assertion is not bound to the new child’s identity.**  
   Commit `9dd91f2`, [provider_scoped_integration_test.go:80](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-18-provider-switch-redesign/dev-workspace/portal/cmd/workspace-portal/provider_scoped_integration_test.go:80).

   `newChildStarted` becomes true for any target-provider request containing an `agent_message`. Parent requests can also contain inter-agent messages, so the assertion at line 423 can succeed without proving that the newly spawned child used the target. Discover that child’s thread ID and check its target request in `threadRequests`, as the fixture already does for retained threads. This is a verification gap, not an identified production routing defect.

The two early stock findings are resolved. [codex_provider_scoped.go:245](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-18-provider-switch-redesign/dev-workspace/portal/cmd/workspace-portal/codex_provider_scoped.go:245) preserves the saved active flag when retry encounters the same interrupted source. Goal ownership follows source-turn changes, and a newer turn discovered after closure cannot inherit the old ownership. The nine focused regression cases cover the reported failure combinations and assert the required continuation count.

The earlier native-patch findings were eliminated by removing that implementation. This review does not establish that the abandoned patch worked.

**Whole-series conclusion:** reviewed all four lanes against these complete ranges:

| Repository | Base → head |
|---|---|
| dev-workspace | `705301228f72` → `33072104068a` |
| codex-web | `56ec377d81e8` → `c064ce09cfce` |

The four dev-workspace commits have coherent purposes: dependency pin, stock transition/backend, browser/docs, and the separate archive-VM timing correction. Recovery fixes belong in the backend commit. Range-diff confirms the browser and VM patches remained equivalent; codex-web’s implementation patch is unchanged, with its README addition composed with the inherited policy documentation.

No obsolete native patch, custom method, build override, child-migration engine or intermediate scoped compatibility path remains in the final series. Native assembly, package tests, release selection and `docs/codex-package.md` match the base. There are **no native-storage or database migrations**. Schema 2 is introduced directly; genuine deployed schema-1 recovery remains supported.

There is **one consolidated dependency stream**, consistently selecting `c064ce09cfce` through the flake URL/lock, Go pseudo-version/checksums and vendor hash. No redundant pin updates remain.

**Compatibility and architecture:** the stock close/reopen strategy fits the revised boundary. Retained idle members remain included; temporary children are left to native teardown and are not migrated or restored. Recovery reopens retained histories before continuation, including previously verified threads after a daemon restart. Native goal state is read after resume rather than reactivated from an old snapshot.

The inherited policy composition is preserved: provider transitions retain captured native permissions, while ordinary execution paths apply the package-wide policy. The fixture’s unmanaged package metadata is valid setup, not a production fallback.

Previously reviewed creation-incarnation binding, strict journal readers, preparation input/handoff admission, schema capability rejection, destination catalogs and subscription restoration remain intact. The shared interfaces remain additive and appropriately owned. I found no additional security-boundary issue within the trusted-host-operator model.

Documentation is appropriately placed and describes stock interruption and possible child-task reassignment. The unchanged package guide no longer carries an abandoned native capability.

**Verification limits:** the prepared native fixture meaningfully covers a saved retained member, old-child interruption and readable history, retained-thread target requests, roster/policy preservation, goals, queue identity, idle state and unrelated busy work. Its new-child claim needs the Advisory strengthening above. It does not verify member environment contents or child-history contents beyond successful reading and identity.

Exact native execution and package/CI checks remain pending. Further evidence should cover native-process restart, uncertain reopen/continuation replies and both provider directions. The supplied quick checks and earlier prototype results do not substitute for that execution.

The review gate can proceed to isolated verification, with the Advisory disposition recorded. This is not deployment or integration approval. I performed read-only inspection and whitespace checks only; both worktrees remain clean at the specified heads.