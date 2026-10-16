# Failure-only guest readiness diagnostics

Reviewed source: `799c0fc9decd87b4f690c69b7e47e776a48e44f5`.
Only `tests/suite/dist-config/nixos-persistence-upgrade.nix` changes,
unstaged; index empty, source frozen. Session/current and retained roster
revision 18 match; implementer0 retains Sol/xhigh/workspace_write.

Attempt ownership identifies `/tmp/ni.fpxcd1j5` at head 799c0fc9/tree fa3adcb3.
The runtime/runner/console/shell logs prove both prior setup corrections work.
`osctl ct start testct-1fb2` returns 0; the initial old 26.05 generation then
returns degraded repeatedly to the exact readiness wait. It times out at 180
seconds before the old live switch and all preservation assertions. The next
case begins before the lead cancels the attempt. No unhealthy baseline is
accepted and no upgrade result is established.

No actual failed guest unit name/result is present in the inspected evidence.
The generic host diagnostic's guest networking journal has no entries, and
host service/pool warnings do not identify the guest's systemd failure. The
source alone cannot select a service cause. No speculative fixture, raw module,
provider or service change is justified.

The suite now calls one local readiness lambda at its original initial/restart
positions. It executes the exact existing systemctl is-system-running --wait
command with timeout 180. Only on a StandardError does it capture:

- Actual guest systemctl --failed, plain/no pager.
- Up to 160 current-boot journal lines with precise timestamps.
- For up to eight failed units, full status (40 lines), ActiveState/SubState,
  Result, ExecMainCode/ExecMainStatus and up to 40 current-boot unit journal lines.

Each diagnostic uses the existing machine.execute/osctl ct exec interfaces,
with a 20-second host timeout plus 2-second kill bound and 25-second machine
execution deadline. Captured output is bounded to 32 KiB per diagnostic. Normal
machine-shell logs retain execution/output; warnings also add results to the
test log, labeled guest and initial-boot/restart phase. Diagnostic exceptions are
caught per command; the original readiness_error is re-raised afterward.
No degraded acceptance, reset-failed, unit disablement, new dependencies,
ownership/data changes or weakening of assertions.

`readiness.patch` is the exact diff. An inverse-wrapper comparison recreates
the previous reviewed suite byte-for-byte, proving all other suite content is
unchanged, including the two setup corrections and every invariant. Fixture and
all source inputs are untouched. Static checks passed: prepared nixfmt --check,
nix-instantiate --parse, prepared Ruby -c on a static combined template with
placeholder Nix values, Bash -n on the diagnostic fragment, git diff --check.
Templates prove syntax only; no generated Nix or runtime evaluation was run.
No staging/commit/ref/push/lifecycle or Nix/build/runtime operation performed.

The next targeted upgrade-26.05 attempt remains a diagnostic runtime under the
lead's committed-review/watcher workflow. The precise failed guest unit(s) and
journal are the missing evidence needed before assigning a cause-driven fix.
