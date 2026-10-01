# Final branch and file inventory

Current clean committed repository-review follow-up graph, inspected 2026-10-01.
Default-branch integration and shared-DNS publication remain unapproved.
Generic final verification head is `618df553`; immutable runtime consumers still
select `e64a9fda` through extension `362ebd4` and workspace `aca3b39d`. The
additional standalone commits change only verification fixtures;
source/derivation identity is not claimed equivalent.

## dev-workspace

Base: `7c133c562ac51076c1f45af46e180f8bfbabe836`. Head: `618df5530ba378f8b98f9557cdca700367016c11`.

38 files changed, 3858 insertions(+), 402 deletions(-)

```text
f00a0e5d46f5dd0a4707ab23bbfc3eb4a9db755a team: derive added member settings from role policy
4f500a50360c7507164de41787ed199a1d8c5183 portal: apply live Codex settings as one draft pair
8c250986d560b13df7f09deeceaa7e19008aef9f review: retain loaded editors and add bounded Load all diffs
7ccb6ba350594b69f80675d056b7fa80c496dc67 repository: isolate GitHub origin enrichment
41c648cd92cb324037778be165e45e17c46bbc75 portal: capture immutable staged and unstaged reviews
50af66d9cfc1be07dcc4cb084de4887dd97a343c portal: label repository origin link generically
50586880d5b4e17e060c045dcc992a748f9c7827 test: sample activity before wake dispatch
3445353c9dd297649052fee9b25bbeb541bcddbc repository review: encode empty comparisons as arrays
8019b9b7970d5ae0e57cc530e047979d91632053 repository review: keep repository actions visible
e64a9fda4f5fb3595ce194cc55359ab61f5d8b3a repository review: align overview actions at desktop width
4a1da3c3d1d099a6b0d309b194bd1e343d8d38c1 test: observe failed Keep open write before rollback
618df5530ba378f8b98f9557cdca700367016c11 test: cover retained repository review editors
```

```text
M	README.md
M	docs/workspace-portal.md
M	libexec/dev-session
M	portal/cmd/workspace-portal/main.go
M	portal/cmd/workspace-portal/main_test.go
A	portal/internal/repository/origin.go
A	portal/internal/repository/origin_github.go
A	portal/internal/repository/origin_test.go
M	portal/internal/repository/review.go
A	portal/internal/repository/review_worktree.go
A	portal/internal/repository/review_worktree_test.go
M	portal/internal/repository/status.go
M	portal/internal/session/manifest_test.go
M	portal/internal/teamruntime/runtime.go
M	portal/internal/teamruntime/runtime_test.go
M	portal/internal/web/page_lifecycle_browser_test.cjs
M	portal/internal/web/presentation_browser_test.cjs
M	portal/internal/web/question_browser_test.go
M	portal/internal/web/repository_review.go
M	portal/internal/web/repository_review_browser_test.cjs
A	portal/internal/web/repository_review_live_browser_test.cjs
M	portal/internal/web/repository_review_test.go
A	portal/internal/web/repository_review_worktree.go
A	portal/internal/web/repository_review_worktree_test.go
M	portal/internal/web/server.go
M	portal/internal/web/server_test.go
M	portal/internal/web/static/app.js
M	portal/internal/web/static/repository-review.css
M	portal/internal/web/static/repository-review.js
M	portal/internal/web/static/style.css
M	portal/internal/web/team_settings_browser_test.cjs
M	portal/internal/web/templates/creation.html
M	portal/internal/web/templates/details.html
M	portal/internal/web/templates/index.html
M	portal/internal/web/templates/session.html
M	portal/internal/web/templates/source-file.html
M	test/dev_session/agent_team_creation_test.rb
M	test/repository_browser.cjs
```

## vpsfree-dev-workspace

Base: `6a0a2eb873e7cb376092c74bdf82fc2c51c349da`. Head: `362ebd4759d090805cd95a800e7131edb930b604`.

13 files changed, 1236 insertions(+), 49 deletions(-)

```text
1d76d6032b40cd5fb035c26a6b9c94c4aa48e109 devcluster: add optional React Web UI alongside PHP
67bfbbd653694e13e8d5aee53ef0f8e283694bf5 flake: select portal review improvements runtime
e0f98557d688d8561be97d3dc6b1964a0304e383 flake: pin generic repository origin label correction
8e04f2626a3abd492768f15ae8d843c8e527f2cd devcluster: start the React Web UI container on boot
361be9c712b63e16bda1866c06fb40805c16ce7f flake: select repository review follow-up
362ebd4759d090805cd95a800e7131edb930b604 flake: select repository review action layout fix
```

```text
M	README.md
M	dev-clusters/lib/runtime.sh
M	dev-clusters/vpsadmin/README.md
M	dev-clusters/vpsadmin/bin/devcluster
M	dev-clusters/vpsadmin/flake.nix
M	dev-clusters/vpsadmin/nix/test.nix
A	dev-clusters/vpsadmin/nix/webui-oauth-seed.rb
M	flake.lock
M	flake.nix
M	test/devcluster_commands_test.rb
M	test/devcluster_nix_smoke.rb
M	test/devcluster_status_test.rb
A	test/devcluster_webui_seed_test.rb
```

## workspace

Base: `034eb08ea56e75f8a582179b8c13bd9b3109d29e`. Head: `aca3b39d400b5d1d6d51e42550421f8362684ee0`.

8 files changed, 99 insertions(+), 44 deletions(-)

```text
e00505e30c7e1a0e982534a3b8c3afed5152c24c policy: select GPT-6.1 Sol for new team roles
bcba17a00335874eaa8ffe664a279637a0ab01ee vpsadmin: enable the React Web UI in the dev cluster
99e387511cd9d6beac2b9cbb4a7c49306b394ab5 flake: select portal and React Web UI runtime
0e00eab555f9a41136f13cad0f82662f5c2f717b flake: pin Codex 0.159.2 for workspace package
45cce0a87d3f0c8d2b404ce7188d8fa0d9098154 flake: select repository origin label and React boot fix
9818b805a34394c73c6ee9799f1c268c21c156d4 flake: select repository review follow-up
aca3b39d400b5d1d6d51e42550421f8362684ee0 flake: select repository review action layout
```

```text
M	AGENTS.md
M	config/agent-teams.nix
M	config/vpsadmin-devcluster.json
M	docs/agent-teams.md
M	flake.lock
M	flake.nix
M	test/agent_instructions_test.rb
M	test/deployment_contract_test.rb
```

## vpsfree-cz-configuration

Base: `ee99382c8c448a15347052a6964030f838cb0381`. Head: `d24b251531a9a482b8f1b5dd81540da85981189f`.

1 file changed, 2 insertions(+), 1 deletion(-)

```text
d24b251531a9a482b8f1b5dd81540da85981189f internal-dns: add the development React Web UI alias
```

```text
M	configs/internal-dns/zone.vpsfree.cz.
```

## History and migration disposition

Preserve externally consumed generic 41c648c/50af66d, extension 1d76d603/67bfbbd/e0f98557/8e04f262 and workspace 0e00eab5/45cce0a8 ancestry. The two new generic behavior commits append to test-only 50586880; consumer updates append to the deployed extension/workspace heads. No deployed history was rewritten. Prior abandoned readers, sidecars and unsupported options were removed before consumption, as documented in the preceding independent review.

No database or persisted-format migration is authored by these four feature ranges. The OAuth runtime seed is not a migration. The selected API 5c76e329 advances former packaged 8d0ccafd through nine already-merged upstream migrations: 20260818115900, 20260818120000, 20260821120000, 20260821210000, 20260823100000, 20260909170000, 20260914120000, 20260914180000 and 20260914190000. Their production release/deployment/external-use status is unknown. 20260823100000 supplies the OAuth is_default column/index; selected-schema disposable cluster use is supported, older-API database rollback is unproved. DNS serial publication/correction remains forward-only.

Read-only inputs remain codex-web d210d3f7, API 5c76e329 and WebUI 534caa83. The consumer graph retains approved llm-agents af40d966, bun2nix 07a5bfc8 and nested nixpkgs f45c6f04, preserving packaged Codex 0.159.2.

Ownership note: implementer0 authored generic 3445353c, 8019b9b7 and e64a9fda. The earlier generic publication and 361be9c7/9818b805 pins were observed from a concurrent writer. For the alignment correction, implementer0 authored extension362ebd4 and prepared the workspace two-file source/message; this lead generated the Nix locks, committed workspaceaca3b39d through the writable shared index with normal hooks, and published both consumer feature refs. No profile or cluster change is claimed. All twelve/six/seven/one commits and final diffs are inventoried above; no new migration or abandoned protocol was added by the alignment correction.
