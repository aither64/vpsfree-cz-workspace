# Isolated workspace registration requires the complete schema

In portal creation performance verification, the real Codex seeded all 3,379
private histories, but `workspace-host register bench <private-workspace>`
rejected `.dev-workspace.json` before launching the isolated runtime.

The workspace-host loader checks the complete schema2 key set. The prototype
provided labels, portal identity and cluster providers but omitted `sshHost`.
An empty string is valid for an isolated fixture with no SSH destination.
Keep the normal loader strict and supply `"sshHost": ""` in the fixture.
Validate fixture configuration against the selected package before expensive
history setup; syntax-only checks cannot establish the registration contract.

The failed run retained genuine seeded history and failure metadata outside Git.
A continuation must prove that it failed before registration/runtime creation,
preserve the original failure evidence, and run the unchanged acceptance gates.
Do not reuse partially created sessions, clear journals, write SQLite directly,
or weaken ownership checks to avoid a setup cost.

Related initiative: `work/2026-10-02-portal-creation-performance/`.
