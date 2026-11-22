# virtiofs pathname listeners retain PID files after daemon exit

The reduced KB qualification's G13 public stop completed its runner and all
14 recorded child exits, then refused socket-directory cleanup. Six ordinary
0600 virtiofs `.sock.pid` files remained. Its phase stayed `stopping`; the own
reservation was already released. Process completion and path finalization
are separate facts, and the native stop remained failed.

The pinned OSVM machine code starts virtiofsd with `--socket-path` and later
unlinks only the socket. virtiofsd 1.13.3 creates a companion PID file and keeps
its file lock, but dropping the handle does not remove the file. Its existing
`--fd` API consumes an already-listening socket and avoids creating that PID
file. K's prospective shared machine adapter uses this API while retaining the
existing OSVM daemon array and reapers. It pins only the directory/socket paths
created by that invocation for exact cleanup; old PID files gain no deletion
authority. Exact K725c/D91c/E02ed source/package checks and independent four-lane review
passed. The selected native daemon test proves its FD listener API and actual
TERM/wait contract. G14 then built and booted both reduced guests, but its
finite qualification failed an inode-observation command before API/PHP/lease
and resume. A separately selected ordinary public stop returned zero; exact
complete/gone/reservation/socket proof shows its new namespace was removed
without pidfiles. Disks and failed qualification remain retained. This is partial
ordinary-guest shutdown evidence, not a full stop/resume or capture pass.

Do not retry dead-state cleanup, whitelist PID-file names, infer unlink or
signal authority from PID-file contents, or treat a systemd unit's Result as
the native campaign result. Preserve the failed receipt and namespace. A fresh
campaign needs a separately recorded retention decision, complete named exit
proof, the own claim's absence, disjoint resources and measured admission.

Evidence and the bounded implementation brief belong to initiative
`2026-10-05-network-ipv4-left-counter`: `finish-corrected-g13-stop-refusal1.json`,
`finish-corrected-g13-residual-pidfiles1.json`, and the design subsection
“virtiofs pidfiles after complete G13 exit”. No old state was cleaned.
