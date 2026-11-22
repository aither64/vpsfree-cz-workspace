# Independent final finite native-core review: changes required

Reviewer0's final report in the bound conversation concludes **changes required**:
two Important findings, no Blocking or additional Advisory finding established.
Lead accepts both for correction. This is a completed finite checkpoint review,
separate from [the schema1/2 review](review-final-schema12.md); it grants no
initiative readiness, integration, deployment or activation approval.

## Identity and exact source

Retained reviewer0, thread `01a1cc9f-6d1a-7de0-9e3c-d76f9d4553af`, verified
`gpt-6.1-sol` / `xhigh` / `read_only`, roster revision67, lowest independent
review-purpose index. Session current matched the trusted binding. No override,
nested reviewer, source/index/ref/record mutation, new test/model/deploy run or
lifecycle action occurred. All four mandatory lanes were applied directly at
high risk: general, architecture/repetition, scope/proportionality and
risk/compatibility.

D primary `dev-workspace`, complete one-commit range
`d4e15e9d6b36fb2c4f4ff93e4f68a290494e265b` to
`d3b0057f6b032d19a4b2cc86b81a3493e5220981`, tree
`7b781df53f78db1c9d8cd526a5706f1c9d8e9f35`:23 files,5460 additions/113 deletions,
seven new files. Final source was clean and index empty. C remains a2 and that
checkpoint's actual Go pin selects a2; no new dependency selection occurs here.
The review assignment is `7289c631-1194-44cb-b7cf-8eb1dca674d7`, real turn
`01a1d1c1-df8f-7503-b29c-6e667b83e3f3`.

## Findings and decisions

**N1 — Important, general and risk/compatibility.**
`portal/internal/piruntime/native_routing.go:929` treats a canceled native arm
context as unresolved without excluding a released arm. Positive
`ownedNativeSettled` sets released, stops expiry and cancels that context
(`native_retry.go:1096–1100`), retaining c.nativeRun. Postsettlement Manager
Inspect therefore reports held/unresolved_state and Manager Load refuses
(`native_routing.go:188–193`). Physical reset does not remove the arm. This
affects even an original with no omission and is independent of the known B1 gap.

Requested narrow correction: ignore released arms in that unresolved predicate,
retaining unreleased expired/held/pending fences. Existing transaction/inspection
fixtures can prove RED/GREEN Inspect, Load and physical-reset inspection without
another SDK run. The actual SDK fixture proves raw idle/receipt bytes, not this
Manager path. Implementer1 owns the priority native-fix package under steering
`8532fddb-10db-4b6f-8f76-0bcbe0f8c9d4`.

**N2 — Important, risk/compatibility and general.**
Manager Configure (`controller.go:75–78`, via handleCall) and ApplyToolPolicy
(`tool_policy.go:133–140`, via toolPolicyCall) do not inspect schema or invoke
their independent Config.NativeRoutingPackageGuard. Their schema3-capable
supervisor counterparts do guard. An accepting supervisor can therefore write
schema3 through these Manager paths despite a nil/failing Manager guard. Generic
runtime handshake/Inspect is not native package admission. This violates the
documented independent per-side default-unavailable contract; it is not merely
the unfinished production composition.

Requested correction: local schema3 preflight/current-runtime recheck on these
supported writers and inspection of the other existing schema3-writing Manager
paths under the same owning rule. Preserve retained1/2/utility2 and original lock/
pending/Unknown behavior. Focused asymmetric Manager/supervisor nil/error tests
must prove no pending publication, native mutation or schema3 save. No new guard
framework, leaf or SDK change is requested. Implementer1 consolidates N2 with
N1 in the same priority package, steering
`e09a969b-98c2-4a52-9f6d-ccdcf91fb153`.

R4-P3 is explicitly parked: its separate R-based worktree contains only three
untested Go hunks, index empty, no command effects. Those hunks are not an accepted
codec export. R4 guard work stays at its independent metadata decoder milestone
until the native fixes and owning codec handover are accepted. Frozen reviewed
d3 stays unchanged while fixes use a separate isolated worktree.

## Evidence and independent conclusions

The reviewer recomputed packet `b60e2f06…`, commit receipt `019288c5…` and quick
graph `c96a360e…`; all23 approved hashes and all121 graph inputs match committed
d3. Evidence supports compile.012s,27 selected Go cases1.785s,Node27/27.348s,
and the changed budget component Go7.267s/command12.408s. One original Accepted
receipt/user, A,A,B,B with no C, two charges/two completed reads, positive
settlement and raw idle are established with fake authorities. These checks do
not cover N1's Manager inspection or N2's asymmetric guards. Earlier c05 happy
evidence retains its separate source scope. [Owning evidence](p3i-native-core-evidence.md).

The optional same-Manager transaction, memory lifetime/expiry and charge bridge
uses existing Unix/worker/receipt boundaries. No new generic scheduler/server/
ledger, second Send or user receipt namespace was found. Concrete strict state/
wire projections serve present boundaries; no additional harmful abstraction or
repeated-rule finding was established. Historical witness storage, B1 relaxation
or history repair would broaden this reviewed finite scope. Passing fixtures and
design acceptance do not excuse N1/N2.

The one native commit is coherent; its tests/docs support the inseparable worker/
supervisor/state transition. No new repeated pin/generated stream or obsolete
native iteration remains in it. The reviewer reconfirmed old d4==parked acd tree
fa1be7 and original43/parked40/refreshed40 counts. Original refs and reviewed
consolidated successors preserve provenance. This native branch still descends
from the old43 organization; it is not the cleaned refreshed candidate. Later
coherent replay/consolidation and exact candidate checks remain necessary.

There is no database migration. There **is an explicit retained1/2→3 transformation**
on first authorized ConfigureNativeRouting: verified physical0 baseline and
complete pending target precede SDK changes; success atomically publishes state/
clears pending; positive initial refusal may retain schema3 physical0; uncertainty
holds prior state/pending without replay. Public-SDK branch charges and witnessed
null edits also change native persisted history. Retained1/2,utility2,original
receipt and H0 layouts stay unchanged; old readers reject3. No abandoned-native
converter, Codex migration or restart/successor recovery is established. Inherited
runtime1→2 and communication1→2 remain real transitions. Evidence concerns
disposable component state; no released/deployed/external native writer use is
established. Installed predecessor/rollback proof is outstanding.

README reaches the owning runtime reference. The reviewer verified that removing
only the new optional-native section reproduces the old document byte-for-byte:
no receipt, recovery prerequisite or supported path was retired. Exact chronology/
graphs stay in session evidence. The reference states first-original scope, B1
rejection after reset and absent historical/restart restoration. N2 makes its
independent-guard claim inaccurate until corrected.

Real route/effect/failure/final-decision authorities, complete production metadata/
inventory/older-target guards and wiring, B1 on edited history, later inputs/
historical/restart recovery and coherent-candidate/package/installed/containment/
Codex acceptance remain unfinished. Apply narrow-fix focused verification; only
new design, contract or scope changes require affected-lane reviewer reruns.

The session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/

## Related committed fix review

N1/N2 fix head `234dfd530d8412a559e6e0b09b9eaa671037d48a` on d3, tree
`52e10df22e75a9254e82aed4ba353d7b363aa6e1`, exact6 files/491 additions/10
deletions, is source/quicks accepted. Lead verified committed/current/receipt
hashes and clean index. Reviewer0 completed affected assignment
`9f4cc4b3-5e87-488b-9785-1b82287e82a0` with unchanged identity/settings, all
four affected lanes and **no new finding**. N1/N2 are resolved in this graph.
[Fix evidence](p3i-native-fix-evidence.md). All6 approved hashes and all121
final quick inputs match committed234; Go1.591 and strict/native/legacy/utility
.126 retain focused scopes, with no unchanged SDK rerun.

The new private ExpectedRecordSchema is a factual schema CAS: omitted legacy1/2,
strict integer3 only for3, initiating Manager guard/current proof, independent
supervisor guard and under-lock comparison before effects. Actual two-Manager
late-conversion Configure/Apply races preserve bytes/inode/mtime/no calls. The
reviewer also traced observational reads, conditional cancellation and unload's
existing supervisor admission/drain/exit checks; keeping those outside the new
Configure/Apply classifier grants no policy/work authority. N1's released-arm
correction preserves independent unresolved holds.

This range remains separate from the transcript branch and still pins C a2.
No new persisted migration is introduced; inherited retained1/2→3 and history
transformations remain. Native fix must fold into its owner later; no cleaned
whole-candidate, native activation or installed proof follows. R4 was resumed
separately after source acceptance/capacity confirmation; its source is not a
native dependency. Production/B1/later-input/restart/recovery gates are unchanged.
