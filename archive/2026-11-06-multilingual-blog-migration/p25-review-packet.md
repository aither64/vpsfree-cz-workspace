# P25 committed retention review packet

CONFIG `99c7d5ec122aa8b32aeb45fcc12bf19719c86287` → `76d7fcf191045ea5ddce332dce341a67610e0315`, tree `25a86a6c1333c587500837cc0d318600771a734d`.
Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/vpsfree-cz-configuration`. Source/index frozen and clean; no P25 publication
or runtime mutation. Seven changed files, 491 other tracked entries identical.
Exact blobs, commands, durations and 27 linked evidence hashes/sizes are in
[p25-source-proof.json](p25-source-proof.json), SHA256
`12d17af71d4129f7ad3d4421aeaf1e72fa4495f47ce425dac9a1ee662dce7375`.

User requested old-release pruning and permits uploads to wait for prune locks
but never fail solely through contention. The accepted brief is design.md:3873,
corrected at4009; implementation stays within its seven-file boundary. Keep five
newest successful distinct available payloads plus current/immediate previous/
floor; preserve pending/uncertain state and all receipts/control/assets/staging.
Prune only try-locks publication then staging, retires payloads by same-filesystem
renames, and performs fd-safe deletion afterward. Upload retains the existing
stage lock through commit, with normal blocking publication acquisition. No new
lock/schema/queue/post-upload cleanup dependency. Maintenance can still pause
during staging and prevent commit.

The one retention commit bundles its helper/module, affected existing fixtures
and reusable operations guidance because they implement and verify the same
operation. The staging extraction is required to avoid a second flock while
preserving the historical-restage race boundary. Protected references may exceed
five; audit/CSS/orphans/external copies mean this does not bound total disk use.
Finite existing transport timeouts still apply to stalled storage/network.

## Checks and limits

Parent59844 terminal0, watcher52641 terminal0/PASS. Atomic quick receipt reports
96.830s, complete=true: primitives13.899s (25 tests, six actual fixed-UID namespace
skips); upload2.567s (nine tests); static-module45.837s; upload-module34.510s.
All six executable/test blobs plus flake.nix/lock equal their before/after hashes
and committed blobs. Watcher's first readable observation already saw terminal
status; its brief observation duration is distinct from parent batch duration.
Six privilege cases still require the postreview integration phase.

First focused run retained: eight passes/one ERROR in11.383s. Missing pruned
archive exposed raw FileNotFoundError; explicit complete-retained-payload
rejection fixed it before the passing batch. No rerun of the passing batch.
A local precommit recovery-ref guard expected missing show-ref exit1 but got128;
it stopped before mutation. Normal rev-parse --verify --quiet resolved absence;
no repair/packing/deletion of refs. Preparation-only syntax/path mistakes also
failed before source writes; no hidden product attempt or live prune.

Normal hooks passed in declared no-lock-write CONFIG Nix environment, commit
14.635s. CommitMsg TextWidth warned at73 columns, within repository80 rule;
raw log retained. Main operations writing pass was applied by lead and returned.
Final guide SHA256 `37d0cc324fbad42c1444a3eacf7aa2ce8c9c0c30df38ac28d602dc93be71b904`.

## Whole branch history and compatibility

Complete review range `5941cdb3dda259e91c6a988a7dbf08c84700b326`..`76d7fcf191045ea5ddce332dce341a67610e0315`:

| Commit | Purpose |
| --- | --- |
| `b4a7f22a46c16be453052a37ac98fc4c39401a9f` | internal-dns: add the blog container address |
| `8a4eee004cadfc26dd9f299445bb5229371f0c13` | blog: route bilingual hosting through the backend |
| `10e66efdffc586bdec8af82b3d0e17df59bee2d7` | blog: replace notification pulls with authenticated release uploads |
| `16496060da4faf81acc7173c5a070dc0f1d39c36` | blog: enable signed delivery with WordPress still public |
| `99c7d5ec122aa8b32aeb45fcc12bf19719c86287` | blog: serve the validated bilingual release |
| `76d7fcf191045ea5ddce332dce341a67610e0315` | blog: prune old completed release payloads independently |

Full series/messages, final full diff and inventory are linked in the JSON.
DNS, hosting, authenticated delivery, enabled coexistence, public selection and
retention each own a separate behavior. No obsolete fixup stack, abandoned
approach or repeated dependency/channel/pin update stream remains in this series.
The independent reviewer must assess that conclusion across the complete range.
No database/application migrations exist. Earlier schema2 publication authority
and ordering are already deployed/consumed on1649/cqjh; retained schema1 release
content is a supported recovery boundary, not an unapplied conversion path.
P25 leaves persisted schema2/control/order unchanged and adds keep_releases only
to compiled policy. Pruned payloads cease rollback eligibility; retained receipts
alone do not permit rollback, and the greatest upload floor remains intact.

The provider is CONFIG tools/blog-static-release.py. Actual consumers are the
same-package tools/blog-upload.py (imports helper and calls Publication.upload),
blog-upload.nix receiver, static-blog.nix fixed helper/maintenance guard/new timer,
and affected existing fixtures. BLOG bin/upload-release and build workflow
consume the unchanged authenticated transport contract; no client/workflow pin
or protocol edit is required. Companion BLOG docs472 is independent and does not
change genuine selected a66/run11 content identity.

Risk HIGH (payload deletion, publication locks, recovery and deployment). Proposed
all four lanes: general, architecture/repetition, scope/proportionality, risk/
compatibility. Lead owns reviewer0 saved Sol/xhigh assignment and acceptance.
This packet is implementation evidence, not a review result.

Fresh final native source/input/system/NAR proof, one bounded actual fixed-UID
CLI/receiver fixture, mapping admission, copy and final switch remain gated.
99c7/4m7 proofs are predecessor evidence, not retention certification;99c7 has a
retained exact recovery ref. Runtime remains prior accepted cqjh/PAUSED/publicWP/
a66 Actions11.1, with backups/roots/private package copies retained. No live prune,
cleanup, proxy activation, default integration or lifecycle action in this phase.
Current local origin/master tracking is8e205f1c (observed only; no fetch/current
remote claim); later publication needs fresh preflight and drift assessment.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/)
