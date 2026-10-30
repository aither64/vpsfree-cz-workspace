# M8 remaining performance acceptance: static preparation only

Prepared29October while owner2 folds R3. Accepted tree is
543cd44c4a1863489ae2289d2a8769a60e7c1b85, accepted sidecar
18b9c73621bb7865bb2f320a7fec295c960734d8. The final folded SHA is pending.
No candidate archive/export or output directory was created at this temporary
head. No Git/index/ref/hook command, runtime/version call, test/build/measurement,
Nix/environment setup, network or utility ran. Only file/path/hash inspection
and this compact preparation note; previous receipts/commands remain untouched.

Remaining batch: current all-client contract, then exactly one direct
f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0→new-final quick. Do not duplicate
ordinary acceptance work. All9neutral harness/fixture/spec hashes match24ec,
but45existing source paths differ, including12renderer/helper/adapter paths.
R3's4current hashes match its accepted receipt. M7 output cannot validate M8.

## Existing environment and static availability

Reuse command-inputs.json's exact immutable tools:

- Ruby: /nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby
- Bash: /nix/store/nnm9gdr70ihc6zc9298mzz8jpcgaciql-bash-5.3p20/bin/bash
- Git: /nix/store/xgw813vgzl2q0696sq45adpj0xd690jq-git-2.56.0/bin/git
- Loader library: /nix/store/7a2cjhcgzyym5zaz6m4fksw47qvm150w-gcc-16.2.0-lib/lib

All4paths and executable/libstdc++ hashes match command-inputs.json. All72frozen
records,69installed gemspecs and2148protected inputs match. Matching specification
files exist for all87weekly-calibration gem declarations in dedicated benchmark
.gems plus7b77Ruby defaults. JSON2.21.2 and io-console0.9.4 native extensions and
all71retained availability directories exist. No static prerequisite gap found;
dynamic loading/activation/live87-gem graph remain unproved until authorized.
Never substitute root/server/Go/Rust bundles. No restore/install is planned.

Use the existing environment, clearing every inherited BUNDLE* plus RUBYOPT,
RUBYLIB,RUBYGEMS_GEMDEPS,GEM_HOME,GEM_PATH,LD_PRELOAD,LD_LIBRARY_PATH, then set:

```sh
GEM_HOME=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi/servers/ruby/benchmarks/.gems
GEM_PATH=$GEM_HOME:/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/lib/ruby/gems/3.4.0
PATH=$GEM_HOME/bin:/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin:/nix/store/xgw813vgzl2q0696sq45adpj0xd690jq-git-2.56.0/bin:/run/current-system/sw/bin
LD_LIBRARY_PATH=/nix/store/7a2cjhcgzyym5zaz6m4fksw47qvm150w-gcc-16.2.0-lib/lib
LC_ALL=C.UTF-8
TZ=UTC
RUBY_YJIT_ENABLE=0
```

Existing commands.md provides exports/the clearing loop. Reuse that environment;
no broad Nix entry/realization. Both profiles enforce weekly87-gem calibration,
not the differing historical quick calibration. Neutral JSON activation and
benchmark:true io-console activation must fail on missing/conflicting versions.

Frozen identities, unchanged across current source, retained f6/M7 preparations:

| Input | SHA256 |
| --- | --- |
| Benchmark Gemfile | eaca394cd1b4b5d05dfc2b95d40bf3d75a42ca058a952cc51d0833b21c7534b4 |
| Benchmark lock | 5bcd8d2fec2f1a66b5a4981554be90165eb7e739b87a732405bbf64b5147fe66 |
| Benchmark shell | fd42593a40e09298b73e31f848cc13d38a3447fbae2f09cd7279548dc4748cef |
| Budgets | 57b8d4725e76c4552e6cb2eb54982cd8d406bd2415eb99e51cb43049bae3a050 |
| Neutral endpoints | d393c397b4453dccd9f90f3160574cd0df3abf8eb8768c7d63d7d8e15dc18630 |
| Comparator | 2fe2d3898c5dc8581c51fe1df8bf0406516de6e335930ca6b1c965f75ed38fe2 |
| All-client spec | 4ab25b1be75522f8b44a6e25fd31b8ea6d73e41aa06c972fd1b221a72b3ec498 |

Fixed reference remains b85ec364057f536940d689b09e612512ffffaf82.
No budget/version/lock/graph/normalization changes or candidate-specific waiver.

## Tasks after the actual folded final SHA and separate grant

After actual final SHA/review reconciliation, under a separate export grant:

1. Verify clean final SHA/tree equals accepted543cd44tree. Make ONE new
   performance-<final-prefix> export using existing preparation: raw archive/hash,
   native mode/blob and full-file manifests; verify actual count, not assumed908.
2. Copy valid existing11generated docs only after source/generation/package
   evidence verification; bind shared source and JSON-schema ERB/copydoc/output.
   No rebuild/makeDoc here; report missing copies instead of silently rebuilding.
3. Rebind original unchanged f6native/archive860blobs/9docs. Static rehash now
   verified its archive b0139d61d086abcb5fafc5d65d12581e3d7096514ea32d42b1bebe6bed8e88d2,
   all860source hashes/9doc hashes. Preserve prior905/d67/908/24ec exports/failures.
4. Bind final neutral/source/loaded-input expectations and frozen inputs; update
   existing commands' final SHA/export/output paths only. No new framework.
5. Fresh Luna/low watcher after main execution grant/free sole utility runs the
   batch serially; all-client must pass before the single pair. No concurrent
   compiler/browser/listener campaign or duplicate ordinary gate.

These are the existing direct recipes, **UNEXECUTED templates**. FINAL_SHA,
FINAL_EXPORT and NEW_EVIDENCE_ROOT must be replaced with actual final values
only after binding; the named paired directory must not already exist:

```sh
# cwd = FINAL_EXPORT, environment above
/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby -S rspec servers/ruby/benchmarks/spec/client_examples_spec.rb --format documentation

# cwd = exact final HaveAPI checkout, same environment, outside Bundler
/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby servers/ruby/benchmarks/endpoints.rb run --baseline-root /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/performance-ab5b1118/baseline --baseline-sha f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0 --candidate-root FINAL_EXPORT --candidate-sha FINAL_SHA --profile quick --budgets servers/ruby/benchmarks/performance_budgets.json --output NEW_EVIDENCE_ROOT/paired-quick
```

First command is the existing Makefile recipe after prepared docs, without
recopy:15×7×both details, real profiles/admin-member-admin,128unrelatedsubtrees,
three8-render allocation batches,+32objects/calls and both2/4/8resource/action
bounds at2.5increment ratio. Pair retains14quick cases, real-cookie final HTML
with per-request crypto/token lookup versus genuine Basic f6; setup, roles,
counters, source-version normalization, budgets and loops remain unchanged.

## Expected duration, proof and stop policy

Observed24ec: all-client22.7s+0.728sload (CI step25s); d67→24ec pair5m40s.
Plan roughly5–10minutes; f6→M8duration is uncertain, so fresh watcher required.
Existing setup120s/request-batch30s watchdogs remain, no invented overall kill.
Quick target1s/adequate750ms,3self/5alternatingpairs,20%wall/CPU,50msminimum
increase and existing allocation/reference/counter limits stay exact.

Stop first deterministic failure/drift/error; no pair after failed all-client.
Retain phase/logs/artifacts, report and diagnose in parent. Inconclusive is a
stop/report outcome even at exit0; no retry-to-green, timing composition,
reference/budget/graph relaxation or watcher repair. No readiness/pass claimed.

Retain original native archive/tree/full-file/source-version/raw-normalized
manifest proof; exact frozen runtime/87activatedgems and loaded-source hashes
per process; all-client matrix/role/growth records; original runner
pilot/calibration/self/alternating samples/report, comparator/budget/consumed-
samples hashes, response/counter/authorization stability, stdout/stderr/exit.
No alternative harness. Actual final graph must match the original calibrated
policy, not merely static gemspec availability.

CI40773074063 remains24ec all-client214/0 +d67→24ec14casePASS,19processes with
87gems/native905/908exports. It demonstrates existing environment/harness use;
it is neither M8 all-client nor directf6→M8. Old35c→a06b failure stays failed.
Ordinary checks/review retain their existing scope without duplication here.

Source/guide/validator/Theme files and old proof are untouched; only this compact
note added to the existing preparation. No active owned process/utility.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
