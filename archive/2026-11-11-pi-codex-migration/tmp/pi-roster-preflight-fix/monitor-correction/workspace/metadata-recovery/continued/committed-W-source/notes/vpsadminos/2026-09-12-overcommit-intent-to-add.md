# Avoid unrelated intent-to-add files during partial commits

In the Nix dev shell, Overcommit stashes unstaged changes before checking a
partial commit. Unrelated `git add -N` entries can make restoration fail with
`Entry ... not uptodate. Cannot merge`. Keep future new files untracked until
staging their actual owning commit. Stage only the intended commit's files.
The NFS cancellation series committed successfully after removing unrelated
intent-to-add entries without deleting their files.

Do not inspect the unstaged implementation concurrently with an active commit:
Overcommit temporarily restores its older version while hooks run. Wait for the
commit to finish before inspecting or editing that tree.

Related initiative: work/2026-09-12-nfs-cancellation/.
