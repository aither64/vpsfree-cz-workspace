# Applied declared-payload fixture correction

The parent reported runtime43016 terminal1 and authorized application of the
accepted constant-marker proposal. Applied only the exact proposed suite at
HEAD `edb90d2fe2190d88d8b9d2d21bd0def79eedc898`. Product file
`tests/suite/dist-config/nixos-persistence-upgrade.nix` SHA256 `685d34b22f83d2a354989c48927feb7f1ac722d15903d2f343021d24a700b3eb` matches the assigned expected full file.
The complete diff is20insertions,0deletions in that one file. Removing the
insert.nix-fragment from the applied suite restores before.nix byte-for-byte;
all other product source, raw modules, fixture definitions, guide and index
remain unchanged. No assertions or snapshots were removed or relaxed.

The declared-only block stays after oldInitial and before first payload.
It checks backing/payload exact mountpoints, source/target identity and shape,
both constant-marker emptiness predicates with explicit find failure exits,
then initializes only the empty mounted placeholder using the allocated
preservation-test account. Device/inode and source identity remain checked
after install. No old guest was modified or resumed.

Approved static checks all passed: prepared nixfmt, Nix parser (no evaluation),
static combined Ruby-c, extracted guest Bash-n, whitespace and empty index.
Commands/statuses are in static-checks.log/.json. Actual suite exactly equals
proposal/proposed.nix. These are syntax/source checks, not guard/guest evidence.

Current source.patch SHA256 `64614b640bea8ee07b5eecca42b2ee49c4f34f28ed26f549beb4a15be9b1da39`; inverse.patch retained.
Original accepted proposal/evidence remain unchanged in ../proposal/.
No Nix evaluation/build, callbacks/harness/VM/runtime, live guest fragment,
hooks, staging, commit, ref, push, lifecycle action or nested agent was launched.
Source is frozen and unstaged. Parent owns final-source evaluation/input
comparison, hooks/fold/narrow review/publication and NEW declared-backing
acceptance. No production or runtime success is claimed here.
