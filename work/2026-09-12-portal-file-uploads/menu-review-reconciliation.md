# Compact menu review reconciliation

Required lanes: general, architecture/repetition, scope/proportionality and
risk/compatibility. Model gpt-5.6-sol, xhigh, fresh context. High classification
because of the shared browser API/deployment boundary, with unchanged state.

General Important: separated-root destroy retained component-mutated hidden
state. Fixed by restoring the value observed at mount, with a provider contract
assertion. General Advisory: stale Go sums removed with go mod tidy; tidy -diff
passes. Architecture: no findings, real-browser acceptance pending.

Risk Important: cached baseline provider could append its controls into roots
hidden by the new markup. Fixed by leaving roots initially unhidden, using CSS
:empty while blank, and letting the current component hide populated empty
notice/card roots. Updated complete changed asset identities: conversation v6,
uploads JS v2 and uploads CSS v2. This also prevents new menu code receiving old
styles during an ordinary upgrade. Browser acceptance explicitly uses warmed
baseline/current caches and both form versions in both directions.

These are direct remedies within the reviewed ownership/cache boundary. They
were folded into the owning commits; pins were consolidated rather than adding
an update stream. No confirmatory general/risk rerun needed under the skill.
Scope review covers final heads in menu-revisions.json. Generated confctl update
was consolidated; its from/to revision and log-range changelog were corrected
intentionally to the actual baseline, preserving generated format/width.

Focused checks after fixes: five provider browser contracts and JavaScript
syntax, runtime web Go suite (28.3s), clean go mod tidy -diff and aligned workspace/
configuration deployment contract. Current provider/runtime CI green; organization
CI pending. Long browser/build/deployment verification follows scope completion.

Scope review completed at the final heads with no findings. All four lanes are
complete; all Important and Advisory findings are fixed. Post-review Firefox
acceptance, provider packaged checks, workspace package build and configuration
build started. No review reruns required for direct fixes.
