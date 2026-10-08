# Independent final review

Lead-recorded summary of reviewer0's completed report. Reviewed base/merge-base
`1b56616eff41e760327f3a0dbed8875e4aa9dbec` through exact
`18d8b4862a2523d629a534ea38d2ba92ef0209c8`. All five commits and the complete
diff were reviewed; the saved diff was byte-identical to Git's diff.

Reviewer0 verified the exact session binding/current, both markers absent;
retained thread `01a11a64-d84f-7bf0-a54b-c4727b0527f8`, review purpose,
`gpt-6.1-sol` / `xhigh` / read-only. No fallback/overrides/nested reviewers.
Overall risk high. All four mandatory lanes and their references were read.
No application or tracking edits, commits, pushes, builds or lifecycle action.

## Findings

No Blocking findings. Two Important and one Advisory:

1. **Important, risk/compatibility and general:**
   `lib/confctl/generation/build_list.rb:44` (runtime commit f76a8a89) resolves
   current from readlink's basename without checking the actual target. Broken
   `current -> missing-directory/G` or an external-directory target can select
   local G and permit implicit old/rotation. Read-only in-memory reproduction
   of the actual initializer produced nil current_error and allowed the guard.
   Validate the actual indexed local target, retain normal relative links and
   preserve invalid links/records/roots. Add a supported-basename broken-target
   regression covering selection and retention.
2. **Important, general and architecture:**
   `lib/confctl/module_options.rb:15` (Nix contract commit 138bbed3) matches the
   leading /nix/ of store paths. All 114 generated declarations are malformed,
   hash-bearing `<confctl/nix/store/H-source/nix/modules/...>` paths. Actual Option
   reproduction with different source hashes returned different false labels.
   Use an owning/bounded source-relative normalization rule, preserve user-owned
   declarations, regenerate manuals and verify stable correct declarations.
3. **Advisory, general:**
   `lib/confctl/cli/configuration.rb:240` (runtime commit f76a8a89) emits an optional
   vpsadminos channel attrset closed with ];. Uncommenting the emitted optional
   block failed actual `nix-instantiate --parse --expr` with unexpected ].
   Correct to }; and verify the example parses.

Lead accepts all three corrections. Implementer0 is assigned only narrow fixes.
No new design or expanded contract is intended. Direct inspection/focused checks
under mandatory-review steps 8-9 suffice; affected lanes must rerun if the fix
introduces a new design or expands a public contract. Do not start long checks
until Important findings have been reconciled.

## Lane conclusions

- General: pin subsystem/backends/cache/migration implementation deleted;
  stateless/init/help remain. Complete example preserves all 25 original flake
  paths, hidden/lock/nested/shell content; only README/configs/confctl differ.
  Four integration selectors and deployment coverage retained. Documentation
  explains deliberate break, v3 conversion, old roots and rollback assets.
- Architecture: one Nix backend and shared option evaluator provide root docs
  and cluster output. Reviewer compared the copy/activation/rollback/profile/
  shell/GC block to the base and found it unchanged. Flake mappings/metadata,
  no-write guards and retries retained. No additional ownership/duplication
  defect beyond declaration normalization.
- Scope: rejection inventory/current/numeric guards implement the accepted
  safety boundary without old readers/converters/cleanup. Existing NIX_PATH and
  developer-shell uses justify retention. No speculative framework, obsolete
  compatibility layer or unrelated application feature found.
- Risk: v3 flake keys, inputsInfo read spelling, links and root naming retained.
  Unsupported records untouched; explicit rejected/numeric ambiguous selection
  fails before host copy/activation. Remote profiles independent; new builds can
  replace current. Current-target validation is the remaining guard defect.
  Optional netboot metadata changed while boot/profile/kernel/revision paths
  remain. No coordinated all-node update required for this operator change.

## Representative consumer evidence

Reviewer inspected canonical cached origin/master refs, not foreign worktrees:

- vpsfree-cz-configuration `7e744b49ef90ba39d13b0f82a10a1f4c161c75f3`
  pins confctl `7bee58a52372b95c2198ce3f2a719807a3c2c66b`.
- vpsadminos-org-configuration `9438bfef7795f457669cbbdafe342f3a505e0a0b`
  pins confctl `af164b442100b92b8d93c0d67b315eff982e0180`.

Both use mkConfctlOutputs/mkConfigDevShell; vpsFree DNS/SSH-exporter consumers
use preserved confLib.getClusterMachines. This establishes actual source
consumers, not deployed versions or complete production inventory. Configuration
input/tool must update together for moduleOptions; operational inventory and
unknown third-party optional netboot readers remain deferred before rollout.

## Whole-branch history and migration conclusions

All five commits in branch-inventory.md were inspected in order. Split is
coherent: atomic runtime/loader removal; shared option provider/consumers;
example/fixtures; independent dependencies/CI; supported docs/reference.
Messages explain final behavior/rationale, no lines over 80 columns. No fixup,
tidy, superseded approach, obsolete unmerged protocol/schema, pin backend/adapter,
repeated dependency refresh or abandoned transitional design remains. Narrow
fixes should be folded into owning unpublished commits and docs regenerated.

**No migrations.** No new database conversion, persisted-state conversion,
schema version or intermediate branch format. Removed migration paths are the
already-merged v3 CLI. Tagged v3.0.0 base flake JSON is the supported predecessor
and rollback format. Historical v3 conversion guidance is not a new migration.
Only this local feature ref contained the reviewed head; no default/tag/remote
ref contained it. Recorded absence of deployment/release/external use is session
provenance, not a production audit. No unapplied intermediate schema needs
consolidation.

## Verification and limits

Reviewer inspected 58/0 full RSpec log and actual 114-option JSON with all seven
representatives/no pins, clean source/index and whitespace. Read-only independent
checks included declaration, initializer parser and in-memory current defect
reproductions, example tree and consumer/history comparisons. Did not rerun full
suite or launch builds/integration. Lint/syntax/format/hooks/generator successes
remain supplied evidence. Package/smoke/CI/integration, production inventory and
rollout are not certified. This review is complete with remediation required;
readiness/deployment approval is not claimed.

## Lead reconciliation

All three findings were implemented as requested and directly inspected under
skill steps 8-9. No new design/public output shape was introduced, so no reviewer
rerun is required. Actual realpath equality protects current; filesystem specs
cover broken and external same-basename targets, explicit current/old/rotation
refusal, byte/symlink/GC-root preservation, and valid relative/absolute links.
The anchored root/store-component rule is bounded to the confctl/cluster owned
module namespaces, including directory declarations; custom/upstream/foreign
paths stay intact. Source-hash regressions pass. Only the init closing delimiter
changed, and the actual generated optional block parsed with nixfmt.

Parent full RSpec after corrections: 66 examples, 0 failures, 22.96 seconds.
Focused member regression/parser checks: 27/0, five Ruby lint/syntax checks passed.
Parent regenerated both manuals, checked all 114 declarations against existing
repository files/directories with no store-hash labels, and verified a second
render's SHA256 was identical. Five remediation source hashes stayed unchanged
through the parent checks. Corrections were folded into the owning unpublished commits; final
inventory/range-diff records the exact new head.

Final folded head `3be154b5f86125146e444d5fb6aa60916e99b77d`; five units retained. Parent checked exact
reviewed-to-final six-file delta and source/reference hashes after fold. Units3/4
patch-identical; units1/2/5 differ only by accepted corrections. Full corrected
tree is unchanged through folding. Final inventory/range-diff records the series;
no migration or design change appeared. Long verification now assigned to a fresh
Luna/low utility watcher, not the retained reviewer.

## Scoped committed revision review at cc40679d

Reviewer0 completed affected general-lane review at exact
`cc40679d267165aecfa569128438bb55fe910268`, base `1b56616`:
retained thread 01a11a64-d84f-7bf0-a54b-c4727b0527f8,
gpt-6.1-sol/xhigh/read_only, no overrides or fallback. No Blocking or Important
findings and no application finding. The two explicit fixture path arguments
address the observed pre-Git lock failure without changing assertions, setup
order, lock cleanup, later Git workflows or public/runtime/state contracts.
Unaffected architecture, scope and risk conclusions remain applicable.

Advisory: the inventory's publication paragraph and d2adc4f0 tree needed explicit
historical labels. Lead corrected them to identify the prior 3be series and
prior remediation tree. Current tree is 08f33e1fe5613f7634ba69b38535fb3c35a3c0c9.

Reviewer independently reproduced complete final diff, exact two-line delta
and five-unit range-diff, all byte-identical to packet artifacts. Whole-history
conclusion: coherent five units, fixes folded into owners, no obsolete approach,
fixup sequence, unused compatibility path or transitional migration. No
migrations. Previously published 3be consumption is unknown; the correction
rewrites no API/schema/state behavior. Full quick logs 66/0 and95-file lint
passed. Two failed-suite retries and final-head CI remain outstanding; prior
rollback3/3 and carrier/deploy8/8 cover unchanged code. Review permits proceeding
to verification and makes no rollout/readiness claim.
