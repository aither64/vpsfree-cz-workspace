# Static API specs rebalance: accepted implementation plan

User approved implementation on 2026-10-04 after accepting this plan. Dynamic
weighted shards and timing-based assignment are explicitly rejected. Keep
13 static domain topics in each full/core mode,26 test jobs, existing tests,
plugin skip semantics, randomized order and isolated processes/databases.

## Changes

Commit1: capture RSpec native JSON results alongside readable output; retain
seven-day mode-qualified artifacts. Upload manifests for both modes. The stable
API specs - topic coverage gate validates13nonempty manifests per mode against
the eligible tracked spec universe, exact once, and fails if either matrix is
failed/cancelled/timed out. Keep original13topics for this baseline commit.

Commit2: static partition and developer placement guidance. Foundation combines
smoke, coverage, routes, engine/models and supervisor. Platform becomes
infrastructure (node_*,os_*,migration_plan), operations (security_advisory*,
oom_report*,incident_report,lifecycle_bypass,object_history,transaction*), and
configuration (explicit remaining original patterns and spec/lib). Auth holds
oauth2_client,password_change_log,webauthn,user_known_device,user_public_key,
user_session,user_totp_device,user_webauthn_credential. Users holds existing
user_cluster_resource*,user_environment_config,user_namespace*,user_read,
user_state_log,user_touch,user_available_ips,user_write. IP ownership holds
ip_address*,ip_release*; network holds existing network/interface patterns,
host_ip_address,location_network. DNS/storage/mail/plugins/VPS unchanged.
All resource patterns retain existing directory and _spec.rb suffix. No test
moves, catch-all assignment, runtime/auth/schema changes or new selector system.
Update workflow, docs/agent-instructions/testing.md, and AGENTS.md.

## Verification and delivery

Quick checks: syntax/YAML/workflow checks and mandatory hooks in project Nix
shell; compare original/candidate file universe (currently415) in both modes;
exercise missing/duplicate/untracked/empty/incomplete manifest cases and
matrix failure/cancellation result gate. Native JSON replaces custom formatters.
Retained reviewer0 independently reviews both committed changes, complete
base-to-head history/final diff, CI status compatibility, and no migrations
before long CI. Two functional commits are intended and legitimate, not
obsolete iterative history.

Push only baseline commit1 to the same feature branch, run all full/core tests,
retain IDs/results/timings; after completion push candidate commit2. Run candidate
twice. API code/dependency pins must be identical across snapshots. Fresh
catalog-policy Luna/low utility watchers observe each operation. Compare example
IDs, outcomes/pending reasons by mode; require no omissions or extra skips and
all matrices+aggregate successful. Seek <=25min slowest-job time across both
candidate runs, recording queue/setup separately. Investigate failure evidence
before retries; material design deviations return through lead/architect.

No production deployment or database migration needed. Required-check context
lookup previously403; inventory when possible and report exact rename/migration
requirements. No default-branch integration without explicit direction for
vpsadmin/master. Rollback restores prior matrix/check settings. Keep session
active/open and branches retained.

## Owners

Lead: records, worktree/review/CI coordination, evidence reconciliation.
architect0: finalize focused design/verification brief before implementation.
implementer0: source edits, two commits, quick checks, hook setup.
reviewer0: independent read-only change/history review.
Fresh verification watcher: long operations only, no edits/diagnosis/retries.
