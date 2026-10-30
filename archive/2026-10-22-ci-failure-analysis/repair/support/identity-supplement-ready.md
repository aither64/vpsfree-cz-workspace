# Frozen identity-only correction

Preparation only; no native identity query/evaluation/build/VM/Git mutation or
cleanup. The original guardian/query/checker, three raw catalog JSON files,
stderr and failed checker receipt are unchanged. Original final-effects proof
was accepted with its readable-view/674 permission-gap qualification; no repeat
scan was performed for acceptance.

Cause: the original identity record used the special outPath attribute. Nix
JSON serialization coerced each complete identity to its source-path string,
losing the object fields. The nested input records used the same special key.
The three native catalog/tag queries succeeded; the checker then failed before
TagFilters when it fetched rev on a String. This is a serialization failure,
not proof of a catalog selection failure or source identity pass.

The minimal query production-identity-only.nix returns only candidate and
production identity records, using sourcePath at BOTH levels. It asserts exact
4de50f0046052d377780a3be3a9aeec37ad86f6e and
2abbe3cc1c102a4b39022d3f73ef4a432ad4d616 revisions and exact previously returned
source paths vp408cmsdyd625lcrr4kizrn7rklzm7j-source and
96g5h6c9kzwsr3n1cgsvzyq44wzyzixa-source. It returns source NAR, complete raw
lock graphs and all top-level evaluated input identities. There is no catalog
import, historical boot, system/config JSON realization or component build.

check_production_discovery_supplement.rb requires the supplemental objects,
exact revisions/source paths/NAR identities, full lock equality and every
root input identity. It hashes all three original catalog bytes and requires
all three original source-string maps equal. It then runs actual native
TestRunner::Cli::TagFilters#pass? over the retained names and combined tags.
No revision or missing identity check is dropped. The output explicitly says
identity was supplemented; it does not pretend the original JSON retained it.

The candidate store source path is currently unavailable, so the checker must
not depend on reading a possibly collected store path after evaluator exit.
Exact raw lock bytes from immutable local Git4de/2ab are retained in
identity-locks/ (SHAfd0361f8.../1f401890...). The query reads locks during
evaluation, and the checker compares those complete objects against the
hash-verified Git bytes. There is no inferred GC timing/cause. getFlake may
refetch the same immutable source/input objects; the new query can force input
source identities that the earlier coerced object did not force. Fetch size is
not yet proven. This is no new recipe, but still needs bounded fresh-watcher
selection. No store path is exclusively owned or selected for cleanup.

Exact command for separate lead selection:

```sh
VPSADMINOS_DISCOVERY_EXPECTED_HEAD=4de50f0046052d377780a3be3a9aeec37ad86f6e \
  /nix/store/pwxj9ycwqd117yra6czifh3xfx5p88lh-bash-interactive-5.3p9/bin/bash \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/support/run_production_identity.sh \
  /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos-production-commit
```

The fixed guardian keeps both session guards and literal isolated4de/clean/
tracked-fixture binding, cached absolute tools, FSIZE unlimited/core0 and the
same env cleanup. Exactly ONE native identity-only query with IFDfalse,
builders-empty/fallbackfalse, followed by a5s Ruby checker. No retry or second
recipe. Proposed fresh watcher budget120s total; native loop120s aggregate,
query90s/checker5s,5s cancellation-reap escalation retaining watcher/handles.
SIGINT only to authenticated started native PID/birth/PGID; no automatic
TERM/KILL, and a deadline/guardian exit never proves effects ended.

Implemented continuous pipe draining hard-caps retained stdout2MiB/stderr1MiB
aggregate and rejects unexpected build output.40GiB free floor and2GiB shared
free-space-decline refusal are sampled on the verified common filesystem.
This is NOT a cumulative owned allocation quota: foreign frees can mask
allocation and foreign writes can stop preparation. Exact new source-fetch
allocation is unproven; record returned source/input paths and their allocations
where observable. Source objects can be shared or disappear after client exit.

Original catalogs remain immutable:

- default:90a45736e8bf3434e540e8fa4cd13e5d6719f97c9522164032425cfd61a78a8a
- historical:73fd5608c2a690020491cb48c41741105ebeca2c518dee3b348dc1fd3aad0297
- diagnostic:ec1ac9c7aea8e0d77be6684eb0eab756bba7094ec06896d34d6fdb3c83dfa06a

Syntax/AST/Nix parse/Ruby syntax pass.16 quick checks use synthetic identities/
NAR/input values over the actual retained catalogs and native TagFilters, and
inert Python children for stream/space/deadline/reap tests. They do not supply
actual source-identity acceptance. They reject coerced identities, wrong path/
revision, missing NAR, lost lock/input nodes, nested coercion and changed raw
catalog bytes. All started inert groups end. No original semantic38check rerun
or original effects rescan was needed.

After the selected watcher has ended and delivered raw result, the owner must
perform the prepared read-only combined final-effects command:

```sh
/nix/store/jy00n3jp5xj8s40n1fbldmkcr5n7avxc-python3-3.13.15/bin/python3.13 \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/support/reconcile_identity_effects.py
```

It combines original4 child identities with the identity/checker children,
checks exact births/groups plus canonical isolated-source/evidence argv/cwd/
root/open-fd references independently of PGID, handles detached references,
qualifies unreadable process fields and refuses positive ambiguous own refs.
Only exact read-only observer semantics are ignored; find is not exempted.
No path-only signal, foreign cleanup or deletion occurs. This command has not
run, since its future native result does not exist. Guardian PGID checks alone
are not the final-effects gate. Publication remains held pending actual
supplement+native selector acceptance; packaged daemon bytes and machine/runtime
admission remain separate unexecuted obligations.

Full frozen file hashes and quick evidence: identity-preparation-checks.json.
