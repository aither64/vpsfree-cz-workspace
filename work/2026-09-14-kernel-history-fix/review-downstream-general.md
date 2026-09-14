# Downstream general review

Reviewed the committed downstream series and prepared rollout against the exact
packet revisions:

- vpsadmin `791ab3aa89e2f613979da6090b89785c78245db5..2a312616b0bf10465c33bbca97c79b31b22e8ec8`
- vpsfree-cz-configuration `249bed1ee28e69a907edd09ea97a1144dbcdefeb..4145e961376f064bccd665b36a7f7ef02de66867`
- vpsfree-kb-contracts `919577d0c770e47b623c591f8bf0cce4e8d30666..0770dcfae7834a43d8bc1a59f468aed037de2d80`

Lane: general. Model/effort: gpt-5.6-sol, xhigh. Risk: high because the
rollout adds schema used by two production supervisor writers and prepares a
separately authorized historical write.

## Findings

### Important

1. **The pre-migration check proves only that both supervisors are inactive,
   not that their runtime masks are installed and retained across the first API
   switch.** `rollout.md:15-23` runs `systemctl mask --runtime --now`, then
   checks only `systemctl is-active` before switching API1. An inactive service
   can still be unmasked, and there is no post-switch mask check before the
   migration. This distinction matters here: both hosts enable
   `vpsadmin.supervisor`, the unit is enabled through `multi-user.target`, its
   definition changes with the vpsAdmin package, and
   `vpsadmin.databaseSetup.autoSetup = false` means activation does not install
   `last_confirmed_at`. If a mask failed or did not remain effective, activation
   could resume the new supervisor against the pre-migration schema, defeating
   the required writer pause and causing unknown-column failures while reports
   are arriving.

   Require both `UnitFileState=masked-runtime` (systemd may display the
   equivalent runtime-mask state for its version) and `ActiveState=inactive` on
   API1 and API2 before the first switch. Recheck those two properties on API1
   after its switch and before running migration `20260914120000`; rechecking
   both hosts before the API2 switch would make the gate explicit. The existing
   `docs/operations/vpsadmin-livepatch-history-deployment.md` uses this stronger
   `systemctl show --property UnitFileState --property ActiveState` pattern and
   explicitly checks the mask after switching API1.

## Other review results

- The configuration commit is one generated `confctl` pin commit with its
  generated message intact. Its diff changes only the `vpsadminServices` lock
  node from `791ab3aa...` to `2a312616...`; `vpsadminStaging`,
  `vpsadminProduction`, all vpsAdminOS inputs, and channel definitions are
  unchanged. Flake metadata resolves the pinned revision and matching NAR hash.
- The KB commit is one logical contract-pin update. The exact vpsAdmin revision
  appears consistently in `flake.nix`, `flake.lock`, `captures.json`,
  `contract/navigation.yml`, and `contract/pages.yml`. The final diff leaves the
  vpsAdminOS revision at `6bdf458fd9105379860234ff33d352e55844f08f` and has no
  page, screenshot, source, test, or navigation-content change. The canonical
  check passed, including 94 semantic navigation bindings and all checker
  suites, so there are no new WebUI instructions requiring annotation.
- The two vpsAdmin commits retain the intended logical split between recorder /
  schema behavior and repair / integration / operator support. Commit messages
  describe the final behavior and meet repository rules. The pushed feature ref
  resolves to the exact downstream pin.
- The migration command derives the new database package from
  `vpsadmin-database-setup.service`, runs as the DDL-capable
  `vpsadmin-database` account from that package's `database` working directory,
  and supplies the corresponding production schema path. The later repair is
  kept as a separate dry-run-first action and the rollback retains both the
  additive column and evidence-supported repairs.

## Residual validation limits

The 11-consumer configuration build and the restarted short-path integration
runs were still in progress during this review. Their completion remains a
release gate. No production state or database rows were inspected, so the
node1 repair may legitimately find no retained proof and must remain separately
reviewed and authorized as the rollout says.
