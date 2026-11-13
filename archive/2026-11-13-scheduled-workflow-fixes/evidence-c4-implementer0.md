# C4 vpsFree: repository-locked confctl only

Owner: implementer0. Lead released the sufficient C4 brief in
[design.md](design.md). Only `flake.lock` and
`.github/workflows/daily-update.yml` are in scope. Earlier B2/C3 workflow pins
and successful hosted runs are historical evidence, not this architecture or
its acceptance.

**C4 delivery fully accepted: exact reviewed/focused-tested head integrated and
final vpsFree hosted workflow passed. No remaining package work.** Final head
`7d9807e021e6106d628c021da45f5f55077b2e9c`; lead accepted reviewer0's four-lane
final review without findings. Lead's sole managed observer confirmed hosted success;
historical C3 runs are not represented as C4 hosted acceptance.

## Baseline and generated input update

- Session/environment and saved live roster verified; current repository AGENTS
  and full persisted C4 brief read.
- Existing feature worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/vpsfree-cz-configuration`.
- Fresh fetched master and feature both
  `07a85cae5fdb4525e4ce2cca28a05a0888be8e0c`; clean index/source, no fast-forward
  needed. Preserve all merged B1/B2/C3 and authorized generated history.
- Preserved own prior ignored `.gems`, `.bundle` and `.bin` under
  `/tmp/scheduled-workflow-fixes-c4-implementer0/preserved-pre-c4/`. Copied the
  separately verified B2 Ruby3.4.11 native bundle into a fresh current-worktree
  cache; no unchecked native-cache reuse or broad clean/reset/stash.
- Actual declared initial shell setup passed bundle check, normal Overcommit
  install/config sign/plugin verification and native date/Overcommit loading.
  Current worktree GEM_HOME/BUNDLE_PATH and app config are used, not a workflow
  provider override. Ruby remains
  `/nix/store/hyrhia8cgzghr216z0r5wnbsqg7gbb9x-ruby-3.4.11/bin/ruby`,
  Bundler4.1.0.beta3, Overcommit0.76.0, native date3.6.0. Detailed whitelist in
  `initial-environment.json`; setup log `prepare-initial.log` under the temporary
  C4 evidence root above.

Ran the repository's normal command from the clean tracked checkout:

```sh
nix develop -c confctl inputs update --commit confctl
```

Generated input commit:
`0e66bd37ec51d5997a126e381fef68cc31438cba` —
`inputs: update confctl to ff5e0177`, lock only, 12 insertions/12 deletions.
Normal hooks passed; generated-message TextWidth warning was retained without
amending/rewrapping the generated message. Full output `input-update.log`.
No hand-edited lock JSON, exact-revision override, registry or channel change.

Semantic logical-path comparison ignores generated node IDs and verifies every
unrelated source and follows edge is unchanged. Exact changed paths:

| Logical path | Old revision | New revision |
| --- | --- | --- |
| confctl | 7bee58a52372b95c2198ce3f2a719807a3c2c66b | ff5e017780a35fb97b549db2a51b570193867c3b |
| confctl/nixpkgs | bd0ff2d3eac24699c3664d5966b9ef36f388e2ca | 8b8c811c7c2541c30382c5de7ed26be055569c60 |
| confctl/vpsadminos | 6f9b2c755143197bd9c3452e1c0121b22e978c4d | 67fcc17372d175b036706a1459a8b471bfc225e0 |
| confctl/vpsadminos/nixpkgs | bd0ff2d3eac24699c3664d5966b9ef36f388e2ca | 8b8c811c7c2541c30382c5de7ed26be055569c60 |
| confctl/vpsadminos/nixpkgsUnstable | 9ae611a455b90cf061d8f332b977e387bda8e1ca | f13ff45afd1bb73e640eaa08a7066dbed07e3238 |

`flake.nix` including normal `confctl.url = "github:vpsfreecz/confctl"`,
Gemfile.lock and production/channel roots are byte-identical to baseline.
Normalized full before/after graphs and check in temporary
`lock-graph-before.json`, `lock-graph-after.json`, `check-lock-scope.py`,
`lock-scope.txt`.

## Workflow change and preparation

Separate workflow commit `7d9807e021e6106d628c021da45f5f55077b2e9c` removes
`CONFCTL_FLAKE` and all five explicit
`nix shell ... -c confctl` wrappers. Every updater and final check-update now
uses plain `confctl` inside existing declared-shell blocks. The llm-agents
wrapper's Nix-only `--accept-flake-config` moves to that block's existing
`nix develop`; explicit `nix eval` flags remain intact. No flag, role/channel,
schedule, auth, permission, action, baseline/final lock or ordinary push changes.
B1's profile producer and all consumers stay intact.

Recorded preparation derivations:

- Initial declared shell:
  `/nix/store/iwhjiw7yjz4ssw93289qva17m1ysnc6v-nix-shell.drv`.
- Adopted declared shell:
  `/nix/store/a8y875bshlb1a9grzjsip905na0l9gis-nix-shell.drv`.
- Declared confctl package:
  `/nix/store/6nq336f5rfs8jgd38bsmdgpdhy5rw0rd-confctl.drv`.

Fresh utility `/root/c4_vpsfree_quick_watcher` passed adopted-shell
preparation, normal hook metadata, native probe, semantic graph/workflow,
YAML/Bash/actionlint and read-only channel/machine inventory evaluation.
Command `bash /tmp/scheduled-workflow-fixes-c4-implementer0/run-quick-checks.sh`;
log/receipt `quick-checks.log` / `quick-checks.result`, actual cache profile
`adopted-shell`, outputs `channels.txt`, `machines.txt`,
`adopted-environment.json` under the same temporary root. No node/kernel build
is allowed. Utility policy: selected package
`/nix/store/0s5dljmmfngj7ia2r9lfkxwydnfiz6b6-dev-workspace-0.2.0`, catalog
`f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d`,
verification watcher gpt-6-luna/low, full_access, matching native utility
`dw_e792014d07f1ab00a4e052aeb6fbc575674f9dbc9073f569`
(danger-full-access, never approvals).

The batch exited 0 in 36 seconds; tool session92423 completed with no remaining
effects and no node/kernel build. It passed bundle/hook/native preparation,
semantic logical graph/follows checks, YAML, all 7 Bash blocks, actionlint1.7.12,
exact allowed workflow delta and all five declared-shell calls, B1 profile
producer/consumer coverage, and read-only `confctl inputs channel ls` plus
`confctl ls` inventory evaluation. Outputs `channels.txt` and `machines.txt`
are retained. No source mutation or production machine connection/build was
performed by that batch.

Adopted profile resolves to
`/nix/store/6krdzayrv18d8y4m2rh65jjxdvnpbcf0-nix-shell-env`.
Actual caller Ruby remains 3.4.11 at the initial executable recorded above;
native date/Overcommit load from the current feature worktree `.gems`, not the
preserved pre-C4 cache. Actual Bundler4.1.0.beta3 / Overcommit0.76 remain compatible.
The source commit also ran ordinary Nixfmt and all commit-message hooks through
normal `nix develop`; all passed without warnings. `git diff --check` passed.

## Complete reviewed-candidate series and publication

```text
07a85cae5fdb4525e4ce2cca28a05a0888be8e0c  current master/base
0e66bd37ec51d5997a126e381fef68cc31438cba  inputs: update confctl to ff5e0177
7d9807e021e6106d628c021da45f5f55077b2e9c  ci: use confctl from the locked repository input
```

Two logical commits retain the repository's generated-input/source split:
lock12 insertions/12 deletions, workflow6 insertions/7 deletions; total two
files18 insertions/19 deletions. No superseded update streams, intermediate
provider choices, migrations, compatibility shims or rewritten merged history.
The single root-confctl tool update stream is final. Existing schema/rollback
contracts remain intact; machine-system build/runtime is not claimed.

Fresh fetch/rebase was unchanged; ordinary SSH feature push and final
`git ls-remote` prove master still `07a85cae` and feature `7d9807e0`. Worktree/index
clean. Comparison captured at the full exact range, timestamp
`2026-11-13T18:21:33Z`. No default write, claim, dispatch or target action.
[Published comparison](https://github.com/vpsfreecz/vpsfree-cz-configuration/compare/07a85cae5fdb4525e4ce2cca28a05a0888be8e0c...7d9807e021e6106d628c021da45f5f55077b2e9c).

Final receipts (SHA-256):

- `flake.lock`: `08212976733a03e5b879c86c0e0c38823257d2a1106e96dad3ccf57d013958c1`.
- Unchanged `flake.nix`: `fd49c6a1506e5241e93f817060736f63d8930554f5bc499462468d9de5fe1e71`.
- Unchanged Gemfile.lock: `e628cd3b3ddabf3913b2b8d6832daf7bc08dc4146b0780cacf2a8e67de75cb15`.
- Workflow: `f421b3ffd39b13354001eaecd89439e3913eec325487183931beac953c79dfd9`.
- Complete `final.diff` under the temporary root:
  `06b0f9d18fe749d94c409e83bf56e8482eb8ae047ce08abe017bbb54eb02b645`.

## Exact accepted provider proof reuse

Implementer1 confirms the package derivation above exactly matches accepted C3
output `/nix/store/v4b3r3r8102kyf92lidwvk62plpjs13j-confctl`, source
`/nix/store/1qw3c7q3r67drrv0z4vmac9g70pvxyf5-source`, Git
`ff5e017780a35fb97b549db2a51b570193867c3b`, source NAR
`sha256-Y7vwZfDEpElVUxEyDdpwHC8/1IapvkMz3/0AFr7U+yw=` and output NAR
`sha256-SEm2XycyQviAqJXW79ovMIrUM6wwp3LfBCTTpPWEXQ0=`.
The complete 8 locked-node/root input graph/store refs/digests and accepted
225 RSpec /110 RuboCop/actual packaged selection+guard+caller-hook proof remain
authoritative in [evidence-c3.md](evidence-c3.md), immutable package/full input
and post-review tables. Raw accepted artifacts:
`/tmp/2026-11-13-scheduled-workflow-fixes-c3-postreview.70mim6so/`.
No provider suite was repeated; current configuration-specific Ruby/profile
provenance and final check-update acceptance remain a separate post-review gate.

## Delivery boundary

Keep generated input commit separate from the workflow source commit. All
intended substantive commits and quick checks precede independent final review.
Focused environment/package provenance, real check-update and representative
saved-profile mutation acceptance are explicitly held for after that review.
Match existing accepted C3 provider package/source/input receipts before reusing
its selected-only guard/message proof; no provider suite repeat. Lead then owns
integration and fresh actual master workflow. No claims/default mutation,
dispatch, production deployment or source-scope expansion. Conditional target
preparation after the focused pass was separately released and is recorded below.

## Released focused post-review acceptance

Lead accepted exact range
`07a85cae5fdb4525e4ce2cca28a05a0888be8e0c..7d9807e021e6106d628c021da45f5f55077b2e9c`
in all four lanes, including the complete two-commit history/no migrations/single
tool-input stream/sole-lock authority. Then released only final caller provenance,
real final-snapshot no-change guard and the existing disposable profile pattern.

An initial temporary wrapper accidentally joined its clean-status test with
the following `nix develop` command. It exited2 immediately with
`test: too many arguments`, before any proof/environment/fixture mutation.
Diagnosed exact missing newline, preserved failed receipts as
`focused-acceptance-wrapper-failure.log` / `.result`, corrected only that
temporary wrapper and checked its Bash syntax. No product source changed or
unchanged product failure was retried.

Fresh utility `/root/c4_vpsfree_corrected_focused_watcher` ran
`bash /tmp/scheduled-workflow-fixes-c4-implementer0/run-focused-acceptance.sh`.
**Passed exit0 in23 seconds**, all operation-owned tools/cells joined and no
remaining effects. Same validated installed utility policy recorded above.
Main receipts `focused-acceptance.log` / `.result` beneath the temporary root.

The actual normal declared `nix develop` executable is
`/nix/store/v4b3r3r8102kyf92lidwvk62plpjs13j-confctl/bin/confctl`.
Its store deriver is the accepted `6nq336...-confctl.drv`, actual wrapper references
accepted source `/nix/store/1qw3c7q3r67drrv0z4vmac9g70pvxyf5-source`, and actual
package/source NAR hashes equal the accepted C3 hashes above. The sole declared
input lock is Git `ff5e017780a35fb97b549db2a51b570193867c3b`, with matching
source NAR. No separate provider selector was supplied. Receipts:
`declared-executable.txt`, `declared-source-reference.txt`,
`declared-store-info.json` and `final-caller-environment.json`.

Real plain command through that executable:

```sh
confctl inputs check-update --old-lock /tmp/scheduled-workflow-fixes-c4-implementer0/final-head.lock --new-lock /tmp/scheduled-workflow-fixes-c4-implementer0/final-worktree.lock
```

Old snapshot was `git show HEAD:flake.lock`; new snapshot was actual worktree
`flake.lock`. Both exact reviewed final snapshots have SHA-256
`08212976733a03e5b879c86c0e0c38823257d2a1106e96dad3ccf57d013958c1`.
Command exited0; `plain-check-update.log`, `.result` and `final-lock-hashes.txt`
retained. This proves the real final caller/snapshot boundary with no new update;
accepted C3 mixed/rewind/full-guard/provider suite was reused, not repeated.
Caller Ruby3.4.11/Bundler4.1.0.beta3/Overcommit0.76/native date3.6.0 identities
are those verified above, under the actual worktree's compatible bundle.

### Disposable saved-profile identity

Prepared only a same-session disposable clone of reviewed `7d9807e0` under
`saved-profile-fixture/`, with a separate copy of the verified compatible native
bundle. Created a profile from its actual declared shell, then changed only
the fixture's known `nixpkgsStable` locked record:

```text
ac588ef1c914865dad517b337ea0eb9694a4021c -> 718f670e845328e9c2cecdd832835712b2cbd065
lock before: 08212976733a03e5b879c86c0e0c38823257d2a1106e96dad3ccf57d013958c1
lock after:  256d93daaf5cd7a83151258fe0419ed37516e9bcdaff6092fc2cae7e3f5da21d
```

The latter is the known prior B1 Ruby-changing input record. Reentering the saved
profile retained byte-identical executable/native-Ruby/bundle records and exact
profile store target `/nix/store/6krdzayrv18d8y4m2rh65jjxdvnpbcf0-nix-shell-env`.
Tool stayed accepted `v4b3.../bin/confctl`, Ruby stayed3.4.11; no un-frozen old
environment/native-cache activation or provider suite/generation was needed.
Receipts: `fixture-tool-before.txt` / `-after.txt`,
`fixture-native-before.json` / `-after.json`, `fixture-profile-before.txt` /
`-after.txt`, `fixture-lock-mutation.txt`. Real source HEAD/lock/index stayed
clean and exactly reviewed; only disposable test data changed.

## Released final target preparation and window return

After focused PASS, inspected existing target
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/merge-targets/vpsfree-cz-configuration`.
It was already clean/detached at current master
`07a85cae5fdb4525e4ce2cca28a05a0888be8e0c`. Fresh fetch confirmed that default,
so no baseline update was necessary. Preserved target ignored caches.

Prepared normal target Overcommit install/config sign/pre-commit plugin trust
and native probe through the compatible adopted environment; all exited0.
Exact invocation starts from the **feature worktree cwd** recorded above:

```sh
nix develop /tmp/scheduled-workflow-fixes-c4-implementer0/adopted-shell -c git -C <target> ...
```

Profile resolves to `/nix/store/6krdzayrv18d8y4m2rh65jjxdvnpbcf0-nix-shell-env`.
This cwd retains the actual feature's fresh GEM_HOME `.gems/ruby/3.4.0`,
BUNDLE_PATH `.gems`, BUNDLE_APP_CONFIG `.bundle`; target old caches are neither
activated nor assumed compatible. Do not start that profile from target cwd.
Keep workspace coordination CLI outside the repository Ruby environment.

Final target remains clean/detached at `07a85cae`; fresh remote feature is
`7d9807e021e6106d628c021da45f5f55077b2e9c`, and default-to-feature ancestry is
verified. Receipts `target-preparation.log` / `target-environment.json`.
All commands completed0, no unresolved effects or claims. No feature merge,
default push or dispatch. **Exclusive target window explicitly returned to
lead immediately with raw readiness before this prose reconciliation.**

## Lead integration and hosted-run receipt

Lead accepted the local delivery/acceptance and completed approved fast-forward-
only integration of exact `7d9807e021e6106d628c021da45f5f55077b2e9c` from
`07a85cae5fdb4525e4ce2cca28a05a0888be8e0c`, using the feature-cwd adopted profile,
verified native environment and ordinary Git/hooks above. Lead reports a clean
target and exact SSH remote proof. Claim
`1dc84db8-a537-4db7-bd18-e3c90945f208` was held
`18:38:51–18:39:34 UTC`, then released and verified. PTY11893 exited0; no
unfinished effects. These are lead-supplied integration receipts, not duplicate
checks performed by implementer0.

After release, lead started fresh master daily
[43484770367 attempt1](https://github.com/vpsfreecz/vpsfree-cz-configuration/actions/runs/43484770367)
at event head `7d9807e021e6106d628c021da45f5f55077b2e9c`.
Sole managed observer: `e8ad4567-82b4-4e64-92f9-d0f2612ef73e`, with lead-confirmed
frozen current Luna/low/full-access policy and launch receipt. Final vpsFree
hosted acceptance is recorded below. Lead separately reports org C4 run43484020423 succeeded in
all steps. Implementer0 retains vpsFree hosted failure diagnosis if required.
No duplicate observation, source/target/check/dispatch or lifecycle action was
performed for this receipt reconciliation.

### Final vpsFree hosted acceptance: success

Lead reports run43484770367 attempt1 at exact integrated
`7d9807e021e6106d628c021da45f5f55077b2e9c` succeeded. Event
`workflow_dispatch`, `18:39:36–18:44:03 UTC`, elapsed4m27s. Every step passed,
including Update inputs, llm-agents, dependencies, and final Check and push.
Final plain declared `confctl` guard reported `No changes`/exit0, followed by
`Everything up-to-date`; no generated commit is claimed.

Sole managed observer `e8ad4567-82b4-4e64-92f9-d0f2612ef73e` terminated
passed/exit0; session58583 ended and all cells completed. Lead-retained logs:
`/tmp/scheduled-workflow-fixes-c4-vpsfree-hosted/run.json` and `run.log`;
log SHA-256 `6343598c8d2e6f541807e637c94fcee68d5cceda2bf7cfa1531cd4113a334465`.
Lead freshly fetched and verified source/master at exact `7d9807e0`, clean
feature and ancestry, and no workflow override matches. This is authoritative
lead-supplied evidence, not duplicate observation or checks by implementer0.
**C4 delivery fully accepted; no remaining package work.** No source, target,
default, dispatch or lifecycle action was taken for this final reconciliation.

No migration or new persisted format. Retain supported rollback/library paths;
recover source with additive reverts without reintroducing a workflow pin.
State/plan remain lead-owned.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-scheduled-workflow-fixes/)
