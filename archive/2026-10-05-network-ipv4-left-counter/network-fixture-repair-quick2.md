# Fixture repair quick2 packet

Quick1 stopped at scoped Ruby lint: syntax passed, with seven
`RSpec/ExpectInHook` offenses in the new restoration checks. API and W checks did
not run. The original quick1 wrapper, manifest and logs are retained.

The V teardown now collects explicit restoration errors rather than RSpec
expectations. It completes all recorded quota restoration and fixture deletion
before reporting discrepancies, including IDs and original/current row data.
Worker exceptions still fail the example. Both ordinary worker errors and RSpec
expectation failures are handled during joins so they cannot skip cleanup.
No lint policy or exemption changed. W fixture bytes and the component helper
remain unchanged from quick1.

Prepared command, not executed by the implementer:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/run-network-fixture-repair-quick2.sh
```

The wrapper retains the same four sequential steps and head guards, stops on the
first failure, and uses the new `network-fixture-repair-freeze2.sha256` manifest.
Its own subshell captures aggregate output/status in
`fixture-repair-quick2-wrapper.log` and `.exit`; individual steps retain their own
logs/exits. The outer shell disables `errexit` only while recording the subshell's
status. The subshell enables `errexit` itself and is not part of an `||` list, so
a failed gate stops subsequent steps. Existing output paths refuse overwrite.
