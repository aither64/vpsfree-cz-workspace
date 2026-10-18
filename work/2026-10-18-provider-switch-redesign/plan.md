# Provider switching without workspace downtime

Implement the user's requested provider workflow: automatic pause and resume,
session-specific selection, optional provider selection at creation, immediate
progress and concrete delay reasons, and efficient workspace-wide application.
Keep the currently healthy OpenAI subscription environment usable throughout.

## Scope and ownership

The lead owns investigation, design and implementation. No retained native team
was created (`dev-session start --no-codex --no-attach`); use the installed
standalone review and utility policies only when required. Primary repository:
`dev-workspace`; change `codex-web` only if reusable native client capabilities
are required. No live provider switch, service restart, default-branch merge or
deployment is part of development verification.

## Approach

1. Establish native unload/reload behavior and current session/provider routing.
2. Record a design and verification brief covering session authority, automatic
   pause/resume, creation, progress, recovery and compatibility before edits.
3. Implement scoped durable transitions and CLI/portal controls. Reuse cheap
   metadata and precise native receipts; avoid full transcripts for idle checks.
4. Run focused checks, commit the complete deliverable, obtain independent final
   review, then run appropriate isolated integration checks and publish branches.

## Compatibility and recovery

Preserve histories, queued input, pending user requests, delivery identities,
goals, model/effort, saved access and terminal environments. Switch the lead and
all retained team members. The user explicitly accepts stopping temporary subagents during the switch;
they do not gate completion or need provider migration. New subagents inherit the switched parent's provider.
Temporary work must remain recoverable, and retained members must never be
classified as temporary merely because they are idle. Unrelated sessions keep working.
Define workspace default versus explicit session selection. Existing schema-1
provider state and in-progress journals need an explicit supported upgrade and
rollback contract; never silently reinterpret or erase them. Do not bypass
native writer locks. Record crash recovery and observable effective routing.
No database migration is assumed; determine package contract changes in design.

## Verification and documentation

Use the repository Nix environments. Add behavior tests for scoped switching,
busy-thread interruption/resumption, preserved input and settings, concurrent
unrelated work, creation selection, prompt progress, startup races and recovery.
Use disposable fixtures/native homes rather than the working workspace.
Maintain supported behavior and operations in `docs/codex-providers.md` and the
session/portal guides, with reusable client contracts owned by `codex-web`.
Keep investigation and rollout-specific evidence here. No merge/deployment
approval is implied by this implementation request.

## Accepted stock-Codex boundary

The user rejected downstream Codex patches and repeated native rebuilding, then
said: "let the subagents be stopped, it's not that important". Use the unchanged
selected upstream binary. Close/reopen retained leads and members through the
supported API, accepting normal interruption of their temporary children. Keep
saved child histories, but do not attempt to migrate/restart delegated child
work. New children inherit the target provider. This supersedes the earlier
requirement that existing children keep executing while their parents switch.

Remove the abandoned native operation, build override and its unused protocol
fixtures from the final series. No patched output was built/deployed or consumed.
Retain earlier review/build records as evidence, not as supported runtime code.
Normal native interruption can cancel running tools and pending dialogs; only
persisted histories and durable native queue entries have a storage guarantee.
The worker does not gain access to private unsampled native buffers. Do not
claim lossless hot migration or automatic restoration of temporary child work.

## Authorized rollout

User direction: "deploy it to aitherdev". Prepare dedicated workspace and
vpsfree-cz-configuration worktrees, select exact published runtime 2b96a3f
through the nested override and confctl channel, and deploy system then user
profile through the coordinator. Preserve stock Codex and active work. No
default-branch integration, reboot or team creation is authorized. Initialize
the missing ordinary retained conversation through the supported lifecycle
entrypoint for this same initiative and supervise foreground coordinator work.
