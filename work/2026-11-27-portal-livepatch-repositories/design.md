# Repository review implementation brief

The accepted plan.md owns scope and delivery. User “proceed” authorizes execution,
aitherdev deployment and the listed master integrations after verification.

Lead implementation is in the new dev-workspace worktree, starting at 907c14ca.
No saved team exists for this CLI-only record; the originating lead implements.
Mandatory review will use the installed catalog's standalone review-purpose role.

Use a schema-1 private review-base file keyed by existing slug/repository identity,
with scope, exact base and recorded identity. The setting is independent of HEAD
but only valid for descendant heads. Existing durable descriptors remain untouched.
New explicit-base views avoid the legacy immutable automatic comparison slot.
Read APIs expose a comparison version computed from HEAD plus policy and default
identity; browser retries only on changed inputs or explicit refresh.

The CLI uses the existing worktree session lock and Go bridge, validates current
registration/head before publication, and refuses archived mutation. Preserve
old manifest and journal formats. Old packages ignore the setting; upgraded reads
retain it across archive/revive for the same identity. No speculative migration.

Use visible-card lazy history with at most two active history reads. Healthy cards
render independently. Preserve summary/file queues, controls and frozen views.
Keep four-second command and process budgets; errors preserve cancellation and
missing-data distinctions. Stop routine one-second observation from doing costly
pair discovery: consume established immutable results or explicit pre-merge capture,
while preserving automatic capture where it can be reused safely.

Verification follows plan.md: focused Go/Ruby/browser checks, committed final
review, then package/integration/CI, matched input check and scoped host build.
Deployment is system first then user profile. Apply only evidenced per-branch
review bases, verify live browser behavior, and fast-forward all three final
branches. Recovery uses the installed original transition contract and retained
generations; review-base clear is separate from software recovery. No reboot,
archive or destructive cleanup is authorized by this task.
