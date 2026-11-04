# Milestone 2 implementation and causal result

The cause is established and the minimal fix is committed and published.
The lead reports final 742 whole-branch review complete with no Blocking or
Important findings; a cached-builder documentation advisory is accepted as a
nonblocking follow-up. Rebuilt-image/candidate verification remains pending. No merge,
deployment, public image publication or session lifecycle action was performed.

## Cause and controlled resolution

The AA image was built with `--no-recommends` without explicitly requesting
`udev`. It contained systemd, libudev and the systemd network-tagging rule, but
neither udev's binaries nor its service/socket/trigger units. There was no udev
process, database or systemd tag index. eth0 existed and was up. The normal
osctld `/run/udev/control` stub was present before PID 1; it cannot process
events by itself. Both eth0 device-unit names remained loaded/inactive.

The preserved AA image is SHA256
`254523b59106db1d27bcf98e43e942c8ea1d7f0c15238542ca17e21612017214`,
source `aa963dce42859ae4251cdfaded91920d67b3a46e`. Its exact original runner,
VM JSON, kernel/system paths and source inputs remain in
[immutable inputs](device-unit-immutable-inputs.md). Original failure and
pre-install baseline records remain unchanged.

The successful [fixed experiment](device-unit-runtime-closure-restart-aa963dce4.rb),
SHA256 `81c36a5e2b01539953b71af440d80b9e724930810949db80d86b84ee9f3aeed1`,
used native zypper to download only udev's required dependency closure. Temporary
runtime addressing left eth0 inactive with udev absent. Guest DNS, routes and
address state and the host return route were restored before installation.
All 15 signed RPMs passed their hash/signature and whole-transaction dependency
checks. Exactly those 15 packages were added, with none upgraded or removed.
The full NEVRA list and individual hashes are preserved in the raw transcript.

Normal container stop/start changed init PID 3134 to 6034. The original eth0
still had no IPv4 address. Native assertions then returned:

- eth0.device status 0, active (plugged).
- dummy0.device status 3 before creation, then status 0 and active after
  `ip link add dummy0 type dummy`.
- udevd loaded/active/running and udev-trigger loaded/active/exited, both with
  successful conditions/results.
- A real `/run/udev/control` socket, udev database and systemd tag index.
- Initialized eth0 and dummy0 properties containing `SYSTEMD_ALIAS`,
  `TAGS=:systemd:` and `CURRENT_TAGS=:systemd:`.

No manual daemon start, daemon-reload, event trigger, service mask, privilege
change or kernel change was used. The temporary dummy interface was removed.
The native record has 104 completed command entries; the final marker is
`DEVICE_UNIT_CLOSURE_RESTART_PASS`. This proves the runtime cause and remedy;
it does not replace final-source image builds.

## Warnings and evidence limits

The live diagnostic RPM installation returned status 0 but emitted
`Failed to send reload request: Connection refused` and a Lua
`%transfiletriggerin(udev...)` failure. The exact signed udev RPM's trigger
checks only `posix.access("/run/udev/control")`, then asserts the result of
`udevadm control --reload`. Our pre-PID1 regular stub satisfies that existence
check while no udev daemon/socket exists yet, explaining the refused reload and
Lua assertion before the first udev boot. A normal clean restart subsequently
started udev and passed the actual device assertions. Do not relabel the live
installation as a clean scriptlet run or suppress those diagnostics.

The post-restart journal also reports an egress BPF attachment failure for
udevd and missing predictable data for persistent MAC generation on the virtual
eth0/dummy0 devices. Those messages were nonfatal to the observed daemon startup
and device processing: the unit results, initialized properties and device
assertions above all passed. This does not claim the BPF filter was installed or
that the warnings disappeared. No host policy or privilege change was made.
The MAC warning corresponds to the upstream v257 predictable-data path in
[link-config.c](https://github.com/systemd/systemd/blob/v257/src/udev/net/link-config.c).

Fresh rebuilt-image bootstraps must still be inspected for Lua/scriptlet, cpio,
OOM or other unexplained bootstrap failures, even if an outer RPM command exits
0. The runtime warning does not waive the normal clean-build requirement.

Full accepted causal snapshots:

| File | SHA256 |
| --- | --- |
| `device-unit-causal-aa963dce4-shell.log` | `683b4a3ecdcf6fba2deb2bb77e3480b348e26ef179a7c9130038732216f12a53` |
| `device-unit-causal-aa963dce4-console.log` | `c1f840bcd2af234ce2d4becfb7ac3c89d8b18ee425c1b04cc7052f0742013800` |
| `device-unit-causal-aa963dce4-pty.log` | `c99836a609c1fba4702dedd5040f0f682daf1e7c79cf77cc5710ddea17873f8f` |

The lead was asked to close the native diagnostic operation normally after
these snapshots were saved. Closure confirmation belongs to its utility receipt;
this record does not infer process exit.

## Source, checks and publication

Repository `vpsfreecz/vpsadminos`, target `origin/staging`; feature branch
`2026-11-03-opensuse-leap-image-build`, worktree
`worktrees/2026-11-03-opensuse-leap-image-build/vpsadminos`.

Final head `742eb30cb1a8b6766c85e915d26b0400e38244b1`, tree
`19f423e70ff439867d4bb27e8ed07b9c95fdb703`; worktree clean. Fresh fetch and SSH
remote proof show target `dd188397abe37d0bc33f4c5dfb3605206ce5e326` unchanged
and the remote feature branch at that exact final head.

Complete series:

1. `4c2a38bc02d1d10c208d478c01ec90057995825e` — use shared Leap 16.0 builder.
2. `57871a8e3f8f429e86e3ad6abf16de99a44e9416` — add the Leap 16.1 image.
3. `742eb30cb1a8b6766c85e915d26b0400e38244b1` — explicitly install udev in the
   shared openSUSE helper and remove the obsolete device-unit exception.

The third commit changes only `image-scripts/include/opensuse.sh` and
`tests/suite/systemd/device-units.nix`: +4/-12, preserving all original eth0 and
dummy assertions. A nearby comment records why udev must be explicit. No larger
project documentation change was useful for this conventional package choice;
the individual experiment and remaining rollout checks belong here.
The complete branch is seven files, +27/-14. There are no migrations,
API/protocol changes, host-state format changes or dependency lock updates.

`bash -n`, Nix parsing, repository nixfmt and whitespace checks pass. The full
declared `overcommit --run` passed RuboCop and Nixfmt; active commit hooks passed.
The message-only final amendment adds the performed causal/quick validation and
pending rebuilt-image verification in prose. It ran the active hooks, retained
the identical tree and was published with an explicit lease against
`c856aa1b9939d048407ea72d434b087aed42c4af`. The old head remains at
`refs/backup/2026-11-03-opensuse-leap-image-build/device-fix-c856aa1b9`.
Full-range `git range-diff` shows commits 1–2 identical and only validation prose
added to commit 3; `git diff c856aa1b9 742eb30cb` is empty. Prior successful source
quick checks therefore retain their scope; no broad check was repeated for prose.

The builder update stream was already consolidated by Milestone 1. No obsolete
dedicated-builder, fixup/WIP, repeated pin or transitional migration commits
remain in the proposed final series. Earlier AA source is supporting causal
evidence, with its retained historical refs/receipts, and is not final-source
runtime validation. The final reviewer must independently conclude whole-branch
history and migration provenance.

Superseded branch CI runs `41705503484`, `41705503560`, `41714540036` and
`41714540038` are confirmed completed/cancelled. Current-head runs
`41714889091` and `41714888844` were left untouched and queued at handoff;
CI results are pending.

## Compatibility and next verification

The shared helper's real consumers are Leap 15.6, 16.0, 16.1 and Tumbleweed.
Rebuilt/new containers gain udev. Existing containers and published images are
unchanged; an operator would separately install udev with the distribution's
package manager and restart the container. No existing container was deployed
or changed outside the disposable diagnostic guest. Older/newer hosts retain
the same namespaces, mounts, device restrictions and event interfaces. No
coordinated host/fleet update is needed. Image rollback selects the prior image;
this change introduces no persisted host format or API migration.

Removing the exception does not repair an older public `opensuse/latest`
archive. Candidate-backed checks prove the source fix locally; an unqualified
public-image CI case can still exercise the older image until a separately
authorized image rollout replaces it. Preserve that distinction and coordinate
publication/integration ordering through the lead; no publication is implied by
this source package or by local candidate aliases.

The [final review packet](review-final-packet.md) and
[prepared final verification](final-checks-742eb30cb.md) name exact source/config
inputs and commands. Lead-owned final retained review precedes the new long
normal image batch and candidate-backed assertions. In particular,
`opensuse/latest` means Leap, not Tumbleweed; receipts must bind each local
alias to its actual rebuilt image. No extra permanent matrix/framework or public
tag publication is required.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-opensuse-leap-image-build/
