# PR74 successor plan: no protected rewrite authorized

Preserve exact original published alias `dev/haveapi-async-client` and PR74 head
`5dd2333b9af230d4a81c8f772cbbb08d39b14913`. Live/published own branch
`dev/vpsadmin-haveapi-upgrade` remains `f10d3d48c4f21cc39187c3667ffffd9952404c11`. New independent registered
branch `dev/vpsadmin-haveapi-031` is published at `baf00acc31d34ab37720643c5833b4476a341f3b`.
Fresh main remains `5a2d2bdc3ad7a827038f877d75959916528db844`. See [remote reads](final-remote-boundaries.txt).
No PR, alias, old ref/worktree, live config/lock or cluster change occurred.

Old published range:
`7860521f30826c3886c89c35e8ab6f4e082e0a4b..5dd2333b9af230d4a81c8f772cbbb08d39b14913`
(two pilot/docs commits0d05a2584bf30ee4acfa1d64bf00325cdda62934 and5dd2333b).

Concrete independently reviewed new range:
`5a2d2bdc3ad7a827038f877d75959916528db844..baf00acc31d34ab37720643c5833b4476a341f3b`,
exactly `4d040e0357e405761432075a23783b4d0d779432` (direct npm0.31) and
`baf00acc31d34ab37720643c5833b4476a341f3b` (carried production/R2/OPTIONS plus current docs).
Tree `2e7b4cb5eba6bc96f34f834c49fc097d5fdd987b`. No migrations or obsolete intermediate pin commits.
[Full mapping](content-mapping.json), [old/new range-diff](old-new-range-diff.txt),
[complete series](commit-series.txt), [final diff](final.diff).
Original f10 is a retained live/consumed predecessor, not literal ancestry;
all its runtime/test content is unchanged in this successor. Preserve that ref.

Final review, quick, full unit/build and required Nix checks passed. The two
bounded browser batches remain 3/6 and 5/6; the separately released controlled
desktop expiry comparison now passes at both f10 and baf. See the
[paired receipt](expiry-paired/receipt.md). Lead accepted the scoped current
correctness disposition and released the new own-branch publication. Its
[final receipt](publication/receipt.md) includes independent remote proof and
bounded CI discovery. No failed result is masked or exact failure cause claimed.

The new own branch was published by one explicit no-force SSH refspec. This
plan grants no protected rewrite. Reusing PR74 still
requires explicit authorization for replacing the exact old/new published ranges.
If granted later, freshly verify target, source and expected old alias head before
any exact-lease action; a moved boundary returns to lead. No force command was
executed, and no default integration or live deployment follows from publication.
