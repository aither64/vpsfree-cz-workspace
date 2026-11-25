# vpsAdmin history consolidation

Published canonical feature head `669fb9feebb191e94a08ea719388ffa6cc0e3291`,
tree `c8332d430a13845fd3452e1ba203e05542d7b155`. Above unchanged base/default
`4062a8da3314aa7b48170b0d6f441446bad9b207` there are exactly two purposes:

1. API `1bf47e4ec55d9f15cea486762479db8bc2c8d6aa`.
2. Combined PHP UI `669fb9feebb191e94a08ea719388ffa6cc0e3291`.

API-first is the smallest mechanical ordering: original `926b..8846` API patch
applies directly to4062 unchanged; the final PHP UI then includes its original
Overview/History purpose and the later simplification. Original author and
committer identities/dates are preserved for API8846 and PHP926b. The API message
is unchanged; the PHP message describes final behavior. No obsolete UX fixup
remains. [Old history](old-history.txt), [new history](new-history.txt),
[range comparison](old-new-range-diff.txt) and [proof](history-proof.json) bind
this disposition.

Final tree and complete binary4062 diff equal deployed/publica25b exactly.
[Original API patch](original-api.diff) and [new API patch](new-api.diff) are
byte-equal. No file content, mode, catalog, documentation, API contract, schema
or migration changed in this package. [Old full diff](old-full.diff) equals
[new full diff](new-full.diff). Consumed migration20261030180000 is the same
Git blob `ff9dd726f935aabef487ad7b9b8b047756eeefcc` in4062, a25b and669fb9;
SHA256 `2eec970fb3620ad25f3ac01c06a9eae61af2d208f88184e995c74b8ad2ba2c1e`.
Obsolete20261115120000 remains absent. Existing consumption/deployment and review
provenance remain in the [accepted backend packet](../../nov24-admin-incidents/backend/review-consolidation/packet.md)
and [full review](../../nov24-admin-incidents/ux-final-review.md).

Reconstruction and normal hooks ran only in nonmounted `vpsadmin-nov24-ux`, on
`2026-11-24-incident-admin-consolidated`, with ordinary0022umask. API hooks passed
in72.839s; PHP hooks passed in67.872s. API commit-message warnings concern its
retained73–75column lines; every line meets the repository80column limit. Both
source commands, fresh installed Luna/low utilities and parent handles joined.
One API observer-only read had a quoting error; the PHP observer looked in the
wrong directory. Their original reports remain; parent reads of the actual
absolute result/log paths establish both hook results. No app checks were rerun.
Earlier product, derivation and runtime evidence retains its literal original
revision/input scope; this package proves history/content equivalence.

Canonical live-mounted `vpsadmin` remains on its registered feature branch.
After fresh expected-olda25b, exact-tree and clean-index/worktree guards, only
`git update-ref` changed its branch metadata to669fb9. No checkout, replay,
restore, chmod, reset, clean or stash occurred there. Before/after logical index,
tracked permission/type aggregate and clean content/mode checks agree across
3238tracked paths. [Before](canonical-before.json), [after](canonical-after.json)
and [publication proof](publication-proof.json) retain these results.

Fresh fetch/default/unmerged checks preceded an explicit a25blease SSH push.
SSH readback and immutable [GitHub commit](github-commit.json) confirm669fb9/treec833;
master stays4062. Public `2026-11-24-incident-admin-php-ux` stays at olda25b for
existing KB/deployment references. Create-only local preservation branches retain
926b,8846,a25b; existing review refs remain. Olda25b is not an ancestor of669fb9:
this is an equivalent successor, not a claim of literal deployed-head integration.
Comparison capture records4062..669fb9. No KB repin or default integration occurred.

One finite CI page inventoried100of161branch runs. Five current669fb9 workflows
were queued at that reading. Only freshly guarded superseded same-branch CI runs
45431668108/a25b and45405368956/8846 received successful cancellation requests;
terminal cancellation was not observed. No CI wait, rerun or dispatch occurred.

All owned native/source/Git/check/publication effects are terminal; no uncertain
local effect remains. Source/index/Git windows and capacity return to root.
Root owns the combined bounded history review and acceptance. Product docs are
unchanged because this package changes history only. No runtime, build, SQL,
browser, deployment, cleanup or lifecycle action occurred; the session stays open.

[Receipt](receipt.json) · [Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
