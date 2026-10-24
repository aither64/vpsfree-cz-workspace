# Prepared post-review configuration and runtime checks

Prepared only. Independent review passed the eight exact ranges in
[review-report.md](review-report.md). No package build, live updater candidate,
node build, deployment or workflow dispatch was started by this preparation.
The lead serializes each authorized operation through a fresh Luna/low watcher.
The parent owns diagnosis and acceptance; no automatic retry.

Use `github:vpsfreecz/confctl/7ba361d22a4aac044cb02abf8397800bcf5726bf#confctl`
for every invocation. Supply `GITHUB_TOKEN` through the watcher's environment
without putting its value in commands or receipts. Preserve ordinary hooks and
the existing old development shell. Do not clear Ruby/Bundler variables in the
actual supported invocation; harness-only stdlib isolation is separate evidence.

## Executable driver and launch requirements

[package-d-post-review.py](package-d-post-review.py) consumes
[package-d-verification-manifest.json](package-d-verification-manifest.json).
The manifest binds both exact reviewed heads/trees, workflow and source Git
blobs/hashes, complete baseline lock graphs, original/transformed shell bodies,
provider source/input graph, runtime probe hash and explicit omitted lines.

| Artifact | SHA-256 |
| --- | --- |
| Driver | `4ebf3d4005650be41610fed02ef58b8a8d311596a1244ce66c616dfaee37a75d` |
| Manifest | `e077eabe3008e195980e7794f07bc3a4343e66869e17029fc62aae25920a1655` |
| Runtime probe | `9b4fb25f65ededc3e5a5aa7e4f5b0c014ee217dc1ce245a081676fc3fae3a752` |

The lead must first accept C's successful exact-provider startup receipt. That
receipt must name provider `7ba361d`, its actual package output, wrapper hash and
bundled Nix path. A shared build receipt proves the artifact, not equivalence
between the old config/IRC shells and a clean hosted workflow environment.

Give a fresh watcher the following setup and only the separately assigned stage
line below. Canonical working directory is `/home/aither/workspace/ai/vpsfree.cz`.
`D_PROVIDER_RECEIPT` must name the actual successful C startup `receipt.json`
(C's prepared root places it under `startup/receipt.json`). Do not substitute an
in-progress or failed receipt. No credential values belong in the command.

```sh
set -euo pipefail
: "${GITHUB_TOKEN:?Provide GITHUB_TOKEN through the private environment}"
: "${D_PROVIDER_RECEIPT:?Set the successful exact-provider startup receipt path}"
D_VERIFICATION_DRIVER=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/package-d-post-review.py
D_VERIFICATION_ROOT=/tmp/flake-update-guard-d-2026-10-24-postreview-1
D_REVIEW_RECEIPT=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/review-report.md
D_MANIFEST_SHA256=e077eabe3008e195980e7794f07bc3a4343e66869e17029fc62aae25920a1655
```

Run each line as its own lead-assigned serialized operation:

```sh
python3 "$D_VERIFICATION_DRIVER" runtime vpsfree-cz-configuration --root "$D_VERIFICATION_ROOT" --review-receipt "$D_REVIEW_RECEIPT" --provider-receipt "$D_PROVIDER_RECEIPT" --manifest-sha256 "$D_MANIFEST_SHA256"
python3 "$D_VERIFICATION_DRIVER" runtime vpsadminos-org-configuration --root "$D_VERIFICATION_ROOT" --review-receipt "$D_REVIEW_RECEIPT" --provider-receipt "$D_PROVIDER_RECEIPT" --manifest-sha256 "$D_MANIFEST_SHA256"
python3 "$D_VERIFICATION_DRIVER" project vpsfree-cz-configuration --root "$D_VERIFICATION_ROOT" --review-receipt "$D_REVIEW_RECEIPT" --provider-receipt "$D_PROVIDER_RECEIPT" --manifest-sha256 "$D_MANIFEST_SHA256"
python3 "$D_VERIFICATION_DRIVER" project vpsadminos-org-configuration --root "$D_VERIFICATION_ROOT" --review-receipt "$D_REVIEW_RECEIPT" --provider-receipt "$D_PROVIDER_RECEIPT" --manifest-sha256 "$D_MANIFEST_SHA256"
```

Each stage uses a fresh exact-head SSH clone in its own directory, disables the
origin push URL, rechecks source hashes and refuses to reuse an existing attempt.
The root marker binds this session, manifest and review receipt. The watcher must
verify the exact session identity, read the monitor skill and applicable routed
procedures, and retain its explicit full-access launch policy. It must not edit,
diagnose, retry, approve, deploy or launch another watcher.

Receipts record command argv/cwd, PID/process group, stdout/stderr hashes,
statuses, elapsed time, source graphs and lock/index/HEAD snapshots. Raw token
values are redacted if emitted; that condition fails the operation. Metadata
receipts never dump the environment. An unexpected local kernel build interrupts
only the owned process group and escalates with status 125; a kernel announcement
seen as a command exits also fails. There is no quiet-build timeout. Return the
raw status, receipt/log paths, bounded failure excerpt and any unfinished owned
process; parent diagnosis determines the next action.

## Actual package in old development shells

Prepare disposable checkouts at the exact reviewed feature heads from
`package-d-branches.json` and C's `package-c-branches.json`. Keep `RUNNER_TEMP` and
`RUNTIME_RECEIPT` outside each checkout. The runtime probe is read-only with
respect to tracked configuration files and never updates or commits inputs.
Invoke it from the selected checkout as follows:

```sh
export RUNTIME_RECEIPT="$RUNNER_TEMP/provider-runtime-vpsfree"
export PROBE_CHANNELS=1
export PROBE_INPUT=nixpkgsStable # vpsFree configuration
nix develop -c bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/provider-runtime-probe.sh
```

Use a distinct receipt directory for each consumer:

| Disposable checkout | PROBE_INPUT | PROBE_CHANNELS | RUNTIME_RECEIPT suffix under RUNNER_TEMP |
| --- | --- | --- | --- |
| vpsFree configuration | `nixpkgsStable` | `1` | `provider-runtime-vpsfree` |
| vpsadminos.org configuration | `nixpkgs` | `1` | `provider-runtime-org` |
| IRC bot | `nixpkgs` | `0` | `provider-runtime-irc` |

`PROBE_INPUT=nixpkgsStable` in vpsFree configuration is confirmed against the
exact reviewed root lock graph. Its `nixpkgs` alias also follows that stable input;
production and staging remain separate root inputs. In vpsadminos.org configuration
set `PROBE_INPUT=nixpkgs` and keep `PROBE_CHANNELS=1`. In IRC set
`PROBE_INPUT=nixpkgs` and `PROBE_CHANNELS=0`. The script requires `PROBE_INPUT`,
exports it to the pinned-tool shell, and asserts exactly one row with that input
name and a full 40-hex-character revision. IRC's declared shell exports
`RUBYOPT=-rbundler/setup` and `BUNDLE_GEMFILE`; the probe must retain them to
exercise the known supported-boundary concern. A failure requires B/C diagnosis
and a lead-approved minimal fix, not broad environment clearing to obtain a pass.

The probe verifies the immutable provider source revision, selects the actual
package executable, records its source and runtime store paths and bundled Nix
version, requires the new forward-only help and full JSON listing, and reads old
configuration channel outputs without moduleOptions. It captures metadata with
the complete source input graph, consumer input hashes, exact consumer head and
before/after tracked status. Metadata is checked in memory against the token
environment values before a receipt is written; no token value or complete
environment is logged. Only Ruby-variable presence booleans are printed.
Shell setup may install ignored development gems.
The old config tools-shell smoke checks already observed RUBYOPT and
BUNDLE_GEMFILE absent, but that is not package execution proof.

## Real configuration workflow patterns without publication

For each reviewed D head, create a clean disposable checkout and disable its
origin push URL before running any workflow commands. Record the exact head and
SHA-256 of `.github/workflows/daily-update.yml`, `flake.nix`, `flake.lock`, Gemfile
and Gemfile.lock. Do not run against the initiative feature worktree.

The driver extracts the following shell blocks from the reviewed workflow blob.
It removes the single explicit final `git push origin master` line and exactly
two hosted-runner GC-root setup lines from `Install git hooks`: its
`sudo mkdir` and `sudo chown` for `/nix/var/nix/gcroots/per-user/$USER`.
The manifest retains each exact omitted line and original/transformed hash.
Preparation read-only verified that `/nix/var/nix/gcroots/per-user/aither` is an
ordinary directory owned by executing UID 1000, writable and searchable, mode
0755 on `aitherdev`. Execution repeats this preflight and fails before any clone
or workflow command if the postcondition no longer holds. It performs no
privileged host mutation, directory recreation or broad sudo substitution.
Every other byte of each shell block is retained. Do not replace dependency,
metadata, commit or llm-agents version-selection code with a second implementation.
Run blocks with GitHub's Bash failure behavior (`bash --noprofile --norc -e -o
pipefail`), with environment `CONFCTL_FLAKE` taken from that exact workflow and
its explicit provider token. Retain the workflow's `Setup git` block and local
author identity so generated commits retain their original messages.

vpsFree configuration, in order:

1. `Save input baseline` (before any Nix/dependency setup).
2. `Setup git` (retains the workflow's local bot identity).
3. `Install git hooks`, with the two verified environment-only omissions above.
4. `Update inputs`.
5. `Update llm-agents when Codex changes`.
6. `Update package dependencies` (retains required RSpec/RuboCop/audit and package
   gem regeneration; these are long checks and run only after review).
7. `Check and push updates`, with only its last push line removed.

vpsadminos.org configuration, in order:

1. `Save input baseline`.
2. `Setup git`.
3. `Install git hooks`, with the two verified environment-only omissions above.
4. `Update flake inputs`.
5. `Check and push updates`, with only its last push line removed.

Hosted checkout is replaced by the exact SSH clone/detached checkout; the
installer/cache actions are omitted because this host already provides Nix and
the actual provider package is separately recorded. The manifest identifies each
action and this environment-only difference. The driver records the host Nix
version; the runtime stages separately identify the actual bundled Nix. This
does not assert equivalence with every GitHub-hosted runner dependency.

The retained final block exports `git show HEAD:flake.lock` to
`$RUNNER_TEMP/flake-update-final.lock`, then invokes the exact-pinned
`inputs check-update` against `$RUNNER_TEMP/flake-update-baseline.lock`.
Thus it validates the lock blob that would be published even if hooks/tests
changed the working tree or index. No push is part of this verification.

Record each command/status, baseline/final hashes, complete semantic path
changes, generated commit messages and actual bundled tool/Nix source evidence.
A known rejection (3) with the guard's rejection marker is recorded as
`policy_rejection` and stops the sequence. The guard preserves the rejected
invocation's baseline; earlier successful local commits can remain. Driver state
snapshots bracket a whole workflow step, which may contain several invocations;
they do not claim a rollback of the entire job. The guard's unknown-evidence
marker records `evidence_error`; setup failures record `fixture_error`, other
workflow failures `workflow_error`, and package startup failures `runtime_error`.
Every nonzero status remains nonzero and needs parent interpretation, including
a legitimate policy stop. No evidence/tool error is a successful skip. Preserve all logs
and any unfinished owned operation; never retry a stale candidate after target
movement. The live channel may legitimately reject the update.

## Seven-pattern combined coverage

These two patterns combine with the five exact prepared ordinary-project
patterns in [package-c-live-checks.md](package-c-live-checks.md). That document
owns HaveAPI/Terraform/IRC helpers and vpsAdminOS/status workflow extraction,
including their existing package/Go checks and resolved nixpkgs leaf evidence.
All seven final checks use the same provider SHA and committed final blob.
The offline D fixture's 20 cases and C fixture's 40 cases are separate evidence;
they do not replace these real package/workflow checks or actual target-movement
Git repository tests selected by the lead.

Preparation checks: Python compile and Bash syntax for all 12 transformed blocks
passed, hashes agree, and exactly the declared omissions remain. See
[package-d-driver-preflight.log](package-d-driver-preflight.log). No `runtime` or
`project` stage was run during preparation.
