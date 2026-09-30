# Final branch and file inventory

This inventory records the deployment candidates for the mandatory review.
Default-branch integration remains unapproved.

## dev-workspace

Base: `7c133c562ac51076c1f45af46e180f8bfbabe836`. Head: `50586880d5b4e17e060c045dcc992a748f9c7827`.

31 files changed, 3487 insertions(+), 363 deletions(-)

```text
f00a0e5d46f5dd0a4707ab23bbfc3eb4a9db755a team: derive added member settings from role policy
4f500a50360c7507164de41787ed199a1d8c5183 portal: apply live Codex settings as one draft pair
8c250986d560b13df7f09deeceaa7e19008aef9f review: retain loaded editors and add bounded Load all diffs
7ccb6ba350594b69f80675d056b7fa80c496dc67 repository: isolate GitHub origin enrichment
41c648cd92cb324037778be165e45e17c46bbc75 portal: capture immutable staged and unstaged reviews
50af66d9cfc1be07dcc4cb084de4887dd97a343c portal: label repository origin link generically
50586880d5b4e17e060c045dcc992a748f9c7827 test: sample activity before wake dispatch
```

```text
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
M	portal/internal/web/static/repository-review.js
M	portal/internal/web/team_settings_browser_test.cjs
M	portal/internal/web/templates/details.html
M	portal/internal/web/templates/index.html
M	portal/internal/web/templates/session.html
M	test/dev_session/agent_team_creation_test.rb
```

Runtime consumers currently pin production revision `50af66d`; the successor changes only a browser fixture.

## vpsfree-dev-workspace

Base: `6a0a2eb873e7cb376092c74bdf82fc2c51c349da`. Head: `8e04f2626a3abd492768f15ae8d843c8e527f2cd`.

13 files changed, 1236 insertions(+), 49 deletions(-)

```text
1d76d6032b40cd5fb035c26a6b9c94c4aa48e109 devcluster: add optional React Web UI alongside PHP
67bfbbd653694e13e8d5aee53ef0f8e283694bf5 flake: select portal review improvements runtime
e0f98557d688d8561be97d3dc6b1964a0304e383 flake: pin generic repository origin label correction
8e04f2626a3abd492768f15ae8d843c8e527f2cd devcluster: start the React Web UI container on boot
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

Base: `034eb08ea56e75f8a582179b8c13bd9b3109d29e`. Head: `45cce0a87d3f0c8d2b404ce7188d8fa0d9098154`.

8 files changed, 99 insertions(+), 44 deletions(-)

```text
e00505e30c7e1a0e982534a3b8c3afed5152c24c policy: select GPT-6.1 Sol for new team roles
bcba17a00335874eaa8ffe664a279637a0ab01ee vpsadmin: enable the React Web UI in the dev cluster
99e387511cd9d6beac2b9cbb4a7c49306b394ab5 flake: select portal and React Web UI runtime
0e00eab555f9a41136f13cad0f82662f5c2f717b flake: pin Codex 0.159.2 for workspace package
45cce0a87d3f0c8d2b404ce7188d8fa0d9098154 flake: select repository origin label and React boot fix
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

The remote-base series also includes coordination-only tracking commits:

```text
9c887314f6edbddf9f8292c299a594dc6571c3a6 session: plan portal review improvements
034eb08ea56e75f8a582179b8c13bd9b3109d29e session: record portal review design and implementation checkpoint
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
