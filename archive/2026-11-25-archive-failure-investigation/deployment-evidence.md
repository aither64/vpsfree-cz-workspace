# Candidate preparation evidence

Package D, implementer1. Preparation only; no activation, machine claim, default
integration, live lifecycle action or peer mutation is authorized by this package.

## Current result

G freshness successors are workspace `30b74dc3278728ab36197e0d2ef2cf76c66cf791`
on `e7b876f69aca4554d52a3ac19ed097263847ad43`, and configuration
`fdcb0a2c3f6413224a8e32b4b887eaf2ca8ecf81` on
`9bdb0c68b47ceebde450fcdf018727b382cacc09`, both published/clean. Original reviewed
D ranges below remain immutable evidence; G's supplement records the successor.

Final generated selection updates are committed and SSH-published. Both owned
worktrees are clean; fresh remote branch heads equal local heads. Runtime
`f6d60bf87002fb1896599f35f0284743c16d7e6f` preserves installed parent `91cafd4`
plus C's unchanged patch. The earlier `e50f54d` core range was never selected.
Independent final review and longer verification remain pending; no build or
deployment result is claimed.

| Repository | Owned worktree under `worktrees/2026-11-25-archive-failure-investigation/` | Initial base/head | Branch |
| --- | --- | --- | --- |
| workspace | `workspace` | `d43347c1fd4f9ff9dfdf5c19f6cccb9531bbd639` | `2026-11-25-archive-failure-investigation` |
| vpsfree-cz-configuration | `vpsfree-cz-configuration` | `d5055ec0b2ea22de976f6703208f5526c3e185ca` | `2026-11-25-archive-failure-investigation` |

Initial heads were freshly fetched origin/master. Workspace routing/AGENTS at its
base has no differences from the procedures already read in the shared checkout.
The shared checkout, plan/state and peer worktrees remain untouched. Registration
tools updated this session's portal normally.

Complete final D histories and diffs:

| Repository/range | Entire commit list | Final diff |
| --- | --- | --- |
| workspace `d43347c1..18275679109c2adda4084af1ea7474e21be98b4e` | `18275679109c2adda4084af1ea7474e21be98b4e` inputs: select archive preparation fix | `flake.nix` nested URL + `flake.lock`; 5 insertions/5 deletions |
| configuration `d5055ec0..6f6cb452e17ca663114a07013a0402ef85a7fee3` | `6f6cb452e17ca663114a07013a0402ef85a7fee3` inputs: set devWorkspace to f6d60bf8 | `flake.lock` only; 3 insertions/3 deletions |

Each selection stream has one consolidated final commit; there are no superseded
pins, transitional compatibility paths or migrations. Neither D branch has been
integrated, deployed or externally consumed by this package. No rebase was needed:
fresh target fetches before updates still matched both initial bases. Comparison
captures bind the exact base/head pairs above. Workspace origin is
`git@github.com:aither64/vpsfree-cz-workspace.git`; configuration origin is
`git@github.com:vpsfreecz/vpsfree-cz-configuration.git`, both target `master` only
after separate explicit integration approval. No PR workflow is required.

## Installed composition to preserve

See [accepted preflight](deployment-preflight.md) for exact selected profile,
system, immutable source and graph paths. Installed runtime `91cafd4` contains two
published feature commits above `65544340`; complete source tree is
`f3bff8f5008ade6561a92856eec22a25ac48488c`. Immutable composition source
`/nix/store/csv89jnlh1zrbi9xff9ahmkzjsg6zmgf-source` locks it with extension
`bf12ac71a8a00b1581eed5352f99c1b2daaeff5b` and codex-web
`2547d535eefd4154afef4125ea0fb76e5894a8b6`. Preserve sibling inputs/follows,
site, catalog, native package and retained runtime/claim/cluster/service contracts.

Architect-owned design records original ordinary parent review and exact graph
receipts. `/tmp/pi-d13-91ca-mechanical-pin-review.json` proves the original
workspace/config pin reconstruction and patch-equivalent workspace successor;
this is reference evidence, not permission or proof of completed activation.
No parent source, branch, record, claim or runtime has been modified or contacted.

## Hook and environment preparation

- Configuration worktree add created the intended branch/checkout, then exited78
  from existing post-checkout Overcommit because ambient Ruby lacked Gemfile.lock
  gems. Its effects were inspected before retrying; no branch reset/recreation.
- Declared `nix develop --no-write-lock-file` prepared ignored local gems. Ruby
  3.4.12, `bundle check`, Overcommit0.76.0, confctl and nixfmt were verified.
  Existing hook framework was installed/signed; post-checkout hook passed without
  disabling hooks. Tool log: `/tmp/archive-failure-d-config-hooks-verified.log`.
- The installed dev-session wrapper uses Ruby3.4.9; invoking it inside configuration's
  Ruby3.4.12 GEM_PATH fails on the JSON native extension. Idempotent registration
  was therefore run outside that Nix shell and succeeded. Subsequent configuration
  commits/confctl still run in the declared shell with ordinary hooks.
- Workspace declares no hook framework or active pre-commit/pre-push hook.
- One related environment setup was monitored in parent because installed watcher
  maximum1 was occupied by C's native check. It exited0; no surviving setup process.
  Log: `/tmp/archive-failure-d-config-env.log`.

## Planned final validation and history

The following quick checks completed:

- Workspace updated its existing direct nested URL and ran
  `nix flake update vpsfree-dev-workspace/dev-workspace` (exit0). Only runtime node
  `dev-workspace` changed. Full final lock equals the installed immutable composed
  lock with only that node replaced, including unchanged sibling/follows paths.
- Configuration ran in its Nix shell:
  `confctl inputs channel set --commit dev-workspace devWorkspace f6d60bf87002fb1896599f35f0284743c16d7e6f` (exit0).
  Only node `devWorkspace` changed. Ordinary Nixfmt precommit and commit-message
  hooks passed; generated width warnings were retained under repository rules.
  Log: `/tmp/archive-failure-d-config-pin.log`.
- `bin/check-dev-workspace-deployment --workspace-root WORKSPACE --configuration-root CONFIGURATION`
  passed for the canonical site and exact final runtime. Complete locked runtime
  identities agree in both graphs. `git diff --check` and script syntax passed.
- `ruby test/deployment_contract_test.rb`: 4 runs, 19 assertions, zero failures,
  errors or skips. Log: `/tmp/archive-failure-d-deployment-contract-test.log`.
- Both feature pushes used SSH; fresh `git ls-remote` proved exact final equality.
  No branch push CI applies: workspace has no workflow; configuration has only
  manual/scheduled daily update. No CI was started or awaited.

Final runtime NAR: `sha256-JZJQaci1y3dGVSQwHbdHS8X0IDFpyrz+dk3rqntZJOE=`.
Full lock graphs and bounded host-delta evidence are in local, Git-ignored,
untracked `candidate-inputs.json`. Lock SHA-256 values:

- Workspace: `f411b1b56173b128a85d4c18a17869d12d9eca4add6ba1b2a843ab8b6c426919`.
- Configuration: `8f3738f6c1f9a583fc4692cb0f67de4a9db7e46dbccb896bcdb021d09546b0f3`.

`nix eval --no-write-lock-file --raw .#packages.x86_64-linux.default.drvPath`
on final workspace head evaluates to
`/nix/store/m9pdsbnrrlwkyhp87d3cic5am7c10rbs-dev-workspace-0.2.0.drv`, output
`/nix/store/apjaqip0xj9cy297z2wmb8hmfqn2c8x1-dev-workspace-0.2.0` (not realized
here). Its source is `/nix/store/hh81k6nk1r1x0jhi0v8a1l9d53jr0h4n-source`.
Before/after-commit evaluations give the same derivation. Both derivations refer
to identical immutable package-metadata, catalog, model/provider and machine-policy
source paths; the runtime contract was compared byte-for-byte to installed;
native Codex remains `/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0`
and worker remains `/nix/store/y3a1wlsbp8gj3j5raq7b9nm806a4fpvc-dev-workspace-pi-worker`.
This proves candidate selection compatibility, not activation/effect completion.
The generated extension/coordination descriptors differ only by expected roots:
runtime `vp5r16...` → `hh81k6...`, workspace `csv89...` → `cv964...`, extension
tools output `m399w4...` → `fjr83w...`. Exact substitutions reconstruct the final
descriptors; command/provider/skill identities, adapter protocol and policy remain
unchanged. The final tools output is
`/nix/store/fjr83w57f3m5rvljszpwhgl7n33fm9b9-vpsfree-dev-workspace-tools-0.1.0`.
The unchanged extension source graph acquires this output through its runtime
dependency; do not confuse a generated executable path change with a source pin
or capability change. Raw descriptor deltas are local files
`/tmp/archive-failure-d-dev-workspace-{extensions,coordination}-delta.json`.

## Effective host boundary

Quick evaluation used
`nix eval --no-write-lock-file --raw .#confctl.toplevel.m_cz_vpsfree_machines_aitherdev_0b1e0938.drvPath`;
the parent used the same attribute from
`git+file:///home/aither/workspace/ai/vpsfree.cz/repos/vpsfree-cz-configuration.git?rev=9bdb0c68b47ceebde450fcdf018727b382cacc09`.

| Configuration | System derivation | Expected output |
| --- | --- | --- |
| Parent `9bdb0c68` | `/nix/store/810hcsq90pyl6d47jvf9j6g0fidjwj5z-nixos-system-aitherdev-26.05.20261122.0dc498b.drv` | `/nix/store/y0fizvwzkgilnf9jmi6hc6hi0fsvb9bq-nixos-system-aitherdev-26.05.20261122.0dc498b` |
| Final `6f6cb452` | `/nix/store/fggpznza8b0p7cssamc1rw65vp3bapc4-nixos-system-aitherdev-26.05.20261122.0dc498b.drv` | `/nix/store/9s87mgyc089m143xxy3sd5i7gqqxfmcc-nixos-system-aitherdev-26.05.20261122.0dc498b` |

Every differing dependency was followed recursively with `nix derivation show`:
five paired derivations, system → activate/etc → two confctl metadata files.
Leaves change only configuration revision `9bdb0c68` → `6f6cb452` and runtime input
revision `91cafd4` → `f6d60bf` (plus its timestamp/short revision). Builder/args,
input sources and every other dependency are unchanged. Thus the exact toplevel
changes for provenance while host/service/kernel/native payload derivations do
not. Raw delta: `/tmp/archive-failure-d-host-derivation-delta.json`.

This supports a profile-only boundary relative to the parent configuration
candidate, subject to lead/architect decision and fresh parent deployed-state
proof. It does not establish equivalence to the older live `109d789` system or
certify the parent's activation/effects/release. No system was built or activated.
If final execution requires exact confctl metadata publication, use the prepared
system route after review rather than claiming literal derivation equality.

Lead reports final review passed with no findings on frozen runtimef6/workspace1827/
configuration6f. E owns the four postreview artifact/check targets and its single
watcher; D/F do not duplicate them.

## F: fresh live host and parent-effects bridge

Read-only window: `2026-11-25T15:00:35Z`–`15:04:30Z`. Own session/environment
identity matched. Parent ordinary sensitivity marker was checked absent before
retaining bounded receipts. No peer contact, mutations, recovery, resource control,
lifecycle actions, builds or repeated E checks. Reviewed heads remain frozen.

Authoritative `workspace-host coordination status --json` reported parent claim
`6097deba-584b-49c4-9ed9-c3008e09d306` **released**, revision2, updated
`2026-11-25T14:54:26Z`, owner `81918fa7-e729-4d43-afa3-068c9ce7ccb9`, exact
configuration9bdb/aitherdev typed binding. The installed host wrapper supports this
global status read, not its attempted direct `coordination claim-status` entry;
no peer identity was adopted to work around that CLI boundary.

Parent `state.md:2026` and updated rollout header record switch exit0/125s,
profile1zn, unchanged systemk79/native PID3138515, exact8/8 Pi worker identity
tuples, four active services and three HTTP200. Its later saved recovery returned503
before reservation/Stop/Load/clear/Publish. That command and both bounded diagnostics
were joined and reconciled with no durable/process effects; original hold persists.
This is an unresolved separate recovery goal, not successful restoration or an
uncertain deployment effect.

Bounded parent receipts:

| Path | SHA-256 |
| --- | --- |
| `/tmp/pi-d13-deployment-verified.json` | `2615267e251535ee4952e59d40ca6e60a49db1ec7ac8df631c7b44c2baa3ab25` |
| `/tmp/pi-d13-integrated-lineage.json` (14:54:06Z) | `1d6acfbf2100e60fde47078777a5c73bff9637437396d3961bdf1d0eb6852eee` |
| `/tmp/pi-d13-machine-released-status.json` | `360a6736f65f9200bef9740e45c0eebe6368b738cf0a77e43a6a6d9d07294487` |

Fresh SSH remote reads returned runtime master91cafd4, configuration master9bdb0c68
and workspace mastere7b876f6. Deployed workspace9d302f8f has the independently
proved patch-equivalent successore7 with exact app+5-check derivation/output
equality; it is not literally an ancestor. Parent approval/release applies only
to its batch. This session still needs its own integration approval and fresh claim.

Fresh live identities match that deployment checkpoint:

- System and system profile both remain
  `/nix/store/k79k3l35lnhfikw65zwnacag112w7z9p-nixos-system-aitherdev-26.05.20261121.94c3211`,
  effective configuration109d789/runtime host rolef3bd843.
- Application remains `/nix/store/1zn1a51qrsin83fszrprdjp45208vsj4-dev-workspace-0.2.0`;
  portal PID3106725 executes its `bin/workspace-portal`. Native PID3138515 executes
  `/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0/libexec/codex/bin/codex`.
  Portal/router/coordinator/Codex services are active/running (router3106646,
  coordinator3106754).
- Pi helper/entry remain `/nix/store/xhc71rg58zl44927y9j43s2l23f1r606-workspace-pi-host`;
  host parser SHA-256 `85334aded975ddb79967b2d5048696052bbe56aa2ddddfe557c49ac04e35e448`.
  Actual template is `/nix/store/8q48nsnsf05ps2k23n6j4kfl90k8h789-unit-workspace-pi-session-.service/workspace-pi-session@.service`,
  SHA-256 `ab1a2af2dc8687be361e28f8084c982cd9a21942ff76372f5481a0f28ff29281`.
- Live sudoers source `/nix/store/33scrpdrij5hyx7bk4ssxl9q5gmhxfjv-sudoers` hashes to
  `1bd17db15f97554abe2b957a76fa2fdde955432059aa0e11cf51a36c5208e7c8`.
  Current portal drop-in selects Pi host state root
  `/home/aither/.local/state/dev-workspaces/pi-runtime-host` and auth directory
  `/home/aither/.pi/agent`, preserving ExecStart.
- Portal-owned naming child PID3107017 executes the same native binary and has
  its owned socket under `naming-1727971747/app.sock`. Passive `/healthz`, this
  session page and this session details each returned200 through the local socket.

Parent `D1-host-impact.json` (SHA-256
`2af3ddc5149f6ace966a34eede6b975edce494f66eae72ba3e98fc427ee0ce68`) binds that
same live system/configuration to the exact helper/template/portal host contract,
full sudo bytes and rule order. Fresh helper/template/sudo identities match its
concrete artifacts. Targeted
`git diff --name-only f3bd843..f6d60bf -- nix/host-module.nix nix/pi-runtime-host.nix nix/pi-runtime-host-package.nix libexec/workspace-pi-host`
is empty. Live ownerUID1000, state root, service mount/kill policy and host capability
schema1/launcher1/request1/handshake1 align with the unchanged candidate contract
`bin/workspace-portal pi-runtime supervise`. The installed app manifest SHA-256 is
`841e817260b56dbb35255094dd9170f1b59930066643231e8ad82822d0f79451`.

This concrete bridge plus accepted parent9bdb→final6f6 metadata-only evidence
supports profile-only activation; no functional host mismatch or host build
prerequisite was found. It does not claim literal live109d/system equality with
either newer toplevel. Lead repeats authority/claim/freshness/admission at activation.
The native launch marker retains older original package provenance and capacity0;
selection is not proof of relaunch. Ordinary switch admission must validate actual
native invocation/registration and refuse incompatibility. Passive naming/process
and HTTP reads prove availability only; no inference, sending or live archive was
attempted. E artifacts and ordinary switch preflights remain gates.

Later lead batch uses separate fresh machine ownership only after the prior parent
claim is released. Follow accepted preflight for typed machine verification,
prepared confctl generation activation when required, ordinary user-profile switch,
effect/usability verification and integrated-lineage release conditions. No reboot,
archive retry or cleanup is implied. Candidate preparation does not grant merge
approval.

No reusable configuration documentation change was useful for a generated pin.
Topic routing: installed/input proof and individual execution → this record and
`rollout.md`; lasting archive proof lifetime → C's runtime recovery documentation;
repeatable site deployment → current configuration
`docs/operations/codex-providers-aitherdev.md#deploying-a-change`, which explicitly
supports application-only profile selection; matching host/application contract →
`docs/operations/pi-runtime-aitherdev.md`; package-transition policy → installed
`share/dev-workspace/workspace-updates.md`. B's historical coordination-guide
read remains historical evidence, not current site-operation routing. These
current guides were read in full for this factual routing correction. Lead owns
session state/portal coordination edits and review invocation.

## G: mechanical freshness successor

Fresh defaults contained only accepted parent selection changes: workspace e7
changes flake.nix/lock, configuration9bdb changes lock. No new instructions,
behavior or unrelated input graph. Own `-reviewed-d` backup refs retain exact
reviewed1827/6f; E's immutable refs/sources and coref6 were untouched. The branches
were moved to fresh defaults and the established Nix/confctl generators reapplied
one finalf6 selection. No machine ownership, activation or new build/check watcher.

| Repository | Reviewed range | Refreshed range and entire final commit list |
| --- | --- | --- |
| workspace | `d43347c1..18275679109c2adda4084af1ea7474e21be98b4e` | `e7b876f69aca4554d52a3ac19ed097263847ad43..30b74dc3278728ab36197e0d2ef2cf76c66cf791`; one commit `30b74dc3278728ab36197e0d2ef2cf76c66cf791` inputs: select archive preparation fix |
| configuration | `d5055ec0..6f6cb452e17ca663114a07013a0402ef85a7fee3` | `9bdb0c68b47ceebde450fcdf018727b382cacc09..fdcb0a2c3f6413224a8e32b4b887eaf2ca8ecf81`; one commit `fdcb0a2c3f6413224a8e32b4b887eaf2ca8ecf81` inputs: set devWorkspace to f6d60bf8 |

Range-diffs `/tmp/archive-failure-g-{workspace,config}-range-diff.txt` show only
the predecessor selection655→91 and regenerated config changelog. Final pin files
are byte-equal reviewed D. Configuration's entire tracked final tree equals6f;
workspace's full nontracking source equals1827 (accepted work/archive tracking
baseline differs). No migrations, runtime changes, fixup/intermediate pin stream
or obsolete unmerged approach. Each final stream is one consolidated commit.

Reproducible read-only reconstruction from workspace root:

```sh
python3 work/2026-11-25-archive-failure-investigation/verify-g-pins.py
```

The ignored/untracked script proves all tracked paths/modes equal the fresh
default except declared selection files; reconstructs full locks by changing only
the runtime node to reviewed finalf6; verifies the direct nested URL replacement,
exact reviewed final locks and one-commit ranges. Script SHA-256
`524ac349d626425b37888b9854c19a95b75fef160ea7ffe95c0e14d5452d028c`;
receipt `g-pin-reconstruction.json` SHA-256
`d3b9689f202b05d2ffe2c41ab7d64a59394c7661e9039ef9752676ecc9635eb8`.
This is supplied evidence, not an independent-review claim.

Generator commands were the existing `nix flake update vpsfree-dev-workspace/dev-workspace`
and configuration-shell `confctl inputs channel set --commit dev-workspace devWorkspace f6d60bf87002fb1896599f35f0284743c16d7e6f`.
Cross-lock/site, whitespace and ordinary configuration Nixfmt/commit-message hooks
passed. Generated message now records only91→f6. Exact1827/6f publication leases
and fresh remote equality passed; both comparison captures were refreshed. No
applicable branch-push CI was superseded. Unchanged deployment-contract checks are
reused for identical script/site inputs.

Immutable evaluations of both reviewed1827 and refreshed30b74 prove exact equality:

| Artifact | Identical derivation | Identical output |
| --- | --- | --- |
| composed app | `/nix/store/m9pdsbnrrlwkyhp87d3cic5am7c10rbs-dev-workspace-0.2.0.drv` | `/nix/store/apjaqip0xj9cy297z2wmb8hmfqn2c8x1-dev-workspace-0.2.0` |
| composition check | `/nix/store/26hx1kp1xlmsklpx2zmz991m6qj3krn7-workspace-pi-runtime-composition-tests.drv` | `/nix/store/nxf02z6jccv47rzwzkl5gx3zadq67jya-workspace-pi-runtime-composition-tests` |

Reproduce either exact evaluation by setting the immutable `rev` to the retained
reviewed head or refreshed head, without realizing an artifact:

```sh
nix eval --no-write-lock-file --json --expr 'let f = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-archive-failure-investigation/workspace?rev=30b74dc3278728ab36197e0d2ef2cf76c66cf791"; in { appDrv = f.packages.x86_64-linux.default.drvPath; appOut = f.packages.x86_64-linux.default.outPath; compositionDrv = f.checks.x86_64-linux.pi-runtime-composition.drvPath; compositionOut = f.checks.x86_64-linux.pi-runtime-composition.outPath; }'
```

Both full final lock graphs remain byte-equal to reviewed D; exact app derivation
inputs map SHA-256 is
`b8498333b3bf949119400d9f808d9150ec6b146af4cd32f1ddfa0f641d728b62`.
Runtime source remains `/nix/store/hh81k6nk1r1x0jhi0v8a1l9d53jr0h4n-source`;
same derivation inputs/postInstall bind identical generated metadata/descriptors,
native Codex, worker, site/team catalogs and machine policy recorded by D. No
source-label normalization is needed between D and G artifacts: the derivations
are literally equal. Saved receipt `g-artifact-equivalence.json` SHA-256
`f52faaa125283401725cff97066cb2d20de3affadf6537a416f7b7122694379d`.

E's app/composition results may be reused on G only for those exact derivations
and complete inputs; coref6 remains unchanged. This is not tree-only test reuse or
an independent-review decision. Lead/retained reviewer owns the mechanical/history
supplement. No longer tests/builds were run by G. Previous D6f system paths are
historical evaluated metadata outputs; profile-only selection is retained and no
fdcb whole-system generation was built, evaluated or selected by G.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-archive-failure-investigation/
