# Prepared Terraform VM successor

The first attempt is preserved at
`/tmp/flake-update-guard-provider-r-1/terraform-smoke/`. Exact failure/effects and
source/native trace hashes are in
[package-c-terraform-r-failure-reconciliation.json](package-c-terraform-r-failure-reconciliation.json).
It stopped in the before-suite services.start call: OsVm::Shell#prepare tried
to create a 125-byte UNIX socket path, exceeding the 108-byte limit. No one of
the eight examples ran and no test guest QEMU process was spawned. Image build
preparation completed earlier; it is separate from test-guest startup. Native
machine logs show kill NONE/destroy. Source/index/lock are unchanged, external
push stays disabled, and process/UNIX-socket scans found no owned remainder.
No cleanup or retry was performed by implementer0.

The lead confirmed that the first utility transcribed a shorter root by omitting
the date. The original driver did honor its --root argument. Even that shorter
root exceeded the socket limit, so correcting argv alone would not suffice.
The successor changes only two evidence-driver state path references from
`terraform-workflows-state` to `t`, and uses exact new root
`/tmp/flake-update-guard-tf2`. Original driver/manifest/receipts/logs remain frozen.
The new state path is
`/tmp/flake-update-guard-tf2/terraform-smoke/runner-temp/t`.

Exact native source/config analysis gives all expected shell/virtiofs socket
lengths of 88, 92, 97 and 101 bytes, below 108. Both machines have one shell and
no extra shared filesystem; the native vmSharedDir is included. The
[static preflight](package-c-r-terraform-smoke-2-preflight.json) and
[two-line diff](package-c-r-terraform-smoke-2.diff) retain this calculation and
scope. No socket, test runner, VM or build was launched during preparation.

Frozen source identities:

- Terraform reviewed source: `f835d63b14931712129771792039f645cf6a3305`.
- Provider R: `5436d3d7c36d3d5174eab3c44e3578830749d3db`.
- Successor driver `package-c-r-terraform-smoke-2.py`:
  `685afed748231be3b8b9a708de4dc22045217282d6a7f54a6a67e6200da2d179`.
- Fixed launcher `package-c-r-terraform-smoke-2-launch.py`:
  `e7a1e4b1adac62283a958667db0a5f4dee14e3e8c21364c70522ce0f4adf3249`.
- Unchanged manifest `package-c-r-verification-manifest.json`:
  `bbeec793c0c6407023bd4f5eda8d942dbeaeded7cc7e435725d4352575023e8c`.
- Unchanged final R review `review-r-report.md`:
  `2b9ecce9d66a5994e664b99ba0c1f1454631c14a923a53f58b25ece48ded99a9`.

The no-argument launcher verifies those frozen driver/manifest/review hashes,
prints the full JSON argv without reading or printing credentials, then execs
the driver. Its root, review and terraform-smoke stage are literal. The fresh
Luna watcher must launch only the following command from the verified workspace
root, with GITHUB_TOKEN supplied privately; do not transcribe the inner argv:

```sh
python3 work/2026-10-24-flake-update-downgrade-guard-replacement/package-c-r-terraform-smoke-2-launch.py
```

The driver first checks `./test-runner.sh ls workflows` returns only workflows.
The actual native command is unchanged except for its shorter state path:

```sh
./test-runner.sh test -f --jobs 1 --stop-on-failure \
  --state-dir /tmp/flake-update-guard-tf2/terraform-smoke/runner-temp/t workflows
```

Keep the singleton workflows test and all eight ordered shared-state examples,
two native machines, existing user/socket networks and native runner defaults.
The selected Nix output remains .#tests.x86_64-linux.workflows. There is no
cluster, network override, per-example subset, source/input/pin/application edit
or alternative runner. Preserve full source/input/derivation/output receipts.

Root alone launches the authorized serialized watcher after accepting this
packet. Require the receipt at
`/tmp/flake-update-guard-tf2/terraform-smoke/receipt.json`. Any different printed
root/argv or nonzero result stops and reports; no retry, alternate root, source
edit, diagnosis or cleanup belongs to the watcher. Stop/escalate an unexpected
local Linux kernel build, retaining native owned-process cleanup. Quiet output
is not a timeout. No machine ownership, default integration, deployment or
session lifecycle operation is authorized by this packet.
