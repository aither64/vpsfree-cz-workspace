# Narrow policy correction and final pin refresh

Continue your independent final review in the same verified thread
01a18222-4859-70c0-80d2-70a784f5cac6, Sol/xhigh. Read-only, no nested agents,
no long tests. Apply mandatory-change-review's affected general/risk lanes and
its whole-branch history/pin conclusion. Retain your completed other lanes.

Full local packaged check and CI 40675068067 failed at runtime 93bc7792 in
TestLeadPolicyBindsSessionWithoutReplacingFrozenRoleInstructions and
TestCoordinationPolicyReleasesVerifiedDeploymentAfterIntegration. Policy text
was appended after the saved role and also altered unbound conversations.
The correction places unchanged communication instructions inside the refreshed
bound-session technical prefix. Existing tests preserve the exact retained
role and unbound behavior; added assertions require communication policy in the
bound prefix. Focused TestLeadPolicy/TestCoordinationPolicy/TestFallbackLead
passed in the Nix shell. Inspect 93bc7792..e9153e61 for the complete code delta.

The correction is consolidated into the core implementation commit; the
separate user-requested UI commit remains. No migrations, releases, deployments
or external consumers of this feature state exist. Runtime origin/master still
4a002f52. Workspace rebased onto shared master abdc82d25, retaining its newly
integrated observer guidance and selecting the same runtime feature. Its pin
conflict was resolved by starting from the current master inputs and regenerating
only the nested runtime input. Extension and siblings stay unchanged.
Configuration deliberately retains reviewed/deployed predecessor base 47155805:
new upstream automated llm-agents, OS, nixpkgs and gems updates are unrelated to
this rollout. Its one generated confctl pin was recreated from that base.

Final ranges:
- dev-workspace: 4a002f52c3b55099540aa99708d5fcf29f7b2456 .. e9153e614e44766d0f0efd6721b34b7bf2f4c14a
  cc106266 core; e9153e61 transcript UI.
- workspace: abdc82d25f893f39d53b9e093a511cc58ad3707a .. 31a3deb3449aa4357bb8ff942e9f30ae948625e0
  6d9da148 guidance; 31a3deb3 single runtime pin.
- configuration: 4715580512a4042bea75cb44167efb42b3618f70 .. b4b0c17b11a873bc0b864cb8a6e91345d76653a3
  b4b0c17b single generated confctl pin.

All worktrees are under worktrees/2026-10-28-cross-session-messaging. Intended
changes are committed. Quick policy checks, whitespace checks and final composed
deployment contract passed; configuration hooks passed. Both final locks select
e9153e61 with sha256-fyuH/vpnLQML2mnAnrlG5LdxZsJJ2FbFbNhlKOFYO00=.
No default-branch integration is authorized. Confirm code correction, complete
final history/consolidation, no migrations and changed baseline preservation.
Report any findings and residual check gaps; do not claim deployment readiness.
