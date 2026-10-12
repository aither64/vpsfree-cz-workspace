# Compact attachment-menu review

Scope: follow-up to the previously reviewed, deployed upload implementation.
User asked to replace the permanently visible Attach files button with a + icon
opening a submenu, and remove the persistent limits sentence entirely. User
accepted placing + beside Send and Create session in both forms. Deployment to
aitherdev remains authorized; default-branch integration and session closure do
not. Review the following committed delta, not the already deployed baseline.

Workspace /home/aither/workspace/ai/vpsfree.cz.
Initiative work/2026-09-12-portal-file-uploads; see the follow-up sections in
plan.md and state.md. Worktrees are worktrees/2026-09-12-portal-file-uploads/NAME.
All branches use that slug. Full heads are in menu-revisions.json.

| Repository | Follow-up base | Head |
| --- | --- | --- |
| codex-web | 7b79942eee2d7bcaf52252249d8599db76c033b2 | aa26ec23712e7bdcefd5545ca7715d9bff00f8b7 |
| dev-workspace | 30bfb2a378138a7fdfe8f6aaa05fcbf8d98037b3 | 4ddf911fc73e2c8d3c96e1b713cea404dacc7296 |
| vpsfree-dev-workspace | 9db07ad92eeb62490dbb14cdb5b9cd9a47b4412c | 905f7a52b766d219d90940885d6cccb3de5a0360 |
| workspace | a3b8e6b4945dfedcee48c6a732e933df4dc48f45 | 19dc77784383ae0063ed240a2210347cb74c3f46 |
| vpsfree-cz-configuration | 63652724f9ed0202d6f9c842d842da89ab33bbaa | 3d3fa67dd306e1261237cb7df331b664b8b0e8e1 |

Workspace original deployed feature was fb339980; its existing three commits
were rebased unchanged onto shared master 6f47880 before the new pin commit, as
workspace rules require. a3b8e6b is the rebased previous pin. Older pin updates
belong to separate already deployed iterations and are retained intentionally.
This follow-up has one provider UI/API/doc/test commit, separate runtime pin and
consumer UI commits, then one pin per downstream. Generated confctl message is
kept exactly as generated per configuration AGENTS.md.

Owner is codex-web conversation/assets/uploads.js mountUploads. Optional
controlsRoot places only owned controls in a host action row, leaving cards and
errors in root. Default single-root callers remain supported. Shared
mountConversation consumes it, and dev-workspace uses the exported mountUploads
in its existing-session and new-session forms. Other components are packaging
consumers, not independent browser implementations; inspect actual pins/imports.
Native auto popover owns outside dismissal/top-layer rendering; component owns
viewport placement, keyboard/focus and cleanup. Limits still fetched/enforced;
actual rejection errors remain. New labels are Add attachments, Attachments and
Attach files, reviewed directly under vpsfree-user-facing-writing.

Acceptance: no empty upload row or limits sentence; + and submit share a row;
menu overlays without resizing composer, prefers above and fits viewport with
below fallback; multiple-file picker via trusted synchronous click; Escape,
outside click, repeat toggle, keyboard focus; lock closes menu; selected cards,
progress, removal, drag/drop and prompt IDs still work. Destroy removes owned
controls/listeners without removing neighboring host actions.

Non-goals: changes to transfer/backend/quotas/Codex protocol or state, submenu
frameworks or speculative options, moving limits prose to another location,
1 GiB transfer rerun or real Codex lifecycle rerun for a browser-only delta.
Those transport/lifecycle behaviors were accepted in the baseline and unchanged.
No schema, migration, path, ownership, authentication, or client version change.
Trusted operator administers host; remote clients remain untrusted per runtime
AGENTS.md. User profile owns workspace app, system configuration owns integration.
Deploy package then configuration from existing feature worktrees with normal
guards and health checks. Rollback reads unchanged upload state. Existing five
minute asset cache may display old UI until refreshed/expired; no new wire shape.

Quick verification passed: Node syntax for both provider modules and portal app;
node --test test/*browser*test.cjs in provider (5 passing including ownership,
lock, fallback root and initialization error contracts); go test ./conversation/...
in provider; go -C portal test ./internal/web/... in runtime (28.6s). Tools from
repository Nix development environment, TMPDIR=/tmp, GOWORK=off, GOFLAGS=-mod=mod.
Nix vendor hash remeasured through an expected fake-hash mismatch:
sha256-3XWxCKVZOsnMJawQaQOl3jeu1aA4AUDwUlf2qD4RhRg=.
All pins generated with nix flake update / confctl. git diff --check passed.
Provider head CI already green; runtime/organization head CI in progress.

After review: focused real Firefox checks (menu-browser-acceptance.py) for
both forms at 1280 and 390 CSS pixels, plus native provider root/lock/limit/cleanup
behavior; packaged checks, full package/system build, guarded deployment and
live HTTPS smoke. Script is a curated acceptance artifact, not shipped code.

Risk classification high because shared browser API and deployment/rollback
cross project boundaries, though implementation is bounded and state-compatible.
Lanes: general, architecture/repetition, scope/proportionality, risk/compatibility.
All reviewers gpt-5.6-sol, xhigh, fresh context. Do not launch subagents or edit
project code. Write findings to menu-review-LANE.md in the tracking directory.

## Direct review remediations

General: restore the root's initial hidden value in destroy, with a focused
provider assertion; remove obsolete Go sums with go mod tidy. Risk: remove
template hidden attributes so old providers still render controls, use :empty
CSS for pre-initialization layout, and change the full browser cache chain to
conversation.js?v=6, uploads.js?v=2 and uploads.css?v=2. These are the direct
compatible-markup/cache-key remedies described by the risk reviewer. Curated
Firefox acceptance now warms baseline provider/app/styles and exercises forward
and reverse mode switches with both forms. Baseline templates are represented
by the same form structure with legacy stylesheet URL; unused new action slots
remain to explicitly verify old providers against new markup.

Fixes folded into their owning follow-up commits, all pins consolidated. Final
heads in menu-revisions.json replace the packet-head table for remediation
verification. Original review-head objects remain available locally. No new API
or persistence behavior beyond the original controlsRoot boundary. Scope lane
will inspect the final consolidated heads. No confirmatory reruns required for
the narrow general/risk fixes.
