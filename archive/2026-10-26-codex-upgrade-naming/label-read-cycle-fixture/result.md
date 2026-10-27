# Badge read-cycle fixture correction

The extracted `refreshSessionDetails` fixture omitted the renderer that production
initializes before the details function is called. Its new `capture()` ran before
the fixture function’s try block and caused the observed ReferenceError.

Minimal correction imports `createThreadStatusBadge` and supplies an actual
renderer for the fixture element/thread. No product code, existing assertion,
concurrency wiring, or failure expectation changes. Existing no-op recovery
control callback remains unchanged; the newly required renderer is real.

Repository Nix syntax check and `node --test
portal/internal/web/read_cycle_browser_test.cjs` passed17/17, Node343ms. Full
command/elapsed/exit and original stdout/stderr retained alongside. Diff check
passes. Bounded source search of other CJS fixtures found no second extraction
of these changed badge-call sites; browser_contract uses the exported renderer
directly, while other fixtures only stub unchanged refresh calls. No broader
framework or checks selected.

Only read_cycle_browser_test.cjs changed (+2/-1); owner0 owns Git/folding into
the label unit and preserves prior published/deployed heads and failed receipts.
System deployment remains held on the failed final-profile prerequisite.
