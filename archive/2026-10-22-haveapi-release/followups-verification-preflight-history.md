# Verification preflight diagnosis history

Historical snapshots, preserved from state.md. None of the first two attempts
reached a build/test phase. Current status is in [state](state.md).

## Active verification operation

Implementer0 launched one fresh standalone verification utility, native thread
`01a1698d-8aee-7e63-b263-67706b836c0e`, saved watcher identity
`dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12`, gpt-6-luna/low, explicit
danger-full-access/never, pinned catalog `840de475`. Evidence directory:
`followups-verification-090a188c-20261023T161428Z/`. Exact source/head/tool/
cache/dist guards and per-step evidence are prepared; source/Git writers frozen.

Lead inspected launch metadata only, without duplicate batch-log polling. The
initial `utility-ready.json` says ready=false solely for
`developer_instructions_layered=false`, while `utility-launch.json` contains the
required verbatim native developer-instructions CLI setting. Implementer0 is
reconciling recorder predicate versus actual launch at a safe boundary; no blind
relaunch or acceptance. Utility owns existing operation/log handle. Readiness discrepancy was subsequently reconciled as a recorder bug; the
operation then stopped at the formatter version guard, as detailed below. No
publication/default integration or session lifecycle action.

## Verification preflight failure and bounded recovery

First verification attempt exited 1 in 38.5587 seconds before any of its eight
phases. Its session-owned guard incorrectly required rustfmt's displayed version
to contain 1.99; the exact pinned `rustfmt-1.99.0` package binary reports the
independently versioned `rustfmt 1.10.0`. No product/source defect is indicated.
The normal root Nix hook prepared only this worktree's root bundle (33 gems);
no component dependency phase, build, test or artifact ran. Exact reviewed head/
tree, clean tracked source/index, 302 known cache paths and empty dist were
rechecked; no operation remains.

[Readiness reconciliation](followups-verification-090a188c-20261023T161428Z/utility-ready-reconciled.json)
proves the initial false flag was a recorder predicate comparing the bare
instruction string to whole argv entries. Parsing the actual TOML CLI override
reproduces the exact native instruction digest; no launch policy changed.
[Effect proof](followups-verification-090a188c-20261023T161428Z/failure-source-effect-proof.json).
Original evidence remains intact.

Lead granted one new attempt to implementer0 with a new evidence directory and
fresh pinned Luna/low utility. Only the session tool guard changes: exact pinned
formatter path and actual 1.10.0 identity; compiler/Cargo 1.99 and independent
1.95 checks remain. Correct parsed readiness must pass before execution. Same
reviewed source, same accepted cumulative plan, no application edits or blind
retry. The utility stops on failure; no publication/default integration authority.

## Current verification attempt: readiness passed

Fresh utility thread `01a16991-f92e-7e42-8b34-95930ff8682a` owns the recovery batch
at exact `090a188c`, evidence `followups-verification-090a188c-20261023T162121Z/`.
Lead read its actual readiness/identity files: all eight checks true, ready=true,
model/effort/policy/native/catalog verified and parsed launch/native instruction
digests equal (`20212a3e814132d953ca91029e022451e03acc83fc52872ca238f8c76f4dfbb5`).
The raw metadata is authoritative over abbreviated narrative hashes. The batch
requires readiness success both before launch and inside run.py. Prior attempt
remains unchanged; no duplicate operation. Source/Git writers remain frozen.
Watcher/owner retain execution and logs; lead does not duplicate batch polling.
Results and full verification acceptance are still pending.

## Second verification attempt stopped in evidence capture

Recovery batch exited 1 in 9.531 seconds before any of eight verification phases
or artifacts. Readiness and exact formatter/compiler/MSRV identities passed.
A session evidence export queried rustfmt's recorded store deriver, then attempted
recursive derivation export; Nix rejected that recorded .drv as invalid. The
root-shell recursive graph export had already succeeded. This is not a product
check failure. Only normal authorized root setup ran; exact reviewed source/tree
remain unchanged, no owned process remains and no retry was made.

Implementer0 owns bounded diagnosis against the saved graph/output bindings and
store metadata before proposing evidence-only recovery. No application/Git/lock
change, test/build or additional install is part of that diagnosis. Keep prior
records intact. Full build/test/artifact verification remains pending.

## Accepted Nix graph diagnosis and fresh attempt grant

Lead read the owner diagnosis. The evaluated locked-root recursive graph has
2067 nodes (SHA `7d394152391db092c3059053548a0a3d30dec997c658bd9c3e71cb1137f9d0bb`)
and binds all three exact selected development tool outputs to valid evaluated
derivations. Their recorded store-producer pointers differ; the formatter's old
pointer is absent. Independent Rust 1.95 graph export succeeds with 1377 nodes
(SHA `73c7ec394365b777c149977899237a47d4e999e4424f6d85c4c6fc34cd294c01`) and
binds both exact documented output paths. All remaining recorder prerequisites
were audited without launching tests, builds or installs; no operation remains.

One fresh attempt is authorized using a new pinned Luna/low utility and evidence
directory. Only session evidence capture changes: derive development tool
bindings from exact outputs in the evaluated locked-root graph; recorded store
derivers remain diagnostic. Export independent 1.95 inputs from the exact valid
roots. Same reviewed source/tools/eight-phase plan and strict readiness/source/
cache/dist guards. Stop on any failure; no blind retry or source change.

Evidence limits remain explicit: Rust's temporary generated schema/Cargo.lock/
tree are not retained by the existing runner; historical MSRV nixpkgs revision
is unknown, while exact derivation roots/full input graph/output and executable
identities are retained. These facts grant no reuse claim or release authority.


## Third attempt: startup path resolution

Evidence `followups-verification-090a188c-20261023T162837Z`, thread
`01a16997-f33d-7602-9cd8-da3e03e72f28`, stopped before readiness/run.py. The brief
used correct relative workspace `docs/agent-instructions/verification.md`, but
the watcher attempted nonexistent workspace `doc/agent-instructions/verification.md`.
No setup/test/build/effect/process. A fresh operation was authorized with all
guidance and command paths absolute, existing scripts/policy/phases unchanged.

## Fourth attempt: successful setup/docs, generated-output guard

Thread `01a1699b-4a15-7dd1-b08c-b1e43ac82c21`, evidence
`followups-verification-090a188c-20261023T163216Z`, passed release-deps and actual
gulp doc. It stopped afterward because the strict cache-only untracked guard
did not classify the 69 generated html_doc regular files. Source/index/tracked
inputs/caches stayed unchanged and dist empty. Lead accepted their exact path/
hash inventory as generated output separate from caches and authorized a fresh
remaining-phase resume with exact source/input/tool proof. No ignore edit or
cleanup, no repeat of the successful phases.

## First remaining-phase resume: successful release/full tests

Evidence `followups-verification-resume-090a188c-20261023T163855Z`, thread
`01a169a2-65ec-7db0-8c19-269af66a90a5`, passed release build and full make test.
It stopped only on a newly created PHPUnit result cache after test success.
The exact cache is separately inventoried; source/locks/69 docs/302 prior caches
remain unchanged and 12 artifacts are retained. Lead authorized a fresh05–08
resume with input/tool/full-graph/artifact proofs, without repeating passed phases.
