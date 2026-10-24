# Provider R verification commands for package C

Prepared only. The source deliverables are fixed for final mechanical pin/history review.
The lead supplies the completed review receipt, publishes provider R first,
then owns serialized runtime launch. No startup, updater, race or VM command
below has run. Historical 7ba and P/Q attempts remain in their original
files and roots; all seven complete real updater patterns must run on R.

Provider R is `5436d3d7c36d3d5174eab3c44e3578830749d3db`, with reference
`github:vpsfreecz/confctl/5436d3d7c36d3d5174eab3c44e3578830749d3db#confctl`.

| C project | Exact final source head | Final series length |
| --- | --- | --- |
| HaveAPI | `baec8e58e11a4868a6c713e70d406709bb94c152` | 1 |
| Terraform provider | `f835d63b14931712129771792039f645cf6a3305` | 1 |
| vpsAdminOS, staging | `d86ea84e653e09bb1d47e21f6b219406c5462906` | 1 |
| Status | `6b5e8a6089926112bfbb63a45413b886ee56e549` | 2 |
| IRC bot | `5b68640fdf0d52bbf5786c886d37d62db595e1a9` | 1 |

[Complete final branch inventory](package-c-r-branches.json) contains full
ranges, paths, old-to-new range-diffs, backups, original publication provenance
and exact remote lease heads. Status preserves its independent baseline hash
fix, including its verified native-check prerequisite, after the consolidated adoption. All original project lock bytes remain
unchanged. There are no migrations or deployment/runtime input changes.

| Prepared artifact | SHA-256 |
| --- | --- |
| [Manifest](package-c-r-verification-manifest.json) | `bbeec793c0c6407023bd4f5eda8d942dbeaeded7cc7e435725d4352575023e8c` |
| [Driver](package-c-r-post-review.py) | `237b5b40646218726a33355ec0a35a706e96330390454621035558291b70f1bf` |
| [Real Git race](package-c-r-git-race.py) | `5c5ff67aba1e412888f5d0db1a005e4bd3535356705fb5502a8d1eee2e585ff1` |

The manifest binds full Git trees, selected Git blobs/content hashes, complete
baseline lock JSON, and extracted original workflow-block hashes. The driver
and race use these final filenames. They leave the original manifests, driver,
review report, attempts and receipts unchanged. The completed affected-review
receipt is bound by its hash when the lead launches the new root; its existence
alone does not establish approval.


The root already retained the exact clean-Git R exported check: all 197 examples
passed, with actual package/caller/hook cases active. This prerequisite released
repinning; the prepared startup and seven final-consumer patterns below remain
unexecuted by implementer0. Status's native-check prerequisite separately passed
its real sandbox package at local predecessor `589f233`; the exact patch is
preserved in the second final commit. Its artifact/input/runtime receipts are in
[the retained verification](package-c-status-native-check-verification.json).
The complete final status updater still reruns on R. No focused package repeat
is required solely for the mechanical CI pin change.

## Prerequisites and exact commands

Use the installed fresh Luna/low verification utility after review under the
monitor skill. The canonical working directory is
`/home/aither/workspace/ai/vpsfree.cz`. Recheck the exact bound session identity
before launch. Only one operation watcher runs at a time, coordinated with
implementer1's two D patterns. Root owns
launch; implementer0 has launched none of these stages.

Supply `GITHUB_TOKEN` through the private environment without printing it.
Set `R_REVIEW_RECEIPT` to the actual completed R review report.
First run startup. Compare GitHub R's source NAR, package, check derivation and
recursive input identities with `verification/local-R-identities.json`. If they
match the successful exact local R check, its 197 examples already cover both
actual-package caller/hook regressions; no duplicate two-probe run is needed.
Any identity mismatch stops the batch and must be reported to the lead.
Do not run from the feature worktrees or change source while review is active.

```sh
set -euo pipefail
: "${GITHUB_TOKEN:?Supply GITHUB_TOKEN through the private environment}"
: "${R_REVIEW_RECEIPT:?Set the completed affected-review report path}"
C_R_ROOT=/tmp/flake-update-guard-2026-10-24-provider-r-1
C_R_DRIVER=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/package-c-r-post-review.py

python3 "$C_R_DRIVER" --root "$C_R_ROOT" --review-receipt "$R_REVIEW_RECEIPT" startup
```

After that identity gate, run the five C patterns, with the two D patterns
also selected by the lead. Each stage has a separate fresh checkout and receipt:

```sh
python3 "$C_R_DRIVER" --root "$C_R_ROOT" --review-receipt "$R_REVIEW_RECEIPT" project haveapi
python3 "$C_R_DRIVER" --root "$C_R_ROOT" --review-receipt "$R_REVIEW_RECEIPT" project terraform-provider-vpsadmin
python3 "$C_R_DRIVER" --root "$C_R_ROOT" --review-receipt "$R_REVIEW_RECEIPT" project vpsadminos
python3 "$C_R_DRIVER" --root "$C_R_ROOT" --review-receipt "$R_REVIEW_RECEIPT" project vpsf-status
python3 "$C_R_DRIVER" --root "$C_R_ROOT" --review-receipt "$R_REVIEW_RECEIPT" project vpsfree-irc-bot
```

Run the real publication-race fixture and the minimal supported Terraform VM
selection in the same serialized verification plan:

```sh
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/package-c-r-git-race.py \
  --root "$C_R_ROOT" --review-receipt "$R_REVIEW_RECEIPT"
python3 "$C_R_DRIVER" --root "$C_R_ROOT" --review-receipt "$R_REVIEW_RECEIPT" terraform-smoke
```

Stop the batch on any nonzero result and return to the parent. A known guard
rejection remains status 3; an evidence/tool failure remains an error. Do not
diagnose, edit, retry, rebase, repin, publish or launch an alternate command in
the watcher. Quiet output is not a deadline. Each stage refuses a reused attempt
directory, retains logs and records PID/process-group ownership. Report and
retain any unfinished operation pending parent direction.

## Retention and evidence

Startup uses `nix build --json --out-link` with an owned link at
`$C_R_ROOT/startup/confctl-package`. It verifies that link resolves to the
recorded package output. Keep this link and its normal Nix root registration;
there is no global root preparation or cleanup. The prior unrooted output's
disappearance has an unknown cause and supplies no explanation for this run.

Startup captures exact provider metadata/archive/source closure, recursive
derivations and realized runtime closure, wrapper bytes/hash, actual bundled
Nix executable/version, and the real package's help entry points. Project
receipts capture baseline/final full source/input graphs, complete lock JSON
and hashes, exact selected scripts, resolved input rows, generated commits,
ordinary hook behavior and final committed-blob validation. Source metadata
and archive paths must agree. Raw command logs have individual SHA-256 hashes.

Each updater uses its final checked-in blocks with only the last external push
removed. Its SSH clone is detached at the exact final source, has external push
disabled, saves the original lock before setup, and uses its declared shell and
hooks. Preserve HaveAPI checks, vpsAdminOS `--all`, status's complete Go/vendor
refresh/test/build sequence, and IRC's exact caller environment and Git hooks.
Status/IRC parent identities must remain unchanged during their leaf update;
confctl supplies the terminal selector. IRC's unchanged auxiliary mutable jq
source is archived with package/closure receipts and must resolve consistently
across the run. No root duplicate diagnosis or token/environment dumps.

The Git race uses a real owned local bare remote and ordinary clones. Its
supported raw GitHub fixture revisions are initial `9d63ab4f...`, stale tip
`cc40679d...` and manual R `5436d3d7...`; full SHAs are constants in the script.
Actual checker/API evidence accepts the old candidate, a concurrent manual
target advance makes the real ordinary push reject, and a fresh clone's manual
baseline rejects the regenerated stale tip with status 3 while equality retains
the manual pin. Lock/index/HEAD/remote preservation is asserted. Pushes target
only the exact owned local bare path. Candidate files are deterministic; the
seven updater patterns exercise real Nix generation separately.

Terraform's exact selected command, inside its separate final-head checkout,
is:

```sh
./test-runner.sh test -f --jobs 1 --stop-on-failure \
  --state-dir "$RUNNER_TEMP/terraform-workflows-state" workflows
```

This is the singleton registered `workflows` test with eight ordered examples
sharing two machines. First require `./test-runner.sh ls workflows` to return
exactly `workflows`. The selected output is
`.#tests.x86_64-linux.workflows`; the complete baseline lock is in the manifest.
Keep native test-framework networking. No development cluster is created and
the pinned runner has no `--network` or per-example selector. A separately
selected development cluster would retain the bridge default.

Stop and escalate an unexpected local Linux kernel build. The driver interrupts
only its exact owned process group and waits for native cleanup; the watcher
must also apply the rule if a build announcement escapes the detector. No
local kernel rebuild or generic timeout is authorized. No machine, merge,
deployment or session lifecycle action is part of this packet.

Static preflight passed: JSON/Python AST, exact source file hashes, extracted
Bash syntax, absence of external publication in updater blocks and preservation
of frozen hashes. Runtime verification remains pending lead launch.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
