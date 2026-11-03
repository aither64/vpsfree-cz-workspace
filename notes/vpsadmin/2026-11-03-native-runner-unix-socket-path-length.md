# Keep native runner state paths short

The osvm native test runner constructs Unix socket paths beneath its
`--state-dir`. A long evidence-directory prefix can exceed the platform limit
before any product assertion runs.

In session2026-11-01-published-advisory-corrections, the four-target services-up/
WebUI batch failed in `osvm/shell.rb` at `UNIXServer.new`:163bytes given,
108bytes maximum. All three WebUI scripts failed setup; services-up was not run
because stop-on-failure stopped the batch. The setup exception preceded
shared-directory setup, virtiofs and process spawn; machine logs and absent
pidfiles supported cleanup reconciliation.

Keep detailed evidence at its descriptive path but give the runner a fresh,
unique short `/tmp` state directory. Check the longest actual socket path from
the selected osvm/config construction, including its generated suffix, before
launch. The corrected operation's longest path was64bytes. The short-path recovery subsequently passed services-up/user-core/lifecycle;
an independent admin pagination-test failure was corrected and all three admin
cases then passed under the same short-path convention. This setup fix itself
is separate from product acceptance evidence. Preserve the original failed logs and run only uncovered
checks after reconciling old owned effects.

See [session state](../../work/2026-11-01-published-advisory-corrections/state.md)
and its linked owner receipt for source/input, exact operation and outcomes.
