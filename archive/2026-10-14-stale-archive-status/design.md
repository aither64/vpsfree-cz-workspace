# Design and verification brief

Use the existing details read, adding a required string pendingLifecycle in new
server responses. Read the exact session's validated journal presence; return
an error on unsafe/conflicting journal state. Absence is never inferred from a
cached idle operation. No change to mutation authorization or identity formats.

One browser reconciliation path consumes a fresh successful details response.
Only archived tracking with explicitly empty pendingLifecycle establishes a
completed archive. Clear pending UI state and reload once; coalesce reads and
ignore outdated responses. Use this path during initial/polling reads, ordinary
details refresh and fresh Retry preflight. Preserve running operations, genuine
journals and warnings on failed or older reads.

Acceptance: old pending page becomes the normal archived page without user
action or mutation; Retry after completion does the same; real unfinished
operations retain recovery; read failures/missing fields cause no reload loop.
Index authoritative refresh hides an absent pending badge.

Quick checks: JavaScript syntax, focused Go details/journal tests and existing
Node lifecycle contracts. Longer checks: Chromium/Firefox stale archive and
lifecycle regressions, packaged application and matching aitherdev build.
Final independent review covers General, Architecture, Scope and Risk lanes,
including additive API mixed-version behavior and whole-branch history. No
migrations or repeated pin streams should remain.

Deployment: same runtime in workspace nested override and confctl devWorkspace
role, preserving extension/siblings/native package. Existing coordinator schema,
adapters, machine mapping and provider state must remain supported. Prepare and
build outside claims; merge without reservations; reserve aitherdev near prepared
activation; system then profile jobs. Keep reservation through acceptance and
requested UI review. Recover original uncertain jobs; forward-only profile
recovery. Verify live system/profile identity, provider selection and retained
thread/tmux continuity before finish. Existing archived records are read-only.
