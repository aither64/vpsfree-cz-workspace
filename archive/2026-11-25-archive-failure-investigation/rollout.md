# Archive preparation fix rollout

Profile-only deployment completed and passively verified. Root's ordinary switch
on exact workspace30b74 returned0 in162.454s (`15:38:21Z`–`15:41:04Z`), selecting
appapja with unchanged systemk79/nativePID3138515. I's passive reads at
`15:43:45Z`–`15:45:23Z` confirm exact G source/input/deriver graph, four healthy
services, three HTTP200 and retained session/tmux continuity. See
[deployment verification](deployment-verification.md), [deployment evidence](deployment-evidence.md)
and [accepted preflight](deployment-preflight.md). Root owns the held machine claim
51ed48c0 and its final effect/approval/integration/release boundary. No merge
approval or live archive retry is inferred.

Current reusable site guidance is configuration's
`docs/operations/codex-providers-aitherdev.md#deploying-a-change` for application-only
profile selection, and `docs/operations/pi-runtime-aitherdev.md` for the matching
host/application contract. The selected package's installed
`share/dev-workspace/workspace-updates.md` owns transition policy. The historical
coordination guide cited by B is absent from final configuration `6f6cb452` and
does not supply current routing. The parent live-state/effects/ownership bridge
below remains required.

## Frozen prepared heads

| Repository | Base | Final prepared head |
| --- | --- | --- |
| dev-workspace | `91cafd4c0c50ffb7208498a605707c4c3b1b1174` | `f6d60bf87002fb1896599f35f0284743c16d7e6f` |
| workspace | `e7b876f69aca4554d52a3ac19ed097263847ad43` | `30b74dc3278728ab36197e0d2ef2cf76c66cf791` |
| vpsfree-cz-configuration | `9bdb0c68b47ceebde450fcdf018727b382cacc09` | `fdcb0a2c3f6413224a8e32b4b887eaf2ca8ecf81` |

All use this session's branch `2026-11-25-archive-failure-investigation`; D/G own
workspace/configuration, implementer0 owns runtime. Runtime includes installed
two-commit parent lineage above `65544340` plus C. See core-evidence/design for
old/new range equivalence and original independent parent review. D has one pin
commit per repository, no intermediate pins and no migrations.

G's fresh pin ranges replace reviewed workspace `d43347c1..182756791` and config
`d5055ec0..6f6cb452`; originals remain under owned `-reviewed-d` refs and in the
original review/evidence. Both final locks and nontracking source equal reviewed
D. Reproducible complete fresh-tree/generated-pin proof is `verify-g-pins.py` and
`g-pin-reconstruction.json`; full range/history/consolidation provenance is in the
G supplement of deployment-evidence.md. Lead/retained reviewer owns acceptance,
not this reconstruction script.

Application derivation is
`/nix/store/m9pdsbnrrlwkyhp87d3cic5am7c10rbs-dev-workspace-0.2.0.drv`, expected
output `/nix/store/apjaqip0xj9cy297z2wmb8hmfqn2c8x1-dev-workspace-0.2.0`.
E realized and verified the application; root selected it through the ordinary
profile switch. Configuration's exact system output
changes only for confctl provenance relative to parent `9bdb0c68`; functional
payload derivations are unchanged. Exact parent/final system paths and all input
graphs are in deployment-evidence.md and ignored candidate-inputs.json.
Those D6f system paths remain historical: G selects profile-only and does not
evaluate/build an fdcb whole-system generation. Exact immutable reviewed1827 and
refreshed30b74 evaluations agree on app m9pds/apja and composition26hx/nxf0,
with equal complete inputs. `g-artifact-equivalence.json` binds this equality;
E's results for those exact targets remain reusable without a second build.

## Checks and artifact preparation after final review

Lead reports review passed with no findings on frozen f6/1827/6f. E owns the four
related postreview targets below and the single watcher. F does not run or duplicate
them. Use the installed monitor skill and fresh utility policy for any later batch.

Runtime owner, in its own runtime worktree:

```sh
nix build --no-link --print-build-logs .#checks.x86_64-linux.package
nix build --no-link --print-build-logs .#checks.x86_64-linux.session-archive-lifecycle
```

In this session's workspace worktree, prepare the final composed application and
the composition check that validates the retained extension/worker/site catalogs:

```sh
nix build --no-link --print-out-paths .#default
nix build --no-link --print-build-logs .#checks.x86_64-linux.pi-runtime-composition
```

Confirm realized paths equal the evaluated final derivation/output, compare the
installed metadata/launch and retained compatibility contracts, and retain exact
source/input receipts. A changed final source/head requires applicable refreshed
verification/review and comparison capture; never reuse checks from tree equality
alone. Stop an unexpected local kernel build and follow the verification procedure.

### Package E execution

Independent final review passed without findings at the three frozen prepared
heads. Package E (implementer0) launched one related immutable four-target Nix
batch after lead release: runtime package check, isolated archive lifecycle VM,
composed application and site composition check. Evaluated derivations match
the prepared identities above. See [verification evidence](verification-evidence.md)
for exact command, source/input/output identities, fresh Luna/low native utility
and complete log paths. All four targets passed in the original invocation,
exit0,15:04:23Z–15:35:08Z (1845s,30m45s). Actual registered derivations/outputs
match the prepared identities, including app `apjaqip...`; no operation-owned
work remains. The isolated VM script and ordinary QEMU cleanup completed.
Retained compatibility metadata matches the installed package. Accepted G
mechanical refresh reuse still requires its recorded exact derivation/full-input
equality. This changes no activation, freshness or claim boundary below.

## Activation gate and later commands

No activation is authorized by D/F. F's read-only window
`2026-11-25T15:00:35Z`–`15:04:30Z` established parent claim
`6097deba-584b-49c4-9ed9-c3008e09d306` authoritatively released revision2 at14:54:26Z.
Parent deployment/integrated-lineage/joined no-effect recovery receipts match live
profile1zn/systemk79/native2rq and fresh remote defaults. The parent retains a
separate unresolved recovery goal; no restoration is claimed. F's exact receipt
and live helper/service bridge is in deployment-evidence.md. This session still
needs fresh machine-only ownership for any later activation.

Before acquisition, refresh exact selected system/profile/native identities and
the entire deployed lineage. If the parent or another owner selects newer content,
refresh this candidate without dropping it. Resolve final review, required tests,
artifact realization and the profile-only versus exact-system-provenance choice
before acquisition. Builds/copies stay outside machine ownership when supported.

Live helper/template/sudo identities match the parent's host-impact receipt;
targeted host source is unchanged through f6, and the accepted parent→final system
delta is metadata-only. No host mismatch was found; profile-only selection is
supported without building a system solely for provenance. Lead repeats final
authority/claim/freshness/admission checks. If lead chooses exact confctl provenance
publication, prepare from configuration's
Nix shell before reserving the machine:

```sh
confctl build cz.vpsfree/machines/aitherdev
confctl deploy --generation GENERATION --copy-only cz.vpsfree/machines/aitherdev
```

Retain the exact named generation and store output. A profile-only decision may
omit system realization/activation only after fresh parent host/effects proof
establishes the unchanged payload boundary. Do not describe it as deploying the
new system derivation.

Lead requests a fresh schema-2 machine-only claim for registered repository
`vpsfree-cz-configuration`, selector `cz.vpsfree/machines/aitherdev`, adapter
`confctl`. Use exact claim UUID/session/workspace values and inspect held status.
Then verify the committed mapping once for the intended batch:

```sh
workspace-host coordination verify-machine 2026-11-25-archive-failure-investigation \
  --as-is --id CLAIM_UUID --repository vpsfree-cz-configuration \
  --selector cz.vpsfree/machines/aitherdev --json
```

If system activation is required, under that claim use the exact prepared generation:

```sh
confctl deploy --generation GENERATION cz.vpsfree/machines/aitherdev dry-activate
confctl deploy --generation GENERATION cz.vpsfree/machines/aitherdev switch
```

Preserve configured rollback; no reboot. Verify both `/run/current-system` and
`/nix/var/nix/profiles/system` and actual effects before proceeding. Select the
composed user-profile application through the installed ordinary switch:

```sh
DEV_SESSION_SLUG=2026-11-25-archive-failure-investigation \
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
DEV_WORKSPACE_CLAIM_ID=CLAIM_UUID \
  workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-archive-failure-investigation/workspace
```

Candidate admission must preserve original lifecycle/service/cluster/authority and
maintenance gates. A newly present unfinished journal blocks conflicting package
changes; it retains its original command and requires separate exact lifecycle
authorization. No archive retry, helper invocation, stop, delete or cleanup is
part of this rollout. No live archive/revive smoke is authorized.

Verify exact profile and source graph, portal/router/coordinator health, naming,
conversation and tmux continuity. Account for every local/remote command effect.
Initial exact read-only verification commands include:

```sh
workspace-host status
readlink -f /home/aither/.local/state/dev-workspaces/profile
readlink -f /run/current-system
readlink -f /nix/var/nix/profiles/system
systemctl --user is-active workspace-portal@vpsfree-cz.service workspace-router.service workspace-coordinator.service workspace-codex@vpsfree-cz.service
dev-session current
```

These reads establish selection/service status only. Naming and retained
conversation usability still need the supported portal/native read checks under
the lead's driver; do not start or archive a real session as a smoke test.
The supported passive local HTTP checks used by F are:

```sh
curl --silent --show-error --fail --unix-socket /run/user/1000/dev-workspaces/vpsfree-cz/portal.sock --max-time 10 http://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/healthz
curl --silent --show-error --fail --unix-socket /run/user/1000/dev-workspaces/vpsfree-cz/portal.sock --max-time 10 -o /dev/null http://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-archive-failure-investigation/
curl --silent --show-error --fail --unix-socket /run/user/1000/dev-workspaces/vpsfree-cz/portal.sock --max-time 10 -o /dev/null http://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/api/sessions/2026-11-25-archive-failure-investigation/details
```

For passive naming provenance, get the portal MainPID from `systemctl --user show`,
inspect `ps -o pid,ppid,lstart,comm --ppid PORTAL_PID`, resolve the naming child's
`/proc/NAMING_PID/exe` and its owned naming socket, and compare the pinned native
and catalog contract. Do not submit a naming request to prove inference. Actual
conversation sending, new session creation or lifecycle smoke is outside these
reads. The current conversation/HTTP response and preserved native process provide
continuity evidence; ordinary activation preflights remain authoritative.
Keep uncertain/failed activation held and use source-owned forward recovery;
do not roll back to an older profile or edit receipts.

Integration remains separately unapproved. Once deployment/effects are verified
and all deployed lineage is integrated into explicitly approved remote defaults,
lead reads authoritative status for this exact owned claim, releases it promptly
and verifies released status. Release needs no additional UI acceptance and grants
no session lifecycle permission. Ordinary completion still needs exact final heads.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-archive-failure-investigation/


## Approved integration and verified machine release

All three final registered heads are integrated into their approved remote masters.
Root used separate short repository claims and released each before records/CI.
The workspace tracking-only base advance was handled outside ownership; its final
successor is equivalent to the deployed source by the original independent review
and coordinator reconstruction certificate. Do not call old30 literally merged.
Live effects, exact own claim and all five canonical remote roots were checked
immediately before release. Machine20 released16:29:11Z, authoritative state
released/revision2 verified. No unfinished/uncertain command effect remains.
Post-merge exact-head CI completed SUCCESS after release.

```json
{
  "schema": 1,
  "approval": {
    "wording": "ok, merge and release aitherdev",
    "source": "current conversation user message",
    "targets": [
      "dev-workspace/master",
      "workspace/master",
      "vpsfree-cz-configuration/master"
    ]
  },
  "remoteFinalHeads": {
    "git@github.com:aither64/dev-workspace.git": "f6d60bf87002fb1896599f35f0284743c16d7e6f",
    "git@github.com:aither64/vpsfree-cz-workspace.git": "f1741f4982a3bfef710fc3837f8929b3fa4d8f76",
    "git@github.com:vpsfreecz/vpsfree-cz-configuration.git": "fdcb0a2c3f6413224a8e32b4b887eaf2ca8ecf81"
  },
  "deployedProfile": "/nix/store/apjaqip0xj9cy297z2wmb8hmfqn2c8x1-dev-workspace-0.2.0",
  "actualSystemAndProfile": "/nix/store/k79k3l35lnhfikw65zwnacag112w7z9p-nixos-system-aitherdev-26.05.20261121.94c3211",
  "completeInputGraphProof": {
    "profile": "/nix/store/apjaqip0xj9cy297z2wmb8hmfqn2c8x1-dev-workspace-0.2.0",
    "deriver": "/nix/store/m9pdsbnrrlwkyhp87d3cic5am7c10rbs-dev-workspace-0.2.0.drv",
    "runtimeSource": "/nix/store/hh81k6nk1r1x0jhi0v8a1l9d53jr0h4n-source",
    "compositionSource": "/nix/store/cv964n61y041iyi3gp4nb76rgjhnx2nc-source",
    "runtime": {
      "lastModified": 1795617689,
      "narHash": "sha256-JZJQaci1y3dGVSQwHbdHS8X0IDFpyrz+dk3rqntZJOE=",
      "owner": "aither64",
      "repo": "dev-workspace",
      "rev": "f6d60bf87002fb1896599f35f0284743c16d7e6f",
      "type": "github"
    },
    "completeInputsSHA256": "b8498333b3bf949119400d9f808d9150ec6b146af4cd32f1ddfa0f641d728b62",
    "fullLockEqual": true,
    "runtimeContractSHA256": "aa915624b9627cde1e0dc296d0a90247e7e63164e565aa4018d83509fede6e05",
    "packageMetadataSHA256": "d39df2dc4f9d2318ec381f5065ef36aa932c7d1e13c0d5850de74fc80c533a9e",
    "machinePolicy": {
      "legacyAliases": [
        {
          "identity": {
            "kind": "repository",
            "name": "cz.vpsfree/machines/aitherdev",
            "origin": "github.com/vpsfreecz/vpsfree-cz-configuration"
          },
          "resource": "machine:vpsfree:aitherdev"
        }
      ],
      "profileTarget": {
        "kind": "repository",
        "name": "cz.vpsfree/machines/aitherdev",
        "origin": "github.com/vpsfreecz/vpsfree-cz-configuration"
      },
      "schema": 1
    }
  },
  "unchangedBaselineRemoteProof": [
    {
      "repository": "dev-workspace",
      "origin": "git@github.com:aither64/dev-workspace.git",
      "target": "refs/heads/master",
      "selectedHead": "f6d60bf87002fb1896599f35f0284743c16d7e6f",
      "freshRemoteHead": "f6d60bf87002fb1896599f35f0284743c16d7e6f",
      "relation": "exact equality",
      "acceptedParent": "91cafd4c0c50ffb7208498a605707c4c3b1b1174"
    },
    {
      "repository": "vpsfree-cz-configuration",
      "origin": "git@github.com:vpsfreecz/vpsfree-cz-configuration.git",
      "target": "refs/heads/master",
      "selectedHead": "fdcb0a2c3f6413224a8e32b4b887eaf2ca8ecf81",
      "freshRemoteHead": "fdcb0a2c3f6413224a8e32b4b887eaf2ca8ecf81",
      "relation": "exact equality",
      "acceptedParent": "9bdb0c68b47ceebde450fcdf018727b382cacc09"
    },
    {
      "repository": "vpsfree-dev-workspace",
      "origin": "git@github.com:vpsfreecz/dev-workspace.git",
      "target": "refs/heads/master",
      "selectedHead": "bf12ac71a8a00b1581eed5352f99c1b2daaeff5b",
      "freshRemoteHead": "bf12ac71a8a00b1581eed5352f99c1b2daaeff5b",
      "relation": "exact equality",
      "acceptedParent": null
    },
    {
      "repository": "codex-web",
      "origin": "git@github.com:aither64/codex-web.git",
      "target": "refs/heads/master",
      "selectedHead": "2547d535eefd4154afef4125ea0fb76e5894a8b6",
      "freshRemoteHead": "2547d535eefd4154afef4125ea0fb76e5894a8b6",
      "relation": "exact equality",
      "acceptedParent": null
    }
  ],
  "workspaceLineage": {
    "deployedBase": "e7b876f69aca4554d52a3ac19ed097263847ad43",
    "deployedHead": "30b74dc3278728ab36197e0d2ef2cf76c66cf791",
    "finalBase": "97bf6db040d35ac10be0a5a9302ecb5c4c037df7",
    "finalHead": "f1741f4982a3bfef710fc3837f8929b3fa4d8f76",
    "relation": "independently proven patch-equivalent successor; old deployed head is not literally merged",
    "stablePatchID": "3a3e8dcf13db76da2ba49e602f41c2e616ba76b6",
    "wholeTreeReconstructed": true,
    "completeActualDerivationsEqual": true,
    "fullLockGraphEqual": true,
    "reviewCertificate": "workspace-final-refresh-review.md",
    "migrations": []
  },
  "effects": {
    "ordinaryActivationExit": 0,
    "sourceHead": "30b74dc3278728ab36197e0d2ef2cf76c66cf791",
    "activationProcessesAbsent": true,
    "maintenanceComplete": true,
    "continuationsSettled": true,
    "restorationCompleted": true,
    "finalLiveProfileAndSystemChecked": true,
    "nativeUnchanged": true,
    "fourServicesActive": true,
    "healthz": 200,
    "uncertainCommandEffects": false
  },
  "freshRemoteCheck": "Five canonical SSH master refs checked immediately before machine release: runtimef6, workspacef174, configfdcb, extensionbf12, codex-web2547; all exact equality",
  "machine": {
    "claimId": "51ed48c0-8052-4e9b-ad36-399562a20020",
    "ownerId": "b6290bcd-8006-434c-a1c8-8c3140699c31",
    "canonicalTarget": "machine:github.com/vpsfreecz/vpsfree-cz-configuration:cz.vpsfree/machines/aitherdev",
    "legacyAlias": "machine:vpsfree:aitherdev",
    "typedBindingSource": "fdcb0a2c3f6413224a8e32b4b887eaf2ca8ecf81",
    "stateBefore": "held",
    "stateAfter": "released",
    "revisionAfter": 2,
    "releasedAt": "2026-11-25T16:29:11Z",
    "authoritativeReadAfterRelease": true
  },
  "repositoryClaims": {
    "51ed48c0-8052-4e9b-ad36-399562a20030": "released",
    "51ed48c0-8052-4e9b-ad36-399562a20031": "released after local-only FF and before stale tooling preparation",
    "51ed48c0-8052-4e9b-ad36-399562a20032": "released after no-mutation stale shared-base preflight",
    "51ed48c0-8052-4e9b-ad36-399562a20033": "released after config SSH publication/proof",
    "51ed48c0-8052-4e9b-ad36-399562a20034": "released after workspace SSH publication/proof and tracking unlock"
  },
  "postMergeCI": {
    "run": 45651730877,
    "workflow": 354263807,
    "head": "f6d60bf87002fb1896599f35f0284743c16d7e6f",
    "status": "completed",
    "conclusion": "success",
    "url": "https://github.com/aither64/dev-workspace/actions/runs/45651730877"
  },
  "lifecycle": "Session remains open; no archive/delete/stop/cleanup or original failed-archive retry."
}
```
