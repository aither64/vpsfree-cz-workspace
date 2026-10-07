# Site team roles

The installed catalog comes from [`config/agent-teams.nix`](../config/agent-teams.nix).
Each role has a compact identifier for member addresses, a purpose for routing,
and instructions for its Codex thread. The `mkRole` helper derives purpose from
behavior; the role identifier can be different. For example, define a security
reviewer in the file's `let` block:

```nix
security = mkRole {
  model = "gpt-6.1-sol";
  effort = "xhigh";
  behavior = "reviewer";
  lifetime = "session";
  fresh_context = true;
  instructions = ''
    Review the assigned change for security flaws and concrete abuse paths.
    Report findings to the lead; do not edit application source.
  '';
};
```

Add `security` to a team's `roles` attribute set to make members such as
`security0` available in that preset. Its saved purpose is `review`, so the
review workflow can select it independently of its role name. Existing session
members keep their saved instructions and settings; a member added later uses
the currently installed catalog.

The site catalog gives leads, architects (`designer` in the catalog) and
implementers workspace-write access. New teams use GPT-6.1 Sol (`gpt-6.1-sol`)
for leads and implementers. The default Lead and reviewer team uses a Sol/xhigh
lead and an Astra/xhigh reviewer; the other presets use Sol reviewers. Architects
use GPT-6 Astra/xhigh. Reviewers stay read-only, and a separate GPT-6 Luna/low
utility watches long checks.

| Preset | Persistent members | Design owner | Application edits | Specialist slots |
| --- | --- | --- | --- | --- |
| `solo` | lead (1 total) | lead | lead | 0 |
| `lead_reviewed` (Lead and reviewer, default) | lead, reviewer (2 total) | lead | lead | 1 |
| `lead_designed` | lead, implementer, reviewer (3 total) | lead | implementer | 2 |
| `delegated` (Full team) | lead, architect, implementer, reviewer (4 total) | architect | implementer | 3 |

Solo leads investigate, design and implement without automatic specialists.
In Lead and reviewer sessions, the lead does the same and uses the retained
reviewer for independent final review. Lead-designed leads write the design
and verification brief before substantive implementation. Full-team architects
write that brief. The brief lives in
`work/<slug>/design.md`; implementers accept either owner's brief. A bounded
small edit may use a direct lead brief. Leads report a compact progress
checklist at the end of every turn and integrate member reports.

Solo and Full-team leads default to high effort and allow high/xhigh;
the lead in Lead-designed and Lead and reviewer sessions defaults to xhigh
and allows high/xhigh. Substantive design and implementation use xhigh, with high
allowed for a bounded simple unit when
the reason is recorded. Independent reviewers retain their saved effort.

Run independent final review after the intended substantive deliverable is
complete, all intended changes are committed and quick checks pass, before
long integration tests. Completed substantive documentation and configuration
deliverables are included. Routine
planning, investigation, findings, session tracking and evidence alone never
trigger automatic review. Earlier review requires an explicit user request,
is advisory, and does not replace final review. A reviewer in a preset receives
no automatic assignment. Solo uses the mandatory-review skill's temporary
standalone reviewer. That reviewer and the utility watcher do not join its
roster. Preserve whole-branch history and migration review and the skill's
narrow-fix policy.

Adding, replacing or reconfiguring members requires explicit user direction;
manual team controls remain available. The portal shows each member's saved
access, which may differ from the current catalog. Existing members retain
their saved model, effort, access, and instructions. Newly added members use
the installed catalog; creation retries and forks keep retained snapshots,
including an older Lead-designed lineup containing an architect. Do not
reconfigure an existing roster to apply new defaults.

Shared workspace rules and installed skills change globally rather than being
frozen with a session. They can conflict with older saved prompts. These defaults
do not refresh those prompts, change existing rosters or add a policy-refresh
mechanism.
