# Naming evaluator availability successor

Static preparation only. The original naming-runtime-evaluation-preparation-v1
directory, its37 inputs, external expectations and verify-evaluation.py remain
unchanged. This successor references that frozen base instead of refreshing its
source, consumer or tool expectations. No evaluator was imported or executed;
no Nix, query, build, test, native/provider/VM/browser, Git or network command ran.
Only this new directory was written. Session/current and the full environment
pair matched; live roster32 confirmed ready Sol/xhigh/workspace_write.

The accepted method snapshot has SHA256
473683b855cbd0e64a6b96cbf899a2795f9b555fc22ebcfd1a447c5ef298b11b.
Only its selected-root availability postcondition is applied. The evaluator
retains its original modern eval argv and options. It adds no legacy evaluation,
instantiation, source retrieval, repair, root or build route. No cause is assigned
to the browser's earlier eval0/missing-drv observation.

## Narrow change

After learning exactly the four returned output derivations plus the assembled
package, the successor requires five distinct canonical store .drv paths:

1. Record each regular, non-symlink raw file's mode, size and SHA256. Each file
   must be readable, nonempty and at most16MiB. File identity is checked while
   reading. A supplied preacceptedRootSHA256 entry is compared only for that
   exact root; otherwise the hash is a new observation for parent acceptance.
2. Run the bound modern nix derivation show on exactly those five roots,
   without --recursive. Require exit0, complete JSON and exactly the full selected
   identity set, accepting the retained full-path or basename JSON encoding.
3. Repeat raw observations, require equality, then run the separately bound
   nix-store --check-validity on exactly those roots. Require exit0. This command
   has the common no-build settings; it has no unsupported legacy --offline flag.
4. Repeat raw observations and require equality to the first observations.
   Retain the successful availability observation with parent acceptance pending.
   Only then enter the unchanged recursive inspection and original JSON inspector.

The recursive call and Nix options compare AST-exact with the original. The
original inspector is used at its original path, SHA256
ba37b1d3ce35a0ad6b572ff90b7ffd2c3126ba91daa21c2ae3c8c394322d7ccc.
The selection expression and all application/fixture assertions are unchanged.
The full narrow evaluator diff is evaluate-original-to-successor.diff.

Every new subprocess uses the existing bounded stage/owned-client join and
source/input/receipt/environment/tool pre/post guards. Original stage deadlines
and caps are unchanged. Nonrecursive metadata and validity each have60seconds;
the three raw-observation sets each check a60-second budget over at most five
16MiB files. Overall stage admission is900seconds; the parent watchdog is960.
The parent watchdog bounds an unexpectedly blocked local file read too. No group
emptiness, daemon settlement, atomic cancellation or durable retention is inferred.
Missing/invalid/mismatched roots or nonzero/unfinished commands stop before
recursive inspection. Partial raw/query receipts remain; no retry or cleanup.

The new absent attempt is attempt-evaluation-availability-01. Attempt creation
is exclusive and every new gate receipt uses exclusive creation. The original
attempt path is never reused. The runner validates both the original packet
hashes and this successor's hashes, preserving all original external expectations.

## Pending release and exact future command

ready.json records full argv templates, cwd, bounds and new gate effects. The
future command, only after parent accepts the same current Python entry, is:

```sh
/home/aither/.nix-profile/bin/python3 -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/naming-runtime-evaluation-availability-successor-v1/evaluate.py --execute-parent-released-evaluation
```

Cwd is this successor directory. Parent must create NEW final-bindings.json and
parent-release.json here, using the original nonsecret binding schema and exact
release scope. The release's attemptDirectory and packetHashesSHA256 bind this
successor. launchTools must additionally contain a parent-accepted nix-store
entry, resolved immutable executable identity and hash. No nix-store path was
guessed, scanned or measured during preparation. The original pending binding
template is retained byte-for-byte under snapshots; all final consumer,
provenance, output, release and current-tool bindings remain pending. Optional
preacceptedRootSHA256 is a map of actual previously accepted full root paths to
their SHA256s, never invented expectations.

No evaluation or metadata launch is authorized. Parent owns source assessments,
current tools, final input binding and one fresh Luna/low/max1 utility release.
This operation's unchanged --offline/substitute settings are not a universal
network prohibition. Any needed exact locked-source retrieval remains a separate
explicit parent disposition; this successor does not add that permission or an
automatic fallback. No output presence, builder success or acceptance is inferred
from an evaluated path or from this static preparation.

Static checks are Python AST and JSON decoding only, plus exact base evaluator/
inspector/packet-manifest hashes and snapshot equality. There is no import of
the executor, Nix syntax/evaluation check or fixture execution. The final binding,
release and fresh attempt are absent. Availability observations remain temporal:
later graph/build admission must use current actual proof, not a permanent claim
based on an old hash. Root retention, application, provider and deployment gates
remain separate. The dedicated real account/home remains unresolved.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
