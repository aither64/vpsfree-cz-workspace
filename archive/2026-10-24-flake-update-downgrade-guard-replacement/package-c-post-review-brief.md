# Package C verification launch packet

Prepared only. No package build, live updater or VM command in this packet has
been executed. These are the intended review heads; this packet does not assert
that independent review has passed. The lead must bind the completed review
receipt to the manifest below before authorizing its launch.

Use [the driver](package-c-post-review.py) with
[the immutable source manifest](package-c-verification-manifest.json). The
manifest contains exact Git trees, relevant file Git blobs and SHA-256 hashes,
complete baseline lock JSON, original workflow shell-block hashes and the single
removed push line from each workflow.

| Artifact | SHA-256 |
| --- | --- |
| `package-c-verification-manifest.json` | `31d8445a688c8c3b6f44cddaa1eae9fb34a5a658afcf8f45c5f5bfcea02ded9d` |
| `package-c-post-review.py` | `158cfaed2c0bd75462efdf2ca9921bc3b4236017f8d4f86d61723ae6ce9c99cb` |

The CI package is
`github:vpsfreecz/confctl/7ba361d22a4aac044cb02abf8397800bcf5726bf#confctl`.
Its baseline lock SHA-256 is
`17af06ae76afeba640d695a8e974d76be742e795977d026771c178c523a4eaba`.

| Project | Exact source head | Baseline `flake.lock` SHA-256 |
| --- | --- | --- |
| HaveAPI | `d4dc3c7c6b15d3bdad51ce18f6959136dc68b23e` | `a52bdf3a3b9a069175d3af298234c3cf7adeba54540833eed6ad902e9ccc0a64` |
| Terraform provider | `171e32d8bf6706748651ba33df6abb05849244fa` | `a1643702334dcbb1993ca064359182e7705b54024e31fb7445082acc105b7b8a` |
| vpsAdminOS | `0552cfeecf127671e21dcb72db78b7188d342107` | `cc3cdd6cc5f5d911b0f17ba89db0b8d2384f3a71eb6baa9612036a0f351e428c` |
| Status | `7641e48787281d29cdd0df95f7ee06555c73fac6` | `70ee266d388a3b0eaa8786a54dd83ce39e392addb2fcb4742b4a2a4e2c9a3c33` |
| IRC bot | `a2ab57b8169ad978f6f8542dd19cf5199517b0cb` | `006122d3d852e2da6eb985f610278ac3680849dda25e59d16fb1dd58318efcfb` |

## Launch after review

Coordinate with implementer1 and the lead before launching: C and B/D use one
fresh Luna/low operation watcher at a time. The startup result may be shared
when the exact provider package, derivation/input graph, runtime closure and
environment match. Do not repeat B's runtime diagnosis. No watcher was launched
for this preparation.

The watcher must read the monitor skill and applicable workspace/repository
guidance, verify `dev-session current` and the exact bound environment, then own
the following related batch. Use the installed verification utility policy with
full access explicitly. The canonical working directory is
`/home/aither/workspace/ai/vpsfree.cz`. Supply `GITHUB_TOKEN` privately through
the environment; do not print environment contents or enable shell tracing.
Set `C_REVIEW_RECEIPT` to the actual completed-review receipt path. A file's
existence alone does not establish review approval; the lead checks its scope.

```sh
set -euo pipefail
: "${GITHUB_TOKEN:?Provide GITHUB_TOKEN through the private environment}"
: "${C_REVIEW_RECEIPT:?Set the completed independent-review receipt path}"
C_VERIFICATION_ROOT=/tmp/flake-update-guard-2026-10-24-C-postreview-1
C_VERIFICATION_DRIVER=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/package-c-post-review.py

python3 "$C_VERIFICATION_DRIVER" --root "$C_VERIFICATION_ROOT" --review-receipt "$C_REVIEW_RECEIPT" startup
python3 "$C_VERIFICATION_DRIVER" --root "$C_VERIFICATION_ROOT" --review-receipt "$C_REVIEW_RECEIPT" project haveapi
python3 "$C_VERIFICATION_DRIVER" --root "$C_VERIFICATION_ROOT" --review-receipt "$C_REVIEW_RECEIPT" project terraform-provider-vpsadmin
python3 "$C_VERIFICATION_DRIVER" --root "$C_VERIFICATION_ROOT" --review-receipt "$C_REVIEW_RECEIPT" project vpsadminos
python3 "$C_VERIFICATION_DRIVER" --root "$C_VERIFICATION_ROOT" --review-receipt "$C_REVIEW_RECEIPT" project vpsf-status
python3 "$C_VERIFICATION_DRIVER" --root "$C_VERIFICATION_ROOT" --review-receipt "$C_REVIEW_RECEIPT" project vpsfree-irc-bot
python3 "$C_VERIFICATION_DRIVER" --root "$C_VERIFICATION_ROOT" --review-receipt "$C_REVIEW_RECEIPT" terraform-smoke
```

Each stage refuses an existing attempt directory. A failure returns to the
parent for interpretation; the watcher does not repair, retry, switch revisions
or change commands. The driver never pushes, dispatches workflows, merges,
deploys, uses a development cluster or performs session lifecycle actions. It
uses fresh SSH clones detached at the selected heads and disables their origin
push URL. Evidence and disposable checkouts remain at the named root.

## Environment and receipt scope

Startup builds the actual immutable package, captures recursive derivations and
runtime closure, saves its wrapper, locates the wrapper's bundled Nix executable
and runs that executable's `--version`. It invokes the real package's root,
update, list and final-check help entry points. It does not infer runtime Nix
from the ambient install-nix action.

Each project saves its original lock outside the checkout before setup. It
installs ordinary required hooks in the declared Nix shell and verifies that
setup did not change the pinned source files. It runs the exact extracted
workflow shell blocks separately, removing only the final push. All blocks run
through `nix develop -c bash` so local required hooks have their declared tools;
this is a local environment compatibility test as well as workflow logic
validation, not an assertion that GitHub's ambient environment is identical.
Ruby/Bundler variables are preserved. IRC's inherited `RUBYOPT` and
`BUNDLE_GEMFILE` boundary remains implementer1's diagnosis responsibility.

The driver preserves HaveAPI's `nix flake check`, vpsAdminOS's `--all`, status's
Go dependency/vendor refresh, tests and package build, helper commit formats,
and final committed-blob checks. Shared `inputs ls --json` receipts capture all
root identities before/after; status/IRC parent identities must remain equal.
Their leaf selector is `vpsadmin/vpsadminos/nixpkgs`, supplied by confctl rather
than a consumer graph parser. IRC's existing auxiliary mutable jq flake is
resolved and archived, with its derivation/runtime closure recorded; a changed
resolution across the operation makes verification fail.

For provider, each project's original/final sources, and the Terraform smoke,
capture `nix flake metadata --json --no-write-lock-file` plus
`nix flake archive --json --no-write-lock-file`. Require the two source store
paths to agree. Record recursive `nix path-info --json` for every archived
source path, retaining full transitive input graphs and store/NAR identities.
Record recursive derivation graphs and realized output closures for the CI
package, baseline/final dev shells, auxiliary jq, status package and selected
Terraform VM configuration. This captures Nix source/input closures; it does
not assert that unrelated host tools or GitHub runner state are identical.

Every command has argv, cwd, PID/process-group identity, complete stdout/stderr
paths and SHA-256, exit status and elapsed time in its stage receipt. The receipt
also binds manifest, driver and review receipt hashes, full lock JSON and hashes,
generated Git heads/subjects, original index hash, and final status. Nonzero
guard statuses remain nonzero: rejection 3 is a stopped policy result, while
error 1 requires diagnosis. Neither permits publication or an automatic retry.

## Minimal Terraform VM check

Local `AGENTS.md` requires `make test-integration` or a focused runner for
provider workflow changes. `Makefile` maps the former to the whole `ci` tag.
`tests/all-tests.nix` registers only `workflows`; its suite has eight ordered
examples sharing state on two machines. The locked runner source at
`vpsadminos/8e44a5124439b1f3048ffc56b1717614a5360358` supports test-path selection,
one job, fail-fast and an owned state directory, but no example filter or
`--network` option. The driver first requires `./test-runner.sh ls workflows`
to return exactly `workflows`, then runs:

```sh
./test-runner.sh test -f --jobs 1 --stop-on-failure \
  --state-dir "$RUNNER_TEMP/terraform-workflows-state" workflows
```

Run this only in the driver's separate Terraform clone at the reviewed head and
baseline lock above. The selected flake output is
`.#tests.x86_64-linux.workflows`. The baseline also resolves vpsAdmin to
`fb2f51222503a45f2e5a42af505f719e44279ed0` and nixpkgs to
`a9e6d84f9c2f9012f5fe7d964a7851352300e61a`.

Keep native framework networking unchanged; this command creates no development
cluster, so no bridge/local cluster override applies. If separate authorized
cluster verification is later selected, bridge remains the default. Do not add
an unsupported `--network bridge` flag or prune stateful examples to invent a
smaller smoke test.

## Watcher stop and report rules

Stop and escalate any unexpected local Linux kernel build. The driver watches
Nix build announcements and sends SIGINT only to its exact owned process group,
then awaits native cleanup. The watcher must also observe this rule if output
does not match the driver's detector. No local kernel rebuild is authorized.
No generic quiet-build deadline is imposed. Do not leave a running command,
guest or Nix operation without an owner; report any unfinished identity and
retain ownership pending parent direction. No parallel parent log polling or
duplicate root diagnosis is needed.

Return passed/failed/incomplete with exact source/provider heads, command/stage,
exit status, elapsed time, receipt/log paths, a bounded failure excerpt and any
unfinished process or authorized kernel interruption. Preserve receipts and
normal runner recovery evidence. The parent interprets results and selects any
subsequent action.

Preparation checks passed: Python AST parsing, JSON parsing, `bash -n` for all
extracted shell bodies, and absence of publication commands. These are static
checks only; runtime/build/VM validation remains pending review and launch.

## Actual Git target movement fixture

The 40 offline workflow scenarios mock Git commit/push and do not prove a real
publication race. [package-c-git-race.py](package-c-git-race.py) supplies this
separate bounded check. Its SHA-256 is
`552f7e00a3833f45c7e517297ea26420e26e6aecd805b94cf6f2f965661e8313`.
It uses the stable driver for exact command/receipt handling and the same
review-bound root. Launch only through the lead's serialized watcher:

```sh
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/package-c-git-race.py \
  --root /tmp/flake-update-guard-2026-10-24-C-postreview-1 \
  --review-receipt /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/review-report.md
```

The fixture uses an owned local bare remote and four ordinary clones. Pushes
go only to that exact absolute local fixture path; no external ref is written.
The synthetic lock contains one supported raw GitHub source for confctl, using
real immutable public revisions: initial `9d63ab4f30929043b8695225c0128029b188a985`,
old channel tip `cc40679d267165aecfa569128438bb55fe910268`, and manual pin
`7ba361d22a4aac044cb02abf8397800bcf5726bf`. It records a local source ancestry
witness, then calls the actual pinned `check-update` package with live GitHub
evidence before and after the stale candidate's commit. A concurrent writer
advances the real local target to the manual pin. The stale ordinary push must
return 1 with a rejection, preserving the target. A fresh clone must start from
the manual target; the checker must reject the regenerated old tip with status
3, accept equality, and leave the fresh lock, index, HEAD and remote unchanged.

Git operations and guard evidence are real. Candidate generation uses explicit
deterministic fixture lock files, so it does not claim to test Nix generation;
the five live updater patterns cover that separately. New empty fixture
repositories declare no hook framework. This script needs private
`GITHUB_TOKEN`, has no retries, and retains all logs, lock hashes and target
heads. Only AST parsing has run; the fixture itself remains unexecuted.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
