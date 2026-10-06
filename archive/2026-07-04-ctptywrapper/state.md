---
lifecycle: abandoned
---
# 2026-07-04-ctptywrapper

## Repositories

- `vpsadminos`: read from canonical bare repo at `repos/vpsadminos.git`

## Status

- Investigated current Rust wrapper behavior on osctld disconnect.
- Compared with historical Ruby and Go wrapper implementations.

## Commands run

- `bin/dev-session current`
- `git --git-dir=repos/vpsadminos.git show HEAD:ctptywrapper/src/main.rs`
- `git --git-dir=repos/vpsadminos.git show HEAD:osctld/lib/osctld/console.rb`
- `git --git-dir=repos/vpsadminos.git show HEAD:osctld/lib/osctld/console/console.rb`
- `git --git-dir=repos/vpsadminos.git show HEAD:osctld/lib/osctld/console/tty.rb`
- `git --git-dir=repos/vpsadminos.git show HEAD:osctld/lib/osctld/pool.rb`
- `git --git-dir=repos/vpsadminos.git show cbb271941^:osctld/bin/osctld-ct-wrapper`
- `git --git-dir=repos/vpsadminos.git show cbb271941:ctptywrapper/main.go`
- `git --git-dir=repos/vpsadminos.git show ac7f43191 -- osctld/bin/osctld-ct-wrapper`
- `git --git-dir=repos/vpsadminos.git show 205031b57 -- osctld/bin/osctld-ct-wrapper`
- `git --git-dir=repos/vpsadminos.git show HEAD:tests/suite/osctl/ct-console.nix`

## Results

- Current Rust wrapper keeps running when osctld's client socket closes.
  It sets `client = None`, continues polling the PTY and the listening socket,
  and accepts a later root client on the same socket path.
- Rust wrapper does not buffer console output while no client is connected.
  PTY output is read and discarded when `client` is `None`; a failed write to
  the client is also dropped before the client is cleared.
- The only current buffer is `LineBuffer`, used for partial JSON commands from
  osctld to the wrapper. It is bounded to 64 KiB and is not console output.
- osctld reconnects tty0 during pool/container load for containers whose fresh
  state is running (`Console.reconnect_tty0(ct)`).
- Older Ruby wrapper had a console output buffer, later limited to 4 KiB in
  commit `205031b57`, then removed in commit `ac7f43191`.
- Go prototype had a 32 KiB output buffer, but its commit message says it was
  not replacing the Ruby wrapper yet. Rust does not carry that buffer forward.
- Existing `tests/suite/osctl/ct-console.nix` covers round-trip console use
  after `sv -w 180 restart osctld`, but not replay of output emitted while
  osctld is disconnected.

## Open questions

- Whether to reintroduce a bounded output buffer in Rust depends on desired
  operator/user semantics during osctld crash or update windows.

## Cleanup

- No worktree was created and no code was changed.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
