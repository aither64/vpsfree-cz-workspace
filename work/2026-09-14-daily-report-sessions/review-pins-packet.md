# Final configuration pin review

Review the committed configuration range
249bed1ee28e69a907edd09ea97a1144dbcdefeb..5036135728832d5c375705e3b69949c33460ff7e in
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-daily-report-sessions/vpsfree-cz-configuration.
Read the repository AGENTS.md and mandatory-change-review skill/lane reference.
Review directly, without editing code or delegating. Save your assigned result
under this tracking directory.

This is the downstream phase of the approved daily report session/password
feature. Full scope: plan.md. Functional reviews: review-packet.md, review-*.md,
and review-reconciliation.md. User selected validated branches: push and build
all three, no merge/deploy or session lifecycle actions.

Two generated confctl --commit commits intentionally remain separate, with their
automatic changelog messages unchanged. They alter only flake.lock:

- vpsadmin channel / vpsadmin role -> vpsadminServices at
  9456fae6f181cef2e8982eed462e873095fd49da
- vpsfree-notification-templates channel / same role ->
  vpsfreeNotificationTemplates at 08402ffd8010384f950b1ec4a1b95de8e5410ba3

Both source heads are committed and pushed on
2026-09-14-daily-report-sessions. Their worktrees are siblings of the configuration
worktree. Verify exact pins, the template's vpsadmin follows relation to
vpsadminServices, and that staging/production vpsAdmin, vpsAdminOS, nixpkgs, and
unrelated inputs are unchanged. API1 owns scheduler plus managed templates;
API2 consumes vpsadminServices only. No template upload or manual flake edits.

Functional final-head narrow fixes after full review added the four Hash vars
to MailTemplate metadata, parity comments in the helper, registry assertions in
the existing spec, and an HTML Storage heading. No authentication/query behavior
changed. Final 17 report specs and final template flake check passed.
Functional commit hooks and template CI, migration CI, and lint CI passed.
Local delivered-mail integration is now running after functional review.
Configuration builds have NOT started; they follow this final pin review.

Quick checks: diff --check, generated commit hooks, Python lock comparison
proving only the two expected nodes change, exact revisions/follows, and
git ls-remote proving source revisions are pushed.

Risk remains high because of additive live-table indexes and rollout order.
No hand-written configuration logic changed; this bounded follow-up review uses
general and risk lanes, gpt-5.6-sol/xhigh. Previous architecture/scope findings
and dispositions remain applicable. No index is needed for schema correctness
but indexed query performance requires explicit migrate-db on the live API hosts
(autoSetup=false). Rollback can leave indexes, and new template sections guard
old payloads. Build --yes 'cz.vpsfree/vpsadmin/int.api*' after review, no activation.
