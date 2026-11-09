# Monitor contract diagnosis

Implementer3; diagnosis/proposal only; 2026-11-03. No application edits, commits,
pushes, builds, deployment, lifecycle operations or peer-session access.

The installed monitor skill implies automatic parent continuation without
specifying an application-owned idle-turn delivery mechanism. Its current
instructions support an active parent using native waits. They do not establish
that ending the parent turn is safe. Correct that promise immediately in policy;
an actual idle wake-up fix additionally needs the runtime delivery path being
designed by the architect.

## Evidence boundary

- **Seed, not re-exercised:** the original native watcher remained running after
  its parent ended; native messaging had no verified idle-turn wake path; its MCP
  `report_to_lead` attempt returned the nonmember error. No original-session
  files, logs, roster, commands or credentials were accessed.
- **Directly checked here:** session/environment identity; selected command and
  installed skill paths; immutable package/catalog/native utility metadata;
  catalog digest reconstruction; installed-source NAR hash and relevant file
  equality; canonical source and documentation references below.
- **Limited live evidence:** ordinary reports from this retained implementer
  received application receipts with `steered: true`; a same-session assignment
  to architect0 also received that receipt. This establishes active-turn
  steering for those sends, not idle activation or native-utility delivery.
- **Not exercised:** disposable `turn/start`/`turn/steer`, native idle-parent
  behavior, restart, disconnection, cancellation or duplicate-delivery behavior.
  This package requires no runtime reproduction; those are other assigned
  diagnostic packages and proposed acceptance tests.

## Installed provenance

`dev-session current` printed `2026-11-03-lead-wakeup-delivery`; both environment
variables matched that slug and `/home/aither/workspace/ai/vpsfree.cz`.

`/home/aither/bin/dev-session` resolves to the seed package:

`/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0/bin/dev-session`

Its wrapper selects its own `share/dev-workspace/extensions.json`. That catalog's
`dev-session-monitor` entry and the installed Codex-home skill resolve to:

`/nix/store/pw7ffd5bsg55wvcbqwc3vs91h9f1894i-source/skills/dev-session-monitor/SKILL.md`

`nix hash path /nix/store/pw7ffd5bsg55wvcbqwc3vs91h9f1894i-source` returned
`sha256-k6d90hicmnStL/tT6AeBLbYBQ5U7O/pmUls1zGYwsMg=`, exactly the coordination
workspace lock's generic runtime source hash at
`c2182254d29c4175c3e9fe4267e5a92dd1da6b79`. The installed skill, session guide,
catalog generator and package composer also matched the assigned generic
worktree byte for byte. Monitor skill SHA-256:
`4c4abbecb062573014d6c9b9be0ee60799d6161fc497acc94e2e6b61c1150cd4`.

Both installed `share/dev-workspace/package.json` and `agent-teams.json` declare
catalog digest
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`, schema 6.
Reconstructing the original configuration by removing generated catalog fields
and team digests, serializing sorted compact JSON, and hashing it produced the
same digest. The package names generator `dev-workspace-nix-agent-teams` v1,
canonicalization `nix-builtins-toJSON-attrset-v1`, native adapter
`codex-custom-agent-toml` v1.

The separate `utilities.verification_watcher` record is:

| Field | Installed value |
| --- | --- |
| model / effort | `gpt-6-luna` / `low` |
| behavior / lifetime | `verification_watcher` / `operation` |
| saved access / effective execution | `workspace_write` / `full_access` |
| startup / maximum concurrent | `on_demand` / `1` |
| required for | long/uncertain checks, workflow/CI/deployment waits |

The matching native identity is
`dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`, at
`share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml` under
the seed package. Behavior digest:
`20212a3e814132d953ca91029e022451e03acc83fc52872ca238f8c76f4dfbb5`.
That TOML contains the bounded watcher instruction,
`sandbox_mode = "danger-full-access"`, and `approval_policy = "never"`.
It does not contain a completion callback or idle-turn delivery registration.
Model and effort remain explicit caller selections, as documented in
`dev-workspace/docs/workspace-portal.md:1503–1509`.

The coordination workspace's effective input graph selects:

| Repository | Assigned worktree HEAD / effective locked revision |
| --- | --- |
| `aither64/dev-workspace` | `c2182254d29c4175c3e9fe4267e5a92dd1da6b79` |
| `vpsfreecz/dev-workspace` | `e4e7e95ed39bf514b33f8f8ae61ba9868de060ae` |
| `aither64/codex-web` | `d3a29bee90ef00a08816920408c596152339a637` |

`flake.nix:6–8` overrides the extension's generic input. The extension's own lock
alone selects older generic `832d9f1a6a21337dd44063ddf39f7a88cfc95450` and
codex-web `5f15b9293f9b1eef7469a34d7b2044c743160283`; those defaults must not be
mistaken for the installed monitor source. The generic-source NAR check above
is the independent installed-source proof; the other rows are inspected input
graph/worktree evidence, not a reconstructed complete installed closure receipt.

## Source contract and ownership

All generic references below are at `c2182254`; extension references at
`e4e7e95`.

| Source | Finding |
| --- | --- |
| Generic `skills/dev-session-monitor/SKILL.md:17–31` | Separate pinned utility policy; explicit execution access; fresh context and operation lifetime; utility is not a team member. |
| Same file `:40–51` | Brief names command/run, revision, logs/status source and cancellation, but gives no required durable parent report registration or receipt. |
| Same file `:53–57` | Native waiting is prescribed, followed by an unqualified promise of automatic continuation. |
| Same file `:74–78,85–94` | Watcher must report completion/escalation and parent resumes, without a supported report transport or acknowledgement contract. |
| Generic `docs/dev-sessions.md:205–228` | Human guide says parent continues when watcher returns; describes native ownership but no idle wake guarantee or limitation. |
| Workspace `docs/agent-instructions/verification.md:124–145` | Consuming policy repeats automatic parent continuation on completion/escalation. |
| Generic `nix/agent-teams.nix:418–449` | Utility generator supplies bounded instructions and access policy, no report registration. |
| Generic `nix/workspace-portal.nix:80–96` | Runtime owns the monitor skill; core/extension skill names must not overlap. |
| Extension `flake.nix:40–44,133–139`; `README.md` catalog composition | Extension contributes its own skill directories and composes generic skills; it does not own this monitor skill. |
| Generic `portal/cmd/workspace-portal/team_mcp.go:310–348` | Native report caller resolves through current retained membership; rejection matches seed wording; successful reports validate the stable message-ID receipt. |
| Generic `portal/internal/teamruntime/reporting.go:19–69` | Reporter resolution requires a unique ready roster member and matching active session/root thread. A utility's absence is intentional. |

The minimal policy correction belongs in the generic skill and its session-guide
paragraph, with the consuming verification policy aligned. An extension skill
shadow would conflict with composition and create a second authority. No
codex-web or catalog/model/roster change is needed for that correction.

## Current workaround and proposed wording

Keep the parent turn active after launching an authorized native watcher. Do
independent work, then use interruptible native blocking waits with bounded
output. Continue on the result within that active turn. If delegation or an
existing run's observation interface is unavailable, use the existing visible
parent-monitoring fallback. Preserve the original command/run owner.

Suggested replacement for the skill's continuation paragraph:

> With native-only delivery, keep the parent turn active and use native waiting
> until the watcher reports. Resume the authorized workflow on completion or
> escalation. Ending the parent turn does not establish a supported automatic
> wake-up. Promise continuation after an idle period only when an
> application-owned operation registration and durable lead-delivery path are
> available and verified for the current session.

Use the same qualification in the human guide and consuming verification rule.
The watcher instructions should name the selected delivery mechanism and require
an acknowledgement, rather than assuming that a native message wakes an idle
parent. This is proposed wording; no policy source was changed.

## Requirements for a future asynchronous launch/report contract

These are design inputs, not implemented APIs or verified guarantees:

1. Before launching, register the exact owning workspace/session, current lead
   thread, operation ID, watcher identity and approved observation/execution
   scope. Preserve catalog digest/model/effort/access and operation lifetime.
   A report must derive authority from that registration; do not add utilities
   to the retained roster or pass a member's identity to `report_to_lead`.
2. Preserve command identity or repository/revision/workflow/run/attempt, outcome
   (`passed`, `failed`, `incomplete`/escalation), exit status/conclusion, elapsed
   time, evidence paths and any still-running operation. An escalation is not
   completion and does not relinquish command ownership.
3. Report through an application-owned durable operation capability with a
   stable event/message ID. Retry an uncertain acknowledgement with the same
   ID. Distinguish recorded delivery, accepted native submission and verified
   turn activation. Native send success alone proves none of the latter.
4. Reuse the existing durable prompt/submission and receipt mechanisms beneath
   ordinary team reporting where their lifecycle and recovery semantics fit.
   Preserve active-turn steering and create a real turn when idle. The other
   diagnostic owners must establish the exact reusable primitive; the MCP
   member resolver itself must remain restricted.
5. Retain pending delivery across supported disconnect/restart; suppress
   duplicates; recheck exact ownership and stopped/archived/revoked boundaries
   before submission. Uncertain submission requires receipt reconciliation,
   not a fresh delivery ID or an automatic replay loop.
6. Do not advertise the idle-continuation mode until isolated tests demonstrate
   actual lead activation for success, failure and escalation, plus busy
   steering, duplicate reports, exact run/attempt identity, restart/disconnect,
   cancel/revoke and session/utility isolation. Preserve ordinary member reports
   and saved settings. These tests remain unrun in this diagnostic package.

Policy-only changes affect future instruction interpretation and introduce no
persisted format. They cannot fix already-idle parents. A runtime operation
capability needs separate compatibility/recovery design and explicit later
implementation scope; package rollback must not misinterpret pending delivery.

## Handoff

No blocker for the bounded policy/source diagnosis. Architect and lead own
synthesis and the actual idle-turn reproduction. No project documentation was
changed because this assignment is a diagnosis/proposal, not an implemented
behavior change. State/portal updates and all Git mutations remain lead-owned.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/)
