# Livepatch fixture failure investigation

## Current delivery and authorization

Delivered to canonical vpsfreecz/vpsadminos **staging6033c54a233370c4833823e5354a1d1fb8dc59ef**.
The current-module witness/OSVM/shutdown/NFS implementation was independently
reviewed and fully qualified at074ca388: CI42204546740 SUCCESS/all11, native323
scripts/109groups, ALL9 lifecycle audits with original14400 ages and all original
semantic/health/data/state/recovery contracts. It was normally fast-forwarded
into staging after the user's conditional approval.

A separate automatic staging RSpec run exposed a caused omission in an existing
minimal fake package fixture: new NFS Ruby interpolation needed pkgs.ruby.
The one-line6033 successor supplies an unused path without changing any runtime
consumer, provider/writer, assertion, workflow or input. Existing15spec/normal
hooks and independent general+architecture LOW review passed; hosted FULL13RSpec
3400examples/0failures and RuboCop passed at6033 before its normal approved
staging FF/push. Original074 runtime proof remains074-scoped; no6033VM/closure
certificate is asserted. The reviewer found no changed VM behavior needing a
new VM audit solely for this unit-fixture delta. Normal automatic fullCI runs
remain accounted in state, unmodified and without a claimed result.

User instruction “all right, so when the CI passes, you can merge it” authorizes
vpsadminos→staging; later “so continue” retained this work. Both approved merges
have fresh canonical remote proofs, normal hooks and immediately verified claim
releases before records/CI. No deployed node/system or session lifecycle action
is authorized. Session OPEN/active; all refs/checkouts/diagnostic provenance and
original faults/limits retained. See [state.md](state.md) for precise scope,
heads, jobs, reviews, claims, automatic workflows and future-action boundaries.

Original user constraints remain: current normal producer, no historical digest
allowlist/input freeze, validated finite semantic sites or explicit semantic
redesign, meaningful regression assertions and unchanged integrity/recovery.
The separately approved shutdown correction remains a distinct merged owner.
The old six-image Leap16.1 exception was never broadened; exact074 native ran
all six successfully, with no waiver applied. The two F-native faults remain
historical unwaived failures; no retrospective causal solution is invented.

The separate user-requested lead-wakeup initiative owns its own work; no
cross-session communication/access grant is inferred here. Optional LXC scope
remains unanswered and governs extra diagnostics only. No optional expansion,
new test matrix, deployment, cleanup or session closure is queued.

The following sections retain earlier accepted decisions and historical
milestones; the current delivery/authority above and state.md govern.

## Current implementation milestone

The user authorized implementation with the latest instruction `implement it`,
following the delivered plan for current-build-safe tests:
remove the historical candidate digest allowlist, replace candidate-dependent
numeric instruction offsets with validated current-build locations or explicit
semantic redesign, and preserve meaningful regression checks. The proposed
historical-offset test lane is withdrawn, along with the earlier input freeze.
This authorizes the scoped test implementation, checks and feature-branch
commits/publication. Integration, deployment, lifecycle actions and production
input/pin changes remain outside scope. No promise that tests never fail: genuine regressions,
incompatible ABI/semantics and unsafe/ambiguous sites must still fail clearly.

Architect0 delivered the revised [design.md](design.md) and
[implementation-plan.md](implementation-plan.md). Implementer1 delivered
[probe-elf-feasibility.md](probe-elf-feasibility.md), using cached published ELF
artifacts; implementer3 delivered [probe-redesign.md](probe-redesign.md), mapping
finite semantic/argument/frame contracts,
negative controls and implementation boundaries. Lead owns this plan/state and
acceptance. Other implementers are available for execution only after future
authorization and stable package boundaries. Retained settings are unchanged.

The plan must distinguish current candidate identity/transfer checks, immutable
released predecessors, fixed boot identity and candidate-probe site semantics.
No global Nixpkgs or production producer change is proposed. Use one selected
artifact/digest throughout the CI matrix. Read-only cached module restoration
is bounded and uses a fresh utility; no kernel/module compilation is implied.

The lead accepted the finite plan against both diagnostics. Future package
owners are implementer0 (identity/CI/consumers), implementer1 (resolver/package),
implementer3 (runtime witnesses/docs) and implementer2 (independent resolver
controls). Their exact boundaries and dependencies are in the execution plan;
these execution packages are now assigned under the user's instruction.
Current-source witnesses remain in the
default coverage. Parser/selector tests and quick checks precede committed
independent final review; focused runtime acceptance then precedes the full
existing matrix. Remaining proof points are explicitly implementation-stage,
especially FUSE safe-entry caller filtering and TCP live-value reachability.

## Investigation scope and evidence packages

Identify why the vpsAdminOS livepatch lifecycle CI jobs fail during fixture
preparation, independently verify the supplied leads, and give the user a
concrete correction proposal. This authorizes investigation and recommendations
only: no application implementation, integrity pin changes, integration,
deployment, cross-session access/communication, or session lifecycle actions.

Affected repository: canonical vpsfreecz/vpsadminos; inspect fresh staging in
this session's independent worktree. Lead serializes Git mutations. Preserve
all other sessions' work and use no other session's evidence files.

The retained Full team owns these packages:

| Owner | Deliverable | Acceptance / dependencies |
| --- | --- | --- |
| architect0 | design.md with diagnosis and smallest proposed correction | Source/input provenance, integrity invariants, compatibility, affected files and verification plan; synthesizes both diagnostic packages |
| implementer0 | workflow-lineage.md | Canonical GitHub failed/green revisions and logs, exact regression boundary or bounded interval, Fedora relevance; depends on own worktree |
| implementer1 | candidate-identity.md | Actual module identity/digest against pin, exact derivation/input graph, cache/reproducibility evidence; no unexpected kernel builds |
| implementer2 | historical-candidate.md | Added by explicit user direction; historical expected candidate producer, published bytes and restorability; independent of current-byte and CI packages |
| implementer3 | fixture-contract.md | Added by explicit user direction; fixture consumers and normal-package linkage, narrow correction acceptance; analysis rather than change review |
| lead | plan/state, acceptance inspection and final recommendation | Reconcile evidence and uncertainty, preserve stable portal link and user decisions |
| reviewer0 | Retained independent review role | No automatic review for investigation/findings alone; application deliverables remain out of scope |

Use source and published derivations/artifacts first. Bound expensive checks;
fresh Luna/low utility owns launch/monitoring of long or uncertain builds under
the monitoring skill. Stop unexpected local kernel compilation. Do not rerun
CI or launch full VM tests just to replace diagnosis.

Compatibility assessment must cover fixture/kernel/toolchain byte identity,
mixed versions and supported test variants, integrity and rollback contracts.
No running systems, persisted state, database schemas, APIs or protocols change
during this investigation. Proposed implementation must identify its test-only
or runtime impact explicitly, with quick checks before review and long tests.

Readers are the user deciding the next step and a future implementer. Findings
and proposed design belong in this session's Markdown records; no project docs
are changed because no correction has been accepted or implemented.

User feedback milestone: reassess the historical v7 digest allowlist as a
development-CI policy. Propose testing the current normal candidate without
freezing Nixpkgs, retaining exact released predecessors, boot compatibility,
runtime/data-integrity checks and useful artifact identity evidence. Architect
owns revised design; implementer3 maps candidate hash/layout dependencies and
implementer1 assesses kernel rebuild implications from existing source/graphs.
This remains a proposal only. A runtime digest may establish that the guest
tested the selected build; it does not establish historical qualification.

## Conditional integration authorization

The user subsequently directed: “all right, so when the CI passes, you can
merge it”. This authorizes this feature into vpsfreecz/vpsadminos staging only
after complete CI success; see state.md for exact scope, run and merge gates.
Deployment and session closure remain outside scope.
