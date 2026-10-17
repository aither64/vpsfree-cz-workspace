# Final committed-deliverable review

User requested stronger delegation: Full-team lead coordinates/communicates;
specialists own execution; two implementers; smaller teams retain hands-on leads.
User approved coordinator policy with narrow exceptions and new teams only, then
requested implementation. Plan and design.md own the agreed acceptance criteria.

Read mandatory-change-review SKILL.md and all four lane references in full. Apply
general, architecture/repetition, scope/proportionality and risk/compatibility.
Perform the review directly; no nested reviewers. Read workspace AGENTS.md and
applicable projects, sessions, documentation, git, lifecycle, verification,
deployment and commits procedures. Read each affected repository's AGENTS.md.
Only inspect/report; do not edit source or run long integration checks.

Overall risk HIGH: catalog schema/public package contract, creation recovery and
forward-only deployment. Local host operator is trusted; remote callers remain
untrusted. Keep session ownership, input validation and retained-state checks.

## Complete ranges and histories

- dev-workspace: base `9b50f357b40aeb4b3bd9715609815ebcdca57043`, head `732f3f382c6918319c211cc84e6ab434dff4a8b5`

```
ced922c533c7d51ff35d488780a0020162883e7f agent-teams: create repeated members from catalog counts
732f3f382c6918319c211cc84e6ab434dff4a8b5 lead-policy: delegate complete execution packages
```

- workspace: base `a4aa81eb3a028b066ae11823dd11d5a3480ef1e8`, head `7aefc9669ffcb1ecb13f484db957f2854bcf8dbc`

```
7c6a03780c3d13861fa7074290c6fd6cc41022cb sessions: plan full-team delegation improvements
b347b3f05bd3780b30741adc6182d1a821702531 inputs: select repeated-member runtime support
7aefc9669ffcb1ecb13f484db957f2854bcf8dbc agent-teams: delegate full-team execution to two implementers
```

- vpsfree-cz-configuration: base `fbe190dc93e2d788aed561f367d049d2fe025b13`, head `c9ed3e3169016eaece6955cfb716d3f75c6b142c`

```
c9ed3e3169016eaece6955cfb716d3f75c6b142c inputs: set devWorkspace to 732f3f38
```

Each full final diff and complete series is retained next to this packet. Review
all three complete ranges, not just the latest commits. Workspace includes the
owned initial tracking commit because its remote master precedes that record.
Runtime count/creation changes and fallback prompt changes are separate commits.
Workspace runtime pin and site policy are separate commits, ordered so each
catalog is paired with a capable runtime. Configuration has one generated pin.

No database or persisted-state conversion migrations. Schema 4 is already merged
and deployed; its exact digests and interpretation remain supported. Schema 5 is
new, unmerged/unreleased and not yet deployed. No obsolete intermediate schema or
transitional migration is retained. Original combined runtime commit 989c72c was
split into logical commits before downstream consumption; it was never deployed
or pinned by a consumer. There are no repeated pin streams: exactly one workspace
nested runtime update and one matching configuration channel update, both 732f3f3.
Give explicit history, repeated-stream and migration-lineage conclusions.

## Contract and consumers

Generic runtime owns optional team initial_member_counts, stable expansion,
numbered-member validation, recovery/forks and fallback prompt. Site workspace
passes teamConfig through the unchanged extension (767dfd5). Configuration's
dev-workspace/devWorkspace channel selects the matching host module. Generic
schema-4 Nix test config and site schema-5 config represent both consumers.
Rosters and creation receipt fields remain unchanged. Old binaries reject new
repeated-role creation selections; existing policy already requires forward-only
recovery. Existing saved selections and prompts are not rewritten. Native child
capacity remains four because members are independent App Server threads.

No automatic dispatcher, task service, roster migration, permission changes or
model/effort changes. Busy/inaccessible retained members do not permit lead
execution. Lead-designed keeps lead-owned design. Global shared rules stay visible
while saved roster prompts remain frozen. Current snapshot byte limits remain;
assess whether expansion and all recovery readers preserve bounded acceptance.

## Verification and documentation

Focused Go catalog, projection, retry/fork/add, lead-policy and web creation tests
pass; quick-final.log has exact output. Focused Ruby snapshot readers pass (3 tests,
22 assertions), workspace instruction suite passes (9 tests, 152 assertions).
Initial watcher run found a stale source snapshot in the new test, corrected by
using the current returned roster. Its unrelated unmanaged web fixture also read
the deployed /etc provider catalog; final checks isolate DEV_WORKSPACES_CODEX_PROVIDERS
to an absent owned path, and pass. No source weakening was used.
Nix catalog assertion evaluation passes for both preceding and repeated-member
configs; site check derivation evaluates. Paired deployment-pin checker passes at
732f3f3, with extension/siblings/follows preserved. Long packaged checks, CI
acceptance and aitherdev deployment remain pending until this review finishes.

Runtime session and portal docs explain ownership, counts, compatibility/recovery;
site team guide owns its roster and prompt policy; core AGENTS.md routes there
within its 16 KiB discovery budget. Exact rollout state belongs in this session.
No default-branch merge direction exists. Deployment is authorized by the approved
plan and implementation request, using configuration feature refs and app profile.

Report findings ordered by severity with file/line and commit references. State
residual risks/test gaps and an explicit whole-branch history/migration conclusion.
