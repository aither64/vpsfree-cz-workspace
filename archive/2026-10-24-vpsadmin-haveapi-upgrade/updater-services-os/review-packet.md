# Services-only applied OS selection correction

Status: final review accepted by lead (reviewer0 native01a18ed0, all four HIGH lanes, no findings, complete history and NO MIGRATIONS). Exact feature publication and independent SSH readback passed; [publication receipt](publication.json). Postreview flake check and the retained-output installed-flake/runner retry passed; [final result and limits](postreview-receipt.md). No activation or live retry is authorized.

Head: `acc495827de81cce0fa7a7cf3f34e9f15c9516b1`, tree `c3fb82f170a9757d5c5e0928cc3381ba90233bdd`.
Complete base-to-head range is one commit; [history](history.txt), [final diff](final.diff), [inventory](final-inventory.json), [effects](final-effects.json).

Repository: `git@github.com:vpsfreecz/dev-workspace.git` (`vpsfree-dev-workspace`).
Worktree: `worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsfree-dev-workspace-services-os`.
Branch: `2026-10-24-vpsadmin-haveapi-upgrade-services-os`.
Base: `767dfd587e346168e1443e65ccdb67ce748f3fe3`, tree `80181fb9f3805e99734b85edfdbcdd022f5e4b67`.
Design: [accepted E0 brief](../design.md#2026-10-30-services-only-applied-os-selection-correction-e0).
Plan/state: [plan](../plan.md), [state](../state.md).

## Requested behavior and boundary

Ordinary services-only update must use the immutable OS source in the validated old applied configuration for both OS overrides and the identical shared-source mount. Mutable staging and an optional OS checkout must not select a different OS. The internal projection requires services provenance, equal source paths across all machine descriptors, an available store directory with readable flake files, and nil pending or exactly an update of services. A same-target retry uses the old configuration, never the pending candidate. Missing or unproved selections refuse before credentials/build/root publication. No complete provenance requirement is imposed on unrelated machines.

The retained path is content authority; its Git revision stays unknown/empty and dirty is zero. No Git command targets a store source. Strict layout, ownership, generation, credential, copy/activation, pending and promotion checks remain. Start, other/default targets and maintenance copy-only retain their selection paths. A direct copy-only regression checks its original missing-maintenance-hold refusal without an applied selection.

Owning files are exactly the provider command, maintenance projection, provider README and their two existing test files. The README contains the lead's settled operator explanation. There is no runtime or state-schema change, new public option, credential copy, OS upgrade, generic-runtime edit, logging framework or new dependency.

## Verification and original failures

- Declared environment: `nix develop .#checks.x86_64-linux.tests`, pinned Ruby 3.4.9, ordinary cleared Ruby/Bundler variables and `Gem.default_dir` as declared by the flake. Retained runtime contract SHA256 `6c99ec97e8650a4a511b719d0d9e7c1bcf24d5f7973b6f913ad730430e059fa3`.
- Initial shell setup could not load minitest/mock before assertions; preserved in `attempt-1/`. The declared gem environment corrected it.
- Final maintenance suite: 36 tests / 283 assertions / zero failures, errors or skips, exit 0, 2.545s; [log](maintenance-final.log). Rerun after the diagnostic-emission fix; includes unchanged node provenance and strict mount-layout checks.
- Original full command attempt: deliberately interrupted on lead instruction after 29 tests / 315 assertions / one failure, exit 1, incomplete. Retained in `attempt-2/`; this is not a full-suite success. One verified pidfd SIGINT, all known runner and fixture identities gone; [effects](partial-command-effects.json).
- Unchanged failing case alone: 1 test / 7 assertions / one failure, exit 1. Domain refusal and no-WebUI-credentials checks passed; only the old empty-events assertion failed on five legitimate applied-payload root registrations. The corrected assertion permits exactly those five event/item pairs and no other effects; it preserves every refusal check.
- Focused intermediate batch: 11 methods / 188 assertions / one failure, exit 1, 256.506s, [retained log](focused-attempt-1/focused.log). The new refusal test exposed two concrete diagnostic issues: the command fixture's `$VERBOSE=nil` suppressed all `warn` output, while the real CLI's outer rescue replaced the approved projection error with generic text. The fixture now uses normal `$VERBOSE=false`; only the new projection action emits its wrapped `Invalid` message. Other actions and unexpected exception classes retain the existing generic behavior.
- Final affected command selection: **6 tests / 147 assertions / zero failures, errors or skips, exit 0**, 71.238s; [log](commands-final.log), [exact final source hashes/methods](final-inputs.json). Covers all nine refusal variants, old-applied pending retry, both overrides/mount during moving staging/worktree, invalid-domain rejection with exactly permitted roots, copy-only maintenance refusal and generic existing maintenance guards.
- Six unaffected passing command methods are retained from the completed intermediate batch: start/default/node selection; credential generation failure; invalid credential bundles; failed-build result/runner safety; stable credential bytes/modes and source labels; failed copy/activation sequencing. Their relevant behavior is unchanged by the narrow diagnostic correction. This is explicitly bounded quick evidence, not a final full-suite success or Nix-result reuse.
- Bash/Ruby syntax and diff whitespace checks passed with the final subset; [batch log](final-quick.log), [exit 0](final-quick-exit.txt). No declared hook framework or active Git hooks exist; [hook inventory](worktree-hooks.json), [fresh precommit guard](precommit-guard.json). Ordinary `git commit -F` completed with no bypass; [commit output](commit.log). Final file hashes match the tested source and Git tree; all 107 other tracked entries have exact base/head equality.

The full command suite now contains 49 methods and remains required in the ordinary postreview flake check. `nix flake check --print-build-logs` and `nix run .#devcluster-check` remain deferred until accepted review. All owned quick commands ended and the source is clean; original logs, private control evidence and roots are preserved. No VM, real cluster retry, package activation or live query was performed. The pinned840 watcher configuration remains unavailable; the existing visible owner-monitor fallback was used without substitution.

## History, compatibility and review request

Final history is exactly one coherent commit, `acc495827de81cce0fa7a7cf3f34e9f15c9516b1` (`devcluster: preserve the applied OS source for services updates`), above exact767dfd5. The complete final diff is 5 paths, +346/-22. No fixup or interim commit exists. Implementation, regression tests and the operator explanation describe the same behavior and belong together. No dependency/channel/generated-artifact update stream or superseded development commit is retained. **NO MIGRATIONS**: no persisted-format/schema change or migration versions; old packages can still read existing state. New services-only updates deliberately refuse proofless legacy state rather than falling back to today's OS; recovery stays the existing workflow. This requires no coordinated node OS upgrade.

Risk: HIGH because this selects deployment inputs and preserves retained state/recovery. Request general, architecture/repetition, scope/proportionality and risk/compatibility lanes plus explicit complete base-to-head history and migration conclusions. Lead selects retained independent reviewer0 (Sol/xhigh/read_only); implementer does not self-approve or start long checks.

The owning extension is consumed by the workspace through lib.mkPackage and its selected extension input/siteConfig. [Selected-versus-installed comparison](selected-installed-comparison.json) binds the original4x0 provider/maintenance bytes to767dfd5, with ordinary shebang treatment. This local source package does not install or activate a helper. Publication, consuming-workspace preparation and activation are subsequent lead-owned release boundaries. No source/default integration, installed-helper patch, live update, GC or session lifecycle action is authorized here.

Session remains open: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/

Postreview connection recovery: [original operation reconciliation](postreview-original-reconciliation.json). Original handle60909/driver3213099 ended during preliminary identity evaluation, with unknown exit and no required-check result. No matching query survived. Input metadata was retained at the exact source identity. Only the outstanding required checks were launched as handle62683; no successful check was repeated. Complete raw evidence remains private at `/tmp/e0os-postreview-0siudjgz`.
