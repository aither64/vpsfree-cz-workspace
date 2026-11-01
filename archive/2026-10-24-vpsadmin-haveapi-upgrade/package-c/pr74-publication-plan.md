# PR74 reuse — exact published-history decision pending

Own feature branch is published and independently verified at
`f10d3d48c4f21cc39187c3667ffffd9952404c11`:
https://github.com/vpsfreecz/vpsadmin-webui/tree/dev/vpsadmin-haveapi-upgrade
Repository SSH remote: `git@github.com:vpsfreecz/vpsadmin-webui.git`.
No force push, PR edit/new PR, default integration or deployment occurred.
PR74 remains open on its original `dev/haveapi-async-client` alias:
https://github.com/vpsfreecz/vpsadmin-webui/pull/74 .

## Concrete range replacement for approval

The user permits PR reuse. Replacing these exact published commits still needs
separate explicit authorization; own-branch publication does not grant it.

Old published range:
`7860521f30826c3886c89c35e8ab6f4e082e0a4b..5dd2333b9af230d4a81c8f772cbbb08d39b14913`.
Its two commits:

- `0d05a2584bf30ee4acfa1d64bf00325cdda62934`: injectable package pilot.
- `5dd2333b9af230d4a81c8f772cbbb08d39b14913`: prior package proof docs.

New final complete range:
`5a2d2bdc3ad7a827038f877d75959916528db844..f10d3d48c4f21cc39187c3667ffffd9952404c11`.
Its two commits:

- `02b45a7de7eec8966b6a2ade16a46fbb9e1b6c83`: exact npm0.30.2 registry
  dependency, lock, provenance, source guards and normal Nix hash.
- `f10d3d48c4f21cc39187c3667ffffd9952404c11`: production AsyncClient adoption,
  application admission/error/renewal policy, actual-client fixtures/tests,
  current docs, closed R2 ambiguity correction and accepted narrow OPTIONS
  script-assertion correction.

Final tree `e1084bb80dd07140719034ab908a6f62daff855b`.
The old final local content source is
`7860521f30826c3886c89c35e8ab6f4e082e0a4b..8772bab21cd8739bf4672cdf4976aea2a6e59de3`,
including intermediate archive dependency `3b2eed453f385ee37d07c7339edcce8fc28ffd31`.
It is a nonancestor content source, not literal merged ancestry. Obsolete pilot/
vendor history was not replayed. Seven current-main overlaps and carried original
Jakub Skokan authorship/dates are preserved. Complete content-mapping.json,
commit-series.txt, final.diff and old/new range-diffs remain in this packet.
Retained reviewed014f7b9c/757f7fd8refs/evidence remain unchanged.

No migrations, schema/persisted-format/wire change or released/deployed/external
consumer boundary requires the superseded history. Old local refs, old worktree/
records, PR63 and unrelated refs remain untouched.

## Actual acceptance and publication evidence

Independent final review and narrow-fix acceptance retained. Quick checks,
script228/BFF57/unit1899cases, normal production build and Nix frontend/BFF/
provenance/source/package-content checks passed at exactf10. Normal artifacts
and sources are restored to recorded exact paths/NARs and persistently rooted.

The current full rooted browser result is60/62(desktop31/31,mobile29/31).
Both mobile user/admin transaction-expand failures reproduce on exactbase
under identical runtime/context/geometry/interception. Architect/lead accepted
that specific preexisting interaction residual as nonblocking for scoped upgrade
and development testing subject to remaining gates. This is not a clean-browser
claim; exact CSS cause remains unproven. No UI/test fix or new run assigned.

Lead explicitly released ordinary own-branch publication. Fresh fetch verified
main5a2d2bdc without updating refs; source/head/clean/SSH/hook/alias boundaries
passed. One-refspec no-force push completed exit0 in2.634s. Independent remote
proof confirms ownref=f10, main/HEAD=5a2d2bdc, PR74alias=5dd2333b. All existing
local refs/worktree unchanged. Exact command/log/preflight/remote/ref snapshots
and receipt are under0.30.2/publication/ (relative to package-c).

Exact-head GitHub run/check/status queries show no CI triggered. Workflow push
filters accept main, PR events apply after PR updates, and nightly uses schedule/
manual events; ordinary own-branch push alone does not match. No manual dispatch
or PR action was substituted. No failing CI run to retry/cancel at this head.

## Only after exact rewrite authorization

1. Lead records approval of the named old/new ranges above. Freshly inspect
   remote ownref=f10, main=5a2d2bdc, and PR74open/headalias=5dd2333b targeting main.
   Any moved source/alias/base returns to lead; never silently expand the lease.
2. Authorized exact-lease command (NOT executed):

   ```sh
   git push origin f10d3d48c4f21cc39187c3667ffffd9952404c11:refs/heads/dev/haveapi-async-client --force-with-lease=refs/heads/dev/haveapi-async-client:5dd2333b9af230d4a81c8f772cbbb08d39b14913
   ```

3. Reconcile remote effect before retry if uncertain. Require both own branch
   and PR74head=f10, PR targetmain and default/PR63unmodified. Keep old local
   refs/worktree/records/reviewrefs intact. PR74is a publication alias only,
   not a reassignment of the owned registered branch.
4. Update PRmetadata only as lead directs. Observe exact-head triggered checks;
   cancel only superseded queued/in-progress runs for that headbranch, retaining
   logs and diagnosing failures before any rerun. No new PR requested.

No default-branch integration, cluster action, deployment, root cleanup or
session lifecycle action is authorized by this plan or publication.
