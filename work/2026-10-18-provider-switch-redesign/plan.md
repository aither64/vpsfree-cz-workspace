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
goals, model/effort, saved access and terminal environments. Include retained
team members and owned utility descendants. Unrelated sessions keep working.
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
