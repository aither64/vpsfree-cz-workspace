# Original retained start17669: effects reconciliation

Original public `start <slug> --existing`, selected ns0/ac34, exited1 after
58.549714s. Recorded native interval:2026-10-31T11:02:41.899673Z to
11:03:40.428575Z. No retry, guest request, source/build/eval, stop/recovery,
GC/storage repair or lifecycle action was run by E3. A0 owns the layout diagnosis.

**No guest launch or retained promotion is observed.** This conclusion uses the
unchanged owned runner log/timestamps and exact runner/socket/process/disk
observations below, together with the native path's guard-before-runner order;
it does not infer effects merely from exit1.

- Driver3613463 and native/launcher3613589 are absent. The original scope is
  not-found/inactive/dead and its recorded cgroup no longer exists. There is no
  remaining recorded child. Systemd's default Result=success for the vanished
  transient unit is not treated as native success; native result remains1.
- Public status exits0: stopped/not-ready/single/bridge, identical to preflight.
  Runner PID/ready files remain absent. All previously recorded runner/QEMU/
  virtiofs PID candidates remain absent; socket ownerUID1000/mode0700 is retained,
  zero socket nodes. Structured baseline and current state both contain17 stale
  socket pid files with PID values from the same before-set. Earlier prose's16
  was a counting error; the saved structured baseline already recorded17.
- Applied pending remains null. Services toplevel6dsi and every saved boot
  payload/hosttools field match preflight. All four guest proofs still match
  their immutable source receipts. Applied envelope file mtime/ctime predates
  the attempt, current SHA256def320a126057467d8f44f23c7ad53acbe117e364b9bc25a9ab5e7757b0380ed.
- Result selection remains
  `/nix/store/isj7505havzk1s606p10akz4d7lcxnj1-os-test-vpsadmin-devcluster-2026-10-24-vpsadmin-haveapi-upgrade.json`.
  Its symlink identity/mtime/ctime predates the attempt. No applied-boot.json was
  published. Preflight did not save the full envelope/result hashes, so this is
  a saved-field/provenance/identity/timestamp comparison, not an invented full
  before-byte equality proof.
- **A native configuration rewrite did occur:** config.json mtime/ctime falls
  within the attempt, with mode0600 and current SHA256
  `10819c2d393795f4909695f04e4caf3d4035a94e84e25c871ecfc1ab19a16332`.
  Exact before bytes were not captured in this preflight; no content-equality
  claim is made. No shared state was edited during this reconciliation.
- All four managed disks retain exact before device/inode/size/owner/preserve
  identities and positive sizes. Disk contents were not read or claimed equal.
  The final64KiB of the existing runner log and its mtime exactly equal preflight.
- All39148 recorded canonical/rollback private entries retain bytes and metadata;
  canonical33d6/inode51940894 and rollbackaae/inode52098765 remain exact. This is
  comparison of recorded entries, not a new exhaustive content inventory.
  Six actual provider SSH/certificate files and the three React credential files
  all have content/metadata timestamps predating the attempt: no generation,
  rewrite or rotation is observed. Current hashes/identities are retained only
  privately; no exact preflight credential-hash snapshot is invented.
  Guest hook/JSON/key state was not queried while stopped.

[Process/public status](process-status-effects.json),
[cluster/applied/result/disk effects](cluster-effects.json),
[protected source/private effects](private-effects.json),
[parent original result](result.json). Original stderr remains at the parent's
private path; an exact copy and private identity records are retained under
`/tmp/implementer3-retained-start-effects-i6ir9m0b` mode0700/files0600. Its copy SHA256 matches the parent's saved
stderr hash: True.

E3 has no active operation or product writer. Parent owns further action and the
held machine; A0 owns exact-field diagnosis. Original source/evidence remain.
