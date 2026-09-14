# Mandatory change review packet

Initiative: `2026-09-14-portal-review-fixes`. Read this packet, `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-14-portal-review-fixes/plan.md`, and
`/home/aither/workspace/ai/vpsfree.cz/work/2026-09-14-portal-review-fixes/state.md`. All project worktrees are beneath `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes`.
Skill: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/vpsfree-dev-workspace/skills/mandatory-change-review/SKILL.md`.
Use gpt-6-astra with xhigh effort, as explicitly requested by the user. Perform
your assigned lane directly, using fresh context. Do not launch subagents.

## Revisions

| Repository | Base | Head |
| --- | --- | --- |
| codex-web | `6335da93acdcc82cc26200d2fbc7f479655aa7c3` | `1a0ed38060db44bc3849d7adec481519d78dfa90` |
| dev-workspace | `83136101866eb42d9e079f47191308c0549ac9e7` | `94e3114c6fef510ca21d29efd1741faa848a4147` |
| vpsfree-dev-workspace | `a08a40eeff124bdbcc1ce6b6b06aed1839a9d9fc` | `7dc4ea2ac169064de0034983377f9f19c23a281d` |
| workspace | `8f31bab` | `997f4aa2ce7ae58b2be13348036a2d168c71a2b1` |

The workspace feature was rebased onto the shared master's initial tracking
commit. Review its flake pin change relative to 8f31bab. Do not edit another
initiative or the shared root. Review committed changes and their series; write
findings only to your assigned file in this review directory.

## Requested behavior

- Exact Git changed lines in Unified and Split. The reported vpsAdmin OAuth2
  commit must show +116/-6, rather than +1091/-981. Retain read-only CodeMirror
  and Shiki. Character highlights may approximate only inside a Git block.
- Unified fallback, with URL and saved Split honored.
- Every file collapsible; changes above 2000 added+deleted lines initially
  hidden, with no automatic blob/editor/highlighter work. Choices survive
  layout and frozen-comparison navigation. Explicit file/line/full-file links
  expand the target.
- Automatically batch-refresh histories on repository-tab activation and
  visible polling. Keep open comparisons frozen until explicit refresh. Ignore
  stale details HTML and out-of-order head/history reads.
- Abort old-document reads before pagehide to prevent Firefox's transient
  details NetworkError. Restore polling after navigation restoration.
- Keep timing while inactive tabs recover, freeze stale extrapolation, and
  wait ten visible seconds before warning; do not count hidden time as working.
- Prevent retired App Server readers from republishing prompts. Bind answers,
  snoozes and timers to an exact offer. Preserve drafts and wizard page through
  temporary absence; secret answers remain memory-only. Replace submit/snooze
  alerts with inline controls. At most one automatic answer retry, only after
  definite non-delivery and authoritative restoration of the same
  thread/turn/item/questions. Never automatically replay uncertain delivery or
  answers to changed questions.
- Move Automatic archival into Session settings in the left sidebar.
- Update mandatory review instructions to gpt-6-astra, retaining xhigh.

## Ownership, consumers and commit series

codex-web owns connection admission/retirement, offer tokens, the optional
PromptResponder Go interface, HTTP errors and browser error fields. The example
application and dev-workspace consume its conversation interfaces. The runtime's
workspacecodex.Client embeds the provider Client, so the optional responder is
available on the concrete HTTP target. Legacy Go clients retain existing APIs.

The runtime owns Git resolution, diff ranges, editor projection, file lifecycle,
histories and the session page UI. The organization extension imports the runtime
and owns the review skill. The workspace imports the organization package and
supplies site configuration. Nix and Go pins refer to the same provider revision;
the vendor hash was regenerated from the actual updated module contents.

Provider 1a0ed38 is the connection/response contract and its tests. Runtime
b18a82d moves archival settings, 9d71b41 implements exact/lazy repository review
and automatic histories, and 94e3114 handles read/question recovery with the
required provider pin. Renderer and lazy loading share editor/content lifecycle;
review the broader repository commit's grouping as part of the series review.
Organization 660db8d changes the reviewer model separately from the runtime pin
in 7dc4ea2. Workspace 997f4aa updates only its consuming pin.

## Bounds and compatibility

No protocol version, database, manifest/journal/activity format, privileged host
configuration or node update. Git ranges and prompt metadata are additive HTTP
fields. Updated clients require offer tokens; retained legacy Go consumers keep
existing methods. A new client against an unsupported responder requests reload.
New draft records include their question schema and identity, so unbound legacy
records or changed questions are not silently applied. Secret values are never
written to browser storage. Collapse choices are page-local and keyed by exact
comparison/file identity. No answer is blindly replayed onto another connection.

The local operator is trusted for workspace administration. Preserve existing
remote authorization, origins, payload/path/object bounds and immutable Git
resolution. Do not invent a compromised-local-operator threat model. The actual
OAuth2 sources are test-only data with the upstream GPLv3 COPYING and provenance;
they are not compiled into the browser assets.

No integration into default branches is requested here. Deploy from the feature
workspace using workspace-host switch; keep the previous user profile for
rollback and the session/feature branches open. No system configuration pin is
needed. No archive/delete/session stop is authorized.

## Verification before review

- Provider: focused go test ./codex ./conversation passes. Twenty Node browser
  contract/sync checks pass. CI run 34875990096 passed at the provider head.
- Runtime: go test ./internal/repository ./internal/web ./internal/workspacecodex
  passes with the new provider. Includes Node contracts for identity/retry/grace,
  real-Git ranges and 2000/2001 preview boundaries.
- Editor: npm build and all nine tests pass; exact OAuth2 +116/-6 in both
  projections, Git-generated fixture comparisons, UTF-16 marks, newline/CRLF,
  grammar context, malformed ranges and worker cancellation. Packaged review
  assets also built successfully while calculating the Go vendor hash.
- Runtime CI 34876413264 passed at 94e3114. Workspace flake evaluation passes.
  Organization flake evaluation is being checked. Diff whitespace checks pass.
- Long browser, packaged/profile and isolated live App Server acceptance remain
  scheduled AFTER required review findings are resolved. Do not treat them as
  already verified. Browser test changes are committed but not yet executed.

Overall risk is high due to response-delivery semantics, secret drafts,
cross-project contracts and deployment/rollback. All four lanes apply: general,
architecture/repetition, scope/proportionality and risk/compatibility. Report
Blocking, Important and Advisory findings with file/line and commit references.
