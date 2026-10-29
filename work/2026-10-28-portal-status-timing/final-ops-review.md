# Process-admission refinement and final consumer pins

Review committed operational delta abe635989..cf92beac0 in shared rollout.md.
The real host preflight found protected same-UID /proc entries that user scanning
cannot inspect. Native process classification now uses the same existing root
SSH read-only scan path as descriptor inspection, selecting fixed aither UID1000.
It recognizes --remote clients for the exact portal socket, leaving them to the
ordinary switch. The initial idle loop now waits for stock CLI clients before
stopping backends. Final publication still refuses all source native processes.
No user client is killed, no permissions/cgroups changed. A copied executable
fixture tests privileged embedded-client discovery; 16 migration tests pass.
The user says they closed stock clients, then correctly noted one remaining CLI
is probably this conversation. Detached job must wait until it exits normally.
No live deployment or migration yet. No journal exists in prepared private root.

Review this bounded operational refinement with general/risk lanes; no new
observation architecture. Prior same-thread reviews remain authoritative for
unchanged source. A report in final-ops-review-result.md is allowed; no source
edits, live mutations or delegation.

Final consumer refresh is committed/published and composition checker passes:
configuration 584691d9b96ce1555a5787a0a1d999eeb528811f from
7a254c88b0b54a32300a319b3e4ed32936d9b004; workspace
c2511ea7358322b4a68e3161de0c18af25883a12 from abe635989.
Both pin reviewed runtime cc0d452a0653a112c8a013492c1734d9554bb909.
Configuration has one generated runtime pin plus the unchanged credential/doc
commit; workspace has one pin commit. The extension/codex-web/native inputs are
unchanged. Confirm mechanical final pin/history/migration conclusion. Workspace
will be rebased patch-equivalently onto the latest shared operational commit
before final readiness; no feature-content changes in that rebase.
Browser/final build batch is running on these exact final consumer inputs.
