# Follow-up post-review verification command plan

Prepared from the current `haveapi-followups` Makefile, release build/CLI and
Rust integration runner on 2026-10-22. **Not executed.** Lead launches a fresh
policy verification utility only after the entire six-part series is committed,
quick checks pass and independent final review accepts the exact head. No new
package version, tag, release, publication-confirmation probe or default integration belongs
to this plan. Normal dependency downloads and local fixture servers are part of
the later authorized verification; architect performed neither.

## Frozen inputs and preconditions

- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-followups`.
  Branch: `2026-10-22-haveapi-release-followups`; base:
  `b64fb25bea8d8222fb3263b99956c0b61438a859`.
- Lead supplies the full independently reviewed final commit as
  `HAVEAPI_FOLLOWUP_HEAD`; do not infer it from whatever HEAD happens to be at
  launch. Before shell entry and again before packaging, require exact HEAD,
  clean index/tracked worktree and no uncommitted source. All eight generated JS
  outputs must be committed. Preserve the known untracked caches
  `clients/rust/.bundle-user/` and `utils/release/__pycache__/`; inventory their
  exact paths in the receipt and refuse unexpected untracked paths. Do not
  delete caches, change global ignores or treat all untracked files as harmless.
  Freeze writers until the batch ends.
- Use the final source's top-level Nix shell, without updating flake.lock.
  Current lock still selects nixpkgs
  `02c087f3fe673c9e317f206a627cb6b910336dbe`, NAR
  `sha256-IoNisKcGbUjdd45qCqywGMCYmZ5EnkxezvLII0FWwNA=`. Final flake.nix includes
  the reviewed libffi inputs. Record final source/lock hashes and resolved tools;
  do not reuse the pre-libffi shell derivation as the final environment receipt.
- The standard top-level shell hook prepares the root Ruby bundle. Do not enter
  component shells again just to repeat their install hooks. `make release-deps`
  prepares maintained components, using the frozen Rust bundle, npm lock and uv
  lock. Other existing Ruby/Composer resolution behavior is unchanged; retain
  resolved locks in the release manifest/evidence rather than claim all package
  downloads were fixed by flake.lock alone.
- Unset inherited compiler/bundler overrides before launch; preserve ordinary
  proxy compatibility and do not dump the environment. Do not supply publication
  credentials. No source or lock repair is allowed during this verification.
- Top-level `dist` must be absent or empty. If it contains prior **follow-up**
  candidates, lead/owner preserves them under a distinct receipt path before
  launch; never remove/overwrite the original official-release directory or any
  accepted artifacts. The utility should refuse a nonempty dist, not improvise
  cleanup. Use a fresh session receipt directory and retain the new dist intact.
  These unchanged-version development artifacts are not replacements for the
  published 0.30.0 bytes and must never be uploaded.

## Exact tool selection

The unchanged nixpkgs Rust selection was previously identified as Cargo/rustc
1.99.0. Reconfirm paths and verbose identities inside the final top-level shell;
stop if selection differs, rather than silently substituting a compiler:

```text
development cargo /nix/store/1jwkiz96iwqdhm4bh2hvgd86ysb0b67q-cargo-1.99.0/bin/cargo
development rustc /nix/store/6l9kbzxwq9ij2lcmwl2qb1jdpqisjr8l-rustc-wrapper-1.99.0/bin/rustc
formatter          /nix/store/zfrqd9ahnccql0zgzgc5swwi4zmm14zl-rustfmt-1.99.0/bin/rustfmt
MSRV cargo         /nix/store/rai05nypxnmj22l65nwsk5xjsaq8s4vc-cargo-1.95.0/bin/cargo
MSRV rustc         /nix/store/m4hrdkg9ypcw8y1banfc26q3f27kfqvb-rustc-wrapper-1.95.0/bin/rustc
```

[MSRV readiness](api-doc-msrv-readiness.md) records exact commits, derivation
roots, source hashes and input graph for the independently selected 1.95 pair.
Use those installed non-bootstrap paths; do not install rustup or change Nix
inputs. Record executable availability/versions at launch. Generation retains
the development formatter; only compilation selects the independent MSRV pair.

## One cumulative batch

Launch from the worktree root through the fresh utility, not from an agent tool
call during planning. Lead supplies `HAVEAPI_FOLLOWUP_HEAD` and a fresh
`HAVEAPI_FOLLOWUP_EVIDENCE` absolute session directory, both passed unchanged.
Capture stdout/stderr and exit status without shell tracing or environment dumps.
Lead also supplies `HAVEAPI_FOLLOWUP_CACHE_INVENTORY`, a JSON array of exact
repository-relative untracked cache paths retained at final preflight. Capture
it after final commits, before shell entry, with `git ls-files --others
--exclude-standard -z`; every entry must be strictly beneath one of the two
known cache directories. Save names only, not cache/config contents. Any other
untracked path needs owner reconciliation before launch. Existing repository
ignore rules continue to cover normal build products; no ignore rules change.
Recheck this frozen allowlist at each source guard. A new untracked cache entry
also requires reconciliation of the inventory, not automatic deletion or a
silently broadened exception. This keeps the exact initial cache evidence.
Read-only planning inventory on 2026-10-23 found 301 paths under `.bundle-user`
and one Python bytecode path. SHA-256 of sorted NUL-separated relative paths,
with a trailing NUL, was
`db331c45e380f9cbb47a8a507b0c65b5e6e810a956e8992470447bbdbc56ac43`.
This names-only observation is not the final preflight inventory: commits are
still owner0's responsibility, and the final utility must bind its own receipt.
The launch command removes only known interfering build overrides:

```sh
env -u RUBYOPT -u BUNDLE_BIN_PATH -u BUNDLE_LOCKFILE -u BUNDLE_PATH \
  -u BUNDLER_SETUP -u BUNDLE_GEMFILE -u GEM_HOME -u GEM_PATH \
  -u RUSTC -u RUSTC_WRAPPER -u RUSTC_WORKSPACE_WRAPPER \
  -u RUSTFLAGS -u CARGO_ENCODED_RUSTFLAGS \
  -u HAVEAPI_RUST_NAME_LINT -u HAVEAPI_RELEASE_TOOLS_ONLY \
  nix develop --no-write-lock-file -c bash -euo pipefail -s
```

Supply this command body on stdin after the preconditions/tool identity receipt:

```sh
: "${HAVEAPI_FOLLOWUP_HEAD:?reviewed full head required}"
: "${HAVEAPI_FOLLOWUP_EVIDENCE:?fresh session receipt directory required}"
: "${HAVEAPI_FOLLOWUP_CACHE_INVENTORY:?exact known-cache path inventory required}"
assert_source_clean() {
  test "$(git rev-parse HEAD)" = "$HAVEAPI_FOLLOWUP_HEAD"
  git diff --quiet --exit-code
  git diff --cached --quiet --exit-code
  python3 - <<'PY'
import json, os, subprocess
from pathlib import PurePosixPath
with open(os.environ['HAVEAPI_FOLLOWUP_CACHE_INVENTORY']) as stream:
    known = json.load(stream)
roots = ('clients/rust/.bundle-user/', 'utils/release/__pycache__/')
assert isinstance(known, list) and len(known) == len(set(known))
assert all(isinstance(p, str) and p.startswith(roots)
           and '..' not in PurePosixPath(p).parts for p in known)
raw = subprocess.check_output(['git', 'ls-files', '--others',
                               '--exclude-standard', '-z'])
actual = {os.fsdecode(p) for p in raw.split(b'\0') if p}
unexpected = actual - set(known)
if unexpected:
    raise SystemExit('Unexpected untracked paths: ' + repr(sorted(unexpected)))
print('Known untracked cache paths retained:', len(actual))
PY
}
assert_source_clean
test ! -e "$HAVEAPI_FOLLOWUP_EVIDENCE/dist"
if test -d dist; then
  test -z "$(find dist -mindepth 1 -maxdepth 1 -print -quit)"
else
  test ! -e dist
fi

make release-deps
(cd clients/js && ./node_modules/.bin/gulp doc)

# Setup/doc generation must not change committed source or generated dist.
assert_source_clean
make release
make test
ruby utils/release/cli.rb smoke-npm dist
(cd clients/python && uv run --locked python utils/package_smoke.py)

env -u RUBYOPT -u BUNDLE_BIN_PATH -u BUNDLE_LOCKFILE -u BUNDLE_PATH \
  -u BUNDLER_SETUP \
  GEM_HOME="$PWD/clients/rust/.gems" \
  GEM_PATH="$PWD/clients/rust/.gems:$(ruby -e 'puts Gem.default_dir')" \
  BUNDLE_GEMFILE="$PWD/clients/rust/Gemfile" \
  HAVEAPI_RUST_INTEGRATION=1 HAVEAPI_RUST_NAME_LINT=1 \
  HAVEAPI_RUST_MSRV_CARGO=/nix/store/rai05nypxnmj22l65nwsk5xjsaq8s4vc-cargo-1.95.0/bin/cargo \
  HAVEAPI_RUST_MSRV_RUSTC=/nix/store/m4hrdkg9ypcw8y1banfc26q3f27kfqvb-rustc-wrapper-1.95.0/bin/rustc \
  ruby clients/rust/spec/integration/run.rb

ruby utils/release/cli.rb verify dist
assert_source_clean
cp -a dist "$HAVEAPI_FOLLOWUP_EVIDENCE/dist"
```

The evidence parent must already exist and be owned by this session; the dist
destination must be new. Keep worktree dist as well. On failure, preserve
partial artifacts/logs and stop; no automatic rebuild, source repair, rerun,
publication or cleanup. A subsequent attempt uses a distinct receipt.

## Coverage without repeated campaigns

- `gulp doc` exercises the actual maintained documentation task and alias
  postprocessing. Its content/navigation tests also run within `make test`'s
  compatibility suite; one explicit task invocation verifies the task wiring.
- `make release` performs clean-source validation, shared docs, all maintained
  package builds, artifact inspection/manifest and **the retained Rust gem smoke**
  including Fiddle activation. Do not invoke rust_smoke.rb again in this batch.
- `make test` already includes all Ruby/Go/JS/PHP/Python core/integration suites,
  JS loader/helper/graph/type fixtures, Rust generator units, runtime default and
  blocking features, ordinary generated-client protocol acceptance at root and
  mounted paths, plus server documentation assets/Python checks. Do not append
  separate full JS, test-rust or test-documentation campaigns.
- `smoke-npm dist` adds isolated retained-tarball consumption/strict declarations.
  Python package_smoke adds standalone wheel/sdist installation coverage absent
  from `make test`; it builds temporary Python packages itself. It is **not** an
  exact-retained-wheel install test. `verify dist` binds retained artifact bytes
  to their manifest; this distinction must remain in the receipt.
- NAME_LINT is a separate necessary mode: it compiles the generated fixture
  library with all transport features and `-D non_snake_case` under development
  and explicit Rust1.95, at both mounts. Ordinary `make test` runs protocol tests
  instead. Do not set NAME_LINT globally or accidentally replace protocol tests.
- No live registry-confirmation experiments: the pre-review fake transport/clock
  suite is the proof for HTTP/status/backoff/conflict paths. Do not rerun unchanged
  release unit tests solely because this long batch began; reuse exact-head quick
  receipts, with rechecks only if source/inputs or failures justify them.

Retain whole logs, per-step exit results, exact source and tool identities,
manifest/checksums/locks and a concise named-warning summary. The current Rust
integration runner deletes its temporary generated crate on exit and has no
receipt-output option: logs establish the named-lint pass, but do **not** retain
its generated Cargo.lock/schema/tree. Do not claim a saved generated-input graph
that the runner did not write. Lead must decide whether a small pre-review
evidence-retention change is required for that stronger claim; this plan neither
implements one nor substitutes an unreviewed instrumentation wrapper.

The complete new six-commit series and final generated outputs remain the review
unit. Successful local verification means development-branch readiness only,
never integration or another publication authorization.

Downstream crate preparation may start after the fixed generator is committed,
reviewed and verified: pin that exact generator source/package, regenerate the
downstream SDK, inspect its diff and run its own review/verification. A new
HaveAPI registry release is not a prerequisite. This sequencing grants no
downstream edits or crate publication; lead owns those separate assignments and
publication still requires fresh authorization.
