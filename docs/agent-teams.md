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
