# Reading atomically published private receipts

The first direct portable campaign in `work/2026-10-05-network-ipv4-left-counter`
failed during readiness with a named/opened receipt inode mismatch. The runner
publishes process receipts by atomic rename while engine/control readers consume
them. The exact interleaving was inferred from source and the reported error;
it was not independently reproduced on the failed guest campaign.

The State reader now restarts at most three complete validated reads when both
named and opened snapshots are safe but dev/ino differ. Each mismatched descriptor
closes before retry. Unsafe paths, mode/owner/type/size, missing files, I/O and JSON
failures still refuse immediately. Lock inode/flock validation is unchanged.
This yields one complete receipt snapshot, not newest multi-record consistency.

Hosted K Check37916587198 at 7dc4d708 passed 44 runtime cases and 392 assertions, including deterministic
real atomic replacements, descriptor closure, safety refusals, forced readiness
interleaving and synthetic public stop compatibility. No local tests ran. These
checks do not prove live guests or recover incomplete retained ownership evidence.

A new stop fixture initially exceeded the runtime's 100-byte UNIX socket limit
because Nix CI supplied a nested TMPDIR. It now uses a short private root under
/tmp while retaining0700 XDG runtime isolation and the production path guard.
Native failed37915315928 remains evidence of that fixture failure.

The actual failed campaign has an incomplete process receipt despite later exit
observations for all recorded processes. Its missing final receipt cause remains
unknown. Preserve it and its claims; a reader repair is not orphan recovery or
permission to stop/reset/clear ownership manually. The accepted subsequent route
uses fresh roots and explicitly disjoint ports under the same resource registry.
