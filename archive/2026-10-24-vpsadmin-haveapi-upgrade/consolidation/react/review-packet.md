# React consolidation — final review packet

Requested outcome: one current-main React review candidate, preserving the
reviewed released-client behavior and current upstream work. No runtime feature,
version upgrade, UI wording, live deployment or default integration is included.
The accepted boundary is design.md:6219 and its final React clarification.

## Exact source and history

Repository: `repos/vpsadmin-webui.git` (canonical SSH vpsfreecz/vpsadmin-webui).
Candidate: `worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-webui-031`,
registered branch `dev/vpsadmin-haveapi-031`.
The same02e local `dev/vpsadmin-haveapi-current-main` ref remains preserved;
[ordinary branch alignment](execution/branch-alignment.json) changed no source.

- Fresh main/base: `40653dffed4561dd6086716fd506a7223d3631d7`.
- Dependency: `b38a4eea6ef2e98fe28a3761c96c4b936a922ddd`.
- Final adapter/head: `02e58932cef3b667ff68401ff93e4e43bc2a3ce5`.
- Final tree: `c273b4a0a86b88d15613fb96e4981ac7b70604e4`.
- Original reviewed range: `9113caa0915b2908373ecd616f8f752e779ed4c9..2e32c814d3af70ac39257f2542075bd580ee38d4`.
- Mapping: `73070a17` → `b38a4eea` (range-diff equal), `2e32c814` →
  `02e58932` (requirements conflict plus dated reconciliation documentation).
  Both original author identities and author dates are preserved.

[Full two-commit series](execution/final-series.txt),
[complete final diff](execution/final.diff), [stat](execution/final-stat.txt),
[range comparison](execution/range-diff.txt),
[upstream-relative tree changes](execution/retained-upstream.diff),
[source/preservation receipt](execution/source-reconciliation.json).
Original feature:75 paths; final:76, adding only the dated reconciliation record.
The dependency update occurs once. The adapter retains the reviewed final R2
contradictory-receipt/no-replay behavior directly; no pilot/archive transport,
old dependency update stream or feature merge commit is introduced. Historical
release work logs describe their actual earlier inputs, not new verification.

## Reconciliation and source boundaries

The one textual conflict in REQUIREMENTS preserves current main's complete
REQ-010 mobile-lookup and REQ-012 Tasks behavior while adding the reviewed
production-client links to REQ-011/012. Other overlap paths merge normally:
WORK_LOG, API_CONTRACTS, E2E coverage, structural debt, blocking VPS fixtures and
E2E tsconfig. Current main's adopted browser coverage remains and public overview
is adopted; the obsolete haveapi.ts structural exception is removed. The new
synchronous lifetime-date and admin-preference tests use apiWire while preserving
upstream assertions. Three new upstream response assignments were corrected after
the initial focused run exposed six transport-fixture failures; no runtime fix.
All feature paths outside those seven overlaps exactly match old2e32.
The production adapter and public/error/XHR implementations are byte-identical
to the reviewed2e32 versions. Upstream-only paths retain main's bytes.

Dependency remains exact haveapi-client0.31.2 and XMLHttpRequest1.8.0 with the
same root/BFF/flake locks and frontend npm dependency hash as old2e32. No BFF,
Nix module or wire contract change relative to the original feature is added.
Owning interfaces are src/lib/api/haveapiRequestClient.ts and haveapi.ts;
actual consumers remain the domain adapters, public calls and mutation guards.
Useful contracts are in docs/design/{API_CONTRACTS,HAVEAPI_CLIENT,PACKAGING}.md.
New documentation: docs/work-log/2026-10-31-haveapi-current-main.md and WORK_LOG.

## Preservation, migration and publication

Canonical live path `vpsadmin-webui` stays clean2e32/inode51692404.
Candidate alias inode51554956 and all19972 private/ignored entry descriptors
(content, links, modes, owners, inodes) remain equal. Its retained Bash952323,
PTY323/path and childless state are preserved; no signal was sent. Oldbaf is
retained both on original dev/vpsadmin-haveapi-031 and explicit recovery ref
`dev/recovery-haveapi-031-baf00acc`. Original dev/vpsadmin-haveapi-0312 remains.

NO MIGRATIONS in the owned delta. src/lib/api/migrations.test.ts is a VPS action
fixture, not a database migration; no schema or persisted-format change. This
claim does not rewrite or make claims about upstream migration history. No
coordinated node upgrade is required. Application rollback uses prior matching
frontend/BFF artifacts and preserves BFF credentials/session data.

Final lead disposition uses already-registered own031 without registry changes.
Explicit oldbaf recovery was published nonforce and independently verified first;
then only own031 moved oldbaf→02e using the specifically authorized exact lease.
[Final remote refs](publication/remote-final.json) and [comparison](publication/comparison.json).
Existing031 is the sole active review alias; lead retains protected PR disposition. Canonical live2e32 and
old recovery aliases are retained paths, not additional merge candidates.
PR74/dev/haveapi-async-client at5dd2333 and PR63 are untouched. No duplicate PR
or protected published-history rewrite is authorized/performed.

## Verification and requested review

Complete ci:quick passed at predecessor90f9d1a9. Only the blocking-VPS test fixture
and dated technical log subsequently changed; all quick-gate implementation,
locks, type/coverage/audit configs remain exact. Final-head root typecheck and nine focused test files pass:123/0, exit0,
77.173s. [Final quick result](execution/quick.result.json).
[Final preservation/installed-input guards](execution/final-guards.json) pass.
Docs inventory regeneration was byte-identical to the committed tracked file.
No E2E coverage/structural exception was added, and no long check has started.
[Exact2487-entry Gitless export and locks](execution/export.json),
[tracked modes/blob/hash inventory](execution/tracked-source-inventory.json),
[final affected quick command](execution/quick.sh), [stdout](execution/quick.stdout.log),
[stderr](execution/quick.stderr.log). npm ci runs only in the owned disposable
export, never against retained checkout dependencies. The package-source guard
used the exact existing nix/source.nix filter at90f9d1a9. Its required paths,
dependency/provenance inputs, path set and filter implementation remain unchanged
by the final fixture/log correction; that earlier result retains its exact scope. Initial attempt1 incorrectly
passed the full tracked export (including tracked .env.example/output) to that
filtered-source guard and stopped before npm; its command/log/result is retained
as quick-attempt-1. No product fix or bypass was needed. Attempt2 retained the full ci:quick pass
and117PASS/6FAIL focused run; its exact old fixture is saved alongside the logs.
All19 npm audit advisories (16 moderate/3high) affect development-only nodes
whose lock entries exactly equal fresh main; none affects HaveAPI/XMLHttpRequest.
[Bounded advisory classification](execution/npm-audit-summary.json); no dependency
repair is included in this consolidation. Native utility delegation
is unavailable in this context; documented parent monitoring is used, without
adding Nix job/core limits or a timeout cancellation rule.

Overall risk HIGH: existing authentication/session recovery, public protocol
mapping and uncertain mutations are preserved across a substantive newer base.
Request all four lanes (general, architecture/repetition, scope/proportionality,
risk/compatibility), complete base-to-head history and explicit migration/no
obsolete-stream conclusions. Retained eligible reviewer0 is Sol/xhigh/read_only;
lead assigns final review, without settings overrides. Review the reconciliation
and actual final branch, not only old reviewed source.

Final review was accepted by lead: retained reviewer0 native01a192de-9521-7972-ac0a-bff61ac5a3c2, all4/HIGH NO FINDINGS, whole history/one dependency stream/NO MIGRATIONS.
Released postreview checks are now complete: full unit307files/1929PASS, normal
buildPASS, frontend/BFF/provenance/source/package Nix outputsPASS. [Final receipt](receipt.md). Existing browser/live
proofs remain scoped to their old inputs; no live OAuth/browser campaign, source
retargeting, deployment, default merge, worktree cleanup or lifecycle action.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/).
