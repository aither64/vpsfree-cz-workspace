# Mandatory change review: risk and compatibility

Lane: risk and compatibility
Model/effort: `gpt-5.6-sol`, `xhigh`
Reviewed repository: `vpsfree-dev-workspace`
Reviewed range: `0a9c974994746e2a6d9d74e83cde8abbf0e65f0a..54b1d7a3f3cbfc4261abbe2fc3632d0908599696`

The review covered the four commits in the range, the consuming workspace's
`siteConfig.clusterDefaults` and extension pin, the generic runtime at
`bcbaf825d71285cbbd05b56e78bc386f2df480bd`, and the vpsAdminOS overlay and Ruby
gem interfaces at `3eaf7b7320754715b38fc629e7f0ce23d13402cd`.

## Blocking

None.

## Important

1. **A failed certificate replacement can destroy the last usable credential set.**
   In commit `35a7090`, `ensure_cert_domains` treats an encrypted CA that cannot
   sign unattended as a reason to call `cert_init --force`
   (`dev-clusters/vpsadmin/bin/devcluster:366-390`). `cert_init --force` first
   removes every existing CA and server-certificate file and only then runs the
   individually checked OpenSSL steps (`dev-clusters/vpsadmin/bin/devcluster:393-432`).
   `cert_import --force` has the same remove-before-copy sequence at lines
   435-490. For example, after defaults add a required domain, an existing
   encrypted CA returns status 2 from `cert_reissue_server`; the helper removes
   the working CA and certificate, then a disk-full or OpenSSL failure while
   creating the replacement makes `start`/`update` return nonzero with no usable
   credentials left. Retrying may create a different CA and forces browser trust
   to be re-established. This violates the packet's credential-integrity and
   retry/rollback assumptions. Build the complete replacement in a private
   temporary directory on the same filesystem, validate it, and swap it into
   place only after every step succeeds. Add a failure test that begins with a
   usable credential set and compares its contents after a late replacement or
   import failure. The destructive sequence predates this range, but the changed
   failure-propagation path and its new credential-failure tests directly claim
   this safety boundary without covering preservation.

2. **Start can report success from a stale readiness marker after preparation
   cleanup has failed.** Both start functions remove the prior readiness/PID
   files and socket directory, recreate the socket directory, and append the log
   header without checking any result
   (`dev-clusters/vpsadmin/bin/devcluster:912-920` and
   `dev-clusters/vpsadminos/bin/devcluster:405-413`). These functions execute as
   callbacks below `devcluster_with_lock`'s shell conditional, so `set -e` is not
   reliable here; that is the exact execution property commit `35a7090` was
   written to address. If an owned cluster directory becomes non-writable, the
   filesystem becomes read-only, or removal otherwise fails while an old `ready`
   file remains, the helper still launches the runner. The vpsAdminOS readiness
   loop observes the old file immediately, prints cluster information, and
   returns success before the new launcher has become ready; the launcher may
   then fail because its socket/PID paths could not be prepared. vpsAdmin can
   similarly act on stale readiness and contact previously configured nodes.
   Check and propagate every cleanup/create/log-write result before launch, and
   cover a retained-ready preparation failure in the actual-command tests.

3. **The repaired package introduces an undocumented minimum vpsAdminOS source
   revision for every existing development worktree.** Commit `30516d8` calls
   the imported overlay as a function with `vpsadminos.inputs.netlinkrb` and
   `ruby-lxc`, then requires `pkgs.vpsadminosRubyGemConfig`
   (`dev-clusters/vpsadminos/flake.nix:39-43,69-78`). Those interfaces were
   introduced together by vpsAdminOS commit
   `b0c2ea2552ab9b3bcb493a6bdad5f23c698addcc` on 2026-06-11. The public provider
   contract selects any `worktrees/<slug>/vpsadminos` checkout, but neither the
   CLI nor documentation declares that minimum. After deploying this package,
   starting or updating a retained initiative whose vpsAdminOS branch predates
   that commit fails during flake evaluation: the older overlay is a list rather
   than a function and has no `vpsadminosRubyGemConfig`. The new smoke test pins
   only the current `3eaf7b7` interface, so it cannot detect this mixed-version
   failure. Either support both interface shapes, or explicitly constrain and
   validate the source revision/interface before building and record the rollout
   action and rollback limitation in the plan and provider documentation.

## Advisory

1. **The vpsAdmin config replacement is not guaranteed to be atomic.**
   `ensure_cluster_config` creates its temporary file with bare `mktemp`, then
   moves it over the persistent cluster config
   (`dev-clusters/vpsadmin/bin/devcluster:152-160`, commit `35a7090`). When
   `$TMPDIR` and the workspace are on different filesystems, `mv` degrades to a
   copy-and-remove operation. An interrupted or out-of-space copy can damage the
   retained config even though the command returns failure; a failed `mv` also
   leaves the temporary file behind. Create the temporary file beside
   `config.json`, preserve its intended mode, remove it on every failure, and use
   same-filesystem rename for the commit.

## Residual risks and test gaps

- The amended `54b1d7a` smoke test evaluates both network modes and loads the
  runners, but it deliberately does not realize VM closures or exercise runner
  state and disk compatibility. The planned start/update/stop/restart and data
  marker checks remain necessary after the Important findings are resolved or
  explicitly accepted.
- The command stubs prove control flow for selected failures but do not exercise
  real Nix out-link replacement, real SSH partial activation, certificate
  preservation, retry after partial setup, or package rollback with retained
  cluster state.
- The consumer worktree still pins organization commit `0a9c974`; review of the
  generic extension/generation contract found no incompatible catalog, CLI,
  state-schema, socket-identity, or VM-disk format change in this range. The
  eventual mechanical pin must name the final reviewed and pushed extension
  head and retain the generic runtime pin.
