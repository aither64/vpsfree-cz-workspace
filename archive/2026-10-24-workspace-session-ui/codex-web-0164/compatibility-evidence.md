# Frozen Codex 0.164 dependency preparation

Status: source preparation only; not reviewed or native-isolation accepted.
Session identity is `2026-10-24-workspace-session-ui`, implementer0.

## Exact inputs

- codex-web canonical base: `8b60554bc10c2a6bcbf9732a8b77ad959c317036`.
  The SQLite submission/delivery baseline is retained. No production source,
  protocol call site or catalog byte change has been demonstrated necessary.
- Frozen llm-agents: `ea188d2f072e0ec8d5b71245e228803672801a22`.
- Codex release: `0.164.0`; tag object
  `fe3b29455488c2e189e43ad5526a107900c5e1b7`, peeled upstream source
  `6aaac694803004a63c6f393d153c96d22521a6b9`.
- Native prerequisite: `/nix/store/16f481b2zzvyvr2ycw51sm51b3f0508f-codex-0.164.0/libexec/codex/bin/codex`;
  SHA-256 `d2af1cd0ea4187d413c237e80204e94ffcd5c7d8142840a662156b89750f54ae`.
  Deriver: `/nix/store/w0byl70npn8n740k0cqv0nca24kakn6i-codex-0.164.0.drv`.
  Parent watcher realized and rooted it; this owner did not rebuild it.
- Exact source: `/nix/store/10pdz4z8bfg35ysd7aqrhnzdkijpmmwb-source/codex-rs`.
  Source NAR `sha256-iib2+qQcGewC4Ga8cA80sInDJpzdSxDJP0y1DDOouI4=`.
  Config schema SHA-256 `ea611ee3f12a6df314b3e49585015ec6e2ebc7c3f072ccbf63c21306a4cdb5dc`.
- Exact recipe: `/nix/store/dyw4sx7rn0bhj9kyb3s1r58vsmh9vwj8-source/packages/codex/package.nix`,
  SHA-256 `b361fc99ac33a98519dbde0a18656338d2e161fb1e9997a7e3e9e6e346f937df`.
  Applied daemon patch SHA-256 `5956d86812387d67a377a853e1939f90f4fdf886440ed80b2326e43c99d4cc1a`.
  The patch and substitutions touch only daemon `prepare_install.rs`; postPatch
  also raises the chatgpt crate recursion limit if absent. Cargo patches are
  empty at 0.164; the older-version webpki patch is not applied. preBuild only
  changes compilation flags. These declared changes do not alter schema,
  catalog or tool-router sources. This is prerequisite provenance, not final
  mkCodexPackage assembly or running-daemon equality proof.

The parent raw realization/derivation/input receipts and output roots remain in
`../native0164-prerequisite/`; compact parent watcher reports are one directory
above this evidence. No private credential/config state was copied.

## Executed bounded checks

Exact native `app-server generate-json-schema --experimental` completed with
an owned private probe home and absolute output path. No service/inference was
started. `schema-manifest.json` binds all 458 generated JSON files.

- Exact generated-schema request corpus/client consumed-shape contract: PASS.
- Fixed config policy against exact release config schema: PASS, 55 fixed
  restrictions plus literal configured MCP disabling.
- Request-corpus call-site coverage: PASS.
- Catalog refresh helper: PASS; full source bytes and three-field Luna
  transformation are byte-identical to 0.163. Only the provenance version
  changes. Full: 472072 bytes, SHA-256
  `943ca7fe1d19ed019054158303f0dbbd80b3bef43b3aa425a71aa7cb3fb52c2b`.
  Luna: 62680 bytes, SHA-256
  `049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1`.
- All declared Node browser contracts: 109 tests PASS, no skipped tests;
  `browser-quick.log` records the result (about 1.8 seconds).
- Browser module syntax: PASS.
- gofmt and Git whitespace checks: PASS for current owned edits.
- No declared hook framework; core.hooksPath is unset.

## Bounded source comparison and unresolved gate

`selected-upstream-identities.json` binds 16 selected old/new source files;
`selected-upstream-delta.diff` preserves their deltas. The old source is
`/nix/store/9is267xl3palxb615kk86qlli9nggkf9-source/codex-rs`.
`upstream-state-migration-delta.json` is empty: all state migration SQL paths and
bytes match, although SQLite connection/retention and native behavior change.
This does not establish old-reader or write compatibility.

Base instructions still use a developer prefix; current logger table DDL is
unchanged. New log routing uses explicit log_dir only when no managed sqlite_home
applies. The isolation fixture sets neither log_dir nor inherited SQLite env,
so root logs_2.sqlite remains its exact acceptance boundary. Its strict schema,
unknown/nested-file and non-logger marker checks remain unchanged.

Material tool exposure concern sent to lead and architect: new
core/src/tools/spec_plan.rs:1409 registers ApplyPatchHandler whenever the catalog
selects it; the previous execution-environment gate was removed. Both pinned
profiles retain freeform apply_patch metadata. Default Direct exposure flows
through registry and model-visible-spec construction without an empty-environment
filter. ToolPolicy permits by default; only guardian startup uses a special
ceiling. The handler later resolves an execution environment, but a dispatch
error does not satisfy the required empty exposure/native registry rejection.
RequestPermissionsTool also loses its environment gate; current fixed policy
does not disable that inherited feature explicitly. No native behavior was
observed for this concern. No policy/catalog/restriction changes or weakened
assertions are authorized or implemented pending architect disposition.

## Deferred acceptance

Implementer3 handed back only `codex/native_upgrade_integration_test.go`,
SHA-256 `9eaff2784a5b9c420aed201bfb397c3c6bf3b28086ad181a21d172c5d9c1da32`.
Owner0 retains serialized Git/fold ownership. The parent launched the two-command
non-native Go/compile quick batch as outer18699; owner0 does not observe or
duplicate it. `go-quick-inputs.json` binds 80 Go/testdata/mod/sum inputs, SHA-256
`510d0633b62a483bc759e4dbcdba23fef0193639aa6948893fcff9c3971cd728`.
These inputs remain frozen pending the parent result. The new fixture hashes the
raw prerequisite; if the architect selects a native restoration patch, a bounded
exact new-binary hash refresh is required after an actual patched receipt. After all intended changes are
committed and affected final independent review is accepted, fresh watchers must
run namespace ownership, both-profile hostile dispatch, two-binary state upgrade
and old-reader evidence. Final consumer assembly, daemon executable/launch identity,
shared-home idle cutover, system/profile activation and default integration are
outside this dependency preparation. No native campaign, activation, claim,
cleanup or lifecycle action has been performed here.

## First Go quick batch environment failure and corrected runner

Parent watcher outer18699 completed with exit 1 before tests: runtime/cgo could
not find gcc in PATH. The second helper/compile command did not run. All 80
input hashes matched. Original go-ephemeral-quick.log/.exit and watcher result
files are retained unchanged. An absolute Nix Go executable identifies Go but
does not enter stdenv or supply its compiler wrapper and link flags.

Read-only evaluation of the unchanged locked flake selected nixpkgs
6aefcda9401be8acc2b74244fb3b37520ea1f0a8, Go 1.26.7, GCC wrapper 15.2.0
(/nix/store/hbsz2ngi9ixbhd9na1xagh2yc8qnmj7y-gcc-wrapper-15.2.0), and stdenv
/nix/store/99v98l4khhp1yib367g1bxgx8frmp9hs-stdenv-linux. The compiler wrapper
is already executable. The declared package derivation is
/nix/store/3mymyhggwhcndh677pk501cndhy33hr4-codex-web-checks-0.0.0.drv.
Its environment explicitly uses CGO_ENABLED=1, GOTOOLCHAIN=local, GO111MODULE=on
and GOFLAGS=-mod=vendor -trimpath. The two focused commands explicitly select
-mod=readonly; this retains checked module files without needing a vendor copy.
No source, SQLite, dependency or CGO-disabling workaround is made.

run-go-quick-nix-v2.sh enters the explicit package derivation through
nix develop --no-update-lock-file .#packages.x86_64-linux.default, retaining
stdenv setup and PATH, then explicitly selects the same declared Go/CC/CXX and
CGO_ENABLED=1. It verifies the original manifest and both flake file hashes
before/after the same two commands, refuses existing v2 receipts and stops at
the first failure. It records bounded toolchain metadata and separate fresh
logs/exits. bash -n PASS only; the script and tests were NOT launched here.
The parent owns any Nix environment realization and the fresh watcher batch.
Read-only Nix evaluations completed; no own operation remains running.

## Corrected non-native Go quick batch result

Parent watcher outer98463 completed the exact corrected v2 runner once, exit 0,
about 29 seconds. The original 80-file manifest and both flake hashes matched
before and after. Exact scope:

1. `go test -mod=readonly ./codex -run '^TestEphemeral' -count=1 -timeout=60s`:
   PASS, exit 0, 12 seconds. These are the untagged fake-transport/client tests.
2. `go test -mod=readonly -tags=codex_integration ./codex -run
   '^TestNativeStateUpgradeFixtureHelpers$' -count=1 -timeout=60s`:
   PASS, exit 0, 7 seconds. This compiles tagged source and runs only the new
   file/hash/offline-snapshot helper test. It does not execute the two-binary
   upgrade test, native App Server, utility protocol or namespace integration.

The parent report is `../codex-web0164-quick-v2-watcher-result.md`; fresh receipts
are `go-nix-env-v2.log`, `go-ephemeral-nix-v2.log/.exit`,
`go-upgrade-helpers-nix-v2.log/.exit` and `go-quick-nix-v2.batch.exit`. The earlier
missing-gcc failure and its diagnosis remain retained. No process remains.

The parent released the Go freeze for concrete follow-up only. No native
restoration patch is authorized, no source follow-up is implemented here, and
coherent commit/publication remains held pending the accepted compatibility
route. These quick results do not establish Codex 0.164 native isolation or
state compatibility. Any native restoration changing executable bytes needs
new exact-binary provenance and applicable quick checks before the final packet.

## User disposition: raw 0.164 and naming-specific prompt control

The lead relayed the user's explicit rejection of a Codex patch and acceptance
of prompt-controlled tools for naming. Raw frozen EA 0.164, native SHA-256
`d2af1cd0ea4187d413c237e80204e94ffcd5c7d8142840a662156b89750f54ae`, remains
the intended executable. No custom native patch or build is authorized. The
empty-environment restoration artifact above is a retained rejected proposal,
not implemented behavior or a current execution plan.

The user directed takeover of canonical 2026-10-20 workspace session naming
source into the current branch and explicitly selected Codex 0.164. Architect
owns the revised canonical-source/API/naming design and file handoffs. Naming
prompt control does not silently relax the reusable strict utility API, its
empty-tool assertions, or native acceptance claims. Source, fixture support
labels and final docs wait for the revised intended package.

No source, Git history, native process, publication or commit action followed
this disposition. Prepared schemas/catalog identities, exact quick PASS, state
fixture and failed-run evidence remain intact. No foreign session records,
worktree or team is accessed for the takeover by this owner.
