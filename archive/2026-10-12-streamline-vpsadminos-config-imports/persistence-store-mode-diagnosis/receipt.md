# Fresh /nix fixture traversal mode

Frozen, unstaged two-line suite change on clean reviewed/published
`6abc650f378a8cd4cc8ef4ecc25d74929ab6e1ed`, tree
`9393d0e2ef98af874f845934f49a8f79fcd15a33`. Identity matches the bound
session; both environment markers remain absent. Retained roster revision 18
has implementer0 ready with Sol/xhigh/workspace_write. Applicable workspace
guidance is unchanged; repository AGENTS/policy are byte-unchanged since the
prior assignment. No index or unrelated product changes.

## Cause and boundary

The completed focused attempt `runtime-attempt.dymifpby` selected only
upgrade-26.05 at that exact head and retained `/tmp/ni.ljm4450b`.
Its runtime status is 1, result unexpected_failure, and VM is terminated.

`machine-shell.log:196-211` shows copying the bounded closures into the private
native-mapped /nix store succeeded in 86.81 seconds. Container start succeeds
at lines 253-262. Readiness then remains degraded before any old live switch,
healthy baseline snapshot or input update. The failure-only diagnostics run
and retain/re-raise the original timeout.

The failed set is now dbus-broker.service, dhcpcd.service, nscd.service and
dbus.socket. Logrotate-checkconf is absent; the old wrong-owner rejection
does not occur in the actual logs. The remaining service execution attempts
report EACCES; the old generated units still execute nsncd/dhcpcd as their
named users and broker launches a child after dropping credentials.

The concrete setup omission is established by the existing source chain:

- `osctld/lib/osctld/commands/dataset/create.rb` creates and mounts the dataset,
  calls create_private!, and registers its /nix mount.
- `libosctl/lib/libosctl/zfs/dataset.rb:83-93` creates that private root with
  mode 0750. `Mount::Entry#fs` returns exactly this private_path.
- `Container::MountDataset` selects map_ids=true; CtPreMount maps that actual
  private source. The log confirms native mode and the /nix private ID map.
  Mapping preserves mode bits and exposes the native root owner as guest root.
- The suite creates store/profiles below this directory and copies store
  entries, but never provisions the already-existing /nix directory's mode.
  A root-owned 0750 parent denies traversal to unrelated service users even
  when the executable below it is 0555. Root init/osctl exec can still work.

The normal image build has a different layout initialization: the exact stable
nixpkgs tarball builder creates an ordinary `nix/store` tree with mkdir -p,
archives its parent directory and root ownership, and
`image-scripts/include/nixos.sh` extracts that complete tree. The impermanence
image then configures its /nix dataset from that populated image. It does not
leave a new raw create_private! placeholder as /nix. Normal traversable /nix
mode is 0755. The generated nix-daemon tmpfiles rules provision store/var,
not the /nix root, so they do not correct this suite omission. This comparison
uses the normal build layout/source, not a newly built or measured guest image.

This proves a fresh-fixture traversal defect and supports the small setup
correction. No live guest stat/pathwalk was performed on the stopped VM, and
the next runtime must still confirm resolution of every remaining EXEC error.
No noexec, unrelated hardening or provider defect is asserted.

## Exact correction and static checks

Only `tests/suite/dist-config/nixos-persistence-upgrade.nix` changes, adding
these lines inside the existing checked setup heredoc, immediately after
set -e and before closure copying:

```sh
# The fresh dataset root is 0750; /nix needs non-root traversal.
chmod 0755 "#{nix_root}"
```

The path is the existing queried private source for /nix. This is provisioning
the newly created empty fixture filesystem before its accounts/data exist.
There is no recursion, chown, account/map/ID repair or persistent-state-source
metadata change. All generation roots, software, stateVersion, storage,
switches, diagnostics/readiness and preservation/failure assertions remain
byte-for-byte unchanged.

`prepare-static-evidence.py` verifies the exact expected two-line addition and
its inverse; removing it recreates HEAD byte-for-byte. It also checks HEAD's
suite against the prior frozen setup SHA256. `mode-setup.patch` and
`scope-comparison.txt` contain the diff and passing comparison receipt.
`original-logs.json` hashes all original attempt metadata/logs; hashes were
rechecked unchanged. Source and runtime excerpts are in `source-evidence.txt`
and `runtime-evidence.txt`; originals remain intact.

Passed, all exit 0:

- Prepared nixfmt --check and nix-instantiate --parse on the suite.
- Prepared Ruby -c on eight static amendments of the retained evaluated
  registered scripts: eight Syntax OK results. These are syntax fixtures;
  no new Nix evaluation or script execution is claimed.
- Bash -n on the actual copy heredoc with inert path placeholders.
- git diff --check and exact expected/inverse source comparison.

Current suite SHA256:
`9275ca80ba39615e76a96cd9c0d7138a32116693b74da81a577021af5cca65f3`.
Diff: one file, two insertions. Index empty; source frozen.
No Nix evaluation/build/runtime, stage/commit/ref/push or lifecycle operation.

The parent owns folding, affected review, actual generated-script evaluation,
hooks and the next focused runtime. The previous session export
`persistence-store-fixture-diagnosis/generated-scripts.nix` remains suitable
for all eight actual script strings at the reviewed final source. Reuse normal
discovery/hook commands, then a new owned exact-head diagnostic attempt for
`dist-config/nixos-persistence-upgrade#upgrade-26.05`. Do not reuse the failed
attempt's paths. No upgrade acceptance is claimed before a healthy old guest
and all old-to-new preservation checks pass.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-12-streamline-vpsadminos-config-imports/
