# Proposed prerequisite: preserve allocated identities before activation

Status: **historical, unverified mechanism proposal; scope approved and diagnosis
superseded**. On 2026-10-14 the user approved fixing impermanence within this
initiative and required understanding the root cause. See
[the established cause and remaining integration gates](impermanence-root-cause.md).
The dependency/preparation mechanism below is not an implementation instruction.
The final cause-driven correction is recorded in [design.md](design.md): the
accepted compatibility-preserving whole-specialfs callback revision supersedes
both this proposal and the later split-phase mechanism B/non-root restriction.
It remains a separate logical baseline-fix commit from the selector change.
No application changes, Nix evaluations or runtime checks were made by architect0
for this proposal. The lead owns implementation assignment and verification.

## Historical user alternatives (decision now made)

- **Include the prerequisite:** authorize a separate logical baseline-fix commit
  for critical backing-directory preparation and activation ordering in the four
  files named below, followed by review and runtime verification.
- **Defer the independent fix:** keep import-interface work within its accepted
  scope and record dynamic UID/GID preservation as an unmet acceptance criterion.
  Do not claim complete impermanence preservation or runtime verification.

The original import-only design excluded raw compatibility changes, which was
the reason for the scope question. The user's subsequent approval admits a
cause-driven correction; it does not establish this earlier mechanism's
sufficiency. Do not repeat the scope question or implement the candidate blindly.

## Problem and evidence

The new preservation fixture declares system accounts without fixed UID/GID
values, records an owned payload, adds an earlier-sorting account, switches and
restarts. Preserving those identities is an existing requirement, not a new
public interface. The unchanged 25.11, 26.05 and unstable raw modules explicitly
describe their early persistence mounts as preventing identity changes.

All three hosted impermanence cases failed on the post-restart UID assertion.
Both switches and the restart machine-id assertion passed. The later GID,
payload and ownership assertions were not reached. The unchanged explicit
unstable path fails too. This is strong baseline evidence, not an independently
executed baseline-commit reproduction. See
[the implementer's diagnosis](implementer-ci-impermanence-diagnosis.md) and
`ci-image-failure-artifacts/`.

The source-level failure mechanism has two parts:

1. NixOS stage 2 sources its early mounts only when `/proc/1` is absent. LXC
   supplies proc before starting the guest, so that boot path is skipped.
2. NixOS activation also sources the same mounts in its `specialfs` snippet.
   The legacy `users` snippet has no dependency on `specialfs`. The `etc`
   snippet depends on users, groups and specialfs; that does not place mounts
   before users. Impermanence's directory creator also depends on users/groups.
   Allocation can therefore precede visibility of the persisted UID/GID maps.

Do not attribute the failure to a release-wide sysusers migration. The inspected
legacy allocator revives `/var/lib/nixos/uid-map` and `gid-map`; the alternative
sysusers backend also has owned marker files below `/var/lib/nixos/uid` and
`gid`. Backend and generated-script checks remain part of implementation
verification.

## Exact product boundary proposed for approval

Only these standalone compatibility files are candidate product edits:

- `os/lib/nixos-container/stable/vpsadminos-25.11.nix`
- `os/lib/nixos-container/stable/vpsadminos-26.05.nix`
- `os/lib/nixos-container/stable/vpsadminos.nix`
- `os/lib/nixos-container/unstable/vpsadminos.nix`

Keep the latest-stable and versioned 26.05 files equivalent and every raw file
self-contained. Do not add a shared import that breaks downloaded raw files.
Older retained 22.11 through 25.05 files do not contain this newer mount
selection; no backport or support claim for them belongs to this prerequisite.

Companion scope is a focused activation-order check, diagnostic improvements to
`image-scripts/tests/nixos_rebuild.sh` if needed, and a concise explanation in
`docs/containers/nixos.md`. Preserve the allocation-order challenge and every
data/identity assertion. Existing selector/evaluation tests may be extended to
cover the ordering without replacing their current checks.

No release-map, alias, guest-lib selection, stateVersion, root assertion,
account allocator selection, UID allocation algorithm, template persistence
policy, host daemon/kernel, KB content or contract change is included.

## Prefer the existing activation dependency, with a first-boot gate

The smallest candidate for legacy account activation is:

```nix
system.activationScripts.users.deps = lib.mkIf
  (!config.systemd.sysusers.enable && !config.services.userborn.enable)
  [ "specialfs" ];
```

This appends an ordering edge without copying the mount generator or adding a
second mount invocation. It places the already-existing `specialfs` execution
before legacy users, independently of the stage-2 proc guard. Preserve any
other user dependencies. The backend condition avoids merging a dependency
attribute into the empty-string users definition used by sysusers/userborn.
These later systemd services do not need this legacy-users edge.

The dependency alone is **not yet a sufficient complete proposal**. On a fresh
image, the persistent source directories do not exist. The 26.05 diagnostic log
at lines 643 and 656 explicitly records creation of
`/persistent/var/lib/nixos` during activation. Pinned impermanence creates those
directories after users/groups; its initrd-only preparation is unavailable in
the container. Moving specialfs ahead of users also moves the mount ahead of
that source creation. Existing maps make this candidate suitable for the
observed restart, but new-image boot must not gain a failed bind/activation or
lose its first allocation maps. Do not mark the fix complete on the restart
test alone.

The whole impermanence directory creator cannot simply move before users: it
also creates user-owned paths and already depends on users/groups. Adding a
dependency back to that creator would introduce a cycle. Do not resolve this
by setting fixed IDs, changing the backend, persisting passwd files or repairing
ownership after activation.

## Proposed bounded source preparation and ordering

The proposed complete scope combines the dependency with preparation of missing
critical backing directories. Use this activation order:

```text
critical backing-directory preparation -> specialfs -> users
                                               users -> groups
                         users/groups -> normal impermanence creator
```

Derive sources from the existing compatibility mount selection. For the shipped
configuration, prepare missing root-owned allocation state at
`/persistent/var/lib/nixos`, its missing parents, and other selected critical bind
sources that must exist when specialfs moves earlier, such as
`/persistent/var/log`. Do not hard-code `/persistent` as a universal source.
Use existing mkdir/coreutils and root/0755 defaults for missing directories;
leave existing metadata and content untouched. The normal impermanence creator
retains its later responsibility for declared permissions. This is prerequisite
initialization, not ownership repair. No chown or UID/map repair is included.

The persistent backing filesystem must already be available or ordered by the
existing configuration. Do not turn an unavailable persistent filesystem into
an ordinary directory on the ephemeral root. A custom non-root prerequisite,
missing backing mount or dependency cycle must not be handled by guessing an
identity or moving the entire user-dependent impermanence creator earlier.

Reuse `specialfs` unchanged for source, destination, type, options, upstream
mount order and its existing util-linux handling. Add no second mount replay,
filtered callback, registry, sorter or generic mount/remount code. Do not add
operations that replace, stack or unmount live mounts. Existing upstream live
mount/remount semantics remain unchanged; the product change is ordering plus
preparation of absent prerequisite directories.

The exact supported integration for preparation before upstream specialfs must
be checked against generated activation definitions and their option types.
Do not copy its shell body merely to add a dependency. If the required ordering,
backing-storage checks or fail-before-allocation behavior cannot be achieved
within this boundary, return to the lead before expanding the mechanism.
The proposal is not claimed sufficient until those checks and runtime pass.

## Upstream interfaces and reuse limits

Source inspected for real 25.11, pinned 26.05 and the available 26.11 unstable
source contains `system.activationScripts` dependency lists and dry-activation
controls, the legacy users snippet, `specialfs`, and
`system.build.earlyMountScript`. The latter is a generated sequence of
four-argument `specialMount` calls, ordered using `utils.fsBefore` (source,
destination and declared dependencies). It is an internal NixOS interface;
verify it against the exact guest locks in the quick checks.

`boot.loader.initScript` exposes enablement, not a pre-activation hook. Its
generated `/sbin/init` delegates to the selected system's init.
`boot.postBootCommands` executes after activation and is too late. Do not patch
the generated init text or replace stage 2. `specialfs` already uses util-linux
and handles live mounts by remounting; the dependency candidate changes its
order, not its callback, number of invocations or existing semantics. This is
why it is preferable if the first-boot gate can be satisfied.

The pinned impermanence source is
[nixos.nix at 7b1d382](https://raw.githubusercontent.com/nix-community/impermanence/7b1d382faf603b6d264f58627330f9faa5cba149/nixos.nix).
Its source preparation and initrd behavior explain the first-boot qualification.
No additional Linux feature, syscall, host protocol or Nix CLI version is
introduced. Reuse the existing directory-bind implementation and utilities; no
new Linux mount API or mount implementation is proposed.

## Migration, activation and recovery

There is no schema, persisted-map format or host deployment migration. Old and
new guests can run on the same nodes; no coordinated host update is needed.
After adoption, guest rebuild changes activation ordering, and the next guest
restart exercises the corrected boot path. A live switch must preserve existing
mounts, IDs, payload and original numeric ownership. First boot must initialize
only absent allocation-state storage before allocation.

Previously changed identities and stale/wrong persisted maps are not repaired
by this change. Record such damage separately; automatic chown or map rewriting
would be an additional migration with different risks.

Rollback selects the prior guest generation/input. Existing maps and payload
remain readable because their formats are unchanged. A rollback restart can
reintroduce the baseline allocation-order defect, so do not promise preserved
identities merely because rollback loads the data. Preserve the old generation
and, for an affected real guest, its persistent dataset backup and recorded
numeric IDs before an operator-approved rollout. No production rollout is
authorized by this proposal.

## Planned verification, not executed

Quick checks after approved implementation:

- Evaluate exact supported guest inputs with legacy users and separately with
  sysusers/userborn. Verify the resulting dependency graph and generated
  activation order, no cycle, compatible option types and no mount work in dry
  activation. Confirm users runs only after its identity storage is available.
- Check raw standalone importability, latest-stable/26.05 equivalence and all
  original selector, alias, unknown-release, caller-lib and stateVersion checks.
- Inspect both the fresh-source and existing-source paths, source/destination
  dependencies, configured options, a matching live mount and a conflicting
  mount. Test prerequisite preparation and ordering with controlled
  command doubles before runtime where useful. An unavailable backing mount or bind
  failure must prevent allocation; verify rather than assume shell ERR-trap
  behavior is fail-closed.
- Run repository formatting/hooks and generated-template evaluation. Confirm
  only the four approved raw files plus bounded tests/docs changed. Commit the
  prerequisite separately and obtain independent final review before long tests.

Long checks, launched later only by the lead's authorized watcher:

- Retain/reproduce the baseline failing identity scenario using exact locked
  inputs and a preserved failed fixture. No duplicate baseline run is needed
  if equivalent diagnostic evidence is accepted and clearly labeled.
- Test a fresh impermanence image with no backing state, first switch, addition
  of the earlier-sorting account, second switch and restart. Keep the original
  expected IDs throughout. Check machine-id, UID, GID, payload and numeric
  ownership independently so one failure does not conceal the others.
- Run stable 26.05 and explicit unstable impermanence image cases on the final
  reviewed head, plus an actual 25.11 guest when claiming 25.11 runtime coverage.
  The nominal 25.11 image uses the shared stable builder and is not independent
  evidence of historical guest nixpkgs. Ordinary guest checks cover activation
  without persistence; preserve existing successful results but rerun relevant
  smoke checks after a raw activation change.
- Demonstrate the normal already-mounted switch path has no new mount stacking
  or identity changes. Exercise fresh-source creation and failed/conflicting
  mount behavior in disposable fixtures. Stop unexpected local kernel builds
  under the existing verification policy.

Approval covers the bounded prerequisite (dependency plus missing critical
backing-directory preparation), followed by verification, or defers the fix
with unmet UID/GID acceptance. It does not permit weakening preservation tests,
changing public release APIs, guest pins, stateVersion, root assertions, account
backends or persistence policy. No host, KB/contract or data-repair changes are
included. The diagnostic-only test edit currently held by the implementer is
not authorization for this product fix.

Historical scope question (answered; do not ask again):

> CI exposed a pre-existing impermanence problem: an allocated user's UID changes
> after restart, including with the unchanged unstable module. May we include a
> separate prerequisite fix in the four supported compatibility files to prepare
> critical backing directories and mount them before user allocation, or should
> we defer it and leave UID preservation explicitly unmet? This expands the
> accepted scope, which excluded raw compatibility changes; the proposed fix
> still needs implementation and runtime verification.
