# Scoped verification memory

Owner: implementer1. Metadata-only verification passed (exit 0, 99 seconds).
The fresh utility has finished and its slot is free; no operation remains.
No application edits or Git mutations were made. Source head:
`1a637e9eac4311adba2b08d60dfa7a17d07bcb52`.

The global temporary memory override conflicted with unrelated fixtures using
`mkForce 4096` during full-suite metadata evaluation. The original
`final-image-tests.log` is preserved, SHA-256
`78152a0d10ab7facd136bff934ec8d809eca33f1d9343aaab456c3237a72b3f1`.
That failure occurred before scheduling and had no VM effects.

The corrected `verification-memory.nix` contains exactly:

```nix
{ config, lib, ... }:
{
  boot.qemu.memory = lib.mkIf (lib.hasAttrByPath [
    "boot"
    "zfs"
    "pools"
    "tank"
    "datasets"
    "image-scripts/build"
  ] config) (lib.mkForce (8 * 1024));
}
```

Module SHA-256:
`adef87cd3c928b4a5687150fc5a43f271e64f1fceeb64745bcc4639aad62b582`.
Parsing passes. The dataset marker is declared by the shared image-test template
in `tests/suite/image-scripts/test.nix`; no other source declares this marker.
The ZFS pool/dataset option declarations do not depend on QEMU memory. Applying
`mkIf` at the memory leaf leaves the other machine definitions intact and keeps
the existing override priority.

A fresh pinned `gpt-6-luna` / `low` utility ran the native full metadata reader
through `Cli::Command#with_repository_source` and `NixCli#eval_tests_meta_all`.
This retains the normal source snapshot rooting and scoped environment, without
reusing an unrooted cached source or introducing another test harness. The local
`.#test-runner` shell sets native `RUBYLIB` inside `env`, as documented in
`metadata-result.md`. Only `VPSADMINOS_CONFIG` selects the temporary module.

The shell invocation was `nix develop .#test-runner --command env`, followed by:

- `RUBYLIB=/nix/store/givmi31xrbr231gxnry1xc2ggb5s4imf-libosctl-native-local/lib`
- `VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-redhat-image-releases/verification-memory.nix`
- `TEST_RUNNER_REPO_REV=1a637e9eac4311adba2b08d60dfa7a17d07bcb52`
- `bundle exec ruby -I test-runner/lib -r test-runner/cli`, with inline Ruby
  constructing `Cli::Command.new({}, { 'system' => 'x86_64-linux' }, [])`,
  entering `with_repository_source`, and invoking
  `NixCli.new(system: 'x86_64-linux', repo_root: command.send(:repo_root)).eval_tests_meta_all`.

All 168 metadata entries evaluated successfully without recursion or conflicting
memory definitions. Generated resources:

| Test | Machines | Memory MiB | Max machine MiB | Shared memory MiB | CPUs |
| --- | --- | --- | --- | --- | --- |
| `image-scripts/test@centos-9-stream` | 1 | 8192 | 8192 | 8192 | 4 |
| `image-scripts/test@centos-10-stream` | 1 | 8192 | 8192 | 8192 | 4 |
| `image-scripts/test@rocky-9` | 1 | 8192 | 8192 | 8192 | 4 |
| `image-scripts/test@rocky-10` | 1 | 8192 | 8192 | 8192 | 4 |
| `osctl/ct-transient-failures-v1` | 1 | 4096 | 4096 | 4096 | 4 |
| `osctl/ct-transient-failures-v2` | 1 | 4096 | 4096 | 4096 | 4 |

The watcher asserted the four selected images' generated resources and both
fixtures' retained 4096 MiB values. It also checked all 51 image-suite entries:
every one reports 8192 MiB. The captured source path was
`/nix/store/91nflgfhifb631q7816j30smqm76afjv-source`, revision
`1a637e9eac4311adba2b08d60dfa7a17d07bcb52`, `shortRev=1a637e9`, `dirty=true`.
The reported dirty flag is retained as observed, despite the clean app worktree.

Full log: `/tmp/redhat-verification-memory-metadata.log`, SHA-256
`a1ab81454342e6c84d900048b1a51b3614c39283bd549f736b4d6507d5a2aa43`.
Exit status: `/tmp/redhat-verification-memory-metadata.exit` (0). Final app
status remains clean, the temporary module hash is unchanged, and the original
failure log hash is unchanged. Only normal development-shell preparation and
the authorized source-snapshot realization occurred; no VM, image, system or
kernel build ran. No reserve, source, security, timeout or assertion setting
was changed. The lead owns the fresh actual image batch.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-redhat-image-releases/)
