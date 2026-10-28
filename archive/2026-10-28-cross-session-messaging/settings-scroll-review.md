# Settings scroll correction

User reports Automation scrolling Settings tabs out of view. Review runtime
f199947c..HEAD in owned dev-workspace worktree. General and architecture lanes;
low risk, no API/state/security/protocol changes. Fix uses existing sidebar
keyboard pattern: history.pushState then hashchange, avoiding native fragment
scroll while preserving dependent listeners and popstate. Adds viewport and
Back/Forward assertions in existing Chromium/Firefox acceptance test; bumps
all app cache selectors together to64. No new feature design or docs needed.
Folded into Settings owning commit; complete six-commit branch remains coherent,
no migrations, same pin stream. Final tree equals pre-rebase fixup snapshot
f89b3f98 exactly; conflicts were only cache versions62/63/64, resolved to64.
Quick syntax, composer and shipped-client tests pass. Prior review remains
applicable; review this bounded follow-up before affected browser/build batch.
No integration authorized. Updated deployment pins will be mechanically amended
and consolidated, unchanged extension and native. Same verified Sol/xhigh
reviewer; read-only, no nested agents or long tests.

Final mechanical pins: workspace58298dc0ed6f41993c9c3cc9c52db4299ed5ab4e; config43f064ab2206f8f8586ab0a05b5601d21bc12026.
Both select2caa9419, input hashsha256-i2LaP14ZxIGTqlIUmnKUlWrKfWt35gOmMTDGePGpmqA=.
One final pin per stream, config changelog covers real4a002f52 predecessor.
Only pin identities changed; extension and siblings preserved. Composition check passed.
