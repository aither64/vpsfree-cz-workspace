# Campaign parity diagnosis

Campaign exited 0 without retries at frozen b85ec364057f536940d689b09e612512ffffaf82.
The lead accepted the narrow analysis-only exception below after the architect independently verified the reconstruction. Timing analysis is recorded in package-d-campaign-report.md.

Runtime, host, activated gems, lock/input hashes and loaded feature sets match.
Exact source graphs differ only the assigned Context implementation and, in Rust
mode, its adapter. All four HTML body digests and all Rust code digests match
strictly. Concentrated-actions context bodies match strictly.

Many-resources descriptions and context raw JSON digests differ only in the
insertion order of the root resources Hash. HaveAPI.resources enumerates
Module.constants without sorting; Server#describe_version retains the resulting
route order. HTML templates sort resource/action maps.

The bounded no-timing diagnostic script package-d-description-diagnostic.rb
loads baseline and candidate with identical prepared unbundled Ruby environments,
performs OPTIONS only for each shape, and retains complete actual authorized
descriptions in the original campaign's parity-diagnostic directory. No timing
campaign, source edit or Git mutation occurred. The actual descriptions compare
equal for every key/value, with different resource insertion orders.

A Python structural comparison then enumerated only the eight top-level resource
key permutations, holding every other serialized byte fixed. It reconstructed
every original description SHA-256 and byte count exactly. Combining each exact
reconstructed description with the fixed profile/sample lane sample bytes also
reconstructed all 80 original context trial SHA-256 and byte counts exactly.
The retained order-proof.json records the original orders, canonical structural
digests and matched trial counts. Actual and reconstructed JSON bodies remain
intact. No field was removed or value normalized.

Accepted exception: compare only the many-resources description/context JSON
structurally after the exact digest reconstruction proof; keep status, bytes,
all values, other key order, and all rendered HTML/Rust digests strict. The
architect and lead accepted this exact scope before medians were interpreted.
