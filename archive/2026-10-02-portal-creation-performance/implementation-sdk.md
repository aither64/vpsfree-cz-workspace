# SDK implementation result

The bounded codex-web change is ready for parent inspection. No commit,
publication, deployment, long check or session cleanup was performed.

Session identity: `dev-session current` from this tracking directory printed
`2026-10-02-portal-creation-performance`, matching the trusted thread binding.
Both `DEV_SESSION_SLUG` and `DEV_SESSION_WORKSPACE` were absent. The codex-web
worktree was initially clean on the matching feature branch at
`d210d3f7cc93981d0ab163b1fcf0718f9587f47e`.

## Changed files

- `codex/client.go`: adds `ThreadListOptions.UseStateDBOnly bool`; `ListThreads`
  serializes `useStateDbOnly: true` only when requested. False leaves the
  existing request shape unchanged.
- `codex/client_test.go`: adds `TestListThreadsStateDBOnly`, covering omission
  with zero options and filtered false options, true with all existing filters
  and the request cursor, and unchanged response metadata/pagination.
- `test/codex_protocol_contract.py`: requires the selected schema to declare
  `ThreadListParams.useStateDbOnly`; validates both omitted and true params
  and full request envelopes. Keeps the existing call-site corpus count.
- `docs/reference.md`: drafts the owning-project API explanation and records
  that database-only discovery can miss threads or retain stale metadata.
  Parent must apply the user-facing writing skill before committing.

## Evidence and focused checks

Read the workspace AGENTS.md and full projects, sessions, git, lifecycle,
documentation, verification, knowledge-base and commits procedures, plus
codex-web AGENTS.md, README, relevant reference sections and client/protocol
tests. Applied the documentation and handoff skills within this assigned scope;
the lead owns aggregate state, portal registration and commits.

- `git diff --check`: passed.
- `codex --version`: installed package is `codex-cli 0.160.0`.
- Installed executable resolves to
  `/nix/store/53p8l7hck9kca8jcyy6fcpw5iysdfmj6-codex-package-0.160.0/bin/codex`.
- Read the selected source at
  `/nix/store/kdq60x8qayhgkx6d3zbfdgw1i7dqp9q5-source/codex-rs/app-server-protocol/src/protocol/v2/thread.rs:1433`.
  Its camelCase serialization, default boolean and false-omission attribute
  match the SDK change; omitted or false retains scan-and-repair behavior.
- Generated the installed package's experimental schema with
  `codex app-server generate-json-schema --experimental --out DIR` into
  `/tmp/portal-sdk-schema.3kfIeZ`. The generated `v2/ThreadListParams.json`
  declares `useStateDbOnly` with type `boolean` and does not require it.
- `nix develop --offline -c sh -c 'command -v go; command -v python3'`:
  blocked immediately by the member sandbox's denied Nix daemon socket access
  (`Operation not permitted`). Reported to lead; no escalation is available
  under this member's approval policy. No substitute environment was used.

Parent focused commands from the codex-web worktree:

```sh
nix develop -c gofmt -w codex/client.go codex/client_test.go
nix develop -c go test ./codex \
  -run '^(TestListThreadsStateDBOnly|TestProjectIDStartsAndListsOnlyMatchingThreads)$' \
  -count=1 -timeout=30s
nix develop -c python3 test/codex_protocol_contract.py \
  --coverage-only codex/client.go
nix develop -c python3 test/codex_protocol_contract.py \
  /tmp/portal-sdk-schema.3kfIeZ codex/client.go
git diff --check
```

## Compatibility and remaining work

No schema migration, persisted state change, Codex version change, runtime
source change or other SDK semantics change. Existing keyed callers and the
zero option preserve their wire requests. Callers enabling the field must
select a Codex package whose generated protocol schema declares it. Complete
recovery remains the caller's responsibility.

Remaining: parent Nix formatting/focused checks, writing pass, inspection,
commit and independent review. No technical questions or design deviations.
The Nix daemon restriction is the only verification gap.

Suggested commit message:

```text
codex: support database-only thread listing

Expose an optional thread-list flag for callers that need indexed discovery
without scanning JSONL rollouts to repair metadata. Omit the field when false
so existing callers retain their request shape and scan-and-repair behavior.

Require the selected protocol schema to declare the field and document that
callers requiring complete discovery must retain a full-scan recovery path.
```

Session portal:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-portal-creation-performance/>
