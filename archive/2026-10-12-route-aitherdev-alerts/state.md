---
lifecycle: complete
---

# 2026-10-12-route-aitherdev-alerts

## Status

Phase: merged into configuration master; deployment remains pending direction.
Implementation, focused checks, independent final review, remediation, real
alerter builds, publication and integration are complete. No production
configuration has been deployed or notifications sent. Session remains open.

Final head: `b17dbea2cb1b9bf93714c929da776a4d4a6618f8` on published
`origin/2026-10-12-route-aitherdev-alerts` and `origin/master`. Historical base
is `8e4da52c55f1d4396547630d1d4de518f8255619`. Both owned project checkouts
are clean, and the feature ref/worktree is retained.

## Phase checklist

- [x] Verify exact session identity, environment and retained roster.
- [x] Investigate and record generic design before implementation.
- [x] Implement recipient metadata, registry, routing, aitherdev policy and docs.
- [x] Pass quick checks and commit the complete deliverable with active hooks.
- [x] Independent final review, including whole-branch history and migrations.
- [x] Fix and verify netboot carrier duplication; fold into feature commit.
- [x] Pass remaining rules checks and real alerts1/alerts2 builds.
- [x] Publish exact final branch and save portal comparison.
- [x] Merge into configuration master after explicit user direction.
- [ ] Deploy and verify both Alertmanager replicas (not requested).

## Next action

User approved integration with "ok, merge it", following the handoff naming
`vpsfree-cz-configuration/master`. Scope is this repository/target only;
deployment remains unrequested. At preflight, default matched the reviewed base,
the full series and diff matched the saved final inventory, and no rebase was
needed. [Integration preflight](integration-preflight.json) records exact heads.

Master was fast-forwarded and pushed from a fresh detached target checkout at
`worktrees/2026-10-12-route-aitherdev-alerts/vpsfree-cz-configuration-merge`,
preserving canonical shared branches and the retained feature worktree/ref.
[Integration proof](integration.json) verifies remote master and feature heads
both equal `b17dbea2...`. Focused checks passed from the target checkout before
its non-force SSH push; the exact reviewed/remediated tree is unchanged.
Both live replicas still require a separately authorized deployment before
aitherdev alerts stop notifying the team. Keep the session open.

## Repositories and history

- Repository: `vpsfree-cz-configuration`.
- Worktree: `worktrees/2026-10-12-route-aitherdev-alerts/vpsfree-cz-configuration`.
- Complete series: supporting refactor `c9dffde58bddc37736da2cea3c79dc4bd55ba7e3`,
  then feature/tests/docs `b17dbea2cb1b9bf93714c929da776a4d4a6618f8`.
- [Final inventory](branch-inventory.md), [final diff](configuration-final.diff)
  and saved portal comparison identify the exact base and final head.
- Lead inspected the full final series and correction diff after review:
  no obsolete history, no migrations and no repeated update streams. Both
  feature commits were merged into remote master after user approval; no
  deployment has been performed by this session.
- Published over the canonical SSH remote; exact remote feature/default heads
  were checked. The repository has only a scheduled/manual Daily update
  workflow, with no feature push-triggered verification workflow.

## Independent review

Risk high; general, architecture/repetition, scope/proportionality and
risk/compatibility lanes completed. Retained `reviewer0` remained read-only,
with saved and actual native GPT-6 Astra/xhigh settings; no fallback or nested
reviewer. Thread `01a13084-9461-7121-8f22-b3d5f06c2591`, turn
`01a1309e-fcd4-7771-a38b-2cc0f98d49b4`.

[Review](review.md) and [assigned packet](review-packet.md) preserve the evidence.
The reviewer covered both commits at original feature head `a33c499f...` and
explicitly concluded coherent history, no migrations and no repeated streams.
No Blocking findings or extra Advisories; one Important finding identified
receiver duplication for selected netboot nodes. The exact requested narrow
fix filters `carrier == null` and tests real pinned confctl carrier expansion.
It passed focused checks and was folded into the owning feature commit.
[Correction evidence](carrier-fix-checks.md) and [diff](carrier-fix.diff) record
lead verification. The reviewer's narrow-fix conclusion requires no rerun.

## Verification

- Pinned `nix develop` setup installed/signed Overcommit; all three commit
  operations ran active Nixfmt and message hooks. Only advisory TextWidth
  warnings (>72, within the required 80 columns) occurred.
- Nix evaluation, Nixfmt, shell syntax and whitespace checks passed.
- Focused `alert-recipients` and `infra-monitoring-config` checks passed before
  review in 26 seconds: [quick.log](quick.log), [quick.status](quick.status).
- Both focused checks passed again after the carrier correction. The test uses
  actual carrier expansion, asserts unique receivers/identity routes, and runs
  real amtool validation and receiver selection with inert transports.
- Fresh Luna/low watcher completed [verify.sh](verify.sh) at the exact final
  head in 176 seconds, exit 0: [verification.log](verification.log),
  [verification.status](verification.status). This passed
  `infra-monitoring-rules` and built exactly alerts1 and alerts2.
- No unexpected local Linux kernel build and no outstanding verification run.
- Integration rechecked `alert-recipients` and `infra-monitoring-config` from
  the target checkout before pushing master; both passed.
- Offline checks do not exercise live delivery, runtime daytime activation,
  repeat timers, inhibition or loaded production replicas.

## Documentation and compatibility

[Design](design.md) and [initial findings](findings.md) explain the choices.
Project `docs/services/monitoring.md` now documents the setting, registry,
identity precedence, SMS policies, rollout and rollback. Its existing mkdocs
navigation was checked. The main agent applied vpsfree-user-facing-writing.

No metric labels/rules, transport credentials, input pins, APIs, client/CLI
contracts, protocols, schemas or persisted formats changed. Public/global
alerts without machine identity retain team routing. Only both Alertmanager
replicas need a runtime update; old replicas can still notify the team during
mixed versions. Reverting both previous configurations restores team delivery
and can read retained state without migration/deletion.

## Coordination and recovery evidence

`dev-session current` and both environment markers matched the exact developer
binding at each work phase; retained roster was verified before implementation
and review. Initial coordination plan/state committed as `d1e128eb`; later
tracking remains current under the normal checkpoint cadence.

Worktree creation reached Git but failed post-checkout hooks due to missing
ambient gems. Pinned-shell setup succeeded in 71 seconds; ordinary registration
retry reused the checkout without bypassing hooks. [Reusable lesson](../../notes/vpsfree-cz-configuration/2026-10-12-worktree-hook-setup.md).
No lifecycle action or session cleanup was requested or performed.
