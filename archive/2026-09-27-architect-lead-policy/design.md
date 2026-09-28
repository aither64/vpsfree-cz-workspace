# Design and verification brief

Accepted implementation brief for this initiative. The lead owns coordination;
the architect owns technical design and verification planning; implementers own
application edits. Keep the phase checklist and execution evidence in
[`state.md`](state.md).

## Scope and ownership

Change the workspace policy and catalog, plus the extension's mandatory-review
skill. The pinned generic runtime already supports these settings and freezes
member instructions and settings; no runtime or roster migration is needed.

| Repository | Intended files |
| --- | --- |
| Workspace | `AGENTS.md`, `config/agent-teams.nix`, `docs/agent-teams.md`, `docs/agent-instructions/{git,verification,sessions}.md`, `test/agent_instructions_test.rb`, catalog checks in `flake.nix` |
| Extension | `skills/mandatory-change-review/SKILL.md`, its `references/{general-review,risk-review}.md`, `test/skill_policy_test.rb` |
| Later package update | Workspace extension input in `flake.nix` and generated `flake.lock`, after extension review and focused checks |

Adapt workspace `04b0e5c682` and extension `dcb2762192` onto current code.
Preserve newer access-failure protections and architect workspace-write access.
Do not replay workspace `3f539b0f6f`: it only installs the obsolete extension pin.

## Role and prompt contract

Keep `AGENTS.md`, routed procedures, site role documentation, and catalog initial
instructions consistent. Catalog prompts must state these obligations directly;
a documentation link alone is insufficient.

- **Lead:** inspect the verified same-session roster for each substantive work
  item; assign by saved purpose and access; coordinate design, implementation,
  review, verification, and deployment. Maintain coordination records and
  integrate member reports. Do not take over application edits, including when
  a delegated member has an access or identity failure. Resolve that failure.
- **Architect:** before substantive implementation, write or update
  `work/<slug>/design.md` with the scope, affected interfaces and files,
  invariants, implementation boundaries, compatibility, deployment and recovery
  implications, acceptance criteria, and quick and longer verification steps.
  Edit assigned design documents and prototypes. Report consequential design
  revisions through the lead; application implementation goes to implementers.
- **Implementer:** follow the assigned architect brief, preserve unrelated
  files, run the assigned quick checks, and report changes, evidence, gaps, and
  deviations. Refer consequential deviations back through the lead before
  changing the design. A small bounded edit may be assigned directly by the
  lead without a separate design document.
- **Reviewer:** independently inspect the committed change using the mandatory
  review workflow and saved settings. Remain read-only. For readiness, assess
  the complete branch history, final diff, and migration provenance, and give
  explicit history and migration conclusions.

At the end of every lead turn, give a compact progress checklist with the current
phase, completed work, remaining work, blockers or material risks, and next
action. Also report material milestones during long turns. Distinguish code
implemented, checked locally, independently reviewed, deployed, and ready for
use. Update the durable phase checklist when its state changes; this does not
change the existing tracking-commit cadence.

Replace the existing permission to keep short or dependent work with the lead
with coordination-only wording. Remove the designer prompt's permission to take
over application implementation. Keep the existing reviewer independence and
Luna verification-watcher rules.

## Catalog and retained members

Set the internal `designer` role to `gpt-6-astra/xhigh`. Keep its `design`
purpose, workspace-write access, and bounded `high` option with a recorded
reason. Lead, implementer, reviewer, and watcher model/effort defaults remain
unchanged. Replace global Sol-only and Astra-forbidden checks with precise
role-based assertions; Astra is an explicit architect default, not a fallback.

Keep `delegated` as the default. Preserve the `lead_designed` preset key for
compatibility, but give newly created instances the same architect, implementer,
and reviewer topology, with `design_owner = "designer"`. Remove the unused
design-owning lead value and update descriptions. The generic portal may still
display its built-in “Lead-designed team” label; document this limitation rather
than expanding this initiative into portal changes.

Keep `solo` for discussion and read-only investigation. Its initial instructions
must require appropriate team setup before substantive development; the lead
must not silently take over implementation. Do not change existing solo rosters.

New sessions and newly added members use the installed catalog. Existing members
retain their saved model, effort, access, and instructions. Creation retries and
forks use their retained snapshots. Do not reconfigure or recreate members to
force this policy onto existing sessions.

## Final branch review

Before a readiness claim, the lead inventories each affected branch's complete
base-to-head commit series and final diff. Identify superseded approaches,
follow-up fixes, unused compatibility paths, and migrations. Establish whether
each migration version was merged, released, deployed, or externally consumed.
Consolidate only obsolete, unapplied branch history; preserve supported paths.

Send that inventory to the dedicated independent reviewer. Earlier incremental
reviews do not complete this gate. Require explicit conclusions about obsolete
history and migration lineage, including “no migrations” when applicable.
Retain the existing adaptive lane and remediation-rerun rules; the final gate
does not require repeated full reviews for every narrow review fix.

## Compatibility and rollout

The baseline is extension `47d9d93cc2373f010a3e6963f76b1cb57bbc1240`, consuming
generic runtime `3b570f0a8b75d809a2753177590158e9dc4639f1`. Preserve its fixes and
runtime selection. After extension review and focused checks, advance the
workspace input to the new extension revision; never replace it with old
`dcb2762192`. Inspect the resulting lock diff for unrelated changes.

While the workspace still selects `47d9d93`, edits in the extension worktree do
not change the installed review skill. Validate the combined candidate using a
temporary extension input override with `--no-write-lock-file`; do not describe
that candidate as deployed. Deploy the reviewed package through the user profile
and verify its generated catalog and packaged skill. Keep prepared and executed
rollout steps distinct in the session state.

There are no database, persisted-format, protocol, CLI, cluster, node, or system
option changes. No coordinated machine update is needed. Package transitions
remain forward-only; recover through a corrected newer package or retry the
same switch, not a promised rollback to an older generation. Deployment does
not authorize integration into default branches.

## Verification and acceptance

Before independent review:

1. Compare instructions and prompts for conflicting ownership, model defaults,
   end-of-turn status, and final-review obligations.
2. Run the workspace `ruby test/agent_instructions_test.rb` and extension
   `ruby test/skill_policy_test.rb` using the repositories' Nix tooling.
3. Evaluate `nix eval --json --file config/agent-teams.nix`. Check architect
   Astra/xhigh and access, unchanged other role defaults, both development
   preset topologies, solo instructions, and watcher isolation.
4. Extend existing policy tests for these consequential invariants, without
   matching entire paragraphs. Keep AGENTS size and procedure routing valid.
5. Commit intended changes and prepare a whole-branch review packet for both
   repositories, including the package baseline and a no-migrations inventory.

After review findings are resolved, use a fresh Luna/low watcher for the affected
workspace Nix checks, extension `nix flake check --print-build-logs`, and combined
candidate packaging. Inspect the generated catalog and packaged skill; a build
against unchanged `47d9d93` alone does not validate the edited extension skill.
No migration VM or development-cluster test is warranted by this policy change.

After deployment, smoke-test a new team: architect settings and initial prompt,
lead checklist, design-to-implementation handoff, and independent full-branch
review assignment. Check retained settings without mutating an existing session.
Record exact revisions, results, and any limitations in `state.md`. These are
planned checks, not verification already performed by this design brief.
