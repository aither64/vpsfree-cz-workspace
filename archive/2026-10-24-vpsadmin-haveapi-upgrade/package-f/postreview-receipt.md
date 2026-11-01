# Package F postreview verification and publication

Status: reviewed, local postreview checks passed, own feature branch published.
Exact-head GitHub Check succeeded (run 40379808743, attempt 1); no merge,
installation or live-certificate repair.

Source remains `ab9346b0c4b942fccd0da6af760401fad3a55bd1`, tree
`ff22b629479737a274510d395730190a442463ee`, parent/base
`767dfd587e346168e1443e65ccdb67ce748f3fe3`. See the unchanged
[review packet](review-packet.md), [full diff](final.diff), [history](history.txt)
and [focused test hashes](tested-files.sha256).

Lead released postreview verification after reviewer0's saved
Sol/xhigh/read-only four-lane review of the complete base-to-head range:
no Blocking, Important or Advisory findings; history/consolidation and no
migrations accepted. No source change or quick-test rerun followed that review.

The session and complete environment identity matched before action. Clean
exact head, tree and tested-file/lock hashes passed preflight. Host capacity:
64 CPUs, 41 GiB memory available and 108 GiB disk available. A0 holds the sole
verification utility slot, so this operation uses the explicitly released
visible parent-monitor fallback, one owned handle per operation, interruptible
waits no longer than 50 seconds and full logs/status. Command affinity is CPUs
62-63, nice10; Nix max-jobs1 and cores2. No global resource controls changed.

Exact immutable source: `/nix/store/gmddc94pkw4x2hs3214z5g1gqfhh0cg2-source`,
NAR `sha256-FMjjuVkWZlhLRXT7NFY8E0kWuFVaJ9t9U67mS7M5vUo=`.
[Flake metadata](final-flake-metadata.json) includes the complete 34-node lock
graph. [Check identities](checks-derivation-identities.json) bind all nine
checks to drv/output paths; [recursive graph](checks-input-graph.json) contains
all 5,597 derivations. The initial identity export named a field `outPath`,
which Nix JSON coerced to a store string; the preserved output-only export is
[here](checks-derivations.json). Using non-coercing field names captured both
identities. This was evidence preparation, before the single aggregate run.

## Required sequential checks

1. `taskset -c 62-63 nice -n 10 nix --option max-jobs 1 --option cores 2 flake check --print-build-logs`
   PASS exit0, 2552 seconds; original parent handle10748 reconciled complete.
   [Full log](flake-check.log), [status](flake-check.exit),
   [elapsed](flake-check.elapsed). All nine checks passed. Own aggregate Ruby
   suites: 21 suites, 371 cases, 3415 assertions, no failures/errors,
   1 existing skip. Upstream dependencies also passed under their declared skip
   conditions. Nonfatal Codex helper PATH-alias warning under `/build` retained.
   [All nine output NAR/reference identities](check-output-identities.json)
   were queried successfully after completion; no kernel build was logged.
2. Original `nix run .#devcluster-check`: FAILED exit1 after 506 seconds,
   parent handle89918 reconciled complete. [Full log](devcluster-check.log),
   [status](devcluster-check.exit), [elapsed](devcluster-check.elapsed).
   Its vpsAdmin passes and two vpsAdminOS bridge passes are partial only.
   The inherited `NIX_CONFIG` receives only
   max-jobs1/cores2 resource settings for nested Nix calls; the command also
   retains taskset62-63/nice10 and the same Nix options. No retry preceded diagnosis. This declared
   application uses temporary configuration, evaluates both network modes and
   builds/loads runners; no VM is started. No host-migration VM is assigned.
   [Application identity](smoke-application-identity.json) binds drv
   `/nix/store/c0xyqds3ycjb7j2f9mr28ajykpgdf8gy-devcluster-check.drv` and program
   `/nix/store/3ia7c0nfz1vji8rh0d746h9g9bl9nq4f-devcluster-check/bin/devcluster-check`;
   [recursive app input graph](smoke-input-graph.json) captured before launch.
   Source/hash/capacity preflight passed separately before launch (39 GiB memory,
   103 GiB disk available).

## Confirmed environment failure and rooted correction

[Exact pressure-GC journal](smoke-gc-journal.log) proves deletion during the run:
app drv and output at 19:24:35+01, packaged tools at 19:24:42+01. The declared smoke
then failed reading the previously available packaged default configuration.
This was unrooted test-artifact loss, not a provider source finding. The original
failure remains preserved. All nine completed flake outputs were also collected;
prior exit0, input graph and NAR/reference receipts are historical evidence,
not a claim those unrooted output paths remain available. No aggregate or focused
test was repeated to restore them; no installed output is selected or deployed.

Lead authorized environment-only correction after diagnosis. Re-evaluated app
identity and all 2,576 recursive derivations equal the originals exactly. Same
`c0xy...drv^out` was realized with normal owned out-link
`package-f/smoke-gc-root`; exact source has normal indirect
`package-f/source-gc-root`. [Realization log](smoke-root-realization.log),
[status](smoke-root-realization.exit), [elapsed](smoke-root-realization.elapsed),
[registered roots](smoke-registered-roots.txt), [restored input graph](smoke-restored-input-graph.json).
All 202 runtime/source paths and every embedded app input were valid before
retry. [Full closure/NAR/reference identities](rooted-smoke-closure-before.json).
Source NAR and all tested hashes match the original exact F source.
App NAR: `sha256-dy++i3WhGu2QUWp1Xxp5mC28g2bkKyfdPqNaINEQo7s=`;
tools NAR: `sha256-58h04ZbpW4A1tI29g/s07AiclJHk+lLDyYl6VxugW/M=`.
The original app/tools NARs were not separately recorded, so no byte-equivalence
claim is made for them; the corrected complete run proves the current rooted
artifact directly. No existing comparable identity has an unexplained mismatch.

One fresh full declared smoke PASS exit0, 444 seconds, parent handle70754
reconciled complete, same command and resource limits. Separate
[log](devcluster-check-rooted.log), [status](devcluster-check-rooted.exit),
[elapsed](devcluster-check-rooted.elapsed). Both providers passed bridge/local
configuration defaults and overrides; enabled bridge WebUI and the enabled-local
refusal passed; both Ruby runners built and loaded. The complete result comes
from this single rooted run; partial runs were not combined.

Afterchecks: all 202 runtime/source paths valid, exact before/after NAR hash,
NAR size and reference-set equality; source/head/tree/hashes remain exact and
worktree clean. [After closure identities](rooted-smoke-closure-after.json),
[registered roots after](smoke-registered-roots-after.txt). Source and runtime inputs are unchanged; only normal
owned retention was added. No collector, service, host policy or global GC control
was changed. Keep roots and evidence; no cleanup was requested.

## Publication boundary and limitations

Both local check gates passed and source/process effects reconciled before
publication. Fresh source/branch/clean/SSH/hooks preflight passed; only
`origin/master` was fetched (no tags, no prune), still exact base767; own remote
ref was absent. No active non-sample hooks or configured hook framework were
found; no hook bypass or configuration change.

Executed exactly one NO-FORCE refspec with ordinary Git hooks:

```sh
git push --porcelain origin ab9346b0c4b942fccd0da6af760401fad3a55bd1:refs/heads/2026-10-24-vpsadmin-haveapi-upgrade-boot-proof
```

Canonical SSH: `git@github.com:vpsfreecz/dev-workspace.git`. Push exit0,
original handle95708 reconciled complete. Independent remote query proves the
feature ref at exact ab9346b0 and default HEAD/master still exact767; local
head/tree/clean status unchanged. [Preflight](publication-preflight.txt),
[push log](publication-push.log), [status](publication-push.exit),
[remote proof](publication-remote-proof.txt). No PR was created.

Exact-head CI: push-triggered Check run
[40379808743, attempt 1](https://github.com/vpsfreecz/dev-workspace/actions/runs/40379808743/attempts/1)
completed **successfully** at 2026-10-26T19:01:23Z for
`ab9346b0c4b942fccd0da6af760401fad3a55bd1`. Its sole job
[`flake` 121772673835](https://github.com/vpsfreecz/dev-workspace/actions/runs/40379808743/job/121772673835)
succeeded, including both `nix flake check --print-build-logs` and
`nix run .#devcluster-check`.

This reconciliation uses implementer2's existing
[final-handoff F evidence](../package-a-0.30.2/publication/final-handoff-f-ab934.json)
and [successful evidence-read exit](../package-a-0.30.2/publication/final-handoff-f-ab934.exit),
accepted by lead. The earlier [discovery](ci-discovery.json) and
[bounded job detail](ci-run-40379808743.json) remain historical in-progress
snapshots. No new query, test, project/Git operation or runtime action was used
for this records update. CI is complete; merge, installation and any
live-certificate repair remain separate, unperformed actions.

No F migrations, pins, policy/schema changes or installed package selection.
The source fix does not repair the running cluster's existing certificate.
No live guest/root/envelope, cluster, host/profile, session lifecycle, default
branch or Package C/PR74 changes are assigned or performed.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
