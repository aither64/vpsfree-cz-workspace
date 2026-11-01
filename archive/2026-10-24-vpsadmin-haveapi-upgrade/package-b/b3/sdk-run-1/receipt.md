# B3 representative SDK compilation

Passed the one assigned parent-monitored batch on 2026-10-26, without retry.
`acceptance.json` records all predicates passing. Exact source head remained
clean at `70a2ed54b98d0c2f359a9cc4484452a257a9807b` before and after execution.
No repository, profile, SDK, schema or provider source changed. The existing
base `b82eeca50cd4dd7bd76728685c7de8aad66e7ba5`, A
`44393c352fbd5e9247850ed8490f369999553d62` and B head are unchanged; their
complete history and no-migration inventory remain in the B3 source receipt.

| Unique complete programs built | Go | Rust async | Rust blocking | Total |
| --- | ---: | ---: | ---: | ---: |
| Unchanged current administrator page output | 6 | 7 | 7 | 20 |
| Separately labelled synthetic member fixtures | 2 | 2 | 2 | 6 |
| Total | 8 | 9 | 9 | 26 |

The 20 page programs are initialization, Basic/OAuth2 authentication, existing
token authentication in Rust, Cluster.PublicStats, Location.Update and
DnsResolver.Index. `program-selection.json` retains their original role/panel/
sample coordinates. It records the prebuild state `compiled: false`;
`acceptance.json` records the final successful compilation for all 26 programs.
Final validation compared every consumer source byte and SHA256 to its original
capture. No auth builders were combined, calls replaced or sources reformatted.

The normal API fixture loaded once. A member-authorized `OPTIONS /v7.0/`
returned HTTP 200; status and raw response were saved before assertions. Actual
mounted profiles and upstream renderers produced all six additional programs,
with selected authorized contracts, structured samples and source bytes retained
before output predicates. The fixture spec passed one example, zero failures,
seed 41771; outer identity/mount/capture elapsed 45.004s.

Dataset.Snapshot.Show uses the verified SDK route
`/v7.0/datasets/{dataset_id}/snapshots/{snapshot_id}`, two Go path arguments and
the Rust `dataset__snapshot("101").show("202")` chain. DnsRecord.Update uses
only Go `SetTtlNil(true)` or Rust `.ttl_null()`. The IDs and responses are
synthetic; these six programs did not appear on the published page. Retained
SDK contract files independently show the corresponding routes and nullable
setters. No emitted program or API mutation was executed; compilation does not
prove wire serialization, credentials or successful server actions.

The exact Go module pseudo-version is
`v0.0.0-20260604065514-1d9240f3d27b`. Download metadata identifies Git source
`1d9240f3d27b5831baf3694baab5fe06294875d8`; all 648 downloaded Go source files
equal the previously inspected source export. The SDK's Nix shell selected Go
1.26.8 from `/nix/store/640irzgl08asrnjly4dspdbx8lz3cvqr-source`.
`go build -buildvcs=false ./cmd/...` passed in 62.150s (70.211s including shell
entry and identity work). Module metadata, go.mod/go.sum, compiler store paths,
derivers, closure and selected nixpkgs identity are retained.

The Rust verification consumer pins registry `vpsadmin-client = "=0.1.0"`.
Both Cargo.lock and the downloaded archive match SHA256
`2099d96e698e23912879cc15a32097c920f0db96976c2bee671a5ce2239777d0`;
archive VCS metadata identifies `b6f84679d33ff041388535dcf4dc060aeb0d1b9d`.
The fresh consumer lock resolves 159 packages. The SDK's locked nixpkgs
`fe13242281a67641c0102cdb1087f0ebe586c7df` provides Rust/Cargo 1.98.1;
complete flake metadata, lock, tool paths, derivations and closures are retained.
This is one supported compiler, not a separate MSRV matrix or reuse of an older
dependency graph's compilation result. Normal application/KB version selection
was not changed to an exact verification pin.

`cargo build --locked --bins` passed first, in 272.330s. The consumer has no
default features and all nine blocking bins require its `blocking` feature.
`cargo build --locked --bins --features blocking` then passed in 159.199s,
building the nine additional blocking programs and the async bins with that
feature enabled. Both commands exited 0; outer Rust shell/resolution/build time
was 463.310s. All eighteen Rust binaries and their hashes are retained. Neither
compiler reported warnings or errors.

Installed canonical HaveAPI 0.30.2 loaded files, absolute paths, hashes,
effective/packaged Ruby locks and full Nix input graph match the accepted
performance receipt. Original performance and baseline file hashes remain
unchanged. All six Go limitation records remain explicit: existing-token auth
and Vps.Index for each of the three captured roles. Only 20 of the 168 actual
page programs were compiled; the other 148 retain their prior static audit and
output-equivalence evidence. Supplemental synthetic compilation does not expand
that published-page count.

The lead explicitly selected the dev-session-monitor parent fallback while A
services occupied the sole utility slot. No extra watcher launched. Commands
used affinity 56–57, CARGO_BUILD_JOBS=2, GOMAXPROCS=2 and Nix cores=2/max-jobs=1;
the effective Cargo process limits were observed. Capacity snapshots retain 64
CPUs, load 18.61 before/7.17 after and available memory about 44/55 GiB. These
are host observations, not a claim of global idleness. No foreign process was
controlled and no kernel build occurred.

`operation-reconciliation.json` confirms every owned command/helper PID is gone,
the fixture listener is absent and no current run reference remains in owned
Ruby/Go/Cargo/Rust/database processes. The fixture's normal exit hook stopped
its disposable database. No cancellation or retry was needed. All tool handles
completed; the parent owns no remaining operation. No push, merge, deployment,
cleanup or session lifecycle action was performed. R1's earlier lead closure
and source/performance proof remain unchanged; this separate gate supplies
bounded SDK consumer compatibility evidence.
