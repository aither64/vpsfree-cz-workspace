# Final verification and maintenance integration preparation

Owner: implementer0 after a future explicit checkout transfer. Prepared from the
accepted [design](design.md), repository development/release guides, Makefile,
release build/smoke implementation and selected runtime coordination guide.
Planning only: no source/index/Git mutation, dependency setup, tests, builds,
CI, pushes or publication are authorized by this document.

## Entry gate and handoff

The lead must confirm final committed-deliverable review is complete for final
candidate **C**, with all findings reconciled, quick checks passed and whole
branch history/migration conclusions recorded. Implementer1 then transfers sole
checkout/Git ownership and supplies:

- Full C, version `0.30.2`, clean checkout/index, complete A/B/C history, accepted
  review receipt and package B lineage/raw-normalization evidence.
- Prepared root/server/Ruby-client/Go/Rust bundles, JS/highlighter/PHP/Python
  installations, all nine resolved lockfiles, exact Nix/tools and setup receipts.
  Identify any missing preparation explicitly. Keep current third-party graphs.
- Fixed budget SHA-256, source-reference mapping and final quick checks. The
  original reference remains `b85ec364057f536940d689b09e612512ffffaf82`; mapped
  ancestor remains `8b7abc097db49893da9cc8fa4395648901fec71d`.
- Any existing successful verification for exact C, with commands, locks,
  derivation/input receipts and retained artifacts, so covered work can be reused.

C and the final-review receipt are currently pending; checkout belongs to
implementer1. No machine reservation is needed.

Supplementary prepared-input handoff: `package-bc-prepared-environment.json`
retains exact tools/default-shell receipts. Ruby-client and Go-generator ignored
locks still have own .1 path entries; after review and explicit checkout transfer,
refresh only those local identities before capturing final verification inputs:
(Use the exact-C guard defined below.)

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -euo pipefail -c '
  guard
  (cd clients/ruby && bundle lock --local)
  (cd clients/go && bundle lock --local)
  python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-25-haveapi-backport-release/package-c-verify-inputs.py
  guard
'
```

Require the helper to prove unchanged complete external graphs against the
retained pre-version locks (`package-c-inputs-before`), and preserve its resulting
`package-c-dependency-graph.json`. Server was refreshed by final quick checks and
Rust by `make version`. This step uses cached inputs and edits ignored locks only;
do not perform external re-resolution. It has not been executed by implementer0.

## Common guards and evidence

After that gate, use an explicit full reviewed SHA, never a moving branch name:

```sh
W=/home/aither/workspace/ai/vpsfree.cz
S=2026-10-25-haveapi-backport-release
R="$W/worktrees/$S/haveapi"
C=REPLACE_WITH_FULL_REVIEWED_FINAL_SHA
E="$W/work/$S/postreview-$C-attempt-1"
export W S R C E
cd "$R"
[[ "$C" =~ ^[0-9a-f]{40}$ && "$C" != 0000000000000000000000000000000000000000 ]]
guard() {
  test "$(git rev-parse HEAD)" = "$C"
  test "$(cat VERSION)" = 0.30.2
  test -z "$(git status --porcelain)"
  git diff --quiet 38ecca75edaf797d048fb36c6a50ea7e05eb50a9 "$C" -- \
    servers/ruby/benchmarks/performance_budgets.json
}
guard
export -f guard
# Create only after the lead confirms final review and ownership transfer.
test ! -e "$E"
mkdir "$E"
```

Run with `set -euo pipefail`; source guards are mandatory before and after every
batch, including inside its Nix shell. Recheck exact session identity before
writing records, and run installed workspace commands outside project Ruby/Gem/
Bundler variables (the setup note documents that runtime boundary). Create E
once as a new directory; later batches reuse it but receive unique log/result
paths. Never reuse failed output directories or discard their evidence.

Every long/uncertain batch below gets a **fresh** policy-resolved Luna/low watcher
under dev-session-monitor, explicit full access/approval-never launch policy,
exact command/C/log path and exit receipt. One operation owns its handles; no
parallel parent log polling. The watcher reports command, start/end, exit,
tested C, log/result paths and any running operation. Parent assesses failures
and owns diagnosis/retries. Stop unexpected local kernel builds and investigate.
No repository claim is held during preparation or verification. Keep timing
campaigns exclusive of other local checks/builds to avoid measurement contention.

Reuse prepared dependencies with `HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c
bash -euo pipefail -c '...'`. In each shell re-establish the guard above (or
export it with `export -f guard`). This flag skips installation only; it does
not disable source checks or Git hooks. Do not use the server/Go shell's inherited
`BUNDLE_GEMFILE`/`RUBYOPT` for tree-wide commands.

## Batches, in order

| Batch | Commands in prepared top-level Nix shell | Evidence / acceptance |
| --- | --- | --- |
| Inputs / missing setup | `make release-check`; if final setup is incomplete, one authorized `make release-deps`, then `make release-check` | `inputs.log`, `inputs.result.json`; exact prepared graphs/locks. Never rerun resolution merely for reassurance. |
| Release tests and full suite | `bundle exec rake i18n:health`; `make release-test`; `make test` | `full-suite.log`, `full-suite.result.json`; every command exit 0, all components exercised. `make test` runs `make doc`, JS build, all Ruby/Go/JS/PHP/Python checks, Rust unit/runtime/generated-client protocol checks, documentation assets and supplemental Python checks. |
| One retained release build / smokes | Commands below | `packaging.log`, `packaging.result.json`, original `dist` and manifest; exit 0 and C/.2 identity. |
| Quick paired campaign | Exact manual pair C vs `1c3c98f0d77e0b23c8da1a8937f25c5799864a3b` | `quick/` plus `quick-sources/`, `quick.log`, `quick.result.json`; complete pass. |
| Weekly paired campaign | Exact manual pair C vs original fixed reference | `weekly/` plus `weekly-sources/`, `weekly.log`, `weekly.result.json`; complete pass and approved equivalent-ancestor proof. |

One watcher may own the related release-test/full-suite batch. Packaging and each
timing campaign receive separate fresh watchers. Known quick metadata checks may
stay inline. Preserve a failed command's actual exit; do not let piping through
`tee` or a successful final command hide it. Do not automatically rerun failures.

Capture input receipts before the full suite and compare them after packaging:

```sh
mkdir -p "$E/inputs"
cp flake.lock "$E/inputs/flake.lock"
sha256sum servers/ruby/benchmarks/performance_budgets.json \
  > "$E/inputs/performance-budgets.sha256"
git ls-tree -r --full-tree "$C" > "$E/inputs/source-tree.txt"
git archive --format=tar "$C" > "$E/inputs/source.tar"
git rev-parse origin/master origin/haveapi-0.30 > "$E/inputs/captured-refs.txt"
nix flake metadata --json --no-update-lock-file . > "$E/inputs/flake-metadata.json"
nix flake archive --json --no-update-lock-file . > "$E/inputs/flake-sources.json"
system=$(nix eval --impure --raw --expr builtins.currentSystem)
for shell in default server-ruby client-rust; do
  nix derivation show --recursive ".#devShells.$system.$shell" \
    > "$E/inputs/$shell-derivations.json"
done
ruby -r ./utils/release/artifacts -r fileutils -e '
  HaveAPI::Release::Artifacts::LOCK_PATHS.each do |path|
    destination = File.join(ENV.fetch("E"), "inputs", "locks", path)
    FileUtils.mkdir_p(File.dirname(destination))
    FileUtils.cp(path, destination)
  end'
```

Retain exact tool realpaths/versions for Ruby, gem, Bundler, Node/npm, Go, PHP/
Composer, Python/uv and Rust tools, plus host identity and source/archive/input
hashes. Do not dump ambient environment variables or credentials. Root/server/
Rust recursive derivations plus recursive flake sources bind the measurement
environment; if a separately selected component environment is used, retain its
graph too. Retain actual loaded-gem identities from campaign observations.

The nine locks are root, server, Ruby client, Go generator and Rust generator
Gemfile.lock; Rust runtime Cargo.lock; JS package-lock.json; PHP composer.lock;
Python uv.lock. `dist/release-manifest.json` retains their exact texts and tool
versions; compare them with the captured inputs. An unexpected graph or lock
change requires diagnosis and affected revalidation, not a silent new resolution.

Packaging commands, guarded at exact C:

```sh
test ! -e dist || test -z "$(find dist -mindepth 1 -maxdepth 1 -print -quit)"
make release-check
make release
ruby utils/release/cli.rb smoke-npm dist
ruby utils/release/cli.rb verify dist
(cd clients/python && uv run --locked python utils/package_smoke.py)
sha256sum dist/* > "$E/packaging.sha256"
```

`make release` already builds all maintained packages, writes the manifest and
runs `ruby utils/release/rust_smoke.rb dist`; retain its successful output rather
than repeating that smoke. Run that exact standalone command only if the build
receipt does not cover it or a concrete change invalidates it. The Python smoke
intentionally builds temporary wheel/sdist outputs and a wheel from extracted
sdist, then installs outside the checkout; it is a separate packaging test and
does not replace the original release artifacts. `verify dist` inspects the
retained Python distributions and all package identities/hashes. Do not repeat
`make release` after smoke checks. Existing exact-C artifacts can replace this
build only after manifest, prepared inputs/graph and successful smoke receipts
are independently matched. If `dist` already contains other artifacts, stop and
reconcile their ownership; do not empty it automatically.

## Exact timing commands

For each profile independently, in its fresh watcher, prepare event JSON outside
the timed work (quick values shown; weekly replaces both values as stated):

```sh
profile=quick
baseline=1c3c98f0d77e0b23c8da1a8937f25c5799864a3b
# Weekly: profile=weekly; baseline=b85ec364057f536940d689b09e612512ffffaf82
mkdir "$E/$profile"
python3 - "$C" "$profile" "$baseline" "$E/$profile/event.json" <<'PY'
import json, sys
candidate, profile, baseline, path = sys.argv[1:]
with open(path, "x") as stream:
    json.dump({"repository": {"default_branch": "master"}, "inputs": {
        "candidate_sha": candidate, "baseline_sha": baseline, "profile": profile
    }}, stream, indent=2)
PY
```

In the prepared top-level Nix shell, guard C/.2/cleanliness and run outside
Bundler with the same prepared gems for both sources:

```sh
env -u RUBYOPT -u RUBYLIB -u BUNDLE_BIN_PATH -u BUNDLE_GEMFILE \
  -u BUNDLE_LOCKFILE -u BUNDLE_PATH -u BUNDLE_FROZEN -u BUNDLER_SETUP \
  GEM_PATH="$R/.gems:$R/clients/rust/.gems:$(ruby -e 'puts Gem.default_dir')" \
  ruby utils/performance_ci.rb resolve \
    --event "$E/$profile/event.json" --event-name workflow_dispatch \
    --event-sha "$C" --repository "$R" --output "$E/$profile/selection.json"
env -u RUBYOPT -u RUBYLIB -u BUNDLE_BIN_PATH -u BUNDLE_GEMFILE \
  -u BUNDLE_LOCKFILE -u BUNDLE_PATH -u BUNDLE_FROZEN -u BUNDLER_SETUP \
  GEM_PATH="$R/.gems:$R/clients/rust/.gems:$(ruby -e 'puts Gem.default_dir')" \
  ruby utils/performance_ci.rb run --repository "$R" \
    --selection "$E/$profile/selection.json" \
    --evidence "$E/$profile" --sources "$E/$profile-sources"
```

Require exit 0, `runner.exit` 0, `results/report.json` status `pass`, baseline/C
identities and profile correct, complete workload inventory, unchanged fixed
budget digest, exact original source exports and raw/normalized dependency/body
proofs. Weekly must measure original reference bytes with the approved mapping,
not substitute the mapped ancestor as its baseline. Retain source trees/archive
hashes, all locks/input graphs, raw samples/bodies, report and process logs.
Regression, inconclusive, provenance or output errors block readiness. Local
campaigns do not replace the hosted exact-C Performance gate. Later branch CI
requires separate lead authorization to push; do not launch or monitor it now.

## Temporary maintenance checkout: future unlocked preparation

After B/C, accepted final review and checkout transfer, prepare outside every
repository claim. The lead must serialize canonical-ref/worktree mutations with
the current Git owner. First reread current Git/verification/commits procedures
and `workspace-host coordination guide`; record its selected package/catalog.
Fetch SSH origin and record target T; confirm T is an ancestor of reviewed C.
If T moved beyond the reviewed base, stop for unlocked reconciliation/review
policy rather than preparing a stale merge.

```sh
git --git-dir="$W/repos/haveapi.git" fetch origin
T=$(git --git-dir="$W/repos/haveapi.git" rev-parse refs/remotes/origin/haveapi-0.30)
git --git-dir="$W/repos/haveapi.git" merge-base --is-ancestor "$T" "$C"
TARGET="$W/worktrees/$S/haveapi-maintenance-target"
export T TARGET
test ! -e "$TARGET"
# Run from the prepared source Nix shell so checkout hooks have their toolchain.
git --git-dir="$W/repos/haveapi.git" worktree add --detach "$TARGET" "$T"
```

Inspect actual checkout/ref/registration effects if the checkout hook refuses;
do not recreate a branch or bypass hooks. This is an unregistered detached merge
target, not another feature registration. Read its AGENTS/routed procedures.
Then a fresh watcher may prepare its own root Nix hook environment, retaining a
profile GC root and exact Ruby/gem/tool paths before the claim:

```sh
cd "$TARGET"
nix develop --profile "$E/target-hook-shell" -c bash -euo pipefail -c '
  bundle exec overcommit --install
  bundle exec overcommit --sign
  bundle exec overcommit --list
  git hook run post-checkout -- "$T" "$T" 1
'
test "$(git rev-parse HEAD)" = "$T"
test -z "$(git status --porcelain)"
test "$(git config --get overcommit.configuration.verifysignatures)" = 1
```

Review configuration/custom hook bytes before signing; linked worktrees share
trust/configuration, so coordinate concurrent signing. Prove ordinary hooks
load in the retained Nix environment. Keep this preparation separate from C's
resolved application graph and do not copy native gems from a different Ruby.
Capture final feature comparison after the last C change, before integration:
`dev-session worktree capture-comparison "$S" haveapi --as-is`.

Only the lead's explicit future integration direction permits acquiring one
`haveapi` claim. Its critical section is fresh remote-T/C/cleanliness checks,
ordinary fast-forward merge and required hook-result inspection, non-force SSH
push and remote exact-C proof, then authoritative claim release verification.
Git can return success despite a failing post-merge hook: inspect that outcome
before pushing. Target movement or hook intervention requires stopped commands,
known effects and release before unlocked repair. Never wait for review/tests/
approval/CI under the claim. No merge/push/tag/publication or target creation is
performed by this brief; future execution needs the corresponding lead gates.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-haveapi-backport-release/>
