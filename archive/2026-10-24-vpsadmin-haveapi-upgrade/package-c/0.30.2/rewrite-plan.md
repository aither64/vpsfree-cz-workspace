# Unpublished history consolidation

Old exact range:
`5a2d2bdc3ad7a827038f877d75959916528db844..014f7b9c9f451d6275af73c4af30a24668b77b7b`.
Old final ref `refs/heads/dev/vpsadmin-haveapi-upgrade-reviewed-0301` preserved.
Old two commits: dependency `cd3577a6365685273c1b39a724814f7d67931508`,
production+R2 `014f7b9c9f451d6275af73c4af30a24668b77b7b`.
No published own branch, merged/released/deployed source or migration boundary.
PR74 protected published commits remain untouched by this local reconstruction.

Prepare two narrowly scoped local fixups using ordinary Git commit/hook path:
root dependency/lock/Nix hash/provenance folds into dependency commit; current
provenance/package docs and dated work-log folds into production commit. Run
interactive autosquash from unchanged base, reword dependency subject to0.30.2.
Keep both original authors and author dates. Compare the pre-rewrite full tree
with the reconstructed final tree, require equality and inspect range-diff.
Save exact old/new range, tree IDs, complete final series/diff/source map and
no-migrations conclusion. The final branch contains two logical commits with
one selected0.30.2 dependency stream, not successive0.30.1/0.30.2 pin commits.

No repository-wide reset/stash/clean, main/ref rewrite, push, PR update,
deployment or merge. Fixup refs/commits are local intermediate Git operations;
original old final ref remains the read-only review/recovery anchor. Any rebase
conflict needs owner diagnosis and explicit patch verification before continuing.
