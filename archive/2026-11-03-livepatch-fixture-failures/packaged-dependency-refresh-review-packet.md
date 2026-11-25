# Packaged dependency baseline refresh: affected committed review

Repository vpsfreecz/vpsadminos, SSH git@github.com:vpsfreecz/vpsadminos.git.
Session 2026-11-03-livepatch-fixture-failures. Worktree
worktrees/2026-11-03-livepatch-fixture-failures/vpsadminos.
Final range 2951a632c4254a44747a8da326e3dde897eaa0e2..e1751c917f216897292ab0b893727a6e5553a540.
Retained reviewed range 54b4313404cea35b58ebb9df951ae75e27c44971..dc74bcdadef75f181934bad2178afb589c34644c.
All intended source committed; A reports clean index/worktree/nonignored-untracked,
Git ownership released, finite checks terminal and passing. No publication yet.

## Scope, decisions and affected boundary

User authorized qualification of the current normal module with nine meaningful
semantic witnesses, fixed predecessors/boot and recovery. Rejected freeze,
blind repin and historical-only witness lane. Conditional vpsadminos -> staging
merge approval requires accepted full exact-final-head CI. No merge now.

The reviewed two-purpose implementation is unchanged. The canonical incoming
baseline is ONE commit2951, `os: update packaged gem dependencies`, two files
+3/-3: os/packages/osctl-env-exec/Gemfile.lock and gemset.nix, rake-compiler
1.3.2 -> 1.3.3 with its paired hash. No twenty-feature-file overlap. The
conditional initial refresh correctly stopped because this is a packaged lock,
then architect defined the current bounded package in implementation-plan.md,
section Packaged dependency refresh onto 2951a63, with rationale in design.md.

The bundlerApp uses this separate bootstrap bundle. Source-gem configuration
uses the whole repository for osctl/osctld and other local gems, so those guest
build inputs may change even without a direct pkgs.osctl-env-exec guest reference.
Channel copies os/ for enabled QEMU/ISO paths; test default differs. Captured
source revision also changes. Therefore do not claim whole guest/test closure
equality or transfer old-head runtime CI. No public API, production state,
protocol, migration or coordinated fleet update introduced by the feature refresh.

Review only this actual baseline interaction, evidence reuse and complete final
history. Reuse osvm-boot-evidence-review.md, source-identity-refresh-review.md and
the earlier review/reconciliation chain for unchanged source bodies; no repeated
unrelated twenty-file audit. All four adaptive lanes remain applicable overall,
restricted to the affected scope. Retained reviewer0 Sol/xhigh/read_only, unchanged
settings, independent; no nested reviewer or source/session writes.

## Complete final history and provenance

1. 8169b8189c29f471b2ecf27a33b6f71dbde5e70e — tests/livepatch: qualify current module probe sites.
2. e1751c917f216897292ab0b893727a6e5553a540 — osvm: record bounded host evidence for boot failures.

Two purposes remain independently meaningful; full feature range twenty paths
+2923/-184. A reports ordinary conflict-free Bundler-activated rebase; both
ordered patch IDs, raw messages and all twenty modes/blobs/inventory equal old
reviewed range; range-diff '=' for both. Complete old/new tree delta is exactly
the incoming paired bootstrap lock/gemset. Confirm independently.
No feature dependency update streams, obsolete fixes or migrations. Incoming
canonical dependency commit remains baseline history, not an unmerged feature
update to consolidate. No deployed/external intermediate or migration lineage.
Seven exact local provenance backups retained, including reviewed-dc74bcda;
detached old5235 debug source retained. No backup publication/removal.

## Checks, identities and reuse

A's package-a-2951-equivalence.log and package-a-2951-checks.log retain exact
history, commands, bundle bindings, hooks and hashes. Both current evaluations
were IFD-disabled and evaluation-only; no build/realization/gem regeneration.

- package-a-2951-livepatch-identity.json: exactly ten fields, every drvPath,
  outputPath and module value structurally equal package-a-osvm-identity.json.
  Normal qi47 module, aiqijl sites, resolver5nps, controls94hk and frozen SDK,
  compiler/config/corrected inputs unchanged. Realized module SHA
  7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f;
  sites SHA093cf255a38db5275b62370da8bac1297781e48e2ae3245c1c5b5e1ceeb23ed1,
  schema1/module binding matches. Supports only matching artifact evidence reuse.
- package-a-2951-package-identity.json: exactly four requested drv/output pairs
  for osctlEnvExec, osctl, osctld, testRunner on actual refreshed head. No old
  comparison invented where none was recorded; no new gem-byte/closure pass.
- Declared Bundler-activated Overcommit Diff: Nixfmt/RuboCop pass; whitespace pass.
  Both original messages unchanged; ordinary rebase hooks enabled, no bypass.
- D81 focused/207 full OSVM and A99 integration successes reused, not rerun or
  relabeled as new-head executions. A compared actual loaded source/specs,
  runner/libosctl/OSVM, owning framework and Bundler inputs, exact Ruby3.4.11,
  native givmi path, Bundler4.0.23/RSpec3.13.6 and local loaded class paths.
  Main lockSHA604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa;
  test-runner lockSHA10cc972d84899008e01de673d812f14827493520037b64e22ab7f30f3356a744.
  Incoming bootstrap lock is separate from the unit bundle. Inspect actual
  bindings; tree equality alone is insufficient for verification reuse.
- Prior standalone metadata evals only retain unchanged code/locked-input scope.
  No broad environment realization, 9-minute ELF repeat, compile or VM.

Technical behavior docs remain unchanged because feature behavior is unchanged;
individual refresh status belongs in package-a-result.md/verification-launch.md,
plan/state and this packet. Existing near-code OSVM privacy/budget invariants and
docs/os/testing.md keep their owning explanations; no new product docs needed.

## Required disposition and limits

Return findings ordered by severity, exact final range, affected baseline/consumer
conclusions, evidence limits and explicit whole-series history, repeated-stream
and no-migrations conclusions. Use saved independent settings and mandatory
skill/all applicable lane references/current workspace/repo guidance. No source
or session write, eval/build/VM, Git mutation, CI polling/fetch/cancel/retry,
push/merge/deploy/lifecycle. Return complete report through report_to_lead for
root to save packaged-dependency-refresh-review.md.

Old original5235 CI41773470432 remains owned by sole native utility, not a new
head check. Old native41811208607's shared cgv1 firmware-only boot stall remains
unclassified/unwaived. New OSVM observation does not fix or explain it. Actual
old5235 updated-image device tests pass, but all final-head native and nine
lifecycle/witness/boot/recovery acceptance remain required. Review success
permits publication/CI only. Keep the session open.
