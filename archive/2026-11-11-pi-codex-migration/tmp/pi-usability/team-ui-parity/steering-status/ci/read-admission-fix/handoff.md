# Read-admission fix: committed source handoff

Exact isolated branch `2026-11-11-pi-codex-migration-pi-read-admission-fix`:
`741c1df06ef3c43c60dd52e7d1ac6be007aa0516`, tree
`f1447b798533ca6354133b956338527c68b40b04`, literal R42 parent
`42acdec08d4f24ea38574ef0a93c3beec3bad56a`. Clean/index empty; all effects joined.
No publication or long check. Main owns composition, review invocation and delivery.

The resolver retains shared runtime/package-transition admission through initial
Verify. A separate adapter field consumes that grant once under a mutex shared
with abandonment cleanup. Its checks use the Verify context, including a final
cancellation check. The stored lease supplies only idempotent close; initial
verification never calls mutation lease.run. Later read/page/activity/subscription
admission and mutation/ACK/receipt paths retain their existing behavior and budgets.

Scope is three files: pi_workflows.go, its existing owning test, and the exact
main-authored pi-runtime.md paragraph (line wrapping only). No module, native,
wire, schema, provider, timeout, retry, generic HTTP-error or plan change. Owner1's
plan constructor/render hunks are isolated; main must reconcile after both releases.

## Verification and original evidence

Declared Nix environment is the retained R-focused-env.nix, SHA
1dd7e14061161a808af46380fda58ffea6c70d97aee5a833bacd2e948c927e7a.
Every Go invocation used literal isolated portal cwd and -mod=readonly.
Exact argv/input hashes/log hashes/joins are in each *-result.json.

- pre-fix-result.json: expected failure on literal42 production, 36.495s /
  package1.315s: writer acquired the released gap and initial Verify hit its60ms
  deadline. The original early fixture revision differs from final; its exact
  early source bytes were not separately exported by that original receipt.
- fixed-batch-result.json:32.289s / package7.623s, exit1. Four unchanged owning
  selectors passed: follow-up scoped canonical/alias HTTP controls, invalidation
  ACK, post-runtime-wait generation recheck, and scope transport preconditions.
  Nine of ten new real-lock/release/cancel/abandonment/SSE controls passed. The
  stale-authority fixture mistakenly wrote the existing8 generation; this is the
  sole unexpected failure. Original receipt/log retained unchanged.
- stale-authority-result.json:26.264s / package1.149s, exit0 after changing only that
  fixture to distinct9 and asserting the generations differ; sole failed subtest.
- finite-channel-result.json:25.134s / package1.244s, exit0. Only two previously
  green channel controls were rerun after bounding their future failure waits.
  No production change after the original fixed batch. All other passed scopes
  retain their original stage; no whole-batch replay.
- Declared-Nix gofmt cleanliness and git diff --check passed before normal commit.
  No hook framework is declared; configured Git hooks directory contains samples
  only. Normal Git commit exit0, no bypass. Commit-result.json proves staged patch
  equals final committed patch and tested/current/committed source hashes match.

The expanded existing lock fixture uses real disposable transition/runtime locks,
queued exclusive admission, actual BindRead, C invalid-target cleanup, double
Release, consumed-grant refusal, cancellation before/during verification, verifier
error, stale authority and subscription lifetime/fresh-admission checks. Original
mutation detached-context/identity/lock assertions remain. Ensure/Create/Send stay
1/1/1. The scoped follow-up control is synthetic browser/source consumption, not a
new native or hydrated-browser proof.

Original CI creation-failed.log SHA
be8967c51b148aae8b8fe25d1afe9fb8bf6244f718b23d3b7a045105de0b9c2b remains
unchanged. It proves Verify timeout and a concurrent pending POST, not the exact
exclusive holder/stage. This deterministic regression proves the source defect,
not a reconstruction of original scheduling. Existing session-creation VM/CI on
final composed/reviewed source remains required; no local native/VM/CI run here.
An initial edit helper used a repository-relative path from portal and failed
before writing; corrected cwd/path only. Formatting and all child handles joined.

## History, compatibility and documentation

full-series.txt/full.patch export complete9241-to-head117 history and binary diff.
history-proof.json proves all116 R42 prefix commits unchanged, plus one focused
append. No obsolete intermediate commits or repeated pin stream were introduced.
Whole R remains migration-bearing: inherited59/60/74/81/F state lineage and deployed
8fe boundary, consumed39ed/C1993 and current pinnedC0bf provenance are retained.
The accepted delivery42 candidate packet is referenced by exact hash in that proof;
retain its earlier complete history/migration and consumer inventories. No ancestor
was rewritten. This append has no migration; rollback keeps formats loadable but
restores the race. Original held/unknown operations remain untouched.

Documentation routing: read-admission lifetime → runtime developers/reference →
docs/pi-runtime.md, already linked by README → implementation and real-lock tests.
The accepted main paragraph is preserved, existing warnings unchanged. Individual
CI/check evidence stays here. General, Architecture, Scope and Risk lanes are
appropriate for main's independent review; overall inherited HIGH risk retained.
Reviewer must independently conclude complete history/migration/stream disposition.

All code/index/check/commit effects are joined and whole isolated source/index is
released. OriginalR42, isolated plan worktree, W/H/C and shared master were not
mutated. No source push, pins, CI/network observation, activation, target/native/
provider/session/lifecycle action occurred. Provisional installed-plan helper final
binding remains parked separately on owner1 source/main disposition.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
