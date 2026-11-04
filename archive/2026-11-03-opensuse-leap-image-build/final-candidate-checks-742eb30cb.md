# Final candidate execution packet

Prepared only. `final_image_batch_native` owns the normal image batch; implementer1 has
not polled its logs or launched a test, VM or server. Start this packet only
after the lead accepts the completed normal four-image result and inspects these
inputs. Use fresh utility ownership for the related export/focused operations
and a separate explicitly owned foreground HTTP server. Stop on any failure;
do not improvise, retry or count ordinary Pry exit as a test pass.

## Fixed inputs and identity

Keep product head `742eb30cb1a8b6766c85e915d26b0400e38244b1`, clean source
`/nix/store/m1n49nc1qdf1f3j298zcmjjb5ni43iag-source`, existing source/runner GC
roots and v2 8 GiB module from [input recovery](final-input-recovery-742eb30cb.md).
Use only [final-runner-742eb30cb-v3.sh](final-runner-742eb30cb-v3.sh), SHA256
`c13929304f04033528bba1b5e98bd24bde862a35b2d6d6d9aa234631790c4e06`.

The two Ruby inputs use the existing native Pry context and interfaces:

- [Export input](final-candidate-export-742eb30cb.rb): one selected successful
  image fixture, source/selection/memory guards, retained builder identity if
  present, actual archive metadata and `/usr/lib/os-release`, native
  osctl-repo packaging, exact archive/tar hashes and host extraction.
  SHA256 `f5a280a7ce603f907c501d07f1b5fe82f44dc7d4800a684700b1b07a56530fa8`.
- [Focused input](final-candidate-focused-742eb30cb.rb): one selected existing
  test script and one exact local candidate. `FINAL_CANDIDATE_IMAGE` selects
  one of the four fixed artifact names below; no new launcher or test module.
  It checks a single-image native index/latest alias, synchronous default URL,
  no `repositories-tank`, exact URL readback and byte-identical guest index.
  It prunes and asserts no cached target archive before native test execution,
  then requires native result JSON plus `successful?` and the final marker.
  SHA256 `cab2b7ce716bdf5d82553535424c173d11059d356f0d52e17056668253490221`.

Both pass Ruby syntax parsing. The completed four native image cases have the
following actual successful primary JSON identities, independently checked against
the frozen copies in [completed-case audit](final-completed-case-audit-742eb30cb.md):

| Image | Successful primary JSON path | Expected SHA256 |
| --- | --- | --- |
| `opensuse-leap-15.6` | `/nix/store/fbn2vwka2qdnbyrkqsp3jpqqgmjjhgsq-os-test-image-scripts-test-opensuse-leap-15.6.json` | `4e08e5486ab3df102f681a001158e6245e7541bcf058fababb2ea2d55af715f5` |
| `opensuse-leap-16.0` | `/nix/store/dw0qknr27z2gyqv4k7b6glrhy988dk8g-os-test-image-scripts-test-opensuse-leap-16.0.json` | `07052fb31996fd48b84c4e9f48ab9e9b7c60c9569e2d6cc00a9fd6ae9099f8fa` |
| `opensuse-leap-16.1` | `/nix/store/j50dk28jfqwz1nvlmrm8s0nbg3jln0i0-os-test-image-scripts-test-opensuse-leap-16.1.json` | `aadb815caca564460f176718719ed8eba3608b0b059d61c7f6dcb7389144aae9` |
| `opensuse-tumbleweed` | `/nix/store/a6z3vcbfx1j1qycms0rzk1bmllqsbbj7-os-test-image-scripts-test-opensuse-tumbleweed.json` | `cc959e564a7119d3a8360b25e5d3a393a4007a02aadd2231a6a2f03f496c4942` |

Archive hashes and Tumbleweed archive release date remain pending the owned
export receipts; no values are inferred here. Its target release package
`20261102-4384.1` does not substitute for archive metadata. Each Ruby input
prints its actual JSON path/hash before work.
The lead must match each export's regenerated JSON to the corresponding
successful primary config before the first VM command. The two fixed Ruby inputs
and their hashes above remain unchanged.

## Serialize four retained image exports

The retained normal batch state base is
`/tmp/2026-11-03-opensuse-leap-image-build-final-742eb30cb-images`.
Open only one of the following native debug PTYs at a time, without `--fresh`:

```sh
/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/final-runner-742eb30cb-v3.sh debug --state-dir /tmp/2026-11-03-opensuse-leap-image-build-final-742eb30cb-images image-scripts/test@opensuse-leap-15.6
/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/final-runner-742eb30cb-v3.sh debug --state-dir /tmp/2026-11-03-opensuse-leap-image-build-final-742eb30cb-images image-scripts/test@opensuse-leap-16.0
/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/final-runner-742eb30cb-v3.sh debug --state-dir /tmp/2026-11-03-opensuse-leap-image-build-final-742eb30cb-images image-scripts/test@opensuse-leap-16.1
/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/final-runner-742eb30cb-v3.sh debug --state-dir /tmp/2026-11-03-opensuse-leap-image-build-final-742eb30cb-images image-scripts/test@opensuse-tumbleweed
```

At each live Pry prompt, evaluate the same fixed input, capture its complete
output and `FINAL_CANDIDATE_EXPORTED`, then send ordinary `exit` and verify the
native runner/VM has closed before opening the next one:

```ruby
eval(File.read('/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/final-candidate-export-742eb30cb.rb'), binding, 'final-candidate-export-742eb30cb.rb')
exit
```

The input never builds or downloads an image. It finds exactly one target
archive in the existing output directory, validates release/arch/vendor,
hashes it and adds it to a new disposable native repository with local `latest`
tag and ordinary defaults. Actual and alias paths must resolve to the same
archive and hash. The Tumbleweed archive includes a build-date version; the
input reads that actual version rather than recomputing today's date.

The builder ID is derived exactly as native `Builder` does from the selected
shared builder name. If it survives, capture configured metadata, actual
`/etc/os-release` and `rpm --version`, starting a stopped builder only for those
reads and restoring its stopped state. If it does not survive, the normal
build log remains primary builder identity evidence; the input records absence
and does not recreate it. Fresh bootstrap/scriptlet checks are not waived by
the older diagnostic installation warning.

Each VM's repository is tarred/copied with the existing native pull operation
and unpacked on the host into an isolated subdirectory:

```text
/tmp/2026-11-03-opensuse-leap-image-build-final-742eb30cb-candidates/<image>
```

Host tar files are
`/tmp/2026-11-03-opensuse-leap-image-build-final-742eb30cb-<image>-repo.tar`.
Existing output paths cause a stop, preventing evidence mixing. No public
repository or tag is changed.

## One explicitly owned local repository server

After all export VMs have closed, confirm port 18080 is free and the four
isolated repositories exist. A fresh utility owns this foreground process,
its terminal and complete `final-candidate-http-742eb30cb.log` capture:

```sh
python3 -m http.server --bind 127.0.0.1 --directory /tmp/2026-11-03-opensuse-leap-image-build-final-742eb30cb-candidates 18080
```

Each QEMU VM reaches only its candidate subtree at
`http://10.0.2.2:18080/<image>`. Keep the server owned through focused checks;
after their effects are reconciled, stop it normally through its owned terminal.
This is an operation close, not session lifecycle permission.

## Nine native focused checks

For each table row, open native debug with the exact image environment,
selector and a new state base. This CLI form is unchanged:

```sh
env FINAL_CANDIDATE_IMAGE=<image> /home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/final-runner-742eb30cb-v3.sh debug --state-dir <state-base> '<selector>'
```

Use the short, distinct state bases below from
[the literal command manifest](final-candidate-commands-742.json), SHA256
`d37ff138a5be07b4ae23dd46e7ee0571a17eaff26b0c88117df97213009f2b98`.
Use at most two 8 GiB/four-vCPU focused VMs concurrently after fresh resource
preflight. Each row uses its own native state; no public artifact cache is reused.
Require the first actual case's complete native result and `FINAL_CANDIDATE_PASSED`
before executing the other eight cases.

| Image | Selector | State base | Shell0 / longest socket bytes |
| --- | --- | --- | --- |
| `opensuse-leap-15.6` | `systemd/device-units#opensuse-latest` | `/tmp/osl742-d156` | 50 / 59 |
| `opensuse-leap-16.0` | `systemd/device-units#opensuse-latest` | `/tmp/osl742-d160` | 50 / 59 |
| `opensuse-leap-16.1` | `systemd/device-units#opensuse-leap-16.1` | `/tmp/osl742-d161` | 50 / 59 |
| `opensuse-tumbleweed` | `systemd/device-units#opensuse-latest` | `/tmp/osl742-dtw` | 49 / 58 |
| `opensuse-leap-16.1` | `dist-config/start-stop#opensuse-leap-16.1` | `/tmp/osl742-ss` | 48 / 57 |
| `opensuse-leap-16.1` | `dist-config/systemd-rundir#opensuse-leap-16.1` | `/tmp/osl742-run` | 49 / 58 |
| `opensuse-leap-16.1` | `dist-config/netif-routed#opensuse-leap-16.1` | `/tmp/osl742-net` | 49 / 58 |
| `opensuse-leap-16.1` | `cgroups/mount-v1#opensuse-leap-16.1` | `/tmp/osl742-cg1` | 49 / 58 |
| `opensuse-leap-16.1` | `cgroups/mount-v2#opensuse-leap-16.1` | `/tmp/osl742-cg2` | 49 / 58 |

The prior first literal case reached Pry, then `Shell#prepare` failed with
`ArgumentError` creating a 117-byte Unix socket path at pinned OSVM `shell.rb:52`.
No `FINAL_CANDIDATE_INPUT`/`PASSED` marker or actual assertion completion occurred.
This is a fixture path-length failure, not candidate-image test evidence.
The original manifest is preserved byte-for-byte as
[final-candidate-commands-742-long-state.json](final-candidate-commands-742-long-state.json),
SHA256 `95db1392875e1cfa62911fe22648ff00fd61ffb812c5e6578d59457704512e5f`.
Its failed long state and utility-owned transcript are untouched. Transcript
strings in the manifest are unchanged; retain the existing failed transcript
without truncating it when the next owned capture starts.

Pinned native path construction was read directly, without launching anything:
`test-runner` store `dh4npwsl659j3nivaqfknfkg3h70ag9m`,
`cli/command.rb:85–95` / `test_state.rb:9–11`; OSVM store
`hbxqbmd08gcyg6cs0238z03wvzk61471`, `machine.rb:1119–1184` and
`shared_dir.rb:23`. The test directory is
`<base>/os-test-<test.path.gsub(/[^A-Za-z0-9_.-]+/, '__')>-<SHA256(test.path)[0,8]>`.
The actual directory suffixes are:

| Test path (selector before `#`) | Generated state-directory suffix | Socket hash |
| --- | --- | --- |
| `systemd/device-units` | `os-test-systemd__device-units-e983cb16` | `ab47cdd7e62aeb1f` |
| `dist-config/start-stop` | `os-test-dist-config__start-stop-3c0e3c48` | `061a944b3033093a` |
| `dist-config/systemd-rundir` | `os-test-dist-config__systemd-rundir-739135eb` | `25a6e13e6c7aa49d` |
| `dist-config/netif-routed` | `os-test-dist-config__netif-routed-2d22f49c` | `3a7682216817b06b` |
| `cgroups/mount-v1` | `os-test-cgroups__mount-v1-1b384484` | `0636ea561f772e27` |
| `cgroups/mount-v2` | `os-test-cgroups__mount-v2-891d7b33` | `5c2758f7edb89792` |

Sockets use the separate `<base>/socks/` directory, not that test-directory
suffix. Native socket hash is SHA256 of length-prefixed (`Q>` byte count) test
path and machine name `machine`, truncated to 16 hex characters. The shell
suffix is `-shell.sock` (workers 1–4 add one digit); the longest socket is the
automatic shared filesystem's `-fs-vmSharedDir.sock`. These fixtures declare
no additional shared filesystems/named shells. The first actual paths are:

```text
/tmp/osl742-d156/os-test-systemd__device-units-e983cb16
/tmp/osl742-d156/socks/ab47cdd7e62aeb1f-shell.sock                 (50 bytes)
/tmp/osl742-d156/socks/ab47cdd7e62aeb1f-fs-vmSharedDir.sock        (59 bytes)
```

The same formula reproduces the failed original first shell length of 117 bytes.
Every revised case is at most 59 bytes, below the 107-byte pathname limit excluding
the terminating NUL. All nine state bases were checked absent, including symlinks,
before the manifest edit; none was created by this preparation. Only the `state`,
`argv` state argument and corresponding command state path changed in each case.
Parsed commands equal their argv arrays; all other JSON fields, product source,
runner, configuration and both Ruby inputs are unchanged. This preparation does
not establish a passing runtime result or authorize overlapping the old utility's
normal closure.

At each live Pry prompt, run exactly:

```ruby
eval(File.read('/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/final-candidate-focused-742eb30cb.rb'), binding, 'final-candidate-focused-742eb30cb.rb')
exit
```

Require `FINAL_CANDIDATE_INPUT`, native result JSON with success true, and
`FINAL_CANDIDATE_PASSED` matching source, selector, real release and archive
hash. Preserve native shell/console logs and HTTP image requests. The original
scripts prune cached archives at completion, so the input binds the local
single-image index and absent cache before execution; a missing post-cleanup
archive is not substituted as a hash receipt. Record the exported archive hash
and the server's corresponding request in the existing candidate receipt.

For all four device cases, retain the original eth0 status0, dummy-before
nonzero, creation0 and dummy-after status0 records through script completion.
There is no expected failure. The temporary local `latest` alias is an explicit
verification selector; it does not claim Tumbleweed is public `opensuse/latest`.

Any source/selection/memory, URL, service, index, archive/release or result mismatch
stops the operation. Preserve the failure and ownership for lead diagnosis; no
public fallback, manual daemon trigger/mask, test-script edit or retry is part
of this packet. Normal native shutdown/exit must be confirmed after every case.
