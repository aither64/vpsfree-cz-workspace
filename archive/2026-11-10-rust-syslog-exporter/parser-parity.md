# Executable Ruby/Rust parser and collector parity

Owner: implementer1, packageP2. **Complete, ready for acceptance; all owned
processes and candidate services are stopped.** Both exact supplied archive
records behave the same in the actual retained Ruby and Rust applications.
Each increments only the known node2 message counter with `program="1"`;
neither raises the null-pointer gauge. A direct `kernel` positive control
raises the gauge from0 to1 in both. This is executable evidence, not only a
source interpretation. It does not establish universal parser parity.

## Inputs and actual applications

- Ruby package `/nix/store/w7g32wplgls6x79608h6nij02a4vvq9y-syslog-exporter`,
  source7c5a8e74e44a704cceb99cd05716af6800d78efd; real Ruby3.4.9/Puma8.0.2/
  Rack3.2.7/prometheus-client4.2.5 closure retained from production baseline.
- Rust package `/nix/store/3hk34i2k760dirn1xrarxqsrwrcryaj5-syslog-exporter-0.14.0`,
  source6ecada0a9d2f6457a11031a3a4ffc341584fb29c, complete tree identical to the
  measuredfaf source. Immutable binary SHA256
  `f1ad1b4f65be4e4315224b8e3426603f67eb8e99a42593e8f7cfe40ddbc4062c`.
- Exact67-host JSONK5 was copied, changing only each localFIFOpathname. Node2
  key `cz.vpsfree/nodes/stg/node2`, alias `node2.stg`, FQDN
  `node2.stg.vpsfree.cz`, OSvpsadminos remained identical. Per-run JSON bytes and
  hashes, local listener addresses and full commands are in the receipts.

Ruby ran through the real wrappedw7/bin/puma with a standard isolated Puma
configuration and Rackup.app(ownJSON). Workers0, WEB_CONCURRENCY unset, production
environment; no monkey patch or exporter source modification. Rust ran its
existing CLI. Each used a separate ownedFIFO,1MiB capacity and loopback listener,
registered with public dev-session service run. No production FIFO/process was
opened. Metrics came from the real middleware/HTTP applications.

The recipe writes exact LF-terminated fixture bytes and waits for a unique
message-count drain marker after each input. Legacy node2 metrics are normalized
by metric name, label values and numeric value; marker-only rows are excluded
from comparison. Full before/after selected metrics and raw HTTP response hashes
are retained. Program values below are directly observed legacy counter labels;
no parser instrumentation was added.

## First decisive result and startup separation

Both user frames are233bytes includingLF:

| Case | SHA256 | Both applications | Null gauge |
| --- | --- | --- | --- |
| 21:32 archive record | b1b4c7cfcac9c082644422f5ea8daf42a11442253102c2be57185132938ea12c | program1 messagecount+1 |0→0|
| 22:33 archive record | 1cf90f3e892ad8b5d95275587799dee7f3ffc3e8ec8e30dcdf9b10b796431015 | program1 messagecount+1 |0→0|
| Outerkernel/FQDN positive | b2753e02ef9b35bd8e5415a7c79874e562b5a6e8dae417b146f9f2b9673ade8f | kernelmessage+1, programkernelmessage+1 |0→1|

The nested timestamp/hostname/kernel text in the supplied frames is a body after
outerprogram1; neither application recursively unwraps it for the kernel
collector. This reproduces the observed compatibility question without changing
producer or transport behavior.

Separately, a complete initial p2first record was counted0 byRuby and1 byRust.
Two subsequent warmup records and a barrier were drained before all comparisons.
The intentional complete-first-line fix is therefore recorded separately and
does not explain the program1 outcome. Exact startup bytes are in the manifest.

## Only the requested finite edge vectors and controls

All edge vectors came from reviewer0's current P2 clarification. U+00A0 isNBSP;
U+0661 is the Arabic-Indic digit. These are observed differences, with bounded
classifications; no application fix was made.

| Input | Ruby | Rust | Scope |
| --- | --- | --- | --- |
| Two spaces afterkernel, leading MSG space | Empty namespace, OOM+1 | Same | Canonical leading-space control agrees |
| Extra space before outerprogram | Counter label contains the odd whole remaining program string | No legacy update | Documented malformed-header rejection boundary |
| kernel[U+0661] | programkernel[U+0661], no detector | programkernel, kernelcounter+1/nullgauge1 | Real Unicode regex edge; producer occurrence/support not established |
| Kernel namespaceNBSPns | syslogns=NBSPns | syslogns=ns | Real Unicode namespace-label edge; normalASCII control agrees |
| LXC prefixNBSP42NBSP | id=NBSP42NBSP | id=42 | Real trimming edge; no producer occurrence established |
| Nodectld body with rawFF | messagecount+1/crashgauge1 | No legacy update | Explicit accepted UTF8-rejection boundary; producer passage not measured |
| LXC body startscolon | id=whole stripped body | id=empty | Legacy index0/slice quirk; no producer occurrence established |
| Normalkernel[]/[ns] | Normalizedkernel, namespace ns counter+1 | Same | Requested normal control agrees |
| Supported old-spec SVLOGD nodectld/FQDN form | Messagecount+1/crashgauge0→1 | Same | Fresh-state control agrees |

The initial SVLOGD comparison followed the invalidUTF8 vector, which had already
set the Ruby crash flare. Its raw gauge deltas differed while both final gauges
were1. A single focused fresh-application SVLOGD replay corrected that fixture
state confound and showed identical0→1 behavior. The original result is
preserved, not mislabeled as a parser regression. No full batch was repeated.

Malformed and invalidUTF8 boundaries were already deliberate design choices.
Unicode/trim/colon findings are finite edge differences, not evidence that all
producer-reachable normal records are identical. No rawFF producer/transport
campaign was run; no producer validity or universal compatibility claim follows.
Architect/reviewer own contract classification; lead/user requested leaving the
current application behavior unchanged.

## Reproduction and evidence

From the verified workspace, these commands create only new owned isolated
services and regenerate the fixtures:

```sh
python3 work/2026-11-10-rust-syslog-exporter/p2-replay.py first
python3 work/2026-11-10-rust-syslog-exporter/p2-replay.py edges
python3 work/2026-11-10-rust-syslog-exporter/p2-replay.py svlogd
```

[Recipe](p2-replay.py), [fixture bytes/hashes](p2-artifacts/fixture-manifest.json),
[first compact result](p2-artifacts/first-compact.json),
[all classifications/deltas](p2-artifacts/parity-summary.json),
[original edge run](p2-artifacts/edges-result.json),
[cleanup recovery](p2-artifacts/edges-cleanup-recovery.json),
[fresh SVLOGD control](p2-artifacts/svlogd-result.json). Per-run configs, Rackup/
Puma settings and application logs remain compact raw evidence.

## Effects and delivery boundary

Recipe elapsed times: first22.243s, edges17.415s, focusedSVLOGD20.933s; setup and
coordination waits are separate. A fresh installed-policy Luna/low observer owned
the uncertain first batch (22.48s including wrapper). The known quick later
commands ran inline. First and focused control exited0. Edge application replay
completed, but its cleanup exit2 preserved a public service-stop refusal75 due
to another session command holding the lock. Only the exact owned stop was
retried after diagnosis; no application batch rerun or private helper was used.

All6 own registered units are now retired/inactive/dead, MainPID0, empty
cgroups. Exact unit IDs/properties and cleanup command are in the receipts.
All local drivers, service children, watcher and tool sessions ended, including
44425,61188 and12639; no uncertain effect remains. All3 owned disposable
scratch/FIFO/config directories were removed only after reaping proof. No Cargo
target, source build, vendor fetch, GC, peer data or recovery root was touched.

No production access/injection, deployment, shipped source/docs/driver change,
commit, claim, merge or session lifecycle action occurred in P2. Production
3hk/gsw and the lead-held claim remain untouched. P2 is ready for acceptance;
capacity is available for separately assigned configuration integration
preparation after acceptance, and that next package has not started.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/>.
