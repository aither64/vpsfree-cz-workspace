# Default-branch integration record

## Explicit approval

On 2026-10-01 the user directed: "merge it into the default branches" and
explicitly defined approval for every affected repository registered to
`2026-09-30-portal-review-improvements` and each configured remote default branch.
The same instruction requires fresh upstream fetches, reviewed patch equivalence
for any rebase, saved final comparisons, fast-forward-only integration, SSH
pushes and exact final-head ancestry verification. The approval covers:

| Registration | Repository | Remote default |
| --- | --- | --- |
| codex-web | aither64/codex-web | master |
| dev-workspace | aither64/dev-workspace | master |
| vpsadmin | vpsfreecz/vpsadmin | master |
| vpsadmin-webui | vpsfreecz/vpsadmin-webui | main |
| vpsfree-cz-configuration | vpsfreecz/vpsfree-cz-configuration | master |
| vpsfree-dev-workspace | vpsfreecz/dev-workspace | master |
| workspace | aither64/vpsfree-cz-workspace | master |

Scope is taken from this initiative's portal.yml, checked against the clean
feature worktrees. Unchanged dependency registrations may already be contained
in their defaults; verify them without inventing a new patch.

Deployment and lifecycle authority are unchanged: z20 remains selected, the
successful profile switch is not retried, shared DNS/configuration deployment
remains unpublished even after its source is merged, and the session remains
open. Preserve all feature refs and unrelated shared-checkout/index changes.

## Pre-integration heads

- codex-web: d210d3f7cc93981d0ab163b1fcf0718f9587f47e
- dev-workspace: 869b8d4728394127ba949dc76724dce56eae136b
- vpsadmin: 5c76e3290481b297dcd0baa76d246133f0353d8f
- vpsadmin-webui: 534caa83a5f97d2b40b4a126886649b14dc9e8d3
- vpsfree-cz-configuration: d24b251531a9a482b8f1b5dd81540da85981189f
- vpsfree-dev-workspace: 074926d33f7306288f7cfad87c6a85e8a430e750
- workspace: cd2875f3d4fb2199dd1992b07a3e664eb901e50f

Roster revalidated: saved architect0 Astra/xhigh/workspace_write, implementer0
Sol/xhigh/workspace_write, reviewer0 Sol/xhigh/read_only, all ready. No settings
override. Prior independent whole-history/migration review is complete; rebased
changes will receive an affected-lane equivalence review before long verification.

## Progress

- [x] Verify session identity and retained roster.
- [x] Record exact integration approval and repository/target scope.
- [ ] Fetch upstreams and classify ancestry for every registration.
- [ ] Resolve required rebases with reviewed patch equivalence.
- [ ] Save final comparisons and verify exact-head checks.
- [ ] Fast-forward defaults, push over SSH and prove remote ancestry.
- [ ] Observe applicable exact-head CI through a fresh Luna/low watcher.
- [ ] Update the durable handoff, retaining deployment/lifecycle holds.

## Fresh upstream and clean rebases

Fetched all seven SSH origins. Two bare clones have no origin.fetch mapping;
explicit default refspecs were fetched for extension and WebUI. WebUI's feature
ref is absent remotely, but its unchanged selected head534caa83 is already an
ancestor of freshly fetched mainaa2f60b8. No patch was invented for it.

| Repository | Fresh default before integration | Disposition / final feature |
| --- | --- | --- |
| codex-web | d210d3f7cc93981d0ab163b1fcf0718f9587f47e | unchanged head already contained |
| vpsadmin | 90184b374ce0a139319b66326a29373b92d8ee93 | unchanged head5c76 already contained |
| vpsadmin-webui | aa2f60b89df65d2f987be48784ed42bab7010833 | unchanged head534 already contained |
| dev-workspace | 7c133c562ac51076c1f45af46e180f8bfbabe836 | FF to869b8d4728394127ba949dc76724dce56eae136b |
| vpsfree-dev-workspace | 6a0a2eb873e7cb376092c74bdf82fc2c51c349da | FF to074926d33f7306288f7cfad87c6a85e8a430e750 |
| vpsfree-cz-configuration | b6f4e231eb50c0373883c578f21c2ed055b95dc3 | rebased to9824c02b657ad394dce6b81ed10abfbf3aed9d0e |
| workspace | b38992f07a759274494bd23b11f8786304c671f4 | rebased toc3b0361cc4e9ad51d58304b833c0e5cdd4c4b27f |

Both normal Git rebases completed without conflicts. Range-diff marks every
replayed commit `=` (configuration1/1 and workspace9/9). Each feature-changed
file's blob equals its reviewed predecessor exactly. Configuration absorbs only
upstream lock updates; workspace absorbs only committed coordination records.
The approved functional patches and exact extension/generic/Codex pins are
unchanged. Existing deployed z20 remains built from old workspacecd287; a new
source identity is not a new deployment. Old published/consumed commit objects
remain preserved; rebasing for the expressly approved current-default integration
does not rewrite remote master or alter deployed packages.

Detailed preflight/equivalence inventories: integration-preflight.json and
integration-rebases.json. Independent reviewer0 is assigned the stabilized
integration ranges before long exact-head verification. Nix parse, lock JSON and
both range whitespace checks pass. Shared checkout's empty staged diff and59
unrelated modified tracked files were fingerprinted before operations; they will
be rechecked after its fast-forward. No reset/clean/stash was used.

## CI direction superseding the earlier wait

The user subsequently directs completion of required pre-integration review and
checks, fast-forward integrations, SSH pushes and remote ancestry proofs without
waiting for post-push CI. After pushes, identify applicable run URLs and their
initial states only. Do not wait for completion or assign a CI-wait watcher.
This supersedes the earlier request to monitor long CI; any required long local
pre-integration verification still uses a fresh Luna/low watcher. Deployment,
DNS publication and lifecycle holds remain unchanged.

## Final comparisons and pre-integration check scope

Saved final comparisons for generic869, extension074, configuration9824 and
workspacec3b against their freshly fetched default bases. The comparison helper
rejects identical base/head for the three unchanged dependency registrations;
their equal initial/head pairs are documented as not applicable rather than
inventing a change. Exact metadata is in integration-comparisons.json.

Prior full browser/Go/flake/build/protocol/cluster smoke evidence remains at its
actual tested heads; generic869 and extension074 have not changed. Required
rebase checks use the declared Nix environments from the fresh detached target
worktrees: workspace agent-instruction/deployment-contract fixtures, and four
rendered configuration DNS zones with named-checkzone. No deployment/build of a
shared DNS host or package switch is part of these checks. The uncertain-duration
Nix shell/check batch will be assigned once to a fresh Luna/low watcher after
independent equivalence review; post-push CI remains report-only.

## Independent integration-equivalence gate

Retained reviewer0 completed general/architecture/risk review at the stabilized
clean heads with no Blocking, Important or Advisory source finding. Independent
range-diff is '=' for configuration1/1 and workspace9/9; every feature-changed
blob equals the reviewed predecessor. Target-relative series/diffs remain coherent
and migration disposition is unchanged: no feature-authored database/persisted
migration, upstream nine API migrations retain their documented unknown production
provenance, DNS serial is operational state and OAuth seed is a runtime action.

The reviewer recommends no new long suite solely for these equivalent rebases.
Its smallest integration gates are final comparison captures (done), final clean/
target ancestry recheck, existing exact-head parse/JSON/whitespace checks, and
workspace package drvPath evaluation because source identity changed. The earlier
prepared broad shell/check batch is NOT launched; prior full suites retain their
actual tested revisions. Four DNS consumer rerenders/builds against rebased
configuration9824 remain prerequisites for any later DNS deployment, which is
held. No deployment or new package-byte identity is inferred.

## Completed integrations and proofs

Normal detached-target fast-forwards and SSH default pushes succeeded:
- generic7c133→869b8d47;
- extension6a0a2→074926d3;
- configurationb6f4e231→9824c02b;
- workspaceb38992f0→c3b0361c.

Fresh SSH fetches then proved all seven exact final feature heads are ancestors
of their configured remote defaults (integration-remote-proofs.json), including
unchanged codex d210, API5c76 and WebUI534. The four product target worktrees and
all seven registered source worktrees are clean. Source refs/worktrees are
retained. Workspace and configuration pre-rebase source heads are also retained
under their own repository tag2026-09-30-portal-review-improvements-pre-integration
for source provenance; this does not authorize an operational rollback.

The workspace package evaluates atc3 to drv ad34hy4q21lj2kppdddj7256glpm6djr
and outputz20g487rcankkgaprsrdya5na079i1rl. This is actual evaluation evidence,
not a newly performed build/switch. Shared master fast-forwarded normally with
59 unrelated modified tracked files byte-identical and the staged diff unchanged.

Configuration's fresh target worktree initially failed its active Overcommit
post-checkout hook because its local Ruby bundle was absent. Fresh Luna/low
integration_config_hook_environment ran the declared Nix/bundle setup once,
status0/76s. The normal checkout, FF merge and both pushes then ran with active
hooks through nix develop; no bypass. The prepared broad rebase check script
was not run after independent review found no new long-suite requirement.

Applicable new master CI was queried once after push:
- Generic Check36904460292: in_progress initially;
  https://github.com/aither64/dev-workspace/actions/runs/36904460292
- Extension Check36904534674: in_progress initially;
  https://github.com/vpsfreecz/dev-workspace/actions/runs/36904534674

No waiting, rerun or dispatch. Workspace has no workflow; configuration has only
scheduled/manual Daily update, so these default pushes do not trigger CI there.
The three unchanged dependency defaults received no new push. Extension's
path-filtered Host migration workflow is not selected by this feature diff.
Exact initial observations are in integration-ci-initial.json.

## Durable handoff and retained operational boundaries

The user explicitly requests the consolidated tracking/handoff commit and push.
Stage only owned records/notes; this checkpoint may extend shared master beyond
the integrated source head without changing product content. Recheck that the
source final heads remain ancestors of remote defaults afterwards. All source
integrations are complete; CI completion is expressly not awaited. z20 is still
selected; DNS publication, system/cluster actions and lifecycle actions remain
held. Temporary clean target worktrees and feature refs are retained.
