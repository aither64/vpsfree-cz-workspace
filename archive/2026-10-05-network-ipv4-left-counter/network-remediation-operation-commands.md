# Network availability correction operations

Prepared for the root lead to inspect and execute only after accepting the
passing evidence and exact packet. Nothing in this document has been executed
by the implementer. All source bodies remain fixed at the passing quick2
snapshot; the approved work-log update contains evidence prose only.

## Source commits and history

Run from the verified tracking directory in the parent context:

```sh
bash run-network-remediation-source-commits.sh v-api
bash run-network-remediation-source-commits.sh v-webui
bash run-network-remediation-source-commits.sh w
bash run-network-remediation-source-commits.sh consolidate-v
bash run-network-remediation-source-commits.sh consolidate-w
```

Before the W commit, the root's known-short documentation audit must be
recorded as `remediation-final-docs.log` and `remediation-final-docs.exit` with
exit 0. The normal-hook helper stages the exact path lists and commits with
the prepared message files. It refuses any other changes or hook bypass.
Fixup commits use the existing API/legacy/W subjects. Autosquash retains the
two V logical commits and one W commit, checks exact before/after tree identity,
and verifies that V migrations/schema are unchanged from the original review.

`remediation-source-{v,w}.sha` records the selected final source heads. Original
review and quick-check files are preserved; history, trees, fixups and range-diffs
use separate remediation-prefixed files. Inspect them before publication.

Parent source operations have now completed: V
`30603a832d2848207bd7319c79c6b0388bc8646a` (two logical commits) and W
`b3b756a7b45864459bd39481a0d5245886777660` (one). Normal commits, autosquash tree
equality and unchanged V migration/schema checks passed. The publication and
pin helpers are bound to these exact selected heads. Their operations remain
unexecuted until root inspection.

## Feature publication and superseded CI

Reverify the session binding in the parent, set both verified markers for each
command, and use these exact repository directories/shells. These calls are
prepared instructions, not permission to integrate a default branch.

```sh
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
worktrees=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
cd "$worktrees/vpsadmin"
env DEV_SESSION_SLUG=2026-10-05-network-ipv4-left-counter \
  DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz VPSADMIN_PLUGINS=all \
  nix develop .#vpsadmin --command bash "$tracking/remediation-publish-in-shell.sh" v
cd "$worktrees/vpsadmin-webui"
env DEV_SESSION_SLUG=2026-10-05-network-ipv4-left-counter \
  DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
  nix develop --command bash "$tracking/remediation-publish-in-shell.sh" w
```

The helpers verify the SSH remote, clean feature worktree, current default
ancestry, selected final head and exact previous remote feature head. They push
with explicit leases V `6b3628af665049dc095ba985ef0fbe8a22286863` and W
`811742f50cce2b7724784d0a674c8d4d5dcb6273`. If a default or feature ref has
advanced, stop for lead reconciliation; do not weaken the guards.

After publication, in the parent's `gh`-capable context with both verified
markers, run `bash "$tracking/remediation-cancel-superseded-ci.sh" v` and the
same command for `w`. It inventories only that feature branch's queued/running
runs, rechecks each run and the remote feature head, and cancels only a run
whose SHA differs from the selected current head. It never waits for current
CI or cancels another branch. A missing tool or a saturated inventory stops for
the lead. No deliberate integration run is started by these operations.

## Regenerate pins from original bases

After both exact source publications are accepted:

```sh
cd "$tracking"
v_sha=$(cat remediation-source-v.sha)
w_sha=$(cat remediation-source-w.sha)
bash prepare-network-remediation-pins.sh config "$v_sha" "$w_sha"
bash prepare-network-remediation-pins.sh kb "$v_sha"
```

The pin helper first fetches/checks the published source heads and defaults.
It requires exact clean C/K original heads and original pin-only series, saves
their histories/diffs, and returns only those feature refs to their original
bases with `git rebase --onto BASE OLD_HEAD` inside each declared Nix shell.
It uses no reset, clean, stash, worktree removal or default-branch operation.

- C original head `dea15f88c38341ecfd3e5030c700d1fee3d854a7`, two pin commits;
  base `cde8451718d75929c931db63626b48f7de92fc4f`.
- K original head `ef72876da07dae61449502e2d03856d1d3b133e4`, one pin commit;
  base `873758fd6aec0c03f50a94600e0ceab97946f255`.

C uses the existing inspected confctl helper, with hooks active:
`inputs channel set --commit --no-editor vpsadmin vpsadmin V_SHA`, followed by
`inputs channel set --commit --no-editor vpsadmin-webui vpsadmin-webui W_SHA`.
Changelogs remain enabled and both messages stay exactly generated. The helper
checks the follows edge and records two final hashes. Root must inspect the full
transitive generated input diff before accepting it; no configuration build or
deployment is part of this operation.

K changes the four canonical source pin records through the existing exact-pin
helper, then runs `nix flake update vpsadmin` and `nix develop --command bin/check`.
No semantic fingerprint, page prose or capture changes are accepted blindly.
The candidate is left uncommitted with a recorded diff and file hashes for root
inspection. After acceptance, commit it inside its Nix shell:

```sh
cd "$worktrees/vpsfree-kb-contracts"
env DEV_SESSION_SLUG=2026-10-05-network-ipv4-left-counter \
  DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
  nix develop --command bash "$tracking/remediation-kb-commit-in-shell.sh"
```

The existing approved `commit-k.message` is reused. Installed Git hooks run
normally; unexpected newly declared frameworks stop the helper. Final C hashes
are `remediation-pin-c-{v,w}.sha`; K is `remediation-pin-k.sha`.

## Limits and failure recovery

These are bounded dependent operations for a fresh watcher when shell/startup
or command duration is uncertain. Stop on the first refusal or failure and
report the actual HEAD, index/worktree state, and saved evidence. Do not rerun
the original-head gates against a partially completed operation or apply an
automatic reset; the lead selects the exact recovery step.

No source semantics, migration lineage, production state, deployment, merge,
capture or session lifecycle action is changed. KB capture generation remains
blocked on a supported execution environment with the required lifecycle
generation and socket ownership contract. The old helper is not started.
