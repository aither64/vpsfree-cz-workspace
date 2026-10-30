# Immutable Git identity supplement — preparation only

This distinct package preserves both failed metadata packages and their effects
receipts. It changes only the candidate flake reference and source attestation
around one identity-only query. No catalog rerun, evaluator invocation, build,
VM, Git mutation, archive/export/root creation, source-tree copy or cleanup has
been performed. The product source and original three JSON catalogs are unchanged.

The candidate query uses exactly:

```text
git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos-production-commit?rev=4de50f0046052d377780a3be3a9aeec37ad86f6e
```

The supervisor's source directory remains a separate literal absolute path.
Before and after the operation, read-only Git with lazy fetching disabled must
prove detached HEAD4de50f0046052d377780a3be3a9aeec37ad86f6e, actual tree
e5e074bad8c74a27eb3dc422e44cb8e08389a245, empty staged and unstaged diffs, no
nonignored untracked files, tracked fixture and unchanged lock hash. Source
state/error snapshots are retained; a post-check failure prevents success.

The native Git flake must report revision4de and EXACT source path
/nix/store/vp408cmsdyd625lcrr4kizrn7rklzm7j-source before full input metadata is
forced. Production remains exact2abbe3cc1c102a4b39022d3f73ef4a432ad4d616 and
/nix/store/96g5h6c9kzwsr3n1cgsvzyq44wzyzixa-source. Both native SHA256 NAR
identities, full lock graphs and all root input identities are mandatory; all
record keys are ordinary sourcePath, including input records. No injected/null
root revision or path fallback is accepted. Any path, revision, NAR, tree,
lock or input mismatch stops for diagnosis.

The original catalogs retained source-path strings but NO NAR hashes. Native
immutable Git NAR identity plus exact original content-addressed source path
is the binding; this does not directly compare a native hash with a previously
recorded NAR. It attests only the4de discovery checkpoint. It does not attest a
later feature head, actual packaged daemon bytes, machine config or runtime.
Do not normalize a path mismatch or substitute a different source graph.
Source paths need not remain materialized after evaluator exit. Complete locks
are compared with raw SHA-verified immutable Git bytes already retained under
identity-locks/; no post-client store-source reread is required.

The unchanged818f91da supplement checker hashes the original default/history/
diagnostic JSON, binds all three source-string maps, validates the supplement
and invokes actual native TagFilters only over retained names and tags. It
receives git-identity-supplement.json. The original catalogs remain immutable:

- default90a45736e8bf3434e540e8fa4cd13e5d6719f97c9522164032425cfd61a78a8a
- historical73fd5608c2a690020491cb48c41741105ebeca2c518dee3b348dc1fd3aad0297
- diagnostic ec1ac9c7aea8e0d77be6684eb0eab756bba7094ec06896d34d6fdb3c83dfa06a

Exact proposed command for separate fresh lead-watcher selection:

```sh
VPSADMINOS_DISCOVERY_EXPECTED_HEAD=4de50f0046052d377780a3be3a9aeec37ad86f6e \
  /nix/store/pwxj9ycwqd117yra6czifh3xfx5p88lh-bash-interactive-5.3p9/bin/bash \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/support/run_production_identity_git.sh \
  /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos-production-commit
```

Exactly three argv entries after the environment assignment; no punctuation arg.
The fixed guardian retains both session guards and cached absolute Git/Nix/
Ruby/Bash/Python/dev-session tools, unlimited FSIZE/core0, clean environment,
IFDfalse/builders-empty/fallbackfalse, streamed output and source/hash guards.
New receipts use git-identity-* and cannot overwrite existing receipts.

Architect-set bounds remain120s total, query90s, checker5s;5s cancellation-reap
escalation retains watcher and handles. The total timer includes source/session
preflight. It drains pipes during cancellation and hard-caps retained native
stdout2MiB/stderr1MiB, rejecting unexpected build output. It sends only an
identity-authenticated native group INT; no automatic TERM/KILL. A deadline or
guardian exit is not effects-ended proof.

The40GiB floor and2GiB shared-free-space decline are sampled on the verified
common source/store/evidence filesystem. They are NOT a cumulative owned-growth
quota: foreign frees can mask allocation. Native Git/input metadata can fetch
sources; exact new allocation remains unknown. This package adds no archive,
export, full-tree copy, realization, GC root or store cleanup. Any inherent
source fetch still needs the lead's bounded operation selection. Retain actual
paths/observed allocations without claiming exclusive store ownership.

29 preparation checks pass: native selector over real retained catalogs with
synthetic identity/NAR/input records, strict missing/wrong revision/path/NAR/
lock/input rejection and raw catalog integrity, inert stream/space/deadline/
reap behavior, actual source-reader logic with inert Git replies for correct
head/tree/detachment and dirty/mutated pre/post state, and unchanged accepted
Coreutils-dispatch refusal in the combined future scanner. One driver-only old
receipt filename was corrected before the final pass. These checks are not
native identity/selector acceptance. Nix parse, Python AST, Ruby and Bash syntax
also pass; unchanged shipping38 assertions were not rerun.

After authoritative result, owner runs reconcile_identity_git_effects.py exactly
once with cached Python. It includes every actually recorded child from the
original catalogs, failed path attempt and latest attempt; a missing checker
is never invented. It retains independent canonical argv/cwd/root/fd scans,
PID/birth/groups, permission qualifications, strict readonly observer dispatch
checks and no signal/cleanup behavior. This future scanner has not run. No
prior effects rescan was performed for this preparation.

Full frozen hashes and quick evidence: identity-git-preparation-checks.json.
Publication stays held pending actual supplement/native selector and final
source/effects acceptance. Packaged-byte and machine/runtime admission remain
separate obligations.

Finalization correction (source-only): the pre-finalization d032 packet is
preserved byte-exact under identity-git-before-finalization/. The guardian now
uses captured source lock hashes, records primary-operation and post-source
errors independently, and reads final free space from the retained evidence
filesystem with an explicit error field. It never rereads a vanished/unreadable
source lock while constructing its result. Missing/unreadable source state
still forces nonzero; cached hashes provide evidence, not acceptance fallback.
Four focused actual-finalization checks pass: primary failure plus missing lock,
primary failure plus injected unreadable lock, successful native operations
plus vanished source directory (retained receipt/nonzero), and reproduction of
the old lost-receipt bug. Existing29 preparation checks are retained; unchanged
shipping38 checks were not repeated. All guardian helper functions, query,
launcher, native checker, catalogs and locks are unchanged.
