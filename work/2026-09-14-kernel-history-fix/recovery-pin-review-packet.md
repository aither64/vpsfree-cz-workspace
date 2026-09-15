# Recovery delivery pin review

Review the exact final feature heads and prepared operator instructions after
implementation review. User explicitly selected GPT-6 Astra at xhigh. No
persistent instruction changes, production actions or session lifecycle actions.
Perform the review directly; no nested agents. Read the mandatory review skill
and relevant lane reference and project AGENTS files.

Workspace: /home/aither/workspace/ai/vpsfree.cz
Session: 2026-09-14-kernel-history-fix
Worktrees: worktrees/2026-09-14-kernel-history-fix/<project>
Tracking: work/2026-09-14-kernel-history-fix

Final heads:
- vpsadmin: 42984def67d405c235e2a34d91820563858ddd89
  base014fbc78422f3660b295add7a50f35cc7acdf0c8.
- vpsfree-maintenance-tasks: 2fdc9f2889ac419136cd0cde0e0955c015ae7107
  base6eea682ede8d8e2634b2d41e5b11cf0f02231bc6.
- vpsfree-cz-configuration: c8b7a4995b587b7e072b5f77be6006356fbb104d
  base3f213d5ebf922ab5522690ab28b3fdfa9b3bed1d.
- vpsfree-kb-contracts: 610cb7bf35953ea6c1a9110fc12102e0713fcfc5,
  base919577d0c770e47b623c591f8bf0cce4e8d30666.

All implementation lanes completed; see recovery-review-reconciliation.md and
four recovery-review-*.md reports. Direct fixes: full synthetic SHA; small
unconditional maintenance executable with importable runner and installed-load
subprocess test; approved task-owned default1000. No change in repair or public
API scope. No further implementation review is requested unless evidence shows
an unreviewed material problem.

Review focus: exact pin consistency across C/K, intended channel-only scope,
prepared rollout and all-node maintenance invocation. C changes only
vpsadminServices, generated commit message untouched. K changes five canonical
V revision files only; OS6bdf458 and existing nixpkgs pins preserved. One commit
per generated pin; V two logical permanent commits; M one dated task commit.
No one-time repair code remains in V. No public API field/protocol/UI layout.

Quick checks: 130 focused DB examples; 23 API visibility/CLI cases; two migrations;
403 non-migration specs covered once; CI selector16runs55assertions; full current
upstream+migrations schema exactly matches core schema. Remediation: exact Nix
fixture parser preflight; 29 maintenance DB cases including installed-load help,
all-node preview/subset apply/all-node apply/rerun; six task Ruby files lint clean.
K bin/check passed with no drift; 120PNGvariants valid. All eleven C buildPlan
consumers resolve vpsadminServices at exactV42984def6, recorded in
recovery-consumer-inputs.json. Their full builds and local supervisor/WebUI
integration are running; inspect results if available, do not presume success.
New V CI has passed migrations/lint/i18n/PHPUnit/libnodectld; API/full integration
are queued. All final-head CI will be monitored to completion separately.

Operator instructions: rollout.md and M dated task README. Rollout file is being
updated mechanically to final C/V/M hashes and eventual build generation by root;
review current order and safety behavior. Pause both supervisors with the reviewed runtime condition drop-in and marker,
activate API1, migrate with database account and new package, activate API2,
remove only the temporary guard files, reload/restart both, verify normal health and advancing confirmation metadata
without public revisions changing. Both additive migrations have no backfill.
Old code can ignore schema on application rollback, but old bugs return.
No node upgrade/reboot. Repair is separate, default all eligible node/storage
including inactive, --node repeated subset, --apply explicit. Immutable proof
only, strict lower<proof<upper, fixed candidates, revalidation under node lock,
revision invalidation, idempotence. Dry-run does not reserve later proposals;
exact preview procedure keeps all writers paused. No evidence invention.

Output only your report under tracking: recovery-pin-review-<lane>.md. Do not
edit state.md, project files or other reports. Report Blocking/Important/Advisory
or clearly no findings, with residual validation limitations.
