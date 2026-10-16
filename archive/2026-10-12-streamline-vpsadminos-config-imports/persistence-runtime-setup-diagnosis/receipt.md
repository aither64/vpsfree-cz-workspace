# Registered upgrade setup correction

Source: `96b69056cb16017dfef2c9a73a1acc755c032b72`, initially clean.
Only `tests/suite/dist-config/nixos-persistence-upgrade.nix` is changed,
unstaged. Index and refs are unchanged. Source is frozen for the lead.
Session/current and live roster revision 18 match the trusted binding;
implementer0 retains Sol/xhigh/workspace_write and both env markers are absent.

## Evidence and classification

Read the retained attempt ownership/invocation/status and runtime log; inspected
the full runner/command stream and failure diagnostics, along with complete
console and machine event logs. The build completed through guest closures,
host squashfs and test JSON. Seven scripts stop at dataset lookup and one stops
in LXC pre-mount; none reach preservation assertions or guest allocation.
This is test setup failure, not product behavior acceptance or regression proof.
All original artifacts and managed state remain intact. `original-logs.json`
records their paths, line counts, sizes and hashes; selected numbered excerpts
and all command/status records are alongside this receipt.

1. `ct mounts dataset <ct> / /persistent` fails because
   `osctld/lib/osctld/commands/container/mount_dataset.rb` joins the literal
   argument to the root dataset name. `Zfs::Dataset` preserves that name, so the
   lookup becomes `tank/ct/<ct>/`. The seven errors show that exact trailing
   slash. The CLI manual describes subdatasets only. Image builders' `dataset:
   /` is a different input: `Mount::Entry.load` explicitly substitutes the root
   dataset before constructing it. There is no equivalent root shortcut in the
   mount-dataset command. Empty strings/dot guessing or provider changes are
   unwarranted.

   The suite now uses the normal `ct mounts new` command with `--fs #{rootfs}`,
   retaining bind/create=dir/rw and default native ID mapping. `rootfs` was
   queried from this same container and is its private root directory, exactly
   the directory used by the image's root-dataset binding. This test does not
   export/import or move containers, so a fixed source path is appropriate.
   The persistent dataset and guest storage definitions do not change.

2. Root-backed startup fails while mapping the shared store. Original
   `machine-shell.log` lines 30953-30960 show root and nix private ZFS mounts
   succeeding, then mapping `/nix/store` fails with code 32 and
   `mount_setattr() failed: cannot set ID-mapping: Invalid argument`. Lines
   30962-30968 show LXC aborting its pre-mount hook/rootfs setup. No guest init or
   activation runs. The diagnostic `df -h` identifies host `/nix/store` as an
   overlay. The mount JSON shows `map_ids: true` for that shared store, inherited
   from the CLI default. `CtPreMount` maps every mount with this flag, directly
   explaining the failing command.

   The shared read-only store setup now passes documented `--no-map-ids`, as
   supported by `osctl/lib/osctl/cli/app.rb` and used in the existing ct-mounts
   test. This prevents an unsupported ID-mapped overlay bind; it preserves the
   ordinary read-only closure sharing. Native ID mapping stays enabled on all
   container root/nix/persistent datasets. No guest/backend/ID/ownership change.

## Exact edit and static evidence

`setup.patch` contains two changed setup commands and four explanatory comment
lines. A byte-level expected-replacement comparison proves every other suite
line, including all identity/map/data/metadata/mount/allocator assertions, is
unchanged. No fixture correction was needed. The previously corrected absolute
nix dataset private-source profile remains untouched.

Known parser, prepared nixfmt --check, prepared Ruby -c on the static template
with all conditional bodies, and git diff --check passed. The template contains
placeholder Nix values; it is not evaluated-script or runtime evidence.
`static-checks.txt` records this and the frozen suite hash. No Nix evaluation,
build, runtime, staging, commit, ref, push or lifecycle action was performed.

The concrete setup causes are established. Successful startup, old-to-new
switch/restart preservation and negative allocator gates still require the
lead's quick checks/review/fresh exact-head runtime attempt. The six hosted
image passes reported by the lead establish supplied image behavior separately;
they do not resolve the blocked upgrade acceptance.

The normal runtime selection remains `dist-config/nixos-persistence-upgrade#*`.
The parent owns the fresh short state root, metadata, watcher and all execution.
