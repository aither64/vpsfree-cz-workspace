# Prepared final-source verification

Prepared commands only. Lead-owned retained final review must finish before
fresh long checks. Each operation uses the required fresh utility watcher;
implementer1 has launched no final-source VM/server/test batch.

## Immutable identity

- Final Git head `742eb30cb1a8b6766c85e915d26b0400e38244b1`, tree
  `19f423e70ff439867d4bb27e8ed07b9c95fdb703`.
- Clean source `/nix/store/m1n49nc1qdf1f3j298zcmjjb5ni43iag-source`, NAR
  `sha256-MwArttbMI6mzt/YzUwvSbK1Pd4mizjKqO600EnK2fNE=`. All 2,371 regular
  files/symlinks and executable flags match the committed tree, with no extras
  or missing files. The final message-only amendment has the identical tree.
  It is now protected by the session's durable source GC root; see
  [input recovery](final-input-recovery-742eb30cb.md) for the materialization,
  source/runner roots and rechecked identity after the v2 missing-source failure.
- Immutable existing wrapper
  `/nix/store/jwkyiqgfq607h40zasf5p0rkd3rzkkly-test-runner/bin/test-runner`,
  SHA256 `b587483082b031fb8606d150c4da39f5a7082ba8ce3aa2bb1572f436e424f0a2`.
  Runner/framework code and pins are unchanged; its own script supplies the
  exact Ruby/gem/environment paths. Do not transcribe those paths manually.
- Use the generated [fixed invocation](final-runner-742eb30cb-v3.sh), SHA256
  `c13929304f04033528bba1b5e98bd24bde862a35b2d6d6d9aa234631790c4e06`.
  It exports the exact metadata below and executes the existing rooted wrapper;
  shell syntax and the wrapper's require-only dependency preflight pass.
- [Final revision module](final-revision-742eb30cb.nix), SHA256
  `3e8392da46d70a81a15727e8a8162cf59da8c67460724026e49f4a0818304876`.
- [Final 8 GiB module v2](final-verification-742eb30cb-v2.nix), SHA256
  `f6bebf53ebdb690c996fd325ced3db201403d97dc1e525731ea9178b849fd90d`.
  It imports the exact revision and sets `lib.mkOverride 60 8192`. Ordinary
  image-fixture memory has priority 100; explicit `mkForce` has priority 50.
  Priority 60 replaces the ordinary 24 GiB image size while preserving special
  fixtures' forced sizes, including kernel/namespaces at 4096 MiB.
  Fresh watcher syntax/priority validation passed; selector discovery remains
  pending after source recovery. Historical AA, 578 and c856 files remain
  unchanged and must not be substituted.
- Complete dependency graph is the committed `flake.lock`, SHA256
  `604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa`, unchanged.
  Its root/nested edges and NAR hashes are authoritative. Locked revisions:

| Node | Revision |
| --- | --- |
| Root nixpkgs (`nixpkgs_2`) | `7dcdd87373d72e7a2173e4db02e20d3d7f495cfd` |
| nixpkgsUnstable | `0bb2eedc20e4739f29e8045034f2828ad7054f8f` |
| netlinkrb | `d9de53d843d2586ffa5b7b404887fa801c697ddf` |
| ruby-lxc | `004bf35eb90d41ba60b347b5b1e73d868a4f95d9` |
| impermanence | `fa627f4c8b8e92f58f58a73d99ee4e1304e64eb2` |
| Its nixpkgs (`nixpkgs`) | `e4bae1bd10c9c57b2cf517953ab70060a828ee6f` |
| home-manager | `c47b2cc64a629f8e075de52e4742de688f930dc6` |

The final realized JSON/system/kernel/initrd/store paths and their hashes must
be recorded by the actual operation. They have not been built or inferred here.

## Native listing and one normal image batch

The original `final-verification-742eb30cb.nix` remains unchanged as failed
evidence, SHA256
`ac4c0d2f88be2925fc10256874838253dfde7a91a328c6cf165dce93dea12194`.
[First discovery](final-discovery-result.md) failed before VM/build because its
global `mkForce 8192` conflicted with the unrelated namespaces fixture's
`mkForce 4096` during all-suite resource metadata enumeration. No product change
is needed. The v2 priority fixes that conflict without overriding forced sizes.

The fresh v2 lead watcher already validated syntax and exact priority behavior
using the pinned native module system. The successful command below is retained
as evidence, not a required repeat after source recovery:

```sh
nix-instantiate --parse /home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/final-verification-742eb30cb-v2.nix > /dev/null
nix-instantiate --eval --strict --expr '
let
  lib = import /nix/store/2xl4y8v0mpkqbvxdra2c0ci02w8mczyy-source/lib;
  sizing = import /home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/final-verification-742eb30cb-v2.nix { inherit lib; };
  memory = definition: (lib.evalModules {
    modules = [
      { options.boot.qemu.memory = lib.mkOption { type = lib.types.int; }; }
      { boot.qemu.memory = definition; }
      { boot.qemu.memory = sizing.boot.qemu.memory; }
    ];
  }).config.boot.qemu.memory;
in { image = memory (24 * 1024); namespaces = memory (lib.mkForce 4096); }
'
```

The observed priority result was `{ image = 8192; namespaces = 4096; }`.
The native listing below still must confirm the actual four cases. The v2
listing failed before selection because its unrooted source had disappeared;
[input recovery](final-input-recovery-742eb30cb.md) restores the exact source
and durably roots it and the existing runner.

Run from the initiative's vpsadminos worktree. Use this fixed invocation so the
exact source/revision/config and native wrapper environment are not retyped.

```sh
/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/final-runner-742eb30cb-v3.sh \
  ls 'image-scripts/test@opensuse-{leap-15.6,leap-16.0,leap-16.1,tumbleweed}'
```

Listing must select exactly those four actual shared-helper consumers. The
reviewed source's shared Leap builder serves all three Leap releases; normal
Tumbleweed coverage is required because it uses the same changed helper.
The same fixed invocation also lists existing device selectors, without test or
VM execution:

```sh
/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/final-runner-742eb30cb-v3.sh ls 'systemd/device-units#opensuse-*'
```

Check fresh host RAM, shared-memory and CPU headroom before the batch. Two
guests require 16 GiB RAM, 16 GiB shm and eight vCPUs plus the normal reserves;
lower jobs to one if necessary. Confirm the following state path is unused so
no name-keyed old builder or retained image is reused. Do not destroy old AA
evidence to make it fresh.

```sh
/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/final-runner-742eb30cb-v3.sh \
  test --jobs 2 --stop-on-failure --no-destructive \
  --state-dir /tmp/2026-11-03-opensuse-leap-image-build-final-742eb30cb-images \
  'image-scripts/test@opensuse-{leap-15.6,leap-16.0,leap-16.1,tumbleweed}'
```

Stop unexpected local kernel builds, genuine OOM, guest kernel failures or
bootstrap errors. Preserve failing logs; no blind retry. Inspect fresh bootstrap
and scriptlets for Lua/cpio/unexplained errors even if an outer command exits
0. The live diagnostic reload warning is explained in
[the causal result](device-unit-result.md) and does not waive this requirement.
Retain actual builder OS/RPM versions, candidate paths/hashes and complete input
identity in the existing image/candidate receipts.

## Candidate-backed assertions

The ready [final candidate execution packet](final-candidate-checks-742eb30cb.md)
provides two fixed native Ruby inputs, four serialized retained exports, one
owned local server and the nine guarded focused checks. Lead inspection and the
successful normal batch receipt precede those operations. AA files retain their
historical source identity; final execution uses the new 742 inputs.

After successful normal builds, use the existing manual candidate extraction
and local repository mechanism in [candidate checks](candidate-checks.md).
Preserve its URL/service-absence assertions before invoking a test script.
Do not introduce asynchronous repository-setting hooks, a public tag move or a
new permanent test matrix.

Run the complete original device assertions against each of the four rebuilt
artifacts. Use `systemd/device-units#opensuse-leap-16.1` for explicit 16.1.
For the three existing releases, the architect-approved method reuses the
existing `opensuse-latest` script with a temporary local `latest` alias bound
to one exact rebuilt artifact at a time. Record each selector, real release,
archive hash and `/etc/os-release`; no public image may substitute silently.
`opensuse/latest` is a Leap selector (public 16.0 before this feature,
registration 16.1 after it), not Tumbleweed's `latest-tumbleweed`. Tumbleweed
alone cannot prove removal of the Leap/latest exception.

Every case must prove eth0 active, dummy0 absent before creation, dummy0 active
after creation and the original script's completion. No expected failure or
timeout is a pass. Rebuilt 16.0 and 16.1 proof covers the relevant latest
meanings; the 15.6/Tumbleweed checks cover the other helper consumers. Finish the
previously selected final-16.1 start-stop, `/run`, routed networking and both
cgroup-mode checks with that same final artifact. Earlier AA results retain
their historical scope and do not validate the final shared-builder/helper tree.
