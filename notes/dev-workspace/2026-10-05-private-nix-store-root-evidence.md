# Evidence from a private Nix store

The retained-selection regression in the vpsFree workspace provider uses a
fresh `local?store=...&state=...&log=...` store for each case. Nix child commands
receive that store explicitly; the fixture performs no builds or GC.

Three verification failures exposed separate issues:

- The command stub expected an internal validation message, but the public CLI
  reports a generic diagnostic and the fixture suppresses warnings. Per-attempt
  mock refusal events establish the cause without changing the public error.
- Nix imports read-only trees. Implicit `Dir.mktmpdir` cleanup raised EACCES and
  could replace an earlier test error. The fixture now records only its own
  pending exception, restores its Nix environment, makes its exact private store
  writable without following symlinks, and uses ordinary FileUtils removal.
  Secondary cleanup failure preserves the primary error; cleanup-only failure
  still fails. This applies only to the current test's temporary directory.
- With Nix 2.34.8, `nix-store --query --roots ITEM` reports
  `ROOT -> ITEM`, not a bare root path. The registrar requires that exact pair,
  a successful query and the exact root symlink. Mocks use the same format.

All six actual-Nix cases passed after these corrections. They cover raw JSON
with empty registered references, selected payload roots, exact source items
with identical JSON bytes, and refusal cases. This is registration evidence;
no survival-through-GC observation is claimed. Full provider checks and the
native DNS scenario have separate status in the session record.

## Linux names in the native build monitor

A broad pattern matching any derivation name containing `-linux-<version>`
also matched module trimming and initrd packing. Two native launches stopped
before examples. Parent inspection of the exact derivations established that
one copies existing modules/firmware and runs depmod; the other uses
make-initrd-ng/cpio/compression with registered inputs. Neither compiles Linux.

The monitor permits only those two inspected derivation paths and retains its
cancellation rule for every other matching Linux build. This changes monitoring,
not source or test acceptance; the native result is recorded separately.

The subsequent native launch reached its example but failed because the long
artifact prefix produced a 122-byte Unix socket path (Linux permits 108 bytes).
The fixture puts its sockets beneath the artifact directory, so the owning
launch uses a short /tmp/ndns.* directory. The same observed socket is estimated
at 68 bytes with that prefix. Source and assertions remain unchanged; failed
artifacts are retained. Use short artifact paths for OSVM native fixtures.

## Preservation baselines and systemd readiness

The native preservation failure logged only a Boolean and did not persist its
original counter or disk-stat baseline. A counter read was followed by an
unlogged File.stat assertion, so the final shell command could not distinguish
which predicate failed. Keep bounded private baselines and comparisons before
exact assertions; never reconstruct an unmeasured old baseline from current
values. Raw projection rows and unknown counter names need not appear in
failure output: hashes and fixed-name numeric counters identify the boundary.

`systemctl is-active --quiet` with several units returns success when any unit
is active. A baseline that requires every counted service to have started must
check each unit individually. Stop an enabled timer before its oneshot service
and check both inactive states before collecting counters. This establishes a
fixture prerequisite; it does not attribute an earlier failure without its
missing evidence. Unexpected later restarts still fail exact counter equality.

A newly tracked `.diff` evidence file contains blank context lines consisting
of a single space. Git's whitespace checker reports those as trailing spaces
in the artifact itself. Preserve the exact reviewed patch and its digest;
check prose/JSON separately and validate that the artifact warnings are only
those required context-prefix lines. Do not trim or silently alter the proof.

[Session evidence](../../work/2026-09-23-storage-redesign/state.md).
