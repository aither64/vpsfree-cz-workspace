# Fedora 45 container image design

Design owner: architect0. Investigation completed 2026-11-03; implementation,
independent review and image verification remain with the lead and implementer.

## Scope and evidence

Only `vpsadminos` is affected. Its SSH remote is
`git@github.com:vpsfreecz/vpsadminos.git`; live `ls-remote --symref` identifies
`staging` as the default branch at
`5918f94e5e4eef3733b60aca4e03c1a6c0d43748`. Canonical bare-repository inspection
used that revision, without accessing other sessions' worktrees. The previous
Fedora addition, `a246c260bef5e8b27a453c6dd244d840039e6ab8`, changed precisely
the two image files and the repository registration.

Live HTTP directory listings, checked on 2026-11-03:

- [Release packages](http://ftp.fi.muni.cz/pub/linux/fedora/linux/releases/45/Everything/x86_64/os/Packages/f/)
  returned HTTP 200 and listed `fedora-release-server-45-13.noarch.rpm`,
  `fedora-release-45-13.noarch.rpm`, `fedora-release-common-45-13.noarch.rpm`
  and `fedora-release-identity-basic-45-13.noarch.rpm`. Each exact RPM URL also
  returned HTTP 200 to HEAD. The repository release-discovery script's
  `common_fedora_versions` helper independently returned shared suffix `13`.
- [System packages](http://ftp.fi.muni.cz/pub/linux/fedora/linux/releases/45/Everything/x86_64/os/Packages/s/)
  returned HTTP 200 and listed `systemd-262-3.fc45.x86_64.rpm`.

## One implementation package

Assign one existing implementer the following three paths together:

| Path | Required change |
| --- | --- |
| `image-scripts/images/fedora-45/build.sh` | Copy Fedora 44's recipe, replacing the shared release RPM suffix `17` with `13` in all four URLs. Keep `$RELVER` interpolation, package list, shared configuration calls, NetworkManager keyfiles, hostnamed mask and console-getty configuration. |
| `image-scripts/images/fedora-45/config.sh` | Add `BUILDER=fedora`, matching Fedora 44. The directory name supplies `DISTNAME=fedora` and `RELVER=45`; architecture defaults to `x86_64`. |
| `os/configs/image-repository.nix` | Retain `"44" = { };`, add `"45"` with the sole Fedora `latest` and `stable` tags, and preserve Fedora 43 and rawhide. |

There are no independent application packages worth splitting. The files share
one image identity and should form one focused commit, conventionally
`image-scripts: add fedora-45`. Do not update existing release RPMs, rawhide,
other distributions, dependencies, builders or shared helpers speculatively.
Escalate a demonstrated need for shared changes to the lead before expanding
the package; shared changes require checks for the affected existing images.

### Distribution test integration

Keep `tests/distributions.nix` unchanged. Its existing `table.fedora` selects
`distribution = "fedora"; version = "latest";` and already appears once in
`cgroupv2` and once in `systemd`. Moving `latest` to Fedora 45 integrates the new
release into that matrix when its image is published. Systemd 262 fits the
existing cgroups v2 classification. This fulfills the image-addition skill's
test-integration purpose without duplicating the same release under explicit
`45` and `latest` entries or replacing the repository's rolling test convention.
`tests/all-tests.nix` discovers the new directory automatically for the separate
`image-scripts/test@fedora-45` test; no manual test registration is necessary.

## Interfaces, invariants and compatibility

Reuse `image-scripts/builders/fedora`, currently based on the published Fedora
44 image. This avoids needing Fedora 45 to build itself. The recipe keeps the
existing `redhat-family.sh` and `systemd.sh` contracts; all four bootstrapping
RPMs must carry the same observed `45-13` version. The package does not change
the image archive format, repository schema, APIs, CLI, database, generated
clients, host module options, kernel or daemon protocols.

Existing containers and explicit Fedora 43/44 selections are unaffected.
Consumers selecting Fedora `latest` or `stable` will get Fedora 45 after
publication. Fedora 45 needs the existing cgroups v2-capable container setup;
this does not introduce a coordinated update of all running machines. Mixed
host versions retain their current compatibility limits, to be exercised by
the established image test rather than inferred from the release number.

## Preparation and verification

The lead reports initial tracking commit `06898d32b` complete. Before assigning
edits, verify the same-session roster/access and create/register the dedicated
worktree from the default branch:

```sh
dev-session worktree add 2026-11-03-fedora-45-image-build vpsadminos --as-is --base origin/staging
```

This should create branch `2026-11-03-fedora-45-image-build` at
`worktrees/2026-11-03-fedora-45-image-build/vpsadminos`. Let the command fetch;
recheck the three-path plan if the target changed. No repository claim is
needed. Implementer must read local `AGENTS.md`,
`skills/add-image-build-script/SKILL.md` and the Red Hat release skill, plus the
workspace procedures applicable to edits, commits and checks.

Use the repository's `nix develop` environment. Its `.overcommit.yml` enables
Nixfmt and RuboCop; verify active hooks and use the standard
`overcommit --install` setup if absent. Run the declared hooks without bypass.
Write the commit message to a temporary file and use `git commit -F`, with
what/why in the body and lines at most 80 characters. The default shell may
need to install its declared Bundler dependencies; delegate uncertain shell
preparation/build waits according to the monitoring skill.

Quick acceptance checks before final review:

- `bash -n` succeeds for both new scripts; `git diff --check` succeeds.
- Nix parsing/format hooks pass for `os/configs/image-repository.nix`.
- Evaluate that module with empty `config`, `pkgs` and `lib` arguments and
  inspect `.services.osctl.image-repository.vpsadminos.images.fedora`: 43/44
  remain, 45 owns `latest`/`stable` exactly once, rawhide is unchanged.
- Confirm the existing test matrix still has Fedora `latest` in cgroupv2 and
  systemd. Stage the new files before Nix flake discovery so they are included.
- `./test-runner.sh ls 'image-scripts/test@fedora-45'` discovers the image test.
  The wrapper builds its runner first; delegate if preparation is not already
  known quick. Inspect the final three-file diff and complete commit series.

After the committed deliverable and quick checks pass, run independent final
review, including whole-branch history and the conclusion "no migrations".
Then a fresh verification watcher must launch and monitor:

```sh
./test-runner.sh test image-scripts/test@fedora-45
```

This test builds the candidate recipe in a VM and runs the established image
checks for boot/shutdown, packages, networking, SSH, passwords, hostname and
systemd. It requests 24 GiB guest RAM and allows up to three hours for the image
operation. Ensure KVM, sufficient capacity, outbound mirrors and the
vpsAdminOS binary cache are available. Stop and investigate an unexpected local
kernel build. No `osvm`/`test-runner` edits are planned, so use the wrapper's
prebuilt runner path. Record exact revision, result and logs; do not label the
image verified before this test passes. Inspect the image workflow after the
feature branch is pushed; it detects new image directories automatically.

Dist-config tests create containers from the public repository, not the local
candidate recipe. A current `fedora-latest` pass may still test Fedora 44.
Do not use it as Fedora 45 evidence without checking the downloaded version.
If image-test diagnosis requires new boot/service/shared-helper behavior,
coordinate extra targeted start/stop and systemd-rundir verification against
the actual candidate with the lead; do not add test infrastructure preemptively.

## Delivery and recovery

Build support and repository registration do not deploy a host or publish an
image. No configuration-repository pins or machine reservations are needed for
this package. Actual publication requires the image builder to consume the
approved revision, then successfully build/test Fedora 45 before clients can
resolve the moved tags. Integration into `vpsadminos/staging` requires separate
explicit user approval; feature publication alone is not integration.

Before publication, recovery is reverting the focused addition. After
publication, restore Fedora `latest`/`stable` to 44 in the repository builder
configuration and republish its metadata if rollback is required; confirm the
actual tag resolution. Existing Fedora 45 containers are not downgraded or
removed by a tag rollback, and the earlier image/host formats remain readable.

The existing image-build documentation already describes this unchanged
workflow. No new project documentation or user-facing prose is needed; retain
the exact release evidence and test results in session records. The lead owns
plan/state/portal updates and commits. This design creates no lifecycle action.

## Addendum: requested configuration channel updates

The lead relayed the user's scope expansion on 2026-11-03:
"when the change is verified, you can merge it + I'll need you to update staging
and os-staging channels in vpsfree-cz-configuration". This authorizes integration
of the verified image change into `vpsadminos/staging`. It requests the two
configuration channel updates, but does not explicitly authorize integration
into `vpsfree-cz-configuration/master` or any deployment. This addendum supersedes
the original single-repository scope and approval assumption above.

### Configuration package and dependency

One separate package can be assigned to implementer1 in
`worktrees/2026-11-03-fedora-45-image-build/vpsfree-cz-configuration`, on the
matching dated feature branch, based on fresh `origin/master`. Setup and hook
preparation are independent; the channel mutation must wait until successful
Fedora 45 verification and completed, remotely verified vpsAdminOS integration.
Do not pin the unmerged image branch.

Canonical inspection used configuration `origin/master` at
`c4107822060e9e34b24a83950d618c9f28a7722b`, confirmed by SSH `ls-remote`.
Its bare `HEAD` is an older master revision; do not use that as the new baseline.
The current channel mapping in `flake.nix` is:

| Channel / selected role | Root input | Its nixpkgs follows |
| --- | --- | --- |
| `staging / vpsadminos` | `vpsadminosStaging` | `nixpkgsStaging` |
| `os-staging / vpsadminos` | `vpsadminosOsStaging` | `nixpkgsStable` |

Both vpsAdminOS inputs use `github:vpsfreecz/vpsadminos` without a branch
override, resolving the upstream default `staging`. Both follow the existing
root `nixpkgsUnstable` too. At the inspected configuration baseline they pin
`b45b27b4330a08d85f413999e4bf66ba4503eee1`.
`staging` also contains `nixpkgs` and `vpsadmin` roles: always specify the
`vpsadminos` role to avoid updating them. Preserve production and every other
channel/input.

Use the published-revision update operation, not `set` or manual lock edits.
Current `.github/workflows/daily-update.yml` establishes this exact guarded
variant, using a newer confctl CLI without changing the configuration's own
confctl input:

```sh
nix develop -c nix shell github:vpsfreecz/confctl/822c0e35dbe2549111912f539116b4225dfd3035#confctl -c confctl inputs channel update --forward-only --commit '{staging,os-staging}' vpsadminos
```

Read the current workflow again at setup in case it changed. Its newer CLI is
intentional: the locked confctl `7bee58a...` predates `--forward-only`. The guard
requires a clean tracked checkout/index, one writer, a tracked version-7 lock,
and supported Nix (the packaged CLI supplies Nix). Install/sign the declared
Overcommit hooks inside `nix develop` as the workflow does before the generated
commit. Leave the vpsAdminOS changelog enabled and preserve the generated commit
message unchanged. A guarded rejection must be diagnosed, not retried without
the guard; a post-install hook failure can leave the candidate lock installed,
so inspect effects before retrying.

Expected generated application scope is **only `flake.lock`**, normally one
commit containing the two input updates and any required descendant lock
updates. `flake.nix`, channel definitions, nixpkgs selections, the confctl pin,
host modules and workflow files need no edits. Compare logical input paths and
locked identities rather than generated node suffixes. Inspect the full
old-to-new vpsAdminOS range: the current pins lag staging, so this update can
also import already-integrated changes beyond the Fedora addition. Record that
range and any transitive input changes rather than describing it as only a
three-file image diff.

### Bounded checks, compatibility and recovery

Save the pre-update lock outside the checkout. After the generated commit:

- Verify JSON validity, `git diff --check`, successful hooks, one logical update
  stream and an otherwise clean checkout. Confirm both vpsAdminOS pins resolve
  to the verified integrated revision. If upstream moved meanwhile, report and
  assess that newer range before accepting it.
- Compare the complete semantic lock graph: preserve unrelated root revisions
  and follows edges, and explain expected descendant changes. Export the final
  committed lock outside the checkout and run the same newer CLI's
  `confctl inputs check-update --old-lock <baseline> --new-lock <committed-final>`.
  Do not publish after a guard/evidence failure. The complete-graph check may
  fetch ancestry mirrors; monitor a long read-only check with the verification
  watcher, while the implementer owns the mutation and generated commit.
- Run `confctl inputs channel ls '{staging,os-staging}'` in the configuration
  environment and evaluate selected `confctl.buildPlan` input metadata for
  `cz.vpsfree/nodes/stg/node1` and `cz.vpsfree/machines/build`. The former uses
  staging; the latter combines nixos-stable with os-staging. Confirm their
  `inputsInfo.vpsadminos` resolves to the intended input/revision.
- Apply the mandatory-review skill's actual mechanical-update exemption and
  history requirements; do not add a review gate solely for generated pins.
  No full fleet build or deployment is needed for this lock-only request.
  An evaluation failure or unexpected substantive delta requires diagnosis and
  a revised check plan, not silent scope expansion.

These pins affect staging nodes, NixOS services using os-staging, and downstream
consumers following the selected vpsAdminOS inputs (including vpsAdmin service
inputs). Existing nixpkgs follow mappings preserve their channel separation.
The image addition introduces no schema or wire change; older and newer running
systems remain unchanged until separately deployed. Do not infer deployment
compatibility for all intervening upstream changes solely from the image test.

No machine reservation, activation, image publication or configuration-master
merge is part of this package. Before any deployment, its complete input range
would require the normal target-specific build/recovery assessment. Recovery
for this undeployed package is reverting its generated lock update; no live
state migration or container downgrade is involved. Keep feature publication,
pending configuration merge approval, exact input revisions and checks in the
lead-owned session state; no routine project documentation commit is needed.
