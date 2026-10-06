# Registered fixture follow-on preparation

Historical checkpoint: this continuation was consumed and launched the runtime
and one warm-up. Do not repeat its command. Current after-warm-up preparation,
code hashes and the later accepted-stream listener correction are recorded in
[verification-warmup-preparation.md](verification-warmup-preparation.md).
The hashes and preflight evidence below describe the earlier reviewed run.

Prepared for parent inspection, affected-lane independent review and one fresh
watcher execution. No live continuation, model turn or history RPC was run
during this preparation. Real acceptance and latency measurements remain pending.

The parent reports that actual read-only preflight passed through SSH,
`sudo -H -u aither` and the runtime Nix shell in **10.447 seconds**, validating
all 3,379 histories, retained PID 1687746 and the exact alias, target, listener
and proofs. It created no claim and made no fixture mutation. Both code hashes
below were stable before and after that preflight. The retained independent
reviewer is reviewing those exact hashes in four affected lanes; this is not
benchmark execution or acceptance evidence.

Exact SHA256:

- `verify-creation.py`:
  `4a483d39a5a5d9b93bbbf9f2eef0a901cef749ca1a0e10ad6e9de3aefe846605`
- `verify-started-creation.py`:
  `721de6f01de6762bc639d4b09275c8dac96f5c9c0e8b7906d6ed651167f9022c`

The original prepared driver was
`f49abcaba01417863866dddf698274a024c013b2d6bae9859afc8878f682ca8a`.
The temporary socket-mode exemption at SHA256
`021b2b36b27dca819b65bf26c39740b6697d8846675ede382f57659c493e5c9e`
was removed by a byte-for-byte restoration of that original driver before this
alias correction. The private fixture and original host proof are unchanged.

The failed preflights remain diagnostic evidence: the first refused
the writable-path guard; the next observation differed from the proof's socket
inode. Metadata showed device 64769, inode 20106708, UID 1000, mode 0777 and
size 87. Architect read-only `lstat` correctly identified a symlink, while the
parent initially misread `S_IFLNK` as socket type and later used `stat -L`.
The focused-check audit found no unmocked fixture mutation path; it did not
establish the tool provider's internal behavior.

The parent's subsequent correction establishes that tool and SSH observations
agree: the advertised path is an alias to the original physical socket.
The earlier proxy/environment explanation, including the claim that SSH would
make the original `lstat` guard pass, was wrong. The original proof used
`socket.stat()` and therefore recorded the target: device 64769, inode
18775180, UID 1000, mode 0600, size 0, mtime
`2026-10-02T18:14:23.029563Z`. The alias has inode 20106708 and mtime
`2026-10-02T18:14:23.030563Z`. Neither was replaced by the preparation.

The selected [Codex 0.160 Unix transport source](https://github.com/openai/codex/blob/rust-v0.160.0/codex-rs/app-server-transport/src/transport/unix_socket.rs#L45-L105)
binds a protected physical socket, sets mode 0600 and publishes a symlink at the
advertised path. Its protected filename derives from that path's SHA256.
This is the selected transport contract, not a proxy workaround. The driver now
validates the exact known alias and original target against both parent proofs
and ties the listener to the retained PID. No private chmod, proof change,
claim or relaunch occurs.

The preceding watched script was
`57c28957b019ddba36cebf2ae650c30bd1a9fcc2468be7077da4e9544c367b28`.
Earlier SHA/check/review provenance is retained in
[verification-resume-preparation.md](verification-resume-preparation.md).

## Observed failure and package contract

The corrected seeded continuation reached successful public registration,
generated genuine registration/inventory markers, profile/token/config and
adapters, and launched App Server PID 1687746. The next prototype assertion
failed with `running App Server executable is not the selected Codex` before
portal/tmux or any warm-up/creation. `seeded-continuation/` remains in place.
This is a prototype identity error, not a Codex or workspace contract mismatch.

The owning `dev-workspace/docs/codex-package.md` and
`nix/codex-package.nix` define a public shell launcher and a materialized native
runtime. Selected assembled package:
`/nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0`.
Its public `bin/codex` forwards to the entrypoint declared in
`libexec/codex/codex-package.json`: layout 1, version 0.160.0, variant `codex`,
target `x86_64-unknown-linux-gnu`, entrypoint `bin/codex`, resources
`codex-resources`, path directory `codex-path`. The process executable is
therefore the package's `libexec/codex/bin/codex`.

`native_codex_entrypoint` is the single prototype helper owning that resolution.
Fresh main now compares `/proc/<pid>/exe` with this declared native path;
config and registration retain the public launcher. No version, package,
catalog, pin, application interface or runtime marker was changed or forged.

## Exact follow-on boundary

The bounded driver fixes root `/tmp/pcp-oct02-a` and candidate
`/nix/store/0klh7dhca2dwyfwsz0m67pbjj2nml70d-dev-workspace-0.2.0`.
It accepts only the current exact incomplete executable-mismatch failure with
zero results/no warm-up. It pins non-credential records by digest, including
current result, config, preset, adapters, registry, genuine registration and
inventory, history summary and the preserved original failure. Profile symlink
identity and ownership must still match. It verifies the selected runtime
registration contract and rejects changed paths, unexpected links, runtime or
creation state, portal/tmux sockets, or a previous `started-continuation/` claim.
Auth is only checked for ownership/type/mode; its contents are never read/copied.

The parent's owned mode-0600 host metadata proof is:
`/home/aither/.local/state/dev-workspaces/verification/2026-10-02-portal-creation-performance/benchmark-started-proof.json`.
Its SHA256 is
`21d0465d65e5ec4a171dd50daf295f0328968d401cc4932164a1f40f8ed08a6f`.
The driver checks that exact proof and PID 1687746's boot ID, kernel start ticks,
native executable, cwd, command-line digest and owned target socket inode/device.
The cwd is `/tmp/pcp-oct02-a`, matching the original `spawn(..., cwd=root)`.
It prints neither argv nor credential content and scans no other processes.
It repeats the identity check before the exclusive claim.

The sibling owned mode-0600 `benchmark-socket-alias-proof.json` is pinned at
SHA256 `3f6b7faf3e402bc3a4981a78b5dd0c56c447ddf5b398ea087ebfb14bfcaef84d`.
It links to the unchanged original proof hash and process start identity. The
driver checks exact alias/target device, inode, owner, mode and timestamps,
readlink/resolved target and the original socket identity. Only this proved
alias passes the fixture link/writability guard; other links, writable files
and sockets retain their refusals. The original PID's FD 30 must still refer
to kernel socket inode 355192150, with exactly one matching LISTEN stream row
at the resolved target in `/proc/1687746/net/unix`. No global process scan or
generic socket adoption is added.

The architect's focused checks model process and socket observations in memory;
this tool context cannot inspect the retained PID and a read-only target
metadata attempt returned PermissionError. That limits local verification,
not the transport contract. The parent will use direct SSH to aitherdev under
`sudo -H -u aither` in the runtime Nix shell for consistent host observation.
Missing visibility, an exited/reused PID, changed identity or listener still
refuses. The driver does not infer ownership, restart Codex or replace a process.

The driver validates the retained 3,379 rollouts/208,256,155 bytes and original
16 KiB seed payloads through the existing validator. It then exclusively
creates `started-continuation/`, preserves/fsyncs the current failure, process,
config, marker and other pinned records plus both host proofs, and only then writes
the next result. Original history and `seeded-continuation/` remain unchanged.
Any partial claim or later failure retains all evidence/services and refuses
another attempt; no automatic retry, reset, cleanup or lifecycle action exists.

## Shared sequence and focused evidence

The existing environment allowlist and tmux/portal/full acceptance tail were
extracted into `isolated_environment` and `finish_creation_verification`.
AST comparisons prove those extracted blocks are identical to their previous
main blocks. Every pre-existing helper is unchanged. The only changed existing
function is main: the two extractions and corrected executable assertion.
The driver calls that shared tail directly; it neither registers nor launches
an App Server and adds no main CLI flag or generic resume mechanism.

All original gates remain: one warm-up and five sequential Full teams, every
duration retained, median <10 s and maximum <15 s, separate model completion,
one initial request, no-tool assertion, detailed phase/stage evidence, identity
checks and both original helper-boundary fault cases. Process retention and
the documented fault/recovery limitations are unchanged.

Checks passed:

- AST/compile and whitespace/Markdown checks for both scripts/docs; exact
  extraction equivalence and unchanged pre-existing helpers.
- Actual assembled manifest/launcher/native metadata inspection, without
  executing a package binary.
- 77 focused checks: 8 manifest cases, 35 host/alias/listener cases, 25 fixture guards,
  4 driver ordering/failure cases, 3 shared acceptance cases and 2 preservation/
  interruption cases. Source is outside Git at `/tmp/portal-started-focused-alias.py`.
  Process/socket observations were in memory, with separate symlink and socket
  metadata matching the proofs; fixture checks used read-only retained records
  and mocked rollout validation. No auth content,
  model/history RPC, real subprocess or private-data write was involved.
- Cases reject replaced alias or target, changed owner/mode/device/timestamps,
  changed readlink/resolution, altered proof linkage, foreign/replaced listener,
  wrong FD, missing/duplicate listener rows, writable files/directories and
  other links/sockets. Preservation checks confirm both proofs are copied and
  an interrupted claim cannot be reused; all writes in those checks are mocked.
- Earlier 48-check evidence and the temporary 61-check variant remain historical
  provenance at `/tmp/portal-started-focused-before-socket-mode.py` and
  `/tmp/portal-started-focused-proxy-mode.py`. They modeled the advertised path
  as a socket and did not establish the real alias contract. The current checks
  correct that model. The first current fixture check attempted read-only
  target metadata and refused PermissionError; rerun used separate proof-based
  alias/target mocks and passed, without changing runtime guards.
- `verify-creation.py` retains its exact earlier SHA256, preserving the native
  helper, extractions and every acceptance gate. AST/compile passed. Compared
  with `f49abcab`, the driver adds `require_socket_alias` and changes only host
  identity, fixture validation, proof preservation and argument plumbing in
  main. No private state or process was changed.
- Shared acceptance checks used synthetic values: a maximum of 15 seconds or
  median of 10 seconds remained incomplete, with all five samples and both
  faults retained. These numbers are not performance evidence.

## Prepared command

Run once after parent inspection and the retained independent review, using a
fresh operation-only watcher through direct SSH to `root@172.16.106.40`
(aitherdev), then `sudo -H -u aither` inside the runtime Nix shell. The parent
owns that host wrapper and read-only preflight. Run this command in that actual
host environment:

```sh
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-02-portal-creation-performance/verify-started-creation.py
```

Keep both proofs unchanged and available at their recorded private paths. Do not
repeat the historical `--resume-seeded` command or clear either claim. The
watcher reports the current command diagnostic separately from any retained
older result, then the final result/timings/fault conclusions if reached. The
parent owns acceptance and further action after any refusal.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-portal-creation-performance/)
