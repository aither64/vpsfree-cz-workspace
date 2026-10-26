# Package D: benchmark and contributor documentation

Package D is committed at `b85ec364057f536940d689b09e612512ffffaf82`.
Implementation, focused checks and the accepted campaign are complete; the lead
reported final review and full verification passed at this unchanged head. See
[the campaign report](package-d-campaign-report.md) for accepted measurements and
[the cleanup receipt](package-d-baseline-cleanup.json) for retained test-temp data.
No deployment, integration,
publication or session cleanup was performed. The Git window is relinquished;
the worktree and index were clean after the commit.

## Deliverable

Only the five assigned application paths changed:

- `servers/ruby/benchmarks/documentation.rb`
- `Makefile`
- `doc/client-examples.md`
- `doc/agent-instructions/development.md`
- `clients/rust/docs/documentation.md`

`make benchmark-documentation` synchronizes documentation and emits JSON.
The default lanes are `context_profile`, `context_sample` and `html`.
`--rust` enables a matching optional profile and adds `rust_async_example`,
`rust_async_auth`, `rust_blocking_example` and `rust_blocking_auth`.
Every lane reports each trial, its output identity and a component-wise median
of wall seconds, process CPU seconds and allocated objects. Setup and validation
are outside lane measurements. The report includes runtime, source and input
identity. Invalid options, missing dependencies and invalid output exit nonzero
with a failed JSON report.

Final options: `--shape resources|actions|both|custom`, `--size`, `--resources`,
`--actions`, `--samples`, `--parameters`, `--warmup`, `--trials`, `--iterations`,
`--lanes context,html,rust`, `--rust`, `--user admin|member`, `--source-root`,
`--source-revision`, `--help`. Defaults are both shapes, size 8, one public sample,
two additional string parameters, one warmup, three trials and 100 iterations.
The HTML lane always performs one request per trial. Only the custom shape uses
`--resources` and `--actions`. Fixture dimensions exclude its extra privileged
sample per ordinary action and one admin-only action on resource0.

The contributor guide documents ownership precisely: unchanged fields are shared
by base Context derivations; explicitly supplied containers still need copying;
profiles and arbitrary leaves retain reference semantics; subclasses retain
constructor behavior. The Rust guide explains authorized subtree selection and
remaining ancestor/IR lookup costs. No production latency or universal future
regression guarantee is claimed. No CI workflow or timing gate was added.

## Focused evidence

- Ruby syntax and changed-file RuboCop passed. `git diff --check` passed.
- All local Markdown targets/anchors in the three edited guides resolve.
- CLI help and invalid size, warmup, lane and positional arguments were checked.
  Invalid cases produced failed JSON and exit 1.
- [Dynamic smoke](package-d-smoke.json): both shapes, size 1, no warmup,
  two trials and three iterations. HTML 200, 59,886 bytes, stable body SHA-256.
- [Restricted/custom smoke](package-d-member.json): member, 2x2 ordinary
  resources/actions, one warmup/trial and two iterations. HTML 200, 87,903 bytes.
- [Rust smoke](package-d-rust.json): size 1, one warmup, two trials and two
  iterations. HTML 200, 70,621 bytes; both Rust variants present, four adapter
  lanes return nonempty code with stable body digests.
- [Final smoke](package-d-final-smoke.json): both shapes, size 2, one warmup,
  two trials and two iterations, with Rust. All seven lanes passed. HTML sizes
  are 105,390 bytes for resources and 105,108 bytes for concentrated actions.
- [Baseline source-selection smoke](package-d-source-selection-unbundled.json):
  exact baseline export, size 1, no warmup, one trial and one iteration, with
  Rust. Context and Rust source-location checks confirmed baseline loading.
  All seven lane statuses, byte counts and body digests equal the size-1
  candidate smoke. Baseline description sharing is false; candidate is true.
  This is output/source-selection evidence, not a timing-improvement campaign.
- A server-bundle `--rust` invocation was checked to fail explicitly with
  `LoadError: cannot load such file -- tomlrb`, JSON status `failed`, exit 1.
  Use the combined prepared environment below for optional Rust.

Normal commit hooks passed: HaveapiI18n, RuboCop, SingleLineSubject,
TrailingPeriod and TextWidth. The first commit message produced width warnings;
a message-only amend within the granted D window removed them. Final hooks have
no warnings. No hooks or dependency checks were bypassed.

Smokes used the prepared top-level shell with
`HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -lc ...`; the inspected
flake shellHook uses that flag only to skip dependency installation. No
dependency installation, shared bundle changes or long suites were run by D.

The retained final smoke's harness, fixture and lock hashes match the committed
files and currently prepared locks. Its Git HEAD predates the D commit, because
the smoke ran before committing. No post-commit timing result is claimed.

## Exact baseline export and inputs

The lead-approved disposable source export is
`/tmp/haveapi-context-copy-baseline-39909094649b`. Its path was absent before
creation. `git archive --format=tar 39909094649b1d14a23f00615775ca7136acf4fd`
exported 772 files without changing repository refs, index or worktree. The
archive SHA-256 is
`c61f0e459fc14db61194ed6134a0e3da89f5d53c3b59c0aad11a5685785107d2`.
[The export receipt](package-d-baseline-export.json) contains the source identity
and every exported file SHA-256. D created this disposable directory for this
session; it remains in place, with no cleanup scheduled. Do not modify it or
use it as a worktree. The candidate harness and C fixture load its implementation
through `--source-root`; the export needs no copied benchmark code.

Runtime: Ruby 3.4.11, x86_64-linux, executable
`/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby`.
The raw JSON records hostname, complete Ruby description, activated gem versions,
gem search paths, loaded source digests and input file digests.

| Input | SHA-256 |
| --- | --- |
| Harness | `a2cae676b0b6d647e31978893775c94b0fe9a0cec9025fd478c9f62e38f584fb` |
| Shared fixture | `85a5f387f69556c91a615efe29ac3a9536bd5a3d4dcb29785f994f00a67cbeb4` |
| `flake.lock` | `a52bdf3a3b9a069175d3af298234c3cf7adeba54540833eed6ad902e9ccc0a64` |
| Server `Gemfile.lock` | `fdc5129f60f9ed2f6a56fbf7f9483af5d6a003fedb13a93e895e9cab87193b52` |
| Rust `Gemfile.lock` | `53b94ab0ef92f5dccfd413eb1e313ed65868f1e2ba41af8b95ce6e62ae8d447f` |

[Committed flake metadata](package-d-committed-flake-metadata.json) retains the
complete resolved graph. The Nixpkgs input is
`02c087f3fe673c9e317f206a627cb6b910336dbe`, NAR hash
`sha256-IoNisKcGbUjdd45qCqywGMCYmZ5EnkxezvLII0FWwNA=`.
[Pre-commit metadata](package-d-flake-metadata.json) records the smoke preparation
source path `/nix/store/892ax87387dxzzjkrxj89g0xb8sygmyp-source`; the committed
receipt supplies the later clean source path. Lock/input equality, actual loaded
sources and runtime paths establish the intended equivalent environment.

## Prepared post-review campaign

Do not launch this until the lead accepts final independent review. A fresh
verification utility must launch/monitor it under the monitoring skill. The
command below is prepared, not executed. If review changes the candidate, replace
the expected candidate SHA only after revalidation and the lead's updated brief.
Keep baseline exact. The modest campaign uses both shapes, size 8, five trials,
two warmups and 100 derivations/renders; no compilation or external server.

Run from the HaveAPI worktree in the ambient shell. Dependencies are already
prepared. The installation-only flag avoids rewriting them. Both modes use the
same unbundled Ruby and combined prepared stores, avoiding Bundler's candidate
gemspec/version preload when loading an exported baseline.

```bash
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop --command bash -s <<'CAMPAIGN'
set -euo pipefail
candidate_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-context-copy-performance-tests/haveapi
baseline_root=/tmp/haveapi-context-copy-baseline-39909094649b
candidate_head=b85ec364057f536940d689b09e612512ffffaf82
baseline_head=39909094649b1d14a23f00615775ca7136acf4fd
evidence_root=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-context-copy-performance-tests
output="$evidence_root/documentation-campaign-$candidate_head"
cd "$candidate_root"
test "$(git rev-parse HEAD)" = "$candidate_head"
test -z "$(git status --porcelain)"
test ! -e "$output"
python3 - <<'VERIFY_EXPORT'
import hashlib, json
from pathlib import Path
receipt = Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-context-copy-performance-tests/package-d-baseline-export.json')
data = json.loads(receipt.read_text())
root = Path(data['export'])
assert data['source_revision'] == '39909094649b1d14a23f00615775ca7136acf4fd'
actual = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
          for p in sorted(root.rglob('*')) if p.is_file()}
assert actual == data['files_sha256']
VERIFY_EXPORT
mkdir "$output"
make --no-print-directory --silent doc
nix flake metadata --offline --json --no-write-lock-file > "$output/flake-metadata.json"
sha256sum flake.lock servers/ruby/Gemfile.lock clients/rust/Gemfile.lock \
  servers/ruby/benchmarks/documentation.rb \
  servers/ruby/test_support/documentation_performance_fixture.rb > "$output/input-sha256.txt"
combined_gem_path="$candidate_root/.gems:$candidate_root/clients/rust/.gems:$(ruby -e 'puts Gem.default_dir')"
for mode in dynamic rust; do
  for revision in baseline candidate; do
    if test "$revision" = baseline; then
      source_root="$baseline_root"
      source_head="$baseline_head"
    else
      source_root="$candidate_root"
      source_head="$candidate_head"
    fi
    extra=()
    if test "$mode" = rust; then extra+=(--rust); fi
    env -u RUBYOPT -u RUBYLIB -u BUNDLE_BIN_PATH -u BUNDLE_GEMFILE \
      -u BUNDLE_LOCKFILE -u BUNDLE_PATH -u BUNDLE_FROZEN -u BUNDLER_SETUP \
      GEM_PATH="$combined_gem_path" \
      ruby "$candidate_root/servers/ruby/benchmarks/documentation.rb" \
      --source-root "$source_root" --source-revision "$source_head" \
      --shape both --size 8 --samples 1 --parameters 2 \
      --warmup 2 --trials 5 --iterations 100 --lanes context,html \
      "${extra[@]}" > "$output/$mode-$revision.json" \
      2> "$output/$mode-$revision.stderr"
  done
done
CAMPAIGN
```

The watcher should retain its exact command/log/exit receipt separately. Stop on
missing dependencies, changed ownership/source inputs, failed output or time
uncertainty and report through the lead; do not repair or install dependencies
inside the watcher. The lead can select a larger campaign after these results.

Before interpreting medians, compare each baseline/candidate pair:

- Both reports have `status: ok`, identical runtime executable/description,
  hostname, activated gem versions and fixture/harness/input hashes.
- The expected exact source identities and actual Context/Rust source paths
  match baseline/candidate. Candidate Git status is empty. Baseline exported
  file digests still match its receipt; both flake.lock hashes agree.
- Cases have identical dimensions, renderer IDs, profile modes, description
  digests, lane names and operations per trial.
- Every corresponding trial has the same successful output status, nonzero byte
  count and body SHA-256. The harness separately rejects changing outputs within
  a run. Context `description_shared` is intentionally false/true; it is not
  part of body parity. Minimal smoke needed no volatile-field normalization.
- Only after parity passes, compare medians for each shape/lane independently.
  Retain raw trials and report variance; distinguish context batches, individual
  HTML requests and adapter batches. Do not claim production latency.

If any output differs, retain exact bodies in an explicitly assigned follow-up
diagnostic and explain the difference before accepting timing results. Do not
drop fields merely to obtain parity. Ordinary CI keeps deterministic identity,
authorization, allocation and traversal gates; it gains no timing threshold.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-context-copy-performance-tests/
