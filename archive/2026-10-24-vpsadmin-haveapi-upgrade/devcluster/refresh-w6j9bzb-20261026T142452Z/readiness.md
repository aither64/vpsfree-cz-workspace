# Package E read-only refresh, 2026-10-26 14:24 UTC

Preparation only; activation remains unreleased. Earlier receipts, driver,
native stub and prepared roots were preserved. Lifecycle, deployment,
verification, selected installed coordination guides and provider contracts
were reread; the unchanged provider documentation/source was reconciled.

Two deltas require lead disposition before preparing the launch command:

- Selected runtime is now
  `/nix/store/w6j9bzbv7m04h7snndb5bs9jj39jd2kc-dev-workspace-0.2.0`,
  provider `/nix/store/q19s1vj5yn00jq46n4gs7g10z5f76y68-vpsfree-dev-workspace-tools-0.1.0`.
  The accepted driver's runtime/provider constants are still `fa7zlb...` /
  `7vrkd...`; both command realpaths fail its old runtime guard. Driver bytes
  remain SHA-256 `99308b0ece76fbe53a003b844c3b137056e904eccf6b614024610a46ad89d3e1`.
  The new catalog SHA-256 is
  `2bdcaf54019f518a3c7876a04c7f30a8c9f6b86dd86649da9585b2f7c770d12a`.
  All 42 provider native files equal the accepted provider. Runtime contract
  SHA-256 remains `9c8e9e5c371eda46ccb49eaf275ee4996d2ddce3930c9047da39ccd195f67183`,
  state schema 1 / transition policy 3.
- The 20-node effective graph has one changed node, `vpsadmin`:
  locked NAR hash changed from
  `sha256-4l9c0i/1a3ia7r9ylbZeOv0IzYC6Q9PUUpXEg6+c4EU=` to
  `sha256-7+95mErWohWFPhKV1g7NkUP7k0ftftDIXS1q+hMnQQA=`, and
  lastModified from `1793007627` to `1793023582`. Its own worktree path,
  original input identity and follows remain identical. All other 19 nodes
  match. Clean Git status alone does not explain or establish equivalence of
  this changed path-input content; the file-level cause was not investigated
  or accepted in this refresh.

Own API `70a2ed54b98d0c2f359a9cc4484452a257a9807b` and React
`f10d3d48c4f21cc39187c3667ffffd9952404c11` remain clean. Native OS
`origin/staging` remains `d9be8c4bada590c0405df85444600d40e6f3caa6`.
The advanced API master is not selected; no source/ref rewrite occurred.

One public metadata command completed exit 0 in 32.56 seconds with IFD
disabled, max-jobs=0 and no lock write. Its exact parent handle completed;
no duplicate command or watcher was launched. Metadata SHA-256:
`f3d029afb75246aec606f6eda29257967f470b4d49d9cf99ad02ad1218936501`.
Provider source/NAR remain `kvr5zvhzdd03ps2lb9fbw8k5gvz9hk1d-source` /
`sha256-SxA5jLINqum9hG3IpkFIwv5LivBi2Sck1ZRf72GOCwg=`.

Allowlisted native status is stopped, ready=false, no selected topology or
network. Only original `config.json` / `socket-dir` remain; before/after
status checks have identical entry and file hashes. Config SHA-256 remains
`10819c2d393795f4909695f04e4caf3d4035a94e84e25c871ecfc1ab19a16332`;
the recorded socket matches the workspace/slug digest and remains absent.
No pending/applied selection, result, runner, disks or credential bundle was
created. All seven prepared root links remain registered at original targets.

No capacity/address snapshot was taken. Immediate pre-start graph/source,
generation, native ownership/pending, capacity/process and collision checks
remain necessary after final VPS-ops/guest clearance and lead release. The
accepted 32 GiB / 12 CPU resident scope, separate daemon headroom, two-job /
four-core requests, output filter and independent observation contract remain
the proposed boundaries. Whole-cluster derivation proof remains deliberately
IFD-blocked historical evidence, not a newly passed check.

No driver edit, graph acceptance, startup, build, host/foreign-hold/lifecycle,
KB/staging/production mutation or shared-index/commit action occurred.
Evidence: [refresh.json](refresh.json), [full metadata](effective-flake-metadata.json).
