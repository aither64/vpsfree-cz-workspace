# LC1: existing trace_marker under noclobber

**Complete narrow remediation; source FROZEN, uncommitted.** Owner implementer3,
retained Sol/xhigh/workspace-write, same verified session/env/roster. Reviewed
HEAD remains `12df7c05ac72a48fac748b09f6f9c7660f3a1e0e`; the index is empty
and only `tests/suite/kernel/livepatch-6.12.95/qualification.rb` is dirty.
No Git/index/ref/commit/publication/runtime action was performed by C.

The lead supplied the complete Blocking LC1 finding and accepted exact remedy.
The canonical `loader-csd-review.md` was not yet present at C's bounded reads;
no whole-report-read claim is made. Root owns recording the report and final
step-9 reconciliation. LC1 says set-C also protects the already-existing regular
trace_marker, so the normal clock-used marker causes failure before exec.
The old control created only its directory and missed that real precondition.

## Representative RED before source edit

The control was changed first to precreate a **regular, non-symlink** marker
containing `loader clock=begin uptime=0.9`. The actual unmodified command from
12df, under sh-ec/set-C, then exited **1** at the marker redirection:
`cannot overwrite existing file`. The PID file was created, the marker retained
its clock bytes, and the actual exec replacement was **not reached** (0 calls).
The affected control batch exited1 at that test after its earlier controls.

[RED batch](package-c-loader-lc1-red.log) and
[exact RED command/output](package-c-loader-lc1-red-commands.log) preserve the
first failing command and condition. Invocation from the tracking directory:

```sh
LC1_COMMAND_LOG="$PWD/package-c-loader-lc1-red-commands.log"   /nix/store/z30vypx0r6mgbfs0a86m6vd3s7pk07sb-ruby-3.4.11/bin/ruby   package-c-loader-controls.rb
```

This is a real shell/executable-fixture result, not a guest/module load.
Original source SHA256:
`a6813d0b7ae8ec5f9eb0ff37d0053f21cadc5e2149dfe30d106b31b45208cc12`.

## Smallest correction and GREEN

Only the trace_marker redirection in qualification_loader_command changes:
`cat ... > trace_marker` becomes `cat ... >| trace_marker`. The attempt PID file
still uses plain `>` under set-C. No global clobber change, marker-format,
module/locale/attempt, activation/deadline or other behavior change is made.
Byte comparison against HEAD proves this is the only application source change.

[GREEN batch](package-c-loader-lc1-green.log) and
[exact GREEN commands/results](package-c-loader-lc1-green-commands.log) show:

- Attempt1: status0, one actual exec; PID1576094 matches its file/marker and
  executor, locale C and `/fixture/current.ko` unchanged.
- Distinct attempt2: status0, two cumulative execs; PID1576116 matches its own
  file/marker/executor, and attempt1 file bytes remain identical.
- Repeated attempt1: status1 at its exclusive PID file, still two execs;
  attempt1 bytes and the attempt2 marker remain unchanged.

All **35 affected actual-loader controls pass**. The two previous command
controls were strengthened and a distinct-attempt control added. The existing
[control file](package-c-loader-controls.rb) runs actual extracted methods;
Open3 waits/reaps every owned fixture executable. The matching GREEN command
uses the same cached Ruby/control file with LC1_COMMAND_LOG pointing at the
GREEN command log. No fixture process remains.

Final source SHA256:
`5c4db809f464110d1eea2a29008fc23f9359d9d944a8cd48ee00c818422caf72`.
[One-line caused diff](package-c-loader-lc1.diff), SHA256
`b1dedf7496d0efdb6b52f8e6af338704e59852719bb2d2ef8f6827031821a818`.

## Quick checks and retained evidence

Cached Ruby3.4.11 `ruby -c` on qualification.rb returns0 / Syntax OK.
The declared absolute-primary Gemfile/.gems Bundler command runs RuboCop on
that file only: [log](package-c-loader-lc1-rubocop.log), one file/no offenses,
status0. `git --no-optional-locks diff --check -- <qualification.rb>` returns0.
No broader host batch, Nix evaluation, build, network, CI or VM ran.

Other three application files are byte-unchanged at their accepted hashes:

| File | SHA256 |
| --- | --- |
| `.github/workflows/ci.yml` | `ffce88c8ad7a5e5654ff967c98f5e8218cbfa546bead738102c08c5f9cdf2ed7` |
| `tests/suite/kernel/livepatch-6.12.95-common.nix` | `8acb93d5d59568b65e35e0a7fb436ce1354da149a5b882b7e66f9e94518c0509` |
| `tests/suite/kernel/livepatch-6.12.95/loader_host_sched.sh` | `6b85cedda7222e0b37019d7040767204b4a306a5b9eb9c006d32822b1db8045c` |

The old116-green source/check receipt remains historical and is superseded for
this defect; it is not proof that12df can activate. The unaffected44 dying-
observer controls retain their byte-identical method prefix, host20 retains
the exact unchanged helper, and selector/workflow18 retains its exact unchanged
files/interfaces. Their **82 prior checks were not rerun** or relabelled as a
new batch. Fresh evidence here is the affected35-control GREEN plus one-file
parse/style/whitespace; no117-check or guest-pass claim is made.

A owns the later absent-guarded local reviewed-12df provenance ref and ordinary
hooked amend of the existing loader purpose, preserving all six prefix objects
and truthful owner message. C has no Git window. Root owns the requested narrow
inspection/reconciliation before publication or runtime. The original runtime
limits, primary645927/14400, source GC roots, all refs and old fault attribution
remain intact. All C clients/fixture children are terminal; no owned process.
The session stays open, and no cleanup or lifecycle action occurred.
