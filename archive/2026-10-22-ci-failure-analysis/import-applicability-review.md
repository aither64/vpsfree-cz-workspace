# Independent final review: import applicability

Reviewer0, gpt-6.1-sol/xhigh/read_only. High risk; all four lanes completed:
general, architecture/repetition, scope/proportionality, risk/compatibility.

**No findings.** No Blocking, Important or Advisory source issue identified.

Reviewed repository/worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos-import-applicability`.
Base: `e2b2b9186de6e0aec66f87a0e4d16e86bc2d7854`.
Head: `36965e88b8ac71a547b2672f12d472d4c33ea46b`.
Tree: `6699cbd7ea4a58633d7a150f683543415a148286`.
HEAD/tree matched and index/worktree were clean. Public session binding matched;
both reviewer-shell identity variables were absent. Live roster confirmed saved
review-purpose settings; no overrides or nested agents. Reviewer read the packet,
skill/all four references, instructions/policy, design, prior review, committed
correction/specs/docs and check receipts. This file retains the returned review
conclusions; the reviewer performed no record writes.

## Behavior and compatibility

Reader owner450da920, run_configuration.rb:204, accepts a base candidate only
with complete saved base selection, cleanup false, no same-run owner and no
overlapping cleanup owner. It then proves the held init/PID1/birth/cgroup, exact
mount/ZFS source/GUID and private-root identity through the existing preparation,
final-recheck and publication path. Missing ownership never proves a temporary
root: a live temporary root cannot pass the base-candidate checks, and there is
no catch-and-fallback after failed authentication. Existing temporary-owner,
suffix and overlap checks remain at impermanent_root_owner:498.

At root_dataset_identity:563, a legitimate cloned base relaxes only the
temporary-only origin restriction. Temporary roots still require origin `-`;
all returned identity properties are compared across preparation. The ordinary
case preserves the loaded dataset object, cleanup false, YAML/run ID and GC
records. Identity retention, error cleanup, manipulation exclusion and
publication/monitor/console ordering remain intact. Genuine failure retains the
collector's retirement fence.

garbage_collector.rb:123 keeps strict reads by default. Explicit absence requires
empty in-memory ownership and an absent path. Malformed, unreadable or symlink
evidence is not absence. Final snapshot comparison rejects observed file
appearance/disappearance or ownership changes. No file/owner is invented.

## Architecture and proportionality

The correction extends the existing authenticated import transaction and shared
root-identity helper, without an alternate importer, framework, management API
or external runner contract. The base/temporary distinction supports a concrete
legitimate run. Publication and fencing remain centralized. The small overlap
checks express different ownership cardinalities and need no new abstraction.

Specs cover absent/empty/unrelated/clone acceptance, unchanged bytes/object/
ownership, same-run and overlap contradictions, temporary-without-owner refusal,
and changed root/process/file/GC evidence. Owning docs explain next-start
semantics and the ordinary import exception. Broader reverse-toggle behavior is
not claimed.

## History, migrations and repeated streams

Exactly five coherent owners remain, oldest first:

1. `0d649b80f67a262830682d1651cc748d752e1d42` — writer, exact unchanged object.
2. `450da920081a1c2765b340b1279102ebe9c6b596` — reader/import/GC v2; correction,
   specs and docs folded into their owner with truthful history and limits.
3. `e00ee7027c9ccfd7b0f29a99f651a2a019beb34a` — hotplug health.
4. `43ff36ab23c5cf9b2e8444e7b3bea03a71869342` — production transition regression.
5. `36965e88b8ac71a547b2672f12d472d4c33ea46b` — retirement/policy.

Reviewer independently compared committed objects: later three patches,
messages and author identities/dates equal their previously reviewed owners;
writer is identical. Only reader changed. Old04a2-to-new36965 changes exactly
seven paths, +230/-35. Full-index binary delta SHA256:
`b6673b368cf6a4e1f4a4d83ec857552057e61e3059c8e99e7a6da0860aad11c3`.
The dated pre-applicability backup points exactly to old04a2. All messages are
within80 columns. Prior full review is explicitly reused for unchanged owners.
No obsolete approach, superseded reader/fixup, diagnostic add/delete cycle or
recorder residue ships.

**No migrations.** No schema/YAML/run-ID version or transitional migration is
introduced; no migration merge/release/deployment/external-use lineage exists.
Old saved/running-state compatibility remains intentional. Older daemons retain
format readability; rollback loses newer import protections and can restore the
old refusal. No coordinated node update is required.

**No repeated update streams.** No repeated dependency/channel/input/kernel/gem/
generated-artifact updates. flake.lock equals the selected base; inputs, tests
and shared runner/framework contracts are unchanged by this correction.

## Verification limits and disposition

Retained final spec-4:113 examples/0 failures, seed58689,1.68s. Style-2: five Ruby
syntax passes and RuboCop with no offenses. Normal reader/health/regression/
cleanup hooks passed with unsuppressed width preferences; messages satisfy the
repository limit. These are cached focused spec/static receipts, not native
package/runtime proof. Prior broader evidence retains its earlier limits.

Native catalog/VM acceptance remains blocked by recorded discovery OOMs.
Packaged-source/ZFS/kernel recovery, data continuity and v1/v2 runtime remain
unproven. Source review is complete with no source/history finding blocking
acceptance. Native launch, runtime readiness, publication and integration are
not approved by this review.

Reviewer inspected source/Git objects/receipts read-only: no tests, Nix, builds,
probes, fetch, mutations, push, cleanup or record writes.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/
