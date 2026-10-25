# Downstream committed-head verification

Status: **all eleven local checks passed** after accepted final review. Outer
exit zero, elapsed 1118.60 seconds; all 710 tracked-file hashes remained identical
and final source/index status was clean. No verification process remains active.
Feature push and exact-head CI are separate later gates owned by the lead and
implementer0. The lead granted the complete
eleven-check batch at downstream HEAD
`ff876abe17e3301da62c1b6afbda055ec89db9d2`, tree
`322fa86ba290b5936a327c21371c94f96f86b249`, using read-only HaveAPI
`090a188cb4ef3477324718627f4ae3415d1c0975`.

## Execution and retained attempts

The fresh standalone watcher was launched with the installed catalog's
gpt-6-luna/low policy and explicit danger-full-access/approval never. Its thread
`01a16a1b-aed2-70a1-a30c-9a23e4f2b89b` initially reported a transient preferred
account error, then reconnected. It stopped because it read the base configuration
as its effective settings. Its actual turn context confirms Luna/low and the
required execution policy. The watcher created no readiness file and ran no
verification batch. CLI exit zero means the blocked turn completed. The launcher
exited and all its read-only command handles completed. See
[launch stream](vpsadmin-client-verification-launch.jsonl),
[launch settings](vpsadmin-client-verification-launch.json) and
[reconciled failure](vpsadmin-client-verification-failed-watcher.json).

The lead authorized visible parent monitoring under the monitor skill's fallback.
Actual execution uses retained implementer3 thread
`01a16451-f29e-7391-9cc3-8aaa7001961c`, gpt-6.1-sol/xhigh,
full_access/danger-full-access/approval never. The parsed `parent_fallback`
readiness record states: “delegated watcher failed readiness despite correct
effective settings.” It makes no Luna readiness claim.

The first parent attempt stopped before Nix evaluation or any of the eleven
checks. The session recorder sorted Path components; the generator sorts relative
path strings. All thirteen canonical and working source files were identical.
The correct order reproduced the accepted generator digest. The lead approved
only the recorder sort-key correction, preserving the expected digest and every
other guard. Retained failed attempt:
[raw log](vpsadmin-client-verification-ff876abe-parent/batch.log) and
[diagnosis](vpsadmin-client-verification-ff876abe-parent/source-digest-diagnosis.json).

The authorized corrected operation uses new evidence directory
[vpsadmin-client-verification-ff876abe-parent2](vpsadmin-client-verification-ff876abe-parent2/).
Its initial source/readiness preflight passed. Both verification target
directories were absent before execution. Source hashes, complete derivation
graphs, exact-output tool bindings, NAR identities and command logs are retained.
The operation uses the existing frozen isolated Ruby 3.3 bundle, downstream
rustfmt 1.9.0/Cargo 1.98.0/rustc 1.98.1 and explicit Cargo/rustc 1.95.0.

The session scripts are
[run.sh](vpsadmin-client-verification-package/run.sh) and
[batch.py](vpsadmin-client-verification-package/batch.py). The corrected recorder
SHA-256 is `80fb31ecf212cc8afde3995ab226a485be490e8afe7fc1c40abd1854be806576`.

## Completed checks

| Check | Seconds | Exit |
| --- | ---: | ---: |
| Provenance | 0.22 | 0 |
| Deterministic regeneration `--check` | 5.17 | 0 |
| Development async all-target tests | 162.64 | 0 |
| Development blocking all-target tests | 131.66 | 0 |
| Development all-feature documentation | 81.49 | 0 |
| Development `-D non_snake_case` | 139.05 | 0 |
| Locked package list | 0.24 | 0 |
| Locked package and extracted-source verification | 124.80 | 0 |
| Rust 1.95 async all-target tests | 166.51 | 0 |
| Rust 1.95 blocking all-target tests | 135.38 | 0 |
| Rust 1.95 `-D non_snake_case` | 140.72 | 0 |

Each test pass ran two unit tests successfully. Async passes left one disposable
real-vpsAdmin test ignored; blocking passes left both ignored. Both naming lint
commands passed with no naming warning. The builds report two unused-field
warnings in generated actionless resource handles; these are separate from the
scoped naming lint and did not fail any check.

Retained archive
[vpsadmin-client-0.1.0.crate](vpsadmin-client-verification-ff876abe-parent2/vpsadmin-client-0.1.0.crate)
has SHA-256 `ab6f3ce4faf00eba8ded4eaa3e69ee1da786c1d5f8e34714796620bff036ff93`
and 697 members. All 686 owned generated files, the ownership manifest and
handwritten facade match the committed source byte-for-byte. Packed Cargo
identity remains `vpsadmin-client` 0.1.0, with registry-only runtime dependencies.

The development shell was evaluated as
`/nix/store/wcq2rxldc19yrz0h7dzyha0h8p9calgk-nix-shell.drv`. Selected executable
outputs are bound to exact producer records within its retained complete graph;
independent Rust 1.95 outputs are likewise bound to their two explicit graph
roots. No producer was inferred from a stale external receipt. Full graph file
SHA-256 values are `bef96ac38e8b5431a4d7f8787490ae416e6c8af770578160462975dc6f6e2a77`
(downstream) and `73c7ec394365b777c149977899237a47d4e999e4424f6d85c4c6fc34cd294c01`
(MSRV). Exact binary/version/NAR records are in
[tool bindings](vpsadmin-client-verification-ff876abe-parent2/selected-tools-and-graph-bindings.json).

Final evidence includes
[batch result](vpsadmin-client-verification-ff876abe-parent2/result.json),
[outer execution and identity](vpsadmin-client-verification-ff876abe-parent2/parent-result.json),
[all command exits and logs](vpsadmin-client-verification-ff876abe-parent2/steps.json),
[final source hashes](vpsadmin-client-verification-ff876abe-parent2/source-after.json) and
[46-file evidence digest inventory](vpsadmin-client-verification-ff876abe-parent2/evidence-sha256.json).
The inventory SHA-256 is `35a9c4304edffdb1c28a76c9d0d818e85498a4b25241e5db9e776b142ac56ed4`.
Direct PID 820437 exited and tool handle 70965 completed. The failed watcher and
first failed preflight remain preserved separately; no source or tool guard was
weakened to obtain this result.

No source/Git/pin/lock change, writing regeneration, production/API access,
publication, release workflow, default integration or lifecycle action is part
of verification. Ignored real-vpsAdmin mutation tests remain unselected.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
