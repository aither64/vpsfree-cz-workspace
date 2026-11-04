# Application preparation — 2026-11-04

## Current shared-master integration preparation

User approval "merge and activate" is retained by the lead for workspace/master
and aitherdev profile activation; equal-patch refresh does not expand that scope.
**READY: source/review-equivalence preparation, fresh exact three-output batch
and realized final artifact comparison pass.** Lead owns claims,
shared merge/default push and subsequent activation. No such action was performed
by implementer1. The previously built/tested graph remains intact below.

- Fresh remote default: `12a3df65467c7c460cae5e0a3cd8dca60138288e`.
- Exact shared local target: `5840893834f1d76e2bf3401a9d043e588f636442`.
- Final feature: `2b5944e8df2ba06fb3193264c231adafa8329b5c`.
- Final complete series: A `ebf00e3cbea124ce49289afa3d584ac60c9621c2`,
  B `2b5944e8df2ba06fb3193264c231adafa8329b5c`.
- Old reviewed/tested range:
  `12a3df65467c7c460cae5e0a3cd8dca60138288e..59bc3d8f7f59cfe6dc4f4c1cbc67dbad73db8fb5`.
- New complete range:
  `5840893834f1d76e2bf3401a9d043e588f636442..2b5944e8df2ba06fb3193264c231adafa8329b5c`.

Fresh remote is an ancestor of shared target; shared target is an ancestor of
feature. Baseline changes are only work/archive records and one durable notes
Markdown file. No code/policy/lock/machine-identity change occurred. Rebase was
conflict-free; range-diff is `=` / `=` and ordered stable IDs remain
`7a3d2aea7e3c8e189ba2f0c8d314980dd6ce3774`,
`973b4fba3ba512e3eb8c786e45df2d7c60afc8da`. Two focused commits, four feature
files, +140/-24; no obsolete history, migrations or repeated update streams.

### Original review binding and mechanical proof

The installed `workspace-integration-certification.rb` explicitly allows
`work/`, `archive/`, `notes/` as non-behavior incoming paths and requires exact
reconstruction, not patch IDs alone. Original independent reviewer remains
reviewer0, native thread `01a19245-f638-7533-96b7-166d158e3e84`, saved
`gpt-6.1-sol` / `xhigh`. The accepted original report is
[final-refresh-review.md](final-refresh-review.md), SHA-256
`af801ff2593894daadf3d1fb5ff5d5dae8256b911a8b719c36ca37d4eaf5a621`.
Its schema-1 review binding is:

```json
{"schema":1,"decision":"accepted","reviewer":"reviewer0 / 01a19245-f638-7533-96b7-166d158e3e84 / gpt-6.1-sol / xhigh","repository":"workspace","target":"refs/heads/master","base":"12a3df65467c7c460cae5e0a3cd8dca60138288e","head":"59bc3d8f7f59cfe6dc4f4c1cbc67dbad73db8fb5","migrations":[]}
```

Implementer1 independently reconstructed the final full Git tree in a fresh
scratch index: `git read-tree NEW_BASE`, apply the original reviewed binary
diff with `git apply --cached --whitespace=error-all`, then `git write-tree`.
Result exactly equals final feature tree
`8a60019df0cc10a30742f0534180d57d1ed6da44`. The installed policy's independent
`git merge-tree --write-tree --merge-base=OLD_BASE NEW_BASE OLD_HEAD`
reconstruction produces that same tree. Neither operation changed shared master
or the feature's real index. No intermediate deployment needs a lineage bridge.

The exact installed schema-1 proof shape, including complete incoming/changed
paths and empty migration inventory, is retained in
[shared-target-equivalence.json](shared-target-equivalence.json) (10,249 bytes),
SHA-256 `22351a9e426d1dd11622589ed7e7eed2f5ed8ffc3faf5c1e1bbafa5ef02624ee`.
Relation is `reconstructed_patch`. Lead independently verifies this binding/tree
before accepting mechanical review reuse. This is evidence under the installed
policy, not a newly performed independent code review or a new runtime job.

Lead subsequently reproduced the full tree with its own isolated index and
accepted [shared-target-review-reuse.json](shared-target-review-reuse.json),
binding the original reviewer/report/range to the final exact range and proof.
The accepted receipt explicitly says `test_reuse: false`; the fresh utility
`/root/integration_checks` owns the same three-output batch on frozen 2b5944e8.
Its fresh result and realized-output comparison are now complete, as recorded
in the final milestone below.

### Exact verification identity: reuse refused, fresh batch completed

The accepted notes file enters the workspace source filter, changing its source
input from `wwd642llpvq7klnqs8jnhq1gh0q4rakz-source` to
`sj9h2xl6qvs5a198fz2gn61jp52a5j54-source`. Identical code/patch is insufficient:
all three new derivations differ from tested receipts. No successful old result
is relabeled current. Lead's utility ran the same bounded batch on final head:

| Output | Final realized derivation | Verified actual output |
| --- | --- | --- |
| `vpsfree-dev-workspace` | `/nix/store/wxvyrlfx7ik8r8k5ldijk62h0d2752w7-dev-workspace-0.2.0.drv` | `/nix/store/zmyllqw6x1cxk8vhwliy7r11ykd19cz9-dev-workspace-0.2.0` |
| `checks.x86_64-linux.agent-instructions` | `/nix/store/bpq6xw3l55bssc0rfi7sgq2ak5d99jl6-workspace-agent-instructions-tests.drv` | `/nix/store/aix09qb2c2ahc5y5hfp8kibi0gnwv2ax-workspace-agent-instructions-tests` |
| `checks.x86_64-linux.agent-team-policy` | `/nix/store/vxma0g300clkp1v62nfkjlx05p0rjrg1-workspace-agent-team-policy-tests.drv` | `/nix/store/bm96lmx7qhdnsi92apknbmxdhki7xljq-workspace-agent-team-policy-tests` |

No uncertain checks/builds were launched by implementer1. Current locks,
runtime 3bb08df, extension f8da821, machine identity and catalog equal their
immutable reviewed Git source at 59bc3d8f. The earlier copied workspace source
path is no longer materialized; no assumption of its retention was used.
Configuration reference remains clean f4069909 with matching runtime. Selected
profile remains myjy32; typed mapping/bridge is unchanged. No profile/system/
claim/lifecycle action occurred. Publication/comparison and final Git-window
handoff are recorded in publication.md; lead must recheck exact shared target
immediately before its claimed integration.

Final evaluated source/input graph is in
[shared-target-input-graph.json.gz](shared-target-input-graph.json.gz), preserving
the older graph artifact unchanged. It has 3,817 derivations / 472 source
vertices. Compared with the tested graph, only the workspace source vertex is
replaced; only package root and generated extensions JSON derivations differ.
Normalized graph SHA-256 is
`57d45d380e0048b8bdd52ee890c9f0da9f53fe4fae77a77154511a6b05014b3e`;
compressed artifact SHA-256
`3a5e1d23bfcf17d129937a9d20326df50d0f082383d0a69b789b47f9ce6cf5cd`.
Native runtime, catalog and machine-policy inputs remain unchanged.

Git handoff completed by **2026-11-04T20:05:21Z**: explicit feature lease guarded
old remote 59bc3d8f; push succeeded; independent SSH read verifies final remote
feature `2b5944e8df2ba06fb3193264c231adafa8329b5c` and unchanged remote default
12a3df65. Shared local target remains exactly 58408938, worktree/index clean.
Comparison was explicitly captured as 58408938..2b5944e8; no CI runs existed.
Ordinary Nix environment/hooks are prepared, with no bypass. Feature Git/index
window is released. Source preparation is READY for lead's independent
reconstruction acceptance and required same-three-output batch; tested artifact
reuse and final merge/activation verification readiness are not claimed.

### Read-only critical-section preparation — 2026-11-04T20:08:23Z

Repository Nix environment is prepared with ordinary Git 2.54.0:
`/nix/store/5vpcfsdx1lcnlb2y4k7xyc74shp5qwbh-git-2.54.0/bin/git`.
It was resolved by `nix develop --no-update-lock-file --command sh -c
'command -v git; readlink -f "$(command -v git)"; git --version'` outside claims.
No wrapper, hook bypass or source mutation was introduced.

Read-only shared-root preflight: branch master / exact target 58408938, staged
index empty, all four feature paths clean. `core.hooksPath` is unset; root has no
hook framework declarations or active non-sample files in
`/home/aither/workspace/ai/vpsfree.cz/.git/hooks`. Unrelated shared tracking
changes are preserved, not asserted globally clean. Lead still takes its short
repository claim then tries the tracking lock and rechecks fresh exact refs;
this observation is preparation, not ownership or a merge.

Selected application remains myjy32; live system/system profile remain
g1xc1pam and user profile remains zqbf2pf4, with full immutable paths preserved
below. Configuration reference and typed bridge/input compatibility remain as
prepared. No profile change, claim, shared write or default push occurred.

### Fresh canonical ancestry and continuity observations — 2026-11-04T20:16:10Z

Read-only SSH `git ls-remote ORIGIN refs/heads/master` plus local commit and
`git merge-base --is-ancestor` checks establish the following exact snapshot.
All commit objects were already present in canonical repositories; no fetch,
target/ref change or peer checkout/record inspection was needed.

| Canonical SSH origin | Observed approved default | Prepared/source lineage conclusion |
| --- | --- | --- |
| `git@github.com:aither64/vpsfree-cz-workspace.git` | `refs/heads/master = 12a3df65467c7c460cae5e0a3cd8dca60138288e` | Ancestor of prepared shared `5840893834f1d76e2bf3401a9d043e588f636442`, which is ancestor of feature `2b5944e8df2ba06fb3193264c231adafa8329b5c`; remote feature independently equals that final head. Feature is not yet integrated. |
| `git@github.com:vpsfreecz/vpsfree-cz-configuration.git` | `refs/heads/master = f4069909b55fbed907cb658f350ec6a59f97e05a` | Unchanged registered reference f4069909 equals remote default; no configuration feature integration needed. |
| `git@github.com:aither64/dev-workspace.git` | `refs/heads/master = 3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7` | Inherited selected/candidate generic runtime equals approved remote default; local ancestry check passes. |
| `git@github.com:vpsfreecz/dev-workspace.git` | `refs/heads/master = f8da821e3c76e26e73aa9d89a712eab0e0faa319` | Inherited selected/candidate extension equals approved remote default; local ancestry check passes. |

This is dependency lineage evidence, not additional merge scope or proof of a
deployment. Lead retains the fresh exact target and remote checks inside its
short integration claim, and later exact integrated-lineage proof before machine
release. No third-party closure branch inventory was added.

Existing activation observations/checks, derived from canonical runtime 3bb08df
(`nix/systemd/workspace-{router,portal@,codex@}.service`,
`libexec/workspace-host:3675`, `portal/internal/web/server.go:742,952`,
`portal/cmd/workspace-portal/router.go:83`) and actual aitherdev configuration:

```sh
systemctl --user show workspace-router.service workspace-portal@vpsfree-cz.service workspace-codex@vpsfree-cz.service --property=Id,ActiveState,SubState,MainPID,ExecMainStartTimestamp
curl --fail --silent --show-error --unix-socket /run/user/1000/dev-workspaces/vpsfree-cz/portal.sock -H 'Host: vpsfree-cz.workspace.aitherdev.int.vpsfree.cz' http://localhost/healthz
curl --fail --silent --show-error --unix-socket /run/dev-workspaces/router.sock -H 'Host: vpsfree-cz.workspace.aitherdev.int.vpsfree.cz' http://localhost/healthz
systemctl --user show workspace-codex@vpsfree-cz.service --property=MainPID --value
stat -Lc '%d:%i %F' /run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock
readlink -f /home/aither/.local/state/dev-workspaces/profile
```

These are concrete existing read-only checks for the lead's ordinary activation,
not a new fixture/service or a command to restart anything. Each HTTP endpoint
should return `{"ok":true}`. The direct portal read checks the portal; the router
read also exercises hostname routing and its Unix upstream. They do not prove
native App Server responsiveness by themselves. For that, the existing read-only
same-session `GET /api/sessions/2026-10-31-team-workload-parallelization/team-stats`
uses authorized thread activity reads; inspect the lead's available/nonstale
snapshot and ongoing same-session conversation. No new session/turn/probe is
needed. Health curls were identified here, not executed as extra tests.

Observed units were active/running: router PID 371638, portal PID 371750,
native App Server **PID 1906**, started `2026-10-30 23:06:55 CET`. `/proc/1906/exe`
resolves to
`/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0/libexec/codex/bin/codex`.
Its actual listener is
`unix:///run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock`, device 64769,
inode 18744292. Compare the PID/start identity, immutable executable and socket
device/inode after the ordinary compatible switch; portal/router may restart.
The helper's normal launch-policy checks remain authoritative; never force a
restart/refusal bypass to obtain continuity. Source
`workspace-host:2010-2030` explicitly permits only the package-dependent reporting
path change when all remaining native invocation policy remains equivalent.

Actual selected profile symlink above still resolves to myjy32; expected final
candidate is zmyllqw6, pending the fresh utility result. After an authorized
switch, compare the selected output to the realized candidate and read
`share/dev-workspace/package.json` catalog digest (expected unchanged policy
digest `a3f49bd3...`); runtime/claim/native/bridge descriptors must match the
final artifact verification. Do not treat successful HTTP health as that proof.

Saved own-roster baseline from `dev-session team list
2026-10-31-team-workload-parallelization --as-is`: seven members, root thread
`01a19245-d2e7-7d93-a92d-7c440a942e0f`. SHA-256 of address-sorted objects with
fields `address,role,index,threadId,model,reasoningEffort,behavior,purpose,access,instructions`,
serialized by Python `json.dumps(..., sort_keys=True, separators=(',', ':'), ensure_ascii=False)`:
`26ffeea89cee18d5dc52bbb678d01df317ea9e14cabd0324704abda1ad7045ce`.
Recompute that same saved-field projection after activation; omit volatile
activity/state/usage fields. This checks retained members/settings/instructions,
not whether new catalog defaults apply retroactively. No peer roster was read.

### Final preparation completion — 2026-11-04T20:20:56Z

Fresh utility status/result in
[integration-checks-status.json](integration-checks-status.json) and
[integration-checks-result.json](integration-checks-result.json) bind exact
head `2b5944e8df2ba06fb3193264c231adafa8329b5c`, **exit 0 in 698 seconds**,
and all three actual derivation/output pairs in the current table above.
No cancellation, retries, extra targets or old-result reuse occurred.

Actual output zmyllqw6 independently returns deriver wxvyrlfx through
`nix-store --query --deriver`. Its retained complete recursive graph is
byte-identical to the prepared shared-target graph artifact: **3,817 derivations,
472 sources**, normalized SHA-256
`57d45d380e0048b8bdd52ee890c9f0da9f53fe4fae77a77154511a6b05014b3e`.
This proves the realized final graph; the old fa20p0 graph/results remain separate.

Direct output comparison against selected myjy32 verifies byte-identical runtime,
coordination, claim, repository-claim, machine-claim and integration contracts;
coordination/integration catalogs; machine-identity policy and native metadata.
Full relevant hashes remain those recorded in the prior proof below. Native
entrypoint SHA-256 stays
`8da58a478557a971106be8f69fc484fc5777650d1d6aabbdb7feb229f3b3861f` and both
packages invoke the identical immutable native executable
`/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0/libexec/codex/bin/codex`.
Built package/team/extensions JSON exactly matches evaluated generated derivation
text, including actual new catalog digest
`a3f49bd3c1429d2d570cde01d509ae2d65a84c03b896c4265d9b9ccb0e317958`.
No discrepancy, new contract, extra check or independent reviewer was needed.

At the stated observation, selection remained myjy32; live system/system-profile
g1xc1pam and user-profile zqbf2pf4 remained the full exact paths retained below.
This final verification performed no Git command, ref/index/source mutation,
claim, profile/system activation or lifecycle action while lead integration ran.
All remaining preparation ownership is released. **Concrete candidate is READY**
for the lead-owned ordinary activation path after its claimed merge/remote proof
and separate machine ownership. This is not an activation or integration result;
lead retains effect/continuity verification and claim release. Existing command
and dependency-lineage baselines above are available for that work.

## Retained tested preparation on 59bc3d8f

Preparation owner: implementer1. **Preparation complete: reviewed frozen source,
quick/packaged checks, built candidate and final artifact comparison pass.**
Candidate is ready for the lead's separate activation-authorization decision;
ordinary machine ownership and live transition admission remain required.
Refreshed independent review completed without new findings;
see [final-refresh-review.md](final-refresh-review.md). No activation, machine claim, system build/deploy,
or integration has occurred. Refreshed feature publication is recorded below.
Implementation-only
scope is unchanged. The user-profile application route is established in
design.md and configuration's canonical `docs/operations/codex-providers-aitherdev.md`;
no configuration source/channel change is needed.

## Exact source and equivalence

Workspace alias `workspace`, SSH origin
`git@github.com:aither64/vpsfree-cz-workspace.git`, feature checkout
`worktrees/2026-10-31-team-workload-parallelization/workspace`, branch
`2026-10-31-team-workload-parallelization`.

| Range / ordered commits | Identity |
| --- | --- |
| Prior published final range | `aa94433b2c41a17d54f8128b119e33f3289e93ba..4c958a01aeb79f40ca3658e4e759b184e6cf64d8` |
| Prior A / B | `260831af54d39995e033545c54a771e89c4c4908` / `4c958a01aeb79f40ca3658e4e759b184e6cf64d8` |
| Fresh fetched accepted master / frozen refreshed head | `12a3df65467c7c460cae5e0a3cd8dca60138288e..59bc3d8f7f59cfe6dc4f4c1cbc67dbad73db8fb5` |
| Refreshed A / B | `e3a9078b20fc5d373e5dec573de1c3a4e920b07e` / `59bc3d8f7f59cfe6dc4f4c1cbc67dbad73db8fb5` |
| Ordered stable patch IDs, both ranges | `7a3d2aea7e3c8e189ba2f0c8d314980dd6ce3774`; `973b4fba3ba512e3eb8c786e45df2d7c60afc8da` |

`git rebase --onto 12a3df65467c7c460cae5e0a3cd8dca60138288e
aa94433b2c41a17d54f8128b119e33f3289e93ba` completed without conflicts or manual
resolution. Complete-range `git range-diff` marks both commits `=`; ordered
`git show --format= --binary COMMIT | git patch-id --stable` values match.
Combined binary-diff SHA-256 changed from
`6532db9f5f08fc6ce26e630a19822ec10f6a24329ec9917e1470e8096bed45ca` to
`233320923c67b2aed51b3bf6b600ab9ef492e8a3583649d0d25521fce11930b9` because
the baseline inserts unrelated verification guidance before the feature hunk.
Do not call these binary diffs identical.

Both feature ranges contain only the catalog and three guide/procedure files,
two focused commits, +140/-24. **No migrations, obsolete feature iterations or
repeated dependency/generated update streams.** Runtime/extension/machine-identity
changes belong to accepted master, not new feature update commits. Preserve
[final-review.md](final-review.md), [narrow-fix-delivery.md](narrow-fix-delivery.md),
[state.md](state.md) (**Final packaged verification**),
[packaged-checks-status.json](packaged-checks-status.json),
[packaged-checks-result.json](packaged-checks-result.json) and the historical sections of
[final-review-packet.md](final-review-packet.md). Original independent review was
on `aa94433b..b1e8441d`, followed by the documented exact A1 correction. Original
checks certify their old graph only; the refreshed graph requires the lead's
affected review/check decision. Source/head/index remain frozen and clean.

## Selected and candidate graphs

Rechecked selection through the installed coordination guide and stable wrapper:

| Item | Selected | Realized candidate |
| --- | --- | --- |
| Package | `/nix/store/myjy32qh6bd4avgym1awx180y29nvwz9-dev-workspace-0.2.0` | `/nix/store/fa20p0jm04bvzw5wfhh8ymsjrgpypc5j-dev-workspace-0.2.0` |
| Derivation | `/nix/store/gh92nngdvvyynsqgh6b8l2r0rhcig426-dev-workspace-0.2.0.drv` | `/nix/store/p75rk3ppnyp9wnljrx31wrcyw6a7vl7j-dev-workspace-0.2.0.drv` |
| Actual workspace source input | `/nix/store/wx37wyvpzc0jg91imzmla9r3dlwz2s0m-source` | `/nix/store/wwd642llpvq7klnqs8jnhq1gh0q4rakz-source` |
| Catalog digest | `495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7` | `a3f49bd3c1429d2d570cde01d509ae2d65a84c03b896c4265d9b9ccb0e317958` |

Graph proof uses `nix derivation show --recursive`, not package metadata alone.
Selected graph was read from its retained immutable deriver; candidate graph
was evaluated from the exact frozen feature's `#vpsfree-dev-workspace` export,
without building. Each has **3,817 derivation vertices and 472 source vertices**.
The entire source sets differ only by the workspace source above. All 57 changed
derivation vertices per graph are generated native team TOMLs, team/package/
extensions JSON or the package root. All remaining derivations, including native
Codex and machine identity, are identical. Builder/system/arguments also match.

Complete sanitized graph edges, outputs, builders/systems and the full flake lock
are saved in [rollout-input-graphs.json.gz](rollout-input-graphs.json.gz), with no
environment/credential values. Compressed SHA-256:
`b3b0afd0fcc20fde3953a05d3de1b1f504b44c3148c1d3ce09c9e0ed92b8fe10`.
Canonical normalized selected/candidate input-graph SHA-256 respectively:
`d79d72a3cc014cff2936cbb95ee34c69a23338a3268110c3e1741dff4e0dfd2f`,
`7b713fcac6f67e035a2accd698ad10d6a3af58f17e73953c7ce37384d8519237`.
The raw artifact is untracked/disposable; immutable source/deriver identities
and these reproduction commands preserve the durable explanation.

Both actual workspace sources contain the byte-identical **complete 35-node
flake lock**, SHA-256
`28caf178fa143ae40ec86fd80946ed6767dbb05f2356e7bdfa7555cb1f6b8c41`.
Their flake.nix, `.dev-workspace.json`, coordination/integration configuration
and `config/machine-identity.nix` also match. Full source-tree comparison shows
the four feature files plus accepted-baseline `projects.md` entries for Rust/TS
clients; there are no other workspace source differences.

Common actual immutable input roots, independently hashed against locked NARs:

| Input | Source / locked identity |
| --- | --- |
| Generic runtime | `/nix/store/4vkbjz025li2xrsyvhfqkgcnsyw462sd-source`; `3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7`; `sha256-pDaBIdK6uFgVq0Gw7arQLjvIjKsGrKg33IFmwmxnOoo=` |
| vpsFree extension | `/nix/store/y01y2bs4mar8zq9s72npz3lrmlsjvasa-source`; `f8da821e3c76e26e73aa9d89a712eab0e0faa319`; `sha256-U5y/TEny6nsyXWNlCMktmxTZhpVO0QY4kOo/qgwsapM=` |
| codex-web | `/nix/store/qc1pb86d59h49vw9mvadmd5grwvfgl1f-source`; `sha256-Hhh2EYZxKiM1fDfPGxDazhs/ElyOF4q6mMvK5JOUOu0=`; exact revision/edges retained in the common full lock |

At the pre-build stage, candidate evaluation yielded a derivation identity without
realizing/pinning its output or necessarily writing that root derivation into the store. A direct
store-path recursive query refused that unrealized candidate path; querying the
immutable flake graph succeeded. Do not confuse evaluation with artifact proof.
That pre-build limitation is now resolved by the realized artifact proof below;
the historical evaluation/graph receipts remain unchanged.

## Native, compatibility and machine identity

Native Codex remains the identical
`g69s8lglksij04ladjcvpnqqmcqw2ibj-codex-package-0.165.0.drv` in both full graphs.
Selected native package metadata is version 0.165.0, target
`x86_64-unknown-linux-gnu`, layout 1, entrypoint `bin/codex`, unchanged resources/
PATH layout. Native adapter stays `codex-custom-agent-toml` version 1 and capacity
`agents.max_concurrent_threads_per_session = 9`. Catalog names/serialized team
TOMLs change with the catalog digest; retained model/effort/access/instructions
are not rewritten by this preparation.

Installed `share/workspace-portal/runtime-contract.json` SHA-256 is
`c1a1674c51146ea85493b5fd5c55c80119b047fa60a7df91f40ad96d7b27e660`;
it is installed directly from the same actual generic source in both graphs.
It retains lifecycle/recovery, submission, provider, service and live-switch
contracts (`livePackageSwitchPolicy = 1`). This static proof does not establish
live transition admission; the ordinary authorized switch must still check it.

The shared machine-policy derivation is
`xhprf3g8l5xcp20zvvklqmdvl8dap6gs-dev-workspace-machine-identity-policy.json.drv`.
Its output policy SHA-256 is
`ab1f1f8557d5a174ab1f578abfe609aad73a9a5979229a5ad3a743cbe5696be4`.
Profile target remains repository identity
`github.com/vpsfreecz/vpsfree-cz-configuration` / `cz.vpsfree/machines/aitherdev`,
with legacy alias `machine:vpsfree:aitherdev`. Claim record schemas 1/2,
identity version 1 and resolver protocol 1 remain supported. Installed
coordination catalog digest remains
`sha256:0866876d14c76c8750bda045bcf18b39ac8324551eb379ffca8ecb2fe58d7048`.

## Configuration reference and quick evidence

Registered alias/project `vpsfree-cz-configuration`; canonical SSH origin
`git@github.com:vpsfreecz/vpsfree-cz-configuration.git`; own checkout
`worktrees/2026-10-31-team-workload-parallelization/vpsfree-cz-configuration`,
branch `2026-10-31-team-workload-parallelization`, exact clean unchanged head
`f4069909b55fbed907cb658f350ec6a59f97e05a`, fetched remote master. Its
`dev-workspace` channel / `devWorkspace` input selects the same 3bb08df runtime.

- `bin/check-dev-workspace-deployment --workspace-root WORKSPACE_FEATURE
  --configuration-root CONFIGURATION_REFERENCE`, run with Ruby from the
  workspace Nix check environment: **passed**, matching runtime and portal site.
- Public installed confctl protocol-1 adapter, read-only `resolve-machine` with
  exact canonical repository revision f4069909 and selector
  `cz.vpsfree/machines/aitherdev`: **passed**, `sharedLockId: null`. Typed target
  is repository-based; no machine claim was requested or acquired.
- Raw catalog evaluation, full non-instruction equality to fresh base and full
  reviewer/observer role equality: **passed**. Lead bytes: Full 4,023;
  Lead-designed 4,011; reviewed 3,029; Solo 2,807; every role remains <=4,096.
- Existing instructions test via
  `nix develop .#checks.x86_64-linux.agent-instructions --no-update-lock-file
  --command ruby test/agent_instructions_test.rb`: **10 runs / 217 assertions,
  no failures/errors/skips**. Whole-range diff check, local links/workflow anchor
  and peer CLI `bash -n` inspection pass. No new tests or feature edits.
- Ordinary reference checkout initially exited 78 after creating the correct
  branch/worktree because ambient Bundler lacked configured hook gems. Runtime
  source inspection confirmed registration precedes checkout. An idempotent
  `dev-session worktree add ... --base f4069909... --no-fetch` retry succeeded;
  no branch/reset/cleanup was needed. The installed post-checkout hook then ran
  successfully in `nix develop --no-update-lock-file`, without hook bypass or
  source/config changes. Both reference HEAD and cleanliness were rechecked.

Live system and system profile both resolve to
`/nix/store/g1xc1pam59hi7vf648h66zy12dnlgvy6-nixos-system-aitherdev-26.05.20261026.718f670`.
`/home/aither/.nix-profile` resolves to
`/nix/store/zqbf2pf4vpbbwmzrkgbnpy5wc3kmcxmx-user-environment`; the stable
workspace-host wrapper selects the myjy32 application above. These are read-only
observations, not system/profile activation results.

## Final realized artifact verification — 2026-11-04T19:39:39Z

The lead's fresh Luna/low utility completed the exact frozen-head candidate plus
two focused packaged checks with **exit 0 in 667 seconds**, with no retries,
cancellations or additional targets. Read exact receipts in
[candidate-checks-status.json](candidate-checks-status.json) and
[candidate-checks-result.json](candidate-checks-result.json):

| Result | Exact derivation | Actual output |
| --- | --- | --- |
| Candidate | `/nix/store/p75rk3ppnyp9wnljrx31wrcyw6a7vl7j-dev-workspace-0.2.0.drv` | `/nix/store/fa20p0jm04bvzw5wfhh8ymsjrgpypc5j-dev-workspace-0.2.0` |
| Instructions check | `/nix/store/vw22d2yq7866yglhkk9nrhfjkbvn40a3-workspace-agent-instructions-tests.drv` | `/nix/store/gglczakdxxnh366da2xxivq6c9j82c7p-workspace-agent-instructions-tests` |
| Team-policy check | `/nix/store/1zss56x0m8qg8my4q6clhhkzf3s42axs-workspace-agent-team-policy-tests.drv` | `/nix/store/vij7cmy08d5blrh2yiaw4bvpba48aqff-workspace-agent-team-policy-tests` |

`nix-store --query --deriver` independently returned the expected p75rk3
derivation for the actual fa20p0 output. The realized retained recursive graph
is canonically **byte-identical to the evaluated candidate graph**: 3,817 nodes,
normalized SHA-256
`7b713fcac6f67e035a2accd698ad10d6a3af58f17e73953c7ce37384d8519237`.
The complete graph artifact above therefore also describes the realized build.

Direct selected/candidate output comparison verifies byte-identical runtime,
coordination, repository/machine claim and integration contracts, machine-identity
policy, coordination/integration catalogs and native package metadata. In
particular, runtime descriptor hash remains `c1a1674c...`, machine policy
`ab1f1f85...` and coordination catalog `0866876d...` (full hashes above).
The 415-byte native Codex entrypoint is byte-identical, SHA-256
`8da58a478557a971106be8f69fc484fc5777650d1d6aabbdb7feb229f3b3861f`,
and invokes the identical immutable native executable in both packages:
`/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0/libexec/codex/bin/codex`.
Built `package.json`, `agent-teams.json` and `extensions.json` match the exact
evaluated generated-derivation content. Actual new catalog digest is
`a3f49bd3c1429d2d570cde01d509ae2d65a84c03b896c4265d9b9ccb0e317958`;
native adapter version and capacity remain unchanged. No artifact discrepancy
or contract change was found; no extra check or reviewer was launched.

Rechecked live selection is still myjy32, **not** fa20p0. Live system/system-profile
and user-profile paths remain the exact paths recorded above. Configuration
reference stays clean at f4069909. Frozen local head and independent SSH remote
feature both remain `59bc3d8f7f59cfe6dc4f4c1cbc67dbad73db8fb5`, remote master
`12a3df65467c7c460cae5e0a3cd8dca60138288e`; no source/index/ref mutation occurred
during this final artifact step. No migrations/repeated update streams are added.

## Remaining approval actions and authorization boundary

Affected refresh/consumer review completed with no new findings; the original
scope conclusion remains applicable. The utility's candidate/packaged batch and
implementer1's realized artifact comparison are complete. Old test results remain
bound to their original exact derivations; current success has its own exact
input/output receipts, with no reuse based only on tree equality.

Lead still must resolve explicit application activation authority, then follow
the selected package's ordinary machine-claim and profile-switch admission and
verification procedure. The canonical target remains registered repository
`vpsfree-cz-configuration`, adapter `confctl`, selector
`cz.vpsfree/machines/aitherdev`, repository identity
`github.com/vpsfreecz/vpsfree-cz-configuration`; no machine claim is held here.
Workspace/master integration needs separate explicit approval. Preparation does
not authorize either action, and no system deployment is needed for this change.

Refreshed publication was subsequently authorized. The explicit feature-only
lease guarded old remote `4c958a01aeb79f40ca3658e4e759b184e6cf64d8`; push
succeeded and independent SSH proof returned frozen `59bc3d8f7...`. Final
comparison capture matches current base `12a3df65...` and frozen head. No
workflows or branch runs were found; no superseded CI cancellation was needed.
See [publication.md](publication.md) for exact commands/heads. The feature
Git/index window is released; no more rebase without informing the lead.
No default mutation,
integration approval, machine reservation, profile selection, system activation,
roster change, service launch/stop or lifecycle cleanup is supplied by this task.
Any later authorization uses the ordinary selected-package switch and its
forward-recovery rules; no private activation helper or refusal bypass.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-31-team-workload-parallelization/>.

## Approved integration — 2026-11-04

User explicitly directed `merge and activate` in this conversation for workspace
master and application-only aitherdev activation. Lead acquired repository claim
`59e7ac58-665c-4990-a28d-4fa4acd0c90d` (owner
`ad7aeb98-7c28-4d09-944d-2e52745e91ff`), verified held state and took the shared
tracking lock without waiting. Fresh shared target was exactly
`5840893834f1d76e2bf3401a9d043e588f636442`, remote default
`12a3df65467c7c460cae5e0a3cd8dca60138288e`, feature
`2b5944e8df2ba06fb3193264c231adafa8329b5c`. Required normal hooks were prepared;
none active or bypassed. Scoped files were clean, SSH origin and ancestry matched.

Ordinary `git merge --ff-only` completed, then non-force SSH master push succeeded.
Independent SSH proof returned remote master exactly
`2b5944e8df2ba06fb3193264c231adafa8329b5c`. Staged metadata was preserved; unrelated
shared dirt was retained. No intervening tests, repair or cleanup occurred under
ownership. Tracking lock was released; repository claim release and subsequent
authoritative status both report `released`, revision 2, at 20:21:37Z.

This integrates the exact final feature head. Original pre-refresh heads are
retained as reviewed/equivalent history, not called literally merged. Current
source/input graph and actual artifact verification above bind this final source
to built zmyllqw6. No CI workflows/runs are declared. No session lifecycle action
or branch deletion is authorized. Machine ownership and activation follow separately.

## Approved profile activation and verified release — 2026-11-04

After successful integration and released repository claim, lead acquired the
separate schema-2 machine claim `5e6af59b-6ce3-40a8-be11-e1d0572f9729`, owner
`ad7aeb98-7c28-4d09-944d-2e52745e91ff`. Authoritative status was held; typed
verify-machine returned committed config revision
`f4069909b55fbed907cb658f350ec6a59f97e05a` and exact identifier
`machine:github.com/vpsfreecz/vpsfree-cz-configuration:cz.vpsfree/machines/aitherdev`.
No repository resource was bundled with the machine claim.

Lead launched only ordinary `workspace-host switch --source` against the clean
final feature worktree, with exact DEV_SESSION_SLUG/WORKSPACE and
DEV_WORKSPACE_CLAIM_ID. Original command exited 0 in 70.411 seconds. Fresh
Luna/low `/root/activation_watch` observed the parent's original log/status
without launching or retrying the mutation. No operation remains unfinished.
Actual selected package is now
`/nix/store/zmyllqw6x1cxk8vhwliy7r11ykd19cz9-dev-workspace-0.2.0`, actual built
deriver `/nix/store/wxvyrlfx7ik8r8k5ldijk62h0d2752w7-dev-workspace-0.2.0.drv`.
Deployed and final feature head is exactly
`2b5944e8df2ba06fb3193264c231adafa8329b5c`. Complete source/input graph,
mechanical-review lineage, successful exact three-output tests and full artifact
comparison are retained in this receipt's current shared-target sections.

Postactivation verification passed:

- Actual selected profile and selected preset catalog are the expected package
  and digest `a3f49bd3c1429d2d570cde01d509ae2d65a84c03b896c4265d9b9ccb0e317958`.
- Portal and canonical-host router GET /healthz both return `{"ok":true}`.
  Router/portal services are active/running with new PIDs 1789103/1789133.
- Native App Server PID **1906**, original start tick 1149, executable
  `/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0/libexec/codex/bin/codex`
  and socket device/inode **64769:18744292** are unchanged.
- Same-session lead thread `01a19245-d2e7-7d93-a92d-7c440a942e0f` remains working
  with a fresh available activity snapshot (observed age 1,467ms). Existing
  conversation/native process continued; no new probe or test session was created.
- Own address-sorted saved-roster projection remains exactly SHA-256
  `26ffeea89cee18d5dc52bbb678d01df317ea9e14cabd0324704abda1ad7045ce`.
  Saved settings/instructions were not rewritten; new catalog applies to future
  selections, not retroactively to retained teams.
- System and system profile remain
  `/nix/store/g1xc1pam59hi7vf648h66zy12dnlgvy6-nixos-system-aitherdev-26.05.20261026.718f670`;
  user environment remains
  `/nix/store/zqbf2pf4vpbbwmzrkgbnpy5wc3kmcxmx-user-environment`. No NixOS switch.

Fresh independent SSH default proof verified each exact source as an ancestor:

- `workspace` / `refs/heads/master`: deployed source `2b5944e8df2ba06fb3193264c231adafa8329b5c`, remote head `2b5944e8df2ba06fb3193264c231adafa8329b5c`; ancestor verified.
- `vpsfree-cz-configuration` / `refs/heads/master`: deployed source `f4069909b55fbed907cb658f350ec6a59f97e05a`, remote head `f4069909b55fbed907cb658f350ec6a59f97e05a`; ancestor verified.
- `dev-workspace` / `refs/heads/master`: deployed source `3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7`, remote head `3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7`; ancestor verified.
- `vpsfree-dev-workspace` / `refs/heads/master`: deployed source `f8da821e3c76e26e73aa9d89a712eab0e0faa319`, remote head `f8da821e3c76e26e73aa9d89a712eab0e0faa319`; ancestor verified.

Before release, authoritative status for the exact session-owned machine claim
was held. Lead reconciled original command completion, verified deployment
effects, same-native/roster continuity and complete integrated source lineage,
then ran ordinary release without waiting for UI acceptance. Release result and
subsequent authoritative claim-status both report **released**, revision 2, at
**20:27:02Z**. Repository claim was already released at 20:21:37Z. No resource
remains owned; a later deployment requires fresh ownership.

Raw supporting activation-baseline/status/verification/lineage JSON and log are
untracked/disposable; this Markdown preserves the outcome, exact identities and
reproduction/proof contract. No private helper, forced restart, refusal bypass,
rollback, branch deletion, session stop/archive/delete or delayed cleanup was
invoked. Feature and reference worktrees/branches remain. Session remains open.
