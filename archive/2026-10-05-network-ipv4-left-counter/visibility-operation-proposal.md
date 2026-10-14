# Visibility source and pin operation proposal

Prepared for root inspection only. No commit, fetch, push, CI cancellation,
rebase, pin generation or contract check has been executed by the implementer.
The operation manifest is intentionally absent until root approves the message
and helpers. API passes are still pending; prior feature checks do not certify
this follow-up.

## Evidence and exact scope

The source operation requires quick2 Ruby syntax/scoped lint exit 0 and quick3
aggregate/core/full exit 0. Quick3 uses the unchanged existing automatic test
helper with TMPDIR=/tmp; its logs and JSON remain in tracking. Source remains
frozen by visibility-quick3.sha256. The complete eight-path diff is
visibility-quick2.diff: two Index query changes, five matching resource specs
and the exact approved owning docs paragraph. There are 22 added declared
examples and two extended existing export examples; runtime totals must come
from the root's final receipts. No W source edit, catalog change or migration
is included. Existing API topic patterns cover these files without changes.

The sole feature migration and its predecessor/schema retain the exact blobs
recorded in visibility-migration-provenance.txt. The V operation appends one
normal-hook commit to the original two logical commits, then verifies its parent
and unchanged entire migration/schema directory. It does not rewrite V history.

## Bound heads and ancestry

- V old/source remote: be136b6c00f03b85b7a12cc57550b4a1394a94a7;
  original base c4d9b50f4e74417ed37b5fe410cca3ec1addc24e.
- W remains e4c49bcdc91b33b7f644a2f125231cb413cf4bf4 on dev/network-enabled.
- C old dd10d88073da3aed6c4512e938abe4374422aab1;
  original base cde8451718d75929c931db63626b48f7de92fc4f; two pin-only commits.
- K old 291566b2c0bd43389802f607852fd9a4f8241752;
  original base 873758fd6aec0c03f50a94600e0ceab97946f255; one pin-only commit.

The source helper records the newly committed full SHA in visibility-source-v.sha.
Root passes that exact SHA explicitly to every subsequent operation; publication
adds visibility-published-v.sha. SSH URL, exact branch/head, clean index/tree and
receipt checks refuse unexpected state. Source publication fetches master and
its owned feature ref, refuses default nonancestry and uses an ordinary append
push after checking the exact old remote head. The owned tracking-ref fetch uses
a leading +; no default ref is forced.

Pin preparation first fetches both published source refs/defaults and verifies
the selected V/W heads and default ancestry. It also fetches each target default
and requires it to remain an ancestor of the recorded original pin base. A
refusal requires root reconciliation, not automatic reset/rebase of source.

Before each pin operation root must independently inspect the exact current
remote feature lease and write visibility-config-lease.expected or
visibility-kb-lease.expected as one full SHA or the literal absent. These are
not guessed here. The pin helper rechecks that lease and saves it, the old tree,
complete old pin history and base diff under new visibility-* names before any
controlled return-to-base rebase. The old review artifacts remain untouched.

## Proposed operation order

After root final message/diff inspection and passing API receipts, freeze the
listed operation controls and invoke each dependent operation separately:

```bash
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/visibility-operation.sh commit
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/visibility-operation.sh publish EXACT_NEW_V_SHA
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/visibility-operation.sh cancel EXACT_NEW_V_SHA
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/visibility-operation.sh config EXACT_NEW_V_SHA
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/visibility-operation.sh kb EXACT_NEW_V_SHA
```

The outer helper supplies verified session markers, exact per-repository CWD and
Nix shell routing, aggregate log/status and no-overwrite guards. Commit uses the
all-plugin V root shell and verifies installed executable Overcommit integration
and signature settings before staging only the eight paths. It compares the
staged binary diff to the reviewed frozen source diff and uses git commit -F
visibility-commit.message. No hooks are bypassed or automatically re-signed.
Signature or hook failure stops for root investigation.

The optional dependent CI step inventories queued/in-progress runs without a
branch filter, refuses saturation at 1000, then selects only the exact V feature
branch with noncurrent head SHA. It rechecks the current remote head and each
run's branch/head/state before cancellation. It neither cancels W/other branches
nor waits for CI.

C and K drop only their verified pin-only series using the approved guarded
rebase --onto ORIGINAL_BASE OLD_HEAD OWNED_BRANCH. No reset, clean or stash is
used. C then runs, inside its Nix shell:

```bash
confctl inputs channel set --commit --no-editor vpsadmin vpsadmin EXACT_NEW_V_SHA
confctl inputs channel set --commit --no-editor vpsadmin-webui vpsadmin-webui e4c49bcdc91b33b7f644a2f125231cb413cf4bf4
```

Both generated messages/changelogs remain untouched. The strict C guard permits
only vpsadminServices locked rev/narHash/lastModified to change versus dd10d880;
all W fields, unrelated input nodes/identities and follows must compare exactly.
The final generated history must contain two commits over the original base and
change only flake.lock versus the prior current tree. The helper records both
new commits and full series/current diffs; it does not publish C.

K reuses the inspected fixture-final-pin-guards.py setter and semantic guard.
It updates only four exact textual V records, generates the fifth record with
nix flake update vpsadmin and runs bin/check in its pinned shell. The guard
compares the complete graph and existing textual records against the prior
291566b2 snapshot, permitting only the selected V revision/content/time change.
The final status must be exactly the five unstaged pin files; fingerprints,
page prose, capture bindings, PNGs and runtime files remain byte-identical.
K stays at its original base with a checked working candidate plus binary diff
and five-file hash receipt for root inspection. K commit/publication is excluded
from this packet. A contract drift failure must be reported, not normalized.

## Freeze controls and remaining ownership

After root approval, visibility-operation.sha256 should freeze only these
prepared controls (not mutable result/head/lease receipts):
visibility-operation.sh, visibility-v-operation.sh, visibility-cancel-ci.sh,
visibility-pin-operation.sh, visibility-config-pin-guard.py,
visibility-commit.message, this proposal, visibility-quick3.sha256 and
fixture-final-pin-guards.py. The source helper independently verifies the complete
quick3 source manifest before and after commit.

Root owns final staged diff/message acceptance, passing-check interpretation,
remote lease discovery, execution, exact final heads, final whole-branch review
and K candidate inspection/normal commit. No PR action outside W, source W update,
default integration, build, deployment, cluster/session lifecycle or screenshot
operation is part of this proposal.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/
