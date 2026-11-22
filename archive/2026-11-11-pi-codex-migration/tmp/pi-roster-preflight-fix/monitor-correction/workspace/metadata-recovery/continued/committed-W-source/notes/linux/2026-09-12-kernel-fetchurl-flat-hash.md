# Match kernel hashes to fetchurl's flat archive mode

vpsAdminOS os/packages/linux/default.nix fetches a GitHub tarball with fetchurl.
Use `nix store prefetch-file --json --name REV.tar.gz URL` without --unpack.
An unpacked prefetch returns a directory and its NAR hash, which is unsuitable
for this flat hash pin even if its name ends in .tar.gz. Check both the returned
path's type and the consuming derivation's output method.

When github.com archive redirects returned HTTP 429, prefetching the same exact
revision from https://codeload.github.com/vpsfreecz/linux/tar.gz/REV with the
original REV.tar.gz name populated the expected fixed-output store path. Compare
extracted changed source against the committed worktree. This avoids changing
the repository's source URL merely to work around a local rate limit.

Related initiative: work/2026-09-12-nfs-cancellation/.
