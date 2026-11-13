# Final independent review — original six ranges

Reviewer0 delivered the full report to the lead in this conversation on 2026-11-13. This durable lead record preserves its decision, findings, exact ranges and conclusions. Reviewer retained read_only access and made no source/session edits, tests, builds, dispatches, merges, claims or lifecycle actions.

Reviewer: retained thread 01a1d53b-f8ca-7383-8a79-41928077c6df, gpt-6.1-sol / xhigh / read_only. All four lanes: general, architecture/repetition, scope/proportionality and risk/compatibility. Overall risk conservatively high because automated paths publish generated commits to default branches. Identity, saved settings, complete Git series, actual merge bases, heads and clean worktrees independently verified.

## Findings and decision

Important, general and risk lanes: original C1 vpsadminos-org-configuration daily-update.yml:3 at cdb886678ba30d10b5114cab279d5eb602209954 and E1 IRC daily-update.yml:3 at 41fd2f146d1fe7aa548e68b859a5d60cf2c55ba4 declare only schedule. Ordinary dispatch cannot execute either repaired workflow; old-run reruns do not test new source. Smallest correction is workflow_dispatch preserving schedules, default target, permissions, secrets, hooks and update behavior.

Lead accepted this finding, allocated minimal corrections to original owners, and requires quick checks, consolidated commits and affected general/risk follow-up review at actual successor heads. Successors are outside this original report.

No Blocking findings. No other Important source, history, architecture, scope or compatibility findings. Original six repairs are released to planned post-review acceptance checks. Review does not establish runtime success, waive acceptance, or grant merge/dispatch authority.

## Exact complete reviewed series

| Package/repository | Base | Head; sole commit |
| --- | --- | --- |
| B1 vpsfree-cz-configuration | 6e9ed6fb3ded5d72fbfa31c3feb4fccfcdfee494 | 355e269f034422bb042f6c39fdab1725855b47e0 — ci: reuse the initial daily update shell |
| C1 vpsadminos-org-configuration | ca96c95a1fee04793468785d8323a759615b2b4e | cdb886678ba30d10b5114cab279d5eb602209954 — ci: sign the custom pre-commit plugin before updating inputs |
| E1 vpsfree-irc-bot | 7d7a48b2b2dc45732cf5853deca196b1ae05571f | 41fd2f146d1fe7aa548e68b859a5d60cf2c55ba4 — ci: isolate dependency updates from Bundler preloads |
| F1 vpsadmin | 6f71da9777edfc902f6483edcdd84a2ef7d464ab | 81d754f47a58e92fddb2a84c67b1aec98b740ae3 — api: correct raw migration default expectations |
| G1 haveapi | b606b4b3c32bf05779c05babeaa1c31a33dee6fa | 3194488d1ab3403bbb83896bdac8089f1195e645 — utils: synchronize Ruff with guarded nixpkgs updates |
| H1 vpsfree-kb-contracts | f97785c2c265172a4c78893e0673034fde56e4dd | 2cfbde649769509e2628600535e3023d872f1735 — tests: wait for all firewall fixture listeners |

All worktrees are under worktrees/2026-11-13-scheduled-workflow-fixes/<repository>. Full diffs and packet remain review-diffs.md and review-packet.md.

## Scope and proportionality

Reviewer compared actual request and later merge/run direction with plan/state/design/audit/inventory and final diffstats: 19 files, 466 insertions, 55 deletions. G1 contributes 369 additions/9 deletions, comprising a 60-line stdlib helper, 264 lines of focused regression tests, bounded updater logic and existing docs; no dependency-management framework. Five other packages are small workflow/test changes.

Timeline assessed from dispatch14:10UTC to all six committed by approximately14:42 and review dispatch14:44:53, including C1 delivery14:21 and B1 delivery14:24. Overlapping member time was not summed. Concrete learning and independent repairs justify elapsed work; no scope-reduction finding. Native Nix profiles, standard signing, scoped preload clearing/fail-fast Bash, raw metadata assertions and the existing readiness primitive are conventional. Product optimization, retry frameworks, generated bumps and broad audits remain excluded.

## Correctness and compatibility conclusions

- B1: capture initial shell before inputs mutate and reuse all five later entries; guarded confctl, Codex conditional, dependency/security checks, hooks, lock guard and nonforce push retained. Actual native-gem fixture validates mechanism without claiming moving upstream success.
- C1: trust checked-out plugin locally after configuration signing; neither global trust nor signature enforcement is relaxed. Unsigned/signed/bad-format actual commit fixture verifies repair and rejection.
- E1: one non-login fail-fast declared-shell Bash clears project preload before lock/Bundix; forced source platform, native purity exception and same-Ruby install/hooks/commit retained. Failures cannot report successful update; ordinary push requires commit. Actual bundle generation remains pending.
- F1: eleven expectations now match raw MySQL Column#default returned unchanged by existing helper. Types/nullability/unsignedness/data/nil/rollback assertions preserved. Migration/schema/helper/runtime/API/client bytes unchanged; no client regeneration requirement.
- G1: existing repository updater owns behavior, consumed by existing workflow/local invocation. Shared parity/run_ruff contract retained. Exact-pin helper limits parsed-TOML change and preserves unrelated bytes. Dirty owned inputs/unrelated staged entries rejected. Newly selected environment sync/format/lint and Nix checks precede confined lock/pin staging and generated commit. Existing guarded nonforce publication retained. No runtime requirement or protocol change.
- H1: every22/80/81/443 listener required, including real service for denied port81. Existing bounded wait at setup/restart, prompt setup failure and bounded diagnostics preserving original error. External dual-stack/ICMP/established/zone/restart assertions and units intact. Local listeners do not prove external policy; actual firewalld remains required.

No new cross-project API or reusable framework interface. Actual updater caller, parity check, Python shell/shared Ruff entrypoint and consumer pins inspected. No production ordering, mixed-version change, fleet coordination or persisted-state conversion. Revert each repair for source recovery; future HaveAPI lock+Ruff updates revert together.

## Whole-branch history, migrations and update streams

Each repository has one coherent final repair with no obsolete history or transitional paths. No migrations in any of the six. vpsAdmin spec/migrations files are tests; definitions/schema are byte-identical and have no new merged/released/deployed/external-use lineage.

Only IRC has an action update stream (checkout v6→v7), consolidated in its one workflow repair; no repeated or retained intermediate pin. Other repositories contain no actual dependency/input/generated update stream. HaveAPI unpublished design iteration and published message-only predecessor are absent from final series; source equality and cancellation evidence retained in G1 receipt. No intermediate state/release boundary requires obsolete commits. Separate repositories/causes and tests/rationale with owning behavior are the appropriate commit split.

## Documentation placement and preservation

B1 invariant is next to workflow; individual failure/store/fixture evidence remains session-owned. C1 standard one-line signing needs no separate project page. IRC README→Bundix remains contributor how-to, preserving shell/preload/source-platform/purity facts and existing links/anchors. F1 adapter diagnosis belongs in session evidence without changing raw helper API. HaveAPI Python README→CONTRIBUTING and AGENTS→development procedure are appropriate contributor/maintainer homes; prerequisites, clean index/input, checks, ignored uv.lock, failure/staging/guard/recovery semantics match source. H1 helper/test contract remains authoritative; no KB prose/WebUI/capture/release work.

No docs moved, recovery instructions lost, supported upgrade retired, or permanent rollout receipt introduced. Existing entry points remain useful and checks distinguish prepared from executed. Earlier package snapshots saying no approval are superseded by current explicit approval in state.

## Remaining acceptance and residuals

Quick evidence reviewed, not rerun: B/C actual hook fixtures and workflow checks; E eight stub control-flow scenarios/hooks/exact RSpec; F18changed-file examples locally and hostedMariaDB11.8 plus syntax/style/full-plugin hooks; G13focused Git/stub tests/new Python checks/hooks; H actual generated Ruby/helper and full static contract checks. Stubs and static evidence do not establish runtime acceptance.

Required next: E real generation/native install/hook commit and one no-change pass; G actual coherent locked Nix/Ruff parity and exact runtime gate; F full84migration examples; H one actual firewalld scenario with before/after listeners. Complete before acceptance/integration claims. C/E manual triggers require focused follow-up at successors.

Preserve residuals: separate HaveAPI Rust auth-rendering performance regression, unchanged baseline/budgets; KB upstream GitHub504; H original postrestartSSH failure not yet proven cured; older vpsAdmin general failure followed by success; syslog no retained scheduled runs. No optional audit expansion justified.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-scheduled-workflow-fixes/)
