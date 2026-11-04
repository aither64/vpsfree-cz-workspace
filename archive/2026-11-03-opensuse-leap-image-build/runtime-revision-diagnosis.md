# Image-test source revision diagnosis

The first primary run failed before test JSON generation, VM startup or image
build. Preserve [original output](image-test.log),
[result](image-test-result.md), and native trace at
`/tmp/2026-11-03-opensuse-leap-image-build-image/os-test-image-scripts__test__opensuse-leap-16.1-90ada9d4/test-runner.log`.
There were no VM disks or kernel builds in this attempt.

## Exact identity and cause

- Repository `vpsfreecz/vpsadminos`, feature branch
  `2026-11-03-opensuse-leap-image-build`, target `staging`.
- Tested head `fe9182dd2fb1ba627c30d54c39c1acd7b140df69`, tree
  `05b7f416e90b321f7d9c81a21198ed8d5b1625a5`.
- Immutable source: `/nix/store/qzj1g8vq7274kalzc5h1niza39kkg4y6-source`.
- Runner wrapper: `/nix/store/jwkyiqgfq607h40zasf5p0rkd3rzkkly-test-runner`;
  runner helper/code: `/nix/store/dh4npwsl659j3nivaqfknfkg3h70ag9m-test-runner`.
- Root nixpkgs: revision `7dcdd87373d72e7a2173e4db02e20d3d7f495cfd`,
  `/nix/store/2xl4y8v0mpkqbvxdra2c0ci02w8mczyy-source`.
- Exact dependency graph is the unchanged candidate `flake.lock`, SHA256
  `604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa`.
  Other locked revisions: nixpkgsUnstable `0bb2eedc20e4739f29e8045034f2828ad7054f8f`,
  netlinkrb `d9de53d843d2586ffa5b7b404887fa801c697ddf`, ruby-lxc
  `004bf35eb90d41ba60b347b5b1e73d868a4f95d9`, impermanence
  `fa627f4c8b8e92f58f58a73d99ee4e1304e64eb2`, its nixpkgs
  `e4bae1bd10c9c57b2cf517953ab70060a828ee6f`, and home-manager
  `c47b2cc64a629f8e075de52e4742de688f930dc6`.

The runner resolves the Git worktree to an immutable flake source snapshot.
That source has neither `.git` nor `.git-revision`. The default for
`system.vpsadminos.revision` in `os/modules/misc/version.nix` is therefore null.
`tests/make-test.nix` supplies exact nixpkgs metadata but does not populate this
OS revision. The image-test VM enables channel registration;
`os/modules/installer/cd-dvd/channel.nix` interpolates the null revision into
its `echo -n ... > .git-revision` command, causing the reported coercion error.

This is an existing baseline metadata gap: `git diff --exit-code
dd188397abe37d0bc33f4c5dfb3605206ce5e326 HEAD --
os/modules/installer/cd-dvd/channel.nix os/modules/misc/version.nix
tests/make-test.nix tests/suite/image-scripts/test.nix test-runner flake.nix
flake.lock` passed with no differences. The channel blob at both heads is
`cded987bbacf826ede1a69d06c19392f422ffdaf`; both relevant modules also compare
identically to the actual failed store snapshot. No baseline runtime repro was
needed to establish the unchanged code path and null default.

## Bounded environment remedy

The documented `VPSADMINOS_CONFIG` interface supplies a module to the test
framework. Session-only [test-revision.nix](test-revision.nix) records the exact
candidate revision and clean status; it passed Nix parsing. No project source,
helper, builder, dependency pin or test-runner change is needed.

Run the existing primary command through the lead's fresh watcher:

```sh
env VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/test-revision.nix ./test-runner.sh test --no-destructive --state-dir /tmp/2026-11-03-opensuse-leap-image-build-image image-scripts/test@opensuse-leap-16.1
```

Use a separate retry log/result and retain the original failure evidence.
The config binds this exact head; revise its metadata if later source changes.
All candidate debug commands require the same configuration.

## Unsuitable standalone probe

The evaluation-only probe used `nix-instantiate --eval --strict` on the
`testJson` result. That result is a derivation attrset, so strict recursion
walked `.all`, `drvAttrs`, `stdenv`, requisites and test passthru attributes until
max-call-depth. [Probe output](revision-evaluation.log) records that distinct
failure. It did not run a VM or image test and does not establish failure of the
revision module. Do not repeat this probe or add another probe framework; the
actual runner realizes test JSON through its normal `nix-build` path.
