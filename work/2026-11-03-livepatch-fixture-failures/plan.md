# Livepatch fixture failure investigation

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
