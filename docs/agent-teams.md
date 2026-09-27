# Site team roles

The installed catalog comes from [`config/agent-teams.nix`](../config/agent-teams.nix).
Each role has a compact identifier for member addresses, a purpose for routing,
and instructions for its Codex thread. The `mkRole` helper derives purpose from
behavior; the role identifier can be different. For example, define a security
reviewer in the file's `let` block:

```nix
security = mkRole {
  model = "gpt-6-sol";
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

The site catalog gives architects (`designer` in the catalog) and implementers
workspace-write access. In new development teams, the lead uses GPT-6 Sol,
the architect uses GPT-6 Astra/xhigh, and the implementer and independent
reviewer use GPT-6 Sol. The architect writes the design and verification brief
before substantive implementation and may edit assigned design documents and
prototypes. The implementer makes application edits. The lead coordinates
their work and reports a compact progress checklist at the end of every turn.
Reviewers stay read-only, and a separate GPT-6 Luna/low utility watches long
checks.

`delegated` is the default team. The `lead_designed` key remains available for
compatibility but creates the same architect, implementer, and reviewer roles;
its Sol lead retains xhigh effort. Its name no longer means that the lead owns
design. The generic portal may still display its built-in "Lead-designed team"
label. `solo` is for discussion and read-only investigation. Substantive
development requires a suitable team.

The portal shows each member's saved access, which may differ from the current
catalog. Existing members retain their saved model, effort, access, and
instructions. Newly added members use the installed catalog; creation retries
and forks keep the retained snapshots. Do not reconfigure an existing roster
just to apply new defaults.
