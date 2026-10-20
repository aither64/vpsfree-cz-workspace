# Complete branch and file inventory

Current archive-fixture verification follow-up, 2026-10-01. All four worktrees
are clean at the exact heads below. Generic verification head `869b8d47` adds
only an optional CJS fixture to runtime input `1227f5c2`; consumers retain
`074926d3`/`cd2875f3` and the evaluated ad34/z20 candidate. No source/derivation
identity equivalence is claimed. Review and long checks remain separate gates.

## dev-workspace

Base: `7c133c562ac51076c1f45af46e180f8bfbabe836`. Head: `869b8d4728394127ba949dc76724dce56eae136b`.

Worktree: `worktrees/2026-09-30-portal-review-improvements/dev-workspace`. Status: clean.

16 commits; 41 files changed, 4538 insertions(+), 438 deletions(-).

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
b52ab03284c3a41d441d44394f8e1da2e78d554f repository review: show closed card summaries
6245fe9b2ab12f6d435dfe0bc2f4e8d0ae761e57 repository-review: retain focus on refreshed workflow runs
1227f5c21f4f9a38bbde37c141c2f35f50008554 repository-review: advance script revisions for focus repair
869b8d4728394127ba949dc76724dce56eae136b test: await archive refresh before checking running state
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
M	portal/internal/web/archive_failure_browser_test.cjs
M	portal/internal/web/page_lifecycle_browser_test.cjs
M	portal/internal/web/presentation_browser_test.cjs
M	portal/internal/web/question_browser_test.go
A	portal/internal/web/repository_presentation.go
A	portal/internal/web/repository_presentation_test.go
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

Base: `6a0a2eb873e7cb376092c74bdf82fc2c51c349da`. Head: `074926d33f7306288f7cfad87c6a85e8a430e750`.

Worktree: `worktrees/2026-09-30-portal-review-improvements/vpsfree-dev-workspace`. Status: clean.

8 commits; 13 files changed, 1236 insertions(+), 49 deletions(-).

```text
1d76d6032b40cd5fb035c26a6b9c94c4aa48e109 devcluster: add optional React Web UI alongside PHP
67bfbbd653694e13e8d5aee53ef0f8e283694bf5 flake: select portal review improvements runtime
e0f98557d688d8561be97d3dc6b1964a0304e383 flake: pin generic repository origin label correction
8e04f2626a3abd492768f15ae8d843c8e527f2cd devcluster: start the React Web UI container on boot
361be9c712b63e16bda1866c06fb40805c16ce7f flake: select repository review follow-up
362ebd4759d090805cd95a800e7131edb930b604 flake: select repository review action layout fix
2495d6235da0b352602e9179eb8035beb15a8257 flake: select repository card summaries
074926d33f7306288f7cfad87c6a85e8a430e750 inputs: pin generic repository-review cache update
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

Base: `034eb08ea56e75f8a582179b8c13bd9b3109d29e`. Head: `cd2875f3d4fb2199dd1992b07a3e664eb901e50f`.

Worktree: `worktrees/2026-09-30-portal-review-improvements/workspace`. Status: clean.

9 commits; 8 files changed, 99 insertions(+), 44 deletions(-).

```text
e00505e30c7e1a0e982534a3b8c3afed5152c24c policy: select GPT-6.1 Sol for new team roles
bcba17a00335874eaa8ffe664a279637a0ab01ee vpsadmin: enable the React Web UI in the dev cluster
99e387511cd9d6beac2b9cbb4a7c49306b394ab5 flake: select portal and React Web UI runtime
0e00eab555f9a41136f13cad0f82662f5c2f717b flake: pin Codex 0.159.2 for workspace package
45cce0a87d3f0c8d2b404ce7188d8fa0d9098154 flake: select repository origin label and React boot fix
9818b805a34394c73c6ee9799f1c268c21c156d4 flake: select repository review follow-up
aca3b39d400b5d1d6d51e42550421f8362684ee0 flake: select repository review action layout
4a6d44a2d803d8d804e58400cadd4691715f0bc6 flake: select repository card summaries
cd2875f3d4fb2199dd1992b07a3e664eb901e50f inputs: pin repository-review focus cache update
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

Worktree: `worktrees/2026-09-30-portal-review-improvements/vpsfree-cz-configuration`. Status: clean.

1 commits; 1 file changed, 2 insertions(+), 1 deletion(-).

```text
d24b251531a9a482b8f1b5dd81540da85981189f internal-dns: add the development React Web UI alias
```

```text
M	configs/internal-dns/zone.vpsfree.cz.
```

## History and migration disposition

The new generic correction is published `6245fe9b`, followed by cache successor
`1227f5c2`; its tree equals the checked unpublished amendment `6d797f50`.
The finite non-force push established that `6245` had already been published
while the cache amendment was prepared. Only the unpublished amendment was
rebased onto that exact published parent. No published commit was rewritten;
no force push was used. The unsupported alternative heads remain outside the
final series. Both cache URLs and browser fixtures acquire the corrected source.

The correction's separate extension/workspace successors preserve published
`b52ab032`/`2495d623`, reviewed local `4a6d44a2`, and the previously selected
`e64a9fda`/`362ebd4`/`aca3b39d` ancestry. Assess the complete series and final
source, including the append-only disposition, rather than inferring readiness
from incremental reviews. Earlier abandoned clean-filter discovery, mutable
provenance sidecar, unsupported systemd option and conflicting consolidated
branch iteration are absent from the final series. Workspace coordination-only
commits `9c887314`/`034eb08e` precede its product base and are not product units.

No database or persisted-format migration is authored in any of the four
feature ranges. Runtime OAuth seed is not a migration; DNS serial changes are
forward-only operational protocol state. Selected upstream API `5c76e329`
advances former packaged `8d0ccafd` through nine already-merged migrations:
`20260818115900`, `20260818120000`, `20260821120000`, `20260821210000`,
`20260823100000`, `20260909170000`, `20260914120000`, `20260914180000` and
`20260914190000`. `20260823100000` supplies OAuth is_default/index. Their
production release, deployment and external-use provenance is unknown.
Fresh disposable selected schema is supported; older-API rollback after
migration remains unproved. Require the independent reviewer's explicit history
and migration conclusions.

The selected package remains `bpzvfhdnrj3clw9zfd1qhrhw7fjksyvb`, runtime generic
`e64a9fda` / extension `362ebd4` / workspace `aca3b39d`. The new card UI is not
deployed. The new consumer graph preserves Codex 0.159.2 closure
`af40d966`/`07a5bfc8`/`f45c6f04`, API `5c76e329`, WebUI `534caa83` and
codex-web `d210d3f7`. Shared DNS publication, default integration and session
lifecycle actions remain unapproved.


Archive synchronization follow-up `869b8d47` appends only
`portal/internal/web/archive_failure_browser_test.cjs` to published runtime
`1227f5c2`. It retains all production code, cache and consumer pins. Packaging
excludes this optional fixture from runtime embeds/install. Standalone append
preserves published ancestry; no migrations or persisted-format changes arise.
The source supports an insufficient fixture synchronization point; no private
guard trace or production defect is claimed. Bounded independent review cleared
the exact 16/8/9/1 history with no findings; corrected long verification is pending.

## Final integration inventory (2026-10-01)

Generic869/extension074 remain unchanged. Workspacec3 is the nine-commit equivalent
ofcd287 onto b38992; configuration9824 is the one-commit equivalent ofd24 onto
b6f4e231. Every replayed patch is '=' in range-diff; feature final blobs are
identical. Final target-relative lists and changed paths are recorded in
integration-rebases.json; seven final-head ancestry proofs are recorded in
integration-remote-proofs.json. Independent reviewer0 explicitly cleared coherent
whole-history/migration lineage at these final ranges. User-approved FF-only
integrations and SSH pushes are complete; CI is initial-state reporting only.
