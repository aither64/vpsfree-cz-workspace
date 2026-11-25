# React shared incident escalation — final affected review packet

Phase: complete local committed source and quick checks, awaiting lead-coordinated
independent affected review. Builds/browsers/captures/publication remain held.
No merge, deployment or lifecycle action is authorized.

## Scope and exact source

User approved shared escalation: “ok, agreed, reworkit”. Architect/lead released
[implementation-contract.md](implementation-contract.md), aligned
[design.md](design.md) and final [copy](mail-rework-copy.md). Owner2 implements
only separate React `vpsadmin-webui`; owner0 owns backend, owner1 legacy UI and
owner3 templates/KB. See [plan](plan.md), [state](state.md) and
[React progress](react-rework.md).

- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/vpsadmin-webui`.
- Feature: `dev/oomd-abuse-policy`; existing PR115 remains open at original b67.
- SSH main/base: `40653dffed4561dd6086716fd506a7223d3631d7`.
- Final head: `55a813b44edb915c7ed5ce68366d6d797a551606`.
- Tree: `a9de950ca24ba002143a24744e6d8c1091e6a067`; worktree/index clean.
- Complete series: one commit, `55a813b4 vps: show selected incident escalation status and settings`.
- Final scope:30files,1040insertions/23deletions. Exact diff:
  `react-rework-verification/final.diff`.

Single application commit includes directly supporting adapters, UI, catalogs,
tests and feature docs because they implement one selected-type contract. There
is no independently useful transport, rule framework, pin or deployment change.
The frontend consumes backend policy; it does not implement enforcement.

## History and migration conclusion

Original reviewed/published OOM-only range
`40653dff..b67c7917e8758e707e0b88512f055eab9fbd8529` contained626c6cf6application
andb67c7917evidence/4PNGs. Preserved under
`refs/heads/dev/oomd-abuse-policy-original-b67c7917`; original receipts remain in
[react-package.md](react-package.md), [review.md](review.md) and
`react-verification/`. Original captures are also copied into
`react-verification/historical-b67-captures/`. They are historical only.

Shared conversion first committed as2fb91af6c21ec9fe84219fb957ca327178ad3e9d,
preserved under `refs/heads/dev/incident-escalation-before-consolidation-2fb91af6`.
Interactive rebase folded original app/evidence and conversion into one final
generic implementation. Old screenshot additions and superseded OOM feature
paths disappear from final series. Full pre/post trees equal
`a9de950ca24ba002143a24744e6d8c1091e6a067`; `git diff old new` exit0.
Original-to-rework substantive differences are intentional contract rework,
not claimed equivalent to the original implementation.

Receipts in `react-rework-verification/`:

- `preconsolidation.json`, `consolidation.range-diff`.
- `original-to-rework.diff`, `original-to-final.range-diff`.
- `final-source.json`: exact hashes, clean status, series, check-input differences.

**No migrations** in React, no persisted schema/protocol changes. Backend owns
its separate migration provenance. No repeated dependency/input/generated update
streams; package locks and flake pins unchanged. No transitional OOM aliases or
intermediate old-label media remain in this feature range.

## Implemented acceptance and boundaries

- Existing VPS Index/Show/Update consume exact common `incident_*` flat fields.
  Initial reads omit new parameters; numeric count plus returned selector detect
  capability. Known list/detail refreshes carry the returned key. Old APIs hide
  controls/indicators; no fabricated zero counts or per-row report pagination.
- API-localized `incident_policy_label` renders escaped as text. Counts, limits,
  warning time and history key are selected-type. Stop permission, cooldown and
  unfinished physical stop are described as VPS-wide with approved exact help.
- Only registered `oomd` gets memory-protection help. Synthetic `test_rule` exists
  in tests only and proves count/limit/history/settings/readback isolation.
- Admin editor submits explicit selector plus nullable overrides/shared bool;
  confirmation, immutable snapshot, preflight and durable lock remain. Selected
  readback verifies selector and values before clearing drafts. Unrelated async
  receipt guards remain strict. Backend rejects mixed fields before effects;
  client tests describe only its defensive synchronous allowlist.
- Server status/mode/action/cooldown fields remain authoritative. Cooldown is
  next-new-incident eligibility at/after24h, never a scheduled stop. Defaults5/7d,
  10/30d unchanged. Pending/failed/uncertain differ from confirmed stop history.
- Existing desktop/mobile list and admin status/exemption filters preserve owner
  scope and pagination reset. Latest-search ref retains rapid consecutive edits
  before router commit and resynchronizes external/Back navigation.
- No arbitrary type/rule editor, extra navigation, BFF route, action, transport,
  local threshold calculation or unrelated process OOM screen changes.

## Quick evidence and failures retained honestly

Commands use pinned `nix develop`. Root dependencies restored only via offline
`npm ci --offline --no-audit --no-fund`:293,654,528allocated bytes,31.22s,exit0.
This is a new verification allocation after cleanup; BFF deps/dist absent.
See `root-dependency-allocation.json`/install log. No wholesale cache refill.

1. Initial watcher wrapper failed before test launch: `/usr/bin/time` unavailable.
   Python monotonic runner replaced only that wrapper; no false test result.
2. First actual focused batch, six files:
   `vps.incident.test.ts`, `vps.blocking.test.ts`,
   `vpsIncidentEscalation.test.ts`, `VpsIncident.test.tsx`,
   `VpsIncidentFilters.test.tsx`, `useVpsListSmartFilters.test.tsx`:
   **75passed/1failed**. Ambiguous test mock returned both `vps` and `vpses`;
   strict adapter correctly rejected it. Mock corrected to distinct responses.
   Failed `focused-quick.log/result.json` remain unchanged.
3. Only affected adapter file rerun: **18/18passed**,~8s. Other five successful
   files retained for unchanged production inputs; not relabeled as one full run.
4. Remaining batch81.93s: `typecheck`, `typecheck:e2e:core`,
   `audit:design-docs`, `lint` all passed. First failure `format:check` on renamed
   `tsconfig.e2e.json`; Prettier fixed formatting only. Adopted lists retain
   coverage, sorted without baseline/deferral relaxation. Failed receipt retained.
5. Fresh watcher20.6s,exit0: `format:check`, `audit:i18n`,
   `audit:i18n-structure`, `audit:structural`, `audit:component-contracts`,
   `audit:pages`, `audit:active-docs`, `audit:ui-strings:check`,
   `audit:mutations:check`.8411matching EN/CS keys;0unaccepted structural
   violations/0new exceptions;225mutations/no warnings.
6. Final rendered-file assertion uses current exemption catalog text and checks
   EN/CS API type labels: **19/19passed**,10.76s. Final `typecheck` and
   `audit:design-docs` passed after changed tests/docs; log
   `final-types-docs.log`. `git diff --check` passed before commit.

`final-source.json` binds the final commit and enumerates changed files since
each hashed batch. Product source did not change after focused/audit checks;
differences are corrected mock, strengthened rendered tests, documentation and
sorted/formatted adoption configuration, covered by the affected follow-ups.
History consolidation proved exact tree equality to the committed checked tree.

Watchers used fresh catalog495ef662 Luna/low fullaccess/never operations;
standalone audit watcher launch header/session01a18ea9-2abb-7f00-8c40-db981812e519
is retained. No operation is still running. No hooks are declared; actual
Git identity verified and normal Nix Git commit/rebase used, without bypass.

## Documentation, consumers and remaining limits

Changed project explanations: `docs/design/API_CONTRACTS.md`, `WORKFLOWS.md`,
`REQUIREMENTS.md` REQ-051, `EVIDENCE_MATRIX.md` and
`docs/work-log/2026-10-30-incident-escalation.md`. Inventory regenerated/checked
(257routes,64adapters), no generated drift. Terminology pinned at vpsAdmin
`a65a4dfeb92a59df4a80a737a20bcbf8558793ff`; locked guides read. Lead applied
writing skill directly and approved generic indicator/statusfilter wording.

Backend `vpsadmin/docs/incident-escalation.md` owns common semantics; React
adapter/components are a consumer. Legacy UI/templates have separate owners.
Canonical external KB workflow read; owner3 handles affected legacy list concepts
with final backend pin. Current KB contract does not certify React. No KB
production/staging write or new capture is claimed here.

Risk classification high because admin settings, cross-project contract and
mixed-version capability are involved. Request general, architecture/repetition,
scope/proportionality and risk/compatibility lanes via lead's retained independent
reviewer0 saved settings. Review the completed consolidated range and affected
rework; original review does not certify changed common API behavior. Require
explicit whole-series/consolidation/no-migrations conclusion. Implementer does
not dispatch a duplicate reviewer while lead coordinates combined application.

Still held: full required checks/build/audits, affected desktop/mobile cs/en
browser cases and current screenshots, feature publication/PR refresh. Existing
browser source is typechecked only. Original hosted b67 evidence is exact-input
historical proof, never new API enforcement proof. Fixture browsers will not
certify real backend stop/mail execution. Future rollout uses matching backend/
schema/templates in observe mode, compatible UIs, then deliberate enablement;
frontend rollback leaves backend state intact. No deploy/default integration.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
