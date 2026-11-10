# Linux repository review performance

Implement the first delivery stage of the accepted portal performance proposal:
make committed comparison metadata independent of blob reads and line statistics,
bound rename detection, and isolate missing/large/slow content to individual files.
Affected repository: dev-workspace. The Linux repository supplies read-only
benchmark inputs. No production Git configuration or other session state changes.

The second proposed stage (larger paginated inventories, browser editor eviction
and controlled partial-clone preparation) remains follow-up after the core path.
The first stage must retain existing staged/unstaged capture guarantees, durable
comparison IDs, permissions and object identity checks. Explicitly represent
unknown line counts rather than claiming zero changes or binary files.

Compatibility: additive response metadata; no manifest, saved comparison, database
or operation journal migrations. Browser assets ship with the backend. Preserve
old saved comparison references and old response handling. Deployment is a later
workspace user-profile update, not a system pin or default-branch merge. No merge
or deployment was requested. Keep branches published for review.

Documentation: update README entry-point behavior and docs/workspace-portal.md
for operators and portal users. Keep exact benchmark and rollout evidence here.
Verification: targeted Go/browser checks, missing-object and rename fixtures,
read-only real Linux metadata/content probes, independent final review, then
appropriate full package tests/CI. Preserve bounded process/output/time limits.
