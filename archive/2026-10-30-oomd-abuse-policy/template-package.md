# Notification template package

Implementation committed and published; awaiting lead-coordinated final review.
No deployment or integration performed.

- Repository: `git@github.com:vpsfreecz/vpsfree-notification-templates.git`.
- Worktree: `worktrees/2026-10-30-oomd-abuse-policy/vpsfree-notification-templates`.
- Branch: `2026-10-30-oomd-abuse-policy`.
- Fresh fetched base/remote master: `2cfd218d9152888feea4109f064459078ea9f76e`.
- Head/verified remote feature ref: `e8c2c3df4ae57015ff4fba3647b13aa219d0c216`.
- Final tree: `c3f5bbe495de2581705720604d4e38f68093d1a7`.
- Whole series: one commit, `e8c2c3d vps_oom: add repeated-incident warning and stopped mail`.
- No migrations. No obsolete approaches, follow-up commits, repeated dependency
  updates, pin changes or generated streams. No release/deployment/external use.
- Captured portal comparison at this exact base/head; worktree clean.

## Changes and acceptance

Two declarative templates, `vps_oom_warning` and `vps_oom_stopped`, each with
metadata and Czech/English subject/text. Shared stop template covers first/repeat
stops. Source matches the lead's mail-copy brief; lead accepted source and
synthetic previews before the commit. Plain text follows existing interpolation
conventions. Incident links use verified legacy `page=incidents&action=list`
handler with `list=1`, VPS ID and `codename=oomd` filters. No HTML changes.

README explains the feature purpose, current limits/enforcement vs decision
counts, backend registration requirement and compatibility. Underlying action
invariants belong to backend documentation; no independent rules added here.
No node changes, deployment, KB writes or integration.

## Verification

- `nix run .#check`: passed, 75 templates and 373 template files.
- `nix flake check`: passed; package check derivation
  `/nix/store/8f6cbc2439cah8pwhcw2sa3njnsyx8rm-vpsfree-notification-templates-1.drv`.
- Synthetic rendering: 16 subject/body cases across both templates/languages,
  enforcement true/false and default 5/10 vs custom 6/15 limits; 8 stopped
  first/repeat equivalence cases. Passed effective-limit substitution, future
  claims suppressed with false, manual restart retained, fixed links and no
  unrendered ERB. Counts remain decision snapshots.
- Final render used exact TemplateBuilder/TimeZones source from repository-pinned
  vpsAdmin `9fc0648accd414246d6422e67106ae7217486020`, under this repository's
  `nix develop` Ruby environment. Europe/Prague converted 15:20 UTC to 16:20 CET.
- No repository hook framework declared and `core.hooksPath` unset. Required
  checker/flake checks passed before commit; no hook bypass.
- Post-check commit tree exactly equals verified staged tree; rebase was no-op.
  An attempted pre-commit rebase correctly refused staged edits; no mutation
  occurred, then commit and clean rebase completed normally.

Checks launched by fresh gpt-6-luna/low verification utility under catalog
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`.
Known short final runtime-helper rendering ran inline. Raw logs/fixtures and
[rendered previews](template-evidence/template-previews.md) remain untracked under
`template-evidence/`; no personal data used.

The original head `c8cb569a2bbeb5abd422e54a26fb928d7e81462c` passed hosted
`Check` run `41104111108`. It is superseded by the correction below; that result
is historical, not exact-current-head CI proof. New `Check` run `41107732433` passed
at exact current head `e8c2c3df4ae57015ff4fba3647b13aa219d0c216`; evidence is
`template-evidence/autostart-fix/ci-status.json`. No superseded running/queued
same-branch run needed cancellation.

## Final autostart wording correction

Lead-approved narrow correction describes the historical stop effect rather
than asserting current autostart state, because a later normal VPS start can
re-enable autostart before delayed mail arrives. Only the Czech/English stopped
body opening changed. All other templates, prose, metadata and conditions are
byte-identical. Same base `2cfd218d9152888feea4109f064459078ea9f76e`:

- Old range ends `c8cb569a2bbeb5abd422e54a26fb928d7e81462c`, old tree
  `b1c3a9b125cb774950d313ee465c34af7d20a647`.
- New range ends `e8c2c3df4ae57015ff4fba3647b13aa219d0c216`, verified tree above.
- Range-diff and exact correction retained under
  `template-evidence/autostart-fix/{range-diff.txt,correction.diff}`.
- Required checker and flake check rerun passed on final tree; final pinned
  renderer16cases+8equivalence checks passed. Updated previews/logs under
  `template-evidence/autostart-fix/`; short cached checks ran inline.
- Folded into owning one-commit unmerged series; no migrations/release/deployment
  or independent final review before correction. Fresh fetch/no-op rebase and
  explicit old-SHA force-with-lease succeeded; remote exact head/master verified.

## Review boundary

Lead coordinates mandatory independent final committed-deliverable review with
all packages. Supply this one-commit complete range and README+two-directory
final diff. Cross-project consumer is vpsAdmin mail registry/TemplateBuilder;
backend implementer owns registrations, fallback templates and freshness of
current send-time `stop_enforced`/limits. Site template false conditions are
verified. No long integration checks started before review.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/>.
