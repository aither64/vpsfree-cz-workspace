# Approved HaveAPI final integration execution

Prepare only until final current-head CI succeeds and lead supplies held claim.
User approval: HaveAPI/master only; vpsadmin-webui explicitly excluded.
Expected feature 7835acafdda19779815a0f1ba905d78e0085456d,
treecd466f8c35cd16dc64795fc9cd6091333d0d1a05;
expected remote target a8ea3132e7efe601aaa8965afe648459b3dab5c5;
original source backup40365b47a1a0c946367bc4596db6060853b52c0a and intermediate
backup e16526d42949bae96bf35e8db6cd984d739dcc2a retained.

After lead release, independently verify exact current identity and HELD HaveAPI
claim; fresh SSH fetch/check target, own feature and backup. Stop on unexpected
movement, dirty source or discrepancy; do not force master or replay on uncertainty.
Inspect complete current newbase-to-head series/diff against accepted review,
all current-head CI success and captured comparison before default mutation.

Create only the fresh session-owned integration checkout needed under this
initiative, through ordinary Git worktree commands/hooks. Use the normal repository
Nix environment and declared hooks, no bypass. Prefer checking out local master
in that new target if it is exactly the remote base and has no existing worktree;
otherwise the recorded detached-target route may preserve other checkouts, with
explicit proof of target effect. Do not inspect foreign working-tree contents.
A post-checkout error does not prove checkout was absent; inspect effects before
retrying. Standard target shell setup may run once through a fresh utility if
uncertain, but a watcher may not perform integration or trust changes.

Run ordinary git merge --ff-only of the exact reviewed feature into the target,
check command AND hook output/effect, then normal non-force SSH push to master.
Use command-scoped Jakub author/committer for any Git operation that can create
an identity (FF creates no commit). Legitimate signing only after exact current
hook/config inspection and within held ownership; no hook bypass.

Verify local target head/tree, feature/source cleanliness, remote master exact
final head (or proven ancestry if concurrent remote policy requires reporting),
feature/backup retained, normal hook result and command exits. Save compact/raw
receipt including target path, old/new refs, claim and user approval. Retain
all source/target checkouts/branches/evidence; no cleanup/lifecycle or registry
release/deployment. Notify lead when no mutation process remains; lead releases
resource ownership after effect verification. Observe automatic post-merge CI
metadata once if useful, without rerunning unchanged successful source gates.
