# Final-P verification commands for package C

Prepared only. The source deliverables are fixed for affected final review.
The lead supplies the completed review receipt, publishes provider P first,
then owns serialized runtime launch. No startup, updater, race or VM command
below has run. Historical 7ba passes and failures remain in their original
files and root; all seven complete real updater patterns must run on P.

Provider P is `bdaed19e901237e05bd0a779f368e76cb311143f`, with reference
`github:vpsfreecz/confctl/bdaed19e901237e05bd0a779f368e76cb311143f#confctl`.

| C project | Exact final source head | Final series length |
| --- | --- | --- |
| HaveAPI | `aebbc9930c39a4df6fad01fefed8254921635b15` | 1 |
| Terraform provider | `58a3d083381ccadf4075e8eeffe2c169741be691` | 1 |
| vpsAdminOS, staging | `afc2eb385096e361b883ff66afe0bc7eb74eb698` | 1 |
| Status | `c8869b8f274dd840539a94da30d19d355cd623c1` | 2 |
| IRC bot | `fb5d72fb44176ebee217370f761762afd275ab54` | 1 |

[Complete final branch inventory](package-c-final-branches.json) contains full
ranges, paths, old-to-new range-diffs, backups, original publication provenance
and exact remote lease heads. Status preserves its independent baseline hash
fix after the consolidated adoption. All original project lock bytes remain
unchanged. There are no migrations or deployment/runtime input changes.

| Prepared artifact | SHA-256 |
| --- | --- |
| [Manifest](package-c-final-verification-manifest.json) | `e5c1c7392a65cc2d6a644321aeac9e46c636c9ca7d52eb917d8d030764df4b2e` |
| [Driver](package-c-final-post-review.py) | `4fb3e7b09ea3dbbbae1f011504e53795b0c2d17bced0dbb2400c1a9ba8b2cdb8` |
| [Real Git race](package-c-final-git-race.py) | `7f92f94cbce48bdd2f21ff283592ff73cf4d17157f69b339a1db805118ac2b99` |

The manifest binds full Git trees, selected Git blobs/content hashes, complete
baseline lock JSON, and extracted original workflow-block hashes. The driver
and race use these final filenames. They leave the original manifests, driver,
review report, attempts and receipts unchanged. The completed affected-review
receipt is bound by its hash when the lead launches the new root; its existence
alone does not establish approval.

## Prerequisites and exact commands

Use the installed fresh Luna/low verification utility after review under the
monitor skill. The canonical working directory is
`/home/aither/workspace/ai/vpsfree.cz`. Recheck the exact bound session identity
before launch. Only one operation watcher runs at a time, coordinated with
implementer1's two D patterns and final-package caller/hook probes. Root owns
launch; implementer0 has launched none of these stages.

Supply `GITHUB_TOKEN` through the private environment without printing it.
Set `FINAL_REVIEW_RECEIPT` to the actual completed affected-review report.
First run startup. Run B's two real final-package caller/hook regressions before
the live patterns; B owns their exact commands and receipts. Candidate-package
probe results are historical prerequisites and do not replace final-P evidence.
Do not run from the feature worktrees or change source while review is active.

```sh
set -euo pipefail
: "${GITHUB_TOKEN:?Supply GITHUB_TOKEN through the private environment}"
: "${FINAL_REVIEW_RECEIPT:?Set the completed affected-review report path}"
C_FINAL_ROOT=/tmp/flake-update-guard-2026-10-24-final-provider-1
C_FINAL_DRIVER=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/package-c-final-post-review.py

python3 "$C_FINAL_DRIVER" --root "$C_FINAL_ROOT" --review-receipt "$FINAL_REVIEW_RECEIPT" startup
```

After the final-package probes, run the five C patterns, with the two D patterns
also selected by the lead. Each stage has a separate fresh checkout and receipt:

```sh
python3 "$C_FINAL_DRIVER" --root "$C_FINAL_ROOT" --review-receipt "$FINAL_REVIEW_RECEIPT" project haveapi
python3 "$C_FINAL_DRIVER" --root "$C_FINAL_ROOT" --review-receipt "$FINAL_REVIEW_RECEIPT" project terraform-provider-vpsadmin
python3 "$C_FINAL_DRIVER" --root "$C_FINAL_ROOT" --review-receipt "$FINAL_REVIEW_RECEIPT" project vpsadminos
python3 "$C_FINAL_DRIVER" --root "$C_FINAL_ROOT" --review-receipt "$FINAL_REVIEW_RECEIPT" project vpsf-status
python3 "$C_FINAL_DRIVER" --root "$C_FINAL_ROOT" --review-receipt "$FINAL_REVIEW_RECEIPT" project vpsfree-irc-bot
```

Run the real publication-race fixture and the minimal supported Terraform VM
selection in the same serialized verification plan:

```sh
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/package-c-final-git-race.py \
  --root "$C_FINAL_ROOT" --review-receipt "$FINAL_REVIEW_RECEIPT"
python3 "$C_FINAL_DRIVER" --root "$C_FINAL_ROOT" --review-receipt "$FINAL_REVIEW_RECEIPT" terraform-smoke
```

Stop the batch on any nonzero result and return to the parent. A known guard
rejection remains status 3; an evidence/tool failure remains an error. Do not
diagnose, edit, retry, rebase, repin, publish or launch an alternate command in
the watcher. Quiet output is not a deadline. Each stage refuses a reused attempt
directory, retains logs and records PID/process-group ownership. Report and
retain any unfinished operation pending parent direction.

## Retention and evidence

Startup uses `nix build --json --out-link` with an owned link at
`$C_FINAL_ROOT/startup/confctl-package`. It verifies that link resolves to the
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
`cc40679d...` and manual P `bdaed19e...`; full SHAs are constants in the script.
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
