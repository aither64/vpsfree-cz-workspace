# Ubuntu 26.10 container image design

Design owner: architect0, retained GPT-6 Astra/xhigh, workspace_write.
Prepared on 2026-10-16 against vpsadminos
`0ffcc1da559c6d76e593e691e113d1e9349eebf1`.

## Scope and implementation boundary

Add the Ubuntu 26.10 minimal x86_64 image and its declarative image repository
entry. The lead accepted the three-file scope below. Implementer0 owns the
application edits; the architect owns this brief. Refer changes to shared
builders, helpers, runtime behavior, test framework or tag policy through the
lead if concrete verification evidence makes them necessary.

| Intended file | Change |
| --- | --- |
| `image-scripts/images/ubuntu-26.10/config.sh` | New file containing `BUILDER=ubuntu`, following 26.04. |
| `image-scripts/images/ubuntu-26.10/build.sh` | Copy the current 26.04 script, changing only `RELNAME=resolute` to `RELNAME=stonking`. Preserve file modes and the existing script conventions. |
| `os/configs/image-repository.nix` | Append `"26.10" = { };` to the existing `images.ubuntu` set. Keep all existing entries and tags unchanged. |

In particular, retain the Debian and systemd includes, the
`configure-systemd-console-getty` call before `run-configure`, existing package
and SSH setup, and resolver cleanup from the 26.04 template. Do not copy the
older 25.10 script, which lacks the console-getty adjustment.

Ubuntu 26.04 keeps `latest`, `stable` and `lts`. Adding this release does not
change what consumers requesting existing aliases receive. An untagged interim
release also follows the existing 25.04/25.10 repository entries. Tag promotion
would be a separate design decision.

## Upstream evidence and sources

The official [Ubuntu release announcement](https://lists.ubuntu.com/archives/ubuntu-announce/2026-October/000330.html)
and [26.10 release notes](https://documentation.ubuntu.com/release-notes/26.10/)
identify Ubuntu 26.10 as **Stonking Stingray**, released on 2026-10-15, with
support until July 2027. Its archive suite is **stonking**.

The lead fetched full Release metadata from both the
[primary archive](https://archive.ubuntu.com/ubuntu/dists/stonking/Release) and
[Czech mirror](https://cz.archive.ubuntu.com/ubuntu/dists/stonking/Release).
The [retained metadata receipt](upstream/ubuntu-stonking-metadata.txt) records
their matching SHA-256 and relevant fields. Both declare
`Suite: stonking`, `Codename: stonking`, `Version: 26.10`, publication date
`Thu, 15 Oct 2026 12:18:34 UTC`, architecture `amd64` among the supported
architectures, and components `main restricted universe multiverse`.
The [upstream suite listing](https://archive.ubuntu.com/ubuntu/dists/)
also lists `stonking-security` and `stonking-updates`.

Use the existing `BASEURL=http://cz.archive.ubuntu.com/ubuntu/`. Generate the
same three APT lines as 26.04, substituting the new suite: `stonking`,
`stonking-security`, and `stonking-updates`, each with all four components.
Keep normal archive signature verification; no insecure bootstrap options or
new package sources are needed. The architect shell could not resolve the
mirror, so the lead's fetched evidence and the browsing results establish
availability; they do not establish a successful image build.

## Interfaces, discovery and compatibility

The directory name supplies distribution `ubuntu` and version `26.10`.
`osctl-image` supplies the established defaults: architecture `x86_64`, vendor
`vpsadminos`, variant `minimal`. The Ubuntu builder at
`image-scripts/builders/ubuntu/config.sh` remains Ubuntu 24.04; its setup
installs curl, debootstrap, patch and wget. There is no dependency on publishing
the new image before its builder can be created.

`image-scripts/include/debian.sh` already handles suites missing from the
builder's debootstrap package: for Ubuntu it links the missing suite name to
the existing `gutsy` script and invokes debootstrap with `--arch amd64` and
locales. Reuse this behavior. It covers suite recognition, not a proof that all
new packages can be bootstrapped by this builder. Package installation,
signature handling and boot compatibility remain targeted-test gates.

Ubuntu's release notes identify systemd 261. Keep the 26.04 console-getty
helper, which applies to systemd versions >= 258. Treat this image as requiring
the same unified cgroup environment as Ubuntu 26.04; do not claim legacy
cgroup compatibility or alter host policy to accommodate it. The existing
`tests/distributions.nix` puts Ubuntu 26.04 in `cgroupv2` and `systemd`, while
its Ubuntu selection omits the existing interim releases. Leave that selection
unchanged: those tests consume already published images, whereas this task's
image test builds the candidate locally.

`tests/all-tests.nix` discovers non-abstract directories under
`image-scripts/images` and instantiates `tests/suite/image-scripts/test.nix`.
The new directory therefore registers `image-scripts/test@ubuntu-26.10`
automatically. No explicit test registration or new test implementation is
needed. The generic Ubuntu distribution implementation in osctld delegates to
Debian and does not require a new release registration.

The repository module at
`os/modules/services/osctl/image-repository/default.nix` already accepts the
distribution/version entry with an empty option set. Its existing build path
resolves the image name `ubuntu-26.10`; vendor and variant defaults remain
unchanged. No repository schema, container metadata format, ZFS layout,
database/migration, API, generated client, CLI, Terraform interface, service
protocol or Nix module option changes are introduced.

## Deployment and recovery implications

This deliverable supplies build definitions; it does not publish an image or
deploy a repository host. A later authorized rollout would install these
scripts and the repository definition on the image builder, build/test the
release, and publish it through the existing image repository workflow.
Existing release builds and aliases remain available throughout.

No coordinated update of all running nodes or existing containers is required.
The new userspace still depends on host capabilities, especially cgroups and
the host kernel; the targeted test establishes compatibility with the tested
vpsAdminOS revision, not every older deployed host. No Ubuntu kernel is
installed as the container's running kernel. Unsupported older nodes should
continue using their existing supported images.

Reverting the three-file addition stops future scheduling of this release and
restores the prior source configuration. It does not downgrade existing
containers or automatically remove an already published image from a repository.
Any later publication rollback must separately manage that repository artifact
under its normal operational authorization. Existing formats remain readable
by the previous software, and old aliases retain their prior destinations.

## Acceptance criteria

1. Only the three intended application files change; 26.04 and shared helpers
   remain intact. The new build script differs from 26.04 only by suite name.
2. Image discovery reports Ubuntu 26.10, x86_64, vpsadminos/minimal with the
   existing Ubuntu builder. Repository evaluation contains the new entry and
   retains exactly the previous Ubuntu aliases.
3. Shell syntax, Nix parsing/evaluation and required project hooks pass. All
   intended changes are committed before independent final review.
4. The whole branch passes independent review, including the explicit absence
   of migrations, before the long image test starts.
5. `image-scripts/test@ubuntu-26.10` builds the new rootfs and passes its existing
   applicable boot, shutdown, systemd, console, package, hostname, password,
   resolver, network and SSH tests. Record exact head, command and result.
   A bootstrap or boot failure is evidence to diagnose, not permission to
   broaden the implementation silently.

## Verification brief

Run from the lead-created worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-ubuntu-container-build/vpsadminos`.
Use the repository Nix environment and mandatory hooks. These commands are a
plan; the architect has not run checks against an implementation.

Quick checks after implementation:

```sh
bash -n image-scripts/images/ubuntu-26.10/config.sh
bash -n image-scripts/images/ubuntu-26.10/build.sh
git diff --check
nix-instantiate --parse os/configs/image-repository.nix >/dev/null
nix eval --impure --json --expr '(import ./os/configs/image-repository.nix { config = {}; pkgs = {}; lib = {}; }).services.osctl.image-repository.vpsadminos.images.ubuntu'
diff -u image-scripts/images/ubuntu-26.04/build.sh image-scripts/images/ubuntu-26.10/build.sh
```

The comparison must show only `resolute` becoming `stonking` (its expected
exit status is 1). The Nix expression evaluates the declarative image selection
without building a host; `--impure` permits its local-path import. The
`.#vpsadminos` development shell does not expose the `osctl-image` command, so
do not use it for a public CLI listing. The targeted CI test below exercises
the public command inside its vpsAdminOS VM. If obtaining the shell itself
requires an uncertain-duration build, delegate environment preparation under
the monitor skill rather than leaving a long foreground operation. Commit with enabled
Overcommit hooks, or run the repository-prescribed
`nix develop --command overcommit --run` as appropriate to the lead's hook setup.

After the committed deliverable passes independent final review, use the
existing image-scripts CI workflow for targeted verification. Its selected
image case invokes:

```sh
./test-runner.sh test image-scripts/test@ubuntu-26.10
```

Use a fresh catalog-policy Luna/low watcher under `dev-session-monitor` to
monitor that CI run. Retain its run URL, exact tested head and targeted result.
A successful targeted CI run on the final reviewed head satisfies this check;
do not duplicate the successful image build locally.

The existing test uses a vpsAdminOS VM, a 24 GiB memory setting, the tank build
and output datasets, and a three-hour image-test command timeout. Its source
mount points at the CI checkout, and it invokes public `osctl-image test`
inside the VM. No full distribution matrix, new development
cluster or production image deployment is needed. Stop and escalate an
unexpected local kernel build under the workspace verification procedure.
Diagnose failed checks before considering retries; route any necessary design
revision through the lead. Record boot/runtime compatibility as unverified
until this targeted test passes.

## Documentation and handoff

Read `README.md`, `image-scripts/README.md`,
`docs/container-images/{creating,repositories}.md`, and
`docs/specifications/{container-image,image-repository}.md`, along with the
nearby release definitions and test discovery code. No project documentation
change is needed: this addition uses existing documented interfaces and adds no
new operator procedure. This brief and the lead's state record retain the
release evidence and verification limits.

The lead owns worktree registration, commits, final review, publication of the
feature branch, test monitoring and state updates. No application edits, commits,
builds, long tests or external publication were performed by the architect.
Session: [Ubuntu container build](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-ubuntu-container-build/).
