# Documentation governance integration and application rollout

Completed 2026-11-09 ~11:35 UTC. All five exact final heads are integrated.
Workspace profile generation229 selects the reviewed candidate7fnhs6zf, updated
skills verified installed, system unchanged/native PID preserved. Typed machine
claim0075 released/status verified11:34:47; no remaining owned resources or
uncertain command effects. Session stays open; no lifecycle action performed.


User authorization: "okay, so proceed with activation & merge", 2026-11-09
current conversation, following explicit explanation of five repo merges and
workspace user-profile app update on aitherdev. No full system or lifecycle
operation authorized. D3 in design.md defines the accepted composition boundary.

## Baseline and preparation

- Profile /home/aither/.local/state/dev-workspaces/profile selected generation228,
  package /nix/store/8p7fs26ja6flmlgc886ddfgpprdkhfjy-dev-workspace-0.2.0,
  deriver /nix/store/ks9kg3a1lrs97sk4q6afl4hwlpgn5v1h-dev-workspace-0.2.0.drv.
- Running system /nix/store/xwldgxzayy9113ljd57ib70vwrbksgp0-nixos-system-aitherdev-26.05.20261026.718f670.
- Active Codex /nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0;
  workspace-codex@vpsfree-cz.service MainPID1309145, portal MainPID4101945.
- D3 matched installed generic d2cb9975 and site f8da821e NAR/source provenance;
  intended generic/site deltas are docs/skills only. Codex-web dd90fb43 and all
  runtime/module/lock/code trees unchanged. Config devWorkspace matching pin is
  required for exact composition contract; no NixOS activation indicated.
- Portal baseline HTTPS curl failed local CA validation before HTTP. Direct exact
  Unix socket /run/user/1000/dev-workspaces/vpsfree-cz/portal.sock with canonical
  Host returned HTTP200 and this session title, no TLS bypass. Use supported local
  transport for health; don't modify trust store for deployment verification.

## Refreshed history

- Generic unchanged reviewed d2cb9975a88079d79f361c5b4c65836ba0835821..
  6587c4c1cedabee95bcc52f4667e7d33e3a82859; stable patch8ca75d38568fe042a8da6a7e2e77c85f85d9785b.
- Site unchanged reviewed f8da821e3c76e26e73aa9d89a712eab0e0faa319..
  0c7168f352f6d4f11c46368e702b9356d81012c6; stable patch72c532a46af4d4982bb9f434040a27c6f271d0f7.
- Workspace old992ce14f..1a3a10d9 → new01c3a7bbd..adc35b7f,
  range-diff equality and stable patch3bd014de698b74825b4edef693439cd8c905cf79;
  preserved shared tracking. Composition pins add a separate final stream.
- OS old4bfed8ba..6154dbcd → new640445ef40cb0daf75ff3b39a79a673f6721b53e..
  14e1c7327d493b212e4c17d3cca053d23883cbba; remote baseline advanced only
  unstable nixpkgs lock. Owner and lead independently proved exact full docs diff
  SHA256738a7cf537b99948314e349180473787c370cd45c914af938bb0801a6d46208c;
  stable patcha069d417ba3f50ddcc5627727626c864b29adb53, no migrations/history residue.
- Configuration docs unchanged9e25b996..f3149765, plus single generated pin commit
  8d040ea216e1524c329abf6fa46691f8c7cdd6ac selects exact generic6587c4c1.
  Sibling graph SHA256 excluding changed node5277a5eb410b169feddec46b7a447c78c6c0c6f4d1c114ac87aeab6ecc1726b3;
  sole node lastModified/NAR/rev changed, all edges/follows/siblings intact.

## Integrations and released claims

| Repository / target | Exact approved final head | Remote proof / claim release |
| --- | --- | --- |
| vpsfree-dev-workspace / master | 0c7168f352f6d4f11c46368e702b9356d81012c6 | FF/push/exact ls-remote ~10:58–10:59; claim a182a705-007d-4c1b-bf1b-202611090070 released and status verified at10:59:07 UTC |
| dev-workspace / master | 6587c4c1cedabee95bcc52f4667e7d33e3a82859 | FF/push/exact ls-remote ~10:59–11:00; claim a182a705-007d-4c1b-bf1b-202611090071 released/status verified11:00:24 UTC |

Both used prepared clean detached target checkouts, fresh feature/remote baseline
checks, normal Git/hook policy and SSH. No claim held across tests/review/records.
Original exact-head CI success remains relevant; default pushes may start routine
CI independently. Remaining source integrations follow final composition review.

## Deployment pending

No machine ownership or profile change yet. Prepare final source/input graph,
app derivation/closure and compatibility checks before fresh typed machine claim.
Then integrate all deployed feature lineage, acquire/verify exact configured
machine cz.vpsfree/machines/aitherdev in registered vpsfree-cz-configuration,
activate ordinary workspace-host switch, verify effects and release promptly.
Uncertain effects keep ownership and ordinary forward recovery; never raw rollback.

## Final composition review and package build

[activation-review.md](activation-review.md) completed with no findings, retained
reviewer0 Sol/xhigh/read_only, all four lanes. Independently confirmed final
graphs, code/host/native equality, old/new docs equivalence and complete history/
no migrations/no superseded streams. Supports profile-only boundary without
waiving candidate admission. OS exact refreshed CI42604952865 passed.

Build operation a182a705-007d-4c1b-bf1b-202611090090 started after review. Exact
workspace894c1ebd, script65c8099b660fee4f9820311cec7f9d5b575b2531dc46e8a3cab8177eab6997f4,
app plus six declared root checks; complete metadata/derivation/closure receipts
under artifacts/. Frozen selected package8p7fs26j, catalogf2d5a890..., Luna/low
full_access; thread01a1c001-935e-79d1-bab3-9c9d53ca589d, receipt
turn01a1c001-98f4-7101-ab11-00dcfd0f3bb1. Lead verified exact source/native policy.
No machine ownership at build start, no duplicate package build.

OS claim0072 held11:12:03, target640445ef→reviewed14e1c732 FF/push/exact remote
proof succeeded; released/status verified11:13:46 UTC. Hook-enabled Nix invocation
unexpectedly realized a small new tool closure before the merge (not a kernel
or source build); by inspection the command had already finished and FF'd cleanly.
No repair or approval wait followed; normal cached offline/no-build push used
active hooks, remote effect known, ownership promptly released. Future critical
sections should use fully materialized direct tool paths to avoid this preparation
gap. No hook bypass or source change. OS final head is literally on remote staging.

Build reassessment ~11:18 UTC: watcher0090 claimed ten minutes at11:17:22,
but exact original script3554778 started11:11:41, Nix3554935 at11:11:42. Treat
actual observed process times as authoritative; no timing-based failure. P5
owner's one bounded log/process snapshot found required rubyChecks.all shards
passing (claims/machine identity/integration/host/coordination/session shards),
no failure/VM/kernel/cache-stall evidence. Generic package mandates complete
shard aggregator; narrower checks cannot replace this exact package build.
No new command/retry/cancel/source fix or claim; watcher retains original run.

P8 prepared /tmp/documentation-governance-p8-target-env outside claims: pinned
Ruby/Git/Nixfmt/SSH PATH + target-local bundle, no Nix evaluation/build/install
or hook bypass. Actual precommit/bundle/Nixfmt checks pass; detached config
target still9e25b996, feature8d040ea2. Later merge critical section uses this
pre-realized environment; no dependency setup under claim.

Supported naming verification boundary: no standalone static-goal nonmutating
naming inference API in exact runtime. Do not create/cancel a session to probe.
Post-profile check exact bundled native0.165.0, naming model catalog hash
049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1
and equality with unchanged codex-web ephemeral_luna_models.json, existing provider
status/native child readiness. No new naming feature/tooling or backend claim.
Original exact-head creation CI+unchanged code supplies prior functional coverage;
final report distinguishes readiness from a fresh naming inference.

## Candidate realized and accepted

Candidate /nix/store/7fnhs6zfm7yn541swmb4hgkj80fqspfi-dev-workspace-0.2.0;
derivation /nix/store/rw76a77sz7s660la3a170p4s1y5agza4-dev-workspace-0.2.0.drv,
NAR sha256-BOUnrtAdcu+P5edCA+rB0XuUhf/KSYyboIHFoJYBWbs=, narSize29985704.
App+all six declared root checks realized, independently nix path-info verified.
Actual original script duration11:11:41→final receipt11:25:20 (~13m39s);
no retry. Watcher native ended without terminal report at11:25:53, original
script/Nix processes verified gone and all ordered set-e final receipts complete.
Runtime resolution0093 accepted11:27:06 with native/process/output evidence.
Aggregate shell exit handle unavailable, historical incomplete report retained;
successful component realization proves checks, no known unfinished effects.

Exact build outputs/graphs: artifacts/activation-package-build.json,
activation-composition-checks.json (6outputs), activation-source-metadata.json
SHA2569c2335022cf64dca870b80f9b2d912e8b678a8f630daed8204867e624f8a60b2,
activation-candidate-derivation.json format2 SHA256
c350e9090130776919c9c1fab809e3646d4a91197c9bef8d68888781b9e0bddc,
activation-candidate-closure.json SHA256
5117d9f86d29105fb620a5a528862ef57a303cf91d37e7a3489a4a7236c7c4f9.
Full graph bound by committed894c1ebd flake.lock; direct drv82derivations+6source
inputs, closure228entries retained. Source metadata ib36aa4c1knakjr4xzdyp3yvh4vni84d
workspace894c1ebd (sparse excluded tracking yields Nix dirty label, Git source
clean/matching final contents checked). Genericpfnyfqh source6587c4c1; sitei251i1
source0c7168f3; codex-webxhjvnra source dd90fb43.

P5 built-content inspection accepted: three intended skill files exact source
bytes, SHA256 respectively9318d5a4f861a328324298472e4cc0712de843a500249afe4b43f146d90c8eec,
94d866d0b3bc622b09cddba938379f8e2e200ba553d9ec47060e5e34b92a3dd7,
1a0690b7ba7ffd3c6a7b3456598336237e867da0f261748752abc8c6ba637440.
Package metadata/catalog52role+1utility configs/runtime contract/machine bridge/
naming catalog unchanged bytewise; wrappers and75site tool files differ only
expected source/self store prefixes, no helper logic/launch option change.
Native package unchanged2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0,
version check succeeded. Ordinary provider readiness status succeeded (scoped
result only; no unrelated session-selection details copied). Profile-only
ordinary activation expected, no hidden system requirement.

## Final source integration

Configuration/master8d040ea216e1524c329abf6fa46691f8c7cdd6ac FF/push/proof
succeeded; claim0073 released/status verified11:28:25. Pre-realized direct
tool/Bundler wrapper used; no dependencies installed under claim, hooks active.
Workspace/master894c1ebd8bbfaf67e96f927c16956a2f79ea7523 FF/push/proof
succeeded; claim0074 released/status verified11:29:33. Claim acquired before
nonblocking .git/dev-session-tracking.lock; held only through checks, merge,
push and remote proof. Unrelated dirty/index state preserved, no staging.
All five exact final feature heads now integrated, original refs retained.
No machine reservation or activation yet.

## Executed activation and final release

Fresh schema2 claim a182a705-007d-4c1b-bf1b-202611090075 held11:30:29 UTC,
owner17e708a8-731b-4b14-a4e3-26f1511535a6; exact configured binding:
canonical origin github.com/vpsfreecz/vpsfree-cz-configuration, repository alias
vpsfree-cz-configuration, selector cz.vpsfree/machines/aitherdev, adapterconfctl,
committed config8d040ea216e1524c329abf6fa46691f8c7cdd6ac. Resource
machine:logical:v1:cb77153513b8abe5862c83655296e6d791660d990494b7f4d037246a0064aa23,
display machine:github.com/vpsfreecz/vpsfree-cz-configuration:cz.vpsfree/machines/aitherdev;
legacy bridge machine:vpsfree:aitherdev unchanged. verify-machine returned exact
claim/source binding before activation. No repository claim bundled or held.

Lead ran ordinary `workspace-host switch --source` with existing owned workspace
feature path, DEV_WORKSPACE_CLAIM_ID0075 and exact verified session/workspace env.
Tool session98048 joined exit0; complete log artifacts/activation-switch.log.
No candidate-private recovery entry, raw profile manipulation or system activation.
Admission verified Codex App Server+semantic observation contracts and0.165.0.
Selected generation228/package8p7fs26j -> generation229/package
/nix/store/7fnhs6zfm7yn541swmb4hgkj80fqspfi-dev-workspace-0.2.0.
Source head894c1ebd, generic6587c4c1, extension0c7168f3, config8d040ea2: same
reviewed/built/integrated graph, no deployment from a nonancestor replacement.

Postactivation evidence before release:
- Profile exact candidate and global ~/.codex plus workspace-private installed
  authoring/review/general-reference hashes match all three source hashes above.
- System remains exact /nix/store/xwldgxzayy9113ljd57ib70vwrbksgp0-nixos-system-aitherdev-26.05.20261026.718f670.
- Codex service MainPID1309145 preserved, same exact native executable/version;
  portal new MainPID4052324, codex/portal/router/coordinator active/running.
- /healthz returns {"ok":true}; own session page HTTP200; exact
  /api/sessions/2026-11-08-documentation-governance-review/details HTTP200, known
  services,5repos, retained currentTarget thread01a1bd4b-eda9-7a61-916d-6dd8f83e0e27,
  correct slug and no pendingLifecycle. Early transient service dependency logs
  during helper refresh cleared; fresh details logged categoryok.
- dev-session current exact bound slug, retained seven member settings/model/effort/
  access unchanged. workspace-host maintenance status returns statusnone.
- Naming childPID4052592 under new portal executes same native2rqwqchj...,
  model_catalog_json points to selected candidate catalog with unchanged
  SHA256049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1.
  Version check0.165.0 and source catalog cmp pass; no naming-unavailable/runtime-
  exited errors in new lifetime. No fresh backend inference/session creation
  performed; readiness+unchanged-source exact CI cover this update's boundary.

Fresh SSH default proofs ~11:33 UTC, all exactly equal final intended heads:
generic/master6587c4c1cedabee95bcc52f4667e7d33e3a82859;
site/master0c7168f352f6d4f11c46368e702b9356d81012c6;
OS/staging14e1c7327d493b212e4c17d3cca053d23883cbba;
configuration/master8d040ea216e1524c329abf6fa46691f8c7cdd6ac;
workspace/master894c1ebd8bbfaf67e96f927c16956a2f79ea7523.
Exact equality independently proves ancestry of all deployed feature lineage.
Original/refreshed ranges and independent equivalence remain recorded above.

Lead inspected authoritative own claim0075 held status, reconciled switch exit0/
no maintenance or pending effects, verified deployment and complete integrated
lineage, released it and verified statereleased at11:34:47 UTC. No separate UI
acceptance or permission wait; no machine remains held. Any later deployment
requires new ownership. All five repository claims already released. Session
open with completed task state; no archival/deletion/stopping/cleanup requested.
