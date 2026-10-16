# Why the persisted allocation maps were missed

Read-only diagnosis of published v2
`4a40154539bf6dc73d391c30326af255b4dc15b2`, hosted image run
`38562488356`. No application edit, Nix evaluation, new runtime operation or
backend change was made by the implementer. The lead owns verification and the
architect owns the accepted correction design.

The defect is allocation before the persistent `/var/lib/nixos` bind becomes
visible. The maps are preserved and mounted eventually; that happens too late
for the activation allocator. This is an existing compatibility-ordering defect
exposed by the allocation challenge, rather than a selector regression.

All three impermanence cases have the same complete pattern:

| Case | After both switches | After restart | Stored maps and payload |
| --- | --- | --- | --- |
| 26.05 | UID 995, GID 993 | UID 996, GID 996 | Maps still 995/993; payload owner still 995:993 |
| nominal 25.11 | UID 995, GID 993 | UID 996, GID 996 | Maps still 995/993; payload owner still 995:993 |
| explicit unstable | UID 995, GID 993 | UID 996, GID 996 | Maps still 995/993; payload owner still 995:993 |

Machine-id and payload contents remain equal to their original values. Both
visible maps are exactly equal to their persistent counterparts, and their
complete JSON contents after the second switch are identical after restart.
The visible and backing directories report the same device/inode. In the
26.05 case `/var/lib/nixos` is `76:385`, and the payload is `76:13` throughout.
These observations exclude destroyed backing state or wrong numeric payload
ownership as the immediate failure. They do not claim that a post-boot mount
was already present during allocation.

The primary 26.05 `machine-shell.log` snapshot starts at line 3147, the second
switch snapshot at 3252, and restart snapshot at 3329. The indented duplicate
restart snapshot starts at 3773. The excerpts here preserve original LF line
numbers, matching `grep -n` and `sed -n`. All three
cases' numbered snapshots and a parsed map/invariant comparison are retained
in this directory. `invariant-audit.status` is 0.

The actual generated activation trace is decisive:

1. `users` starts at generated line 34, invoking the Perl allocator at 40.
2. Impermanence's `createPersistentStorageDirs` starts at 46.
3. `specialfs` starts at 53 and sources the existing mount script at 69.
4. That mount script includes the `/persistent/var/lib/nixos` bind to
   `/var/lib/nixos` at its line 13.

The actual generated init has its early mount source at line 53 under the
`/proc/1` absence guard at 37, then calls activation at 137. LXC supplies proc
for container init, so the reliable container path must also order activation's
existing specialfs before the legacy users snippet. Stage 2's guard alone is
not the complete explanation: activation does mount these paths, after users.

The exact executed allocator is available read-only at
`/nix/store/dyx8qsmgnsz2csfzwn723gbd2jvp0j7g-update-users-groups.pl` and copied
here. All three generated activation traces name it. Its SHA256 is
`686354fabf960cc1602508f1a14c467bdc8b7a148f8c8daa71d4cd5aaf5990bb`.
It reads both maps immediately at lines 10–14. A missing file yields an empty
map; malformed JSON fails instead of silently discarding it. Lines 69–88 revive
recorded IDs, and previous map values also reserve IDs against fresh allocation
at 107–109. Lines 196 and 284 write the selected IDs to the maps before writing
group/passwd. Thus interpreting the existing maps incorrectly cannot explain
successful account changes with the original map contents untouched. The
allocator wrote to the transient directory; the later bind concealed those
writes and exposed the original persistent maps. There is no sysusers or
userborn transition in these actual traces.

The fresh-source path is also established. At 14:46:32 the initial
`test-a8-2722` boot reports creation of `/persistent/var/lib/nixos` during
activation, along with its absent parents. At 14:48:03 the same test restarts as
`test-a8-119f` without those warnings. An ordering edge alone would move the
bind before the existing after-users creator on first boot, where its source
does not yet exist. It would then risk failed activation and losing the initial
maps. Moving the entire creator before users is unsuitable for user-owned
directories and can create a dependency cycle.

The minimal causal correction must prepare only missing critical backing
directories, run the existing mount implementation before account allocation,
and refuse allocation when preparation or the required bind fails. Existing
activation's ERR trap records failure and continues, so dependency ordering
alone does not enforce that refusal. The session option probe evaluates actual
25.11/26.05/unstable option shapes and dry activation behavior; its synthetic
preparation text is not a production implementation or runtime validation.
Do not rely on alphabetical snippet names or sibling dependency order.

`raw-baseline-equivalence.txt` proves each of the four candidate raw modules
has the same Git blob at initial base `1150e37b1cc997b1728f2fda806a3433ef55b798`
and v2. The nominal 25.11 image uses the shared stable 26.05 builder and is not
historical 25.11 runtime evidence. The source-level and artifact evidence
establish the cause, but no syscall trace captured the transient map read or
hidden directory. No corrected runtime outcome is claimed. The independent
baseline correction belongs to its own logical commit after the architect
records the accepted design.
