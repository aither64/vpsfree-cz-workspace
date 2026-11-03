# Advisory corrections — integrated and devcluster released

The user explicitly directed “merge” for the prepared five-repository target
set and then “also stop & release the devcluster”. Both requested operations
are complete. No production deployment, session stop, archive or deletion was
performed. Feature refs and feature worktrees are retained.

## Actual integrations

| Repository | Target | Exact remote final head | Released claim | Released at UTC |
| --- | --- | --- | --- | --- |
| security-advisories | 2026-07-13-security-advisory-automation | 0b771120bb2a878c012512b685208124c2b4263b | 30c995bb-b27f-411c-a9d8-4c794a86b20d | 2026-11-03T13:44:20Z |
| vpsadmin | master | 942c6eaed41331f823d8e0f670ed239e2b308440 | bed6c6e6-14ad-4843-9478-397a1a44bd68 | 2026-11-03T13:44:40Z |
| vpsadmin-webui | main | 1c8478bceb3943645ec06ccde895ee4b0985873f | 54735573-3f98-49a8-9bdc-10fbdb4c40bc | 2026-11-03T13:45:07Z |
| vpsfree-kb-contracts | master | f97785c2c265172a4c78893e0673034fde56e4dd | e3143d5e-7599-4240-9d53-33ca1c5aa09d | 2026-11-03T13:45:46Z |
| vpsfree-cz-configuration | master | c4107822060e9e34b24a83950d618c9f28a7722b | 0dac9e96-6474-42e5-a56b-1e550b0374e7 | 2026-11-03T13:46:01Z |

Each target/default and feature head was unchanged at the fresh critical check.
Lead entered the prepared declared Nix environment before acquiring ownership,
then acquired/verified only that repository, checked exact heads/clean detached
target, performed git merge --ff-only and normal non-force SSH push, verified
the exact remote target and retained feature ref, and released immediately.
No merge commit, default force push, hook/signature bypass or source rewrite.
Git trace2 hook-exit evidence and actual merge/push outputs have no hook failures.
Full reviewed base-to-head series, immutable trees and no-migration/consolidation
conclusions were checked before the batch; no rebase/input refresh was needed.
The canonical KB common Git is repos/vpsadmin-kb-captures.git while its registered
repository/origin is vpsfree-kb-contracts; the claim binds both correctly.

All five claim-status reads now show released; no active claim, job or machine
reservation remains. No claim was held during environment preparation, cluster
shutdown/release, CI, records or cleanup. PR122 auto-merged at2026-11-03T13:45:04Z,
mergeCommit1c8478bceb3943645ec06ccde895ee4b0985873f. No GitHub merge action or
branch deletion was used. Fresh host metadata confirms feature refs remain.

## Explicit devcluster release

The selected public provider documents Stop as retaining disks/configuration,
and portal Release as stopping and removing them. Its supported CLI equivalent
of full Release is reset. Architect0 independently inspected that owner contract;
lead read the applicable guidance and executed only public bound-session commands:

```sh
/home/aither/bin/vpsadmin-devcluster stop 2026-11-01-published-advisory-corrections
/home/aither/bin/vpsadmin-devcluster reset 2026-11-01-published-advisory-corrections
```

Both exited0. Redacted status before:foundtrue/running/readytrue/single/bridge.
After stop:foundtrue/stopped/readyfalse. After full release:foundfalse. The exact
session preview's saved disks/configuration were removed as requested; shared
provider certificates/SSH infrastructure, records, worktrees and feature refs
were not removed. No private lifecycle helper, manual process kill/removal,
archive/delete/session-stop, production host action or other cluster operation.
The DEV preview links are historical and no longer running.

## Execution and retained evidence

Lead-owned original driver and one fresh observation-only utility both exited0.
Actual observer01a1a1a3-fc8c-7ca3-9736-3dc95d217605, catalog495e Luna/low,
native dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96/fullaccess-never.
The actual banner was verified, --disable multi_agent showed false, and the
policy gate was released before lead launched the mutation driver. The watcher
observed only original status/logs; it did not run a claim/merge/cluster command.
Selected package0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0 and its
coordination guide/catalog b17a5618... were read before acquiring any claim.

Private execution root:
/tmp/2026-11-01-published-advisory-corrections-merge-20261103T132728Z/.
It retains manifest/reviewed-history, per-repository request/claim/status/merge/
push/SSH proof/Git trace records, claims-final.json, cluster-release.json and
only whitelisted cluster status, plus observer policy/banner/result/exit.
Existing [source review](admin-pagination-final-review.md), [input evidence](visibility-verification.md),
[API/KB preparation](integration-preparation-implementer0.md) and
[client/modern/config preparation](implementer1-integration-preparation.md)
retain exact ranges, full source/input graphs, actual runtime/guest system store
paths and verification limits. Old nonancestor deployed preview sources are
historical/equivalent-lineage evidence, not literal ancestor claims.

## Post-merge status and remaining boundary

One useful snapshot after release, no waits/retries/new tests:

- Client default RuboCop41647013760 and RSpec41647013747 SUCCESS.
- API master RuboCop41647065600/PHPUnit41647065014/i18n41647065167 SUCCESS;
  CI41647065275 in_progress, API Specs41647065023 queued.
- KB master Managed41647235594 in_progress; Check41647235548 queued.
- Modern main CI41647131321/smoke41647131106/broad41647131208 queued;
  retained exact-head pre-merge checks remain successful.
- Config exact-head CI listing empty; no hosted green claim.

These new automatic runs are not described as green and do not relabel prior
results. Exact942c pre-mergeCI passed; final local strictKBf977 and admin3cases
passed, successful other native/API results have independently reviewed input
reuse. Originalf977 Managed failure was the Ubuntu apt-mirror transport setup,
before firewall assertions; user explicitly accepted it out of scope. Its11
successful scripts/5KVM proof, unknown deeper mirror/egress cause and failed job
remain recorded. The UFW follow-up was withdrawn before launch. Other original
unknown causes/duplicate-utility limits remain historical residuals.

All requested merge/release actions are complete. The session stays open; no
production rollout or advisory data edits are authorized. A later deployment
needs its own source/consumer ordering and machine reservation. Existing privacy,
six-guard consumers, no mixed API pool and backup-only deletion recovery remain.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/
