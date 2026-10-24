# HaveAPI-only premerge preflight

User authorized HaveAPI default-branch integration and explicitly excluded WebUI.
[Compact receipt](premerge.json) binds the existing final review, README deletion
acceptance, installed-package proof and publication evidence without modifying them.

Source remains clean at40365b47a1a0c946367bc4596db6060853b52c0a,
tree3fe6010640cf64a063731fe8c49eb5819ca94b59. All five exact403 CI runs passed,
attempt1: release39431287229, Ruby39431287500, JS39431287329,
RuboCop39431287364 and i18n39431287150. No checks were rerun.

Live default remains refs/heads/master, but advanced from reviewedbasec587 to
c1823f3d70365b0442d0e2171bdf83bd4c6dbe31. Fetched master and local master both
name c182; feature remote still names403. Neither is ancestor of the other and
master contains none of the eight feature commits. Therefore current403 cannot
fast-forward master. Incoming is eight Python-client/release commits, 62 paths;
exact five overlaps are Makefile, README.md, doc/agent-instructions/releases.md,
utils/release/artifacts.rb and utils/release/spec/release_spec.rb.

The held claim1a971f9a-eb1c-4b18-ae1c-156e098d27c2 was independently checked for
HaveAPI repo/commonGit only before the released fetch. It remains held by lead.
No source/ref/worktree/sign/merge/push or other repository operation is authorized
beyond that fetch yet. The original feature/ref, f94 package identity and original
review/proof stay preserved. No cleanup or lifecycle action was taken.

## Minimum reconciliation proposal, not executed

Architect must bind exact overlap treatment before execution. Preserve the entire
incoming Python addition and its trusted publication, manifests/names, artifact
checks, hooks, Nix tools, specs and release docs. Replay the reviewed eight-commit
feature onto c182. Keep the JS source/runtime/declarations equal to403/f94; combine
only the five overlap paths as needed. In particular Python inspection belongs
in complete inspect_packages, outside isolated inspect_npm; version-regression
fixtures now encounter upstream Python uv lock semantics. Published feature
rewrite needs a later explicit lease release. HaveAPI allows development-branch
rewrites; WebUI's separate history constraints do not apply here.

Before any rewrite, preserve old403 (and ancestorf94) under an ordinary retained
source branch/ref, with remote retention authorized separately. Do not create a
tag or delete/rewrite the historical evidence. Ordered range comparison and
reconstruction must account for any overlap resolution; do not claim automatic
certified equivalence. Final affected interaction review and current-head CI are
needed. Proposed proportionate quicks: normal updated Nix release metadata,
combined release RSpec/Python artifact checks, disposable version regression,
scoped lint/hooks and source/runtime/declaration parity. No unrelated full client,
server or WebUI repeat absent a demonstrated interaction.

## Ordinary integration command plan after all gates, not executed

Use the existing exact held HaveAPI claim and verify claim-status again. Recheck
session binding and source identity/cleanliness, fresh fetch master+feature, compare
to the finally reviewed head and base, and capture the registered haveapi comparison.
Enter normal top-level nix develop with command-scoped Jakub author/committer.
Create only this new session-owned detached target checkout from origin/master:

```
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-haveapi-async-client/haveapi-master-integration
```

Commands after final reviewed head/base are supplied:

```sh
git fetch origin refs/heads/master:refs/remotes/origin/master   refs/heads/2026-10-19-haveapi-async-client:refs/remotes/origin/2026-10-19-haveapi-async-client
git merge-base --is-ancestor origin/master "$FINAL_REVIEWED_HEAD"
dev-session worktree capture-comparison 2026-10-19-haveapi-async-client haveapi --as-is
git worktree add --detach "$TARGET" origin/master
git -C "$TARGET" merge --ff-only "$FINAL_REVIEWED_HEAD"
git -C "$TARGET" push origin HEAD:refs/heads/master
git ls-remote --symref origin HEAD refs/heads/master   refs/heads/2026-10-19-haveapi-async-client
```

Stop if source/base/remote/claim differ. Verify normal post-checkout/post-merge/
pre-push hook output and actual target refs even when Git exits0. If hook trust
fails, diagnose before a separately scoped ordinary signing recovery; no bypass.
No force push of master, merge commit, source edit or automatic rebase in this
integration step. Verify exact final master and source clean, retain feature refs
and target checkout, then report to lead for explicit claim release. Do not remove
checkouts, stop/archive/finalize the session or touch WebUI.

Reconciliation design accepted. Owner0 preserved/published original403 under
2026-10-19-haveapi-async-client-before-master-rebase, retainingf94 provenance,
and owns rebase/code/index under the held claim. Updated Nix setup passed once
via fresh watcher01a15af8-5cb6-7662-a23d-4824b7005a58 (~8s), no source/index
change. Owner1's exact two-doc union20df9d3f passed main fact/prose acceptance;
source copying/stage/continuation remain serialized with owner0.

Final affected review accepted e165 all4lanes without findings; narrow prior npm
proof reuse accepted on exact inputs. See reconciliation-review.md. Publication
claim18b88bd2-7216-468e-a3bc-ee2f98a7f9e7 is waiting, no resources owned. No
feature/master publication while waiting; native grant resumes lead. Remaining:
newhead automatic CI, then authorized HaveAPI/master FF. WebUI stays unmerged.

Resume: native grant18b88bd2-7216-468e-a3bc-ee2f98a7f9e7 was independently
confirmed held revision2 at21:22:10Z. Own coordination status has no reservation
or unfinished operation. Current selected1pbx package claim guide/catalog read;
HaveAPI default remains master with the same SSH remote. Owner0 owns guarded
fresh refs and conditional reviewed-feature publication; further drift stops
before rebase/push. Existing user approval remains HaveAPI/master only.

Feature e165 published with exact lease; all6 CI workflows now SUCCESS. Release
job validated/tested/built and skipped registry publication. See
publication-e165/{receipt.json,ci-result.json}. Publication ownership released
while CI ran; final claim1cd94ef4-e345-44cf-b351-cc54733406dc is queued behind
the Python session's approved dependency-refresh default merge. Current target
will be rechecked after native grant; no source/default mutation while waiting.
