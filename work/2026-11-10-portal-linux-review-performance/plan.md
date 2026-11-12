# Linux repository review performance

Implement the first delivery stage of the accepted portal performance proposal:
make committed comparison metadata independent of blob reads and line statistics,
bound rename detection, and isolate missing/large/slow content to individual files.
Implementation owner: dev-workspace. Linux supplies benchmark inputs. The
authorized deployment below also updates matching workspace/configuration pins;
its operational recovery and shared-object index repair are recorded separately.

The second proposed stage (larger paginated inventories, browser editor eviction
and controlled partial-clone preparation) remains follow-up after the core path.
The first stage must retain existing staged/unstaged capture guarantees, durable
comparison IDs, permissions and object identity checks. Explicitly represent
unknown line counts rather than claiming zero changes or binary files.

Compatibility: additive response metadata; no manifest, saved comparison, database
or operation journal migrations. Browser assets ship with the backend. Preserve
old saved comparison references and old response handling. The application is selected through its user profile, with the configuration
selecting the matching host contract. Deployment and integration were explicitly
authorized on November 12 as recorded below.

Documentation: update README entry-point behavior and docs/workspace-portal.md
for operators and portal users. Keep exact benchmark and rollout evidence here.
Verification: targeted Go/browser checks, missing-object and rename fixtures,
read-only real Linux metadata/content probes, independent final review, then
appropriate full package tests/CI. Preserve bounded process/output/time limits.

## Authorized rollout (2026-11-12)

The user directed: "you can deploy aitherdev using vpsfree-cz-configuration.
merge after verification". This authorizes aitherdev deployment and subsequent
master integration of the portal feature and its necessary configuration and
workspace runtime pins. Scope: dev-workspace, vpsfree-cz-configuration and
workspace. Preserve unrelated inputs and the selected vpsFree extension.

Use configuration's dev-workspace/devWorkspace channel and the workspace's direct
nested runtime input to select the published 02881b40 feature. Build the composed
profile and aitherdev system before activation; acquire the exact configured
machine near dry-activation/switch. Verify system/profile identities, portal
health and real Linux metadata/content reads, naming and conversation continuity.
Then integrate the reviewed exact heads into their remote masters under separate
short repository claims and release the machine after complete lineage proof.
No reboot, session archival or branch deletion.

Existing application review and feature CI cover exact runtime 02881b40. Pin
changes are mechanical; verify the exact final input graph and contract.
No state/schema migration or Codex upgrade. System recovery retains confctl
auto-rollback; workspace selection uses ordinary guarded forward recovery.
Individual rollout evidence belongs in rollout.md/state.md, not project docs.

## Rollout recovery and acceptance

The user subsequently directed restoring the offline portal immediately. Resolve
only verified stuck assignment wrappers, complete the original system operation,
and check public HTTPS as well as backend health. Preserve active Codex work.
Live Linux acceptance exposed a stale multi-pack index; refresh that shared
object index once without fetching, repacking, deleting objects or changing
any session branch. All original four-second Git limits remain in force.
Both operations succeeded; exact identities and evidence are in rollout.md/state.md.
The initial three approved feature heads were merged and their master CI passed.
No stage-2 feature was added to this delivery.

## Automatic line counts correction

The user needs additions/deletions to judge changesets in repository overviews
and diff headers, including unopened/collapsed files. Automatically calculate
counts for each frozen comparison, independently of metadata and preview loading.
Reuse the existing bounded Git runner, single-flight cache and HTTP admission.
No new job framework or automatic fetch/maintenance. Initial master CI passed;
follow-up commits preserve the already merged history. Acceptance includes both
registered NFS example repositories and the large Linux comparison.


The final automatic-count correction and full-index preview flag have passed
independent review, complete package/system verification and live NFS/Linux
acceptance. The final heads are deployed and merged; machine ownership is
released. Final feature CI passed. Master fast/host/archive checks passed; its creation
job exposed an unchanged fork-settings race, documented separately without a
blind retry. All delivery work for repository review is complete.
See state.md and rollout.md for exact source, deployment and measurement evidence.
