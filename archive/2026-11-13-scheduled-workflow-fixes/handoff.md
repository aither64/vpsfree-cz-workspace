# Scheduled workflow repairs

## Current phase
Both final configuration corrections are merged. Normal flake.nix URLs are
unchanged; flake.lock alone selects confctlff5e0177. Both workflows use plain
confctl inside their existing Nix shells and contain no independent provider pin.
Both final master runs passed, including actual updater and finalguard/push.
All merge claims released/verified. No physical deployment or lifecycle action.

## Final configuration source and verification
| Repository | Final reviewed/integrated head | Fresh final master run |
| --- | --- | --- |
| vpsadminos-org-configuration |15352aeb13c4011b5dd1a1f78d1fdcb08f7c2420 |[43484020423](https://github.com/vpsfreecz/vpsadminos-org-configuration/actions/runs/43484020423), attempt1 SUCCESS |
| vpsfree-cz-configuration |7d9807e021e6106d628c021da45f5f55077b2e9c |[43484770367](https://github.com/vpsfreecz/vpsfree-cz-configuration/actions/runs/43484770367), attempt1 SUCCESS |

Both complete branches passed all four independent review lanes with no findings:
[final-review-c4.md](final-review-c4.md). Each has one normal generated confctl
lock update and one separate workflow source correction. Only confctl-owned
logical input paths change; unrelated roots/follows are preserved. No migrations.
Prior merged C1/B1/C2/C3 and generated history remain protected.

Focused proofs use the exact accepted provider package/source/derivation:
- /nix/store/v4b3r3r8102kyf92lidwvk62plpjs13j-confctl
- /nix/store/1qw3c7q3r67drrv0z4vmac9g70pvxyf5-source
- /nix/store/6nq336f5rfs8jgd38bsmdgpdhy5rw0rd-confctl.drv

Accepted C3 full225RSpec/110RuboCop and actual mixed-selection/rewind/caller-hook
proof is reused at its complete source/input/NAR identity. Current C4 proofs
record actual declared resolution, native callers and real final check-update
on identical adopted/exportedHEAD locks. That no-op proves wiring, not another
changed ancestry test. VpsFree also proves saved-profile tool/Ruby/native identity
across a disposable stable-lock mutation. No provider suite or update generation
was repeated for C4. Actual org Ruby3.4.9/Bundler4.0.7; vpsFree Ruby3.4.11/
Bundler4.1.0.beta3/Overcommit0.76/native date3.6.0. Complete graphs/native/store
and target/profile invocation receipts:
[evidence-c4-implementer1.md](evidence-c4-implementer1.md),
[evidence-c4-implementer0.md](evidence-c4-implementer0.md).

Org claim2be8f01a released/verified18:34:54UTC; vpsFree1dc84db8 released/verified
18:39:34. Normal ff-only merges/hooks/SSH exact proofs and clean targets.
Org run18:34:57–18:39:14UTC passed every step and final guard/push, with no new
updates. Logs /tmp/scheduled-workflow-fixes-c4-org-hosted/; SHA256
b293501db3bd04045b7f6047e36063364addfc28e48d523e1727b08e40e71344.
VpsFree finalrun18:39:36–18:44:03UTC passed every step, no new updates, final
guard NoChanges and push Everythingup-to-date. Logsha256
6343598c8d2e6f541807e637c94fcee68d5cceda2bf7cfa1531cd4113a334465 under
/tmp/scheduled-workflow-fixes-c4-vpsfree-hosted/. Managede8ad/23d4 both terminal
passed, all operation-owned sessions/cells ended; no observation remains.

## Other accepted repairs
| Repository / workflow | Integrated feature head | Actual successful run |
| --- | --- | --- |
| vpsadmin full migration specs |2d0946c4e699aa61092228d8a7cb275477ee46d0 |[43449334492](https://github.com/vpsfreecz/vpsadmin/actions/runs/43449334492),84examples/0failures |
| HaveAPI coherent Nixpkgs/Ruff updater |3194488d1ab3403bbb83896bdac8089f1195e645 |[43453002644](https://github.com/vpsfreecz/haveapi/actions/runs/43453002644) |
| IRC daily update including push |f15bf5577924da84be217dcd925ab337e1c5c3c5 |[43460321532](https://github.com/vpsfreecz/vpsfree-irc-bot/actions/runs/43460321532) |
| KB complete managed-page runtime |cb7825245ea786fb0f51c469d1a7dc5c6a1ececc |[43454286948](https://github.com/vpsfreecz/vpsfree-kb-contracts/actions/runs/43454286948) |

All attempts1. Normal hooks/guarded publication preserved. IRC actual local
positive/rejecting pre-push proof closed irc-hook-validation-coverage. Full KB
master push executes the same complete suite as schedule/dispatch; no duplicate
campaign. Root causes and exact receipts are linked from state/audit and owner
files. No production machine or KB publication.

## Message policy and historical boundaries
Transitive inputs entered guarded messages in confctl5507177, committed
2026-10-24. Corrected providerff5e0177 filters entire title/body/log to explicit
logical selections while checking/returning the full graph. Dependency-only
changes use a requested-input title only; direct Nixpkgs/llm calls retain
no-changelog. C2 private Tempfile/-F transport4c636b40 is integrated and retained.

Earlier YAML-only tool adoption was rejected by the user and is historical.
Its C3 actual runs43477762211/43478026385 both passed, with selected-only org
messages and no vpsFree changes, but they do not substitute for final C4 source
authority/hosted proof. Their merged history remains; C4 removes the duplicate
pin additively. No workflow pin should be reintroduced for rollback. An older
locked provider can lack guards and cannot silently waive required safety.

## Audit limits and remaining action
Inventory covers26mapped repos/16scheduled workflows. HaveAPI weekly Rust auth
performance remains a separate measured product regression; reference/budgets
unchanged. KB prior GitHub504 was external. Syslog lacks retained schedule
history. Details: [audit](audit.md), [inventory](scheduled-inventory.md).
Confctl automaticTests43474592486 atff completedSUCCESS. Auxiliary vpsAdmin
feature integrationCI43447714261 remainsremotein_progress; required local and
hosted full84migration checks passed.
No local observer owns those auxiliary runs; inspect only if materially needed.

Finalfreshfetch ancestry checks completed18:45:23UTC: every registered exact
finalhead is an ancestorofremote master, bothconfigs/mastersexactfinalheads.
No remaining work for the requested corrections; no rerun/sourcechanges queued.
Keep session
open; no archive/delete/stop/cleanup requested. Retain branches/worktrees and
normal tracking cadence; initial plan/state commit66c6aede3.

[Stable session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-scheduled-workflow-fixes/)
