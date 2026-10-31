# Final review packet

## Outcome, scope and authority

User: “session 2026-10-30-vpsadminos-kernel-cve-check failed to archive. find the root cause, fix it. aitherdev can be deployed using vpsfree-cz-configuration. merge when fixed and verified.” Root cause is workspace retention negations overriding sensitive root exclusions. Fix Git privacy behavior while preserving ordinary retained records. No target lifecycle action, runtime guard change, metadata repair, pin update, deployment or new mechanism is intended. See [design.md](design.md), [plan.md](plan.md), [state.md](state.md).

Owner: workspace repository git@github.com:aither64/vpsfree-cz-workspace.git; target master. Feature worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-31-vpsadminos-archive-fix/workspace`; branch `2026-10-31-vpsadminos-archive-fix`. Exact final range and quick results will be supplied in assignment after implementation completes.

## Acceptance

Both work/archive sensitive roots and descendants stay ignored via ordinary private info/exclude entries, before and after creation. Ordinary direct/nested Markdown and portal.yml stay trackable; raw artifacts stay ignored. Synthetic git add -A must stage only ordinary retained files. Explicit root override must still surface the root so runtime refusal remains valid. Old-rule failure must be proven. Never use target contents as fixture or access target team/transcript; target diagnostic metadata is sufficient.

## Deliverables and history

One functional commit is intended: .gitignore boundary correction, focused real-Git regressions in test/storage_retention_test.rb, and concise durable rationale in docs/operations/workspace-storage-retention.md. These are inseparable support for the one behavior fix. No migrations or schema/state-format changes. No dependency/channel/input update streams. No obsolete branch approaches or supported intermediate consumers are intended; independently inspect full final series and give explicit conclusions on history, migrations and repeated update streams.

## Risk and consumers

High risk: sensitive persisted records could enter Git if ignore semantics regress. General, architecture/repetition, scope/proportionality, risk/compatibility lanes apply. Retained independent reviewer0 is gpt-6.1-sol/xhigh, read-only, no overrides. Read mandatory-change-review SKILL.md and every selected lane reference.

Owning interface is workspace-local Git ignore policy. Consumers are Git staging and the generic runtime's sensitive-session exclusion guard (selected package /nix/store/413w4bai6br4c2vq08gx9diq55iasvqk-dev-workspace-0.2.0, libexec/workspace-sensitive-sessions.rb). Runtime behavior and contracts are unchanged; existing exclusions remain authoritative and journal/recovery data is untouched. Fix applies dynamically when shared master receives it. No aitherdev activation or coordinated vpsAdminOS update required. Rollback restores defect without state migration; preserve protection and prefer forward correction.

## Evidence and remaining verification

Architect used disposable Git prototypes. Implementer old-rule run: 3 tests / 9 assertions / 3 failures / 0 errors, syntax OK. Final quick-check results follow with exact range. Longer packaged `nix build --no-link --print-build-logs .#checks.x86_64-linux.storage-retention` waits until final review, then uses fresh Luna/low watcher. No workspace GitHub workflow directory exists. Live acceptance after integration will use targeted read-only ignore/index probes without opening target contents or retrying archival.

Report concrete findings with severity and paths, residual gaps, and explicit whole-branch history, no-migration and update-stream conclusions. Do not launch subreviewers or change source.

## Exact committed final range and quick evidence

Implementation base a5c046992f0292ea71719f89f3f58adacb1da91d; head d5876d849f77f73d6a51952d31f9f0a04526b53e. One implementation commit: d5876d849 Preserve private session exclusions in tracking retention rules. Diff 3 files, +90/-8. Full remote-master range starts at 4737ef1449278f2b8d9b8398178008cfe401fb3c and contains 5113c4a97df6252c67a6df2393eef5fa554065e4 (this session initial tracking), a5c046992f0292ea71719f89f3f58adacb1da91d (already-existing shared coordination tracking), d5876d849f77f73d6a51952d31f9f0a04526b53e (fix). Do not access another session's tracking contents; a5c04699 is existing shared-master coordination, outside substantive fix review. Inspect full series dispositions and substantive final diff from a5c04699. No superseded approaches, follow-up fix commits, migrations or repeated update streams.

Fixed quick commands: nix develop --command ruby -c test/storage_retention_test.rb => Syntax OK; nix develop --command ruby test/storage_retention_test.rb --name '/tracking_ignore/' => 3 runs, 46 assertions, no failures/errors/skips (0.366 s test time); git diff --check, cached check and committed-range check passed. Worktree clean, fresh fetch and rebase master reported up to date. Published SSH branch independently verified at exact final head; gh run list for branch/head returned no runs. Long checks have not started.
