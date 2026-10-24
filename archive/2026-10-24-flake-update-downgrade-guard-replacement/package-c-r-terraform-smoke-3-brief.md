# Prepared private-auth Terraform VM attempt 3

Prepared only. The lead accepted the fresh root
`/tmp/flake-update-guard-tf3` because the unchanged driver requires that prefix.
The interrupted TF2 root, first failed root, logs, receipts, source and original
scripts/manifests remain preserved. No auth loader, credential command, test,
build, network operation or runtime was executed while preparing this packet.

The new executable, no-argument launcher is
`package-c-r-terraform-smoke-3-launch.py`, mode 0755, SHA-256
`ec2d46195ee75147dba360cad5d8b033622b0694ebb502dd733d1d91ee485319`.
Its only private auth subprocess is `gh auth token --hostname github.com`,
inside deterministic launcher code. Inherited GH_TOKEN/GITHUB_TOKEN are removed
from that subprocess's environment to select the relogged stored credential.
Both stdout and stderr are captured in memory through PIPE; neither is printed,
saved or included in an exception. Failure, decoding error, empty or multiline
output produces only a generic credential-loading error. The stripped value is
placed in the child environment's GITHUB_TOKEN; GH_TOKEN is removed. No token
appears in argv, logs, files or an environment dump. Exec failure is generic too.

The launcher retains frozen driver/manifest/review hash checks, prints only the
full safe JSON argv before exec, and accepts no arguments. It runs unchanged
short-state driver `package-c-r-terraform-smoke-2.py`, SHA-256
`685afed748231be3b8b9a708de4dc22045217282d6a7f54a6a67e6200da2d179`, with unchanged manifest SHA-256
`bbeec793c0c6407023bd4f5eda8d942dbeaeded7cc7e435725d4352575023e8c` and review SHA-256
`2b9ecce9d66a5994e664b99ba0c1f1454631c14a923a53f58b25ece48ded99a9`.
Source remains Terraform `f835d63b14931712129771792039f645cf6a3305` and provider R
`5436d3d7c36d3d5174eab3c44e3578830749d3db`.

Root assigns a fresh serialized watcher only this single executable path:

```text
/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/package-c-r-terraform-smoke-3-launch.py
```

The watcher must not execute auth/token/config commands, read credentials or
environment values, or transcribe the launcher's internal argv. It launches
only this executable and monitors its own evidence. Capture complete launcher
stdout/stderr in the aggregate log
`/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/terraform-workflows-r-3.log`.
The safe printed inner argv fixes root/review/terraform-smoke stage; expected
receipt is `/tmp/flake-update-guard-tf3/terraform-smoke/receipt.json`.

The exact native integration invocation remains:

```sh
./test-runner.sh test -f --jobs 1 --stop-on-failure \
  --state-dir /tmp/flake-update-guard-tf3/terraform-smoke/runner-temp/t workflows
```

Keep the singleton workflows selector, all eight ordered shared-state examples,
two machines and native user/socket networking. No cluster/network override,
source/input/pin change, per-example subset or application edit is introduced.
Exact native socket shapes remain 88, 92, 97 and 101 bytes, under the 108-byte
limit. AST/static private-capture/print/exec checks, frozen input hashes and
path-length checks passed in
[the preflight](package-c-r-terraform-smoke-3-preflight.json).

On different safe argv/root, nonzero result, unexpected local kernel build,
missing aggregate evidence or uncertain process effects, stop and report to
the parent. No retry, alternate root, auth diagnosis, credential read, source
edit or cleanup belongs to the watcher. Quiet output is not a timeout. No
integration, deployment, claim or lifecycle action is authorized here.
