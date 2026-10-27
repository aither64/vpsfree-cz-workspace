# Own-command observation and availability continuation

Immediate `/proc` availability is not a required acceptance gate for these
directly launched, bound commands. It is supplementary observation. Retain
prelaunch selected/resolved executable/hash, exact literal argv (including the
legacy nix-store alias), cwd/environment, direct Popen with no shell, and owned
PID/session/group receipts as dispatch evidence. None proves command success;
actual exit, output validation, settlement and postflight still must pass.

## Saved facts and cause boundary

Only saved `runtime-f520-browser-graph-inspect-preparation-v2/` source/results
were examined after the required session/environment/own-roster check.
`launch.py:494` checks the selected tool's resolution/hash immediately before
`command`; lines97–100 directly Popen the recorded argv/cwd/env with
`start_new_session=True`. Lines109–116 take separate exe/cmdline observations
and require unconditional equality. These are non-atomic observations, not
the authoritative submitted argument array.

The actual root-DB command passed0/0.109s; recursive metadata passed0/2.145s.
The saved full selected graph contains3510 derivations,21325 edges,521 sources,
3577 selected outputs and7608 validity paths. Full root/direct equality and
complete traversal precede writing that graph in the frozen code. Raw recursive
SHA256 is `6a0ab1db260ca41c10af231a958bf46695c3a8f49e4769794562ede965359ddf`;
selected-graph SHA256 is
`f3d82b8b7786b9b954655668bda2101fa54d239f40f662a9c71b180da8163480`.

The third command's literal argv has7626 arguments/505693 NUL-accounted bytes.
Saved ProcExe is exactly pinned Nix; ProcArgv is `['']`. The old decoder maps
either empty bytes or a single NUL to that value; raw bytes were not retained,
so do not invent their length or the OS-level cause. The runner's equality
failure caused its owned SIGINT; actual exit-2 is not availability acceptance.
Outcome SHA256 `8de1ecbceca34b75cb351c7f35da83f86f9ae694717ce1e68655ce7febb80782`
remains failed1/8.575s, joined with no unsettled group and postflight PASS.
Both v1 and v2 failures and all original receipts remain immutable.

## Small owner2 adapter correction

Take at most one best-effort observation per optional proc field for the exact
owned child; no wait-until-match loop or new observer framework. Record fields
independently, so loss of cmdline does not erase an actual exe observation.
Use null plus an explicit unavailable reason for empty cmdline, absent proc
entry/child exit, or a recorded observation I/O error. Retain raw byte length
and digest when bytes were read and errno when a read failed. Do not infer
that the child exited merely because a field is unavailable; label exit only
when the actual child return status establishes it. StartTicks is optional
observation too; this does not alter owned-group settlement safeguards.

An empty byte string or one terminal NUL supplies no meaningful argv; it may
be unavailable without signalling or failing the command. For actual argument
data, remove only one terminal NUL and preserve all legitimate empty arguments.
An observed nonempty, contradictory argv or exe still fails: this pinned direct
invocation has no authorized wrapper/re-exec or argument rewriting. Do not
normalize whitespace, paths, suffixes, missing arguments or truncated arrays
into equality. Malformed nonempty data is not a matching observation. Never
copy expected values into observed fields or treat unavailable as observed PASS.
Ordinary deadline/cap/exit/group/output failures retain their existing behavior.

No stricter observation is essential for this owned no-shell command: its
dispatch inputs are already bound and its result is separately checked. Pure
byte cases should cover empty/missing observations, matching args with a final
empty argument, a nonempty mismatch and large argv; inspect the small source
delta and parse without launching a process. No product source or policy change.

## Reuse graph; finish availability only

The successor binds the old successful root/recursive command receipts, raw
JSON, complete selected graph, exact root expectations/direct metadata, and
old pre/postflight evidence. Verify hashes and the same complete graph/path
selection from saved bytes only; retain historical scope and timestamps.
Fresh ordinary current input/tool/source/lock/root-link guards and exact three
raw root files remain required. Perform the existing strict three-root DB
admission as a current prerequisite, then **only** the unfinished selected
availability query, using the identical7608-path union and fixed options.
No recursive-query, eval, instantiation, root registration or build repeat.

Reuse existing availability parsing and bounded selected-path existence checks;
retain actual DB-invalid and filesystem-absent lists separately. Missing selected
outputs do not imply a build occurred or permit restoration; root loss and
DB-valid/file-absent disagreement still refuse. Cache availability stays unknown.
Retain all current guard sets, argv/output/time caps, warning policy, settlement,
postflight and fresh no-clobber results. No command/result from the failed third
stage is relabelled successful. Owner2 prepares only this bounded adapter;
lead accepts/releases any execution. Session remains open.
