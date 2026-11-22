# Workspace profile switch preflight failures

Related initiative:
`work/2026-09-06-portal-config-deployment-policy`.

`workspace-host switch` can fail before profile mutation when any provider
state directory is not a valid slug. A historical vpsAdmin directory named
`clusters/--help`, containing only `config.json`, caused `transition-adopt` to
report an invalid slug. Inspect the directory first, then move an invalid
pseudo-cluster recoverably outside the provider state root and retry. Do not
remove a real cluster merely to satisfy the transition.

The next preflight found that the Codex request corpus counted fewer methods
than the Go client's literal call sites. Package checks had not generated the
live Codex schema, while `workspace-host check-codex` did. Keep one compatible
request sample per counted call-site shape in `test/codex_protocol_contract.py`
and verify it against `codex app-server generate-json-schema --experimental`
before activation.

The final Nix build also exposed a scheduler-sensitive two-second ceiling in a
mocked process-exit race. The production behavior was unchanged; raising the
test-only ceiling to ten seconds passed 20 focused repetitions and the packaged
suite. Both failed switches stopped before changing the active profile or
restarting services.
