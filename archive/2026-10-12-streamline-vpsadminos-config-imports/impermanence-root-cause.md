# Impermanence allocation-map visibility: established cause

Source examined: `4a40154539bf6dc73d391c30326af255b4dc15b2` (diagnostic v2).
Hosted image workflow: `38562488356`. Evidence directory:
`ci-v2-image-failure-artifacts/os-test-logs-38562488356/`.
Architect investigation is read-only except for these session records; no
additional Nix evaluation or runtime was launched by architect0.

The implementer's independent source/map audit corroborates this diagnosis in
[its causal-evidence record](implementer-ci-v2-causal-evidence/diagnosis.md).
It retains the exact executed allocator, parsed map equality, console evidence
and numbered snapshots; the complete original artifacts remain authoritative.

The user has approved correcting the defect within this initiative, with the
explicit requirement to establish the cause rather than add an unexplained
workaround. Product implementation remains unstarted by this architect; the
lead retains its assignment and verification gates.

## Observed invariant failure

The following line numbers refer to each image's `test-runner.log` and the first
occurrence of each diagnostic block, not the later exception-message copy.

| Image suffix | Initial rebuild | Second rebuild | Restart | Account IDs before → after | Persisted map IDs after |
| --- | --- | --- | --- | --- | --- |
| `nixos-25.11-impermanence-6b983f22` | 3064 | 3169 | 3246 | 995:993 → 996:996 | 995:993 |
| `nixos-26.05-impermanence-458efe2b` | 3008 | 3113 | 3190 | 995:993 → 996:996 | 995:993 |
| `nixos-unstable-impermanence-7c9b9c0c` | 2406 | 2516 | 2591 | 995:993 → 996:996 | 995:993 |

All three retain the earlier-sorting account's saved map entries, UID 994 and
GID 992, after the second rebuild and restart. Visible and backing maps agree.
Machine-id, exact payload contents and payload numeric ownership 995:993 survive
both rebuilds and restart. These assertions are now observed independently.
Identity preservation nevertheless fails: the named account no longer denotes
the UID/GID owning its data. Successful byte/ownership preservation does not
make the account mismatch harmless.

For stable 26.05, `/var/lib/nixos` and `/persistent/var/lib/nixos` both identify
device:inode `76:385` before and after restart. Payload paths both identify
`76:13`. Explicit unstable has matching map-directory identity `76:6` throughout.
Thus the persistent maps were not erased or replaced; their eventual bind mount
is correct. The nominal 25.11 image uses the shared stable builder, so it is not
independent runtime evidence for historical guest nixpkgs.

## Concrete execution order

The generated activation script printed by the failed stable guest has:

```text
line 34  users
line 40    update-users-groups.pl
line 46  createPersistentStorageDirs
line 53  specialfs
line 69    source ...-mounts.sh
line 75  etc
```

The same ordering appears after the second rebuild and after restart (stable
log 3169 and 3246). The generated mount sequence includes the bind from
`/persistent/var/lib/nixos` to `/var/lib/nixos` and the `/var/log` bind. This is
concrete output from the failed system, not merely inferred Nix attribute order.

Its init script guards the earlier mount sequence with `/proc/1` absence at
line 37, sources it at line 53 inside that block, and invokes activation at
line 137. LXC supplies proc before starting the guest. The container boot trace
then reaches users through the activation ordering above.

The inspected legacy `update-users-groups.pl` loads visible uid-map/gid-map at
startup, allocates or revives IDs, writes passwd/group, and writes updated maps
under that same visible directory. It does not re-read the maps after a later
mount. Therefore:

1. Live rebuild sees the already-mounted persistent maps and existing accounts;
   the allocated identities remain stable.
2. Restart starts with an ephemeral root. The proc guard skips the stage-2
   persistence mounts, and activation allocates users before specialfs mounts
   their saved state. The new account IDs are written to ephemeral passwd/group.
3. Later specialfs exposes the intact old maps over the newly used ephemeral
   map directory. That explains why the final visible maps still say 995:993
   while account lookup says 996:996. Later mounting cannot repair passwd/group.
4. Data and machine-id persistence happens successfully; it does not correct
   the preceding account allocation.

The current evidence does not directly dump the hidden ephemeral map directory
at the instant before mounting. That is a limit of the capture, not a competing
cause supported by the evidence: source semantics, exact generated order,
intact backing maps and the account/map divergence establish the causal chain.

The four candidate raw modules are unchanged between baseline `1150e37b` and
diagnostic v2. Explicit unstable bypasses the new stable selector yet fails in
the same way. Classify this as an independent baseline activation-order defect,
not a release-selection regression or a test contract to weaken.

## Fresh boot, switch and backend consequences

The v2 stable failure diagnostics at lines 651–656 record initially absent
backing directories, including `/persistent/var/log` and
`/persistent/var/lib/nixos`. Pinned impermanence creates them after users/groups;
its earlier preparation normally belongs to initrd, absent in these containers.
An ordering edge alone would try the bind before fresh source creation. The
repair must address this prerequisite and preserve first allocation maps, not
only make an existing-state restart pass.

The ordinary activation ERR trap records failure and continues. A DAG edge
orders snippets but does not prevent user allocation after a failed preparation
or bind. The eventual correction needs an explicit pre-allocation visibility
check and an abort before the allocator on failed prerequisites. Dry activation
must remain non-mutating.

Legacy users is an attribute-form snippet; sysusers/userborn make it an empty
string and allocate later through systemd. Guard legacy-only modifications and
verify both alternative configurations still evaluate. Do not force an account
backend. This observed failure is not evidence of a sysusers release migration.

## Accepted correction and remaining implementation proof

The user approved the fix's scope, not a predetermined mkdir/dependency patch.
The repair invariant is settled: prepare only absent critical backing sources,
make their declared mounts visible before legacy allocation, verify visibility,
and retain all original IDs and data expectations.

Prefer existing upstream interfaces over replacing activation machinery. The
specialfs option value is a string; the option type is
`either str (submodule ...)`, with concatenating `types.lines` only inside the
attribute-form `.text`. Plain `types.str` uses equality merging. The actual
evaluation below rejects both adding `specialfs.deps` and using a separate
`mkBefore` string definition. Alphabetical snippet order or sibling
dependency ordering is not a replacement for the required dependency edge.

The lead's session-only evaluator completed on exact supported inputs; see
`activation-option-probe-rerun.json`. Baseline and `usersDependency` succeed on
real 25.11, 26.05 and locked unstable. `beforeString`, `beforeText`,
`specialfsDependency` and `normalizeApply` all fail. The native dependency
preserves upstream body/source once, puts mounting before allocation and omits
mount work from dry activation. It made no product changes and ran no VM.
These rejected equal-priority merges do not rule out replacing the whole value
at a stronger priority. The lead's later bounded probe
([expression](specialfs-value-probe.nix), [results](specialfs-value-probe.json),
[exit status](specialfs-value-probe.status)) passed on all three exact inputs.
`lib.mkOverride 90` with a structured specialfs value preserves the original
callback body/global early mount script, sources once, orders it before users,
omits mount work from dry activation and leaves guest `mkForce` effective. This
is composition evidence using old raw modules, not final product validation.

Direct `options.system.activationScripts.apply` extension is not available:
all three inspected supported sources already use it to add the generated
normal activation script. `lib/modules.nix` rejects duplicate apply declarations.
Changing only an already-generated result would also risk differing normal and
dry activation. A normal `coercedTo` type extension is not a compatible merge
with the existing `either` type: the latter requires matching type names and
compatible children, and `coercedTo.typeMerge` returns null. These are source
findings, not additional architect-run Nix evaluations.

The accepted implementation brief is now in [design.md](design.md). It
supersedes the named critical-state activation and non-root backing restriction
implemented at `29e268350`. Restore complete specialfs promotion and the global
upstream mount order. For legacy users with the selected `/var/lib/nixos` or
`/var/log` binds, replace the whole specialfs value at priority 90, prepare only
missing sources inside those callbacks, verify live identity/mount success,
and explicitly abort before users on a failed prerequisite. Ordinary callbacks,
systemd units and alternative backends retain their behavior. Do not add a
second activation mount replay, overwrite live mounts, repair IDs/maps/ownership,
alter guest pins/stateVersion or weaken the dynamic allocation challenge.

All six image cases passed workflow `38582595251` at exact `29e268350`. That
establishes its supplied-image behavior, not root-backed/custom compatibility
or healthy old-to-new migration. The revised brief requires normal pure checks
and a registered upgrade suite for those remaining implementation gates.

The image build scripts declare `/persistent` as an automounted host bind of
the container's persistent dataset and `/nix` as its own dataset bind before
guest init. `osctld` separately creates the ephemeral root in
`commands/container/start.rb:293` onward. This establishes availability for the
shipped layout without a guest block device. Persistent-root/custom directory
sources remain valid; a source need not have a mount ID different from `/`.
Existing declared early covering mounts must be present before source creation.
For undeclared host mounts, directory/mount identity cannot distinguish absent
storage exposing stale directories from a valid root-backed layout. Retain the
prior source-path contract and state that limit; do not invent a durability
heuristic, new storage policy or impermanence-schema requirement.
