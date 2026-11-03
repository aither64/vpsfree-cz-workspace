# Local Fedora 45 image test recovery

The original exact-head test failed before VM startup during Nix evaluation.
`channel.nix` interpolates `system.vpsadminos.revision`, which was null:
the runner snapshots a linked worktree as a path source, whose `.git` is a
pointer file and which has no `.git-revision`. `version.nix` recognizes a Git
directory or `.git-revision`; `tests/make-test.nix` does not supply flake root
revision metadata. Fedora recipe/build/guest behavior was not exercised.

## Prepared retry

The external [metadata module](image-test-host-metadata.nix) sets only the
exact test-host revision, truthful clean tracked-source flag, and normal
`.git.dd18839` version suffix. SHA-256: `e29bb02c212bd104b7b8efff0873709d93f88f4671107d18483dd09a1588a66b`.
This is verification configuration outside the repository, not a product fix.
Its bytes are an additional declared test input. No kernel, image recipe,
assertion, package input or guest behavior is overridden.

From `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-fedora-45-image-build/vpsadminos`:

```sh
VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-fedora-45-image-build/image-test-host-metadata.nix \
  ./test-runner.sh test image-scripts/test@fedora-45
```

Use a fresh verification utility, preserve combined output in
`fedora-45-image-test-metadata.log`, and preserve native state separately from
the original failure. `VPSADMINOS_CONFIG` applies to this invocation only.
The wrapper supplies `TEST_RUNNER_REPO_REV` from exact HEAD. Current
`test-runner/nix/evaluate-tests.nix` routes a non-null `configuration` through
`flake.lib.testFramework.mkTests`, so no extra empty `--test-config` file is
needed. `RepositorySource.resolve_path` keeps this external module path intact.
A unique short `/tmp` state root may be selected by the lead with `--state-dir`;
record that ownership and avoid long Unix socket paths.

The retry is prepared, not run. A pass will be metadata-adjusted local image
verification, distinct from the original no-override failure and exact-head CI.
Stop/escalate unexpected local kernel compilation under the existing policy.

## Source and inputs

- Exact clean Git HEAD: `dd188397abe37d0bc33f4c5dfb3605206ce5e326`.
- Base: `5918f94e5e4eef3733b60aca4e03c1a6c0d43748`.
- Original and freshly resolved runner source:
  `/nix/store/zz0q306x5n1znadlffhds5yzf5gafc5v-source`.
- One bounded read-only comparison of `git ls-tree -rz HEAD` against that
  snapshot verified all 2,369 tracked regular-file/symlink Git blob identities
  and executable modes. No mismatches. The snapshot additionally has ignored
  development `.gems` tooling and the `.git` pointer file; these do not modify
  tracked product source.
- Fresh clean Git flake metadata resolves source
  `/nix/store/cgk63vdx1wjl4ybd53abkd5aqyzc7sfa-source`, revision `dd188397abe37d0bc33f4c5dfb3605206ce5e326` and NAR hash
  `sha256-LXZP7Ghcr+1obFUD+LjlJRO63qRo/GZtSve5AX5MZ7c=`.
- The snapshot's complete `flake.lock` graph equals the graph in
  [fresh Git metadata](verification-source-metadata.json), including all nested
  nodes and follows edges. [Resolved input paths](verification-input-paths.json)
  record the runner path-flake input store paths.

Locked input nodes:

- `home-manager`: `c47b2cc64a629f8e075de52e4742de688f930dc6`, `sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg=`.
- `impermanence`: `fa627f4c8b8e92f58f58a73d99ee4e1304e64eb2`, `sha256-s0TeXWG5Ci75Y/Hzon0Z7NrN/fG773Rc54/z6oPFszQ=`.
- `netlinkrb`: `d9de53d843d2586ffa5b7b404887fa801c697ddf`, `sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg=`.
- `nixpkgs`: `e4bae1bd10c9c57b2cf517953ab70060a828ee6f`, `sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc=`.
- `nixpkgsUnstable`: `0bb2eedc20e4739f29e8045034f2828ad7054f8f`, `sha256-fiPJ88izTVucjeo2EQ3jk4aWmLg03I1D4vxnX2QjEgE=`.
- `nixpkgs_2`: `7dcdd87373d72e7a2173e4db02e20d3d7f495cfd`, `sha256-tItrb9M8eYA6WhFgmT9tpGKueri3+wRuVA952o/2xSU=`.
- `ruby-lxc`: `004bf35eb90d41ba60b347b5b1e73d868a4f95d9`, `sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE=`.

Root edges: `nixpkgs -> nixpkgs_2`, `nixpkgsUnstable -> nixpkgsUnstable`,
`impermanence -> impermanence`, `netlinkrb -> netlinkrb`, `ruby-lxc -> ruby-lxc`.
`impermanence` uses `nixpkgs` and `home-manager`; `home-manager/nixpkgs` follows
`impermanence/nixpkgs`.

## Retained evidence and limits

Original output: [fedora-45-image-test.log](fedora-45-image-test.log).
Original result: [fedora-45-image-test-result.md](fedora-45-image-test-result.md).
Native failure state remains
`/tmp/os-test-runner/os-test-image-scripts__test__fedora-45-07b223fa`.
No original evidence was removed or overwritten. Existing source quick checks
and independent review remain valid because the repository/head is unchanged.

Existing notes already describe this cause and recovery; no duplicate note is
needed: [image-test metadata](../../notes/vpsadminos/2026-10-14-image-test-worktree-metadata.md)
and [linked-worktree runner revision](../../notes/vpsadminos/2026-08-24-test-runner-linked-worktree-revision.md).
The older image note required an empty test config; the current runner's
non-null configuration route makes that extra file unnecessary.
