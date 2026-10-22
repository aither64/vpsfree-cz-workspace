# Python README context change

User asks only Python client README to explain what vpsAdmin is, that it is the
main HaveAPI user and why examples use it. Lead verified reference README:
vpsAdmin is control panel managing virtual servers on vpsAdminOS, deployed at
vpsFree.cz. Added one linked paragraph after opening client description and
before installation. Exact text points to official vpsAdmin repo, describes
control panel used by vpsFree.cz for VPSes, primary HaveAPI use/examples.

Low-risk documentation-only, general lane. No API/runtime/tooling/dependency/
migration/server/compatibility change. No tests needed beyond link/Markdown/diff
and normal hooks. Separate new doc commit gives this user-requested explanatory
addition one reviewable purpose; prior seven implementation streams unchanged.
Base c58704a; prior verified/published head326c05b. New exact commit in assignment.
Reuse original complete branch/history review, affected reviews and narrow fix
acceptance. Check only paragraph and current series/no obsolete updates/no
migrations. No shell setup/live tests/source writes. Lead main writing pass done.

Lead link check: official GitHub destination returns HTTP200.

Exact committed headc1823f3d70365b0442d0e2171bdf83bd4c6dbe31,
treeaec5847f4c735ac68a7b6158c76a4f667f6a6a18, parent326c05b unchanged.
Only4insertions README, normalhooks passed, clean index/worktree.

Reviewer0 final general-only review: NO FINDINGS. Same retained Sol/xhigh/read-only
identity/settings, exactc1823f3 inspected. Facts/placement/link match usercontext
and reference README, generic client scope remains clear. Standalone explanatory
commit accepted, original7streams unchanged ancestors; no obsolete/fixup/repeated
pin/generated stream. NO MIGRATIONS/runtime/API/dependency/compatibility change.
Clean/diffcheck verified, no tests/setup/writes by reviewer. Review gate complete.

Feature-only normalFF publication confirmed by implementer1 atc1823f3;
origin/master fetched unchangedc58704a, clean/no source changes. NewheadCI3runs
Python39413502893,release39413502904,i18n39413502897; fresh utility assigned.

All3exactheadCI workflows SUCCESS, fresh watcher receipts verification/readme-ci.
Requested documentation update complete; no runtime change.
