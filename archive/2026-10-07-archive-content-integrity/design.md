# Lead design and verification brief

The lead owns design and implementation in this independent, threadless
initiative. Use xhigh effort for substantive work. No persistent team is added.

## Record integrity

The existing tree checksum serializes entry kind, relative path, permission mode
and bytes (or link target). New checksums omit the permission field entirely.
They still detect changed names, additions/removals, types, contents and link
targets. Archive/revive physically move records and retain normal Git executable
metadata; permissions are not a record-integrity prerequisite.

Keep one traversal with a legacy-permissions option. New writes use content-only
checksums. A shared comparison first checks the new digest, then the exact legacy
digest when needed. Apply it to archive source/prepared intent, projected target,
archived target and revived target. No journal/schema changes or receipt rewrites.
Legacy projections retain the old forced-0644 override semantics for exact proof.
Old package executors refuse unfamiliar new digests; pending lifecycle operations
already block package changes. Supported old records stay readable.

## Useful archive status

Keep the worker's typed public diagnostic but store the actual exception,
bounded to 16 KiB of valid UTF-8, in existing last_attempt_error. Preserve last
attempt timestamp and accepted operation identity. Do not add an error taxonomy,
API, queue or repair command. Existing API returns cached state without observing
live conversations or mutating it.

For a failed accepted archive, Settings and the existing archive failure notice
show a single error reason and timestamp. Use the existing Retry operation.
Move policy/schedule/activity information into the existing collapsed details.
Pending-operation and stale-observation notices are metadata, not extra causes
when a concrete saved archive error exists. Keep old cached records supported
and render error text through textContent. Apply the writing skill in the lead.

## Recovery, deployment and acceptance

The old archive's exact target is proven by changing only state.md from 0600 to
0644. Stop its automatic worker while doing that correction under session locks,
then run the matching ordinary archive retry. Do not change contents, root,
branches or journal evidence. Restore the timer after recovery.

Publish runtime and matched downstream feature pins. Review the complete
committed deliverable and histories after quick checks. Then build/test packages,
deploy the matched confctl aitherdev host and user-profile app, and verify actual
selected revisions, portal Settings and recovered journal absence. No other
machines or nodes need updates. Software recovery uses a newer corrected package;
workspace-host does not support backward profile rollback.

Quick checks: focused Ruby tests for tree integrity, archive/revive retry and
automatic errors; browser helper tests; JS syntax. Longer checks: packaged suite,
browser regression and matched configuration/application builds. Cover private
0600 records, 077 umask, already-complete lifecycle and chmod during interruption;
real byte/path/type/link mutations must still refuse. Cover a recorded legacy
checksum through normal retry, and prepared-intent source validation. Error
presentation must survive reload without duplicate generic blockers.
