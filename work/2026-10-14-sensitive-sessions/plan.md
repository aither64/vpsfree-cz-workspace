# Sensitive sessions

Implement the approved conversation plan: immutable creation-time sensitivity for session records only, normal work/archive paths with local Git exclusions, visible portal badges, inherited forks/plans, journal-safe local archive/revive/delete, trusted agent instructions and coordinator compatibility. Project code retains normal Git workflows. No conversion of existing sessions.

Affected repositories: dev-workspace (runtime/portal/docs/tests), vpsfree-dev-workspace (handoff guidance), workspace (agent procedures). Documentation readers are operators and future maintainers; feature behavior belongs in runtime session/archive/portal docs, site policy in workspace procedures.

Compatibility: omit fields on ordinary sessions and preserve their identities. Sensitive metadata must survive retries, archive/revive and package transitions; older readers must refuse rather than strip it. Existing ownership, coordination fences and machine reservations remain authoritative. No database, guest/node protocol or configuration format change. Recovery restores a capable matching CLI/portal package; no coordinated node updates. Activation stays in the user profile.

Verification: focused Ruby/Go/browser tests, committed-deliverable independent review, then packaged checks using the verification watcher. Exercise ignored staging, interrupted lifecycle, inherited creation, local evidence and coordinator identity. All default-branch integration or deployment goes through prepare/approve/submit/status using actual user authorization. Merges need no reservation; authorized deployment requests aitherdev near readiness, retains reservation during review and uses finish after exact integration proofs. No merge/deploy authorization supplied yet.
