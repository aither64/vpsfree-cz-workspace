# Final affected review: preserve packaged status during incident-policy rollout

Requested outcome: deliver the already-approved policy selector/profile and a preserved
demo services update loading sole OOM3/10, while retaining historical report22/eval20
5/10 and data. The current ca7/c087 profile has successfully deployed; before any demo
mutation, ordinary evaluation found floating status f783 -> 561. The smallest supported
correction pins the existing packaged fallback to f783. A local status checkout would
also select the local Go SDK and does not preserve the old composition.

All intended source changes are committed, quick checks completed, and both source
windows frozen. Owner2 may finish independent no-realization preparation. This is final
source/history review before any new long checks, not live acceptance or merge approval.

## Exact complete ranges and history

- Extension worktree: worktrees/2026-10-30-oomd-abuse-policy/vpsfree-dev-workspace.
  Base d76bd681c6db981907a52c187a3298549af87ab0; final
  bf12ac71a8a00b1581eed5352f99c1b2daaeff5b/tree7367dbf2769b706b4f0721c76c565117af59929b.
  Complete two-commit series: ca7d8bdf982ef459fe4e09ac3740e0ea2edfcc36 (incident policy
  selector), bf12ac71 (packaged status fallback). Full diff review-extension-full.patch:
  four files +188/-6. Affected successor delta is ONE URL line in dev-clusters/vpsadmin/flake.nix.
- Workspace worktree: worktrees/2026-10-30-oomd-abuse-policy/workspace.
  Base f6bcb4c4d7c4d3275657734bebc28e763e11a52a; final
  5c9d99dc72c0e4263d7e8d13806b200713a78c46/tree871f5dedc838acc1d20f976968a19745352acd63,
  branch2026-11-23-incident-policy-status-fallback. Complete two-commit series:
  dfe37fa914b42913e8bf8803b4da749a4a61795c (final consumer pin),
  5c9d99dc (unchanged instruction relocation). Full diff review-workspace-full.patch:
  four files +71/-61. Delta from deployed c087 is only flake.nix/generated flake.lock.

Root independently observed both clean source/index states and full commit lists/diffstats.
The repeated consumer extension-pin stream is consolidated in the final pin commit.
Published/deployed c087 is retained on its old Nov22 feature and preservation refs;
new 5c9 is NOT its descendant and is not wholly patch-equivalent (the extension pin
intentionally changes). A new verified deployment is still required. No default rewrite.
Extension selector and status fallback are separate owning purposes/streams. The root
smoke-fixture status587cd65/lock remain unchanged. No migrations in either source range;
no new schema or persisted-format change. Do not generalize this to inherited runtime.
Assess whole-range consolidation/migration conclusions explicitly.

## Scope, documentation and compatibility

Only the existing provider fallback URL selects exact
f783d045ac49a0ae9e8501a8f9a38d0523177b9e. Local-source precedence, API/OS/nixpkgs follows,
incidentPolicyFile snapshot/three-consumer wiring, fixture inputs and all other extension
source remain byte-unchanged. No new selector, config field, status checkout, SDK change,
private override, compatibility layer, test/threshold change or new lockfile.
Workspace retains all37 other lock nodes/edges/follows and current generic0abe,
codex-web3209/Pia22, host/native/site/team/settings, plus byte-identical c087 instruction
files. No host upgrade or demo data mutation. Ordinary forward profile activation and
retained start/services-only update retain their original ownership/admission/recovery.

Authoritative existing provider behavior/operator guidance: extension
 dev-clusters/vpsadmin/README.md; unchanged by bf12. Exact pin rationale is in its normal
commit body and design.md Nov23 top brief. One rollout's evidence belongs in this session.
Workspace instruction routing is unchanged from independently reviewed c087/ecefa.
No new reusable operator procedure or prose was needed for one exact input pin.
Give explicit documentation placement/preservation and all applicable seven-question
conclusions, reusing prior independent conclusions only for exact unchanged content.

## Quick evidence and limits

- Extension ../../nov23-status-pin/handoff.md and receipt.json SHA256
  6224a02d4fdd6020c49609f0907c54d3a1afca868bc95004f2b3c741a73fa282;
  root verified all166 artifact bindings. Nix/Ruby syntax, diffcheck and existing
  projection-only smoke pass. Actual ordinary provider-as-parent observation matches
  exact historical status drv yz96/outputv8l/modules sp5l/source3y96/versionf783d04,
  empty postPatch/vendorHashphYd/released client0.2.0. f783/NARKstS exact.
  Direct-root versiondirty failure and later evidence sourceInfo TypeError remain
  literal native1/utilityFAILED/CLI0; successful parent Nix eval was parsed offline,
  then only pending metadata/graph/dryrun ran. No source workaround or realization.
- Consumer final-source.json, checked-inputs.json, quick-results.json,
  instruction-test-reuse.json, commit-results.json/publication-results.json and logs
  are here. Diffcheck0; own immutable58c host-contract0/0.252s; no-build flake check
  0/30.231s only evaluates checks. All instruction test/read inputs exactc087;
  retain actual Ruby10/219 PASS without claiming a rerun. Normal hooks/commits,
  no declared hooks/framework or bypass. Source/publication observations are exact,
  finite CI inventory0runs is not CI success. Old c087/defaultf6b remain unchanged.
- New long checks and candidate have NOT run. Extension prepared9roots/5597graph,
  5585common full recipes identical,12new. Dryrun28builds includes unchanged old-generic
  shards now absent from cache; original ca7 3533s result remains historical.
  Architect2c6efc2c is assessing only the smallest valid required verification scope
  under actual consumer0abe versus restoring old generic outputs. This does not
  alter source or waive required checks. Owner2 actual current-input8target prep is
  independent. No new full runtime PASS, source-cache equivalence or live3/10 claim.

## Requested independent review

Retained reviewer0 Sol/xhigh/read_only; live roster44 reverified; independent.
Overall HIGH due deployment/package composition and preserved-state recovery.
Read mandatory-change-review skill and all FOUR lane references: GENERAL,
ARCHITECTURE/REPETITION, SCOPE/PROPORTIONALITY, RISK/COMPATIBILITY. Inspect actual
committed ranges and affected pin/reuse/packaged-input boundary. Previous 7a4f1718
and f49ca72c reviews retain unaffected exact architecture/instruction conclusions,
not a new operational result. No nested reviewer, source mutation, tests, build,
restoration, live probes or remote mutation. Return concrete findings/severity,
whole-history/update-stream/migration and documentation conclusions, review settings,
residual verification limits and capacity. Source review grants no switch/merge/lifecycle.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/
