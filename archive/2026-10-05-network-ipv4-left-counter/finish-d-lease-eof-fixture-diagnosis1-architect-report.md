READY for root acceptance. Appended [design.md:6330](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/design.md:6330).

- Source supports a fixture race: `File.exist?` can succeed before `File.write` finishes publishing `EOF`. The native interleaving remains unproved.
- Recommend one fixture-local publisher: write and close a sibling temporary file, then rename it. Apply to all three EOF publication sites.
- Preserve every assertion, five-second bound, generation-lock check and reaping obligation. No production mediator change is justified.
- Recorded affected hosted Ruby selections and exact D/E composition gates. No schema, runtime or rollback changes.

Only design.md changed. No checks, reruns, probes or runtime actions occurred; retained state remains untouched.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/)
