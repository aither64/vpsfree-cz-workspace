# Dated threadless installation integration review

Related follow-up to the completed creation-provider review. Retain reviewer
Astra/xhigh settings and independence; directly perform all four lanes under
mandatory-change-review. Do not edit application code, deploy or run long checks.
Full inventory is bootstrap-helper-final-inventory.json, with workspace new
helper commit and unchanged reviewed runtime/extension/configuration heads.

User authorized integration after successful creation-fix deployment. The fix
and approved Operations UI are deployed and independently live verified (see
creation-provider-deployed-live-checks.json and native regression evidence).
This separately accepted Astra design solves the known threadless bootstrap
admission gap without another conversation or permanent runtime permissions.
Design bootstrap-merge-design.md; lead acceptance bootstrap-merge-lead-acceptance.md.

Substantive source-only workspace helper bin/bootstrap-merge-2026-10-13,
lib/bootstrap_merge_2026_10_13.rb, test/bootstrap_merge_2026_10_13_test.rb,
docs/maintenance/bootstrap-merge-2026-10-13.md. It loads selected installed raw
host, uses generation/lifecycle admission and retained owner, frozen evidence,
ordinary prepare_merge/approval/submission/receipt APIs, owner-only claim when
all other owned jobs settled, standard workers and independent reconciliation.
No direct Git mutation, ledger writer, fixtures in live code, bootstrap token,
thread creation, ownership transfer, machine activation or finish/release.

The lead explicitly excludes all other bootstrap operations during serial merge
window; process lock alone does not exclude deployment bootstrap. This is a dated
installation-only operation under trusted-local-operator boundary, not concurrency
support for arbitrary bootstrap callers. Keep public CLI allowlist/scheduler intact.

Important retry paths: preparation receipt binds owner/request and frozen plan;
immutable bundle fixes approval/submit IDs; exact completion retry must return
ordinary receipts before stale checkout validation. Unknown/no-request claim
never redispatches. New claims reenter selected generation/session admission.
No format/migration change; new opaque receipt/artifact accepted by ordinary
reader, ordinary merge worker and existing recovery. Application derivation must
match before/after helper; no runtime repin/redeploy needed for this source-only
capability. Workspace adds descendant helper commit; no rewrite of deployed head.

Quick private-Git helper checks 7 tests/40 assertions. Actual workers prove project
and shared-root merges, preserve unrelated staged/unstaged files and feature refs,
reuse one job through completed retries and approval-only interruption, refuse
changed condition/evidence/generation/other pending owner job and no-request claim.
Existing fixture helper intentionally uses runtime test fixture policy on private
paths; production route never sets fixture mode. Initial path and catalog fixture
failures retained and explained in bootstrap-merge-helper-reconciliation.md.

Risk high: supervised integration admission, generation/lifecycle, external Git
publication/recovery. All four lanes. Existing whole-series conclusions for
unchanged projects may be reused, but explicitly review complete updated workspace
series/final diff, pin streams, no migrations and scope/proportionality. Assess
whether maintenance helper is bounded and test gaps are material. Save report to
owned tracking bootstrap-helper-review.md; new source and final inventory will be
committed before final assignment.

Final committed workspace head 08115821b03a30242d247985d08e3c4fe7d71683. Other three heads remain exactly
as reviewed in creation-provider-review.md. Complete base-to-head series and
final/delta diffs: bootstrap-helper-final-inventory.json. Quick checks pass
8 examples/40 assertions, explicit independent-systemd test deferred until
this final review. Application drv is identical before/after helper; proof
bootstrap-helper-application-equivalence.json. Installed regression passes
3/24 in creation-provider-installed-regression-corrected.log; actual provider
read-only check passes creation-provider-installed-provider-check.json.
All source/docs/tests are committed and published. Review all four final
histories, consolidated pin streams and no migrations explicitly. Native
retained-reviewer assignment unavailable (HTTP transport error); use fresh
installed default catalog Astra/xhigh fallback. Perform review directly with
no nested agents. Read mandatory-change-review and all four lane references.
Do not run long checks, mutate, deploy or make live RPC calls. Parent CLI saves
your final report. Avoid searching raw *.log or your own review log. Use named
packets and source paths. Treat the local workspace operator as trusted.
