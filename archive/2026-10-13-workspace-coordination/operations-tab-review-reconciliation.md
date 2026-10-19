# Direct Reservations link correction

Independent final review remains operations-clarity-review.md and its recorded
reconciliation. All four lanes, complete branch histories and no-migration
conclusion remain applicable. The new complete inventory and narrow range-diffs
are operations-tab-final-inventory.json and its referenced artifacts.

Live acceptance of the first clarity deployment found an initial-fragment startup
ordering bug. app.js awaits its conversation module before activating the selected
tab and emits the existing session-section-change event. coordination.js had
already paused for the hidden pane and listened only for clicks/hash changes.
It now observes that tab event; three templates advance the asset cache version.
A regression fixture starts the pane hidden, then activates it through the actual
event, verifying initial reads, pause and aborted reads. Ten browser tests pass.
A Chromium preview loads only the corrected coordination script over the actual
deployed backend and unchanged app.js; every original live assertion passes,
including the initial fragment and inactive-tab polling.

Direct inspection and focused checks verify this bounded fix under mandatory
review step 9. No new design, contract, authority, state format or recovery behavior
was introduced; no affected-lane rerun is needed. Production delta contains only
the polling listener, template asset versions and regression fixture. Ruby, Go
backend logic, host modules, package installation, worker envelopes and VM test
sources are unchanged. The prior exact-source VM results remain valid evidence
for those behaviors; successor packaged checks and exact-head CI run again.

The fix is folded into the owning portal commit. Both consumers retain one final
runtime pin update. Configuration's update was regenerated from its preceding
documentation commit through confctl, preserving its full generated changelog
and passing every hook. Deployed predecessors have explicit retained feature refs
and rooted source artifacts; no redundant pin history is retained. No migrations.

Merges remain paused, and aitherdev remains held through review and feedback.
