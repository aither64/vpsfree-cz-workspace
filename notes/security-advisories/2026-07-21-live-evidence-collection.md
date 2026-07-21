# Live advisory evidence collection

## Symptom

`bin/security-advisory collect` could not obtain a stable production snapshot.
Fleet-wide current revision checks repeatedly changed during component
collection. After separating current and historical evidence, reconstruction
also rejected an immutable event because its component digest did not match.

## Cause

Active Nodes normally report about every 30 seconds, so a multi-minute
fleet-wide quiet window is not attainable. A Node's current snapshot, retained
events, reconstruction state, gaps, and component rows share one evidence
revision and must be read inside the same per-Node consistency boundary.

The rejected historical event predated the optional software-component rename
from `vpsfree_cz_configuration` to `system_configuration`. vpsAdmin's current
API projects the current enum name, while the stored event digest correctly
retains the legacy serialized name.

## Fix and verification

Revision-bracket the complete evidence bundle one active Node at a time, and
retry only that Node when its revision changes. Check active inventory and
structural cgroup history around the fleet pass. Keep separate source filters
for current and event components. Reproduce a legacy event digest with the old
component name only as an exact compatibility fallback, then normalize the
accepted component to the current name. Both paths still require the full
stored SHA-256 revision to match.

Stored sampling gaps describe observation precision; they do not erase a
retained release state or boot/release event. Classify upstream stable releases
from the advisory's global introduction/fix boundaries and per-branch rules.
Inspect Linux CNA stable-backport introductions even when the branch predates
the mainline introduction. Represent an EOL affected range without a released
same-branch fix with an explicit null fix bound. Reject missing, inverted,
cross-branch, numeric-keyed, or noncanonical branch metadata so invalid YAML
cannot fall through to a global unaffected result.
Use a reviewed lifecycle start when a Node entered production after the global
history start. Missing configuration on a reconstructed affected release
cannot prove safety, so treat it conservatively as affected unless exact
evidence proves the relevant interface was unavailable.

The full 100-example suite, RuboCop, dossier validation, and installed commit
hooks passed. A live schema-7 collection then completed for all 13 active
Nodes, including 12 compute Nodes and one storage Node. All five evaluations
resolved without `unknown` or `vulnerable` Nodes. The ignored snapshot remained
local and no draft sync or publication was performed.

Related initiative: `work/2026-07-20-security-advisory-review/`.
